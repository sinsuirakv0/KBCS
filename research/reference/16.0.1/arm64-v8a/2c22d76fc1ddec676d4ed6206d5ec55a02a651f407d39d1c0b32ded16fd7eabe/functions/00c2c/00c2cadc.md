# 00c2cadc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00c2cadc",
  "name": "FUN_00c2cadc",
  "size": 1080,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "020e6a385ab5f902b8fd23c87f5c382ed20364eb8c5e69784bc6c3d728e9890e",
  "source_text_sha256": "020e6a385ab5f902b8fd23c87f5c382ed20364eb8c5e69784bc6c3d728e9890e"
}
~~~

## 呼び出し元

- [00c2ca70](../00c2c/00c2ca70.md)

## 呼び出し先

- [00c57e30](../00c57/00c57e30.md)
- [00c57e50](../00c57/00c57e50.md)
- [00c57e70](../00c57/00c57e70.md)

## 関連文字列（未確認候補）

~~~text
"Wednesday"
~~~

## 疑似コード / UTF-8 6936 bytes

~~~c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_00c2cadc(void)

{
  undefined8 uVar1;
  int iVar2;
  char *pcVar3;
  undefined8 *puVar4;
  undefined4 *puVar5;
  
                    /* try { // try from 00c2caf4 to 00d2caff has its CatchHandler @ 00c2ccd4 */
  if (((DAT_011280f8 & 1) == 0) && (iVar2 = __cxa_guard_acquire(&DAT_011280f8), iVar2 != 0)) {
    __cxa_atexit(FUN_00c35ba0,0,&PTR_LOOP_00c62f90);
    __cxa_guard_release(&DAT_011280f8);
  }
  if ((DAT_01127fa8 & 1) == 0) {
    DAT_01127fa8 = 0xc;
    puVar5 = &DAT_01127fa9;
  }
  else {
    DAT_01127fb0 = 6;
    puVar5 = DAT_01127fb8;
  }
  *(undefined1 *)((long)puVar5 + 6) = 0;
  *(undefined2 *)(puVar5 + 1) = 0x7961;
  *puVar5 = 0x646e7553;
  if ((DAT_01127fc0 & 1) == 0) {
    DAT_01127fc0 = 0xc;
    puVar5 = &DAT_01127fc1;
  }
  else {
    DAT_01127fc8 = 6;
    puVar5 = DAT_01127fd0;
  }
  *(undefined1 *)((long)puVar5 + 6) = 0;
  *(undefined2 *)(puVar5 + 1) = 0x7961;
  *puVar5 = 0x646e6f4d;
  if ((DAT_01127fd8 & 1) == 0) {
                    /* try { // try from 00c2cba8 to 00d2cbab has its CatchHandler @ 00c2cd90 */
    DAT_01127fd8 = 0xe;
    puVar5 = &DAT_01127fd9;
  }
  else {
    DAT_01127fe0 = 7;
    puVar5 = DAT_01127fe8;
  }
  *(undefined1 *)((long)puVar5 + 7) = 0;
                    /* try { // try from 00c2cbd4 to 00d2cbdf has its CatchHandler @ 00c2ccb0 */
  *(undefined4 *)((long)puVar5 + 3) = 0x79616473;
                    /* try { // try from 00c2cbe0 to 00d2cbeb has its CatchHandler @ 00c2cc98 */
  *puVar5 = 0x73657554;
  uVar1 = s_Wednesday_002b8d72._0_8_;
  if ((DAT_01127ff0 & 1) == 0) {
    DAT_01127ff0 = 0x12;
    pcVar3 = (char *)&DAT_01127ff1;
  }
  else {
    ram0x01127ff8 = 9;
    pcVar3 = DAT_01128000;
  }
  pcVar3[8] = 'y';
  pcVar3[9] = '\0';
  *(undefined8 *)pcVar3 = uVar1;
                    /* try { // try from 00c2cc30 to 00d2cc37 has its CatchHandler @ 00c2cde0 */
  if ((DAT_01128008 & 1) == 0) {
    DAT_01128008 = 0x10;
    puVar4 = &DAT_01128009;
                    /* try { // try from 00c2cc48 to 00d2cc67 has its CatchHandler @ 00c2cddc */
  }
  else {
    ram0x01128010 = 8;
    puVar4 = DAT_01128018;
  }
  *(undefined1 *)(puVar4 + 1) = 0;
  *puVar4 = 0x7961647372756854;
                    /* try { // try from 00c2cc78 to 00d2cc7f has its CatchHandler @ 00c2cd9c */
  if ((DAT_01128020 & 1) == 0) {
                    /* try { // try from 00c2cc90 to 00d2cc97 has its CatchHandler @ 00c2cd2c */
    DAT_01128020 = 0xc;
    puVar5 = &DAT_01128021;
  }
  else {
                    /* catch() { ... } // from try @ 00c2cbe0 with catch @ 00c2cc98
                       try { // try from 00c2cc98 to 00d2ce47 has its CatchHandler @ 00c2c450 */
    DAT_01128028 = 6;
    puVar5 = DAT_01128030;
  }
                    /* catch() { ... } // from try @ 00c2cbd4 with catch @ 00c2ccb0 */
  *(undefined1 *)((long)puVar5 + 6) = 0;
  *(undefined2 *)(puVar5 + 1) = 0x7961;
                    /* catch() { ... } // from try @ 00c2ca74 with catch @ 00c2ccc0 */
  *puVar5 = 0x64697246;
  if ((DAT_01128038 & 1) == 0) {
                    /* catch() { ... } // from try @ 00c2caf4 with catch @ 00c2ccd4 */
                    /* catch() { ... } // from try @ 00c2cab4 with catch @ 00c2ccdc */
    DAT_01128038 = 0x10;
    puVar4 = &DAT_01128039;
  }
  else {
    ram0x01128040 = 8;
    puVar4 = DAT_01128048;
  }
  *(undefined1 *)(puVar4 + 1) = 0;
                    /* catch() { ... } // from try @ 00c2ca2c with catch @ 00c2cd0c */
  *puVar4 = 0x7961647275746153;
                    /* catch() { ... } // from try @ 00c2c8ac with catch @ 00c2cd10 */
                    /* catch() { ... } // from try @ 00c2c908 with catch @ 00c2cd14 */
                    /* catch() { ... } // from try @ 00c2c880 with catch @ 00c2cd18 */
  if ((DAT_01128050 & 1) == 0) {
    DAT_01128050 = 6;
    puVar5 = &DAT_01128051;
                    /* catch() { ... } // from try @ 00c2c7fc with catch @ 00c2cd2c
                       catch() { ... } // from try @ 00c2cc90 with catch @ 00c2cd2c */
  }
  else {
                    /* catch() { ... } // from try @ 00c2c840 with catch @ 00c2cd34 */
    DAT_01128058 = 3;
    puVar5 = DAT_01128060;
  }
                    /* catch() { ... } // from try @ 00c2c6a0 with catch @ 00c2cd48 */
  *puVar5 = 0x6e7553;
  if ((DAT_01128068 & 1) == 0) {
    DAT_01128068 = 6;
    puVar5 = &DAT_01128069;
  }
  else {
                    /* catch() { ... } // from try @ 00c2c66c with catch @ 00c2cd80 */
    DAT_01128070 = 3;
    puVar5 = DAT_01128078;
  }
  *puVar5 = 0x6e6f4d;
                    /* catch() { ... } // from try @ 00c2c8e4 with catch @ 00c2cd90
                       catch() { ... } // from try @ 00c2cba8 with catch @ 00c2cd90 */
                    /* catch() { ... } // from try @ 00c2c738 with catch @ 00c2cd98 */
  if ((DAT_01128080 & 1) == 0) {
                    /* catch() { ... } // from try @ 00c2c6e8 with catch @ 00c2cd9c
                       catch() { ... } // from try @ 00c2cc78 with catch @ 00c2cd9c */
                    /* catch() { ... } // from try @ 00c2c630 with catch @ 00c2cda4 */
    DAT_01128080 = 6;
    puVar5 = &DAT_01128081;
  }
  else {
                    /* catch() { ... } // from try @ 00c2c5a0 with catch @ 00c2cdb8 */
    DAT_01128088 = 3;
    puVar5 = DAT_01128090;
  }
                    /* catch() { ... } // from try @ 00c2c4b8 with catch @ 00c2cdc8 */
  *puVar5 = 0x657554;
  if ((DAT_01128098 & 1) == 0) {
                    /* catch() { ... } // from try @ 00c2cc48 with catch @ 00c2cddc */
                    /* catch() { ... } // from try @ 00c2c560 with catch @ 00c2cde0
                       catch() { ... } // from try @ 00c2cc30 with catch @ 00c2cde0 */
                    /* catch() { ... } // from try @ 00c2c958 with catch @ 00c2cde8 */
    DAT_01128098 = 6;
    puVar5 = &DAT_01128099;
  }
  else {
    DAT_011280a0 = 3;
    puVar5 = DAT_011280a8;
  }
  *puVar5 = 0x646557;
  if ((DAT_011280b0 & 1) == 0) {
    DAT_011280b0 = 6;
    puVar5 = &DAT_011280b1;
  }
  else {
    DAT_011280b8 = 3;
    puVar5 = DAT_011280c0;
  }
                    /* try { // try from 00c2ce48 to 00d2ceb3 has its CatchHandler @ 00c2ce48
                       catch() { ... } // from try @ 00c2ce48 with catch @ 00c2ce48
                       catch() { ... } // from try @ 00c2cec4 with catch @ 00c2ce48 */
  *puVar5 = 0x756854;
  if ((DAT_011280c8 & 1) == 0) {
    DAT_011280c8 = 6;
    puVar5 = &DAT_011280c9;
  }
  else {
    DAT_011280d0 = 3;
    puVar5 = DAT_011280d8;
  }
  *puVar5 = 0x697246;
  if ((DAT_011280e0 & 1) == 0) {
    DAT_011280e0 = 6;
    puVar5 = &DAT_011280e1;
  }
  else {
                    /* try { // try from 00c2ceb4 to 00d2cec3 has its CatchHandler @ 00c2d218 */
    DAT_011280e8 = 3;
    puVar5 = DAT_011280f0;
  }
                    /* try { // try from 00c2cec4 to 00d2d257 has its CatchHandler @ 00c2ce48 */
  *puVar5 = 0x746153;
  return;
}

~~~
