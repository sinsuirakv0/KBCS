# 00acfbc0

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00acfbc0",
  "name": "FUN_00acfbc0",
  "size": 248,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b17ef6a109212bb1061ad42eb98c34bdb1f04aa9f85109954c103822d689bdef",
  "source_text_sha256": "b17ef6a109212bb1061ad42eb98c34bdb1f04aa9f85109954c103822d689bdef"
}
~~~

## 呼び出し元

- [005e1694](../005e1/005e1694.md)
- [005e1a10](../005e1/005e1a10.md)
- [005e1b40](../005e1/005e1b40.md)
- [006627dc](../00662/006627dc.md)
- [00662880](../00662/00662880.md)
- [00662924](../00662/00662924.md)
- [007cdea8](../007cd/007cdea8.md)
- [007df87c](../007df/007df87c.md)
- [008c5290](../008c5/008c5290.md)
- [00a431dc](../00a43/00a431dc.md)
- [00a48f48](../00a48/00a48f48.md)
- [00acd634](../00acd/00acd634.md)
- [00ad19bc](../00ad1/00ad19bc.md)
- [00ad7fb0](../00ad7/00ad7fb0.md)
- [00aec024](../00aec/00aec024.md)
- [00aed9f0](../00aed/00aed9f0.md)

## 呼び出し先

- [00676b3c](../00676/00676b3c.md)
- [007bcd04](../007bc/007bcd04.md)
- [008011a8](../00801/008011a8.md)
- [00803674](../00803/00803674.md)
- [00803b14](../00803/00803b14.md)
- [00803c64](../00803/00803c64.md)
- [00803e9c](../00803/00803e9c.md)
- [008524fc](../00852/008524fc.md)
- [00a33a4c](../00a33/00a33a4c.md)
- [00a33e50](../00a33/00a33e50.md)
- [00a33ee0](../00a33/00a33ee0.md)

## 疑似コード / UTF-8 1623 bytes

~~~c

int FUN_00acfbc0(long param_1)

{
  int iVar1;
  int iVar2;
  int iVar3;
  int iVar4;
  ulong uVar5;
  long lVar6;
  undefined8 uVar7;
  
  iVar1 = FUN_00803b14(0);
  iVar2 = FUN_00803c64();
  iVar3 = FUN_00803e9c();
  iVar4 = 1000000000;
                    /* try { // try from 00acfc04 to 00bcfc37 has its CatchHandler @ 00ad096c */
  if (iVar3 != 3) {
    iVar4 = 0;
  }
  uVar5 = FUN_00a33a4c(param_1 + 0x530,0xffffffff,0xffffffff);
  if ((uVar5 & 1) != 0) {
    iVar1 = FUN_00a33ee0(param_1 + 0x530,iVar1);
    return iVar4 + iVar2 + iVar1 * 1000;
  }
  uVar5 = FUN_00a33e50(param_1 + 0x530);
  if ((uVar5 & 1) == 0) {
    iVar3 = FUN_00803674(0);
    if (iVar3 == -8) {
      lVar6 = FUN_008524fc();
      return *(int *)(lVar6 + 0x33a0);
    }
                    /* try { // try from 00acfc68 to 00bcfc83 has its CatchHandler @ 00ad0904 */
    uVar5 = FUN_00676b3c(param_1 + 0x13d8,1);
    if ((uVar5 & 1) == 0) {
                    /* try { // try from 00acfc84 to 00bcfc8f has its CatchHandler @ 00ad05f8 */
      uVar5 = FUN_007bcd04(param_1,1);
                    /* try { // try from 00acfc90 to 00bcfcaf has its CatchHandler @ 00ad05a4 */
      if ((uVar5 & 1) == 0) goto LAB_00acfc38;
      uVar7 = 0x44;
    }
    else {
      uVar7 = 0x2a;
    }
    iVar4 = FUN_008011a8(0xfffffff8,uVar7);
    iVar4 = iVar4 * 1000;
  }
  else {
LAB_00acfc38:
                    /* try { // try from 00acfc38 to 00bcfc43 has its CatchHandler @ 00ad0630 */
    iVar4 = iVar2 + iVar1 * 1000 + iVar4;
  }
                    /* try { // try from 00acfcb0 to 00bcfdff has its CatchHandler @ 00acdb7c */
  return iVar4;
}

~~~
