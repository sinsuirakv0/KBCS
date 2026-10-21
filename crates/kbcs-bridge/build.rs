fn main() {
    cc::Build::new()
        .cpp(true)
        .std("c++20")
        .include("../../native/kbcs-core/include")
        .file("../../native/kbcs-core/src/core.cpp")
        .file("../../native/kbcs-core/src/stage.cpp")
        .file("../../native/kbcs-core/src/materials.cpp")
        .compile("kbcs-core");
    println!("cargo:rerun-if-changed=../../native/kbcs-core");
}
