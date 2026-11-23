# 00beffb4

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b733ac`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b733ac.md) · 移動量 `+0x7cc08`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/2-3/alignment_unresolved-0018.md#compare-efd8a2ec2846b7224ebd3bf3a84408f9)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 構造資料不足
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00beffb4",
  "name": "_ZNSt6__ndk112bad_weak_ptrD0Ev",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b61dccad7ab163de2d3dc60bbf4bccabaff1d67e9eb0b6bca32fe292b450fe06",
  "source_text_sha256": "b61dccad7ab163de2d3dc60bbf4bccabaff1d67e9eb0b6bca32fe292b450fe06"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57ab0](../00c57/00c57ab0.md)
- [00c5a390](../00c5a/00c5a390.md)

## 疑似コード / UTF-8 317 bytes

~~~c

void _ZNSt6__ndk112bad_weak_ptrD0Ev(void *param_1)

{
                    /* try { // try from 00beffb8 to 00ceffdb has its CatchHandler @ 00bf006c */
  _ZNSt6__ndk112bad_weak_ptrD2Ev();
                    /* try { // try from 00beffdc to 00cf016b has its CatchHandler @ 00befce0 */
  _ZdlPv(param_1);
  return;
}

~~~
