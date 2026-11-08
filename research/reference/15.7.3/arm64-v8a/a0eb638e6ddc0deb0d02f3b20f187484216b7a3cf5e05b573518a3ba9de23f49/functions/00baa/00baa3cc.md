# 00baa3cc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00baa3cc",
  "name": "_ZNSt6__ndk112ctype_bynameIcEC1ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEm",
  "size": 204,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "dce0723b5f271ed264b2bea923eb4843345530771ae4176d6a99ae75145db73c",
  "source_text_sha256": "dce0723b5f271ed264b2bea923eb4843345530771ae4176d6a99ae75145db73c"
}
~~~

## 呼び出し元

- [00be1800](../00be1/00be1800.md)
- [00be19a0](../00be1/00be19a0.md)

## 呼び出し先

- [00bd70ac](../00bd7/00bd70ac.md)
- [00bdb010](../00bdb/00bdb010.md)
- [00bdb210](../00bdb/00bdb210.md)
- [00be0f60](../00be0/00be0f60.md)
- [00be1520](../00be1/00be1520.md)
- [00be1970](../00be1/00be1970.md)

## 関連文字列（未確認候補）

~~~text
"ctype_byname<char>::ctype_byname failed to construct for "
~~~

## 疑似コード / UTF-8 1285 bytes

~~~c

void _ZNSt6__ndk112ctype_bynameIcEC1ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEm
               (long *param_1,byte *param_2,long param_3)

{
  undefined1 *puVar1;
  undefined *puVar2;
  __locale_t p_Var3;
  undefined8 uVar4;
  byte *__locale;
  byte local_38;
  undefined1 auStack_37 [15];
  undefined1 *local_28;
  
  param_1[2] = (long)&DAT_002fb120;
  puVar2 = PTR__ZTVNSt6__ndk112ctype_bynameIcEE_00c1bf50;
  *(undefined1 *)(param_1 + 3) = 0;
  *param_1 = (long)(puVar2 + 0x10);
  param_1[1] = param_3 + -1;
  __locale = *(byte **)(param_2 + 0x10);
  if ((*param_2 & 1) == 0) {
    __locale = param_2 + 1;
  }
  p_Var3 = newlocale(0x1fbf,(char *)__locale,(__locale_t)0x0);
  param_1[4] = (long)p_Var3;
  if (p_Var3 != (__locale_t)0x0) {
    return;
  }
  _ZNSt6__ndk1plIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EEPKS6_RKS9_
            (&local_38,"ctype_byname<char>::ctype_byname failed to construct for ",param_2);
  puVar1 = local_28;
  if ((local_38 & 1) == 0) {
    puVar1 = auStack_37;
  }
  uVar4 = _ZNSt6__ndk121__throw_runtime_errorEPKc(puVar1);
  if ((local_38 & 1) != 0) {
    _ZdlPv(local_28);
  }
  _ZNSt6__ndk15ctypeIcED2Ev(param_1);
                    /* WARNING: Subroutine does not return */
  FUN_00bd70ac(uVar4);
}

~~~
