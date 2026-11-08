# 00bdabdc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

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
