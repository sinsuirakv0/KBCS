# 00bcbd8c

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b5c88c`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c88c.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/2-3/alignment_unresolved-0017.md#compare-1fc25db11bfbf107df383ba0ee210d6f)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 構造資料不足
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcbd8c",
  "name": "_ZN8firebase4auth23GetCredentialFutureImplEv",
  "size": 16,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f6e41839343f179f054c0e19b9c431dbd681312db7328e30499d1392491581eb",
  "source_text_sha256": "f6e41839343f179f054c0e19b9c431dbd681312db7328e30499d1392491581eb"
}
~~~

## 呼び出し元

- [00c5d750](../00c5d/00c5d750.md)

## 呼び出し先

- [00c5b930](../00c5b/00c5b930.md)

## 関連文字列（未確認候補）

~~~text
"Auth-Credentials"
~~~

## 疑似コード / UTF-8 255 bytes

~~~c

void _ZN8firebase4auth23GetCredentialFutureImplEv(void)

{
                    /* try { // try from 00bcbd90 to 00ccbd9b has its CatchHandler @ 00bcbdf4 */
  _ZN8firebase16StaticFutureData22GetFutureDataForModuleEPKvi("Auth-Credentials",1);
  return;
}

~~~
