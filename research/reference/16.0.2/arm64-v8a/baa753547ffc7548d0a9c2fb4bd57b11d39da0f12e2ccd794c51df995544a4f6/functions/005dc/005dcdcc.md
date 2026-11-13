# 005dcdcc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "005dcdcc",
  "name": "FUN_005dcdcc",
  "size": 2500,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e603dc59bae00e4d9f583579544ffe09fe80997ebf38add01c08759f102b187a",
  "source_text_sha256": "e603dc59bae00e4d9f583579544ffe09fe80997ebf38add01c08759f102b187a"
}
~~~

## 呼び出し元

- [005e9114](../005e9/005e9114.md)
- [005ec2b4](../005ec/005ec2b4.md)

## 呼び出し先

- [005c17dc](../005c1/005c17dc.md)
- [005dd790](../005dd/005dd790.md)
- [005ddae0](../005dd/005ddae0.md)

## 疑似コード / UTF-8 15466 bytes

~~~c

void FUN_005dcdcc(int *param_1,long *param_2,ulong param_3)

{
  int iVar1;
  long lVar2;
  long lVar3;
  int *piVar4;
  int iVar5;
  
  piVar4 = param_1 + 0x18;
  FUN_005c17dc(param_1 + 0x16,*(undefined8 *)piVar4);
  iVar1 = *param_1;
  *(int **)(param_1 + 0x16) = piVar4;
  param_1[0x1a] = 0;
  param_1[0x1b] = 0;
  piVar4[0] = 0;
  piVar4[1] = 0;
  lVar2 = *param_2;
  lVar3 = lVar2 + (long)iVar1 * 2000;
  if ((param_3 & 1) == 0) {
    if (*(char *)(lVar3 + 0x40) != '\0') {
      iVar5 = FUN_005dd790(lVar3 + 0x40,param_1 + 0x16,0xffffffff,0);
      iVar1 = *param_1;
      lVar2 = *param_2;
      param_1[1] = iVar5;
    }
    if (*(char *)(lVar2 + (long)iVar1 * 2000 + 0x1c0) != '\0') {
      iVar5 = FUN_005ddae0(0,lVar2 + (long)iVar1 * 2000 + 0x1c0,param_1 + 0x16,param_1[1]);
      iVar1 = *param_1;
      lVar2 = *param_2;
      param_1[6] = iVar5;
    }
    if (*(char *)(lVar2 + (long)iVar1 * 2000 + 0x240) != '\0') goto LAB_005dcf28;
LAB_005dcf80:
    if (*(char *)(lVar2 + (long)iVar1 * 2000 + 0x80) != '\0') {
LAB_005dcf94:
                    /* try { // try from 005dcfa0 to 006dcfab has its CatchHandler @ 005dd27c */
      iVar1 = FUN_005dd790(lVar2 + (long)iVar1 * 2000 + 0x80,param_1 + 0x16,param_1[1],0);
      param_1[2] = iVar1;
      if ((param_3 & 1) != 0) goto LAB_005dcfb8;
                    /* try { // try from 005dcff0 to 006dcffb has its CatchHandler @ 005dd2f4 */
      iVar1 = *param_1;
      lVar2 = *param_2;
    }
    if (*(char *)(lVar2 + (long)iVar1 * 2000 + 0x2c0) != '\0') goto LAB_005dd010;
LAB_005dd07c:
    if (*(char *)(lVar2 + (long)iVar1 * 2000 + 0x340) != '\0') goto LAB_005dd090;
LAB_005dd104:
                    /* try { // try from 005dd108 to 006dd113 has its CatchHandler @ 005dd25c */
    if (*(char *)(lVar2 + (long)iVar1 * 2000 + 0x3c0) != '\0') goto LAB_005dd118;
LAB_005dd178:
                    /* try { // try from 005dd18c to 006dd197 has its CatchHandler @ 005dc860 */
    if (*(char *)(lVar2 + (long)iVar1 * 2000 + 0x440) == '\0') {
LAB_005dd1f4:
                    /* try { // try from 005dd200 to 006dd20f has its CatchHandler @ 005dd2e4 */
      if (*(char *)(lVar2 + (long)iVar1 * 2000 + 0x480) != '\0') goto LAB_005dd204;
      goto LAB_005dd260;
    }
LAB_005dd190:
                    /* try { // try from 005dd198 to 006dd1a7 has its CatchHandler @ 005dd258 */
                    /* try { // try from 005dd1ac to 006dd1e7 has its CatchHandler @ 005dd254 */
    iVar5 = FUN_005ddae0(0,lVar2 + (long)iVar1 * 2000 + 0x440,param_1 + 0x16,param_1[1]);
    iVar1 = *param_1;
    lVar2 = *param_2;
    param_1[0xb] = iVar5;
    if ((param_3 & 1) == 0) goto LAB_005dd1f4;
    iVar5 = FUN_005ddae0(0,lVar2 + (long)iVar1 * 2000 + 0x480,param_1 + 0x16,param_1[1]);
    iVar1 = *param_1;
                    /* try { // try from 005dd1e8 to 006dd1ff has its CatchHandler @ 005dc860 */
    lVar2 = *param_2;
    param_1[0xc] = iVar5;
LAB_005dd270:
                    /* catch() { ... } // from try @ 005dc990 with catch @ 005dd270 */
                    /* catch() { ... } // from try @ 005dc964 with catch @ 005dd274 */
                    /* catch() { ... } // from try @ 005dc908 with catch @ 005dd278 */
                    /* catch() { ... } // from try @ 005dcfa0 with catch @ 005dd27c */
                    /* catch() { ... } // from try @ 005dca6c with catch @ 005dd280 */
                    /* catch() { ... } // from try @ 005dca2c with catch @ 005dd284 */
                    /* catch() { ... } // from try @ 005dca20 with catch @ 005dd28c */
    iVar1 = FUN_005ddae0(0x437f0000,lVar2 + (long)iVar1 * 2000 + 0x4c0,param_1 + 0x16,param_1[1]);
    param_1[0xd] = iVar1;
                    /* catch() { ... } // from try @ 005dca14 with catch @ 005dd294 */
    if ((param_3 & 1) != 0) goto LAB_005dd298;
    iVar1 = *param_1;
    lVar2 = *param_2;
LAB_005dd2e4:
                    /* catch() { ... } // from try @ 005dd200 with catch @ 005dd2e4 */
    if (*(char *)(lVar2 + (long)iVar1 * 2000 + 0x500) != '\0') goto LAB_005dd2f8;
LAB_005dd350:
    if (*(char *)(lVar2 + (long)iVar1 * 2000 + 0x580) != '\0') {
LAB_005dd368:
      iVar1 = FUN_005ddae0(0,lVar2 + (long)iVar1 * 2000 + 0x580,param_1 + 0x16,param_1[1]);
      param_1[0xf] = iVar1;
      if ((param_3 & 1) != 0) goto LAB_005dd390;
      iVar1 = *param_1;
      lVar2 = *param_2;
    }
    if (*(char *)(lVar2 + (long)iVar1 * 2000 + 0x5c0) != '\0') goto LAB_005dd3e8;
LAB_005dd45c:
    if (*(char *)(lVar2 + (long)iVar1 * 2000 + 0x640) != '\0') goto LAB_005dd470;
LAB_005dd4d0:
    if (*(char *)(lVar2 + (long)iVar1 * 2000 + 0x6c0) == '\0') {
LAB_005dd54c:
      if (*(char *)(lVar2 + (long)iVar1 * 2000 + 0x700) != '\0') goto LAB_005dd55c;
      goto LAB_005dd5c0;
    }
LAB_005dd4e8:
                    /* try { // try from 005dd504 to 006dd513 has its CatchHandler @ 005ddeb4 */
    iVar5 = FUN_005ddae0(0,lVar2 + (long)iVar1 * 2000 + 0x6c0,param_1 + 0x16,param_1[1]);
    iVar1 = *param_1;
    lVar2 = *param_2;
    param_1[0x12] = iVar5;
                    /* try { // try from 005dd514 to 006dd51f has its CatchHandler @ 005ddeac */
    if ((param_3 & 1) == 0) goto LAB_005dd54c;
                    /* try { // try from 005dd520 to 006dd52b has its CatchHandler @ 005ddea4 */
                    /* try { // try from 005dd52c to 006dd537 has its CatchHandler @ 005dde9c */
                    /* try { // try from 005dd538 to 006dd547 has its CatchHandler @ 005dde94 */
    iVar5 = FUN_005ddae0(0,lVar2 + (long)iVar1 * 2000 + 0x700,param_1 + 0x16,param_1[1]);
    iVar1 = *param_1;
    lVar2 = *param_2;
    param_1[0x13] = iVar5;
LAB_005dd5d0:
    iVar5 = FUN_005ddae0(0,lVar2 + (long)iVar1 * 2000 + 0x740,param_1 + 0x16,param_1[1]);
    iVar1 = *param_1;
    lVar2 = *param_2;
    param_1[0x14] = iVar5;
    if ((param_3 & 1) == 0) {
LAB_005dd634:
      if (*(char *)(lVar2 + (long)iVar1 * 2000 + 0x780) != '\0') goto LAB_005dd644;
      goto LAB_005dd6a4;
    }
    iVar5 = FUN_005ddae0(0,lVar2 + (long)iVar1 * 2000 + 0x780,param_1 + 0x16,param_1[1]);
    iVar1 = *param_1;
    lVar2 = *param_2;
    param_1[0x15] = iVar5;
LAB_005dd6b4:
                    /* try { // try from 005dd6c8 to 006dd6df has its CatchHandler @ 005dde8c */
    iVar5 = FUN_005dd790(lVar2 + (long)iVar1 * 2000 + 0xc0,param_1 + 0x16,param_1[1],0);
    iVar1 = *param_1;
    lVar2 = *param_2;
    param_1[3] = iVar5;
    if ((param_3 & 1) != 0) {
      iVar5 = FUN_005dd790(lVar2 + (long)iVar1 * 2000 + 0x140,param_1 + 0x16,param_1[1],0);
      iVar1 = *param_1;
      lVar2 = *param_2;
      param_1[4] = iVar5;
      goto LAB_005dd760;
    }
LAB_005dd710:
    if (*(char *)(lVar2 + (long)iVar1 * 2000 + 0x140) != '\0') goto LAB_005dd720;
  }
  else {
    iVar1 = FUN_005dd790(lVar3 + 0x40,param_1 + 0x16,0xffffffff,0);
    lVar3 = *param_2;
    param_1[1] = iVar1;
    lVar3 = lVar3 + (long)*param_1 * 2000;
    lVar2 = lVar3 + 0x1c0;
    if (*(char *)(lVar3 + 0x200) != '\0') {
      lVar2 = lVar3 + 0x200;
    }
    iVar5 = FUN_005ddae0(0,lVar2,param_1 + 0x16,iVar1);
    iVar1 = *param_1;
    lVar2 = *param_2;
    param_1[6] = iVar5;
    lVar3 = lVar2 + (long)iVar1 * 2000;
    if (*(char *)(lVar3 + 0x280) != '\0') {
      iVar5 = FUN_005ddae0(0,lVar3 + 0x280,param_1 + 0x16,param_1[1]);
      iVar1 = *param_1;
      lVar2 = *param_2;
      param_1[7] = iVar5;
      goto LAB_005dcf94;
    }
LAB_005dcf28:
    iVar5 = FUN_005ddae0(0,lVar2 + (long)iVar1 * 2000 + 0x240,param_1 + 0x16,param_1[1]);
    iVar1 = *param_1;
    lVar2 = *param_2;
    param_1[7] = iVar5;
    if ((param_3 & 1) == 0) goto LAB_005dcf80;
    iVar1 = FUN_005dd790(lVar2 + (long)iVar1 * 2000 + 0x80,param_1 + 0x16,param_1[1],0);
    param_1[2] = iVar1;
LAB_005dcfb8:
    iVar1 = *param_1;
    lVar2 = *param_2;
    lVar3 = lVar2 + (long)iVar1 * 2000;
    if (*(char *)(lVar3 + 0x300) == '\0') {
LAB_005dd010:
                    /* try { // try from 005dd014 to 006dd01f has its CatchHandler @ 005dd250 */
      iVar1 = FUN_005ddae0(0x3f800000,lVar2 + (long)iVar1 * 2000 + 0x2c0,param_1 + 0x16,param_1[1]);
      param_1[8] = iVar1;
      if ((param_3 & 1) == 0) {
        iVar1 = *param_1;
                    /* try { // try from 005dd074 to 006dd07f has its CatchHandler @ 005dd260 */
        lVar2 = *param_2;
        goto LAB_005dd07c;
      }
    }
    else {
                    /* try { // try from 005dcfd8 to 006dcfe3 has its CatchHandler @ 005dd26c */
      iVar1 = FUN_005ddae0(0,lVar3 + 0x300,param_1 + 0x16,param_1[1]);
      param_1[8] = iVar1;
    }
    iVar1 = *param_1;
                    /* try { // try from 005dd040 to 006dd04b has its CatchHandler @ 005dd268 */
    lVar2 = *param_2;
    lVar3 = lVar2 + (long)iVar1 * 2000;
    if (*(char *)(lVar3 + 0x380) == '\0') {
LAB_005dd090:
      iVar1 = FUN_005ddae0(0x3f800000,lVar2 + (long)iVar1 * 2000 + 0x340,param_1 + 0x16,param_1[1]);
      param_1[9] = iVar1;
      if ((param_3 & 1) == 0) {
        iVar1 = *param_1;
        lVar2 = *param_2;
        goto LAB_005dd104;
      }
    }
    else {
      iVar1 = FUN_005ddae0(0,lVar3 + 0x380,param_1 + 0x16,param_1[1]);
      param_1[9] = iVar1;
    }
    iVar1 = *param_1;
    lVar2 = *param_2;
    lVar3 = lVar2 + (long)iVar1 * 2000;
    if (*(char *)(lVar3 + 0x400) != '\0') {
                    /* try { // try from 005dd0d4 to 006dd0df has its CatchHandler @ 005dd264 */
      iVar5 = FUN_005ddae0(0,lVar3 + 0x400,param_1 + 0x16,param_1[1]);
      iVar1 = *param_1;
      lVar2 = *param_2;
      param_1[10] = iVar5;
      goto LAB_005dd190;
    }
LAB_005dd118:
    iVar5 = FUN_005ddae0(0x3f800000,lVar2 + (long)iVar1 * 2000 + 0x3c0,param_1 + 0x16,param_1[1]);
    iVar1 = *param_1;
    lVar2 = *param_2;
    param_1[10] = iVar5;
    if ((param_3 & 1) == 0) goto LAB_005dd178;
                    /* try { // try from 005dd164 to 006dd18b has its CatchHandler @ 005dd2f4 */
    iVar5 = FUN_005ddae0(0,lVar2 + (long)iVar1 * 2000 + 0x440,param_1 + 0x16,param_1[1]);
    iVar1 = *param_1;
    lVar2 = *param_2;
    param_1[0xb] = iVar5;
LAB_005dd204:
                    /* try { // try from 005dd214 to 006dd24f has its CatchHandler @ 005dd2c0 */
    iVar5 = FUN_005ddae0(0,lVar2 + (long)iVar1 * 2000 + 0x480,param_1 + 0x16,param_1[1]);
    iVar1 = *param_1;
    lVar2 = *param_2;
    param_1[0xc] = iVar5;
    if ((param_3 & 1) == 0) {
LAB_005dd260:
                    /* catch() { ... } // from try @ 005dd074 with catch @ 005dd260 */
                    /* catch() { ... } // from try @ 005dd0d4 with catch @ 005dd264 */
                    /* catch() { ... } // from try @ 005dd040 with catch @ 005dd268 */
                    /* catch() { ... } // from try @ 005dcfd8 with catch @ 005dd26c */
      if (*(char *)(lVar2 + (long)iVar1 * 2000 + 0x4c0) != '\0') goto LAB_005dd270;
      goto LAB_005dd2e4;
    }
                    /* catch() { ... } // from try @ 005dd014 with catch @ 005dd250
                       try { // try from 005dd250 to 006dd347 has its CatchHandler @ 005dc860 */
                    /* catch() { ... } // from try @ 005dd1ac with catch @ 005dd254 */
    iVar1 = FUN_005ddae0(0x437f0000,lVar2 + (long)iVar1 * 2000 + 0x4c0,param_1 + 0x16,param_1[1]);
                    /* catch() { ... } // from try @ 005dd198 with catch @ 005dd258 */
    param_1[0xd] = iVar1;
                    /* catch() { ... } // from try @ 005dd108 with catch @ 005dd25c */
LAB_005dd298:
    iVar1 = *param_1;
                    /* catch() { ... } // from try @ 005dca08 with catch @ 005dd29c */
                    /* catch() { ... } // from try @ 005dc93c with catch @ 005dd2a0 */
    lVar2 = *param_2;
    lVar3 = lVar2 + (long)iVar1 * 2000;
    if (*(char *)(lVar3 + 0x540) != '\0') {
                    /* catch() { ... } // from try @ 005dc92c with catch @ 005dd2b4 */
                    /* catch() { ... } // from try @ 005dd214 with catch @ 005dd2c0 */
      iVar5 = FUN_005ddae0(0,lVar3 + 0x540,param_1 + 0x16,param_1[1]);
      iVar1 = *param_1;
      lVar2 = *param_2;
      param_1[0xe] = iVar5;
      goto LAB_005dd368;
    }
LAB_005dd2f8:
    iVar5 = FUN_005ddae0(0,lVar2 + (long)iVar1 * 2000 + 0x500,param_1 + 0x16,param_1[1]);
    iVar1 = *param_1;
                    /* catch() { ... } // from try @ 005dc9dc with catch @ 005dd31c */
    lVar2 = *param_2;
    param_1[0xe] = iVar5;
    if ((param_3 & 1) == 0) goto LAB_005dd350;
    iVar1 = FUN_005ddae0(0,lVar2 + (long)iVar1 * 2000 + 0x580,param_1 + 0x16,param_1[1]);
                    /* try { // try from 005dd348 to 006dd503 has its CatchHandler @ 005dd348
                       catch() { ... } // from try @ 005dd348 with catch @ 005dd348
                       catch() { ... } // from try @ 005ddbe8 with catch @ 005dd348
                       catch() { ... } // from try @ 005ddddc with catch @ 005dd348
                       catch() { ... } // from try @ 005dde68 with catch @ 005dd348 */
    param_1[0xf] = iVar1;
LAB_005dd390:
    iVar1 = *param_1;
    lVar2 = *param_2;
    lVar3 = lVar2 + (long)iVar1 * 2000;
    if (*(char *)(lVar3 + 0x600) == '\0') {
LAB_005dd3e8:
      iVar1 = FUN_005ddae0(0,lVar2 + (long)iVar1 * 2000 + 0x5c0,param_1 + 0x16,param_1[1]);
      param_1[0x10] = iVar1;
      if ((param_3 & 1) == 0) {
        iVar1 = *param_1;
        lVar2 = *param_2;
        goto LAB_005dd45c;
      }
    }
    else {
      iVar1 = FUN_005ddae0(0,lVar3 + 0x600,param_1 + 0x16,param_1[1]);
      param_1[0x10] = iVar1;
    }
    iVar1 = *param_1;
    lVar2 = *param_2;
    lVar3 = lVar2 + (long)iVar1 * 2000;
    if (*(char *)(lVar3 + 0x680) != '\0') {
      iVar5 = FUN_005ddae0(0,lVar3 + 0x680,param_1 + 0x16,param_1[1]);
      iVar1 = *param_1;
      lVar2 = *param_2;
      param_1[0x11] = iVar5;
      goto LAB_005dd4e8;
    }
LAB_005dd470:
    iVar5 = FUN_005ddae0(0,lVar2 + (long)iVar1 * 2000 + 0x640,param_1 + 0x16,param_1[1]);
    iVar1 = *param_1;
    lVar2 = *param_2;
    param_1[0x11] = iVar5;
    if ((param_3 & 1) == 0) goto LAB_005dd4d0;
    iVar5 = FUN_005ddae0(0,lVar2 + (long)iVar1 * 2000 + 0x6c0,param_1 + 0x16,param_1[1]);
    iVar1 = *param_1;
    lVar2 = *param_2;
    param_1[0x12] = iVar5;
LAB_005dd55c:
    iVar5 = FUN_005ddae0(0,lVar2 + (long)iVar1 * 2000 + 0x700,param_1 + 0x16,param_1[1]);
    iVar1 = *param_1;
    lVar2 = *param_2;
    param_1[0x13] = iVar5;
    if ((param_3 & 1) == 0) {
LAB_005dd5c0:
      if (*(char *)(lVar2 + (long)iVar1 * 2000 + 0x740) != '\0') goto LAB_005dd5d0;
      goto LAB_005dd634;
    }
    iVar5 = FUN_005ddae0(0,lVar2 + (long)iVar1 * 2000 + 0x740,param_1 + 0x16,param_1[1]);
    iVar1 = *param_1;
    lVar2 = *param_2;
    param_1[0x14] = iVar5;
LAB_005dd644:
    iVar5 = FUN_005ddae0(0,lVar2 + (long)iVar1 * 2000 + 0x780,param_1 + 0x16,param_1[1]);
    iVar1 = *param_1;
    lVar2 = *param_2;
    param_1[0x15] = iVar5;
    if ((param_3 & 1) == 0) {
LAB_005dd6a4:
      if (*(char *)(lVar2 + (long)iVar1 * 2000 + 0xc0) != '\0') goto LAB_005dd6b4;
      goto LAB_005dd710;
    }
    iVar5 = FUN_005dd790(lVar2 + (long)iVar1 * 2000 + 0xc0,param_1 + 0x16,param_1[1],0);
    iVar1 = *param_1;
    lVar2 = *param_2;
    param_1[3] = iVar5;
LAB_005dd720:
    iVar5 = FUN_005dd790(lVar2 + (long)iVar1 * 2000 + 0x140,param_1 + 0x16,param_1[1],0);
    iVar1 = *param_1;
    lVar2 = *param_2;
    param_1[4] = iVar5;
    if ((param_3 & 1) != 0) goto LAB_005dd760;
  }
  if (*(char *)(lVar2 + (long)iVar1 * 2000 + 0x180) == '\0') {
    return;
  }
LAB_005dd760:
  iVar1 = FUN_005dd790(lVar2 + (long)iVar1 * 2000 + 0x180,param_1 + 0x16,param_1[1],0);
  param_1[5] = iVar1;
  return;
}

~~~
