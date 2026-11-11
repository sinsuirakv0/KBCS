# 00bfad7c

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00bfad7c",
  "name": "_ZNSt6__ndk113random_deviceclEv",
  "size": 148,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8f55d05815ca45746b9f4cdbcbc5f6056326da19f6aedac0478140bd7c8dadfc",
  "source_text_sha256": "8f55d05815ca45746b9f4cdbcbc5f6056326da19f6aedac0478140bd7c8dadfc"
}
~~~

## 呼び出し元

- [00c583b0](../00c58/00c583b0.md)

## 呼び出し先

- [00c580c0](../00c58/00c580c0.md)
- [00c58120](../00c58/00c58120.md)
- [00c5d650](../00c5d/00c5d650.md)

## 関連文字列（未確認候補）

~~~text
"random_device got EOF"
"random_device got an unexpected error"
~~~

## 疑似コード / UTF-8 861 bytes

~~~c

undefined4 _ZNSt6__ndk113random_deviceclEv(int *param_1)

{
  int *piVar1;
  ssize_t sVar2;
  undefined4 *__buf;
  size_t __nbytes;
  undefined4 local_14;
  
  __buf = &local_14;
  __nbytes = 4;
  do {
    while (sVar2 = read(*param_1,__buf,__nbytes), sVar2 != -1) {
      if (sVar2 == 0) {
                    /* WARNING: Subroutine does not return */
        _ZNSt6__ndk120__throw_system_errorEiPKc(0x3d,"random_device got EOF");
      }
      __nbytes = __nbytes - sVar2;
      __buf = (undefined4 *)((long)__buf + sVar2);
      if (__nbytes == 0) {
        return local_14;
      }
    }
    piVar1 = (int *)__errno();
    if (*piVar1 != 4) {
                    /* WARNING: Subroutine does not return */
      _ZNSt6__ndk120__throw_system_errorEiPKc(*piVar1,"random_device got an unexpected error");
    }
  } while (__nbytes != 0);
  return local_14;
}

~~~
