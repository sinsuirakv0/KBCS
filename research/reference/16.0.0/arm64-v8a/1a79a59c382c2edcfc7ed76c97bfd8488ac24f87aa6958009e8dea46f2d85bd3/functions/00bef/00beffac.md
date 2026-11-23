# 00beffac

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b733a4`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b733a4.md) · 移動量 `+0x7cc08`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/2-3/machine_only_observed-0018.md#compare-bc8b688ea848b334af9f49344fffafb1)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 構造資料不足
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00beffac",
  "name": "_ZNSt6__ndk112bad_weak_ptrD2Ev",
  "size": 8,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3ef9527838cc2c7003ae287b05c3e3fcbad8cdbac511a4c0d5e68314237b6e9d",
  "source_text_sha256": "3ef9527838cc2c7003ae287b05c3e3fcbad8cdbac511a4c0d5e68314237b6e9d"
}
~~~

## 呼び出し元

- [00c5a390](../00c5a/00c5a390.md)

## 呼び出し先

- [00c57ee0](../00c57/00c57ee0.md)

## 疑似コード / UTF-8 96 bytes

~~~c

void _ZNSt6__ndk112bad_weak_ptrD2Ev(void)

{
  _ZNSt20bad_array_new_lengthD1Ev();
  return;
}

~~~
