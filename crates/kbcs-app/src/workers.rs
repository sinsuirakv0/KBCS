use std::sync::{
    Arc, Mutex,
    atomic::{AtomicUsize, Ordering},
    mpsc::{SyncSender, TrySendError, sync_channel},
};

type Job = Box<dyn FnOnce(bool) + Send>;
struct Pool {
    sender: SyncSender<Job>,
    active: Arc<AtomicUsize>,
    queued: Arc<AtomicUsize>,
    rejected: AtomicUsize,
    workers: usize,
}
impl Pool {
    fn new(workers: usize, name: &str) -> Self {
        let (sender, receiver) = sync_channel::<Job>(64);
        let receiver = Arc::new(Mutex::new(receiver));
        let active = Arc::new(AtomicUsize::new(0));
        let queued = Arc::new(AtomicUsize::new(0));
        for index in 0..workers {
            let (receiver, active, queued) = (receiver.clone(), active.clone(), queued.clone());
            std::thread::Builder::new()
                .name(format!("kbcs-{name}-{index}"))
                .spawn(move || {
                    loop {
                        let job = receiver.lock().unwrap().recv();
                        let Ok(job) = job else { break };
                        queued.fetch_sub(1, Ordering::Relaxed);
                        active.fetch_add(1, Ordering::Relaxed);
                        // 1要求のパニックでプール全体を失わない。
                        let _ =
                            std::panic::catch_unwind(std::panic::AssertUnwindSafe(|| job(true)));
                        active.fetch_sub(1, Ordering::Relaxed);
                    }
                })
                .expect("要求ワーカーを作成できません");
        }
        Self {
            sender,
            active,
            queued,
            rejected: AtomicUsize::new(0),
            workers,
        }
    }
    fn submit(&self, job: Job) {
        self.queued.fetch_add(1, Ordering::Relaxed);
        if let Err(TrySendError::Full(job) | TrySendError::Disconnected(job)) =
            self.sender.try_send(job)
        {
            self.queued.fetch_sub(1, Ordering::Relaxed);
            self.rejected.fetch_add(1, Ordering::Relaxed);
            job(false);
        }
    }
    fn summary(&self) -> serde_json::Value {
        serde_json::json!({"workers":self.workers,"active":self.active.load(Ordering::Relaxed),"queued":self.queued.load(Ordering::Relaxed),"rejected":self.rejected.load(Ordering::Relaxed)})
    }
}
pub struct Workers {
    ui: Pool,
    compute: Pool,
    io: Pool,
}
impl Workers {
    pub fn new() -> Self {
        let cores = std::thread::available_parallelism().map_or(2, usize::from);
        Self {
            ui: Pool::new(2, "ui"),
            compute: Pool::new(cores.clamp(2, 6), "compute"),
            io: Pool::new(2, "io"),
        }
    }
    pub fn submit(&self, path: &str, job: impl FnOnce(bool) + Send + 'static) {
        let pool = if path.starts_with("/api/stage-audio/") || path.starts_with("/api/import") {
            &self.io
        } else if [
            "/api/stage-scene",
            "/api/battle-frame",
            "/api/battle-session",
            "/api/motion",
            "/api/catalog",
            "/api/stages",
            "/api/enemies",
            "/api/calculate",
        ]
        .iter()
        .any(|prefix| path.starts_with(prefix))
        {
            &self.compute
        } else {
            &self.ui
        };
        pool.submit(Box::new(job));
    }
    pub fn summary(&self) -> serde_json::Value {
        serde_json::json!({"ui":self.ui.summary(),"compute":self.compute.summary(),"io":self.io.summary()})
    }
}

#[test]
fn bounds_workers_and_queue_without_blocking_submitter() {
    let pool = Pool::new(2, "test");
    let gate = Arc::new((Mutex::new(false), std::sync::Condvar::new()));
    let (started, wait_started) = std::sync::mpsc::channel();
    for _ in 0..2 {
        let (gate, started) = (gate.clone(), started.clone());
        pool.submit(Box::new(move |accepted| {
            assert!(accepted);
            started.send(()).unwrap();
            let (lock, wake) = &*gate;
            let mut ready = lock.lock().unwrap();
            while !*ready {
                ready = wake.wait(ready).unwrap();
            }
        }));
    }
    for _ in 0..2 {
        wait_started
            .recv_timeout(std::time::Duration::from_secs(3))
            .unwrap();
    }
    for _ in 0..64 {
        pool.submit(Box::new(|accepted| assert!(accepted)));
    }
    let rejected = Arc::new(AtomicUsize::new(0));
    let count = rejected.clone();
    pool.submit(Box::new(move |accepted| {
        if !accepted {
            count.fetch_add(1, Ordering::Relaxed);
        }
    }));
    // 失敗しても待機中のワーカーを確実に解放する。
    *gate.0.lock().unwrap() = true;
    gate.1.notify_all();
    assert_eq!(rejected.load(Ordering::Relaxed), 1);
    assert_eq!(pool.workers, 2);
}
