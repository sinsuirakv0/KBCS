# 00abe7fc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00abe78c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00abe/00abe78c.md) · 移動量 `+0x70`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/alignment_unresolved-0005.md#compare-f7ec75e512dd74ebf9b45963edbbbe74)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/priority-0076.md#compare-b051613330247e4e02919dfd0164cce2)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00abe7fc",
  "name": "FUN_00abe7fc",
  "size": 108,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5e1f99fd17e5a8044f7990a08f525f6980bb671d73b884e558cfa9d0c897d5f2",
  "source_text_sha256": "5e1f99fd17e5a8044f7990a08f525f6980bb671d73b884e558cfa9d0c897d5f2"
}
~~~

## 呼び出し元

- [006ee798](../006ee/006ee798.md)
- [006f252c](../006f2/006f252c.md)
- [00a52034](../00a52/00a52034.md)

## 呼び出し先

- [00abd080](../00abd/00abd080.md)

## 疑似コード / UTF-8 509 bytes

~~~c

void FUN_00abe7fc(long param_1,int param_2,int param_3)

{
  int iVar1;
  int iVar2;
  
  iVar2 = FUN_00abd080();
                    /* catch() { ... } // from try @ 00abe684 with catch @ 00abe828 */
  iVar1 = iVar2 + param_3;
  if (1999999999 < iVar2 + param_3) {
    iVar1 = 2000000000;
  }
  if (param_2 == 4) {
    *(int *)(param_1 + 0x68) = iVar1;
  }
  else if (param_2 == 1) {
    *(int *)(param_1 + 100) = iVar1;
  }
  else if (param_2 == 0) {
    *(int *)(param_1 + 0x60) = iVar1;
  }
  return;
}

~~~
