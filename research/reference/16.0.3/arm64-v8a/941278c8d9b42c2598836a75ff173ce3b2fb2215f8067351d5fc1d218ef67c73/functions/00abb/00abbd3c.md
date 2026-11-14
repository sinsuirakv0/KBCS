# 00abbd3c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00abbd3c",
  "name": "FUN_00abbd3c",
  "size": 676,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2bba40da582e96b93d1e1d5aaf37d25c82ffca55887efd6fab44c2f1d45b30d7",
  "source_text_sha256": "2bba40da582e96b93d1e1d5aaf37d25c82ffca55887efd6fab44c2f1d45b30d7"
}
~~~

## 呼び出し元

- [005fea5c](../005fe/005fea5c.md)
- [00ab4208](../00ab4/00ab4208.md)
- [00ab77a4](../00ab7/00ab77a4.md)

## 呼び出し先

- [0043bf04](../0043b/0043bf04.md)
- [008524fc](../00852/008524fc.md)
- [00aba21c](../00aba/00aba21c.md)
- [00c58f30](../00c58/00c58f30.md)
- [00c58f50](../00c58/00c58f50.md)
- [00c58f80](../00c58/00c58f80.md)

## 疑似コード / UTF-8 5054 bytes

~~~c

bool FUN_00abbd3c(int param_1,undefined4 param_2)

{
  long lVar1;
  long lVar2;
  undefined8 *puVar3;
  undefined8 *puVar4;
  undefined8 *puVar5;
  long lVar6;
  bool bVar7;
  undefined8 *puVar8;
  undefined8 *puVar9;
  long lVar10;
  int iVar11;
  int local_98 [2];
  void *local_90;
  void *local_88;
  long local_68;
  
  lVar1 = tpidr_el0;
  local_68 = *(long *)(lVar1 + 0x28);
  if (param_1 == 3) {
    bVar7 = false;
  }
  else {
    lVar10 = 0;
    do {
      lVar2 = FUN_008524fc();
                    /* try { // try from 00abbdc0 to 00bbbdcb has its CatchHandler @ 00abdcd8 */
      FUN_00aba21c(local_98,(long)&uleb128_0029a6e0 + lVar2,param_1,param_2);
                    /* try { // try from 00abbdcc to 00bbbddf has its CatchHandler @ 00abdcb4 */
      lVar2 = (long)local_98[0];
      bVar7 = lVar2 <= lVar10;
      if (local_90 != (void *)0x0) {
        local_88 = local_90;
        _ZdlPv(local_90);
      }
      if (lVar2 <= lVar10) {
        bVar7 = true;
        break;
      }
      lVar2 = FUN_008524fc();
      FUN_00aba21c(local_98,(long)&uleb128_0029a6e0 + lVar2,param_1,param_2);
      iVar11 = *(int *)((long)local_90 + lVar10 * 4);
      local_88 = local_90;
      _ZdlPv(local_90);
                    /* try { // try from 00abbe18 to 00bbbe23 has its CatchHandler @ 00abdc40 */
      if (iVar11 < 0x2e) {
        lVar2 = FUN_008524fc();
                    /* try { // try from 00abbe24 to 00bbbe33 has its CatchHandler @ 00abdb94 */
                    /* try { // try from 00abbe34 to 00bbbe4f has its CatchHandler @ 00abdafc */
        FUN_00aba21c(local_98,(long)&uleb128_0029a6e0 + lVar2,param_1,param_2);
        iVar11 = 0x2d - *(int *)((long)local_90 + lVar10 * 4);
      }
      else {
                    /* try { // try from 00abbe50 to 00bbbfb3 has its CatchHandler @ 00abbd00 */
        lVar2 = FUN_008524fc();
        FUN_00aba21c(local_98,(long)&uleb128_0029a6e0 + lVar2,param_1,param_2);
        iVar11 = *(int *)((long)local_90 + lVar10 * 4);
      }
      local_88 = local_90;
      _ZdlPv(local_90);
      lVar2 = FUN_008524fc();
      puVar8 = (undefined8 *)((long)&fde_table_entry_003380d8.initial_loc + lVar2);
      puVar5 = (undefined8 *)*puVar8;
      puVar9 = puVar8;
      if ((undefined8 *)*puVar8 != (undefined8 *)0x0) {
        do {
          while (puVar3 = puVar5, puVar9 = puVar3, param_1 < *(int *)(puVar3 + 4)) {
            puVar5 = (undefined8 *)*puVar3;
            puVar8 = puVar3;
            if ((undefined8 *)*puVar3 == (undefined8 *)0x0) goto LAB_00abbec0;
          }
          if (param_1 <= *(int *)(puVar3 + 4)) goto LAB_00abbf1c;
          puVar5 = (undefined8 *)puVar3[1];
        } while ((undefined8 *)puVar3[1] != (undefined8 *)0x0);
        puVar8 = puVar3 + 1;
      }
LAB_00abbec0:
      puVar3 = (undefined8 *)_Znwm(0x40);
      *(int *)(puVar3 + 4) = param_1;
      puVar3[7] = 0;
      puVar3[6] = 0;
      puVar3[5] = puVar3 + 6;
      *puVar3 = 0;
      puVar3[1] = 0;
      puVar3[2] = puVar9;
      *puVar8 = puVar3;
      lVar6 = **(long **)((long)&fde_table_entry_003380d0.initial_loc + lVar2);
      puVar5 = puVar3;
      if (lVar6 != 0) {
        *(long *)((long)&fde_table_entry_003380d0.initial_loc + lVar2) = lVar6;
        puVar5 = (undefined8 *)*puVar8;
      }
      FUN_0043bf04(*(undefined8 *)((long)&fde_table_entry_003380d8.initial_loc + lVar2),puVar5);
      *(long *)((long)&fde_table_entry_003380e0.initial_loc + lVar2) =
           *(long *)((long)&fde_table_entry_003380e0.initial_loc + lVar2) + 1;
LAB_00abbf1c:
      puVar8 = puVar3 + 6;
      puVar5 = (undefined8 *)*puVar8;
      puVar9 = puVar8;
      if ((undefined8 *)*puVar8 != (undefined8 *)0x0) {
        do {
          while (puVar4 = puVar5, puVar9 = puVar4, iVar11 < *(int *)((long)puVar4 + 0x1c)) {
            puVar5 = (undefined8 *)*puVar4;
            puVar8 = puVar4;
            if ((undefined8 *)*puVar4 == (undefined8 *)0x0) goto LAB_00abbf60;
          }
          if (iVar11 <= *(int *)((long)puVar4 + 0x1c)) goto LAB_00abbda8;
          puVar5 = (undefined8 *)puVar4[1];
        } while ((undefined8 *)puVar4[1] != (undefined8 *)0x0);
        puVar8 = puVar4 + 1;
      }
LAB_00abbf60:
      puVar4 = (undefined8 *)_Znwm(0x28);
      *(int *)((long)puVar4 + 0x1c) = iVar11;
      *(undefined1 *)(puVar4 + 4) = 0;
      *puVar4 = 0;
      puVar4[1] = 0;
      puVar4[2] = puVar9;
      *puVar8 = puVar4;
      puVar5 = puVar4;
      if (*(long *)puVar3[5] != 0) {
        puVar3[5] = *(long *)puVar3[5];
        puVar5 = (undefined8 *)*puVar8;
      }
      FUN_0043bf04(puVar3[6],puVar5);
                    /* try { // try from 00abbd9c to 00bbbda3 has its CatchHandler @ 00abdcf4 */
      puVar3[7] = puVar3[7] + 1;
LAB_00abbda8:
      lVar10 = lVar10 + 1;
    } while ((*(byte *)(puVar4 + 4) & 1) != 0);
  }
                    /* try { // try from 00abbfb4 to 00bbbfc3 has its CatchHandler @ 00abda58 */
  if (*(long *)(lVar1 + 0x28) != local_68) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return bVar7;
}

~~~
