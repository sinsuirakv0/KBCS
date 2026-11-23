# 00bbbebc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bbbdf4`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbb/00bbbdf4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/af8e2f5c5fc38f06774ff85c/0-1/high-0010.md#compare-3b1f84eabf155dd64ab9f697c72c793f)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 構造資料不足
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbbebc",
  "name": "FUN_00bbbebc",
  "size": 160,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "990dba8617a3ac3f718cd16b1e8b674585aa62bec85232c00bb0ad5d72ed4520",
  "source_text_sha256": "990dba8617a3ac3f718cd16b1e8b674585aa62bec85232c00bb0ad5d72ed4520"
}
~~~

## 呼び出し元

- [00bbbb0c](../00bbb/00bbbb0c.md)
- [00bbbdc8](../00bbb/00bbbdc8.md)

## 呼び出し先

- [00bdb770](../00bdb/00bdb770.md)

## 疑似コード / UTF-8 999 bytes

~~~c

bool FUN_00bbbebc(long param_1,long param_2)

{
  bool bVar1;
  long lVar2;
  
  if (param_2 != 0) {
                    /* try { // try from 00bbbef4 to 00cbbefb has its CatchHandler @ 00bbd38c */
    lVar2 = __dynamic_cast(param_2,PTR__ZTIN10__cxxabiv116__shim_type_infoE_00c1bff8,
                           PTR__ZTIN10__cxxabiv129__pointer_to_member_type_infoE_00c1c030,0);
    bVar1 = false;
    if (lVar2 != 0) {
                    /* try { // try from 00bbbf00 to 00cbbf0f has its CatchHandler @ 00bbd370 */
      if (((*(uint *)(lVar2 + 0x10) & (*(uint *)(param_1 + 0x10) ^ 0xffffffff)) == 0) &&
         (*(long *)(*(long *)(param_1 + 0x18) + 8) == *(long *)(*(long *)(lVar2 + 0x18) + 8))) {
        bVar1 = *(long *)(*(long *)(param_1 + 0x20) + 8) == *(long *)(*(long *)(lVar2 + 0x20) + 8);
      }
      else {
                    /* try { // try from 00bbbf24 to 00cbbf2b has its CatchHandler @ 00bbd1a8 */
        bVar1 = false;
      }
    }
    return bVar1;
  }
  return false;
}

~~~
