# 00bdbcd0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bdbc20`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdbc20.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/af8e2f5c5fc38f06774ff85c/0-1/high-0012.md#compare-90c99618b8f9be7e9b326e85671e5714)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 構造資料不足
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdbcd0",
  "name": "_ZN5Botan11DER_Encoder9encode_ifEbRS0_",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "85dcc20208f9a31949d7c797099658a1901a6ff347236ad93e6951df4bad0e88",
  "source_text_sha256": "85dcc20208f9a31949d7c797099658a1901a6ff347236ad93e6951df4bad0e88"
}
~~~

## 呼び出し元

- [004ef204](../004ef/004ef204.md)
- [004f5078](../004f5/004f5078.md)

## 呼び出し先

- [00490d78](../00490/00490d78.md)

## 疑似コード / UTF-8 135 bytes

~~~c

void _ZN5Botan11DER_Encoder9encode_ifEbRS0_(void)

{
  (*(code *)PTR__ZN5Botan11DER_Encoder9encode_ifEbRS0__00c1c6f8)();
  return;
}

~~~
