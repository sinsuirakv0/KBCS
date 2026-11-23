# 00aff2cc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00afeea4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afe/00afeea4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/priority-0066.md#compare-a4d620983c1b7bba5dfb5fc2f72033b1)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/priority-0073.md#compare-ce9e06dcfe1c98db1f949338e2ee8c0f)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aff2cc",
  "name": "FUN_00aff2cc",
  "size": 208,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1da62d81b7a74850beead82b12910edde0c3a03a3dcbdd802905d46f91fa17fd",
  "source_text_sha256": "1da62d81b7a74850beead82b12910edde0c3a03a3dcbdd802905d46f91fa17fd"
}
~~~

## 呼び出し元

- [00685588](../00685/00685588.md)
- [006c52f8](../006c5/006c52f8.md)
- [00a4f3b4](../00a4f/00a4f3b4.md)
- [00af5a94](../00af5/00af5a94.md)
- [00b009dc](../00b00/00b009dc.md)

## 呼び出し先

- [005e7420](../005e7/005e7420.md)
- [008514f8](../00851/008514f8.md)
- [00b04c7c](../00b04/00b04c7c.md)

## 疑似コード / UTF-8 846 bytes

~~~c

ulong FUN_00aff2cc(int param_1,int param_2,int param_3,ulong param_4)

{
  int iVar1;
  long lVar2;
  ulong uVar3;
  
                    /* try { // try from 00aff2cc to 00bff2f7 has its CatchHandler @ 00aff258 */
                    /* catch() { ... } // from try @ 00aff2ac with catch @ 00aff2e4 */
  lVar2 = FUN_008514f8();
  uVar3 = FUN_005e7420(lVar2 + (long)param_1 * 0x1f0 + 0x2768);
  lVar2 = FUN_008514f8();
  if ((uVar3 & 1) == 0) {
    uVar3 = (ulong)(*(int *)((long)__DT_JMPREL + lVar2 + ((long)param_2 + 2) * 0x1c4 + 0x1840) != 0)
    ;
  }
  else {
    iVar1 = *(int *)(lVar2 + ((long)param_2 + 2) * 0x770 + (long)param_3 * 0x1dc + 0x9f724);
    uVar3 = (ulong)(iVar1 != 0);
    if ((iVar1 == 0) && ((param_4 & 1) != 0)) {
      uVar3 = FUN_00b04c7c(param_1,param_2,param_3,0x20);
      return uVar3;
    }
  }
  return uVar3;
}

~~~
