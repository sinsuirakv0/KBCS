# 00aefce0

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00a908b4`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a90/00a908b4.md) · 移動量 `+0x5f42c`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0053.md#compare-8917db606e5885f16c0bc829c4878e06)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00af0108`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af0/00af0108.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0065.md#compare-c29b43462d5526d757d3f865a3f4b810)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aefce0",
  "name": "FUN_00aefce0",
  "size": 896,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d3e6009581566d5c777b1da5e6e40c3ee288b143852f21bbb396110866fb4361",
  "source_text_sha256": "d3e6009581566d5c777b1da5e6e40c3ee288b143852f21bbb396110866fb4361",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aefce0",
        "00af005b"
      ],
      [
        "00af0168",
        "00af016b"
      ]
    ],
    "bytes_sha256": "21a08105ce61051e54eefbee4201e5f1229dad93dd85733cc8dc337e7fd23f6f",
    "instruction_count": 224,
    "instruction_bytes": 896,
    "body_bytes": 896,
    "indirect": 2,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0047acb4](../0047a/0047acb4.md)
- [0047cd94](../0047c/0047cd94.md)
- [0048ce14](../0048c/0048ce14.md)
- [005bc78c](../005bc/005bc78c.md)
- [007441c8](../00744/007441c8.md)
- [008514b8](../00851/008514b8.md)
- [008b6f0c](../008b6/008b6f0c.md)
- [008b9814](../008b9/008b9814.md)
- [008bac84](../008ba/008bac84.md)
- [008bb0a8](../008bb/008bb0a8.md)
- [00ad688c](../00ad6/00ad688c.md)
- [00aeb76c](../00aeb/00aeb76c.md)
- [00af01cc](../00af0/00af01cc.md)
- [00af01d0](../00af0/00af01d0.md)
- [00af0290](../00af0/00af0290.md)
- [00af0294](../00af0/00af0294.md)
- [00c57ab0](../00c57/00c57ab0.md)
- [00c57ae0](../00c57/00c57ae0.md)
- [00c57d90](../00c57/00c57d90.md)

## 関連文字列（未確認候補）

~~~text
"slot_autoset_confirm"
"slot_autoset_error_1"
"slot_autoset_error_2"
"slot_autoset_error_3"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 5863 bytes

~~~c

void FUN_00aefce0(long param_1,undefined8 *param_2,int *param_3)

{
  ulong uVar1;
  byte *pbVar2;
  char *pcVar3;
  char *pcVar4;
  long lVar5;
  uint uVar6;
  int iVar7;
  undefined8 uVar8;
  ulong uVar9;
  long lVar10;
  long lVar11;
  undefined ***pppuVar12;
  undefined4 uVar13;
  long lVar14;
  undefined8 uVar15;
  bool bVar16;
  long lVar17;
  byte local_d0;
  char local_cf [8];
  undefined7 uStack_c7;
  char cStack_c0;
  undefined4 uStack_bf;
  undefined1 uStack_bb;
  undefined2 uStack_ba;
  ushort local_b8 [8];
  void *local_a8;
  undefined **local_a0;
  long lStack_98;
  undefined ***local_80;
  long local_68;
  
  lVar5 = tpidr_el0;
  local_68 = *(long *)(lVar5 + 0x28);
  iVar7 = *param_3;
  uVar15 = *param_2;
  if (iVar7 == 4) {
    lVar14 = *(long *)(param_1 + 8);
    uVar9 = FUN_008b6f0c(uVar15);
    if ((uVar9 & 1) == 0) {
      iVar7 = FUN_00ad688c(lVar14);
      local_b8[0] = 0;
      pcVar3 = "slot_autoset_error_3";
      if (iVar7 != 1) {
        pcVar3 = "slot_autoset_error_2";
      }
      pcVar4 = "slot_autoset_error_1";
      if (iVar7 != 0) {
        pcVar4 = pcVar3;
      }
      _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKc(local_b8,pcVar4)
      ;
      FUN_0048ce14(&local_d0,local_b8);
      local_a0 = &PTR_FUN_00c8df68;
      local_80 = &local_a0;
      FUN_008bac84(lVar14 + 0x2f08,&local_d0,0,0,4,&local_a0);
      if (local_80 == &local_a0) {
        lVar14 = 0x20;
        pppuVar12 = &local_a0;
LAB_00aeff40:
        (**(code **)((long)*pppuVar12 + lVar14))();
      }
      else {
                    /* try { // try from 00aeff2c to 00beff2f has its CatchHandler @ 00af0330 */
        if (local_80 != (undefined ***)0x0) {
                    /* try { // try from 00aeff30 to 00beff9f has its CatchHandler @ 00aefc4c */
          lVar14 = 0x28;
          pppuVar12 = local_80;
          goto LAB_00aeff40;
        }
      }
      if ((local_d0 & 1) != 0) {
        _ZdlPv((void *)CONCAT26(uStack_ba,CONCAT15(uStack_bb,CONCAT41(uStack_bf,cStack_c0))));
      }
      if ((local_b8[0] & 1) == 0) goto LAB_00af002c;
    }
    else {
      bVar16 = false;
      lVar17 = 0xc5b9;
      uVar9 = 0;
      do {
        lVar10 = FUN_008514b8();
        lVar11 = FUN_008514b8();
        lVar10 = lVar10 + (long)*(int *)((long)&DWORD_0039b97c + lVar11) * 0x2c;
        pbVar2 = (byte *)(lVar10 + lVar17);
                    /* try { // try from 00aefdfc to 00befdff has its CatchHandler @ 00af0334 */
                    /* try { // try from 00aefe00 to 00beff2b has its CatchHandler @ 00aefc4c */
        if (1 < (int)((uint)(*(byte *)(lVar10 + 0xc5e2) ^ pbVar2[1]) << 0x10 |
                      (uint)(*(byte *)(lVar10 + 0xc5e3) ^ pbVar2[2]) << 0x18 |
                      (uint)(*(byte *)(lVar10 + 0xc5e1) ^ *pbVar2) << 8 |
                     (uint)(*(byte *)(lVar10 + 0xc5e0) ^ pbVar2[-1]))) break;
        uVar1 = uVar9 + 1;
        lVar17 = lVar17 + 4;
        bVar16 = 8 < uVar9;
        uVar9 = uVar1;
      } while (uVar1 != 10);
      if ((*(char *)(lVar14 + 0x11a4) == '\0') ||
         (uVar6 = FUN_007441c8(lVar14 + 0xbe0), bVar16 || (uVar6 & 1) != 0)) {
        FUN_005bc78c(lVar14 + 0x428,0);
        if (*(long *)(lVar5 + 0x28) == local_68) {
          FUN_00aeb76c(lVar14);
          return;
        }
        goto LAB_00af0168;
      }
      local_d0 = 0x28;
      uStack_bf = 0x6d726966;
      uStack_c7 = (undefined7)s_slot_autoset_confirm_002a8213._8_8_;
      cStack_c0 = SUB81(s_slot_autoset_confirm_002a8213._8_8_,7);
      local_cf[0] = s_slot_autoset_confirm_002a8213[0];
      local_cf[1] = s_slot_autoset_confirm_002a8213[1];
      local_cf[2] = s_slot_autoset_confirm_002a8213[2];
      local_cf[3] = s_slot_autoset_confirm_002a8213[3];
      local_cf[4] = s_slot_autoset_confirm_002a8213[4];
      local_cf[5] = s_slot_autoset_confirm_002a8213[5];
      local_cf[6] = s_slot_autoset_confirm_002a8213[6];
      local_cf[7] = s_slot_autoset_confirm_002a8213[7];
      uStack_bb = 0;
      FUN_0048ce14(local_b8,&local_d0);
                    /* try { // try from 00aeffa0 to 00beffab has its CatchHandler @ 00af02f0 */
      local_80 = &local_a0;
      local_a0 = &PTR_FUN_00c8dfe8;
      lStack_98 = lVar14;
      uVar15 = FUN_008bb0a8(lVar14 + 0x2f08,local_b8,0,0,4,&local_a0);
                    /* try { // try from 00aeffd8 to 00beffe3 has its CatchHandler @ 00af02f4 */
      FUN_008b9814(uVar15,1);
      if (local_80 == &local_a0) {
        lVar14 = 0x20;
        pppuVar12 = &local_a0;
LAB_00af0000:
        (**(code **)((long)*pppuVar12 + lVar14))();
      }
      else if (local_80 != (undefined ***)0x0) {
        lVar14 = 0x28;
        pppuVar12 = local_80;
        goto LAB_00af0000;
      }
                    /* try { // try from 00af0010 to 00bf0017 has its CatchHandler @ 00af02ec */
      if ((local_b8[0] & 1) != 0) {
        _ZdlPv(local_a8);
      }
      if ((local_d0 & 1) == 0) goto LAB_00af002c;
      local_a8 = (void *)CONCAT26(uStack_ba,CONCAT15(uStack_bb,CONCAT41(uStack_bf,cStack_c0)));
    }
    _ZdlPv(local_a8);
  }
  else {
    if (iVar7 == 3) {
      uVar8 = FUN_0047acb4();
      uVar9 = FUN_008b6f0c(uVar15);
      uVar13 = 0xb;
      if ((uVar9 & 1) == 0) {
        uVar13 = 0xf;
      }
      if (*(long *)(lVar5 + 0x28) == local_68) {
LAB_00aefd78:
        FUN_0047cd94(uVar8,uVar13,0);
        return;
      }
      goto LAB_00af0168;
    }
    if (iVar7 == 0) {
      uVar8 = FUN_0047acb4();
      if (*(long *)(lVar5 + 0x28) == local_68) {
        uVar13 = 10;
        goto LAB_00aefd78;
      }
      goto LAB_00af0168;
    }
  }
LAB_00af002c:
  if (*(long *)(lVar5 + 0x28) == local_68) {
                    /* try { // try from 00af0044 to 00bf005b has its CatchHandler @ 00af02cc */
    return;
  }
LAB_00af0168:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aefce0"></a> `00aefce0` | `ff 43 03 d1` | sub sp,sp,#0xd0 | `FALL_THROUGH`
<a id="insn-00aefce4"></a> `00aefce4` | `fd 7b 07 a9` | stp x29,x30,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00aefce8"></a> `00aefce8` | `fb 43 00 f9` | str x27,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00aefcec"></a> `00aefcec` | `fa 67 09 a9` | stp x26,x25,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00aefcf0"></a> `00aefcf0` | `f8 5f 0a a9` | stp x24,x23,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00aefcf4"></a> `00aefcf4` | `f6 57 0b a9` | stp x22,x21,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00aefcf8"></a> `00aefcf8` | `f4 4f 0c a9` | stp x20,x19,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00aefcfc"></a> `00aefcfc` | `fd c3 01 91` | add x29,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00aefd00"></a> `00aefd00` | `55 d0 3b d5` | mrs x21,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00aefd04"></a> `00aefd04` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00aefd08"></a> `00aefd08` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aefd0c"></a> `00aefd0c` | `48 00 40 b9` | ldr w8,[x2] | `FALL_THROUGH`
<a id="insn-00aefd10"></a> `00aefd10` | `34 00 40 f9` | ldr x20,[x1] | `FALL_THROUGH`
<a id="insn-00aefd14"></a> `00aefd14` | `1f 11 00 71` | cmp w8,#0x4 | `FALL_THROUGH`
<a id="insn-00aefd18"></a> `00aefd18` | `20 04 00 54` | b.eq 0x00aefd9c | `CONDITIONAL_JUMP`
<a id="insn-00aefd1c"></a> `00aefd1c` | `1f 0d 00 71` | cmp w8,#0x3 | `FALL_THROUGH`
<a id="insn-00aefd20"></a> `00aefd20` | `20 01 00 54` | b.eq 0x00aefd44 | `CONDITIONAL_JUMP`
<a id="insn-00aefd24"></a> `00aefd24` | `48 18 00 35` | cbnz w8,0x00af002c | `CONDITIONAL_JUMP`
<a id="insn-00aefd28"></a> `00aefd28` | `e3 2b e6 97` | bl 0x0047acb4 | `UNCONDITIONAL_CALL`
<a id="insn-00aefd2c"></a> `00aefd2c` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00aefd30"></a> `00aefd30` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aefd34"></a> `00aefd34` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00aefd38"></a> `00aefd38` | `81 21 00 54` | b.ne 0x00af0168 | `CONDITIONAL_JUMP`
<a id="insn-00aefd3c"></a> `00aefd3c` | `41 01 80 52` | mov w1,#0xa | `FALL_THROUGH`
<a id="insn-00aefd40"></a> `00aefd40` | `0e 00 00 14` | b 0x00aefd78 | `UNCONDITIONAL_JUMP`
<a id="insn-00aefd44"></a> `00aefd44` | `dc 2b e6 97` | bl 0x0047acb4 | `UNCONDITIONAL_CALL`
<a id="insn-00aefd48"></a> `00aefd48` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aefd4c"></a> `00aefd4c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aefd50"></a> `00aefd50` | `6f 1c f7 97` | bl 0x008b6f0c | `UNCONDITIONAL_CALL`
<a id="insn-00aefd54"></a> `00aefd54` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00aefd58"></a> `00aefd58` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aefd5c"></a> `00aefd5c` | `1f 00 00 72` | tst w0,#0x1 | `FALL_THROUGH`
<a id="insn-00aefd60"></a> `00aefd60` | `ea 01 80 52` | mov w10,#0xf | `FALL_THROUGH`
<a id="insn-00aefd64"></a> `00aefd64` | `6b 01 80 52` | mov w11,#0xb | `FALL_THROUGH`
<a id="insn-00aefd68"></a> `00aefd68` | `61 11 8a 1a` | csel w1,w11,w10,ne | `FALL_THROUGH`
<a id="insn-00aefd6c"></a> `00aefd6c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00aefd70"></a> `00aefd70` | `c1 1f 00 54` | b.ne 0x00af0168 | `CONDITIONAL_JUMP`
<a id="insn-00aefd74"></a> `00aefd74` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aefd78"></a> `00aefd78` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00aefd7c"></a> `00aefd7c` | `f4 4f 4c a9` | ldp x20,x19,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00aefd80"></a> `00aefd80` | `fb 43 40 f9` | ldr x27,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00aefd84"></a> `00aefd84` | `f6 57 4b a9` | ldp x22,x21,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00aefd88"></a> `00aefd88` | `f8 5f 4a a9` | ldp x24,x23,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00aefd8c"></a> `00aefd8c` | `fa 67 49 a9` | ldp x26,x25,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00aefd90"></a> `00aefd90` | `fd 7b 47 a9` | ldp x29,x30,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00aefd94"></a> `00aefd94` | `ff 43 03 91` | add sp,sp,#0xd0 | `FALL_THROUGH`
<a id="insn-00aefd98"></a> `00aefd98` | `ff 33 e6 17` | b 0x0047cd94 | `CALL_TERMINATOR`
<a id="insn-00aefd9c"></a> `00aefd9c` | `13 04 40 f9` | ldr x19,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00aefda0"></a> `00aefda0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aefda4"></a> `00aefda4` | `5a 1c f7 97` | bl 0x008b6f0c | `UNCONDITIONAL_CALL`
<a id="insn-00aefda8"></a> `00aefda8` | `e0 07 00 36` | tbz w0,#0x0,0x00aefea4 | `CONDITIONAL_JUMP`
<a id="insn-00aefdac"></a> `00aefdac` | `98 2f 97 52` | mov w24,#0xb97c | `FALL_THROUGH`
<a id="insn-00aefdb0"></a> `00aefdb0` | `f9 03 1f aa` | mov x25,xzr | `FALL_THROUGH`
<a id="insn-00aefdb4"></a> `00aefdb4` | `f6 03 1f 2a` | mov w22,wzr | `FALL_THROUGH`
<a id="insn-00aefdb8"></a> `00aefdb8` | `37 b7 98 52` | mov w23,#0xc5b9 | `FALL_THROUGH`
<a id="insn-00aefdbc"></a> `00aefdbc` | `38 07 a0 72` | movk w24,#0x39, LSL #16 | `FALL_THROUGH`
<a id="insn-00aefdc0"></a> `00aefdc0` | `9a 05 80 52` | mov w26,#0x2c | `FALL_THROUGH`
<a id="insn-00aefdc4"></a> `00aefdc4` | `1b b7 98 52` | mov w27,#0xc5b8 | `FALL_THROUGH`
<a id="insn-00aefdc8"></a> `00aefdc8` | `bc 85 f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00aefdcc"></a> `00aefdcc` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00aefdd0"></a> `00aefdd0` | `ba 85 f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00aefdd4"></a> `00aefdd4` | `08 68 b8 b8` | ldrsw x8,[x0, x24, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00aefdd8"></a> `00aefdd8` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00aefddc"></a> `00aefddc` | `08 51 3a 9b` | smaddl x8,w8,w26,x20 | `FALL_THROUGH`
<a id="insn-00aefde0"></a> `00aefde0` | `09 01 1b 8b` | add x9,x8,x27 | `FALL_THROUGH`
<a id="insn-00aefde4"></a> `00aefde4` | `08 01 17 8b` | add x8,x8,x23 | `FALL_THROUGH`
<a id="insn-00aefde8"></a> `00aefde8` | `0a 05 40 39` | ldrb w10,[x8, #0x1] | `FALL_THROUGH`
<a id="insn-00aefdec"></a> `00aefdec` | `2b a9 40 39` | ldrb w11,[x9, #0x2a] | `FALL_THROUGH`
<a id="insn-00aefdf0"></a> `00aefdf0` | `2c ad 40 39` | ldrb w12,[x9, #0x2b] | `FALL_THROUGH`
<a id="insn-00aefdf4"></a> `00aefdf4` | `0d 01 40 39` | ldrb w13,[x8] | `FALL_THROUGH`
<a id="insn-00aefdf8"></a> `00aefdf8` | `6a 01 0a 4a` | eor w10,w11,w10 | `FALL_THROUGH`
<a id="insn-00aefdfc"></a> `00aefdfc` | `0b 09 40 39` | ldrb w11,[x8, #0x2] | `FALL_THROUGH`
<a id="insn-00aefe00"></a> `00aefe00` | `08 f1 5f 38` | ldurb w8,[x8, #-0x1] | `FALL_THROUGH`
<a id="insn-00aefe04"></a> `00aefe04` | `4a 3d 10 53` | lsl w10,w10,#0x10 | `FALL_THROUGH`
<a id="insn-00aefe08"></a> `00aefe08` | `8b 01 0b 4a` | eor w11,w12,w11 | `FALL_THROUGH`
<a id="insn-00aefe0c"></a> `00aefe0c` | `2c a5 40 39` | ldrb w12,[x9, #0x29] | `FALL_THROUGH`
<a id="insn-00aefe10"></a> `00aefe10` | `29 a1 40 39` | ldrb w9,[x9, #0x28] | `FALL_THROUGH`
<a id="insn-00aefe14"></a> `00aefe14` | `4a 61 0b 2a` | orr w10,w10,w11, LSL #0x18 | `FALL_THROUGH`
<a id="insn-00aefe18"></a> `00aefe18` | `8b 01 0d 4a` | eor w11,w12,w13 | `FALL_THROUGH`
<a id="insn-00aefe1c"></a> `00aefe1c` | `28 01 08 4a` | eor w8,w9,w8 | `FALL_THROUGH`
<a id="insn-00aefe20"></a> `00aefe20` | `4a 21 0b 2a` | orr w10,w10,w11, LSL #0x8 | `FALL_THROUGH`
<a id="insn-00aefe24"></a> `00aefe24` | `48 01 08 2a` | orr w8,w10,w8 | `FALL_THROUGH`
<a id="insn-00aefe28"></a> `00aefe28` | `1f 09 00 71` | cmp w8,#0x2 | `FALL_THROUGH`
<a id="insn-00aefe2c"></a> `00aefe2c` | `ea 00 00 54` | b.ge 0x00aefe48 | `CONDITIONAL_JUMP`
<a id="insn-00aefe30"></a> `00aefe30` | `3f 23 00 f1` | cmp x25,#0x8 | `FALL_THROUGH`
<a id="insn-00aefe34"></a> `00aefe34` | `39 07 00 91` | add x25,x25,#0x1 | `FALL_THROUGH`
<a id="insn-00aefe38"></a> `00aefe38` | `f7 12 00 91` | add x23,x23,#0x4 | `FALL_THROUGH`
<a id="insn-00aefe3c"></a> `00aefe3c` | `f6 97 9f 1a` | cset w22,hi | `FALL_THROUGH`
<a id="insn-00aefe40"></a> `00aefe40` | `3f 2b 00 f1` | cmp x25,#0xa | `FALL_THROUGH`
<a id="insn-00aefe44"></a> `00aefe44` | `21 fc ff 54` | b.ne 0x00aefdc8 | `CONDITIONAL_JUMP`
<a id="insn-00aefe48"></a> `00aefe48` | `88 34 82 52` | mov w8,#0x11a4 | `FALL_THROUGH`
<a id="insn-00aefe4c"></a> `00aefe4c` | `68 6a 68 38` | ldrb w8,[x19, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00aefe50"></a> `00aefe50` | `a8 00 00 34` | cbz w8,0x00aefe64 | `CONDITIONAL_JUMP`
<a id="insn-00aefe54"></a> `00aefe54` | `60 82 2f 91` | add x0,x19,#0xbe0 | `FALL_THROUGH`
<a id="insn-00aefe58"></a> `00aefe58` | `dc 50 f1 97` | bl 0x007441c8 | `UNCONDITIONAL_CALL`
<a id="insn-00aefe5c"></a> `00aefe5c` | `c8 02 00 2a` | orr w8,w22,w0 | `FALL_THROUGH`
<a id="insn-00aefe60"></a> `00aefe60` | `68 08 00 36` | tbz w8,#0x0,0x00aeff6c | `CONDITIONAL_JUMP`
<a id="insn-00aefe64"></a> `00aefe64` | `60 a2 10 91` | add x0,x19,#0x428 | `FALL_THROUGH`
<a id="insn-00aefe68"></a> `00aefe68` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aefe6c"></a> `00aefe6c` | `48 32 eb 97` | bl 0x005bc78c | `UNCONDITIONAL_CALL`
<a id="insn-00aefe70"></a> `00aefe70` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00aefe74"></a> `00aefe74` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aefe78"></a> `00aefe78` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00aefe7c"></a> `00aefe7c` | `61 17 00 54` | b.ne 0x00af0168 | `CONDITIONAL_JUMP`
<a id="insn-00aefe80"></a> `00aefe80` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aefe84"></a> `00aefe84` | `f4 4f 4c a9` | ldp x20,x19,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00aefe88"></a> `00aefe88` | `fb 43 40 f9` | ldr x27,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00aefe8c"></a> `00aefe8c` | `f6 57 4b a9` | ldp x22,x21,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00aefe90"></a> `00aefe90` | `f8 5f 4a a9` | ldp x24,x23,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00aefe94"></a> `00aefe94` | `fa 67 49 a9` | ldp x26,x25,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00aefe98"></a> `00aefe98` | `fd 7b 47 a9` | ldp x29,x30,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00aefe9c"></a> `00aefe9c` | `ff 43 03 91` | add sp,sp,#0xd0 | `FALL_THROUGH`
<a id="insn-00aefea0"></a> `00aefea0` | `33 ee ff 17` | b 0x00aeb76c | `CALL_TERMINATOR`
<a id="insn-00aefea4"></a> `00aefea4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aefea8"></a> `00aefea8` | `79 9a ff 97` | bl 0x00ad688c | `UNCONDITIONAL_CALL`
<a id="insn-00aefeac"></a> `00aefeac` | `08 be ff 90` | adrp x8,0x2af000 | `FALL_THROUGH`
<a id="insn-00aefeb0"></a> `00aefeb0` | `08 f9 07 91` | add x8,x8,#0x1fe | `FALL_THROUGH`
<a id="insn-00aefeb4"></a> `00aefeb4` | `a9 bd ff 90` | adrp x9,0x2a3000 | `FALL_THROUGH`
<a id="insn-00aefeb8"></a> `00aefeb8` | `29 19 22 91` | add x9,x9,#0x886 | `FALL_THROUGH`
<a id="insn-00aefebc"></a> `00aefebc` | `1f 04 00 71` | cmp w0,#0x1 | `FALL_THROUGH`
<a id="insn-00aefec0"></a> `00aefec0` | `ff 33 00 79` | strh wzr,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00aefec4"></a> `00aefec4` | `28 01 88 9a` | csel x8,x9,x8,eq | `FALL_THROUGH`
<a id="insn-00aefec8"></a> `00aefec8` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00aefecc"></a> `00aefecc` | `29 be ff d0` | adrp x9,0x2b5000 | `FALL_THROUGH`
<a id="insn-00aefed0"></a> `00aefed0` | `29 75 1d 91` | add x9,x9,#0x75d | `FALL_THROUGH`
<a id="insn-00aefed4"></a> `00aefed4` | `21 01 88 9a` | csel x1,x9,x8,eq | `FALL_THROUGH`
<a id="insn-00aefed8"></a> `00aefed8` | `e0 63 00 91` | add x0,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00aefedc"></a> `00aefedc` | `ad 9f 05 94` | bl 0x00c57d90 | `UNCONDITIONAL_CALL`
<a id="insn-00aefee0"></a> `00aefee0` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00aefee4"></a> `00aefee4` | `e0 63 00 91` | add x0,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00aefee8"></a> `00aefee8` | `cb 73 e6 97` | bl 0x0048ce14 | `UNCONDITIONAL_CALL`
<a id="insn-00aefeec"></a> `00aefeec` | `e8 0c 00 d0` | adrp x8,0xc8d000 | `FALL_THROUGH`
<a id="insn-00aefef0"></a> `00aefef0` | `08 a1 3d 91` | add x8,x8,#0xf68 | `FALL_THROUGH`
<a id="insn-00aefef4"></a> `00aefef4` | `f4 c3 00 91` | add x20,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00aefef8"></a> `00aefef8` | `e8 1b 00 f9` | str x8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aefefc"></a> `00aefefc` | `08 e1 85 52` | mov w8,#0x2f08 | `FALL_THROUGH`
<a id="insn-00aeff00"></a> `00aeff00` | `f4 2b 00 f9` | str x20,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00aeff04"></a> `00aeff04` | `60 02 08 8b` | add x0,x19,x8 | `FALL_THROUGH`
<a id="insn-00aeff08"></a> `00aeff08` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00aeff0c"></a> `00aeff0c` | `e5 c3 00 91` | add x5,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00aeff10"></a> `00aeff10` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-00aeff14"></a> `00aeff14` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-00aeff18"></a> `00aeff18` | `84 00 80 52` | mov w4,#0x4 | `FALL_THROUGH`
<a id="insn-00aeff1c"></a> `00aeff1c` | `5a 2b f7 97` | bl 0x008bac84 | `UNCONDITIONAL_CALL`
<a id="insn-00aeff20"></a> `00aeff20` | `e0 2b 40 f9` | ldr x0,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00aeff24"></a> `00aeff24` | `1f 00 14 eb` | cmp x0,x20 | `FALL_THROUGH`
<a id="insn-00aeff28"></a> `00aeff28` | `80 00 00 54` | b.eq 0x00aeff38 | `CONDITIONAL_JUMP`
<a id="insn-00aeff2c"></a> `00aeff2c` | `00 01 00 b4` | cbz x0,0x00aeff4c | `CONDITIONAL_JUMP`
<a id="insn-00aeff30"></a> `00aeff30` | `08 05 80 52` | mov w8,#0x28 | `FALL_THROUGH`
<a id="insn-00aeff34"></a> `00aeff34` | `03 00 00 14` | b 0x00aeff40 | `UNCONDITIONAL_JUMP`
<a id="insn-00aeff38"></a> `00aeff38` | `08 04 80 52` | mov w8,#0x20 | `FALL_THROUGH`
<a id="insn-00aeff3c"></a> `00aeff3c` | `e0 c3 00 91` | add x0,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00aeff40"></a> `00aeff40` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-00aeff44"></a> `00aeff44` | `28 69 68 f8` | ldr x8,[x9, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00aeff48"></a> `00aeff48` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aeff4c"></a> `00aeff4c` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-00aeff50"></a> `00aeff50` | `68 00 00 36` | tbz w8,#0x0,0x00aeff5c | `CONDITIONAL_JUMP`
<a id="insn-00aeff54"></a> `00aeff54` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aeff58"></a> `00aeff58` | `d6 9e 05 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00aeff5c"></a> `00aeff5c` | `e8 63 40 39` | ldrb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00aeff60"></a> `00aeff60` | `68 06 00 36` | tbz w8,#0x0,0x00af002c | `CONDITIONAL_JUMP`
<a id="insn-00aeff64"></a> `00aeff64` | `e0 17 40 f9` | ldr x0,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00aeff68"></a> `00aeff68` | `30 00 00 14` | b 0x00af0028 | `UNCONDITIONAL_JUMP`
<a id="insn-00aeff6c"></a> `00aeff6c` | `c9 bd ff b0` | adrp x9,0x2a8000 | `FALL_THROUGH`
<a id="insn-00aeff70"></a> `00aeff70` | `29 4d 08 91` | add x9,x9,#0x213 | `FALL_THROUGH`
<a id="insn-00aeff74"></a> `00aeff74` | `ca 2c 8d 52` | mov w10,#0x6966 | `FALL_THROUGH`
<a id="insn-00aeff78"></a> `00aeff78` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00aeff7c"></a> `00aeff7c` | `08 05 80 52` | mov w8,#0x28 | `FALL_THROUGH`
<a id="insn-00aeff80"></a> `00aeff80` | `4a ae ad 72` | movk w10,#0x6d72, LSL #16 | `FALL_THROUGH`
<a id="insn-00aeff84"></a> `00aeff84` | `e8 03 00 39` | strb w8,[sp] | `FALL_THROUGH`
<a id="insn-00aeff88"></a> `00aeff88` | `ea 13 01 b8` | stur w10,[sp, #0x11] | `FALL_THROUGH`
<a id="insn-00aeff8c"></a> `00aeff8c` | `e0 13 80 3c` | stur q0,[sp, #0x1] | `FALL_THROUGH`
<a id="insn-00aeff90"></a> `00aeff90` | `ff 57 00 39` | strb wzr,[sp, #0x15] | `FALL_THROUGH`
<a id="insn-00aeff94"></a> `00aeff94` | `e8 63 00 91` | add x8,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00aeff98"></a> `00aeff98` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00aeff9c"></a> `00aeff9c` | `9e 73 e6 97` | bl 0x0048ce14 | `UNCONDITIONAL_CALL`
<a id="insn-00aeffa0"></a> `00aeffa0` | `e8 0c 00 d0` | adrp x8,0xc8d000 | `FALL_THROUGH`
<a id="insn-00aeffa4"></a> `00aeffa4` | `08 a1 3f 91` | add x8,x8,#0xfe8 | `FALL_THROUGH`
<a id="insn-00aeffa8"></a> `00aeffa8` | `f4 c3 00 91` | add x20,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00aeffac"></a> `00aeffac` | `e8 4f 03 a9` | stp x8,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aeffb0"></a> `00aeffb0` | `08 e1 85 52` | mov w8,#0x2f08 | `FALL_THROUGH`
<a id="insn-00aeffb4"></a> `00aeffb4` | `f4 2b 00 f9` | str x20,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00aeffb8"></a> `00aeffb8` | `60 02 08 8b` | add x0,x19,x8 | `FALL_THROUGH`
<a id="insn-00aeffbc"></a> `00aeffbc` | `e1 63 00 91` | add x1,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00aeffc0"></a> `00aeffc0` | `e5 c3 00 91` | add x5,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00aeffc4"></a> `00aeffc4` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-00aeffc8"></a> `00aeffc8` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-00aeffcc"></a> `00aeffcc` | `84 00 80 52` | mov w4,#0x4 | `FALL_THROUGH`
<a id="insn-00aeffd0"></a> `00aeffd0` | `36 2c f7 97` | bl 0x008bb0a8 | `UNCONDITIONAL_CALL`
<a id="insn-00aeffd4"></a> `00aeffd4` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00aeffd8"></a> `00aeffd8` | `0f 26 f7 97` | bl 0x008b9814 | `UNCONDITIONAL_CALL`
<a id="insn-00aeffdc"></a> `00aeffdc` | `e0 2b 40 f9` | ldr x0,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00aeffe0"></a> `00aeffe0` | `e8 c3 00 91` | add x8,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00aeffe4"></a> `00aeffe4` | `1f 00 08 eb` | cmp x0,x8 | `FALL_THROUGH`
<a id="insn-00aeffe8"></a> `00aeffe8` | `80 00 00 54` | b.eq 0x00aefff8 | `CONDITIONAL_JUMP`
<a id="insn-00aeffec"></a> `00aeffec` | `00 01 00 b4` | cbz x0,0x00af000c | `CONDITIONAL_JUMP`
<a id="insn-00aefff0"></a> `00aefff0` | `08 05 80 52` | mov w8,#0x28 | `FALL_THROUGH`
<a id="insn-00aefff4"></a> `00aefff4` | `03 00 00 14` | b 0x00af0000 | `UNCONDITIONAL_JUMP`
<a id="insn-00aefff8"></a> `00aefff8` | `08 04 80 52` | mov w8,#0x20 | `FALL_THROUGH`
<a id="insn-00aefffc"></a> `00aefffc` | `e0 c3 00 91` | add x0,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00af0000"></a> `00af0000` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-00af0004"></a> `00af0004` | `28 69 68 f8` | ldr x8,[x9, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00af0008"></a> `00af0008` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00af000c"></a> `00af000c` | `e8 63 40 39` | ldrb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00af0010"></a> `00af0010` | `68 00 00 36` | tbz w8,#0x0,0x00af001c | `CONDITIONAL_JUMP`
<a id="insn-00af0014"></a> `00af0014` | `e0 17 40 f9` | ldr x0,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00af0018"></a> `00af0018` | `a6 9e 05 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00af001c"></a> `00af001c` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-00af0020"></a> `00af0020` | `68 00 00 36` | tbz w8,#0x0,0x00af002c | `CONDITIONAL_JUMP`
<a id="insn-00af0024"></a> `00af0024` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00af0028"></a> `00af0028` | `a2 9e 05 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00af002c"></a> `00af002c` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00af0030"></a> `00af0030` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00af0034"></a> `00af0034` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00af0038"></a> `00af0038` | `81 09 00 54` | b.ne 0x00af0168 | `CONDITIONAL_JUMP`
<a id="insn-00af003c"></a> `00af003c` | `f4 4f 4c a9` | ldp x20,x19,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00af0040"></a> `00af0040` | `fb 43 40 f9` | ldr x27,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00af0044"></a> `00af0044` | `f6 57 4b a9` | ldp x22,x21,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00af0048"></a> `00af0048` | `f8 5f 4a a9` | ldp x24,x23,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00af004c"></a> `00af004c` | `fa 67 49 a9` | ldp x26,x25,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00af0050"></a> `00af0050` | `fd 7b 47 a9` | ldp x29,x30,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00af0054"></a> `00af0054` | `ff 43 03 91` | add sp,sp,#0xd0 | `FALL_THROUGH`
<a id="insn-00af0058"></a> `00af0058` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00af0168"></a> `00af0168` | `5e 9e 05 94` | bl 0x00c57ae0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aefce0`](#insn-00aefce0) 範囲 `[['00aefce0', '00aefd1b']]`
  - `CONDITIONAL_JUMP` [`00aefd18`](#insn-00aefd18) → [`00aefd9c`](#insn-00aefd9c)
  - `FALL_THROUGH` [`00aefd18`](#insn-00aefd18) → [`00aefd1c`](#insn-00aefd1c)
- ブロック [`00aefd1c`](#insn-00aefd1c) 範囲 `[['00aefd1c', '00aefd23']]`
  - `CONDITIONAL_JUMP` [`00aefd20`](#insn-00aefd20) → [`00aefd44`](#insn-00aefd44)
  - `FALL_THROUGH` [`00aefd20`](#insn-00aefd20) → [`00aefd24`](#insn-00aefd24)
- ブロック [`00aefd24`](#insn-00aefd24) 範囲 `[['00aefd24', '00aefd27']]`
  - `CONDITIONAL_JUMP` [`00aefd24`](#insn-00aefd24) → [`00af002c`](#insn-00af002c)
  - `FALL_THROUGH` [`00aefd24`](#insn-00aefd24) → [`00aefd28`](#insn-00aefd28)
- ブロック [`00aefd28`](#insn-00aefd28) 範囲 `[['00aefd28', '00aefd3b']]`
  - `CONDITIONAL_JUMP` [`00aefd38`](#insn-00aefd38) → [`00af0168`](#insn-00af0168)
  - `FALL_THROUGH` [`00aefd38`](#insn-00aefd38) → [`00aefd3c`](#insn-00aefd3c)
- ブロック [`00aefd3c`](#insn-00aefd3c) 範囲 `[['00aefd3c', '00aefd43']]`
  - `UNCONDITIONAL_JUMP` [`00aefd40`](#insn-00aefd40) → [`00aefd78`](#insn-00aefd78)
- ブロック [`00aefd44`](#insn-00aefd44) 範囲 `[['00aefd44', '00aefd73']]`
  - `CONDITIONAL_JUMP` [`00aefd70`](#insn-00aefd70) → [`00af0168`](#insn-00af0168)
  - `FALL_THROUGH` [`00aefd70`](#insn-00aefd70) → [`00aefd74`](#insn-00aefd74)
- ブロック [`00aefd74`](#insn-00aefd74) 範囲 `[['00aefd74', '00aefd77']]`
  - `FALL_THROUGH` [`00aefd74`](#insn-00aefd74) → [`00aefd78`](#insn-00aefd78)
- ブロック [`00aefd78`](#insn-00aefd78) 範囲 `[['00aefd78', '00aefd9b']]`
- ブロック [`00aefd9c`](#insn-00aefd9c) 範囲 `[['00aefd9c', '00aefdab']]`
  - `CONDITIONAL_JUMP` [`00aefda8`](#insn-00aefda8) → [`00aefea4`](#insn-00aefea4)
  - `FALL_THROUGH` [`00aefda8`](#insn-00aefda8) → [`00aefdac`](#insn-00aefdac)
- ブロック [`00aefdac`](#insn-00aefdac) 範囲 `[['00aefdac', '00aefdc7']]`
  - `FALL_THROUGH` [`00aefdc4`](#insn-00aefdc4) → [`00aefdc8`](#insn-00aefdc8)
- ブロック [`00aefdc8`](#insn-00aefdc8) 範囲 `[['00aefdc8', '00aefdfb']]`
  - `FALL_THROUGH` [`00aefdf8`](#insn-00aefdf8) → [`00aefdfc`](#insn-00aefdfc)
- ブロック [`00aefdfc`](#insn-00aefdfc) 範囲 `[['00aefdfc', '00aefdff']]`
  - `FALL_THROUGH` [`00aefdfc`](#insn-00aefdfc) → [`00aefe00`](#insn-00aefe00)
- ブロック [`00aefe00`](#insn-00aefe00) 範囲 `[['00aefe00', '00aefe2f']]`
  - `CONDITIONAL_JUMP` [`00aefe2c`](#insn-00aefe2c) → [`00aefe48`](#insn-00aefe48)
  - `FALL_THROUGH` [`00aefe2c`](#insn-00aefe2c) → [`00aefe30`](#insn-00aefe30)
- ブロック [`00aefe30`](#insn-00aefe30) 範囲 `[['00aefe30', '00aefe47']]`
  - `CONDITIONAL_JUMP` [`00aefe44`](#insn-00aefe44) → [`00aefdc8`](#insn-00aefdc8)
  - `FALL_THROUGH` [`00aefe44`](#insn-00aefe44) → [`00aefe48`](#insn-00aefe48)
- ブロック [`00aefe48`](#insn-00aefe48) 範囲 `[['00aefe48', '00aefe53']]`
  - `CONDITIONAL_JUMP` [`00aefe50`](#insn-00aefe50) → [`00aefe64`](#insn-00aefe64)
  - `FALL_THROUGH` [`00aefe50`](#insn-00aefe50) → [`00aefe54`](#insn-00aefe54)
- ブロック [`00aefe54`](#insn-00aefe54) 範囲 `[['00aefe54', '00aefe63']]`
  - `CONDITIONAL_JUMP` [`00aefe60`](#insn-00aefe60) → [`00aeff6c`](#insn-00aeff6c)
  - `FALL_THROUGH` [`00aefe60`](#insn-00aefe60) → [`00aefe64`](#insn-00aefe64)
- ブロック [`00aefe64`](#insn-00aefe64) 範囲 `[['00aefe64', '00aefe7f']]`
  - `CONDITIONAL_JUMP` [`00aefe7c`](#insn-00aefe7c) → [`00af0168`](#insn-00af0168)
  - `FALL_THROUGH` [`00aefe7c`](#insn-00aefe7c) → [`00aefe80`](#insn-00aefe80)
- ブロック [`00aefe80`](#insn-00aefe80) 範囲 `[['00aefe80', '00aefea3']]`
- ブロック [`00aefea4`](#insn-00aefea4) 範囲 `[['00aefea4', '00aeff2b']]`
  - `CONDITIONAL_JUMP` [`00aeff28`](#insn-00aeff28) → [`00aeff38`](#insn-00aeff38)
  - `FALL_THROUGH` [`00aeff28`](#insn-00aeff28) → [`00aeff2c`](#insn-00aeff2c)
- ブロック [`00aeff2c`](#insn-00aeff2c) 範囲 `[['00aeff2c', '00aeff2f']]`
  - `CONDITIONAL_JUMP` [`00aeff2c`](#insn-00aeff2c) → [`00aeff4c`](#insn-00aeff4c)
  - `FALL_THROUGH` [`00aeff2c`](#insn-00aeff2c) → [`00aeff30`](#insn-00aeff30)
- ブロック [`00aeff30`](#insn-00aeff30) 範囲 `[['00aeff30', '00aeff37']]`
  - `UNCONDITIONAL_JUMP` [`00aeff34`](#insn-00aeff34) → [`00aeff40`](#insn-00aeff40)
- ブロック [`00aeff38`](#insn-00aeff38) 範囲 `[['00aeff38', '00aeff3f']]`
  - `FALL_THROUGH` [`00aeff3c`](#insn-00aeff3c) → [`00aeff40`](#insn-00aeff40)
- ブロック [`00aeff40`](#insn-00aeff40) 範囲 `[['00aeff40', '00aeff4b']]`
  - `FALL_THROUGH` [`00aeff48`](#insn-00aeff48) → [`00aeff4c`](#insn-00aeff4c)
- ブロック [`00aeff4c`](#insn-00aeff4c) 範囲 `[['00aeff4c', '00aeff53']]`
  - `CONDITIONAL_JUMP` [`00aeff50`](#insn-00aeff50) → [`00aeff5c`](#insn-00aeff5c)
  - `FALL_THROUGH` [`00aeff50`](#insn-00aeff50) → [`00aeff54`](#insn-00aeff54)
- ブロック [`00aeff54`](#insn-00aeff54) 範囲 `[['00aeff54', '00aeff5b']]`
  - `FALL_THROUGH` [`00aeff58`](#insn-00aeff58) → [`00aeff5c`](#insn-00aeff5c)
- ブロック [`00aeff5c`](#insn-00aeff5c) 範囲 `[['00aeff5c', '00aeff63']]`
  - `CONDITIONAL_JUMP` [`00aeff60`](#insn-00aeff60) → [`00af002c`](#insn-00af002c)
  - `FALL_THROUGH` [`00aeff60`](#insn-00aeff60) → [`00aeff64`](#insn-00aeff64)
- ブロック [`00aeff64`](#insn-00aeff64) 範囲 `[['00aeff64', '00aeff6b']]`
  - `UNCONDITIONAL_JUMP` [`00aeff68`](#insn-00aeff68) → [`00af0028`](#insn-00af0028)
- ブロック [`00aeff6c`](#insn-00aeff6c) 範囲 `[['00aeff6c', '00aeff9f']]`
  - `FALL_THROUGH` [`00aeff9c`](#insn-00aeff9c) → [`00aeffa0`](#insn-00aeffa0)
- ブロック [`00aeffa0`](#insn-00aeffa0) 範囲 `[['00aeffa0', '00aeffd7']]`
  - `FALL_THROUGH` [`00aeffd4`](#insn-00aeffd4) → [`00aeffd8`](#insn-00aeffd8)
- ブロック [`00aeffd8`](#insn-00aeffd8) 範囲 `[['00aeffd8', '00aeffeb']]`
  - `CONDITIONAL_JUMP` [`00aeffe8`](#insn-00aeffe8) → [`00aefff8`](#insn-00aefff8)
  - `FALL_THROUGH` [`00aeffe8`](#insn-00aeffe8) → [`00aeffec`](#insn-00aeffec)
- ブロック [`00aeffec`](#insn-00aeffec) 範囲 `[['00aeffec', '00aeffef']]`
  - `CONDITIONAL_JUMP` [`00aeffec`](#insn-00aeffec) → [`00af000c`](#insn-00af000c)
  - `FALL_THROUGH` [`00aeffec`](#insn-00aeffec) → [`00aefff0`](#insn-00aefff0)
- ブロック [`00aefff0`](#insn-00aefff0) 範囲 `[['00aefff0', '00aefff7']]`
  - `UNCONDITIONAL_JUMP` [`00aefff4`](#insn-00aefff4) → [`00af0000`](#insn-00af0000)
- ブロック [`00aefff8`](#insn-00aefff8) 範囲 `[['00aefff8', '00aeffff']]`
  - `FALL_THROUGH` [`00aefffc`](#insn-00aefffc) → [`00af0000`](#insn-00af0000)
- ブロック [`00af0000`](#insn-00af0000) 範囲 `[['00af0000', '00af000b']]`
  - `FALL_THROUGH` [`00af0008`](#insn-00af0008) → [`00af000c`](#insn-00af000c)
- ブロック [`00af000c`](#insn-00af000c) 範囲 `[['00af000c', '00af000f']]`
  - `FALL_THROUGH` [`00af000c`](#insn-00af000c) → [`00af0010`](#insn-00af0010)
- ブロック [`00af0010`](#insn-00af0010) 範囲 `[['00af0010', '00af0013']]`
  - `CONDITIONAL_JUMP` [`00af0010`](#insn-00af0010) → [`00af001c`](#insn-00af001c)
  - `FALL_THROUGH` [`00af0010`](#insn-00af0010) → [`00af0014`](#insn-00af0014)
- ブロック [`00af0014`](#insn-00af0014) 範囲 `[['00af0014', '00af001b']]`
  - `FALL_THROUGH` [`00af0018`](#insn-00af0018) → [`00af001c`](#insn-00af001c)
- ブロック [`00af001c`](#insn-00af001c) 範囲 `[['00af001c', '00af0023']]`
  - `CONDITIONAL_JUMP` [`00af0020`](#insn-00af0020) → [`00af002c`](#insn-00af002c)
  - `FALL_THROUGH` [`00af0020`](#insn-00af0020) → [`00af0024`](#insn-00af0024)
- ブロック [`00af0024`](#insn-00af0024) 範囲 `[['00af0024', '00af0027']]`
  - `FALL_THROUGH` [`00af0024`](#insn-00af0024) → [`00af0028`](#insn-00af0028)
- ブロック [`00af0028`](#insn-00af0028) 範囲 `[['00af0028', '00af002b']]`
  - `FALL_THROUGH` [`00af0028`](#insn-00af0028) → [`00af002c`](#insn-00af002c)
- ブロック [`00af002c`](#insn-00af002c) 範囲 `[['00af002c', '00af003b']]`
  - `CONDITIONAL_JUMP` [`00af0038`](#insn-00af0038) → [`00af0168`](#insn-00af0168)
  - `FALL_THROUGH` [`00af0038`](#insn-00af0038) → [`00af003c`](#insn-00af003c)
- ブロック [`00af003c`](#insn-00af003c) 範囲 `[['00af003c', '00af0043']]`
  - `FALL_THROUGH` [`00af0040`](#insn-00af0040) → [`00af0044`](#insn-00af0044)
- ブロック [`00af0044`](#insn-00af0044) 範囲 `[['00af0044', '00af005b']]`
- ブロック [`00af0168`](#insn-00af0168) 範囲 `[['00af0168', '00af016b']]`

## 命令位置別の参照

- [`00aefce4`](#insn-00aefce4) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefce8`](#insn-00aefce8) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefcec`](#insn-00aefcec) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefcf0`](#insn-00aefcf0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefcf4`](#insn-00aefcf4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefcf8`](#insn-00aefcf8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefd08`](#insn-00aefd08) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefd18`](#insn-00aefd18) → [`00aefd9c`](#insn-00aefd9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefd20`](#insn-00aefd20) → [`00aefd44`](#insn-00aefd44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefd24`](#insn-00aefd24) → [`00af002c`](#insn-00af002c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefd28`](#insn-00aefd28) → [`0047acb4`](../0047a/0047acb4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047acb4` · 推定シンボル `None` · 推定型 `None`
- [`00aefd30`](#insn-00aefd30) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefd38`](#insn-00aefd38) → [`00af0168`](#insn-00af0168) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefd40`](#insn-00aefd40) → [`00aefd78`](#insn-00aefd78) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefd44`](#insn-00aefd44) → [`0047acb4`](../0047a/0047acb4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047acb4` · 推定シンボル `None` · 推定型 `None`
- [`00aefd50`](#insn-00aefd50) → [`008b6f0c`](../008b6/008b6f0c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b6f0c` · 推定シンボル `None` · 推定型 `None`
- [`00aefd58`](#insn-00aefd58) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefd70`](#insn-00aefd70) → [`00af0168`](#insn-00af0168) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefd7c`](#insn-00aefd7c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefd80`](#insn-00aefd80) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefd84`](#insn-00aefd84) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefd88`](#insn-00aefd88) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefd8c`](#insn-00aefd8c) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefd90`](#insn-00aefd90) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefd98`](#insn-00aefd98) → [`0047cd94`](../0047c/0047cd94.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047cd94` · 推定シンボル `None` · 推定型 `None`
- [`00aefda4`](#insn-00aefda4) → [`008b6f0c`](../008b6/008b6f0c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b6f0c` · 推定シンボル `None` · 推定型 `None`
- [`00aefda8`](#insn-00aefda8) → [`00aefea4`](#insn-00aefea4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefdc8`](#insn-00aefdc8) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00aefdd0`](#insn-00aefdd0) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00aefdd4`](#insn-00aefdd4) → `0039b97c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00aefe2c`](#insn-00aefe2c) → [`00aefe48`](#insn-00aefe48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefe44`](#insn-00aefe44) → [`00aefdc8`](#insn-00aefdc8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefe50`](#insn-00aefe50) → [`00aefe64`](#insn-00aefe64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefe58`](#insn-00aefe58) → [`007441c8`](../00744/007441c8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `007441c8` · 推定シンボル `None` · 推定型 `None`
- [`00aefe60`](#insn-00aefe60) → [`00aeff6c`](#insn-00aeff6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefe6c`](#insn-00aefe6c) → [`005bc78c`](../005bc/005bc78c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005bc78c` · 推定シンボル `None` · 推定型 `None`
- [`00aefe74`](#insn-00aefe74) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefe7c`](#insn-00aefe7c) → [`00af0168`](#insn-00af0168) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefe84`](#insn-00aefe84) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefe88`](#insn-00aefe88) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefe8c`](#insn-00aefe8c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefe90`](#insn-00aefe90) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefe94`](#insn-00aefe94) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefe98`](#insn-00aefe98) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefea0`](#insn-00aefea0) → [`00aeb76c`](../00aeb/00aeb76c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00aeb76c` · 推定シンボル `None` · 推定型 `None`
- [`00aefea8`](#insn-00aefea8) → [`00ad688c`](../00ad6/00ad688c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ad688c` · 推定シンボル `None` · 推定型 `None`
- [`00aefec0`](#insn-00aefec0) → `Stack[-0xb8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefed4`](#insn-00aefed4) → `002af1fe`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aefed4`](#insn-00aefed4) → `002b575d`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aefed4`](#insn-00aefed4) → `002a3886`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aefedc`](#insn-00aefedc) → [`00c57d90`](../00c57/00c57d90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57d90` · 推定シンボル `None` · 推定型 `None`
- [`00aefee8`](#insn-00aefee8) → [`0048ce14`](../0048c/0048ce14.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0048ce14` · 推定シンボル `None` · 推定型 `None`
- [`00aefef8`](#insn-00aefef8) → `00c8df68`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00aefef8`](#insn-00aefef8) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeff00`](#insn-00aeff00) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeff1c`](#insn-00aeff1c) → [`008bac84`](../008ba/008bac84.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008bac84` · 推定シンボル `None` · 推定型 `None`
- [`00aeff20`](#insn-00aeff20) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeff28`](#insn-00aeff28) → [`00aeff38`](#insn-00aeff38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeff2c`](#insn-00aeff2c) → [`00aeff4c`](#insn-00aeff4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeff34`](#insn-00aeff34) → [`00aeff40`](#insn-00aeff40) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeff40`](#insn-00aeff40) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeff44`](#insn-00aeff44) → `00c8df88`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00aeff44`](#insn-00aeff44) → `00c8df90`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00aeff48`](#insn-00aeff48) → [`00af01cc`](../00af0/00af01cc.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00af01cc` · 推定シンボル `None` · 推定型 `None`
- [`00aeff48`](#insn-00aeff48) → [`00af01d0`](../00af0/00af01d0.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00af01d0` · 推定シンボル `None` · 推定型 `None`
- [`00aeff4c`](#insn-00aeff4c) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeff50`](#insn-00aeff50) → [`00aeff5c`](#insn-00aeff5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeff54`](#insn-00aeff54) → `Stack[-0xc0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeff58`](#insn-00aeff58) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00aeff5c`](#insn-00aeff5c) → `Stack[-0xb8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeff60`](#insn-00aeff60) → [`00af002c`](#insn-00af002c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeff64`](#insn-00aeff64) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeff68`](#insn-00aeff68) → [`00af0028`](#insn-00af0028) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeff78`](#insn-00aeff78) → `002a8213`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aeff84`](#insn-00aeff84) → `Stack[-0xd0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeff88`](#insn-00aeff88) → `Stack[-0xbf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeff8c`](#insn-00aeff8c) → `Stack[-0xcf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeff90`](#insn-00aeff90) → `Stack[-0xbb]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeff9c`](#insn-00aeff9c) → [`0048ce14`](../0048c/0048ce14.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0048ce14` · 推定シンボル `None` · 推定型 `None`
- [`00aeffac`](#insn-00aeffac) → `00c8dfe8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00aeffac`](#insn-00aeffac) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeffb4`](#insn-00aeffb4) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeffd0`](#insn-00aeffd0) → [`008bb0a8`](../008bb/008bb0a8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008bb0a8` · 推定シンボル `None` · 推定型 `None`
- [`00aeffd8`](#insn-00aeffd8) → [`008b9814`](../008b9/008b9814.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b9814` · 推定シンボル `None` · 推定型 `None`
- [`00aeffdc`](#insn-00aeffdc) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeffe8`](#insn-00aeffe8) → [`00aefff8`](#insn-00aefff8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeffec`](#insn-00aeffec) → [`00af000c`](#insn-00af000c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefff4`](#insn-00aefff4) → [`00af0000`](#insn-00af0000) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af0000`](#insn-00af0000) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af0004`](#insn-00af0004) → `00c8e008`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00af0004`](#insn-00af0004) → `00c8e010`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00af0008`](#insn-00af0008) → [`00af0290`](../00af0/00af0290.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00af0290` · 推定シンボル `None` · 推定型 `None`
- [`00af0008`](#insn-00af0008) → [`00af0294`](../00af0/00af0294.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00af0294` · 推定シンボル `None` · 推定型 `None`
- [`00af000c`](#insn-00af000c) → `Stack[-0xb8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af0010`](#insn-00af0010) → [`00af001c`](#insn-00af001c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af0014`](#insn-00af0014) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af0018`](#insn-00af0018) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00af001c`](#insn-00af001c) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af0020`](#insn-00af0020) → [`00af002c`](#insn-00af002c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af0024`](#insn-00af0024) → `Stack[-0xc0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af0028`](#insn-00af0028) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00af0030`](#insn-00af0030) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af0038`](#insn-00af0038) → [`00af0168`](#insn-00af0168) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af003c`](#insn-00af003c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af0040`](#insn-00af0040) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af0044`](#insn-00af0044) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af0048`](#insn-00af0048) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af004c`](#insn-00af004c) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af0050`](#insn-00af0050) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af0168`](#insn-00af0168) → [`00c57ae0`](../00c57/00c57ae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ae0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aefce4`](#insn-00aefce4)

~~~json
{
  "source": "00aefce4",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefce8`](#insn-00aefce8)

~~~json
{
  "source": "00aefce8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefcec`](#insn-00aefcec)

~~~json
{
  "source": "00aefcec",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefcf0`](#insn-00aefcf0)

~~~json
{
  "source": "00aefcf0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefcf4`](#insn-00aefcf4)

~~~json
{
  "source": "00aefcf4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefcf8`](#insn-00aefcf8)

~~~json
{
  "source": "00aefcf8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefd08`](#insn-00aefd08)

~~~json
{
  "source": "00aefd08",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefd18`](#insn-00aefd18)

~~~json
{
  "source": "00aefd18",
  "target": "00aefd9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefd20`](#insn-00aefd20)

~~~json
{
  "source": "00aefd20",
  "target": "00aefd44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefd24`](#insn-00aefd24)

~~~json
{
  "source": "00aefd24",
  "target": "00af002c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefd28`](#insn-00aefd28)

~~~json
{
  "source": "00aefd28",
  "target": "0047acb4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aefd30`](#insn-00aefd30)

~~~json
{
  "source": "00aefd30",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefd38`](#insn-00aefd38)

~~~json
{
  "source": "00aefd38",
  "target": "00af0168",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefd40`](#insn-00aefd40)

~~~json
{
  "source": "00aefd40",
  "target": "00aefd78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefd44`](#insn-00aefd44)

~~~json
{
  "source": "00aefd44",
  "target": "0047acb4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aefd50`](#insn-00aefd50)

~~~json
{
  "source": "00aefd50",
  "target": "008b6f0c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aefd58`](#insn-00aefd58)

~~~json
{
  "source": "00aefd58",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefd70`](#insn-00aefd70)

~~~json
{
  "source": "00aefd70",
  "target": "00af0168",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefd7c`](#insn-00aefd7c)

~~~json
{
  "source": "00aefd7c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefd80`](#insn-00aefd80)

~~~json
{
  "source": "00aefd80",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefd84`](#insn-00aefd84)

~~~json
{
  "source": "00aefd84",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefd88`](#insn-00aefd88)

~~~json
{
  "source": "00aefd88",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefd8c`](#insn-00aefd8c)

~~~json
{
  "source": "00aefd8c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefd90`](#insn-00aefd90)

~~~json
{
  "source": "00aefd90",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefd98`](#insn-00aefd98)

~~~json
{
  "source": "00aefd98",
  "target": "0047cd94",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aefda4`](#insn-00aefda4)

~~~json
{
  "source": "00aefda4",
  "target": "008b6f0c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aefda8`](#insn-00aefda8)

~~~json
{
  "source": "00aefda8",
  "target": "00aefea4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefdc8`](#insn-00aefdc8)

~~~json
{
  "source": "00aefdc8",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aefdd0`](#insn-00aefdd0)

~~~json
{
  "source": "00aefdd0",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aefdd4`](#insn-00aefdd4)

~~~json
{
  "source": "00aefdd4",
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
- 参照命令 [`00aefe2c`](#insn-00aefe2c)

~~~json
{
  "source": "00aefe2c",
  "target": "00aefe48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefe44`](#insn-00aefe44)

~~~json
{
  "source": "00aefe44",
  "target": "00aefdc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefe50`](#insn-00aefe50)

~~~json
{
  "source": "00aefe50",
  "target": "00aefe64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefe58`](#insn-00aefe58)

~~~json
{
  "source": "00aefe58",
  "target": "007441c8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aefe60`](#insn-00aefe60)

~~~json
{
  "source": "00aefe60",
  "target": "00aeff6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefe6c`](#insn-00aefe6c)

~~~json
{
  "source": "00aefe6c",
  "target": "005bc78c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aefe74`](#insn-00aefe74)

~~~json
{
  "source": "00aefe74",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefe7c`](#insn-00aefe7c)

~~~json
{
  "source": "00aefe7c",
  "target": "00af0168",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefe84`](#insn-00aefe84)

~~~json
{
  "source": "00aefe84",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefe88`](#insn-00aefe88)

~~~json
{
  "source": "00aefe88",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefe8c`](#insn-00aefe8c)

~~~json
{
  "source": "00aefe8c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefe90`](#insn-00aefe90)

~~~json
{
  "source": "00aefe90",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefe94`](#insn-00aefe94)

~~~json
{
  "source": "00aefe94",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefe98`](#insn-00aefe98)

~~~json
{
  "source": "00aefe98",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefea0`](#insn-00aefea0)

~~~json
{
  "source": "00aefea0",
  "target": "00aeb76c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aefea8`](#insn-00aefea8)

~~~json
{
  "source": "00aefea8",
  "target": "00ad688c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aefec0`](#insn-00aefec0)

~~~json
{
  "source": "00aefec0",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefed4`](#insn-00aefed4)

~~~json
{
  "source": "00aefed4",
  "target": "002af1fe",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002af1fe",
  "offset": 0,
  "size": 21,
  "datatype": "string",
  "bytes": "736c6f745f6175746f7365745f6572726f725f3200",
  "capture_start": "002af1fe",
  "capture_bytes": 21,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aefed4`](#insn-00aefed4)

~~~json
{
  "source": "00aefed4",
  "target": "002b575d",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b575d",
  "offset": 0,
  "size": 21,
  "datatype": "string",
  "bytes": "736c6f745f6175746f7365745f6572726f725f3100",
  "capture_start": "002b575d",
  "capture_bytes": 21,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aefed4`](#insn-00aefed4)

~~~json
{
  "source": "00aefed4",
  "target": "002a3886",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a3886",
  "offset": 0,
  "size": 21,
  "datatype": "string",
  "bytes": "736c6f745f6175746f7365745f6572726f725f3300",
  "capture_start": "002a3886",
  "capture_bytes": 21,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aefedc`](#insn-00aefedc)

~~~json
{
  "source": "00aefedc",
  "target": "00c57d90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aefee8`](#insn-00aefee8)

~~~json
{
  "source": "00aefee8",
  "target": "0048ce14",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aefef8`](#insn-00aefef8)

~~~json
{
  "source": "00aefef8",
  "target": "00c8df68",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8df68",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aefef8`](#insn-00aefef8)

~~~json
{
  "source": "00aefef8",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeff00`](#insn-00aeff00)

~~~json
{
  "source": "00aeff00",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeff1c`](#insn-00aeff1c)

~~~json
{
  "source": "00aeff1c",
  "target": "008bac84",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeff20`](#insn-00aeff20)

~~~json
{
  "source": "00aeff20",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeff28`](#insn-00aeff28)

~~~json
{
  "source": "00aeff28",
  "target": "00aeff38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeff2c`](#insn-00aeff2c)

~~~json
{
  "source": "00aeff2c",
  "target": "00aeff4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeff34`](#insn-00aeff34)

~~~json
{
  "source": "00aeff34",
  "target": "00aeff40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeff40`](#insn-00aeff40)

~~~json
{
  "source": "00aeff40",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeff44`](#insn-00aeff44)

~~~json
{
  "source": "00aeff44",
  "target": "00c8df88",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8df88",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aeff44`](#insn-00aeff44)

~~~json
{
  "source": "00aeff44",
  "target": "00c8df90",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8df90",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aeff48`](#insn-00aeff48)

~~~json
{
  "source": "00aeff48",
  "target": "00af01cc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeff48`](#insn-00aeff48)

~~~json
{
  "source": "00aeff48",
  "target": "00af01d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeff4c`](#insn-00aeff4c)

~~~json
{
  "source": "00aeff4c",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeff50`](#insn-00aeff50)

~~~json
{
  "source": "00aeff50",
  "target": "00aeff5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeff54`](#insn-00aeff54)

~~~json
{
  "source": "00aeff54",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeff58`](#insn-00aeff58)

~~~json
{
  "source": "00aeff58",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeff5c`](#insn-00aeff5c)

~~~json
{
  "source": "00aeff5c",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeff60`](#insn-00aeff60)

~~~json
{
  "source": "00aeff60",
  "target": "00af002c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeff64`](#insn-00aeff64)

~~~json
{
  "source": "00aeff64",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeff68`](#insn-00aeff68)

~~~json
{
  "source": "00aeff68",
  "target": "00af0028",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeff78`](#insn-00aeff78)

~~~json
{
  "source": "00aeff78",
  "target": "002a8213",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a8213",
  "offset": 0,
  "size": 21,
  "datatype": "string",
  "bytes": "736c6f745f6175746f7365745f636f6e6669726d00",
  "capture_start": "002a8213",
  "capture_bytes": 21,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aeff84`](#insn-00aeff84)

~~~json
{
  "source": "00aeff84",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeff88`](#insn-00aeff88)

~~~json
{
  "source": "00aeff88",
  "target": "Stack[-0xbf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeff8c`](#insn-00aeff8c)

~~~json
{
  "source": "00aeff8c",
  "target": "Stack[-0xcf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeff90`](#insn-00aeff90)

~~~json
{
  "source": "00aeff90",
  "target": "Stack[-0xbb]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeff9c`](#insn-00aeff9c)

~~~json
{
  "source": "00aeff9c",
  "target": "0048ce14",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeffac`](#insn-00aeffac)

~~~json
{
  "source": "00aeffac",
  "target": "00c8dfe8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8dfe8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aeffac`](#insn-00aeffac)

~~~json
{
  "source": "00aeffac",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeffb4`](#insn-00aeffb4)

~~~json
{
  "source": "00aeffb4",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeffd0`](#insn-00aeffd0)

~~~json
{
  "source": "00aeffd0",
  "target": "008bb0a8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeffd8`](#insn-00aeffd8)

~~~json
{
  "source": "00aeffd8",
  "target": "008b9814",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeffdc`](#insn-00aeffdc)

~~~json
{
  "source": "00aeffdc",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeffe8`](#insn-00aeffe8)

~~~json
{
  "source": "00aeffe8",
  "target": "00aefff8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeffec`](#insn-00aeffec)

~~~json
{
  "source": "00aeffec",
  "target": "00af000c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefff4`](#insn-00aefff4)

~~~json
{
  "source": "00aefff4",
  "target": "00af0000",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af0000`](#insn-00af0000)

~~~json
{
  "source": "00af0000",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af0004`](#insn-00af0004)

~~~json
{
  "source": "00af0004",
  "target": "00c8e008",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8e008",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00af0004`](#insn-00af0004)

~~~json
{
  "source": "00af0004",
  "target": "00c8e010",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8e010",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00af0008`](#insn-00af0008)

~~~json
{
  "source": "00af0008",
  "target": "00af0290",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af0008`](#insn-00af0008)

~~~json
{
  "source": "00af0008",
  "target": "00af0294",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af000c`](#insn-00af000c)

~~~json
{
  "source": "00af000c",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af0010`](#insn-00af0010)

~~~json
{
  "source": "00af0010",
  "target": "00af001c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af0014`](#insn-00af0014)

~~~json
{
  "source": "00af0014",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af0018`](#insn-00af0018)

~~~json
{
  "source": "00af0018",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af001c`](#insn-00af001c)

~~~json
{
  "source": "00af001c",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af0020`](#insn-00af0020)

~~~json
{
  "source": "00af0020",
  "target": "00af002c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af0024`](#insn-00af0024)

~~~json
{
  "source": "00af0024",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af0028`](#insn-00af0028)

~~~json
{
  "source": "00af0028",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af0030`](#insn-00af0030)

~~~json
{
  "source": "00af0030",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af0038`](#insn-00af0038)

~~~json
{
  "source": "00af0038",
  "target": "00af0168",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af003c`](#insn-00af003c)

~~~json
{
  "source": "00af003c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af0040`](#insn-00af0040)

~~~json
{
  "source": "00af0040",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af0044`](#insn-00af0044)

~~~json
{
  "source": "00af0044",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af0048`](#insn-00af0048)

~~~json
{
  "source": "00af0048",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af004c`](#insn-00af004c)

~~~json
{
  "source": "00af004c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af0050`](#insn-00af0050)

~~~json
{
  "source": "00af0050",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af0168`](#insn-00af0168)

~~~json
{
  "source": "00af0168",
  "target": "00c57ae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
