# 00baaffc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00baaffc.md)

## 関数情報

~~~json
{
  "address": "00baaffc",
  "name": "std::__ndk1::ctype_byname<wchar_t>::do_widen",
  "size": 156,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "54a79e643331ee5984ee4389f72c22b4793382d2b30766ae2fb1fcb13799a150",
  "source_text_sha256": "54a79e643331ee5984ee4389f72c22b4793382d2b30766ae2fb1fcb13799a150"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00be1480](../00be1/00be1480.md)
- [00be1a00](../00be1/00be1a00.md)

## 疑似コード 1/1 / UTF-8 702 bytes

~~~c

/* std::__ndk1::ctype_byname<wchar_t>::do_widen(char const*, char const*, wchar_t*) const */

char * __thiscall
std::__ndk1::ctype_byname<wchar_t>::do_widen
          (ctype_byname<wchar_t> *this,char *param_1,char *param_2,wchar_t *param_3)

{
  byte bVar1;
  char *pcVar2;
  wchar_t wVar3;
  __locale_t __dataset;
  
  pcVar2 = param_1;
  for (; param_1 != param_2; param_1 = param_1 + 1) {
    bVar1 = *param_1;
    __dataset = uselocale(*(__locale_t *)(this + 0x10));
    wVar3 = btowc((uint)bVar1);
    if (__dataset != (__locale_t)0x0) {
      uselocale(__dataset);
    }
    *param_3 = wVar3;
    pcVar2 = param_2;
    param_3 = param_3 + 1;
  }
  return pcVar2;
}

~~~
