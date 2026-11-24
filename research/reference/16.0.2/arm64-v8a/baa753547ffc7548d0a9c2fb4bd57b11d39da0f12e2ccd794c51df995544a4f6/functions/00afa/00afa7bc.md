# 00afa7bc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00afa720`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afa/00afa720.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/alignment_unresolved-0006.md#compare-0a9b5a73a4ca713f419cdb2b69aefa14)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/priority-0080.md#compare-819af9c5aeca702976224438292899e0)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afa7bc",
  "name": "FUN_00afa7bc",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4d9260173c934c0c37ccd2c5e53c09ec7b3306868c32cd513ec416eea75d8ef8",
  "source_text_sha256": "4d9260173c934c0c37ccd2c5e53c09ec7b3306868c32cd513ec416eea75d8ef8"
}
~~~

## 呼び出し元

- [0070eab4](../0070e/0070eab4.md)
- [00710330](../00710/00710330.md)
- [00711a48](../00711/00711a48.md)

## 呼び出し先

- [005e7460](../005e7/005e7460.md)
- [00851550](../00851/00851550.md)

## 疑似コード / UTF-8 579 bytes

~~~c

bool FUN_00afa7bc(int param_1,int param_2)

{
  bool bVar1;
  long lVar2;
  ulong uVar3;
  
  lVar2 = FUN_00851550();
  uVar3 = FUN_005e7460(lVar2 + (long)param_1 * 0x1f0 + 0x2768);
  if ((uVar3 & 1) == 0) {
    bVar1 = false;
  }
  else {
    lVar2 = FUN_00851550();
                    /* try { // try from 00afa810 to 00bfa823 has its CatchHandler @ 00afab7c */
    bVar1 = *(int *)(lVar2 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84c28) != 0;
  }
                    /* try { // try from 00afa828 to 00bfa83f has its CatchHandler @ 00afaa48 */
  return bVar1;
}

~~~
