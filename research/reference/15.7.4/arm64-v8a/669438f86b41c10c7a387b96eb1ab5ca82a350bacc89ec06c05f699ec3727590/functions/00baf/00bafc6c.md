# 00bafc6c

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-previous -->
**別版の対応** [v15.7.2 `00bafb60`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baf/00bafb60.md) · [本文差分](../../changes/00bafc6c.md)
<!-- /kbcs-version-previous -->

## 関数情報

~~~json
{
  "address": "00bafc6c",
  "name": "FUN_00bafc6c",
  "size": 1080,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7c3a17e7702b4dc0f078a2c2f0e9a42b872a34854a4ae5799a77161d405a2dd8",
  "source_text_sha256": "7c3a17e7702b4dc0f078a2c2f0e9a42b872a34854a4ae5799a77161d405a2dd8"
}
~~~

## 呼び出し元

- [00bafc00](../00baf/00bafc00.md)

## 呼び出し先

- [00bdafe0](../00bda/00bdafe0.md)
- [00bdb000](../00bdb/00bdb000.md)
- [00bdb020](../00bdb/00bdb020.md)

## 関連文字列（未確認候補）

~~~text
"Wednesday"
~~~

## 疑似コード / UTF-8 3745 bytes

~~~c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_00bafc6c(void)

{
  undefined8 uVar1;
  int iVar2;
  char *pcVar3;
  undefined8 *puVar4;
  undefined4 *puVar5;
  
  if (((DAT_010a2df0 & 1) == 0) && (iVar2 = __cxa_guard_acquire(&DAT_010a2df0), iVar2 != 0)) {
                    /* try { // try from 00bb0080 to 00cb0087 has its CatchHandler @ 00bb0df4 */
    __cxa_atexit(FUN_00bb8d30,0,&PTR_LOOP_00be5fd0);
    __cxa_guard_release(&DAT_010a2df0);
  }
  if ((DAT_010a2ca0 & 1) == 0) {
    DAT_010a2ca0 = 0xc;
    puVar5 = &DAT_010a2ca1;
  }
  else {
    DAT_010a2ca8 = 6;
    puVar5 = DAT_010a2cb0;
  }
  *(undefined1 *)((long)puVar5 + 6) = 0;
  *(undefined2 *)(puVar5 + 1) = 0x7961;
  *puVar5 = 0x646e7553;
  if ((DAT_010a2cb8 & 1) == 0) {
    DAT_010a2cb8 = 0xc;
    puVar5 = &DAT_010a2cb9;
  }
  else {
    DAT_010a2cc0 = 6;
    puVar5 = DAT_010a2cc8;
  }
  *(undefined1 *)((long)puVar5 + 6) = 0;
  *(undefined2 *)(puVar5 + 1) = 0x7961;
  *puVar5 = 0x646e6f4d;
  if ((DAT_010a2cd0 & 1) == 0) {
    DAT_010a2cd0 = 0xe;
    puVar5 = &DAT_010a2cd1;
  }
  else {
    DAT_010a2cd8 = 7;
    puVar5 = DAT_010a2ce0;
  }
  *(undefined1 *)((long)puVar5 + 7) = 0;
  *(undefined4 *)((long)puVar5 + 3) = 0x79616473;
  *puVar5 = 0x73657554;
  uVar1 = s_Wednesday_002a8090._0_8_;
  if ((DAT_010a2ce8 & 1) == 0) {
                    /* try { // try from 00bafd84 to 00cafdd3 has its CatchHandler @ 00bb0e00 */
    DAT_010a2ce8 = 0x12;
    pcVar3 = (char *)&DAT_010a2ce9;
  }
  else {
    ram0x010a2cf0 = 9;
    pcVar3 = DAT_010a2cf8;
  }
  pcVar3[8] = 'y';
  pcVar3[9] = '\0';
  *(undefined8 *)pcVar3 = uVar1;
  if ((DAT_010a2d00 & 1) == 0) {
    DAT_010a2d00 = 0x10;
    puVar4 = &DAT_010a2d01;
  }
  else {
    ram0x010a2d08 = 8;
    puVar4 = DAT_010a2d10;
  }
  *(undefined1 *)(puVar4 + 1) = 0;
  *puVar4 = 0x7961647372756854;
  if ((DAT_010a2d18 & 1) == 0) {
    DAT_010a2d18 = 0xc;
    puVar5 = &DAT_010a2d19;
  }
  else {
    DAT_010a2d20 = 6;
    puVar5 = DAT_010a2d28;
  }
  *(undefined1 *)((long)puVar5 + 6) = 0;
  *(undefined2 *)(puVar5 + 1) = 0x7961;
                    /* try { // try from 00bafe50 to 00cafff7 has its CatchHandler @ 00bb0e38 */
  *puVar5 = 0x64697246;
  if ((DAT_010a2d30 & 1) == 0) {
    DAT_010a2d30 = 0x10;
    puVar4 = &DAT_010a2d31;
  }
  else {
    ram0x010a2d38 = 8;
    puVar4 = DAT_010a2d40;
  }
  *(undefined1 *)(puVar4 + 1) = 0;
  *puVar4 = 0x7961647275746153;
  if ((DAT_010a2d48 & 1) == 0) {
    DAT_010a2d48 = 6;
    puVar5 = &DAT_010a2d49;
  }
  else {
    DAT_010a2d50 = 3;
    puVar5 = DAT_010a2d58;
  }
  *puVar5 = 0x6e7553;
  if ((DAT_010a2d60 & 1) == 0) {
    DAT_010a2d60 = 6;
    puVar5 = &DAT_010a2d61;
  }
  else {
    DAT_010a2d68 = 3;
    puVar5 = DAT_010a2d70;
  }
  *puVar5 = 0x6e6f4d;
  if ((DAT_010a2d78 & 1) == 0) {
    DAT_010a2d78 = 6;
    puVar5 = &DAT_010a2d79;
  }
  else {
    DAT_010a2d80 = 3;
    puVar5 = DAT_010a2d88;
  }
  *puVar5 = 0x657554;
  if ((DAT_010a2d90 & 1) == 0) {
    DAT_010a2d90 = 6;
    puVar5 = &DAT_010a2d91;
  }
  else {
    DAT_010a2d98 = 3;
    puVar5 = DAT_010a2da0;
  }
  *puVar5 = 0x646557;
  if ((DAT_010a2da8 & 1) == 0) {
    DAT_010a2da8 = 6;
    puVar5 = &DAT_010a2da9;
  }
  else {
    DAT_010a2db0 = 3;
    puVar5 = DAT_010a2db8;
  }
  *puVar5 = 0x756854;
  if ((DAT_010a2dc0 & 1) == 0) {
                    /* try { // try from 00bafff8 to 00cb007f has its CatchHandler @ 00bafb60 */
    DAT_010a2dc0 = 6;
    puVar5 = &DAT_010a2dc1;
  }
  else {
    DAT_010a2dc8 = 3;
    puVar5 = DAT_010a2dd0;
  }
  *puVar5 = 0x697246;
  if ((DAT_010a2dd8 & 1) == 0) {
    DAT_010a2dd8 = 6;
    puVar5 = &DAT_010a2dd9;
  }
  else {
    DAT_010a2de0 = 3;
    puVar5 = DAT_010a2de8;
  }
  *puVar5 = 0x746153;
  return;
}

~~~
