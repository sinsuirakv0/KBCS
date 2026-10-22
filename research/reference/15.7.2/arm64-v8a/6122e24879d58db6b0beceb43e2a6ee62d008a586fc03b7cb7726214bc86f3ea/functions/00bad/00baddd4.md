# 00baddd4

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00baddd4.md)

## 関数情報

~~~json
{
  "address": "00baddd4",
  "name": "std::__ndk1::__codecvt_utf16<char16_t,false>::do_in",
  "size": 148,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ab9aff7bec089ff7a9925817a05dbcb0763562a92619d00178bf46c6a08e8e2f",
  "source_text_sha256": "ab9aff7bec089ff7a9925817a05dbcb0763562a92619d00178bf46c6a08e8e2f"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード 1/1 / UTF-8 1248 bytes

~~~c

/* std::__ndk1::__codecvt_utf16<char16_t, false>::do_in(mbstate_t&, char const*, char const*, char
   const*&, char16_t*, char16_t*, char16_t*&) const */

undefined1 __thiscall
std::__ndk1::__codecvt_utf16<char16_t,false>::do_in
          (__codecvt_utf16<char16_t,false> *this,mbstate_t *param_1,char *param_2,char *param_3,
          char **param_4,wchar16 *param_5,wchar16 *param_6,wchar16 **param_7)

{
  wchar16 wVar1;
  undefined1 uVar2;
  wchar16 *pwVar3;
  ulong uVar4;
  
  if (((1 < (long)param_3 - (long)param_2) && ((*(uint *)(this + 0x18) >> 2 & 1) != 0)) &&
     (*param_2 == -2)) {
    param_2 = param_2 + (ulong)(param_2[1] == -1) * 2;
  }
  if (param_2 < param_3 + -1) {
    uVar4 = *(ulong *)(this + 0x10);
    uVar2 = 2;
    pwVar3 = param_5;
    while (param_5 = pwVar3, pwVar3 < param_6) {
      if (((*param_2 & 0xf8U) == 0xd8) ||
         (wVar1 = CONCAT11(*param_2,param_2[1]), uVar4 < (ushort)wVar1)) goto LAB_00bade5c;
      param_2 = param_2 + 2;
      param_5 = pwVar3 + 1;
      *pwVar3 = wVar1;
      pwVar3 = param_5;
      if (param_3 + -1 <= param_2) break;
    }
  }
  uVar2 = param_2 < param_3;
LAB_00bade5c:
  *param_4 = param_2;
  *param_7 = param_5;
  return uVar2;
}

~~~
