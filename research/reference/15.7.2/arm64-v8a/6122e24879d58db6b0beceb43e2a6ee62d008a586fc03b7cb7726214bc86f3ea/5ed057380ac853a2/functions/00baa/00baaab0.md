# 00baaab0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00baaab0.md)

## 関数情報

~~~json
{
  "address": "00baaab0",
  "name": "_ZNKSt6__ndk112ctype_bynameIwE5do_isEPKwS3_Pm",
  "size": 412,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7c15fb5a32a1181b30a46ed4089f889256ee6d61994fe526164e718937eb2708",
  "source_text_sha256": "7c15fb5a32a1181b30a46ed4089f889256ee6d61994fe526164e718937eb2708"
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

## 疑似コード 1/1 / UTF-8 1943 bytes

~~~c

uint * _ZNKSt6__ndk112ctype_bynameIwE5do_isEPKwS3_Pm
                 (long param_1,uint *param_2,uint *param_3,ulong *param_4)

{
  uint __wc;
  uint *puVar1;
  int iVar2;
  __locale_t __locale;
  ulong uVar3;
  
  puVar1 = param_2;
  do {
    if (param_2 == param_3) {
      return puVar1;
    }
    __wc = *param_2;
    if (__wc < 0x80) {
      uVar3 = *(ulong *)(&DAT_002fb120 + (ulong)__wc * 8);
LAB_00baaaf0:
      *param_4 = uVar3;
    }
    else {
      __locale = *(__locale_t *)(param_1 + 0x10);
      *param_4 = 0;
      iVar2 = iswspace_l(__wc,__locale);
      if (iVar2 != 0) {
        *param_4 = *param_4 | 1;
      }
      iVar2 = iswprint_l(__wc,*(__locale_t *)(param_1 + 0x10));
      if (iVar2 != 0) {
        *param_4 = *param_4 | 2;
      }
      iVar2 = iswcntrl_l(__wc,*(__locale_t *)(param_1 + 0x10));
      if (iVar2 != 0) {
        *param_4 = *param_4 | 4;
      }
      iVar2 = iswupper_l(__wc,*(__locale_t *)(param_1 + 0x10));
      if (iVar2 != 0) {
        *param_4 = *param_4 | 8;
      }
      iVar2 = iswlower_l(__wc,*(__locale_t *)(param_1 + 0x10));
      if (iVar2 != 0) {
        *param_4 = *param_4 | 0x10;
      }
      iVar2 = iswalpha_l(__wc,*(__locale_t *)(param_1 + 0x10));
      if (iVar2 != 0) {
        *param_4 = *param_4 | 0x20;
      }
      iVar2 = iswdigit_l(__wc,*(__locale_t *)(param_1 + 0x10));
      if (iVar2 != 0) {
        *param_4 = *param_4 | 0x40;
      }
      iVar2 = iswpunct_l(__wc,*(__locale_t *)(param_1 + 0x10));
      if (iVar2 != 0) {
        *param_4 = *param_4 | 0x80;
      }
      iVar2 = iswxdigit_l(__wc,*(__locale_t *)(param_1 + 0x10));
      if (iVar2 != 0) {
        *param_4 = *param_4 | 0x100;
      }
      iVar2 = iswblank_l(__wc,*(__locale_t *)(param_1 + 0x10));
      if (iVar2 != 0) {
        uVar3 = *param_4 | 0x200;
        goto LAB_00baaaf0;
      }
    }
    param_2 = param_2 + 1;
    param_4 = param_4 + 1;
    puVar1 = param_3;
  } while( true );
}

~~~
