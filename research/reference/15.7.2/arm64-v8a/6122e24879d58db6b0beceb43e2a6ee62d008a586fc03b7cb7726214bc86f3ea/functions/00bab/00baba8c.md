# 00baba8c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00baba8c.md)

## 関数情報

~~~json
{
  "address": "00baba8c",
  "name": "std::__ndk1::codecvt<wchar_t,char,mbstate_t>::do_encoding",
  "size": 160,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d8029fb4b289c32a4d0bb91106bb33f33269fbf1611c574f8ca8472efbc6ee9e",
  "source_text_sha256": "d8029fb4b289c32a4d0bb91106bb33f33269fbf1611c574f8ca8472efbc6ee9e"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00be1480](../00be1/00be1480.md)
- [00be1a80](../00be1/00be1a80.md)
- [00be1a90](../00be1/00be1a90.md)

## 疑似コード 1/1 / UTF-8 843 bytes

~~~c

/* std::__ndk1::codecvt<wchar_t, char, mbstate_t>::do_encoding() const */

ulong __thiscall
std::__ndk1::codecvt<wchar_t,char,mbstate_t>::do_encoding(codecvt<wchar_t,char,mbstate_t> *this)

{
  int iVar1;
  __locale_t p_Var2;
  ulong uVar3;
  size_t sVar4;
  
  p_Var2 = uselocale(*(__locale_t *)(this + 0x10));
  iVar1 = mbtowc((wchar_t *)0x0,(char *)0x0,4);
  if (p_Var2 != (__locale_t)0x0) {
    uselocale(p_Var2);
  }
  if (iVar1 == 0) {
    if (*(__locale_t *)(this + 0x10) == (__locale_t)0x0) {
      uVar3 = 1;
    }
    else {
      p_Var2 = uselocale(*(__locale_t *)(this + 0x10));
      sVar4 = __ctype_get_mb_cur_max();
      if (p_Var2 != (__locale_t)0x0) {
        uselocale(p_Var2);
      }
      uVar3 = (ulong)(sVar4 == 1);
    }
  }
  else {
    uVar3 = 0xffffffff;
  }
  return uVar3;
}

~~~
