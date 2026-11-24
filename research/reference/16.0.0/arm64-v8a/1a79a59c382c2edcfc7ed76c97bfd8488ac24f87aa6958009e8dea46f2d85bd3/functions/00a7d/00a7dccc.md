# 00a7dccc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00a1fe3c`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a1f/00a1fe3c.md) · 移動量 `+0x5de90`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0051.md#compare-b0075d50a74190d4691c64a9edbe1a48)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00a7dec4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a7d/00a7dec4.md) · 移動量 `+0x1f8`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0061.md#compare-394f3afb21306d0bbbfdff231d30874e)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00a7dccc",
  "name": "FUN_00a7dccc",
  "size": 452,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3ee0e29b134af75aa520adb5b50f39fbcc31fd79dcac008d375a57ed19d506b5",
  "source_text_sha256": "3ee0e29b134af75aa520adb5b50f39fbcc31fd79dcac008d375a57ed19d506b5",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00a7dccc",
        "00a7de8b"
      ],
      [
        "00a7dedc",
        "00a7dedf"
      ]
    ],
    "bytes_sha256": "772b27a1fbf5c21cf1d6a81a8619d63953238ebdff6eba2b659cc619e499cd41",
    "instruction_count": 113,
    "instruction_bytes": 452,
    "body_bytes": 452,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0047acb4](../0047a/0047acb4.md)
- [0047cd94](../0047c/0047cd94.md)
- [0048ce10](../0048c/0048ce10.md)
- [0048ce14](../0048c/0048ce14.md)
- [008b79cc](../008b7/008b79cc.md)
- [008ba824](../008ba/008ba824.md)
- [00a7df80](../00a7d/00a7df80.md)
- [00a7df84](../00a7d/00a7df84.md)
- [00c57ab0](../00c57/00c57ab0.md)
- [00c57ae0](../00c57/00c57ae0.md)

## 関連文字列（未確認候補）

~~~text
"network_unavailable"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2781 bytes

~~~c

void FUN_00a7dccc(long param_1,undefined8 param_2,int *param_3)

{
  int iVar1;
  long lVar2;
  undefined8 uVar3;
  ulong uVar4;
  undefined ***pppuVar5;
  undefined8 uVar6;
  long lVar7;
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
  
  lVar2 = tpidr_el0;
  local_38 = *(long *)(lVar2 + 0x28);
  iVar1 = *param_3;
  lVar7 = *(long *)(param_1 + 8);
  if (iVar1 == 4) {
    uVar4 = thunk_FUN_00497890();
    if ((uVar4 & 1) != 0) {
      *(undefined4 *)(lVar7 + 0x3478) = 0x2f;
      *(undefined4 *)((long)&QWORD_0039b1b4 + lVar7) = 2;
      if (*(long *)(lVar2 + 0x28) == local_38) {
        FUN_008b79cc(lVar7 + 0x2f38,0);
        return;
      }
      goto LAB_00a7dedc;
    }
    local_a0 = 0x26;
    uStack_97 = (undefined7)s_network_unavailable_002b4b6a._8_8_;
    uStack_90 = CONCAT31(0x656c62,SUB81(s_network_unavailable_002b4b6a._8_8_,7));
    local_9f[0] = s_network_unavailable_002b4b6a[0];
    local_9f[1] = s_network_unavailable_002b4b6a[1];
    local_9f[2] = s_network_unavailable_002b4b6a[2];
    local_9f[3] = s_network_unavailable_002b4b6a[3];
    local_9f[4] = s_network_unavailable_002b4b6a[4];
    local_9f[5] = s_network_unavailable_002b4b6a[5];
    local_9f[6] = s_network_unavailable_002b4b6a[6];
    local_9f[7] = s_network_unavailable_002b4b6a[7];
    uStack_8c = uStack_8c & 0xffffff00;
    FUN_0048ce14(local_88,&local_a0);
    local_70[0] = &PTR_FUN_00c8ba90;
    local_50 = local_70;
    FUN_008ba824(lVar7 + 0x2f08,local_88,0,0,0x24,local_70);
    if (local_50 == local_70) {
      lVar7 = 0x20;
      pppuVar5 = local_70;
LAB_00a7de3c:
      (**(code **)((long)*pppuVar5 + lVar7))();
    }
    else if (local_50 != (undefined ***)0x0) {
      lVar7 = 0x28;
      pppuVar5 = local_50;
      goto LAB_00a7de3c;
    }
    if ((local_88[0] & 1) != 0) {
      _ZdlPv(local_78);
    }
    if ((local_a0 & 1) != 0) {
      _ZdlPv((void *)CONCAT44(uStack_8c,uStack_90));
    }
  }
  else {
    if (iVar1 == 3) {
      uVar3 = FUN_0047acb4();
      if (*(long *)(lVar2 + 0x28) != local_38) goto LAB_00a7dedc;
      uVar6 = 0xb;
LAB_00a7dd4c:
      FUN_0047cd94(uVar3,uVar6,0);
      return;
    }
    if (iVar1 == 0) {
      *(undefined1 *)((long)&fde_table_entry_0033e360.initial_loc + lVar7) = 0;
      *(undefined1 *)((long)&fde_table_entry_0033e368.initial_loc + lVar7) = 0;
      uVar3 = FUN_0047acb4();
      if (*(long *)(lVar2 + 0x28) != local_38) goto LAB_00a7dedc;
      uVar6 = 10;
      goto LAB_00a7dd4c;
    }
  }
  if (*(long *)(lVar2 + 0x28) == local_38) {
    return;
  }
LAB_00a7dedc:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00a7dccc"></a> `00a7dccc` | `ff 83 02 d1` | sub sp,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-00a7dcd0"></a> `00a7dcd0` | `fd 7b 07 a9` | stp x29,x30,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00a7dcd4"></a> `00a7dcd4` | `f5 43 00 f9` | str x21,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00a7dcd8"></a> `00a7dcd8` | `f4 4f 09 a9` | stp x20,x19,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00a7dcdc"></a> `00a7dcdc` | `fd c3 01 91` | add x29,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00a7dce0"></a> `00a7dce0` | `54 d0 3b d5` | mrs x20,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00a7dce4"></a> `00a7dce4` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00a7dce8"></a> `00a7dce8` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00a7dcec"></a> `00a7dcec` | `48 00 40 b9` | ldr w8,[x2] | `FALL_THROUGH`
<a id="insn-00a7dcf0"></a> `00a7dcf0` | `13 04 40 f9` | ldr x19,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00a7dcf4"></a> `00a7dcf4` | `1f 11 00 71` | cmp w8,#0x4 | `FALL_THROUGH`
<a id="insn-00a7dcf8"></a> `00a7dcf8` | `60 03 00 54` | b.eq 0x00a7dd64 | `CONDITIONAL_JUMP`
<a id="insn-00a7dcfc"></a> `00a7dcfc` | `1f 0d 00 71` | cmp w8,#0x3 | `FALL_THROUGH`
<a id="insn-00a7dd00"></a> `00a7dd00` | `a0 01 00 54` | b.eq 0x00a7dd34 | `CONDITIONAL_JUMP`
<a id="insn-00a7dd04"></a> `00a7dd04` | `28 0b 00 35` | cbnz w8,0x00a7de68 | `CONDITIONAL_JUMP`
<a id="insn-00a7dd08"></a> `00a7dd08` | `68 fa 4c 91` | add x8,x19,#0x33e, LSL #12 | `FALL_THROUGH`
<a id="insn-00a7dd0c"></a> `00a7dd0c` | `08 81 0d 91` | add x8,x8,#0x360 | `FALL_THROUGH`
<a id="insn-00a7dd10"></a> `00a7dd10` | `1f 01 00 39` | strb wzr,[x8] | `FALL_THROUGH`
<a id="insn-00a7dd14"></a> `00a7dd14` | `1f 21 00 39` | strb wzr,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00a7dd18"></a> `00a7dd18` | `e7 f3 e7 97` | bl 0x0047acb4 | `UNCONDITIONAL_CALL`
<a id="insn-00a7dd1c"></a> `00a7dd1c` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00a7dd20"></a> `00a7dd20` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00a7dd24"></a> `00a7dd24` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00a7dd28"></a> `00a7dd28` | `a1 0d 00 54` | b.ne 0x00a7dedc | `CONDITIONAL_JUMP`
<a id="insn-00a7dd2c"></a> `00a7dd2c` | `41 01 80 52` | mov w1,#0xa | `FALL_THROUGH`
<a id="insn-00a7dd30"></a> `00a7dd30` | `07 00 00 14` | b 0x00a7dd4c | `UNCONDITIONAL_JUMP`
<a id="insn-00a7dd34"></a> `00a7dd34` | `e0 f3 e7 97` | bl 0x0047acb4 | `UNCONDITIONAL_CALL`
<a id="insn-00a7dd38"></a> `00a7dd38` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00a7dd3c"></a> `00a7dd3c` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00a7dd40"></a> `00a7dd40` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00a7dd44"></a> `00a7dd44` | `c1 0c 00 54` | b.ne 0x00a7dedc | `CONDITIONAL_JUMP`
<a id="insn-00a7dd48"></a> `00a7dd48` | `61 01 80 52` | mov w1,#0xb | `FALL_THROUGH`
<a id="insn-00a7dd4c"></a> `00a7dd4c` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00a7dd50"></a> `00a7dd50` | `f4 4f 49 a9` | ldp x20,x19,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00a7dd54"></a> `00a7dd54` | `f5 43 40 f9` | ldr x21,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00a7dd58"></a> `00a7dd58` | `fd 7b 47 a9` | ldp x29,x30,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00a7dd5c"></a> `00a7dd5c` | `ff 83 02 91` | add sp,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-00a7dd60"></a> `00a7dd60` | `0d fc e7 17` | b 0x0047cd94 | `CALL_TERMINATOR`
<a id="insn-00a7dd64"></a> `00a7dd64` | `2b 3c e8 97` | bl 0x0048ce10 | `UNCONDITIONAL_CALL`
<a id="insn-00a7dd68"></a> `00a7dd68` | `60 02 00 36` | tbz w0,#0x0,0x00a7ddb4 | `CONDITIONAL_JUMP`
<a id="insn-00a7dd6c"></a> `00a7dd6c` | `88 36 96 52` | mov w8,#0xb1b4 | `FALL_THROUGH`
<a id="insn-00a7dd70"></a> `00a7dd70` | `ea 05 80 52` | mov w10,#0x2f | `FALL_THROUGH`
<a id="insn-00a7dd74"></a> `00a7dd74` | `49 00 80 52` | mov w9,#0x2 | `FALL_THROUGH`
<a id="insn-00a7dd78"></a> `00a7dd78` | `28 07 a0 72` | movk w8,#0x39, LSL #16 | `FALL_THROUGH`
<a id="insn-00a7dd7c"></a> `00a7dd7c` | `6a 7a 34 b9` | str w10,[x19, #0x3478] | `FALL_THROUGH`
<a id="insn-00a7dd80"></a> `00a7dd80` | `69 6a 28 b8` | str w9,[x19, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00a7dd84"></a> `00a7dd84` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00a7dd88"></a> `00a7dd88` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00a7dd8c"></a> `00a7dd8c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00a7dd90"></a> `00a7dd90` | `61 0a 00 54` | b.ne 0x00a7dedc | `CONDITIONAL_JUMP`
<a id="insn-00a7dd94"></a> `00a7dd94` | `08 e7 85 52` | mov w8,#0x2f38 | `FALL_THROUGH`
<a id="insn-00a7dd98"></a> `00a7dd98` | `60 02 08 8b` | add x0,x19,x8 | `FALL_THROUGH`
<a id="insn-00a7dd9c"></a> `00a7dd9c` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00a7dda0"></a> `00a7dda0` | `f4 4f 49 a9` | ldp x20,x19,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00a7dda4"></a> `00a7dda4` | `f5 43 40 f9` | ldr x21,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00a7dda8"></a> `00a7dda8` | `fd 7b 47 a9` | ldp x29,x30,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00a7ddac"></a> `00a7ddac` | `ff 83 02 91` | add sp,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-00a7ddb0"></a> `00a7ddb0` | `07 e7 f8 17` | b 0x008b79cc | `CALL_TERMINATOR`
<a id="insn-00a7ddb4"></a> `00a7ddb4` | `a9 c1 ff f0` | adrp x9,0x2b4000 | `FALL_THROUGH`
<a id="insn-00a7ddb8"></a> `00a7ddb8` | `29 a9 2d 91` | add x9,x9,#0xb6a | `FALL_THROUGH`
<a id="insn-00a7ddbc"></a> `00a7ddbc` | `2a 4c 8c 52` | mov w10,#0x6261 | `FALL_THROUGH`
<a id="insn-00a7ddc0"></a> `00a7ddc0` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00a7ddc4"></a> `00a7ddc4` | `c8 04 80 52` | mov w8,#0x26 | `FALL_THROUGH`
<a id="insn-00a7ddc8"></a> `00a7ddc8` | `8a ad ac 72` | movk w10,#0x656c, LSL #16 | `FALL_THROUGH`
<a id="insn-00a7ddcc"></a> `00a7ddcc` | `e8 03 00 39` | strb w8,[sp] | `FALL_THROUGH`
<a id="insn-00a7ddd0"></a> `00a7ddd0` | `ea 13 00 b9` | str w10,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a7ddd4"></a> `00a7ddd4` | `e0 13 80 3c` | stur q0,[sp, #0x1] | `FALL_THROUGH`
<a id="insn-00a7ddd8"></a> `00a7ddd8` | `ff 53 00 39` | strb wzr,[sp, #0x14] | `FALL_THROUGH`
<a id="insn-00a7dddc"></a> `00a7dddc` | `e8 63 00 91` | add x8,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00a7dde0"></a> `00a7dde0` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00a7dde4"></a> `00a7dde4` | `0c 3c e8 97` | bl 0x0048ce14 | `UNCONDITIONAL_CALL`
<a id="insn-00a7dde8"></a> `00a7dde8` | `68 10 00 d0` | adrp x8,0xc8b000 | `FALL_THROUGH`
<a id="insn-00a7ddec"></a> `00a7ddec` | `08 41 2a 91` | add x8,x8,#0xa90 | `FALL_THROUGH`
<a id="insn-00a7ddf0"></a> `00a7ddf0` | `f5 c3 00 91` | add x21,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00a7ddf4"></a> `00a7ddf4` | `e8 1b 00 f9` | str x8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00a7ddf8"></a> `00a7ddf8` | `08 e1 85 52` | mov w8,#0x2f08 | `FALL_THROUGH`
<a id="insn-00a7ddfc"></a> `00a7ddfc` | `f5 2b 00 f9` | str x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00a7de00"></a> `00a7de00` | `60 02 08 8b` | add x0,x19,x8 | `FALL_THROUGH`
<a id="insn-00a7de04"></a> `00a7de04` | `e1 63 00 91` | add x1,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00a7de08"></a> `00a7de08` | `e5 c3 00 91` | add x5,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00a7de0c"></a> `00a7de0c` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-00a7de10"></a> `00a7de10` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-00a7de14"></a> `00a7de14` | `84 04 80 52` | mov w4,#0x24 | `FALL_THROUGH`
<a id="insn-00a7de18"></a> `00a7de18` | `83 f2 f8 97` | bl 0x008ba824 | `UNCONDITIONAL_CALL`
<a id="insn-00a7de1c"></a> `00a7de1c` | `e0 2b 40 f9` | ldr x0,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00a7de20"></a> `00a7de20` | `1f 00 15 eb` | cmp x0,x21 | `FALL_THROUGH`
<a id="insn-00a7de24"></a> `00a7de24` | `80 00 00 54` | b.eq 0x00a7de34 | `CONDITIONAL_JUMP`
<a id="insn-00a7de28"></a> `00a7de28` | `00 01 00 b4` | cbz x0,0x00a7de48 | `CONDITIONAL_JUMP`
<a id="insn-00a7de2c"></a> `00a7de2c` | `08 05 80 52` | mov w8,#0x28 | `FALL_THROUGH`
<a id="insn-00a7de30"></a> `00a7de30` | `03 00 00 14` | b 0x00a7de3c | `UNCONDITIONAL_JUMP`
<a id="insn-00a7de34"></a> `00a7de34` | `08 04 80 52` | mov w8,#0x20 | `FALL_THROUGH`
<a id="insn-00a7de38"></a> `00a7de38` | `e0 c3 00 91` | add x0,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00a7de3c"></a> `00a7de3c` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-00a7de40"></a> `00a7de40` | `28 69 68 f8` | ldr x8,[x9, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00a7de44"></a> `00a7de44` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00a7de48"></a> `00a7de48` | `e8 63 40 39` | ldrb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00a7de4c"></a> `00a7de4c` | `68 00 00 36` | tbz w8,#0x0,0x00a7de58 | `CONDITIONAL_JUMP`
<a id="insn-00a7de50"></a> `00a7de50` | `e0 17 40 f9` | ldr x0,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00a7de54"></a> `00a7de54` | `17 67 07 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00a7de58"></a> `00a7de58` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-00a7de5c"></a> `00a7de5c` | `68 00 00 36` | tbz w8,#0x0,0x00a7de68 | `CONDITIONAL_JUMP`
<a id="insn-00a7de60"></a> `00a7de60` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a7de64"></a> `00a7de64` | `13 67 07 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00a7de68"></a> `00a7de68` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00a7de6c"></a> `00a7de6c` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00a7de70"></a> `00a7de70` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00a7de74"></a> `00a7de74` | `41 03 00 54` | b.ne 0x00a7dedc | `CONDITIONAL_JUMP`
<a id="insn-00a7de78"></a> `00a7de78` | `f4 4f 49 a9` | ldp x20,x19,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00a7de7c"></a> `00a7de7c` | `f5 43 40 f9` | ldr x21,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00a7de80"></a> `00a7de80` | `fd 7b 47 a9` | ldp x29,x30,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00a7de84"></a> `00a7de84` | `ff 83 02 91` | add sp,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-00a7de88"></a> `00a7de88` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00a7dedc"></a> `00a7dedc` | `01 67 07 94` | bl 0x00c57ae0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00a7dccc`](#insn-00a7dccc) 範囲 `[['00a7dccc', '00a7dcfb']]`
  - `CONDITIONAL_JUMP` [`00a7dcf8`](#insn-00a7dcf8) → [`00a7dd64`](#insn-00a7dd64)
  - `FALL_THROUGH` [`00a7dcf8`](#insn-00a7dcf8) → [`00a7dcfc`](#insn-00a7dcfc)
- ブロック [`00a7dcfc`](#insn-00a7dcfc) 範囲 `[['00a7dcfc', '00a7dd03']]`
  - `CONDITIONAL_JUMP` [`00a7dd00`](#insn-00a7dd00) → [`00a7dd34`](#insn-00a7dd34)
  - `FALL_THROUGH` [`00a7dd00`](#insn-00a7dd00) → [`00a7dd04`](#insn-00a7dd04)
- ブロック [`00a7dd04`](#insn-00a7dd04) 範囲 `[['00a7dd04', '00a7dd07']]`
  - `CONDITIONAL_JUMP` [`00a7dd04`](#insn-00a7dd04) → [`00a7de68`](#insn-00a7de68)
  - `FALL_THROUGH` [`00a7dd04`](#insn-00a7dd04) → [`00a7dd08`](#insn-00a7dd08)
- ブロック [`00a7dd08`](#insn-00a7dd08) 範囲 `[['00a7dd08', '00a7dd2b']]`
  - `CONDITIONAL_JUMP` [`00a7dd28`](#insn-00a7dd28) → [`00a7dedc`](#insn-00a7dedc)
  - `FALL_THROUGH` [`00a7dd28`](#insn-00a7dd28) → [`00a7dd2c`](#insn-00a7dd2c)
- ブロック [`00a7dd2c`](#insn-00a7dd2c) 範囲 `[['00a7dd2c', '00a7dd33']]`
  - `UNCONDITIONAL_JUMP` [`00a7dd30`](#insn-00a7dd30) → [`00a7dd4c`](#insn-00a7dd4c)
- ブロック [`00a7dd34`](#insn-00a7dd34) 範囲 `[['00a7dd34', '00a7dd47']]`
  - `CONDITIONAL_JUMP` [`00a7dd44`](#insn-00a7dd44) → [`00a7dedc`](#insn-00a7dedc)
  - `FALL_THROUGH` [`00a7dd44`](#insn-00a7dd44) → [`00a7dd48`](#insn-00a7dd48)
- ブロック [`00a7dd48`](#insn-00a7dd48) 範囲 `[['00a7dd48', '00a7dd4b']]`
  - `FALL_THROUGH` [`00a7dd48`](#insn-00a7dd48) → [`00a7dd4c`](#insn-00a7dd4c)
- ブロック [`00a7dd4c`](#insn-00a7dd4c) 範囲 `[['00a7dd4c', '00a7dd63']]`
- ブロック [`00a7dd64`](#insn-00a7dd64) 範囲 `[['00a7dd64', '00a7dd6b']]`
  - `CONDITIONAL_JUMP` [`00a7dd68`](#insn-00a7dd68) → [`00a7ddb4`](#insn-00a7ddb4)
  - `FALL_THROUGH` [`00a7dd68`](#insn-00a7dd68) → [`00a7dd6c`](#insn-00a7dd6c)
- ブロック [`00a7dd6c`](#insn-00a7dd6c) 範囲 `[['00a7dd6c', '00a7dd93']]`
  - `CONDITIONAL_JUMP` [`00a7dd90`](#insn-00a7dd90) → [`00a7dedc`](#insn-00a7dedc)
  - `FALL_THROUGH` [`00a7dd90`](#insn-00a7dd90) → [`00a7dd94`](#insn-00a7dd94)
- ブロック [`00a7dd94`](#insn-00a7dd94) 範囲 `[['00a7dd94', '00a7ddb3']]`
- ブロック [`00a7ddb4`](#insn-00a7ddb4) 範囲 `[['00a7ddb4', '00a7de27']]`
  - `CONDITIONAL_JUMP` [`00a7de24`](#insn-00a7de24) → [`00a7de34`](#insn-00a7de34)
  - `FALL_THROUGH` [`00a7de24`](#insn-00a7de24) → [`00a7de28`](#insn-00a7de28)
- ブロック [`00a7de28`](#insn-00a7de28) 範囲 `[['00a7de28', '00a7de2b']]`
  - `CONDITIONAL_JUMP` [`00a7de28`](#insn-00a7de28) → [`00a7de48`](#insn-00a7de48)
  - `FALL_THROUGH` [`00a7de28`](#insn-00a7de28) → [`00a7de2c`](#insn-00a7de2c)
- ブロック [`00a7de2c`](#insn-00a7de2c) 範囲 `[['00a7de2c', '00a7de33']]`
  - `UNCONDITIONAL_JUMP` [`00a7de30`](#insn-00a7de30) → [`00a7de3c`](#insn-00a7de3c)
- ブロック [`00a7de34`](#insn-00a7de34) 範囲 `[['00a7de34', '00a7de3b']]`
  - `FALL_THROUGH` [`00a7de38`](#insn-00a7de38) → [`00a7de3c`](#insn-00a7de3c)
- ブロック [`00a7de3c`](#insn-00a7de3c) 範囲 `[['00a7de3c', '00a7de47']]`
  - `FALL_THROUGH` [`00a7de44`](#insn-00a7de44) → [`00a7de48`](#insn-00a7de48)
- ブロック [`00a7de48`](#insn-00a7de48) 範囲 `[['00a7de48', '00a7de4f']]`
  - `CONDITIONAL_JUMP` [`00a7de4c`](#insn-00a7de4c) → [`00a7de58`](#insn-00a7de58)
  - `FALL_THROUGH` [`00a7de4c`](#insn-00a7de4c) → [`00a7de50`](#insn-00a7de50)
- ブロック [`00a7de50`](#insn-00a7de50) 範囲 `[['00a7de50', '00a7de57']]`
  - `FALL_THROUGH` [`00a7de54`](#insn-00a7de54) → [`00a7de58`](#insn-00a7de58)
- ブロック [`00a7de58`](#insn-00a7de58) 範囲 `[['00a7de58', '00a7de5f']]`
  - `CONDITIONAL_JUMP` [`00a7de5c`](#insn-00a7de5c) → [`00a7de68`](#insn-00a7de68)
  - `FALL_THROUGH` [`00a7de5c`](#insn-00a7de5c) → [`00a7de60`](#insn-00a7de60)
- ブロック [`00a7de60`](#insn-00a7de60) 範囲 `[['00a7de60', '00a7de67']]`
  - `FALL_THROUGH` [`00a7de64`](#insn-00a7de64) → [`00a7de68`](#insn-00a7de68)
- ブロック [`00a7de68`](#insn-00a7de68) 範囲 `[['00a7de68', '00a7de77']]`
  - `CONDITIONAL_JUMP` [`00a7de74`](#insn-00a7de74) → [`00a7dedc`](#insn-00a7dedc)
  - `FALL_THROUGH` [`00a7de74`](#insn-00a7de74) → [`00a7de78`](#insn-00a7de78)
- ブロック [`00a7de78`](#insn-00a7de78) 範囲 `[['00a7de78', '00a7de8b']]`
- ブロック [`00a7dedc`](#insn-00a7dedc) 範囲 `[['00a7dedc', '00a7dedf']]`

## 命令位置別の参照

- [`00a7dcd0`](#insn-00a7dcd0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7dcd4`](#insn-00a7dcd4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7dcd8`](#insn-00a7dcd8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7dce8`](#insn-00a7dce8) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7dcf8`](#insn-00a7dcf8) → [`00a7dd64`](#insn-00a7dd64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7dd00`](#insn-00a7dd00) → [`00a7dd34`](#insn-00a7dd34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7dd04`](#insn-00a7dd04) → [`00a7de68`](#insn-00a7de68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7dd10`](#insn-00a7dd10) → `0033e360`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00a7dd14`](#insn-00a7dd14) → `0033e368`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00a7dd18`](#insn-00a7dd18) → [`0047acb4`](../0047a/0047acb4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047acb4` · 推定シンボル `None` · 推定型 `None`
- [`00a7dd20`](#insn-00a7dd20) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7dd28`](#insn-00a7dd28) → [`00a7dedc`](#insn-00a7dedc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7dd30`](#insn-00a7dd30) → [`00a7dd4c`](#insn-00a7dd4c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7dd34`](#insn-00a7dd34) → [`0047acb4`](../0047a/0047acb4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047acb4` · 推定シンボル `None` · 推定型 `None`
- [`00a7dd3c`](#insn-00a7dd3c) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7dd44`](#insn-00a7dd44) → [`00a7dedc`](#insn-00a7dedc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7dd50`](#insn-00a7dd50) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7dd54`](#insn-00a7dd54) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7dd58`](#insn-00a7dd58) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7dd60`](#insn-00a7dd60) → [`0047cd94`](../0047c/0047cd94.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047cd94` · 推定シンボル `None` · 推定型 `None`
- [`00a7dd64`](#insn-00a7dd64) → [`0048ce10`](../0048c/0048ce10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0048ce10` · 推定シンボル `None` · 推定型 `None`
- [`00a7dd68`](#insn-00a7dd68) → [`00a7ddb4`](#insn-00a7ddb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7dd80`](#insn-00a7dd80) → `0039b1b4`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `qword`
- [`00a7dd88`](#insn-00a7dd88) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7dd90`](#insn-00a7dd90) → [`00a7dedc`](#insn-00a7dedc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7dda0`](#insn-00a7dda0) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7dda4`](#insn-00a7dda4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7dda8`](#insn-00a7dda8) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7ddb0`](#insn-00a7ddb0) → [`008b79cc`](../008b7/008b79cc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b79cc` · 推定シンボル `None` · 推定型 `None`
- [`00a7ddc0`](#insn-00a7ddc0) → `002b4b6a`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00a7ddcc`](#insn-00a7ddcc) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7ddd0`](#insn-00a7ddd0) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7ddd4`](#insn-00a7ddd4) → `Stack[-0x9f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7ddd8`](#insn-00a7ddd8) → `Stack[-0x8c]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7dde4`](#insn-00a7dde4) → [`0048ce14`](../0048c/0048ce14.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0048ce14` · 推定シンボル `None` · 推定型 `None`
- [`00a7ddf4`](#insn-00a7ddf4) → `00c8ba90`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00a7ddf4`](#insn-00a7ddf4) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7ddfc`](#insn-00a7ddfc) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7de18`](#insn-00a7de18) → [`008ba824`](../008ba/008ba824.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008ba824` · 推定シンボル `None` · 推定型 `None`
- [`00a7de1c`](#insn-00a7de1c) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7de24`](#insn-00a7de24) → [`00a7de34`](#insn-00a7de34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7de28`](#insn-00a7de28) → [`00a7de48`](#insn-00a7de48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7de30`](#insn-00a7de30) → [`00a7de3c`](#insn-00a7de3c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7de3c`](#insn-00a7de3c) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7de40`](#insn-00a7de40) → `00c8bab0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00a7de40`](#insn-00a7de40) → `00c8bab8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00a7de44`](#insn-00a7de44) → [`00a7df80`](00a7df80.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00a7df80` · 推定シンボル `None` · 推定型 `None`
- [`00a7de44`](#insn-00a7de44) → [`00a7df84`](00a7df84.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00a7df84` · 推定シンボル `None` · 推定型 `None`
- [`00a7de48`](#insn-00a7de48) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7de4c`](#insn-00a7de4c) → [`00a7de58`](#insn-00a7de58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7de50`](#insn-00a7de50) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7de54`](#insn-00a7de54) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00a7de58`](#insn-00a7de58) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7de5c`](#insn-00a7de5c) → [`00a7de68`](#insn-00a7de68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7de60`](#insn-00a7de60) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7de64`](#insn-00a7de64) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00a7de6c`](#insn-00a7de6c) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7de74`](#insn-00a7de74) → [`00a7dedc`](#insn-00a7dedc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7de78`](#insn-00a7de78) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7de7c`](#insn-00a7de7c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7de80`](#insn-00a7de80) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7dedc`](#insn-00a7dedc) → [`00c57ae0`](../00c57/00c57ae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ae0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00a7dcd0`](#insn-00a7dcd0)

~~~json
{
  "source": "00a7dcd0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7dcd4`](#insn-00a7dcd4)

~~~json
{
  "source": "00a7dcd4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7dcd8`](#insn-00a7dcd8)

~~~json
{
  "source": "00a7dcd8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7dce8`](#insn-00a7dce8)

~~~json
{
  "source": "00a7dce8",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7dcf8`](#insn-00a7dcf8)

~~~json
{
  "source": "00a7dcf8",
  "target": "00a7dd64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7dd00`](#insn-00a7dd00)

~~~json
{
  "source": "00a7dd00",
  "target": "00a7dd34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7dd04`](#insn-00a7dd04)

~~~json
{
  "source": "00a7dd04",
  "target": "00a7de68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7dd10`](#insn-00a7dd10)

~~~json
{
  "source": "00a7dd10",
  "target": "0033e360",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0033e360",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "ec6d8b00a4d91100",
  "capture_start": "0033e360",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a7dd14`](#insn-00a7dd14)

~~~json
{
  "source": "00a7dd14",
  "target": "0033e368",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0033e368",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "486f8b00d4d91100",
  "capture_start": "0033e368",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a7dd18`](#insn-00a7dd18)

~~~json
{
  "source": "00a7dd18",
  "target": "0047acb4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a7dd20`](#insn-00a7dd20)

~~~json
{
  "source": "00a7dd20",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7dd28`](#insn-00a7dd28)

~~~json
{
  "source": "00a7dd28",
  "target": "00a7dedc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7dd30`](#insn-00a7dd30)

~~~json
{
  "source": "00a7dd30",
  "target": "00a7dd4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7dd34`](#insn-00a7dd34)

~~~json
{
  "source": "00a7dd34",
  "target": "0047acb4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a7dd3c`](#insn-00a7dd3c)

~~~json
{
  "source": "00a7dd3c",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7dd44`](#insn-00a7dd44)

~~~json
{
  "source": "00a7dd44",
  "target": "00a7dedc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7dd50`](#insn-00a7dd50)

~~~json
{
  "source": "00a7dd50",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7dd54`](#insn-00a7dd54)

~~~json
{
  "source": "00a7dd54",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7dd58`](#insn-00a7dd58)

~~~json
{
  "source": "00a7dd58",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7dd60`](#insn-00a7dd60)

~~~json
{
  "source": "00a7dd60",
  "target": "0047cd94",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a7dd64`](#insn-00a7dd64)

~~~json
{
  "source": "00a7dd64",
  "target": "0048ce10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a7dd68`](#insn-00a7dd68)

~~~json
{
  "source": "00a7dd68",
  "target": "00a7ddb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7dd80`](#insn-00a7dd80)

~~~json
{
  "source": "00a7dd80",
  "target": "0039b1b4",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0039b1b4",
  "offset": 0,
  "size": 8,
  "datatype": "qword",
  "bytes": "0c00000000000000",
  "capture_start": "0039b1b4",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a7dd88`](#insn-00a7dd88)

~~~json
{
  "source": "00a7dd88",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7dd90`](#insn-00a7dd90)

~~~json
{
  "source": "00a7dd90",
  "target": "00a7dedc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7dda0`](#insn-00a7dda0)

~~~json
{
  "source": "00a7dda0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7dda4`](#insn-00a7dda4)

~~~json
{
  "source": "00a7dda4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7dda8`](#insn-00a7dda8)

~~~json
{
  "source": "00a7dda8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7ddb0`](#insn-00a7ddb0)

~~~json
{
  "source": "00a7ddb0",
  "target": "008b79cc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a7ddc0`](#insn-00a7ddc0)

~~~json
{
  "source": "00a7ddc0",
  "target": "002b4b6a",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b4b6a",
  "offset": 0,
  "size": 20,
  "datatype": "string",
  "bytes": "6e6574776f726b5f756e617661696c61626c6500",
  "capture_start": "002b4b6a",
  "capture_bytes": 20,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a7ddcc`](#insn-00a7ddcc)

~~~json
{
  "source": "00a7ddcc",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7ddd0`](#insn-00a7ddd0)

~~~json
{
  "source": "00a7ddd0",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7ddd4`](#insn-00a7ddd4)

~~~json
{
  "source": "00a7ddd4",
  "target": "Stack[-0x9f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7ddd8`](#insn-00a7ddd8)

~~~json
{
  "source": "00a7ddd8",
  "target": "Stack[-0x8c]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7dde4`](#insn-00a7dde4)

~~~json
{
  "source": "00a7dde4",
  "target": "0048ce14",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a7ddf4`](#insn-00a7ddf4)

~~~json
{
  "source": "00a7ddf4",
  "target": "00c8ba90",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8ba90",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00a7ddf4`](#insn-00a7ddf4)

~~~json
{
  "source": "00a7ddf4",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7ddfc`](#insn-00a7ddfc)

~~~json
{
  "source": "00a7ddfc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7de18`](#insn-00a7de18)

~~~json
{
  "source": "00a7de18",
  "target": "008ba824",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a7de1c`](#insn-00a7de1c)

~~~json
{
  "source": "00a7de1c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7de24`](#insn-00a7de24)

~~~json
{
  "source": "00a7de24",
  "target": "00a7de34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7de28`](#insn-00a7de28)

~~~json
{
  "source": "00a7de28",
  "target": "00a7de48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7de30`](#insn-00a7de30)

~~~json
{
  "source": "00a7de30",
  "target": "00a7de3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7de3c`](#insn-00a7de3c)

~~~json
{
  "source": "00a7de3c",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7de40`](#insn-00a7de40)

~~~json
{
  "source": "00a7de40",
  "target": "00c8bab0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8bab0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00a7de40`](#insn-00a7de40)

~~~json
{
  "source": "00a7de40",
  "target": "00c8bab8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8bab8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00a7de44`](#insn-00a7de44)

~~~json
{
  "source": "00a7de44",
  "target": "00a7df80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a7de44`](#insn-00a7de44)

~~~json
{
  "source": "00a7de44",
  "target": "00a7df84",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a7de48`](#insn-00a7de48)

~~~json
{
  "source": "00a7de48",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7de4c`](#insn-00a7de4c)

~~~json
{
  "source": "00a7de4c",
  "target": "00a7de58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7de50`](#insn-00a7de50)

~~~json
{
  "source": "00a7de50",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7de54`](#insn-00a7de54)

~~~json
{
  "source": "00a7de54",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a7de58`](#insn-00a7de58)

~~~json
{
  "source": "00a7de58",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7de5c`](#insn-00a7de5c)

~~~json
{
  "source": "00a7de5c",
  "target": "00a7de68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7de60`](#insn-00a7de60)

~~~json
{
  "source": "00a7de60",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7de64`](#insn-00a7de64)

~~~json
{
  "source": "00a7de64",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a7de6c`](#insn-00a7de6c)

~~~json
{
  "source": "00a7de6c",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7de74`](#insn-00a7de74)

~~~json
{
  "source": "00a7de74",
  "target": "00a7dedc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7de78`](#insn-00a7de78)

~~~json
{
  "source": "00a7de78",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7de7c`](#insn-00a7de7c)

~~~json
{
  "source": "00a7de7c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7de80`](#insn-00a7de80)

~~~json
{
  "source": "00a7de80",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7dedc`](#insn-00a7dedc)

~~~json
{
  "source": "00a7dedc",
  "target": "00c57ae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
