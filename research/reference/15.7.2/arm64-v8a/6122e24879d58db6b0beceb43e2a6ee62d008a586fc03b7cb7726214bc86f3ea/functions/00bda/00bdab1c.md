# 00bdab1c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bdab1c.md)

## 関数情報

~~~json
{
  "address": "00bdab1c",
  "name": "FUN_00bdab1c",
  "size": 252,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "871d4bfa4351b98c985566e041a842036fb84edab98b125bb026d7492407553f",
  "source_text_sha256": "871d4bfa4351b98c985566e041a842036fb84edab98b125bb026d7492407553f"
}
~~~
## 呼び出し元

- [00bda9b4](../00bda/00bda9b4.md)

## 呼び出し先

- [00bdd260](../00bdd/00bdd260.md)
- [00bde1c0](../00bde/00bde1c0.md)
- [00be1e80](../00be1/00be1e80.md)

## 関連文字列（未確認候補）

~~~text
"Can't binary search on variable length encoded data."
"Unknown DWARF encoding for search table."
"getTableEntrySize"
"libunwind: %s - %s\n"
~~~
## 疑似コード 1/1 / UTF-8 2050 bytes

~~~c

undefined8 FUN_00bdab1c(uint param_1)

{
  undefined *puVar1;
  
  puVar1 = PTR___sF_00c1bc48;
                    /* try { // try from 00bdab2c to 00cdab7b has its CatchHandler @ 00bdab2c
                       catch() { ... } // from try @ 00bdab2c with catch @ 00bdab2c
                       catch() { ... } // from try @ 00bdabd0 with catch @ 00bdab2c */
  param_1 = param_1 & 0xf;
  if (param_1 < 9) {
    if (param_1 < 3) {
      if (param_1 == 2) {
        return 4;
      }
      if (param_1 == 1) {
LAB_00bdabe4:
                    /* try { // try from 00bdac00 to 00cdac27 has its CatchHandler @ 00bdac00
                       catch() { ... } // from try @ 00bdac00 with catch @ 00bdac00
                       catch() { ... } // from try @ 00bdac60 with catch @ 00bdac00 */
        fprintf((FILE *)(PTR___sF_00c1bc48 + 0x130),"libunwind: %s - %s\n","getTableEntrySize",
                "Can\'t binary search on variable length encoded data.");
        fflush((FILE *)(puVar1 + 0x130));
                    /* WARNING: Subroutine does not return */
        abort();
      }
    }
    else {
      if (param_1 == 3) {
                    /* try { // try from 00bdab7c to 00cdabcf has its CatchHandler @ 00bdabd0 */
        return 8;
      }
      if (param_1 == 4) {
        return 0x10;
      }
    }
  }
  else if (param_1 < 0xb) {
    if (param_1 == 10) {
      return 4;
    }
    if (param_1 == 9) goto LAB_00bdabe4;
  }
  else {
    if (param_1 == 0xc) {
      return 0x10;
    }
    if (param_1 == 0xb) {
      return 8;
    }
  }
  fprintf((FILE *)(PTR___sF_00c1bc48 + 0x130),"libunwind: %s - %s\n","getTableEntrySize",
          "Unknown DWARF encoding for search table.");
                    /* catch() { ... } // from try @ 00bdab7c with catch @ 00bdabd0
                       try { // try from 00bdabd0 to 00cdabff has its CatchHandler @ 00bdab2c */
  fflush((FILE *)(puVar1 + 0x130));
                    /* WARNING: Subroutine does not return */
  abort();
}

~~~
