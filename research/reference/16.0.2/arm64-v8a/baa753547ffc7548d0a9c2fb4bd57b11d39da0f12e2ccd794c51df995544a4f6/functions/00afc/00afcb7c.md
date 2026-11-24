# 00afcb7c

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00afcae0`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afc/00afcae0.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/alignment_unresolved-0007.md#compare-5bcf4ca3e6b7f08d5c1d8f6850cd3cd8)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/priority-0081.md#compare-959bf921fcf8ac9fec80d4ec99c97cca)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afcb7c",
  "name": "FUN_00afcb7c",
  "size": 84,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1d7bd2d697ddc1ead15244967db44c98d986d5bf3d39f7fcb9c0b4d0fc6997a0",
  "source_text_sha256": "1d7bd2d697ddc1ead15244967db44c98d986d5bf3d39f7fcb9c0b4d0fc6997a0"
}
~~~

## 呼び出し元

- [00700b50](../00700/00700b50.md)

## 呼び出し先

- [00851550](../00851/00851550.md)

## 疑似コード / UTF-8 509 bytes

~~~c

void FUN_00afcb7c(int param_1,int param_2,int param_3)

{
  long lVar1;
  
                    /* catch() { ... } // from try @ 00afb6f0 with catch @ 00afcb84 */
  lVar1 = FUN_00851550();
                    /* catch() { ... } // from try @ 00afb6e4 with catch @ 00afcba4 */
  lVar1 = lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec;
                    /* catch() { ... } // from try @ 00afc848 with catch @ 00afcbbc */
  *(int *)(lVar1 + 0x84bcc) = *(int *)(lVar1 + 0x84bcc) + param_3;
  return;
}

~~~
