# 00a7becc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00a7bcd4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7b/00a7bcd4.md) · 移動量 `+0x1f8`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0061.md#compare-2b6cae5e84e4332930888daf7feb0d03)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00a7bf3c`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a7b/00a7bf3c.md) · 移動量 `+0x70`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0062.md#compare-e1a4b337f6e7761b905902b6a4242b07)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00a7becc",
  "name": "FUN_00a7becc",
  "size": 460,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1129fd49fd5aa040a5b90aa8c76493bb3c53d93a97b65e78ced25cc0c81c3c7b",
  "source_text_sha256": "1129fd49fd5aa040a5b90aa8c76493bb3c53d93a97b65e78ced25cc0c81c3c7b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00a7becc",
        "00a7c093"
      ],
      [
        "00a7c0e4",
        "00a7c0e7"
      ]
    ],
    "bytes_sha256": "a842850b2dade90f2c0b9eea09c4a63645757c50b9d5e53fa9dd3aea5888123e",
    "instruction_count": 115,
    "instruction_bytes": 460,
    "body_bytes": 460,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0047acf4](../0047a/0047acf4.md)
- [0047cdd4](../0047c/0047cdd4.md)
- [0048ce50](../0048c/0048ce50.md)
- [0048ce54](../0048c/0048ce54.md)
- [008b7a10](../008b7/008b7a10.md)
- [008ba868](../008ba/008ba868.md)
- [00a7c188](../00a7c/00a7c188.md)
- [00a7c18c](../00a7c/00a7c18c.md)
- [00c57eb0](../00c57/00c57eb0.md)
- [00c57ee0](../00c57/00c57ee0.md)

## 関連文字列（未確認候補）

~~~text
"network_unavailable"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 3796 bytes

~~~c

void FUN_00a7becc(long param_1,undefined8 param_2,int *param_3)

{
  undefined1 *puVar1;
  int iVar2;
  long lVar3;
  undefined8 uVar4;
  ulong uVar5;
  undefined ***pppuVar6;
  undefined8 uVar7;
  long lVar8;
  byte local_a0;
  char local_9f [8];
  undefined7 uStack_97;
  undefined4 uStack_90;
  uint uStack_8c;
  byte local_88 [16];
  void *local_78;
  undefined **local_70 [4];
  undefined ***local_50;
  long local_38;
  
  lVar3 = tpidr_el0;
                    /* try { // try from 00a7bee4 to 00b7bef7 has its CatchHandler @ 00a7c2d8 */
  local_38 = *(long *)(lVar3 + 0x28);
  iVar2 = *param_3;
  lVar8 = *(long *)(param_1 + 8);
  if (iVar2 == 4) {
    uVar5 = thunk_FUN_004978d0();
    if ((uVar5 & 1) != 0) {
      *(undefined4 *)(lVar8 + 0x3478) = 0x26;
      *(undefined4 *)((long)&DWORD_0039b1b4 + lVar8) = 2;
      if (*(long *)(lVar3 + 0x28) == local_38) {
                    /* try { // try from 00a7bf9c to 00b7bfaf has its CatchHandler @ 00a7c334 */
                    /* try { // try from 00a7bfb4 to 00b7c00b has its CatchHandler @ 00a7c38c */
        FUN_008b7a10(lVar8 + 0x2f38,0);
        return;
      }
      goto LAB_00a7c0e4;
    }
    local_a0 = 0x26;
    uStack_97 = (undefined7)s_network_unavailable_002b4baa._8_8_;
    uStack_90 = CONCAT31(0x656c62,SUB81(s_network_unavailable_002b4baa._8_8_,7));
    local_9f[0] = s_network_unavailable_002b4baa[0];
    local_9f[1] = s_network_unavailable_002b4baa[1];
    local_9f[2] = s_network_unavailable_002b4baa[2];
    local_9f[3] = s_network_unavailable_002b4baa[3];
    local_9f[4] = s_network_unavailable_002b4baa[4];
    local_9f[5] = s_network_unavailable_002b4baa[5];
    local_9f[6] = s_network_unavailable_002b4baa[6];
    local_9f[7] = s_network_unavailable_002b4baa[7];
    uStack_8c = uStack_8c & 0xffffff00;
    FUN_0048ce54(local_88,&local_a0);
    local_70[0] = &PTR_FUN_00c8bb70;
    local_50 = local_70;
    FUN_008ba868(lVar8 + 0x2f08,local_88,0,0,0x24,local_70);
    if (local_50 == local_70) {
      lVar8 = 0x20;
      pppuVar6 = local_70;
LAB_00a7c044:
      (**(code **)((long)*pppuVar6 + lVar8))();
    }
    else if (local_50 != (undefined ***)0x0) {
                    /* try { // try from 00a7c034 to 00b7c03b has its CatchHandler @ 00a7c2c0 */
      lVar8 = 0x28;
      pppuVar6 = local_50;
      goto LAB_00a7c044;
    }
    if ((local_88[0] & 1) != 0) {
      _ZdlPv(local_78);
    }
                    /* try { // try from 00a7c060 to 00b7c067 has its CatchHandler @ 00a7c2a0 */
    if ((local_a0 & 1) != 0) {
                    /* try { // try from 00a7c068 to 00b7c087 has its CatchHandler @ 00a7c2fc */
      _ZdlPv((void *)CONCAT44(uStack_8c,uStack_90));
    }
  }
  else {
                    /* try { // try from 00a7befc to 00b7bf0f has its CatchHandler @ 00a7c2f4 */
    puVar1 = (undefined1 *)((long)&fde_table_entry_0033e360.initial_loc + lVar8);
    if (iVar2 == 3) {
      *puVar1 = 0;
      *(undefined1 *)((long)&fde_table_entry_0033e368.initial_loc + lVar8) = 0;
      uVar4 = FUN_0047acf4();
                    /* try { // try from 00a7bf48 to 00b7bf57 has its CatchHandler @ 00a7c2d4 */
      if (*(long *)(lVar3 + 0x28) != local_38) goto LAB_00a7c0e4;
      uVar7 = 0xb;
LAB_00a7bf54:
                    /* try { // try from 00a7bf58 to 00b7bf67 has its CatchHandler @ 00a7c2d0 */
      FUN_0047cdd4(uVar4,uVar7,0);
      return;
    }
    if (iVar2 == 0) {
      *puVar1 = 0;
      *(undefined1 *)((long)&fde_table_entry_0033e368.initial_loc + lVar8) = 0;
      uVar4 = FUN_0047acf4();
      if (*(long *)(lVar3 + 0x28) != local_38) goto LAB_00a7c0e4;
      uVar7 = 10;
      goto LAB_00a7bf54;
    }
  }
  if (*(long *)(lVar3 + 0x28) == local_38) {
    return;
  }
LAB_00a7c0e4:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00a7becc"></a> `00a7becc` | `ff 83 02 d1` | sub sp,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-00a7bed0"></a> `00a7bed0` | `fd 7b 07 a9` | stp x29,x30,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00a7bed4"></a> `00a7bed4` | `f5 43 00 f9` | str x21,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00a7bed8"></a> `00a7bed8` | `f4 4f 09 a9` | stp x20,x19,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00a7bedc"></a> `00a7bedc` | `fd c3 01 91` | add x29,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00a7bee0"></a> `00a7bee0` | `54 d0 3b d5` | mrs x20,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00a7bee4"></a> `00a7bee4` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00a7bee8"></a> `00a7bee8` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00a7beec"></a> `00a7beec` | `48 00 40 b9` | ldr w8,[x2] | `FALL_THROUGH`
<a id="insn-00a7bef0"></a> `00a7bef0` | `13 04 40 f9` | ldr x19,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00a7bef4"></a> `00a7bef4` | `1f 11 00 71` | cmp w8,#0x4 | `FALL_THROUGH`
<a id="insn-00a7bef8"></a> `00a7bef8` | `a0 03 00 54` | b.eq 0x00a7bf6c | `CONDITIONAL_JUMP`
<a id="insn-00a7befc"></a> `00a7befc` | `69 fa 4c 91` | add x9,x19,#0x33e, LSL #12 | `FALL_THROUGH`
<a id="insn-00a7bf00"></a> `00a7bf00` | `1f 0d 00 71` | cmp w8,#0x3 | `FALL_THROUGH`
<a id="insn-00a7bf04"></a> `00a7bf04` | `29 81 0d 91` | add x9,x9,#0x360 | `FALL_THROUGH`
<a id="insn-00a7bf08"></a> `00a7bf08` | `60 01 00 54` | b.eq 0x00a7bf34 | `CONDITIONAL_JUMP`
<a id="insn-00a7bf0c"></a> `00a7bf0c` | `28 0b 00 35` | cbnz w8,0x00a7c070 | `CONDITIONAL_JUMP`
<a id="insn-00a7bf10"></a> `00a7bf10` | `3f 01 00 39` | strb wzr,[x9] | `FALL_THROUGH`
<a id="insn-00a7bf14"></a> `00a7bf14` | `3f 21 00 39` | strb wzr,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-00a7bf18"></a> `00a7bf18` | `77 fb e7 97` | bl 0x0047acf4 | `UNCONDITIONAL_CALL`
<a id="insn-00a7bf1c"></a> `00a7bf1c` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00a7bf20"></a> `00a7bf20` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00a7bf24"></a> `00a7bf24` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00a7bf28"></a> `00a7bf28` | `e1 0d 00 54` | b.ne 0x00a7c0e4 | `CONDITIONAL_JUMP`
<a id="insn-00a7bf2c"></a> `00a7bf2c` | `41 01 80 52` | mov w1,#0xa | `FALL_THROUGH`
<a id="insn-00a7bf30"></a> `00a7bf30` | `09 00 00 14` | b 0x00a7bf54 | `UNCONDITIONAL_JUMP`
<a id="insn-00a7bf34"></a> `00a7bf34` | `3f 01 00 39` | strb wzr,[x9] | `FALL_THROUGH`
<a id="insn-00a7bf38"></a> `00a7bf38` | `3f 21 00 39` | strb wzr,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-00a7bf3c"></a> `00a7bf3c` | `6e fb e7 97` | bl 0x0047acf4 | `UNCONDITIONAL_CALL`
<a id="insn-00a7bf40"></a> `00a7bf40` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00a7bf44"></a> `00a7bf44` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00a7bf48"></a> `00a7bf48` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00a7bf4c"></a> `00a7bf4c` | `c1 0c 00 54` | b.ne 0x00a7c0e4 | `CONDITIONAL_JUMP`
<a id="insn-00a7bf50"></a> `00a7bf50` | `61 01 80 52` | mov w1,#0xb | `FALL_THROUGH`
<a id="insn-00a7bf54"></a> `00a7bf54` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00a7bf58"></a> `00a7bf58` | `f4 4f 49 a9` | ldp x20,x19,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00a7bf5c"></a> `00a7bf5c` | `f5 43 40 f9` | ldr x21,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00a7bf60"></a> `00a7bf60` | `fd 7b 47 a9` | ldp x29,x30,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00a7bf64"></a> `00a7bf64` | `ff 83 02 91` | add sp,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-00a7bf68"></a> `00a7bf68` | `9b 03 e8 17` | b 0x0047cdd4 | `CALL_TERMINATOR`
<a id="insn-00a7bf6c"></a> `00a7bf6c` | `b9 43 e8 97` | bl 0x0048ce50 | `UNCONDITIONAL_CALL`
<a id="insn-00a7bf70"></a> `00a7bf70` | `60 02 00 36` | tbz w0,#0x0,0x00a7bfbc | `CONDITIONAL_JUMP`
<a id="insn-00a7bf74"></a> `00a7bf74` | `88 36 96 52` | mov w8,#0xb1b4 | `FALL_THROUGH`
<a id="insn-00a7bf78"></a> `00a7bf78` | `ca 04 80 52` | mov w10,#0x26 | `FALL_THROUGH`
<a id="insn-00a7bf7c"></a> `00a7bf7c` | `49 00 80 52` | mov w9,#0x2 | `FALL_THROUGH`
<a id="insn-00a7bf80"></a> `00a7bf80` | `28 07 a0 72` | movk w8,#0x39, LSL #16 | `FALL_THROUGH`
<a id="insn-00a7bf84"></a> `00a7bf84` | `6a 7a 34 b9` | str w10,[x19, #0x3478] | `FALL_THROUGH`
<a id="insn-00a7bf88"></a> `00a7bf88` | `69 6a 28 b8` | str w9,[x19, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00a7bf8c"></a> `00a7bf8c` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00a7bf90"></a> `00a7bf90` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00a7bf94"></a> `00a7bf94` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00a7bf98"></a> `00a7bf98` | `61 0a 00 54` | b.ne 0x00a7c0e4 | `CONDITIONAL_JUMP`
<a id="insn-00a7bf9c"></a> `00a7bf9c` | `08 e7 85 52` | mov w8,#0x2f38 | `FALL_THROUGH`
<a id="insn-00a7bfa0"></a> `00a7bfa0` | `60 02 08 8b` | add x0,x19,x8 | `FALL_THROUGH`
<a id="insn-00a7bfa4"></a> `00a7bfa4` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00a7bfa8"></a> `00a7bfa8` | `f4 4f 49 a9` | ldp x20,x19,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00a7bfac"></a> `00a7bfac` | `f5 43 40 f9` | ldr x21,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00a7bfb0"></a> `00a7bfb0` | `fd 7b 47 a9` | ldp x29,x30,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00a7bfb4"></a> `00a7bfb4` | `ff 83 02 91` | add sp,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-00a7bfb8"></a> `00a7bfb8` | `96 ee f8 17` | b 0x008b7a10 | `CALL_TERMINATOR`
<a id="insn-00a7bfbc"></a> `00a7bfbc` | `c9 c1 ff b0` | adrp x9,0x2b4000 | `FALL_THROUGH`
<a id="insn-00a7bfc0"></a> `00a7bfc0` | `29 a9 2e 91` | add x9,x9,#0xbaa | `FALL_THROUGH`
<a id="insn-00a7bfc4"></a> `00a7bfc4` | `2a 4c 8c 52` | mov w10,#0x6261 | `FALL_THROUGH`
<a id="insn-00a7bfc8"></a> `00a7bfc8` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00a7bfcc"></a> `00a7bfcc` | `c8 04 80 52` | mov w8,#0x26 | `FALL_THROUGH`
<a id="insn-00a7bfd0"></a> `00a7bfd0` | `8a ad ac 72` | movk w10,#0x656c, LSL #16 | `FALL_THROUGH`
<a id="insn-00a7bfd4"></a> `00a7bfd4` | `e8 03 00 39` | strb w8,[sp] | `FALL_THROUGH`
<a id="insn-00a7bfd8"></a> `00a7bfd8` | `ea 13 00 b9` | str w10,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a7bfdc"></a> `00a7bfdc` | `e0 13 80 3c` | stur q0,[sp, #0x1] | `FALL_THROUGH`
<a id="insn-00a7bfe0"></a> `00a7bfe0` | `ff 53 00 39` | strb wzr,[sp, #0x14] | `FALL_THROUGH`
<a id="insn-00a7bfe4"></a> `00a7bfe4` | `e8 63 00 91` | add x8,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00a7bfe8"></a> `00a7bfe8` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00a7bfec"></a> `00a7bfec` | `9a 43 e8 97` | bl 0x0048ce54 | `UNCONDITIONAL_CALL`
<a id="insn-00a7bff0"></a> `00a7bff0` | `88 10 00 90` | adrp x8,0xc8b000 | `FALL_THROUGH`
<a id="insn-00a7bff4"></a> `00a7bff4` | `08 c1 2d 91` | add x8,x8,#0xb70 | `FALL_THROUGH`
<a id="insn-00a7bff8"></a> `00a7bff8` | `f5 c3 00 91` | add x21,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00a7bffc"></a> `00a7bffc` | `e8 1b 00 f9` | str x8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00a7c000"></a> `00a7c000` | `08 e1 85 52` | mov w8,#0x2f08 | `FALL_THROUGH`
<a id="insn-00a7c004"></a> `00a7c004` | `f5 2b 00 f9` | str x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00a7c008"></a> `00a7c008` | `60 02 08 8b` | add x0,x19,x8 | `FALL_THROUGH`
<a id="insn-00a7c00c"></a> `00a7c00c` | `e1 63 00 91` | add x1,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00a7c010"></a> `00a7c010` | `e5 c3 00 91` | add x5,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00a7c014"></a> `00a7c014` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-00a7c018"></a> `00a7c018` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-00a7c01c"></a> `00a7c01c` | `84 04 80 52` | mov w4,#0x24 | `FALL_THROUGH`
<a id="insn-00a7c020"></a> `00a7c020` | `12 fa f8 97` | bl 0x008ba868 | `UNCONDITIONAL_CALL`
<a id="insn-00a7c024"></a> `00a7c024` | `e0 2b 40 f9` | ldr x0,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00a7c028"></a> `00a7c028` | `1f 00 15 eb` | cmp x0,x21 | `FALL_THROUGH`
<a id="insn-00a7c02c"></a> `00a7c02c` | `80 00 00 54` | b.eq 0x00a7c03c | `CONDITIONAL_JUMP`
<a id="insn-00a7c030"></a> `00a7c030` | `00 01 00 b4` | cbz x0,0x00a7c050 | `CONDITIONAL_JUMP`
<a id="insn-00a7c034"></a> `00a7c034` | `08 05 80 52` | mov w8,#0x28 | `FALL_THROUGH`
<a id="insn-00a7c038"></a> `00a7c038` | `03 00 00 14` | b 0x00a7c044 | `UNCONDITIONAL_JUMP`
<a id="insn-00a7c03c"></a> `00a7c03c` | `08 04 80 52` | mov w8,#0x20 | `FALL_THROUGH`
<a id="insn-00a7c040"></a> `00a7c040` | `e0 c3 00 91` | add x0,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00a7c044"></a> `00a7c044` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-00a7c048"></a> `00a7c048` | `28 69 68 f8` | ldr x8,[x9, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00a7c04c"></a> `00a7c04c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00a7c050"></a> `00a7c050` | `e8 63 40 39` | ldrb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00a7c054"></a> `00a7c054` | `68 00 00 36` | tbz w8,#0x0,0x00a7c060 | `CONDITIONAL_JUMP`
<a id="insn-00a7c058"></a> `00a7c058` | `e0 17 40 f9` | ldr x0,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00a7c05c"></a> `00a7c05c` | `95 6f 07 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00a7c060"></a> `00a7c060` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-00a7c064"></a> `00a7c064` | `68 00 00 36` | tbz w8,#0x0,0x00a7c070 | `CONDITIONAL_JUMP`
<a id="insn-00a7c068"></a> `00a7c068` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a7c06c"></a> `00a7c06c` | `91 6f 07 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00a7c070"></a> `00a7c070` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00a7c074"></a> `00a7c074` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00a7c078"></a> `00a7c078` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00a7c07c"></a> `00a7c07c` | `41 03 00 54` | b.ne 0x00a7c0e4 | `CONDITIONAL_JUMP`
<a id="insn-00a7c080"></a> `00a7c080` | `f4 4f 49 a9` | ldp x20,x19,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00a7c084"></a> `00a7c084` | `f5 43 40 f9` | ldr x21,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00a7c088"></a> `00a7c088` | `fd 7b 47 a9` | ldp x29,x30,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00a7c08c"></a> `00a7c08c` | `ff 83 02 91` | add sp,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-00a7c090"></a> `00a7c090` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00a7c0e4"></a> `00a7c0e4` | `7f 6f 07 94` | bl 0x00c57ee0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00a7becc`](#insn-00a7becc) 範囲 `[['00a7becc', '00a7bee3']]`
  - `FALL_THROUGH` [`00a7bee0`](#insn-00a7bee0) → [`00a7bee4`](#insn-00a7bee4)
- ブロック [`00a7bee4`](#insn-00a7bee4) 範囲 `[['00a7bee4', '00a7befb']]`
  - `CONDITIONAL_JUMP` [`00a7bef8`](#insn-00a7bef8) → [`00a7bf6c`](#insn-00a7bf6c)
  - `FALL_THROUGH` [`00a7bef8`](#insn-00a7bef8) → [`00a7befc`](#insn-00a7befc)
- ブロック [`00a7befc`](#insn-00a7befc) 範囲 `[['00a7befc', '00a7bf0b']]`
  - `CONDITIONAL_JUMP` [`00a7bf08`](#insn-00a7bf08) → [`00a7bf34`](#insn-00a7bf34)
  - `FALL_THROUGH` [`00a7bf08`](#insn-00a7bf08) → [`00a7bf0c`](#insn-00a7bf0c)
- ブロック [`00a7bf0c`](#insn-00a7bf0c) 範囲 `[['00a7bf0c', '00a7bf0f']]`
  - `CONDITIONAL_JUMP` [`00a7bf0c`](#insn-00a7bf0c) → [`00a7c070`](#insn-00a7c070)
  - `FALL_THROUGH` [`00a7bf0c`](#insn-00a7bf0c) → [`00a7bf10`](#insn-00a7bf10)
- ブロック [`00a7bf10`](#insn-00a7bf10) 範囲 `[['00a7bf10', '00a7bf2b']]`
  - `CONDITIONAL_JUMP` [`00a7bf28`](#insn-00a7bf28) → [`00a7c0e4`](#insn-00a7c0e4)
  - `FALL_THROUGH` [`00a7bf28`](#insn-00a7bf28) → [`00a7bf2c`](#insn-00a7bf2c)
- ブロック [`00a7bf2c`](#insn-00a7bf2c) 範囲 `[['00a7bf2c', '00a7bf33']]`
  - `UNCONDITIONAL_JUMP` [`00a7bf30`](#insn-00a7bf30) → [`00a7bf54`](#insn-00a7bf54)
- ブロック [`00a7bf34`](#insn-00a7bf34) 範囲 `[['00a7bf34', '00a7bf47']]`
  - `FALL_THROUGH` [`00a7bf44`](#insn-00a7bf44) → [`00a7bf48`](#insn-00a7bf48)
- ブロック [`00a7bf48`](#insn-00a7bf48) 範囲 `[['00a7bf48', '00a7bf4f']]`
  - `CONDITIONAL_JUMP` [`00a7bf4c`](#insn-00a7bf4c) → [`00a7c0e4`](#insn-00a7c0e4)
  - `FALL_THROUGH` [`00a7bf4c`](#insn-00a7bf4c) → [`00a7bf50`](#insn-00a7bf50)
- ブロック [`00a7bf50`](#insn-00a7bf50) 範囲 `[['00a7bf50', '00a7bf53']]`
  - `FALL_THROUGH` [`00a7bf50`](#insn-00a7bf50) → [`00a7bf54`](#insn-00a7bf54)
- ブロック [`00a7bf54`](#insn-00a7bf54) 範囲 `[['00a7bf54', '00a7bf57']]`
  - `FALL_THROUGH` [`00a7bf54`](#insn-00a7bf54) → [`00a7bf58`](#insn-00a7bf58)
- ブロック [`00a7bf58`](#insn-00a7bf58) 範囲 `[['00a7bf58', '00a7bf6b']]`
- ブロック [`00a7bf6c`](#insn-00a7bf6c) 範囲 `[['00a7bf6c', '00a7bf73']]`
  - `CONDITIONAL_JUMP` [`00a7bf70`](#insn-00a7bf70) → [`00a7bfbc`](#insn-00a7bfbc)
  - `FALL_THROUGH` [`00a7bf70`](#insn-00a7bf70) → [`00a7bf74`](#insn-00a7bf74)
- ブロック [`00a7bf74`](#insn-00a7bf74) 範囲 `[['00a7bf74', '00a7bf9b']]`
  - `CONDITIONAL_JUMP` [`00a7bf98`](#insn-00a7bf98) → [`00a7c0e4`](#insn-00a7c0e4)
  - `FALL_THROUGH` [`00a7bf98`](#insn-00a7bf98) → [`00a7bf9c`](#insn-00a7bf9c)
- ブロック [`00a7bf9c`](#insn-00a7bf9c) 範囲 `[['00a7bf9c', '00a7bfb3']]`
  - `FALL_THROUGH` [`00a7bfb0`](#insn-00a7bfb0) → [`00a7bfb4`](#insn-00a7bfb4)
- ブロック [`00a7bfb4`](#insn-00a7bfb4) 範囲 `[['00a7bfb4', '00a7bfbb']]`
- ブロック [`00a7bfbc`](#insn-00a7bfbc) 範囲 `[['00a7bfbc', '00a7c02f']]`
  - `CONDITIONAL_JUMP` [`00a7c02c`](#insn-00a7c02c) → [`00a7c03c`](#insn-00a7c03c)
  - `FALL_THROUGH` [`00a7c02c`](#insn-00a7c02c) → [`00a7c030`](#insn-00a7c030)
- ブロック [`00a7c030`](#insn-00a7c030) 範囲 `[['00a7c030', '00a7c033']]`
  - `CONDITIONAL_JUMP` [`00a7c030`](#insn-00a7c030) → [`00a7c050`](#insn-00a7c050)
  - `FALL_THROUGH` [`00a7c030`](#insn-00a7c030) → [`00a7c034`](#insn-00a7c034)
- ブロック [`00a7c034`](#insn-00a7c034) 範囲 `[['00a7c034', '00a7c03b']]`
  - `UNCONDITIONAL_JUMP` [`00a7c038`](#insn-00a7c038) → [`00a7c044`](#insn-00a7c044)
- ブロック [`00a7c03c`](#insn-00a7c03c) 範囲 `[['00a7c03c', '00a7c043']]`
  - `FALL_THROUGH` [`00a7c040`](#insn-00a7c040) → [`00a7c044`](#insn-00a7c044)
- ブロック [`00a7c044`](#insn-00a7c044) 範囲 `[['00a7c044', '00a7c04f']]`
  - `FALL_THROUGH` [`00a7c04c`](#insn-00a7c04c) → [`00a7c050`](#insn-00a7c050)
- ブロック [`00a7c050`](#insn-00a7c050) 範囲 `[['00a7c050', '00a7c057']]`
  - `CONDITIONAL_JUMP` [`00a7c054`](#insn-00a7c054) → [`00a7c060`](#insn-00a7c060)
  - `FALL_THROUGH` [`00a7c054`](#insn-00a7c054) → [`00a7c058`](#insn-00a7c058)
- ブロック [`00a7c058`](#insn-00a7c058) 範囲 `[['00a7c058', '00a7c05f']]`
  - `FALL_THROUGH` [`00a7c05c`](#insn-00a7c05c) → [`00a7c060`](#insn-00a7c060)
- ブロック [`00a7c060`](#insn-00a7c060) 範囲 `[['00a7c060', '00a7c067']]`
  - `CONDITIONAL_JUMP` [`00a7c064`](#insn-00a7c064) → [`00a7c070`](#insn-00a7c070)
  - `FALL_THROUGH` [`00a7c064`](#insn-00a7c064) → [`00a7c068`](#insn-00a7c068)
- ブロック [`00a7c068`](#insn-00a7c068) 範囲 `[['00a7c068', '00a7c06f']]`
  - `FALL_THROUGH` [`00a7c06c`](#insn-00a7c06c) → [`00a7c070`](#insn-00a7c070)
- ブロック [`00a7c070`](#insn-00a7c070) 範囲 `[['00a7c070', '00a7c07f']]`
  - `CONDITIONAL_JUMP` [`00a7c07c`](#insn-00a7c07c) → [`00a7c0e4`](#insn-00a7c0e4)
  - `FALL_THROUGH` [`00a7c07c`](#insn-00a7c07c) → [`00a7c080`](#insn-00a7c080)
- ブロック [`00a7c080`](#insn-00a7c080) 範囲 `[['00a7c080', '00a7c093']]`
- ブロック [`00a7c0e4`](#insn-00a7c0e4) 範囲 `[['00a7c0e4', '00a7c0e7']]`

## 命令位置別の参照

- [`00a7bed0`](#insn-00a7bed0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7bed4`](#insn-00a7bed4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7bed8`](#insn-00a7bed8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7bee8`](#insn-00a7bee8) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7bef8`](#insn-00a7bef8) → [`00a7bf6c`](#insn-00a7bf6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7bf08`](#insn-00a7bf08) → [`00a7bf34`](#insn-00a7bf34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7bf0c`](#insn-00a7bf0c) → [`00a7c070`](#insn-00a7c070) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7bf10`](#insn-00a7bf10) → `0033e360`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00a7bf14`](#insn-00a7bf14) → `0033e368`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00a7bf18`](#insn-00a7bf18) → [`0047acf4`](../0047a/0047acf4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047acf4` · 推定シンボル `None` · 推定型 `None`
- [`00a7bf20`](#insn-00a7bf20) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7bf28`](#insn-00a7bf28) → [`00a7c0e4`](#insn-00a7c0e4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7bf30`](#insn-00a7bf30) → [`00a7bf54`](#insn-00a7bf54) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7bf34`](#insn-00a7bf34) → `0033e360`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00a7bf38`](#insn-00a7bf38) → `0033e368`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00a7bf3c`](#insn-00a7bf3c) → [`0047acf4`](../0047a/0047acf4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047acf4` · 推定シンボル `None` · 推定型 `None`
- [`00a7bf44`](#insn-00a7bf44) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7bf4c`](#insn-00a7bf4c) → [`00a7c0e4`](#insn-00a7c0e4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7bf58`](#insn-00a7bf58) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7bf5c`](#insn-00a7bf5c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7bf60`](#insn-00a7bf60) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7bf68`](#insn-00a7bf68) → [`0047cdd4`](../0047c/0047cdd4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047cdd4` · 推定シンボル `None` · 推定型 `None`
- [`00a7bf6c`](#insn-00a7bf6c) → [`0048ce50`](../0048c/0048ce50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0048ce50` · 推定シンボル `None` · 推定型 `None`
- [`00a7bf70`](#insn-00a7bf70) → [`00a7bfbc`](#insn-00a7bfbc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7bf88`](#insn-00a7bf88) → `0039b1b4`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00a7bf90`](#insn-00a7bf90) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7bf98`](#insn-00a7bf98) → [`00a7c0e4`](#insn-00a7c0e4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7bfa8`](#insn-00a7bfa8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7bfac`](#insn-00a7bfac) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7bfb0`](#insn-00a7bfb0) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7bfb8`](#insn-00a7bfb8) → [`008b7a10`](../008b7/008b7a10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b7a10` · 推定シンボル `None` · 推定型 `None`
- [`00a7bfc8`](#insn-00a7bfc8) → `002b4baa`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00a7bfd4`](#insn-00a7bfd4) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7bfd8`](#insn-00a7bfd8) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7bfdc`](#insn-00a7bfdc) → `Stack[-0x9f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7bfe0`](#insn-00a7bfe0) → `Stack[-0x8c]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7bfec`](#insn-00a7bfec) → [`0048ce54`](../0048c/0048ce54.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0048ce54` · 推定シンボル `None` · 推定型 `None`
- [`00a7bffc`](#insn-00a7bffc) → `00c8bb70`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00a7bffc`](#insn-00a7bffc) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7c004`](#insn-00a7c004) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7c020`](#insn-00a7c020) → [`008ba868`](../008ba/008ba868.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008ba868` · 推定シンボル `None` · 推定型 `None`
- [`00a7c024`](#insn-00a7c024) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7c02c`](#insn-00a7c02c) → [`00a7c03c`](#insn-00a7c03c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7c030`](#insn-00a7c030) → [`00a7c050`](#insn-00a7c050) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7c038`](#insn-00a7c038) → [`00a7c044`](#insn-00a7c044) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7c044`](#insn-00a7c044) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7c048`](#insn-00a7c048) → `00c8bb90`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00a7c048`](#insn-00a7c048) → `00c8bb98`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00a7c04c`](#insn-00a7c04c) → [`00a7c188`](../00a7c/00a7c188.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00a7c188` · 推定シンボル `None` · 推定型 `None`
- [`00a7c04c`](#insn-00a7c04c) → [`00a7c18c`](../00a7c/00a7c18c.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00a7c18c` · 推定シンボル `None` · 推定型 `None`
- [`00a7c050`](#insn-00a7c050) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7c054`](#insn-00a7c054) → [`00a7c060`](#insn-00a7c060) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7c058`](#insn-00a7c058) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7c05c`](#insn-00a7c05c) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00a7c060`](#insn-00a7c060) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7c064`](#insn-00a7c064) → [`00a7c070`](#insn-00a7c070) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7c068`](#insn-00a7c068) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7c06c`](#insn-00a7c06c) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00a7c074`](#insn-00a7c074) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7c07c`](#insn-00a7c07c) → [`00a7c0e4`](#insn-00a7c0e4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7c080`](#insn-00a7c080) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7c084`](#insn-00a7c084) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7c088`](#insn-00a7c088) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7c0e4`](#insn-00a7c0e4) → [`00c57ee0`](../00c57/00c57ee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ee0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00a7bed0`](#insn-00a7bed0)

~~~json
{
  "source": "00a7bed0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7bed4`](#insn-00a7bed4)

~~~json
{
  "source": "00a7bed4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7bed8`](#insn-00a7bed8)

~~~json
{
  "source": "00a7bed8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7bee8`](#insn-00a7bee8)

~~~json
{
  "source": "00a7bee8",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7bef8`](#insn-00a7bef8)

~~~json
{
  "source": "00a7bef8",
  "target": "00a7bf6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7bf08`](#insn-00a7bf08)

~~~json
{
  "source": "00a7bf08",
  "target": "00a7bf34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7bf0c`](#insn-00a7bf0c)

~~~json
{
  "source": "00a7bf0c",
  "target": "00a7c070",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7bf10`](#insn-00a7bf10)

~~~json
{
  "source": "00a7bf10",
  "target": "0033e360",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0033e360",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "98678b0078d81100",
  "capture_start": "0033e360",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a7bf14`](#insn-00a7bf14)

~~~json
{
  "source": "00a7bf14",
  "target": "0033e368",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0033e368",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "20698b00a8d81100",
  "capture_start": "0033e368",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a7bf18`](#insn-00a7bf18)

~~~json
{
  "source": "00a7bf18",
  "target": "0047acf4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a7bf20`](#insn-00a7bf20)

~~~json
{
  "source": "00a7bf20",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7bf28`](#insn-00a7bf28)

~~~json
{
  "source": "00a7bf28",
  "target": "00a7c0e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7bf30`](#insn-00a7bf30)

~~~json
{
  "source": "00a7bf30",
  "target": "00a7bf54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7bf34`](#insn-00a7bf34)

~~~json
{
  "source": "00a7bf34",
  "target": "0033e360",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0033e360",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "98678b0078d81100",
  "capture_start": "0033e360",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a7bf38`](#insn-00a7bf38)

~~~json
{
  "source": "00a7bf38",
  "target": "0033e368",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0033e368",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "20698b00a8d81100",
  "capture_start": "0033e368",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a7bf3c`](#insn-00a7bf3c)

~~~json
{
  "source": "00a7bf3c",
  "target": "0047acf4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a7bf44`](#insn-00a7bf44)

~~~json
{
  "source": "00a7bf44",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7bf4c`](#insn-00a7bf4c)

~~~json
{
  "source": "00a7bf4c",
  "target": "00a7c0e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7bf58`](#insn-00a7bf58)

~~~json
{
  "source": "00a7bf58",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7bf5c`](#insn-00a7bf5c)

~~~json
{
  "source": "00a7bf5c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7bf60`](#insn-00a7bf60)

~~~json
{
  "source": "00a7bf60",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7bf68`](#insn-00a7bf68)

~~~json
{
  "source": "00a7bf68",
  "target": "0047cdd4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a7bf6c`](#insn-00a7bf6c)

~~~json
{
  "source": "00a7bf6c",
  "target": "0048ce50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a7bf70`](#insn-00a7bf70)

~~~json
{
  "source": "00a7bf70",
  "target": "00a7bfbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7bf88`](#insn-00a7bf88)

~~~json
{
  "source": "00a7bf88",
  "target": "0039b1b4",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0039b1b4",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "e47a4f00",
  "capture_start": "0039b1b4",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a7bf90`](#insn-00a7bf90)

~~~json
{
  "source": "00a7bf90",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7bf98`](#insn-00a7bf98)

~~~json
{
  "source": "00a7bf98",
  "target": "00a7c0e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7bfa8`](#insn-00a7bfa8)

~~~json
{
  "source": "00a7bfa8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7bfac`](#insn-00a7bfac)

~~~json
{
  "source": "00a7bfac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7bfb0`](#insn-00a7bfb0)

~~~json
{
  "source": "00a7bfb0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7bfb8`](#insn-00a7bfb8)

~~~json
{
  "source": "00a7bfb8",
  "target": "008b7a10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a7bfc8`](#insn-00a7bfc8)

~~~json
{
  "source": "00a7bfc8",
  "target": "002b4baa",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b4baa",
  "offset": 0,
  "size": 20,
  "datatype": "string",
  "bytes": "6e6574776f726b5f756e617661696c61626c6500",
  "capture_start": "002b4baa",
  "capture_bytes": 20,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a7bfd4`](#insn-00a7bfd4)

~~~json
{
  "source": "00a7bfd4",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7bfd8`](#insn-00a7bfd8)

~~~json
{
  "source": "00a7bfd8",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7bfdc`](#insn-00a7bfdc)

~~~json
{
  "source": "00a7bfdc",
  "target": "Stack[-0x9f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7bfe0`](#insn-00a7bfe0)

~~~json
{
  "source": "00a7bfe0",
  "target": "Stack[-0x8c]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7bfec`](#insn-00a7bfec)

~~~json
{
  "source": "00a7bfec",
  "target": "0048ce54",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a7bffc`](#insn-00a7bffc)

~~~json
{
  "source": "00a7bffc",
  "target": "00c8bb70",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8bb70",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00a7bffc`](#insn-00a7bffc)

~~~json
{
  "source": "00a7bffc",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7c004`](#insn-00a7c004)

~~~json
{
  "source": "00a7c004",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7c020`](#insn-00a7c020)

~~~json
{
  "source": "00a7c020",
  "target": "008ba868",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a7c024`](#insn-00a7c024)

~~~json
{
  "source": "00a7c024",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7c02c`](#insn-00a7c02c)

~~~json
{
  "source": "00a7c02c",
  "target": "00a7c03c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7c030`](#insn-00a7c030)

~~~json
{
  "source": "00a7c030",
  "target": "00a7c050",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7c038`](#insn-00a7c038)

~~~json
{
  "source": "00a7c038",
  "target": "00a7c044",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7c044`](#insn-00a7c044)

~~~json
{
  "source": "00a7c044",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7c048`](#insn-00a7c048)

~~~json
{
  "source": "00a7c048",
  "target": "00c8bb90",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8bb90",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00a7c048`](#insn-00a7c048)

~~~json
{
  "source": "00a7c048",
  "target": "00c8bb98",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8bb98",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00a7c04c`](#insn-00a7c04c)

~~~json
{
  "source": "00a7c04c",
  "target": "00a7c188",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a7c04c`](#insn-00a7c04c)

~~~json
{
  "source": "00a7c04c",
  "target": "00a7c18c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a7c050`](#insn-00a7c050)

~~~json
{
  "source": "00a7c050",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7c054`](#insn-00a7c054)

~~~json
{
  "source": "00a7c054",
  "target": "00a7c060",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7c058`](#insn-00a7c058)

~~~json
{
  "source": "00a7c058",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7c05c`](#insn-00a7c05c)

~~~json
{
  "source": "00a7c05c",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a7c060`](#insn-00a7c060)

~~~json
{
  "source": "00a7c060",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7c064`](#insn-00a7c064)

~~~json
{
  "source": "00a7c064",
  "target": "00a7c070",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7c068`](#insn-00a7c068)

~~~json
{
  "source": "00a7c068",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7c06c`](#insn-00a7c06c)

~~~json
{
  "source": "00a7c06c",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a7c074`](#insn-00a7c074)

~~~json
{
  "source": "00a7c074",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7c07c`](#insn-00a7c07c)

~~~json
{
  "source": "00a7c07c",
  "target": "00a7c0e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7c080`](#insn-00a7c080)

~~~json
{
  "source": "00a7c080",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7c084`](#insn-00a7c084)

~~~json
{
  "source": "00a7c084",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7c088`](#insn-00a7c088)

~~~json
{
  "source": "00a7c088",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7c0e4`](#insn-00a7c0e4)

~~~json
{
  "source": "00a7c0e4",
  "target": "00c57ee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
