# 00bbffc0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bbffc0.md)

## 関数情報

~~~json
{
  "address": "00bbffc0",
  "name": "FUN_00bbffc0",
  "size": 244,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f1330d8a4117a1246de2e2ac269bc94ab2d910f5a1119e28c5435a99e41e3213",
  "source_text_sha256": "f1330d8a4117a1246de2e2ac269bc94ab2d910f5a1119e28c5435a99e41e3213"
}
~~~
## 呼び出し元

- [00bbd1fc](../00bbd/00bbd1fc.md)

## 呼び出し先

- [00bdb0d0](../00bdb/00bdb0d0.md)
- [00bdd0d0](../00bdd/00bdd0d0.md)

## 疑似コード 1/1 / UTF-8 1934 bytes

~~~c

void FUN_00bbffc0(long param_1,undefined8 *param_2,undefined8 *param_3,undefined8 *param_4,
                 undefined8 *param_5,undefined8 *param_6,undefined4 *param_7,undefined1 *param_8)

{
  undefined4 uVar1;
  undefined1 uVar2;
  undefined8 *puVar3;
  long lVar4;
  undefined8 uVar5;
  undefined8 uVar6;
  undefined8 uVar7;
  void *pvVar8;
  undefined8 uVar9;
  undefined8 uVar10;
  
                    /* try { // try from 00bbffd0 to 00cbffdb has its CatchHandler @ 00bc8b70 */
  pvVar8 = *(void **)(param_1 + 0x1330);
  lVar4 = *(long *)((long)pvVar8 + 8);
  puVar3 = pvVar8;
  if (lVar4 - 4000U < 0xfffffffffffff010) {
    puVar3 = malloc(0x1000);
    if (puVar3 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
      std::terminate();
    }
    lVar4 = 0;
    *puVar3 = pvVar8;
    puVar3[1] = 0;
    *(undefined8 **)(param_1 + 0x1330) = puVar3;
  }
  *(long *)((long)puVar3 + 8) = lVar4 + 0x50;
  *(undefined ***)((long)puVar3 + lVar4 + 0x10) = &PTR_FUN_00c198c8;
  uVar1 = *param_7;
                    /* try { // try from 00bc0054 to 00cc005b has its CatchHandler @ 00bc8b44 */
  uVar2 = *param_8;
  *(undefined1 *)((long)puVar3 + lVar4 + 0x18) = 0x13;
  uVar5 = *param_3;
  uVar6 = *param_5;
  uVar7 = *param_6;
  uVar10 = param_4[1];
  uVar9 = *param_4;
  *(undefined8 *)((long)puVar3 + lVar4 + 0x20) = *param_2;
  *(undefined8 *)((long)puVar3 + lVar4 + 0x28) = uVar5;
  *(ushort *)((long)puVar3 + lVar4 + 0x19) =
       *(ushort *)((long)puVar3 + lVar4 + 0x19) & 0xf000 | 0x100;
  *(undefined8 *)((long)puVar3 + lVar4 + 0x38) = uVar10;
  *(undefined8 *)((long)puVar3 + lVar4 + 0x30) = uVar9;
  *(undefined8 *)((long)puVar3 + lVar4 + 0x40) = uVar6;
  *(undefined8 *)((long)puVar3 + lVar4 + 0x48) = uVar7;
  *(undefined4 *)((long)puVar3 + lVar4 + 0x50) = uVar1;
  *(undefined1 *)((long)puVar3 + lVar4 + 0x54) = uVar2;
  return;
}

~~~
