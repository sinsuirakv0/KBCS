# 00aecbb4

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00aecbb4.md)

## 関数情報

~~~json
{
  "address": "00aecbb4",
  "name": "firebase::util::parcel_file_descriptor::GetMethodId",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7ab0aa244b7d1dccc4cdbdda84de0fd7632fafdea2eaa63b80e14b59fd10fb3c",
  "source_text_sha256": "7ab0aa244b7d1dccc4cdbdda84de0fd7632fafdea2eaa63b80e14b59fd10fb3c"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bde080](../00bde/00bde080.md)

## 関連文字列（未確認候補）

~~~text
"method < kMethodCount"
~~~
## 疑似コード 1/1 / UTF-8 340 bytes

~~~c

/* firebase::util::parcel_file_descriptor::GetMethodId(firebase::util::parcel_file_descriptor::Method)
    */

undefined8 firebase::util::parcel_file_descriptor::GetMethodId(uint param_1)

{
  if (0 < (int)param_1) {
    LogAssert("method < kMethodCount");
  }
  return *(undefined8 *)(&DAT_010a08b8 + (ulong)param_1 * 8);
}

~~~
