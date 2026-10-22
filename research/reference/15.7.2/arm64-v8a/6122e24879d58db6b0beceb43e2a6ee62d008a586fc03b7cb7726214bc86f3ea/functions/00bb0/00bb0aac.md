# 00bb0aac

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bb0aac.md)

## 関数情報

~~~json
{
  "address": "00bb0aac",
  "name": "FUN_00bb0aac",
  "size": 1320,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "830acac1c6917e7c7fd2aa46b6790c9c15ca56739ad558498f9eddfeb1341d74",
  "source_text_sha256": "830acac1c6917e7c7fd2aa46b6790c9c15ca56739ad558498f9eddfeb1341d74"
}
~~~
## 呼び出し元

- [00bb0a2c](../00bb0/00bb0a2c.md)

## 呼び出し先

- [00b76424](../00b76/00b76424.md)
- [00bdaee0](../00bda/00bdaee0.md)
- [00bdaf00](../00bda/00bdaf00.md)
- [00bdaf20](../00bda/00bdaf20.md)

## 関連文字列（未確認候補）

~~~text
"April"
"August"
"December"
"February"
"January"
"March"
"November"
"October"
"September"
~~~
## 疑似コード 1/1 / UTF-8 6497 bytes

~~~c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_00bb0aac(void)

{
  undefined8 uVar1;
  int iVar2;
  undefined8 *puVar3;
  
  if (((DAT_010a32d8 & 1) == 0) && (iVar2 = __cxa_guard_acquire(&DAT_010a32d8), iVar2 != 0)) {
    __cxa_atexit(FUN_00bb8f54,0,&PTR_LOOP_00be5ed0);
    __cxa_guard_release(&DAT_010a32d8);
  }
  FUN_00b76424(&DAT_010a3098,L"January",7);
  FUN_00b76424(&DAT_010a30b0,L"February",8);
  FUN_00b76424(&DAT_010a30c8,L"March",5);
  FUN_00b76424(&DAT_010a30e0,L"April",5);
  if ((DAT_010a30f8 & 1) == 0) {
    DAT_010a30f8 = 6;
    puVar3 = &DAT_010a30fc;
  }
  else {
    ram0x010a3100 = 3;
    puVar3 = ram0x010a3108;
  }
  *puVar3 = 0x610000004d;
  puVar3[1] = 0x79;
  if ((DAT_010a3110 & 1) == 0) {
    DAT_010a3110 = 8;
    puVar3 = (undefined8 *)&DAT_010a3114;
  }
  else {
    DAT_010a3118 = 4;
    puVar3 = DAT_010a3120;
  }
                    /* try { // try from 00bb0b9c to 00cb0ba3 has its CatchHandler @ 00bb0ce0 */
  *(undefined4 *)(puVar3 + 2) = 0;
  uVar1 = _DAT_002fa96c;
  puVar3[1] = _UNK_002fa974;
  *puVar3 = uVar1;
  uVar1 = _DAT_002fa6b8;
  if ((DAT_010a3128 & 1) == 0) {
    DAT_010a3128 = 8;
    puVar3 = (undefined8 *)&DAT_010a312c;
  }
  else {
    DAT_010a3130 = 4;
    puVar3 = DAT_010a3138;
  }
  puVar3[1] = _UNK_002fa6c0;
  *puVar3 = uVar1;
  *(undefined4 *)(puVar3 + 2) = 0;
  FUN_00b76424(&DAT_010a3140,L"August",6);
  FUN_00b76424(&DAT_010a3158,L"September",9);
  FUN_00b76424(&DAT_010a3170,L"October",7);
  FUN_00b76424(&DAT_010a3188,L"November",8);
  FUN_00b76424(&DAT_010a31a0,L"December",8);
                    /* try { // try from 00bb0c68 to 00cb0c87 has its CatchHandler @ 00bb0d18 */
  if ((DAT_010a31b8 & 1) == 0) {
    DAT_010a31b8 = 6;
    puVar3 = &DAT_010a31bc;
  }
  else {
    ram0x010a31c0 = 3;
    puVar3 = ram0x010a31c8;
  }
                    /* try { // try from 00bb0c9c to 00cb0ca7 has its CatchHandler @ 00bb0cfc */
  *puVar3 = 0x610000004a;
  puVar3[1] = 0x6e;
  if ((DAT_010a31d0 & 1) == 0) {
    DAT_010a31d0 = 6;
    puVar3 = &DAT_010a31d4;
                    /* try { // try from 00bb0cbc to 00cb0cdb has its CatchHandler @ 00bb0ce4 */
  }
  else {
    ram0x010a31d8 = 3;
    puVar3 = ram0x010a31e0;
  }
                    /* catch() { ... } // from try @ 00bb019c with catch @ 00bb0cdc
                       try { // try from 00bb0cdc to 00cb0d6f has its CatchHandler @ 00bafa54 */
                    /* catch() { ... } // from try @ 00bb0b9c with catch @ 00bb0ce0 */
  *puVar3 = 0x6500000046;
  puVar3[1] = 0x62;
                    /* catch() { ... } // from try @ 00bb0cbc with catch @ 00bb0ce4 */
                    /* catch() { ... } // from try @ 00baff74 with catch @ 00bb0ce8 */
                    /* catch() { ... } // from try @ 00bb09ec with catch @ 00bb0cec */
  if ((DAT_010a31e8 & 1) == 0) {
                    /* catch() { ... } // from try @ 00bb0a54 with catch @ 00bb0cf0 */
                    /* catch() { ... } // from try @ 00bafc78 with catch @ 00bb0cf4 */
                    /* catch() { ... } // from try @ 00bb059c with catch @ 00bb0cf8 */
                    /* catch() { ... } // from try @ 00bb0c9c with catch @ 00bb0cfc */
    DAT_010a31e8 = 6;
    puVar3 = &DAT_010a31ec;
                    /* catch() { ... } // from try @ 00bafb5c with catch @ 00bb0d00 */
  }
  else {
                    /* catch() { ... } // from try @ 00bb0698 with catch @ 00bb0d08 */
                    /* catch() { ... } // from try @ 00bafaac with catch @ 00bb0d0c */
                    /* catch() { ... } // from try @ 00bb0290 with catch @ 00bb0d14 */
    ram0x010a31f0 = 3;
    puVar3 = ram0x010a31f8;
  }
                    /* catch() { ... } // from try @ 00bb0c68 with catch @ 00bb0d18 */
                    /* catch() { ... } // from try @ 00bb000c with catch @ 00bb0d1c */
                    /* catch() { ... } // from try @ 00bb0270 with catch @ 00bb0d20 */
                    /* catch() { ... } // from try @ 00bb06a8 with catch @ 00bb0d24 */
  *puVar3 = 0x610000004d;
  puVar3[1] = 0x72;
                    /* catch() { ... } // from try @ 00bb02a0 with catch @ 00bb0d28 */
                    /* catch() { ... } // from try @ 00bafd44 with catch @ 00bb0d2c */
  if ((DAT_010a3200 & 1) == 0) {
    DAT_010a3200 = 6;
    puVar3 = &DAT_010a3204;
  }
  else {
    ram0x010a3208 = 3;
    puVar3 = ram0x010a3210;
  }
  *puVar3 = 0x7000000041;
  puVar3[1] = 0x72;
  if ((DAT_010a3218 & 1) == 0) {
    DAT_010a3218 = 6;
    puVar3 = &DAT_010a321c;
  }
  else {
                    /* catch() { ... } // from try @ 00bb0f74 with catch @ 00bb0d98 */
    ram0x010a3220 = 3;
    puVar3 = ram0x010a3228;
  }
  *puVar3 = 0x610000004d;
  puVar3[1] = 0x79;
  if ((DAT_010a3230 & 1) == 0) {
    DAT_010a3230 = 6;
    puVar3 = &DAT_010a3234;
  }
  else {
    ram0x010a3238 = 3;
    puVar3 = ram0x010a3240;
  }
  *puVar3 = 0x750000004a;
  puVar3[1] = 0x6e;
  if ((DAT_010a3248 & 1) == 0) {
    DAT_010a3248 = 6;
    puVar3 = &DAT_010a324c;
  }
  else {
    ram0x010a3250 = 3;
    puVar3 = ram0x010a3258;
  }
  *puVar3 = 0x750000004a;
  puVar3[1] = 0x6c;
  if ((DAT_010a3260 & 1) == 0) {
    DAT_010a3260 = 6;
    puVar3 = &DAT_010a3264;
  }
  else {
    ram0x010a3268 = 3;
    puVar3 = ram0x010a3270;
  }
  *puVar3 = 0x7500000041;
  puVar3[1] = 0x67;
  if ((DAT_010a3278 & 1) == 0) {
    DAT_010a3278 = 6;
    puVar3 = &DAT_010a327c;
  }
  else {
    ram0x010a3280 = 3;
    puVar3 = ram0x010a3288;
  }
  *puVar3 = 0x6500000053;
  puVar3[1] = 0x70;
  if ((DAT_010a3290 & 1) == 0) {
    DAT_010a3290 = 6;
    puVar3 = &DAT_010a3294;
  }
  else {
                    /* try { // try from 00bb0eec to 00cb0f73 has its CatchHandler @ 00bb1058 */
    ram0x010a3298 = 3;
    puVar3 = ram0x010a32a0;
  }
  *puVar3 = 0x630000004f;
  puVar3[1] = 0x74;
  if ((DAT_010a32a8 & 1) == 0) {
    DAT_010a32a8 = 6;
    puVar3 = &DAT_010a32ac;
  }
  else {
    ram0x010a32b0 = 3;
    puVar3 = ram0x010a32b8;
  }
  *puVar3 = 0x6f0000004e;
  puVar3[1] = 0x76;
  if ((DAT_010a32c0 & 1) == 0) {
    DAT_010a32c0 = 6;
    puVar3 = &DAT_010a32c4;
  }
  else {
                    /* try { // try from 00bb0f74 to 00cb1127 has its CatchHandler @ 00bb0d98 */
    ram0x010a32c8 = 3;
    puVar3 = ram0x010a32d0;
  }
  *puVar3 = 0x6500000044;
  puVar3[1] = 99;
  return;
}

~~~
