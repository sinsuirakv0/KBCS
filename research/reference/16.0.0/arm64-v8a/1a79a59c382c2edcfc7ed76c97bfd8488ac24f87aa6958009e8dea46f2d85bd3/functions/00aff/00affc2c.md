# 00affc2c

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00affc2c",
  "name": "FUN_00affc2c",
  "size": 808,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e1c5a772ea04b27de27098d230661cb1e53102c7bc7d61a671572c8c8e5d1d1d",
  "source_text_sha256": "e1c5a772ea04b27de27098d230661cb1e53102c7bc7d61a671572c8c8e5d1d1d"
}
~~~

## 呼び出し元

- [005bc78c](../005bc/005bc78c.md)
- [005c2a54](../005c2/005c2a54.md)
- [005c36f8](../005c3/005c36f8.md)
- [005c38b8](../005c3/005c38b8.md)
- [005c3a84](../005c3/005c3a84.md)
- [005c3cdc](../005c3/005c3cdc.md)
- [005e2e00](../005e2/005e2e00.md)
- [007fb1f0](../007fb/007fb1f0.md)
- [00818d00](../00818/00818d00.md)
- [009f53b8](../009f5/009f53b8.md)
- [009fd490](../009fd/009fd490.md)
- [00a005e0](../00a00/00a005e0.md)
- [00a41f9c](../00a41/00a41f9c.md)
- [00a428ac](../00a42/00a428ac.md)
- [00ae0e64](../00ae0/00ae0e64.md)

## 呼び出し先

- [0049f3b0](../0049f/0049f3b0.md)
- [005e7c00](../005e7/005e7c00.md)
- [005e7c58](../005e7/005e7c58.md)
- [00664780](../00664/00664780.md)
- [0066a5dc](../0066a/0066a5dc.md)
- [00689c7c](../00689/00689c7c.md)
- [008024f4](../00802/008024f4.md)
- [00802b18](../00802/00802b18.md)
- [008514b8](../00851/008514b8.md)
- [008c2e68](../008c2/008c2e68.md)
- [00afe6c0](../00afe/00afe6c0.md)
- [00affb3c](../00aff/00affb3c.md)
- [00c57ab0](../00c57/00c57ab0.md)
- [00c57ae0](../00c57/00c57ae0.md)

## 疑似コード / UTF-8 3959 bytes

~~~c

void FUN_00affc2c(undefined4 param_1,undefined4 param_2,ulong param_3,int param_4)

{
  long lVar1;
  undefined4 uVar2;
  int iVar3;
  int iVar4;
  long lVar5;
  long *plVar6;
  ulong uVar7;
  long *plVar8;
  int *piVar9;
  uint uVar10;
  int *local_70;
  int *local_68;
  long local_58;
  
  lVar1 = tpidr_el0;
  local_58 = *(long *)(lVar1 + 0x28);
  if ((param_3 & 1) == 0) {
LAB_00affca8:
    iVar3 = FUN_00affb3c(0,param_1,param_2);
                    /* try { // try from 00affcb8 to 00bffcff has its CatchHandler @ 00affcb8
                       catch() { ... } // from try @ 00affcb8 with catch @ 00affcb8
                       catch() { ... } // from try @ 00affd1c with catch @ 00affcb8 */
    lVar5 = FUN_008514b8();
    iVar3 = (*(int *)((long)&fde_00393bf8 + lVar5) + 2) * (iVar3 / 100);
    if (iVar3 < 0) {
      iVar3 = iVar3 + 1;
    }
    uVar10 = (iVar3 >> 1) * 100;
    if ((param_3 & 1) != 0) {
                    /* try { // try from 00affd00 to 00bffd1b has its CatchHandler @ 00affd3c */
      lVar5 = FUN_008514b8();
      uVar2 = FUN_00802b18(0);
                    /* try { // try from 00affd1c to 00bffd4f has its CatchHandler @ 00affcb8 */
      iVar3 = FUN_008024f4((long)&fde_table_entry_00337310.initial_loc + lVar5,uVar2);
      if (iVar3 != 0) {
        iVar3 = FUN_00affb3c(0,param_1,param_2);
                    /* catch() { ... } // from try @ 00affd00 with catch @ 00affd3c */
        lVar5 = FUN_008514b8();
        uVar2 = FUN_00802b18(0);
        iVar4 = FUN_008024f4((long)&fde_table_entry_00337310.initial_loc + lVar5,uVar2);
        uVar10 = iVar4 * (iVar3 / 100);
      }
    }
    if (param_4 == -1) {
LAB_00affe8c:
      if ((param_3 & 1) != 0) {
        lVar5 = FUN_008514b8();
        uVar2 = FUN_00802b18(0);
        plVar8 = (long *)FUN_0066a5dc(lVar5 + 0x778,uVar2,5);
        if (plVar8 != (long *)0x0) {
          plVar6 = (long *)FUN_00664780(param_1);
          if ((ulong)(plVar8[1] - *plVar8 >> 2) <= (ulong)(long)(int)plVar6) {
            if (*(long *)(lVar1 + 0x28) == local_58) {
                    /* WARNING: Subroutine does not return */
              FUN_0049f3b0(plVar8);
            }
            goto LAB_00afff50;
          }
          uVar10 = (int)(*(int *)(*plVar8 + (long)(int)plVar6 * 4) * uVar10) / 100;
        }
      }
    }
    else {
      lVar5 = FUN_008514b8();
      uVar7 = FUN_005e7c00(lVar5 + 0x2768,0,param_4);
      iVar3 = 0;
      if ((uVar7 & 1) != 0) {
        lVar5 = FUN_008514b8();
        iVar3 = FUN_00689c7c(lVar5 + 0x1648,param_1,0x16,0,0);
      }
      lVar5 = FUN_008514b8();
      uVar7 = FUN_005e7c58(lVar5 + 0x2768,0,param_4);
      if ((uVar7 & 1) != 0) {
        iVar4 = FUN_00afe6c0(0,param_1,param_2,1000,0);
        iVar3 = iVar4 + iVar3;
      }
      uVar10 = ((int)((100 - iVar3) * uVar10) / 10000) * 100;
      if ((param_3 & 1) != 0) {
        lVar5 = FUN_008514b8();
        FUN_008c2e68(&local_70,&DAT_0044dd00 + lVar5,0x1b,param_1);
        for (piVar9 = local_70; local_68 != piVar9; piVar9 = piVar9 + 1) {
          uVar10 = ((int)((100 - *piVar9) * uVar10) / 10000) * 100;
        }
        if (local_70 != (int *)0x0) {
          local_68 = local_70;
          _ZdlPv(local_70);
        }
        goto LAB_00affe8c;
      }
    }
    uVar10 = uVar10 & ((int)uVar10 >> 0x1f ^ 0xffffffffU);
  }
  else {
    lVar5 = FUN_008514b8();
    uVar2 = FUN_00802b18(0);
    plVar6 = (long *)FUN_0066a5dc(lVar5 + 0x778,uVar2,4);
    if (plVar6 == (long *)0x0) goto LAB_00affca8;
    if ((int *)plVar6[1] == (int *)*plVar6) {
      if (*(long *)(lVar1 + 0x28) == local_58) {
                    /* WARNING: Subroutine does not return */
        FUN_0049f3b0();
      }
      goto LAB_00afff50;
    }
    uVar10 = *(int *)*plVar6 * 100;
  }
  plVar6 = (long *)(ulong)uVar10;
  if (*(long *)(lVar1 + 0x28) == local_58) {
    return;
  }
LAB_00afff50:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail(plVar6);
}

~~~
