# 006fecac

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `006fecac`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006fe/006fecac.md) · 移動量 `+0x0`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/97ee0756e9de6c746e3ce399/1-2/no_difference_in_scope-0008.md#compare-09f6941e09e3a6b0489a3193d18148c7)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 構造資料不足
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "006fecac",
  "name": "FUN_006fecac",
  "size": 92,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1ea20d6be60f4f58a1c1be017f44d107fa6444c35ed7a1ff06f20ed0f05cc274",
  "source_text_sha256": "1ea20d6be60f4f58a1c1be017f44d107fa6444c35ed7a1ff06f20ed0f05cc274"
}
~~~

## 呼び出し元

- [00734830](../00734/00734830.md)
- [0073496c](../00734/0073496c.md)

## 呼び出し先

- [0081f580](../0081f/0081f580.md)

## 疑似コード / UTF-8 1114 bytes

~~~c

undefined4 FUN_006fecac(uint param_1)

{
  uint uVar1;
  long lVar2;
  long lVar3;
  
                    /* catch() { ... } // from try @ 006fe914 with catch @ 006fecac */
                    /* catch() { ... } // from try @ 006fe688 with catch @ 006fecb0 */
                    /* catch() { ... } // from try @ 006fea64 with catch @ 006fecb4
                       catch() { ... } // from try @ 006fec4c with catch @ 006fecb4 */
                    /* catch() { ... } // from try @ 006fea90 with catch @ 006fecbc */
  lVar2 = FUN_0081f580();
  lVar3 = FUN_0081f580();
                    /* catch() { ... } // from try @ 006fe9bc with catch @ 006feccc
                       catch() { ... } // from try @ 006fec34 with catch @ 006feccc */
                    /* catch() { ... } // from try @ 006fea04 with catch @ 006fecd4 */
  uVar1 = *(int *)(BYTE_ARRAY_00343241 + lVar3 + 0x23) + ~param_1 &
          ((int)(*(int *)(BYTE_ARRAY_00343241 + lVar3 + 0x23) + ~param_1) >> 0x1f ^ 0xffffffffU);
  if (0x1f2 < uVar1) {
    uVar1 = 499;
  }
  return *(undefined4 *)(&uleb128_00389fd0 + lVar2 + (ulong)uVar1 * 4);
}

~~~
