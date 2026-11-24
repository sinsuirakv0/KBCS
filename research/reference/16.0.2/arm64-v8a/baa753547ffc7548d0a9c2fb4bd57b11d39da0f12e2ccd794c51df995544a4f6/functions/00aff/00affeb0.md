# 00affeb0

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00affe14`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aff/00affe14.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/priority-0067.md#compare-f77157a3516c9806a445a13bea650420)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/priority-0081.md#compare-5e137b60cbff1460c75408293891062f)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00affeb0",
  "name": "FUN_00affeb0",
  "size": 200,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8870f9559e2bc8678b18a241c8f8f44f364f0e236e1bcffc5fcedf2363682e87",
  "source_text_sha256": "8870f9559e2bc8678b18a241c8f8f44f364f0e236e1bcffc5fcedf2363682e87"
}
~~~

## 呼び出し元

- [00a4f424](../00a4f/00a4f424.md)

## 呼び出し先

- [005e7460](../005e7/005e7460.md)
- [00851550](../00851/00851550.md)
- [00afeb84](../00afe/00afeb84.md)

## 疑似コード / UTF-8 857 bytes

~~~c

int FUN_00affeb0(int param_1,int param_2,int param_3)

{
  int iVar1;
  int iVar2;
  long lVar3;
  ulong uVar4;
  
  lVar3 = FUN_00851550();
  uVar4 = FUN_005e7460(lVar3 + (long)param_1 * 0x1f0 + 0x2768);
  lVar3 = FUN_00851550();
                    /* try { // try from 00affef0 to 00bfff0b has its CatchHandler @ 00afff2c */
  if ((uVar4 & 1) == 0) {
    iVar1 = *(int *)((long)__DT_JMPREL + lVar3 + ((long)param_2 + 2) * 0x1c4 + 0x1808);
                    /* try { // try from 00afff0c to 00bfff3f has its CatchHandler @ 00affea8 */
  }
  else {
                    /* catch() { ... } // from try @ 00affef0 with catch @ 00afff2c */
    iVar1 = *(int *)(lVar3 + ((long)param_2 + 2) * 0x770 + (long)param_3 * 0x1dc + 0x9f6e0);
    iVar2 = FUN_00afeb84(param_1,param_2,param_3,0x3d,0);
    iVar1 = ((100 - iVar2) * iVar1) / 100;
  }
  return iVar1;
}

~~~
