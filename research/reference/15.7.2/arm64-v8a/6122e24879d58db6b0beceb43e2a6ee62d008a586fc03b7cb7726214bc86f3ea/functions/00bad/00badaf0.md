# 00badaf0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00badaf0.md)

## 関数情報

~~~json
{
  "address": "00badaf0",
  "name": "std::__ndk1::__codecvt_utf16<wchar_t,true>::do_in",
  "size": 252,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e04f6bd267530ad7e39d109a9b1a2c02453d4f163b5773c5e729aca9e3f5922c",
  "source_text_sha256": "863e5dde0a647f9f6b57480ae788e6e834acf5287bdb01c764ef7d59b9252ad1"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード 1/1 / UTF-8 1993 bytes

~~~c

/* std::__ndk1::__codecvt_utf16<wchar_t, true>::do_in(mbstate_t&, char const*, char const*, char
   const*&, wchar_t*, wchar_t*, wchar_t*&) const */

ulong __thiscall
std::__ndk1::__codecvt_utf16<wchar_t,true>::do_in
          (__codecvt_utf16<wchar_t,true> *this,mbstate_t *param_1,char *param_2,char *param_3,
          char **param_4,wchar_t *param_5,wchar_t *param_6,wchar_t **param_7)

{
  byte bVar1;
  ulong uVar2;
  wchar_t *pwVar3;
  ulong uVar4;
  wchar_t wVar5;
  
  if (((1 < (long)param_3 - (long)param_2) && ((*(uint *)(this + 0x20) >> 2 & 1) != 0)) &&
     (*param_2 == -1)) {
    param_2 = param_2 + (ulong)(param_2[1] == -2) * 2;
  }
  if (param_2 < param_3 + -1) {
    uVar4 = *(ulong *)(this + 0x18);
    pwVar3 = param_5;
    do {
      param_5 = pwVar3;
      if (param_6 <= pwVar3) break;
      wVar5 = (wchar_t)*(ushort *)param_2;
      bVar1 = *(byte *)((long)param_2 + 1) & 0xfc;
      if (bVar1 == 0xd8) {
        if ((long)param_3 - (long)param_2 < 4) {
          uVar2 = 1;
          goto LAB_00badbd0;
        }
                    /* catch() { ... } // from try @ 00badd8c with catch @ 00badbb0 */
        if (((*(byte *)((long)param_2 + 3) & 0xfc) != 0xdc) ||
           (wVar5 = ((uint)(byte)*(ushort *)((long)param_2 + 2) |
                     (*(byte *)((long)param_2 + 3) & 3) << 8 | (wVar5 & 0x3ffU) << 10) + L'𐀀',
           uVar4 < (uint)wVar5)) goto LAB_00badbdc;
        uVar2 = 4;
      }
      else {
        if (bVar1 == 0xdc) {
LAB_00badbdc:
          uVar2 = 2;
          goto LAB_00badbd0;
        }
        uVar2 = 2;
        if (uVar4 < (uint)wVar5) goto LAB_00badbd0;
      }
      param_2 = (char *)((long)param_2 + uVar2);
      param_5 = pwVar3 + 1;
      *pwVar3 = wVar5;
      pwVar3 = param_5;
    } while (param_2 < param_3 + -1);
  }
  uVar2 = (ulong)(param_2 < param_3);
  pwVar3 = param_5;
LAB_00badbd0:
  *param_4 = param_2;
  *param_7 = pwVar3;
  return uVar2;
}

~~~
