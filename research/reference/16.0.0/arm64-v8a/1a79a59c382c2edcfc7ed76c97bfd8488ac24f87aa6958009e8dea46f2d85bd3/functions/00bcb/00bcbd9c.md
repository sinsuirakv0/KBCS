# 00bcbd9c

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b5c89c`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c89c.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/2-3/high-0004.md#compare-1a29c80400822fb41b3653c30d315c60)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 構造資料不足
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcbd9c",
  "name": "_ZN8firebase4auth27CleanupCredentialFutureImplEv",
  "size": 12,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "baf9cfdea0eee5739c8a17e4959f3f5cec3872258f343bfc5f1edd567d1d0d41",
  "source_text_sha256": "baf9cfdea0eee5739c8a17e4959f3f5cec3872258f343bfc5f1edd567d1d0d41"
}
~~~

## 呼び出し元

- [00c5d620](../00c5d/00c5d620.md)

## 呼び出し先

- [00c5b940](../00c5b/00c5b940.md)

## 関連文字列（未確認候補）

~~~text
"Auth-Credentials"
~~~

## 疑似コード / UTF-8 260 bytes

~~~c

void _ZN8firebase4auth27CleanupCredentialFutureImplEv(void)

{
                    /* try { // try from 00bcbd9c to 00ccbe1b has its CatchHandler @ 00bcbd30 */
  _ZN8firebase16StaticFutureData26CleanupFutureDataForModuleEPKv("Auth-Credentials");
  return;
}

~~~
