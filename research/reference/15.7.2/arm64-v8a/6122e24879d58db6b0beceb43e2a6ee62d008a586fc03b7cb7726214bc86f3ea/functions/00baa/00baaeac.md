# 00baaeac

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00baaeac.md)

## 関数情報

~~~json
{
  "address": "00baaeac",
  "name": "std::__ndk1::ctype_byname<wchar_t>::do_toupper",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f999fc505805b0b06458c640a86ff55f3ece9ec63b04828dc1d7afa9a7d3289d",
  "source_text_sha256": "f999fc505805b0b06458c640a86ff55f3ece9ec63b04828dc1d7afa9a7d3289d"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00be19e0](../00be1/00be19e0.md)

## 疑似コード 1/1 / UTF-8 294 bytes

~~~c

/* std::__ndk1::ctype_byname<wchar_t>::do_toupper(wchar_t) const */

wint_t __thiscall
std::__ndk1::ctype_byname<wchar_t>::do_toupper(ctype_byname<wchar_t> *this,wchar_t param_1)

{
  wint_t wVar1;
  
  wVar1 = towupper_l(param_1,*(__locale_t *)(this + 0x10));
  return wVar1;
}

~~~
