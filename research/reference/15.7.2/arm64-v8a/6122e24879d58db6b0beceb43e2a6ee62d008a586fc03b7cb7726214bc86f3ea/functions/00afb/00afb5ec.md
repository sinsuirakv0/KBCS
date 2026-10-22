# 00afb5ec

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00afb5ec.md)

## 関数情報

~~~json
{
  "address": "00afb5ec",
  "name": "firebase::Logger::GetLogLevel",
  "size": 8,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ade7b84a7bbb0616d6969805b08b9cdce1f813cfa8120a2d2b90ec0cc4138b49",
  "source_text_sha256": "ade7b84a7bbb0616d6969805b08b9cdce1f813cfa8120a2d2b90ec0cc4138b49"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード 1/1 / UTF-8 166 bytes

~~~c

/* firebase::Logger::GetLogLevel() const */

undefined4 __thiscall firebase::Logger::GetLogLevel(Logger *this)

{
  return *(undefined4 *)(this + 0x10);
}

~~~
