# 00ad3bfc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00ad3bb8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad3/00ad3bb8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0060.md#compare-18bada3aa6e3ac326f7deced3180987c)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b336b4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b33/00b336b4.md) · 移動量 `+0x5fab8`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0054.md#compare-afac19eac9129d93d92daadbf1d67e9e)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ad3bfc",
  "name": "FUN_00ad3bfc",
  "size": 592,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f4408e604ad25cc0bf019ab44a709493c988d8b88843afc8cfe140915d001c4e",
  "source_text_sha256": "f4408e604ad25cc0bf019ab44a709493c988d8b88843afc8cfe140915d001c4e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ad3bfc",
        "00ad3e47"
      ],
      [
        "00ad3e94",
        "00ad3e97"
      ]
    ],
    "bytes_sha256": "e2d0114b26c86a28d96eee98c0ad067dccb8fc81ad78b23e4fe5a27536e2652a",
    "instruction_count": 148,
    "instruction_bytes": 592,
    "body_bytes": 592,
    "indirect": 2,
    "unresolved": 2
  }
}
~~~

## 呼び出し元

- [0041cad8](../0041c/0041cad8.md)

## 呼び出し先

- [00449b7c](../00449/00449b7c.md)
- [00551e14](../00551/00551e14.md)
- [00565f94](../00565/00565f94.md)
- [0056626c](../00566/0056626c.md)
- [00566284](../00566/00566284.md)
- [00566448](../00566/00566448.md)
- [00566978](../00566/00566978.md)
- [00bdb040](../00bdb/00bdb040.md)
- [00bdb060](../00bdb/00bdb060.md)
- [00bdb090](../00bdb/00bdb090.md)

## 関連文字列（未確認候補）

~~~text
"(Ljava/lang/String;FZ)V"
"(Ljava/lang/String;FZII)V"
"admobShow"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 4356 bytes

~~~c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_00ad3bfc(float param_1,uint param_2,undefined8 param_3,undefined8 param_4,
                 undefined8 param_5)

{
  undefined4 uVar1;
  undefined4 uVar2;
  long lVar3;
  undefined8 uVar4;
  undefined *puVar5;
  long *plVar6;
  undefined8 uVar7;
  ulong uVar8;
  undefined8 uVar9;
  undefined8 uVar10;
  undefined8 uVar11;
  ulong local_90;
  undefined8 uStack_88;
  char *local_80;
  byte local_78;
  char local_77 [8];
  undefined2 local_6f;
  void *local_68;
  long local_60;
  long local_58;
  
  lVar3 = tpidr_el0;
  local_58 = *(long *)(lVar3 + 0x28);
  plVar6 = (long *)FUN_00565f94();
  uVar7 = (**(code **)(*plVar6 + 0x538))(plVar6,param_5);
  puVar5 = PTR_DAT_00c1ad78;
  uVar8 = FUN_00449b7c(PTR_DAT_00c1ad78);
  if ((uVar8 & 1) == 0) {
    uVar11 = FUN_00566284();
    local_78 = 0x12;
    local_77[0] = s_admobShow_002a1e3b[0];
    local_77[1] = s_admobShow_002a1e3b[1];
    local_77[2] = s_admobShow_002a1e3b[2];
    local_77[3] = s_admobShow_002a1e3b[3];
    local_77[4] = s_admobShow_002a1e3b[4];
    local_77[5] = s_admobShow_002a1e3b[5];
    local_77[6] = s_admobShow_002a1e3b[6];
    local_77[7] = s_admobShow_002a1e3b[7];
    local_6f = 0x77;
    local_80 = (char *)_Znwm(0x19);
    uStack_88 = _UNK_002b0e18;
    local_90 = _DAT_002b0e10;
    uVar4 = s__Ljava_lang_String_FZ_V_002a4e5b._0_8_;
    uVar10 = CONCAT71(s__Ljava_lang_String_FZ_V_002a4e5b._16_7_,
                      s__Ljava_lang_String_FZ_V_002a4e5b[0xf]);
    *(ulong *)(local_80 + 8) =
         CONCAT17(s__Ljava_lang_String_FZ_V_002a4e5b[0xf],s__Ljava_lang_String_FZ_V_002a4e5b._8_7_);
    *(undefined8 *)local_80 = uVar4;
    *(undefined8 *)(local_80 + 0xf) = uVar10;
    local_80[0x17] = '\0';
    local_60 = FUN_00566448(uVar11,&local_78,&local_90,plVar6);
    if ((local_90 & 1) != 0) {
      _ZdlPv(local_80);
    }
    if ((local_78 & 1) != 0) {
      _ZdlPv(local_68);
    }
    uVar8 = FUN_0056626c(&local_60);
    if ((uVar8 & 1) != 0) {
      FUN_00566284();
      uVar10 = FUN_00566978();
      if (local_60 != 0) {
        FUN_00551e14((double)param_1,plVar6,uVar10,local_60,uVar7,param_2 & 1);
      }
      goto LAB_00ad3e1c;
    }
  }
  else {
    uVar9 = FUN_00566284();
    local_78 = 0x12;
    local_77[0] = s_admobShow_002a1e3b[0];
    local_77[1] = s_admobShow_002a1e3b[1];
    local_77[2] = s_admobShow_002a1e3b[2];
    local_77[3] = s_admobShow_002a1e3b[3];
    local_77[4] = s_admobShow_002a1e3b[4];
    local_77[5] = s_admobShow_002a1e3b[5];
    local_77[6] = s_admobShow_002a1e3b[6];
    local_77[7] = s_admobShow_002a1e3b[7];
    local_6f = 0x77;
    local_80 = (char *)_Znwm(0x20);
    uStack_88 = _UNK_002b1128;
    local_90 = _DAT_002b1120;
    uVar11 = s__Ljava_lang_String_FZII_V_002973c2._17_8_;
    uVar4 = s__Ljava_lang_String_FZII_V_002973c2._0_8_;
    uVar10 = CONCAT17(s__Ljava_lang_String_FZII_V_002973c2[0x10],
                      s__Ljava_lang_String_FZII_V_002973c2._9_7_);
                    /* try { // try from 00ad3ca8 to 00bd3d2f has its CatchHandler @ 00ad3e14 */
    *(ulong *)(local_80 + 8) =
         CONCAT71(s__Ljava_lang_String_FZII_V_002973c2._9_7_,s__Ljava_lang_String_FZII_V_002973c2[8]
                 );
    *(undefined8 *)local_80 = uVar4;
    *(undefined8 *)(local_80 + 0x11) = uVar11;
    *(undefined8 *)(local_80 + 9) = uVar10;
    local_80[0x19] = '\0';
    local_60 = FUN_00566448(uVar9,&local_78,&local_90,plVar6);
    if ((local_90 & 1) != 0) {
      _ZdlPv(local_80);
    }
    if ((local_78 & 1) != 0) {
      _ZdlPv(local_68);
    }
    uVar8 = FUN_0056626c(&local_60);
    if ((uVar8 & 1) != 0) {
      uVar1 = *(undefined4 *)(puVar5 + 0x34);
      uVar2 = *(undefined4 *)(puVar5 + 0x40);
      FUN_00566284();
      uVar10 = FUN_00566978();
      if (local_60 != 0) {
                    /* try { // try from 00ad3d30 to 00bd3ee3 has its CatchHandler @ 00ad3b54 */
        FUN_00551e14((double)param_1,plVar6,uVar10,local_60,uVar7,param_2 & 1,uVar1,uVar2);
      }
      goto LAB_00ad3e1c;
    }
  }
                    /* catch() { ... } // from try @ 00ad3ca8 with catch @ 00ad3e14 */
  (**(code **)(*plVar6 + 0xb8))(plVar6,uVar7);
LAB_00ad3e1c:
  if (*(long *)(lVar3 + 0x28) == local_58) {
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
<a id="insn-00ad3bfc"></a> `00ad3bfc` | `ff 43 02 d1` | sub sp,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00ad3c00"></a> `00ad3c00` | `e8 23 00 fd` | str d8,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00ad3c04"></a> `00ad3c04` | `fd 7b 05 a9` | stp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00ad3c08"></a> `00ad3c08` | `f8 5f 06 a9` | stp x24,x23,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00ad3c0c"></a> `00ad3c0c` | `f6 57 07 a9` | stp x22,x21,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00ad3c10"></a> `00ad3c10` | `f4 4f 08 a9` | stp x20,x19,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00ad3c14"></a> `00ad3c14` | `fd 43 01 91` | add x29,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00ad3c18"></a> `00ad3c18` | `58 d0 3b d5` | mrs x24,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00ad3c1c"></a> `00ad3c1c` | `08 40 20 1e` | fmov s8,s0 | `FALL_THROUGH`
<a id="insn-00ad3c20"></a> `00ad3c20` | `f4 03 03 aa` | mov x20,x3 | `FALL_THROUGH`
<a id="insn-00ad3c24"></a> `00ad3c24` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00ad3c28"></a> `00ad3c28` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00ad3c2c"></a> `00ad3c2c` | `a8 83 1e f8` | stur x8,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-00ad3c30"></a> `00ad3c30` | `d9 48 ea 97` | bl 0x00565f94 | `UNCONDITIONAL_CALL`
<a id="insn-00ad3c34"></a> `00ad3c34` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00ad3c38"></a> `00ad3c38` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00ad3c3c"></a> `00ad3c3c` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00ad3c40"></a> `00ad3c40` | `08 9d 42 f9` | ldr x8,[x8, #0x538] | `FALL_THROUGH`
<a id="insn-00ad3c44"></a> `00ad3c44` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ad3c48"></a> `00ad3c48` | `36 0a 00 f0` | adrp x22,0xc1a000 | `FALL_THROUGH`
<a id="insn-00ad3c4c"></a> `00ad3c4c` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00ad3c50"></a> `00ad3c50` | `d6 be 46 f9` | ldr x22,[x22, #0xd78] | `FALL_THROUGH`
<a id="insn-00ad3c54"></a> `00ad3c54` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00ad3c58"></a> `00ad3c58` | `c9 d7 e5 97` | bl 0x00449b7c | `UNCONDITIONAL_CALL`
<a id="insn-00ad3c5c"></a> `00ad3c5c` | `00 07 00 36` | tbz w0,#0x0,0x00ad3d3c | `CONDITIONAL_JUMP`
<a id="insn-00ad3c60"></a> `00ad3c60` | `89 49 ea 97` | bl 0x00566284 | `UNCONDITIONAL_CALL`
<a id="insn-00ad3c64"></a> `00ad3c64` | `69 be ff d0` | adrp x9,0x2a1000 | `FALL_THROUGH`
<a id="insn-00ad3c68"></a> `00ad3c68` | `29 ed 38 91` | add x9,x9,#0xe3b | `FALL_THROUGH`
<a id="insn-00ad3c6c"></a> `00ad3c6c` | `48 02 80 52` | mov w8,#0x12 | `FALL_THROUGH`
<a id="insn-00ad3c70"></a> `00ad3c70` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-00ad3c74"></a> `00ad3c74` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00ad3c78"></a> `00ad3c78` | `e8 63 00 39` | strb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00ad3c7c"></a> `00ad3c7c` | `e8 0e 80 52` | mov w8,#0x77 | `FALL_THROUGH`
<a id="insn-00ad3c80"></a> `00ad3c80` | `e9 93 01 f8` | stur x9,[sp, #0x19] | `FALL_THROUGH`
<a id="insn-00ad3c84"></a> `00ad3c84` | `e8 13 02 78` | sturh w8,[sp, #0x21] | `FALL_THROUGH`
<a id="insn-00ad3c88"></a> `00ad3c88` | `00 04 80 52` | mov w0,#0x20 | `FALL_THROUGH`
<a id="insn-00ad3c8c"></a> `00ad3c8c` | `ed 1c 04 94` | bl 0x00bdb040 | `UNCONDITIONAL_CALL`
<a id="insn-00ad3c90"></a> `00ad3c90` | `28 be ff 90` | adrp x8,0x297000 | `FALL_THROUGH`
<a id="insn-00ad3c94"></a> `00ad3c94` | `08 09 0f 91` | add x8,x8,#0x3c2 | `FALL_THROUGH`
<a id="insn-00ad3c98"></a> `00ad3c98` | `e9 be ff d0` | adrp x9,0x2b1000 | `FALL_THROUGH`
<a id="insn-00ad3c9c"></a> `00ad3c9c` | `00 01 c0 3d` | ldr q0,[x8] | `FALL_THROUGH`
<a id="insn-00ad3ca0"></a> `00ad3ca0` | `01 91 c0 3c` | ldur q1,[x8, #0x9] | `FALL_THROUGH`
<a id="insn-00ad3ca4"></a> `00ad3ca4` | `22 49 c0 3d` | ldr q2,[x9, #0x120] | `FALL_THROUGH`
<a id="insn-00ad3ca8"></a> `00ad3ca8` | `e0 0b 00 f9` | str x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ad3cac"></a> `00ad3cac` | `00 00 80 3d` | str q0,[x0] | `FALL_THROUGH`
<a id="insn-00ad3cb0"></a> `00ad3cb0` | `01 90 80 3c` | stur q1,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00ad3cb4"></a> `00ad3cb4` | `e2 03 80 3d` | str q2,[sp] | `FALL_THROUGH`
<a id="insn-00ad3cb8"></a> `00ad3cb8` | `1f 64 00 39` | strb wzr,[x0, #0x19] | `FALL_THROUGH`
<a id="insn-00ad3cbc"></a> `00ad3cbc` | `e1 63 00 91` | add x1,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00ad3cc0"></a> `00ad3cc0` | `e2 03 00 91` | mov x2,sp | `FALL_THROUGH`
<a id="insn-00ad3cc4"></a> `00ad3cc4` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00ad3cc8"></a> `00ad3cc8` | `e3 03 13 aa` | mov x3,x19 | `FALL_THROUGH`
<a id="insn-00ad3ccc"></a> `00ad3ccc` | `df 49 ea 97` | bl 0x00566448 | `UNCONDITIONAL_CALL`
<a id="insn-00ad3cd0"></a> `00ad3cd0` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-00ad3cd4"></a> `00ad3cd4` | `a0 03 1e f8` | stur x0,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00ad3cd8"></a> `00ad3cd8` | `68 00 00 36` | tbz w8,#0x0,0x00ad3ce4 | `CONDITIONAL_JUMP`
<a id="insn-00ad3cdc"></a> `00ad3cdc` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ad3ce0"></a> `00ad3ce0` | `e0 1c 04 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00ad3ce4"></a> `00ad3ce4` | `e8 63 40 39` | ldrb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00ad3ce8"></a> `00ad3ce8` | `68 00 00 36` | tbz w8,#0x0,0x00ad3cf4 | `CONDITIONAL_JUMP`
<a id="insn-00ad3cec"></a> `00ad3cec` | `e0 17 40 f9` | ldr x0,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00ad3cf0"></a> `00ad3cf0` | `dc 1c 04 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00ad3cf4"></a> `00ad3cf4` | `a0 83 00 d1` | sub x0,x29,#0x20 | `FALL_THROUGH`
<a id="insn-00ad3cf8"></a> `00ad3cf8` | `5d 49 ea 97` | bl 0x0056626c | `UNCONDITIONAL_CALL`
<a id="insn-00ad3cfc"></a> `00ad3cfc` | `60 08 00 36` | tbz w0,#0x0,0x00ad3e08 | `CONDITIONAL_JUMP`
<a id="insn-00ad3d00"></a> `00ad3d00` | `d7 36 40 b9` | ldr w23,[x22, #0x34] | `FALL_THROUGH`
<a id="insn-00ad3d04"></a> `00ad3d04` | `d6 42 40 b9` | ldr w22,[x22, #0x40] | `FALL_THROUGH`
<a id="insn-00ad3d08"></a> `00ad3d08` | `5f 49 ea 97` | bl 0x00566284 | `UNCONDITIONAL_CALL`
<a id="insn-00ad3d0c"></a> `00ad3d0c` | `1b 4b ea 97` | bl 0x00566978 | `UNCONDITIONAL_CALL`
<a id="insn-00ad3d10"></a> `00ad3d10` | `a2 03 5e f8` | ldur x2,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00ad3d14"></a> `00ad3d14` | `42 08 00 b4` | cbz x2,0x00ad3e1c | `CONDITIONAL_JUMP`
<a id="insn-00ad3d18"></a> `00ad3d18` | `00 c1 22 1e` | fcvt d0,s8 | `FALL_THROUGH`
<a id="insn-00ad3d1c"></a> `00ad3d1c` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00ad3d20"></a> `00ad3d20` | `a4 02 00 12` | and w4,w21,#0x1 | `FALL_THROUGH`
<a id="insn-00ad3d24"></a> `00ad3d24` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ad3d28"></a> `00ad3d28` | `e3 03 14 aa` | mov x3,x20 | `FALL_THROUGH`
<a id="insn-00ad3d2c"></a> `00ad3d2c` | `e5 03 17 2a` | mov w5,w23 | `FALL_THROUGH`
<a id="insn-00ad3d30"></a> `00ad3d30` | `e6 03 16 2a` | mov w6,w22 | `FALL_THROUGH`
<a id="insn-00ad3d34"></a> `00ad3d34` | `38 f8 e9 97` | bl 0x00551e14 | `UNCONDITIONAL_CALL`
<a id="insn-00ad3d38"></a> `00ad3d38` | `39 00 00 14` | b 0x00ad3e1c | `UNCONDITIONAL_JUMP`
<a id="insn-00ad3d3c"></a> `00ad3d3c` | `52 49 ea 97` | bl 0x00566284 | `UNCONDITIONAL_CALL`
<a id="insn-00ad3d40"></a> `00ad3d40` | `69 be ff d0` | adrp x9,0x2a1000 | `FALL_THROUGH`
<a id="insn-00ad3d44"></a> `00ad3d44` | `29 ed 38 91` | add x9,x9,#0xe3b | `FALL_THROUGH`
<a id="insn-00ad3d48"></a> `00ad3d48` | `48 02 80 52` | mov w8,#0x12 | `FALL_THROUGH`
<a id="insn-00ad3d4c"></a> `00ad3d4c` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-00ad3d50"></a> `00ad3d50` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00ad3d54"></a> `00ad3d54` | `e8 63 00 39` | strb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00ad3d58"></a> `00ad3d58` | `e8 0e 80 52` | mov w8,#0x77 | `FALL_THROUGH`
<a id="insn-00ad3d5c"></a> `00ad3d5c` | `e9 93 01 f8` | stur x9,[sp, #0x19] | `FALL_THROUGH`
<a id="insn-00ad3d60"></a> `00ad3d60` | `e8 13 02 78` | sturh w8,[sp, #0x21] | `FALL_THROUGH`
<a id="insn-00ad3d64"></a> `00ad3d64` | `20 03 80 52` | mov w0,#0x19 | `FALL_THROUGH`
<a id="insn-00ad3d68"></a> `00ad3d68` | `b6 1c 04 94` | bl 0x00bdb040 | `UNCONDITIONAL_CALL`
<a id="insn-00ad3d6c"></a> `00ad3d6c` | `88 be ff b0` | adrp x8,0x2a4000 | `FALL_THROUGH`
<a id="insn-00ad3d70"></a> `00ad3d70` | `08 6d 39 91` | add x8,x8,#0xe5b | `FALL_THROUGH`
<a id="insn-00ad3d74"></a> `00ad3d74` | `e9 be ff b0` | adrp x9,0x2b0000 | `FALL_THROUGH`
<a id="insn-00ad3d78"></a> `00ad3d78` | `00 01 c0 3d` | ldr q0,[x8] | `FALL_THROUGH`
<a id="insn-00ad3d7c"></a> `00ad3d7c` | `08 f1 40 f8` | ldur x8,[x8, #0xf] | `FALL_THROUGH`
<a id="insn-00ad3d80"></a> `00ad3d80` | `21 85 c3 3d` | ldr q1,[x9, #0xe10] | `FALL_THROUGH`
<a id="insn-00ad3d84"></a> `00ad3d84` | `e0 0b 00 f9` | str x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ad3d88"></a> `00ad3d88` | `00 00 80 3d` | str q0,[x0] | `FALL_THROUGH`
<a id="insn-00ad3d8c"></a> `00ad3d8c` | `08 f0 00 f8` | stur x8,[x0, #0xf] | `FALL_THROUGH`
<a id="insn-00ad3d90"></a> `00ad3d90` | `e1 03 80 3d` | str q1,[sp] | `FALL_THROUGH`
<a id="insn-00ad3d94"></a> `00ad3d94` | `1f 5c 00 39` | strb wzr,[x0, #0x17] | `FALL_THROUGH`
<a id="insn-00ad3d98"></a> `00ad3d98` | `e1 63 00 91` | add x1,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00ad3d9c"></a> `00ad3d9c` | `e2 03 00 91` | mov x2,sp | `FALL_THROUGH`
<a id="insn-00ad3da0"></a> `00ad3da0` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00ad3da4"></a> `00ad3da4` | `e3 03 13 aa` | mov x3,x19 | `FALL_THROUGH`
<a id="insn-00ad3da8"></a> `00ad3da8` | `a8 49 ea 97` | bl 0x00566448 | `UNCONDITIONAL_CALL`
<a id="insn-00ad3dac"></a> `00ad3dac` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-00ad3db0"></a> `00ad3db0` | `a0 03 1e f8` | stur x0,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00ad3db4"></a> `00ad3db4` | `68 00 00 36` | tbz w8,#0x0,0x00ad3dc0 | `CONDITIONAL_JUMP`
<a id="insn-00ad3db8"></a> `00ad3db8` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ad3dbc"></a> `00ad3dbc` | `a9 1c 04 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00ad3dc0"></a> `00ad3dc0` | `e8 63 40 39` | ldrb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00ad3dc4"></a> `00ad3dc4` | `68 00 00 36` | tbz w8,#0x0,0x00ad3dd0 | `CONDITIONAL_JUMP`
<a id="insn-00ad3dc8"></a> `00ad3dc8` | `e0 17 40 f9` | ldr x0,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00ad3dcc"></a> `00ad3dcc` | `a5 1c 04 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00ad3dd0"></a> `00ad3dd0` | `a0 83 00 d1` | sub x0,x29,#0x20 | `FALL_THROUGH`
<a id="insn-00ad3dd4"></a> `00ad3dd4` | `26 49 ea 97` | bl 0x0056626c | `UNCONDITIONAL_CALL`
<a id="insn-00ad3dd8"></a> `00ad3dd8` | `80 01 00 36` | tbz w0,#0x0,0x00ad3e08 | `CONDITIONAL_JUMP`
<a id="insn-00ad3ddc"></a> `00ad3ddc` | `2a 49 ea 97` | bl 0x00566284 | `UNCONDITIONAL_CALL`
<a id="insn-00ad3de0"></a> `00ad3de0` | `e6 4a ea 97` | bl 0x00566978 | `UNCONDITIONAL_CALL`
<a id="insn-00ad3de4"></a> `00ad3de4` | `a2 03 5e f8` | ldur x2,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00ad3de8"></a> `00ad3de8` | `a2 01 00 b4` | cbz x2,0x00ad3e1c | `CONDITIONAL_JUMP`
<a id="insn-00ad3dec"></a> `00ad3dec` | `00 c1 22 1e` | fcvt d0,s8 | `FALL_THROUGH`
<a id="insn-00ad3df0"></a> `00ad3df0` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00ad3df4"></a> `00ad3df4` | `a4 02 00 12` | and w4,w21,#0x1 | `FALL_THROUGH`
<a id="insn-00ad3df8"></a> `00ad3df8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ad3dfc"></a> `00ad3dfc` | `e3 03 14 aa` | mov x3,x20 | `FALL_THROUGH`
<a id="insn-00ad3e00"></a> `00ad3e00` | `05 f8 e9 97` | bl 0x00551e14 | `UNCONDITIONAL_CALL`
<a id="insn-00ad3e04"></a> `00ad3e04` | `06 00 00 14` | b 0x00ad3e1c | `UNCONDITIONAL_JUMP`
<a id="insn-00ad3e08"></a> `00ad3e08` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00ad3e0c"></a> `00ad3e0c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ad3e10"></a> `00ad3e10` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00ad3e14"></a> `00ad3e14` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00ad3e18"></a> `00ad3e18` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ad3e1c"></a> `00ad3e1c` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00ad3e20"></a> `00ad3e20` | `a9 83 5e f8` | ldur x9,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-00ad3e24"></a> `00ad3e24` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00ad3e28"></a> `00ad3e28` | `61 03 00 54` | b.ne 0x00ad3e94 | `CONDITIONAL_JUMP`
<a id="insn-00ad3e2c"></a> `00ad3e2c` | `f4 4f 48 a9` | ldp x20,x19,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00ad3e30"></a> `00ad3e30` | `e8 23 40 fd` | ldr d8,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00ad3e34"></a> `00ad3e34` | `f6 57 47 a9` | ldp x22,x21,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00ad3e38"></a> `00ad3e38` | `f8 5f 46 a9` | ldp x24,x23,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00ad3e3c"></a> `00ad3e3c` | `fd 7b 45 a9` | ldp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00ad3e40"></a> `00ad3e40` | `ff 43 02 91` | add sp,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00ad3e44"></a> `00ad3e44` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00ad3e94"></a> `00ad3e94` | `7f 1c 04 94` | bl 0x00bdb090 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00ad3bfc`](#insn-00ad3bfc) 範囲 `[['00ad3bfc', '00ad3c5f']]`
  - `CONDITIONAL_JUMP` [`00ad3c5c`](#insn-00ad3c5c) → [`00ad3d3c`](#insn-00ad3d3c)
  - `FALL_THROUGH` [`00ad3c5c`](#insn-00ad3c5c) → [`00ad3c60`](#insn-00ad3c60)
- ブロック [`00ad3c60`](#insn-00ad3c60) 範囲 `[['00ad3c60', '00ad3ca7']]`
  - `FALL_THROUGH` [`00ad3ca4`](#insn-00ad3ca4) → [`00ad3ca8`](#insn-00ad3ca8)
- ブロック [`00ad3ca8`](#insn-00ad3ca8) 範囲 `[['00ad3ca8', '00ad3cdb']]`
  - `CONDITIONAL_JUMP` [`00ad3cd8`](#insn-00ad3cd8) → [`00ad3ce4`](#insn-00ad3ce4)
  - `FALL_THROUGH` [`00ad3cd8`](#insn-00ad3cd8) → [`00ad3cdc`](#insn-00ad3cdc)
- ブロック [`00ad3cdc`](#insn-00ad3cdc) 範囲 `[['00ad3cdc', '00ad3ce3']]`
  - `FALL_THROUGH` [`00ad3ce0`](#insn-00ad3ce0) → [`00ad3ce4`](#insn-00ad3ce4)
- ブロック [`00ad3ce4`](#insn-00ad3ce4) 範囲 `[['00ad3ce4', '00ad3ceb']]`
  - `CONDITIONAL_JUMP` [`00ad3ce8`](#insn-00ad3ce8) → [`00ad3cf4`](#insn-00ad3cf4)
  - `FALL_THROUGH` [`00ad3ce8`](#insn-00ad3ce8) → [`00ad3cec`](#insn-00ad3cec)
- ブロック [`00ad3cec`](#insn-00ad3cec) 範囲 `[['00ad3cec', '00ad3cf3']]`
  - `FALL_THROUGH` [`00ad3cf0`](#insn-00ad3cf0) → [`00ad3cf4`](#insn-00ad3cf4)
- ブロック [`00ad3cf4`](#insn-00ad3cf4) 範囲 `[['00ad3cf4', '00ad3cff']]`
  - `CONDITIONAL_JUMP` [`00ad3cfc`](#insn-00ad3cfc) → [`00ad3e08`](#insn-00ad3e08)
  - `FALL_THROUGH` [`00ad3cfc`](#insn-00ad3cfc) → [`00ad3d00`](#insn-00ad3d00)
- ブロック [`00ad3d00`](#insn-00ad3d00) 範囲 `[['00ad3d00', '00ad3d17']]`
  - `CONDITIONAL_JUMP` [`00ad3d14`](#insn-00ad3d14) → [`00ad3e1c`](#insn-00ad3e1c)
  - `FALL_THROUGH` [`00ad3d14`](#insn-00ad3d14) → [`00ad3d18`](#insn-00ad3d18)
- ブロック [`00ad3d18`](#insn-00ad3d18) 範囲 `[['00ad3d18', '00ad3d2f']]`
  - `FALL_THROUGH` [`00ad3d2c`](#insn-00ad3d2c) → [`00ad3d30`](#insn-00ad3d30)
- ブロック [`00ad3d30`](#insn-00ad3d30) 範囲 `[['00ad3d30', '00ad3d3b']]`
  - `UNCONDITIONAL_JUMP` [`00ad3d38`](#insn-00ad3d38) → [`00ad3e1c`](#insn-00ad3e1c)
- ブロック [`00ad3d3c`](#insn-00ad3d3c) 範囲 `[['00ad3d3c', '00ad3db7']]`
  - `CONDITIONAL_JUMP` [`00ad3db4`](#insn-00ad3db4) → [`00ad3dc0`](#insn-00ad3dc0)
  - `FALL_THROUGH` [`00ad3db4`](#insn-00ad3db4) → [`00ad3db8`](#insn-00ad3db8)
- ブロック [`00ad3db8`](#insn-00ad3db8) 範囲 `[['00ad3db8', '00ad3dbf']]`
  - `FALL_THROUGH` [`00ad3dbc`](#insn-00ad3dbc) → [`00ad3dc0`](#insn-00ad3dc0)
- ブロック [`00ad3dc0`](#insn-00ad3dc0) 範囲 `[['00ad3dc0', '00ad3dc7']]`
  - `CONDITIONAL_JUMP` [`00ad3dc4`](#insn-00ad3dc4) → [`00ad3dd0`](#insn-00ad3dd0)
  - `FALL_THROUGH` [`00ad3dc4`](#insn-00ad3dc4) → [`00ad3dc8`](#insn-00ad3dc8)
- ブロック [`00ad3dc8`](#insn-00ad3dc8) 範囲 `[['00ad3dc8', '00ad3dcf']]`
  - `FALL_THROUGH` [`00ad3dcc`](#insn-00ad3dcc) → [`00ad3dd0`](#insn-00ad3dd0)
- ブロック [`00ad3dd0`](#insn-00ad3dd0) 範囲 `[['00ad3dd0', '00ad3ddb']]`
  - `CONDITIONAL_JUMP` [`00ad3dd8`](#insn-00ad3dd8) → [`00ad3e08`](#insn-00ad3e08)
  - `FALL_THROUGH` [`00ad3dd8`](#insn-00ad3dd8) → [`00ad3ddc`](#insn-00ad3ddc)
- ブロック [`00ad3ddc`](#insn-00ad3ddc) 範囲 `[['00ad3ddc', '00ad3deb']]`
  - `CONDITIONAL_JUMP` [`00ad3de8`](#insn-00ad3de8) → [`00ad3e1c`](#insn-00ad3e1c)
  - `FALL_THROUGH` [`00ad3de8`](#insn-00ad3de8) → [`00ad3dec`](#insn-00ad3dec)
- ブロック [`00ad3dec`](#insn-00ad3dec) 範囲 `[['00ad3dec', '00ad3e07']]`
  - `UNCONDITIONAL_JUMP` [`00ad3e04`](#insn-00ad3e04) → [`00ad3e1c`](#insn-00ad3e1c)
- ブロック [`00ad3e08`](#insn-00ad3e08) 範囲 `[['00ad3e08', '00ad3e13']]`
  - `FALL_THROUGH` [`00ad3e10`](#insn-00ad3e10) → [`00ad3e14`](#insn-00ad3e14)
- ブロック [`00ad3e14`](#insn-00ad3e14) 範囲 `[['00ad3e14', '00ad3e1b']]`
  - `FALL_THROUGH` [`00ad3e18`](#insn-00ad3e18) → [`00ad3e1c`](#insn-00ad3e1c)
- ブロック [`00ad3e1c`](#insn-00ad3e1c) 範囲 `[['00ad3e1c', '00ad3e2b']]`
  - `CONDITIONAL_JUMP` [`00ad3e28`](#insn-00ad3e28) → [`00ad3e94`](#insn-00ad3e94)
  - `FALL_THROUGH` [`00ad3e28`](#insn-00ad3e28) → [`00ad3e2c`](#insn-00ad3e2c)
- ブロック [`00ad3e2c`](#insn-00ad3e2c) 範囲 `[['00ad3e2c', '00ad3e47']]`
- ブロック [`00ad3e94`](#insn-00ad3e94) 範囲 `[['00ad3e94', '00ad3e97']]`

## 命令位置別の参照

- [`00ad3c00`](#insn-00ad3c00) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad3c04`](#insn-00ad3c04) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad3c08`](#insn-00ad3c08) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad3c0c`](#insn-00ad3c0c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad3c10`](#insn-00ad3c10) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad3c2c`](#insn-00ad3c2c) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad3c30`](#insn-00ad3c30) → [`00565f94`](../00565/00565f94.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00565f94` · 推定シンボル `None` · 推定型 `None`
- [`00ad3c50`](#insn-00ad3c50) → `00c1ad78`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00ad3c54`](#insn-00ad3c54) → `00c24db0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ad3c58`](#insn-00ad3c58) → [`00449b7c`](../00449/00449b7c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00449b7c` · 推定シンボル `None` · 推定型 `None`
- [`00ad3c5c`](#insn-00ad3c5c) → [`00ad3d3c`](#insn-00ad3d3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad3c60`](#insn-00ad3c60) → [`00566284`](../00566/00566284.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00566284` · 推定シンボル `None` · 推定型 `None`
- [`00ad3c70`](#insn-00ad3c70) → `002a1e3b`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00ad3c78`](#insn-00ad3c78) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad3c80`](#insn-00ad3c80) → `Stack[-0x77]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad3c84`](#insn-00ad3c84) → `Stack[-0x6f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad3c8c`](#insn-00ad3c8c) → [`00bdb040`](../00bdb/00bdb040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb040` · 推定シンボル `None` · 推定型 `None`
- [`00ad3c9c`](#insn-00ad3c9c) → `002973c2`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00ad3ca0`](#insn-00ad3ca0) → `002973cb`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00ad3ca4`](#insn-00ad3ca4) → `002b1120`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad3ca8`](#insn-00ad3ca8) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad3cb4`](#insn-00ad3cb4) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad3ccc`](#insn-00ad3ccc) → [`00566448`](../00566/00566448.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00566448` · 推定シンボル `None` · 推定型 `None`
- [`00ad3cd0`](#insn-00ad3cd0) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad3cd4`](#insn-00ad3cd4) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad3cd8`](#insn-00ad3cd8) → [`00ad3ce4`](#insn-00ad3ce4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad3cdc`](#insn-00ad3cdc) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad3ce0`](#insn-00ad3ce0) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00ad3ce4`](#insn-00ad3ce4) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad3ce8`](#insn-00ad3ce8) → [`00ad3cf4`](#insn-00ad3cf4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad3cec`](#insn-00ad3cec) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad3cf0`](#insn-00ad3cf0) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00ad3cf8`](#insn-00ad3cf8) → [`0056626c`](../00566/0056626c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0056626c` · 推定シンボル `None` · 推定型 `None`
- [`00ad3cfc`](#insn-00ad3cfc) → [`00ad3e08`](#insn-00ad3e08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad3d00`](#insn-00ad3d00) → `00c24de4`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00ad3d04`](#insn-00ad3d04) → `00c24df0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00ad3d08`](#insn-00ad3d08) → [`00566284`](../00566/00566284.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00566284` · 推定シンボル `None` · 推定型 `None`
- [`00ad3d0c`](#insn-00ad3d0c) → [`00566978`](../00566/00566978.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00566978` · 推定シンボル `None` · 推定型 `None`
- [`00ad3d10`](#insn-00ad3d10) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad3d14`](#insn-00ad3d14) → [`00ad3e1c`](#insn-00ad3e1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad3d34`](#insn-00ad3d34) → [`00551e14`](../00551/00551e14.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00551e14` · 推定シンボル `None` · 推定型 `None`
- [`00ad3d38`](#insn-00ad3d38) → [`00ad3e1c`](#insn-00ad3e1c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad3d3c`](#insn-00ad3d3c) → [`00566284`](../00566/00566284.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00566284` · 推定シンボル `None` · 推定型 `None`
- [`00ad3d4c`](#insn-00ad3d4c) → `002a1e3b`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00ad3d54`](#insn-00ad3d54) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad3d5c`](#insn-00ad3d5c) → `Stack[-0x77]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad3d60`](#insn-00ad3d60) → `Stack[-0x6f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad3d68`](#insn-00ad3d68) → [`00bdb040`](../00bdb/00bdb040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb040` · 推定シンボル `None` · 推定型 `None`
- [`00ad3d78`](#insn-00ad3d78) → `002a4e5b`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00ad3d7c`](#insn-00ad3d7c) → `002a4e6a`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00ad3d80`](#insn-00ad3d80) → `002b0e10`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad3d84`](#insn-00ad3d84) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad3d90`](#insn-00ad3d90) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad3da8`](#insn-00ad3da8) → [`00566448`](../00566/00566448.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00566448` · 推定シンボル `None` · 推定型 `None`
- [`00ad3dac`](#insn-00ad3dac) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad3db0`](#insn-00ad3db0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad3db4`](#insn-00ad3db4) → [`00ad3dc0`](#insn-00ad3dc0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad3db8`](#insn-00ad3db8) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad3dbc`](#insn-00ad3dbc) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00ad3dc0`](#insn-00ad3dc0) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad3dc4`](#insn-00ad3dc4) → [`00ad3dd0`](#insn-00ad3dd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad3dc8`](#insn-00ad3dc8) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad3dcc`](#insn-00ad3dcc) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00ad3dd4`](#insn-00ad3dd4) → [`0056626c`](../00566/0056626c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0056626c` · 推定シンボル `None` · 推定型 `None`
- [`00ad3dd8`](#insn-00ad3dd8) → [`00ad3e08`](#insn-00ad3e08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad3ddc`](#insn-00ad3ddc) → [`00566284`](../00566/00566284.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00566284` · 推定シンボル `None` · 推定型 `None`
- [`00ad3de0`](#insn-00ad3de0) → [`00566978`](../00566/00566978.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00566978` · 推定シンボル `None` · 推定型 `None`
- [`00ad3de4`](#insn-00ad3de4) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad3de8`](#insn-00ad3de8) → [`00ad3e1c`](#insn-00ad3e1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad3e00`](#insn-00ad3e00) → [`00551e14`](../00551/00551e14.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00551e14` · 推定シンボル `None` · 推定型 `None`
- [`00ad3e04`](#insn-00ad3e04) → [`00ad3e1c`](#insn-00ad3e1c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad3e20`](#insn-00ad3e20) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad3e28`](#insn-00ad3e28) → [`00ad3e94`](#insn-00ad3e94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad3e2c`](#insn-00ad3e2c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad3e30`](#insn-00ad3e30) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad3e34`](#insn-00ad3e34) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad3e38`](#insn-00ad3e38) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad3e3c`](#insn-00ad3e3c) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad3e94`](#insn-00ad3e94) → [`00bdb090`](../00bdb/00bdb090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb090` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00ad3c00`](#insn-00ad3c00)

~~~json
{
  "source": "00ad3c00",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad3c04`](#insn-00ad3c04)

~~~json
{
  "source": "00ad3c04",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad3c08`](#insn-00ad3c08)

~~~json
{
  "source": "00ad3c08",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad3c0c`](#insn-00ad3c0c)

~~~json
{
  "source": "00ad3c0c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad3c10`](#insn-00ad3c10)

~~~json
{
  "source": "00ad3c10",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad3c2c`](#insn-00ad3c2c)

~~~json
{
  "source": "00ad3c2c",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad3c30`](#insn-00ad3c30)

~~~json
{
  "source": "00ad3c30",
  "target": "00565f94",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad3c50`](#insn-00ad3c50)

~~~json
{
  "source": "00ad3c50",
  "target": "00c1ad78",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1ad78",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00ad3c54`](#insn-00ad3c54)

~~~json
{
  "source": "00ad3c54",
  "target": "00c24db0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24db0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ad3c58`](#insn-00ad3c58)

~~~json
{
  "source": "00ad3c58",
  "target": "00449b7c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad3c5c`](#insn-00ad3c5c)

~~~json
{
  "source": "00ad3c5c",
  "target": "00ad3d3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad3c60`](#insn-00ad3c60)

~~~json
{
  "source": "00ad3c60",
  "target": "00566284",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad3c70`](#insn-00ad3c70)

~~~json
{
  "source": "00ad3c70",
  "target": "002a1e3b",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a1e3b",
  "offset": 0,
  "size": 10,
  "datatype": "string",
  "bytes": "61646d6f6253686f7700",
  "capture_start": "002a1e3b",
  "capture_bytes": 10,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ad3c78`](#insn-00ad3c78)

~~~json
{
  "source": "00ad3c78",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad3c80`](#insn-00ad3c80)

~~~json
{
  "source": "00ad3c80",
  "target": "Stack[-0x77]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad3c84`](#insn-00ad3c84)

~~~json
{
  "source": "00ad3c84",
  "target": "Stack[-0x6f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad3c8c`](#insn-00ad3c8c)

~~~json
{
  "source": "00ad3c8c",
  "target": "00bdb040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad3c9c`](#insn-00ad3c9c)

~~~json
{
  "source": "00ad3c9c",
  "target": "002973c2",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002973c2",
  "offset": 0,
  "size": 26,
  "datatype": "string",
  "bytes": "284c6a6176612f6c616e672f537472696e673b465a4949295600",
  "capture_start": "002973c2",
  "capture_bytes": 26,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ad3ca0`](#insn-00ad3ca0)

~~~json
{
  "source": "00ad3ca0",
  "target": "002973cb",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002973c2",
  "offset": 9,
  "size": 26,
  "datatype": "string",
  "bytes": "284c6a6176612f6c616e672f537472696e673b465a4949295600",
  "capture_start": "002973c2",
  "capture_bytes": 26,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ad3ca4`](#insn-00ad3ca4)

~~~json
{
  "source": "00ad3ca4",
  "target": "002b1120",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad3ca8`](#insn-00ad3ca8)

~~~json
{
  "source": "00ad3ca8",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad3cb4`](#insn-00ad3cb4)

~~~json
{
  "source": "00ad3cb4",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad3ccc`](#insn-00ad3ccc)

~~~json
{
  "source": "00ad3ccc",
  "target": "00566448",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad3cd0`](#insn-00ad3cd0)

~~~json
{
  "source": "00ad3cd0",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad3cd4`](#insn-00ad3cd4)

~~~json
{
  "source": "00ad3cd4",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad3cd8`](#insn-00ad3cd8)

~~~json
{
  "source": "00ad3cd8",
  "target": "00ad3ce4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad3cdc`](#insn-00ad3cdc)

~~~json
{
  "source": "00ad3cdc",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad3ce0`](#insn-00ad3ce0)

~~~json
{
  "source": "00ad3ce0",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad3ce4`](#insn-00ad3ce4)

~~~json
{
  "source": "00ad3ce4",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad3ce8`](#insn-00ad3ce8)

~~~json
{
  "source": "00ad3ce8",
  "target": "00ad3cf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad3cec`](#insn-00ad3cec)

~~~json
{
  "source": "00ad3cec",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad3cf0`](#insn-00ad3cf0)

~~~json
{
  "source": "00ad3cf0",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad3cf8`](#insn-00ad3cf8)

~~~json
{
  "source": "00ad3cf8",
  "target": "0056626c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad3cfc`](#insn-00ad3cfc)

~~~json
{
  "source": "00ad3cfc",
  "target": "00ad3e08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad3d00`](#insn-00ad3d00)

~~~json
{
  "source": "00ad3d00",
  "target": "00c24de4",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24de4",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ad3d04`](#insn-00ad3d04)

~~~json
{
  "source": "00ad3d04",
  "target": "00c24df0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24df0",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ad3d08`](#insn-00ad3d08)

~~~json
{
  "source": "00ad3d08",
  "target": "00566284",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad3d0c`](#insn-00ad3d0c)

~~~json
{
  "source": "00ad3d0c",
  "target": "00566978",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad3d10`](#insn-00ad3d10)

~~~json
{
  "source": "00ad3d10",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad3d14`](#insn-00ad3d14)

~~~json
{
  "source": "00ad3d14",
  "target": "00ad3e1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad3d34`](#insn-00ad3d34)

~~~json
{
  "source": "00ad3d34",
  "target": "00551e14",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad3d38`](#insn-00ad3d38)

~~~json
{
  "source": "00ad3d38",
  "target": "00ad3e1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad3d3c`](#insn-00ad3d3c)

~~~json
{
  "source": "00ad3d3c",
  "target": "00566284",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad3d4c`](#insn-00ad3d4c)

~~~json
{
  "source": "00ad3d4c",
  "target": "002a1e3b",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a1e3b",
  "offset": 0,
  "size": 10,
  "datatype": "string",
  "bytes": "61646d6f6253686f7700",
  "capture_start": "002a1e3b",
  "capture_bytes": 10,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ad3d54`](#insn-00ad3d54)

~~~json
{
  "source": "00ad3d54",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad3d5c`](#insn-00ad3d5c)

~~~json
{
  "source": "00ad3d5c",
  "target": "Stack[-0x77]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad3d60`](#insn-00ad3d60)

~~~json
{
  "source": "00ad3d60",
  "target": "Stack[-0x6f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad3d68`](#insn-00ad3d68)

~~~json
{
  "source": "00ad3d68",
  "target": "00bdb040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad3d78`](#insn-00ad3d78)

~~~json
{
  "source": "00ad3d78",
  "target": "002a4e5b",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a4e5b",
  "offset": 0,
  "size": 24,
  "datatype": "string",
  "bytes": "284c6a6176612f6c616e672f537472696e673b465a295600",
  "capture_start": "002a4e5b",
  "capture_bytes": 24,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ad3d7c`](#insn-00ad3d7c)

~~~json
{
  "source": "00ad3d7c",
  "target": "002a4e6a",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a4e5b",
  "offset": 15,
  "size": 24,
  "datatype": "string",
  "bytes": "284c6a6176612f6c616e672f537472696e673b465a295600",
  "capture_start": "002a4e5b",
  "capture_bytes": 24,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ad3d80`](#insn-00ad3d80)

~~~json
{
  "source": "00ad3d80",
  "target": "002b0e10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad3d84`](#insn-00ad3d84)

~~~json
{
  "source": "00ad3d84",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad3d90`](#insn-00ad3d90)

~~~json
{
  "source": "00ad3d90",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad3da8`](#insn-00ad3da8)

~~~json
{
  "source": "00ad3da8",
  "target": "00566448",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad3dac`](#insn-00ad3dac)

~~~json
{
  "source": "00ad3dac",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad3db0`](#insn-00ad3db0)

~~~json
{
  "source": "00ad3db0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad3db4`](#insn-00ad3db4)

~~~json
{
  "source": "00ad3db4",
  "target": "00ad3dc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad3db8`](#insn-00ad3db8)

~~~json
{
  "source": "00ad3db8",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad3dbc`](#insn-00ad3dbc)

~~~json
{
  "source": "00ad3dbc",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad3dc0`](#insn-00ad3dc0)

~~~json
{
  "source": "00ad3dc0",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad3dc4`](#insn-00ad3dc4)

~~~json
{
  "source": "00ad3dc4",
  "target": "00ad3dd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad3dc8`](#insn-00ad3dc8)

~~~json
{
  "source": "00ad3dc8",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad3dcc`](#insn-00ad3dcc)

~~~json
{
  "source": "00ad3dcc",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad3dd4`](#insn-00ad3dd4)

~~~json
{
  "source": "00ad3dd4",
  "target": "0056626c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad3dd8`](#insn-00ad3dd8)

~~~json
{
  "source": "00ad3dd8",
  "target": "00ad3e08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad3ddc`](#insn-00ad3ddc)

~~~json
{
  "source": "00ad3ddc",
  "target": "00566284",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad3de0`](#insn-00ad3de0)

~~~json
{
  "source": "00ad3de0",
  "target": "00566978",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad3de4`](#insn-00ad3de4)

~~~json
{
  "source": "00ad3de4",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad3de8`](#insn-00ad3de8)

~~~json
{
  "source": "00ad3de8",
  "target": "00ad3e1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad3e00`](#insn-00ad3e00)

~~~json
{
  "source": "00ad3e00",
  "target": "00551e14",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad3e04`](#insn-00ad3e04)

~~~json
{
  "source": "00ad3e04",
  "target": "00ad3e1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad3e20`](#insn-00ad3e20)

~~~json
{
  "source": "00ad3e20",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad3e28`](#insn-00ad3e28)

~~~json
{
  "source": "00ad3e28",
  "target": "00ad3e94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad3e2c`](#insn-00ad3e2c)

~~~json
{
  "source": "00ad3e2c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad3e30`](#insn-00ad3e30)

~~~json
{
  "source": "00ad3e30",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad3e34`](#insn-00ad3e34)

~~~json
{
  "source": "00ad3e34",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad3e38`](#insn-00ad3e38)

~~~json
{
  "source": "00ad3e38",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad3e3c`](#insn-00ad3e3c)

~~~json
{
  "source": "00ad3e3c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad3e94`](#insn-00ad3e94)

~~~json
{
  "source": "00ad3e94",
  "target": "00bdb090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
