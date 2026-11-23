# 00bdccb0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdcc60`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcc60.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/97ee0756e9de6c746e3ce399/1-2/high-0016.md#compare-7099bc784a5a9d1571a82d30beff702e)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 構造資料不足
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdccb0",
  "name": "_ZN5Botan7X509_DN13add_attributeERKNS_3OIDERKNSt6__ndk112basic_stringIcNS4_11char_traitsIcEENS4_9allocatorIcEEEE",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "58468e8c3571a37d1a9304d51171decebfedf1e6439713ee75712912e9ae1676",
  "source_text_sha256": "58468e8c3571a37d1a9304d51171decebfedf1e6439713ee75712912e9ae1676"
}
~~~

## 呼び出し元

- [004e1f38](../004e1/004e1f38.md)
- [004e20fc](../004e2/004e20fc.md)
- [004e40b8](../004e4/004e40b8.md)
- [004e5850](../004e5/004e5850.md)
- [004f10f4](../004f1/004f10f4.md)
- [004f1394](../004f1/004f1394.md)
- [0050af44](../0050a/0050af44.md)

## 呼び出し先

- [004f11e0](../004f1/004f11e0.md)

## 疑似コード / UTF-8 307 bytes

~~~c

void _ZN5Botan7X509_DN13add_attributeERKNS_3OIDERKNSt6__ndk112basic_stringIcNS4_11char_traitsIcEENS4_9allocatorIcEEEE
               (void)

{
  (*(code *)
    PTR__ZN5Botan7X509_DN13add_attributeERKNS_3OIDERKNSt6__ndk112basic_stringIcNS4_11char_traitsIcEENS4_9allocatorIcEEEE_00c1cf10
  )();
  return;
}

~~~
