# 00abacd8

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00abaadc`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aba/00abaadc.md) · 移動量 `+0x1fc`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/priority-0063.md#compare-be10c30061c00d88d0b54e5f31b6f001)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/priority-0068.md#compare-ab074a0b6d56a2f45f51c80b6eefa4f7)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00abacd8",
  "name": "FUN_00abacd8",
  "size": 676,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b0530739e7b858a956d419e5ec4cd78167c038cdbc03dd73dc470b5fbf43a307",
  "source_text_sha256": "b0530739e7b858a956d419e5ec4cd78167c038cdbc03dd73dc470b5fbf43a307"
}
~~~

## 呼び出し元

- [005fe66c](../005fe/005fe66c.md)
- [00ab31a4](../00ab3/00ab31a4.md)
- [00ab6740](../00ab6/00ab6740.md)

## 呼び出し先

- [0043bba4](../0043b/0043bba4.md)
- [008514f8](../00851/008514f8.md)
- [00ab91b8](../00ab9/00ab91b8.md)
- [00c57e90](../00c57/00c57e90.md)
- [00c57eb0](../00c57/00c57eb0.md)
- [00c57ee0](../00c57/00c57ee0.md)

## 疑似コード / UTF-8 6052 bytes

~~~c

bool FUN_00abacd8(int param_1,undefined4 param_2)

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
                    /* catch() { ... } // from try @ 00abae50 with catch @ 00abad00
                       catch() { ... } // from try @ 00abb070 with catch @ 00abad00
                       catch() { ... } // from try @ 00abb1f0 with catch @ 00abad00
                       catch() { ... } // from try @ 00abb364 with catch @ 00abad00
                       catch() { ... } // from try @ 00abb4b8 with catch @ 00abad00
                       catch() { ... } // from try @ 00abb5b4 with catch @ 00abad00
                       catch() { ... } // from try @ 00abb864 with catch @ 00abad00
                       catch() { ... } // from try @ 00abb954 with catch @ 00abad00
                       catch() { ... } // from try @ 00abba44 with catch @ 00abad00
                       catch() { ... } // from try @ 00abbc78 with catch @ 00abad00
                       catch() { ... } // from try @ 00abbe0c with catch @ 00abad00
                       catch() { ... } // from try @ 00abbed4 with catch @ 00abad00
                       catch() { ... } // from try @ 00abbf8c with catch @ 00abad00 */
  if (param_1 == 3) {
    bVar7 = false;
  }
  else {
    lVar10 = 0;
    do {
      lVar2 = FUN_008514f8();
      FUN_00ab91b8(local_98,(long)&uleb128_0029a6e0 + lVar2,param_1,param_2);
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
      lVar2 = FUN_008514f8();
                    /* try { // try from 00abad9c to 00bbada3 has its CatchHandler @ 00abccf4 */
      FUN_00ab91b8(local_98,(long)&uleb128_0029a6e0 + lVar2,param_1,param_2);
      iVar11 = *(int *)((long)local_90 + lVar10 * 4);
      local_88 = local_90;
      _ZdlPv(local_90);
      if (iVar11 < 0x2e) {
        lVar2 = FUN_008514f8();
                    /* try { // try from 00abadc0 to 00bbadcb has its CatchHandler @ 00abccd8 */
                    /* try { // try from 00abadcc to 00bbaddf has its CatchHandler @ 00abccb4 */
        FUN_00ab91b8(local_98,(long)&uleb128_0029a6e0 + lVar2,param_1,param_2);
        iVar11 = 0x2d - *(int *)((long)local_90 + lVar10 * 4);
      }
      else {
        lVar2 = FUN_008514f8();
        FUN_00ab91b8(local_98,(long)&uleb128_0029a6e0 + lVar2,param_1,param_2);
        iVar11 = *(int *)((long)local_90 + lVar10 * 4);
      }
      local_88 = local_90;
      _ZdlPv(local_90);
      lVar2 = FUN_008514f8();
      puVar8 = (undefined8 *)((long)&fde_table_entry_003380d8.initial_loc + lVar2);
                    /* try { // try from 00abae18 to 00bbae23 has its CatchHandler @ 00abcc40 */
                    /* try { // try from 00abae24 to 00bbae33 has its CatchHandler @ 00abcb94 */
      puVar5 = (undefined8 *)*puVar8;
      puVar9 = puVar8;
      if ((undefined8 *)*puVar8 != (undefined8 *)0x0) {
        do {
          while (puVar3 = puVar5, puVar9 = puVar3, param_1 < *(int *)(puVar3 + 4)) {
                    /* try { // try from 00abae34 to 00bbae4f has its CatchHandler @ 00abcafc */
            puVar5 = (undefined8 *)*puVar3;
            puVar8 = puVar3;
            if ((undefined8 *)*puVar3 == (undefined8 *)0x0) goto LAB_00abae5c;
          }
          if (param_1 <= *(int *)(puVar3 + 4)) goto LAB_00abaeb8;
                    /* try { // try from 00abae50 to 00bbafb3 has its CatchHandler @ 00abad00 */
          puVar5 = (undefined8 *)puVar3[1];
        } while ((undefined8 *)puVar3[1] != (undefined8 *)0x0);
        puVar8 = puVar3 + 1;
      }
LAB_00abae5c:
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
      FUN_0043bba4(*(undefined8 *)((long)&fde_table_entry_003380d8.initial_loc + lVar2),puVar5);
      *(long *)((long)&fde_table_entry_003380e0.initial_loc + lVar2) =
           *(long *)((long)&fde_table_entry_003380e0.initial_loc + lVar2) + 1;
LAB_00abaeb8:
      puVar8 = puVar3 + 6;
      puVar5 = (undefined8 *)*puVar8;
      puVar9 = puVar8;
      if ((undefined8 *)*puVar8 != (undefined8 *)0x0) {
        do {
          while (puVar4 = puVar5, puVar9 = puVar4, iVar11 < *(int *)((long)puVar4 + 0x1c)) {
            puVar5 = (undefined8 *)*puVar4;
            puVar8 = puVar4;
            if ((undefined8 *)*puVar4 == (undefined8 *)0x0) goto LAB_00abaefc;
          }
          if (iVar11 <= *(int *)((long)puVar4 + 0x1c)) goto LAB_00abad44;
          puVar5 = (undefined8 *)puVar4[1];
        } while ((undefined8 *)puVar4[1] != (undefined8 *)0x0);
        puVar8 = puVar4 + 1;
      }
LAB_00abaefc:
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
      FUN_0043bba4(puVar3[6],puVar5);
      puVar3[7] = puVar3[7] + 1;
LAB_00abad44:
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
