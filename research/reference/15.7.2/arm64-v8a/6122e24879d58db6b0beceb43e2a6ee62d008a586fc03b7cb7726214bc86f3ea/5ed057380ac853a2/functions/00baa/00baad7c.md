# 00baad7c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00baad7c.md)

## 関数情報

~~~json
{
  "address": "00baad7c",
  "name": "_ZNKSt6__ndk112ctype_bynameIwE11do_scan_notEmPKwS3_",
  "size": 304,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1ff1555b2d0e6bdbf31263f14273c38637eab87cbcc102862f2f52f8b387ed85",
  "source_text_sha256": "1ff1555b2d0e6bdbf31263f14273c38637eab87cbcc102862f2f52f8b387ed85"
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

## 疑似コード 1/1 / UTF-8 1671 bytes

~~~c

wint_t * _ZNKSt6__ndk112ctype_bynameIwE11do_scan_notEmPKwS3_
                   (long param_1,uint param_2,wint_t *param_3,wint_t *param_4)

{
  wint_t __wc;
  int iVar1;
  wint_t *pwVar2;
  
  pwVar2 = param_3;
  while ((param_3 != param_4 &&
         (((((__wc = *param_3, (param_2 & 1) != 0 &&
             (iVar1 = iswspace_l(__wc,*(__locale_t *)(param_1 + 0x10)), iVar1 != 0)) ||
            (((param_2 >> 1 & 1) != 0 &&
             (iVar1 = iswprint_l(__wc,*(__locale_t *)(param_1 + 0x10)), iVar1 != 0)))) ||
           (((((param_2 >> 2 & 1) != 0 &&
              (iVar1 = iswcntrl_l(__wc,*(__locale_t *)(param_1 + 0x10)), iVar1 != 0)) ||
             (((param_2 >> 3 & 1) != 0 &&
              (iVar1 = iswupper_l(__wc,*(__locale_t *)(param_1 + 0x10)), iVar1 != 0)))) ||
            (((((param_2 >> 4 & 1) != 0 &&
               (iVar1 = iswlower_l(__wc,*(__locale_t *)(param_1 + 0x10)), iVar1 != 0)) ||
              (((param_2 >> 5 & 1) != 0 &&
               (iVar1 = iswalpha_l(__wc,*(__locale_t *)(param_1 + 0x10)), iVar1 != 0)))) ||
             (((param_2 >> 6 & 1) != 0 &&
              (iVar1 = iswdigit_l(__wc,*(__locale_t *)(param_1 + 0x10)), iVar1 != 0)))))))) ||
          ((((param_2 >> 7 & 1) != 0 &&
            (iVar1 = iswpunct_l(__wc,*(__locale_t *)(param_1 + 0x10)), iVar1 != 0)) ||
           ((((param_2 >> 8 & 1) != 0 &&
             (iVar1 = iswxdigit_l(__wc,*(__locale_t *)(param_1 + 0x10)), iVar1 != 0)) ||
            ((pwVar2 = param_3, (param_2 >> 9 & 1) != 0 &&
             (iVar1 = iswblank_l(__wc,*(__locale_t *)(param_1 + 0x10)), iVar1 != 0))))))))))) {
    param_3 = param_3 + 1;
    pwVar2 = param_4;
  }
  return pwVar2;
}

~~~
