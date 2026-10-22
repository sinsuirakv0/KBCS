# 00afcdf0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00afcdf0.md)

## 関数情報

~~~json
{
  "address": "00afcdf0",
  "name": "firebase::Path::Path",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2d8b5a5602eea1991ab8f2ef06810729019ec8150191050d1df1a785878c260e",
  "source_text_sha256": "2d8b5a5602eea1991ab8f2ef06810729019ec8150191050d1df1a785878c260e"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdec30](../00bde/00bdec30.md)

## 疑似コード 1/1 / UTF-8 278 bytes

~~~c

/* firebase::Path::Path(std::__ndk1::basic_string<char, std::__ndk1::char_traits<char>,
   std::__ndk1::allocator<char> > const&) */

void __thiscall firebase::Path::Path(Path *this,basic_string *param_1)

{
  NormalizeSlashes((Path *)param_1,param_1);
  return;
}

~~~
