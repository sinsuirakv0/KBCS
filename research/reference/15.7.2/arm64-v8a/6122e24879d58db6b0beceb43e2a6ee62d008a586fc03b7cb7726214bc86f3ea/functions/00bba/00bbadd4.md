# 00bbadd4

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bbadd4.md)

## 関数情報

~~~json
{
  "address": "00bbadd4",
  "name": "std::logic_error::what",
  "size": 12,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "92aadb317bc833b2c1d15db36e3128eb8874cd8412a74169a3c181cc6e543642",
  "source_text_sha256": "92aadb317bc833b2c1d15db36e3128eb8874cd8412a74169a3c181cc6e543642"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード 1/1 / UTF-8 154 bytes

~~~c

/* std::logic_error::what() const */

undefined8 __thiscall std::logic_error::what(logic_error *this)

{
  return *(undefined8 *)(this + 8);
}

~~~
