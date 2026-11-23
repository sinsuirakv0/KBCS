# 00bbbe0c

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bbbdc8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbbdc8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/97ee0756e9de6c746e3ce399/1-2/priority-0078.md#compare-d209222d6d6441168c05e7571dee1561)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 構造資料不足
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbbe0c",
  "name": "FUN_00bbbe0c",
  "size": 244,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "97e55b9bb733a0587a8602cb3fd49961dc308f1eb225d9a7822ca891104bebe6",
  "source_text_sha256": "97e55b9bb733a0587a8602cb3fd49961dc308f1eb225d9a7822ca891104bebe6"
}
~~~

## 呼び出し元

- [00bbbb50](../00bbb/00bbbb50.md)

## 呼び出し先

- [00bbbf00](../00bbb/00bbbf00.md)
- [00bdb7c0](../00bdb/00bdb7c0.md)

## 疑似コード / UTF-8 1347 bytes

~~~c

undefined8 FUN_00bbbe0c(long param_1,long param_2)

{
  undefined *puVar1;
  undefined *puVar2;
  long lVar3;
  undefined8 uVar4;
  long lVar5;
  
  puVar2 = PTR__ZTIN10__cxxabiv119__pointer_type_infoE_00c1c068;
  puVar1 = PTR__ZTIN10__cxxabiv116__shim_type_infoE_00c1c048;
  while( true ) {
    if (param_2 == 0) {
      return 0;
    }
    lVar3 = __dynamic_cast(param_2,puVar1,puVar2,0);
    if (lVar3 == 0) {
      return 0;
    }
    if ((*(uint *)(lVar3 + 0x10) & (*(uint *)(param_1 + 0x10) ^ 0xffffffff)) != 0) {
      return 0;
    }
    lVar5 = *(long *)(param_1 + 0x18);
    param_2 = *(long *)(lVar3 + 0x18);
    if (*(long *)(lVar5 + 8) == *(long *)(param_2 + 8)) break;
    if ((*(uint *)(param_1 + 0x10) & 1) == 0) {
      return 0;
    }
    param_1 = __dynamic_cast(lVar5,puVar1,puVar2,0);
    if (param_1 == 0) {
      lVar3 = __dynamic_cast(lVar5,PTR__ZTIN10__cxxabiv116__shim_type_infoE_00c1c048,
                             PTR__ZTIN10__cxxabiv129__pointer_to_member_type_infoE_00c1c080,0);
                    /* try { // try from 00bbbebc to 00cbbec3 has its CatchHandler @ 00bbd32c */
      if (lVar3 != 0) {
        uVar4 = FUN_00bbbf00(lVar3,param_2);
        return uVar4;
      }
                    /* try { // try from 00bbbeec to 00cbbeff has its CatchHandler @ 00bbd1f0 */
      return 0;
    }
  }
  return 1;
}

~~~
