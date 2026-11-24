# 00c0eabc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00c0ea20`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0e/00c0ea20.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/priority-0087.md#compare-eceaa09ff306fe76365f35b9ec765452)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/priority-0100.md#compare-e41211d49bc4ea3222260ea14ed20986)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00c0eabc",
  "name": "_ZNSt6__ndk19__num_getIwE17__stage2_int_prepERNS_8ios_baseEPwRw",
  "size": 360,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b153d2f8b5ecb282f9b0ac4293618f3584dbb0d65815fa0f86572aacf2dc232b",
  "source_text_sha256": "b153d2f8b5ecb282f9b0ac4293618f3584dbb0d65815fa0f86572aacf2dc232b"
}
~~~

## 呼び出し元

- [00c5e660](../00c5e/00c5e660.md)

## 呼び出し先

- [00c05ff4](../00c05/00c05ff4.md)
- [00c58340](../00c58/00c58340.md)
- [00c58360](../00c58/00c58360.md)
- [00c5dfb0](../00c5d/00c5dfb0.md)

## 関連文字列（未確認候補）

~~~text
"0123456789abcdefABCDEFxX+-pPiInN"
~~~

## 疑似コード / UTF-8 3115 bytes

~~~c

void _ZNSt6__ndk19__num_getIwE17__stage2_int_prepERNS_8ios_baseEPwRw
               (undefined8 param_1,undefined8 param_2,undefined8 param_3,undefined4 *param_4)

{
  long lVar1;
  undefined *puVar2;
  long lVar3;
  undefined4 uVar4;
  long *plVar5;
  long local_58;
  undefined *local_50;
  undefined8 **local_48;
  undefined **local_28;
  
                    /* catch() { ... } // from try @ 00c0ea34 with catch @ 00c0eac8 */
                    /* catch() { ... } // from try @ 00c0ea64 with catch @ 00c0ead0 */
                    /* catch() { ... } // from try @ 00c0ea78 with catch @ 00c0ead8 */
  _ZNKSt6__ndk18ios_base6getlocEv(&local_58);
  lVar3 = local_58;
  puVar2 = PTR__ZNSt6__ndk15ctypeIwE2idE_00c9bc10;
  local_50 = PTR__ZNSt6__ndk15ctypeIwE2idE_00c9bc10;
  if (*(long *)PTR__ZNSt6__ndk15ctypeIwE2idE_00c9bc10 != -1) {
    local_28 = &local_50;
    local_48 = &local_28;
                    /* try { // try from 00c0eb18 to 00d0eb93 has its CatchHandler @ 00c0eb18
                       catch() { ... } // from try @ 00c0eb18 with catch @ 00c0eb18
                       catch() { ... } // from try @ 00c0ebe0 with catch @ 00c0eb18
                       catch() { ... } // from try @ 00c0ecd0 with catch @ 00c0eb18 */
    _ZNSt6__ndk111__call_onceERVmPvPFvS2_E
              (PTR__ZNSt6__ndk15ctypeIwE2idE_00c9bc10,&local_48,FUN_00c36054);
  }
  lVar1 = *(long *)(lVar3 + 0x10);
  if (((ulong)(*(long *)(lVar3 + 0x18) - lVar1 >> 3) <= (long)*(int *)(puVar2 + 8) - 1U) ||
     (plVar5 = *(long **)(lVar1 + ((long)*(int *)(puVar2 + 8) - 1U) * 8), plVar5 == (long *)0x0)) {
                    /* WARNING: Subroutine does not return */
    FUN_00c05ff4();
  }
  (**(code **)(*plVar5 + 0x60))
            (plVar5,PTR__ZNSt6__ndk114__num_get_base5__srcE_00c9bc90,
             PTR__ZNSt6__ndk114__num_get_base5__srcE_00c9bc90 + 0x1a,param_3);
  puVar2 = PTR__ZNSt6__ndk18numpunctIwE2idE_00c9bc98;
  local_50 = PTR__ZNSt6__ndk18numpunctIwE2idE_00c9bc98;
  if (*(long *)PTR__ZNSt6__ndk18numpunctIwE2idE_00c9bc98 != -1) {
    local_28 = &local_50;
    local_48 = &local_28;
                    /* try { // try from 00c0eb94 to 00d0eb9b has its CatchHandler @ 00c0edf0 */
    _ZNSt6__ndk111__call_onceERVmPvPFvS2_E
              (PTR__ZNSt6__ndk18numpunctIwE2idE_00c9bc98,&local_48,FUN_00c36054);
  }
                    /* try { // try from 00c0ebc8 to 00d0ebcf has its CatchHandler @ 00c0eddc */
  if (((long)*(int *)(puVar2 + 8) - 1U <
       (ulong)(*(long *)(local_58 + 0x18) - *(long *)(local_58 + 0x10) >> 3)) &&
     (plVar5 = *(long **)(*(long *)(local_58 + 0x10) + ((long)*(int *)(puVar2 + 8) - 1U) * 8),
     plVar5 != (long *)0x0)) {
                    /* try { // try from 00c0ebd4 to 00d0ebdf has its CatchHandler @ 00c0edf8 */
    uVar4 = (**(code **)(*plVar5 + 0x20))(plVar5);
                    /* try { // try from 00c0ebe0 to 00d0ec37 has its CatchHandler @ 00c0eb18 */
    *param_4 = uVar4;
    (**(code **)(*plVar5 + 0x28))(param_1,plVar5);
    _ZNSt6__ndk16localeD1Ev(&local_58);
    return;
  }
                    /* WARNING: Subroutine does not return */
  FUN_00c05ff4();
}

~~~
