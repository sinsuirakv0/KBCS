# 00bbbfa0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bbbf5c`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbbf5c.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/97ee0756e9de6c746e3ce399/1-2/priority-0078.md#compare-91c8a77b823f33b29b3df49f95249431)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 構造資料不足
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbbfa0",
  "name": "FUN_00bbbfa0",
  "size": 364,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "bd9a0a1165ef10735d581cb3ed1cecff9bb2889c2e4600235bbf92f4ebb07887",
  "source_text_sha256": "bd9a0a1165ef10735d581cb3ed1cecff9bb2889c2e4600235bbf92f4ebb07887"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb7c0](../00bdb/00bdb7c0.md)
- [00bde9d0](../00bde/00bde9d0.md)

## 疑似コード / UTF-8 2451 bytes

~~~c

bool FUN_00bbbfa0(long param_1,long param_2,undefined8 *param_3)

{
  uint uVar1;
  int iVar2;
  long lVar3;
  undefined *puVar4;
  char *__s2;
  
                    /* try { // try from 00bbbfa8 to 00cbbfb3 has its CatchHandler @ 00bbd1e8 */
                    /* try { // try from 00bbbfb4 to 00cbbfc3 has its CatchHandler @ 00bbd1d4 */
  __s2 = *(char **)(param_2 + 8);
                    /* try { // try from 00bbbfc4 to 00cbbfd7 has its CatchHandler @ 00bbd1bc */
  if (__s2 == PTR__ZTSDn_00c1c060) {
    if ((*(long *)(param_1 + 0x18) == 0) ||
       (lVar3 = __dynamic_cast(*(long *)(param_1 + 0x18),
                               PTR__ZTIN10__cxxabiv116__shim_type_infoE_00c1c048,
                               PTR__ZTIN10__cxxabiv120__function_type_infoE_00c1c078,0), lVar3 == 0)
       ) {
                    /* try { // try from 00bbc0d0 to 00cbc0df has its CatchHandler @ 00bbd42c */
      puVar4 = &DAT_002fc9b8;
    }
    else {
      puVar4 = &DAT_002fc9a8;
    }
    *param_3 = puVar4;
    return true;
  }
  uVar1 = *(uint *)(param_1 + 0x10);
  if ((uVar1 & 0x18) == 0) {
    lVar3 = __dynamic_cast(param_2,PTR__ZTIN10__cxxabiv116__shim_type_infoE_00c1c048,
                           PTR__ZTIN10__cxxabiv117__pbase_type_infoE_00c1c058,0);
    if (lVar3 == 0) goto LAB_00bbc070;
    if ((*(byte *)(lVar3 + 0x10) & 0x18) == 0) {
      if (*(char **)(param_1 + 8) == __s2) {
        return true;
      }
      goto LAB_00bbc070;
    }
  }
  if ((param_1 == param_2) || (iVar2 = strcmp(*(char **)(param_1 + 8),__s2), iVar2 == 0)) {
    return true;
  }
LAB_00bbc070:
  lVar3 = __dynamic_cast(param_2,PTR__ZTIN10__cxxabiv116__shim_type_infoE_00c1c048,
                         PTR__ZTIN10__cxxabiv129__pointer_to_member_type_infoE_00c1c080,0);
  if (lVar3 == 0) {
    return false;
  }
                    /* try { // try from 00bbc094 to 00cbc09f has its CatchHandler @ 00bbd3b8 */
  if ((((*(uint *)(lVar3 + 0x10) & (uVar1 ^ 0xffffffff) & 7) == 0) &&
      ((uVar1 & (*(uint *)(lVar3 + 0x10) ^ 0xffffffff) & 0x60) == 0)) &&
     (*(long *)(*(long *)(param_1 + 0x18) + 8) == *(long *)(*(long *)(lVar3 + 0x18) + 8))) {
                    /* try { // try from 00bbc0f4 to 00cbc0fb has its CatchHandler @ 00bbd32c */
                    /* try { // try from 00bbc0fc to 00cbc103 has its CatchHandler @ 00bbd1b8 */
    return *(long *)(*(long *)(param_1 + 0x20) + 8) == *(long *)(*(long *)(lVar3 + 0x20) + 8);
  }
  return false;
}

~~~
