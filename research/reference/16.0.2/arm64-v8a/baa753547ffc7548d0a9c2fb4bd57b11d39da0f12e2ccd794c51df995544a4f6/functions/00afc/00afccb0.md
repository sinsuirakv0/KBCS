# 00afccb0

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00afcc14`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afc/00afcc14.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/alignment_unresolved-0007.md#compare-2a0d6d7b356497d98d16183c90457df8)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/priority-0081.md#compare-5ea46eb666dc794b52880b9f42dc65e2)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afccb0",
  "name": "FUN_00afccb0",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "846d46f2ab4594e647ae3f4a244cdbead4d62f941db83ae00ba09e4650d6dfc4",
  "source_text_sha256": "846d46f2ab4594e647ae3f4a244cdbead4d62f941db83ae00ba09e4650d6dfc4"
}
~~~

## 呼び出し元

- [005f2da8](../005f2/005f2da8.md)
- [00707f38](../00707/00707f38.md)
- [00711a48](../00711/00711a48.md)

## 呼び出し先

- [00851550](../00851/00851550.md)

## 疑似コード / UTF-8 452 bytes

~~~c

undefined4 FUN_00afccb0(int param_1,int param_2)

{
  long lVar1;
  
                    /* catch() { ... } // from try @ 00afc99c with catch @ 00afccb4 */
  lVar1 = FUN_00851550();
                    /* catch() { ... } // from try @ 00afbec8 with catch @ 00afcccc */
                    /* catch() { ... } // from try @ 00afc968 with catch @ 00afccec */
  return *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84c10);
}

~~~
