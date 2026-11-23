# 00bdcdc0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdcd70`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcd70.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/97ee0756e9de6c746e3ce399/1-2/alignment_unresolved-0005.md#compare-f139f03ae0baabd11a4eb6565adcd79c)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 構造資料不足
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdcdc0",
  "name": "_ZNK5Botan16X509_Certificate23load_subject_public_keyEv",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1e61f413f441edf365fe23104b6bdd5bed014a21f28c1bc499411cb45a856552",
  "source_text_sha256": "1e61f413f441edf365fe23104b6bdd5bed014a21f28c1bc499411cb45a856552"
}
~~~

## 呼び出し元

- [004e85ec](../004e8/004e85ec.md)
- [00501b08](../00501/00501b08.md)
- [00503af8](../00503/00503af8.md)
- [005054cc](../00505/005054cc.md)

## 呼び出し先

- [00500f10](../00500/00500f10.md)

## 疑似コード / UTF-8 266 bytes

~~~c

void _ZNK5Botan16X509_Certificate23load_subject_public_keyEv(void)

{
                    /* try { // try from 00bdcdcc to 00cdced3 has its CatchHandler @ 00bdccd8 */
  (*(code *)PTR__ZNK5Botan16X509_Certificate23load_subject_public_keyEv_00c1cf98)();
  return;
}

~~~
