# 00affc2c

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0170.md#review-6813feb9752f686b7fc70669567f09da)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00b00054`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b00/00b00054.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0066.md#compare-b7dc1ddc20a1fa28ea331af4e776ec5b)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

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
  "source_text_sha256": "e1c5a772ea04b27de27098d230661cb1e53102c7bc7d61a671572c8c8e5d1d1d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00affc2c",
        "00afff53"
      ]
    ],
    "bytes_sha256": "7a05d21fbecf5fe3b066824513c998e931bb9ac6c017bf88ed39e61e3fcf0072",
    "instruction_count": 202,
    "instruction_bytes": 808,
    "body_bytes": 808,
    "indirect": 0,
    "unresolved": 0
  }
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

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

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

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00affc2c"></a> `00affc2c` | `ff c3 01 d1` | sub sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00affc30"></a> `00affc30` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00affc34"></a> `00affc34` | `f9 1b 00 f9` | str x25,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00affc38"></a> `00affc38` | `f8 5f 04 a9` | stp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00affc3c"></a> `00affc3c` | `f6 57 05 a9` | stp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00affc40"></a> `00affc40` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00affc44"></a> `00affc44` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00affc48"></a> `00affc48` | `58 d0 3b d5` | mrs x24,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00affc4c"></a> `00affc4c` | `f6 03 03 2a` | mov w22,w3 | `FALL_THROUGH`
<a id="insn-00affc50"></a> `00affc50` | `f4 03 02 2a` | mov w20,w2 | `FALL_THROUGH`
<a id="insn-00affc54"></a> `00affc54` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00affc58"></a> `00affc58` | `f5 03 01 2a` | mov w21,w1 | `FALL_THROUGH`
<a id="insn-00affc5c"></a> `00affc5c` | `f3 03 00 2a` | mov w19,w0 | `FALL_THROUGH`
<a id="insn-00affc60"></a> `00affc60` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00affc64"></a> `00affc64` | `22 02 00 36` | tbz w2,#0x0,0x00affca8 | `CONDITIONAL_JUMP`
<a id="insn-00affc68"></a> `00affc68` | `14 46 f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00affc6c"></a> `00affc6c` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00affc70"></a> `00affc70` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00affc74"></a> `00affc74` | `a9 0b f4 97` | bl 0x00802b18 | `UNCONDITIONAL_CALL`
<a id="insn-00affc78"></a> `00affc78` | `e1 03 00 2a` | mov w1,w0 | `FALL_THROUGH`
<a id="insn-00affc7c"></a> `00affc7c` | `e0 e2 1d 91` | add x0,x23,#0x778 | `FALL_THROUGH`
<a id="insn-00affc80"></a> `00affc80` | `82 00 80 52` | mov w2,#0x4 | `FALL_THROUGH`
<a id="insn-00affc84"></a> `00affc84` | `56 aa ed 97` | bl 0x0066a5dc | `UNCONDITIONAL_CALL`
<a id="insn-00affc88"></a> `00affc88` | `00 01 00 b4` | cbz x0,0x00affca8 | `CONDITIONAL_JUMP`
<a id="insn-00affc8c"></a> `00affc8c` | `08 24 40 a9` | ldp x8,x9,[x0] | `FALL_THROUGH`
<a id="insn-00affc90"></a> `00affc90` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00affc94"></a> `00affc94` | `80 14 00 54` | b.eq 0x00afff24 | `CONDITIONAL_JUMP`
<a id="insn-00affc98"></a> `00affc98` | `08 01 40 b9` | ldr w8,[x8] | `FALL_THROUGH`
<a id="insn-00affc9c"></a> `00affc9c` | `89 0c 80 52` | mov w9,#0x64 | `FALL_THROUGH`
<a id="insn-00affca0"></a> `00affca0` | `00 7d 09 1b` | mul w0,w8,w9 | `FALL_THROUGH`
<a id="insn-00affca4"></a> `00affca4` | `95 00 00 14` | b 0x00affef8 | `UNCONDITIONAL_JUMP`
<a id="insn-00affca8"></a> `00affca8` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00affcac"></a> `00affcac` | `e1 03 13 2a` | mov w1,w19 | `FALL_THROUGH`
<a id="insn-00affcb0"></a> `00affcb0` | `e2 03 15 2a` | mov w2,w21 | `FALL_THROUGH`
<a id="insn-00affcb4"></a> `00affcb4` | `a2 ff ff 97` | bl 0x00affb3c | `UNCONDITIONAL_CALL`
<a id="insn-00affcb8"></a> `00affcb8` | `e8 a3 90 52` | mov w8,#0x851f | `FALL_THROUGH`
<a id="insn-00affcbc"></a> `00affcbc` | `68 3d aa 72` | movk w8,#0x51eb, LSL #16 | `FALL_THROUGH`
<a id="insn-00affcc0"></a> `00affcc0` | `08 7c 28 9b` | smull x8,w0,w8 | `FALL_THROUGH`
<a id="insn-00affcc4"></a> `00affcc4` | `09 fd 7f d3` | lsr x9,x8,#0x3f | `FALL_THROUGH`
<a id="insn-00affcc8"></a> `00affcc8` | `08 fd 65 93` | asr x8,x8,#0x25 | `FALL_THROUGH`
<a id="insn-00affccc"></a> `00affccc` | `17 01 09 0b` | add w23,w8,w9 | `FALL_THROUGH`
<a id="insn-00affcd0"></a> `00affcd0` | `fa 45 f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00affcd4"></a> `00affcd4` | `08 7f 87 52` | mov w8,#0x3bf8 | `FALL_THROUGH`
<a id="insn-00affcd8"></a> `00affcd8` | `89 0c 80 52` | mov w9,#0x64 | `FALL_THROUGH`
<a id="insn-00affcdc"></a> `00affcdc` | `28 07 a0 72` | movk w8,#0x39, LSL #16 | `FALL_THROUGH`
<a id="insn-00affce0"></a> `00affce0` | `08 68 68 b8` | ldr w8,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00affce4"></a> `00affce4` | `08 09 00 11` | add w8,w8,#0x2 | `FALL_THROUGH`
<a id="insn-00affce8"></a> `00affce8` | `08 7d 17 1b` | mul w8,w8,w23 | `FALL_THROUGH`
<a id="insn-00affcec"></a> `00affcec` | `1f 01 00 71` | cmp w8,#0x0 | `FALL_THROUGH`
<a id="insn-00affcf0"></a> `00affcf0` | `08 a5 88 1a` | cinc w8,w8,lt | `FALL_THROUGH`
<a id="insn-00affcf4"></a> `00affcf4` | `08 7d 01 13` | asr w8,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00affcf8"></a> `00affcf8` | `19 7d 09 1b` | mul w25,w8,w9 | `FALL_THROUGH`
<a id="insn-00affcfc"></a> `00affcfc` | `b4 03 00 36` | tbz w20,#0x0,0x00affd70 | `CONDITIONAL_JUMP`
<a id="insn-00affd00"></a> `00affd00` | `ee 45 f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00affd04"></a> `00affd04` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00affd08"></a> `00affd08` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00affd0c"></a> `00affd0c` | `83 0b f4 97` | bl 0x00802b18 | `UNCONDITIONAL_CALL`
<a id="insn-00affd10"></a> `00affd10` | `e8 de 4c 91` | add x8,x23,#0x337, LSL #12 | `FALL_THROUGH`
<a id="insn-00affd14"></a> `00affd14` | `e1 03 00 2a` | mov w1,w0 | `FALL_THROUGH`
<a id="insn-00affd18"></a> `00affd18` | `00 41 0c 91` | add x0,x8,#0x310 | `FALL_THROUGH`
<a id="insn-00affd1c"></a> `00affd1c` | `f6 09 f4 97` | bl 0x008024f4 | `UNCONDITIONAL_CALL`
<a id="insn-00affd20"></a> `00affd20` | `80 02 00 34` | cbz w0,0x00affd70 | `CONDITIONAL_JUMP`
<a id="insn-00affd24"></a> `00affd24` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00affd28"></a> `00affd28` | `e1 03 13 2a` | mov w1,w19 | `FALL_THROUGH`
<a id="insn-00affd2c"></a> `00affd2c` | `e2 03 15 2a` | mov w2,w21 | `FALL_THROUGH`
<a id="insn-00affd30"></a> `00affd30` | `83 ff ff 97` | bl 0x00affb3c | `UNCONDITIONAL_CALL`
<a id="insn-00affd34"></a> `00affd34` | `e8 a3 90 52` | mov w8,#0x851f | `FALL_THROUGH`
<a id="insn-00affd38"></a> `00affd38` | `68 3d aa 72` | movk w8,#0x51eb, LSL #16 | `FALL_THROUGH`
<a id="insn-00affd3c"></a> `00affd3c` | `08 7c 28 9b` | smull x8,w0,w8 | `FALL_THROUGH`
<a id="insn-00affd40"></a> `00affd40` | `09 fd 7f d3` | lsr x9,x8,#0x3f | `FALL_THROUGH`
<a id="insn-00affd44"></a> `00affd44` | `08 fd 65 93` | asr x8,x8,#0x25 | `FALL_THROUGH`
<a id="insn-00affd48"></a> `00affd48` | `19 01 09 0b` | add w25,w8,w9 | `FALL_THROUGH`
<a id="insn-00affd4c"></a> `00affd4c` | `db 45 f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00affd50"></a> `00affd50` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00affd54"></a> `00affd54` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00affd58"></a> `00affd58` | `70 0b f4 97` | bl 0x00802b18 | `UNCONDITIONAL_CALL`
<a id="insn-00affd5c"></a> `00affd5c` | `e8 de 4c 91` | add x8,x23,#0x337, LSL #12 | `FALL_THROUGH`
<a id="insn-00affd60"></a> `00affd60` | `e1 03 00 2a` | mov w1,w0 | `FALL_THROUGH`
<a id="insn-00affd64"></a> `00affd64` | `00 41 0c 91` | add x0,x8,#0x310 | `FALL_THROUGH`
<a id="insn-00affd68"></a> `00affd68` | `e3 09 f4 97` | bl 0x008024f4 | `UNCONDITIONAL_CALL`
<a id="insn-00affd6c"></a> `00affd6c` | `19 7c 19 1b` | mul w25,w0,w25 | `FALL_THROUGH`
<a id="insn-00affd70"></a> `00affd70` | `df 06 00 31` | cmn w22,#0x1 | `FALL_THROUGH`
<a id="insn-00affd74"></a> `00affd74` | `c0 08 00 54` | b.eq 0x00affe8c | `CONDITIONAL_JUMP`
<a id="insn-00affd78"></a> `00affd78` | `d0 45 f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00affd7c"></a> `00affd7c` | `08 ed 84 52` | mov w8,#0x2768 | `FALL_THROUGH`
<a id="insn-00affd80"></a> `00affd80` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00affd84"></a> `00affd84` | `e2 03 16 2a` | mov w2,w22 | `FALL_THROUGH`
<a id="insn-00affd88"></a> `00affd88` | `00 00 08 8b` | add x0,x0,x8 | `FALL_THROUGH`
<a id="insn-00affd8c"></a> `00affd8c` | `9d 9f eb 97` | bl 0x005e7c00 | `UNCONDITIONAL_CALL`
<a id="insn-00affd90"></a> `00affd90` | `f7 03 1f 2a` | mov w23,wzr | `FALL_THROUGH`
<a id="insn-00affd94"></a> `00affd94` | `40 01 00 36` | tbz w0,#0x0,0x00affdbc | `CONDITIONAL_JUMP`
<a id="insn-00affd98"></a> `00affd98` | `c8 45 f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00affd9c"></a> `00affd9c` | `08 c9 82 52` | mov w8,#0x1648 | `FALL_THROUGH`
<a id="insn-00affda0"></a> `00affda0` | `e1 03 13 2a` | mov w1,w19 | `FALL_THROUGH`
<a id="insn-00affda4"></a> `00affda4` | `c2 02 80 52` | mov w2,#0x16 | `FALL_THROUGH`
<a id="insn-00affda8"></a> `00affda8` | `00 00 08 8b` | add x0,x0,x8 | `FALL_THROUGH`
<a id="insn-00affdac"></a> `00affdac` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-00affdb0"></a> `00affdb0` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00affdb4"></a> `00affdb4` | `b2 27 ee 97` | bl 0x00689c7c | `UNCONDITIONAL_CALL`
<a id="insn-00affdb8"></a> `00affdb8` | `f7 03 00 2a` | mov w23,w0 | `FALL_THROUGH`
<a id="insn-00affdbc"></a> `00affdbc` | `bf 45 f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00affdc0"></a> `00affdc0` | `08 ed 84 52` | mov w8,#0x2768 | `FALL_THROUGH`
<a id="insn-00affdc4"></a> `00affdc4` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00affdc8"></a> `00affdc8` | `e2 03 16 2a` | mov w2,w22 | `FALL_THROUGH`
<a id="insn-00affdcc"></a> `00affdcc` | `00 00 08 8b` | add x0,x0,x8 | `FALL_THROUGH`
<a id="insn-00affdd0"></a> `00affdd0` | `a2 9f eb 97` | bl 0x005e7c58 | `UNCONDITIONAL_CALL`
<a id="insn-00affdd4"></a> `00affdd4` | `00 01 00 36` | tbz w0,#0x0,0x00affdf4 | `CONDITIONAL_JUMP`
<a id="insn-00affdd8"></a> `00affdd8` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00affddc"></a> `00affddc` | `e1 03 13 2a` | mov w1,w19 | `FALL_THROUGH`
<a id="insn-00affde0"></a> `00affde0` | `e2 03 15 2a` | mov w2,w21 | `FALL_THROUGH`
<a id="insn-00affde4"></a> `00affde4` | `03 7d 80 52` | mov w3,#0x3e8 | `FALL_THROUGH`
<a id="insn-00affde8"></a> `00affde8` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00affdec"></a> `00affdec` | `35 fa ff 97` | bl 0x00afe6c0 | `UNCONDITIONAL_CALL`
<a id="insn-00affdf0"></a> `00affdf0` | `17 00 17 0b` | add w23,w0,w23 | `FALL_THROUGH`
<a id="insn-00affdf4"></a> `00affdf4` | `88 0c 80 52` | mov w8,#0x64 | `FALL_THROUGH`
<a id="insn-00affdf8"></a> `00affdf8` | `aa 75 91 52` | mov w10,#0x8bad | `FALL_THROUGH`
<a id="insn-00affdfc"></a> `00affdfc` | `09 01 17 4b` | sub w9,w8,w23 | `FALL_THROUGH`
<a id="insn-00affe00"></a> `00affe00` | `6a 1b ad 72` | movk w10,#0x68db, LSL #16 | `FALL_THROUGH`
<a id="insn-00affe04"></a> `00affe04` | `29 7d 19 1b` | mul w9,w9,w25 | `FALL_THROUGH`
<a id="insn-00affe08"></a> `00affe08` | `29 7d 2a 9b` | smull x9,w9,w10 | `FALL_THROUGH`
<a id="insn-00affe0c"></a> `00affe0c` | `2a fd 7f d3` | lsr x10,x9,#0x3f | `FALL_THROUGH`
<a id="insn-00affe10"></a> `00affe10` | `29 fd 6c 93` | asr x9,x9,#0x2c | `FALL_THROUGH`
<a id="insn-00affe14"></a> `00affe14` | `29 01 0a 0b` | add w9,w9,w10 | `FALL_THROUGH`
<a id="insn-00affe18"></a> `00affe18` | `39 7d 08 1b` | mul w25,w9,w8 | `FALL_THROUGH`
<a id="insn-00affe1c"></a> `00affe1c` | `d4 06 00 36` | tbz w20,#0x0,0x00affef4 | `CONDITIONAL_JUMP`
<a id="insn-00affe20"></a> `00affe20` | `a6 45 f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00affe24"></a> `00affe24` | `09 34 51 91` | add x9,x0,#0x44d, LSL #12 | `FALL_THROUGH`
<a id="insn-00affe28"></a> `00affe28` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00affe2c"></a> `00affe2c` | `61 03 80 52` | mov w1,#0x1b | `FALL_THROUGH`
<a id="insn-00affe30"></a> `00affe30` | `20 01 34 91` | add x0,x9,#0xd00 | `FALL_THROUGH`
<a id="insn-00affe34"></a> `00affe34` | `e2 03 13 2a` | mov w2,w19 | `FALL_THROUGH`
<a id="insn-00affe38"></a> `00affe38` | `0c 0c f7 97` | bl 0x008c2e68 | `UNCONDITIONAL_CALL`
<a id="insn-00affe3c"></a> `00affe3c` | `e0 23 40 a9` | ldp x0,x8,[sp] | `FALL_THROUGH`
<a id="insn-00affe40"></a> `00affe40` | `1f 01 00 eb` | cmp x8,x0 | `FALL_THROUGH`
<a id="insn-00affe44"></a> `00affe44` | `e0 01 00 54` | b.eq 0x00affe80 | `CONDITIONAL_JUMP`
<a id="insn-00affe48"></a> `00affe48` | `aa 75 91 52` | mov w10,#0x8bad | `FALL_THROUGH`
<a id="insn-00affe4c"></a> `00affe4c` | `89 0c 80 52` | mov w9,#0x64 | `FALL_THROUGH`
<a id="insn-00affe50"></a> `00affe50` | `eb 03 00 aa` | mov x11,x0 | `FALL_THROUGH`
<a id="insn-00affe54"></a> `00affe54` | `6a 1b ad 72` | movk w10,#0x68db, LSL #16 | `FALL_THROUGH`
<a id="insn-00affe58"></a> `00affe58` | `6c 45 40 b8` | ldr w12,[x11], #0x4 | `FALL_THROUGH`
<a id="insn-00affe5c"></a> `00affe5c` | `7f 01 08 eb` | cmp x11,x8 | `FALL_THROUGH`
<a id="insn-00affe60"></a> `00affe60` | `2c 01 0c 4b` | sub w12,w9,w12 | `FALL_THROUGH`
<a id="insn-00affe64"></a> `00affe64` | `8c 7d 19 1b` | mul w12,w12,w25 | `FALL_THROUGH`
<a id="insn-00affe68"></a> `00affe68` | `8c 7d 2a 9b` | smull x12,w12,w10 | `FALL_THROUGH`
<a id="insn-00affe6c"></a> `00affe6c` | `8d fd 7f d3` | lsr x13,x12,#0x3f | `FALL_THROUGH`
<a id="insn-00affe70"></a> `00affe70` | `8c fd 6c 93` | asr x12,x12,#0x2c | `FALL_THROUGH`
<a id="insn-00affe74"></a> `00affe74` | `8c 01 0d 0b` | add w12,w12,w13 | `FALL_THROUGH`
<a id="insn-00affe78"></a> `00affe78` | `99 7d 09 1b` | mul w25,w12,w9 | `FALL_THROUGH`
<a id="insn-00affe7c"></a> `00affe7c` | `e1 fe ff 54` | b.ne 0x00affe58 | `CONDITIONAL_JUMP`
<a id="insn-00affe80"></a> `00affe80` | `60 00 00 b4` | cbz x0,0x00affe8c | `CONDITIONAL_JUMP`
<a id="insn-00affe84"></a> `00affe84` | `e0 07 00 f9` | str x0,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00affe88"></a> `00affe88` | `0a 5f 05 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00affe8c"></a> `00affe8c` | `54 03 00 36` | tbz w20,#0x0,0x00affef4 | `CONDITIONAL_JUMP`
<a id="insn-00affe90"></a> `00affe90` | `8a 45 f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00affe94"></a> `00affe94` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00affe98"></a> `00affe98` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00affe9c"></a> `00affe9c` | `1f 0b f4 97` | bl 0x00802b18 | `UNCONDITIONAL_CALL`
<a id="insn-00affea0"></a> `00affea0` | `e1 03 00 2a` | mov w1,w0 | `FALL_THROUGH`
<a id="insn-00affea4"></a> `00affea4` | `80 e2 1d 91` | add x0,x20,#0x778 | `FALL_THROUGH`
<a id="insn-00affea8"></a> `00affea8` | `a2 00 80 52` | mov w2,#0x5 | `FALL_THROUGH`
<a id="insn-00affeac"></a> `00affeac` | `cc a9 ed 97` | bl 0x0066a5dc | `UNCONDITIONAL_CALL`
<a id="insn-00affeb0"></a> `00affeb0` | `20 02 00 b4` | cbz x0,0x00affef4 | `CONDITIONAL_JUMP`
<a id="insn-00affeb4"></a> `00affeb4` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00affeb8"></a> `00affeb8` | `e0 03 13 2a` | mov w0,w19 | `FALL_THROUGH`
<a id="insn-00affebc"></a> `00affebc` | `31 92 ed 97` | bl 0x00664780 | `UNCONDITIONAL_CALL`
<a id="insn-00affec0"></a> `00affec0` | `88 2a 40 a9` | ldp x8,x10,[x20] | `FALL_THROUGH`
<a id="insn-00affec4"></a> `00affec4` | `09 7c 40 93` | sxtw x9,w0 | `FALL_THROUGH`
<a id="insn-00affec8"></a> `00affec8` | `4a 01 08 cb` | sub x10,x10,x8 | `FALL_THROUGH`
<a id="insn-00affecc"></a> `00affecc` | `3f 09 8a eb` | cmp x9,x10, ASR #0x2 | `FALL_THROUGH`
<a id="insn-00affed0"></a> `00affed0` | `42 03 00 54` | b.cs 0x00afff38 | `CONDITIONAL_JUMP`
<a id="insn-00affed4"></a> `00affed4` | `08 79 69 b8` | ldr w8,[x8, x9, LSL #0x2] | `FALL_THROUGH`
<a id="insn-00affed8"></a> `00affed8` | `e9 a3 90 52` | mov w9,#0x851f | `FALL_THROUGH`
<a id="insn-00affedc"></a> `00affedc` | `69 3d aa 72` | movk w9,#0x51eb, LSL #16 | `FALL_THROUGH`
<a id="insn-00affee0"></a> `00affee0` | `08 7d 19 1b` | mul w8,w8,w25 | `FALL_THROUGH`
<a id="insn-00affee4"></a> `00affee4` | `08 7d 29 9b` | smull x8,w8,w9 | `FALL_THROUGH`
<a id="insn-00affee8"></a> `00affee8` | `09 fd 7f d3` | lsr x9,x8,#0x3f | `FALL_THROUGH`
<a id="insn-00affeec"></a> `00affeec` | `08 fd 65 93` | asr x8,x8,#0x25 | `FALL_THROUGH`
<a id="insn-00affef0"></a> `00affef0` | `19 01 09 0b` | add w25,w8,w9 | `FALL_THROUGH`
<a id="insn-00affef4"></a> `00affef4` | `20 7f b9 0a` | bic w0,w25,w25, ASR #0x1f | `FALL_THROUGH`
<a id="insn-00affef8"></a> `00affef8` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00affefc"></a> `00affefc` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00afff00"></a> `00afff00` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00afff04"></a> `00afff04` | `61 02 00 54` | b.ne 0x00afff50 | `CONDITIONAL_JUMP`
<a id="insn-00afff08"></a> `00afff08` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00afff0c"></a> `00afff0c` | `f9 1b 40 f9` | ldr x25,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00afff10"></a> `00afff10` | `f6 57 45 a9` | ldp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00afff14"></a> `00afff14` | `f8 5f 44 a9` | ldp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00afff18"></a> `00afff18` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afff1c"></a> `00afff1c` | `ff c3 01 91` | add sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00afff20"></a> `00afff20` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00afff24"></a> `00afff24` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00afff28"></a> `00afff28` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00afff2c"></a> `00afff2c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00afff30"></a> `00afff30` | `01 01 00 54` | b.ne 0x00afff50 | `CONDITIONAL_JUMP`
<a id="insn-00afff34"></a> `00afff34` | `1f 7d e6 97` | bl 0x0049f3b0 | `CALL_TERMINATOR`
<a id="insn-00afff38"></a> `00afff38` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00afff3c"></a> `00afff3c` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00afff40"></a> `00afff40` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00afff44"></a> `00afff44` | `61 00 00 54` | b.ne 0x00afff50 | `CONDITIONAL_JUMP`
<a id="insn-00afff48"></a> `00afff48` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00afff4c"></a> `00afff4c` | `19 7d e6 97` | bl 0x0049f3b0 | `CALL_TERMINATOR`
<a id="insn-00afff50"></a> `00afff50` | `e4 5e 05 94` | bl 0x00c57ae0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00affc2c`](#insn-00affc2c) 範囲 `[['00affc2c', '00affc67']]`
  - `CONDITIONAL_JUMP` [`00affc64`](#insn-00affc64) → [`00affca8`](#insn-00affca8)
  - `FALL_THROUGH` [`00affc64`](#insn-00affc64) → [`00affc68`](#insn-00affc68)
- ブロック [`00affc68`](#insn-00affc68) 範囲 `[['00affc68', '00affc8b']]`
  - `CONDITIONAL_JUMP` [`00affc88`](#insn-00affc88) → [`00affca8`](#insn-00affca8)
  - `FALL_THROUGH` [`00affc88`](#insn-00affc88) → [`00affc8c`](#insn-00affc8c)
- ブロック [`00affc8c`](#insn-00affc8c) 範囲 `[['00affc8c', '00affc97']]`
  - `CONDITIONAL_JUMP` [`00affc94`](#insn-00affc94) → [`00afff24`](#insn-00afff24)
  - `FALL_THROUGH` [`00affc94`](#insn-00affc94) → [`00affc98`](#insn-00affc98)
- ブロック [`00affc98`](#insn-00affc98) 範囲 `[['00affc98', '00affca7']]`
  - `UNCONDITIONAL_JUMP` [`00affca4`](#insn-00affca4) → [`00affef8`](#insn-00affef8)
- ブロック [`00affca8`](#insn-00affca8) 範囲 `[['00affca8', '00affcb7']]`
  - `FALL_THROUGH` [`00affcb4`](#insn-00affcb4) → [`00affcb8`](#insn-00affcb8)
- ブロック [`00affcb8`](#insn-00affcb8) 範囲 `[['00affcb8', '00affcff']]`
  - `CONDITIONAL_JUMP` [`00affcfc`](#insn-00affcfc) → [`00affd70`](#insn-00affd70)
  - `FALL_THROUGH` [`00affcfc`](#insn-00affcfc) → [`00affd00`](#insn-00affd00)
- ブロック [`00affd00`](#insn-00affd00) 範囲 `[['00affd00', '00affd1b']]`
  - `FALL_THROUGH` [`00affd18`](#insn-00affd18) → [`00affd1c`](#insn-00affd1c)
- ブロック [`00affd1c`](#insn-00affd1c) 範囲 `[['00affd1c', '00affd23']]`
  - `CONDITIONAL_JUMP` [`00affd20`](#insn-00affd20) → [`00affd70`](#insn-00affd70)
  - `FALL_THROUGH` [`00affd20`](#insn-00affd20) → [`00affd24`](#insn-00affd24)
- ブロック [`00affd24`](#insn-00affd24) 範囲 `[['00affd24', '00affd3b']]`
  - `FALL_THROUGH` [`00affd38`](#insn-00affd38) → [`00affd3c`](#insn-00affd3c)
- ブロック [`00affd3c`](#insn-00affd3c) 範囲 `[['00affd3c', '00affd6f']]`
  - `FALL_THROUGH` [`00affd6c`](#insn-00affd6c) → [`00affd70`](#insn-00affd70)
- ブロック [`00affd70`](#insn-00affd70) 範囲 `[['00affd70', '00affd77']]`
  - `CONDITIONAL_JUMP` [`00affd74`](#insn-00affd74) → [`00affe8c`](#insn-00affe8c)
  - `FALL_THROUGH` [`00affd74`](#insn-00affd74) → [`00affd78`](#insn-00affd78)
- ブロック [`00affd78`](#insn-00affd78) 範囲 `[['00affd78', '00affd97']]`
  - `CONDITIONAL_JUMP` [`00affd94`](#insn-00affd94) → [`00affdbc`](#insn-00affdbc)
  - `FALL_THROUGH` [`00affd94`](#insn-00affd94) → [`00affd98`](#insn-00affd98)
- ブロック [`00affd98`](#insn-00affd98) 範囲 `[['00affd98', '00affdbb']]`
  - `FALL_THROUGH` [`00affdb8`](#insn-00affdb8) → [`00affdbc`](#insn-00affdbc)
- ブロック [`00affdbc`](#insn-00affdbc) 範囲 `[['00affdbc', '00affdd7']]`
  - `CONDITIONAL_JUMP` [`00affdd4`](#insn-00affdd4) → [`00affdf4`](#insn-00affdf4)
  - `FALL_THROUGH` [`00affdd4`](#insn-00affdd4) → [`00affdd8`](#insn-00affdd8)
- ブロック [`00affdd8`](#insn-00affdd8) 範囲 `[['00affdd8', '00affdf3']]`
  - `FALL_THROUGH` [`00affdf0`](#insn-00affdf0) → [`00affdf4`](#insn-00affdf4)
- ブロック [`00affdf4`](#insn-00affdf4) 範囲 `[['00affdf4', '00affe1f']]`
  - `CONDITIONAL_JUMP` [`00affe1c`](#insn-00affe1c) → [`00affef4`](#insn-00affef4)
  - `FALL_THROUGH` [`00affe1c`](#insn-00affe1c) → [`00affe20`](#insn-00affe20)
- ブロック [`00affe20`](#insn-00affe20) 範囲 `[['00affe20', '00affe47']]`
  - `CONDITIONAL_JUMP` [`00affe44`](#insn-00affe44) → [`00affe80`](#insn-00affe80)
  - `FALL_THROUGH` [`00affe44`](#insn-00affe44) → [`00affe48`](#insn-00affe48)
- ブロック [`00affe48`](#insn-00affe48) 範囲 `[['00affe48', '00affe57']]`
  - `FALL_THROUGH` [`00affe54`](#insn-00affe54) → [`00affe58`](#insn-00affe58)
- ブロック [`00affe58`](#insn-00affe58) 範囲 `[['00affe58', '00affe7f']]`
  - `CONDITIONAL_JUMP` [`00affe7c`](#insn-00affe7c) → [`00affe58`](#insn-00affe58)
  - `FALL_THROUGH` [`00affe7c`](#insn-00affe7c) → [`00affe80`](#insn-00affe80)
- ブロック [`00affe80`](#insn-00affe80) 範囲 `[['00affe80', '00affe83']]`
  - `CONDITIONAL_JUMP` [`00affe80`](#insn-00affe80) → [`00affe8c`](#insn-00affe8c)
  - `FALL_THROUGH` [`00affe80`](#insn-00affe80) → [`00affe84`](#insn-00affe84)
- ブロック [`00affe84`](#insn-00affe84) 範囲 `[['00affe84', '00affe8b']]`
  - `FALL_THROUGH` [`00affe88`](#insn-00affe88) → [`00affe8c`](#insn-00affe8c)
- ブロック [`00affe8c`](#insn-00affe8c) 範囲 `[['00affe8c', '00affe8f']]`
  - `CONDITIONAL_JUMP` [`00affe8c`](#insn-00affe8c) → [`00affef4`](#insn-00affef4)
  - `FALL_THROUGH` [`00affe8c`](#insn-00affe8c) → [`00affe90`](#insn-00affe90)
- ブロック [`00affe90`](#insn-00affe90) 範囲 `[['00affe90', '00affeb3']]`
  - `CONDITIONAL_JUMP` [`00affeb0`](#insn-00affeb0) → [`00affef4`](#insn-00affef4)
  - `FALL_THROUGH` [`00affeb0`](#insn-00affeb0) → [`00affeb4`](#insn-00affeb4)
- ブロック [`00affeb4`](#insn-00affeb4) 範囲 `[['00affeb4', '00affed3']]`
  - `CONDITIONAL_JUMP` [`00affed0`](#insn-00affed0) → [`00afff38`](#insn-00afff38)
  - `FALL_THROUGH` [`00affed0`](#insn-00affed0) → [`00affed4`](#insn-00affed4)
- ブロック [`00affed4`](#insn-00affed4) 範囲 `[['00affed4', '00affef3']]`
  - `FALL_THROUGH` [`00affef0`](#insn-00affef0) → [`00affef4`](#insn-00affef4)
- ブロック [`00affef4`](#insn-00affef4) 範囲 `[['00affef4', '00affef7']]`
  - `FALL_THROUGH` [`00affef4`](#insn-00affef4) → [`00affef8`](#insn-00affef8)
- ブロック [`00affef8`](#insn-00affef8) 範囲 `[['00affef8', '00afff07']]`
  - `CONDITIONAL_JUMP` [`00afff04`](#insn-00afff04) → [`00afff50`](#insn-00afff50)
  - `FALL_THROUGH` [`00afff04`](#insn-00afff04) → [`00afff08`](#insn-00afff08)
- ブロック [`00afff08`](#insn-00afff08) 範囲 `[['00afff08', '00afff23']]`
- ブロック [`00afff24`](#insn-00afff24) 範囲 `[['00afff24', '00afff33']]`
  - `CONDITIONAL_JUMP` [`00afff30`](#insn-00afff30) → [`00afff50`](#insn-00afff50)
  - `FALL_THROUGH` [`00afff30`](#insn-00afff30) → [`00afff34`](#insn-00afff34)
- ブロック [`00afff34`](#insn-00afff34) 範囲 `[['00afff34', '00afff37']]`
- ブロック [`00afff38`](#insn-00afff38) 範囲 `[['00afff38', '00afff47']]`
  - `CONDITIONAL_JUMP` [`00afff44`](#insn-00afff44) → [`00afff50`](#insn-00afff50)
  - `FALL_THROUGH` [`00afff44`](#insn-00afff44) → [`00afff48`](#insn-00afff48)
- ブロック [`00afff48`](#insn-00afff48) 範囲 `[['00afff48', '00afff4f']]`
- ブロック [`00afff50`](#insn-00afff50) 範囲 `[['00afff50', '00afff53']]`

## 命令位置別の参照

- [`00affc30`](#insn-00affc30) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affc34`](#insn-00affc34) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affc38`](#insn-00affc38) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affc3c`](#insn-00affc3c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affc40`](#insn-00affc40) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affc60`](#insn-00affc60) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affc64`](#insn-00affc64) → [`00affca8`](#insn-00affca8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affc68`](#insn-00affc68) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00affc74`](#insn-00affc74) → [`00802b18`](../00802/00802b18.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00802b18` · 推定シンボル `None` · 推定型 `None`
- [`00affc84`](#insn-00affc84) → [`0066a5dc`](../0066a/0066a5dc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0066a5dc` · 推定シンボル `None` · 推定型 `None`
- [`00affc88`](#insn-00affc88) → [`00affca8`](#insn-00affca8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affc94`](#insn-00affc94) → [`00afff24`](#insn-00afff24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affca4`](#insn-00affca4) → [`00affef8`](#insn-00affef8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affcb4`](#insn-00affcb4) → [`00affb3c`](00affb3c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00affb3c` · 推定シンボル `None` · 推定型 `None`
- [`00affcd0`](#insn-00affcd0) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00affce0`](#insn-00affce0) → `00393bf8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `fde_00393bf8` · 推定型 `dword`
- [`00affcfc`](#insn-00affcfc) → [`00affd70`](#insn-00affd70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affd00`](#insn-00affd00) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00affd0c`](#insn-00affd0c) → [`00802b18`](../00802/00802b18.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00802b18` · 推定シンボル `None` · 推定型 `None`
- [`00affd1c`](#insn-00affd1c) → [`008024f4`](../00802/008024f4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008024f4` · 推定シンボル `None` · 推定型 `None`
- [`00affd20`](#insn-00affd20) → [`00affd70`](#insn-00affd70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affd30`](#insn-00affd30) → [`00affb3c`](00affb3c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00affb3c` · 推定シンボル `None` · 推定型 `None`
- [`00affd4c`](#insn-00affd4c) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00affd58`](#insn-00affd58) → [`00802b18`](../00802/00802b18.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00802b18` · 推定シンボル `None` · 推定型 `None`
- [`00affd68`](#insn-00affd68) → [`008024f4`](../00802/008024f4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008024f4` · 推定シンボル `None` · 推定型 `None`
- [`00affd74`](#insn-00affd74) → [`00affe8c`](#insn-00affe8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affd78`](#insn-00affd78) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00affd8c`](#insn-00affd8c) → [`005e7c00`](../005e7/005e7c00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005e7c00` · 推定シンボル `None` · 推定型 `None`
- [`00affd94`](#insn-00affd94) → [`00affdbc`](#insn-00affdbc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affd98`](#insn-00affd98) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00affdb4`](#insn-00affdb4) → [`00689c7c`](../00689/00689c7c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00689c7c` · 推定シンボル `None` · 推定型 `None`
- [`00affdbc`](#insn-00affdbc) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00affdd0`](#insn-00affdd0) → [`005e7c58`](../005e7/005e7c58.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005e7c58` · 推定シンボル `None` · 推定型 `None`
- [`00affdd4`](#insn-00affdd4) → [`00affdf4`](#insn-00affdf4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affdec`](#insn-00affdec) → [`00afe6c0`](../00afe/00afe6c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00afe6c0` · 推定シンボル `None` · 推定型 `None`
- [`00affe1c`](#insn-00affe1c) → [`00affef4`](#insn-00affef4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affe20`](#insn-00affe20) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00affe38`](#insn-00affe38) → [`008c2e68`](../008c2/008c2e68.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008c2e68` · 推定シンボル `None` · 推定型 `None`
- [`00affe3c`](#insn-00affe3c) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affe44`](#insn-00affe44) → [`00affe80`](#insn-00affe80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affe7c`](#insn-00affe7c) → [`00affe58`](#insn-00affe58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affe80`](#insn-00affe80) → [`00affe8c`](#insn-00affe8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affe84`](#insn-00affe84) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affe88`](#insn-00affe88) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00affe8c`](#insn-00affe8c) → [`00affef4`](#insn-00affef4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affe90`](#insn-00affe90) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00affe9c`](#insn-00affe9c) → [`00802b18`](../00802/00802b18.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00802b18` · 推定シンボル `None` · 推定型 `None`
- [`00affeac`](#insn-00affeac) → [`0066a5dc`](../0066a/0066a5dc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0066a5dc` · 推定シンボル `None` · 推定型 `None`
- [`00affeb0`](#insn-00affeb0) → [`00affef4`](#insn-00affef4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affebc`](#insn-00affebc) → [`00664780`](../00664/00664780.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00664780` · 推定シンボル `None` · 推定型 `None`
- [`00affed0`](#insn-00affed0) → [`00afff38`](#insn-00afff38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affefc`](#insn-00affefc) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afff04`](#insn-00afff04) → [`00afff50`](#insn-00afff50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afff08`](#insn-00afff08) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afff0c`](#insn-00afff0c) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afff10`](#insn-00afff10) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afff14`](#insn-00afff14) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afff18`](#insn-00afff18) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afff28`](#insn-00afff28) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afff30`](#insn-00afff30) → [`00afff50`](#insn-00afff50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afff34`](#insn-00afff34) → [`0049f3b0`](../0049f/0049f3b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0049f3b0` · 推定シンボル `None` · 推定型 `None`
- [`00afff3c`](#insn-00afff3c) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afff44`](#insn-00afff44) → [`00afff50`](#insn-00afff50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afff4c`](#insn-00afff4c) → [`0049f3b0`](../0049f/0049f3b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0049f3b0` · 推定シンボル `None` · 推定型 `None`
- [`00afff50`](#insn-00afff50) → [`00c57ae0`](../00c57/00c57ae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ae0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00affc30`](#insn-00affc30)

~~~json
{
  "source": "00affc30",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affc34`](#insn-00affc34)

~~~json
{
  "source": "00affc34",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affc38`](#insn-00affc38)

~~~json
{
  "source": "00affc38",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affc3c`](#insn-00affc3c)

~~~json
{
  "source": "00affc3c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affc40`](#insn-00affc40)

~~~json
{
  "source": "00affc40",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affc60`](#insn-00affc60)

~~~json
{
  "source": "00affc60",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affc64`](#insn-00affc64)

~~~json
{
  "source": "00affc64",
  "target": "00affca8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affc68`](#insn-00affc68)

~~~json
{
  "source": "00affc68",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affc74`](#insn-00affc74)

~~~json
{
  "source": "00affc74",
  "target": "00802b18",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affc84`](#insn-00affc84)

~~~json
{
  "source": "00affc84",
  "target": "0066a5dc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affc88`](#insn-00affc88)

~~~json
{
  "source": "00affc88",
  "target": "00affca8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affc94`](#insn-00affc94)

~~~json
{
  "source": "00affc94",
  "target": "00afff24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affca4`](#insn-00affca4)

~~~json
{
  "source": "00affca4",
  "target": "00affef8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affcb4`](#insn-00affcb4)

~~~json
{
  "source": "00affcb4",
  "target": "00affb3c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affcd0`](#insn-00affcd0)

~~~json
{
  "source": "00affcd0",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affce0`](#insn-00affce0)

~~~json
{
  "source": "00affce0",
  "target": "00393bf8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00393bf8",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "48000000",
  "capture_start": "00393bf8",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00affcfc`](#insn-00affcfc)

~~~json
{
  "source": "00affcfc",
  "target": "00affd70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affd00`](#insn-00affd00)

~~~json
{
  "source": "00affd00",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affd0c`](#insn-00affd0c)

~~~json
{
  "source": "00affd0c",
  "target": "00802b18",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affd1c`](#insn-00affd1c)

~~~json
{
  "source": "00affd1c",
  "target": "008024f4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affd20`](#insn-00affd20)

~~~json
{
  "source": "00affd20",
  "target": "00affd70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affd30`](#insn-00affd30)

~~~json
{
  "source": "00affd30",
  "target": "00affb3c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affd4c`](#insn-00affd4c)

~~~json
{
  "source": "00affd4c",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affd58`](#insn-00affd58)

~~~json
{
  "source": "00affd58",
  "target": "00802b18",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affd68`](#insn-00affd68)

~~~json
{
  "source": "00affd68",
  "target": "008024f4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affd74`](#insn-00affd74)

~~~json
{
  "source": "00affd74",
  "target": "00affe8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affd78`](#insn-00affd78)

~~~json
{
  "source": "00affd78",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affd8c`](#insn-00affd8c)

~~~json
{
  "source": "00affd8c",
  "target": "005e7c00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affd94`](#insn-00affd94)

~~~json
{
  "source": "00affd94",
  "target": "00affdbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affd98`](#insn-00affd98)

~~~json
{
  "source": "00affd98",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affdb4`](#insn-00affdb4)

~~~json
{
  "source": "00affdb4",
  "target": "00689c7c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affdbc`](#insn-00affdbc)

~~~json
{
  "source": "00affdbc",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affdd0`](#insn-00affdd0)

~~~json
{
  "source": "00affdd0",
  "target": "005e7c58",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affdd4`](#insn-00affdd4)

~~~json
{
  "source": "00affdd4",
  "target": "00affdf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affdec`](#insn-00affdec)

~~~json
{
  "source": "00affdec",
  "target": "00afe6c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affe1c`](#insn-00affe1c)

~~~json
{
  "source": "00affe1c",
  "target": "00affef4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affe20`](#insn-00affe20)

~~~json
{
  "source": "00affe20",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affe38`](#insn-00affe38)

~~~json
{
  "source": "00affe38",
  "target": "008c2e68",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affe3c`](#insn-00affe3c)

~~~json
{
  "source": "00affe3c",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affe44`](#insn-00affe44)

~~~json
{
  "source": "00affe44",
  "target": "00affe80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affe7c`](#insn-00affe7c)

~~~json
{
  "source": "00affe7c",
  "target": "00affe58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affe80`](#insn-00affe80)

~~~json
{
  "source": "00affe80",
  "target": "00affe8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affe84`](#insn-00affe84)

~~~json
{
  "source": "00affe84",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affe88`](#insn-00affe88)

~~~json
{
  "source": "00affe88",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affe8c`](#insn-00affe8c)

~~~json
{
  "source": "00affe8c",
  "target": "00affef4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affe90`](#insn-00affe90)

~~~json
{
  "source": "00affe90",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affe9c`](#insn-00affe9c)

~~~json
{
  "source": "00affe9c",
  "target": "00802b18",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affeac`](#insn-00affeac)

~~~json
{
  "source": "00affeac",
  "target": "0066a5dc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affeb0`](#insn-00affeb0)

~~~json
{
  "source": "00affeb0",
  "target": "00affef4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affebc`](#insn-00affebc)

~~~json
{
  "source": "00affebc",
  "target": "00664780",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affed0`](#insn-00affed0)

~~~json
{
  "source": "00affed0",
  "target": "00afff38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affefc`](#insn-00affefc)

~~~json
{
  "source": "00affefc",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afff04`](#insn-00afff04)

~~~json
{
  "source": "00afff04",
  "target": "00afff50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afff08`](#insn-00afff08)

~~~json
{
  "source": "00afff08",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afff0c`](#insn-00afff0c)

~~~json
{
  "source": "00afff0c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afff10`](#insn-00afff10)

~~~json
{
  "source": "00afff10",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afff14`](#insn-00afff14)

~~~json
{
  "source": "00afff14",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afff18`](#insn-00afff18)

~~~json
{
  "source": "00afff18",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afff28`](#insn-00afff28)

~~~json
{
  "source": "00afff28",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afff30`](#insn-00afff30)

~~~json
{
  "source": "00afff30",
  "target": "00afff50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afff34`](#insn-00afff34)

~~~json
{
  "source": "00afff34",
  "target": "0049f3b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afff3c`](#insn-00afff3c)

~~~json
{
  "source": "00afff3c",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afff44`](#insn-00afff44)

~~~json
{
  "source": "00afff44",
  "target": "00afff50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afff4c`](#insn-00afff4c)

~~~json
{
  "source": "00afff4c",
  "target": "0049f3b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afff50`](#insn-00afff50)

~~~json
{
  "source": "00afff50",
  "target": "00c57ae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
