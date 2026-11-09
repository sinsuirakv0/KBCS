# 00abaadc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00abaadc",
  "name": "FUN_00abaadc",
  "size": 676,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "149d6d557778f4dd1b4c1a315ec57e89799b9d6aa9375d6e030ce775f4abb50b",
  "source_text_sha256": "149d6d557778f4dd1b4c1a315ec57e89799b9d6aa9375d6e030ce775f4abb50b"
}
~~~

## 呼び出し元

- [005fe62c](../005fe/005fe62c.md)
- [00ab2fa8](../00ab2/00ab2fa8.md)
- [00ab6544](../00ab6/00ab6544.md)

## 呼び出し先

- [0043bb64](../0043b/0043bb64.md)
- [008514b8](../00851/008514b8.md)
- [00ab8fbc](../00ab8/00ab8fbc.md)
- [00c57a90](../00c57/00c57a90.md)
- [00c57ab0](../00c57/00c57ab0.md)
- [00c57ae0](../00c57/00c57ae0.md)

## 疑似コード / UTF-8 6279 bytes

~~~c

bool FUN_00abaadc(int param_1,undefined4 param_2)

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
  
                    /* catch() { ... } // from try @ 00aba890 with catch @ 00abaadc */
                    /* catch() { ... } // from try @ 00aba90c with catch @ 00abaae4 */
                    /* catch() { ... } // from try @ 00aba9b8 with catch @ 00abaaec */
                    /* catch() { ... } // from try @ 00aba930 with catch @ 00abaaf4 */
  lVar1 = tpidr_el0;
  local_68 = *(long *)(lVar1 + 0x28);
  if (param_1 == 3) {
    bVar7 = false;
  }
  else {
    lVar10 = 0;
    do {
      lVar2 = FUN_008514b8();
                    /* catch() { ... } // from try @ 00abacb4 with catch @ 00abab64
                       catch() { ... } // from try @ 00abaed4 with catch @ 00abab64
                       catch() { ... } // from try @ 00abb054 with catch @ 00abab64
                       catch() { ... } // from try @ 00abb1c8 with catch @ 00abab64
                       catch() { ... } // from try @ 00abb31c with catch @ 00abab64
                       catch() { ... } // from try @ 00abb418 with catch @ 00abab64
                       catch() { ... } // from try @ 00abb6c8 with catch @ 00abab64
                       catch() { ... } // from try @ 00abb7b8 with catch @ 00abab64
                       catch() { ... } // from try @ 00abb8a8 with catch @ 00abab64
                       catch() { ... } // from try @ 00abbadc with catch @ 00abab64
                       catch() { ... } // from try @ 00abbc70 with catch @ 00abab64
                       catch() { ... } // from try @ 00abbd38 with catch @ 00abab64
                       catch() { ... } // from try @ 00abbdf0 with catch @ 00abab64 */
      FUN_00ab8fbc(local_98,&uleb128_0029a6e0 + lVar2,param_1,param_2);
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
      lVar2 = FUN_008514b8();
      FUN_00ab8fbc(local_98,&uleb128_0029a6e0 + lVar2,param_1,param_2);
      iVar11 = *(int *)((long)local_90 + lVar10 * 4);
      local_88 = local_90;
      _ZdlPv(local_90);
      if (iVar11 < 0x2e) {
        lVar2 = FUN_008514b8();
        FUN_00ab8fbc(local_98,&uleb128_0029a6e0 + lVar2,param_1,param_2);
        iVar11 = 0x2d - *(int *)((long)local_90 + lVar10 * 4);
      }
      else {
        lVar2 = FUN_008514b8();
                    /* try { // try from 00abac00 to 00bbac07 has its CatchHandler @ 00abcb58 */
        FUN_00ab8fbc(local_98,&uleb128_0029a6e0 + lVar2,param_1,param_2);
        iVar11 = *(int *)((long)local_90 + lVar10 * 4);
      }
      local_88 = local_90;
      _ZdlPv(local_90);
      lVar2 = FUN_008514b8();
      puVar8 = (undefined8 *)((long)&fde_table_entry_003380d8.initial_loc + lVar2);
                    /* try { // try from 00abac24 to 00bbac2f has its CatchHandler @ 00abcb3c */
      puVar5 = (undefined8 *)*puVar8;
      puVar9 = puVar8;
      if ((undefined8 *)*puVar8 != (undefined8 *)0x0) {
        do {
          while (puVar3 = puVar5, puVar9 = puVar3, param_1 < *(int *)(puVar3 + 4)) {
            puVar5 = (undefined8 *)*puVar3;
            puVar8 = puVar3;
            if ((undefined8 *)*puVar3 == (undefined8 *)0x0) goto LAB_00abac60;
          }
          if (param_1 <= *(int *)(puVar3 + 4)) goto LAB_00abacbc;
          puVar5 = (undefined8 *)puVar3[1];
        } while ((undefined8 *)puVar3[1] != (undefined8 *)0x0);
        puVar8 = puVar3 + 1;
      }
LAB_00abac60:
      puVar3 = (undefined8 *)_Znwm(0x40);
      *(int *)(puVar3 + 4) = param_1;
      puVar3[7] = 0;
                    /* try { // try from 00abac7c to 00bbac87 has its CatchHandler @ 00abcaa4 */
      puVar3[6] = 0;
      puVar3[5] = puVar3 + 6;
                    /* try { // try from 00abac88 to 00bbac97 has its CatchHandler @ 00abc9f8 */
      *puVar3 = 0;
      puVar3[1] = 0;
      puVar3[2] = puVar9;
      *puVar8 = puVar3;
                    /* try { // try from 00abac98 to 00bbacb3 has its CatchHandler @ 00abc960 */
      lVar6 = **(long **)((long)&fde_table_entry_003380d0.initial_loc + lVar2);
      puVar5 = puVar3;
      if (lVar6 != 0) {
        *(long *)((long)&fde_table_entry_003380d0.initial_loc + lVar2) = lVar6;
        puVar5 = (undefined8 *)*puVar8;
      }
      FUN_0043bb64(*(undefined8 *)((long)&fde_table_entry_003380d8.initial_loc + lVar2),puVar5);
                    /* try { // try from 00abacb4 to 00bbae17 has its CatchHandler @ 00abab64 */
      *(long *)((long)&fde_table_entry_003380e0.initial_loc + lVar2) =
           *(long *)((long)&fde_table_entry_003380e0.initial_loc + lVar2) + 1;
LAB_00abacbc:
      puVar8 = puVar3 + 6;
      puVar5 = (undefined8 *)*puVar8;
      puVar9 = puVar8;
      if ((undefined8 *)*puVar8 != (undefined8 *)0x0) {
        do {
          while (puVar4 = puVar5, puVar9 = puVar4, iVar11 < *(int *)((long)puVar4 + 0x1c)) {
            puVar5 = (undefined8 *)*puVar4;
            puVar8 = puVar4;
            if ((undefined8 *)*puVar4 == (undefined8 *)0x0) goto LAB_00abad00;
          }
          if (iVar11 <= *(int *)((long)puVar4 + 0x1c)) goto LAB_00abab48;
          puVar5 = (undefined8 *)puVar4[1];
        } while ((undefined8 *)puVar4[1] != (undefined8 *)0x0);
        puVar8 = puVar4 + 1;
      }
LAB_00abad00:
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
      FUN_0043bb64(puVar3[6],puVar5);
      puVar3[7] = puVar3[7] + 1;
LAB_00abab48:
      lVar10 = lVar10 + 1;
    } while ((*(byte *)(puVar4 + 4) & 1) != 0);
  }
  if (*(long *)(lVar1 + 0x28) != local_68) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return bVar7;
}

~~~
