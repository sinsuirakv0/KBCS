# 00ae1ccc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00ae0cd8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ae0/00ae0cd8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0067.md#compare-b8dba517990b331f3ec1b15e5e310a9d)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ae1ccc",
  "name": "FUN_00ae1ccc",
  "size": 1240,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "aff7bef09f9b9300b90041133426ca68c21fdc8b7edb44f740e320d31a0c28b5",
  "source_text_sha256": "aff7bef09f9b9300b90041133426ca68c21fdc8b7edb44f740e320d31a0c28b5",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ae1ccc",
        "00ae219f"
      ],
      [
        "00ae223c",
        "00ae223f"
      ]
    ],
    "bytes_sha256": "b4198330c8cfd779d9e8534a45256a85abb44c67750c7286d1ae9c762cf53998",
    "instruction_count": 310,
    "instruction_bytes": 1240,
    "body_bytes": 1240,
    "indirect": 4,
    "unresolved": 4
  }
}
~~~

## 呼び出し元

- [0094826c](../00948/0094826c.md)
- [00ad7fb0](../00ad7/00ad7fb0.md)

## 呼び出し先

- [0047e96c](../0047e/0047e96c.md)
- [0048d1b4](../0048d/0048d1b4.md)
- [00666154](../00666/00666154.md)
- [008b7f44](../008b7/008b7f44.md)
- [008b89cc](../008b8/008b89cc.md)
- [009e0634](../009e0/009e0634.md)
- [009e1fc0](../009e1/009e1fc0.md)
- [009e3f94](../009e3/009e3f94.md)
- [00ad0558](../00ad0/00ad0558.md)
- [00ad085c](../00ad0/00ad085c.md)
- [00ad7aec](../00ad7/00ad7aec.md)
- [00c54d90](../00c54/00c54d90.md)
- [00c58ed0](../00c58/00c58ed0.md)
- [00c58ef0](../00c58/00c58ef0.md)
- [00c58f10](../00c58/00c58f10.md)
- [00c58f20](../00c58/00c58f20.md)
- [00c58f50](../00c58/00c58f50.md)
- [00c58f80](../00c58/00c58f80.md)
- [00c596b0](../00c59/00c596b0.md)

## 関連文字列（未確認候補）

~~~text
"uni.imgcut"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 7795 bytes

~~~c

/* WARNING: Type propagation algorithm not settling */

void FUN_00ae1ccc(long param_1,int param_2)

{
  int *piVar1;
  long lVar2;
  byte *pbVar3;
  char cVar4;
  uint uVar5;
  int iVar6;
  uint uVar7;
  long lVar8;
  long *plVar9;
  int iVar10;
  ulong uVar11;
  long lVar12;
  undefined8 uVar13;
  undefined4 uVar14;
  long lVar15;
  undefined4 *puVar16;
  long lVar17;
  long lVar18;
  char *pcVar19;
  fde_table_entry *pfVar20;
  long *plVar21;
  byte local_e8 [11];
  undefined1 local_dd;
  void *local_d8;
  byte local_d0 [16];
  void *local_c0;
  byte local_b8 [8];
  undefined1 local_b0;
  void *local_a8;
  ulong local_a0;
  long *plStack_98;
  void *local_90;
  undefined8 local_80;
  long *plStack_78;
  long local_68;
  
                    /* catch() { ... } // from try @ 00ae13e4 with catch @ 00ae1cdc */
                    /* catch() { ... } // from try @ 00ae159c with catch @ 00ae1ce8 */
                    /* catch() { ... } // from try @ 00ae1558 with catch @ 00ae1cec */
  lVar8 = tpidr_el0;
                    /* catch() { ... } // from try @ 00ae1628 with catch @ 00ae1cf0 */
                    /* catch() { ... } // from try @ 00ae16bc with catch @ 00ae1cf4 */
                    /* catch() { ... } // from try @ 00ae171c with catch @ 00ae1cf8 */
                    /* catch() { ... } // from try @ 00ae18bc with catch @ 00ae1cfc */
  piVar1 = (int *)((long)&QWORD_0039b978 + param_1 + 4);
                    /* catch() { ... } // from try @ 00ae1760 with catch @ 00ae1d00 */
  local_68 = *(long *)(lVar8 + 0x28);
  lVar18 = 0;
                    /* catch() { ... } // from try @ 00ae1a1c with catch @ 00ae1d18 */
  cVar4 = *(char *)((long)&fde_0039b980 + param_1);
  iVar10 = *piVar1 + param_2 + (int)cVar4;
  iVar6 = 0;
  if (cVar4 != 0) {
    iVar6 = iVar10 / (int)cVar4;
  }
                    /* catch() { ... } // from try @ 00ae1c5c with catch @ 00ae1d30
                       catch() { ... } // from try @ 00ae1c90 with catch @ 00ae1d30 */
  lVar2 = param_1 + 0xc5b8;
                    /* catch() { ... } // from try @ 00ae1c40 with catch @ 00ae1d38
                       catch() { ... } // from try @ 00ae1c78 with catch @ 00ae1d38 */
  *(undefined1 *)(param_1 + 0x11a4) = 1;
                    /* catch() { ... } // from try @ 00ae1938 with catch @ 00ae1d40 */
                    /* catch() { ... } // from try @ 00ae17e0 with catch @ 00ae1d44 */
  *piVar1 = iVar10 - iVar6 * cVar4;
  do {
    lVar17 = lVar18 + (long)*piVar1 * 0x2c;
    lVar15 = lVar2 + (long)*piVar1 * 0x2c;
    lVar12 = lVar2 + lVar17;
    uVar5 = (uint)(*(byte *)(lVar15 + 0x2a) ^ *(byte *)(lVar12 + 2)) << 0x10 |
            (uint)(*(byte *)(lVar15 + 0x2b) ^ *(byte *)(lVar12 + 3)) << 0x18 |
            (uint)(*(byte *)(lVar15 + 0x29) ^ *(byte *)(lVar12 + 1)) << 8 |
            (uint)(*(byte *)(lVar15 + 0x28) ^ *(byte *)(lVar2 + lVar17));
    uVar7 = uVar5 - 2;
    if ((int)uVar5 < 2) {
      uVar14 = 0;
    }
    else {
      uVar11 = FUN_009e1fc0(param_1 + 0x50,0xffffffff,0xffffffff);
      if ((((uVar11 & 1) == 0) ||
          (lVar12 = FUN_009e3f94(param_1 + 0x50,0xffffffff,0xffffffff), lVar12 == 0)) ||
         (lVar12 = FUN_009e0634(lVar12,uVar7), lVar12 == 0)) {
        puVar16 = (undefined4 *)(param_1 + 0x49934 + (ulong)uVar7 * 4);
      }
      else {
        puVar16 = (undefined4 *)(lVar12 + 4);
      }
      uVar14 = *puVar16;
    }
    *(undefined4 *)((long)&fde_table_entry_003339b8.initial_loc + lVar18 + param_1) = uVar14;
    lVar18 = lVar18 + 4;
  } while (lVar18 != 0x28);
  if (DAT_00ca5a38 == 0) {
    lVar18 = 0;
  }
  else {
    lVar18 = __dynamic_cast(DAT_00ca5a38,&PTR__ZTVN10__cxxabiv117__class_type_infoE_16__00c66ef8,
                            &PTR__ZTVN10__cxxabiv120__si_class_type_infoE_16__00c8e9f0,0);
  }
  lVar12 = 0;
  pfVar20 = &fde_table_entry_003339b8;
  pcVar19 = (char *)((ulong)local_e8 | 1);
  lVar15 = 0xc5b8;
  do {
    lVar17 = lVar2 + (long)*piVar1 * 0x2c;
    pbVar3 = (byte *)(param_1 + lVar15 + (long)*piVar1 * 0x2c);
    uVar5 = (uint)(*(byte *)(lVar17 + 0x2a) ^ pbVar3[2]) << 0x10 |
            (uint)(*(byte *)(lVar17 + 0x2b) ^ pbVar3[3]) << 0x18 |
            (uint)(*(byte *)(lVar17 + 0x29) ^ pbVar3[1]) << 8 |
            (uint)(*(byte *)(lVar17 + 0x28) ^ *pbVar3);
    if (uVar5 == 0xffffffff) {
      if (((DAT_00ca5ff8 & 1) == 0) && (iVar10 = __cxa_guard_acquire(&DAT_00ca5ff8), iVar10 != 0)) {
        DAT_00ca5fc8 = 0;
        DAT_00ca5fc0 = &DAT_00ca5fc8;
        DAT_00ca5fe8 = 0;
        DAT_00ca5ff0 = 0;
        DAT_00ca5fe0 = 0;
        DAT_00ca5fd0 = 0;
        DAT_00ca5fd8 = &DAT_00ca5fe0;
        __cxa_atexit(FUN_0047f114,&DAT_00ca5fc0,&PTR_LOOP_00c64030);
        __cxa_guard_release(&DAT_00ca5ff8);
      }
      local_b0 = 0;
      local_b8[0] = 0xe;
      *(undefined4 *)((ulong)local_b8 | 1) = 0x2e696e75;
      *(undefined4 *)((long)((ulong)local_b8 | 1) + 3) = 0x676e702e;
      FUN_0048d1b4(&local_a0,local_b8);
      uVar13 = s_uni_imgcut_002caba4._0_8_;
      local_dd = 0;
      local_e8[0] = 0x14;
      pcVar19[8] = 'u';
      pcVar19[9] = 't';
      *(undefined8 *)pcVar19 = uVar13;
      FUN_0048d1b4(local_d0,local_e8);
      FUN_0047e96c(&local_80,&DAT_00ca5fc0,&local_a0,local_d0,0x2601);
      plVar9 = plStack_78;
      uVar13 = local_80;
      local_80 = 0;
      plStack_78 = (long *)0x0;
      lVar17 = lVar18 + lVar12;
      plVar21 = *(long **)(lVar17 + 0x348);
      *(long **)(lVar17 + 0x348) = plVar9;
      *(undefined8 *)(lVar17 + 0x340) = uVar13;
      plVar9 = plStack_78;
      if ((plVar21 != (long *)0x0) &&
         (lVar17 = FUN_00c54d90(0xffffffffffffffff,plVar21 + 1), plVar9 = plStack_78, lVar17 == 0))
      {
        (**(code **)(*plVar21 + 0x10))(plVar21);
        _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar21);
        plVar9 = plStack_78;
      }
      plStack_78 = plVar9;
      if ((plVar9 != (long *)0x0) &&
         (lVar17 = FUN_00c54d90(0xffffffffffffffff,plVar9 + 1), lVar17 == 0)) {
        (**(code **)(*plVar9 + 0x10))(plVar9);
        _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar9);
      }
      if ((local_d0[0] & 1) != 0) {
        _ZdlPv(local_c0);
      }
      if ((local_e8[0] & 1) != 0) {
        _ZdlPv(local_d8);
      }
      if ((local_a0 & 1) != 0) {
        _ZdlPv(local_90);
      }
      if ((local_b8[0] & 1) != 0) {
        _ZdlPv(local_a8);
      }
    }
    else {
      FUN_00666154(&local_a0,uVar5 - 2,*(undefined4 *)((long)&pfVar20->initial_loc + param_1),0);
      plVar9 = plStack_98;
      uVar11 = local_a0;
      local_a0 = 0;
      plStack_98 = (long *)0x0;
      lVar17 = lVar18 + lVar12;
      plVar21 = *(long **)(lVar17 + 0x348);
      *(long **)(lVar17 + 0x348) = plVar9;
      *(ulong *)(lVar17 + 0x340) = uVar11;
      plVar9 = plStack_98;
      if ((plVar21 != (long *)0x0) &&
         (lVar17 = FUN_00c54d90(0xffffffffffffffff,plVar21 + 1), plVar9 = plStack_98, lVar17 == 0))
      {
        (**(code **)(*plVar21 + 0x10))(plVar21);
        _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar21);
        plVar9 = plStack_98;
      }
      plStack_98 = plVar9;
      if ((plVar9 != (long *)0x0) &&
         (lVar17 = FUN_00c54d90(0xffffffffffffffff,plVar9 + 1), lVar17 == 0)) {
        (**(code **)(*plVar9 + 0x10))(plVar9);
        _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar9);
      }
    }
    lVar12 = lVar12 + 0x10;
    pfVar20 = (fde_table_entry *)&pfVar20->data_loc;
    lVar15 = lVar15 + 4;
  } while (lVar12 != 0xa0);
  FUN_00ad085c(lVar18);
  FUN_00ad0558(param_1);
  uVar13 = FUN_008b89cc(param_1 + 0x2f38,0x324);
  iVar10 = FUN_00ad7aec(param_1);
  FUN_008b7f44(uVar13,iVar10 == 3);
  if (*(long *)(lVar8 + 0x28) == local_68) {
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
<a id="insn-00ae1ccc"></a> `00ae1ccc` | `ff 03 04 d1` | sub sp,sp,#0x100 | `FALL_THROUGH`
<a id="insn-00ae1cd0"></a> `00ae1cd0` | `fd 7b 0a a9` | stp x29,x30,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00ae1cd4"></a> `00ae1cd4` | `fc 6f 0b a9` | stp x28,x27,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00ae1cd8"></a> `00ae1cd8` | `fa 67 0c a9` | stp x26,x25,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00ae1cdc"></a> `00ae1cdc` | `f8 5f 0d a9` | stp x24,x23,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-00ae1ce0"></a> `00ae1ce0` | `f6 57 0e a9` | stp x22,x21,[sp, #0xe0] | `FALL_THROUGH`
<a id="insn-00ae1ce4"></a> `00ae1ce4` | `f4 4f 0f a9` | stp x20,x19,[sp, #0xf0] | `FALL_THROUGH`
<a id="insn-00ae1ce8"></a> `00ae1ce8` | `fd 83 02 91` | add x29,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-00ae1cec"></a> `00ae1cec` | `48 d0 3b d5` | mrs x8,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00ae1cf0"></a> `00ae1cf0` | `09 6c 4e 91` | add x9,x0,#0x39b, LSL #12 | `FALL_THROUGH`
<a id="insn-00ae1cf4"></a> `00ae1cf4` | `2b 00 80 52` | mov w11,#0x1 | `FALL_THROUGH`
<a id="insn-00ae1cf8"></a> `00ae1cf8` | `e8 07 00 f9` | str x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00ae1cfc"></a> `00ae1cfc` | `3b f1 25 91` | add x27,x9,#0x97c | `FALL_THROUGH`
<a id="insn-00ae1d00"></a> `00ae1d00` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00ae1d04"></a> `00ae1d04` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00ae1d08"></a> `00ae1d08` | `f5 03 1f aa` | mov x21,xzr | `FALL_THROUGH`
<a id="insn-00ae1d0c"></a> `00ae1d0c` | `98 05 80 52` | mov w24,#0x2c | `FALL_THROUGH`
<a id="insn-00ae1d10"></a> `00ae1d10` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00ae1d14"></a> `00ae1d14` | `68 03 40 b9` | ldr w8,[x27] | `FALL_THROUGH`
<a id="insn-00ae1d18"></a> `00ae1d18` | `69 13 c0 39` | ldrsb w9,[x27, #0x4] | `FALL_THROUGH`
<a id="insn-00ae1d1c"></a> `00ae1d1c` | `08 01 01 0b` | add w8,w8,w1 | `FALL_THROUGH`
<a id="insn-00ae1d20"></a> `00ae1d20` | `08 01 09 0b` | add w8,w8,w9 | `FALL_THROUGH`
<a id="insn-00ae1d24"></a> `00ae1d24` | `0a 0d c9 1a` | sdiv w10,w8,w9 | `FALL_THROUGH`
<a id="insn-00ae1d28"></a> `00ae1d28` | `48 a1 09 1b` | msub w8,w10,w9,w8 | `FALL_THROUGH`
<a id="insn-00ae1d2c"></a> `00ae1d2c` | `89 34 82 52` | mov w9,#0x11a4 | `FALL_THROUGH`
<a id="insn-00ae1d30"></a> `00ae1d30` | `0a b7 98 52` | mov w10,#0xc5b8 | `FALL_THROUGH`
<a id="insn-00ae1d34"></a> `00ae1d34` | `1c 00 0a 8b` | add x28,x0,x10 | `FALL_THROUGH`
<a id="insn-00ae1d38"></a> `00ae1d38` | `0b 68 29 38` | strb w11,[x0, x9, LSL ] | `FALL_THROUGH`
<a id="insn-00ae1d3c"></a> `00ae1d3c` | `09 24 41 91` | add x9,x0,#0x49, LSL #12 | `FALL_THROUGH`
<a id="insn-00ae1d40"></a> `00ae1d40` | `0a cc 4c 91` | add x10,x0,#0x333, LSL #12 | `FALL_THROUGH`
<a id="insn-00ae1d44"></a> `00ae1d44` | `36 d1 24 91` | add x22,x9,#0x934 | `FALL_THROUGH`
<a id="insn-00ae1d48"></a> `00ae1d48` | `57 e1 26 91` | add x23,x10,#0x9b8 | `FALL_THROUGH`
<a id="insn-00ae1d4c"></a> `00ae1d4c` | `68 03 00 b9` | str w8,[x27] | `FALL_THROUGH`
<a id="insn-00ae1d50"></a> `00ae1d50` | `06 00 00 14` | b 0x00ae1d68 | `UNCONDITIONAL_JUMP`
<a id="insn-00ae1d54"></a> `00ae1d54` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00ae1d58"></a> `00ae1d58` | `e8 6a 35 b8` | str w8,[x23, x21, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ae1d5c"></a> `00ae1d5c` | `b5 12 00 91` | add x21,x21,#0x4 | `FALL_THROUGH`
<a id="insn-00ae1d60"></a> `00ae1d60` | `bf a2 00 f1` | cmp x21,#0x28 | `FALL_THROUGH`
<a id="insn-00ae1d64"></a> `00ae1d64` | `40 05 00 54` | b.eq 0x00ae1e0c | `CONDITIONAL_JUMP`
<a id="insn-00ae1d68"></a> `00ae1d68` | `68 03 80 b9` | ldrsw x8,[x27] | `FALL_THROUGH`
<a id="insn-00ae1d6c"></a> `00ae1d6c` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00ae1d70"></a> `00ae1d70` | `09 55 38 9b` | smaddl x9,w8,w24,x21 | `FALL_THROUGH`
<a id="insn-00ae1d74"></a> `00ae1d74` | `08 71 38 9b` | smaddl x8,w8,w24,x28 | `FALL_THROUGH`
<a id="insn-00ae1d78"></a> `00ae1d78` | `8a 03 09 8b` | add x10,x28,x9 | `FALL_THROUGH`
<a id="insn-00ae1d7c"></a> `00ae1d7c` | `89 6b 69 38` | ldrb w9,[x28, x9, LSL ] | `FALL_THROUGH`
<a id="insn-00ae1d80"></a> `00ae1d80` | `4b 09 40 39` | ldrb w11,[x10, #0x2] | `FALL_THROUGH`
<a id="insn-00ae1d84"></a> `00ae1d84` | `0c a9 40 39` | ldrb w12,[x8, #0x2a] | `FALL_THROUGH`
<a id="insn-00ae1d88"></a> `00ae1d88` | `0d ad 40 39` | ldrb w13,[x8, #0x2b] | `FALL_THROUGH`
<a id="insn-00ae1d8c"></a> `00ae1d8c` | `8b 01 0b 4a` | eor w11,w12,w11 | `FALL_THROUGH`
<a id="insn-00ae1d90"></a> `00ae1d90` | `4c 0d 40 39` | ldrb w12,[x10, #0x3] | `FALL_THROUGH`
<a id="insn-00ae1d94"></a> `00ae1d94` | `4a 05 40 39` | ldrb w10,[x10, #0x1] | `FALL_THROUGH`
<a id="insn-00ae1d98"></a> `00ae1d98` | `6b 3d 10 53` | lsl w11,w11,#0x10 | `FALL_THROUGH`
<a id="insn-00ae1d9c"></a> `00ae1d9c` | `ac 01 0c 4a` | eor w12,w13,w12 | `FALL_THROUGH`
<a id="insn-00ae1da0"></a> `00ae1da0` | `0d a5 40 39` | ldrb w13,[x8, #0x29] | `FALL_THROUGH`
<a id="insn-00ae1da4"></a> `00ae1da4` | `08 a1 40 39` | ldrb w8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00ae1da8"></a> `00ae1da8` | `6b 61 0c 2a` | orr w11,w11,w12, LSL #0x18 | `FALL_THROUGH`
<a id="insn-00ae1dac"></a> `00ae1dac` | `aa 01 0a 4a` | eor w10,w13,w10 | `FALL_THROUGH`
<a id="insn-00ae1db0"></a> `00ae1db0` | `08 01 09 4a` | eor w8,w8,w9 | `FALL_THROUGH`
<a id="insn-00ae1db4"></a> `00ae1db4` | `6a 21 0a 2a` | orr w10,w11,w10, LSL #0x8 | `FALL_THROUGH`
<a id="insn-00ae1db8"></a> `00ae1db8` | `48 01 08 2a` | orr w8,w10,w8 | `FALL_THROUGH`
<a id="insn-00ae1dbc"></a> `00ae1dbc` | `14 09 00 71` | subs w20,w8,#0x2 | `FALL_THROUGH`
<a id="insn-00ae1dc0"></a> `00ae1dc0` | `ab fc ff 54` | b.lt 0x00ae1d54 | `CONDITIONAL_JUMP`
<a id="insn-00ae1dc4"></a> `00ae1dc4` | `60 42 01 91` | add x0,x19,#0x50 | `FALL_THROUGH`
<a id="insn-00ae1dc8"></a> `00ae1dc8` | `01 00 80 12` | mov w1,#0xffffffff | `FALL_THROUGH`
<a id="insn-00ae1dcc"></a> `00ae1dcc` | `02 00 80 12` | mov w2,#0xffffffff | `FALL_THROUGH`
<a id="insn-00ae1dd0"></a> `00ae1dd0` | `7c 00 fc 97` | bl 0x009e1fc0 | `UNCONDITIONAL_CALL`
<a id="insn-00ae1dd4"></a> `00ae1dd4` | `60 01 00 36` | tbz w0,#0x0,0x00ae1e00 | `CONDITIONAL_JUMP`
<a id="insn-00ae1dd8"></a> `00ae1dd8` | `60 42 01 91` | add x0,x19,#0x50 | `FALL_THROUGH`
<a id="insn-00ae1ddc"></a> `00ae1ddc` | `01 00 80 12` | mov w1,#0xffffffff | `FALL_THROUGH`
<a id="insn-00ae1de0"></a> `00ae1de0` | `02 00 80 12` | mov w2,#0xffffffff | `FALL_THROUGH`
<a id="insn-00ae1de4"></a> `00ae1de4` | `6c 08 fc 97` | bl 0x009e3f94 | `UNCONDITIONAL_CALL`
<a id="insn-00ae1de8"></a> `00ae1de8` | `c0 00 00 b4` | cbz x0,0x00ae1e00 | `CONDITIONAL_JUMP`
<a id="insn-00ae1dec"></a> `00ae1dec` | `e1 03 14 2a` | mov w1,w20 | `FALL_THROUGH`
<a id="insn-00ae1df0"></a> `00ae1df0` | `11 fa fb 97` | bl 0x009e0634 | `UNCONDITIONAL_CALL`
<a id="insn-00ae1df4"></a> `00ae1df4` | `60 00 00 b4` | cbz x0,0x00ae1e00 | `CONDITIONAL_JUMP`
<a id="insn-00ae1df8"></a> `00ae1df8` | `08 10 00 91` | add x8,x0,#0x4 | `FALL_THROUGH`
<a id="insn-00ae1dfc"></a> `00ae1dfc` | `02 00 00 14` | b 0x00ae1e04 | `UNCONDITIONAL_JUMP`
<a id="insn-00ae1e00"></a> `00ae1e00` | `c8 4a 34 8b` | add x8,x22,w20, UXTW  #0x2 | `FALL_THROUGH`
<a id="insn-00ae1e04"></a> `00ae1e04` | `08 01 40 b9` | ldr w8,[x8] | `FALL_THROUGH`
<a id="insn-00ae1e08"></a> `00ae1e08` | `d4 ff ff 17` | b 0x00ae1d58 | `UNCONDITIONAL_JUMP`
<a id="insn-00ae1e0c"></a> `00ae1e0c` | `28 0e 00 90` | adrp x8,0xca5000 | `FALL_THROUGH`
<a id="insn-00ae1e10"></a> `00ae1e10` | `00 1d 45 f9` | ldr x0,[x8, #0xa38] | `FALL_THROUGH`
<a id="insn-00ae1e14"></a> `00ae1e14` | `20 01 00 b4` | cbz x0,0x00ae1e38 | `CONDITIONAL_JUMP`
<a id="insn-00ae1e18"></a> `00ae1e18` | `21 0c 00 b0` | adrp x1,0xc66000 | `FALL_THROUGH`
<a id="insn-00ae1e1c"></a> `00ae1e1c` | `21 e0 3b 91` | add x1,x1,#0xef8 | `FALL_THROUGH`
<a id="insn-00ae1e20"></a> `00ae1e20` | `62 0d 00 b0` | adrp x2,0xc8e000 | `FALL_THROUGH`
<a id="insn-00ae1e24"></a> `00ae1e24` | `42 c0 27 91` | add x2,x2,#0x9f0 | `FALL_THROUGH`
<a id="insn-00ae1e28"></a> `00ae1e28` | `e3 03 1f aa` | mov x3,xzr | `FALL_THROUGH`
<a id="insn-00ae1e2c"></a> `00ae1e2c` | `21 de 05 94` | bl 0x00c596b0 | `UNCONDITIONAL_CALL`
<a id="insn-00ae1e30"></a> `00ae1e30` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00ae1e34"></a> `00ae1e34` | `02 00 00 14` | b 0x00ae1e3c | `UNCONDITIONAL_JUMP`
<a id="insn-00ae1e38"></a> `00ae1e38` | `f4 03 1f aa` | mov x20,xzr | `FALL_THROUGH`
<a id="insn-00ae1e3c"></a> `00ae1e3c` | `e8 23 01 91` | add x8,sp,#0x48 | `FALL_THROUGH`
<a id="insn-00ae1e40"></a> `00ae1e40` | `e9 63 00 91` | add x9,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00ae1e44"></a> `00ae1e44` | `18 37 87 52` | mov w24,#0x39b8 | `FALL_THROUGH`
<a id="insn-00ae1e48"></a> `00ae1e48` | `f7 03 1f aa` | mov x23,xzr | `FALL_THROUGH`
<a id="insn-00ae1e4c"></a> `00ae1e4c` | `78 06 a0 72` | movk w24,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00ae1e50"></a> `00ae1e50` | `08 01 40 b2` | orr x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00ae1e54"></a> `00ae1e54` | `35 01 40 b2` | orr x21,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00ae1e58"></a> `00ae1e58` | `16 b7 98 52` | mov w22,#0xc5b8 | `FALL_THROUGH`
<a id="insn-00ae1e5c"></a> `00ae1e5c` | `9a 05 80 52` | mov w26,#0x2c | `FALL_THROUGH`
<a id="insn-00ae1e60"></a> `00ae1e60` | `e8 0b 00 f9` | str x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ae1e64"></a> `00ae1e64` | `06 00 00 14` | b 0x00ae1e7c | `UNCONDITIONAL_JUMP`
<a id="insn-00ae1e68"></a> `00ae1e68` | `f7 42 00 91` | add x23,x23,#0x10 | `FALL_THROUGH`
<a id="insn-00ae1e6c"></a> `00ae1e6c` | `18 13 00 91` | add x24,x24,#0x4 | `FALL_THROUGH`
<a id="insn-00ae1e70"></a> `00ae1e70` | `d6 12 00 91` | add x22,x22,#0x4 | `FALL_THROUGH`
<a id="insn-00ae1e74"></a> `00ae1e74` | `ff 82 02 f1` | cmp x23,#0xa0 | `FALL_THROUGH`
<a id="insn-00ae1e78"></a> `00ae1e78` | `c0 15 00 54` | b.eq 0x00ae2130 | `CONDITIONAL_JUMP`
<a id="insn-00ae1e7c"></a> `00ae1e7c` | `68 03 80 b9` | ldrsw x8,[x27] | `FALL_THROUGH`
<a id="insn-00ae1e80"></a> `00ae1e80` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00ae1e84"></a> `00ae1e84` | `09 59 3a 9b` | smaddl x9,w8,w26,x22 | `FALL_THROUGH`
<a id="insn-00ae1e88"></a> `00ae1e88` | `08 71 3a 9b` | smaddl x8,w8,w26,x28 | `FALL_THROUGH`
<a id="insn-00ae1e8c"></a> `00ae1e8c` | `69 02 09 8b` | add x9,x19,x9 | `FALL_THROUGH`
<a id="insn-00ae1e90"></a> `00ae1e90` | `2a 09 40 39` | ldrb w10,[x9, #0x2] | `FALL_THROUGH`
<a id="insn-00ae1e94"></a> `00ae1e94` | `0b a9 40 39` | ldrb w11,[x8, #0x2a] | `FALL_THROUGH`
<a id="insn-00ae1e98"></a> `00ae1e98` | `0c ad 40 39` | ldrb w12,[x8, #0x2b] | `FALL_THROUGH`
<a id="insn-00ae1e9c"></a> `00ae1e9c` | `2d 05 40 39` | ldrb w13,[x9, #0x1] | `FALL_THROUGH`
<a id="insn-00ae1ea0"></a> `00ae1ea0` | `6a 01 0a 4a` | eor w10,w11,w10 | `FALL_THROUGH`
<a id="insn-00ae1ea4"></a> `00ae1ea4` | `2b 0d 40 39` | ldrb w11,[x9, #0x3] | `FALL_THROUGH`
<a id="insn-00ae1ea8"></a> `00ae1ea8` | `29 01 40 39` | ldrb w9,[x9] | `FALL_THROUGH`
<a id="insn-00ae1eac"></a> `00ae1eac` | `4a 3d 10 53` | lsl w10,w10,#0x10 | `FALL_THROUGH`
<a id="insn-00ae1eb0"></a> `00ae1eb0` | `8b 01 0b 4a` | eor w11,w12,w11 | `FALL_THROUGH`
<a id="insn-00ae1eb4"></a> `00ae1eb4` | `0c a5 40 39` | ldrb w12,[x8, #0x29] | `FALL_THROUGH`
<a id="insn-00ae1eb8"></a> `00ae1eb8` | `08 a1 40 39` | ldrb w8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00ae1ebc"></a> `00ae1ebc` | `4a 61 0b 2a` | orr w10,w10,w11, LSL #0x18 | `FALL_THROUGH`
<a id="insn-00ae1ec0"></a> `00ae1ec0` | `8b 01 0d 4a` | eor w11,w12,w13 | `FALL_THROUGH`
<a id="insn-00ae1ec4"></a> `00ae1ec4` | `08 01 09 4a` | eor w8,w8,w9 | `FALL_THROUGH`
<a id="insn-00ae1ec8"></a> `00ae1ec8` | `4a 21 0b 2a` | orr w10,w10,w11, LSL #0x8 | `FALL_THROUGH`
<a id="insn-00ae1ecc"></a> `00ae1ecc` | `48 01 08 2a` | orr w8,w10,w8 | `FALL_THROUGH`
<a id="insn-00ae1ed0"></a> `00ae1ed0` | `1f 05 00 31` | cmn w8,#0x1 | `FALL_THROUGH`
<a id="insn-00ae1ed4"></a> `00ae1ed4` | `a0 03 00 54` | b.eq 0x00ae1f48 | `CONDITIONAL_JUMP`
<a id="insn-00ae1ed8"></a> `00ae1ed8` | `61 6a 78 b8` | ldr w1,[x19, x24, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ae1edc"></a> `00ae1edc` | `00 09 00 51` | sub w0,w8,#0x2 | `FALL_THROUGH`
<a id="insn-00ae1ee0"></a> `00ae1ee0` | `a8 03 01 d1` | sub x8,x29,#0x40 | `FALL_THROUGH`
<a id="insn-00ae1ee4"></a> `00ae1ee4` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-00ae1ee8"></a> `00ae1ee8` | `9b 10 ee 97` | bl 0x00666154 | `UNCONDITIONAL_CALL`
<a id="insn-00ae1eec"></a> `00ae1eec` | `a0 03 dc 3c` | ldur q0,[x29, #-0x40] | `FALL_THROUGH`
<a id="insn-00ae1ef0"></a> `00ae1ef0` | `bf 7f 3c a9` | stp xzr,xzr,[x29, #-0x40] | `FALL_THROUGH`
<a id="insn-00ae1ef4"></a> `00ae1ef4` | `88 02 17 8b` | add x8,x20,x23 | `FALL_THROUGH`
<a id="insn-00ae1ef8"></a> `00ae1ef8` | `19 a5 41 f9` | ldr x25,[x8, #0x348] | `FALL_THROUGH`
<a id="insn-00ae1efc"></a> `00ae1efc` | `00 d1 80 3d` | str q0,[x8, #0x340] | `FALL_THROUGH`
<a id="insn-00ae1f00"></a> `00ae1f00` | `b9 00 00 b4` | cbz x25,0x00ae1f14 | `CONDITIONAL_JUMP`
<a id="insn-00ae1f04"></a> `00ae1f04` | `21 23 00 91` | add x1,x25,#0x8 | `FALL_THROUGH`
<a id="insn-00ae1f08"></a> `00ae1f08` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00ae1f0c"></a> `00ae1f0c` | `a1 cb 05 94` | bl 0x00c54d90 | `UNCONDITIONAL_CALL`
<a id="insn-00ae1f10"></a> `00ae1f10` | `20 09 00 b4` | cbz x0,0x00ae2034 | `CONDITIONAL_JUMP`
<a id="insn-00ae1f14"></a> `00ae1f14` | `b9 83 5c f8` | ldur x25,[x29, #-0x38] | `FALL_THROUGH`
<a id="insn-00ae1f18"></a> `00ae1f18` | `99 fa ff b4` | cbz x25,0x00ae1e68 | `CONDITIONAL_JUMP`
<a id="insn-00ae1f1c"></a> `00ae1f1c` | `21 23 00 91` | add x1,x25,#0x8 | `FALL_THROUGH`
<a id="insn-00ae1f20"></a> `00ae1f20` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00ae1f24"></a> `00ae1f24` | `9b cb 05 94` | bl 0x00c54d90 | `UNCONDITIONAL_CALL`
<a id="insn-00ae1f28"></a> `00ae1f28` | `00 fa ff b5` | cbnz x0,0x00ae1e68 | `CONDITIONAL_JUMP`
<a id="insn-00ae1f2c"></a> `00ae1f2c` | `28 03 40 f9` | ldr x8,[x25] | `FALL_THROUGH`
<a id="insn-00ae1f30"></a> `00ae1f30` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-00ae1f34"></a> `00ae1f34` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00ae1f38"></a> `00ae1f38` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ae1f3c"></a> `00ae1f3c` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-00ae1f40"></a> `00ae1f40` | `f8 db 05 94` | bl 0x00c58f20 | `UNCONDITIONAL_CALL`
<a id="insn-00ae1f44"></a> `00ae1f44` | `c9 ff ff 17` | b 0x00ae1e68 | `UNCONDITIONAL_JUMP`
<a id="insn-00ae1f48"></a> `00ae1f48` | `28 0e 00 90` | adrp x8,0xca5000 | `FALL_THROUGH`
<a id="insn-00ae1f4c"></a> `00ae1f4c` | `08 e1 3f 91` | add x8,x8,#0xff8 | `FALL_THROUGH`
<a id="insn-00ae1f50"></a> `00ae1f50` | `08 fd df 08` | ldarb w8,[x8] | `FALL_THROUGH`
<a id="insn-00ae1f54"></a> `00ae1f54` | `28 0c 00 36` | tbz w8,#0x0,0x00ae20d8 | `CONDITIONAL_JUMP`
<a id="insn-00ae1f58"></a> `00ae1f58` | `c8 01 80 52` | mov w8,#0xe | `FALL_THROUGH`
<a id="insn-00ae1f5c"></a> `00ae1f5c` | `a9 ce 8d 52` | mov w9,#0x6e75 | `FALL_THROUGH`
<a id="insn-00ae1f60"></a> `00ae1f60` | `ff 43 01 39` | strb wzr,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00ae1f64"></a> `00ae1f64` | `e8 23 01 39` | strb w8,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00ae1f68"></a> `00ae1f68` | `e8 0b 40 f9` | ldr x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ae1f6c"></a> `00ae1f6c` | `29 cd a5 72` | movk w9,#0x2e69, LSL #16 | `FALL_THROUGH`
<a id="insn-00ae1f70"></a> `00ae1f70` | `09 01 00 b9` | str w9,[x8] | `FALL_THROUGH`
<a id="insn-00ae1f74"></a> `00ae1f74` | `c9 05 8e 52` | mov w9,#0x702e | `FALL_THROUGH`
<a id="insn-00ae1f78"></a> `00ae1f78` | `c9 ed ac 72` | movk w9,#0x676e, LSL #16 | `FALL_THROUGH`
<a id="insn-00ae1f7c"></a> `00ae1f7c` | `09 31 00 b8` | stur w9,[x8, #0x3] | `FALL_THROUGH`
<a id="insn-00ae1f80"></a> `00ae1f80` | `a8 03 01 d1` | sub x8,x29,#0x40 | `FALL_THROUGH`
<a id="insn-00ae1f84"></a> `00ae1f84` | `e0 23 01 91` | add x0,sp,#0x48 | `FALL_THROUGH`
<a id="insn-00ae1f88"></a> `00ae1f88` | `8b ac e6 97` | bl 0x0048d1b4 | `UNCONDITIONAL_CALL`
<a id="insn-00ae1f8c"></a> `00ae1f8c` | `88 02 80 52` | mov w8,#0x14 | `FALL_THROUGH`
<a id="insn-00ae1f90"></a> `00ae1f90` | `a9 8e 8e 52` | mov w9,#0x7475 | `FALL_THROUGH`
<a id="insn-00ae1f94"></a> `00ae1f94` | `ff 8f 00 39` | strb wzr,[sp, #0x23] | `FALL_THROUGH`
<a id="insn-00ae1f98"></a> `00ae1f98` | `e8 63 00 39` | strb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00ae1f9c"></a> `00ae1f9c` | `48 bf ff b0` | adrp x8,0x2ca000 | `FALL_THROUGH`
<a id="insn-00ae1fa0"></a> `00ae1fa0` | `08 91 2e 91` | add x8,x8,#0xba4 | `FALL_THROUGH`
<a id="insn-00ae1fa4"></a> `00ae1fa4` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00ae1fa8"></a> `00ae1fa8` | `a9 12 00 79` | strh w9,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00ae1fac"></a> `00ae1fac` | `a8 02 00 f9` | str x8,[x21] | `FALL_THROUGH`
<a id="insn-00ae1fb0"></a> `00ae1fb0` | `e8 c3 00 91` | add x8,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00ae1fb4"></a> `00ae1fb4` | `e0 63 00 91` | add x0,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00ae1fb8"></a> `00ae1fb8` | `7f ac e6 97` | bl 0x0048d1b4 | `UNCONDITIONAL_CALL`
<a id="insn-00ae1fbc"></a> `00ae1fbc` | `a8 83 00 d1` | sub x8,x29,#0x20 | `FALL_THROUGH`
<a id="insn-00ae1fc0"></a> `00ae1fc0` | `a1 03 01 d1` | sub x1,x29,#0x40 | `FALL_THROUGH`
<a id="insn-00ae1fc4"></a> `00ae1fc4` | `e2 c3 00 91` | add x2,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00ae1fc8"></a> `00ae1fc8` | `20 0e 00 90` | adrp x0,0xca5000 | `FALL_THROUGH`
<a id="insn-00ae1fcc"></a> `00ae1fcc` | `00 00 3f 91` | add x0,x0,#0xfc0 | `FALL_THROUGH`
<a id="insn-00ae1fd0"></a> `00ae1fd0` | `23 c0 84 52` | mov w3,#0x2601 | `FALL_THROUGH`
<a id="insn-00ae1fd4"></a> `00ae1fd4` | `66 72 e6 97` | bl 0x0047e96c | `UNCONDITIONAL_CALL`
<a id="insn-00ae1fd8"></a> `00ae1fd8` | `a0 03 de 3c` | ldur q0,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00ae1fdc"></a> `00ae1fdc` | `bf 7f 3e a9` | stp xzr,xzr,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00ae1fe0"></a> `00ae1fe0` | `88 02 17 8b` | add x8,x20,x23 | `FALL_THROUGH`
<a id="insn-00ae1fe4"></a> `00ae1fe4` | `19 a5 41 f9` | ldr x25,[x8, #0x348] | `FALL_THROUGH`
<a id="insn-00ae1fe8"></a> `00ae1fe8` | `00 d1 80 3d` | str q0,[x8, #0x340] | `FALL_THROUGH`
<a id="insn-00ae1fec"></a> `00ae1fec` | `b9 00 00 b4` | cbz x25,0x00ae2000 | `CONDITIONAL_JUMP`
<a id="insn-00ae1ff0"></a> `00ae1ff0` | `21 23 00 91` | add x1,x25,#0x8 | `FALL_THROUGH`
<a id="insn-00ae1ff4"></a> `00ae1ff4` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00ae1ff8"></a> `00ae1ff8` | `66 cb 05 94` | bl 0x00c54d90 | `UNCONDITIONAL_CALL`
<a id="insn-00ae1ffc"></a> `00ae1ffc` | `e0 02 00 b4` | cbz x0,0x00ae2058 | `CONDITIONAL_JUMP`
<a id="insn-00ae2000"></a> `00ae2000` | `b9 83 5e f8` | ldur x25,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-00ae2004"></a> `00ae2004` | `b9 03 00 b4` | cbz x25,0x00ae2078 | `CONDITIONAL_JUMP`
<a id="insn-00ae2008"></a> `00ae2008` | `21 23 00 91` | add x1,x25,#0x8 | `FALL_THROUGH`
<a id="insn-00ae200c"></a> `00ae200c` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00ae2010"></a> `00ae2010` | `60 cb 05 94` | bl 0x00c54d90 | `UNCONDITIONAL_CALL`
<a id="insn-00ae2014"></a> `00ae2014` | `20 03 00 b5` | cbnz x0,0x00ae2078 | `CONDITIONAL_JUMP`
<a id="insn-00ae2018"></a> `00ae2018` | `28 03 40 f9` | ldr x8,[x25] | `FALL_THROUGH`
<a id="insn-00ae201c"></a> `00ae201c` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-00ae2020"></a> `00ae2020` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00ae2024"></a> `00ae2024` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ae2028"></a> `00ae2028` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-00ae202c"></a> `00ae202c` | `bd db 05 94` | bl 0x00c58f20 | `UNCONDITIONAL_CALL`
<a id="insn-00ae2030"></a> `00ae2030` | `12 00 00 14` | b 0x00ae2078 | `UNCONDITIONAL_JUMP`
<a id="insn-00ae2034"></a> `00ae2034` | `28 03 40 f9` | ldr x8,[x25] | `FALL_THROUGH`
<a id="insn-00ae2038"></a> `00ae2038` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-00ae203c"></a> `00ae203c` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00ae2040"></a> `00ae2040` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ae2044"></a> `00ae2044` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-00ae2048"></a> `00ae2048` | `b6 db 05 94` | bl 0x00c58f20 | `UNCONDITIONAL_CALL`
<a id="insn-00ae204c"></a> `00ae204c` | `b9 83 5c f8` | ldur x25,[x29, #-0x38] | `FALL_THROUGH`
<a id="insn-00ae2050"></a> `00ae2050` | `79 f6 ff b5` | cbnz x25,0x00ae1f1c | `CONDITIONAL_JUMP`
<a id="insn-00ae2054"></a> `00ae2054` | `85 ff ff 17` | b 0x00ae1e68 | `UNCONDITIONAL_JUMP`
<a id="insn-00ae2058"></a> `00ae2058` | `28 03 40 f9` | ldr x8,[x25] | `FALL_THROUGH`
<a id="insn-00ae205c"></a> `00ae205c` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-00ae2060"></a> `00ae2060` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00ae2064"></a> `00ae2064` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ae2068"></a> `00ae2068` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-00ae206c"></a> `00ae206c` | `ad db 05 94` | bl 0x00c58f20 | `UNCONDITIONAL_CALL`
<a id="insn-00ae2070"></a> `00ae2070` | `b9 83 5e f8` | ldur x25,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-00ae2074"></a> `00ae2074` | `b9 fc ff b5` | cbnz x25,0x00ae2008 | `CONDITIONAL_JUMP`
<a id="insn-00ae2078"></a> `00ae2078` | `e8 c3 40 39` | ldrb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00ae207c"></a> `00ae207c` | `08 01 00 37` | tbnz w8,#0x0,0x00ae209c | `CONDITIONAL_JUMP`
<a id="insn-00ae2080"></a> `00ae2080` | `e8 63 40 39` | ldrb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00ae2084"></a> `00ae2084` | `48 01 00 37` | tbnz w8,#0x0,0x00ae20ac | `CONDITIONAL_JUMP`
<a id="insn-00ae2088"></a> `00ae2088` | `a8 03 5c 38` | ldurb w8,[x29, #-0x40] | `FALL_THROUGH`
<a id="insn-00ae208c"></a> `00ae208c` | `88 01 00 37` | tbnz w8,#0x0,0x00ae20bc | `CONDITIONAL_JUMP`
<a id="insn-00ae2090"></a> `00ae2090` | `e8 23 41 39` | ldrb w8,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00ae2094"></a> `00ae2094` | `a8 ee 07 36` | tbz w8,#0x0,0x00ae1e68 | `CONDITIONAL_JUMP`
<a id="insn-00ae2098"></a> `00ae2098` | `0d 00 00 14` | b 0x00ae20cc | `UNCONDITIONAL_JUMP`
<a id="insn-00ae209c"></a> `00ae209c` | `e0 23 40 f9` | ldr x0,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00ae20a0"></a> `00ae20a0` | `ac db 05 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00ae20a4"></a> `00ae20a4` | `e8 63 40 39` | ldrb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00ae20a8"></a> `00ae20a8` | `08 ff 07 36` | tbz w8,#0x0,0x00ae2088 | `CONDITIONAL_JUMP`
<a id="insn-00ae20ac"></a> `00ae20ac` | `e0 17 40 f9` | ldr x0,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00ae20b0"></a> `00ae20b0` | `a8 db 05 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00ae20b4"></a> `00ae20b4` | `a8 03 5c 38` | ldurb w8,[x29, #-0x40] | `FALL_THROUGH`
<a id="insn-00ae20b8"></a> `00ae20b8` | `c8 fe 07 36` | tbz w8,#0x0,0x00ae2090 | `CONDITIONAL_JUMP`
<a id="insn-00ae20bc"></a> `00ae20bc` | `a0 03 5d f8` | ldur x0,[x29, #-0x30] | `FALL_THROUGH`
<a id="insn-00ae20c0"></a> `00ae20c0` | `a4 db 05 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00ae20c4"></a> `00ae20c4` | `e8 23 41 39` | ldrb w8,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00ae20c8"></a> `00ae20c8` | `08 ed 07 36` | tbz w8,#0x0,0x00ae1e68 | `CONDITIONAL_JUMP`
<a id="insn-00ae20cc"></a> `00ae20cc` | `e0 2f 40 f9` | ldr x0,[sp, #0x58] | `FALL_THROUGH`
<a id="insn-00ae20d0"></a> `00ae20d0` | `a0 db 05 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00ae20d4"></a> `00ae20d4` | `65 ff ff 17` | b 0x00ae1e68 | `UNCONDITIONAL_JUMP`
<a id="insn-00ae20d8"></a> `00ae20d8` | `00 0e 00 f0` | adrp x0,0xca5000 | `FALL_THROUGH`
<a id="insn-00ae20dc"></a> `00ae20dc` | `00 e0 3f 91` | add x0,x0,#0xff8 | `FALL_THROUGH`
<a id="insn-00ae20e0"></a> `00ae20e0` | `84 db 05 94` | bl 0x00c58ef0 | `UNCONDITIONAL_CALL`
<a id="insn-00ae20e4"></a> `00ae20e4` | `a0 f3 ff 34` | cbz w0,0x00ae1f58 | `CONDITIONAL_JUMP`
<a id="insn-00ae20e8"></a> `00ae20e8` | `01 0e 00 f0` | adrp x1,0xca5000 | `FALL_THROUGH`
<a id="insn-00ae20ec"></a> `00ae20ec` | `21 00 3f 91` | add x1,x1,#0xfc0 | `FALL_THROUGH`
<a id="insn-00ae20f0"></a> `00ae20f0` | `e0 cc ff b0` | adrp x0,0x47f000 | `FALL_THROUGH`
<a id="insn-00ae20f4"></a> `00ae20f4` | `00 50 04 91` | add x0,x0,#0x114 | `FALL_THROUGH`
<a id="insn-00ae20f8"></a> `00ae20f8` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00ae20fc"></a> `00ae20fc` | `02 0c 00 d0` | adrp x2,0xc64000 | `FALL_THROUGH`
<a id="insn-00ae2100"></a> `00ae2100` | `42 c0 00 91` | add x2,x2,#0x30 | `FALL_THROUGH`
<a id="insn-00ae2104"></a> `00ae2104` | `1f 8d 00 f8` | str xzr,[x8, #0x8]! | `FALL_THROUGH`
<a id="insn-00ae2108"></a> `00ae2108` | `28 00 00 f9` | str x8,[x1] | `FALL_THROUGH`
<a id="insn-00ae210c"></a> `00ae210c` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00ae2110"></a> `00ae2110` | `3f fc 02 a9` | stp xzr,xzr,[x1, #0x28] | `FALL_THROUGH`
<a id="insn-00ae2114"></a> `00ae2114` | `1f 0d 02 f8` | str xzr,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-00ae2118"></a> `00ae2118` | `3f 20 01 a9` | stp xzr,x8,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-00ae211c"></a> `00ae211c` | `6d db 05 94` | bl 0x00c58ed0 | `UNCONDITIONAL_CALL`
<a id="insn-00ae2120"></a> `00ae2120` | `00 0e 00 f0` | adrp x0,0xca5000 | `FALL_THROUGH`
<a id="insn-00ae2124"></a> `00ae2124` | `00 e0 3f 91` | add x0,x0,#0xff8 | `FALL_THROUGH`
<a id="insn-00ae2128"></a> `00ae2128` | `7a db 05 94` | bl 0x00c58f10 | `UNCONDITIONAL_CALL`
<a id="insn-00ae212c"></a> `00ae212c` | `8b ff ff 17` | b 0x00ae1f58 | `UNCONDITIONAL_JUMP`
<a id="insn-00ae2130"></a> `00ae2130` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00ae2134"></a> `00ae2134` | `ca b9 ff 97` | bl 0x00ad085c | `UNCONDITIONAL_CALL`
<a id="insn-00ae2138"></a> `00ae2138` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ae213c"></a> `00ae213c` | `07 b9 ff 97` | bl 0x00ad0558 | `UNCONDITIONAL_CALL`
<a id="insn-00ae2140"></a> `00ae2140` | `08 e7 85 52` | mov w8,#0x2f38 | `FALL_THROUGH`
<a id="insn-00ae2144"></a> `00ae2144` | `81 64 80 52` | mov w1,#0x324 | `FALL_THROUGH`
<a id="insn-00ae2148"></a> `00ae2148` | `60 02 08 8b` | add x0,x19,x8 | `FALL_THROUGH`
<a id="insn-00ae214c"></a> `00ae214c` | `20 5a f7 97` | bl 0x008b89cc | `UNCONDITIONAL_CALL`
<a id="insn-00ae2150"></a> `00ae2150` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00ae2154"></a> `00ae2154` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ae2158"></a> `00ae2158` | `65 d6 ff 97` | bl 0x00ad7aec | `UNCONDITIONAL_CALL`
<a id="insn-00ae215c"></a> `00ae215c` | `1f 0c 00 71` | cmp w0,#0x3 | `FALL_THROUGH`
<a id="insn-00ae2160"></a> `00ae2160` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00ae2164"></a> `00ae2164` | `e1 17 9f 1a` | cset w1,eq | `FALL_THROUGH`
<a id="insn-00ae2168"></a> `00ae2168` | `77 57 f7 97` | bl 0x008b7f44 | `UNCONDITIONAL_CALL`
<a id="insn-00ae216c"></a> `00ae216c` | `e8 07 40 f9` | ldr x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00ae2170"></a> `00ae2170` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00ae2174"></a> `00ae2174` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00ae2178"></a> `00ae2178` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00ae217c"></a> `00ae217c` | `01 06 00 54` | b.ne 0x00ae223c | `CONDITIONAL_JUMP`
<a id="insn-00ae2180"></a> `00ae2180` | `f4 4f 4f a9` | ldp x20,x19,[sp, #0xf0] | `FALL_THROUGH`
<a id="insn-00ae2184"></a> `00ae2184` | `f6 57 4e a9` | ldp x22,x21,[sp, #0xe0] | `FALL_THROUGH`
<a id="insn-00ae2188"></a> `00ae2188` | `f8 5f 4d a9` | ldp x24,x23,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-00ae218c"></a> `00ae218c` | `fa 67 4c a9` | ldp x26,x25,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00ae2190"></a> `00ae2190` | `fc 6f 4b a9` | ldp x28,x27,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00ae2194"></a> `00ae2194` | `fd 7b 4a a9` | ldp x29,x30,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00ae2198"></a> `00ae2198` | `ff 03 04 91` | add sp,sp,#0x100 | `FALL_THROUGH`
<a id="insn-00ae219c"></a> `00ae219c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00ae223c"></a> `00ae223c` | `51 db 05 94` | bl 0x00c58f80 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00ae1ccc`](#insn-00ae1ccc) 範囲 `[['00ae1ccc', '00ae1cdb']]`
  - `FALL_THROUGH` [`00ae1cd8`](#insn-00ae1cd8) → [`00ae1cdc`](#insn-00ae1cdc)
- ブロック [`00ae1cdc`](#insn-00ae1cdc) 範囲 `[['00ae1cdc', '00ae1ce7']]`
  - `FALL_THROUGH` [`00ae1ce4`](#insn-00ae1ce4) → [`00ae1ce8`](#insn-00ae1ce8)
- ブロック [`00ae1ce8`](#insn-00ae1ce8) 範囲 `[['00ae1ce8', '00ae1ceb']]`
  - `FALL_THROUGH` [`00ae1ce8`](#insn-00ae1ce8) → [`00ae1cec`](#insn-00ae1cec)
- ブロック [`00ae1cec`](#insn-00ae1cec) 範囲 `[['00ae1cec', '00ae1cef']]`
  - `FALL_THROUGH` [`00ae1cec`](#insn-00ae1cec) → [`00ae1cf0`](#insn-00ae1cf0)
- ブロック [`00ae1cf0`](#insn-00ae1cf0) 範囲 `[['00ae1cf0', '00ae1cf3']]`
  - `FALL_THROUGH` [`00ae1cf0`](#insn-00ae1cf0) → [`00ae1cf4`](#insn-00ae1cf4)
- ブロック [`00ae1cf4`](#insn-00ae1cf4) 範囲 `[['00ae1cf4', '00ae1cf7']]`
  - `FALL_THROUGH` [`00ae1cf4`](#insn-00ae1cf4) → [`00ae1cf8`](#insn-00ae1cf8)
- ブロック [`00ae1cf8`](#insn-00ae1cf8) 範囲 `[['00ae1cf8', '00ae1cfb']]`
  - `FALL_THROUGH` [`00ae1cf8`](#insn-00ae1cf8) → [`00ae1cfc`](#insn-00ae1cfc)
- ブロック [`00ae1cfc`](#insn-00ae1cfc) 範囲 `[['00ae1cfc', '00ae1cff']]`
  - `FALL_THROUGH` [`00ae1cfc`](#insn-00ae1cfc) → [`00ae1d00`](#insn-00ae1d00)
- ブロック [`00ae1d00`](#insn-00ae1d00) 範囲 `[['00ae1d00', '00ae1d17']]`
  - `FALL_THROUGH` [`00ae1d14`](#insn-00ae1d14) → [`00ae1d18`](#insn-00ae1d18)
- ブロック [`00ae1d18`](#insn-00ae1d18) 範囲 `[['00ae1d18', '00ae1d2f']]`
  - `FALL_THROUGH` [`00ae1d2c`](#insn-00ae1d2c) → [`00ae1d30`](#insn-00ae1d30)
- ブロック [`00ae1d30`](#insn-00ae1d30) 範囲 `[['00ae1d30', '00ae1d37']]`
  - `FALL_THROUGH` [`00ae1d34`](#insn-00ae1d34) → [`00ae1d38`](#insn-00ae1d38)
- ブロック [`00ae1d38`](#insn-00ae1d38) 範囲 `[['00ae1d38', '00ae1d3f']]`
  - `FALL_THROUGH` [`00ae1d3c`](#insn-00ae1d3c) → [`00ae1d40`](#insn-00ae1d40)
- ブロック [`00ae1d40`](#insn-00ae1d40) 範囲 `[['00ae1d40', '00ae1d43']]`
  - `FALL_THROUGH` [`00ae1d40`](#insn-00ae1d40) → [`00ae1d44`](#insn-00ae1d44)
- ブロック [`00ae1d44`](#insn-00ae1d44) 範囲 `[['00ae1d44', '00ae1d53']]`
  - `UNCONDITIONAL_JUMP` [`00ae1d50`](#insn-00ae1d50) → [`00ae1d68`](#insn-00ae1d68)
- ブロック [`00ae1d54`](#insn-00ae1d54) 範囲 `[['00ae1d54', '00ae1d57']]`
  - `FALL_THROUGH` [`00ae1d54`](#insn-00ae1d54) → [`00ae1d58`](#insn-00ae1d58)
- ブロック [`00ae1d58`](#insn-00ae1d58) 範囲 `[['00ae1d58', '00ae1d67']]`
  - `CONDITIONAL_JUMP` [`00ae1d64`](#insn-00ae1d64) → [`00ae1e0c`](#insn-00ae1e0c)
  - `FALL_THROUGH` [`00ae1d64`](#insn-00ae1d64) → [`00ae1d68`](#insn-00ae1d68)
- ブロック [`00ae1d68`](#insn-00ae1d68) 範囲 `[['00ae1d68', '00ae1dc3']]`
  - `CONDITIONAL_JUMP` [`00ae1dc0`](#insn-00ae1dc0) → [`00ae1d54`](#insn-00ae1d54)
  - `FALL_THROUGH` [`00ae1dc0`](#insn-00ae1dc0) → [`00ae1dc4`](#insn-00ae1dc4)
- ブロック [`00ae1dc4`](#insn-00ae1dc4) 範囲 `[['00ae1dc4', '00ae1dd7']]`
  - `CONDITIONAL_JUMP` [`00ae1dd4`](#insn-00ae1dd4) → [`00ae1e00`](#insn-00ae1e00)
  - `FALL_THROUGH` [`00ae1dd4`](#insn-00ae1dd4) → [`00ae1dd8`](#insn-00ae1dd8)
- ブロック [`00ae1dd8`](#insn-00ae1dd8) 範囲 `[['00ae1dd8', '00ae1deb']]`
  - `CONDITIONAL_JUMP` [`00ae1de8`](#insn-00ae1de8) → [`00ae1e00`](#insn-00ae1e00)
  - `FALL_THROUGH` [`00ae1de8`](#insn-00ae1de8) → [`00ae1dec`](#insn-00ae1dec)
- ブロック [`00ae1dec`](#insn-00ae1dec) 範囲 `[['00ae1dec', '00ae1df7']]`
  - `CONDITIONAL_JUMP` [`00ae1df4`](#insn-00ae1df4) → [`00ae1e00`](#insn-00ae1e00)
  - `FALL_THROUGH` [`00ae1df4`](#insn-00ae1df4) → [`00ae1df8`](#insn-00ae1df8)
- ブロック [`00ae1df8`](#insn-00ae1df8) 範囲 `[['00ae1df8', '00ae1dff']]`
  - `UNCONDITIONAL_JUMP` [`00ae1dfc`](#insn-00ae1dfc) → [`00ae1e04`](#insn-00ae1e04)
- ブロック [`00ae1e00`](#insn-00ae1e00) 範囲 `[['00ae1e00', '00ae1e03']]`
  - `FALL_THROUGH` [`00ae1e00`](#insn-00ae1e00) → [`00ae1e04`](#insn-00ae1e04)
- ブロック [`00ae1e04`](#insn-00ae1e04) 範囲 `[['00ae1e04', '00ae1e0b']]`
  - `UNCONDITIONAL_JUMP` [`00ae1e08`](#insn-00ae1e08) → [`00ae1d58`](#insn-00ae1d58)
- ブロック [`00ae1e0c`](#insn-00ae1e0c) 範囲 `[['00ae1e0c', '00ae1e17']]`
  - `CONDITIONAL_JUMP` [`00ae1e14`](#insn-00ae1e14) → [`00ae1e38`](#insn-00ae1e38)
  - `FALL_THROUGH` [`00ae1e14`](#insn-00ae1e14) → [`00ae1e18`](#insn-00ae1e18)
- ブロック [`00ae1e18`](#insn-00ae1e18) 範囲 `[['00ae1e18', '00ae1e37']]`
  - `UNCONDITIONAL_JUMP` [`00ae1e34`](#insn-00ae1e34) → [`00ae1e3c`](#insn-00ae1e3c)
- ブロック [`00ae1e38`](#insn-00ae1e38) 範囲 `[['00ae1e38', '00ae1e3b']]`
  - `FALL_THROUGH` [`00ae1e38`](#insn-00ae1e38) → [`00ae1e3c`](#insn-00ae1e3c)
- ブロック [`00ae1e3c`](#insn-00ae1e3c) 範囲 `[['00ae1e3c', '00ae1e67']]`
  - `UNCONDITIONAL_JUMP` [`00ae1e64`](#insn-00ae1e64) → [`00ae1e7c`](#insn-00ae1e7c)
- ブロック [`00ae1e68`](#insn-00ae1e68) 範囲 `[['00ae1e68', '00ae1e7b']]`
  - `CONDITIONAL_JUMP` [`00ae1e78`](#insn-00ae1e78) → [`00ae2130`](#insn-00ae2130)
  - `FALL_THROUGH` [`00ae1e78`](#insn-00ae1e78) → [`00ae1e7c`](#insn-00ae1e7c)
- ブロック [`00ae1e7c`](#insn-00ae1e7c) 範囲 `[['00ae1e7c', '00ae1ed7']]`
  - `CONDITIONAL_JUMP` [`00ae1ed4`](#insn-00ae1ed4) → [`00ae1f48`](#insn-00ae1f48)
  - `FALL_THROUGH` [`00ae1ed4`](#insn-00ae1ed4) → [`00ae1ed8`](#insn-00ae1ed8)
- ブロック [`00ae1ed8`](#insn-00ae1ed8) 範囲 `[['00ae1ed8', '00ae1f03']]`
  - `CONDITIONAL_JUMP` [`00ae1f00`](#insn-00ae1f00) → [`00ae1f14`](#insn-00ae1f14)
  - `FALL_THROUGH` [`00ae1f00`](#insn-00ae1f00) → [`00ae1f04`](#insn-00ae1f04)
- ブロック [`00ae1f04`](#insn-00ae1f04) 範囲 `[['00ae1f04', '00ae1f13']]`
  - `CONDITIONAL_JUMP` [`00ae1f10`](#insn-00ae1f10) → [`00ae2034`](#insn-00ae2034)
  - `FALL_THROUGH` [`00ae1f10`](#insn-00ae1f10) → [`00ae1f14`](#insn-00ae1f14)
- ブロック [`00ae1f14`](#insn-00ae1f14) 範囲 `[['00ae1f14', '00ae1f1b']]`
  - `CONDITIONAL_JUMP` [`00ae1f18`](#insn-00ae1f18) → [`00ae1e68`](#insn-00ae1e68)
  - `FALL_THROUGH` [`00ae1f18`](#insn-00ae1f18) → [`00ae1f1c`](#insn-00ae1f1c)
- ブロック [`00ae1f1c`](#insn-00ae1f1c) 範囲 `[['00ae1f1c', '00ae1f2b']]`
  - `CONDITIONAL_JUMP` [`00ae1f28`](#insn-00ae1f28) → [`00ae1e68`](#insn-00ae1e68)
  - `FALL_THROUGH` [`00ae1f28`](#insn-00ae1f28) → [`00ae1f2c`](#insn-00ae1f2c)
- ブロック [`00ae1f2c`](#insn-00ae1f2c) 範囲 `[['00ae1f2c', '00ae1f47']]`
  - `UNCONDITIONAL_JUMP` [`00ae1f44`](#insn-00ae1f44) → [`00ae1e68`](#insn-00ae1e68)
- ブロック [`00ae1f48`](#insn-00ae1f48) 範囲 `[['00ae1f48', '00ae1f57']]`
  - `CONDITIONAL_JUMP` [`00ae1f54`](#insn-00ae1f54) → [`00ae20d8`](#insn-00ae20d8)
  - `FALL_THROUGH` [`00ae1f54`](#insn-00ae1f54) → [`00ae1f58`](#insn-00ae1f58)
- ブロック [`00ae1f58`](#insn-00ae1f58) 範囲 `[['00ae1f58', '00ae1fef']]`
  - `CONDITIONAL_JUMP` [`00ae1fec`](#insn-00ae1fec) → [`00ae2000`](#insn-00ae2000)
  - `FALL_THROUGH` [`00ae1fec`](#insn-00ae1fec) → [`00ae1ff0`](#insn-00ae1ff0)
- ブロック [`00ae1ff0`](#insn-00ae1ff0) 範囲 `[['00ae1ff0', '00ae1fff']]`
  - `CONDITIONAL_JUMP` [`00ae1ffc`](#insn-00ae1ffc) → [`00ae2058`](#insn-00ae2058)
  - `FALL_THROUGH` [`00ae1ffc`](#insn-00ae1ffc) → [`00ae2000`](#insn-00ae2000)
- ブロック [`00ae2000`](#insn-00ae2000) 範囲 `[['00ae2000', '00ae2007']]`
  - `CONDITIONAL_JUMP` [`00ae2004`](#insn-00ae2004) → [`00ae2078`](#insn-00ae2078)
  - `FALL_THROUGH` [`00ae2004`](#insn-00ae2004) → [`00ae2008`](#insn-00ae2008)
- ブロック [`00ae2008`](#insn-00ae2008) 範囲 `[['00ae2008', '00ae2017']]`
  - `CONDITIONAL_JUMP` [`00ae2014`](#insn-00ae2014) → [`00ae2078`](#insn-00ae2078)
  - `FALL_THROUGH` [`00ae2014`](#insn-00ae2014) → [`00ae2018`](#insn-00ae2018)
- ブロック [`00ae2018`](#insn-00ae2018) 範囲 `[['00ae2018', '00ae2033']]`
  - `UNCONDITIONAL_JUMP` [`00ae2030`](#insn-00ae2030) → [`00ae2078`](#insn-00ae2078)
- ブロック [`00ae2034`](#insn-00ae2034) 範囲 `[['00ae2034', '00ae2053']]`
  - `CONDITIONAL_JUMP` [`00ae2050`](#insn-00ae2050) → [`00ae1f1c`](#insn-00ae1f1c)
  - `FALL_THROUGH` [`00ae2050`](#insn-00ae2050) → [`00ae2054`](#insn-00ae2054)
- ブロック [`00ae2054`](#insn-00ae2054) 範囲 `[['00ae2054', '00ae2057']]`
  - `UNCONDITIONAL_JUMP` [`00ae2054`](#insn-00ae2054) → [`00ae1e68`](#insn-00ae1e68)
- ブロック [`00ae2058`](#insn-00ae2058) 範囲 `[['00ae2058', '00ae2077']]`
  - `CONDITIONAL_JUMP` [`00ae2074`](#insn-00ae2074) → [`00ae2008`](#insn-00ae2008)
  - `FALL_THROUGH` [`00ae2074`](#insn-00ae2074) → [`00ae2078`](#insn-00ae2078)
- ブロック [`00ae2078`](#insn-00ae2078) 範囲 `[['00ae2078', '00ae207f']]`
  - `CONDITIONAL_JUMP` [`00ae207c`](#insn-00ae207c) → [`00ae209c`](#insn-00ae209c)
  - `FALL_THROUGH` [`00ae207c`](#insn-00ae207c) → [`00ae2080`](#insn-00ae2080)
- ブロック [`00ae2080`](#insn-00ae2080) 範囲 `[['00ae2080', '00ae2087']]`
  - `CONDITIONAL_JUMP` [`00ae2084`](#insn-00ae2084) → [`00ae20ac`](#insn-00ae20ac)
  - `FALL_THROUGH` [`00ae2084`](#insn-00ae2084) → [`00ae2088`](#insn-00ae2088)
- ブロック [`00ae2088`](#insn-00ae2088) 範囲 `[['00ae2088', '00ae208f']]`
  - `CONDITIONAL_JUMP` [`00ae208c`](#insn-00ae208c) → [`00ae20bc`](#insn-00ae20bc)
  - `FALL_THROUGH` [`00ae208c`](#insn-00ae208c) → [`00ae2090`](#insn-00ae2090)
- ブロック [`00ae2090`](#insn-00ae2090) 範囲 `[['00ae2090', '00ae2097']]`
  - `CONDITIONAL_JUMP` [`00ae2094`](#insn-00ae2094) → [`00ae1e68`](#insn-00ae1e68)
  - `FALL_THROUGH` [`00ae2094`](#insn-00ae2094) → [`00ae2098`](#insn-00ae2098)
- ブロック [`00ae2098`](#insn-00ae2098) 範囲 `[['00ae2098', '00ae209b']]`
  - `UNCONDITIONAL_JUMP` [`00ae2098`](#insn-00ae2098) → [`00ae20cc`](#insn-00ae20cc)
- ブロック [`00ae209c`](#insn-00ae209c) 範囲 `[['00ae209c', '00ae20ab']]`
  - `CONDITIONAL_JUMP` [`00ae20a8`](#insn-00ae20a8) → [`00ae2088`](#insn-00ae2088)
  - `FALL_THROUGH` [`00ae20a8`](#insn-00ae20a8) → [`00ae20ac`](#insn-00ae20ac)
- ブロック [`00ae20ac`](#insn-00ae20ac) 範囲 `[['00ae20ac', '00ae20bb']]`
  - `CONDITIONAL_JUMP` [`00ae20b8`](#insn-00ae20b8) → [`00ae2090`](#insn-00ae2090)
  - `FALL_THROUGH` [`00ae20b8`](#insn-00ae20b8) → [`00ae20bc`](#insn-00ae20bc)
- ブロック [`00ae20bc`](#insn-00ae20bc) 範囲 `[['00ae20bc', '00ae20cb']]`
  - `CONDITIONAL_JUMP` [`00ae20c8`](#insn-00ae20c8) → [`00ae1e68`](#insn-00ae1e68)
  - `FALL_THROUGH` [`00ae20c8`](#insn-00ae20c8) → [`00ae20cc`](#insn-00ae20cc)
- ブロック [`00ae20cc`](#insn-00ae20cc) 範囲 `[['00ae20cc', '00ae20d7']]`
  - `UNCONDITIONAL_JUMP` [`00ae20d4`](#insn-00ae20d4) → [`00ae1e68`](#insn-00ae1e68)
- ブロック [`00ae20d8`](#insn-00ae20d8) 範囲 `[['00ae20d8', '00ae20e7']]`
  - `CONDITIONAL_JUMP` [`00ae20e4`](#insn-00ae20e4) → [`00ae1f58`](#insn-00ae1f58)
  - `FALL_THROUGH` [`00ae20e4`](#insn-00ae20e4) → [`00ae20e8`](#insn-00ae20e8)
- ブロック [`00ae20e8`](#insn-00ae20e8) 範囲 `[['00ae20e8', '00ae212f']]`
  - `UNCONDITIONAL_JUMP` [`00ae212c`](#insn-00ae212c) → [`00ae1f58`](#insn-00ae1f58)
- ブロック [`00ae2130`](#insn-00ae2130) 範囲 `[['00ae2130', '00ae217f']]`
  - `CONDITIONAL_JUMP` [`00ae217c`](#insn-00ae217c) → [`00ae223c`](#insn-00ae223c)
  - `FALL_THROUGH` [`00ae217c`](#insn-00ae217c) → [`00ae2180`](#insn-00ae2180)
- ブロック [`00ae2180`](#insn-00ae2180) 範囲 `[['00ae2180', '00ae219f']]`
- ブロック [`00ae223c`](#insn-00ae223c) 範囲 `[['00ae223c', '00ae223f']]`

## 命令位置別の参照

- [`00ae1cd0`](#insn-00ae1cd0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae1cd4`](#insn-00ae1cd4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae1cd8`](#insn-00ae1cd8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae1cdc`](#insn-00ae1cdc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae1ce0`](#insn-00ae1ce0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae1ce4`](#insn-00ae1ce4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae1cf8`](#insn-00ae1cf8) → `Stack[-0xf8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae1d10`](#insn-00ae1d10) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae1d14`](#insn-00ae1d14) → `0039b97c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `qword`
- [`00ae1d18`](#insn-00ae1d18) → `0039b980`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `fde_0039b980` · 推定型 `dword`
- [`00ae1d4c`](#insn-00ae1d4c) → `0039b97c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `qword`
- [`00ae1d50`](#insn-00ae1d50) → [`00ae1d68`](#insn-00ae1d68) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae1d58`](#insn-00ae1d58) → `003339b8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ae1d64`](#insn-00ae1d64) → [`00ae1e0c`](#insn-00ae1e0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae1d68`](#insn-00ae1d68) → `0039b97c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `qword`
- [`00ae1dc0`](#insn-00ae1dc0) → [`00ae1d54`](#insn-00ae1d54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae1dd0`](#insn-00ae1dd0) → [`009e1fc0`](../009e1/009e1fc0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009e1fc0` · 推定シンボル `None` · 推定型 `None`
- [`00ae1dd4`](#insn-00ae1dd4) → [`00ae1e00`](#insn-00ae1e00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae1de4`](#insn-00ae1de4) → [`009e3f94`](../009e3/009e3f94.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009e3f94` · 推定シンボル `None` · 推定型 `None`
- [`00ae1de8`](#insn-00ae1de8) → [`00ae1e00`](#insn-00ae1e00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae1df0`](#insn-00ae1df0) → [`009e0634`](../009e0/009e0634.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009e0634` · 推定シンボル `None` · 推定型 `None`
- [`00ae1df4`](#insn-00ae1df4) → [`00ae1e00`](#insn-00ae1e00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae1dfc`](#insn-00ae1dfc) → [`00ae1e04`](#insn-00ae1e04) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae1e08`](#insn-00ae1e08) → [`00ae1d58`](#insn-00ae1d58) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae1e10`](#insn-00ae1e10) → `00ca5a38`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ae1e14`](#insn-00ae1e14) → [`00ae1e38`](#insn-00ae1e38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae1e1c`](#insn-00ae1e1c) → `00c66ef8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x10)))`
- [`00ae1e24`](#insn-00ae1e24) → `00c8e9f0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x10)))`
- [`00ae1e2c`](#insn-00ae1e2c) → [`00c596b0`](../00c59/00c596b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c596b0` · 推定シンボル `None` · 推定型 `None`
- [`00ae1e34`](#insn-00ae1e34) → [`00ae1e3c`](#insn-00ae1e3c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae1e60`](#insn-00ae1e60) → `Stack[-0xf0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae1e64`](#insn-00ae1e64) → [`00ae1e7c`](#insn-00ae1e7c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae1e78`](#insn-00ae1e78) → [`00ae2130`](#insn-00ae2130) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae1e7c`](#insn-00ae1e7c) → `0039b97c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `qword`
- [`00ae1ed4`](#insn-00ae1ed4) → [`00ae1f48`](#insn-00ae1f48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae1ed8`](#insn-00ae1ed8) → `003339b8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ae1ee8`](#insn-00ae1ee8) → [`00666154`](../00666/00666154.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00666154` · 推定シンボル `None` · 推定型 `None`
- [`00ae1eec`](#insn-00ae1eec) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae1ef0`](#insn-00ae1ef0) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae1f00`](#insn-00ae1f00) → [`00ae1f14`](#insn-00ae1f14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae1f0c`](#insn-00ae1f0c) → [`00c54d90`](../00c54/00c54d90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c54d90` · 推定シンボル `None` · 推定型 `None`
- [`00ae1f10`](#insn-00ae1f10) → [`00ae2034`](#insn-00ae2034) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae1f14`](#insn-00ae1f14) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae1f18`](#insn-00ae1f18) → [`00ae1e68`](#insn-00ae1e68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae1f24`](#insn-00ae1f24) → [`00c54d90`](../00c54/00c54d90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c54d90` · 推定シンボル `None` · 推定型 `None`
- [`00ae1f28`](#insn-00ae1f28) → [`00ae1e68`](#insn-00ae1e68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae1f40`](#insn-00ae1f40) → [`00c58f20`](../00c58/00c58f20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f20` · 推定シンボル `None` · 推定型 `None`
- [`00ae1f44`](#insn-00ae1f44) → [`00ae1e68`](#insn-00ae1e68) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae1f50`](#insn-00ae1f50) → `00ca5ff8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00ae1f54`](#insn-00ae1f54) → [`00ae20d8`](#insn-00ae20d8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae1f60`](#insn-00ae1f60) → `Stack[-0xb0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae1f64`](#insn-00ae1f64) → `Stack[-0xb8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae1f68`](#insn-00ae1f68) → `Stack[-0xf0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae1f88`](#insn-00ae1f88) → [`0048d1b4`](../0048d/0048d1b4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0048d1b4` · 推定シンボル `None` · 推定型 `None`
- [`00ae1f94`](#insn-00ae1f94) → `Stack[-0xdd]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae1f98`](#insn-00ae1f98) → `Stack[-0xe8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae1fa4`](#insn-00ae1fa4) → `002caba4`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00ae1fb8`](#insn-00ae1fb8) → [`0048d1b4`](../0048d/0048d1b4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0048d1b4` · 推定シンボル `None` · 推定型 `None`
- [`00ae1fcc`](#insn-00ae1fcc) → `00ca5fc0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ae1fd4`](#insn-00ae1fd4) → [`0047e96c`](../0047e/0047e96c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047e96c` · 推定シンボル `None` · 推定型 `None`
- [`00ae1fd8`](#insn-00ae1fd8) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae1fdc`](#insn-00ae1fdc) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae1fec`](#insn-00ae1fec) → [`00ae2000`](#insn-00ae2000) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae1ff8`](#insn-00ae1ff8) → [`00c54d90`](../00c54/00c54d90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c54d90` · 推定シンボル `None` · 推定型 `None`
- [`00ae1ffc`](#insn-00ae1ffc) → [`00ae2058`](#insn-00ae2058) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae2000`](#insn-00ae2000) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae2004`](#insn-00ae2004) → [`00ae2078`](#insn-00ae2078) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae2010`](#insn-00ae2010) → [`00c54d90`](../00c54/00c54d90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c54d90` · 推定シンボル `None` · 推定型 `None`
- [`00ae2014`](#insn-00ae2014) → [`00ae2078`](#insn-00ae2078) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae202c`](#insn-00ae202c) → [`00c58f20`](../00c58/00c58f20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f20` · 推定シンボル `None` · 推定型 `None`
- [`00ae2030`](#insn-00ae2030) → [`00ae2078`](#insn-00ae2078) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae2048`](#insn-00ae2048) → [`00c58f20`](../00c58/00c58f20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f20` · 推定シンボル `None` · 推定型 `None`
- [`00ae204c`](#insn-00ae204c) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae2050`](#insn-00ae2050) → [`00ae1f1c`](#insn-00ae1f1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae2054`](#insn-00ae2054) → [`00ae1e68`](#insn-00ae1e68) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae206c`](#insn-00ae206c) → [`00c58f20`](../00c58/00c58f20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f20` · 推定シンボル `None` · 推定型 `None`
- [`00ae2070`](#insn-00ae2070) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae2074`](#insn-00ae2074) → [`00ae2008`](#insn-00ae2008) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae2078`](#insn-00ae2078) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae207c`](#insn-00ae207c) → [`00ae209c`](#insn-00ae209c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae2080`](#insn-00ae2080) → `Stack[-0xe8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae2084`](#insn-00ae2084) → [`00ae20ac`](#insn-00ae20ac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae2088`](#insn-00ae2088) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae208c`](#insn-00ae208c) → [`00ae20bc`](#insn-00ae20bc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae2090`](#insn-00ae2090) → `Stack[-0xb8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae2094`](#insn-00ae2094) → [`00ae1e68`](#insn-00ae1e68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae2098`](#insn-00ae2098) → [`00ae20cc`](#insn-00ae20cc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae209c`](#insn-00ae209c) → `Stack[-0xc0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae20a0`](#insn-00ae20a0) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00ae20a4`](#insn-00ae20a4) → `Stack[-0xe8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae20a8`](#insn-00ae20a8) → [`00ae2088`](#insn-00ae2088) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae20ac`](#insn-00ae20ac) → `Stack[-0xd8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae20b0`](#insn-00ae20b0) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00ae20b4`](#insn-00ae20b4) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae20b8`](#insn-00ae20b8) → [`00ae2090`](#insn-00ae2090) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae20bc`](#insn-00ae20bc) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae20c0`](#insn-00ae20c0) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00ae20c4`](#insn-00ae20c4) → `Stack[-0xb8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae20c8`](#insn-00ae20c8) → [`00ae1e68`](#insn-00ae1e68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae20cc`](#insn-00ae20cc) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae20d0`](#insn-00ae20d0) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00ae20d4`](#insn-00ae20d4) → [`00ae1e68`](#insn-00ae1e68) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae20dc`](#insn-00ae20dc) → `00ca5ff8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00ae20e0`](#insn-00ae20e0) → [`00c58ef0`](../00c58/00c58ef0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58ef0` · 推定シンボル `None` · 推定型 `None`
- [`00ae20e4`](#insn-00ae20e4) → [`00ae1f58`](#insn-00ae1f58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae20ec`](#insn-00ae20ec) → `00ca5fc0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ae20f4`](#insn-00ae20f4) → [`0047f114`](../0047f/0047f114.md) · `PARAM` · `ANALYSIS` · 関数 `0047f114` · 推定シンボル `None` · 推定型 `None`
- [`00ae2100`](#insn-00ae2100) → `00c64030`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00ae2104`](#insn-00ae2104) → `00ca5fc8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ae2108`](#insn-00ae2108) → `00ca5fc0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ae2108`](#insn-00ae2108) → `00ca5fc8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ae2110`](#insn-00ae2110) → `00ca5fe8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ae2110`](#insn-00ae2110) → `00ca5ff0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ae2114`](#insn-00ae2114) → `00ca5fe0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ae2118`](#insn-00ae2118) → `00ca5fd0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ae2118`](#insn-00ae2118) → `00ca5fd8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ae2118`](#insn-00ae2118) → `00ca5fe0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ae211c`](#insn-00ae211c) → [`00c58ed0`](../00c58/00c58ed0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58ed0` · 推定シンボル `None` · 推定型 `None`
- [`00ae2124`](#insn-00ae2124) → `00ca5ff8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00ae2128`](#insn-00ae2128) → [`00c58f10`](../00c58/00c58f10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f10` · 推定シンボル `None` · 推定型 `None`
- [`00ae212c`](#insn-00ae212c) → [`00ae1f58`](#insn-00ae1f58) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae2134`](#insn-00ae2134) → [`00ad085c`](../00ad0/00ad085c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ad085c` · 推定シンボル `None` · 推定型 `None`
- [`00ae213c`](#insn-00ae213c) → [`00ad0558`](../00ad0/00ad0558.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ad0558` · 推定シンボル `None` · 推定型 `None`
- [`00ae214c`](#insn-00ae214c) → [`008b89cc`](../008b8/008b89cc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b89cc` · 推定シンボル `None` · 推定型 `None`
- [`00ae2158`](#insn-00ae2158) → [`00ad7aec`](../00ad7/00ad7aec.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ad7aec` · 推定シンボル `None` · 推定型 `None`
- [`00ae2168`](#insn-00ae2168) → [`008b7f44`](../008b7/008b7f44.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b7f44` · 推定シンボル `None` · 推定型 `None`
- [`00ae216c`](#insn-00ae216c) → `Stack[-0xf8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae2174`](#insn-00ae2174) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae217c`](#insn-00ae217c) → [`00ae223c`](#insn-00ae223c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae2180`](#insn-00ae2180) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae2184`](#insn-00ae2184) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae2188`](#insn-00ae2188) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae218c`](#insn-00ae218c) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae2190`](#insn-00ae2190) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae2194`](#insn-00ae2194) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae223c`](#insn-00ae223c) → [`00c58f80`](../00c58/00c58f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f80` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00ae1cd0`](#insn-00ae1cd0)

~~~json
{
  "source": "00ae1cd0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae1cd4`](#insn-00ae1cd4)

~~~json
{
  "source": "00ae1cd4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae1cd8`](#insn-00ae1cd8)

~~~json
{
  "source": "00ae1cd8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae1cdc`](#insn-00ae1cdc)

~~~json
{
  "source": "00ae1cdc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae1ce0`](#insn-00ae1ce0)

~~~json
{
  "source": "00ae1ce0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae1ce4`](#insn-00ae1ce4)

~~~json
{
  "source": "00ae1ce4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae1cf8`](#insn-00ae1cf8)

~~~json
{
  "source": "00ae1cf8",
  "target": "Stack[-0xf8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae1d10`](#insn-00ae1d10)

~~~json
{
  "source": "00ae1d10",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae1d14`](#insn-00ae1d14)

~~~json
{
  "source": "00ae1d14",
  "target": "0039b97c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0039b978",
  "offset": 4,
  "size": 8,
  "datatype": "qword",
  "bytes": "1c00000000000000",
  "capture_start": "0039b978",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ae1d18`](#insn-00ae1d18)

~~~json
{
  "source": "00ae1d18",
  "target": "0039b980",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0039b980",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "10000000",
  "capture_start": "0039b980",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ae1d4c`](#insn-00ae1d4c)

~~~json
{
  "source": "00ae1d4c",
  "target": "0039b97c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0039b978",
  "offset": 4,
  "size": 8,
  "datatype": "qword",
  "bytes": "1c00000000000000",
  "capture_start": "0039b978",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ae1d50`](#insn-00ae1d50)

~~~json
{
  "source": "00ae1d50",
  "target": "00ae1d68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae1d58`](#insn-00ae1d58)

~~~json
{
  "source": "00ae1d58",
  "target": "003339b8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003339b8",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "60b66a00a0770900",
  "capture_start": "003339b8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ae1d64`](#insn-00ae1d64)

~~~json
{
  "source": "00ae1d64",
  "target": "00ae1e0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae1d68`](#insn-00ae1d68)

~~~json
{
  "source": "00ae1d68",
  "target": "0039b97c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0039b978",
  "offset": 4,
  "size": 8,
  "datatype": "qword",
  "bytes": "1c00000000000000",
  "capture_start": "0039b978",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ae1dc0`](#insn-00ae1dc0)

~~~json
{
  "source": "00ae1dc0",
  "target": "00ae1d54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae1dd0`](#insn-00ae1dd0)

~~~json
{
  "source": "00ae1dd0",
  "target": "009e1fc0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ae1dd4`](#insn-00ae1dd4)

~~~json
{
  "source": "00ae1dd4",
  "target": "00ae1e00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae1de4`](#insn-00ae1de4)

~~~json
{
  "source": "00ae1de4",
  "target": "009e3f94",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ae1de8`](#insn-00ae1de8)

~~~json
{
  "source": "00ae1de8",
  "target": "00ae1e00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae1df0`](#insn-00ae1df0)

~~~json
{
  "source": "00ae1df0",
  "target": "009e0634",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ae1df4`](#insn-00ae1df4)

~~~json
{
  "source": "00ae1df4",
  "target": "00ae1e00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae1dfc`](#insn-00ae1dfc)

~~~json
{
  "source": "00ae1dfc",
  "target": "00ae1e04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae1e08`](#insn-00ae1e08)

~~~json
{
  "source": "00ae1e08",
  "target": "00ae1d58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae1e10`](#insn-00ae1e10)

~~~json
{
  "source": "00ae1e10",
  "target": "00ca5a38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5a38",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ae1e14`](#insn-00ae1e14)

~~~json
{
  "source": "00ae1e14",
  "target": "00ae1e38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae1e1c`](#insn-00ae1e1c)

~~~json
{
  "source": "00ae1e1c",
  "target": "00c66ef8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c66ef8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00ae1e24`](#insn-00ae1e24)

~~~json
{
  "source": "00ae1e24",
  "target": "00c8e9f0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8e9f0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00ae1e2c`](#insn-00ae1e2c)

~~~json
{
  "source": "00ae1e2c",
  "target": "00c596b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ae1e34`](#insn-00ae1e34)

~~~json
{
  "source": "00ae1e34",
  "target": "00ae1e3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae1e60`](#insn-00ae1e60)

~~~json
{
  "source": "00ae1e60",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae1e64`](#insn-00ae1e64)

~~~json
{
  "source": "00ae1e64",
  "target": "00ae1e7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae1e78`](#insn-00ae1e78)

~~~json
{
  "source": "00ae1e78",
  "target": "00ae2130",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae1e7c`](#insn-00ae1e7c)

~~~json
{
  "source": "00ae1e7c",
  "target": "0039b97c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0039b978",
  "offset": 4,
  "size": 8,
  "datatype": "qword",
  "bytes": "1c00000000000000",
  "capture_start": "0039b978",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ae1ed4`](#insn-00ae1ed4)

~~~json
{
  "source": "00ae1ed4",
  "target": "00ae1f48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae1ed8`](#insn-00ae1ed8)

~~~json
{
  "source": "00ae1ed8",
  "target": "003339b8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003339b8",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "60b66a00a0770900",
  "capture_start": "003339b8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ae1ee8`](#insn-00ae1ee8)

~~~json
{
  "source": "00ae1ee8",
  "target": "00666154",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ae1eec`](#insn-00ae1eec)

~~~json
{
  "source": "00ae1eec",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae1ef0`](#insn-00ae1ef0)

~~~json
{
  "source": "00ae1ef0",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae1f00`](#insn-00ae1f00)

~~~json
{
  "source": "00ae1f00",
  "target": "00ae1f14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae1f0c`](#insn-00ae1f0c)

~~~json
{
  "source": "00ae1f0c",
  "target": "00c54d90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ae1f10`](#insn-00ae1f10)

~~~json
{
  "source": "00ae1f10",
  "target": "00ae2034",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae1f14`](#insn-00ae1f14)

~~~json
{
  "source": "00ae1f14",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae1f18`](#insn-00ae1f18)

~~~json
{
  "source": "00ae1f18",
  "target": "00ae1e68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae1f24`](#insn-00ae1f24)

~~~json
{
  "source": "00ae1f24",
  "target": "00c54d90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ae1f28`](#insn-00ae1f28)

~~~json
{
  "source": "00ae1f28",
  "target": "00ae1e68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae1f40`](#insn-00ae1f40)

~~~json
{
  "source": "00ae1f40",
  "target": "00c58f20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ae1f44`](#insn-00ae1f44)

~~~json
{
  "source": "00ae1f44",
  "target": "00ae1e68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae1f50`](#insn-00ae1f50)

~~~json
{
  "source": "00ae1f50",
  "target": "00ca5ff8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5ff8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ae1f54`](#insn-00ae1f54)

~~~json
{
  "source": "00ae1f54",
  "target": "00ae20d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae1f60`](#insn-00ae1f60)

~~~json
{
  "source": "00ae1f60",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae1f64`](#insn-00ae1f64)

~~~json
{
  "source": "00ae1f64",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae1f68`](#insn-00ae1f68)

~~~json
{
  "source": "00ae1f68",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae1f88`](#insn-00ae1f88)

~~~json
{
  "source": "00ae1f88",
  "target": "0048d1b4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ae1f94`](#insn-00ae1f94)

~~~json
{
  "source": "00ae1f94",
  "target": "Stack[-0xdd]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae1f98`](#insn-00ae1f98)

~~~json
{
  "source": "00ae1f98",
  "target": "Stack[-0xe8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae1fa4`](#insn-00ae1fa4)

~~~json
{
  "source": "00ae1fa4",
  "target": "002caba4",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002caba4",
  "offset": 0,
  "size": 11,
  "datatype": "string",
  "bytes": "756e692e696d6763757400",
  "capture_start": "002caba4",
  "capture_bytes": 11,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ae1fb8`](#insn-00ae1fb8)

~~~json
{
  "source": "00ae1fb8",
  "target": "0048d1b4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ae1fcc`](#insn-00ae1fcc)

~~~json
{
  "source": "00ae1fcc",
  "target": "00ca5fc0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5fc0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ae1fd4`](#insn-00ae1fd4)

~~~json
{
  "source": "00ae1fd4",
  "target": "0047e96c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ae1fd8`](#insn-00ae1fd8)

~~~json
{
  "source": "00ae1fd8",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae1fdc`](#insn-00ae1fdc)

~~~json
{
  "source": "00ae1fdc",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae1fec`](#insn-00ae1fec)

~~~json
{
  "source": "00ae1fec",
  "target": "00ae2000",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae1ff8`](#insn-00ae1ff8)

~~~json
{
  "source": "00ae1ff8",
  "target": "00c54d90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ae1ffc`](#insn-00ae1ffc)

~~~json
{
  "source": "00ae1ffc",
  "target": "00ae2058",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae2000`](#insn-00ae2000)

~~~json
{
  "source": "00ae2000",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae2004`](#insn-00ae2004)

~~~json
{
  "source": "00ae2004",
  "target": "00ae2078",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae2010`](#insn-00ae2010)

~~~json
{
  "source": "00ae2010",
  "target": "00c54d90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ae2014`](#insn-00ae2014)

~~~json
{
  "source": "00ae2014",
  "target": "00ae2078",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae202c`](#insn-00ae202c)

~~~json
{
  "source": "00ae202c",
  "target": "00c58f20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ae2030`](#insn-00ae2030)

~~~json
{
  "source": "00ae2030",
  "target": "00ae2078",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae2048`](#insn-00ae2048)

~~~json
{
  "source": "00ae2048",
  "target": "00c58f20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ae204c`](#insn-00ae204c)

~~~json
{
  "source": "00ae204c",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae2050`](#insn-00ae2050)

~~~json
{
  "source": "00ae2050",
  "target": "00ae1f1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae2054`](#insn-00ae2054)

~~~json
{
  "source": "00ae2054",
  "target": "00ae1e68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae206c`](#insn-00ae206c)

~~~json
{
  "source": "00ae206c",
  "target": "00c58f20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ae2070`](#insn-00ae2070)

~~~json
{
  "source": "00ae2070",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae2074`](#insn-00ae2074)

~~~json
{
  "source": "00ae2074",
  "target": "00ae2008",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae2078`](#insn-00ae2078)

~~~json
{
  "source": "00ae2078",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae207c`](#insn-00ae207c)

~~~json
{
  "source": "00ae207c",
  "target": "00ae209c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae2080`](#insn-00ae2080)

~~~json
{
  "source": "00ae2080",
  "target": "Stack[-0xe8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae2084`](#insn-00ae2084)

~~~json
{
  "source": "00ae2084",
  "target": "00ae20ac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae2088`](#insn-00ae2088)

~~~json
{
  "source": "00ae2088",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae208c`](#insn-00ae208c)

~~~json
{
  "source": "00ae208c",
  "target": "00ae20bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae2090`](#insn-00ae2090)

~~~json
{
  "source": "00ae2090",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae2094`](#insn-00ae2094)

~~~json
{
  "source": "00ae2094",
  "target": "00ae1e68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae2098`](#insn-00ae2098)

~~~json
{
  "source": "00ae2098",
  "target": "00ae20cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae209c`](#insn-00ae209c)

~~~json
{
  "source": "00ae209c",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae20a0`](#insn-00ae20a0)

~~~json
{
  "source": "00ae20a0",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ae20a4`](#insn-00ae20a4)

~~~json
{
  "source": "00ae20a4",
  "target": "Stack[-0xe8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae20a8`](#insn-00ae20a8)

~~~json
{
  "source": "00ae20a8",
  "target": "00ae2088",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae20ac`](#insn-00ae20ac)

~~~json
{
  "source": "00ae20ac",
  "target": "Stack[-0xd8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae20b0`](#insn-00ae20b0)

~~~json
{
  "source": "00ae20b0",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ae20b4`](#insn-00ae20b4)

~~~json
{
  "source": "00ae20b4",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae20b8`](#insn-00ae20b8)

~~~json
{
  "source": "00ae20b8",
  "target": "00ae2090",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae20bc`](#insn-00ae20bc)

~~~json
{
  "source": "00ae20bc",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae20c0`](#insn-00ae20c0)

~~~json
{
  "source": "00ae20c0",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ae20c4`](#insn-00ae20c4)

~~~json
{
  "source": "00ae20c4",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae20c8`](#insn-00ae20c8)

~~~json
{
  "source": "00ae20c8",
  "target": "00ae1e68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae20cc`](#insn-00ae20cc)

~~~json
{
  "source": "00ae20cc",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae20d0`](#insn-00ae20d0)

~~~json
{
  "source": "00ae20d0",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ae20d4`](#insn-00ae20d4)

~~~json
{
  "source": "00ae20d4",
  "target": "00ae1e68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae20dc`](#insn-00ae20dc)

~~~json
{
  "source": "00ae20dc",
  "target": "00ca5ff8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5ff8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ae20e0`](#insn-00ae20e0)

~~~json
{
  "source": "00ae20e0",
  "target": "00c58ef0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ae20e4`](#insn-00ae20e4)

~~~json
{
  "source": "00ae20e4",
  "target": "00ae1f58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae20ec`](#insn-00ae20ec)

~~~json
{
  "source": "00ae20ec",
  "target": "00ca5fc0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5fc0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ae20f4`](#insn-00ae20f4)

~~~json
{
  "source": "00ae20f4",
  "target": "0047f114",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ae2100`](#insn-00ae2100)

~~~json
{
  "source": "00ae2100",
  "target": "00c64030",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c64030",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00ae2104`](#insn-00ae2104)

~~~json
{
  "source": "00ae2104",
  "target": "00ca5fc8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5fc8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ae2108`](#insn-00ae2108)

~~~json
{
  "source": "00ae2108",
  "target": "00ca5fc0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5fc0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ae2108`](#insn-00ae2108)

~~~json
{
  "source": "00ae2108",
  "target": "00ca5fc8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5fc8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ae2110`](#insn-00ae2110)

~~~json
{
  "source": "00ae2110",
  "target": "00ca5fe8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5fe8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ae2110`](#insn-00ae2110)

~~~json
{
  "source": "00ae2110",
  "target": "00ca5ff0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5ff0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ae2114`](#insn-00ae2114)

~~~json
{
  "source": "00ae2114",
  "target": "00ca5fe0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5fe0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ae2118`](#insn-00ae2118)

~~~json
{
  "source": "00ae2118",
  "target": "00ca5fd0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5fd0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ae2118`](#insn-00ae2118)

~~~json
{
  "source": "00ae2118",
  "target": "00ca5fd8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5fd8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ae2118`](#insn-00ae2118)

~~~json
{
  "source": "00ae2118",
  "target": "00ca5fe0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5fe0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ae211c`](#insn-00ae211c)

~~~json
{
  "source": "00ae211c",
  "target": "00c58ed0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ae2124`](#insn-00ae2124)

~~~json
{
  "source": "00ae2124",
  "target": "00ca5ff8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5ff8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ae2128`](#insn-00ae2128)

~~~json
{
  "source": "00ae2128",
  "target": "00c58f10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ae212c`](#insn-00ae212c)

~~~json
{
  "source": "00ae212c",
  "target": "00ae1f58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae2134`](#insn-00ae2134)

~~~json
{
  "source": "00ae2134",
  "target": "00ad085c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ae213c`](#insn-00ae213c)

~~~json
{
  "source": "00ae213c",
  "target": "00ad0558",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ae214c`](#insn-00ae214c)

~~~json
{
  "source": "00ae214c",
  "target": "008b89cc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ae2158`](#insn-00ae2158)

~~~json
{
  "source": "00ae2158",
  "target": "00ad7aec",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ae2168`](#insn-00ae2168)

~~~json
{
  "source": "00ae2168",
  "target": "008b7f44",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ae216c`](#insn-00ae216c)

~~~json
{
  "source": "00ae216c",
  "target": "Stack[-0xf8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae2174`](#insn-00ae2174)

~~~json
{
  "source": "00ae2174",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae217c`](#insn-00ae217c)

~~~json
{
  "source": "00ae217c",
  "target": "00ae223c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae2180`](#insn-00ae2180)

~~~json
{
  "source": "00ae2180",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae2184`](#insn-00ae2184)

~~~json
{
  "source": "00ae2184",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae2188`](#insn-00ae2188)

~~~json
{
  "source": "00ae2188",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae218c`](#insn-00ae218c)

~~~json
{
  "source": "00ae218c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae2190`](#insn-00ae2190)

~~~json
{
  "source": "00ae2190",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae2194`](#insn-00ae2194)

~~~json
{
  "source": "00ae2194",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae223c`](#insn-00ae223c)

~~~json
{
  "source": "00ae223c",
  "target": "00c58f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
