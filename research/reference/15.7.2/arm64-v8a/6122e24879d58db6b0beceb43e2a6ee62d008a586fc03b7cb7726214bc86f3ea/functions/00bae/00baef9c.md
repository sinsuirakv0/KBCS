# 00baef9c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00baef9c.md)

## 関数情報

~~~json
{
  "address": "00baef9c",
  "name": "std::__ndk1::numpunct<char>::~numpunct",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "fab26a4cfbd4d2e359e705142a46004e11b8aa485b13f1f4cf1e43abe25b1a63",
  "source_text_sha256": "fab26a4cfbd4d2e359e705142a46004e11b8aa485b13f1f4cf1e43abe25b1a63"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdaf60](../00bda/00bdaf60.md)
- [00be1b40](../00be1/00be1b40.md)

## 疑似コード 1/1 / UTF-8 197 bytes

~~~c

/* std::__ndk1::numpunct<char>::~numpunct() */

void __thiscall std::__ndk1::numpunct<char>::~numpunct(numpunct<char> *this)

{
  ~numpunct(this);
  operator_delete(this);
  return;
}

~~~
