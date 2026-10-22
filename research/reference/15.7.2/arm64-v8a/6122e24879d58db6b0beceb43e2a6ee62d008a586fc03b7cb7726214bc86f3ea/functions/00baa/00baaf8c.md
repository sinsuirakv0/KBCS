# 00baaf8c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00baaf8c.md)

## 関数情報

~~~json
{
  "address": "00baaf8c",
  "name": "std::__ndk1::ctype_byname<wchar_t>::do_widen",
  "size": 88,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3622c2a68a669b189524a4ae46c78a6816e62c97fcd83a9e354ad4aa0ff4378f",
  "source_text_sha256": "3622c2a68a669b189524a4ae46c78a6816e62c97fcd83a9e354ad4aa0ff4378f"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00be1480](../00be1/00be1480.md)
- [00be1a00](../00be1/00be1a00.md)

## 疑似コード 1/1 / UTF-8 414 bytes

~~~c

/* std::__ndk1::ctype_byname<wchar_t>::do_widen(char) const */

wint_t __thiscall
std::__ndk1::ctype_byname<wchar_t>::do_widen(ctype_byname<wchar_t> *this,char param_1)

{
  wint_t wVar1;
  __locale_t __dataset;
  
  __dataset = uselocale(*(__locale_t *)(this + 0x10));
  wVar1 = btowc((uint)(byte)param_1);
  if (__dataset != (__locale_t)0x0) {
    uselocale(__dataset);
  }
  return wVar1;
}

~~~
