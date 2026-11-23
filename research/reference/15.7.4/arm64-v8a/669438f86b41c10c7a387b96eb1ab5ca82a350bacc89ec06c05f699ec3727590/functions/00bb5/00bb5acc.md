# 00bb5acc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bb5a88`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb5/00bb5a88.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/97ee0756e9de6c746e3ce399/1-2/priority-0078.md#compare-411f40608cd00fa33a1cc29dbda9609b)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 構造資料不足
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

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
