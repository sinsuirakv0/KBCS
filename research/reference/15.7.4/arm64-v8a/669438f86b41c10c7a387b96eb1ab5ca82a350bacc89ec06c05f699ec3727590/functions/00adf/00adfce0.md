# 00adfce0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00adfc9c`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adf/00adfc9c.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0060.md#compare-2ccf8c57a8f54f4114aa86bcce16a9b4)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b3f6b8`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3f6b8.md) · 移動量 `+0x5f9d8`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0055.md#compare-8ad6dc34d5ff4f1c106f08504810c122)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00adfce0",
  "name": "_INIT_268",
  "size": 708,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e962fddbe6e909bcd5a6afd5a9581e3dbc40106c51d3189828b05be9c49b6ebb",
  "source_text_sha256": "e962fddbe6e909bcd5a6afd5a9581e3dbc40106c51d3189828b05be9c49b6ebb",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00adfce0",
        "00adff9f"
      ],
      [
        "00ae006c",
        "00ae006f"
      ]
    ],
    "bytes_sha256": "4b6c8881db41e520185040cdbbfb031be0091424b4d4c0355ad576219a6c3691",
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
- [00bdafe0](../00bda/00bdafe0.md)
- [00bdb060](../00bdb/00bdb060.md)
- [00bdb090](../00bdb/00bdb090.md)

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
                    /* try { // try from 00adfd24 to 00bdfdbb has its CatchHandler @ 00adfd24
                       catch() { ... } // from try @ 00adfd24 with catch @ 00adfd24
                       catch() { ... } // from try @ 00adfdcc with catch @ 00adfd24
                       catch() { ... } // from try @ 00adff88 with catch @ 00adfd24
                       catch() { ... } // from try @ 00ae0378 with catch @ 00adfd24
                       catch() { ... } // from try @ 00ae0454 with catch @ 00adfd24 */
  uStack_ff = 0x6741;
  local_f8[0] = 1;
  uStack_107 = (undefined7)s_CgkIjM3y_ZQaEAIQAg_002a7377._8_8_;
  cStack_100 = SUB81(s_CgkIjM3y_ZQaEAIQAg_002a7377._8_8_,7);
  local_10f = (char  [8])s_CgkIjM3y_ZQaEAIQAg_002a7377._0_8_;
  uStack_df = 0x4142;
  local_d8[0] = 2;
  uStack_e7 = (undefined7)s_CgkIjM3y_ZQaEAIQBA_002a738a._8_8_;
  cStack_e0 = SUB81(s_CgkIjM3y_ZQaEAIQBA_002a738a._8_8_,7);
  local_ef = (char  [8])s_CgkIjM3y_ZQaEAIQBA_002a738a._0_8_;
  uStack_bf = 0x6742;
  local_b8[0] = 3;
  uStack_c7 = (undefined7)s_CgkIjM3y_ZQaEAIQBg_002a80e0._8_8_;
  cStack_c0 = SUB81(s_CgkIjM3y_ZQaEAIQBg_002a80e0._8_8_,7);
  local_cf = (char  [8])s_CgkIjM3y_ZQaEAIQBg_002a80e0._0_8_;
  uStack_9f = 0x7741;
  local_98[0] = 4;
  uStack_a7 = (undefined7)s_CgkIjM3y_ZQaEAIQAw_002936ae._8_8_;
  cStack_a0 = SUB81(s_CgkIjM3y_ZQaEAIQAw_002936ae._8_8_,7);
  local_af = (char  [8])s_CgkIjM3y_ZQaEAIQAw_002936ae._0_8_;
  uStack_7f = 0x5142;
  local_78[0] = 5;
  uStack_87 = (undefined7)s_CgkIjM3y_ZQaEAIQBQ_0029c36c._8_8_;
  cStack_80 = SUB81(s_CgkIjM3y_ZQaEAIQBQ_0029c36c._8_8_,7);
  local_8f = (char  [8])s_CgkIjM3y_ZQaEAIQBQ_0029c36c._0_8_;
                    /* try { // try from 00adfdbc to 00bdfdcb has its CatchHandler @ 00ae0860 */
  uStack_5f = 0x7742;
                    /* try { // try from 00adfdcc to 00bdfea3 has its CatchHandler @ 00adfd24 */
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
  uStack_47 = (undefined7)s_CgkIjM3y_ZQaEAIQCA_00294526._8_8_;
  cStack_40 = SUB81(s_CgkIjM3y_ZQaEAIQCA_00294526._8_8_,7);
  local_4f = (char  [8])s_CgkIjM3y_ZQaEAIQCA_00294526._0_8_;
  uStack_3d = 0;
  DAT_010a0040 = 0;
  DAT_010a0038 = 0;
  DAT_010a0030 = &DAT_010a0038;
  FUN_00418cb8(&DAT_010a0030,&DAT_010a0038,local_118,local_118);
  FUN_00418cb8(&DAT_010a0030,&DAT_010a0038,local_f8,local_f8);
  FUN_00418cb8(&DAT_010a0030,&DAT_010a0038,local_d8,local_d8);
  FUN_00418cb8(&DAT_010a0030,&DAT_010a0038,local_b8,local_b8);
  FUN_00418cb8(&DAT_010a0030,&DAT_010a0038,local_98,local_98);
                    /* try { // try from 00adfea4 to 00bdfeaf has its CatchHandler @ 00ae08d0 */
  FUN_00418cb8(&DAT_010a0030,&DAT_010a0038,local_78,local_78);
  FUN_00418cb8(&DAT_010a0030,&DAT_010a0038,local_58,local_58);
                    /* try { // try from 00adfec0 to 00bdfecf has its CatchHandler @ 00ae06fc */
  if ((local_50 & 1) != 0) {
                    /* try { // try from 00adff40 to 00bdff53 has its CatchHandler @ 00ae08d0 */
    _ZdlPv((void *)CONCAT44(uStack_3c,CONCAT13(uStack_3d,CONCAT21(uStack_3f,cStack_40))));
  }
  if ((local_70 & 1) != 0) {
    _ZdlPv((void *)CONCAT44(uStack_5c,CONCAT13(uStack_5d,CONCAT21(uStack_5f,cStack_60))));
  }
                    /* try { // try from 00adfed0 to 00bdfedb has its CatchHandler @ 00ae06e0 */
  if ((local_90 & 1) != 0) {
    _ZdlPv((void *)CONCAT44(uStack_7c,CONCAT13(uStack_7d,CONCAT21(uStack_7f,cStack_80))));
  }
  if ((local_b0 & 1) != 0) {
                    /* try { // try from 00adff6c to 00bdff87 has its CatchHandler @ 00ae0810 */
    _ZdlPv((void *)CONCAT44(uStack_9c,CONCAT13(uStack_9d,CONCAT21(uStack_9f,cStack_a0))));
  }
                    /* try { // try from 00adfee0 to 00bdfee7 has its CatchHandler @ 00ae06c4 */
  if ((local_d0 & 1) != 0) {
    _ZdlPv((void *)CONCAT44(uStack_bc,CONCAT13(uStack_bd,CONCAT21(uStack_bf,cStack_c0))));
  }
                    /* try { // try from 00adff88 to 00be00f3 has its CatchHandler @ 00adfd24 */
  if ((local_f0 & 1) != 0) {
    _ZdlPv((void *)CONCAT44(uStack_dc,CONCAT13(uStack_dd,CONCAT21(uStack_df,cStack_e0))));
  }
  if ((local_110 & 1) != 0) {
    _ZdlPv((void *)CONCAT44(uStack_fc,CONCAT13(uStack_fd,CONCAT21(uStack_ff,cStack_100))));
  }
  __cxa_atexit(FUN_00418330,&DAT_010a0030,&PTR_LOOP_00be5fd0);
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
<a id="insn-00adfce0"></a> `00adfce0` | `ff 83 04 d1` | sub sp,sp,#0x120 | `FALL_THROUGH`
<a id="insn-00adfce4"></a> `00adfce4` | `fd 7b 0f a9` | stp x29,x30,[sp, #0xf0] | `FALL_THROUGH`
<a id="insn-00adfce8"></a> `00adfce8` | `fc 57 10 a9` | stp x28,x21,[sp, #0x100] | `FALL_THROUGH`
<a id="insn-00adfcec"></a> `00adfcec` | `f4 4f 11 a9` | stp x20,x19,[sp, #0x110] | `FALL_THROUGH`
<a id="insn-00adfcf0"></a> `00adfcf0` | `fd c3 03 91` | add x29,sp,#0xf0 | `FALL_THROUGH`
<a id="insn-00adfcf4"></a> `00adfcf4` | `55 d0 3b d5` | mrs x21,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00adfcf8"></a> `00adfcf8` | `2a e8 8c 52` | mov w10,#0x6741 | `FALL_THROUGH`
<a id="insn-00adfcfc"></a> `00adfcfc` | `f4 23 00 91` | add x20,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00adfd00"></a> `00adfd00` | `a9 16 40 f9` | ldr x9,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00adfd04"></a> `00adfd04` | `88 04 80 52` | mov w8,#0x24 | `FALL_THROUGH`
<a id="insn-00adfd08"></a> `00adfd08` | `13 2e 00 b0` | adrp x19,0x10a0000 | `FALL_THROUGH`
<a id="insn-00adfd0c"></a> `00adfd0c` | `73 c2 00 91` | add x19,x19,#0x30 | `FALL_THROUGH`
<a id="insn-00adfd10"></a> `00adfd10` | `a9 83 1f f8` | stur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00adfd14"></a> `00adfd14` | `49 be ff 90` | adrp x9,0x2a7000 | `FALL_THROUGH`
<a id="insn-00adfd18"></a> `00adfd18` | `29 dd 0d 91` | add x9,x9,#0x377 | `FALL_THROUGH`
<a id="insn-00adfd1c"></a> `00adfd1c` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00adfd20"></a> `00adfd20` | `29 00 80 52` | mov w9,#0x1 | `FALL_THROUGH`
<a id="insn-00adfd24"></a> `00adfd24` | `ea 13 02 78` | sturh w10,[sp, #0x21] | `FALL_THROUGH`
<a id="insn-00adfd28"></a> `00adfd28` | `e9 2b 00 b9` | str w9,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00adfd2c"></a> `00adfd2c` | `49 28 88 52` | mov w9,#0x4142 | `FALL_THROUGH`
<a id="insn-00adfd30"></a> `00adfd30` | `4a be ff 90` | adrp x10,0x2a7000 | `FALL_THROUGH`
<a id="insn-00adfd34"></a> `00adfd34` | `4a 29 0e 91` | add x10,x10,#0x38a | `FALL_THROUGH`
<a id="insn-00adfd38"></a> `00adfd38` | `e0 13 81 3c` | stur q0,[sp, #0x11] | `FALL_THROUGH`
<a id="insn-00adfd3c"></a> `00adfd3c` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00adfd40"></a> `00adfd40` | `40 01 c0 3d` | ldr q0,[x10] | `FALL_THROUGH`
<a id="insn-00adfd44"></a> `00adfd44` | `e9 13 04 78` | sturh w9,[sp, #0x41] | `FALL_THROUGH`
<a id="insn-00adfd48"></a> `00adfd48` | `49 00 80 52` | mov w9,#0x2 | `FALL_THROUGH`
<a id="insn-00adfd4c"></a> `00adfd4c` | `e9 4b 00 b9` | str w9,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00adfd50"></a> `00adfd50` | `49 e8 8c 52` | mov w9,#0x6742 | `FALL_THROUGH`
<a id="insn-00adfd54"></a> `00adfd54` | `4a be ff b0` | adrp x10,0x2a8000 | `FALL_THROUGH`
<a id="insn-00adfd58"></a> `00adfd58` | `4a 81 03 91` | add x10,x10,#0xe0 | `FALL_THROUGH`
<a id="insn-00adfd5c"></a> `00adfd5c` | `e0 13 83 3c` | stur q0,[sp, #0x31] | `FALL_THROUGH`
<a id="insn-00adfd60"></a> `00adfd60` | `40 01 c0 3d` | ldr q0,[x10] | `FALL_THROUGH`
<a id="insn-00adfd64"></a> `00adfd64` | `e9 13 06 78` | sturh w9,[sp, #0x61] | `FALL_THROUGH`
<a id="insn-00adfd68"></a> `00adfd68` | `69 00 80 52` | mov w9,#0x3 | `FALL_THROUGH`
<a id="insn-00adfd6c"></a> `00adfd6c` | `e9 6b 00 b9` | str w9,[sp, #0x68] | `FALL_THROUGH`
<a id="insn-00adfd70"></a> `00adfd70` | `29 e8 8e 52` | mov w9,#0x7741 | `FALL_THROUGH`
<a id="insn-00adfd74"></a> `00adfd74` | `aa bd ff 90` | adrp x10,0x293000 | `FALL_THROUGH`
<a id="insn-00adfd78"></a> `00adfd78` | `4a b9 1a 91` | add x10,x10,#0x6ae | `FALL_THROUGH`
<a id="insn-00adfd7c"></a> `00adfd7c` | `e0 13 85 3c` | stur q0,[sp, #0x51] | `FALL_THROUGH`
<a id="insn-00adfd80"></a> `00adfd80` | `40 01 c0 3d` | ldr q0,[x10] | `FALL_THROUGH`
<a id="insn-00adfd84"></a> `00adfd84` | `e9 13 08 78` | sturh w9,[sp, #0x81] | `FALL_THROUGH`
<a id="insn-00adfd88"></a> `00adfd88` | `89 00 80 52` | mov w9,#0x4 | `FALL_THROUGH`
<a id="insn-00adfd8c"></a> `00adfd8c` | `e9 8b 00 b9` | str w9,[sp, #0x88] | `FALL_THROUGH`
<a id="insn-00adfd90"></a> `00adfd90` | `e9 bd ff b0` | adrp x9,0x29c000 | `FALL_THROUGH`
<a id="insn-00adfd94"></a> `00adfd94` | `29 b1 0d 91` | add x9,x9,#0x36c | `FALL_THROUGH`
<a id="insn-00adfd98"></a> `00adfd98` | `e0 13 87 3c` | stur q0,[sp, #0x71] | `FALL_THROUGH`
<a id="insn-00adfd9c"></a> `00adfd9c` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00adfda0"></a> `00adfda0` | `49 28 8a 52` | mov w9,#0x5142 | `FALL_THROUGH`
<a id="insn-00adfda4"></a> `00adfda4` | `89 92 09 78` | sturh w9,[x20, #0x99] | `FALL_THROUGH`
<a id="insn-00adfda8"></a> `00adfda8` | `a9 00 80 52` | mov w9,#0x5 | `FALL_THROUGH`
<a id="insn-00adfdac"></a> `00adfdac` | `e9 ab 00 b9` | str w9,[sp, #0xa8] | `FALL_THROUGH`
<a id="insn-00adfdb0"></a> `00adfdb0` | `89 bd ff d0` | adrp x9,0x291000 | `FALL_THROUGH`
<a id="insn-00adfdb4"></a> `00adfdb4` | `29 dd 21 91` | add x9,x9,#0x877 | `FALL_THROUGH`
<a id="insn-00adfdb8"></a> `00adfdb8` | `80 92 88 3c` | stur q0,[x20, #0x89] | `FALL_THROUGH`
<a id="insn-00adfdbc"></a> `00adfdbc` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00adfdc0"></a> `00adfdc0` | `49 e8 8e 52` | mov w9,#0x7742 | `FALL_THROUGH`
<a id="insn-00adfdc4"></a> `00adfdc4` | `89 92 0b 78` | sturh w9,[x20, #0xb9] | `FALL_THROUGH`
<a id="insn-00adfdc8"></a> `00adfdc8` | `c9 00 80 52` | mov w9,#0x6 | `FALL_THROUGH`
<a id="insn-00adfdcc"></a> `00adfdcc` | `e9 cb 00 b9` | str w9,[sp, #0xc8] | `FALL_THROUGH`
<a id="insn-00adfdd0"></a> `00adfdd0` | `a9 bd ff b0` | adrp x9,0x294000 | `FALL_THROUGH`
<a id="insn-00adfdd4"></a> `00adfdd4` | `29 99 14 91` | add x9,x9,#0x526 | `FALL_THROUGH`
<a id="insn-00adfdd8"></a> `00adfdd8` | `80 92 8a 3c` | stur q0,[x20, #0xa9] | `FALL_THROUGH`
<a id="insn-00adfddc"></a> `00adfddc` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00adfde0"></a> `00adfde0` | `e8 43 00 39` | strb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00adfde4"></a> `00adfde4` | `e8 c3 00 39` | strb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00adfde8"></a> `00adfde8` | `e8 43 01 39` | strb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00adfdec"></a> `00adfdec` | `e8 c3 01 39` | strb w8,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00adfdf0"></a> `00adfdf0` | `e8 43 02 39` | strb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00adfdf4"></a> `00adfdf4` | `e8 c3 02 39` | strb w8,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00adfdf8"></a> `00adfdf8` | `e8 43 03 39` | strb w8,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-00adfdfc"></a> `00adfdfc` | `68 28 88 52` | mov w8,#0x4143 | `FALL_THROUGH`
<a id="insn-00adfe00"></a> `00adfe00` | `ff 0b 00 b9` | str wzr,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00adfe04"></a> `00adfe04` | `ff 8f 00 39` | strb wzr,[sp, #0x23] | `FALL_THROUGH`
<a id="insn-00adfe08"></a> `00adfe08` | `ff 0f 01 39` | strb wzr,[sp, #0x43] | `FALL_THROUGH`
<a id="insn-00adfe0c"></a> `00adfe0c` | `ff 8f 01 39` | strb wzr,[sp, #0x63] | `FALL_THROUGH`
<a id="insn-00adfe10"></a> `00adfe10` | `ff 0f 02 39` | strb wzr,[sp, #0x83] | `FALL_THROUGH`
<a id="insn-00adfe14"></a> `00adfe14` | `ff 8f 02 39` | strb wzr,[sp, #0xa3] | `FALL_THROUGH`
<a id="insn-00adfe18"></a> `00adfe18` | `ff 0f 03 39` | strb wzr,[sp, #0xc3] | `FALL_THROUGH`
<a id="insn-00adfe1c"></a> `00adfe1c` | `88 92 0d 78` | sturh w8,[x20, #0xd9] | `FALL_THROUGH`
<a id="insn-00adfe20"></a> `00adfe20` | `80 92 8c 3c` | stur q0,[x20, #0xc9] | `FALL_THROUGH`
<a id="insn-00adfe24"></a> `00adfe24` | `ff 8f 03 39` | strb wzr,[sp, #0xe3] | `FALL_THROUGH`
<a id="insn-00adfe28"></a> `00adfe28` | `7f 0a 00 f9` | str xzr,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00adfe2c"></a> `00adfe2c` | `3f 8c 00 f8` | str xzr,[x1, #0x8]! | `FALL_THROUGH`
<a id="insn-00adfe30"></a> `00adfe30` | `61 02 00 f9` | str x1,[x19] | `FALL_THROUGH`
<a id="insn-00adfe34"></a> `00adfe34` | `e2 23 00 91` | add x2,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00adfe38"></a> `00adfe38` | `e3 23 00 91` | add x3,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00adfe3c"></a> `00adfe3c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00adfe40"></a> `00adfe40` | `9e e3 e4 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-00adfe44"></a> `00adfe44` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00adfe48"></a> `00adfe48` | `82 82 00 91` | add x2,x20,#0x20 | `FALL_THROUGH`
<a id="insn-00adfe4c"></a> `00adfe4c` | `83 82 00 91` | add x3,x20,#0x20 | `FALL_THROUGH`
<a id="insn-00adfe50"></a> `00adfe50` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00adfe54"></a> `00adfe54` | `99 e3 e4 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-00adfe58"></a> `00adfe58` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00adfe5c"></a> `00adfe5c` | `82 02 01 91` | add x2,x20,#0x40 | `FALL_THROUGH`
<a id="insn-00adfe60"></a> `00adfe60` | `83 02 01 91` | add x3,x20,#0x40 | `FALL_THROUGH`
<a id="insn-00adfe64"></a> `00adfe64` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00adfe68"></a> `00adfe68` | `94 e3 e4 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-00adfe6c"></a> `00adfe6c` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00adfe70"></a> `00adfe70` | `82 82 01 91` | add x2,x20,#0x60 | `FALL_THROUGH`
<a id="insn-00adfe74"></a> `00adfe74` | `83 82 01 91` | add x3,x20,#0x60 | `FALL_THROUGH`
<a id="insn-00adfe78"></a> `00adfe78` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00adfe7c"></a> `00adfe7c` | `8f e3 e4 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-00adfe80"></a> `00adfe80` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00adfe84"></a> `00adfe84` | `82 02 02 91` | add x2,x20,#0x80 | `FALL_THROUGH`
<a id="insn-00adfe88"></a> `00adfe88` | `83 02 02 91` | add x3,x20,#0x80 | `FALL_THROUGH`
<a id="insn-00adfe8c"></a> `00adfe8c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00adfe90"></a> `00adfe90` | `8a e3 e4 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-00adfe94"></a> `00adfe94` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00adfe98"></a> `00adfe98` | `82 82 02 91` | add x2,x20,#0xa0 | `FALL_THROUGH`
<a id="insn-00adfe9c"></a> `00adfe9c` | `83 82 02 91` | add x3,x20,#0xa0 | `FALL_THROUGH`
<a id="insn-00adfea0"></a> `00adfea0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00adfea4"></a> `00adfea4` | `85 e3 e4 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-00adfea8"></a> `00adfea8` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00adfeac"></a> `00adfeac` | `82 02 03 91` | add x2,x20,#0xc0 | `FALL_THROUGH`
<a id="insn-00adfeb0"></a> `00adfeb0` | `83 02 03 91` | add x3,x20,#0xc0 | `FALL_THROUGH`
<a id="insn-00adfeb4"></a> `00adfeb4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00adfeb8"></a> `00adfeb8` | `80 e3 e4 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-00adfebc"></a> `00adfebc` | `e8 43 43 39` | ldrb w8,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-00adfec0"></a> `00adfec0` | `e8 03 00 37` | tbnz w8,#0x0,0x00adff3c | `CONDITIONAL_JUMP`
<a id="insn-00adfec4"></a> `00adfec4` | `e8 c3 42 39` | ldrb w8,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00adfec8"></a> `00adfec8` | `28 04 00 37` | tbnz w8,#0x0,0x00adff4c | `CONDITIONAL_JUMP`
<a id="insn-00adfecc"></a> `00adfecc` | `e8 43 42 39` | ldrb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00adfed0"></a> `00adfed0` | `68 04 00 37` | tbnz w8,#0x0,0x00adff5c | `CONDITIONAL_JUMP`
<a id="insn-00adfed4"></a> `00adfed4` | `e8 c3 41 39` | ldrb w8,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00adfed8"></a> `00adfed8` | `a8 04 00 37` | tbnz w8,#0x0,0x00adff6c | `CONDITIONAL_JUMP`
<a id="insn-00adfedc"></a> `00adfedc` | `e8 43 41 39` | ldrb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00adfee0"></a> `00adfee0` | `e8 04 00 37` | tbnz w8,#0x0,0x00adff7c | `CONDITIONAL_JUMP`
<a id="insn-00adfee4"></a> `00adfee4` | `e8 c3 40 39` | ldrb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00adfee8"></a> `00adfee8` | `28 05 00 37` | tbnz w8,#0x0,0x00adff8c | `CONDITIONAL_JUMP`
<a id="insn-00adfeec"></a> `00adfeec` | `e8 43 40 39` | ldrb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00adfef0"></a> `00adfef0` | `68 00 00 36` | tbz w8,#0x0,0x00adfefc | `CONDITIONAL_JUMP`
<a id="insn-00adfef4"></a> `00adfef4` | `e0 13 40 f9` | ldr x0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00adfef8"></a> `00adfef8` | `5a ec 03 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00adfefc"></a> `00adfefc` | `c0 c9 ff b0` | adrp x0,0x418000 | `FALL_THROUGH`
<a id="insn-00adff00"></a> `00adff00` | `00 c0 0c 91` | add x0,x0,#0x330 | `FALL_THROUGH`
<a id="insn-00adff04"></a> `00adff04` | `01 2e 00 b0` | adrp x1,0x10a0000 | `FALL_THROUGH`
<a id="insn-00adff08"></a> `00adff08` | `21 c0 00 91` | add x1,x1,#0x30 | `FALL_THROUGH`
<a id="insn-00adff0c"></a> `00adff0c` | `22 08 00 d0` | adrp x2,0xbe5000 | `FALL_THROUGH`
<a id="insn-00adff10"></a> `00adff10` | `42 40 3f 91` | add x2,x2,#0xfd0 | `FALL_THROUGH`
<a id="insn-00adff14"></a> `00adff14` | `33 ec 03 94` | bl 0x00bdafe0 | `UNCONDITIONAL_CALL`
<a id="insn-00adff18"></a> `00adff18` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00adff1c"></a> `00adff1c` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00adff20"></a> `00adff20` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00adff24"></a> `00adff24` | `41 0a 00 54` | b.ne 0x00ae006c | `CONDITIONAL_JUMP`
<a id="insn-00adff28"></a> `00adff28` | `f4 4f 51 a9` | ldp x20,x19,[sp, #0x110] | `FALL_THROUGH`
<a id="insn-00adff2c"></a> `00adff2c` | `fc 57 50 a9` | ldp x28,x21,[sp, #0x100] | `FALL_THROUGH`
<a id="insn-00adff30"></a> `00adff30` | `fd 7b 4f a9` | ldp x29,x30,[sp, #0xf0] | `FALL_THROUGH`
<a id="insn-00adff34"></a> `00adff34` | `ff 83 04 91` | add sp,sp,#0x120 | `FALL_THROUGH`
<a id="insn-00adff38"></a> `00adff38` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00adff3c"></a> `00adff3c` | `e0 73 40 f9` | ldr x0,[sp, #0xe0] | `FALL_THROUGH`
<a id="insn-00adff40"></a> `00adff40` | `48 ec 03 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00adff44"></a> `00adff44` | `e8 c3 42 39` | ldrb w8,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00adff48"></a> `00adff48` | `28 fc 07 36` | tbz w8,#0x0,0x00adfecc | `CONDITIONAL_JUMP`
<a id="insn-00adff4c"></a> `00adff4c` | `e0 63 40 f9` | ldr x0,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00adff50"></a> `00adff50` | `44 ec 03 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00adff54"></a> `00adff54` | `e8 43 42 39` | ldrb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00adff58"></a> `00adff58` | `e8 fb 07 36` | tbz w8,#0x0,0x00adfed4 | `CONDITIONAL_JUMP`
<a id="insn-00adff5c"></a> `00adff5c` | `e0 53 40 f9` | ldr x0,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00adff60"></a> `00adff60` | `40 ec 03 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00adff64"></a> `00adff64` | `e8 c3 41 39` | ldrb w8,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00adff68"></a> `00adff68` | `a8 fb 07 36` | tbz w8,#0x0,0x00adfedc | `CONDITIONAL_JUMP`
<a id="insn-00adff6c"></a> `00adff6c` | `e0 43 40 f9` | ldr x0,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00adff70"></a> `00adff70` | `3c ec 03 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00adff74"></a> `00adff74` | `e8 43 41 39` | ldrb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00adff78"></a> `00adff78` | `68 fb 07 36` | tbz w8,#0x0,0x00adfee4 | `CONDITIONAL_JUMP`
<a id="insn-00adff7c"></a> `00adff7c` | `e0 33 40 f9` | ldr x0,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00adff80"></a> `00adff80` | `38 ec 03 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00adff84"></a> `00adff84` | `e8 c3 40 39` | ldrb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00adff88"></a> `00adff88` | `28 fb 07 36` | tbz w8,#0x0,0x00adfeec | `CONDITIONAL_JUMP`
<a id="insn-00adff8c"></a> `00adff8c` | `e0 23 40 f9` | ldr x0,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00adff90"></a> `00adff90` | `34 ec 03 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00adff94"></a> `00adff94` | `e8 43 40 39` | ldrb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00adff98"></a> `00adff98` | `e8 fa 07 37` | tbnz w8,#0x0,0x00adfef4 | `CONDITIONAL_JUMP`
<a id="insn-00adff9c"></a> `00adff9c` | `d8 ff ff 17` | b 0x00adfefc | `UNCONDITIONAL_JUMP`
<a id="insn-00ae006c"></a> `00ae006c` | `09 ec 03 94` | bl 0x00bdb090 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00adfce0`](#insn-00adfce0) 範囲 `[['00adfce0', '00adfd23']]`
  - `FALL_THROUGH` [`00adfd20`](#insn-00adfd20) → [`00adfd24`](#insn-00adfd24)
- ブロック [`00adfd24`](#insn-00adfd24) 範囲 `[['00adfd24', '00adfdbb']]`
  - `FALL_THROUGH` [`00adfdb8`](#insn-00adfdb8) → [`00adfdbc`](#insn-00adfdbc)
- ブロック [`00adfdbc`](#insn-00adfdbc) 範囲 `[['00adfdbc', '00adfdcb']]`
  - `FALL_THROUGH` [`00adfdc8`](#insn-00adfdc8) → [`00adfdcc`](#insn-00adfdcc)
- ブロック [`00adfdcc`](#insn-00adfdcc) 範囲 `[['00adfdcc', '00adfea3']]`
  - `FALL_THROUGH` [`00adfea0`](#insn-00adfea0) → [`00adfea4`](#insn-00adfea4)
- ブロック [`00adfea4`](#insn-00adfea4) 範囲 `[['00adfea4', '00adfebf']]`
  - `FALL_THROUGH` [`00adfebc`](#insn-00adfebc) → [`00adfec0`](#insn-00adfec0)
- ブロック [`00adfec0`](#insn-00adfec0) 範囲 `[['00adfec0', '00adfec3']]`
  - `CONDITIONAL_JUMP` [`00adfec0`](#insn-00adfec0) → [`00adff3c`](#insn-00adff3c)
  - `FALL_THROUGH` [`00adfec0`](#insn-00adfec0) → [`00adfec4`](#insn-00adfec4)
- ブロック [`00adfec4`](#insn-00adfec4) 範囲 `[['00adfec4', '00adfecb']]`
  - `CONDITIONAL_JUMP` [`00adfec8`](#insn-00adfec8) → [`00adff4c`](#insn-00adff4c)
  - `FALL_THROUGH` [`00adfec8`](#insn-00adfec8) → [`00adfecc`](#insn-00adfecc)
- ブロック [`00adfecc`](#insn-00adfecc) 範囲 `[['00adfecc', '00adfecf']]`
  - `FALL_THROUGH` [`00adfecc`](#insn-00adfecc) → [`00adfed0`](#insn-00adfed0)
- ブロック [`00adfed0`](#insn-00adfed0) 範囲 `[['00adfed0', '00adfed3']]`
  - `CONDITIONAL_JUMP` [`00adfed0`](#insn-00adfed0) → [`00adff5c`](#insn-00adff5c)
  - `FALL_THROUGH` [`00adfed0`](#insn-00adfed0) → [`00adfed4`](#insn-00adfed4)
- ブロック [`00adfed4`](#insn-00adfed4) 範囲 `[['00adfed4', '00adfedb']]`
  - `CONDITIONAL_JUMP` [`00adfed8`](#insn-00adfed8) → [`00adff6c`](#insn-00adff6c)
  - `FALL_THROUGH` [`00adfed8`](#insn-00adfed8) → [`00adfedc`](#insn-00adfedc)
- ブロック [`00adfedc`](#insn-00adfedc) 範囲 `[['00adfedc', '00adfedf']]`
  - `FALL_THROUGH` [`00adfedc`](#insn-00adfedc) → [`00adfee0`](#insn-00adfee0)
- ブロック [`00adfee0`](#insn-00adfee0) 範囲 `[['00adfee0', '00adfee3']]`
  - `CONDITIONAL_JUMP` [`00adfee0`](#insn-00adfee0) → [`00adff7c`](#insn-00adff7c)
  - `FALL_THROUGH` [`00adfee0`](#insn-00adfee0) → [`00adfee4`](#insn-00adfee4)
- ブロック [`00adfee4`](#insn-00adfee4) 範囲 `[['00adfee4', '00adfeeb']]`
  - `CONDITIONAL_JUMP` [`00adfee8`](#insn-00adfee8) → [`00adff8c`](#insn-00adff8c)
  - `FALL_THROUGH` [`00adfee8`](#insn-00adfee8) → [`00adfeec`](#insn-00adfeec)
- ブロック [`00adfeec`](#insn-00adfeec) 範囲 `[['00adfeec', '00adfef3']]`
  - `CONDITIONAL_JUMP` [`00adfef0`](#insn-00adfef0) → [`00adfefc`](#insn-00adfefc)
  - `FALL_THROUGH` [`00adfef0`](#insn-00adfef0) → [`00adfef4`](#insn-00adfef4)
- ブロック [`00adfef4`](#insn-00adfef4) 範囲 `[['00adfef4', '00adfefb']]`
  - `FALL_THROUGH` [`00adfef8`](#insn-00adfef8) → [`00adfefc`](#insn-00adfefc)
- ブロック [`00adfefc`](#insn-00adfefc) 範囲 `[['00adfefc', '00adff27']]`
  - `CONDITIONAL_JUMP` [`00adff24`](#insn-00adff24) → [`00ae006c`](#insn-00ae006c)
  - `FALL_THROUGH` [`00adff24`](#insn-00adff24) → [`00adff28`](#insn-00adff28)
- ブロック [`00adff28`](#insn-00adff28) 範囲 `[['00adff28', '00adff3b']]`
- ブロック [`00adff3c`](#insn-00adff3c) 範囲 `[['00adff3c', '00adff3f']]`
  - `FALL_THROUGH` [`00adff3c`](#insn-00adff3c) → [`00adff40`](#insn-00adff40)
- ブロック [`00adff40`](#insn-00adff40) 範囲 `[['00adff40', '00adff4b']]`
  - `CONDITIONAL_JUMP` [`00adff48`](#insn-00adff48) → [`00adfecc`](#insn-00adfecc)
  - `FALL_THROUGH` [`00adff48`](#insn-00adff48) → [`00adff4c`](#insn-00adff4c)
- ブロック [`00adff4c`](#insn-00adff4c) 範囲 `[['00adff4c', '00adff5b']]`
  - `CONDITIONAL_JUMP` [`00adff58`](#insn-00adff58) → [`00adfed4`](#insn-00adfed4)
  - `FALL_THROUGH` [`00adff58`](#insn-00adff58) → [`00adff5c`](#insn-00adff5c)
- ブロック [`00adff5c`](#insn-00adff5c) 範囲 `[['00adff5c', '00adff6b']]`
  - `CONDITIONAL_JUMP` [`00adff68`](#insn-00adff68) → [`00adfedc`](#insn-00adfedc)
  - `FALL_THROUGH` [`00adff68`](#insn-00adff68) → [`00adff6c`](#insn-00adff6c)
- ブロック [`00adff6c`](#insn-00adff6c) 範囲 `[['00adff6c', '00adff7b']]`
  - `CONDITIONAL_JUMP` [`00adff78`](#insn-00adff78) → [`00adfee4`](#insn-00adfee4)
  - `FALL_THROUGH` [`00adff78`](#insn-00adff78) → [`00adff7c`](#insn-00adff7c)
- ブロック [`00adff7c`](#insn-00adff7c) 範囲 `[['00adff7c', '00adff87']]`
  - `FALL_THROUGH` [`00adff84`](#insn-00adff84) → [`00adff88`](#insn-00adff88)
- ブロック [`00adff88`](#insn-00adff88) 範囲 `[['00adff88', '00adff8b']]`
  - `CONDITIONAL_JUMP` [`00adff88`](#insn-00adff88) → [`00adfeec`](#insn-00adfeec)
  - `FALL_THROUGH` [`00adff88`](#insn-00adff88) → [`00adff8c`](#insn-00adff8c)
- ブロック [`00adff8c`](#insn-00adff8c) 範囲 `[['00adff8c', '00adff9b']]`
  - `CONDITIONAL_JUMP` [`00adff98`](#insn-00adff98) → [`00adfef4`](#insn-00adfef4)
  - `FALL_THROUGH` [`00adff98`](#insn-00adff98) → [`00adff9c`](#insn-00adff9c)
- ブロック [`00adff9c`](#insn-00adff9c) 範囲 `[['00adff9c', '00adff9f']]`
  - `UNCONDITIONAL_JUMP` [`00adff9c`](#insn-00adff9c) → [`00adfefc`](#insn-00adfefc)
- ブロック [`00ae006c`](#insn-00ae006c) 範囲 `[['00ae006c', '00ae006f']]`

## 命令位置別の参照

- [`00adfce4`](#insn-00adfce4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfce8`](#insn-00adfce8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfcec`](#insn-00adfcec) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfd10`](#insn-00adfd10) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfd1c`](#insn-00adfd1c) → `002a7377`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00adfd24`](#insn-00adfd24) → `Stack[-0xff]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfd28`](#insn-00adfd28) → `Stack[-0xf8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfd38`](#insn-00adfd38) → `Stack[-0x10f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfd40`](#insn-00adfd40) → `002a738a`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00adfd44`](#insn-00adfd44) → `Stack[-0xdf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfd4c`](#insn-00adfd4c) → `Stack[-0xd8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfd5c`](#insn-00adfd5c) → `Stack[-0xef]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfd60`](#insn-00adfd60) → `002a80e0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00adfd64`](#insn-00adfd64) → `Stack[-0xbf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfd6c`](#insn-00adfd6c) → `Stack[-0xb8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfd7c`](#insn-00adfd7c) → `Stack[-0xcf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfd80`](#insn-00adfd80) → `002936ae`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00adfd84`](#insn-00adfd84) → `Stack[-0x9f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfd8c`](#insn-00adfd8c) → `Stack[-0x98]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfd98`](#insn-00adfd98) → `Stack[-0xaf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfd9c`](#insn-00adfd9c) → `0029c36c`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00adfda4`](#insn-00adfda4) → `Stack[-0x7f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfdac`](#insn-00adfdac) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfdb8`](#insn-00adfdb8) → `Stack[-0x8f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfdbc`](#insn-00adfdbc) → `00291877`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00adfdc4`](#insn-00adfdc4) → `Stack[-0x5f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfdcc`](#insn-00adfdcc) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfdd8`](#insn-00adfdd8) → `Stack[-0x6f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfddc`](#insn-00adfddc) → `00294526`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00adfde0`](#insn-00adfde0) → `Stack[-0x110]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfde4`](#insn-00adfde4) → `Stack[-0xf0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfde8`](#insn-00adfde8) → `Stack[-0xd0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfdec`](#insn-00adfdec) → `Stack[-0xb0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfdf0`](#insn-00adfdf0) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfdf4`](#insn-00adfdf4) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfdf8`](#insn-00adfdf8) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfe00`](#insn-00adfe00) → `Stack[-0x118]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfe04`](#insn-00adfe04) → `Stack[-0xfd]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfe08`](#insn-00adfe08) → `Stack[-0xdd]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfe0c`](#insn-00adfe0c) → `Stack[-0xbd]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfe10`](#insn-00adfe10) → `Stack[-0x9d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfe14`](#insn-00adfe14) → `Stack[-0x7d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfe18`](#insn-00adfe18) → `Stack[-0x5d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfe1c`](#insn-00adfe1c) → `Stack[-0x3f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfe20`](#insn-00adfe20) → `Stack[-0x4f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfe24`](#insn-00adfe24) → `Stack[-0x3d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfe28`](#insn-00adfe28) → `010a0040`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adfe2c`](#insn-00adfe2c) → `010a0038`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adfe30`](#insn-00adfe30) → `010a0030`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adfe30`](#insn-00adfe30) → `010a0038`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adfe3c`](#insn-00adfe3c) → `010a0030`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adfe40`](#insn-00adfe40) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`00adfe44`](#insn-00adfe44) → `010a0038`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adfe50`](#insn-00adfe50) → `010a0030`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adfe54`](#insn-00adfe54) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`00adfe58`](#insn-00adfe58) → `010a0038`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adfe64`](#insn-00adfe64) → `010a0030`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adfe68`](#insn-00adfe68) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`00adfe6c`](#insn-00adfe6c) → `010a0038`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adfe78`](#insn-00adfe78) → `010a0030`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adfe7c`](#insn-00adfe7c) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`00adfe80`](#insn-00adfe80) → `010a0038`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adfe8c`](#insn-00adfe8c) → `010a0030`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adfe90`](#insn-00adfe90) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`00adfe94`](#insn-00adfe94) → `010a0038`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adfea0`](#insn-00adfea0) → `010a0030`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adfea4`](#insn-00adfea4) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`00adfea8`](#insn-00adfea8) → `010a0038`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adfeb4`](#insn-00adfeb4) → `010a0030`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adfeb8`](#insn-00adfeb8) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`00adfebc`](#insn-00adfebc) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfec0`](#insn-00adfec0) → [`00adff3c`](#insn-00adff3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfec4`](#insn-00adfec4) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfec8`](#insn-00adfec8) → [`00adff4c`](#insn-00adff4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfecc`](#insn-00adfecc) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfed0`](#insn-00adfed0) → [`00adff5c`](#insn-00adff5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfed4`](#insn-00adfed4) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfed8`](#insn-00adfed8) → [`00adff6c`](#insn-00adff6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfedc`](#insn-00adfedc) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfee0`](#insn-00adfee0) → [`00adff7c`](#insn-00adff7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfee4`](#insn-00adfee4) → `Stack[-0xf0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfee8`](#insn-00adfee8) → [`00adff8c`](#insn-00adff8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfeec`](#insn-00adfeec) → `Stack[-0x110]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfef0`](#insn-00adfef0) → [`00adfefc`](#insn-00adfefc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfef4`](#insn-00adfef4) → `Stack[-0x100]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfef8`](#insn-00adfef8) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00adff00`](#insn-00adff00) → [`00418330`](../00418/00418330.md) · `PARAM` · `ANALYSIS` · 関数 `00418330` · 推定シンボル `None` · 推定型 `None`
- [`00adff08`](#insn-00adff08) → `010a0030`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adff10`](#insn-00adff10) → `00be5fd0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00adff14`](#insn-00adff14) → [`00bdafe0`](../00bda/00bdafe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdafe0` · 推定シンボル `None` · 推定型 `None`
- [`00adff1c`](#insn-00adff1c) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adff24`](#insn-00adff24) → [`00ae006c`](#insn-00ae006c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adff28`](#insn-00adff28) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adff2c`](#insn-00adff2c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adff30`](#insn-00adff30) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adff3c`](#insn-00adff3c) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adff40`](#insn-00adff40) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00adff44`](#insn-00adff44) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adff48`](#insn-00adff48) → [`00adfecc`](#insn-00adfecc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adff4c`](#insn-00adff4c) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adff50`](#insn-00adff50) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00adff54`](#insn-00adff54) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adff58`](#insn-00adff58) → [`00adfed4`](#insn-00adfed4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adff5c`](#insn-00adff5c) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adff60`](#insn-00adff60) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00adff64`](#insn-00adff64) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adff68`](#insn-00adff68) → [`00adfedc`](#insn-00adfedc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adff6c`](#insn-00adff6c) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adff70`](#insn-00adff70) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00adff74`](#insn-00adff74) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adff78`](#insn-00adff78) → [`00adfee4`](#insn-00adfee4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adff7c`](#insn-00adff7c) → `Stack[-0xc0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adff80`](#insn-00adff80) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00adff84`](#insn-00adff84) → `Stack[-0xf0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adff88`](#insn-00adff88) → [`00adfeec`](#insn-00adfeec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adff8c`](#insn-00adff8c) → `Stack[-0xe0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adff90`](#insn-00adff90) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00adff94`](#insn-00adff94) → `Stack[-0x110]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adff98`](#insn-00adff98) → [`00adfef4`](#insn-00adfef4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adff9c`](#insn-00adff9c) → [`00adfefc`](#insn-00adfefc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae006c`](#insn-00ae006c) → [`00bdb090`](../00bdb/00bdb090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb090` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00adfce4`](#insn-00adfce4)

~~~json
{
  "source": "00adfce4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfce8`](#insn-00adfce8)

~~~json
{
  "source": "00adfce8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfcec`](#insn-00adfcec)

~~~json
{
  "source": "00adfcec",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfd10`](#insn-00adfd10)

~~~json
{
  "source": "00adfd10",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfd1c`](#insn-00adfd1c)

~~~json
{
  "source": "00adfd1c",
  "target": "002a7377",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a7377",
  "offset": 0,
  "size": 19,
  "datatype": "string",
  "bytes": "43676b496a4d33795f5a516145414951416700",
  "capture_start": "002a7377",
  "capture_bytes": 19,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00adfd24`](#insn-00adfd24)

~~~json
{
  "source": "00adfd24",
  "target": "Stack[-0xff]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfd28`](#insn-00adfd28)

~~~json
{
  "source": "00adfd28",
  "target": "Stack[-0xf8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfd38`](#insn-00adfd38)

~~~json
{
  "source": "00adfd38",
  "target": "Stack[-0x10f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfd40`](#insn-00adfd40)

~~~json
{
  "source": "00adfd40",
  "target": "002a738a",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a738a",
  "offset": 0,
  "size": 19,
  "datatype": "string",
  "bytes": "43676b496a4d33795f5a516145414951424100",
  "capture_start": "002a738a",
  "capture_bytes": 19,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00adfd44`](#insn-00adfd44)

~~~json
{
  "source": "00adfd44",
  "target": "Stack[-0xdf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfd4c`](#insn-00adfd4c)

~~~json
{
  "source": "00adfd4c",
  "target": "Stack[-0xd8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfd5c`](#insn-00adfd5c)

~~~json
{
  "source": "00adfd5c",
  "target": "Stack[-0xef]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfd60`](#insn-00adfd60)

~~~json
{
  "source": "00adfd60",
  "target": "002a80e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a80e0",
  "offset": 0,
  "size": 19,
  "datatype": "string",
  "bytes": "43676b496a4d33795f5a516145414951426700",
  "capture_start": "002a80e0",
  "capture_bytes": 19,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00adfd64`](#insn-00adfd64)

~~~json
{
  "source": "00adfd64",
  "target": "Stack[-0xbf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfd6c`](#insn-00adfd6c)

~~~json
{
  "source": "00adfd6c",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfd7c`](#insn-00adfd7c)

~~~json
{
  "source": "00adfd7c",
  "target": "Stack[-0xcf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfd80`](#insn-00adfd80)

~~~json
{
  "source": "00adfd80",
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
- 参照命令 [`00adfd84`](#insn-00adfd84)

~~~json
{
  "source": "00adfd84",
  "target": "Stack[-0x9f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfd8c`](#insn-00adfd8c)

~~~json
{
  "source": "00adfd8c",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfd98`](#insn-00adfd98)

~~~json
{
  "source": "00adfd98",
  "target": "Stack[-0xaf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfd9c`](#insn-00adfd9c)

~~~json
{
  "source": "00adfd9c",
  "target": "0029c36c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029c36c",
  "offset": 0,
  "size": 19,
  "datatype": "string",
  "bytes": "43676b496a4d33795f5a516145414951425100",
  "capture_start": "0029c36c",
  "capture_bytes": 19,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00adfda4`](#insn-00adfda4)

~~~json
{
  "source": "00adfda4",
  "target": "Stack[-0x7f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfdac`](#insn-00adfdac)

~~~json
{
  "source": "00adfdac",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfdb8`](#insn-00adfdb8)

~~~json
{
  "source": "00adfdb8",
  "target": "Stack[-0x8f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfdbc`](#insn-00adfdbc)

~~~json
{
  "source": "00adfdbc",
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
- 参照命令 [`00adfdc4`](#insn-00adfdc4)

~~~json
{
  "source": "00adfdc4",
  "target": "Stack[-0x5f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfdcc`](#insn-00adfdcc)

~~~json
{
  "source": "00adfdcc",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfdd8`](#insn-00adfdd8)

~~~json
{
  "source": "00adfdd8",
  "target": "Stack[-0x6f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfddc`](#insn-00adfddc)

~~~json
{
  "source": "00adfddc",
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
- 参照命令 [`00adfde0`](#insn-00adfde0)

~~~json
{
  "source": "00adfde0",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfde4`](#insn-00adfde4)

~~~json
{
  "source": "00adfde4",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfde8`](#insn-00adfde8)

~~~json
{
  "source": "00adfde8",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfdec`](#insn-00adfdec)

~~~json
{
  "source": "00adfdec",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfdf0`](#insn-00adfdf0)

~~~json
{
  "source": "00adfdf0",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfdf4`](#insn-00adfdf4)

~~~json
{
  "source": "00adfdf4",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfdf8`](#insn-00adfdf8)

~~~json
{
  "source": "00adfdf8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfe00`](#insn-00adfe00)

~~~json
{
  "source": "00adfe00",
  "target": "Stack[-0x118]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfe04`](#insn-00adfe04)

~~~json
{
  "source": "00adfe04",
  "target": "Stack[-0xfd]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfe08`](#insn-00adfe08)

~~~json
{
  "source": "00adfe08",
  "target": "Stack[-0xdd]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfe0c`](#insn-00adfe0c)

~~~json
{
  "source": "00adfe0c",
  "target": "Stack[-0xbd]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfe10`](#insn-00adfe10)

~~~json
{
  "source": "00adfe10",
  "target": "Stack[-0x9d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfe14`](#insn-00adfe14)

~~~json
{
  "source": "00adfe14",
  "target": "Stack[-0x7d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfe18`](#insn-00adfe18)

~~~json
{
  "source": "00adfe18",
  "target": "Stack[-0x5d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfe1c`](#insn-00adfe1c)

~~~json
{
  "source": "00adfe1c",
  "target": "Stack[-0x3f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfe20`](#insn-00adfe20)

~~~json
{
  "source": "00adfe20",
  "target": "Stack[-0x4f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfe24`](#insn-00adfe24)

~~~json
{
  "source": "00adfe24",
  "target": "Stack[-0x3d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfe28`](#insn-00adfe28)

~~~json
{
  "source": "00adfe28",
  "target": "010a0040",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0040",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adfe2c`](#insn-00adfe2c)

~~~json
{
  "source": "00adfe2c",
  "target": "010a0038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0038",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adfe30`](#insn-00adfe30)

~~~json
{
  "source": "00adfe30",
  "target": "010a0030",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0030",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adfe30`](#insn-00adfe30)

~~~json
{
  "source": "00adfe30",
  "target": "010a0038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0038",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adfe3c`](#insn-00adfe3c)

~~~json
{
  "source": "00adfe3c",
  "target": "010a0030",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0030",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adfe40`](#insn-00adfe40)

~~~json
{
  "source": "00adfe40",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adfe44`](#insn-00adfe44)

~~~json
{
  "source": "00adfe44",
  "target": "010a0038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0038",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adfe50`](#insn-00adfe50)

~~~json
{
  "source": "00adfe50",
  "target": "010a0030",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0030",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adfe54`](#insn-00adfe54)

~~~json
{
  "source": "00adfe54",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adfe58`](#insn-00adfe58)

~~~json
{
  "source": "00adfe58",
  "target": "010a0038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0038",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adfe64`](#insn-00adfe64)

~~~json
{
  "source": "00adfe64",
  "target": "010a0030",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0030",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adfe68`](#insn-00adfe68)

~~~json
{
  "source": "00adfe68",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adfe6c`](#insn-00adfe6c)

~~~json
{
  "source": "00adfe6c",
  "target": "010a0038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0038",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adfe78`](#insn-00adfe78)

~~~json
{
  "source": "00adfe78",
  "target": "010a0030",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0030",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adfe7c`](#insn-00adfe7c)

~~~json
{
  "source": "00adfe7c",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adfe80`](#insn-00adfe80)

~~~json
{
  "source": "00adfe80",
  "target": "010a0038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0038",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adfe8c`](#insn-00adfe8c)

~~~json
{
  "source": "00adfe8c",
  "target": "010a0030",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0030",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adfe90`](#insn-00adfe90)

~~~json
{
  "source": "00adfe90",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adfe94`](#insn-00adfe94)

~~~json
{
  "source": "00adfe94",
  "target": "010a0038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0038",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adfea0`](#insn-00adfea0)

~~~json
{
  "source": "00adfea0",
  "target": "010a0030",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0030",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adfea4`](#insn-00adfea4)

~~~json
{
  "source": "00adfea4",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adfea8`](#insn-00adfea8)

~~~json
{
  "source": "00adfea8",
  "target": "010a0038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0038",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adfeb4`](#insn-00adfeb4)

~~~json
{
  "source": "00adfeb4",
  "target": "010a0030",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0030",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adfeb8`](#insn-00adfeb8)

~~~json
{
  "source": "00adfeb8",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adfebc`](#insn-00adfebc)

~~~json
{
  "source": "00adfebc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfec0`](#insn-00adfec0)

~~~json
{
  "source": "00adfec0",
  "target": "00adff3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfec4`](#insn-00adfec4)

~~~json
{
  "source": "00adfec4",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfec8`](#insn-00adfec8)

~~~json
{
  "source": "00adfec8",
  "target": "00adff4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfecc`](#insn-00adfecc)

~~~json
{
  "source": "00adfecc",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfed0`](#insn-00adfed0)

~~~json
{
  "source": "00adfed0",
  "target": "00adff5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfed4`](#insn-00adfed4)

~~~json
{
  "source": "00adfed4",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfed8`](#insn-00adfed8)

~~~json
{
  "source": "00adfed8",
  "target": "00adff6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfedc`](#insn-00adfedc)

~~~json
{
  "source": "00adfedc",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfee0`](#insn-00adfee0)

~~~json
{
  "source": "00adfee0",
  "target": "00adff7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfee4`](#insn-00adfee4)

~~~json
{
  "source": "00adfee4",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfee8`](#insn-00adfee8)

~~~json
{
  "source": "00adfee8",
  "target": "00adff8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfeec`](#insn-00adfeec)

~~~json
{
  "source": "00adfeec",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfef0`](#insn-00adfef0)

~~~json
{
  "source": "00adfef0",
  "target": "00adfefc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfef4`](#insn-00adfef4)

~~~json
{
  "source": "00adfef4",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfef8`](#insn-00adfef8)

~~~json
{
  "source": "00adfef8",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adff00`](#insn-00adff00)

~~~json
{
  "source": "00adff00",
  "target": "00418330",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adff08`](#insn-00adff08)

~~~json
{
  "source": "00adff08",
  "target": "010a0030",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0030",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adff10`](#insn-00adff10)

~~~json
{
  "source": "00adff10",
  "target": "00be5fd0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00be5fd0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00adff14`](#insn-00adff14)

~~~json
{
  "source": "00adff14",
  "target": "00bdafe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adff1c`](#insn-00adff1c)

~~~json
{
  "source": "00adff1c",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adff24`](#insn-00adff24)

~~~json
{
  "source": "00adff24",
  "target": "00ae006c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adff28`](#insn-00adff28)

~~~json
{
  "source": "00adff28",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adff2c`](#insn-00adff2c)

~~~json
{
  "source": "00adff2c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adff30`](#insn-00adff30)

~~~json
{
  "source": "00adff30",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adff3c`](#insn-00adff3c)

~~~json
{
  "source": "00adff3c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adff40`](#insn-00adff40)

~~~json
{
  "source": "00adff40",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adff44`](#insn-00adff44)

~~~json
{
  "source": "00adff44",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adff48`](#insn-00adff48)

~~~json
{
  "source": "00adff48",
  "target": "00adfecc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adff4c`](#insn-00adff4c)

~~~json
{
  "source": "00adff4c",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adff50`](#insn-00adff50)

~~~json
{
  "source": "00adff50",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adff54`](#insn-00adff54)

~~~json
{
  "source": "00adff54",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adff58`](#insn-00adff58)

~~~json
{
  "source": "00adff58",
  "target": "00adfed4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adff5c`](#insn-00adff5c)

~~~json
{
  "source": "00adff5c",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adff60`](#insn-00adff60)

~~~json
{
  "source": "00adff60",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adff64`](#insn-00adff64)

~~~json
{
  "source": "00adff64",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adff68`](#insn-00adff68)

~~~json
{
  "source": "00adff68",
  "target": "00adfedc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adff6c`](#insn-00adff6c)

~~~json
{
  "source": "00adff6c",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adff70`](#insn-00adff70)

~~~json
{
  "source": "00adff70",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adff74`](#insn-00adff74)

~~~json
{
  "source": "00adff74",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adff78`](#insn-00adff78)

~~~json
{
  "source": "00adff78",
  "target": "00adfee4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adff7c`](#insn-00adff7c)

~~~json
{
  "source": "00adff7c",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adff80`](#insn-00adff80)

~~~json
{
  "source": "00adff80",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adff84`](#insn-00adff84)

~~~json
{
  "source": "00adff84",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adff88`](#insn-00adff88)

~~~json
{
  "source": "00adff88",
  "target": "00adfeec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adff8c`](#insn-00adff8c)

~~~json
{
  "source": "00adff8c",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adff90`](#insn-00adff90)

~~~json
{
  "source": "00adff90",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adff94`](#insn-00adff94)

~~~json
{
  "source": "00adff94",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adff98`](#insn-00adff98)

~~~json
{
  "source": "00adff98",
  "target": "00adfef4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adff9c`](#insn-00adff9c)

~~~json
{
  "source": "00adff9c",
  "target": "00adfefc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae006c`](#insn-00ae006c)

~~~json
{
  "source": "00ae006c",
  "target": "00bdb090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
