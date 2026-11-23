# 00bdaff0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdafa0`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafa0.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/97ee0756e9de6c746e3ce399/1-2/alignment_unresolved-0004.md#compare-a15970af6f4c66ee86ebeb4e950fcabc)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 構造資料不足
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdaff0",
  "name": "<EXTERNAL>::__register_atfork",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "097c888f1382fc1ba10f6d8f4dab5e20f04ef0b3ef7a08a4dcc4df0014984a78",
  "source_text_sha256": "097c888f1382fc1ba10f6d8f4dab5e20f04ef0b3ef7a08a4dcc4df0014984a78"
}
~~~

## 呼び出し元

- [00418320](../00418/00418320.md)

## 呼び出し先

- [010a5010](../010a5/010a5010.md)

## 疑似コード / UTF-8 190 bytes

~~~c

void __register_atfork(void)

{
                    /* try { // try from 00bdaff8 to 00cdb057 has its CatchHandler @ 00bdaf98 */
  (*(code *)PTR___register_atfork_00c1c0b0)();
  return;
}

~~~
