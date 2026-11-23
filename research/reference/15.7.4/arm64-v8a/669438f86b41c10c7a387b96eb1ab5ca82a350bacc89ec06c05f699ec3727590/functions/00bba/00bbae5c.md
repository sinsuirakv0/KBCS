# 00bbae5c

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bbae18`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbae18.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/97ee0756e9de6c746e3ce399/1-2/high-0011.md#compare-8c9c18788f61437b73c01c200709e42d)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 構造資料不足
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbae5c",
  "name": "_ZNSt11logic_errorD1Ev",
  "size": 88,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "801e6e4b3b1a56ba8d9ddc5890ccfe0c2b35e4aa81b2b0bc3b0e21008b9233f5",
  "source_text_sha256": "801e6e4b3b1a56ba8d9ddc5890ccfe0c2b35e4aa81b2b0bc3b0e21008b9233f5"
}
~~~

## 呼び出し元

- [00bdb0b0](../00bdb/00bdb0b0.md)
- [00bdb250](../00bdb/00bdb250.md)
- [00be1130](../00be1/00be1130.md)
- [00be1210](../00be1/00be1210.md)
- [00be1e60](../00be1/00be1e60.md)
- [00be1e70](../00be1/00be1e70.md)

## 呼び出し先

- [00bd6e30](../00bd6/00bd6e30.md)
- [00bdb060](../00bdb/00bdb060.md)
- [00bdb490](../00bdb/00bdb490.md)

## 疑似コード / UTF-8 1548 bytes

~~~c

void _ZNSt11logic_errorD1Ev(long *param_1)

{
  int iVar1;
  long lVar2;
  
                    /* catch() { ... } // from try @ 00bb4d84 with catch @ 00bbae60 */
                    /* catch() { ... } // from try @ 00bb49a4 with catch @ 00bbae64 */
                    /* catch() { ... } // from try @ 00bb45e4 with catch @ 00bbae68 */
                    /* catch() { ... } // from try @ 00bb7cf4 with catch @ 00bbae6c */
                    /* catch() { ... } // from try @ 00bb9d34 with catch @ 00bbae70 */
                    /* catch() { ... } // from try @ 00bb996c with catch @ 00bbae74 */
                    /* catch() { ... } // from try @ 00bb9978 with catch @ 00bbae78 */
  lVar2 = param_1[1];
                    /* catch() { ... } // from try @ 00bb3640 with catch @ 00bbae7c */
  *param_1 = (long)(PTR__ZTVSt11logic_error_00c1bc60 + 0x10);
                    /* catch() { ... } // from try @ 00bb3584 with catch @ 00bbae8c */
  iVar1 = FUN_00bd6e30(0xffffffff,lVar2 + -8);
                    /* catch() { ... } // from try @ 00bb7c40 with catch @ 00bbae90 */
                    /* catch() { ... } // from try @ 00bb35ec with catch @ 00bbae94 */
  if (iVar1 + -1 < 0) {
                    /* catch() { ... } // from try @ 00bb3878 with catch @ 00bbae98 */
                    /* catch() { ... } // from try @ 00bb386c with catch @ 00bbae9c */
    _ZdlPv((void *)(lVar2 + -0x18));
  }
                    /* catch() { ... } // from try @ 00bb9d40 with catch @ 00bbaea4 */
  _ZNSt20bad_array_new_lengthD1Ev(param_1);
  return;
}

~~~
