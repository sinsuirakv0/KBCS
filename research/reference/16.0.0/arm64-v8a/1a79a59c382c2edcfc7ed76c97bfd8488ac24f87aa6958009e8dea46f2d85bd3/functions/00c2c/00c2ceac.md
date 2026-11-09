# 00c2ceac

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00c2ceac",
  "name": "FUN_00c2ceac",
  "size": 1748,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9e41c038f4e56f244ee6f48ba1def11bb37c88d4e7114bc8bb4aac04275b4907",
  "source_text_sha256": "9e41c038f4e56f244ee6f48ba1def11bb37c88d4e7114bc8bb4aac04275b4907"
}
~~~

## 呼び出し元

- [00c2ce40](../00c2c/00c2ce40.md)

## 呼び出し先

- [00c57a30](../00c57/00c57a30.md)
- [00c57a50](../00c57/00c57a50.md)
- [00c57a70](../00c57/00c57a70.md)

## 関連文字列（未確認候補）

~~~text
"September"
~~~

## 疑似コード / UTF-8 6700 bytes

~~~c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_00c2ceac(void)

{
  undefined8 uVar1;
  int iVar2;
  char *pcVar3;
  undefined8 *puVar4;
  undefined4 *puVar5;
  
  if (((DAT_01128098 & 1) == 0) && (iVar2 = __cxa_guard_acquire(&DAT_01128098), iVar2 != 0)) {
    __cxa_atexit(FUN_00c35a58,0,&PTR_LOOP_00c62b90);
    __cxa_guard_release(&DAT_01128098);
  }
  if ((DAT_01127e58 & 1) == 0) {
    DAT_01127e58 = 0xe;
    puVar5 = &DAT_01127e59;
  }
  else {
    DAT_01127e60 = 7;
    puVar5 = DAT_01127e68;
  }
  *(undefined1 *)((long)puVar5 + 7) = 0;
  *(undefined4 *)((long)puVar5 + 3) = 0x79726175;
  *puVar5 = 0x756e614a;
  if ((DAT_01127e70 & 1) == 0) {
    DAT_01127e70 = 0x10;
    puVar4 = &DAT_01127e71;
  }
  else {
    ram0x01127e78 = 8;
    puVar4 = DAT_01127e80;
  }
  *(undefined1 *)(puVar4 + 1) = 0;
  *puVar4 = 0x7972617572626546;
  if ((DAT_01127e88 & 1) == 0) {
    DAT_01127e88 = 10;
    puVar5 = &DAT_01127e89;
  }
  else {
    DAT_01127e90 = 5;
    puVar5 = DAT_01127e98;
  }
  *(undefined2 *)(puVar5 + 1) = 0x68;
  *puVar5 = 0x6372614d;
  if ((DAT_01127ea0 & 1) == 0) {
    DAT_01127ea0 = 10;
    puVar5 = &DAT_01127ea1;
  }
  else {
    DAT_01127ea8 = 5;
    puVar5 = DAT_01127eb0;
  }
  *(undefined2 *)(puVar5 + 1) = 0x6c;
  *puVar5 = 0x69727041;
  if ((DAT_01127eb8 & 1) == 0) {
    DAT_01127eb8 = 6;
    puVar5 = &DAT_01127eb9;
  }
  else {
    DAT_01127ec0 = 3;
    puVar5 = DAT_01127ec8;
  }
  *puVar5 = 0x79614d;
  if ((DAT_01127ed0 & 1) == 0) {
    DAT_01127ed0 = 8;
    puVar5 = &DAT_01127ed1;
  }
  else {
    DAT_01127ed8 = 4;
    puVar5 = DAT_01127ee0;
  }
  *(undefined1 *)(puVar5 + 1) = 0;
  *puVar5 = 0x656e754a;
  if ((DAT_01127ee8 & 1) == 0) {
    DAT_01127ee8 = 8;
    puVar5 = &DAT_01127ee9;
  }
  else {
    DAT_01127ef0 = 4;
    puVar5 = DAT_01127ef8;
  }
  *(undefined1 *)(puVar5 + 1) = 0;
                    /* try { // try from 00c2d0b4 to 00d2d197 has its CatchHandler @ 00c2d0b4
                       catch(type#1 @ 00000000) { ... } // from try @ 00c2d0b4 with catch @ 00c2d0b4
                       catch(type#1 @ 00000000) { ... } // from try @ 00c2d228 with catch @ 00c2d0b4
                        */
  *puVar5 = 0x796c754a;
  if ((DAT_01127f00 & 1) == 0) {
    DAT_01127f00 = 0xc;
    puVar5 = &DAT_01127f01;
  }
  else {
    DAT_01127f08 = 6;
    puVar5 = DAT_01127f10;
  }
  *(undefined1 *)((long)puVar5 + 6) = 0;
  *(undefined2 *)(puVar5 + 1) = 0x7473;
  *puVar5 = 0x75677541;
  uVar1 = s_September_002a0dc9._0_8_;
  if ((DAT_01127f18 & 1) == 0) {
    DAT_01127f18 = 0x12;
    pcVar3 = (char *)&DAT_01127f19;
  }
  else {
    ram0x01127f20 = 9;
    pcVar3 = DAT_01127f28;
  }
  pcVar3[8] = 'r';
  pcVar3[9] = '\0';
  *(undefined8 *)pcVar3 = uVar1;
  if ((DAT_01127f30 & 1) == 0) {
    DAT_01127f30 = 0xe;
    puVar5 = &DAT_01127f31;
  }
  else {
    DAT_01127f38 = 7;
    puVar5 = DAT_01127f40;
  }
  *(undefined1 *)((long)puVar5 + 7) = 0;
                    /* try { // try from 00c2d198 to 00d2d1a3 has its CatchHandler @ 00c2d2b0 */
  *(undefined4 *)((long)puVar5 + 3) = 0x7265626f;
  *puVar5 = 0x6f74634f;
  if ((DAT_01127f48 & 1) == 0) {
    DAT_01127f48 = 0x10;
    puVar4 = &DAT_01127f49;
  }
  else {
    ram0x01127f50 = 8;
    puVar4 = DAT_01127f58;
  }
  *(undefined1 *)(puVar4 + 1) = 0;
  *puVar4 = 0x7265626d65766f4e;
  if ((DAT_01127f60 & 1) == 0) {
    DAT_01127f60 = 0x10;
    puVar4 = &DAT_01127f61;
  }
  else {
    ram0x01127f68 = 8;
    puVar4 = DAT_01127f70;
  }
                    /* try { // try from 00c2d224 to 00d2d227 has its CatchHandler @ 00c2d2b4 */
                    /* try { // try from 00c2d228 to 00d2d2b7 has its CatchHandler @ 00c2d0b4 */
  *(undefined1 *)(puVar4 + 1) = 0;
  *puVar4 = 0x7265626d65636544;
  if ((DAT_01127f78 & 1) == 0) {
    DAT_01127f78 = 6;
    puVar5 = &DAT_01127f79;
  }
  else {
    DAT_01127f80 = 3;
    puVar5 = DAT_01127f88;
  }
  *puVar5 = 0x6e614a;
  if ((DAT_01127f90 & 1) == 0) {
    DAT_01127f90 = 6;
    puVar5 = &DAT_01127f91;
  }
  else {
    DAT_01127f98 = 3;
    puVar5 = DAT_01127fa0;
  }
                    /* catch(type#1 @ 00000000) { ... } // from try @ 00c2d198 with catch @ 00c2d2b0
                        */
                    /* catch(type#1 @ 00000000) { ... } // from try @ 00c2d224 with catch @ 00c2d2b4
                        */
  *puVar5 = 0x626546;
  if ((DAT_01127fa8 & 1) == 0) {
    DAT_01127fa8 = 6;
    puVar5 = &DAT_01127fa9;
  }
  else {
    DAT_01127fb0 = 3;
    puVar5 = DAT_01127fb8;
  }
  *puVar5 = 0x72614d;
  if ((DAT_01127fc0 & 1) == 0) {
    DAT_01127fc0 = 6;
    puVar5 = &DAT_01127fc1;
  }
  else {
                    /* try { // try from 00c2d32c to 00d2d37b has its CatchHandler @ 00c2d32c
                       catch() { ... } // from try @ 00c2d32c with catch @ 00c2d32c
                       catch() { ... } // from try @ 00c2d384 with catch @ 00c2d32c */
    DAT_01127fc8 = 3;
    puVar5 = DAT_01127fd0;
  }
  *puVar5 = 0x727041;
  if ((DAT_01127fd8 & 1) == 0) {
    DAT_01127fd8 = 6;
    puVar5 = &DAT_01127fd9;
  }
  else {
    DAT_01127fe0 = 3;
    puVar5 = DAT_01127fe8;
  }
  *puVar5 = 0x79614d;
                    /* try { // try from 00c2d37c to 00d2d383 has its CatchHandler @ 00c2d394 */
                    /* try { // try from 00c2d384 to 00d2d3a7 has its CatchHandler @ 00c2d32c */
  if ((DAT_01127ff0 & 1) == 0) {
                    /* catch() { ... } // from try @ 00c2d37c with catch @ 00c2d394 */
    DAT_01127ff0 = 6;
    puVar5 = &DAT_01127ff1;
  }
  else {
    DAT_01127ff8 = 3;
    puVar5 = DAT_01128000;
  }
  *puVar5 = 0x6e754a;
  if ((DAT_01128008 & 1) == 0) {
    DAT_01128008 = 6;
    puVar5 = &DAT_01128009;
  }
  else {
    DAT_01128010 = 3;
    puVar5 = DAT_01128018;
  }
  *puVar5 = 0x6c754a;
  if ((DAT_01128020 & 1) == 0) {
    DAT_01128020 = 6;
    puVar5 = &DAT_01128021;
  }
  else {
    DAT_01128028 = 3;
    puVar5 = DAT_01128030;
  }
  *puVar5 = 0x677541;
  if ((DAT_01128038 & 1) == 0) {
    DAT_01128038 = 6;
    puVar5 = &DAT_01128039;
  }
  else {
                    /* catch() { ... } // from try @ 00c2d644 with catch @ 00c2d468 */
    DAT_01128040 = 3;
    puVar5 = DAT_01128048;
  }
  *puVar5 = 0x706553;
  if ((DAT_01128050 & 1) == 0) {
    DAT_01128050 = 6;
    puVar5 = &DAT_01128051;
  }
  else {
    DAT_01128058 = 3;
    puVar5 = DAT_01128060;
  }
  *puVar5 = 0x74634f;
  if ((DAT_01128068 & 1) == 0) {
    DAT_01128068 = 6;
    puVar5 = &DAT_01128069;
  }
  else {
    DAT_01128070 = 3;
    puVar5 = DAT_01128078;
  }
  *puVar5 = 0x766f4e;
  if ((DAT_01128080 & 1) == 0) {
    DAT_01128080 = 6;
    puVar5 = &DAT_01128081;
  }
  else {
    DAT_01128088 = 3;
    puVar5 = DAT_01128090;
  }
  *puVar5 = 0x636544;
  return;
}

~~~
