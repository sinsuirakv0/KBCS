use serde_json::{Value, json};
use std::time::Instant;

#[derive(Default)]
pub struct Monitor {
    previous: Option<(Instant, u64, u64)>,
    cached: Option<Value>,
}
impl Monitor {
    pub fn sample(&mut self) -> Value {
        if self
            .previous
            .is_some_and(|(at, _, _)| at.elapsed().as_millis() < 750)
        {
            return self.cached.clone().unwrap_or(Value::Null);
        }
        let mut result = json!({"cpuPercent":null,"memoryTotal":null,"memoryAvailable":null,"hostWorkingSet":null,"logicalProcessors":std::thread::available_parallelism().map_or(1,usize::from)});
        #[cfg(windows)]
        unsafe {
            use windows_sys::Win32::{
                Foundation::FILETIME,
                System::{
                    ProcessStatus::{K32GetProcessMemoryInfo, PROCESS_MEMORY_COUNTERS},
                    SystemInformation::{GlobalMemoryStatusEx, MEMORYSTATUSEX},
                    Threading::{GetCurrentProcess, GetSystemTimes},
                },
            };
            let (mut idle, mut kernel, mut user) = (
                FILETIME::default(),
                FILETIME::default(),
                FILETIME::default(),
            );
            if GetSystemTimes(&mut idle, &mut kernel, &mut user) != 0 {
                let ticks =
                    |v: FILETIME| (u64::from(v.dwHighDateTime) << 32) | u64::from(v.dwLowDateTime);
                let (idle, total) = (ticks(idle), ticks(kernel) + ticks(user));
                if let Some((_, old_idle, old_total)) = self.previous {
                    let elapsed = total.saturating_sub(old_total);
                    if elapsed > 0 {
                        result["cpuPercent"] = json!(
                            (100. * (1. - idle.saturating_sub(old_idle) as f64 / elapsed as f64))
                                .clamp(0., 100.)
                        );
                    }
                }
                self.previous = Some((Instant::now(), idle, total));
            }
            let mut memory = MEMORYSTATUSEX {
                dwLength: std::mem::size_of::<MEMORYSTATUSEX>() as u32,
                ..Default::default()
            };
            if GlobalMemoryStatusEx(&mut memory) != 0 {
                result["memoryTotal"] = json!(memory.ullTotalPhys);
                result["memoryAvailable"] = json!(memory.ullAvailPhys);
            }
            let mut process = PROCESS_MEMORY_COUNTERS {
                cb: std::mem::size_of::<PROCESS_MEMORY_COUNTERS>() as u32,
                ..Default::default()
            };
            if K32GetProcessMemoryInfo(GetCurrentProcess(), &mut process, process.cb) != 0 {
                result["hostWorkingSet"] = json!(process.WorkingSetSize);
            }
        }
        self.cached = Some(result.clone());
        result
    }
}
