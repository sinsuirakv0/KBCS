# 009bcdac

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `009bcd58`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009bc/009bcd58.md) · 移動量 `+0x54`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/inspection-0031.md#compare-fd87fe52524d7cc58358e6254313c31f)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/inspection-0025.md#compare-e67e34b06fe85f655211e4b00674eafb)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

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
