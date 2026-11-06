# 00adb2ac

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

ページ 1/1。[入口](00adb2ac.md)

## 関数情報

~~~json
{
  "address": "00adb2ac",
  "name": "FUN_00adb2ac",
  "size": 284,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e0de78bf7572dd15e99c73c3cf089118e63ac27d35fcf8a5590a345dca99aac4",
  "source_text_sha256": "e0de78bf7572dd15e99c73c3cf089118e63ac27d35fcf8a5590a345dca99aac4"
}
~~~
## 呼び出し元

- [00ad9b64](../00ad9/00ad9b64.md)

## 呼び出し先

- [00418fe0](../00418/00418fe0.md)
- [00419064](../00419/00419064.md)
- [00adb3f0](../00adb/00adb3f0.md)
- [00bdb040](../00bdb/00bdb040.md)
- [00bdb090](../00bdb/00bdb090.md)

## 疑似コード 1/1 / UTF-8 2207 bytes

~~~c

undefined8 * FUN_00adb2ac(long *param_1,undefined8 param_2,undefined8 param_3,undefined8 *param_4)

{
  long lVar1;
  undefined8 *puVar2;
  undefined8 uVar3;
  undefined8 *puVar4;
  byte *pbVar5;
  undefined8 *puVar6;
  undefined8 uVar7;
  undefined8 local_68;
  undefined8 *local_60;
  long *local_58;
  undefined1 local_50;
  long local_48;
  
                    /* try { // try from 00adb2b0 to 00bdb2c7 has its CatchHandler @ 00adb8d8 */
  lVar1 = tpidr_el0;
                    /* try { // try from 00adb2c8 to 00bdb3a7 has its CatchHandler @ 00adb014 */
  local_48 = *(long *)(lVar1 + 0x28);
  puVar2 = (undefined8 *)FUN_00adb3f0(param_1,&local_68,param_2);
  puVar6 = (undefined8 *)*puVar2;
  if (puVar6 == (undefined8 *)0x0) {
    puVar6 = (undefined8 *)_Znwm(0xd0);
    pbVar5 = (byte *)*param_4;
    local_50 = 0;
    local_60 = puVar6;
    local_58 = param_1 + 1;
    if ((*pbVar5 & 1) == 0) {
      uVar7 = *(undefined8 *)(pbVar5 + 8);
      uVar3 = *(undefined8 *)pbVar5;
      puVar6[6] = *(undefined8 *)(pbVar5 + 0x10);
      puVar6[5] = uVar7;
      puVar6[4] = uVar3;
    }
    else {
      FUN_00418fe0(puVar6 + 4,*(undefined8 *)(pbVar5 + 0x10),*(undefined8 *)(pbVar5 + 8));
    }
    *puVar6 = 0;
    puVar6[1] = 0;
    puVar6[2] = local_68;
    puVar6[0xb] = 0;
    puVar6[10] = 0;
    puVar6[0xd] = 0;
    puVar6[0xc] = 0;
    puVar6[0xf] = 0;
    puVar6[0xe] = 0;
    puVar6[0x11] = 0;
    puVar6[0x10] = 0;
    puVar6[0x13] = 0;
    puVar6[0x12] = 0;
    puVar6[0x15] = 0;
    puVar6[0x14] = 0;
    puVar6[0x17] = 0;
    puVar6[0x16] = 0;
    puVar6[0x19] = 0;
    puVar6[0x18] = 0;
    puVar6[9] = 0;
    puVar6[8] = 0;
    *puVar2 = puVar6;
    puVar4 = puVar6;
    if (*(long *)*param_1 != 0) {
      *param_1 = *(long *)*param_1;
      puVar4 = (undefined8 *)*puVar2;
    }
    puVar2 = (undefined8 *)FUN_00419064(param_1[1],puVar4);
    uVar3 = 1;
    param_1[2] = param_1[2] + 1;
  }
  else {
    uVar3 = 0;
  }
  if (*(long *)(lVar1 + 0x28) == local_48) {
                    /* try { // try from 00adb3a8 to 00bdb4f7 has its CatchHandler @ 00adb9f0 */
    return puVar6;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail(puVar2,uVar3);
}

~~~
