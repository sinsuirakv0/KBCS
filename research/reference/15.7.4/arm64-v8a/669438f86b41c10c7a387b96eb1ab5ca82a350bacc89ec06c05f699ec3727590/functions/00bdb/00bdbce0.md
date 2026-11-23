# 00bdbce0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdbc90`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbc90.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/97ee0756e9de6c746e3ce399/1-2/high-0013.md#compare-625d2f94d37e1bae7b2dab9be8ede2a8)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 構造資料不足
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdbce0",
  "name": "_ZN5Botan11DER_Encoder6encodeEPKhmNS_8ASN1_TagES3_S3_",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "890d9ad8533da7bb460c58c7694ad6b5bc631c0852a558286f5885d9643ebf7e",
  "source_text_sha256": "890d9ad8533da7bb460c58c7694ad6b5bc631c0852a558286f5885d9643ebf7e"
}
~~~

## 呼び出し元

- [00490268](../00490/00490268.md)
- [00490d40](../00490/00490d40.md)
- [00490d5c](../00490/00490d5c.md)
- [004c6f64](../004c6/004c6f64.md)
- [004eebcc](../004ee/004eebcc.md)
- [004fc21c](../004fc/004fc21c.md)

## 呼び出し先

- [00490274](../00490/00490274.md)

## 疑似コード / UTF-8 165 bytes

~~~c

void _ZN5Botan11DER_Encoder6encodeEPKhmNS_8ASN1_TagES3_S3_(void)

{
  (*(code *)PTR__ZN5Botan11DER_Encoder6encodeEPKhmNS_8ASN1_TagES3_S3__00c1c728)();
  return;
}

~~~
