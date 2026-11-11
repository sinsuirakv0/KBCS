# 00aae1cc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00aae1cc",
  "name": "FUN_00aae1cc",
  "size": 268,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "05b381d2458457e7f12195191b15e1cd4af28555fcf200f17d2ab3dcbea03cfe",
  "source_text_sha256": "05b381d2458457e7f12195191b15e1cd4af28555fcf200f17d2ab3dcbea03cfe"
}
~~~

## 呼び出し元

- [00aa78e0](../00aa7/00aa78e0.md)
- [00aa84a4](../00aa8/00aa84a4.md)

## 呼び出し先

- [0043bb20](../0043b/0043bb20.md)
- [0043bba4](../0043b/0043bba4.md)
- [00aae2fc](../00aae/00aae2fc.md)
- [00c57e90](../00c57/00c57e90.md)
- [00c57ee0](../00c57/00c57ee0.md)

## 疑似コード / UTF-8 2336 bytes

~~~c

undefined8 * FUN_00aae1cc(long *param_1,undefined8 param_2,undefined8 param_3,undefined4 *param_4)

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
  puVar3 = (undefined8 *)FUN_00aae2fc(param_1,param_2,&local_68,auStack_70,param_3);
  puVar6 = (undefined8 *)*puVar3;
  if (puVar6 == (undefined8 *)0x0) {
    puVar6 = (undefined8 *)_Znwm(0x40);
    bVar1 = *(byte *)(param_4 + 2);
    local_50 = 0;
    *(undefined4 *)(puVar6 + 4) = *param_4;
                    /* catch() { ... } // from try @ 00aae18c with catch @ 00aae244 */
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
      FUN_0043bb20(puVar6 + 5,*(undefined8 *)(param_4 + 6),*(undefined8 *)(param_4 + 4));
    }
                    /* try { // try from 00aae26c to 00bae2db has its CatchHandler @ 00aae26c
                       catch() { ... } // from try @ 00aae26c with catch @ 00aae26c
                       catch() { ... } // from try @ 00aae330 with catch @ 00aae26c
                       catch() { ... } // from try @ 00aae39c with catch @ 00aae26c
                       catch() { ... } // from try @ 00aae44c with catch @ 00aae26c
                       catch() { ... } // from try @ 00aae5a0 with catch @ 00aae26c */
    *puVar6 = 0;
    puVar6[1] = 0;
    puVar6[2] = local_68;
    *puVar3 = puVar6;
    puVar5 = puVar6;
    if (*(long *)*param_1 != 0) {
      *param_1 = *(long *)*param_1;
      puVar5 = (undefined8 *)*puVar3;
    }
    puVar3 = (undefined8 *)FUN_0043bba4(param_1[1],puVar5);
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
                    /* try { // try from 00aae2f8 to 00bae303 has its CatchHandler @ 00aae8d4 */
  __stack_chk_fail(puVar3,uVar4);
}

~~~
