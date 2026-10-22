# 00bada1c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bada1c.md)

## 関数情報

~~~json
{
  "address": "00bada1c",
  "name": "std::__ndk1::__codecvt_utf16<wchar_t,true>::do_out",
  "size": 212,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "12ccfa90bd229dd632131b02cbd544afb4b33c25f2412aa8c0cbc6f05c18b40c",
  "source_text_sha256": "12ccfa90bd229dd632131b02cbd544afb4b33c25f2412aa8c0cbc6f05c18b40c"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード 1/1 / UTF-8 1668 bytes

~~~c

/* std::__ndk1::__codecvt_utf16<wchar_t, true>::do_out(mbstate_t&, wchar_t const*, wchar_t const*,
   wchar_t const*&, char*, char*, char*&) const */

undefined8 __thiscall
std::__ndk1::__codecvt_utf16<wchar_t,true>::do_out
          (__codecvt_utf16<wchar_t,true> *this,mbstate_t *param_1,wchar_t *param_2,wchar_t *param_3,
          wchar_t **param_4,char *param_5,char *param_6,char **param_7)

{
  int iVar1;
  wchar_t wVar2;
  undefined8 uVar3;
  byte *pbVar4;
  ulong uVar5;
  
  uVar5 = *(ulong *)(this + 0x18);
  if (((byte)this[0x20] >> 1 & 1) != 0) {
    if ((long)param_6 - (long)param_5 < 2) {
LAB_00bada38:
      uVar3 = 1;
      goto LAB_00badae4;
    }
    param_5[0] = -1;
    param_5[1] = -2;
    param_5 = param_5 + 2;
  }
  for (; param_2 < param_3; param_2 = param_2 + 1) {
    wVar2 = *param_2;
    if ((uint)wVar2 >> 0xb == 0x1b || uVar5 < (uint)wVar2) {
      uVar3 = 2;
      goto LAB_00badae4;
    }
    if ((wVar2 & 0xffff0000U) == 0) {
      if ((long)param_6 - (long)param_5 < 2) goto LAB_00bada38;
      pbVar4 = (byte *)(param_5 + 2);
      *(short *)param_5 = (short)wVar2;
    }
    else {
      if ((long)param_6 - (long)param_5 < 4) goto LAB_00bada38;
      param_5[2] = (byte)wVar2;
      iVar1 = ((uint)wVar2 >> 10 & 0x7c0) + 0x3fc0;
      param_5[3] = (byte)((uint)wVar2 >> 8) & 3 | 0xdc;
      pbVar4 = (byte *)(param_5 + 4);
      *param_5 = (byte)iVar1 | (byte)((uint)wVar2 >> 10) & 0x3f;
      param_5[1] = (byte)((uint)iVar1 >> 8) | 0xd8;
    }
    param_5 = (char *)pbVar4;
  }
  uVar3 = 0;
LAB_00badae4:
  *param_4 = param_2;
  *param_7 = param_5;
  return uVar3;
}

~~~
