# 00bcbd8c

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

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
