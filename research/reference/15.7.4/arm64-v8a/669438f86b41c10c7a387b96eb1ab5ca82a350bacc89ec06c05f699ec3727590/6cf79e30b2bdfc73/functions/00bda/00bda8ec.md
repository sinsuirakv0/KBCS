# 00bda8ec

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

ページ 1/1。[入口](00bda8ec.md)

## 関数情報

~~~json
{
  "address": "00bda8ec",
  "name": "FUN_00bda8ec",
  "size": 456,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "69f9e3e74fb611672321366f0c09c2616fe86173bf6425ac0c18c8ea78b3f10a",
  "source_text_sha256": "69f9e3e74fb611672321366f0c09c2616fe86173bf6425ac0c18c8ea78b3f10a"
}
~~~
## 呼び出し元

- [00bda3c8](../00bda/00bda3c8.md)

## 呼び出し先

- [00bd7760](../00bd7/00bd7760.md)
- [00bd94b0](../00bd9/00bd94b0.md)
- [00bd983c](../00bd9/00bd983c.md)

## 疑似コード 1/1 / UTF-8 2598 bytes

~~~c

undefined8
FUN_00bda8ec(undefined8 param_1,ulong param_2,uint *param_3,long param_4,uint *param_5,
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
    if (puVar9 <= puVar3) {
      return 0;
    }
    local_68 = puVar3 + 1;
    uVar8 = (ulong)*puVar3;
    if (*puVar3 == 0xffffffff) {
      uVar8 = *(ulong *)(puVar3 + 1);
      local_68 = puVar3 + 3;
    }
                    /* try { // try from 00bda978 to 00cda9eb has its CatchHandler @ 00bda978
                       catch() { ... } // from try @ 00bda978 with catch @ 00bda978
                       catch() { ... } // from try @ 00bdaa00 with catch @ 00bda978 */
    if (uVar8 == 0) break;
    puVar1 = (uint *)((long)local_68 + uVar8);
    if ((((*local_68 != 0) &&
         (puVar7 = (uint *)((long)local_68 - (ulong)*local_68), param_3 <= puVar7)) &&
        (puVar7 < puVar9)) && (lVar4 = FUN_00bd7760(param_1,puVar7,param_7), lVar4 == 0)) {
      local_68 = local_68 + 1;
      uVar8 = FUN_00bd94b0(param_1,&local_68,puVar1,*(undefined1 *)(param_7 + 0x18),0);
                    /* try { // try from 00bda9ec to 00cda9ff has its CatchHandler @ 00bdaabc */
      lVar4 = FUN_00bd94b0(param_1,&local_68,puVar1,*(byte *)(param_7 + 0x18) & 0xf,0);
                    /* try { // try from 00bdaa00 to 00cdaafb has its CatchHandler @ 00bda978 */
      if ((uVar8 < param_2) && (param_2 <= lVar4 + uVar8)) {
        bVar2 = *(byte *)(param_7 + 0x31);
        param_6[5] = 0;
        puVar9 = local_68;
        if ((bVar2 & 1) != 0) {
          lVar5 = FUN_00bd983c(&local_68,puVar1);
          puVar7 = local_68;
          puVar9 = (uint *)((long)local_68 + lVar5);
          if ((*(byte *)(param_7 + 0x19) != 0xff) &&
             (lVar5 = FUN_00bd94b0(param_1,&local_68,puVar1,*(byte *)(param_7 + 0x19) & 0xf,0),
             lVar5 != 0)) {
            local_68 = puVar7;
            uVar6 = FUN_00bd94b0(param_1,&local_68,puVar1,*(undefined1 *)(param_7 + 0x19),0);
            param_6[5] = uVar6;
          }
        }
        param_6[2] = puVar9;
        param_6[3] = uVar8;
        *param_6 = puVar3;
        param_6[1] = (long)puVar1 - (long)puVar3;
        param_6[4] = lVar4 + uVar8;
        return 1;
      }
    }
  }
  return 0;
}

~~~
