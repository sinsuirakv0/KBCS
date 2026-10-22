# 00bda7ec

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bda7ec.md)

## 関数情報

~~~json
{
  "address": "00bda7ec",
  "name": "FUN_00bda7ec",
  "size": 456,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e9dd2267bc314f80ed0b07c45d6190cc339ff58609b2d685dd80360472601a1a",
  "source_text_sha256": "e9dd2267bc314f80ed0b07c45d6190cc339ff58609b2d685dd80360472601a1a"
}
~~~
## 呼び出し元

- [00bda2c8](../00bda/00bda2c8.md)

## 呼び出し先

- [00bd7660](../00bd7/00bd7660.md)
- [00bd93b0](../00bd9/00bd93b0.md)
- [00bd973c](../00bd9/00bd973c.md)

## 疑似コード 1/1 / UTF-8 2851 bytes

~~~c

undefined8
FUN_00bda7ec(undefined8 param_1,ulong param_2,uint *param_3,long param_4,uint *param_5,
            undefined8 *param_6,long param_7)

{
  uint *puVar1;
  byte bVar2;
  uint *puVar3;
  long lVar4;
  long lVar5;
  undefined8 uVar6;
  uint *puVar7;
  ulong uVar8;
  uint *puVar9;
  uint *local_68;
  
  puVar9 = (uint *)(param_4 + (long)param_3);
  puVar1 = param_3;
  if (param_5 != (uint *)0x0) {
    puVar1 = param_5;
  }
  if (param_4 == -1) {
    puVar9 = (uint *)0xffffffffffffffff;
  }
  while( true ) {
    puVar3 = puVar1;
                    /* catch() { ... } // from try @ 00bda720 with catch @ 00bda82c */
    if (puVar9 <= puVar3) {
      return 0;
    }
    local_68 = puVar3 + 1;
    uVar8 = (ulong)*puVar3;
    if (*puVar3 == 0xffffffff) {
                    /* try { // try from 00bda86c to 00cda8df has its CatchHandler @ 00bda86c
                       catch() { ... } // from try @ 00bda86c with catch @ 00bda86c
                       catch() { ... } // from try @ 00bda8f4 with catch @ 00bda86c */
      uVar8 = *(ulong *)(puVar3 + 1);
      local_68 = puVar3 + 3;
    }
    if (uVar8 == 0) break;
    puVar1 = (uint *)((long)local_68 + uVar8);
    if ((((*local_68 != 0) &&
         (puVar7 = (uint *)((long)local_68 - (ulong)*local_68), param_3 <= puVar7)) &&
        (puVar7 < puVar9)) && (lVar4 = FUN_00bd7660(param_1,puVar7,param_7), lVar4 == 0)) {
      local_68 = local_68 + 1;
      uVar8 = FUN_00bd93b0(param_1,&local_68,puVar1,*(undefined1 *)(param_7 + 0x18),0);
                    /* try { // try from 00bda8e0 to 00cda8f3 has its CatchHandler @ 00bda9b0 */
      lVar4 = FUN_00bd93b0(param_1,&local_68,puVar1,*(byte *)(param_7 + 0x18) & 0xf,0);
                    /* try { // try from 00bda8f4 to 00cda9ef has its CatchHandler @ 00bda86c */
      if ((uVar8 < param_2) && (param_2 <= lVar4 + uVar8)) {
        bVar2 = *(byte *)(param_7 + 0x31);
        param_6[5] = 0;
        puVar9 = local_68;
        if ((bVar2 & 1) != 0) {
          lVar5 = FUN_00bd973c(&local_68,puVar1);
          puVar7 = local_68;
          puVar9 = (uint *)((long)local_68 + lVar5);
          if ((*(byte *)(param_7 + 0x19) != 0xff) &&
             (lVar5 = FUN_00bd93b0(param_1,&local_68,puVar1,*(byte *)(param_7 + 0x19) & 0xf,0),
             lVar5 != 0)) {
            local_68 = puVar7;
            uVar6 = FUN_00bd93b0(param_1,&local_68,puVar1,*(undefined1 *)(param_7 + 0x19),0);
            param_6[5] = uVar6;
          }
        }
        param_6[2] = puVar9;
        param_6[3] = uVar8;
        *param_6 = puVar3;
        param_6[1] = (long)puVar1 - (long)puVar3;
        param_6[4] = lVar4 + uVar8;
        return 1;
                    /* catch() { ... } // from try @ 00bda8e0 with catch @ 00bda9b0 */
      }
    }
  }
  return 0;
}

~~~
