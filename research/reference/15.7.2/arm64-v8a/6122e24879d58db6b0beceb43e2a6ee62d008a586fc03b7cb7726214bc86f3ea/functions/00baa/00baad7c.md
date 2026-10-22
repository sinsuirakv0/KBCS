# 00baad7c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00baad7c.md)

## 関数情報

~~~json
{
  "address": "00baad7c",
  "name": "std::__ndk1::ctype_byname<wchar_t>::do_scan_not",
  "size": 304,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d1879e1c8b8b1f80e37d003342dbc04f49b5379cdacb033bf7106bc4f09396c4",
  "source_text_sha256": "d1879e1c8b8b1f80e37d003342dbc04f49b5379cdacb033bf7106bc4f09396c4"
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

## 疑似コード 1/1 / UTF-8 1865 bytes

~~~c

/* std::__ndk1::ctype_byname<wchar_t>::do_scan_not(unsigned long, wchar_t const*, wchar_t const*)
   const */

wchar_t * __thiscall
std::__ndk1::ctype_byname<wchar_t>::do_scan_not
          (ctype_byname<wchar_t> *this,ulong param_1,wchar_t *param_2,wchar_t *param_3)

{
  wchar_t __wc;
  wchar_t *pwVar1;
  int iVar2;
  uint uVar3;
  
  pwVar1 = param_2;
  do {
    if (param_2 == param_3) {
      return pwVar1;
    }
    __wc = *param_2;
    uVar3 = (uint)param_1;
    if (((((((param_1 & 1) == 0) ||
           (iVar2 = iswspace_l(__wc,*(__locale_t *)(this + 0x10)), iVar2 == 0)) &&
          (((uVar3 >> 1 & 1) == 0 ||
           (iVar2 = iswprint_l(__wc,*(__locale_t *)(this + 0x10)), iVar2 == 0)))) &&
         (((uVar3 >> 2 & 1) == 0 ||
          (iVar2 = iswcntrl_l(__wc,*(__locale_t *)(this + 0x10)), iVar2 == 0)))) &&
        (((uVar3 >> 3 & 1) == 0 ||
         (iVar2 = iswupper_l(__wc,*(__locale_t *)(this + 0x10)), iVar2 == 0)))) &&
       ((((((uVar3 >> 4 & 1) == 0 ||
           (iVar2 = iswlower_l(__wc,*(__locale_t *)(this + 0x10)), iVar2 == 0)) &&
          (((uVar3 >> 5 & 1) == 0 ||
           (iVar2 = iswalpha_l(__wc,*(__locale_t *)(this + 0x10)), iVar2 == 0)))) &&
         (((uVar3 >> 6 & 1) == 0 ||
          (iVar2 = iswdigit_l(__wc,*(__locale_t *)(this + 0x10)), iVar2 == 0)))) &&
        ((((uVar3 >> 7 & 1) == 0 ||
          (iVar2 = iswpunct_l(__wc,*(__locale_t *)(this + 0x10)), iVar2 == 0)) &&
         (((uVar3 >> 8 & 1) == 0 ||
          (iVar2 = iswxdigit_l(__wc,*(__locale_t *)(this + 0x10)), iVar2 == 0)))))))) {
      if ((uVar3 >> 9 & 1) == 0) {
        return param_2;
      }
      iVar2 = iswblank_l(__wc,*(__locale_t *)(this + 0x10));
      if (iVar2 == 0) {
        return param_2;
      }
    }
    param_2 = param_2 + 1;
    pwVar1 = param_3;
  } while( true );
}

~~~
