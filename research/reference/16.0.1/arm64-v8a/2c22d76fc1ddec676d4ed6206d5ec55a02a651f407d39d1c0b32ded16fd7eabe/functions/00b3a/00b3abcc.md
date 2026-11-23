# 00b3abcc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b3a7a4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3a/00b3a7a4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/priority-0069.md#compare-fbb302573bbdec938e37f1c92ed7f7e6)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/priority-0075.md#compare-39c7d1e21ff23dc1a78d583e76449d77)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b3abcc",
  "name": "Java_jp_co_ponos_battlecats_TapjoyImplementation_onTapjoyPlacementRequestFailure",
  "size": 200,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "49780c986b547de2dd3e6bdeade6deedd6f1d3bc8b1400db1d23771aec54fbc0",
  "source_text_sha256": "49780c986b547de2dd3e6bdeade6deedd6f1d3bc8b1400db1d23771aec54fbc0"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00589954](../00589/00589954.md)
- [00b3b820](../00b3b/00b3b820.md)
- [00c57eb0](../00c57/00c57eb0.md)
- [00c57ee0](../00c57/00c57ee0.md)

## 疑似コード / UTF-8 1041 bytes

~~~c

void Java_jp_co_ponos_battlecats_TapjoyImplementation_onTapjoyPlacementRequestFailure
               (undefined8 param_1,undefined8 param_2,undefined8 param_3)

{
  long lVar1;
  undefined8 *puVar2;
  long *plVar3;
  byte local_68 [16];
  void *local_58;
  byte local_50 [16];
  void *local_40;
  long local_38;
  
  lVar1 = tpidr_el0;
  local_38 = *(long *)(lVar1 + 0x28);
  FUN_00589954(local_50,param_1,param_3);
  FUN_00589954(local_68,param_1,param_3);
  puVar2 = (undefined8 *)FUN_00b3b820(&DAT_011251f8,local_50);
  if ((puVar2 != &DAT_01125200) && (plVar3 = (long *)puVar2[0x12], plVar3 != (long *)0x0)) {
    (**(code **)(*plVar3 + 0x30))(plVar3,local_50,local_68);
  }
  if ((local_68[0] & 1) != 0) {
    _ZdlPv(local_58);
  }
  if ((local_50[0] & 1) != 0) {
    _ZdlPv(local_40);
  }
  if (*(long *)(lVar1 + 0x28) == local_38) {
                    /* try { // try from 00b3ac84 to 00c3ac87 has its CatchHandler @ 00b3b080 */
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
