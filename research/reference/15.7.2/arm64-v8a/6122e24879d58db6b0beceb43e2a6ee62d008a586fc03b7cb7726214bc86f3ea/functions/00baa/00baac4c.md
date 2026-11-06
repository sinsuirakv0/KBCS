# 00baac4c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

## 関数情報

~~~json
{
  "address": "00baac4c",
  "name": "_ZNKSt6__ndk112ctype_bynameIwE10do_scan_isEmPKwS3_",
  "size": 304,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ec36b9e5437f80e35fc8decf13489e52bc7ffe01ade2ba60edce1f707635addc",
  "source_text_sha256": "ec36b9e5437f80e35fc8decf13489e52bc7ffe01ade2ba60edce1f707635addc"
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

## 疑似コード / UTF-8 1787 bytes

~~~c

wint_t * _ZNKSt6__ndk112ctype_bynameIwE10do_scan_isEmPKwS3_
                   (long param_1,uint param_2,wint_t *param_3,wint_t *param_4)

{
  wint_t __wc;
  int iVar1;
  
  if (param_3 != param_4) {
    while (((((__wc = *param_3, (param_2 & 1) == 0 ||
              (iVar1 = iswspace_l(__wc,*(__locale_t *)(param_1 + 0x10)), iVar1 == 0)) &&
             (((param_2 >> 1 & 1) == 0 ||
              (iVar1 = iswprint_l(__wc,*(__locale_t *)(param_1 + 0x10)), iVar1 == 0)))) &&
            (((param_2 >> 2 & 1) == 0 ||
             (iVar1 = iswcntrl_l(__wc,*(__locale_t *)(param_1 + 0x10)), iVar1 == 0)))) &&
           (((param_2 >> 3 & 1) == 0 ||
            (iVar1 = iswupper_l(__wc,*(__locale_t *)(param_1 + 0x10)), iVar1 == 0))))) {
      if (((param_2 >> 4 & 1) != 0) &&
         (iVar1 = iswlower_l(__wc,*(__locale_t *)(param_1 + 0x10)), iVar1 != 0)) {
        return param_3;
      }
      if (((param_2 >> 5 & 1) != 0) &&
         (iVar1 = iswalpha_l(__wc,*(__locale_t *)(param_1 + 0x10)), iVar1 != 0)) {
        return param_3;
      }
      if (((param_2 >> 6 & 1) != 0) &&
         (iVar1 = iswdigit_l(__wc,*(__locale_t *)(param_1 + 0x10)), iVar1 != 0)) {
        return param_3;
      }
      if (((param_2 >> 7 & 1) != 0) &&
         (iVar1 = iswpunct_l(__wc,*(__locale_t *)(param_1 + 0x10)), iVar1 != 0)) {
        return param_3;
      }
      if (((param_2 >> 8 & 1) != 0) &&
         (iVar1 = iswxdigit_l(__wc,*(__locale_t *)(param_1 + 0x10)), iVar1 != 0)) {
        return param_3;
      }
      if (((param_2 >> 9 & 1) != 0) &&
         (iVar1 = iswblank_l(__wc,*(__locale_t *)(param_1 + 0x10)), iVar1 != 0)) {
        return param_3;
      }
      param_3 = param_3 + 1;
      if (param_3 == param_4) {
        return param_4;
      }
    }
  }
  return param_3;
}

~~~
