# 00bb5acc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

## 関数情報

~~~json
{
  "address": "00bb5acc",
  "name": "_ZNSt6__ndk110__time_putC2ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
  "size": 156,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1d745c7a23b71a2781e486e1f315c346c39e55eebc7768dbc8fa8c5601ff80b9",
  "source_text_sha256": "1d745c7a23b71a2781e486e1f315c346c39e55eebc7768dbc8fa8c5601ff80b9"
}
~~~

## 呼び出し元

- [00be18c0](../00be1/00be18c0.md)

## 呼び出し先

- [00bd70ec](../00bd7/00bd70ec.md)
- [00bdb060](../00bdb/00bdb060.md)
- [00bdb260](../00bdb/00bdb260.md)
- [00be0fb0](../00be0/00be0fb0.md)
- [00be1570](../00be1/00be1570.md)

## 関連文字列（未確認候補）

~~~text
"time_put_byname failed to construct for "
~~~

## 疑似コード / UTF-8 1090 bytes

~~~c

void _ZNSt6__ndk110__time_putC2ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE
               (undefined8 *param_1,byte *param_2)

{
  undefined1 *puVar1;
  __locale_t p_Var2;
  undefined8 uVar3;
  byte *__locale;
  byte local_38;
  undefined1 auStack_37 [15];
  undefined1 *local_28;
  
  __locale = *(byte **)(param_2 + 0x10);
  if ((*param_2 & 1) == 0) {
    __locale = param_2 + 1;
  }
  p_Var2 = newlocale(0x1fbf,(char *)__locale,(__locale_t)0x0);
  *param_1 = p_Var2;
  if (p_Var2 != (__locale_t)0x0) {
                    /* try { // try from 00bb5b10 to 00cb5b17 has its CatchHandler @ 00bbacdc */
    return;
  }
  _ZNSt6__ndk1plIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EEPKS6_RKS9_
            (&local_38,"time_put_byname failed to construct for ",param_2);
  puVar1 = local_28;
  if ((local_38 & 1) == 0) {
    puVar1 = auStack_37;
  }
  uVar3 = _ZNSt6__ndk121__throw_runtime_errorEPKc(puVar1);
  if ((local_38 & 1) != 0) {
    _ZdlPv(local_28);
  }
                    /* WARNING: Subroutine does not return */
  FUN_00bd70ec(uVar3);
}

~~~
