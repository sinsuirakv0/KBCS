# 00afb5bc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00afb194`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afb/00afb194.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/alignment_unresolved-0006.md#compare-9f2e7735b7e196c2d14eb4fc16d3d37a)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/priority-0072.md#compare-91cedfab9d429fc2533c33a00ec7dde8)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afb5bc",
  "name": "FUN_00afb5bc",
  "size": 408,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2305d76a39a8c579edceddec0441b6d5c0e27ceadaa8ed17e74434a3df24dbbc",
  "source_text_sha256": "2305d76a39a8c579edceddec0441b6d5c0e27ceadaa8ed17e74434a3df24dbbc"
}
~~~

## 呼び出し元

- [005f3a70](../005f3/005f3a70.md)
- [005fb93c](../005fb/005fb93c.md)
- [00700af8](../00700/00700af8.md)
- [0070ea5c](../0070e/0070ea5c.md)
- [007119f0](../00711/007119f0.md)
- [00716d90](../00716/00716d90.md)

## 呼び出し先

- [005e0300](../005e0/005e0300.md)
- [005e08d8](../005e0/005e08d8.md)
- [005e0920](../005e0/005e0920.md)
- [005e09a0](../005e0/005e09a0.md)
- [008514f8](../00851/008514f8.md)

## 疑似コード / UTF-8 2194 bytes

~~~c

void FUN_00afb5bc(int param_1,int param_2,int param_3)

{
  int iVar1;
  ulong uVar2;
  long lVar3;
  
  if (param_1 == 1) {
    uVar2 = FUN_005e08d8();
    if ((uVar2 & 1) == 0) {
                    /* try { // try from 00afb604 to 00bfb60f has its CatchHandler @ 00afc974 */
      if (param_2 != 0) goto LAB_00afb638;
    }
    else {
      iVar1 = FUN_005e0920();
      if (iVar1 != param_2) goto LAB_00afb638;
    }
    uVar2 = FUN_005e09a0();
    if ((uVar2 & 1) != 0) {
                    /* try { // try from 00afb614 to 00bfb62b has its CatchHandler @ 00afc970 */
      lVar3 = FUN_008514f8();
                    /* try { // try from 00afb62c to 00bfb68f has its CatchHandler @ 00afb44c */
      FUN_005e0300(lVar3 + 0x980,1);
      return;
    }
  }
LAB_00afb638:
  lVar3 = FUN_008514f8();
  lVar3 = lVar3 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec;
  *(int *)(lVar3 + 0x84914) = *(int *)(lVar3 + 0x84914) + param_3;
  lVar3 = FUN_008514f8();
  lVar3 = lVar3 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec;
  *(int *)(lVar3 + 0x84a88) = *(int *)(lVar3 + 0x84a88) + param_3;
  lVar3 = FUN_008514f8();
                    /* try { // try from 00afb690 to 00bfb69b has its CatchHandler @ 00afcb50 */
                    /* try { // try from 00afb69c to 00bfb6af has its CatchHandler @ 00afcb30 */
                    /* try { // try from 00afb6c8 to 00bfb6d7 has its CatchHandler @ 00afcb10 */
                    /* try { // try from 00afb6f0 to 00bfb707 has its CatchHandler @ 00afcad4 */
  if (((0 < *(int *)(lVar3 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84ad0)) &&
      (lVar3 = FUN_008514f8(),
      *(int *)(lVar3 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84ad0) < param_3)) &&
     (lVar3 = FUN_008514f8(),
     *(int *)(lVar3 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84ad4) == 0)) {
    lVar3 = FUN_008514f8();
                    /* try { // try from 00afb708 to 00bfb75f has its CatchHandler @ 00afb44c */
    *(undefined4 *)(lVar3 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84ad4) = 1;
  }
  lVar3 = FUN_008514f8();
  *(undefined4 *)(lVar3 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84b50) = 1;
  return;
}

~~~
