# 00bfbda0

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b7f358`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f358.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/alignment_unresolved-0018.md#compare-810e4b2a534f7b897b4179091d1dead2)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bfc1c8`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfc1c8.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0086.md#compare-6b0e3917c926e767d484ffed57c37796)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfbda0",
  "name": "_ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE6sentryC1ERS3_b",
  "size": 452,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c28bee5ac4eab5e3005744132dccc7e909fe01ec43366ffaa5a27c1b495db617",
  "source_text_sha256": "c28bee5ac4eab5e3005744132dccc7e909fe01ec43366ffaa5a27c1b495db617",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfbda0",
        "00bfbf63"
      ]
    ],
    "bytes_sha256": "db4ac84eade7a351479016dec99f62c103b7fe9c25e65bdd8f846c6727e4434e",
    "instruction_count": 113,
    "instruction_bytes": 452,
    "body_bytes": 452,
    "indirect": 4,
    "unresolved": 4
  }
}
~~~

## 呼び出し元

- [00c599d0](../00c59/00c599d0.md)

## 呼び出し先

- [00c57e70](../00c57/00c57e70.md)
- [00c57e80](../00c57/00c57e80.md)
- [00c57e90](../00c57/00c57e90.md)
- [00c57ea0](../00c57/00c57ea0.md)
- [00c58af0](../00c58/00c58af0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2402 bytes

~~~c

void _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE6sentryC1ERS3_b
               (undefined1 *param_1,long *param_2,ulong param_3)

{
  byte bVar1;
  int iVar2;
  long lVar3;
  long lVar4;
  ulong uVar5;
  long *plVar6;
  undefined1 auStack_38 [8];
  
  lVar4 = *param_2;
  *param_1 = 0;
  lVar3 = (long)param_2 + *(long *)(lVar4 + -0x18);
  if (*(uint *)(lVar3 + 0x20) != 0) {
    _ZNSt6__ndk18ios_base5clearEj(lVar3,*(uint *)(lVar3 + 0x20) | 4);
    return;
  }
  if (*(long *)(lVar3 + 0x88) != 0) {
    param_3 = param_3 & 0xffffffff;
    _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEE5flushEv();
    lVar4 = *param_2;
  }
  if (((param_3 & 1) != 0) ||
     ((*(byte *)((long)param_2 + *(long *)(lVar4 + -0x18) + 9) >> 4 & 1) == 0)) {
LAB_00bfbf14:
    *param_1 = *(int *)((long)param_2 + *(long *)(lVar4 + -0x18) + 0x20) == 0;
    return;
  }
  _ZNKSt6__ndk18ios_base6getlocEv(auStack_38);
  lVar3 = _ZNKSt6__ndk16locale9use_facetERNS0_2idE
                    (auStack_38,PTR__ZNSt6__ndk15ctypeIcE2idE_00c9a830);
  _ZNSt6__ndk16localeD1Ev(auStack_38);
  plVar6 = *(long **)((long)param_2 + *(long *)(*param_2 + -0x18) + 0x28);
joined_r0x00bfbe54:
  if (plVar6 != (long *)0x0) {
    do {
      if ((plVar6[3] == plVar6[4]) && (iVar2 = (**(code **)(*plVar6 + 0x48))(plVar6), iVar2 == -1))
      break;
      if ((byte *)plVar6[3] == (byte *)plVar6[4]) {
        uVar5 = (**(code **)(*plVar6 + 0x48))(plVar6);
        uVar5 = uVar5 & 0xff;
        if ((uint)uVar5 >> 7 == 0) goto LAB_00bfbec4;
LAB_00bfbf04:
        if (plVar6[3] != plVar6[4]) goto LAB_00bfbf10;
        iVar2 = (**(code **)(*plVar6 + 0x48))(plVar6);
        lVar4 = *param_2;
        if (iVar2 != -1) goto LAB_00bfbf14;
        goto LAB_00bfbeec;
      }
      bVar1 = *(byte *)plVar6[3];
      uVar5 = (ulong)bVar1;
      if ((char)bVar1 < '\0') goto LAB_00bfbf04;
LAB_00bfbec4:
      if ((*(ulong *)(*(long *)(lVar3 + 0x10) + uVar5 * 8) & 1) == 0) goto LAB_00bfbf04;
      if (plVar6[3] != plVar6[4]) goto code_r0x00bfbedc;
      (**(code **)(*plVar6 + 0x50))(plVar6);
      if (plVar6 == (long *)0x0) break;
    } while( true );
  }
  lVar4 = *param_2;
LAB_00bfbeec:
  lVar3 = (long)param_2 + *(long *)(lVar4 + -0x18);
  _ZNSt6__ndk18ios_base5clearEj(lVar3,*(uint *)(lVar3 + 0x20) | 6);
LAB_00bfbf10:
  lVar4 = *param_2;
  goto LAB_00bfbf14;
code_r0x00bfbedc:
  plVar6[3] = plVar6[3] + 1;
  goto joined_r0x00bfbe54;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfbda0"></a> `00bfbda0` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfbda4"></a> `00bfbda4` | `ff 03 01 d1` | sub sp,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00bfbda8"></a> `00bfbda8` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfbdac"></a> `00bfbdac` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfbdb0"></a> `00bfbdb0` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bfbdb4"></a> `00bfbdb4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bfbdb8"></a> `00bfbdb8` | `28 00 40 f9` | ldr x8,[x1] | `FALL_THROUGH`
<a id="insn-00bfbdbc"></a> `00bfbdbc` | `1f 00 00 39` | strb wzr,[x0] | `FALL_THROUGH`
<a id="insn-00bfbdc0"></a> `00bfbdc0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bfbdc4"></a> `00bfbdc4` | `09 81 5e f8` | ldur x9,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfbdc8"></a> `00bfbdc8` | `20 00 09 8b` | add x0,x1,x9 | `FALL_THROUGH`
<a id="insn-00bfbdcc"></a> `00bfbdcc` | `09 20 40 b9` | ldr w9,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00bfbdd0"></a> `00bfbdd0` | `09 01 00 34` | cbz w9,0x00bfbdf0 | `CONDITIONAL_JUMP`
<a id="insn-00bfbdd4"></a> `00bfbdd4` | `21 01 1e 32` | orr w1,w9,#0x4 | `FALL_THROUGH`
<a id="insn-00bfbdd8"></a> `00bfbdd8` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bfbddc"></a> `00bfbddc` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfbde0"></a> `00bfbde0` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfbde4"></a> `00bfbde4` | `ff 03 01 91` | add sp,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00bfbde8"></a> `00bfbde8` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfbdec"></a> `00bfbdec` | `2d 70 01 14` | b 0x00c57ea0 | `CALL_TERMINATOR`
<a id="insn-00bfbdf0"></a> `00bfbdf0` | `00 44 40 f9` | ldr x0,[x0, #0x88] | `FALL_THROUGH`
<a id="insn-00bfbdf4"></a> `00bfbdf4` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00bfbdf8"></a> `00bfbdf8` | `a0 00 00 b4` | cbz x0,0x00bfbe0c | `CONDITIONAL_JUMP`
<a id="insn-00bfbdfc"></a> `00bfbdfc` | `f5 03 02 2a` | mov w21,w2 | `FALL_THROUGH`
<a id="insn-00bfbe00"></a> `00bfbe00` | `3c 73 01 94` | bl 0x00c58af0 | `UNCONDITIONAL_CALL`
<a id="insn-00bfbe04"></a> `00bfbe04` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bfbe08"></a> `00bfbe08` | `e2 03 15 2a` | mov w2,w21 | `FALL_THROUGH`
<a id="insn-00bfbe0c"></a> `00bfbe0c` | `42 08 00 37` | tbnz w2,#0x0,0x00bfbf14 | `CONDITIONAL_JUMP`
<a id="insn-00bfbe10"></a> `00bfbe10` | `09 81 5e f8` | ldur x9,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfbe14"></a> `00bfbe14` | `80 02 09 8b` | add x0,x20,x9 | `FALL_THROUGH`
<a id="insn-00bfbe18"></a> `00bfbe18` | `09 24 40 39` | ldrb w9,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00bfbe1c"></a> `00bfbe1c` | `c9 07 20 36` | tbz w9,#0x4,0x00bfbf14 | `CONDITIONAL_JUMP`
<a id="insn-00bfbe20"></a> `00bfbe20` | `e8 23 00 91` | add x8,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bfbe24"></a> `00bfbe24` | `13 70 01 94` | bl 0x00c57e70 | `UNCONDITIONAL_CALL`
<a id="insn-00bfbe28"></a> `00bfbe28` | `e1 04 00 f0` | adrp x1,0xc9a000 | `FALL_THROUGH`
<a id="insn-00bfbe2c"></a> `00bfbe2c` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bfbe30"></a> `00bfbe30` | `21 18 44 f9` | ldr x1,[x1, #0x830] | `FALL_THROUGH`
<a id="insn-00bfbe34"></a> `00bfbe34` | `13 70 01 94` | bl 0x00c57e80 | `UNCONDITIONAL_CALL`
<a id="insn-00bfbe38"></a> `00bfbe38` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bfbe3c"></a> `00bfbe3c` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bfbe40"></a> `00bfbe40` | `14 70 01 94` | bl 0x00c57e90 | `UNCONDITIONAL_CALL`
<a id="insn-00bfbe44"></a> `00bfbe44` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bfbe48"></a> `00bfbe48` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfbe4c"></a> `00bfbe4c` | `88 02 08 8b` | add x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00bfbe50"></a> `00bfbe50` | `16 15 40 f9` | ldr x22,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00bfbe54"></a> `00bfbe54` | `f6 00 00 b5` | cbnz x22,0x00bfbe70 | `CONDITIONAL_JUMP`
<a id="insn-00bfbe58"></a> `00bfbe58` | `24 00 00 14` | b 0x00bfbee8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bfbe5c"></a> `00bfbe5c` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00bfbe60"></a> `00bfbe60` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bfbe64"></a> `00bfbe64` | `08 29 40 f9` | ldr x8,[x8, #0x50] | `FALL_THROUGH`
<a id="insn-00bfbe68"></a> `00bfbe68` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bfbe6c"></a> `00bfbe6c` | `f6 03 00 b4` | cbz x22,0x00bfbee8 | `CONDITIONAL_JUMP`
<a id="insn-00bfbe70"></a> `00bfbe70` | `c8 a6 41 a9` | ldp x8,x9,[x22, #0x18] | `FALL_THROUGH`
<a id="insn-00bfbe74"></a> `00bfbe74` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bfbe78"></a> `00bfbe78` | `e1 00 00 54` | b.ne 0x00bfbe94 | `CONDITIONAL_JUMP`
<a id="insn-00bfbe7c"></a> `00bfbe7c` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00bfbe80"></a> `00bfbe80` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bfbe84"></a> `00bfbe84` | `08 25 40 f9` | ldr x8,[x8, #0x48] | `FALL_THROUGH`
<a id="insn-00bfbe88"></a> `00bfbe88` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bfbe8c"></a> `00bfbe8c` | `1f 04 00 31` | cmn w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bfbe90"></a> `00bfbe90` | `c0 02 00 54` | b.eq 0x00bfbee8 | `CONDITIONAL_JUMP`
<a id="insn-00bfbe94"></a> `00bfbe94` | `c8 a6 41 a9` | ldp x8,x9,[x22, #0x18] | `FALL_THROUGH`
<a id="insn-00bfbe98"></a> `00bfbe98` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bfbe9c"></a> `00bfbe9c` | `80 00 00 54` | b.eq 0x00bfbeac | `CONDITIONAL_JUMP`
<a id="insn-00bfbea0"></a> `00bfbea0` | `08 01 40 39` | ldrb w8,[x8] | `FALL_THROUGH`
<a id="insn-00bfbea4"></a> `00bfbea4` | `08 01 38 36` | tbz w8,#0x7,0x00bfbec4 | `CONDITIONAL_JUMP`
<a id="insn-00bfbea8"></a> `00bfbea8` | `17 00 00 14` | b 0x00bfbf04 | `UNCONDITIONAL_JUMP`
<a id="insn-00bfbeac"></a> `00bfbeac` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00bfbeb0"></a> `00bfbeb0` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bfbeb4"></a> `00bfbeb4` | `08 25 40 f9` | ldr x8,[x8, #0x48] | `FALL_THROUGH`
<a id="insn-00bfbeb8"></a> `00bfbeb8` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bfbebc"></a> `00bfbebc` | `08 1c 40 92` | and x8,x0,#0xff | `FALL_THROUGH`
<a id="insn-00bfbec0"></a> `00bfbec0` | `28 02 38 37` | tbnz w8,#0x7,0x00bfbf04 | `CONDITIONAL_JUMP`
<a id="insn-00bfbec4"></a> `00bfbec4` | `a9 0a 40 f9` | ldr x9,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-00bfbec8"></a> `00bfbec8` | `28 79 68 f8` | ldr x8,[x9, x8, LSL #0x3] | `FALL_THROUGH`
<a id="insn-00bfbecc"></a> `00bfbecc` | `c8 01 00 36` | tbz w8,#0x0,0x00bfbf04 | `CONDITIONAL_JUMP`
<a id="insn-00bfbed0"></a> `00bfbed0` | `c8 a6 41 a9` | ldp x8,x9,[x22, #0x18] | `FALL_THROUGH`
<a id="insn-00bfbed4"></a> `00bfbed4` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bfbed8"></a> `00bfbed8` | `20 fc ff 54` | b.eq 0x00bfbe5c | `CONDITIONAL_JUMP`
<a id="insn-00bfbedc"></a> `00bfbedc` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bfbee0"></a> `00bfbee0` | `c8 0e 00 f9` | str x8,[x22, #0x18] | `FALL_THROUGH`
<a id="insn-00bfbee4"></a> `00bfbee4` | `76 fc ff b5` | cbnz x22,0x00bfbe70 | `CONDITIONAL_JUMP`
<a id="insn-00bfbee8"></a> `00bfbee8` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bfbeec"></a> `00bfbeec` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfbef0"></a> `00bfbef0` | `80 02 08 8b` | add x0,x20,x8 | `FALL_THROUGH`
<a id="insn-00bfbef4"></a> `00bfbef4` | `08 20 40 b9` | ldr w8,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00bfbef8"></a> `00bfbef8` | `01 05 1f 32` | orr w1,w8,#0x6 | `FALL_THROUGH`
<a id="insn-00bfbefc"></a> `00bfbefc` | `e9 6f 01 94` | bl 0x00c57ea0 | `UNCONDITIONAL_CALL`
<a id="insn-00bfbf00"></a> `00bfbf00` | `04 00 00 14` | b 0x00bfbf10 | `UNCONDITIONAL_JUMP`
<a id="insn-00bfbf04"></a> `00bfbf04` | `c8 a6 41 a9` | ldp x8,x9,[x22, #0x18] | `FALL_THROUGH`
<a id="insn-00bfbf08"></a> `00bfbf08` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bfbf0c"></a> `00bfbf0c` | `c0 01 00 54` | b.eq 0x00bfbf44 | `CONDITIONAL_JUMP`
<a id="insn-00bfbf10"></a> `00bfbf10` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bfbf14"></a> `00bfbf14` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfbf18"></a> `00bfbf18` | `88 02 08 8b` | add x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00bfbf1c"></a> `00bfbf1c` | `08 21 40 b9` | ldr w8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00bfbf20"></a> `00bfbf20` | `1f 01 00 71` | cmp w8,#0x0 | `FALL_THROUGH`
<a id="insn-00bfbf24"></a> `00bfbf24` | `e8 17 9f 1a` | cset w8,eq | `FALL_THROUGH`
<a id="insn-00bfbf28"></a> `00bfbf28` | `68 02 00 39` | strb w8,[x19] | `FALL_THROUGH`
<a id="insn-00bfbf2c"></a> `00bfbf2c` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bfbf30"></a> `00bfbf30` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfbf34"></a> `00bfbf34` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfbf38"></a> `00bfbf38` | `ff 03 01 91` | add sp,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00bfbf3c"></a> `00bfbf3c` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfbf40"></a> `00bfbf40` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bfbf44"></a> `00bfbf44` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00bfbf48"></a> `00bfbf48` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bfbf4c"></a> `00bfbf4c` | `08 25 40 f9` | ldr x8,[x8, #0x48] | `FALL_THROUGH`
<a id="insn-00bfbf50"></a> `00bfbf50` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bfbf54"></a> `00bfbf54` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bfbf58"></a> `00bfbf58` | `1f 04 00 31` | cmn w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bfbf5c"></a> `00bfbf5c` | `c1 fd ff 54` | b.ne 0x00bfbf14 | `CONDITIONAL_JUMP`
<a id="insn-00bfbf60"></a> `00bfbf60` | `e3 ff ff 17` | b 0x00bfbeec | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00bfbda0`](#insn-00bfbda0) 範囲 `[['00bfbda0', '00bfbdd3']]`
  - `CONDITIONAL_JUMP` [`00bfbdd0`](#insn-00bfbdd0) → [`00bfbdf0`](#insn-00bfbdf0)
  - `FALL_THROUGH` [`00bfbdd0`](#insn-00bfbdd0) → [`00bfbdd4`](#insn-00bfbdd4)
- ブロック [`00bfbdd4`](#insn-00bfbdd4) 範囲 `[['00bfbdd4', '00bfbdef']]`
- ブロック [`00bfbdf0`](#insn-00bfbdf0) 範囲 `[['00bfbdf0', '00bfbdfb']]`
  - `CONDITIONAL_JUMP` [`00bfbdf8`](#insn-00bfbdf8) → [`00bfbe0c`](#insn-00bfbe0c)
  - `FALL_THROUGH` [`00bfbdf8`](#insn-00bfbdf8) → [`00bfbdfc`](#insn-00bfbdfc)
- ブロック [`00bfbdfc`](#insn-00bfbdfc) 範囲 `[['00bfbdfc', '00bfbe0b']]`
  - `FALL_THROUGH` [`00bfbe08`](#insn-00bfbe08) → [`00bfbe0c`](#insn-00bfbe0c)
- ブロック [`00bfbe0c`](#insn-00bfbe0c) 範囲 `[['00bfbe0c', '00bfbe0f']]`
  - `CONDITIONAL_JUMP` [`00bfbe0c`](#insn-00bfbe0c) → [`00bfbf14`](#insn-00bfbf14)
  - `FALL_THROUGH` [`00bfbe0c`](#insn-00bfbe0c) → [`00bfbe10`](#insn-00bfbe10)
- ブロック [`00bfbe10`](#insn-00bfbe10) 範囲 `[['00bfbe10', '00bfbe1f']]`
  - `CONDITIONAL_JUMP` [`00bfbe1c`](#insn-00bfbe1c) → [`00bfbf14`](#insn-00bfbf14)
  - `FALL_THROUGH` [`00bfbe1c`](#insn-00bfbe1c) → [`00bfbe20`](#insn-00bfbe20)
- ブロック [`00bfbe20`](#insn-00bfbe20) 範囲 `[['00bfbe20', '00bfbe57']]`
  - `CONDITIONAL_JUMP` [`00bfbe54`](#insn-00bfbe54) → [`00bfbe70`](#insn-00bfbe70)
  - `FALL_THROUGH` [`00bfbe54`](#insn-00bfbe54) → [`00bfbe58`](#insn-00bfbe58)
- ブロック [`00bfbe58`](#insn-00bfbe58) 範囲 `[['00bfbe58', '00bfbe5b']]`
  - `UNCONDITIONAL_JUMP` [`00bfbe58`](#insn-00bfbe58) → [`00bfbee8`](#insn-00bfbee8)
- ブロック [`00bfbe5c`](#insn-00bfbe5c) 範囲 `[['00bfbe5c', '00bfbe6f']]`
  - `CONDITIONAL_JUMP` [`00bfbe6c`](#insn-00bfbe6c) → [`00bfbee8`](#insn-00bfbee8)
  - `FALL_THROUGH` [`00bfbe6c`](#insn-00bfbe6c) → [`00bfbe70`](#insn-00bfbe70)
- ブロック [`00bfbe70`](#insn-00bfbe70) 範囲 `[['00bfbe70', '00bfbe7b']]`
  - `CONDITIONAL_JUMP` [`00bfbe78`](#insn-00bfbe78) → [`00bfbe94`](#insn-00bfbe94)
  - `FALL_THROUGH` [`00bfbe78`](#insn-00bfbe78) → [`00bfbe7c`](#insn-00bfbe7c)
- ブロック [`00bfbe7c`](#insn-00bfbe7c) 範囲 `[['00bfbe7c', '00bfbe93']]`
  - `CONDITIONAL_JUMP` [`00bfbe90`](#insn-00bfbe90) → [`00bfbee8`](#insn-00bfbee8)
  - `FALL_THROUGH` [`00bfbe90`](#insn-00bfbe90) → [`00bfbe94`](#insn-00bfbe94)
- ブロック [`00bfbe94`](#insn-00bfbe94) 範囲 `[['00bfbe94', '00bfbe9f']]`
  - `CONDITIONAL_JUMP` [`00bfbe9c`](#insn-00bfbe9c) → [`00bfbeac`](#insn-00bfbeac)
  - `FALL_THROUGH` [`00bfbe9c`](#insn-00bfbe9c) → [`00bfbea0`](#insn-00bfbea0)
- ブロック [`00bfbea0`](#insn-00bfbea0) 範囲 `[['00bfbea0', '00bfbea7']]`
  - `CONDITIONAL_JUMP` [`00bfbea4`](#insn-00bfbea4) → [`00bfbec4`](#insn-00bfbec4)
  - `FALL_THROUGH` [`00bfbea4`](#insn-00bfbea4) → [`00bfbea8`](#insn-00bfbea8)
- ブロック [`00bfbea8`](#insn-00bfbea8) 範囲 `[['00bfbea8', '00bfbeab']]`
  - `UNCONDITIONAL_JUMP` [`00bfbea8`](#insn-00bfbea8) → [`00bfbf04`](#insn-00bfbf04)
- ブロック [`00bfbeac`](#insn-00bfbeac) 範囲 `[['00bfbeac', '00bfbec3']]`
  - `CONDITIONAL_JUMP` [`00bfbec0`](#insn-00bfbec0) → [`00bfbf04`](#insn-00bfbf04)
  - `FALL_THROUGH` [`00bfbec0`](#insn-00bfbec0) → [`00bfbec4`](#insn-00bfbec4)
- ブロック [`00bfbec4`](#insn-00bfbec4) 範囲 `[['00bfbec4', '00bfbecf']]`
  - `CONDITIONAL_JUMP` [`00bfbecc`](#insn-00bfbecc) → [`00bfbf04`](#insn-00bfbf04)
  - `FALL_THROUGH` [`00bfbecc`](#insn-00bfbecc) → [`00bfbed0`](#insn-00bfbed0)
- ブロック [`00bfbed0`](#insn-00bfbed0) 範囲 `[['00bfbed0', '00bfbedb']]`
  - `CONDITIONAL_JUMP` [`00bfbed8`](#insn-00bfbed8) → [`00bfbe5c`](#insn-00bfbe5c)
  - `FALL_THROUGH` [`00bfbed8`](#insn-00bfbed8) → [`00bfbedc`](#insn-00bfbedc)
- ブロック [`00bfbedc`](#insn-00bfbedc) 範囲 `[['00bfbedc', '00bfbee7']]`
  - `CONDITIONAL_JUMP` [`00bfbee4`](#insn-00bfbee4) → [`00bfbe70`](#insn-00bfbe70)
  - `FALL_THROUGH` [`00bfbee4`](#insn-00bfbee4) → [`00bfbee8`](#insn-00bfbee8)
- ブロック [`00bfbee8`](#insn-00bfbee8) 範囲 `[['00bfbee8', '00bfbeeb']]`
  - `FALL_THROUGH` [`00bfbee8`](#insn-00bfbee8) → [`00bfbeec`](#insn-00bfbeec)
- ブロック [`00bfbeec`](#insn-00bfbeec) 範囲 `[['00bfbeec', '00bfbf03']]`
  - `UNCONDITIONAL_JUMP` [`00bfbf00`](#insn-00bfbf00) → [`00bfbf10`](#insn-00bfbf10)
- ブロック [`00bfbf04`](#insn-00bfbf04) 範囲 `[['00bfbf04', '00bfbf0f']]`
  - `CONDITIONAL_JUMP` [`00bfbf0c`](#insn-00bfbf0c) → [`00bfbf44`](#insn-00bfbf44)
  - `FALL_THROUGH` [`00bfbf0c`](#insn-00bfbf0c) → [`00bfbf10`](#insn-00bfbf10)
- ブロック [`00bfbf10`](#insn-00bfbf10) 範囲 `[['00bfbf10', '00bfbf13']]`
  - `FALL_THROUGH` [`00bfbf10`](#insn-00bfbf10) → [`00bfbf14`](#insn-00bfbf14)
- ブロック [`00bfbf14`](#insn-00bfbf14) 範囲 `[['00bfbf14', '00bfbf43']]`
- ブロック [`00bfbf44`](#insn-00bfbf44) 範囲 `[['00bfbf44', '00bfbf5f']]`
  - `CONDITIONAL_JUMP` [`00bfbf5c`](#insn-00bfbf5c) → [`00bfbf14`](#insn-00bfbf14)
  - `FALL_THROUGH` [`00bfbf5c`](#insn-00bfbf5c) → [`00bfbf60`](#insn-00bfbf60)
- ブロック [`00bfbf60`](#insn-00bfbf60) 範囲 `[['00bfbf60', '00bfbf63']]`
  - `UNCONDITIONAL_JUMP` [`00bfbf60`](#insn-00bfbf60) → [`00bfbeec`](#insn-00bfbeec)

## 命令位置別の参照

- [`00bfbda8`](#insn-00bfbda8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbdac`](#insn-00bfbdac) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbdb0`](#insn-00bfbdb0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbdd0`](#insn-00bfbdd0) → [`00bfbdf0`](#insn-00bfbdf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbdd8`](#insn-00bfbdd8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbddc`](#insn-00bfbddc) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbde0`](#insn-00bfbde0) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbdec`](#insn-00bfbdec) → [`00c57ea0`](../00c57/00c57ea0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ea0` · 推定シンボル `None` · 推定型 `None`
- [`00bfbdf8`](#insn-00bfbdf8) → [`00bfbe0c`](#insn-00bfbe0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbe00`](#insn-00bfbe00) → [`00c58af0`](../00c58/00c58af0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58af0` · 推定シンボル `None` · 推定型 `None`
- [`00bfbe0c`](#insn-00bfbe0c) → [`00bfbf14`](#insn-00bfbf14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbe1c`](#insn-00bfbe1c) → [`00bfbf14`](#insn-00bfbf14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbe24`](#insn-00bfbe24) → [`00c57e70`](../00c57/00c57e70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e70` · 推定シンボル `None` · 推定型 `None`
- [`00bfbe30`](#insn-00bfbe30) → `00c9a830`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bfbe30`](#insn-00bfbe30) → `01127a18`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZNSt6__ndk15ctypeIcE2idE` · 推定型 `undefined8`
- [`00bfbe34`](#insn-00bfbe34) → [`00c57e80`](../00c57/00c57e80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e80` · 推定シンボル `None` · 推定型 `None`
- [`00bfbe40`](#insn-00bfbe40) → [`00c57e90`](../00c57/00c57e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e90` · 推定シンボル `None` · 推定型 `None`
- [`00bfbe54`](#insn-00bfbe54) → [`00bfbe70`](#insn-00bfbe70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbe58`](#insn-00bfbe58) → [`00bfbee8`](#insn-00bfbee8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbe6c`](#insn-00bfbe6c) → [`00bfbee8`](#insn-00bfbee8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbe78`](#insn-00bfbe78) → [`00bfbe94`](#insn-00bfbe94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbe90`](#insn-00bfbe90) → [`00bfbee8`](#insn-00bfbee8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbe9c`](#insn-00bfbe9c) → [`00bfbeac`](#insn-00bfbeac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbea4`](#insn-00bfbea4) → [`00bfbec4`](#insn-00bfbec4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbea8`](#insn-00bfbea8) → [`00bfbf04`](#insn-00bfbf04) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbec0`](#insn-00bfbec0) → [`00bfbf04`](#insn-00bfbf04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbecc`](#insn-00bfbecc) → [`00bfbf04`](#insn-00bfbf04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbed8`](#insn-00bfbed8) → [`00bfbe5c`](#insn-00bfbe5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbee4`](#insn-00bfbee4) → [`00bfbe70`](#insn-00bfbe70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbefc`](#insn-00bfbefc) → [`00c57ea0`](../00c57/00c57ea0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ea0` · 推定シンボル `None` · 推定型 `None`
- [`00bfbf00`](#insn-00bfbf00) → [`00bfbf10`](#insn-00bfbf10) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbf0c`](#insn-00bfbf0c) → [`00bfbf44`](#insn-00bfbf44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbf2c`](#insn-00bfbf2c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbf30`](#insn-00bfbf30) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbf34`](#insn-00bfbf34) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbf5c`](#insn-00bfbf5c) → [`00bfbf14`](#insn-00bfbf14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbf60`](#insn-00bfbf60) → [`00bfbeec`](#insn-00bfbeec) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfbda8`](#insn-00bfbda8)

~~~json
{
  "source": "00bfbda8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbdac`](#insn-00bfbdac)

~~~json
{
  "source": "00bfbdac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbdb0`](#insn-00bfbdb0)

~~~json
{
  "source": "00bfbdb0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbdd0`](#insn-00bfbdd0)

~~~json
{
  "source": "00bfbdd0",
  "target": "00bfbdf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbdd8`](#insn-00bfbdd8)

~~~json
{
  "source": "00bfbdd8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbddc`](#insn-00bfbddc)

~~~json
{
  "source": "00bfbddc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbde0`](#insn-00bfbde0)

~~~json
{
  "source": "00bfbde0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbdec`](#insn-00bfbdec)

~~~json
{
  "source": "00bfbdec",
  "target": "00c57ea0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfbdf8`](#insn-00bfbdf8)

~~~json
{
  "source": "00bfbdf8",
  "target": "00bfbe0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbe00`](#insn-00bfbe00)

~~~json
{
  "source": "00bfbe00",
  "target": "00c58af0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfbe0c`](#insn-00bfbe0c)

~~~json
{
  "source": "00bfbe0c",
  "target": "00bfbf14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbe1c`](#insn-00bfbe1c)

~~~json
{
  "source": "00bfbe1c",
  "target": "00bfbf14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbe24`](#insn-00bfbe24)

~~~json
{
  "source": "00bfbe24",
  "target": "00c57e70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfbe30`](#insn-00bfbe30)

~~~json
{
  "source": "00bfbe30",
  "target": "00c9a830",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9a830",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bfbe30`](#insn-00bfbe30)

~~~json
{
  "source": "00bfbe30",
  "target": "01127a18",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127a18",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bfbe34`](#insn-00bfbe34)

~~~json
{
  "source": "00bfbe34",
  "target": "00c57e80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfbe40`](#insn-00bfbe40)

~~~json
{
  "source": "00bfbe40",
  "target": "00c57e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfbe54`](#insn-00bfbe54)

~~~json
{
  "source": "00bfbe54",
  "target": "00bfbe70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbe58`](#insn-00bfbe58)

~~~json
{
  "source": "00bfbe58",
  "target": "00bfbee8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbe6c`](#insn-00bfbe6c)

~~~json
{
  "source": "00bfbe6c",
  "target": "00bfbee8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbe78`](#insn-00bfbe78)

~~~json
{
  "source": "00bfbe78",
  "target": "00bfbe94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbe90`](#insn-00bfbe90)

~~~json
{
  "source": "00bfbe90",
  "target": "00bfbee8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbe9c`](#insn-00bfbe9c)

~~~json
{
  "source": "00bfbe9c",
  "target": "00bfbeac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbea4`](#insn-00bfbea4)

~~~json
{
  "source": "00bfbea4",
  "target": "00bfbec4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbea8`](#insn-00bfbea8)

~~~json
{
  "source": "00bfbea8",
  "target": "00bfbf04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbec0`](#insn-00bfbec0)

~~~json
{
  "source": "00bfbec0",
  "target": "00bfbf04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbecc`](#insn-00bfbecc)

~~~json
{
  "source": "00bfbecc",
  "target": "00bfbf04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbed8`](#insn-00bfbed8)

~~~json
{
  "source": "00bfbed8",
  "target": "00bfbe5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbee4`](#insn-00bfbee4)

~~~json
{
  "source": "00bfbee4",
  "target": "00bfbe70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbefc`](#insn-00bfbefc)

~~~json
{
  "source": "00bfbefc",
  "target": "00c57ea0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfbf00`](#insn-00bfbf00)

~~~json
{
  "source": "00bfbf00",
  "target": "00bfbf10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbf0c`](#insn-00bfbf0c)

~~~json
{
  "source": "00bfbf0c",
  "target": "00bfbf44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbf2c`](#insn-00bfbf2c)

~~~json
{
  "source": "00bfbf2c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbf30`](#insn-00bfbf30)

~~~json
{
  "source": "00bfbf30",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbf34`](#insn-00bfbf34)

~~~json
{
  "source": "00bfbf34",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbf5c`](#insn-00bfbf5c)

~~~json
{
  "source": "00bfbf5c",
  "target": "00bfbf14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbf60`](#insn-00bfbf60)

~~~json
{
  "source": "00bfbf60",
  "target": "00bfbeec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
