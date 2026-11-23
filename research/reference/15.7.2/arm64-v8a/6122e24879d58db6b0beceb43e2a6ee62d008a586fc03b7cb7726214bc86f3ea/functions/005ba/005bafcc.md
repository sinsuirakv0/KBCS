# 005bafcc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `005bafcc`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ba/005bafcc.md) · 移動量 `+0x0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0024.md#compare-d2f6bc43dba4179bcd6f0afb28ed78a3)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "005bafcc",
  "name": "_INIT_63",
  "size": 708,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4a188249fb22fc8874b5b354fccd4679af365b894d72507ab225b4fd4e30dfd3",
  "source_text_sha256": "4a188249fb22fc8874b5b354fccd4679af365b894d72507ab225b4fd4e30dfd3",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "005bafcc",
        "005bb28b"
      ],
      [
        "005bb358",
        "005bb35b"
      ]
    ],
    "bytes_sha256": "7315e9b4e5bafffca58ec7653bc3c024b41d17c224fb6bd1f14e344db61d4101",
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

- [00418cb8](../00418/00418cb8.md)
- [00bdaee0](../00bda/00bdaee0.md)
- [00bdaf60](../00bda/00bdaf60.md)
- [00bdaf90](../00bda/00bdaf90.md)

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

## 疑似コード / UTF-8 6141 bytes

~~~c

/* WARNING: Type propagation algorithm not settling */

void _INIT_63(void)

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
  
                    /* catch() { ... } // from try @ 005baf04 with catch @ 005bafcc */
                    /* catch() { ... } // from try @ 005badb0 with catch @ 005bafdc */
                    /* catch() { ... } // from try @ 005bad98 with catch @ 005bafe0 */
  lVar1 = tpidr_el0;
  local_38 = *(long *)(lVar1 + 0x28);
  uStack_ff = 0x6741;
  local_f8[0] = 1;
  uStack_107 = (undefined7)s_CgkIjM3y_ZQaEAIQAg_002a72e4._8_8_;
  cStack_100 = SUB81(s_CgkIjM3y_ZQaEAIQAg_002a72e4._8_8_,7);
  local_10f = (char  [8])s_CgkIjM3y_ZQaEAIQAg_002a72e4._0_8_;
                    /* try { // try from 005bb030 to 006bb0e7 has its CatchHandler @ 005bb030
                       catch() { ... } // from try @ 005bb030 with catch @ 005bb030
                       catch() { ... } // from try @ 005bb138 with catch @ 005bb030 */
  uStack_df = 0x4142;
  local_d8[0] = 2;
  uStack_e7 = (undefined7)s_CgkIjM3y_ZQaEAIQBA_002a72f7._8_8_;
  cStack_e0 = SUB81(s_CgkIjM3y_ZQaEAIQBA_002a72f7._8_8_,7);
  local_ef = (char  [8])s_CgkIjM3y_ZQaEAIQBA_002a72f7._0_8_;
  uStack_bf = 0x6742;
  local_b8[0] = 3;
  uStack_c7 = (undefined7)s_CgkIjM3y_ZQaEAIQBg_002a80da._8_8_;
  cStack_c0 = SUB81(s_CgkIjM3y_ZQaEAIQBg_002a80da._8_8_,7);
  local_cf = (char  [8])s_CgkIjM3y_ZQaEAIQBg_002a80da._0_8_;
  uStack_9f = 0x7741;
  local_98[0] = 4;
  uStack_a7 = (undefined7)s_CgkIjM3y_ZQaEAIQAw_002936ae._8_8_;
  cStack_a0 = SUB81(s_CgkIjM3y_ZQaEAIQAw_002936ae._8_8_,7);
  local_af = (char  [8])s_CgkIjM3y_ZQaEAIQAw_002936ae._0_8_;
  uStack_7f = 0x5142;
  local_78[0] = 5;
  uStack_87 = (undefined7)s_CgkIjM3y_ZQaEAIQBQ_0029c2e1._8_8_;
  cStack_80 = SUB81(s_CgkIjM3y_ZQaEAIQBQ_0029c2e1._8_8_,7);
  local_8f = (char  [8])s_CgkIjM3y_ZQaEAIQBQ_0029c2e1._0_8_;
  uStack_5f = 0x7742;
  local_58[0] = 6;
  uStack_67 = (undefined7)s_CgkIjM3y_ZQaEAIQBw_00291877._8_8_;
  cStack_60 = SUB81(s_CgkIjM3y_ZQaEAIQBw_00291877._8_8_,7);
  local_6f = (char  [8])s_CgkIjM3y_ZQaEAIQBw_00291877._0_8_;
  local_110 = 0x24;
  local_f0 = 0x24;
  local_d0 = 0x24;
  local_b0 = 0x24;
  local_90 = 0x24;
  local_70 = 0x24;
  local_50 = 0x24;
                    /* try { // try from 005bb0e8 to 006bb0f7 has its CatchHandler @ 005bb194 */
  local_118[0] = 0;
  uStack_fd = 0;
  uStack_dd = 0;
  uStack_bd = 0;
                    /* try { // try from 005bb0fc to 006bb137 has its CatchHandler @ 005bb170 */
  uStack_9d = 0;
  uStack_7d = 0;
  uStack_5d = 0;
  uStack_3f = 0x4143;
  uStack_47 = (undefined7)s_CgkIjM3y_ZQaEAIQCA_00294526._8_8_;
  cStack_40 = SUB81(s_CgkIjM3y_ZQaEAIQCA_00294526._8_8_,7);
  local_4f = (char  [8])s_CgkIjM3y_ZQaEAIQCA_00294526._0_8_;
  uStack_3d = 0;
  DAT_00c268e0 = 0;
  DAT_00c268d8 = 0;
  DAT_00c268d0 = &DAT_00c268d8;
  FUN_00418cb8(&DAT_00c268d0,&DAT_00c268d8,local_118,local_118);
                    /* try { // try from 005bb138 to 006bb1bf has its CatchHandler @ 005bb030 */
  FUN_00418cb8(&DAT_00c268d0,&DAT_00c268d8,local_f8,local_f8);
  FUN_00418cb8(&DAT_00c268d0,&DAT_00c268d8,local_d8,local_d8);
  FUN_00418cb8(&DAT_00c268d0,&DAT_00c268d8,local_b8,local_b8);
                    /* catch() { ... } // from try @ 005bb0fc with catch @ 005bb170 */
  FUN_00418cb8(&DAT_00c268d0,&DAT_00c268d8,local_98,local_98);
  FUN_00418cb8(&DAT_00c268d0,&DAT_00c268d8,local_78,local_78);
                    /* catch() { ... } // from try @ 005bb0e8 with catch @ 005bb194 */
  FUN_00418cb8(&DAT_00c268d0,&DAT_00c268d8,local_58,local_58);
  if ((local_50 & 1) != 0) {
    _ZdlPv((void *)CONCAT44(uStack_3c,CONCAT13(uStack_3d,CONCAT21(uStack_3f,cStack_40))));
  }
                    /* try { // try from 005bb234 to 006bb27f has its CatchHandler @ 005bb1c0 */
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
    _ZdlPv((void *)CONCAT44(uStack_dc,CONCAT13(uStack_dd,CONCAT21(uStack_df,cStack_e0))));
                    /* try { // try from 005bb280 to 006bb28b has its CatchHandler @ 005bb3a8 */
  }
  if ((local_110 & 1) != 0) {
    _ZdlPv((void *)CONCAT44(uStack_fc,CONCAT13(uStack_fd,CONCAT21(uStack_ff,cStack_100))));
  }
  __cxa_atexit(FUN_00418330,&DAT_00c268d0,&PTR_LOOP_00be5ed0);
                    /* try { // try from 005bb210 to 006bb233 has its CatchHandler @ 005bb3ac */
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
<a id="insn-005bafcc"></a> `005bafcc` | `ff 83 04 d1` | sub sp,sp,#0x120 | `FALL_THROUGH`
<a id="insn-005bafd0"></a> `005bafd0` | `fd 7b 0f a9` | stp x29,x30,[sp, #0xf0] | `FALL_THROUGH`
<a id="insn-005bafd4"></a> `005bafd4` | `fc 57 10 a9` | stp x28,x21,[sp, #0x100] | `FALL_THROUGH`
<a id="insn-005bafd8"></a> `005bafd8` | `f4 4f 11 a9` | stp x20,x19,[sp, #0x110] | `FALL_THROUGH`
<a id="insn-005bafdc"></a> `005bafdc` | `fd c3 03 91` | add x29,sp,#0xf0 | `FALL_THROUGH`
<a id="insn-005bafe0"></a> `005bafe0` | `55 d0 3b d5` | mrs x21,tpidr_el0 | `FALL_THROUGH`
<a id="insn-005bafe4"></a> `005bafe4` | `2a e8 8c 52` | mov w10,#0x6741 | `FALL_THROUGH`
<a id="insn-005bafe8"></a> `005bafe8` | `f4 23 00 91` | add x20,sp,#0x8 | `FALL_THROUGH`
<a id="insn-005bafec"></a> `005bafec` | `a9 16 40 f9` | ldr x9,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-005baff0"></a> `005baff0` | `88 04 80 52` | mov w8,#0x24 | `FALL_THROUGH`
<a id="insn-005baff4"></a> `005baff4` | `73 33 00 90` | adrp x19,0xc26000 | `FALL_THROUGH`
<a id="insn-005baff8"></a> `005baff8` | `73 42 23 91` | add x19,x19,#0x8d0 | `FALL_THROUGH`
<a id="insn-005baffc"></a> `005baffc` | `a9 83 1f f8` | stur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-005bb000"></a> `005bb000` | `69 e7 ff 90` | adrp x9,0x2a7000 | `FALL_THROUGH`
<a id="insn-005bb004"></a> `005bb004` | `29 91 0b 91` | add x9,x9,#0x2e4 | `FALL_THROUGH`
<a id="insn-005bb008"></a> `005bb008` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-005bb00c"></a> `005bb00c` | `29 00 80 52` | mov w9,#0x1 | `FALL_THROUGH`
<a id="insn-005bb010"></a> `005bb010` | `ea 13 02 78` | sturh w10,[sp, #0x21] | `FALL_THROUGH`
<a id="insn-005bb014"></a> `005bb014` | `e9 2b 00 b9` | str w9,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-005bb018"></a> `005bb018` | `49 28 88 52` | mov w9,#0x4142 | `FALL_THROUGH`
<a id="insn-005bb01c"></a> `005bb01c` | `6a e7 ff 90` | adrp x10,0x2a7000 | `FALL_THROUGH`
<a id="insn-005bb020"></a> `005bb020` | `4a dd 0b 91` | add x10,x10,#0x2f7 | `FALL_THROUGH`
<a id="insn-005bb024"></a> `005bb024` | `e0 13 81 3c` | stur q0,[sp, #0x11] | `FALL_THROUGH`
<a id="insn-005bb028"></a> `005bb028` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-005bb02c"></a> `005bb02c` | `40 01 c0 3d` | ldr q0,[x10] | `FALL_THROUGH`
<a id="insn-005bb030"></a> `005bb030` | `e9 13 04 78` | sturh w9,[sp, #0x41] | `FALL_THROUGH`
<a id="insn-005bb034"></a> `005bb034` | `49 00 80 52` | mov w9,#0x2 | `FALL_THROUGH`
<a id="insn-005bb038"></a> `005bb038` | `e9 4b 00 b9` | str w9,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-005bb03c"></a> `005bb03c` | `49 e8 8c 52` | mov w9,#0x6742 | `FALL_THROUGH`
<a id="insn-005bb040"></a> `005bb040` | `6a e7 ff b0` | adrp x10,0x2a8000 | `FALL_THROUGH`
<a id="insn-005bb044"></a> `005bb044` | `4a 69 03 91` | add x10,x10,#0xda | `FALL_THROUGH`
<a id="insn-005bb048"></a> `005bb048` | `e0 13 83 3c` | stur q0,[sp, #0x31] | `FALL_THROUGH`
<a id="insn-005bb04c"></a> `005bb04c` | `40 01 c0 3d` | ldr q0,[x10] | `FALL_THROUGH`
<a id="insn-005bb050"></a> `005bb050` | `e9 13 06 78` | sturh w9,[sp, #0x61] | `FALL_THROUGH`
<a id="insn-005bb054"></a> `005bb054` | `69 00 80 52` | mov w9,#0x3 | `FALL_THROUGH`
<a id="insn-005bb058"></a> `005bb058` | `e9 6b 00 b9` | str w9,[sp, #0x68] | `FALL_THROUGH`
<a id="insn-005bb05c"></a> `005bb05c` | `29 e8 8e 52` | mov w9,#0x7741 | `FALL_THROUGH`
<a id="insn-005bb060"></a> `005bb060` | `ca e6 ff 90` | adrp x10,0x293000 | `FALL_THROUGH`
<a id="insn-005bb064"></a> `005bb064` | `4a b9 1a 91` | add x10,x10,#0x6ae | `FALL_THROUGH`
<a id="insn-005bb068"></a> `005bb068` | `e0 13 85 3c` | stur q0,[sp, #0x51] | `FALL_THROUGH`
<a id="insn-005bb06c"></a> `005bb06c` | `40 01 c0 3d` | ldr q0,[x10] | `FALL_THROUGH`
<a id="insn-005bb070"></a> `005bb070` | `e9 13 08 78` | sturh w9,[sp, #0x81] | `FALL_THROUGH`
<a id="insn-005bb074"></a> `005bb074` | `89 00 80 52` | mov w9,#0x4 | `FALL_THROUGH`
<a id="insn-005bb078"></a> `005bb078` | `e9 8b 00 b9` | str w9,[sp, #0x88] | `FALL_THROUGH`
<a id="insn-005bb07c"></a> `005bb07c` | `09 e7 ff b0` | adrp x9,0x29c000 | `FALL_THROUGH`
<a id="insn-005bb080"></a> `005bb080` | `29 85 0b 91` | add x9,x9,#0x2e1 | `FALL_THROUGH`
<a id="insn-005bb084"></a> `005bb084` | `e0 13 87 3c` | stur q0,[sp, #0x71] | `FALL_THROUGH`
<a id="insn-005bb088"></a> `005bb088` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-005bb08c"></a> `005bb08c` | `49 28 8a 52` | mov w9,#0x5142 | `FALL_THROUGH`
<a id="insn-005bb090"></a> `005bb090` | `89 92 09 78` | sturh w9,[x20, #0x99] | `FALL_THROUGH`
<a id="insn-005bb094"></a> `005bb094` | `a9 00 80 52` | mov w9,#0x5 | `FALL_THROUGH`
<a id="insn-005bb098"></a> `005bb098` | `e9 ab 00 b9` | str w9,[sp, #0xa8] | `FALL_THROUGH`
<a id="insn-005bb09c"></a> `005bb09c` | `a9 e6 ff d0` | adrp x9,0x291000 | `FALL_THROUGH`
<a id="insn-005bb0a0"></a> `005bb0a0` | `29 dd 21 91` | add x9,x9,#0x877 | `FALL_THROUGH`
<a id="insn-005bb0a4"></a> `005bb0a4` | `80 92 88 3c` | stur q0,[x20, #0x89] | `FALL_THROUGH`
<a id="insn-005bb0a8"></a> `005bb0a8` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-005bb0ac"></a> `005bb0ac` | `49 e8 8e 52` | mov w9,#0x7742 | `FALL_THROUGH`
<a id="insn-005bb0b0"></a> `005bb0b0` | `89 92 0b 78` | sturh w9,[x20, #0xb9] | `FALL_THROUGH`
<a id="insn-005bb0b4"></a> `005bb0b4` | `c9 00 80 52` | mov w9,#0x6 | `FALL_THROUGH`
<a id="insn-005bb0b8"></a> `005bb0b8` | `e9 cb 00 b9` | str w9,[sp, #0xc8] | `FALL_THROUGH`
<a id="insn-005bb0bc"></a> `005bb0bc` | `c9 e6 ff b0` | adrp x9,0x294000 | `FALL_THROUGH`
<a id="insn-005bb0c0"></a> `005bb0c0` | `29 99 14 91` | add x9,x9,#0x526 | `FALL_THROUGH`
<a id="insn-005bb0c4"></a> `005bb0c4` | `80 92 8a 3c` | stur q0,[x20, #0xa9] | `FALL_THROUGH`
<a id="insn-005bb0c8"></a> `005bb0c8` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-005bb0cc"></a> `005bb0cc` | `e8 43 00 39` | strb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-005bb0d0"></a> `005bb0d0` | `e8 c3 00 39` | strb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-005bb0d4"></a> `005bb0d4` | `e8 43 01 39` | strb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-005bb0d8"></a> `005bb0d8` | `e8 c3 01 39` | strb w8,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-005bb0dc"></a> `005bb0dc` | `e8 43 02 39` | strb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-005bb0e0"></a> `005bb0e0` | `e8 c3 02 39` | strb w8,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-005bb0e4"></a> `005bb0e4` | `e8 43 03 39` | strb w8,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-005bb0e8"></a> `005bb0e8` | `68 28 88 52` | mov w8,#0x4143 | `FALL_THROUGH`
<a id="insn-005bb0ec"></a> `005bb0ec` | `ff 0b 00 b9` | str wzr,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-005bb0f0"></a> `005bb0f0` | `ff 8f 00 39` | strb wzr,[sp, #0x23] | `FALL_THROUGH`
<a id="insn-005bb0f4"></a> `005bb0f4` | `ff 0f 01 39` | strb wzr,[sp, #0x43] | `FALL_THROUGH`
<a id="insn-005bb0f8"></a> `005bb0f8` | `ff 8f 01 39` | strb wzr,[sp, #0x63] | `FALL_THROUGH`
<a id="insn-005bb0fc"></a> `005bb0fc` | `ff 0f 02 39` | strb wzr,[sp, #0x83] | `FALL_THROUGH`
<a id="insn-005bb100"></a> `005bb100` | `ff 8f 02 39` | strb wzr,[sp, #0xa3] | `FALL_THROUGH`
<a id="insn-005bb104"></a> `005bb104` | `ff 0f 03 39` | strb wzr,[sp, #0xc3] | `FALL_THROUGH`
<a id="insn-005bb108"></a> `005bb108` | `88 92 0d 78` | sturh w8,[x20, #0xd9] | `FALL_THROUGH`
<a id="insn-005bb10c"></a> `005bb10c` | `80 92 8c 3c` | stur q0,[x20, #0xc9] | `FALL_THROUGH`
<a id="insn-005bb110"></a> `005bb110` | `ff 8f 03 39` | strb wzr,[sp, #0xe3] | `FALL_THROUGH`
<a id="insn-005bb114"></a> `005bb114` | `7f 0a 00 f9` | str xzr,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-005bb118"></a> `005bb118` | `3f 8c 00 f8` | str xzr,[x1, #0x8]! | `FALL_THROUGH`
<a id="insn-005bb11c"></a> `005bb11c` | `61 02 00 f9` | str x1,[x19] | `FALL_THROUGH`
<a id="insn-005bb120"></a> `005bb120` | `e2 23 00 91` | add x2,sp,#0x8 | `FALL_THROUGH`
<a id="insn-005bb124"></a> `005bb124` | `e3 23 00 91` | add x3,sp,#0x8 | `FALL_THROUGH`
<a id="insn-005bb128"></a> `005bb128` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-005bb12c"></a> `005bb12c` | `e3 76 f9 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-005bb130"></a> `005bb130` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-005bb134"></a> `005bb134` | `82 82 00 91` | add x2,x20,#0x20 | `FALL_THROUGH`
<a id="insn-005bb138"></a> `005bb138` | `83 82 00 91` | add x3,x20,#0x20 | `FALL_THROUGH`
<a id="insn-005bb13c"></a> `005bb13c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-005bb140"></a> `005bb140` | `de 76 f9 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-005bb144"></a> `005bb144` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-005bb148"></a> `005bb148` | `82 02 01 91` | add x2,x20,#0x40 | `FALL_THROUGH`
<a id="insn-005bb14c"></a> `005bb14c` | `83 02 01 91` | add x3,x20,#0x40 | `FALL_THROUGH`
<a id="insn-005bb150"></a> `005bb150` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-005bb154"></a> `005bb154` | `d9 76 f9 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-005bb158"></a> `005bb158` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-005bb15c"></a> `005bb15c` | `82 82 01 91` | add x2,x20,#0x60 | `FALL_THROUGH`
<a id="insn-005bb160"></a> `005bb160` | `83 82 01 91` | add x3,x20,#0x60 | `FALL_THROUGH`
<a id="insn-005bb164"></a> `005bb164` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-005bb168"></a> `005bb168` | `d4 76 f9 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-005bb16c"></a> `005bb16c` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-005bb170"></a> `005bb170` | `82 02 02 91` | add x2,x20,#0x80 | `FALL_THROUGH`
<a id="insn-005bb174"></a> `005bb174` | `83 02 02 91` | add x3,x20,#0x80 | `FALL_THROUGH`
<a id="insn-005bb178"></a> `005bb178` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-005bb17c"></a> `005bb17c` | `cf 76 f9 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-005bb180"></a> `005bb180` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-005bb184"></a> `005bb184` | `82 82 02 91` | add x2,x20,#0xa0 | `FALL_THROUGH`
<a id="insn-005bb188"></a> `005bb188` | `83 82 02 91` | add x3,x20,#0xa0 | `FALL_THROUGH`
<a id="insn-005bb18c"></a> `005bb18c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-005bb190"></a> `005bb190` | `ca 76 f9 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-005bb194"></a> `005bb194` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-005bb198"></a> `005bb198` | `82 02 03 91` | add x2,x20,#0xc0 | `FALL_THROUGH`
<a id="insn-005bb19c"></a> `005bb19c` | `83 02 03 91` | add x3,x20,#0xc0 | `FALL_THROUGH`
<a id="insn-005bb1a0"></a> `005bb1a0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-005bb1a4"></a> `005bb1a4` | `c5 76 f9 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-005bb1a8"></a> `005bb1a8` | `e8 43 43 39` | ldrb w8,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-005bb1ac"></a> `005bb1ac` | `e8 03 00 37` | tbnz w8,#0x0,0x005bb228 | `CONDITIONAL_JUMP`
<a id="insn-005bb1b0"></a> `005bb1b0` | `e8 c3 42 39` | ldrb w8,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-005bb1b4"></a> `005bb1b4` | `28 04 00 37` | tbnz w8,#0x0,0x005bb238 | `CONDITIONAL_JUMP`
<a id="insn-005bb1b8"></a> `005bb1b8` | `e8 43 42 39` | ldrb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-005bb1bc"></a> `005bb1bc` | `68 04 00 37` | tbnz w8,#0x0,0x005bb248 | `CONDITIONAL_JUMP`
<a id="insn-005bb1c0"></a> `005bb1c0` | `e8 c3 41 39` | ldrb w8,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-005bb1c4"></a> `005bb1c4` | `a8 04 00 37` | tbnz w8,#0x0,0x005bb258 | `CONDITIONAL_JUMP`
<a id="insn-005bb1c8"></a> `005bb1c8` | `e8 43 41 39` | ldrb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-005bb1cc"></a> `005bb1cc` | `e8 04 00 37` | tbnz w8,#0x0,0x005bb268 | `CONDITIONAL_JUMP`
<a id="insn-005bb1d0"></a> `005bb1d0` | `e8 c3 40 39` | ldrb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-005bb1d4"></a> `005bb1d4` | `28 05 00 37` | tbnz w8,#0x0,0x005bb278 | `CONDITIONAL_JUMP`
<a id="insn-005bb1d8"></a> `005bb1d8` | `e8 43 40 39` | ldrb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-005bb1dc"></a> `005bb1dc` | `68 00 00 36` | tbz w8,#0x0,0x005bb1e8 | `CONDITIONAL_JUMP`
<a id="insn-005bb1e0"></a> `005bb1e0` | `e0 13 40 f9` | ldr x0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-005bb1e4"></a> `005bb1e4` | `5f 7f 18 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-005bb1e8"></a> `005bb1e8` | `e0 f2 ff b0` | adrp x0,0x418000 | `FALL_THROUGH`
<a id="insn-005bb1ec"></a> `005bb1ec` | `00 c0 0c 91` | add x0,x0,#0x330 | `FALL_THROUGH`
<a id="insn-005bb1f0"></a> `005bb1f0` | `41 33 00 f0` | adrp x1,0xc26000 | `FALL_THROUGH`
<a id="insn-005bb1f4"></a> `005bb1f4` | `21 40 23 91` | add x1,x1,#0x8d0 | `FALL_THROUGH`
<a id="insn-005bb1f8"></a> `005bb1f8` | `42 31 00 d0` | adrp x2,0xbe5000 | `FALL_THROUGH`
<a id="insn-005bb1fc"></a> `005bb1fc` | `42 40 3b 91` | add x2,x2,#0xed0 | `FALL_THROUGH`
<a id="insn-005bb200"></a> `005bb200` | `38 7f 18 94` | bl 0x00bdaee0 | `UNCONDITIONAL_CALL`
<a id="insn-005bb204"></a> `005bb204` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-005bb208"></a> `005bb208` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-005bb20c"></a> `005bb20c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-005bb210"></a> `005bb210` | `41 0a 00 54` | b.ne 0x005bb358 | `CONDITIONAL_JUMP`
<a id="insn-005bb214"></a> `005bb214` | `f4 4f 51 a9` | ldp x20,x19,[sp, #0x110] | `FALL_THROUGH`
<a id="insn-005bb218"></a> `005bb218` | `fc 57 50 a9` | ldp x28,x21,[sp, #0x100] | `FALL_THROUGH`
<a id="insn-005bb21c"></a> `005bb21c` | `fd 7b 4f a9` | ldp x29,x30,[sp, #0xf0] | `FALL_THROUGH`
<a id="insn-005bb220"></a> `005bb220` | `ff 83 04 91` | add sp,sp,#0x120 | `FALL_THROUGH`
<a id="insn-005bb224"></a> `005bb224` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-005bb228"></a> `005bb228` | `e0 73 40 f9` | ldr x0,[sp, #0xe0] | `FALL_THROUGH`
<a id="insn-005bb22c"></a> `005bb22c` | `4d 7f 18 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-005bb230"></a> `005bb230` | `e8 c3 42 39` | ldrb w8,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-005bb234"></a> `005bb234` | `28 fc 07 36` | tbz w8,#0x0,0x005bb1b8 | `CONDITIONAL_JUMP`
<a id="insn-005bb238"></a> `005bb238` | `e0 63 40 f9` | ldr x0,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-005bb23c"></a> `005bb23c` | `49 7f 18 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-005bb240"></a> `005bb240` | `e8 43 42 39` | ldrb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-005bb244"></a> `005bb244` | `e8 fb 07 36` | tbz w8,#0x0,0x005bb1c0 | `CONDITIONAL_JUMP`
<a id="insn-005bb248"></a> `005bb248` | `e0 53 40 f9` | ldr x0,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-005bb24c"></a> `005bb24c` | `45 7f 18 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-005bb250"></a> `005bb250` | `e8 c3 41 39` | ldrb w8,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-005bb254"></a> `005bb254` | `a8 fb 07 36` | tbz w8,#0x0,0x005bb1c8 | `CONDITIONAL_JUMP`
<a id="insn-005bb258"></a> `005bb258` | `e0 43 40 f9` | ldr x0,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-005bb25c"></a> `005bb25c` | `41 7f 18 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-005bb260"></a> `005bb260` | `e8 43 41 39` | ldrb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-005bb264"></a> `005bb264` | `68 fb 07 36` | tbz w8,#0x0,0x005bb1d0 | `CONDITIONAL_JUMP`
<a id="insn-005bb268"></a> `005bb268` | `e0 33 40 f9` | ldr x0,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-005bb26c"></a> `005bb26c` | `3d 7f 18 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-005bb270"></a> `005bb270` | `e8 c3 40 39` | ldrb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-005bb274"></a> `005bb274` | `28 fb 07 36` | tbz w8,#0x0,0x005bb1d8 | `CONDITIONAL_JUMP`
<a id="insn-005bb278"></a> `005bb278` | `e0 23 40 f9` | ldr x0,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-005bb27c"></a> `005bb27c` | `39 7f 18 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-005bb280"></a> `005bb280` | `e8 43 40 39` | ldrb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-005bb284"></a> `005bb284` | `e8 fa 07 37` | tbnz w8,#0x0,0x005bb1e0 | `CONDITIONAL_JUMP`
<a id="insn-005bb288"></a> `005bb288` | `d8 ff ff 17` | b 0x005bb1e8 | `UNCONDITIONAL_JUMP`
<a id="insn-005bb358"></a> `005bb358` | `0e 7f 18 94` | bl 0x00bdaf90 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`005bafcc`](#insn-005bafcc) 範囲 `[['005bafcc', '005bafdb']]`
  - `FALL_THROUGH` [`005bafd8`](#insn-005bafd8) → [`005bafdc`](#insn-005bafdc)
- ブロック [`005bafdc`](#insn-005bafdc) 範囲 `[['005bafdc', '005bafdf']]`
  - `FALL_THROUGH` [`005bafdc`](#insn-005bafdc) → [`005bafe0`](#insn-005bafe0)
- ブロック [`005bafe0`](#insn-005bafe0) 範囲 `[['005bafe0', '005bb02f']]`
  - `FALL_THROUGH` [`005bb02c`](#insn-005bb02c) → [`005bb030`](#insn-005bb030)
- ブロック [`005bb030`](#insn-005bb030) 範囲 `[['005bb030', '005bb0e7']]`
  - `FALL_THROUGH` [`005bb0e4`](#insn-005bb0e4) → [`005bb0e8`](#insn-005bb0e8)
- ブロック [`005bb0e8`](#insn-005bb0e8) 範囲 `[['005bb0e8', '005bb0fb']]`
  - `FALL_THROUGH` [`005bb0f8`](#insn-005bb0f8) → [`005bb0fc`](#insn-005bb0fc)
- ブロック [`005bb0fc`](#insn-005bb0fc) 範囲 `[['005bb0fc', '005bb137']]`
  - `FALL_THROUGH` [`005bb134`](#insn-005bb134) → [`005bb138`](#insn-005bb138)
- ブロック [`005bb138`](#insn-005bb138) 範囲 `[['005bb138', '005bb16f']]`
  - `FALL_THROUGH` [`005bb16c`](#insn-005bb16c) → [`005bb170`](#insn-005bb170)
- ブロック [`005bb170`](#insn-005bb170) 範囲 `[['005bb170', '005bb193']]`
  - `FALL_THROUGH` [`005bb190`](#insn-005bb190) → [`005bb194`](#insn-005bb194)
- ブロック [`005bb194`](#insn-005bb194) 範囲 `[['005bb194', '005bb1af']]`
  - `CONDITIONAL_JUMP` [`005bb1ac`](#insn-005bb1ac) → [`005bb228`](#insn-005bb228)
  - `FALL_THROUGH` [`005bb1ac`](#insn-005bb1ac) → [`005bb1b0`](#insn-005bb1b0)
- ブロック [`005bb1b0`](#insn-005bb1b0) 範囲 `[['005bb1b0', '005bb1b7']]`
  - `CONDITIONAL_JUMP` [`005bb1b4`](#insn-005bb1b4) → [`005bb238`](#insn-005bb238)
  - `FALL_THROUGH` [`005bb1b4`](#insn-005bb1b4) → [`005bb1b8`](#insn-005bb1b8)
- ブロック [`005bb1b8`](#insn-005bb1b8) 範囲 `[['005bb1b8', '005bb1bf']]`
  - `CONDITIONAL_JUMP` [`005bb1bc`](#insn-005bb1bc) → [`005bb248`](#insn-005bb248)
  - `FALL_THROUGH` [`005bb1bc`](#insn-005bb1bc) → [`005bb1c0`](#insn-005bb1c0)
- ブロック [`005bb1c0`](#insn-005bb1c0) 範囲 `[['005bb1c0', '005bb1c7']]`
  - `CONDITIONAL_JUMP` [`005bb1c4`](#insn-005bb1c4) → [`005bb258`](#insn-005bb258)
  - `FALL_THROUGH` [`005bb1c4`](#insn-005bb1c4) → [`005bb1c8`](#insn-005bb1c8)
- ブロック [`005bb1c8`](#insn-005bb1c8) 範囲 `[['005bb1c8', '005bb1cf']]`
  - `CONDITIONAL_JUMP` [`005bb1cc`](#insn-005bb1cc) → [`005bb268`](#insn-005bb268)
  - `FALL_THROUGH` [`005bb1cc`](#insn-005bb1cc) → [`005bb1d0`](#insn-005bb1d0)
- ブロック [`005bb1d0`](#insn-005bb1d0) 範囲 `[['005bb1d0', '005bb1d7']]`
  - `CONDITIONAL_JUMP` [`005bb1d4`](#insn-005bb1d4) → [`005bb278`](#insn-005bb278)
  - `FALL_THROUGH` [`005bb1d4`](#insn-005bb1d4) → [`005bb1d8`](#insn-005bb1d8)
- ブロック [`005bb1d8`](#insn-005bb1d8) 範囲 `[['005bb1d8', '005bb1df']]`
  - `CONDITIONAL_JUMP` [`005bb1dc`](#insn-005bb1dc) → [`005bb1e8`](#insn-005bb1e8)
  - `FALL_THROUGH` [`005bb1dc`](#insn-005bb1dc) → [`005bb1e0`](#insn-005bb1e0)
- ブロック [`005bb1e0`](#insn-005bb1e0) 範囲 `[['005bb1e0', '005bb1e7']]`
  - `FALL_THROUGH` [`005bb1e4`](#insn-005bb1e4) → [`005bb1e8`](#insn-005bb1e8)
- ブロック [`005bb1e8`](#insn-005bb1e8) 範囲 `[['005bb1e8', '005bb20f']]`
  - `FALL_THROUGH` [`005bb20c`](#insn-005bb20c) → [`005bb210`](#insn-005bb210)
- ブロック [`005bb210`](#insn-005bb210) 範囲 `[['005bb210', '005bb213']]`
  - `CONDITIONAL_JUMP` [`005bb210`](#insn-005bb210) → [`005bb358`](#insn-005bb358)
  - `FALL_THROUGH` [`005bb210`](#insn-005bb210) → [`005bb214`](#insn-005bb214)
- ブロック [`005bb214`](#insn-005bb214) 範囲 `[['005bb214', '005bb227']]`
- ブロック [`005bb228`](#insn-005bb228) 範囲 `[['005bb228', '005bb233']]`
  - `FALL_THROUGH` [`005bb230`](#insn-005bb230) → [`005bb234`](#insn-005bb234)
- ブロック [`005bb234`](#insn-005bb234) 範囲 `[['005bb234', '005bb237']]`
  - `CONDITIONAL_JUMP` [`005bb234`](#insn-005bb234) → [`005bb1b8`](#insn-005bb1b8)
  - `FALL_THROUGH` [`005bb234`](#insn-005bb234) → [`005bb238`](#insn-005bb238)
- ブロック [`005bb238`](#insn-005bb238) 範囲 `[['005bb238', '005bb247']]`
  - `CONDITIONAL_JUMP` [`005bb244`](#insn-005bb244) → [`005bb1c0`](#insn-005bb1c0)
  - `FALL_THROUGH` [`005bb244`](#insn-005bb244) → [`005bb248`](#insn-005bb248)
- ブロック [`005bb248`](#insn-005bb248) 範囲 `[['005bb248', '005bb257']]`
  - `CONDITIONAL_JUMP` [`005bb254`](#insn-005bb254) → [`005bb1c8`](#insn-005bb1c8)
  - `FALL_THROUGH` [`005bb254`](#insn-005bb254) → [`005bb258`](#insn-005bb258)
- ブロック [`005bb258`](#insn-005bb258) 範囲 `[['005bb258', '005bb267']]`
  - `CONDITIONAL_JUMP` [`005bb264`](#insn-005bb264) → [`005bb1d0`](#insn-005bb1d0)
  - `FALL_THROUGH` [`005bb264`](#insn-005bb264) → [`005bb268`](#insn-005bb268)
- ブロック [`005bb268`](#insn-005bb268) 範囲 `[['005bb268', '005bb277']]`
  - `CONDITIONAL_JUMP` [`005bb274`](#insn-005bb274) → [`005bb1d8`](#insn-005bb1d8)
  - `FALL_THROUGH` [`005bb274`](#insn-005bb274) → [`005bb278`](#insn-005bb278)
- ブロック [`005bb278`](#insn-005bb278) 範囲 `[['005bb278', '005bb27f']]`
  - `FALL_THROUGH` [`005bb27c`](#insn-005bb27c) → [`005bb280`](#insn-005bb280)
- ブロック [`005bb280`](#insn-005bb280) 範囲 `[['005bb280', '005bb287']]`
  - `CONDITIONAL_JUMP` [`005bb284`](#insn-005bb284) → [`005bb1e0`](#insn-005bb1e0)
  - `FALL_THROUGH` [`005bb284`](#insn-005bb284) → [`005bb288`](#insn-005bb288)
- ブロック [`005bb288`](#insn-005bb288) 範囲 `[['005bb288', '005bb28b']]`
  - `UNCONDITIONAL_JUMP` [`005bb288`](#insn-005bb288) → [`005bb1e8`](#insn-005bb1e8)
- ブロック [`005bb358`](#insn-005bb358) 範囲 `[['005bb358', '005bb35b']]`

## 命令位置別の参照

- [`005bafd0`](#insn-005bafd0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bafd4`](#insn-005bafd4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bafd8`](#insn-005bafd8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005baffc`](#insn-005baffc) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bb008`](#insn-005bb008) → `002a72e4`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`005bb010`](#insn-005bb010) → `Stack[-0xff]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bb014`](#insn-005bb014) → `Stack[-0xf8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bb024`](#insn-005bb024) → `Stack[-0x10f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bb02c`](#insn-005bb02c) → `002a72f7`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`005bb030`](#insn-005bb030) → `Stack[-0xdf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bb038`](#insn-005bb038) → `Stack[-0xd8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bb048`](#insn-005bb048) → `Stack[-0xef]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bb04c`](#insn-005bb04c) → `002a80da`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`005bb050`](#insn-005bb050) → `Stack[-0xbf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bb058`](#insn-005bb058) → `Stack[-0xb8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bb068`](#insn-005bb068) → `Stack[-0xcf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bb06c`](#insn-005bb06c) → `002936ae`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`005bb070`](#insn-005bb070) → `Stack[-0x9f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bb078`](#insn-005bb078) → `Stack[-0x98]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bb084`](#insn-005bb084) → `Stack[-0xaf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bb088`](#insn-005bb088) → `0029c2e1`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`005bb090`](#insn-005bb090) → `Stack[-0x7f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bb098`](#insn-005bb098) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bb0a4`](#insn-005bb0a4) → `Stack[-0x8f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bb0a8`](#insn-005bb0a8) → `00291877`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`005bb0b0`](#insn-005bb0b0) → `Stack[-0x5f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bb0b8`](#insn-005bb0b8) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bb0c4`](#insn-005bb0c4) → `Stack[-0x6f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bb0c8`](#insn-005bb0c8) → `00294526`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`005bb0cc`](#insn-005bb0cc) → `Stack[-0x110]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bb0d0`](#insn-005bb0d0) → `Stack[-0xf0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bb0d4`](#insn-005bb0d4) → `Stack[-0xd0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bb0d8`](#insn-005bb0d8) → `Stack[-0xb0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bb0dc`](#insn-005bb0dc) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bb0e0`](#insn-005bb0e0) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bb0e4`](#insn-005bb0e4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bb0ec`](#insn-005bb0ec) → `Stack[-0x118]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bb0f0`](#insn-005bb0f0) → `Stack[-0xfd]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bb0f4`](#insn-005bb0f4) → `Stack[-0xdd]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bb0f8`](#insn-005bb0f8) → `Stack[-0xbd]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bb0fc`](#insn-005bb0fc) → `Stack[-0x9d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bb100`](#insn-005bb100) → `Stack[-0x7d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bb104`](#insn-005bb104) → `Stack[-0x5d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bb108`](#insn-005bb108) → `Stack[-0x3f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bb10c`](#insn-005bb10c) → `Stack[-0x4f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bb110`](#insn-005bb110) → `Stack[-0x3d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bb114`](#insn-005bb114) → `00c268e0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`005bb118`](#insn-005bb118) → `00c268d8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`005bb11c`](#insn-005bb11c) → `00c268d0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`005bb11c`](#insn-005bb11c) → `00c268d8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`005bb128`](#insn-005bb128) → `00c268d0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`005bb12c`](#insn-005bb12c) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`005bb130`](#insn-005bb130) → `00c268d8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`005bb13c`](#insn-005bb13c) → `00c268d0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`005bb140`](#insn-005bb140) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`005bb144`](#insn-005bb144) → `00c268d8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`005bb150`](#insn-005bb150) → `00c268d0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`005bb154`](#insn-005bb154) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`005bb158`](#insn-005bb158) → `00c268d8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`005bb164`](#insn-005bb164) → `00c268d0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`005bb168`](#insn-005bb168) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`005bb16c`](#insn-005bb16c) → `00c268d8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`005bb178`](#insn-005bb178) → `00c268d0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`005bb17c`](#insn-005bb17c) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`005bb180`](#insn-005bb180) → `00c268d8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`005bb18c`](#insn-005bb18c) → `00c268d0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`005bb190`](#insn-005bb190) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`005bb194`](#insn-005bb194) → `00c268d8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`005bb1a0`](#insn-005bb1a0) → `00c268d0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`005bb1a4`](#insn-005bb1a4) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`005bb1a8`](#insn-005bb1a8) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bb1ac`](#insn-005bb1ac) → [`005bb228`](#insn-005bb228) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bb1b0`](#insn-005bb1b0) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bb1b4`](#insn-005bb1b4) → [`005bb238`](#insn-005bb238) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bb1b8`](#insn-005bb1b8) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bb1bc`](#insn-005bb1bc) → [`005bb248`](#insn-005bb248) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bb1c0`](#insn-005bb1c0) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bb1c4`](#insn-005bb1c4) → [`005bb258`](#insn-005bb258) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bb1c8`](#insn-005bb1c8) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bb1cc`](#insn-005bb1cc) → [`005bb268`](#insn-005bb268) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bb1d0`](#insn-005bb1d0) → `Stack[-0xf0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bb1d4`](#insn-005bb1d4) → [`005bb278`](#insn-005bb278) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bb1d8`](#insn-005bb1d8) → `Stack[-0x110]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bb1dc`](#insn-005bb1dc) → [`005bb1e8`](#insn-005bb1e8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bb1e0`](#insn-005bb1e0) → `Stack[-0x100]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bb1e4`](#insn-005bb1e4) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`005bb1ec`](#insn-005bb1ec) → [`00418330`](../00418/00418330.md) · `PARAM` · `ANALYSIS` · 関数 `00418330` · 推定シンボル `None` · 推定型 `None`
- [`005bb1f4`](#insn-005bb1f4) → `00c268d0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`005bb1fc`](#insn-005bb1fc) → `00be5ed0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`005bb200`](#insn-005bb200) → [`00bdaee0`](../00bda/00bdaee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaee0` · 推定シンボル `None` · 推定型 `None`
- [`005bb208`](#insn-005bb208) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bb210`](#insn-005bb210) → [`005bb358`](#insn-005bb358) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bb214`](#insn-005bb214) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bb218`](#insn-005bb218) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bb21c`](#insn-005bb21c) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bb228`](#insn-005bb228) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bb22c`](#insn-005bb22c) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`005bb230`](#insn-005bb230) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bb234`](#insn-005bb234) → [`005bb1b8`](#insn-005bb1b8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bb238`](#insn-005bb238) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bb23c`](#insn-005bb23c) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`005bb240`](#insn-005bb240) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bb244`](#insn-005bb244) → [`005bb1c0`](#insn-005bb1c0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bb248`](#insn-005bb248) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bb24c`](#insn-005bb24c) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`005bb250`](#insn-005bb250) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bb254`](#insn-005bb254) → [`005bb1c8`](#insn-005bb1c8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bb258`](#insn-005bb258) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bb25c`](#insn-005bb25c) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`005bb260`](#insn-005bb260) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bb264`](#insn-005bb264) → [`005bb1d0`](#insn-005bb1d0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bb268`](#insn-005bb268) → `Stack[-0xc0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bb26c`](#insn-005bb26c) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`005bb270`](#insn-005bb270) → `Stack[-0xf0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bb274`](#insn-005bb274) → [`005bb1d8`](#insn-005bb1d8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bb278`](#insn-005bb278) → `Stack[-0xe0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bb27c`](#insn-005bb27c) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`005bb280`](#insn-005bb280) → `Stack[-0x110]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bb284`](#insn-005bb284) → [`005bb1e0`](#insn-005bb1e0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bb288`](#insn-005bb288) → [`005bb1e8`](#insn-005bb1e8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bb358`](#insn-005bb358) → [`00bdaf90`](../00bda/00bdaf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf90` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`005bafd0`](#insn-005bafd0)

~~~json
{
  "source": "005bafd0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bafd4`](#insn-005bafd4)

~~~json
{
  "source": "005bafd4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bafd8`](#insn-005bafd8)

~~~json
{
  "source": "005bafd8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005baffc`](#insn-005baffc)

~~~json
{
  "source": "005baffc",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bb008`](#insn-005bb008)

~~~json
{
  "source": "005bb008",
  "target": "002a72e4",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a72e4",
  "offset": 0,
  "size": 19,
  "datatype": "string",
  "bytes": "43676b496a4d33795f5a516145414951416700",
  "capture_start": "002a72e4",
  "capture_bytes": 19,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`005bb010`](#insn-005bb010)

~~~json
{
  "source": "005bb010",
  "target": "Stack[-0xff]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bb014`](#insn-005bb014)

~~~json
{
  "source": "005bb014",
  "target": "Stack[-0xf8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bb024`](#insn-005bb024)

~~~json
{
  "source": "005bb024",
  "target": "Stack[-0x10f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bb02c`](#insn-005bb02c)

~~~json
{
  "source": "005bb02c",
  "target": "002a72f7",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a72f7",
  "offset": 0,
  "size": 19,
  "datatype": "string",
  "bytes": "43676b496a4d33795f5a516145414951424100",
  "capture_start": "002a72f7",
  "capture_bytes": 19,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`005bb030`](#insn-005bb030)

~~~json
{
  "source": "005bb030",
  "target": "Stack[-0xdf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bb038`](#insn-005bb038)

~~~json
{
  "source": "005bb038",
  "target": "Stack[-0xd8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bb048`](#insn-005bb048)

~~~json
{
  "source": "005bb048",
  "target": "Stack[-0xef]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bb04c`](#insn-005bb04c)

~~~json
{
  "source": "005bb04c",
  "target": "002a80da",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a80da",
  "offset": 0,
  "size": 19,
  "datatype": "string",
  "bytes": "43676b496a4d33795f5a516145414951426700",
  "capture_start": "002a80da",
  "capture_bytes": 19,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`005bb050`](#insn-005bb050)

~~~json
{
  "source": "005bb050",
  "target": "Stack[-0xbf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bb058`](#insn-005bb058)

~~~json
{
  "source": "005bb058",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bb068`](#insn-005bb068)

~~~json
{
  "source": "005bb068",
  "target": "Stack[-0xcf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bb06c`](#insn-005bb06c)

~~~json
{
  "source": "005bb06c",
  "target": "002936ae",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002936ae",
  "offset": 0,
  "size": 19,
  "datatype": "string",
  "bytes": "43676b496a4d33795f5a516145414951417700",
  "capture_start": "002936ae",
  "capture_bytes": 19,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`005bb070`](#insn-005bb070)

~~~json
{
  "source": "005bb070",
  "target": "Stack[-0x9f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bb078`](#insn-005bb078)

~~~json
{
  "source": "005bb078",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bb084`](#insn-005bb084)

~~~json
{
  "source": "005bb084",
  "target": "Stack[-0xaf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bb088`](#insn-005bb088)

~~~json
{
  "source": "005bb088",
  "target": "0029c2e1",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029c2e1",
  "offset": 0,
  "size": 19,
  "datatype": "string",
  "bytes": "43676b496a4d33795f5a516145414951425100",
  "capture_start": "0029c2e1",
  "capture_bytes": 19,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`005bb090`](#insn-005bb090)

~~~json
{
  "source": "005bb090",
  "target": "Stack[-0x7f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bb098`](#insn-005bb098)

~~~json
{
  "source": "005bb098",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bb0a4`](#insn-005bb0a4)

~~~json
{
  "source": "005bb0a4",
  "target": "Stack[-0x8f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bb0a8`](#insn-005bb0a8)

~~~json
{
  "source": "005bb0a8",
  "target": "00291877",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00291877",
  "offset": 0,
  "size": 19,
  "datatype": "string",
  "bytes": "43676b496a4d33795f5a516145414951427700",
  "capture_start": "00291877",
  "capture_bytes": 19,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`005bb0b0`](#insn-005bb0b0)

~~~json
{
  "source": "005bb0b0",
  "target": "Stack[-0x5f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bb0b8`](#insn-005bb0b8)

~~~json
{
  "source": "005bb0b8",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bb0c4`](#insn-005bb0c4)

~~~json
{
  "source": "005bb0c4",
  "target": "Stack[-0x6f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bb0c8`](#insn-005bb0c8)

~~~json
{
  "source": "005bb0c8",
  "target": "00294526",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00294526",
  "offset": 0,
  "size": 19,
  "datatype": "string",
  "bytes": "43676b496a4d33795f5a516145414951434100",
  "capture_start": "00294526",
  "capture_bytes": 19,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`005bb0cc`](#insn-005bb0cc)

~~~json
{
  "source": "005bb0cc",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bb0d0`](#insn-005bb0d0)

~~~json
{
  "source": "005bb0d0",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bb0d4`](#insn-005bb0d4)

~~~json
{
  "source": "005bb0d4",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bb0d8`](#insn-005bb0d8)

~~~json
{
  "source": "005bb0d8",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bb0dc`](#insn-005bb0dc)

~~~json
{
  "source": "005bb0dc",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bb0e0`](#insn-005bb0e0)

~~~json
{
  "source": "005bb0e0",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bb0e4`](#insn-005bb0e4)

~~~json
{
  "source": "005bb0e4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bb0ec`](#insn-005bb0ec)

~~~json
{
  "source": "005bb0ec",
  "target": "Stack[-0x118]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bb0f0`](#insn-005bb0f0)

~~~json
{
  "source": "005bb0f0",
  "target": "Stack[-0xfd]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bb0f4`](#insn-005bb0f4)

~~~json
{
  "source": "005bb0f4",
  "target": "Stack[-0xdd]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bb0f8`](#insn-005bb0f8)

~~~json
{
  "source": "005bb0f8",
  "target": "Stack[-0xbd]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bb0fc`](#insn-005bb0fc)

~~~json
{
  "source": "005bb0fc",
  "target": "Stack[-0x9d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bb100`](#insn-005bb100)

~~~json
{
  "source": "005bb100",
  "target": "Stack[-0x7d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bb104`](#insn-005bb104)

~~~json
{
  "source": "005bb104",
  "target": "Stack[-0x5d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bb108`](#insn-005bb108)

~~~json
{
  "source": "005bb108",
  "target": "Stack[-0x3f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bb10c`](#insn-005bb10c)

~~~json
{
  "source": "005bb10c",
  "target": "Stack[-0x4f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bb110`](#insn-005bb110)

~~~json
{
  "source": "005bb110",
  "target": "Stack[-0x3d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bb114`](#insn-005bb114)

~~~json
{
  "source": "005bb114",
  "target": "00c268e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c268e0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`005bb118`](#insn-005bb118)

~~~json
{
  "source": "005bb118",
  "target": "00c268d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c268d8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`005bb11c`](#insn-005bb11c)

~~~json
{
  "source": "005bb11c",
  "target": "00c268d0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c268d0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`005bb11c`](#insn-005bb11c)

~~~json
{
  "source": "005bb11c",
  "target": "00c268d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c268d8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`005bb128`](#insn-005bb128)

~~~json
{
  "source": "005bb128",
  "target": "00c268d0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c268d0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`005bb12c`](#insn-005bb12c)

~~~json
{
  "source": "005bb12c",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005bb130`](#insn-005bb130)

~~~json
{
  "source": "005bb130",
  "target": "00c268d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c268d8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`005bb13c`](#insn-005bb13c)

~~~json
{
  "source": "005bb13c",
  "target": "00c268d0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c268d0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`005bb140`](#insn-005bb140)

~~~json
{
  "source": "005bb140",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005bb144`](#insn-005bb144)

~~~json
{
  "source": "005bb144",
  "target": "00c268d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c268d8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`005bb150`](#insn-005bb150)

~~~json
{
  "source": "005bb150",
  "target": "00c268d0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c268d0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`005bb154`](#insn-005bb154)

~~~json
{
  "source": "005bb154",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005bb158`](#insn-005bb158)

~~~json
{
  "source": "005bb158",
  "target": "00c268d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c268d8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`005bb164`](#insn-005bb164)

~~~json
{
  "source": "005bb164",
  "target": "00c268d0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c268d0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`005bb168`](#insn-005bb168)

~~~json
{
  "source": "005bb168",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005bb16c`](#insn-005bb16c)

~~~json
{
  "source": "005bb16c",
  "target": "00c268d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c268d8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`005bb178`](#insn-005bb178)

~~~json
{
  "source": "005bb178",
  "target": "00c268d0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c268d0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`005bb17c`](#insn-005bb17c)

~~~json
{
  "source": "005bb17c",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005bb180`](#insn-005bb180)

~~~json
{
  "source": "005bb180",
  "target": "00c268d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c268d8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`005bb18c`](#insn-005bb18c)

~~~json
{
  "source": "005bb18c",
  "target": "00c268d0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c268d0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`005bb190`](#insn-005bb190)

~~~json
{
  "source": "005bb190",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005bb194`](#insn-005bb194)

~~~json
{
  "source": "005bb194",
  "target": "00c268d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c268d8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`005bb1a0`](#insn-005bb1a0)

~~~json
{
  "source": "005bb1a0",
  "target": "00c268d0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c268d0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`005bb1a4`](#insn-005bb1a4)

~~~json
{
  "source": "005bb1a4",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005bb1a8`](#insn-005bb1a8)

~~~json
{
  "source": "005bb1a8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bb1ac`](#insn-005bb1ac)

~~~json
{
  "source": "005bb1ac",
  "target": "005bb228",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bb1b0`](#insn-005bb1b0)

~~~json
{
  "source": "005bb1b0",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bb1b4`](#insn-005bb1b4)

~~~json
{
  "source": "005bb1b4",
  "target": "005bb238",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bb1b8`](#insn-005bb1b8)

~~~json
{
  "source": "005bb1b8",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bb1bc`](#insn-005bb1bc)

~~~json
{
  "source": "005bb1bc",
  "target": "005bb248",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bb1c0`](#insn-005bb1c0)

~~~json
{
  "source": "005bb1c0",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bb1c4`](#insn-005bb1c4)

~~~json
{
  "source": "005bb1c4",
  "target": "005bb258",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bb1c8`](#insn-005bb1c8)

~~~json
{
  "source": "005bb1c8",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bb1cc`](#insn-005bb1cc)

~~~json
{
  "source": "005bb1cc",
  "target": "005bb268",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bb1d0`](#insn-005bb1d0)

~~~json
{
  "source": "005bb1d0",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bb1d4`](#insn-005bb1d4)

~~~json
{
  "source": "005bb1d4",
  "target": "005bb278",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bb1d8`](#insn-005bb1d8)

~~~json
{
  "source": "005bb1d8",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bb1dc`](#insn-005bb1dc)

~~~json
{
  "source": "005bb1dc",
  "target": "005bb1e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bb1e0`](#insn-005bb1e0)

~~~json
{
  "source": "005bb1e0",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bb1e4`](#insn-005bb1e4)

~~~json
{
  "source": "005bb1e4",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005bb1ec`](#insn-005bb1ec)

~~~json
{
  "source": "005bb1ec",
  "target": "00418330",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005bb1f4`](#insn-005bb1f4)

~~~json
{
  "source": "005bb1f4",
  "target": "00c268d0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c268d0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`005bb1fc`](#insn-005bb1fc)

~~~json
{
  "source": "005bb1fc",
  "target": "00be5ed0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00be5ed0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`005bb200`](#insn-005bb200)

~~~json
{
  "source": "005bb200",
  "target": "00bdaee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005bb208`](#insn-005bb208)

~~~json
{
  "source": "005bb208",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bb210`](#insn-005bb210)

~~~json
{
  "source": "005bb210",
  "target": "005bb358",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bb214`](#insn-005bb214)

~~~json
{
  "source": "005bb214",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bb218`](#insn-005bb218)

~~~json
{
  "source": "005bb218",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bb21c`](#insn-005bb21c)

~~~json
{
  "source": "005bb21c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bb228`](#insn-005bb228)

~~~json
{
  "source": "005bb228",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bb22c`](#insn-005bb22c)

~~~json
{
  "source": "005bb22c",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005bb230`](#insn-005bb230)

~~~json
{
  "source": "005bb230",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bb234`](#insn-005bb234)

~~~json
{
  "source": "005bb234",
  "target": "005bb1b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bb238`](#insn-005bb238)

~~~json
{
  "source": "005bb238",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bb23c`](#insn-005bb23c)

~~~json
{
  "source": "005bb23c",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005bb240`](#insn-005bb240)

~~~json
{
  "source": "005bb240",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bb244`](#insn-005bb244)

~~~json
{
  "source": "005bb244",
  "target": "005bb1c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bb248`](#insn-005bb248)

~~~json
{
  "source": "005bb248",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bb24c`](#insn-005bb24c)

~~~json
{
  "source": "005bb24c",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005bb250`](#insn-005bb250)

~~~json
{
  "source": "005bb250",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bb254`](#insn-005bb254)

~~~json
{
  "source": "005bb254",
  "target": "005bb1c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bb258`](#insn-005bb258)

~~~json
{
  "source": "005bb258",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bb25c`](#insn-005bb25c)

~~~json
{
  "source": "005bb25c",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005bb260`](#insn-005bb260)

~~~json
{
  "source": "005bb260",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bb264`](#insn-005bb264)

~~~json
{
  "source": "005bb264",
  "target": "005bb1d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bb268`](#insn-005bb268)

~~~json
{
  "source": "005bb268",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bb26c`](#insn-005bb26c)

~~~json
{
  "source": "005bb26c",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005bb270`](#insn-005bb270)

~~~json
{
  "source": "005bb270",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bb274`](#insn-005bb274)

~~~json
{
  "source": "005bb274",
  "target": "005bb1d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bb278`](#insn-005bb278)

~~~json
{
  "source": "005bb278",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bb27c`](#insn-005bb27c)

~~~json
{
  "source": "005bb27c",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005bb280`](#insn-005bb280)

~~~json
{
  "source": "005bb280",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bb284`](#insn-005bb284)

~~~json
{
  "source": "005bb284",
  "target": "005bb1e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bb288`](#insn-005bb288)

~~~json
{
  "source": "005bb288",
  "target": "005bb1e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bb358`](#insn-005bb358)

~~~json
{
  "source": "005bb358",
  "target": "00bdaf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
