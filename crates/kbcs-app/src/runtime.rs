use serde_json::{Value, json};
use std::time::Instant;

pub fn system() -> Value {
    let mut value = json!({"os":std::env::consts::OS,"architecture":std::env::consts::ARCH,"processId":std::process::id(),"logicalProcessors":std::thread::available_parallelism().map_or(1,usize::from),"cpu":std::env::var("PROCESSOR_IDENTIFIER").ok()});
    #[cfg(windows)]
    unsafe {
        #[link(name = "ntdll")]
        unsafe extern "system" {
            fn RtlGetVersion(info: *mut u32) -> i32;
        }
        let mut info = [0u32; 69];
        info[0] = std::mem::size_of_val(&info) as u32;
        if RtlGetVersion(info.as_mut_ptr()) == 0 {
            value["osVersion"] = json!(format!("{}.{}.{}", info[1], info[2], info[3]));
        }
    }
    #[cfg(target_os = "macos")]
    unsafe {
        for (key, name) in [
            ("osVersion", c"kern.osproductversion"),
            ("model", c"hw.model"),
            ("cpu", c"machdep.cpu.brand_string"),
        ] {
            let mut bytes = [0u8; 512];
            let mut length = bytes.len();
            if libc::sysctlbyname(
                name.as_ptr(),
                bytes.as_mut_ptr().cast(),
                &mut length,
                std::ptr::null_mut(),
                0,
            ) == 0
            {
                value[key] = json!(
                    String::from_utf8_lossy(&bytes[..length.min(bytes.len())])
                        .trim_end_matches('\0')
                );
            }
        }
    }
    value
}

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
        #[cfg(target_os = "macos")]
        unsafe {
            let host = mach2::mach_init::mach_host_self();
            let mut cpu: libc::host_cpu_load_info = std::mem::zeroed();
            let mut count = libc::HOST_CPU_LOAD_INFO_COUNT;
            if libc::host_statistics(
                host,
                libc::HOST_CPU_LOAD_INFO,
                (&mut cpu as *mut libc::host_cpu_load_info).cast(),
                &mut count,
            ) == libc::KERN_SUCCESS
            {
                let idle = u64::from(cpu.cpu_ticks[libc::CPU_STATE_IDLE as usize]);
                let total = cpu
                    .cpu_ticks
                    .iter()
                    .map(|&ticks| u64::from(ticks))
                    .sum::<u64>();
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
            let mut memory: libc::vm_statistics64 = std::mem::zeroed();
            let mut count = libc::HOST_VM_INFO64_COUNT;
            let page_size = libc::sysconf(libc::_SC_PAGESIZE);
            if page_size > 0
                && libc::host_statistics64(
                    host,
                    libc::HOST_VM_INFO64,
                    (&mut memory as *mut libc::vm_statistics64).cast(),
                    &mut count,
                ) == libc::KERN_SUCCESS
            {
                // macOSの空き容量は、空きページと再利用可能な非活性ページの概算。
                result["memoryAvailable"] = json!(
                    (u64::from(memory.free_count) + u64::from(memory.inactive_count))
                        * page_size as u64
                );
            }
            mach2::mach_port::mach_port_deallocate(mach2::traps::mach_task_self(), host);
            let mut total = 0u64;
            let mut length = std::mem::size_of_val(&total);
            if libc::sysctlbyname(
                c"hw.memsize".as_ptr(),
                (&mut total as *mut u64).cast(),
                &mut length,
                std::ptr::null_mut(),
                0,
            ) == 0
            {
                result["memoryTotal"] = json!(total);
            }
            let mut process: libc::proc_taskinfo = std::mem::zeroed();
            let length = std::mem::size_of_val(&process) as i32;
            if libc::proc_pidinfo(
                std::process::id() as i32,
                libc::PROC_PIDTASKINFO,
                0,
                (&mut process as *mut libc::proc_taskinfo).cast(),
                length,
            ) == length
            {
                result["hostWorkingSet"] = json!(process.pti_resident_size);
            }
        }
        self.cached = Some(result.clone());
        result
    }
}
