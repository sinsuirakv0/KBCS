# 00adfc9c

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00adfbd4`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00adf/00adfbd4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0057.md#compare-70782906235216062f0d645a567b24a7)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00adfce0`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adf/00adfce0.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0060.md#compare-2ccf8c57a8f54f4114aa86bcce16a9b4)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00adfc9c",
  "name": "_INIT_268",
  "size": 708,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "82735594ce605330ae9cb02e0155d2e2f1a8e9037d3f47bc562358854ac707f8",
  "source_text_sha256": "82735594ce605330ae9cb02e0155d2e2f1a8e9037d3f47bc562358854ac707f8",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00adfc9c",
        "00adff5b"
      ],
      [
        "00ae0028",
        "00ae002b"
      ]
    ],
    "bytes_sha256": "367b65298c047388920fbbf9175c7806a840f7a44fb9027c1779fb40a754ac10",
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
- [00bdaf90](../00bda/00bdaf90.md)
- [00bdb010](../00bdb/00bdb010.md)
- [00bdb040](../00bdb/00bdb040.md)

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

## 疑似コード / UTF-8 6250 bytes

~~~c

/* WARNING: Type propagation algorithm not settling */

void _INIT_268(void)

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
                    /* try { // try from 00adfce0 to 00bdfd77 has its CatchHandler @ 00adfce0
                       catch() { ... } // from try @ 00adfce0 with catch @ 00adfce0
                       catch() { ... } // from try @ 00adfd88 with catch @ 00adfce0
                       catch() { ... } // from try @ 00adff44 with catch @ 00adfce0
                       catch() { ... } // from try @ 00ae0334 with catch @ 00adfce0
                       catch() { ... } // from try @ 00ae0410 with catch @ 00adfce0 */
  uStack_ff = 0x6741;
  local_f8[0] = 1;
  uStack_107 = (undefined7)s_CgkIjM3y_ZQaEAIQAg_002a72dd._8_8_;
  cStack_100 = SUB81(s_CgkIjM3y_ZQaEAIQAg_002a72dd._8_8_,7);
  local_10f = (char  [8])s_CgkIjM3y_ZQaEAIQAg_002a72dd._0_8_;
  uStack_df = 0x4142;
  local_d8[0] = 2;
  uStack_e7 = (undefined7)s_CgkIjM3y_ZQaEAIQBA_002a72f0._8_8_;
  cStack_e0 = SUB81(s_CgkIjM3y_ZQaEAIQBA_002a72f0._8_8_,7);
  local_ef = (char  [8])s_CgkIjM3y_ZQaEAIQBA_002a72f0._0_8_;
  uStack_bf = 0x6742;
  local_b8[0] = 3;
  uStack_c7 = (undefined7)s_CgkIjM3y_ZQaEAIQBg_002a8046._8_8_;
  cStack_c0 = SUB81(s_CgkIjM3y_ZQaEAIQBg_002a8046._8_8_,7);
  local_cf = (char  [8])s_CgkIjM3y_ZQaEAIQBg_002a8046._0_8_;
  uStack_9f = 0x7741;
  local_98[0] = 4;
  uStack_a7 = (undefined7)s_CgkIjM3y_ZQaEAIQAw_0029373b._8_8_;
  cStack_a0 = SUB81(s_CgkIjM3y_ZQaEAIQAw_0029373b._8_8_,7);
  local_af = (char  [8])s_CgkIjM3y_ZQaEAIQAw_0029373b._0_8_;
  uStack_7f = 0x5142;
  local_78[0] = 5;
  uStack_87 = (undefined7)s_CgkIjM3y_ZQaEAIQBQ_0029c36e._8_8_;
  cStack_80 = SUB81(s_CgkIjM3y_ZQaEAIQBQ_0029c36e._8_8_,7);
  local_8f = (char  [8])s_CgkIjM3y_ZQaEAIQBQ_0029c36e._0_8_;
                    /* try { // try from 00adfd78 to 00bdfd87 has its CatchHandler @ 00ae081c */
  uStack_5f = 0x7742;
                    /* try { // try from 00adfd88 to 00bdfe5f has its CatchHandler @ 00adfce0 */
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
  local_118[0] = 0;
  uStack_fd = 0;
  uStack_dd = 0;
  uStack_bd = 0;
  uStack_9d = 0;
  uStack_7d = 0;
  uStack_5d = 0;
  uStack_3f = 0x4143;
  uStack_47 = (undefined7)s_CgkIjM3y_ZQaEAIQCA_002945b3._8_8_;
  cStack_40 = SUB81(s_CgkIjM3y_ZQaEAIQCA_002945b3._8_8_,7);
  local_4f = (char  [8])s_CgkIjM3y_ZQaEAIQCA_002945b3._0_8_;
  uStack_3d = 0;
  DAT_010a0000 = 0;
  DAT_0109fff8 = 0;
  DAT_0109fff0 = &DAT_0109fff8;
  FUN_00418cb8(&DAT_0109fff0,&DAT_0109fff8,local_118,local_118);
  FUN_00418cb8(&DAT_0109fff0,&DAT_0109fff8,local_f8,local_f8);
  FUN_00418cb8(&DAT_0109fff0,&DAT_0109fff8,local_d8,local_d8);
  FUN_00418cb8(&DAT_0109fff0,&DAT_0109fff8,local_b8,local_b8);
  FUN_00418cb8(&DAT_0109fff0,&DAT_0109fff8,local_98,local_98);
                    /* try { // try from 00adfe60 to 00bdfe6b has its CatchHandler @ 00ae088c */
  FUN_00418cb8(&DAT_0109fff0,&DAT_0109fff8,local_78,local_78);
  FUN_00418cb8(&DAT_0109fff0,&DAT_0109fff8,local_58,local_58);
                    /* try { // try from 00adfe7c to 00bdfe8b has its CatchHandler @ 00ae06b8 */
  if ((local_50 & 1) != 0) {
                    /* try { // try from 00adfefc to 00bdff0f has its CatchHandler @ 00ae088c */
    _ZdlPv((void *)CONCAT44(uStack_3c,CONCAT13(uStack_3d,CONCAT21(uStack_3f,cStack_40))));
  }
  if ((local_70 & 1) != 0) {
    _ZdlPv((void *)CONCAT44(uStack_5c,CONCAT13(uStack_5d,CONCAT21(uStack_5f,cStack_60))));
  }
                    /* try { // try from 00adfe8c to 00bdfe97 has its CatchHandler @ 00ae069c */
  if ((local_90 & 1) != 0) {
    _ZdlPv((void *)CONCAT44(uStack_7c,CONCAT13(uStack_7d,CONCAT21(uStack_7f,cStack_80))));
  }
  if ((local_b0 & 1) != 0) {
                    /* try { // try from 00adff28 to 00bdff43 has its CatchHandler @ 00ae07cc */
    _ZdlPv((void *)CONCAT44(uStack_9c,CONCAT13(uStack_9d,CONCAT21(uStack_9f,cStack_a0))));
  }
                    /* try { // try from 00adfe9c to 00bdfea3 has its CatchHandler @ 00ae0680 */
  if ((local_d0 & 1) != 0) {
    _ZdlPv((void *)CONCAT44(uStack_bc,CONCAT13(uStack_bd,CONCAT21(uStack_bf,cStack_c0))));
  }
                    /* try { // try from 00adff44 to 00be00af has its CatchHandler @ 00adfce0 */
  if ((local_f0 & 1) != 0) {
    _ZdlPv((void *)CONCAT44(uStack_dc,CONCAT13(uStack_dd,CONCAT21(uStack_df,cStack_e0))));
  }
  if ((local_110 & 1) != 0) {
    _ZdlPv((void *)CONCAT44(uStack_fc,CONCAT13(uStack_fd,CONCAT21(uStack_ff,cStack_100))));
  }
  __cxa_atexit(FUN_00418330,&DAT_0109fff0,&PTR_LOOP_00be5f80);
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
<a id="insn-00adfc9c"></a> `00adfc9c` | `ff 83 04 d1` | sub sp,sp,#0x120 | `FALL_THROUGH`
<a id="insn-00adfca0"></a> `00adfca0` | `fd 7b 0f a9` | stp x29,x30,[sp, #0xf0] | `FALL_THROUGH`
<a id="insn-00adfca4"></a> `00adfca4` | `fc 57 10 a9` | stp x28,x21,[sp, #0x100] | `FALL_THROUGH`
<a id="insn-00adfca8"></a> `00adfca8` | `f4 4f 11 a9` | stp x20,x19,[sp, #0x110] | `FALL_THROUGH`
<a id="insn-00adfcac"></a> `00adfcac` | `fd c3 03 91` | add x29,sp,#0xf0 | `FALL_THROUGH`
<a id="insn-00adfcb0"></a> `00adfcb0` | `55 d0 3b d5` | mrs x21,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00adfcb4"></a> `00adfcb4` | `2a e8 8c 52` | mov w10,#0x6741 | `FALL_THROUGH`
<a id="insn-00adfcb8"></a> `00adfcb8` | `f4 23 00 91` | add x20,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00adfcbc"></a> `00adfcbc` | `a9 16 40 f9` | ldr x9,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00adfcc0"></a> `00adfcc0` | `88 04 80 52` | mov w8,#0x24 | `FALL_THROUGH`
<a id="insn-00adfcc4"></a> `00adfcc4` | `13 2e 00 90` | adrp x19,0x109f000 | `FALL_THROUGH`
<a id="insn-00adfcc8"></a> `00adfcc8` | `73 c2 3f 91` | add x19,x19,#0xff0 | `FALL_THROUGH`
<a id="insn-00adfccc"></a> `00adfccc` | `a9 83 1f f8` | stur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00adfcd0"></a> `00adfcd0` | `49 be ff 90` | adrp x9,0x2a7000 | `FALL_THROUGH`
<a id="insn-00adfcd4"></a> `00adfcd4` | `29 75 0b 91` | add x9,x9,#0x2dd | `FALL_THROUGH`
<a id="insn-00adfcd8"></a> `00adfcd8` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00adfcdc"></a> `00adfcdc` | `29 00 80 52` | mov w9,#0x1 | `FALL_THROUGH`
<a id="insn-00adfce0"></a> `00adfce0` | `ea 13 02 78` | sturh w10,[sp, #0x21] | `FALL_THROUGH`
<a id="insn-00adfce4"></a> `00adfce4` | `e9 2b 00 b9` | str w9,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00adfce8"></a> `00adfce8` | `49 28 88 52` | mov w9,#0x4142 | `FALL_THROUGH`
<a id="insn-00adfcec"></a> `00adfcec` | `4a be ff 90` | adrp x10,0x2a7000 | `FALL_THROUGH`
<a id="insn-00adfcf0"></a> `00adfcf0` | `4a c1 0b 91` | add x10,x10,#0x2f0 | `FALL_THROUGH`
<a id="insn-00adfcf4"></a> `00adfcf4` | `e0 13 81 3c` | stur q0,[sp, #0x11] | `FALL_THROUGH`
<a id="insn-00adfcf8"></a> `00adfcf8` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00adfcfc"></a> `00adfcfc` | `40 01 c0 3d` | ldr q0,[x10] | `FALL_THROUGH`
<a id="insn-00adfd00"></a> `00adfd00` | `e9 13 04 78` | sturh w9,[sp, #0x41] | `FALL_THROUGH`
<a id="insn-00adfd04"></a> `00adfd04` | `49 00 80 52` | mov w9,#0x2 | `FALL_THROUGH`
<a id="insn-00adfd08"></a> `00adfd08` | `e9 4b 00 b9` | str w9,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00adfd0c"></a> `00adfd0c` | `49 e8 8c 52` | mov w9,#0x6742 | `FALL_THROUGH`
<a id="insn-00adfd10"></a> `00adfd10` | `4a be ff b0` | adrp x10,0x2a8000 | `FALL_THROUGH`
<a id="insn-00adfd14"></a> `00adfd14` | `4a 19 01 91` | add x10,x10,#0x46 | `FALL_THROUGH`
<a id="insn-00adfd18"></a> `00adfd18` | `e0 13 83 3c` | stur q0,[sp, #0x31] | `FALL_THROUGH`
<a id="insn-00adfd1c"></a> `00adfd1c` | `40 01 c0 3d` | ldr q0,[x10] | `FALL_THROUGH`
<a id="insn-00adfd20"></a> `00adfd20` | `e9 13 06 78` | sturh w9,[sp, #0x61] | `FALL_THROUGH`
<a id="insn-00adfd24"></a> `00adfd24` | `69 00 80 52` | mov w9,#0x3 | `FALL_THROUGH`
<a id="insn-00adfd28"></a> `00adfd28` | `e9 6b 00 b9` | str w9,[sp, #0x68] | `FALL_THROUGH`
<a id="insn-00adfd2c"></a> `00adfd2c` | `29 e8 8e 52` | mov w9,#0x7741 | `FALL_THROUGH`
<a id="insn-00adfd30"></a> `00adfd30` | `aa bd ff 90` | adrp x10,0x293000 | `FALL_THROUGH`
<a id="insn-00adfd34"></a> `00adfd34` | `4a ed 1c 91` | add x10,x10,#0x73b | `FALL_THROUGH`
<a id="insn-00adfd38"></a> `00adfd38` | `e0 13 85 3c` | stur q0,[sp, #0x51] | `FALL_THROUGH`
<a id="insn-00adfd3c"></a> `00adfd3c` | `40 01 c0 3d` | ldr q0,[x10] | `FALL_THROUGH`
<a id="insn-00adfd40"></a> `00adfd40` | `e9 13 08 78` | sturh w9,[sp, #0x81] | `FALL_THROUGH`
<a id="insn-00adfd44"></a> `00adfd44` | `89 00 80 52` | mov w9,#0x4 | `FALL_THROUGH`
<a id="insn-00adfd48"></a> `00adfd48` | `e9 8b 00 b9` | str w9,[sp, #0x88] | `FALL_THROUGH`
<a id="insn-00adfd4c"></a> `00adfd4c` | `e9 bd ff b0` | adrp x9,0x29c000 | `FALL_THROUGH`
<a id="insn-00adfd50"></a> `00adfd50` | `29 b9 0d 91` | add x9,x9,#0x36e | `FALL_THROUGH`
<a id="insn-00adfd54"></a> `00adfd54` | `e0 13 87 3c` | stur q0,[sp, #0x71] | `FALL_THROUGH`
<a id="insn-00adfd58"></a> `00adfd58` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00adfd5c"></a> `00adfd5c` | `49 28 8a 52` | mov w9,#0x5142 | `FALL_THROUGH`
<a id="insn-00adfd60"></a> `00adfd60` | `89 92 09 78` | sturh w9,[x20, #0x99] | `FALL_THROUGH`
<a id="insn-00adfd64"></a> `00adfd64` | `a9 00 80 52` | mov w9,#0x5 | `FALL_THROUGH`
<a id="insn-00adfd68"></a> `00adfd68` | `e9 ab 00 b9` | str w9,[sp, #0xa8] | `FALL_THROUGH`
<a id="insn-00adfd6c"></a> `00adfd6c` | `89 bd ff d0` | adrp x9,0x291000 | `FALL_THROUGH`
<a id="insn-00adfd70"></a> `00adfd70` | `29 dd 21 91` | add x9,x9,#0x877 | `FALL_THROUGH`
<a id="insn-00adfd74"></a> `00adfd74` | `80 92 88 3c` | stur q0,[x20, #0x89] | `FALL_THROUGH`
<a id="insn-00adfd78"></a> `00adfd78` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00adfd7c"></a> `00adfd7c` | `49 e8 8e 52` | mov w9,#0x7742 | `FALL_THROUGH`
<a id="insn-00adfd80"></a> `00adfd80` | `89 92 0b 78` | sturh w9,[x20, #0xb9] | `FALL_THROUGH`
<a id="insn-00adfd84"></a> `00adfd84` | `c9 00 80 52` | mov w9,#0x6 | `FALL_THROUGH`
<a id="insn-00adfd88"></a> `00adfd88` | `e9 cb 00 b9` | str w9,[sp, #0xc8] | `FALL_THROUGH`
<a id="insn-00adfd8c"></a> `00adfd8c` | `a9 bd ff b0` | adrp x9,0x294000 | `FALL_THROUGH`
<a id="insn-00adfd90"></a> `00adfd90` | `29 cd 16 91` | add x9,x9,#0x5b3 | `FALL_THROUGH`
<a id="insn-00adfd94"></a> `00adfd94` | `80 92 8a 3c` | stur q0,[x20, #0xa9] | `FALL_THROUGH`
<a id="insn-00adfd98"></a> `00adfd98` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00adfd9c"></a> `00adfd9c` | `e8 43 00 39` | strb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00adfda0"></a> `00adfda0` | `e8 c3 00 39` | strb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00adfda4"></a> `00adfda4` | `e8 43 01 39` | strb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00adfda8"></a> `00adfda8` | `e8 c3 01 39` | strb w8,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00adfdac"></a> `00adfdac` | `e8 43 02 39` | strb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00adfdb0"></a> `00adfdb0` | `e8 c3 02 39` | strb w8,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00adfdb4"></a> `00adfdb4` | `e8 43 03 39` | strb w8,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-00adfdb8"></a> `00adfdb8` | `68 28 88 52` | mov w8,#0x4143 | `FALL_THROUGH`
<a id="insn-00adfdbc"></a> `00adfdbc` | `ff 0b 00 b9` | str wzr,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00adfdc0"></a> `00adfdc0` | `ff 8f 00 39` | strb wzr,[sp, #0x23] | `FALL_THROUGH`
<a id="insn-00adfdc4"></a> `00adfdc4` | `ff 0f 01 39` | strb wzr,[sp, #0x43] | `FALL_THROUGH`
<a id="insn-00adfdc8"></a> `00adfdc8` | `ff 8f 01 39` | strb wzr,[sp, #0x63] | `FALL_THROUGH`
<a id="insn-00adfdcc"></a> `00adfdcc` | `ff 0f 02 39` | strb wzr,[sp, #0x83] | `FALL_THROUGH`
<a id="insn-00adfdd0"></a> `00adfdd0` | `ff 8f 02 39` | strb wzr,[sp, #0xa3] | `FALL_THROUGH`
<a id="insn-00adfdd4"></a> `00adfdd4` | `ff 0f 03 39` | strb wzr,[sp, #0xc3] | `FALL_THROUGH`
<a id="insn-00adfdd8"></a> `00adfdd8` | `88 92 0d 78` | sturh w8,[x20, #0xd9] | `FALL_THROUGH`
<a id="insn-00adfddc"></a> `00adfddc` | `80 92 8c 3c` | stur q0,[x20, #0xc9] | `FALL_THROUGH`
<a id="insn-00adfde0"></a> `00adfde0` | `ff 8f 03 39` | strb wzr,[sp, #0xe3] | `FALL_THROUGH`
<a id="insn-00adfde4"></a> `00adfde4` | `7f 0a 00 f9` | str xzr,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00adfde8"></a> `00adfde8` | `3f 8c 00 f8` | str xzr,[x1, #0x8]! | `FALL_THROUGH`
<a id="insn-00adfdec"></a> `00adfdec` | `61 02 00 f9` | str x1,[x19] | `FALL_THROUGH`
<a id="insn-00adfdf0"></a> `00adfdf0` | `e2 23 00 91` | add x2,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00adfdf4"></a> `00adfdf4` | `e3 23 00 91` | add x3,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00adfdf8"></a> `00adfdf8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00adfdfc"></a> `00adfdfc` | `af e3 e4 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-00adfe00"></a> `00adfe00` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00adfe04"></a> `00adfe04` | `82 82 00 91` | add x2,x20,#0x20 | `FALL_THROUGH`
<a id="insn-00adfe08"></a> `00adfe08` | `83 82 00 91` | add x3,x20,#0x20 | `FALL_THROUGH`
<a id="insn-00adfe0c"></a> `00adfe0c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00adfe10"></a> `00adfe10` | `aa e3 e4 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-00adfe14"></a> `00adfe14` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00adfe18"></a> `00adfe18` | `82 02 01 91` | add x2,x20,#0x40 | `FALL_THROUGH`
<a id="insn-00adfe1c"></a> `00adfe1c` | `83 02 01 91` | add x3,x20,#0x40 | `FALL_THROUGH`
<a id="insn-00adfe20"></a> `00adfe20` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00adfe24"></a> `00adfe24` | `a5 e3 e4 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-00adfe28"></a> `00adfe28` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00adfe2c"></a> `00adfe2c` | `82 82 01 91` | add x2,x20,#0x60 | `FALL_THROUGH`
<a id="insn-00adfe30"></a> `00adfe30` | `83 82 01 91` | add x3,x20,#0x60 | `FALL_THROUGH`
<a id="insn-00adfe34"></a> `00adfe34` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00adfe38"></a> `00adfe38` | `a0 e3 e4 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-00adfe3c"></a> `00adfe3c` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00adfe40"></a> `00adfe40` | `82 02 02 91` | add x2,x20,#0x80 | `FALL_THROUGH`
<a id="insn-00adfe44"></a> `00adfe44` | `83 02 02 91` | add x3,x20,#0x80 | `FALL_THROUGH`
<a id="insn-00adfe48"></a> `00adfe48` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00adfe4c"></a> `00adfe4c` | `9b e3 e4 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-00adfe50"></a> `00adfe50` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00adfe54"></a> `00adfe54` | `82 82 02 91` | add x2,x20,#0xa0 | `FALL_THROUGH`
<a id="insn-00adfe58"></a> `00adfe58` | `83 82 02 91` | add x3,x20,#0xa0 | `FALL_THROUGH`
<a id="insn-00adfe5c"></a> `00adfe5c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00adfe60"></a> `00adfe60` | `96 e3 e4 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-00adfe64"></a> `00adfe64` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00adfe68"></a> `00adfe68` | `82 02 03 91` | add x2,x20,#0xc0 | `FALL_THROUGH`
<a id="insn-00adfe6c"></a> `00adfe6c` | `83 02 03 91` | add x3,x20,#0xc0 | `FALL_THROUGH`
<a id="insn-00adfe70"></a> `00adfe70` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00adfe74"></a> `00adfe74` | `91 e3 e4 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-00adfe78"></a> `00adfe78` | `e8 43 43 39` | ldrb w8,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-00adfe7c"></a> `00adfe7c` | `e8 03 00 37` | tbnz w8,#0x0,0x00adfef8 | `CONDITIONAL_JUMP`
<a id="insn-00adfe80"></a> `00adfe80` | `e8 c3 42 39` | ldrb w8,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00adfe84"></a> `00adfe84` | `28 04 00 37` | tbnz w8,#0x0,0x00adff08 | `CONDITIONAL_JUMP`
<a id="insn-00adfe88"></a> `00adfe88` | `e8 43 42 39` | ldrb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00adfe8c"></a> `00adfe8c` | `68 04 00 37` | tbnz w8,#0x0,0x00adff18 | `CONDITIONAL_JUMP`
<a id="insn-00adfe90"></a> `00adfe90` | `e8 c3 41 39` | ldrb w8,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00adfe94"></a> `00adfe94` | `a8 04 00 37` | tbnz w8,#0x0,0x00adff28 | `CONDITIONAL_JUMP`
<a id="insn-00adfe98"></a> `00adfe98` | `e8 43 41 39` | ldrb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00adfe9c"></a> `00adfe9c` | `e8 04 00 37` | tbnz w8,#0x0,0x00adff38 | `CONDITIONAL_JUMP`
<a id="insn-00adfea0"></a> `00adfea0` | `e8 c3 40 39` | ldrb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00adfea4"></a> `00adfea4` | `28 05 00 37` | tbnz w8,#0x0,0x00adff48 | `CONDITIONAL_JUMP`
<a id="insn-00adfea8"></a> `00adfea8` | `e8 43 40 39` | ldrb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00adfeac"></a> `00adfeac` | `68 00 00 36` | tbz w8,#0x0,0x00adfeb8 | `CONDITIONAL_JUMP`
<a id="insn-00adfeb0"></a> `00adfeb0` | `e0 13 40 f9` | ldr x0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00adfeb4"></a> `00adfeb4` | `57 ec 03 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00adfeb8"></a> `00adfeb8` | `c0 c9 ff b0` | adrp x0,0x418000 | `FALL_THROUGH`
<a id="insn-00adfebc"></a> `00adfebc` | `00 c0 0c 91` | add x0,x0,#0x330 | `FALL_THROUGH`
<a id="insn-00adfec0"></a> `00adfec0` | `01 2e 00 90` | adrp x1,0x109f000 | `FALL_THROUGH`
<a id="insn-00adfec4"></a> `00adfec4` | `21 c0 3f 91` | add x1,x1,#0xff0 | `FALL_THROUGH`
<a id="insn-00adfec8"></a> `00adfec8` | `22 08 00 d0` | adrp x2,0xbe5000 | `FALL_THROUGH`
<a id="insn-00adfecc"></a> `00adfecc` | `42 00 3e 91` | add x2,x2,#0xf80 | `FALL_THROUGH`
<a id="insn-00adfed0"></a> `00adfed0` | `30 ec 03 94` | bl 0x00bdaf90 | `UNCONDITIONAL_CALL`
<a id="insn-00adfed4"></a> `00adfed4` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00adfed8"></a> `00adfed8` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00adfedc"></a> `00adfedc` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00adfee0"></a> `00adfee0` | `41 0a 00 54` | b.ne 0x00ae0028 | `CONDITIONAL_JUMP`
<a id="insn-00adfee4"></a> `00adfee4` | `f4 4f 51 a9` | ldp x20,x19,[sp, #0x110] | `FALL_THROUGH`
<a id="insn-00adfee8"></a> `00adfee8` | `fc 57 50 a9` | ldp x28,x21,[sp, #0x100] | `FALL_THROUGH`
<a id="insn-00adfeec"></a> `00adfeec` | `fd 7b 4f a9` | ldp x29,x30,[sp, #0xf0] | `FALL_THROUGH`
<a id="insn-00adfef0"></a> `00adfef0` | `ff 83 04 91` | add sp,sp,#0x120 | `FALL_THROUGH`
<a id="insn-00adfef4"></a> `00adfef4` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00adfef8"></a> `00adfef8` | `e0 73 40 f9` | ldr x0,[sp, #0xe0] | `FALL_THROUGH`
<a id="insn-00adfefc"></a> `00adfefc` | `45 ec 03 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00adff00"></a> `00adff00` | `e8 c3 42 39` | ldrb w8,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00adff04"></a> `00adff04` | `28 fc 07 36` | tbz w8,#0x0,0x00adfe88 | `CONDITIONAL_JUMP`
<a id="insn-00adff08"></a> `00adff08` | `e0 63 40 f9` | ldr x0,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00adff0c"></a> `00adff0c` | `41 ec 03 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00adff10"></a> `00adff10` | `e8 43 42 39` | ldrb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00adff14"></a> `00adff14` | `e8 fb 07 36` | tbz w8,#0x0,0x00adfe90 | `CONDITIONAL_JUMP`
<a id="insn-00adff18"></a> `00adff18` | `e0 53 40 f9` | ldr x0,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00adff1c"></a> `00adff1c` | `3d ec 03 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00adff20"></a> `00adff20` | `e8 c3 41 39` | ldrb w8,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00adff24"></a> `00adff24` | `a8 fb 07 36` | tbz w8,#0x0,0x00adfe98 | `CONDITIONAL_JUMP`
<a id="insn-00adff28"></a> `00adff28` | `e0 43 40 f9` | ldr x0,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00adff2c"></a> `00adff2c` | `39 ec 03 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00adff30"></a> `00adff30` | `e8 43 41 39` | ldrb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00adff34"></a> `00adff34` | `68 fb 07 36` | tbz w8,#0x0,0x00adfea0 | `CONDITIONAL_JUMP`
<a id="insn-00adff38"></a> `00adff38` | `e0 33 40 f9` | ldr x0,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00adff3c"></a> `00adff3c` | `35 ec 03 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00adff40"></a> `00adff40` | `e8 c3 40 39` | ldrb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00adff44"></a> `00adff44` | `28 fb 07 36` | tbz w8,#0x0,0x00adfea8 | `CONDITIONAL_JUMP`
<a id="insn-00adff48"></a> `00adff48` | `e0 23 40 f9` | ldr x0,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00adff4c"></a> `00adff4c` | `31 ec 03 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00adff50"></a> `00adff50` | `e8 43 40 39` | ldrb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00adff54"></a> `00adff54` | `e8 fa 07 37` | tbnz w8,#0x0,0x00adfeb0 | `CONDITIONAL_JUMP`
<a id="insn-00adff58"></a> `00adff58` | `d8 ff ff 17` | b 0x00adfeb8 | `UNCONDITIONAL_JUMP`
<a id="insn-00ae0028"></a> `00ae0028` | `06 ec 03 94` | bl 0x00bdb040 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00adfc9c`](#insn-00adfc9c) 範囲 `[['00adfc9c', '00adfcdf']]`
  - `FALL_THROUGH` [`00adfcdc`](#insn-00adfcdc) → [`00adfce0`](#insn-00adfce0)
- ブロック [`00adfce0`](#insn-00adfce0) 範囲 `[['00adfce0', '00adfd77']]`
  - `FALL_THROUGH` [`00adfd74`](#insn-00adfd74) → [`00adfd78`](#insn-00adfd78)
- ブロック [`00adfd78`](#insn-00adfd78) 範囲 `[['00adfd78', '00adfd87']]`
  - `FALL_THROUGH` [`00adfd84`](#insn-00adfd84) → [`00adfd88`](#insn-00adfd88)
- ブロック [`00adfd88`](#insn-00adfd88) 範囲 `[['00adfd88', '00adfe5f']]`
  - `FALL_THROUGH` [`00adfe5c`](#insn-00adfe5c) → [`00adfe60`](#insn-00adfe60)
- ブロック [`00adfe60`](#insn-00adfe60) 範囲 `[['00adfe60', '00adfe7b']]`
  - `FALL_THROUGH` [`00adfe78`](#insn-00adfe78) → [`00adfe7c`](#insn-00adfe7c)
- ブロック [`00adfe7c`](#insn-00adfe7c) 範囲 `[['00adfe7c', '00adfe7f']]`
  - `CONDITIONAL_JUMP` [`00adfe7c`](#insn-00adfe7c) → [`00adfef8`](#insn-00adfef8)
  - `FALL_THROUGH` [`00adfe7c`](#insn-00adfe7c) → [`00adfe80`](#insn-00adfe80)
- ブロック [`00adfe80`](#insn-00adfe80) 範囲 `[['00adfe80', '00adfe87']]`
  - `CONDITIONAL_JUMP` [`00adfe84`](#insn-00adfe84) → [`00adff08`](#insn-00adff08)
  - `FALL_THROUGH` [`00adfe84`](#insn-00adfe84) → [`00adfe88`](#insn-00adfe88)
- ブロック [`00adfe88`](#insn-00adfe88) 範囲 `[['00adfe88', '00adfe8b']]`
  - `FALL_THROUGH` [`00adfe88`](#insn-00adfe88) → [`00adfe8c`](#insn-00adfe8c)
- ブロック [`00adfe8c`](#insn-00adfe8c) 範囲 `[['00adfe8c', '00adfe8f']]`
  - `CONDITIONAL_JUMP` [`00adfe8c`](#insn-00adfe8c) → [`00adff18`](#insn-00adff18)
  - `FALL_THROUGH` [`00adfe8c`](#insn-00adfe8c) → [`00adfe90`](#insn-00adfe90)
- ブロック [`00adfe90`](#insn-00adfe90) 範囲 `[['00adfe90', '00adfe97']]`
  - `CONDITIONAL_JUMP` [`00adfe94`](#insn-00adfe94) → [`00adff28`](#insn-00adff28)
  - `FALL_THROUGH` [`00adfe94`](#insn-00adfe94) → [`00adfe98`](#insn-00adfe98)
- ブロック [`00adfe98`](#insn-00adfe98) 範囲 `[['00adfe98', '00adfe9b']]`
  - `FALL_THROUGH` [`00adfe98`](#insn-00adfe98) → [`00adfe9c`](#insn-00adfe9c)
- ブロック [`00adfe9c`](#insn-00adfe9c) 範囲 `[['00adfe9c', '00adfe9f']]`
  - `CONDITIONAL_JUMP` [`00adfe9c`](#insn-00adfe9c) → [`00adff38`](#insn-00adff38)
  - `FALL_THROUGH` [`00adfe9c`](#insn-00adfe9c) → [`00adfea0`](#insn-00adfea0)
- ブロック [`00adfea0`](#insn-00adfea0) 範囲 `[['00adfea0', '00adfea7']]`
  - `CONDITIONAL_JUMP` [`00adfea4`](#insn-00adfea4) → [`00adff48`](#insn-00adff48)
  - `FALL_THROUGH` [`00adfea4`](#insn-00adfea4) → [`00adfea8`](#insn-00adfea8)
- ブロック [`00adfea8`](#insn-00adfea8) 範囲 `[['00adfea8', '00adfeaf']]`
  - `CONDITIONAL_JUMP` [`00adfeac`](#insn-00adfeac) → [`00adfeb8`](#insn-00adfeb8)
  - `FALL_THROUGH` [`00adfeac`](#insn-00adfeac) → [`00adfeb0`](#insn-00adfeb0)
- ブロック [`00adfeb0`](#insn-00adfeb0) 範囲 `[['00adfeb0', '00adfeb7']]`
  - `FALL_THROUGH` [`00adfeb4`](#insn-00adfeb4) → [`00adfeb8`](#insn-00adfeb8)
- ブロック [`00adfeb8`](#insn-00adfeb8) 範囲 `[['00adfeb8', '00adfee3']]`
  - `CONDITIONAL_JUMP` [`00adfee0`](#insn-00adfee0) → [`00ae0028`](#insn-00ae0028)
  - `FALL_THROUGH` [`00adfee0`](#insn-00adfee0) → [`00adfee4`](#insn-00adfee4)
- ブロック [`00adfee4`](#insn-00adfee4) 範囲 `[['00adfee4', '00adfef7']]`
- ブロック [`00adfef8`](#insn-00adfef8) 範囲 `[['00adfef8', '00adfefb']]`
  - `FALL_THROUGH` [`00adfef8`](#insn-00adfef8) → [`00adfefc`](#insn-00adfefc)
- ブロック [`00adfefc`](#insn-00adfefc) 範囲 `[['00adfefc', '00adff07']]`
  - `CONDITIONAL_JUMP` [`00adff04`](#insn-00adff04) → [`00adfe88`](#insn-00adfe88)
  - `FALL_THROUGH` [`00adff04`](#insn-00adff04) → [`00adff08`](#insn-00adff08)
- ブロック [`00adff08`](#insn-00adff08) 範囲 `[['00adff08', '00adff17']]`
  - `CONDITIONAL_JUMP` [`00adff14`](#insn-00adff14) → [`00adfe90`](#insn-00adfe90)
  - `FALL_THROUGH` [`00adff14`](#insn-00adff14) → [`00adff18`](#insn-00adff18)
- ブロック [`00adff18`](#insn-00adff18) 範囲 `[['00adff18', '00adff27']]`
  - `CONDITIONAL_JUMP` [`00adff24`](#insn-00adff24) → [`00adfe98`](#insn-00adfe98)
  - `FALL_THROUGH` [`00adff24`](#insn-00adff24) → [`00adff28`](#insn-00adff28)
- ブロック [`00adff28`](#insn-00adff28) 範囲 `[['00adff28', '00adff37']]`
  - `CONDITIONAL_JUMP` [`00adff34`](#insn-00adff34) → [`00adfea0`](#insn-00adfea0)
  - `FALL_THROUGH` [`00adff34`](#insn-00adff34) → [`00adff38`](#insn-00adff38)
- ブロック [`00adff38`](#insn-00adff38) 範囲 `[['00adff38', '00adff43']]`
  - `FALL_THROUGH` [`00adff40`](#insn-00adff40) → [`00adff44`](#insn-00adff44)
- ブロック [`00adff44`](#insn-00adff44) 範囲 `[['00adff44', '00adff47']]`
  - `CONDITIONAL_JUMP` [`00adff44`](#insn-00adff44) → [`00adfea8`](#insn-00adfea8)
  - `FALL_THROUGH` [`00adff44`](#insn-00adff44) → [`00adff48`](#insn-00adff48)
- ブロック [`00adff48`](#insn-00adff48) 範囲 `[['00adff48', '00adff57']]`
  - `CONDITIONAL_JUMP` [`00adff54`](#insn-00adff54) → [`00adfeb0`](#insn-00adfeb0)
  - `FALL_THROUGH` [`00adff54`](#insn-00adff54) → [`00adff58`](#insn-00adff58)
- ブロック [`00adff58`](#insn-00adff58) 範囲 `[['00adff58', '00adff5b']]`
  - `UNCONDITIONAL_JUMP` [`00adff58`](#insn-00adff58) → [`00adfeb8`](#insn-00adfeb8)
- ブロック [`00ae0028`](#insn-00ae0028) 範囲 `[['00ae0028', '00ae002b']]`

## 命令位置別の参照

- [`00adfca0`](#insn-00adfca0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfca4`](#insn-00adfca4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfca8`](#insn-00adfca8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfccc`](#insn-00adfccc) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfcd8`](#insn-00adfcd8) → `002a72dd`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00adfce0`](#insn-00adfce0) → `Stack[-0xff]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfce4`](#insn-00adfce4) → `Stack[-0xf8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfcf4`](#insn-00adfcf4) → `Stack[-0x10f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfcfc`](#insn-00adfcfc) → `002a72f0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00adfd00`](#insn-00adfd00) → `Stack[-0xdf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfd08`](#insn-00adfd08) → `Stack[-0xd8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfd18`](#insn-00adfd18) → `Stack[-0xef]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfd1c`](#insn-00adfd1c) → `002a8046`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00adfd20`](#insn-00adfd20) → `Stack[-0xbf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfd28`](#insn-00adfd28) → `Stack[-0xb8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfd38`](#insn-00adfd38) → `Stack[-0xcf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfd3c`](#insn-00adfd3c) → `0029373b`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00adfd40`](#insn-00adfd40) → `Stack[-0x9f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfd48`](#insn-00adfd48) → `Stack[-0x98]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfd54`](#insn-00adfd54) → `Stack[-0xaf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfd58`](#insn-00adfd58) → `0029c36e`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00adfd60`](#insn-00adfd60) → `Stack[-0x7f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfd68`](#insn-00adfd68) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfd74`](#insn-00adfd74) → `Stack[-0x8f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfd78`](#insn-00adfd78) → `00291877`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00adfd80`](#insn-00adfd80) → `Stack[-0x5f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfd88`](#insn-00adfd88) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfd94`](#insn-00adfd94) → `Stack[-0x6f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfd98`](#insn-00adfd98) → `002945b3`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00adfd9c`](#insn-00adfd9c) → `Stack[-0x110]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfda0`](#insn-00adfda0) → `Stack[-0xf0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfda4`](#insn-00adfda4) → `Stack[-0xd0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfda8`](#insn-00adfda8) → `Stack[-0xb0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfdac`](#insn-00adfdac) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfdb0`](#insn-00adfdb0) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfdb4`](#insn-00adfdb4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfdbc`](#insn-00adfdbc) → `Stack[-0x118]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfdc0`](#insn-00adfdc0) → `Stack[-0xfd]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfdc4`](#insn-00adfdc4) → `Stack[-0xdd]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfdc8`](#insn-00adfdc8) → `Stack[-0xbd]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfdcc`](#insn-00adfdcc) → `Stack[-0x9d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfdd0`](#insn-00adfdd0) → `Stack[-0x7d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfdd4`](#insn-00adfdd4) → `Stack[-0x5d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfdd8`](#insn-00adfdd8) → `Stack[-0x3f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfddc`](#insn-00adfddc) → `Stack[-0x4f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfde0`](#insn-00adfde0) → `Stack[-0x3d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfde4`](#insn-00adfde4) → `010a0000`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adfde8`](#insn-00adfde8) → `0109fff8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adfdec`](#insn-00adfdec) → `0109fff0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adfdec`](#insn-00adfdec) → `0109fff8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adfdf8`](#insn-00adfdf8) → `0109fff0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adfdfc`](#insn-00adfdfc) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`00adfe00`](#insn-00adfe00) → `0109fff8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adfe0c`](#insn-00adfe0c) → `0109fff0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adfe10`](#insn-00adfe10) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`00adfe14`](#insn-00adfe14) → `0109fff8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adfe20`](#insn-00adfe20) → `0109fff0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adfe24`](#insn-00adfe24) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`00adfe28`](#insn-00adfe28) → `0109fff8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adfe34`](#insn-00adfe34) → `0109fff0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adfe38`](#insn-00adfe38) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`00adfe3c`](#insn-00adfe3c) → `0109fff8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adfe48`](#insn-00adfe48) → `0109fff0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adfe4c`](#insn-00adfe4c) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`00adfe50`](#insn-00adfe50) → `0109fff8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adfe5c`](#insn-00adfe5c) → `0109fff0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adfe60`](#insn-00adfe60) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`00adfe64`](#insn-00adfe64) → `0109fff8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adfe70`](#insn-00adfe70) → `0109fff0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adfe74`](#insn-00adfe74) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`00adfe78`](#insn-00adfe78) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfe7c`](#insn-00adfe7c) → [`00adfef8`](#insn-00adfef8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfe80`](#insn-00adfe80) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfe84`](#insn-00adfe84) → [`00adff08`](#insn-00adff08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfe88`](#insn-00adfe88) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfe8c`](#insn-00adfe8c) → [`00adff18`](#insn-00adff18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfe90`](#insn-00adfe90) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfe94`](#insn-00adfe94) → [`00adff28`](#insn-00adff28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfe98`](#insn-00adfe98) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfe9c`](#insn-00adfe9c) → [`00adff38`](#insn-00adff38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfea0`](#insn-00adfea0) → `Stack[-0xf0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfea4`](#insn-00adfea4) → [`00adff48`](#insn-00adff48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfea8`](#insn-00adfea8) → `Stack[-0x110]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfeac`](#insn-00adfeac) → [`00adfeb8`](#insn-00adfeb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfeb0`](#insn-00adfeb0) → `Stack[-0x100]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfeb4`](#insn-00adfeb4) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00adfebc`](#insn-00adfebc) → [`00418330`](../00418/00418330.md) · `PARAM` · `ANALYSIS` · 関数 `00418330` · 推定シンボル `None` · 推定型 `None`
- [`00adfec4`](#insn-00adfec4) → `0109fff0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adfecc`](#insn-00adfecc) → `00be5f80`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00adfed0`](#insn-00adfed0) → [`00bdaf90`](../00bda/00bdaf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf90` · 推定シンボル `None` · 推定型 `None`
- [`00adfed8`](#insn-00adfed8) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfee0`](#insn-00adfee0) → [`00ae0028`](#insn-00ae0028) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfee4`](#insn-00adfee4) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfee8`](#insn-00adfee8) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfeec`](#insn-00adfeec) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfef8`](#insn-00adfef8) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfefc`](#insn-00adfefc) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00adff00`](#insn-00adff00) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adff04`](#insn-00adff04) → [`00adfe88`](#insn-00adfe88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adff08`](#insn-00adff08) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adff0c`](#insn-00adff0c) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00adff10`](#insn-00adff10) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adff14`](#insn-00adff14) → [`00adfe90`](#insn-00adfe90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adff18`](#insn-00adff18) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adff1c`](#insn-00adff1c) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00adff20`](#insn-00adff20) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adff24`](#insn-00adff24) → [`00adfe98`](#insn-00adfe98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adff28`](#insn-00adff28) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adff2c`](#insn-00adff2c) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00adff30`](#insn-00adff30) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adff34`](#insn-00adff34) → [`00adfea0`](#insn-00adfea0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adff38`](#insn-00adff38) → `Stack[-0xc0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adff3c`](#insn-00adff3c) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00adff40`](#insn-00adff40) → `Stack[-0xf0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adff44`](#insn-00adff44) → [`00adfea8`](#insn-00adfea8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adff48`](#insn-00adff48) → `Stack[-0xe0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adff4c`](#insn-00adff4c) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00adff50`](#insn-00adff50) → `Stack[-0x110]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adff54`](#insn-00adff54) → [`00adfeb0`](#insn-00adfeb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adff58`](#insn-00adff58) → [`00adfeb8`](#insn-00adfeb8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae0028`](#insn-00ae0028) → [`00bdb040`](../00bdb/00bdb040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb040` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00adfca0`](#insn-00adfca0)

~~~json
{
  "source": "00adfca0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfca4`](#insn-00adfca4)

~~~json
{
  "source": "00adfca4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfca8`](#insn-00adfca8)

~~~json
{
  "source": "00adfca8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfccc`](#insn-00adfccc)

~~~json
{
  "source": "00adfccc",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfcd8`](#insn-00adfcd8)

~~~json
{
  "source": "00adfcd8",
  "target": "002a72dd",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a72dd",
  "offset": 0,
  "size": 19,
  "datatype": "string",
  "bytes": "43676b496a4d33795f5a516145414951416700",
  "capture_start": "002a72dd",
  "capture_bytes": 19,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00adfce0`](#insn-00adfce0)

~~~json
{
  "source": "00adfce0",
  "target": "Stack[-0xff]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfce4`](#insn-00adfce4)

~~~json
{
  "source": "00adfce4",
  "target": "Stack[-0xf8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfcf4`](#insn-00adfcf4)

~~~json
{
  "source": "00adfcf4",
  "target": "Stack[-0x10f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfcfc`](#insn-00adfcfc)

~~~json
{
  "source": "00adfcfc",
  "target": "002a72f0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a72f0",
  "offset": 0,
  "size": 19,
  "datatype": "string",
  "bytes": "43676b496a4d33795f5a516145414951424100",
  "capture_start": "002a72f0",
  "capture_bytes": 19,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00adfd00`](#insn-00adfd00)

~~~json
{
  "source": "00adfd00",
  "target": "Stack[-0xdf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfd08`](#insn-00adfd08)

~~~json
{
  "source": "00adfd08",
  "target": "Stack[-0xd8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfd18`](#insn-00adfd18)

~~~json
{
  "source": "00adfd18",
  "target": "Stack[-0xef]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfd1c`](#insn-00adfd1c)

~~~json
{
  "source": "00adfd1c",
  "target": "002a8046",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a8046",
  "offset": 0,
  "size": 19,
  "datatype": "string",
  "bytes": "43676b496a4d33795f5a516145414951426700",
  "capture_start": "002a8046",
  "capture_bytes": 19,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00adfd20`](#insn-00adfd20)

~~~json
{
  "source": "00adfd20",
  "target": "Stack[-0xbf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfd28`](#insn-00adfd28)

~~~json
{
  "source": "00adfd28",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfd38`](#insn-00adfd38)

~~~json
{
  "source": "00adfd38",
  "target": "Stack[-0xcf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfd3c`](#insn-00adfd3c)

~~~json
{
  "source": "00adfd3c",
  "target": "0029373b",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029373b",
  "offset": 0,
  "size": 19,
  "datatype": "string",
  "bytes": "43676b496a4d33795f5a516145414951417700",
  "capture_start": "0029373b",
  "capture_bytes": 19,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00adfd40`](#insn-00adfd40)

~~~json
{
  "source": "00adfd40",
  "target": "Stack[-0x9f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfd48`](#insn-00adfd48)

~~~json
{
  "source": "00adfd48",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfd54`](#insn-00adfd54)

~~~json
{
  "source": "00adfd54",
  "target": "Stack[-0xaf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfd58`](#insn-00adfd58)

~~~json
{
  "source": "00adfd58",
  "target": "0029c36e",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029c36e",
  "offset": 0,
  "size": 19,
  "datatype": "string",
  "bytes": "43676b496a4d33795f5a516145414951425100",
  "capture_start": "0029c36e",
  "capture_bytes": 19,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00adfd60`](#insn-00adfd60)

~~~json
{
  "source": "00adfd60",
  "target": "Stack[-0x7f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfd68`](#insn-00adfd68)

~~~json
{
  "source": "00adfd68",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfd74`](#insn-00adfd74)

~~~json
{
  "source": "00adfd74",
  "target": "Stack[-0x8f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfd78`](#insn-00adfd78)

~~~json
{
  "source": "00adfd78",
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
- 参照命令 [`00adfd80`](#insn-00adfd80)

~~~json
{
  "source": "00adfd80",
  "target": "Stack[-0x5f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfd88`](#insn-00adfd88)

~~~json
{
  "source": "00adfd88",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfd94`](#insn-00adfd94)

~~~json
{
  "source": "00adfd94",
  "target": "Stack[-0x6f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfd98`](#insn-00adfd98)

~~~json
{
  "source": "00adfd98",
  "target": "002945b3",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002945b3",
  "offset": 0,
  "size": 19,
  "datatype": "string",
  "bytes": "43676b496a4d33795f5a516145414951434100",
  "capture_start": "002945b3",
  "capture_bytes": 19,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00adfd9c`](#insn-00adfd9c)

~~~json
{
  "source": "00adfd9c",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfda0`](#insn-00adfda0)

~~~json
{
  "source": "00adfda0",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfda4`](#insn-00adfda4)

~~~json
{
  "source": "00adfda4",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfda8`](#insn-00adfda8)

~~~json
{
  "source": "00adfda8",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfdac`](#insn-00adfdac)

~~~json
{
  "source": "00adfdac",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfdb0`](#insn-00adfdb0)

~~~json
{
  "source": "00adfdb0",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfdb4`](#insn-00adfdb4)

~~~json
{
  "source": "00adfdb4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfdbc`](#insn-00adfdbc)

~~~json
{
  "source": "00adfdbc",
  "target": "Stack[-0x118]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfdc0`](#insn-00adfdc0)

~~~json
{
  "source": "00adfdc0",
  "target": "Stack[-0xfd]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfdc4`](#insn-00adfdc4)

~~~json
{
  "source": "00adfdc4",
  "target": "Stack[-0xdd]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfdc8`](#insn-00adfdc8)

~~~json
{
  "source": "00adfdc8",
  "target": "Stack[-0xbd]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfdcc`](#insn-00adfdcc)

~~~json
{
  "source": "00adfdcc",
  "target": "Stack[-0x9d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfdd0`](#insn-00adfdd0)

~~~json
{
  "source": "00adfdd0",
  "target": "Stack[-0x7d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfdd4`](#insn-00adfdd4)

~~~json
{
  "source": "00adfdd4",
  "target": "Stack[-0x5d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfdd8`](#insn-00adfdd8)

~~~json
{
  "source": "00adfdd8",
  "target": "Stack[-0x3f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfddc`](#insn-00adfddc)

~~~json
{
  "source": "00adfddc",
  "target": "Stack[-0x4f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfde0`](#insn-00adfde0)

~~~json
{
  "source": "00adfde0",
  "target": "Stack[-0x3d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfde4`](#insn-00adfde4)

~~~json
{
  "source": "00adfde4",
  "target": "010a0000",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0000",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adfde8`](#insn-00adfde8)

~~~json
{
  "source": "00adfde8",
  "target": "0109fff8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fff8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adfdec`](#insn-00adfdec)

~~~json
{
  "source": "00adfdec",
  "target": "0109fff0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fff0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adfdec`](#insn-00adfdec)

~~~json
{
  "source": "00adfdec",
  "target": "0109fff8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fff8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adfdf8`](#insn-00adfdf8)

~~~json
{
  "source": "00adfdf8",
  "target": "0109fff0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fff0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adfdfc`](#insn-00adfdfc)

~~~json
{
  "source": "00adfdfc",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adfe00`](#insn-00adfe00)

~~~json
{
  "source": "00adfe00",
  "target": "0109fff8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fff8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adfe0c`](#insn-00adfe0c)

~~~json
{
  "source": "00adfe0c",
  "target": "0109fff0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fff0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adfe10`](#insn-00adfe10)

~~~json
{
  "source": "00adfe10",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adfe14`](#insn-00adfe14)

~~~json
{
  "source": "00adfe14",
  "target": "0109fff8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fff8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adfe20`](#insn-00adfe20)

~~~json
{
  "source": "00adfe20",
  "target": "0109fff0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fff0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adfe24`](#insn-00adfe24)

~~~json
{
  "source": "00adfe24",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adfe28`](#insn-00adfe28)

~~~json
{
  "source": "00adfe28",
  "target": "0109fff8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fff8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adfe34`](#insn-00adfe34)

~~~json
{
  "source": "00adfe34",
  "target": "0109fff0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fff0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adfe38`](#insn-00adfe38)

~~~json
{
  "source": "00adfe38",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adfe3c`](#insn-00adfe3c)

~~~json
{
  "source": "00adfe3c",
  "target": "0109fff8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fff8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adfe48`](#insn-00adfe48)

~~~json
{
  "source": "00adfe48",
  "target": "0109fff0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fff0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adfe4c`](#insn-00adfe4c)

~~~json
{
  "source": "00adfe4c",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adfe50`](#insn-00adfe50)

~~~json
{
  "source": "00adfe50",
  "target": "0109fff8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fff8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adfe5c`](#insn-00adfe5c)

~~~json
{
  "source": "00adfe5c",
  "target": "0109fff0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fff0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adfe60`](#insn-00adfe60)

~~~json
{
  "source": "00adfe60",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adfe64`](#insn-00adfe64)

~~~json
{
  "source": "00adfe64",
  "target": "0109fff8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fff8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adfe70`](#insn-00adfe70)

~~~json
{
  "source": "00adfe70",
  "target": "0109fff0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fff0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adfe74`](#insn-00adfe74)

~~~json
{
  "source": "00adfe74",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adfe78`](#insn-00adfe78)

~~~json
{
  "source": "00adfe78",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfe7c`](#insn-00adfe7c)

~~~json
{
  "source": "00adfe7c",
  "target": "00adfef8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfe80`](#insn-00adfe80)

~~~json
{
  "source": "00adfe80",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfe84`](#insn-00adfe84)

~~~json
{
  "source": "00adfe84",
  "target": "00adff08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfe88`](#insn-00adfe88)

~~~json
{
  "source": "00adfe88",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfe8c`](#insn-00adfe8c)

~~~json
{
  "source": "00adfe8c",
  "target": "00adff18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfe90`](#insn-00adfe90)

~~~json
{
  "source": "00adfe90",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfe94`](#insn-00adfe94)

~~~json
{
  "source": "00adfe94",
  "target": "00adff28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfe98`](#insn-00adfe98)

~~~json
{
  "source": "00adfe98",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfe9c`](#insn-00adfe9c)

~~~json
{
  "source": "00adfe9c",
  "target": "00adff38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfea0`](#insn-00adfea0)

~~~json
{
  "source": "00adfea0",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfea4`](#insn-00adfea4)

~~~json
{
  "source": "00adfea4",
  "target": "00adff48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfea8`](#insn-00adfea8)

~~~json
{
  "source": "00adfea8",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfeac`](#insn-00adfeac)

~~~json
{
  "source": "00adfeac",
  "target": "00adfeb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfeb0`](#insn-00adfeb0)

~~~json
{
  "source": "00adfeb0",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfeb4`](#insn-00adfeb4)

~~~json
{
  "source": "00adfeb4",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adfebc`](#insn-00adfebc)

~~~json
{
  "source": "00adfebc",
  "target": "00418330",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adfec4`](#insn-00adfec4)

~~~json
{
  "source": "00adfec4",
  "target": "0109fff0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fff0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adfecc`](#insn-00adfecc)

~~~json
{
  "source": "00adfecc",
  "target": "00be5f80",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00be5f80",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00adfed0`](#insn-00adfed0)

~~~json
{
  "source": "00adfed0",
  "target": "00bdaf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adfed8`](#insn-00adfed8)

~~~json
{
  "source": "00adfed8",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfee0`](#insn-00adfee0)

~~~json
{
  "source": "00adfee0",
  "target": "00ae0028",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfee4`](#insn-00adfee4)

~~~json
{
  "source": "00adfee4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfee8`](#insn-00adfee8)

~~~json
{
  "source": "00adfee8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfeec`](#insn-00adfeec)

~~~json
{
  "source": "00adfeec",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfef8`](#insn-00adfef8)

~~~json
{
  "source": "00adfef8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfefc`](#insn-00adfefc)

~~~json
{
  "source": "00adfefc",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adff00`](#insn-00adff00)

~~~json
{
  "source": "00adff00",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adff04`](#insn-00adff04)

~~~json
{
  "source": "00adff04",
  "target": "00adfe88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adff08`](#insn-00adff08)

~~~json
{
  "source": "00adff08",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adff0c`](#insn-00adff0c)

~~~json
{
  "source": "00adff0c",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adff10`](#insn-00adff10)

~~~json
{
  "source": "00adff10",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adff14`](#insn-00adff14)

~~~json
{
  "source": "00adff14",
  "target": "00adfe90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adff18`](#insn-00adff18)

~~~json
{
  "source": "00adff18",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adff1c`](#insn-00adff1c)

~~~json
{
  "source": "00adff1c",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adff20`](#insn-00adff20)

~~~json
{
  "source": "00adff20",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adff24`](#insn-00adff24)

~~~json
{
  "source": "00adff24",
  "target": "00adfe98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adff28`](#insn-00adff28)

~~~json
{
  "source": "00adff28",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adff2c`](#insn-00adff2c)

~~~json
{
  "source": "00adff2c",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adff30`](#insn-00adff30)

~~~json
{
  "source": "00adff30",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adff34`](#insn-00adff34)

~~~json
{
  "source": "00adff34",
  "target": "00adfea0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adff38`](#insn-00adff38)

~~~json
{
  "source": "00adff38",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adff3c`](#insn-00adff3c)

~~~json
{
  "source": "00adff3c",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adff40`](#insn-00adff40)

~~~json
{
  "source": "00adff40",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adff44`](#insn-00adff44)

~~~json
{
  "source": "00adff44",
  "target": "00adfea8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adff48`](#insn-00adff48)

~~~json
{
  "source": "00adff48",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adff4c`](#insn-00adff4c)

~~~json
{
  "source": "00adff4c",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adff50`](#insn-00adff50)

~~~json
{
  "source": "00adff50",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adff54`](#insn-00adff54)

~~~json
{
  "source": "00adff54",
  "target": "00adfeb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adff58`](#insn-00adff58)

~~~json
{
  "source": "00adff58",
  "target": "00adfeb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae0028`](#insn-00ae0028)

~~~json
{
  "source": "00ae0028",
  "target": "00bdb040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
