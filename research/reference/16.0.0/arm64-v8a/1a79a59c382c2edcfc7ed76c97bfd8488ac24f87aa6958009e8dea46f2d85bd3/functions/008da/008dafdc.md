# 008dafdc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `008a7144`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a7/008a7144.md) · 移動量 `+0x33e98`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0044.md#compare-1c36700b5764fd1c340fc36c73092c38)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `008db178`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008db/008db178.md) · 移動量 `+0x19c`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0050.md#compare-fde9b78768b2bd92445a5d9defb98175)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "008dafdc",
  "name": "_INIT_172",
  "size": 708,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ed30e8761d7359fec2045ac062b497d03914d3ec3ff052d4206c3e7dd09ff334",
  "source_text_sha256": "ed30e8761d7359fec2045ac062b497d03914d3ec3ff052d4206c3e7dd09ff334",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "008dafdc",
        "008db29b"
      ],
      [
        "008db368",
        "008db36b"
      ]
    ],
    "bytes_sha256": "f82d78b7408c4c3aba8e3aff92a84e827c1e8b0295f25db60ff298184530e713",
    "instruction_count": 177,
    "instruction_bytes": 708,
    "body_bytes": 708,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0043b7b8](../0043b/0043b7b8.md)
- [00c57a30](../00c57/00c57a30.md)
- [00c57ab0](../00c57/00c57ab0.md)
- [00c57ae0](../00c57/00c57ae0.md)

## 関連文字列（未確認候補）

~~~text
"CgkIjM3y_ZQaEAIQAg"
"CgkIjM3y_ZQaEAIQAw"
"CgkIjM3y_ZQaEAIQBA"
"CgkIjM3y_ZQaEAIQBQ"
"CgkIjM3y_ZQaEAIQBg"
"CgkIjM3y_ZQaEAIQBw"
"CgkIjM3y_ZQaEAIQCA"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 5208 bytes

~~~c

/* WARNING: Type propagation algorithm not settling */

void _INIT_172(void)

{
  long lVar1;
  undefined4 local_118 [2];
  byte local_110;
  char local_10f [8];
  undefined7 uStack_107;
  char cStack_100;
  undefined2 uStack_ff;
  undefined1 uStack_fd;
  undefined4 uStack_fc;
  undefined4 local_f8 [2];
  byte local_f0;
  char local_ef [8];
  undefined7 uStack_e7;
  char cStack_e0;
  undefined2 uStack_df;
  undefined1 uStack_dd;
  undefined4 uStack_dc;
  undefined4 local_d8 [2];
  byte local_d0;
  char local_cf [8];
  undefined7 uStack_c7;
  char cStack_c0;
  undefined2 uStack_bf;
  undefined1 uStack_bd;
  undefined4 uStack_bc;
  undefined4 local_b8 [2];
  byte local_b0;
  char local_af [8];
  undefined7 uStack_a7;
  char cStack_a0;
  undefined2 uStack_9f;
  undefined1 uStack_9d;
  undefined4 uStack_9c;
  undefined4 local_98 [2];
  byte local_90;
  char local_8f [8];
  undefined7 uStack_87;
  char cStack_80;
  undefined2 uStack_7f;
  undefined1 uStack_7d;
  undefined4 uStack_7c;
  undefined4 local_78 [2];
  byte local_70;
  char local_6f [8];
  undefined7 uStack_67;
  char cStack_60;
  undefined2 uStack_5f;
  undefined1 uStack_5d;
  undefined4 uStack_5c;
  undefined4 local_58 [2];
  byte local_50;
  char local_4f [8];
  undefined7 uStack_47;
  char cStack_40;
  undefined2 uStack_3f;
  undefined1 uStack_3d;
  undefined4 uStack_3c;
  long local_38;
  
  lVar1 = tpidr_el0;
  local_38 = *(long *)(lVar1 + 0x28);
  uStack_ff = 0x6741;
  local_f8[0] = 1;
  uStack_107 = (undefined7)s_CgkIjM3y_ZQaEAIQAg_002b7ee6._8_8_;
  cStack_100 = SUB81(s_CgkIjM3y_ZQaEAIQAg_002b7ee6._8_8_,7);
  local_10f = (char  [8])s_CgkIjM3y_ZQaEAIQAg_002b7ee6._0_8_;
  uStack_df = 0x4142;
  local_d8[0] = 2;
  uStack_e7 = (undefined7)s_CgkIjM3y_ZQaEAIQBA_002b7ef9._8_8_;
  cStack_e0 = SUB81(s_CgkIjM3y_ZQaEAIQBA_002b7ef9._8_8_,7);
  local_ef = (char  [8])s_CgkIjM3y_ZQaEAIQBA_002b7ef9._0_8_;
  uStack_bf = 0x6742;
  local_b8[0] = 3;
  uStack_c7 = (undefined7)s_CgkIjM3y_ZQaEAIQBg_002b8d82._8_8_;
  cStack_c0 = SUB81(s_CgkIjM3y_ZQaEAIQBg_002b8d82._8_8_,7);
  local_cf = (char  [8])s_CgkIjM3y_ZQaEAIQBg_002b8d82._0_8_;
  uStack_9f = 0x7741;
  local_98[0] = 4;
  uStack_a7 = (undefined7)s_CgkIjM3y_ZQaEAIQAw_002a2e95._8_8_;
  cStack_a0 = SUB81(s_CgkIjM3y_ZQaEAIQAw_002a2e95._8_8_,7);
  local_af = (char  [8])s_CgkIjM3y_ZQaEAIQAw_002a2e95._0_8_;
  uStack_7f = 0x5142;
  local_78[0] = 5;
  uStack_87 = (undefined7)s_CgkIjM3y_ZQaEAIQBQ_002ac592._8_8_;
  cStack_80 = SUB81(s_CgkIjM3y_ZQaEAIQBQ_002ac592._8_8_,7);
  local_8f = (char  [8])s_CgkIjM3y_ZQaEAIQBQ_002ac592._0_8_;
  uStack_5f = 0x7742;
  local_58[0] = 6;
  uStack_67 = (undefined7)s_CgkIjM3y_ZQaEAIQBw_002a0e90._8_8_;
  cStack_60 = SUB81(s_CgkIjM3y_ZQaEAIQBw_002a0e90._8_8_,7);
  local_6f = (char  [8])s_CgkIjM3y_ZQaEAIQBw_002a0e90._0_8_;
  local_110 = 0x24;
  local_f0 = 0x24;
  local_d0 = 0x24;
  local_b0 = 0x24;
  local_90 = 0x24;
  local_70 = 0x24;
  local_50 = 0x24;
  local_118[0] = 0;
  uStack_fd = 0;
  uStack_dd = 0;
  uStack_bd = 0;
  uStack_9d = 0;
  uStack_7d = 0;
  uStack_5d = 0;
  uStack_3f = 0x4143;
  uStack_47 = (undefined7)s_CgkIjM3y_ZQaEAIQCA_002a3e3c._8_8_;
  cStack_40 = SUB81(s_CgkIjM3y_ZQaEAIQCA_002a3e3c._8_8_,7);
  local_4f = (char  [8])s_CgkIjM3y_ZQaEAIQCA_002a3e3c._0_8_;
  uStack_3d = 0;
  DAT_01123580 = 0;
  DAT_01123578 = 0;
  DAT_01123570 = &DAT_01123578;
  FUN_0043b7b8(&DAT_01123570,&DAT_01123578,local_118,local_118);
  FUN_0043b7b8(&DAT_01123570,&DAT_01123578,local_f8,local_f8);
  FUN_0043b7b8(&DAT_01123570,&DAT_01123578,local_d8,local_d8);
  FUN_0043b7b8(&DAT_01123570,&DAT_01123578,local_b8,local_b8);
  FUN_0043b7b8(&DAT_01123570,&DAT_01123578,local_98,local_98);
  FUN_0043b7b8(&DAT_01123570,&DAT_01123578,local_78,local_78);
  FUN_0043b7b8(&DAT_01123570,&DAT_01123578,local_58,local_58);
  if ((local_50 & 1) != 0) {
    _ZdlPv((void *)CONCAT44(uStack_3c,CONCAT13(uStack_3d,CONCAT21(uStack_3f,cStack_40))));
  }
  if ((local_70 & 1) != 0) {
    _ZdlPv((void *)CONCAT44(uStack_5c,CONCAT13(uStack_5d,CONCAT21(uStack_5f,cStack_60))));
  }
  if ((local_90 & 1) != 0) {
    _ZdlPv((void *)CONCAT44(uStack_7c,CONCAT13(uStack_7d,CONCAT21(uStack_7f,cStack_80))));
  }
  if ((local_b0 & 1) != 0) {
    _ZdlPv((void *)CONCAT44(uStack_9c,CONCAT13(uStack_9d,CONCAT21(uStack_9f,cStack_a0))));
  }
  if ((local_d0 & 1) != 0) {
    _ZdlPv((void *)CONCAT44(uStack_bc,CONCAT13(uStack_bd,CONCAT21(uStack_bf,cStack_c0))));
  }
  if ((local_f0 & 1) != 0) {
                    /* catch() { ... } // from try @ 008d9788 with catch @ 008db288 */
                    /* catch() { ... } // from try @ 008d977c with catch @ 008db28c */
    _ZdlPv((void *)CONCAT44(uStack_dc,CONCAT13(uStack_dd,CONCAT21(uStack_df,cStack_e0))));
                    /* catch() { ... } // from try @ 008d9738 with catch @ 008db290 */
                    /* catch() { ... } // from try @ 008d972c with catch @ 008db294 */
  }
  if ((local_110 & 1) != 0) {
    _ZdlPv((void *)CONCAT44(uStack_fc,CONCAT13(uStack_fd,CONCAT21(uStack_ff,cStack_100))));
  }
  __cxa_atexit(FUN_0043ae30,&DAT_01123570,&PTR_LOOP_00c62b90);
  if (*(long *)(lVar1 + 0x28) == local_38) {
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
<a id="insn-008dafdc"></a> `008dafdc` | `ff 83 04 d1` | sub sp,sp,#0x120 | `FALL_THROUGH`
<a id="insn-008dafe0"></a> `008dafe0` | `fd 7b 0f a9` | stp x29,x30,[sp, #0xf0] | `FALL_THROUGH`
<a id="insn-008dafe4"></a> `008dafe4` | `fc 57 10 a9` | stp x28,x21,[sp, #0x100] | `FALL_THROUGH`
<a id="insn-008dafe8"></a> `008dafe8` | `f4 4f 11 a9` | stp x20,x19,[sp, #0x110] | `FALL_THROUGH`
<a id="insn-008dafec"></a> `008dafec` | `fd c3 03 91` | add x29,sp,#0xf0 | `FALL_THROUGH`
<a id="insn-008daff0"></a> `008daff0` | `55 d0 3b d5` | mrs x21,tpidr_el0 | `FALL_THROUGH`
<a id="insn-008daff4"></a> `008daff4` | `2a e8 8c 52` | mov w10,#0x6741 | `FALL_THROUGH`
<a id="insn-008daff8"></a> `008daff8` | `f4 23 00 91` | add x20,sp,#0x8 | `FALL_THROUGH`
<a id="insn-008daffc"></a> `008daffc` | `a9 16 40 f9` | ldr x9,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-008db000"></a> `008db000` | `88 04 80 52` | mov w8,#0x24 | `FALL_THROUGH`
<a id="insn-008db004"></a> `008db004` | `53 42 00 90` | adrp x19,0x1123000 | `FALL_THROUGH`
<a id="insn-008db008"></a> `008db008` | `73 c2 15 91` | add x19,x19,#0x570 | `FALL_THROUGH`
<a id="insn-008db00c"></a> `008db00c` | `a9 83 1f f8` | stur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-008db010"></a> `008db010` | `e9 ce ff 90` | adrp x9,0x2b7000 | `FALL_THROUGH`
<a id="insn-008db014"></a> `008db014` | `29 99 3b 91` | add x9,x9,#0xee6 | `FALL_THROUGH`
<a id="insn-008db018"></a> `008db018` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-008db01c"></a> `008db01c` | `29 00 80 52` | mov w9,#0x1 | `FALL_THROUGH`
<a id="insn-008db020"></a> `008db020` | `ea 13 02 78` | sturh w10,[sp, #0x21] | `FALL_THROUGH`
<a id="insn-008db024"></a> `008db024` | `e9 2b 00 b9` | str w9,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-008db028"></a> `008db028` | `49 28 88 52` | mov w9,#0x4142 | `FALL_THROUGH`
<a id="insn-008db02c"></a> `008db02c` | `ea ce ff 90` | adrp x10,0x2b7000 | `FALL_THROUGH`
<a id="insn-008db030"></a> `008db030` | `4a e5 3b 91` | add x10,x10,#0xef9 | `FALL_THROUGH`
<a id="insn-008db034"></a> `008db034` | `e0 13 81 3c` | stur q0,[sp, #0x11] | `FALL_THROUGH`
<a id="insn-008db038"></a> `008db038` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-008db03c"></a> `008db03c` | `40 01 c0 3d` | ldr q0,[x10] | `FALL_THROUGH`
<a id="insn-008db040"></a> `008db040` | `e9 13 04 78` | sturh w9,[sp, #0x41] | `FALL_THROUGH`
<a id="insn-008db044"></a> `008db044` | `49 00 80 52` | mov w9,#0x2 | `FALL_THROUGH`
<a id="insn-008db048"></a> `008db048` | `e9 4b 00 b9` | str w9,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-008db04c"></a> `008db04c` | `49 e8 8c 52` | mov w9,#0x6742 | `FALL_THROUGH`
<a id="insn-008db050"></a> `008db050` | `ea ce ff b0` | adrp x10,0x2b8000 | `FALL_THROUGH`
<a id="insn-008db054"></a> `008db054` | `4a 09 36 91` | add x10,x10,#0xd82 | `FALL_THROUGH`
<a id="insn-008db058"></a> `008db058` | `e0 13 83 3c` | stur q0,[sp, #0x31] | `FALL_THROUGH`
<a id="insn-008db05c"></a> `008db05c` | `40 01 c0 3d` | ldr q0,[x10] | `FALL_THROUGH`
<a id="insn-008db060"></a> `008db060` | `e9 13 06 78` | sturh w9,[sp, #0x61] | `FALL_THROUGH`
<a id="insn-008db064"></a> `008db064` | `69 00 80 52` | mov w9,#0x3 | `FALL_THROUGH`
<a id="insn-008db068"></a> `008db068` | `e9 6b 00 b9` | str w9,[sp, #0x68] | `FALL_THROUGH`
<a id="insn-008db06c"></a> `008db06c` | `29 e8 8e 52` | mov w9,#0x7741 | `FALL_THROUGH`
<a id="insn-008db070"></a> `008db070` | `2a ce ff f0` | adrp x10,0x2a2000 | `FALL_THROUGH`
<a id="insn-008db074"></a> `008db074` | `4a 55 3a 91` | add x10,x10,#0xe95 | `FALL_THROUGH`
<a id="insn-008db078"></a> `008db078` | `e0 13 85 3c` | stur q0,[sp, #0x51] | `FALL_THROUGH`
<a id="insn-008db07c"></a> `008db07c` | `40 01 c0 3d` | ldr q0,[x10] | `FALL_THROUGH`
<a id="insn-008db080"></a> `008db080` | `e9 13 08 78` | sturh w9,[sp, #0x81] | `FALL_THROUGH`
<a id="insn-008db084"></a> `008db084` | `89 00 80 52` | mov w9,#0x4 | `FALL_THROUGH`
<a id="insn-008db088"></a> `008db088` | `e9 8b 00 b9` | str w9,[sp, #0x88] | `FALL_THROUGH`
<a id="insn-008db08c"></a> `008db08c` | `89 ce ff b0` | adrp x9,0x2ac000 | `FALL_THROUGH`
<a id="insn-008db090"></a> `008db090` | `29 49 16 91` | add x9,x9,#0x592 | `FALL_THROUGH`
<a id="insn-008db094"></a> `008db094` | `e0 13 87 3c` | stur q0,[sp, #0x71] | `FALL_THROUGH`
<a id="insn-008db098"></a> `008db098` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-008db09c"></a> `008db09c` | `49 28 8a 52` | mov w9,#0x5142 | `FALL_THROUGH`
<a id="insn-008db0a0"></a> `008db0a0` | `89 92 09 78` | sturh w9,[x20, #0x99] | `FALL_THROUGH`
<a id="insn-008db0a4"></a> `008db0a4` | `a9 00 80 52` | mov w9,#0x5 | `FALL_THROUGH`
<a id="insn-008db0a8"></a> `008db0a8` | `e9 ab 00 b9` | str w9,[sp, #0xa8] | `FALL_THROUGH`
<a id="insn-008db0ac"></a> `008db0ac` | `29 ce ff b0` | adrp x9,0x2a0000 | `FALL_THROUGH`
<a id="insn-008db0b0"></a> `008db0b0` | `29 41 3a 91` | add x9,x9,#0xe90 | `FALL_THROUGH`
<a id="insn-008db0b4"></a> `008db0b4` | `80 92 88 3c` | stur q0,[x20, #0x89] | `FALL_THROUGH`
<a id="insn-008db0b8"></a> `008db0b8` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-008db0bc"></a> `008db0bc` | `49 e8 8e 52` | mov w9,#0x7742 | `FALL_THROUGH`
<a id="insn-008db0c0"></a> `008db0c0` | `89 92 0b 78` | sturh w9,[x20, #0xb9] | `FALL_THROUGH`
<a id="insn-008db0c4"></a> `008db0c4` | `c9 00 80 52` | mov w9,#0x6 | `FALL_THROUGH`
<a id="insn-008db0c8"></a> `008db0c8` | `e9 cb 00 b9` | str w9,[sp, #0xc8] | `FALL_THROUGH`
<a id="insn-008db0cc"></a> `008db0cc` | `49 ce ff 90` | adrp x9,0x2a3000 | `FALL_THROUGH`
<a id="insn-008db0d0"></a> `008db0d0` | `29 f1 38 91` | add x9,x9,#0xe3c | `FALL_THROUGH`
<a id="insn-008db0d4"></a> `008db0d4` | `80 92 8a 3c` | stur q0,[x20, #0xa9] | `FALL_THROUGH`
<a id="insn-008db0d8"></a> `008db0d8` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-008db0dc"></a> `008db0dc` | `e8 43 00 39` | strb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-008db0e0"></a> `008db0e0` | `e8 c3 00 39` | strb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-008db0e4"></a> `008db0e4` | `e8 43 01 39` | strb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-008db0e8"></a> `008db0e8` | `e8 c3 01 39` | strb w8,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-008db0ec"></a> `008db0ec` | `e8 43 02 39` | strb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-008db0f0"></a> `008db0f0` | `e8 c3 02 39` | strb w8,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-008db0f4"></a> `008db0f4` | `e8 43 03 39` | strb w8,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-008db0f8"></a> `008db0f8` | `68 28 88 52` | mov w8,#0x4143 | `FALL_THROUGH`
<a id="insn-008db0fc"></a> `008db0fc` | `ff 0b 00 b9` | str wzr,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-008db100"></a> `008db100` | `ff 8f 00 39` | strb wzr,[sp, #0x23] | `FALL_THROUGH`
<a id="insn-008db104"></a> `008db104` | `ff 0f 01 39` | strb wzr,[sp, #0x43] | `FALL_THROUGH`
<a id="insn-008db108"></a> `008db108` | `ff 8f 01 39` | strb wzr,[sp, #0x63] | `FALL_THROUGH`
<a id="insn-008db10c"></a> `008db10c` | `ff 0f 02 39` | strb wzr,[sp, #0x83] | `FALL_THROUGH`
<a id="insn-008db110"></a> `008db110` | `ff 8f 02 39` | strb wzr,[sp, #0xa3] | `FALL_THROUGH`
<a id="insn-008db114"></a> `008db114` | `ff 0f 03 39` | strb wzr,[sp, #0xc3] | `FALL_THROUGH`
<a id="insn-008db118"></a> `008db118` | `88 92 0d 78` | sturh w8,[x20, #0xd9] | `FALL_THROUGH`
<a id="insn-008db11c"></a> `008db11c` | `80 92 8c 3c` | stur q0,[x20, #0xc9] | `FALL_THROUGH`
<a id="insn-008db120"></a> `008db120` | `ff 8f 03 39` | strb wzr,[sp, #0xe3] | `FALL_THROUGH`
<a id="insn-008db124"></a> `008db124` | `7f 0a 00 f9` | str xzr,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-008db128"></a> `008db128` | `3f 8c 00 f8` | str xzr,[x1, #0x8]! | `FALL_THROUGH`
<a id="insn-008db12c"></a> `008db12c` | `61 02 00 f9` | str x1,[x19] | `FALL_THROUGH`
<a id="insn-008db130"></a> `008db130` | `e2 23 00 91` | add x2,sp,#0x8 | `FALL_THROUGH`
<a id="insn-008db134"></a> `008db134` | `e3 23 00 91` | add x3,sp,#0x8 | `FALL_THROUGH`
<a id="insn-008db138"></a> `008db138` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-008db13c"></a> `008db13c` | `9f 81 ed 97` | bl 0x0043b7b8 | `UNCONDITIONAL_CALL`
<a id="insn-008db140"></a> `008db140` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-008db144"></a> `008db144` | `82 82 00 91` | add x2,x20,#0x20 | `FALL_THROUGH`
<a id="insn-008db148"></a> `008db148` | `83 82 00 91` | add x3,x20,#0x20 | `FALL_THROUGH`
<a id="insn-008db14c"></a> `008db14c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-008db150"></a> `008db150` | `9a 81 ed 97` | bl 0x0043b7b8 | `UNCONDITIONAL_CALL`
<a id="insn-008db154"></a> `008db154` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-008db158"></a> `008db158` | `82 02 01 91` | add x2,x20,#0x40 | `FALL_THROUGH`
<a id="insn-008db15c"></a> `008db15c` | `83 02 01 91` | add x3,x20,#0x40 | `FALL_THROUGH`
<a id="insn-008db160"></a> `008db160` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-008db164"></a> `008db164` | `95 81 ed 97` | bl 0x0043b7b8 | `UNCONDITIONAL_CALL`
<a id="insn-008db168"></a> `008db168` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-008db16c"></a> `008db16c` | `82 82 01 91` | add x2,x20,#0x60 | `FALL_THROUGH`
<a id="insn-008db170"></a> `008db170` | `83 82 01 91` | add x3,x20,#0x60 | `FALL_THROUGH`
<a id="insn-008db174"></a> `008db174` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-008db178"></a> `008db178` | `90 81 ed 97` | bl 0x0043b7b8 | `UNCONDITIONAL_CALL`
<a id="insn-008db17c"></a> `008db17c` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-008db180"></a> `008db180` | `82 02 02 91` | add x2,x20,#0x80 | `FALL_THROUGH`
<a id="insn-008db184"></a> `008db184` | `83 02 02 91` | add x3,x20,#0x80 | `FALL_THROUGH`
<a id="insn-008db188"></a> `008db188` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-008db18c"></a> `008db18c` | `8b 81 ed 97` | bl 0x0043b7b8 | `UNCONDITIONAL_CALL`
<a id="insn-008db190"></a> `008db190` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-008db194"></a> `008db194` | `82 82 02 91` | add x2,x20,#0xa0 | `FALL_THROUGH`
<a id="insn-008db198"></a> `008db198` | `83 82 02 91` | add x3,x20,#0xa0 | `FALL_THROUGH`
<a id="insn-008db19c"></a> `008db19c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-008db1a0"></a> `008db1a0` | `86 81 ed 97` | bl 0x0043b7b8 | `UNCONDITIONAL_CALL`
<a id="insn-008db1a4"></a> `008db1a4` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-008db1a8"></a> `008db1a8` | `82 02 03 91` | add x2,x20,#0xc0 | `FALL_THROUGH`
<a id="insn-008db1ac"></a> `008db1ac` | `83 02 03 91` | add x3,x20,#0xc0 | `FALL_THROUGH`
<a id="insn-008db1b0"></a> `008db1b0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-008db1b4"></a> `008db1b4` | `81 81 ed 97` | bl 0x0043b7b8 | `UNCONDITIONAL_CALL`
<a id="insn-008db1b8"></a> `008db1b8` | `e8 43 43 39` | ldrb w8,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-008db1bc"></a> `008db1bc` | `e8 03 00 37` | tbnz w8,#0x0,0x008db238 | `CONDITIONAL_JUMP`
<a id="insn-008db1c0"></a> `008db1c0` | `e8 c3 42 39` | ldrb w8,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-008db1c4"></a> `008db1c4` | `28 04 00 37` | tbnz w8,#0x0,0x008db248 | `CONDITIONAL_JUMP`
<a id="insn-008db1c8"></a> `008db1c8` | `e8 43 42 39` | ldrb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-008db1cc"></a> `008db1cc` | `68 04 00 37` | tbnz w8,#0x0,0x008db258 | `CONDITIONAL_JUMP`
<a id="insn-008db1d0"></a> `008db1d0` | `e8 c3 41 39` | ldrb w8,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-008db1d4"></a> `008db1d4` | `a8 04 00 37` | tbnz w8,#0x0,0x008db268 | `CONDITIONAL_JUMP`
<a id="insn-008db1d8"></a> `008db1d8` | `e8 43 41 39` | ldrb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-008db1dc"></a> `008db1dc` | `e8 04 00 37` | tbnz w8,#0x0,0x008db278 | `CONDITIONAL_JUMP`
<a id="insn-008db1e0"></a> `008db1e0` | `e8 c3 40 39` | ldrb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-008db1e4"></a> `008db1e4` | `28 05 00 37` | tbnz w8,#0x0,0x008db288 | `CONDITIONAL_JUMP`
<a id="insn-008db1e8"></a> `008db1e8` | `e8 43 40 39` | ldrb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-008db1ec"></a> `008db1ec` | `68 00 00 36` | tbz w8,#0x0,0x008db1f8 | `CONDITIONAL_JUMP`
<a id="insn-008db1f0"></a> `008db1f0` | `e0 13 40 f9` | ldr x0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-008db1f4"></a> `008db1f4` | `2f f2 0d 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-008db1f8"></a> `008db1f8` | `e0 da ff f0` | adrp x0,0x43a000 | `FALL_THROUGH`
<a id="insn-008db1fc"></a> `008db1fc` | `00 c0 38 91` | add x0,x0,#0xe30 | `FALL_THROUGH`
<a id="insn-008db200"></a> `008db200` | `41 42 00 90` | adrp x1,0x1123000 | `FALL_THROUGH`
<a id="insn-008db204"></a> `008db204` | `21 c0 15 91` | add x1,x1,#0x570 | `FALL_THROUGH`
<a id="insn-008db208"></a> `008db208` | `22 1c 00 f0` | adrp x2,0xc62000 | `FALL_THROUGH`
<a id="insn-008db20c"></a> `008db20c` | `42 40 2e 91` | add x2,x2,#0xb90 | `FALL_THROUGH`
<a id="insn-008db210"></a> `008db210` | `08 f2 0d 94` | bl 0x00c57a30 | `UNCONDITIONAL_CALL`
<a id="insn-008db214"></a> `008db214` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-008db218"></a> `008db218` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-008db21c"></a> `008db21c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-008db220"></a> `008db220` | `41 0a 00 54` | b.ne 0x008db368 | `CONDITIONAL_JUMP`
<a id="insn-008db224"></a> `008db224` | `f4 4f 51 a9` | ldp x20,x19,[sp, #0x110] | `FALL_THROUGH`
<a id="insn-008db228"></a> `008db228` | `fc 57 50 a9` | ldp x28,x21,[sp, #0x100] | `FALL_THROUGH`
<a id="insn-008db22c"></a> `008db22c` | `fd 7b 4f a9` | ldp x29,x30,[sp, #0xf0] | `FALL_THROUGH`
<a id="insn-008db230"></a> `008db230` | `ff 83 04 91` | add sp,sp,#0x120 | `FALL_THROUGH`
<a id="insn-008db234"></a> `008db234` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-008db238"></a> `008db238` | `e0 73 40 f9` | ldr x0,[sp, #0xe0] | `FALL_THROUGH`
<a id="insn-008db23c"></a> `008db23c` | `1d f2 0d 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-008db240"></a> `008db240` | `e8 c3 42 39` | ldrb w8,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-008db244"></a> `008db244` | `28 fc 07 36` | tbz w8,#0x0,0x008db1c8 | `CONDITIONAL_JUMP`
<a id="insn-008db248"></a> `008db248` | `e0 63 40 f9` | ldr x0,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-008db24c"></a> `008db24c` | `19 f2 0d 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-008db250"></a> `008db250` | `e8 43 42 39` | ldrb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-008db254"></a> `008db254` | `e8 fb 07 36` | tbz w8,#0x0,0x008db1d0 | `CONDITIONAL_JUMP`
<a id="insn-008db258"></a> `008db258` | `e0 53 40 f9` | ldr x0,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-008db25c"></a> `008db25c` | `15 f2 0d 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-008db260"></a> `008db260` | `e8 c3 41 39` | ldrb w8,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-008db264"></a> `008db264` | `a8 fb 07 36` | tbz w8,#0x0,0x008db1d8 | `CONDITIONAL_JUMP`
<a id="insn-008db268"></a> `008db268` | `e0 43 40 f9` | ldr x0,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-008db26c"></a> `008db26c` | `11 f2 0d 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-008db270"></a> `008db270` | `e8 43 41 39` | ldrb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-008db274"></a> `008db274` | `68 fb 07 36` | tbz w8,#0x0,0x008db1e0 | `CONDITIONAL_JUMP`
<a id="insn-008db278"></a> `008db278` | `e0 33 40 f9` | ldr x0,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-008db27c"></a> `008db27c` | `0d f2 0d 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-008db280"></a> `008db280` | `e8 c3 40 39` | ldrb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-008db284"></a> `008db284` | `28 fb 07 36` | tbz w8,#0x0,0x008db1e8 | `CONDITIONAL_JUMP`
<a id="insn-008db288"></a> `008db288` | `e0 23 40 f9` | ldr x0,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-008db28c"></a> `008db28c` | `09 f2 0d 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-008db290"></a> `008db290` | `e8 43 40 39` | ldrb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-008db294"></a> `008db294` | `e8 fa 07 37` | tbnz w8,#0x0,0x008db1f0 | `CONDITIONAL_JUMP`
<a id="insn-008db298"></a> `008db298` | `d8 ff ff 17` | b 0x008db1f8 | `UNCONDITIONAL_JUMP`
<a id="insn-008db368"></a> `008db368` | `de f1 0d 94` | bl 0x00c57ae0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`008dafdc`](#insn-008dafdc) 範囲 `[['008dafdc', '008db1bf']]`
  - `CONDITIONAL_JUMP` [`008db1bc`](#insn-008db1bc) → [`008db238`](#insn-008db238)
  - `FALL_THROUGH` [`008db1bc`](#insn-008db1bc) → [`008db1c0`](#insn-008db1c0)
- ブロック [`008db1c0`](#insn-008db1c0) 範囲 `[['008db1c0', '008db1c7']]`
  - `CONDITIONAL_JUMP` [`008db1c4`](#insn-008db1c4) → [`008db248`](#insn-008db248)
  - `FALL_THROUGH` [`008db1c4`](#insn-008db1c4) → [`008db1c8`](#insn-008db1c8)
- ブロック [`008db1c8`](#insn-008db1c8) 範囲 `[['008db1c8', '008db1cf']]`
  - `CONDITIONAL_JUMP` [`008db1cc`](#insn-008db1cc) → [`008db258`](#insn-008db258)
  - `FALL_THROUGH` [`008db1cc`](#insn-008db1cc) → [`008db1d0`](#insn-008db1d0)
- ブロック [`008db1d0`](#insn-008db1d0) 範囲 `[['008db1d0', '008db1d7']]`
  - `CONDITIONAL_JUMP` [`008db1d4`](#insn-008db1d4) → [`008db268`](#insn-008db268)
  - `FALL_THROUGH` [`008db1d4`](#insn-008db1d4) → [`008db1d8`](#insn-008db1d8)
- ブロック [`008db1d8`](#insn-008db1d8) 範囲 `[['008db1d8', '008db1df']]`
  - `CONDITIONAL_JUMP` [`008db1dc`](#insn-008db1dc) → [`008db278`](#insn-008db278)
  - `FALL_THROUGH` [`008db1dc`](#insn-008db1dc) → [`008db1e0`](#insn-008db1e0)
- ブロック [`008db1e0`](#insn-008db1e0) 範囲 `[['008db1e0', '008db1e7']]`
  - `CONDITIONAL_JUMP` [`008db1e4`](#insn-008db1e4) → [`008db288`](#insn-008db288)
  - `FALL_THROUGH` [`008db1e4`](#insn-008db1e4) → [`008db1e8`](#insn-008db1e8)
- ブロック [`008db1e8`](#insn-008db1e8) 範囲 `[['008db1e8', '008db1ef']]`
  - `CONDITIONAL_JUMP` [`008db1ec`](#insn-008db1ec) → [`008db1f8`](#insn-008db1f8)
  - `FALL_THROUGH` [`008db1ec`](#insn-008db1ec) → [`008db1f0`](#insn-008db1f0)
- ブロック [`008db1f0`](#insn-008db1f0) 範囲 `[['008db1f0', '008db1f7']]`
  - `FALL_THROUGH` [`008db1f4`](#insn-008db1f4) → [`008db1f8`](#insn-008db1f8)
- ブロック [`008db1f8`](#insn-008db1f8) 範囲 `[['008db1f8', '008db223']]`
  - `CONDITIONAL_JUMP` [`008db220`](#insn-008db220) → [`008db368`](#insn-008db368)
  - `FALL_THROUGH` [`008db220`](#insn-008db220) → [`008db224`](#insn-008db224)
- ブロック [`008db224`](#insn-008db224) 範囲 `[['008db224', '008db237']]`
- ブロック [`008db238`](#insn-008db238) 範囲 `[['008db238', '008db247']]`
  - `CONDITIONAL_JUMP` [`008db244`](#insn-008db244) → [`008db1c8`](#insn-008db1c8)
  - `FALL_THROUGH` [`008db244`](#insn-008db244) → [`008db248`](#insn-008db248)
- ブロック [`008db248`](#insn-008db248) 範囲 `[['008db248', '008db257']]`
  - `CONDITIONAL_JUMP` [`008db254`](#insn-008db254) → [`008db1d0`](#insn-008db1d0)
  - `FALL_THROUGH` [`008db254`](#insn-008db254) → [`008db258`](#insn-008db258)
- ブロック [`008db258`](#insn-008db258) 範囲 `[['008db258', '008db267']]`
  - `CONDITIONAL_JUMP` [`008db264`](#insn-008db264) → [`008db1d8`](#insn-008db1d8)
  - `FALL_THROUGH` [`008db264`](#insn-008db264) → [`008db268`](#insn-008db268)
- ブロック [`008db268`](#insn-008db268) 範囲 `[['008db268', '008db277']]`
  - `CONDITIONAL_JUMP` [`008db274`](#insn-008db274) → [`008db1e0`](#insn-008db1e0)
  - `FALL_THROUGH` [`008db274`](#insn-008db274) → [`008db278`](#insn-008db278)
- ブロック [`008db278`](#insn-008db278) 範囲 `[['008db278', '008db287']]`
  - `CONDITIONAL_JUMP` [`008db284`](#insn-008db284) → [`008db1e8`](#insn-008db1e8)
  - `FALL_THROUGH` [`008db284`](#insn-008db284) → [`008db288`](#insn-008db288)
- ブロック [`008db288`](#insn-008db288) 範囲 `[['008db288', '008db28b']]`
  - `FALL_THROUGH` [`008db288`](#insn-008db288) → [`008db28c`](#insn-008db28c)
- ブロック [`008db28c`](#insn-008db28c) 範囲 `[['008db28c', '008db28f']]`
  - `FALL_THROUGH` [`008db28c`](#insn-008db28c) → [`008db290`](#insn-008db290)
- ブロック [`008db290`](#insn-008db290) 範囲 `[['008db290', '008db293']]`
  - `FALL_THROUGH` [`008db290`](#insn-008db290) → [`008db294`](#insn-008db294)
- ブロック [`008db294`](#insn-008db294) 範囲 `[['008db294', '008db297']]`
  - `CONDITIONAL_JUMP` [`008db294`](#insn-008db294) → [`008db1f0`](#insn-008db1f0)
  - `FALL_THROUGH` [`008db294`](#insn-008db294) → [`008db298`](#insn-008db298)
- ブロック [`008db298`](#insn-008db298) 範囲 `[['008db298', '008db29b']]`
  - `UNCONDITIONAL_JUMP` [`008db298`](#insn-008db298) → [`008db1f8`](#insn-008db1f8)
- ブロック [`008db368`](#insn-008db368) 範囲 `[['008db368', '008db36b']]`

## 命令位置別の参照

- [`008dafe0`](#insn-008dafe0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008dafe4`](#insn-008dafe4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008dafe8`](#insn-008dafe8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db00c`](#insn-008db00c) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db018`](#insn-008db018) → `002b7ee6`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`008db020`](#insn-008db020) → `Stack[-0xff]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db024`](#insn-008db024) → `Stack[-0xf8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db034`](#insn-008db034) → `Stack[-0x10f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db03c`](#insn-008db03c) → `002b7ef9`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`008db040`](#insn-008db040) → `Stack[-0xdf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db048`](#insn-008db048) → `Stack[-0xd8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db058`](#insn-008db058) → `Stack[-0xef]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db05c`](#insn-008db05c) → `002b8d82`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`008db060`](#insn-008db060) → `Stack[-0xbf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db068`](#insn-008db068) → `Stack[-0xb8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db078`](#insn-008db078) → `Stack[-0xcf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db07c`](#insn-008db07c) → `002a2e95`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`008db080`](#insn-008db080) → `Stack[-0x9f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db088`](#insn-008db088) → `Stack[-0x98]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db094`](#insn-008db094) → `Stack[-0xaf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db098`](#insn-008db098) → `002ac592`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`008db0a0`](#insn-008db0a0) → `Stack[-0x7f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db0a8`](#insn-008db0a8) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db0b4`](#insn-008db0b4) → `Stack[-0x8f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db0b8`](#insn-008db0b8) → `002a0e90`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`008db0c0`](#insn-008db0c0) → `Stack[-0x5f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db0c8`](#insn-008db0c8) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db0d4`](#insn-008db0d4) → `Stack[-0x6f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db0d8`](#insn-008db0d8) → `002a3e3c`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`008db0dc`](#insn-008db0dc) → `Stack[-0x110]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db0e0`](#insn-008db0e0) → `Stack[-0xf0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db0e4`](#insn-008db0e4) → `Stack[-0xd0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db0e8`](#insn-008db0e8) → `Stack[-0xb0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db0ec`](#insn-008db0ec) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db0f0`](#insn-008db0f0) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db0f4`](#insn-008db0f4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db0fc`](#insn-008db0fc) → `Stack[-0x118]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db100`](#insn-008db100) → `Stack[-0xfd]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db104`](#insn-008db104) → `Stack[-0xdd]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db108`](#insn-008db108) → `Stack[-0xbd]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db10c`](#insn-008db10c) → `Stack[-0x9d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db110`](#insn-008db110) → `Stack[-0x7d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db114`](#insn-008db114) → `Stack[-0x5d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db118`](#insn-008db118) → `Stack[-0x3f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db11c`](#insn-008db11c) → `Stack[-0x4f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db120`](#insn-008db120) → `Stack[-0x3d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db124`](#insn-008db124) → `01123580`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008db128`](#insn-008db128) → `01123578`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008db12c`](#insn-008db12c) → `01123570`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008db12c`](#insn-008db12c) → `01123578`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008db138`](#insn-008db138) → `01123570`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008db13c`](#insn-008db13c) → [`0043b7b8`](../0043b/0043b7b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043b7b8` · 推定シンボル `None` · 推定型 `None`
- [`008db140`](#insn-008db140) → `01123578`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008db14c`](#insn-008db14c) → `01123570`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008db150`](#insn-008db150) → [`0043b7b8`](../0043b/0043b7b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043b7b8` · 推定シンボル `None` · 推定型 `None`
- [`008db154`](#insn-008db154) → `01123578`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008db160`](#insn-008db160) → `01123570`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008db164`](#insn-008db164) → [`0043b7b8`](../0043b/0043b7b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043b7b8` · 推定シンボル `None` · 推定型 `None`
- [`008db168`](#insn-008db168) → `01123578`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008db174`](#insn-008db174) → `01123570`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008db178`](#insn-008db178) → [`0043b7b8`](../0043b/0043b7b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043b7b8` · 推定シンボル `None` · 推定型 `None`
- [`008db17c`](#insn-008db17c) → `01123578`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008db188`](#insn-008db188) → `01123570`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008db18c`](#insn-008db18c) → [`0043b7b8`](../0043b/0043b7b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043b7b8` · 推定シンボル `None` · 推定型 `None`
- [`008db190`](#insn-008db190) → `01123578`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008db19c`](#insn-008db19c) → `01123570`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008db1a0`](#insn-008db1a0) → [`0043b7b8`](../0043b/0043b7b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043b7b8` · 推定シンボル `None` · 推定型 `None`
- [`008db1a4`](#insn-008db1a4) → `01123578`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008db1b0`](#insn-008db1b0) → `01123570`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008db1b4`](#insn-008db1b4) → [`0043b7b8`](../0043b/0043b7b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043b7b8` · 推定シンボル `None` · 推定型 `None`
- [`008db1b8`](#insn-008db1b8) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db1bc`](#insn-008db1bc) → [`008db238`](#insn-008db238) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db1c0`](#insn-008db1c0) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db1c4`](#insn-008db1c4) → [`008db248`](#insn-008db248) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db1c8`](#insn-008db1c8) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db1cc`](#insn-008db1cc) → [`008db258`](#insn-008db258) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db1d0`](#insn-008db1d0) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db1d4`](#insn-008db1d4) → [`008db268`](#insn-008db268) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db1d8`](#insn-008db1d8) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db1dc`](#insn-008db1dc) → [`008db278`](#insn-008db278) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db1e0`](#insn-008db1e0) → `Stack[-0xf0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db1e4`](#insn-008db1e4) → [`008db288`](#insn-008db288) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db1e8`](#insn-008db1e8) → `Stack[-0x110]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db1ec`](#insn-008db1ec) → [`008db1f8`](#insn-008db1f8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db1f0`](#insn-008db1f0) → `Stack[-0x100]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db1f4`](#insn-008db1f4) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`008db1fc`](#insn-008db1fc) → [`0043ae30`](../0043a/0043ae30.md) · `PARAM` · `ANALYSIS` · 関数 `0043ae30` · 推定シンボル `None` · 推定型 `None`
- [`008db204`](#insn-008db204) → `01123570`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008db20c`](#insn-008db20c) → `00c62b90`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`008db210`](#insn-008db210) → [`00c57a30`](../00c57/00c57a30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a30` · 推定シンボル `None` · 推定型 `None`
- [`008db218`](#insn-008db218) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db220`](#insn-008db220) → [`008db368`](#insn-008db368) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db224`](#insn-008db224) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db228`](#insn-008db228) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db22c`](#insn-008db22c) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db238`](#insn-008db238) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db23c`](#insn-008db23c) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`008db240`](#insn-008db240) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db244`](#insn-008db244) → [`008db1c8`](#insn-008db1c8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db248`](#insn-008db248) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db24c`](#insn-008db24c) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`008db250`](#insn-008db250) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db254`](#insn-008db254) → [`008db1d0`](#insn-008db1d0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db258`](#insn-008db258) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db25c`](#insn-008db25c) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`008db260`](#insn-008db260) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db264`](#insn-008db264) → [`008db1d8`](#insn-008db1d8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db268`](#insn-008db268) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db26c`](#insn-008db26c) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`008db270`](#insn-008db270) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db274`](#insn-008db274) → [`008db1e0`](#insn-008db1e0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db278`](#insn-008db278) → `Stack[-0xc0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db27c`](#insn-008db27c) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`008db280`](#insn-008db280) → `Stack[-0xf0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db284`](#insn-008db284) → [`008db1e8`](#insn-008db1e8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db288`](#insn-008db288) → `Stack[-0xe0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db28c`](#insn-008db28c) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`008db290`](#insn-008db290) → `Stack[-0x110]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db294`](#insn-008db294) → [`008db1f0`](#insn-008db1f0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db298`](#insn-008db298) → [`008db1f8`](#insn-008db1f8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008db368`](#insn-008db368) → [`00c57ae0`](../00c57/00c57ae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ae0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`008dafe0`](#insn-008dafe0)

~~~json
{
  "source": "008dafe0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008dafe4`](#insn-008dafe4)

~~~json
{
  "source": "008dafe4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008dafe8`](#insn-008dafe8)

~~~json
{
  "source": "008dafe8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db00c`](#insn-008db00c)

~~~json
{
  "source": "008db00c",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db018`](#insn-008db018)

~~~json
{
  "source": "008db018",
  "target": "002b7ee6",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b7ee6",
  "offset": 0,
  "size": 19,
  "datatype": "string",
  "bytes": "43676b496a4d33795f5a516145414951416700",
  "capture_start": "002b7ee6",
  "capture_bytes": 19,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008db020`](#insn-008db020)

~~~json
{
  "source": "008db020",
  "target": "Stack[-0xff]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db024`](#insn-008db024)

~~~json
{
  "source": "008db024",
  "target": "Stack[-0xf8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db034`](#insn-008db034)

~~~json
{
  "source": "008db034",
  "target": "Stack[-0x10f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db03c`](#insn-008db03c)

~~~json
{
  "source": "008db03c",
  "target": "002b7ef9",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b7ef9",
  "offset": 0,
  "size": 19,
  "datatype": "string",
  "bytes": "43676b496a4d33795f5a516145414951424100",
  "capture_start": "002b7ef9",
  "capture_bytes": 19,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008db040`](#insn-008db040)

~~~json
{
  "source": "008db040",
  "target": "Stack[-0xdf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db048`](#insn-008db048)

~~~json
{
  "source": "008db048",
  "target": "Stack[-0xd8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db058`](#insn-008db058)

~~~json
{
  "source": "008db058",
  "target": "Stack[-0xef]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db05c`](#insn-008db05c)

~~~json
{
  "source": "008db05c",
  "target": "002b8d82",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b8d82",
  "offset": 0,
  "size": 19,
  "datatype": "string",
  "bytes": "43676b496a4d33795f5a516145414951426700",
  "capture_start": "002b8d82",
  "capture_bytes": 19,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008db060`](#insn-008db060)

~~~json
{
  "source": "008db060",
  "target": "Stack[-0xbf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db068`](#insn-008db068)

~~~json
{
  "source": "008db068",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db078`](#insn-008db078)

~~~json
{
  "source": "008db078",
  "target": "Stack[-0xcf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db07c`](#insn-008db07c)

~~~json
{
  "source": "008db07c",
  "target": "002a2e95",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a2e95",
  "offset": 0,
  "size": 19,
  "datatype": "string",
  "bytes": "43676b496a4d33795f5a516145414951417700",
  "capture_start": "002a2e95",
  "capture_bytes": 19,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008db080`](#insn-008db080)

~~~json
{
  "source": "008db080",
  "target": "Stack[-0x9f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db088`](#insn-008db088)

~~~json
{
  "source": "008db088",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db094`](#insn-008db094)

~~~json
{
  "source": "008db094",
  "target": "Stack[-0xaf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db098`](#insn-008db098)

~~~json
{
  "source": "008db098",
  "target": "002ac592",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002ac592",
  "offset": 0,
  "size": 19,
  "datatype": "string",
  "bytes": "43676b496a4d33795f5a516145414951425100",
  "capture_start": "002ac592",
  "capture_bytes": 19,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008db0a0`](#insn-008db0a0)

~~~json
{
  "source": "008db0a0",
  "target": "Stack[-0x7f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db0a8`](#insn-008db0a8)

~~~json
{
  "source": "008db0a8",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db0b4`](#insn-008db0b4)

~~~json
{
  "source": "008db0b4",
  "target": "Stack[-0x8f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db0b8`](#insn-008db0b8)

~~~json
{
  "source": "008db0b8",
  "target": "002a0e90",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a0e90",
  "offset": 0,
  "size": 19,
  "datatype": "string",
  "bytes": "43676b496a4d33795f5a516145414951427700",
  "capture_start": "002a0e90",
  "capture_bytes": 19,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008db0c0`](#insn-008db0c0)

~~~json
{
  "source": "008db0c0",
  "target": "Stack[-0x5f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db0c8`](#insn-008db0c8)

~~~json
{
  "source": "008db0c8",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db0d4`](#insn-008db0d4)

~~~json
{
  "source": "008db0d4",
  "target": "Stack[-0x6f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db0d8`](#insn-008db0d8)

~~~json
{
  "source": "008db0d8",
  "target": "002a3e3c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a3e3c",
  "offset": 0,
  "size": 19,
  "datatype": "string",
  "bytes": "43676b496a4d33795f5a516145414951434100",
  "capture_start": "002a3e3c",
  "capture_bytes": 19,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008db0dc`](#insn-008db0dc)

~~~json
{
  "source": "008db0dc",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db0e0`](#insn-008db0e0)

~~~json
{
  "source": "008db0e0",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db0e4`](#insn-008db0e4)

~~~json
{
  "source": "008db0e4",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db0e8`](#insn-008db0e8)

~~~json
{
  "source": "008db0e8",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db0ec`](#insn-008db0ec)

~~~json
{
  "source": "008db0ec",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db0f0`](#insn-008db0f0)

~~~json
{
  "source": "008db0f0",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db0f4`](#insn-008db0f4)

~~~json
{
  "source": "008db0f4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db0fc`](#insn-008db0fc)

~~~json
{
  "source": "008db0fc",
  "target": "Stack[-0x118]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db100`](#insn-008db100)

~~~json
{
  "source": "008db100",
  "target": "Stack[-0xfd]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db104`](#insn-008db104)

~~~json
{
  "source": "008db104",
  "target": "Stack[-0xdd]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db108`](#insn-008db108)

~~~json
{
  "source": "008db108",
  "target": "Stack[-0xbd]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db10c`](#insn-008db10c)

~~~json
{
  "source": "008db10c",
  "target": "Stack[-0x9d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db110`](#insn-008db110)

~~~json
{
  "source": "008db110",
  "target": "Stack[-0x7d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db114`](#insn-008db114)

~~~json
{
  "source": "008db114",
  "target": "Stack[-0x5d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db118`](#insn-008db118)

~~~json
{
  "source": "008db118",
  "target": "Stack[-0x3f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db11c`](#insn-008db11c)

~~~json
{
  "source": "008db11c",
  "target": "Stack[-0x4f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db120`](#insn-008db120)

~~~json
{
  "source": "008db120",
  "target": "Stack[-0x3d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db124`](#insn-008db124)

~~~json
{
  "source": "008db124",
  "target": "01123580",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01123580",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008db128`](#insn-008db128)

~~~json
{
  "source": "008db128",
  "target": "01123578",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01123578",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008db12c`](#insn-008db12c)

~~~json
{
  "source": "008db12c",
  "target": "01123570",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01123570",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008db12c`](#insn-008db12c)

~~~json
{
  "source": "008db12c",
  "target": "01123578",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01123578",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008db138`](#insn-008db138)

~~~json
{
  "source": "008db138",
  "target": "01123570",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01123570",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008db13c`](#insn-008db13c)

~~~json
{
  "source": "008db13c",
  "target": "0043b7b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008db140`](#insn-008db140)

~~~json
{
  "source": "008db140",
  "target": "01123578",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01123578",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008db14c`](#insn-008db14c)

~~~json
{
  "source": "008db14c",
  "target": "01123570",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01123570",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008db150`](#insn-008db150)

~~~json
{
  "source": "008db150",
  "target": "0043b7b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008db154`](#insn-008db154)

~~~json
{
  "source": "008db154",
  "target": "01123578",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01123578",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008db160`](#insn-008db160)

~~~json
{
  "source": "008db160",
  "target": "01123570",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01123570",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008db164`](#insn-008db164)

~~~json
{
  "source": "008db164",
  "target": "0043b7b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008db168`](#insn-008db168)

~~~json
{
  "source": "008db168",
  "target": "01123578",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01123578",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008db174`](#insn-008db174)

~~~json
{
  "source": "008db174",
  "target": "01123570",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01123570",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008db178`](#insn-008db178)

~~~json
{
  "source": "008db178",
  "target": "0043b7b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008db17c`](#insn-008db17c)

~~~json
{
  "source": "008db17c",
  "target": "01123578",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01123578",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008db188`](#insn-008db188)

~~~json
{
  "source": "008db188",
  "target": "01123570",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01123570",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008db18c`](#insn-008db18c)

~~~json
{
  "source": "008db18c",
  "target": "0043b7b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008db190`](#insn-008db190)

~~~json
{
  "source": "008db190",
  "target": "01123578",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01123578",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008db19c`](#insn-008db19c)

~~~json
{
  "source": "008db19c",
  "target": "01123570",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01123570",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008db1a0`](#insn-008db1a0)

~~~json
{
  "source": "008db1a0",
  "target": "0043b7b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008db1a4`](#insn-008db1a4)

~~~json
{
  "source": "008db1a4",
  "target": "01123578",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01123578",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008db1b0`](#insn-008db1b0)

~~~json
{
  "source": "008db1b0",
  "target": "01123570",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01123570",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008db1b4`](#insn-008db1b4)

~~~json
{
  "source": "008db1b4",
  "target": "0043b7b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008db1b8`](#insn-008db1b8)

~~~json
{
  "source": "008db1b8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db1bc`](#insn-008db1bc)

~~~json
{
  "source": "008db1bc",
  "target": "008db238",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db1c0`](#insn-008db1c0)

~~~json
{
  "source": "008db1c0",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db1c4`](#insn-008db1c4)

~~~json
{
  "source": "008db1c4",
  "target": "008db248",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db1c8`](#insn-008db1c8)

~~~json
{
  "source": "008db1c8",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db1cc`](#insn-008db1cc)

~~~json
{
  "source": "008db1cc",
  "target": "008db258",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db1d0`](#insn-008db1d0)

~~~json
{
  "source": "008db1d0",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db1d4`](#insn-008db1d4)

~~~json
{
  "source": "008db1d4",
  "target": "008db268",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db1d8`](#insn-008db1d8)

~~~json
{
  "source": "008db1d8",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db1dc`](#insn-008db1dc)

~~~json
{
  "source": "008db1dc",
  "target": "008db278",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db1e0`](#insn-008db1e0)

~~~json
{
  "source": "008db1e0",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db1e4`](#insn-008db1e4)

~~~json
{
  "source": "008db1e4",
  "target": "008db288",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db1e8`](#insn-008db1e8)

~~~json
{
  "source": "008db1e8",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db1ec`](#insn-008db1ec)

~~~json
{
  "source": "008db1ec",
  "target": "008db1f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db1f0`](#insn-008db1f0)

~~~json
{
  "source": "008db1f0",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db1f4`](#insn-008db1f4)

~~~json
{
  "source": "008db1f4",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008db1fc`](#insn-008db1fc)

~~~json
{
  "source": "008db1fc",
  "target": "0043ae30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008db204`](#insn-008db204)

~~~json
{
  "source": "008db204",
  "target": "01123570",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01123570",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008db20c`](#insn-008db20c)

~~~json
{
  "source": "008db20c",
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
- 参照命令 [`008db210`](#insn-008db210)

~~~json
{
  "source": "008db210",
  "target": "00c57a30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008db218`](#insn-008db218)

~~~json
{
  "source": "008db218",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db220`](#insn-008db220)

~~~json
{
  "source": "008db220",
  "target": "008db368",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db224`](#insn-008db224)

~~~json
{
  "source": "008db224",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db228`](#insn-008db228)

~~~json
{
  "source": "008db228",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db22c`](#insn-008db22c)

~~~json
{
  "source": "008db22c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db238`](#insn-008db238)

~~~json
{
  "source": "008db238",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db23c`](#insn-008db23c)

~~~json
{
  "source": "008db23c",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008db240`](#insn-008db240)

~~~json
{
  "source": "008db240",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db244`](#insn-008db244)

~~~json
{
  "source": "008db244",
  "target": "008db1c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db248`](#insn-008db248)

~~~json
{
  "source": "008db248",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db24c`](#insn-008db24c)

~~~json
{
  "source": "008db24c",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008db250`](#insn-008db250)

~~~json
{
  "source": "008db250",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db254`](#insn-008db254)

~~~json
{
  "source": "008db254",
  "target": "008db1d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db258`](#insn-008db258)

~~~json
{
  "source": "008db258",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db25c`](#insn-008db25c)

~~~json
{
  "source": "008db25c",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008db260`](#insn-008db260)

~~~json
{
  "source": "008db260",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db264`](#insn-008db264)

~~~json
{
  "source": "008db264",
  "target": "008db1d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db268`](#insn-008db268)

~~~json
{
  "source": "008db268",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db26c`](#insn-008db26c)

~~~json
{
  "source": "008db26c",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008db270`](#insn-008db270)

~~~json
{
  "source": "008db270",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db274`](#insn-008db274)

~~~json
{
  "source": "008db274",
  "target": "008db1e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db278`](#insn-008db278)

~~~json
{
  "source": "008db278",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db27c`](#insn-008db27c)

~~~json
{
  "source": "008db27c",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008db280`](#insn-008db280)

~~~json
{
  "source": "008db280",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db284`](#insn-008db284)

~~~json
{
  "source": "008db284",
  "target": "008db1e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db288`](#insn-008db288)

~~~json
{
  "source": "008db288",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db28c`](#insn-008db28c)

~~~json
{
  "source": "008db28c",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008db290`](#insn-008db290)

~~~json
{
  "source": "008db290",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db294`](#insn-008db294)

~~~json
{
  "source": "008db294",
  "target": "008db1f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db298`](#insn-008db298)

~~~json
{
  "source": "008db298",
  "target": "008db1f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008db368`](#insn-008db368)

~~~json
{
  "source": "008db368",
  "target": "00c57ae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
