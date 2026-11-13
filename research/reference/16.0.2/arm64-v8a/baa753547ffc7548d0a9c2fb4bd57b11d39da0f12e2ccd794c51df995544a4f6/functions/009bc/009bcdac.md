# 009bcdac

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "009bcdac",
  "name": "FUN_009bcdac",
  "size": 296,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "056c3d04bc0d0f52a5924e73b5800a0c339218e58738987e970362d85d20e723",
  "source_text_sha256": "056c3d04bc0d0f52a5924e73b5800a0c339218e58738987e970362d85d20e723"
}
~~~

## 呼び出し元

- [009bdb8c](../009bd/009bdb8c.md)
- [009bdcd4](../009bd/009bdcd4.md)

## 呼び出し先

- [00c53da0](../00c53/00c53da0.md)
- [00c57f50](../00c57/00c57f50.md)

## 疑似コード / UTF-8 1708 bytes

~~~c

void FUN_009bcdac(undefined8 *param_1)

{
  long lVar1;
  long *plVar2;
  
  plVar2 = (long *)param_1[1];
  *param_1 = 0;
  param_1[1] = 0;
  if ((plVar2 != (long *)0x0) && (lVar1 = FUN_00c53da0(0xffffffffffffffff,plVar2 + 1), lVar1 == 0))
  {
    (**(code **)(*plVar2 + 0x10))(plVar2);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar2);
  }
  plVar2 = (long *)param_1[3];
  param_1[2] = 0;
  param_1[3] = 0;
  if ((plVar2 != (long *)0x0) && (lVar1 = FUN_00c53da0(0xffffffffffffffff,plVar2 + 1), lVar1 == 0))
  {
    (**(code **)(*plVar2 + 0x10))(plVar2);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar2);
  }
  plVar2 = (long *)param_1[5];
  param_1[4] = 0;
  param_1[5] = 0;
  if ((plVar2 != (long *)0x0) && (lVar1 = FUN_00c53da0(0xffffffffffffffff,plVar2 + 1), lVar1 == 0))
  {
    (**(code **)(*plVar2 + 0x10))(plVar2);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar2);
  }
  plVar2 = (long *)param_1[7];
  param_1[6] = 0;
  param_1[7] = 0;
  if ((plVar2 != (long *)0x0) && (lVar1 = FUN_00c53da0(0xffffffffffffffff,plVar2 + 1), lVar1 == 0))
  {
                    /* try { // try from 009bce7c to 00abce93 has its CatchHandler @ 009bdacc */
    (**(code **)(*plVar2 + 0x10))(plVar2);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar2);
  }
  plVar2 = (long *)param_1[9];
  param_1[8] = 0;
  param_1[9] = 0;
                    /* try { // try from 009bce94 to 00abcf8f has its CatchHandler @ 009bc920 */
  if ((plVar2 != (long *)0x0) && (lVar1 = FUN_00c53da0(0xffffffffffffffff,plVar2 + 1), lVar1 == 0))
  {
    (**(code **)(*plVar2 + 0x10))(plVar2);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar2);
    return;
  }
  return;
}

~~~
