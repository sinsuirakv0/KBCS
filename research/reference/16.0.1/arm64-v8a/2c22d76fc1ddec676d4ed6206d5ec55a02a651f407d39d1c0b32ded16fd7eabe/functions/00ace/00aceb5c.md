# 00aceb5c

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00aceb5c",
  "name": "FUN_00aceb5c",
  "size": 248,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "bd078ecf97f3b2218232503918f40ba73ba4ac5b132d9ceca682ec726317fb6b",
  "source_text_sha256": "bd078ecf97f3b2218232503918f40ba73ba4ac5b132d9ceca682ec726317fb6b"
}
~~~

## 呼び出し元

- [005e12a4](../005e1/005e12a4.md)
- [005e1620](../005e1/005e1620.md)
- [005e1750](../005e1/005e1750.md)
- [006623ec](../00662/006623ec.md)
- [00662490](../00662/00662490.md)
- [00662534](../00662/00662534.md)
- [007cceec](../007cc/007cceec.md)
- [007de8c0](../007de/007de8c0.md)
- [008c4290](../008c4/008c4290.md)
- [00a42194](../00a42/00a42194.md)
- [00a47f00](../00a47/00a47f00.md)
- [00acc5d0](../00acc/00acc5d0.md)
- [00ad0958](../00ad0/00ad0958.md)
- [00ad6f4c](../00ad6/00ad6f4c.md)
- [00aeaf94](../00aea/00aeaf94.md)
- [00aec960](../00aec/00aec960.md)

## 呼び出し先

- [0067674c](../00676/0067674c.md)
- [007bbd48](../007bb/007bbd48.md)
- [008001ec](../00800/008001ec.md)
- [008026b8](../00802/008026b8.md)
- [00802b58](../00802/00802b58.md)
- [00802ca8](../00802/00802ca8.md)
- [00802ee0](../00802/00802ee0.md)
- [008514f8](../00851/008514f8.md)
- [00a32a04](../00a32/00a32a04.md)
- [00a32e08](../00a32/00a32e08.md)
- [00a32e98](../00a32/00a32e98.md)

## 疑似コード / UTF-8 1235 bytes

~~~c

int FUN_00aceb5c(long param_1)

{
  int iVar1;
  int iVar2;
  int iVar3;
  int iVar4;
  ulong uVar5;
  long lVar6;
  undefined8 uVar7;
  
  iVar1 = FUN_00802b58(0);
  iVar2 = FUN_00802ca8();
  iVar3 = FUN_00802ee0();
  iVar4 = 1000000000;
  if (iVar3 != 3) {
    iVar4 = 0;
  }
  uVar5 = FUN_00a32a04(param_1 + 0x530,0xffffffff,0xffffffff);
  if ((uVar5 & 1) != 0) {
    iVar1 = FUN_00a32e98(param_1 + 0x530,iVar1);
    return iVar4 + iVar2 + iVar1 * 1000;
  }
  uVar5 = FUN_00a32e08(param_1 + 0x530);
  if ((uVar5 & 1) == 0) {
    iVar3 = FUN_008026b8(0);
    if (iVar3 == -8) {
      lVar6 = FUN_008514f8();
      return *(int *)(lVar6 + 0x33a0);
    }
                    /* try { // try from 00acec04 to 00bcec37 has its CatchHandler @ 00acf96c */
    uVar5 = FUN_0067674c(param_1 + 0x13d8,1);
    if ((uVar5 & 1) == 0) {
      uVar5 = FUN_007bbd48(param_1,1);
      if ((uVar5 & 1) == 0) goto LAB_00acebd4;
      uVar7 = 0x44;
    }
    else {
      uVar7 = 0x2a;
    }
                    /* try { // try from 00acec38 to 00bcec43 has its CatchHandler @ 00acf630 */
    iVar4 = FUN_008001ec(0xfffffff8,uVar7);
    iVar4 = iVar4 * 1000;
  }
  else {
LAB_00acebd4:
    iVar4 = iVar2 + iVar1 * 1000 + iVar4;
  }
  return iVar4;
}

~~~
