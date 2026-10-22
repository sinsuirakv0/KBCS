# 00baaab0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00baaab0.md)

## 関数情報

~~~json
{
  "address": "00baaab0",
  "name": "std::__ndk1::ctype_byname<wchar_t>::do_is",
  "size": 412,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "fda756c96b482b5079cdb4d70c7dd3d0a3abcaf6015362acadac068aa6571be8",
  "source_text_sha256": "fda756c96b482b5079cdb4d70c7dd3d0a3abcaf6015362acadac068aa6571be8"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00be18b0](../00be1/00be18b0.md)
- [00be1950](../00be1/00be1950.md)
- [00be1960](../00be1/00be1960.md)
- [00be1970](../00be1/00be1970.md)
- [00be1980](../00be1/00be1980.md)
- [00be1990](../00be1/00be1990.md)
- [00be19a0](../00be1/00be19a0.md)
- [00be19b0](../00be1/00be19b0.md)
- [00be19c0](../00be1/00be19c0.md)
- [00be19d0](../00be1/00be19d0.md)

## 疑似コード 1/1 / UTF-8 2139 bytes

~~~c

/* std::__ndk1::ctype_byname<wchar_t>::do_is(wchar_t const*, wchar_t const*, unsigned long*) const
    */

wchar_t * __thiscall
std::__ndk1::ctype_byname<wchar_t>::do_is
          (ctype_byname<wchar_t> *this,wchar_t *param_1,wchar_t *param_2,ulong *param_3)

{
  wchar_t __wc;
  wchar_t *pwVar1;
  int iVar2;
  __locale_t __locale;
  ulong uVar3;
  
  pwVar1 = param_1;
  do {
    if (param_1 == param_2) {
      return pwVar1;
    }
    __wc = *param_1;
    if ((uint)__wc < 0x80) {
      uVar3 = *(ulong *)(&DAT_002fb120 + (ulong)(uint)__wc * 8);
LAB_00baaaf0:
      *param_3 = uVar3;
    }
    else {
      __locale = *(__locale_t *)(this + 0x10);
      *param_3 = 0;
      iVar2 = iswspace_l(__wc,__locale);
      if (iVar2 != 0) {
        *param_3 = *param_3 | 1;
      }
      iVar2 = iswprint_l(__wc,*(__locale_t *)(this + 0x10));
      if (iVar2 != 0) {
        *param_3 = *param_3 | 2;
      }
      iVar2 = iswcntrl_l(__wc,*(__locale_t *)(this + 0x10));
      if (iVar2 != 0) {
        *param_3 = *param_3 | 4;
      }
      iVar2 = iswupper_l(__wc,*(__locale_t *)(this + 0x10));
      if (iVar2 != 0) {
        *param_3 = *param_3 | 8;
      }
      iVar2 = iswlower_l(__wc,*(__locale_t *)(this + 0x10));
      if (iVar2 != 0) {
        *param_3 = *param_3 | 0x10;
      }
      iVar2 = iswalpha_l(__wc,*(__locale_t *)(this + 0x10));
      if (iVar2 != 0) {
        *param_3 = *param_3 | 0x20;
      }
      iVar2 = iswdigit_l(__wc,*(__locale_t *)(this + 0x10));
      if (iVar2 != 0) {
        *param_3 = *param_3 | 0x40;
      }
      iVar2 = iswpunct_l(__wc,*(__locale_t *)(this + 0x10));
      if (iVar2 != 0) {
        *param_3 = *param_3 | 0x80;
      }
      iVar2 = iswxdigit_l(__wc,*(__locale_t *)(this + 0x10));
      if (iVar2 != 0) {
        *param_3 = *param_3 | 0x100;
      }
      iVar2 = iswblank_l(__wc,*(__locale_t *)(this + 0x10));
      if (iVar2 != 0) {
        uVar3 = *param_3 | 0x200;
        goto LAB_00baaaf0;
      }
    }
    param_1 = param_1 + 1;
    param_3 = param_3 + 1;
    pwVar1 = param_2;
  } while( true );
}

~~~
