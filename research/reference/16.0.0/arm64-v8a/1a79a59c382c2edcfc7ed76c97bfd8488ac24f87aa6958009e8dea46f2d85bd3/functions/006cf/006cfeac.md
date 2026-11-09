# 006cfeac

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "006cfeac",
  "name": "FUN_006cfeac",
  "size": 764,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "83c2bad6ad02b305a040f2aa9dee142b94f15fd398bc390b5f7115a76434a6e5",
  "source_text_sha256": "83c2bad6ad02b305a040f2aa9dee142b94f15fd398bc390b5f7115a76434a6e5"
}
~~~

## 呼び出し元

- [006d0264](../006d0/006d0264.md)
- [0089c00c](../0089c/0089c00c.md)
- [00b1f000](../00b1f/00b1f000.md)

## 呼び出し先

- [00440e80](../00440/00440e80.md)
- [006d7024](../006d7/006d7024.md)
- [006d7048](../006d7/006d7048.md)
- [006d7660](../006d7/006d7660.md)
- [006d773c](../006d7/006d773c.md)
- [00c57a90](../00c57/00c57a90.md)
- [00c57ab0](../00c57/00c57ab0.md)
- [00c57ae0](../00c57/00c57ae0.md)
- [00c5a470](../00c5a/00c5a470.md)

## 疑似コード / UTF-8 5699 bytes

~~~c

void FUN_006cfeac(undefined8 param_1,byte *param_2)

{
  uint uVar1;
  uint uVar2;
  ulong uVar3;
  byte *pbVar4;
  uint uVar5;
  long lVar6;
  undefined *puVar7;
  long *plVar8;
  uint *puVar9;
  uint *puVar10;
  ulong uVar11;
  ulong uVar12;
  long lVar13;
  uint *puVar14;
  ulong uVar15;
  ulong local_b0;
  ulong local_a8;
  uint *local_a0;
  byte local_98 [8];
  ulong local_90;
  uint *local_88;
  ulong local_80;
  undefined8 uStack_78;
  void *local_70;
  ulong local_68;
  undefined8 local_60;
  void *pvStack_58;
  long *local_50;
  undefined8 local_48;
  undefined8 uStack_40;
  long local_38;
  
                    /* catch() { ... } // from try @ 006cfdc4 with catch @ 006cfeb8
                       catch() { ... } // from try @ 006cfe84 with catch @ 006cfeb8 */
  lVar6 = tpidr_el0;
  local_38 = *(long *)(lVar6 + 0x28);
                    /* try { // try from 006cfed8 to 007cfeef has its CatchHandler @ 006cfed8
                       catch() { ... } // from try @ 006cfed8 with catch @ 006cfed8
                       catch() { ... } // from try @ 006cfef8 with catch @ 006cfed8 */
  plVar8 = (long *)_Znwm(0x28);
  _ZNSt6__ndk17codecvtIwc9mbstate_tEC1Em(plVar8,0);
  puVar7 = PTR__ZTVNSt6__ndk118codecvt_utf8_utf16IwLm1114111ELNS_12codecvt_modeE0EEE_00c9b140;
                    /* try { // try from 006cfef0 to 007cfef7 has its CatchHandler @ 006cff10 */
                    /* try { // try from 006cfef8 to 007cff23 has its CatchHandler @ 006cfed8 */
  plVar8[3] = 0x10ffff;
  uVar3 = *(ulong *)(param_2 + 8);
  pbVar4 = *(byte **)(param_2 + 0x10);
  *(undefined4 *)(plVar8 + 4) = 0;
  local_48 = 0;
  uStack_40 = 0;
  *plVar8 = (long)(puVar7 + 0x10);
                    /* catch() { ... } // from try @ 006cfef0 with catch @ 006cff10 */
  uStack_78 = 0;
  local_80 = 0;
  local_68 = 0;
  local_70 = (void *)0x0;
  pvStack_58 = (void *)0x0;
  local_60 = 0;
  if ((*param_2 & 1) == 0) {
    pbVar4 = param_2 + 1;
    uVar3 = (ulong)(*param_2 >> 1);
  }
  local_50 = plVar8;
  FUN_006d7048(local_98,&local_80,pbVar4,pbVar4 + uVar3);
  uVar3 = (ulong)(local_98[0] >> 1);
  if ((local_98[0] & 1) != 0) {
    uVar3 = local_90;
  }
  if (0x3ffffffffffffff7 < uVar3) {
    if (*(long *)(lVar6 + 0x28) != local_38) goto LAB_006d0208;
    FUN_006d7660(&local_b0);
LAB_006d0190:
    if (*(long *)(lVar6 + 0x28) == local_38) {
                    /* WARNING: Subroutine does not return */
      FUN_00440e80();
    }
    goto LAB_006d0208;
  }
  if (uVar3 < 5) {
    puVar9 = (uint *)((ulong)&local_b0 | 4);
    local_b0 = CONCAT71(local_b0._1_7_,(char)((int)uVar3 << 1));
    if (uVar3 != 0) goto LAB_006cffb8;
  }
  else {
    uVar11 = (uVar3 & 0x3ffffffffffffffe) + 2;
    if ((uVar3 | 1) != 5) {
      uVar11 = uVar3 | 1;
    }
    if (0x3ffffffffffffffe < uVar11) goto LAB_006d0190;
    puVar9 = (uint *)_Znwm((uVar11 + 1) * 4);
                    /* try { // try from 006cffac to 007d00b3 has its CatchHandler @ 006cffac
                       catch() { ... } // from try @ 006cffac with catch @ 006cffac
                       catch() { ... } // from try @ 006d00c0 with catch @ 006cffac */
    local_b0 = uVar11 + 1 | 1;
    local_a8 = uVar3;
    local_a0 = puVar9;
LAB_006cffb8:
    puVar10 = puVar9;
    uVar11 = uVar3;
    if (7 < uVar3) {
      uVar12 = uVar3 & 0x3ffffffffffffff8;
      uVar11 = uVar3 & 7;
      puVar10 = puVar9 + uVar12;
      puVar14 = puVar9 + 4;
      uVar15 = uVar12;
      do {
        uVar15 = uVar15 - 8;
        puVar14[-2] = 0x20;
        puVar14[-1] = 0x20;
        puVar14[-4] = 0x20;
        puVar14[-3] = 0x20;
        puVar14[2] = 0x20;
        puVar14[3] = 0x20;
        puVar14[0] = 0x20;
        puVar14[1] = 0x20;
        puVar14 = puVar14 + 8;
      } while (uVar15 != 0);
      if (uVar3 == uVar12) goto LAB_006d0008;
    }
    do {
      uVar11 = uVar11 - 1;
      *puVar10 = 0x20;
      puVar10 = puVar10 + 1;
    } while (uVar11 != 0);
  }
LAB_006d0008:
  puVar9[uVar3] = 0;
  puVar9 = (uint *)((ulong)local_98 | 4);
  uVar3 = (ulong)(local_98[0] >> 1);
  if ((local_98[0] & 1) != 0) {
    puVar9 = local_88;
    uVar3 = local_90;
  }
  if (uVar3 != 0) {
    lVar13 = uVar3 << 2;
    puVar10 = (uint *)((ulong)&local_b0 | 4);
    if ((local_b0 & 1) != 0) {
      puVar10 = local_a0;
    }
    do {
      uVar5 = *puVar9;
      uVar1 = uVar5 - 0xfee0;
      uVar2 = uVar1;
      if (0x19 < uVar5 - 0xff41) {
        uVar2 = uVar5;
      }
      if (uVar5 - 0xff21 < 0x1a) {
        uVar2 = uVar1;
      }
      if (uVar5 - 0xff10 < 10) {
        uVar2 = uVar1;
      }
      uVar1 = uVar2 + 0x60;
      if (0x55 < uVar2 - 0x3041) {
        uVar1 = uVar2;
      }
      if (uVar2 - 0x41 < 0x1a) {
        uVar1 = uVar2 | 0x20;
      }
      lVar13 = lVar13 + -4;
                    /* try { // try from 006d00b4 to 007d00bf has its CatchHandler @ 006d0168 */
      *puVar10 = uVar1;
      puVar9 = puVar9 + 1;
      puVar10 = puVar10 + 1;
    } while (lVar13 != 0);
  }
  uVar3 = local_b0 >> 1 & 0x7f;
  puVar9 = (uint *)((ulong)&local_b0 | 4);
  if ((local_b0 & 1) != 0) {
    uVar3 = local_a8;
    puVar9 = local_a0;
  }
  FUN_006d773c(param_1,&local_80,puVar9,puVar9 + uVar3);
  if ((local_b0 & 1) != 0) {
    _ZdlPv(local_a0);
  }
  if ((local_98[0] & 1) != 0) {
                    /* catch() { ... } // from try @ 006d00b4 with catch @ 006d0168 */
    _ZdlPv(local_88);
  }
  if (local_50 != (long *)0x0) {
    (**(code **)(*local_50 + 8))();
  }
  if ((local_68 & 1) != 0) {
    _ZdlPv(pvStack_58);
  }
  if ((local_80 & 1) != 0) {
    _ZdlPv(local_70);
  }
  if (*(long *)(lVar6 + 0x28) == local_38) {
    return;
  }
LAB_006d0208:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
