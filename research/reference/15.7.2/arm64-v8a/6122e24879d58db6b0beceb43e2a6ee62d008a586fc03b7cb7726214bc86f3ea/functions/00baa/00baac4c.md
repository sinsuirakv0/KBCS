# 00baac4c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00baac4c.md)

## 関数情報

~~~json
{
  "address": "00baac4c",
  "name": "std::__ndk1::ctype_byname<wchar_t>::do_scan_is",
  "size": 304,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ad75e063179d75d773910764e7772388f96d21d2a931cd9ecbbaf10965e31a21",
  "source_text_sha256": "ad75e063179d75d773910764e7772388f96d21d2a931cd9ecbbaf10965e31a21"
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

## 疑似コード 1/1 / UTF-8 1984 bytes

~~~c

/* std::__ndk1::ctype_byname<wchar_t>::do_scan_is(unsigned long, wchar_t const*, wchar_t const*)
   const */

wchar_t * __thiscall
std::__ndk1::ctype_byname<wchar_t>::do_scan_is
          (ctype_byname<wchar_t> *this,ulong param_1,wchar_t *param_2,wchar_t *param_3)

{
  wchar_t __wc;
  int iVar1;
  uint uVar2;
  
  if (param_2 != param_3) {
    while( true ) {
      __wc = *param_2;
      uVar2 = (uint)param_1;
      if ((((((param_1 & 1) != 0) &&
            (iVar1 = iswspace_l(__wc,*(__locale_t *)(this + 0x10)), iVar1 != 0)) ||
           (((uVar2 >> 1 & 1) != 0 &&
            (iVar1 = iswprint_l(__wc,*(__locale_t *)(this + 0x10)), iVar1 != 0)))) ||
          (((uVar2 >> 2 & 1) != 0 &&
           (iVar1 = iswcntrl_l(__wc,*(__locale_t *)(this + 0x10)), iVar1 != 0)))) ||
         (((uVar2 >> 3 & 1) != 0 &&
          (iVar1 = iswupper_l(__wc,*(__locale_t *)(this + 0x10)), iVar1 != 0)))) break;
      if (((uVar2 >> 4 & 1) != 0) &&
         (iVar1 = iswlower_l(__wc,*(__locale_t *)(this + 0x10)), iVar1 != 0)) {
        return param_2;
      }
      if (((uVar2 >> 5 & 1) != 0) &&
         (iVar1 = iswalpha_l(__wc,*(__locale_t *)(this + 0x10)), iVar1 != 0)) {
        return param_2;
      }
      if (((uVar2 >> 6 & 1) != 0) &&
         (iVar1 = iswdigit_l(__wc,*(__locale_t *)(this + 0x10)), iVar1 != 0)) {
        return param_2;
      }
      if (((uVar2 >> 7 & 1) != 0) &&
         (iVar1 = iswpunct_l(__wc,*(__locale_t *)(this + 0x10)), iVar1 != 0)) {
        return param_2;
      }
      if (((uVar2 >> 8 & 1) != 0) &&
         (iVar1 = iswxdigit_l(__wc,*(__locale_t *)(this + 0x10)), iVar1 != 0)) {
        return param_2;
      }
      if (((uVar2 >> 9 & 1) != 0) &&
         (iVar1 = iswblank_l(__wc,*(__locale_t *)(this + 0x10)), iVar1 != 0)) {
        return param_2;
      }
      param_2 = param_2 + 1;
      if (param_2 == param_3) {
        return param_3;
      }
    }
  }
  return param_2;
}

~~~
