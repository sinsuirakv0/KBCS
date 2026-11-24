# 00acf5fc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0162.md#review-aa5fd960162fd48d6c590df235eaa741)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 要確認
  - [v16.0.0 → v16.0.1 候補と検査根拠](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/review-0042.md#review-aa5fd960162fd48d6c590df235eaa741)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acf5fc",
  "name": "FUN_00acf5fc",
  "size": 556,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "03a834c3b54ee483a7aa85f8b202ce4f7b462a4d33b0deffa3051b14012cd924",
  "source_text_sha256": "03a834c3b54ee483a7aa85f8b202ce4f7b462a4d33b0deffa3051b14012cd924",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00acf5fc",
        "00acf827"
      ]
    ],
    "bytes_sha256": "0ecf41f9e4a3ca600bdb0e0af55f377d17458964c0624e24bd2d22951c02596a",
    "instruction_count": 139,
    "instruction_bytes": 556,
    "body_bytes": 556,
    "indirect": 2,
    "unresolved": 2
  }
}
~~~

## 呼び出し元

- [00acc3d4](../00acc/00acc3d4.md)
- [00ae0814](../00ae0/00ae0814.md)
- [00aec538](../00aec/00aec538.md)
- [00aeec98](../00aee/00aeec98.md)

## 呼び出し先

- [0043bb64](../0043b/0043bb64.md)
- [0047e89c](../0047e/0047e89c.md)
- [008514b8](../00851/008514b8.md)
- [00c538e0](../00c53/00c538e0.md)
- [00c57a30](../00c57/00c57a30.md)
- [00c57a50](../00c57/00c57a50.md)
- [00c57a70](../00c57/00c57a70.md)
- [00c57a80](../00c57/00c57a80.md)
- [00c57a90](../00c57/00c57a90.md)
- [00c57ae0](../00c57/00c57ae0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 5572 bytes

~~~c

void FUN_00acf5fc(long param_1)

{
  byte bVar1;
  long lVar2;
  undefined8 uVar3;
  int iVar4;
  long lVar5;
  long lVar6;
  long lVar7;
  byte *pbVar8;
  byte *pbVar9;
  long *plVar10;
  byte *pbVar11;
  long *plVar12;
  byte *pbVar13;
  undefined8 local_70;
  long *plStack_68;
  long local_58;
  
                    /* catch() { ... } // from try @ 00acd88c with catch @ 00acf5fc */
  lVar2 = tpidr_el0;
  local_58 = *(long *)(lVar2 + 0x28);
                    /* catch() { ... } // from try @ 00acea68 with catch @ 00acf7d0 */
  if (((DAT_00ca4b38 & 1) == 0) && (iVar4 = __cxa_guard_acquire(&DAT_00ca4b38), iVar4 != 0)) {
                    /* catch() { ... } // from try @ 00acce14 with catch @ 00acf7e4 */
                    /* catch() { ... } // from try @ 00accde0 with catch @ 00acf7ec */
                    /* catch() { ... } // from try @ 00acce20 with catch @ 00acf7f4 */
    DAT_00ca4b08 = 0;
    DAT_00ca4b00 = &DAT_00ca4b08;
    DAT_00ca4b28 = 0;
    DAT_00ca4b30 = 0;
    DAT_00ca4b20 = 0;
    DAT_00ca4b10 = 0;
    DAT_00ca4b18 = &DAT_00ca4b20;
    __cxa_atexit(FUN_0047ed74,&DAT_00ca4b00,&PTR_LOOP_00c62b90);
    __cxa_guard_release(&DAT_00ca4b38);
  }
  lVar5 = FUN_008514b8();
  lVar6 = FUN_008514b8();
  lVar7 = FUN_008514b8();
                    /* catch() { ... } // from try @ 00acd5cc with catch @ 00acf64c */
                    /* catch() { ... } // from try @ 00acd848 with catch @ 00acf650 */
                    /* catch() { ... } // from try @ 00acd5b8 with catch @ 00acf660 */
  bVar1 = BYTE_ARRAY_004347ed[lVar6 + (long)*(int *)((long)&DWORD_0039b97c + lVar7) * 3 + 0xb];
                    /* catch() { ... } // from try @ 00acd83c with catch @ 00acf670 */
  pbVar9 = *(byte **)(BYTE_ARRAY_0043616d + lVar5 + 0x33);
  if (*(byte **)(BYTE_ARRAY_0043616d + lVar5 + 0x33) == (byte *)0x0) {
    pbVar11 = BYTE_ARRAY_0043616d + lVar5 + 0x33;
    pbVar13 = BYTE_ARRAY_0043616d + lVar5 + 0x33;
  }
  else {
    do {
      while( true ) {
        pbVar8 = pbVar9;
        pbVar11 = pbVar8;
        if ((int)(char)bVar1 < *(int *)(pbVar8 + 0x20)) break;
        if ((int)(char)bVar1 <= *(int *)(pbVar8 + 0x20)) goto LAB_00acf700;
                    /* catch() { ... } // from try @ 00acd558 with catch @ 00acf6a4 */
        pbVar9 = *(byte **)(pbVar8 + 8);
        if (*(byte **)(pbVar8 + 8) == (byte *)0x0) {
                    /* catch() { ... } // from try @ 00acd544 with catch @ 00acf6a8 */
          pbVar13 = pbVar8 + 8;
          goto LAB_00acf6ac;
        }
      }
                    /* catch() { ... } // from try @ 00acd564 with catch @ 00acf684 */
      pbVar9 = *(byte **)pbVar8;
      pbVar13 = pbVar8;
    } while (*(byte **)pbVar8 != (byte *)0x0);
  }
LAB_00acf6ac:
  pbVar8 = (byte *)_Znwm(0x40);
                    /* catch() { ... } // from try @ 00acd454 with catch @ 00acf6b8 */
  pbVar8[0x30] = 0;
  pbVar8[0x31] = 0;
  pbVar8[0x32] = 0;
  pbVar8[0x33] = 0;
  pbVar8[0x34] = 0;
  pbVar8[0x35] = 0;
  pbVar8[0x36] = 0;
  pbVar8[0x37] = 0;
  pbVar8[0x38] = 0;
  pbVar8[0x39] = 0;
  pbVar8[0x3a] = 0;
  pbVar8[0x3b] = 0;
  pbVar8[0x3c] = 0;
  pbVar8[0x3d] = 0;
  pbVar8[0x3e] = 0;
  pbVar8[0x3f] = 0;
  pbVar8[0x28] = 0;
  pbVar8[0x29] = 0;
  pbVar8[0x2a] = 0;
  pbVar8[0x2b] = 0;
  pbVar8[0x2c] = 0;
  pbVar8[0x2d] = 0;
  pbVar8[0x2e] = 0;
  pbVar8[0x2f] = 0;
  pbVar8[0] = 0;
  pbVar8[1] = 0;
  pbVar8[2] = 0;
  pbVar8[3] = 0;
  pbVar8[4] = 0;
  pbVar8[5] = 0;
  pbVar8[6] = 0;
  pbVar8[7] = 0;
  pbVar8[8] = 0;
  pbVar8[9] = 0;
  pbVar8[10] = 0;
  pbVar8[0xb] = 0;
  pbVar8[0xc] = 0;
  pbVar8[0xd] = 0;
  pbVar8[0xe] = 0;
  pbVar8[0xf] = 0;
  *(byte **)(pbVar8 + 0x10) = pbVar11;
  *(byte **)pbVar13 = pbVar8;
  plVar10 = *(long **)(BYTE_ARRAY_0043616d + lVar5 + 0x2b);
  *(int *)(pbVar8 + 0x20) = (int)(char)bVar1;
  pbVar9 = pbVar8;
  if (*plVar10 != 0) {
    *(long *)(BYTE_ARRAY_0043616d + lVar5 + 0x2b) = *plVar10;
    pbVar9 = *(byte **)pbVar13;
  }
  FUN_0043bb64(*(undefined8 *)(BYTE_ARRAY_0043616d + lVar5 + 0x33),pbVar9);
                    /* catch() { ... } // from try @ 00acd448 with catch @ 00acf6f4 */
  *(long *)(BYTE_ARRAY_0043616d + lVar5 + 0x3b) = *(long *)(BYTE_ARRAY_0043616d + lVar5 + 0x3b) + 1;
LAB_00acf700:
                    /* catch() { ... } // from try @ 00acd434 with catch @ 00acf714 */
  FUN_0047e89c(&local_70,&DAT_00ca4b00,*(long *)(pbVar8 + 0x28) + 0x60,PTR_DAT_00c9a8a0,0x12,1,0,0);
  plVar10 = plStack_68;
  uVar3 = local_70;
                    /* catch() { ... } // from try @ 00acd400 with catch @ 00acf734 */
  plVar12 = *(long **)(param_1 + 0x4b0);
  local_70 = 0;
  plStack_68 = (long *)0x0;
  *(long **)(param_1 + 0x4b0) = plVar10;
  *(undefined8 *)(param_1 + 0x4a8) = uVar3;
  if ((plVar12 != (long *)0x0) && (lVar5 = FUN_00c538e0(0xffffffffffffffff,plVar12 + 1), lVar5 == 0)
     ) {
                    /* catch() { ... } // from try @ 00acd3ec with catch @ 00acf758 */
    (**(code **)(*plVar12 + 0x10))(plVar12);
                    /* catch() { ... } // from try @ 00aceacc with catch @ 00acf768 */
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar12);
  }
  plVar10 = plStack_68;
  if ((plStack_68 != (long *)0x0) &&
     (lVar5 = FUN_00c538e0(0xffffffffffffffff,plStack_68 + 1), lVar5 == 0)) {
    (**(code **)(*plVar10 + 0x10))(plVar10);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar10);
  }
                    /* catch() { ... } // from try @ 00accbac with catch @ 00acf7a8 */
  if (*(long *)(lVar2 + 0x28) == local_58) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00acf5fc"></a> `00acf5fc` | `ff c3 01 d1` | sub sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00acf600"></a> `00acf600` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00acf604"></a> `00acf604` | `f9 1b 00 f9` | str x25,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00acf608"></a> `00acf608` | `f8 5f 04 a9` | stp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00acf60c"></a> `00acf60c` | `f6 57 05 a9` | stp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00acf610"></a> `00acf610` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00acf614"></a> `00acf614` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00acf618"></a> `00acf618` | `55 d0 3b d5` | mrs x21,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00acf61c"></a> `00acf61c` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00acf620"></a> `00acf620` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00acf624"></a> `00acf624` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00acf628"></a> `00acf628` | `a8 0e 00 b0` | adrp x8,0xca4000 | `FALL_THROUGH`
<a id="insn-00acf62c"></a> `00acf62c` | `08 e1 2c 91` | add x8,x8,#0xb38 | `FALL_THROUGH`
<a id="insn-00acf630"></a> `00acf630` | `08 fd df 08` | ldarb w8,[x8] | `FALL_THROUGH`
<a id="insn-00acf634"></a> `00acf634` | `c8 0c 00 36` | tbz w8,#0x0,0x00acf7cc | `CONDITIONAL_JUMP`
<a id="insn-00acf638"></a> `00acf638` | `a0 07 f6 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00acf63c"></a> `00acf63c` | `16 d8 50 91` | add x22,x0,#0x436, LSL #12 | `FALL_THROUGH`
<a id="insn-00acf640"></a> `00acf640` | `9e 07 f6 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00acf644"></a> `00acf644` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00acf648"></a> `00acf648` | `9c 07 f6 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00acf64c"></a> `00acf64c` | `88 2f 97 52` | mov w8,#0xb97c | `FALL_THROUGH`
<a id="insn-00acf650"></a> `00acf650` | `0a ff 88 52` | mov w10,#0x47f8 | `FALL_THROUGH`
<a id="insn-00acf654"></a> `00acf654` | `28 07 a0 72` | movk w8,#0x39, LSL #16 | `FALL_THROUGH`
<a id="insn-00acf658"></a> `00acf658` | `6a 08 a0 72` | movk w10,#0x43, LSL #16 | `FALL_THROUGH`
<a id="insn-00acf65c"></a> `00acf65c` | `08 68 a8 b8` | ldrsw x8,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00acf660"></a> `00acf660` | `08 05 08 8b` | add x8,x8,x8, LSL #0x1 | `FALL_THROUGH`
<a id="insn-00acf664"></a> `00acf664` | `89 02 08 8b` | add x9,x20,x8 | `FALL_THROUGH`
<a id="insn-00acf668"></a> `00acf668` | `c8 d2 40 f9` | ldr x8,[x22, #0x1a0] | `FALL_THROUGH`
<a id="insn-00acf66c"></a> `00acf66c` | `37 69 ea 38` | ldrsb w23,[x9, x10, LSL ] | `FALL_THROUGH`
<a id="insn-00acf670"></a> `00acf670` | `e8 00 00 b5` | cbnz x8,0x00acf68c | `CONDITIONAL_JUMP`
<a id="insn-00acf674"></a> `00acf674` | `d8 82 06 91` | add x24,x22,#0x1a0 | `FALL_THROUGH`
<a id="insn-00acf678"></a> `00acf678` | `f4 03 18 aa` | mov x20,x24 | `FALL_THROUGH`
<a id="insn-00acf67c"></a> `00acf67c` | `0c 00 00 14` | b 0x00acf6ac | `UNCONDITIONAL_JUMP`
<a id="insn-00acf680"></a> `00acf680` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00acf684"></a> `00acf684` | `f8 03 14 aa` | mov x24,x20 | `FALL_THROUGH`
<a id="insn-00acf688"></a> `00acf688` | `28 01 00 b4` | cbz x8,0x00acf6ac | `CONDITIONAL_JUMP`
<a id="insn-00acf68c"></a> `00acf68c` | `f4 03 08 aa` | mov x20,x8 | `FALL_THROUGH`
<a id="insn-00acf690"></a> `00acf690` | `08 21 40 b9` | ldr w8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00acf694"></a> `00acf694` | `1f 01 17 6b` | cmp w8,w23 | `FALL_THROUGH`
<a id="insn-00acf698"></a> `00acf698` | `4c ff ff 54` | b.gt 0x00acf680 | `CONDITIONAL_JUMP`
<a id="insn-00acf69c"></a> `00acf69c` | `2a 03 00 54` | b.ge 0x00acf700 | `CONDITIONAL_JUMP`
<a id="insn-00acf6a0"></a> `00acf6a0` | `88 06 40 f9` | ldr x8,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00acf6a4"></a> `00acf6a4` | `48 ff ff b5` | cbnz x8,0x00acf68c | `CONDITIONAL_JUMP`
<a id="insn-00acf6a8"></a> `00acf6a8` | `98 22 00 91` | add x24,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00acf6ac"></a> `00acf6ac` | `00 08 80 52` | mov w0,#0x40 | `FALL_THROUGH`
<a id="insn-00acf6b0"></a> `00acf6b0` | `f9 03 14 aa` | mov x25,x20 | `FALL_THROUGH`
<a id="insn-00acf6b4"></a> `00acf6b4` | `f7 20 06 94` | bl 0x00c57a90 | `UNCONDITIONAL_CALL`
<a id="insn-00acf6b8"></a> `00acf6b8` | `1f 7c 03 a9` | stp xzr,xzr,[x0, #0x30] | `FALL_THROUGH`
<a id="insn-00acf6bc"></a> `00acf6bc` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00acf6c0"></a> `00acf6c0` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00acf6c4"></a> `00acf6c4` | `1f 14 00 f9` | str xzr,[x0, #0x28] | `FALL_THROUGH`
<a id="insn-00acf6c8"></a> `00acf6c8` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00acf6cc"></a> `00acf6cc` | `19 08 00 f9` | str x25,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00acf6d0"></a> `00acf6d0` | `00 03 00 f9` | str x0,[x24] | `FALL_THROUGH`
<a id="insn-00acf6d4"></a> `00acf6d4` | `c8 ce 40 f9` | ldr x8,[x22, #0x198] | `FALL_THROUGH`
<a id="insn-00acf6d8"></a> `00acf6d8` | `17 20 00 b9` | str w23,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00acf6dc"></a> `00acf6dc` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00acf6e0"></a> `00acf6e0` | `68 00 00 b4` | cbz x8,0x00acf6ec | `CONDITIONAL_JUMP`
<a id="insn-00acf6e4"></a> `00acf6e4` | `c8 ce 00 f9` | str x8,[x22, #0x198] | `FALL_THROUGH`
<a id="insn-00acf6e8"></a> `00acf6e8` | `01 03 40 f9` | ldr x1,[x24] | `FALL_THROUGH`
<a id="insn-00acf6ec"></a> `00acf6ec` | `c0 d2 40 f9` | ldr x0,[x22, #0x1a0] | `FALL_THROUGH`
<a id="insn-00acf6f0"></a> `00acf6f0` | `1d b1 e5 97` | bl 0x0043bb64 | `UNCONDITIONAL_CALL`
<a id="insn-00acf6f4"></a> `00acf6f4` | `c8 d6 40 f9` | ldr x8,[x22, #0x1a8] | `FALL_THROUGH`
<a id="insn-00acf6f8"></a> `00acf6f8` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00acf6fc"></a> `00acf6fc` | `c8 d6 00 f9` | str x8,[x22, #0x1a8] | `FALL_THROUGH`
<a id="insn-00acf700"></a> `00acf700` | `89 16 40 f9` | ldr x9,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00acf704"></a> `00acf704` | `42 0e 00 f0` | adrp x2,0xc9a000 | `FALL_THROUGH`
<a id="insn-00acf708"></a> `00acf708` | `a0 0e 00 b0` | adrp x0,0xca4000 | `FALL_THROUGH`
<a id="insn-00acf70c"></a> `00acf70c` | `00 00 2c 91` | add x0,x0,#0xb00 | `FALL_THROUGH`
<a id="insn-00acf710"></a> `00acf710` | `42 50 44 f9` | ldr x2,[x2, #0x8a0] | `FALL_THROUGH`
<a id="insn-00acf714"></a> `00acf714` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00acf718"></a> `00acf718` | `21 81 01 91` | add x1,x9,#0x60 | `FALL_THROUGH`
<a id="insn-00acf71c"></a> `00acf71c` | `43 02 80 52` | mov w3,#0x12 | `FALL_THROUGH`
<a id="insn-00acf720"></a> `00acf720` | `24 00 80 52` | mov w4,#0x1 | `FALL_THROUGH`
<a id="insn-00acf724"></a> `00acf724` | `e5 03 1f 2a` | mov w5,wzr | `FALL_THROUGH`
<a id="insn-00acf728"></a> `00acf728` | `e6 03 1f 2a` | mov w6,wzr | `FALL_THROUGH`
<a id="insn-00acf72c"></a> `00acf72c` | `5c bc e6 97` | bl 0x0047e89c | `UNCONDITIONAL_CALL`
<a id="insn-00acf730"></a> `00acf730` | `e0 03 c0 3d` | ldr q0,[sp] | `FALL_THROUGH`
<a id="insn-00acf734"></a> `00acf734` | `74 5a 42 f9` | ldr x20,[x19, #0x4b0] | `FALL_THROUGH`
<a id="insn-00acf738"></a> `00acf738` | `68 a2 12 91` | add x8,x19,#0x4a8 | `FALL_THROUGH`
<a id="insn-00acf73c"></a> `00acf73c` | `ff 7f 00 a9` | stp xzr,xzr,[sp] | `FALL_THROUGH`
<a id="insn-00acf740"></a> `00acf740` | `00 01 80 3d` | str q0,[x8] | `FALL_THROUGH`
<a id="insn-00acf744"></a> `00acf744` | `74 01 00 b4` | cbz x20,0x00acf770 | `CONDITIONAL_JUMP`
<a id="insn-00acf748"></a> `00acf748` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00acf74c"></a> `00acf74c` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00acf750"></a> `00acf750` | `64 10 06 94` | bl 0x00c538e0 | `UNCONDITIONAL_CALL`
<a id="insn-00acf754"></a> `00acf754` | `e0 00 00 b5` | cbnz x0,0x00acf770 | `CONDITIONAL_JUMP`
<a id="insn-00acf758"></a> `00acf758` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00acf75c"></a> `00acf75c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00acf760"></a> `00acf760` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00acf764"></a> `00acf764` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00acf768"></a> `00acf768` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00acf76c"></a> `00acf76c` | `c5 20 06 94` | bl 0x00c57a80 | `UNCONDITIONAL_CALL`
<a id="insn-00acf770"></a> `00acf770` | `f3 07 40 f9` | ldr x19,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00acf774"></a> `00acf774` | `73 01 00 b4` | cbz x19,0x00acf7a0 | `CONDITIONAL_JUMP`
<a id="insn-00acf778"></a> `00acf778` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00acf77c"></a> `00acf77c` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00acf780"></a> `00acf780` | `58 10 06 94` | bl 0x00c538e0 | `UNCONDITIONAL_CALL`
<a id="insn-00acf784"></a> `00acf784` | `e0 00 00 b5` | cbnz x0,0x00acf7a0 | `CONDITIONAL_JUMP`
<a id="insn-00acf788"></a> `00acf788` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00acf78c"></a> `00acf78c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00acf790"></a> `00acf790` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00acf794"></a> `00acf794` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00acf798"></a> `00acf798` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00acf79c"></a> `00acf79c` | `b9 20 06 94` | bl 0x00c57a80 | `UNCONDITIONAL_CALL`
<a id="insn-00acf7a0"></a> `00acf7a0` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00acf7a4"></a> `00acf7a4` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00acf7a8"></a> `00acf7a8` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00acf7ac"></a> `00acf7ac` | `c1 03 00 54` | b.ne 0x00acf824 | `CONDITIONAL_JUMP`
<a id="insn-00acf7b0"></a> `00acf7b0` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00acf7b4"></a> `00acf7b4` | `f9 1b 40 f9` | ldr x25,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00acf7b8"></a> `00acf7b8` | `f6 57 45 a9` | ldp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00acf7bc"></a> `00acf7bc` | `f8 5f 44 a9` | ldp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00acf7c0"></a> `00acf7c0` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00acf7c4"></a> `00acf7c4` | `ff c3 01 91` | add sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00acf7c8"></a> `00acf7c8` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00acf7cc"></a> `00acf7cc` | `a0 0e 00 b0` | adrp x0,0xca4000 | `FALL_THROUGH`
<a id="insn-00acf7d0"></a> `00acf7d0` | `00 e0 2c 91` | add x0,x0,#0xb38 | `FALL_THROUGH`
<a id="insn-00acf7d4"></a> `00acf7d4` | `9f 20 06 94` | bl 0x00c57a50 | `UNCONDITIONAL_CALL`
<a id="insn-00acf7d8"></a> `00acf7d8` | `00 f3 ff 34` | cbz w0,0x00acf638 | `CONDITIONAL_JUMP`
<a id="insn-00acf7dc"></a> `00acf7dc` | `a1 0e 00 b0` | adrp x1,0xca4000 | `FALL_THROUGH`
<a id="insn-00acf7e0"></a> `00acf7e0` | `21 00 2c 91` | add x1,x1,#0xb00 | `FALL_THROUGH`
<a id="insn-00acf7e4"></a> `00acf7e4` | `60 cd ff f0` | adrp x0,0x47e000 | `FALL_THROUGH`
<a id="insn-00acf7e8"></a> `00acf7e8` | `00 d0 35 91` | add x0,x0,#0xd74 | `FALL_THROUGH`
<a id="insn-00acf7ec"></a> `00acf7ec` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00acf7f0"></a> `00acf7f0` | `82 0c 00 f0` | adrp x2,0xc62000 | `FALL_THROUGH`
<a id="insn-00acf7f4"></a> `00acf7f4` | `42 40 2e 91` | add x2,x2,#0xb90 | `FALL_THROUGH`
<a id="insn-00acf7f8"></a> `00acf7f8` | `1f 8d 00 f8` | str xzr,[x8, #0x8]! | `FALL_THROUGH`
<a id="insn-00acf7fc"></a> `00acf7fc` | `28 00 00 f9` | str x8,[x1] | `FALL_THROUGH`
<a id="insn-00acf800"></a> `00acf800` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00acf804"></a> `00acf804` | `3f fc 02 a9` | stp xzr,xzr,[x1, #0x28] | `FALL_THROUGH`
<a id="insn-00acf808"></a> `00acf808` | `1f 0d 02 f8` | str xzr,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-00acf80c"></a> `00acf80c` | `3f 20 01 a9` | stp xzr,x8,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-00acf810"></a> `00acf810` | `88 20 06 94` | bl 0x00c57a30 | `UNCONDITIONAL_CALL`
<a id="insn-00acf814"></a> `00acf814` | `a0 0e 00 b0` | adrp x0,0xca4000 | `FALL_THROUGH`
<a id="insn-00acf818"></a> `00acf818` | `00 e0 2c 91` | add x0,x0,#0xb38 | `FALL_THROUGH`
<a id="insn-00acf81c"></a> `00acf81c` | `95 20 06 94` | bl 0x00c57a70 | `UNCONDITIONAL_CALL`
<a id="insn-00acf820"></a> `00acf820` | `86 ff ff 17` | b 0x00acf638 | `UNCONDITIONAL_JUMP`
<a id="insn-00acf824"></a> `00acf824` | `af 20 06 94` | bl 0x00c57ae0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00acf5fc`](#insn-00acf5fc) 範囲 `[['00acf5fc', '00acf637']]`
  - `CONDITIONAL_JUMP` [`00acf634`](#insn-00acf634) → [`00acf7cc`](#insn-00acf7cc)
  - `FALL_THROUGH` [`00acf634`](#insn-00acf634) → [`00acf638`](#insn-00acf638)
- ブロック [`00acf638`](#insn-00acf638) 範囲 `[['00acf638', '00acf64b']]`
  - `FALL_THROUGH` [`00acf648`](#insn-00acf648) → [`00acf64c`](#insn-00acf64c)
- ブロック [`00acf64c`](#insn-00acf64c) 範囲 `[['00acf64c', '00acf64f']]`
  - `FALL_THROUGH` [`00acf64c`](#insn-00acf64c) → [`00acf650`](#insn-00acf650)
- ブロック [`00acf650`](#insn-00acf650) 範囲 `[['00acf650', '00acf65f']]`
  - `FALL_THROUGH` [`00acf65c`](#insn-00acf65c) → [`00acf660`](#insn-00acf660)
- ブロック [`00acf660`](#insn-00acf660) 範囲 `[['00acf660', '00acf66f']]`
  - `FALL_THROUGH` [`00acf66c`](#insn-00acf66c) → [`00acf670`](#insn-00acf670)
- ブロック [`00acf670`](#insn-00acf670) 範囲 `[['00acf670', '00acf673']]`
  - `CONDITIONAL_JUMP` [`00acf670`](#insn-00acf670) → [`00acf68c`](#insn-00acf68c)
  - `FALL_THROUGH` [`00acf670`](#insn-00acf670) → [`00acf674`](#insn-00acf674)
- ブロック [`00acf674`](#insn-00acf674) 範囲 `[['00acf674', '00acf67f']]`
  - `UNCONDITIONAL_JUMP` [`00acf67c`](#insn-00acf67c) → [`00acf6ac`](#insn-00acf6ac)
- ブロック [`00acf680`](#insn-00acf680) 範囲 `[['00acf680', '00acf683']]`
  - `FALL_THROUGH` [`00acf680`](#insn-00acf680) → [`00acf684`](#insn-00acf684)
- ブロック [`00acf684`](#insn-00acf684) 範囲 `[['00acf684', '00acf68b']]`
  - `CONDITIONAL_JUMP` [`00acf688`](#insn-00acf688) → [`00acf6ac`](#insn-00acf6ac)
  - `FALL_THROUGH` [`00acf688`](#insn-00acf688) → [`00acf68c`](#insn-00acf68c)
- ブロック [`00acf68c`](#insn-00acf68c) 範囲 `[['00acf68c', '00acf69b']]`
  - `CONDITIONAL_JUMP` [`00acf698`](#insn-00acf698) → [`00acf680`](#insn-00acf680)
  - `FALL_THROUGH` [`00acf698`](#insn-00acf698) → [`00acf69c`](#insn-00acf69c)
- ブロック [`00acf69c`](#insn-00acf69c) 範囲 `[['00acf69c', '00acf69f']]`
  - `CONDITIONAL_JUMP` [`00acf69c`](#insn-00acf69c) → [`00acf700`](#insn-00acf700)
  - `FALL_THROUGH` [`00acf69c`](#insn-00acf69c) → [`00acf6a0`](#insn-00acf6a0)
- ブロック [`00acf6a0`](#insn-00acf6a0) 範囲 `[['00acf6a0', '00acf6a3']]`
  - `FALL_THROUGH` [`00acf6a0`](#insn-00acf6a0) → [`00acf6a4`](#insn-00acf6a4)
- ブロック [`00acf6a4`](#insn-00acf6a4) 範囲 `[['00acf6a4', '00acf6a7']]`
  - `CONDITIONAL_JUMP` [`00acf6a4`](#insn-00acf6a4) → [`00acf68c`](#insn-00acf68c)
  - `FALL_THROUGH` [`00acf6a4`](#insn-00acf6a4) → [`00acf6a8`](#insn-00acf6a8)
- ブロック [`00acf6a8`](#insn-00acf6a8) 範囲 `[['00acf6a8', '00acf6ab']]`
  - `FALL_THROUGH` [`00acf6a8`](#insn-00acf6a8) → [`00acf6ac`](#insn-00acf6ac)
- ブロック [`00acf6ac`](#insn-00acf6ac) 範囲 `[['00acf6ac', '00acf6b7']]`
  - `FALL_THROUGH` [`00acf6b4`](#insn-00acf6b4) → [`00acf6b8`](#insn-00acf6b8)
- ブロック [`00acf6b8`](#insn-00acf6b8) 範囲 `[['00acf6b8', '00acf6e3']]`
  - `CONDITIONAL_JUMP` [`00acf6e0`](#insn-00acf6e0) → [`00acf6ec`](#insn-00acf6ec)
  - `FALL_THROUGH` [`00acf6e0`](#insn-00acf6e0) → [`00acf6e4`](#insn-00acf6e4)
- ブロック [`00acf6e4`](#insn-00acf6e4) 範囲 `[['00acf6e4', '00acf6eb']]`
  - `FALL_THROUGH` [`00acf6e8`](#insn-00acf6e8) → [`00acf6ec`](#insn-00acf6ec)
- ブロック [`00acf6ec`](#insn-00acf6ec) 範囲 `[['00acf6ec', '00acf6f3']]`
  - `FALL_THROUGH` [`00acf6f0`](#insn-00acf6f0) → [`00acf6f4`](#insn-00acf6f4)
- ブロック [`00acf6f4`](#insn-00acf6f4) 範囲 `[['00acf6f4', '00acf6ff']]`
  - `FALL_THROUGH` [`00acf6fc`](#insn-00acf6fc) → [`00acf700`](#insn-00acf700)
- ブロック [`00acf700`](#insn-00acf700) 範囲 `[['00acf700', '00acf713']]`
  - `FALL_THROUGH` [`00acf710`](#insn-00acf710) → [`00acf714`](#insn-00acf714)
- ブロック [`00acf714`](#insn-00acf714) 範囲 `[['00acf714', '00acf733']]`
  - `FALL_THROUGH` [`00acf730`](#insn-00acf730) → [`00acf734`](#insn-00acf734)
- ブロック [`00acf734`](#insn-00acf734) 範囲 `[['00acf734', '00acf747']]`
  - `CONDITIONAL_JUMP` [`00acf744`](#insn-00acf744) → [`00acf770`](#insn-00acf770)
  - `FALL_THROUGH` [`00acf744`](#insn-00acf744) → [`00acf748`](#insn-00acf748)
- ブロック [`00acf748`](#insn-00acf748) 範囲 `[['00acf748', '00acf757']]`
  - `CONDITIONAL_JUMP` [`00acf754`](#insn-00acf754) → [`00acf770`](#insn-00acf770)
  - `FALL_THROUGH` [`00acf754`](#insn-00acf754) → [`00acf758`](#insn-00acf758)
- ブロック [`00acf758`](#insn-00acf758) 範囲 `[['00acf758', '00acf767']]`
  - `FALL_THROUGH` [`00acf764`](#insn-00acf764) → [`00acf768`](#insn-00acf768)
- ブロック [`00acf768`](#insn-00acf768) 範囲 `[['00acf768', '00acf76f']]`
  - `FALL_THROUGH` [`00acf76c`](#insn-00acf76c) → [`00acf770`](#insn-00acf770)
- ブロック [`00acf770`](#insn-00acf770) 範囲 `[['00acf770', '00acf777']]`
  - `CONDITIONAL_JUMP` [`00acf774`](#insn-00acf774) → [`00acf7a0`](#insn-00acf7a0)
  - `FALL_THROUGH` [`00acf774`](#insn-00acf774) → [`00acf778`](#insn-00acf778)
- ブロック [`00acf778`](#insn-00acf778) 範囲 `[['00acf778', '00acf787']]`
  - `CONDITIONAL_JUMP` [`00acf784`](#insn-00acf784) → [`00acf7a0`](#insn-00acf7a0)
  - `FALL_THROUGH` [`00acf784`](#insn-00acf784) → [`00acf788`](#insn-00acf788)
- ブロック [`00acf788`](#insn-00acf788) 範囲 `[['00acf788', '00acf79f']]`
  - `FALL_THROUGH` [`00acf79c`](#insn-00acf79c) → [`00acf7a0`](#insn-00acf7a0)
- ブロック [`00acf7a0`](#insn-00acf7a0) 範囲 `[['00acf7a0', '00acf7a7']]`
  - `FALL_THROUGH` [`00acf7a4`](#insn-00acf7a4) → [`00acf7a8`](#insn-00acf7a8)
- ブロック [`00acf7a8`](#insn-00acf7a8) 範囲 `[['00acf7a8', '00acf7af']]`
  - `CONDITIONAL_JUMP` [`00acf7ac`](#insn-00acf7ac) → [`00acf824`](#insn-00acf824)
  - `FALL_THROUGH` [`00acf7ac`](#insn-00acf7ac) → [`00acf7b0`](#insn-00acf7b0)
- ブロック [`00acf7b0`](#insn-00acf7b0) 範囲 `[['00acf7b0', '00acf7cb']]`
- ブロック [`00acf7cc`](#insn-00acf7cc) 範囲 `[['00acf7cc', '00acf7cf']]`
  - `FALL_THROUGH` [`00acf7cc`](#insn-00acf7cc) → [`00acf7d0`](#insn-00acf7d0)
- ブロック [`00acf7d0`](#insn-00acf7d0) 範囲 `[['00acf7d0', '00acf7db']]`
  - `CONDITIONAL_JUMP` [`00acf7d8`](#insn-00acf7d8) → [`00acf638`](#insn-00acf638)
  - `FALL_THROUGH` [`00acf7d8`](#insn-00acf7d8) → [`00acf7dc`](#insn-00acf7dc)
- ブロック [`00acf7dc`](#insn-00acf7dc) 範囲 `[['00acf7dc', '00acf7e3']]`
  - `FALL_THROUGH` [`00acf7e0`](#insn-00acf7e0) → [`00acf7e4`](#insn-00acf7e4)
- ブロック [`00acf7e4`](#insn-00acf7e4) 範囲 `[['00acf7e4', '00acf7eb']]`
  - `FALL_THROUGH` [`00acf7e8`](#insn-00acf7e8) → [`00acf7ec`](#insn-00acf7ec)
- ブロック [`00acf7ec`](#insn-00acf7ec) 範囲 `[['00acf7ec', '00acf7f3']]`
  - `FALL_THROUGH` [`00acf7f0`](#insn-00acf7f0) → [`00acf7f4`](#insn-00acf7f4)
- ブロック [`00acf7f4`](#insn-00acf7f4) 範囲 `[['00acf7f4', '00acf823']]`
  - `UNCONDITIONAL_JUMP` [`00acf820`](#insn-00acf820) → [`00acf638`](#insn-00acf638)
- ブロック [`00acf824`](#insn-00acf824) 範囲 `[['00acf824', '00acf827']]`

## 命令位置別の参照

- [`00acf600`](#insn-00acf600) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf604`](#insn-00acf604) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf608`](#insn-00acf608) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf60c`](#insn-00acf60c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf610`](#insn-00acf610) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf624`](#insn-00acf624) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf630`](#insn-00acf630) → `00ca4b38`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00acf634`](#insn-00acf634) → [`00acf7cc`](#insn-00acf7cc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf638`](#insn-00acf638) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00acf640`](#insn-00acf640) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00acf648`](#insn-00acf648) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00acf65c`](#insn-00acf65c) → `0039b97c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00acf668`](#insn-00acf668) → `004361a0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[63]`
- [`00acf66c`](#insn-00acf66c) → `004347f8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[47]`
- [`00acf670`](#insn-00acf670) → [`00acf68c`](#insn-00acf68c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf67c`](#insn-00acf67c) → [`00acf6ac`](#insn-00acf6ac) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf688`](#insn-00acf688) → [`00acf6ac`](#insn-00acf6ac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf698`](#insn-00acf698) → [`00acf680`](#insn-00acf680) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf69c`](#insn-00acf69c) → [`00acf700`](#insn-00acf700) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf6a4`](#insn-00acf6a4) → [`00acf68c`](#insn-00acf68c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf6b4`](#insn-00acf6b4) → [`00c57a90`](../00c57/00c57a90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a90` · 推定シンボル `None` · 推定型 `None`
- [`00acf6d0`](#insn-00acf6d0) → `004361a0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[63]`
- [`00acf6d4`](#insn-00acf6d4) → `00436198`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[63]`
- [`00acf6e0`](#insn-00acf6e0) → [`00acf6ec`](#insn-00acf6ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf6e4`](#insn-00acf6e4) → `00436198`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[63]`
- [`00acf6e8`](#insn-00acf6e8) → `004361a0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[63]`
- [`00acf6ec`](#insn-00acf6ec) → `004361a0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[63]`
- [`00acf6f0`](#insn-00acf6f0) → [`0043bb64`](../0043b/0043bb64.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bb64` · 推定シンボル `None` · 推定型 `None`
- [`00acf6f4`](#insn-00acf6f4) → `004361a8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[63]`
- [`00acf6fc`](#insn-00acf6fc) → `004361a8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[63]`
- [`00acf70c`](#insn-00acf70c) → `00ca4b00`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acf710`](#insn-00acf710) → `00c9a8a0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00acf710`](#insn-00acf710) → `00ca4bd8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00acf72c`](#insn-00acf72c) → [`0047e89c`](../0047e/0047e89c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047e89c` · 推定シンボル `None` · 推定型 `None`
- [`00acf730`](#insn-00acf730) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf73c`](#insn-00acf73c) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf744`](#insn-00acf744) → [`00acf770`](#insn-00acf770) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf750`](#insn-00acf750) → [`00c538e0`](../00c53/00c538e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c538e0` · 推定シンボル `None` · 推定型 `None`
- [`00acf754`](#insn-00acf754) → [`00acf770`](#insn-00acf770) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf76c`](#insn-00acf76c) → [`00c57a80`](../00c57/00c57a80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a80` · 推定シンボル `None` · 推定型 `None`
- [`00acf770`](#insn-00acf770) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf774`](#insn-00acf774) → [`00acf7a0`](#insn-00acf7a0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf780`](#insn-00acf780) → [`00c538e0`](../00c53/00c538e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c538e0` · 推定シンボル `None` · 推定型 `None`
- [`00acf784`](#insn-00acf784) → [`00acf7a0`](#insn-00acf7a0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf79c`](#insn-00acf79c) → [`00c57a80`](../00c57/00c57a80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a80` · 推定シンボル `None` · 推定型 `None`
- [`00acf7a4`](#insn-00acf7a4) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf7ac`](#insn-00acf7ac) → [`00acf824`](#insn-00acf824) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf7b0`](#insn-00acf7b0) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf7b4`](#insn-00acf7b4) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf7b8`](#insn-00acf7b8) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf7bc`](#insn-00acf7bc) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf7c0`](#insn-00acf7c0) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf7d0`](#insn-00acf7d0) → `00ca4b38`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00acf7d4`](#insn-00acf7d4) → [`00c57a50`](../00c57/00c57a50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a50` · 推定シンボル `None` · 推定型 `None`
- [`00acf7d8`](#insn-00acf7d8) → [`00acf638`](#insn-00acf638) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf7e0`](#insn-00acf7e0) → `00ca4b00`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acf7e8`](#insn-00acf7e8) → [`0047ed74`](../0047e/0047ed74.md) · `PARAM` · `ANALYSIS` · 関数 `0047ed74` · 推定シンボル `None` · 推定型 `None`
- [`00acf7f4`](#insn-00acf7f4) → `00c62b90`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00acf7f8`](#insn-00acf7f8) → `00ca4b08`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acf7fc`](#insn-00acf7fc) → `00ca4b00`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acf7fc`](#insn-00acf7fc) → `00ca4b08`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acf804`](#insn-00acf804) → `00ca4b28`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acf804`](#insn-00acf804) → `00ca4b30`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acf808`](#insn-00acf808) → `00ca4b20`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acf80c`](#insn-00acf80c) → `00ca4b10`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acf80c`](#insn-00acf80c) → `00ca4b18`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acf80c`](#insn-00acf80c) → `00ca4b20`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acf810`](#insn-00acf810) → [`00c57a30`](../00c57/00c57a30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a30` · 推定シンボル `None` · 推定型 `None`
- [`00acf818`](#insn-00acf818) → `00ca4b38`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00acf81c`](#insn-00acf81c) → [`00c57a70`](../00c57/00c57a70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a70` · 推定シンボル `None` · 推定型 `None`
- [`00acf820`](#insn-00acf820) → [`00acf638`](#insn-00acf638) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf824`](#insn-00acf824) → [`00c57ae0`](../00c57/00c57ae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ae0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00acf600`](#insn-00acf600)

~~~json
{
  "source": "00acf600",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf604`](#insn-00acf604)

~~~json
{
  "source": "00acf604",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf608`](#insn-00acf608)

~~~json
{
  "source": "00acf608",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf60c`](#insn-00acf60c)

~~~json
{
  "source": "00acf60c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf610`](#insn-00acf610)

~~~json
{
  "source": "00acf610",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf624`](#insn-00acf624)

~~~json
{
  "source": "00acf624",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf630`](#insn-00acf630)

~~~json
{
  "source": "00acf630",
  "target": "00ca4b38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b38",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acf634`](#insn-00acf634)

~~~json
{
  "source": "00acf634",
  "target": "00acf7cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf638`](#insn-00acf638)

~~~json
{
  "source": "00acf638",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acf640`](#insn-00acf640)

~~~json
{
  "source": "00acf640",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acf648`](#insn-00acf648)

~~~json
{
  "source": "00acf648",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acf65c`](#insn-00acf65c)

~~~json
{
  "source": "00acf65c",
  "target": "0039b97c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0039b97c",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "348b5000",
  "capture_start": "0039b97c",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00acf668`](#insn-00acf668)

~~~json
{
  "source": "00acf668",
  "target": "004361a0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0043616d",
  "offset": 51,
  "size": 63,
  "datatype": "byte[63]",
  "bytes": "442d440e90035c0c1d609302940495069608970a980c990e9a109b129c149e16",
  "capture_start": "0043616d",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00acf66c`](#insn-00acf66c)

~~~json
{
  "source": "00acf66c",
  "target": "004347f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "004347ed",
  "offset": 11,
  "size": 47,
  "datatype": "byte[47]",
  "bytes": "442d440e40500c1d409302940495069608970c9e0e9d100a032c010c1f40500e",
  "capture_start": "004347ed",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00acf670`](#insn-00acf670)

~~~json
{
  "source": "00acf670",
  "target": "00acf68c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf67c`](#insn-00acf67c)

~~~json
{
  "source": "00acf67c",
  "target": "00acf6ac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf688`](#insn-00acf688)

~~~json
{
  "source": "00acf688",
  "target": "00acf6ac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf698`](#insn-00acf698)

~~~json
{
  "source": "00acf698",
  "target": "00acf680",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf69c`](#insn-00acf69c)

~~~json
{
  "source": "00acf69c",
  "target": "00acf700",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf6a4`](#insn-00acf6a4)

~~~json
{
  "source": "00acf6a4",
  "target": "00acf68c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf6b4`](#insn-00acf6b4)

~~~json
{
  "source": "00acf6b4",
  "target": "00c57a90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acf6d0`](#insn-00acf6d0)

~~~json
{
  "source": "00acf6d0",
  "target": "004361a0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0043616d",
  "offset": 51,
  "size": 63,
  "datatype": "byte[63]",
  "bytes": "442d440e90035c0c1d609302940495069608970a980c990e9a109b129c149e16",
  "capture_start": "0043616d",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00acf6d4`](#insn-00acf6d4)

~~~json
{
  "source": "00acf6d4",
  "target": "00436198",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0043616d",
  "offset": 43,
  "size": 63,
  "datatype": "byte[63]",
  "bytes": "442d440e90035c0c1d609302940495069608970a980c990e9a109b129c149e16",
  "capture_start": "0043616d",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00acf6e0`](#insn-00acf6e0)

~~~json
{
  "source": "00acf6e0",
  "target": "00acf6ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf6e4`](#insn-00acf6e4)

~~~json
{
  "source": "00acf6e4",
  "target": "00436198",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0043616d",
  "offset": 43,
  "size": 63,
  "datatype": "byte[63]",
  "bytes": "442d440e90035c0c1d609302940495069608970a980c990e9a109b129c149e16",
  "capture_start": "0043616d",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00acf6e8`](#insn-00acf6e8)

~~~json
{
  "source": "00acf6e8",
  "target": "004361a0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0043616d",
  "offset": 51,
  "size": 63,
  "datatype": "byte[63]",
  "bytes": "442d440e90035c0c1d609302940495069608970a980c990e9a109b129c149e16",
  "capture_start": "0043616d",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00acf6ec`](#insn-00acf6ec)

~~~json
{
  "source": "00acf6ec",
  "target": "004361a0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0043616d",
  "offset": 51,
  "size": 63,
  "datatype": "byte[63]",
  "bytes": "442d440e90035c0c1d609302940495069608970a980c990e9a109b129c149e16",
  "capture_start": "0043616d",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00acf6f0`](#insn-00acf6f0)

~~~json
{
  "source": "00acf6f0",
  "target": "0043bb64",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acf6f4`](#insn-00acf6f4)

~~~json
{
  "source": "00acf6f4",
  "target": "004361a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0043616d",
  "offset": 59,
  "size": 63,
  "datatype": "byte[63]",
  "bytes": "442d440e90035c0c1d609302940495069608970a980c990e9a109b129c149e16",
  "capture_start": "0043616d",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00acf6fc`](#insn-00acf6fc)

~~~json
{
  "source": "00acf6fc",
  "target": "004361a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0043616d",
  "offset": 59,
  "size": 63,
  "datatype": "byte[63]",
  "bytes": "442d440e90035c0c1d609302940495069608970a980c990e9a109b129c149e16",
  "capture_start": "0043616d",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00acf70c`](#insn-00acf70c)

~~~json
{
  "source": "00acf70c",
  "target": "00ca4b00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acf710`](#insn-00acf710)

~~~json
{
  "source": "00acf710",
  "target": "00c9a8a0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9a8a0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00acf710`](#insn-00acf710)

~~~json
{
  "source": "00acf710",
  "target": "00ca4bd8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4bd8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acf72c`](#insn-00acf72c)

~~~json
{
  "source": "00acf72c",
  "target": "0047e89c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acf730`](#insn-00acf730)

~~~json
{
  "source": "00acf730",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf73c`](#insn-00acf73c)

~~~json
{
  "source": "00acf73c",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf744`](#insn-00acf744)

~~~json
{
  "source": "00acf744",
  "target": "00acf770",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf750`](#insn-00acf750)

~~~json
{
  "source": "00acf750",
  "target": "00c538e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acf754`](#insn-00acf754)

~~~json
{
  "source": "00acf754",
  "target": "00acf770",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf76c`](#insn-00acf76c)

~~~json
{
  "source": "00acf76c",
  "target": "00c57a80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acf770`](#insn-00acf770)

~~~json
{
  "source": "00acf770",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf774`](#insn-00acf774)

~~~json
{
  "source": "00acf774",
  "target": "00acf7a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf780`](#insn-00acf780)

~~~json
{
  "source": "00acf780",
  "target": "00c538e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acf784`](#insn-00acf784)

~~~json
{
  "source": "00acf784",
  "target": "00acf7a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf79c`](#insn-00acf79c)

~~~json
{
  "source": "00acf79c",
  "target": "00c57a80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acf7a4`](#insn-00acf7a4)

~~~json
{
  "source": "00acf7a4",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf7ac`](#insn-00acf7ac)

~~~json
{
  "source": "00acf7ac",
  "target": "00acf824",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf7b0`](#insn-00acf7b0)

~~~json
{
  "source": "00acf7b0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf7b4`](#insn-00acf7b4)

~~~json
{
  "source": "00acf7b4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf7b8`](#insn-00acf7b8)

~~~json
{
  "source": "00acf7b8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf7bc`](#insn-00acf7bc)

~~~json
{
  "source": "00acf7bc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf7c0`](#insn-00acf7c0)

~~~json
{
  "source": "00acf7c0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf7d0`](#insn-00acf7d0)

~~~json
{
  "source": "00acf7d0",
  "target": "00ca4b38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b38",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acf7d4`](#insn-00acf7d4)

~~~json
{
  "source": "00acf7d4",
  "target": "00c57a50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acf7d8`](#insn-00acf7d8)

~~~json
{
  "source": "00acf7d8",
  "target": "00acf638",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf7e0`](#insn-00acf7e0)

~~~json
{
  "source": "00acf7e0",
  "target": "00ca4b00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acf7e8`](#insn-00acf7e8)

~~~json
{
  "source": "00acf7e8",
  "target": "0047ed74",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acf7f4`](#insn-00acf7f4)

~~~json
{
  "source": "00acf7f4",
  "target": "00c62b90",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c62b90",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00acf7f8`](#insn-00acf7f8)

~~~json
{
  "source": "00acf7f8",
  "target": "00ca4b08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b08",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acf7fc`](#insn-00acf7fc)

~~~json
{
  "source": "00acf7fc",
  "target": "00ca4b00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acf7fc`](#insn-00acf7fc)

~~~json
{
  "source": "00acf7fc",
  "target": "00ca4b08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b08",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acf804`](#insn-00acf804)

~~~json
{
  "source": "00acf804",
  "target": "00ca4b28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b28",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acf804`](#insn-00acf804)

~~~json
{
  "source": "00acf804",
  "target": "00ca4b30",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b30",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acf808`](#insn-00acf808)

~~~json
{
  "source": "00acf808",
  "target": "00ca4b20",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b20",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acf80c`](#insn-00acf80c)

~~~json
{
  "source": "00acf80c",
  "target": "00ca4b10",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b10",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acf80c`](#insn-00acf80c)

~~~json
{
  "source": "00acf80c",
  "target": "00ca4b18",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b18",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acf80c`](#insn-00acf80c)

~~~json
{
  "source": "00acf80c",
  "target": "00ca4b20",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b20",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acf810`](#insn-00acf810)

~~~json
{
  "source": "00acf810",
  "target": "00c57a30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acf818`](#insn-00acf818)

~~~json
{
  "source": "00acf818",
  "target": "00ca4b38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b38",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acf81c`](#insn-00acf81c)

~~~json
{
  "source": "00acf81c",
  "target": "00c57a70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acf820`](#insn-00acf820)

~~~json
{
  "source": "00acf820",
  "target": "00acf638",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf824`](#insn-00acf824)

~~~json
{
  "source": "00acf824",
  "target": "00c57ae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
