# 00baabbc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

## 関数情報

~~~json
{
  "address": "00baabbc",
  "name": "_ZNKSt6__ndk112ctype_bynameIwE5do_isEPKwS3_Pm",
  "size": 412,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1602342f78134560b6bd598c68adf2a44bf617a9703ea765a79fc884e81dbc7d",
  "source_text_sha256": "1602342f78134560b6bd598c68adf2a44bf617a9703ea765a79fc884e81dbc7d"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00be19b0](../00be1/00be19b0.md)
- [00be1a50](../00be1/00be1a50.md)
- [00be1a60](../00be1/00be1a60.md)
- [00be1a70](../00be1/00be1a70.md)
- [00be1a80](../00be1/00be1a80.md)
- [00be1a90](../00be1/00be1a90.md)
- [00be1aa0](../00be1/00be1aa0.md)
- [00be1ab0](../00be1/00be1ab0.md)
- [00be1ac0](../00be1/00be1ac0.md)
- [00be1ad0](../00be1/00be1ad0.md)

## 疑似コード / UTF-8 1943 bytes

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
LAB_00baabfc:
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
        goto LAB_00baabfc;
      }
    }
    param_2 = param_2 + 1;
    param_4 = param_4 + 1;
    puVar1 = param_3;
  } while( true );
}

~~~
