# 00babb5c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00babb5c.md)

## 関数情報

~~~json
{
  "address": "00babb5c",
  "name": "std::__ndk1::codecvt<wchar_t,char,mbstate_t>::do_length",
  "size": 224,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b4af35d1e9e41f41683d2f0e2e05630aef6f740db93733020bf0c083d8711b26",
  "source_text_sha256": "b4af35d1e9e41f41683d2f0e2e05630aef6f740db93733020bf0c083d8711b26"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00be1480](../00be1/00be1480.md)
- [00be1aa0](../00be1/00be1aa0.md)

## 疑似コード 1/1 / UTF-8 1697 bytes

~~~c

/* std::__ndk1::codecvt<wchar_t, char, mbstate_t>::do_length(mbstate_t&, char const*, char const*,
   unsigned long) const */

int __thiscall
std::__ndk1::codecvt<wchar_t,char,mbstate_t>::do_length
          (codecvt<wchar_t,char,mbstate_t> *this,mbstate_t *param_1,char *param_2,char *param_3,
          ulong param_4)

{
  __locale_t __dataset;
  size_t sVar1;
  int iVar2;
  int iVar3;
  ulong uVar4;
  
                    /* try { // try from 00babb68 to 00cabb7f has its CatchHandler @ 00babbd0 */
  iVar3 = 0;
                    /* try { // try from 00babb80 to 00cabd3b has its CatchHandler @ 00bab67c */
  if ((param_4 != 0) && (param_2 != param_3)) {
    iVar3 = 0;
    uVar4 = 1;
    do {
      __dataset = uselocale(*(__locale_t *)(this + 0x10));
      sVar1 = mbrlen(param_2,(long)param_3 - (long)param_2,param_1);
                    /* catch() { ... } // from try @ 00babb68 with catch @ 00babbd0 */
      if (__dataset != (__locale_t)0x0) {
        uselocale(__dataset);
      }
      if (sVar1 == 0) {
        sVar1 = 1;
        iVar2 = 1;
      }
      else {
                    /* catch() { ... } // from try @ 00babb58 with catch @ 00babbe8 */
        if (sVar1 + 2 < 2) {
          return iVar3;
        }
        iVar2 = (int)sVar1;
      }
                    /* catch() { ... } // from try @ 00baba44 with catch @ 00babbfc */
      iVar3 = iVar2 + iVar3;
      if (param_4 <= uVar4) {
        return iVar3;
      }
      param_2 = param_2 + sVar1;
      uVar4 = uVar4 + 1;
    } while (param_2 != param_3);
  }
                    /* catch() { ... } // from try @ 00bab8c8 with catch @ 00babc18 */
  return iVar3;
}

~~~
