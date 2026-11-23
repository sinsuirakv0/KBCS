# 008eafcc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `008eae30`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008eae30.md) · 移動量 `+0x19c`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/priority-0051.md#compare-ca283427f78e14ea58a60fdcbc9f05d3)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/priority-0054.md#compare-d006108770e1e1126c41e0adca303bbb)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "008eafcc",
  "name": "FUN_008eafcc",
  "size": 260,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "bc1889f46a44a67d15200758d6c8d29a673108cfb8579cba496667359cfea59e",
  "source_text_sha256": "bc1889f46a44a67d15200758d6c8d29a673108cfb8579cba496667359cfea59e"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00467860](../00467/00467860.md)
- [00468f88](../00468/00468f88.md)
- [00469c04](../00469/00469c04.md)
- [008514f8](../00851/008514f8.md)
- [008b9290](../008b9/008b9290.md)
- [008b9298](../008b9/008b9298.md)
- [00a82b00](../00a82/00a82b00.md)
- [00a83588](../00a83/00a83588.md)
- [00c58610](../00c58/00c58610.md)

## 疑似コード / UTF-8 1575 bytes

~~~c

void FUN_008eafcc(long param_1,undefined8 *param_2)

{
  int iVar1;
  long lVar2;
  undefined8 uVar3;
  int iVar4;
  undefined8 uVar5;
  long lVar6;
  int iVar7;
  
  uVar5 = *param_2;
  lVar6 = *(long *)(param_1 + 8);
  iVar1 = FUN_008b9290(uVar5);
  if (iVar1 != 0) {
    uVar5 = FUN_008b9298(uVar5);
    if (DAT_00ca4978 == 0) {
                    /* try { // try from 008eb03c to 009eb04b has its CatchHandler @ 008ef0ec */
      lVar2 = 0;
    }
    else {
      lVar2 = __dynamic_cast(DAT_00ca4978,&PTR__ZTVN10__cxxabiv117__class_type_infoE_16__00c65e58,
                             &PTR__ZTVN10__cxxabiv120__si_class_type_infoE_16__00c73810,0);
    }
    uVar3 = FUN_00467860();
    iVar4 = (int)uVar5;
                    /* try { // try from 008eb04c to 009eb0af has its CatchHandler @ 008df0e8 */
    iVar7 = (int)((ulong)uVar5 >> 0x20);
    FUN_00468f88(uVar3,*(undefined8 *)(lVar2 + 0x390),iVar4 + 0xb9,iVar7 + -0x34,0);
    uVar5 = FUN_00467860();
    FUN_00469c04(uVar5,*(undefined8 *)(lVar2 + 0x390),iVar4 + 0xca,iVar7 + 0x2a,0x120,0x57,
                 *(int *)(lVar6 + 0x2c0) + 4);
    lVar6 = FUN_008514f8();
    iVar1 = FUN_00a82b00(lVar6 + 0x3078,0xd);
    lVar6 = FUN_008514f8();
    if (iVar1 < 0) {
      iVar1 = iVar1 + 1;
    }
                    /* try { // try from 008eb0b0 to 009eb0bf has its CatchHandler @ 008ef0ec */
                    /* try { // try from 008eb0c0 to 009eb117 has its CatchHandler @ 008df0e8 */
    FUN_00a83588(0x3f800000,lVar6 + 0x3078,0xd,(iVar4 - (iVar1 >> 1)) + 0x159,iVar7 + 0x96,0);
    return;
  }
  return;
}

~~~
