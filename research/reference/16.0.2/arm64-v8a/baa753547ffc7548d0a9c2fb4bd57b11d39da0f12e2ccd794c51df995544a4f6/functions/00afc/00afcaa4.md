# 00afcaa4

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00afca08`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afc/00afca08.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/alignment_unresolved-0007.md#compare-614b782bc9053a89f9b3b2ee129e516c)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/priority-0081.md#compare-1a2200d55c61c1772d1cae3f4386718e)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afcaa4",
  "name": "FUN_00afcaa4",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d2ef84b7ce28af67bcd09b99049ad8adac451d66b7ddd8384bd95cad42ec5374",
  "source_text_sha256": "d2ef84b7ce28af67bcd09b99049ad8adac451d66b7ddd8384bd95cad42ec5374"
}
~~~

## 呼び出し元

- [00700b50](../00700/00700b50.md)
- [00716de8](../00716/00716de8.md)
- [00a4f424](../00a4f/00a4f424.md)

## 呼び出し先

- [00851550](../00851/00851550.md)

## 疑似コード / UTF-8 478 bytes

~~~c

void FUN_00afcaa4(int param_1,int param_2,undefined4 param_3)

{
  long lVar1;
  
  lVar1 = FUN_00851550();
                    /* catch() { ... } // from try @ 00afc094 with catch @ 00afcac8 */
                    /* catch() { ... } // from try @ 00afba7c with catch @ 00afcacc */
  *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84bc8) = param_3;
                    /* catch() { ... } // from try @ 00afba30 with catch @ 00afcae8 */
  return;
}

~~~
