# 004bbbac

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `004bbbac`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004bb/004bbbac.md) · 移動量 `+0x0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/af8e2f5c5fc38f06774ff85c/0-1/detail_skipped-0003.md#compare-1bb189eb07547a55f87fa71f7c9dfc82)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 構造資料不足
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "004bbbac",
  "name": "_ZN5Botan9Power_Mod11window_bitsEmmNS0_11Usage_HintsE",
  "size": 132,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0bbad264736ce2902588b97bd8bfe144a275970b79279062d89cd280ad8e554d",
  "source_text_sha256": "0bbad264736ce2902588b97bd8bfe144a275970b79279062d89cd280ad8e554d"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 805 bytes

~~~c

long _ZN5Botan9Power_Mod11window_bitsEmmNS0_11Usage_HintsE
               (ulong param_1,undefined8 param_2,uint param_3)

{
  long lVar1;
  undefined *puVar2;
  
  if (param_1 == 0) {
LAB_004bbbd8:
    lVar1 = 1;
  }
  else {
    if (param_1 < 0x59a) {
      if (param_1 < 0x21b) {
        if (param_1 < 0xc5) {
          if (param_1 < 0x46) {
            if (param_1 < 0x19) goto LAB_004bbbd8;
            puVar2 = &UNK_002b99b8;
          }
          else {
            puVar2 = &UNK_002b99a8;
          }
        }
        else {
          puVar2 = &UNK_002b9998;
        }
      }
      else {
        puVar2 = &UNK_002b9988;
      }
    }
    else {
      puVar2 = &UNK_002b9978;
    }
    lVar1 = *(long *)(puVar2 + 8) + 1;
  }
  return lVar1 + (ulong)((param_3 & 1) << 1 | param_3 >> 10 & 1);
}

~~~
