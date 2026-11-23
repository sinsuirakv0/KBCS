# 00bdcdf0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bdcd40`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcd40.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/af8e2f5c5fc38f06774ff85c/0-1/high-0014.md#compare-4983c4d9156275f5aa8874126f134034)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 構造資料不足
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdcdf0",
  "name": "_ZNK5Botan14PKCS10_Request18subject_public_keyEv",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d55cea7e94b2c6a67e1302c7c6817493734b9fb089cbc46af5a41c8125d33e00",
  "source_text_sha256": "d55cea7e94b2c6a67e1302c7c6817493734b9fb089cbc46af5a41c8125d33e00"
}
~~~

## 呼び出し元

- [004eb16c](../004eb/004eb16c.md)
- [004ede80](../004ed/004ede80.md)

## 呼び出し先

- [004ec0b4](../004ec/004ec0b4.md)

## 疑似コード / UTF-8 155 bytes

~~~c

void _ZNK5Botan14PKCS10_Request18subject_public_keyEv(void)

{
  (*(code *)PTR__ZNK5Botan14PKCS10_Request18subject_public_keyEv_00c1cf88)();
  return;
}

~~~
