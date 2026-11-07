# 00a4ffac

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-previous -->
**別版の対応** [v15.7.2 `00a4ff68`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a4f/00a4ff68.md)
<!-- /kbcs-version-previous -->

## 関数情報

~~~json
{
  "address": "00a4ffac",
  "name": "FUN_00a4ffac",
  "size": 268,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ba3eea9ac3d775ecda42c30a98dc174be70de6101201c9c32d83f6137e4c2436",
  "source_text_sha256": "ba3eea9ac3d775ecda42c30a98dc174be70de6101201c9c32d83f6137e4c2436"
}
~~~

## 呼び出し元

- [00a496c0](../00a49/00a496c0.md)
- [00a4a284](../00a4a/00a4a284.md)

## 呼び出し先

- [00418fe0](../00418/00418fe0.md)
- [00419064](../00419/00419064.md)
- [00a500dc](../00a50/00a500dc.md)
- [00bdb040](../00bdb/00bdb040.md)
- [00bdb090](../00bdb/00bdb090.md)

## 疑似コード / UTF-8 1829 bytes

~~~c

undefined8 * FUN_00a4ffac(long *param_1,undefined8 param_2,undefined8 param_3,undefined4 *param_4)

{
  byte bVar1;
  long lVar2;
  undefined8 *puVar3;
  undefined8 uVar4;
  undefined8 *puVar5;
  undefined8 *puVar6;
  undefined8 uVar7;
  undefined1 auStack_70 [8];
  undefined8 local_68;
  undefined8 *local_60;
  long *plStack_58;
  undefined1 local_50;
  long local_48;
  
  lVar2 = tpidr_el0;
  local_48 = *(long *)(lVar2 + 0x28);
  puVar3 = (undefined8 *)FUN_00a500dc(param_1,param_2,&local_68,auStack_70,param_3);
  puVar6 = (undefined8 *)*puVar3;
  if (puVar6 == (undefined8 *)0x0) {
    puVar6 = (undefined8 *)_Znwm(0x40);
                    /* try { // try from 00a50010 to 00b5001f has its CatchHandler @ 00a56a3c */
    bVar1 = *(byte *)(param_4 + 2);
    local_50 = 0;
                    /* try { // try from 00a50020 to 00b5119b has its CatchHandler @ 00a4f7d0 */
    *(undefined4 *)(puVar6 + 4) = *param_4;
    local_60 = puVar6;
    plStack_58 = param_1 + 1;
    if ((bVar1 & 1) == 0) {
      uVar7 = *(undefined8 *)(param_4 + 2);
      uVar4 = *(undefined8 *)(param_4 + 6);
      puVar6[6] = *(undefined8 *)(param_4 + 4);
      puVar6[5] = uVar7;
      puVar6[7] = uVar4;
    }
    else {
      FUN_00418fe0(puVar6 + 5,*(undefined8 *)(param_4 + 6),*(undefined8 *)(param_4 + 4));
    }
    *puVar6 = 0;
    puVar6[1] = 0;
    puVar6[2] = local_68;
    *puVar3 = puVar6;
    puVar5 = puVar6;
    if (*(long *)*param_1 != 0) {
      *param_1 = *(long *)*param_1;
      puVar5 = (undefined8 *)*puVar3;
    }
    puVar3 = (undefined8 *)FUN_00419064(param_1[1],puVar5);
    uVar4 = 1;
    param_1[2] = param_1[2] + 1;
  }
  else {
    uVar4 = 0;
  }
  if (*(long *)(lVar2 + 0x28) == local_48) {
    return puVar6;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail(puVar3,uVar4);
}

~~~
