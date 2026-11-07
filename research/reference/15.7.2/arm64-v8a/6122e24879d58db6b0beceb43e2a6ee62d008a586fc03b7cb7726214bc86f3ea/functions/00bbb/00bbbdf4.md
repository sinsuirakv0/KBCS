# 00bbbdf4

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

<!-- kbcs-version-next -->
**別版の対応** [v15.7.4 `00bbbf00`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbbf00.md)
<!-- /kbcs-version-next -->

## 関数情報

~~~json
{
  "address": "00bbbdf4",
  "name": "FUN_00bbbdf4",
  "size": 160,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "df906d4277d9f9902da3146e7f277251c1d44a5e9dc305652ebfb6f1cc582ea7",
  "source_text_sha256": "df906d4277d9f9902da3146e7f277251c1d44a5e9dc305652ebfb6f1cc582ea7"
}
~~~

## 呼び出し元

- [00bbba44](../00bbb/00bbba44.md)
- [00bbbd00](../00bbb/00bbbd00.md)

## 呼び出し先

- [00bdb6c0](../00bdb/00bdb6c0.md)

## 疑似コード / UTF-8 999 bytes

~~~c

bool FUN_00bbbdf4(long param_1,long param_2)

{
  bool bVar1;
  long lVar2;
  
  if (param_2 != 0) {
                    /* try { // try from 00bbbe2c to 00cbbe33 has its CatchHandler @ 00bbd2c4 */
    lVar2 = __dynamic_cast(param_2,PTR__ZTIN10__cxxabiv116__shim_type_infoE_00c1bf48,
                           PTR__ZTIN10__cxxabiv129__pointer_to_member_type_infoE_00c1bf80,0);
    bVar1 = false;
    if (lVar2 != 0) {
                    /* try { // try from 00bbbe38 to 00cbbe47 has its CatchHandler @ 00bbd2a8 */
      if (((*(uint *)(lVar2 + 0x10) & (*(uint *)(param_1 + 0x10) ^ 0xffffffff)) == 0) &&
         (*(long *)(*(long *)(param_1 + 0x18) + 8) == *(long *)(*(long *)(lVar2 + 0x18) + 8))) {
        bVar1 = *(long *)(*(long *)(param_1 + 0x20) + 8) == *(long *)(*(long *)(lVar2 + 0x20) + 8);
      }
      else {
                    /* try { // try from 00bbbe5c to 00cbbe63 has its CatchHandler @ 00bbd0e0 */
        bVar1 = false;
      }
    }
    return bVar1;
  }
  return false;
}

~~~
