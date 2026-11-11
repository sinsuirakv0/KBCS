# 00aefad8

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00aefad8",
  "name": "FUN_00aefad8",
  "size": 784,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "791b1e10ac97121726d20bc572317b2e39b86d69919146ad815ca2174f0700d2",
  "source_text_sha256": "791b1e10ac97121726d20bc572317b2e39b86d69919146ad815ca2174f0700d2"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00467b60](../00467/00467b60.md)
- [00469c04](../00469/00469c04.md)
- [00489f4c](../00489/00489f4c.md)
- [008b6d9c](../008b6/008b6d9c.md)
- [008b79c8](../008b7/008b79c8.md)
- [008b9290](../008b9/008b9290.md)
- [008b92ec](../008b9/008b92ec.md)
- [008b9794](../008b9/008b9794.md)
- [008b980c](../008b9/008b980c.md)
- [00c58610](../00c58/00c58610.md)

## 疑似コード / UTF-8 6098 bytes

~~~c

void FUN_00aefad8(long param_1,undefined8 *param_2,undefined8 *param_3)

{
  int iVar1;
  int iVar2;
  int iVar3;
  int iVar4;
  int iVar5;
  int iVar6;
  long lVar7;
  ulong uVar8;
  long lVar9;
  int extraout_var;
  int extraout_var_00;
  int extraout_w1;
  int extraout_w1_00;
  int extraout_var_01;
  int extraout_var_02;
  undefined8 uVar10;
  undefined8 uVar11;
  undefined8 uVar12;
  long lVar13;
  
  uVar11 = *param_2;
  uVar10 = *param_3;
  lVar13 = *(long *)(param_1 + 8);
  iVar4 = FUN_008b9290(uVar11);
  if ((iVar4 != 1) && (iVar4 = FUN_008b9290(uVar11), iVar4 != 2)) {
    return;
  }
  if (DAT_00ca4978 == 0) {
    lVar7 = 0;
  }
  else {
    lVar7 = __dynamic_cast(DAT_00ca4978,&PTR__ZTVN10__cxxabiv117__class_type_infoE_16__00c65e58,
                           &PTR__ZTVN10__cxxabiv120__si_class_type_infoE_16__00c8d950,0);
                    /* try { // try from 00aefb48 to 00befb4f has its CatchHandler @ 00aefda8 */
  }
                    /* try { // try from 00aefb50 to 00befbc7 has its CatchHandler @ 00aef8e0 */
  uVar8 = FUN_008b9794(uVar11,0);
  if ((uVar8 & 1) == 0) {
    FUN_00467b60(uVar10,0x7f,0x7f,0x7f,0xff);
  }
  iVar5 = FUN_008b980c(uVar11,0);
  uVar12 = *(undefined8 *)(lVar7 + 0x118);
  iVar6 = FUN_008b92ec(uVar11,0);
  FUN_008b92ec(uVar11,0);
  lVar9 = FUN_00489f4c(*(undefined8 *)(lVar7 + 0x118),0x80);
  iVar4 = extraout_w1 - *(int *)(lVar9 + 8);
                    /* try { // try from 00aefbc8 to 00befbcf has its CatchHandler @ 00aefda4 */
  if (extraout_w1 < *(int *)(lVar9 + 8)) {
    iVar4 = iVar4 + 1;
  }
  iVar1 = iVar5;
                    /* try { // try from 00aefbd0 to 00befc43 has its CatchHandler @ 00aef8e0 */
  if (iVar5 < 0) {
    iVar1 = iVar5 + 1;
  }
  FUN_008b92ec(uVar11,0);
  FUN_008b92ec(uVar11,0);
  lVar9 = FUN_00489f4c(*(undefined8 *)(lVar7 + 0x118),0x80);
  iVar3 = extraout_var_01 - *(int *)(lVar9 + 0xc);
  if (extraout_var_01 < *(int *)(lVar9 + 0xc)) {
    iVar3 = iVar3 + 1;
  }
  lVar9 = FUN_00489f4c(*(undefined8 *)(lVar7 + 0x118),0x80);
  iVar2 = *(int *)(lVar9 + 8);
  lVar9 = FUN_00489f4c(*(undefined8 *)(lVar7 + 0x118),0x80);
                    /* try { // try from 00aefc44 to 00befc4b has its CatchHandler @ 00aefda0 */
                    /* try { // try from 00aefc4c to 00befcb7 has its CatchHandler @ 00aef8e0 */
  FUN_00469c04(uVar10,uVar12,(iVar6 - (iVar1 >> 1)) + (iVar4 >> 1),
               (extraout_var - (iVar1 >> 1)) + (iVar3 >> 1),iVar2 + iVar5,
               *(int *)(lVar9 + 0xc) + iVar5,0x80);
  FUN_00467b60(uVar10,0xff,0xff,0xff,0xff);
  uVar8 = FUN_008b9794(uVar11,1);
  if ((uVar8 & 1) == 0) {
    FUN_00467b60(uVar10,0x7f,0x7f,0x7f,0xff);
  }
  iVar5 = FUN_008b980c(uVar11,1);
  uVar12 = *(undefined8 *)(lVar7 + 0x118);
                    /* try { // try from 00aefcb8 to 00befcbf has its CatchHandler @ 00aefd9c */
  iVar6 = FUN_008b92ec(uVar11,1);
  FUN_008b92ec(uVar11,1);
  lVar9 = FUN_00489f4c(*(undefined8 *)(lVar7 + 0x118),0x7f);
  iVar4 = extraout_w1_00 - *(int *)(lVar9 + 8);
  if (extraout_w1_00 < *(int *)(lVar9 + 8)) {
    iVar4 = iVar4 + 1;
  }
  iVar1 = iVar5;
  if (iVar5 < 0) {
    iVar1 = iVar5 + 1;
  }
  FUN_008b92ec(uVar11,1);
                    /* try { // try from 00aefd0c to 00befd0f has its CatchHandler @ 00aefdb8 */
  FUN_008b92ec(uVar11,1);
                    /* try { // try from 00aefd20 to 00befd23 has its CatchHandler @ 00aefdb4 */
  lVar9 = FUN_00489f4c(*(undefined8 *)(lVar7 + 0x118),0x7f);
                    /* try { // try from 00aefd34 to 00befd37 has its CatchHandler @ 00aefdb0 */
  iVar3 = extraout_var_02 - *(int *)(lVar9 + 0xc);
  if (extraout_var_02 < *(int *)(lVar9 + 0xc)) {
    iVar3 = iVar3 + 1;
  }
  lVar9 = FUN_00489f4c(*(undefined8 *)(lVar7 + 0x118),0x7f);
                    /* try { // try from 00aefd48 to 00befd4b has its CatchHandler @ 00aefdac */
  iVar2 = *(int *)(lVar9 + 8);
  lVar7 = FUN_00489f4c(*(undefined8 *)(lVar7 + 0x118),0x7f);
                    /* try { // try from 00aefd5c to 00befd5f has its CatchHandler @ 00aefda8 */
                    /* try { // try from 00aefd70 to 00befd73 has its CatchHandler @ 00aefda4 */
  FUN_00469c04(uVar10,uVar12,(iVar6 - (iVar1 >> 1)) + (iVar4 >> 1),
               (extraout_var_00 - (iVar1 >> 1)) + (iVar3 >> 1),iVar2 + iVar5,
               *(int *)(lVar7 + 0xc) + iVar5,0x7f);
                    /* try { // try from 00aefd84 to 00befd87 has its CatchHandler @ 00aefda0 */
  FUN_00467b60(uVar10,0xff,0xff,0xff,0xff);
                    /* try { // try from 00aefd98 to 00befd9b has its CatchHandler @ 00aefd9c */
                    /* catch() { ... } // from try @ 00aefcb8 with catch @ 00aefd9c
                       catch() { ... } // from try @ 00aefd98 with catch @ 00aefd9c
                       try { // try from 00aefd9c to 00befde7 has its CatchHandler @ 00aef8e0 */
                    /* catch() { ... } // from try @ 00aefc44 with catch @ 00aefda0
                       catch() { ... } // from try @ 00aefd84 with catch @ 00aefda0 */
                    /* catch() { ... } // from try @ 00aefbc8 with catch @ 00aefda4
                       catch() { ... } // from try @ 00aefd70 with catch @ 00aefda4 */
  uVar10 = FUN_008b79c8(lVar13 + 0x2f38,0x326);
                    /* catch() { ... } // from try @ 00aefb48 with catch @ 00aefda8
                       catch() { ... } // from try @ 00aefd5c with catch @ 00aefda8 */
                    /* catch() { ... } // from try @ 00aefac8 with catch @ 00aefdac
                       catch() { ... } // from try @ 00aefd48 with catch @ 00aefdac */
                    /* catch() { ... } // from try @ 00aefa50 with catch @ 00aefdb0
                       catch() { ... } // from try @ 00aefd34 with catch @ 00aefdb0 */
                    /* catch() { ... } // from try @ 00aef9d8 with catch @ 00aefdb4
                       catch() { ... } // from try @ 00aefd20 with catch @ 00aefdb4 */
                    /* catch() { ... } // from try @ 00aef960 with catch @ 00aefdb8
                       catch() { ... } // from try @ 00aefd0c with catch @ 00aefdb8 */
  FUN_008b6d9c(uVar10,0,0);
  return;
}

~~~
