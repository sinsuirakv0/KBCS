# 00bdac1c

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

ページ 1/1。[入口](00bdac1c.md)

## 関数情報

~~~json
{
  "address": "00bdac1c",
  "name": "FUN_00bdac1c",
  "size": 252,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "07e5efe3dd140e677898eb6008e03fa309d36baf715d7ef38206032e01432596",
  "source_text_sha256": "07e5efe3dd140e677898eb6008e03fa309d36baf715d7ef38206032e01432596"
}
~~~
## 呼び出し元

- [00bdaab4](../00bda/00bdaab4.md)

## 呼び出し先

- [00bdd360](../00bdd/00bdd360.md)
- [00bde2c0](../00bde/00bde2c0.md)
- [00be1f80](../00be1/00be1f80.md)

## 関連文字列（未確認候補）

~~~text
"Can't binary search on variable length encoded data."
"Unknown DWARF encoding for search table."
"getTableEntrySize"
"libunwind: %s - %s\n"
~~~
## 疑似コード 1/1 / UTF-8 1989 bytes

~~~c

undefined8 FUN_00bdac1c(uint param_1)

{
  undefined *puVar1;
  
  puVar1 = PTR___sF_00c1bd48;
  param_1 = param_1 & 0xf;
                    /* try { // try from 00bdac38 to 00cdac87 has its CatchHandler @ 00bdac38
                       catch() { ... } // from try @ 00bdac38 with catch @ 00bdac38
                       catch() { ... } // from try @ 00bdacdc with catch @ 00bdac38 */
  if (param_1 < 9) {
    if (param_1 < 3) {
      if (param_1 == 2) {
        return 4;
      }
      if (param_1 == 1) {
LAB_00bdace4:
        fprintf((FILE *)(PTR___sF_00c1bd48 + 0x130),"libunwind: %s - %s\n","getTableEntrySize",
                "Can\'t binary search on variable length encoded data.");
                    /* try { // try from 00bdad0c to 00cdad33 has its CatchHandler @ 00bdad0c
                       catch() { ... } // from try @ 00bdad0c with catch @ 00bdad0c
                       catch() { ... } // from try @ 00bdad6c with catch @ 00bdad0c */
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
    if (param_1 == 10) {
      return 4;
    }
                    /* catch() { ... } // from try @ 00bdac88 with catch @ 00bdacdc
                       try { // try from 00bdacdc to 00cdad0b has its CatchHandler @ 00bdac38 */
    if (param_1 == 9) goto LAB_00bdace4;
  }
  else {
    if (param_1 == 0xc) {
                    /* try { // try from 00bdac88 to 00cdacdb has its CatchHandler @ 00bdacdc */
      return 0x10;
    }
    if (param_1 == 0xb) {
      return 8;
    }
  }
  fprintf((FILE *)(PTR___sF_00c1bd48 + 0x130),"libunwind: %s - %s\n","getTableEntrySize",
          "Unknown DWARF encoding for search table.");
  fflush((FILE *)(puVar1 + 0x130));
                    /* WARNING: Subroutine does not return */
  abort();
}

~~~
