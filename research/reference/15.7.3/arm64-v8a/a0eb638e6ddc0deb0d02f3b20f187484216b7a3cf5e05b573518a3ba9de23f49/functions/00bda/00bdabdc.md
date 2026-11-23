# 00bdabdc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bdab1c`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdab1c.md) · 移動量 `+0xc0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/af8e2f5c5fc38f06774ff85c/0-1/priority-0080.md#compare-6ad743562ae5ed670db46bfd55bb578f)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 構造資料不足
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdabdc",
  "name": "FUN_00bdabdc",
  "size": 252,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a25dac38b0b5bb107537cc0760f2f897fa833d9b7a36a8d62788d032f95494e2",
  "source_text_sha256": "a25dac38b0b5bb107537cc0760f2f897fa833d9b7a36a8d62788d032f95494e2"
}
~~~

## 呼び出し元

- [00bdaa74](../00bda/00bdaa74.md)

## 呼び出し先

- [00bdd310](../00bdd/00bdd310.md)
- [00bde270](../00bde/00bde270.md)
- [00be1f30](../00be1/00be1f30.md)

## 関連文字列（未確認候補）

~~~text
"Can't binary search on variable length encoded data."
"Unknown DWARF encoding for search table."
"getTableEntrySize"
"libunwind: %s - %s\n"
~~~

## 疑似コード / UTF-8 1989 bytes

~~~c

undefined8 FUN_00bdabdc(uint param_1)

{
  undefined *puVar1;
  
  puVar1 = PTR___sF_00c1bcf8;
  param_1 = param_1 & 0xf;
                    /* try { // try from 00bdabf4 to 00cdac43 has its CatchHandler @ 00bdabf4
                       catch() { ... } // from try @ 00bdabf4 with catch @ 00bdabf4
                       catch() { ... } // from try @ 00bdac98 with catch @ 00bdabf4 */
  if (param_1 < 9) {
    if (param_1 < 3) {
      if (param_1 == 2) {
        return 4;
      }
      if (param_1 == 1) {
LAB_00bdaca4:
                    /* try { // try from 00bdacc8 to 00cdacef has its CatchHandler @ 00bdacc8
                       catch() { ... } // from try @ 00bdacc8 with catch @ 00bdacc8
                       catch() { ... } // from try @ 00bdad28 with catch @ 00bdacc8 */
        fprintf((FILE *)(PTR___sF_00c1bcf8 + 0x130),"libunwind: %s - %s\n","getTableEntrySize",
                "Can\'t binary search on variable length encoded data.");
        fflush((FILE *)(puVar1 + 0x130));
                    /* WARNING: Subroutine does not return */
        abort();
      }
    }
    else {
      if (param_1 == 3) {
        return 8;
      }
      if (param_1 == 4) {
        return 0x10;
      }
    }
  }
  else if (param_1 < 0xb) {
                    /* catch() { ... } // from try @ 00bdac44 with catch @ 00bdac98
                       try { // try from 00bdac98 to 00cdacc7 has its CatchHandler @ 00bdabf4 */
    if (param_1 == 10) {
      return 4;
    }
    if (param_1 == 9) goto LAB_00bdaca4;
  }
  else {
    if (param_1 == 0xc) {
                    /* try { // try from 00bdac44 to 00cdac97 has its CatchHandler @ 00bdac98 */
      return 0x10;
    }
    if (param_1 == 0xb) {
      return 8;
    }
  }
  fprintf((FILE *)(PTR___sF_00c1bcf8 + 0x130),"libunwind: %s - %s\n","getTableEntrySize",
          "Unknown DWARF encoding for search table.");
  fflush((FILE *)(puVar1 + 0x130));
                    /* WARNING: Subroutine does not return */
  abort();
}

~~~
