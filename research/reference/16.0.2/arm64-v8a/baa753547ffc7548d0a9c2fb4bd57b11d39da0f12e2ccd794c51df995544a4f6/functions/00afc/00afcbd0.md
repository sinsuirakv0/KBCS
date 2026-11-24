# 00afcbd0

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00afcb34`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afc/00afcb34.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/alignment_unresolved-0007.md#compare-9fffb7ca0094db2eae6b9a4304fb1e23)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/priority-0081.md#compare-3a3ead16d6eaff533366423327197136)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afcbd0",
  "name": "FUN_00afcbd0",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d61106c17658076a3c8011997a5fc222274b3e324a214d5af3a94e29186e966c",
  "source_text_sha256": "d61106c17658076a3c8011997a5fc222274b3e324a214d5af3a94e29186e966c"
}
~~~

## 呼び出し元

- [00707f38](../00707/00707f38.md)
- [00716de8](../00716/00716de8.md)

## 呼び出し先

- [00851550](../00851/00851550.md)

## 疑似コード / UTF-8 794 bytes

~~~c

undefined4 FUN_00afcbd0(int param_1,int param_2)

{
  long lVar1;
  
  lVar1 = FUN_00851550();
                    /* catch() { ... } // from try @ 00afc0b8 with catch @ 00afcbfc */
                    /* catch() { ... } // from try @ 00afc088 with catch @ 00afcc00
                       catch() { ... } // from try @ 00afc164 with catch @ 00afcc00 */
                    /* catch() { ... } // from try @ 00afbf44 with catch @ 00afcc04 */
                    /* catch() { ... } // from try @ 00afc770 with catch @ 00afcc08 */
                    /* catch() { ... } // from try @ 00afc734 with catch @ 00afcc0c
                       catch() { ... } // from try @ 00afc818 with catch @ 00afcc0c */
  return *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84bd4);
}

~~~
