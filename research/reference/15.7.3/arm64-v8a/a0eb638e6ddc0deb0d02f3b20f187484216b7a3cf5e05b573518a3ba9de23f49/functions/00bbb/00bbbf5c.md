# 00bbbf5c

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bbbe94`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbb/00bbbe94.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/af8e2f5c5fc38f06774ff85c/0-1/priority-0078.md#compare-8340ce8479ec6e2134df1e28dd611903)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 構造資料不足
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbbf5c",
  "name": "FUN_00bbbf5c",
  "size": 364,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7a2e0bbe7055dfcf1067c2df772e817161422077e9ac045c428b5aacce6d9d0b",
  "source_text_sha256": "7a2e0bbe7055dfcf1067c2df772e817161422077e9ac045c428b5aacce6d9d0b"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb770](../00bdb/00bdb770.md)
- [00bde980](../00bde/00bde980.md)

## 疑似コード / UTF-8 2451 bytes

~~~c

bool FUN_00bbbf5c(long param_1,long param_2,undefined8 *param_3)

{
  uint uVar1;
  int iVar2;
  long lVar3;
  undefined *puVar4;
  char *__s2;
  
                    /* try { // try from 00bbbf64 to 00cbbf6f has its CatchHandler @ 00bbd1a4 */
                    /* try { // try from 00bbbf70 to 00cbbf7f has its CatchHandler @ 00bbd190 */
  __s2 = *(char **)(param_2 + 8);
                    /* try { // try from 00bbbf80 to 00cbbf93 has its CatchHandler @ 00bbd178 */
  if (__s2 == PTR__ZTSDn_00c1c010) {
    if ((*(long *)(param_1 + 0x18) == 0) ||
       (lVar3 = __dynamic_cast(*(long *)(param_1 + 0x18),
                               PTR__ZTIN10__cxxabiv116__shim_type_infoE_00c1bff8,
                               PTR__ZTIN10__cxxabiv120__function_type_infoE_00c1c028,0), lVar3 == 0)
       ) {
                    /* try { // try from 00bbc08c to 00cbc09b has its CatchHandler @ 00bbd3e8 */
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
    lVar3 = __dynamic_cast(param_2,PTR__ZTIN10__cxxabiv116__shim_type_infoE_00c1bff8,
                           PTR__ZTIN10__cxxabiv117__pbase_type_infoE_00c1c008,0);
    if (lVar3 == 0) goto LAB_00bbc02c;
    if ((*(byte *)(lVar3 + 0x10) & 0x18) == 0) {
      if (*(char **)(param_1 + 8) == __s2) {
        return true;
      }
      goto LAB_00bbc02c;
    }
  }
  if ((param_1 == param_2) || (iVar2 = strcmp(*(char **)(param_1 + 8),__s2), iVar2 == 0)) {
    return true;
  }
LAB_00bbc02c:
  lVar3 = __dynamic_cast(param_2,PTR__ZTIN10__cxxabiv116__shim_type_infoE_00c1bff8,
                         PTR__ZTIN10__cxxabiv129__pointer_to_member_type_infoE_00c1c030,0);
  if (lVar3 == 0) {
    return false;
  }
                    /* try { // try from 00bbc050 to 00cbc05b has its CatchHandler @ 00bbd374 */
  if ((((*(uint *)(lVar3 + 0x10) & (uVar1 ^ 0xffffffff) & 7) == 0) &&
      ((uVar1 & (*(uint *)(lVar3 + 0x10) ^ 0xffffffff) & 0x60) == 0)) &&
     (*(long *)(*(long *)(param_1 + 0x18) + 8) == *(long *)(*(long *)(lVar3 + 0x18) + 8))) {
                    /* try { // try from 00bbc0b0 to 00cbc0b7 has its CatchHandler @ 00bbd2e8 */
                    /* try { // try from 00bbc0b8 to 00cbc0bf has its CatchHandler @ 00bbd174 */
    return *(long *)(*(long *)(param_1 + 0x20) + 8) == *(long *)(*(long *)(lVar3 + 0x20) + 8);
  }
  return false;
}

~~~
