# 00a0eadc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00a0ea98`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a0e/00a0ea98.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0053.md#compare-b51f45e08908c4510ca3d488a4a215eb)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00a6c954`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6c/00a6c954.md) · 移動量 `+0x5de78`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0050.md#compare-84eae8eb6af2932da5f2884e3bc4bcc9)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00a0eadc",
  "name": "_INIT_216",
  "size": 708,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "07d8c9201d45dcc25ba2cfccc8351ff12b31cc2f2810cc6a22b6074c4b8fe0df",
  "source_text_sha256": "07d8c9201d45dcc25ba2cfccc8351ff12b31cc2f2810cc6a22b6074c4b8fe0df",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00a0eadc",
        "00a0ed9b"
      ],
      [
        "00a0ee68",
        "00a0ee6b"
      ]
    ],
    "bytes_sha256": "9d77958bbb155340406f52bb7a1cdb73886574900d4e74b9c8425c65016609fe",
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

## 疑似コード / UTF-8 5539 bytes

~~~c

/* WARNING: Type propagation algorithm not settling */

void _INIT_216(void)

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
  
                    /* try { // try from 00a0eadc to 00b0eae7 has its CatchHandler @ 00a0f04c */
  lVar1 = tpidr_el0;
  local_38 = *(long *)(lVar1 + 0x28);
                    /* try { // try from 00a0eb20 to 00b0eb2b has its CatchHandler @ 00a0f040 */
  uStack_ff = 0x6741;
  local_f8[0] = 1;
  uStack_107 = (undefined7)s_CgkIjM3y_ZQaEAIQAg_002a7377._8_8_;
  cStack_100 = SUB81(s_CgkIjM3y_ZQaEAIQAg_002a7377._8_8_,7);
  local_10f = (char  [8])s_CgkIjM3y_ZQaEAIQAg_002a7377._0_8_;
  uStack_df = 0x4142;
  local_d8[0] = 2;
  uStack_e7 = (undefined7)s_CgkIjM3y_ZQaEAIQBA_002a738a._8_8_;
  cStack_e0 = SUB81(s_CgkIjM3y_ZQaEAIQBA_002a738a._8_8_,7);
                    /* try { // try from 00a0eb54 to 00b0eb5f has its CatchHandler @ 00a0f028 */
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
  DAT_0109edb8 = 0;
  DAT_0109edb0 = 0;
  DAT_0109eda8 = &DAT_0109edb0;
  FUN_00418cb8(&DAT_0109eda8,&DAT_0109edb0,local_118,local_118);
  FUN_00418cb8(&DAT_0109eda8,&DAT_0109edb0,local_f8,local_f8);
  FUN_00418cb8(&DAT_0109eda8,&DAT_0109edb0,local_d8,local_d8);
  FUN_00418cb8(&DAT_0109eda8,&DAT_0109edb0,local_b8,local_b8);
  FUN_00418cb8(&DAT_0109eda8,&DAT_0109edb0,local_98,local_98);
  FUN_00418cb8(&DAT_0109eda8,&DAT_0109edb0,local_78,local_78);
  FUN_00418cb8(&DAT_0109eda8,&DAT_0109edb0,local_58,local_58);
  if ((local_50 & 1) != 0) {
    _ZdlPv((void *)CONCAT44(uStack_3c,CONCAT13(uStack_3d,CONCAT21(uStack_3f,cStack_40))));
  }
  if ((local_70 & 1) != 0) {
    _ZdlPv((void *)CONCAT44(uStack_5c,CONCAT13(uStack_5d,CONCAT21(uStack_5f,cStack_60))));
  }
  if ((local_90 & 1) != 0) {
                    /* try { // try from 00a0ed5c to 00b0ed63 has its CatchHandler @ 00a0f06c */
    _ZdlPv((void *)CONCAT44(uStack_7c,CONCAT13(uStack_7d,CONCAT21(uStack_7f,cStack_80))));
  }
                    /* try { // try from 00a0ed64 to 00b0ee97 has its CatchHandler @ 00a0e8f0 */
  if ((local_b0 & 1) != 0) {
    _ZdlPv((void *)CONCAT44(uStack_9c,CONCAT13(uStack_9d,CONCAT21(uStack_9f,cStack_a0))));
  }
  if ((local_d0 & 1) != 0) {
    _ZdlPv((void *)CONCAT44(uStack_bc,CONCAT13(uStack_bd,CONCAT21(uStack_bf,cStack_c0))));
  }
  if ((local_f0 & 1) != 0) {
    _ZdlPv((void *)CONCAT44(uStack_dc,CONCAT13(uStack_dd,CONCAT21(uStack_df,cStack_e0))));
  }
                    /* try { // try from 00a0ecec to 00b0ecf3 has its CatchHandler @ 00a0f094 */
  if ((local_110 & 1) != 0) {
    _ZdlPv((void *)CONCAT44(uStack_fc,CONCAT13(uStack_fd,CONCAT21(uStack_ff,cStack_100))));
  }
  __cxa_atexit(FUN_00418330,&DAT_0109eda8,&PTR_LOOP_00be5fd0);
  if (*(long *)(lVar1 + 0x28) == local_38) {
                    /* try { // try from 00a0ed2c to 00b0ed33 has its CatchHandler @ 00a0f084 */
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
<a id="insn-00a0eadc"></a> `00a0eadc` | `ff 83 04 d1` | sub sp,sp,#0x120 | `FALL_THROUGH`
<a id="insn-00a0eae0"></a> `00a0eae0` | `fd 7b 0f a9` | stp x29,x30,[sp, #0xf0] | `FALL_THROUGH`
<a id="insn-00a0eae4"></a> `00a0eae4` | `fc 57 10 a9` | stp x28,x21,[sp, #0x100] | `FALL_THROUGH`
<a id="insn-00a0eae8"></a> `00a0eae8` | `f4 4f 11 a9` | stp x20,x19,[sp, #0x110] | `FALL_THROUGH`
<a id="insn-00a0eaec"></a> `00a0eaec` | `fd c3 03 91` | add x29,sp,#0xf0 | `FALL_THROUGH`
<a id="insn-00a0eaf0"></a> `00a0eaf0` | `55 d0 3b d5` | mrs x21,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00a0eaf4"></a> `00a0eaf4` | `2a e8 8c 52` | mov w10,#0x6741 | `FALL_THROUGH`
<a id="insn-00a0eaf8"></a> `00a0eaf8` | `f4 23 00 91` | add x20,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00a0eafc"></a> `00a0eafc` | `a9 16 40 f9` | ldr x9,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00a0eb00"></a> `00a0eb00` | `88 04 80 52` | mov w8,#0x24 | `FALL_THROUGH`
<a id="insn-00a0eb04"></a> `00a0eb04` | `93 34 00 90` | adrp x19,0x109e000 | `FALL_THROUGH`
<a id="insn-00a0eb08"></a> `00a0eb08` | `73 a2 36 91` | add x19,x19,#0xda8 | `FALL_THROUGH`
<a id="insn-00a0eb0c"></a> `00a0eb0c` | `a9 83 1f f8` | stur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00a0eb10"></a> `00a0eb10` | `c9 c4 ff b0` | adrp x9,0x2a7000 | `FALL_THROUGH`
<a id="insn-00a0eb14"></a> `00a0eb14` | `29 dd 0d 91` | add x9,x9,#0x377 | `FALL_THROUGH`
<a id="insn-00a0eb18"></a> `00a0eb18` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00a0eb1c"></a> `00a0eb1c` | `29 00 80 52` | mov w9,#0x1 | `FALL_THROUGH`
<a id="insn-00a0eb20"></a> `00a0eb20` | `ea 13 02 78` | sturh w10,[sp, #0x21] | `FALL_THROUGH`
<a id="insn-00a0eb24"></a> `00a0eb24` | `e9 2b 00 b9` | str w9,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00a0eb28"></a> `00a0eb28` | `49 28 88 52` | mov w9,#0x4142 | `FALL_THROUGH`
<a id="insn-00a0eb2c"></a> `00a0eb2c` | `ca c4 ff b0` | adrp x10,0x2a7000 | `FALL_THROUGH`
<a id="insn-00a0eb30"></a> `00a0eb30` | `4a 29 0e 91` | add x10,x10,#0x38a | `FALL_THROUGH`
<a id="insn-00a0eb34"></a> `00a0eb34` | `e0 13 81 3c` | stur q0,[sp, #0x11] | `FALL_THROUGH`
<a id="insn-00a0eb38"></a> `00a0eb38` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00a0eb3c"></a> `00a0eb3c` | `40 01 c0 3d` | ldr q0,[x10] | `FALL_THROUGH`
<a id="insn-00a0eb40"></a> `00a0eb40` | `e9 13 04 78` | sturh w9,[sp, #0x41] | `FALL_THROUGH`
<a id="insn-00a0eb44"></a> `00a0eb44` | `49 00 80 52` | mov w9,#0x2 | `FALL_THROUGH`
<a id="insn-00a0eb48"></a> `00a0eb48` | `e9 4b 00 b9` | str w9,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00a0eb4c"></a> `00a0eb4c` | `49 e8 8c 52` | mov w9,#0x6742 | `FALL_THROUGH`
<a id="insn-00a0eb50"></a> `00a0eb50` | `ca c4 ff d0` | adrp x10,0x2a8000 | `FALL_THROUGH`
<a id="insn-00a0eb54"></a> `00a0eb54` | `4a 81 03 91` | add x10,x10,#0xe0 | `FALL_THROUGH`
<a id="insn-00a0eb58"></a> `00a0eb58` | `e0 13 83 3c` | stur q0,[sp, #0x31] | `FALL_THROUGH`
<a id="insn-00a0eb5c"></a> `00a0eb5c` | `40 01 c0 3d` | ldr q0,[x10] | `FALL_THROUGH`
<a id="insn-00a0eb60"></a> `00a0eb60` | `e9 13 06 78` | sturh w9,[sp, #0x61] | `FALL_THROUGH`
<a id="insn-00a0eb64"></a> `00a0eb64` | `69 00 80 52` | mov w9,#0x3 | `FALL_THROUGH`
<a id="insn-00a0eb68"></a> `00a0eb68` | `e9 6b 00 b9` | str w9,[sp, #0x68] | `FALL_THROUGH`
<a id="insn-00a0eb6c"></a> `00a0eb6c` | `29 e8 8e 52` | mov w9,#0x7741 | `FALL_THROUGH`
<a id="insn-00a0eb70"></a> `00a0eb70` | `2a c4 ff b0` | adrp x10,0x293000 | `FALL_THROUGH`
<a id="insn-00a0eb74"></a> `00a0eb74` | `4a b9 1a 91` | add x10,x10,#0x6ae | `FALL_THROUGH`
<a id="insn-00a0eb78"></a> `00a0eb78` | `e0 13 85 3c` | stur q0,[sp, #0x51] | `FALL_THROUGH`
<a id="insn-00a0eb7c"></a> `00a0eb7c` | `40 01 c0 3d` | ldr q0,[x10] | `FALL_THROUGH`
<a id="insn-00a0eb80"></a> `00a0eb80` | `e9 13 08 78` | sturh w9,[sp, #0x81] | `FALL_THROUGH`
<a id="insn-00a0eb84"></a> `00a0eb84` | `89 00 80 52` | mov w9,#0x4 | `FALL_THROUGH`
<a id="insn-00a0eb88"></a> `00a0eb88` | `e9 8b 00 b9` | str w9,[sp, #0x88] | `FALL_THROUGH`
<a id="insn-00a0eb8c"></a> `00a0eb8c` | `69 c4 ff d0` | adrp x9,0x29c000 | `FALL_THROUGH`
<a id="insn-00a0eb90"></a> `00a0eb90` | `29 b1 0d 91` | add x9,x9,#0x36c | `FALL_THROUGH`
<a id="insn-00a0eb94"></a> `00a0eb94` | `e0 13 87 3c` | stur q0,[sp, #0x71] | `FALL_THROUGH`
<a id="insn-00a0eb98"></a> `00a0eb98` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00a0eb9c"></a> `00a0eb9c` | `49 28 8a 52` | mov w9,#0x5142 | `FALL_THROUGH`
<a id="insn-00a0eba0"></a> `00a0eba0` | `89 92 09 78` | sturh w9,[x20, #0x99] | `FALL_THROUGH`
<a id="insn-00a0eba4"></a> `00a0eba4` | `a9 00 80 52` | mov w9,#0x5 | `FALL_THROUGH`
<a id="insn-00a0eba8"></a> `00a0eba8` | `e9 ab 00 b9` | str w9,[sp, #0xa8] | `FALL_THROUGH`
<a id="insn-00a0ebac"></a> `00a0ebac` | `09 c4 ff f0` | adrp x9,0x291000 | `FALL_THROUGH`
<a id="insn-00a0ebb0"></a> `00a0ebb0` | `29 dd 21 91` | add x9,x9,#0x877 | `FALL_THROUGH`
<a id="insn-00a0ebb4"></a> `00a0ebb4` | `80 92 88 3c` | stur q0,[x20, #0x89] | `FALL_THROUGH`
<a id="insn-00a0ebb8"></a> `00a0ebb8` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00a0ebbc"></a> `00a0ebbc` | `49 e8 8e 52` | mov w9,#0x7742 | `FALL_THROUGH`
<a id="insn-00a0ebc0"></a> `00a0ebc0` | `89 92 0b 78` | sturh w9,[x20, #0xb9] | `FALL_THROUGH`
<a id="insn-00a0ebc4"></a> `00a0ebc4` | `c9 00 80 52` | mov w9,#0x6 | `FALL_THROUGH`
<a id="insn-00a0ebc8"></a> `00a0ebc8` | `e9 cb 00 b9` | str w9,[sp, #0xc8] | `FALL_THROUGH`
<a id="insn-00a0ebcc"></a> `00a0ebcc` | `29 c4 ff d0` | adrp x9,0x294000 | `FALL_THROUGH`
<a id="insn-00a0ebd0"></a> `00a0ebd0` | `29 99 14 91` | add x9,x9,#0x526 | `FALL_THROUGH`
<a id="insn-00a0ebd4"></a> `00a0ebd4` | `80 92 8a 3c` | stur q0,[x20, #0xa9] | `FALL_THROUGH`
<a id="insn-00a0ebd8"></a> `00a0ebd8` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00a0ebdc"></a> `00a0ebdc` | `e8 43 00 39` | strb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a0ebe0"></a> `00a0ebe0` | `e8 c3 00 39` | strb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00a0ebe4"></a> `00a0ebe4` | `e8 43 01 39` | strb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00a0ebe8"></a> `00a0ebe8` | `e8 c3 01 39` | strb w8,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00a0ebec"></a> `00a0ebec` | `e8 43 02 39` | strb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00a0ebf0"></a> `00a0ebf0` | `e8 c3 02 39` | strb w8,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00a0ebf4"></a> `00a0ebf4` | `e8 43 03 39` | strb w8,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-00a0ebf8"></a> `00a0ebf8` | `68 28 88 52` | mov w8,#0x4143 | `FALL_THROUGH`
<a id="insn-00a0ebfc"></a> `00a0ebfc` | `ff 0b 00 b9` | str wzr,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00a0ec00"></a> `00a0ec00` | `ff 8f 00 39` | strb wzr,[sp, #0x23] | `FALL_THROUGH`
<a id="insn-00a0ec04"></a> `00a0ec04` | `ff 0f 01 39` | strb wzr,[sp, #0x43] | `FALL_THROUGH`
<a id="insn-00a0ec08"></a> `00a0ec08` | `ff 8f 01 39` | strb wzr,[sp, #0x63] | `FALL_THROUGH`
<a id="insn-00a0ec0c"></a> `00a0ec0c` | `ff 0f 02 39` | strb wzr,[sp, #0x83] | `FALL_THROUGH`
<a id="insn-00a0ec10"></a> `00a0ec10` | `ff 8f 02 39` | strb wzr,[sp, #0xa3] | `FALL_THROUGH`
<a id="insn-00a0ec14"></a> `00a0ec14` | `ff 0f 03 39` | strb wzr,[sp, #0xc3] | `FALL_THROUGH`
<a id="insn-00a0ec18"></a> `00a0ec18` | `88 92 0d 78` | sturh w8,[x20, #0xd9] | `FALL_THROUGH`
<a id="insn-00a0ec1c"></a> `00a0ec1c` | `80 92 8c 3c` | stur q0,[x20, #0xc9] | `FALL_THROUGH`
<a id="insn-00a0ec20"></a> `00a0ec20` | `ff 8f 03 39` | strb wzr,[sp, #0xe3] | `FALL_THROUGH`
<a id="insn-00a0ec24"></a> `00a0ec24` | `7f 0a 00 f9` | str xzr,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00a0ec28"></a> `00a0ec28` | `3f 8c 00 f8` | str xzr,[x1, #0x8]! | `FALL_THROUGH`
<a id="insn-00a0ec2c"></a> `00a0ec2c` | `61 02 00 f9` | str x1,[x19] | `FALL_THROUGH`
<a id="insn-00a0ec30"></a> `00a0ec30` | `e2 23 00 91` | add x2,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00a0ec34"></a> `00a0ec34` | `e3 23 00 91` | add x3,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00a0ec38"></a> `00a0ec38` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00a0ec3c"></a> `00a0ec3c` | `1f 28 e8 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-00a0ec40"></a> `00a0ec40` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00a0ec44"></a> `00a0ec44` | `82 82 00 91` | add x2,x20,#0x20 | `FALL_THROUGH`
<a id="insn-00a0ec48"></a> `00a0ec48` | `83 82 00 91` | add x3,x20,#0x20 | `FALL_THROUGH`
<a id="insn-00a0ec4c"></a> `00a0ec4c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00a0ec50"></a> `00a0ec50` | `1a 28 e8 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-00a0ec54"></a> `00a0ec54` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00a0ec58"></a> `00a0ec58` | `82 02 01 91` | add x2,x20,#0x40 | `FALL_THROUGH`
<a id="insn-00a0ec5c"></a> `00a0ec5c` | `83 02 01 91` | add x3,x20,#0x40 | `FALL_THROUGH`
<a id="insn-00a0ec60"></a> `00a0ec60` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00a0ec64"></a> `00a0ec64` | `15 28 e8 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-00a0ec68"></a> `00a0ec68` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00a0ec6c"></a> `00a0ec6c` | `82 82 01 91` | add x2,x20,#0x60 | `FALL_THROUGH`
<a id="insn-00a0ec70"></a> `00a0ec70` | `83 82 01 91` | add x3,x20,#0x60 | `FALL_THROUGH`
<a id="insn-00a0ec74"></a> `00a0ec74` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00a0ec78"></a> `00a0ec78` | `10 28 e8 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-00a0ec7c"></a> `00a0ec7c` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00a0ec80"></a> `00a0ec80` | `82 02 02 91` | add x2,x20,#0x80 | `FALL_THROUGH`
<a id="insn-00a0ec84"></a> `00a0ec84` | `83 02 02 91` | add x3,x20,#0x80 | `FALL_THROUGH`
<a id="insn-00a0ec88"></a> `00a0ec88` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00a0ec8c"></a> `00a0ec8c` | `0b 28 e8 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-00a0ec90"></a> `00a0ec90` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00a0ec94"></a> `00a0ec94` | `82 82 02 91` | add x2,x20,#0xa0 | `FALL_THROUGH`
<a id="insn-00a0ec98"></a> `00a0ec98` | `83 82 02 91` | add x3,x20,#0xa0 | `FALL_THROUGH`
<a id="insn-00a0ec9c"></a> `00a0ec9c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00a0eca0"></a> `00a0eca0` | `06 28 e8 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-00a0eca4"></a> `00a0eca4` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00a0eca8"></a> `00a0eca8` | `82 02 03 91` | add x2,x20,#0xc0 | `FALL_THROUGH`
<a id="insn-00a0ecac"></a> `00a0ecac` | `83 02 03 91` | add x3,x20,#0xc0 | `FALL_THROUGH`
<a id="insn-00a0ecb0"></a> `00a0ecb0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00a0ecb4"></a> `00a0ecb4` | `01 28 e8 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-00a0ecb8"></a> `00a0ecb8` | `e8 43 43 39` | ldrb w8,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-00a0ecbc"></a> `00a0ecbc` | `e8 03 00 37` | tbnz w8,#0x0,0x00a0ed38 | `CONDITIONAL_JUMP`
<a id="insn-00a0ecc0"></a> `00a0ecc0` | `e8 c3 42 39` | ldrb w8,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00a0ecc4"></a> `00a0ecc4` | `28 04 00 37` | tbnz w8,#0x0,0x00a0ed48 | `CONDITIONAL_JUMP`
<a id="insn-00a0ecc8"></a> `00a0ecc8` | `e8 43 42 39` | ldrb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00a0eccc"></a> `00a0eccc` | `68 04 00 37` | tbnz w8,#0x0,0x00a0ed58 | `CONDITIONAL_JUMP`
<a id="insn-00a0ecd0"></a> `00a0ecd0` | `e8 c3 41 39` | ldrb w8,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00a0ecd4"></a> `00a0ecd4` | `a8 04 00 37` | tbnz w8,#0x0,0x00a0ed68 | `CONDITIONAL_JUMP`
<a id="insn-00a0ecd8"></a> `00a0ecd8` | `e8 43 41 39` | ldrb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00a0ecdc"></a> `00a0ecdc` | `e8 04 00 37` | tbnz w8,#0x0,0x00a0ed78 | `CONDITIONAL_JUMP`
<a id="insn-00a0ece0"></a> `00a0ece0` | `e8 c3 40 39` | ldrb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00a0ece4"></a> `00a0ece4` | `28 05 00 37` | tbnz w8,#0x0,0x00a0ed88 | `CONDITIONAL_JUMP`
<a id="insn-00a0ece8"></a> `00a0ece8` | `e8 43 40 39` | ldrb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a0ecec"></a> `00a0ecec` | `68 00 00 36` | tbz w8,#0x0,0x00a0ecf8 | `CONDITIONAL_JUMP`
<a id="insn-00a0ecf0"></a> `00a0ecf0` | `e0 13 40 f9` | ldr x0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00a0ecf4"></a> `00a0ecf4` | `db 30 07 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00a0ecf8"></a> `00a0ecf8` | `40 d0 ff d0` | adrp x0,0x418000 | `FALL_THROUGH`
<a id="insn-00a0ecfc"></a> `00a0ecfc` | `00 c0 0c 91` | add x0,x0,#0x330 | `FALL_THROUGH`
<a id="insn-00a0ed00"></a> `00a0ed00` | `81 34 00 90` | adrp x1,0x109e000 | `FALL_THROUGH`
<a id="insn-00a0ed04"></a> `00a0ed04` | `21 a0 36 91` | add x1,x1,#0xda8 | `FALL_THROUGH`
<a id="insn-00a0ed08"></a> `00a0ed08` | `a2 0e 00 f0` | adrp x2,0xbe5000 | `FALL_THROUGH`
<a id="insn-00a0ed0c"></a> `00a0ed0c` | `42 40 3f 91` | add x2,x2,#0xfd0 | `FALL_THROUGH`
<a id="insn-00a0ed10"></a> `00a0ed10` | `b4 30 07 94` | bl 0x00bdafe0 | `UNCONDITIONAL_CALL`
<a id="insn-00a0ed14"></a> `00a0ed14` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00a0ed18"></a> `00a0ed18` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00a0ed1c"></a> `00a0ed1c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00a0ed20"></a> `00a0ed20` | `41 0a 00 54` | b.ne 0x00a0ee68 | `CONDITIONAL_JUMP`
<a id="insn-00a0ed24"></a> `00a0ed24` | `f4 4f 51 a9` | ldp x20,x19,[sp, #0x110] | `FALL_THROUGH`
<a id="insn-00a0ed28"></a> `00a0ed28` | `fc 57 50 a9` | ldp x28,x21,[sp, #0x100] | `FALL_THROUGH`
<a id="insn-00a0ed2c"></a> `00a0ed2c` | `fd 7b 4f a9` | ldp x29,x30,[sp, #0xf0] | `FALL_THROUGH`
<a id="insn-00a0ed30"></a> `00a0ed30` | `ff 83 04 91` | add sp,sp,#0x120 | `FALL_THROUGH`
<a id="insn-00a0ed34"></a> `00a0ed34` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00a0ed38"></a> `00a0ed38` | `e0 73 40 f9` | ldr x0,[sp, #0xe0] | `FALL_THROUGH`
<a id="insn-00a0ed3c"></a> `00a0ed3c` | `c9 30 07 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00a0ed40"></a> `00a0ed40` | `e8 c3 42 39` | ldrb w8,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00a0ed44"></a> `00a0ed44` | `28 fc 07 36` | tbz w8,#0x0,0x00a0ecc8 | `CONDITIONAL_JUMP`
<a id="insn-00a0ed48"></a> `00a0ed48` | `e0 63 40 f9` | ldr x0,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00a0ed4c"></a> `00a0ed4c` | `c5 30 07 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00a0ed50"></a> `00a0ed50` | `e8 43 42 39` | ldrb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00a0ed54"></a> `00a0ed54` | `e8 fb 07 36` | tbz w8,#0x0,0x00a0ecd0 | `CONDITIONAL_JUMP`
<a id="insn-00a0ed58"></a> `00a0ed58` | `e0 53 40 f9` | ldr x0,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00a0ed5c"></a> `00a0ed5c` | `c1 30 07 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00a0ed60"></a> `00a0ed60` | `e8 c3 41 39` | ldrb w8,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00a0ed64"></a> `00a0ed64` | `a8 fb 07 36` | tbz w8,#0x0,0x00a0ecd8 | `CONDITIONAL_JUMP`
<a id="insn-00a0ed68"></a> `00a0ed68` | `e0 43 40 f9` | ldr x0,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00a0ed6c"></a> `00a0ed6c` | `bd 30 07 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00a0ed70"></a> `00a0ed70` | `e8 43 41 39` | ldrb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00a0ed74"></a> `00a0ed74` | `68 fb 07 36` | tbz w8,#0x0,0x00a0ece0 | `CONDITIONAL_JUMP`
<a id="insn-00a0ed78"></a> `00a0ed78` | `e0 33 40 f9` | ldr x0,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00a0ed7c"></a> `00a0ed7c` | `b9 30 07 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00a0ed80"></a> `00a0ed80` | `e8 c3 40 39` | ldrb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00a0ed84"></a> `00a0ed84` | `28 fb 07 36` | tbz w8,#0x0,0x00a0ece8 | `CONDITIONAL_JUMP`
<a id="insn-00a0ed88"></a> `00a0ed88` | `e0 23 40 f9` | ldr x0,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00a0ed8c"></a> `00a0ed8c` | `b5 30 07 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00a0ed90"></a> `00a0ed90` | `e8 43 40 39` | ldrb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a0ed94"></a> `00a0ed94` | `e8 fa 07 37` | tbnz w8,#0x0,0x00a0ecf0 | `CONDITIONAL_JUMP`
<a id="insn-00a0ed98"></a> `00a0ed98` | `d8 ff ff 17` | b 0x00a0ecf8 | `UNCONDITIONAL_JUMP`
<a id="insn-00a0ee68"></a> `00a0ee68` | `8a 30 07 94` | bl 0x00bdb090 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00a0eadc`](#insn-00a0eadc) 範囲 `[['00a0eadc', '00a0eb1f']]`
  - `FALL_THROUGH` [`00a0eb1c`](#insn-00a0eb1c) → [`00a0eb20`](#insn-00a0eb20)
- ブロック [`00a0eb20`](#insn-00a0eb20) 範囲 `[['00a0eb20', '00a0eb53']]`
  - `FALL_THROUGH` [`00a0eb50`](#insn-00a0eb50) → [`00a0eb54`](#insn-00a0eb54)
- ブロック [`00a0eb54`](#insn-00a0eb54) 範囲 `[['00a0eb54', '00a0ecbf']]`
  - `CONDITIONAL_JUMP` [`00a0ecbc`](#insn-00a0ecbc) → [`00a0ed38`](#insn-00a0ed38)
  - `FALL_THROUGH` [`00a0ecbc`](#insn-00a0ecbc) → [`00a0ecc0`](#insn-00a0ecc0)
- ブロック [`00a0ecc0`](#insn-00a0ecc0) 範囲 `[['00a0ecc0', '00a0ecc3']]`
  - `FALL_THROUGH` [`00a0ecc0`](#insn-00a0ecc0) → [`00a0ecc4`](#insn-00a0ecc4)
- ブロック [`00a0ecc4`](#insn-00a0ecc4) 範囲 `[['00a0ecc4', '00a0ecc7']]`
  - `CONDITIONAL_JUMP` [`00a0ecc4`](#insn-00a0ecc4) → [`00a0ed48`](#insn-00a0ed48)
  - `FALL_THROUGH` [`00a0ecc4`](#insn-00a0ecc4) → [`00a0ecc8`](#insn-00a0ecc8)
- ブロック [`00a0ecc8`](#insn-00a0ecc8) 範囲 `[['00a0ecc8', '00a0eccf']]`
  - `CONDITIONAL_JUMP` [`00a0eccc`](#insn-00a0eccc) → [`00a0ed58`](#insn-00a0ed58)
  - `FALL_THROUGH` [`00a0eccc`](#insn-00a0eccc) → [`00a0ecd0`](#insn-00a0ecd0)
- ブロック [`00a0ecd0`](#insn-00a0ecd0) 範囲 `[['00a0ecd0', '00a0ecd7']]`
  - `CONDITIONAL_JUMP` [`00a0ecd4`](#insn-00a0ecd4) → [`00a0ed68`](#insn-00a0ed68)
  - `FALL_THROUGH` [`00a0ecd4`](#insn-00a0ecd4) → [`00a0ecd8`](#insn-00a0ecd8)
- ブロック [`00a0ecd8`](#insn-00a0ecd8) 範囲 `[['00a0ecd8', '00a0ecdf']]`
  - `CONDITIONAL_JUMP` [`00a0ecdc`](#insn-00a0ecdc) → [`00a0ed78`](#insn-00a0ed78)
  - `FALL_THROUGH` [`00a0ecdc`](#insn-00a0ecdc) → [`00a0ece0`](#insn-00a0ece0)
- ブロック [`00a0ece0`](#insn-00a0ece0) 範囲 `[['00a0ece0', '00a0ece7']]`
  - `CONDITIONAL_JUMP` [`00a0ece4`](#insn-00a0ece4) → [`00a0ed88`](#insn-00a0ed88)
  - `FALL_THROUGH` [`00a0ece4`](#insn-00a0ece4) → [`00a0ece8`](#insn-00a0ece8)
- ブロック [`00a0ece8`](#insn-00a0ece8) 範囲 `[['00a0ece8', '00a0eceb']]`
  - `FALL_THROUGH` [`00a0ece8`](#insn-00a0ece8) → [`00a0ecec`](#insn-00a0ecec)
- ブロック [`00a0ecec`](#insn-00a0ecec) 範囲 `[['00a0ecec', '00a0ecef']]`
  - `CONDITIONAL_JUMP` [`00a0ecec`](#insn-00a0ecec) → [`00a0ecf8`](#insn-00a0ecf8)
  - `FALL_THROUGH` [`00a0ecec`](#insn-00a0ecec) → [`00a0ecf0`](#insn-00a0ecf0)
- ブロック [`00a0ecf0`](#insn-00a0ecf0) 範囲 `[['00a0ecf0', '00a0ecf7']]`
  - `FALL_THROUGH` [`00a0ecf4`](#insn-00a0ecf4) → [`00a0ecf8`](#insn-00a0ecf8)
- ブロック [`00a0ecf8`](#insn-00a0ecf8) 範囲 `[['00a0ecf8', '00a0ed23']]`
  - `CONDITIONAL_JUMP` [`00a0ed20`](#insn-00a0ed20) → [`00a0ee68`](#insn-00a0ee68)
  - `FALL_THROUGH` [`00a0ed20`](#insn-00a0ed20) → [`00a0ed24`](#insn-00a0ed24)
- ブロック [`00a0ed24`](#insn-00a0ed24) 範囲 `[['00a0ed24', '00a0ed2b']]`
  - `FALL_THROUGH` [`00a0ed28`](#insn-00a0ed28) → [`00a0ed2c`](#insn-00a0ed2c)
- ブロック [`00a0ed2c`](#insn-00a0ed2c) 範囲 `[['00a0ed2c', '00a0ed37']]`
- ブロック [`00a0ed38`](#insn-00a0ed38) 範囲 `[['00a0ed38', '00a0ed47']]`
  - `CONDITIONAL_JUMP` [`00a0ed44`](#insn-00a0ed44) → [`00a0ecc8`](#insn-00a0ecc8)
  - `FALL_THROUGH` [`00a0ed44`](#insn-00a0ed44) → [`00a0ed48`](#insn-00a0ed48)
- ブロック [`00a0ed48`](#insn-00a0ed48) 範囲 `[['00a0ed48', '00a0ed57']]`
  - `CONDITIONAL_JUMP` [`00a0ed54`](#insn-00a0ed54) → [`00a0ecd0`](#insn-00a0ecd0)
  - `FALL_THROUGH` [`00a0ed54`](#insn-00a0ed54) → [`00a0ed58`](#insn-00a0ed58)
- ブロック [`00a0ed58`](#insn-00a0ed58) 範囲 `[['00a0ed58', '00a0ed5b']]`
  - `FALL_THROUGH` [`00a0ed58`](#insn-00a0ed58) → [`00a0ed5c`](#insn-00a0ed5c)
- ブロック [`00a0ed5c`](#insn-00a0ed5c) 範囲 `[['00a0ed5c', '00a0ed63']]`
  - `FALL_THROUGH` [`00a0ed60`](#insn-00a0ed60) → [`00a0ed64`](#insn-00a0ed64)
- ブロック [`00a0ed64`](#insn-00a0ed64) 範囲 `[['00a0ed64', '00a0ed67']]`
  - `CONDITIONAL_JUMP` [`00a0ed64`](#insn-00a0ed64) → [`00a0ecd8`](#insn-00a0ecd8)
  - `FALL_THROUGH` [`00a0ed64`](#insn-00a0ed64) → [`00a0ed68`](#insn-00a0ed68)
- ブロック [`00a0ed68`](#insn-00a0ed68) 範囲 `[['00a0ed68', '00a0ed77']]`
  - `CONDITIONAL_JUMP` [`00a0ed74`](#insn-00a0ed74) → [`00a0ece0`](#insn-00a0ece0)
  - `FALL_THROUGH` [`00a0ed74`](#insn-00a0ed74) → [`00a0ed78`](#insn-00a0ed78)
- ブロック [`00a0ed78`](#insn-00a0ed78) 範囲 `[['00a0ed78', '00a0ed87']]`
  - `CONDITIONAL_JUMP` [`00a0ed84`](#insn-00a0ed84) → [`00a0ece8`](#insn-00a0ece8)
  - `FALL_THROUGH` [`00a0ed84`](#insn-00a0ed84) → [`00a0ed88`](#insn-00a0ed88)
- ブロック [`00a0ed88`](#insn-00a0ed88) 範囲 `[['00a0ed88', '00a0ed97']]`
  - `CONDITIONAL_JUMP` [`00a0ed94`](#insn-00a0ed94) → [`00a0ecf0`](#insn-00a0ecf0)
  - `FALL_THROUGH` [`00a0ed94`](#insn-00a0ed94) → [`00a0ed98`](#insn-00a0ed98)
- ブロック [`00a0ed98`](#insn-00a0ed98) 範囲 `[['00a0ed98', '00a0ed9b']]`
  - `UNCONDITIONAL_JUMP` [`00a0ed98`](#insn-00a0ed98) → [`00a0ecf8`](#insn-00a0ecf8)
- ブロック [`00a0ee68`](#insn-00a0ee68) 範囲 `[['00a0ee68', '00a0ee6b']]`

## 命令位置別の参照

- [`00a0eae0`](#insn-00a0eae0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0eae4`](#insn-00a0eae4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0eae8`](#insn-00a0eae8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0eb0c`](#insn-00a0eb0c) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0eb18`](#insn-00a0eb18) → `002a7377`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00a0eb20`](#insn-00a0eb20) → `Stack[-0xff]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0eb24`](#insn-00a0eb24) → `Stack[-0xf8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0eb34`](#insn-00a0eb34) → `Stack[-0x10f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0eb3c`](#insn-00a0eb3c) → `002a738a`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00a0eb40`](#insn-00a0eb40) → `Stack[-0xdf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0eb48`](#insn-00a0eb48) → `Stack[-0xd8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0eb58`](#insn-00a0eb58) → `Stack[-0xef]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0eb5c`](#insn-00a0eb5c) → `002a80e0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00a0eb60`](#insn-00a0eb60) → `Stack[-0xbf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0eb68`](#insn-00a0eb68) → `Stack[-0xb8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0eb78`](#insn-00a0eb78) → `Stack[-0xcf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0eb7c`](#insn-00a0eb7c) → `002936ae`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00a0eb80`](#insn-00a0eb80) → `Stack[-0x9f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0eb88`](#insn-00a0eb88) → `Stack[-0x98]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0eb94`](#insn-00a0eb94) → `Stack[-0xaf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0eb98`](#insn-00a0eb98) → `0029c36c`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00a0eba0`](#insn-00a0eba0) → `Stack[-0x7f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0eba8`](#insn-00a0eba8) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ebb4`](#insn-00a0ebb4) → `Stack[-0x8f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ebb8`](#insn-00a0ebb8) → `00291877`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00a0ebc0`](#insn-00a0ebc0) → `Stack[-0x5f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ebc8`](#insn-00a0ebc8) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ebd4`](#insn-00a0ebd4) → `Stack[-0x6f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ebd8`](#insn-00a0ebd8) → `00294526`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00a0ebdc`](#insn-00a0ebdc) → `Stack[-0x110]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ebe0`](#insn-00a0ebe0) → `Stack[-0xf0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ebe4`](#insn-00a0ebe4) → `Stack[-0xd0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ebe8`](#insn-00a0ebe8) → `Stack[-0xb0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ebec`](#insn-00a0ebec) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ebf0`](#insn-00a0ebf0) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ebf4`](#insn-00a0ebf4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ebfc`](#insn-00a0ebfc) → `Stack[-0x118]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ec00`](#insn-00a0ec00) → `Stack[-0xfd]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ec04`](#insn-00a0ec04) → `Stack[-0xdd]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ec08`](#insn-00a0ec08) → `Stack[-0xbd]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ec0c`](#insn-00a0ec0c) → `Stack[-0x9d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ec10`](#insn-00a0ec10) → `Stack[-0x7d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ec14`](#insn-00a0ec14) → `Stack[-0x5d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ec18`](#insn-00a0ec18) → `Stack[-0x3f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ec1c`](#insn-00a0ec1c) → `Stack[-0x4f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ec20`](#insn-00a0ec20) → `Stack[-0x3d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ec24`](#insn-00a0ec24) → `0109edb8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a0ec28`](#insn-00a0ec28) → `0109edb0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a0ec2c`](#insn-00a0ec2c) → `0109eda8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a0ec2c`](#insn-00a0ec2c) → `0109edb0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a0ec38`](#insn-00a0ec38) → `0109eda8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a0ec3c`](#insn-00a0ec3c) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`00a0ec40`](#insn-00a0ec40) → `0109edb0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a0ec4c`](#insn-00a0ec4c) → `0109eda8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a0ec50`](#insn-00a0ec50) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`00a0ec54`](#insn-00a0ec54) → `0109edb0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a0ec60`](#insn-00a0ec60) → `0109eda8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a0ec64`](#insn-00a0ec64) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`00a0ec68`](#insn-00a0ec68) → `0109edb0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a0ec74`](#insn-00a0ec74) → `0109eda8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a0ec78`](#insn-00a0ec78) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`00a0ec7c`](#insn-00a0ec7c) → `0109edb0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a0ec88`](#insn-00a0ec88) → `0109eda8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a0ec8c`](#insn-00a0ec8c) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`00a0ec90`](#insn-00a0ec90) → `0109edb0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a0ec9c`](#insn-00a0ec9c) → `0109eda8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a0eca0`](#insn-00a0eca0) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`00a0eca4`](#insn-00a0eca4) → `0109edb0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a0ecb0`](#insn-00a0ecb0) → `0109eda8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a0ecb4`](#insn-00a0ecb4) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`00a0ecb8`](#insn-00a0ecb8) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ecbc`](#insn-00a0ecbc) → [`00a0ed38`](#insn-00a0ed38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ecc0`](#insn-00a0ecc0) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ecc4`](#insn-00a0ecc4) → [`00a0ed48`](#insn-00a0ed48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ecc8`](#insn-00a0ecc8) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0eccc`](#insn-00a0eccc) → [`00a0ed58`](#insn-00a0ed58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ecd0`](#insn-00a0ecd0) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ecd4`](#insn-00a0ecd4) → [`00a0ed68`](#insn-00a0ed68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ecd8`](#insn-00a0ecd8) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ecdc`](#insn-00a0ecdc) → [`00a0ed78`](#insn-00a0ed78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ece0`](#insn-00a0ece0) → `Stack[-0xf0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ece4`](#insn-00a0ece4) → [`00a0ed88`](#insn-00a0ed88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ece8`](#insn-00a0ece8) → `Stack[-0x110]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ecec`](#insn-00a0ecec) → [`00a0ecf8`](#insn-00a0ecf8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ecf0`](#insn-00a0ecf0) → `Stack[-0x100]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ecf4`](#insn-00a0ecf4) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00a0ecfc`](#insn-00a0ecfc) → [`00418330`](../00418/00418330.md) · `PARAM` · `ANALYSIS` · 関数 `00418330` · 推定シンボル `None` · 推定型 `None`
- [`00a0ed04`](#insn-00a0ed04) → `0109eda8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a0ed0c`](#insn-00a0ed0c) → `00be5fd0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00a0ed10`](#insn-00a0ed10) → [`00bdafe0`](../00bda/00bdafe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdafe0` · 推定シンボル `None` · 推定型 `None`
- [`00a0ed18`](#insn-00a0ed18) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ed20`](#insn-00a0ed20) → [`00a0ee68`](#insn-00a0ee68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ed24`](#insn-00a0ed24) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ed28`](#insn-00a0ed28) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ed2c`](#insn-00a0ed2c) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ed38`](#insn-00a0ed38) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ed3c`](#insn-00a0ed3c) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00a0ed40`](#insn-00a0ed40) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ed44`](#insn-00a0ed44) → [`00a0ecc8`](#insn-00a0ecc8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ed48`](#insn-00a0ed48) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ed4c`](#insn-00a0ed4c) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00a0ed50`](#insn-00a0ed50) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ed54`](#insn-00a0ed54) → [`00a0ecd0`](#insn-00a0ecd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ed58`](#insn-00a0ed58) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ed5c`](#insn-00a0ed5c) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00a0ed60`](#insn-00a0ed60) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ed64`](#insn-00a0ed64) → [`00a0ecd8`](#insn-00a0ecd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ed68`](#insn-00a0ed68) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ed6c`](#insn-00a0ed6c) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00a0ed70`](#insn-00a0ed70) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ed74`](#insn-00a0ed74) → [`00a0ece0`](#insn-00a0ece0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ed78`](#insn-00a0ed78) → `Stack[-0xc0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ed7c`](#insn-00a0ed7c) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00a0ed80`](#insn-00a0ed80) → `Stack[-0xf0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ed84`](#insn-00a0ed84) → [`00a0ece8`](#insn-00a0ece8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ed88`](#insn-00a0ed88) → `Stack[-0xe0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ed8c`](#insn-00a0ed8c) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00a0ed90`](#insn-00a0ed90) → `Stack[-0x110]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ed94`](#insn-00a0ed94) → [`00a0ecf0`](#insn-00a0ecf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ed98`](#insn-00a0ed98) → [`00a0ecf8`](#insn-00a0ecf8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ee68`](#insn-00a0ee68) → [`00bdb090`](../00bdb/00bdb090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb090` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00a0eae0`](#insn-00a0eae0)

~~~json
{
  "source": "00a0eae0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0eae4`](#insn-00a0eae4)

~~~json
{
  "source": "00a0eae4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0eae8`](#insn-00a0eae8)

~~~json
{
  "source": "00a0eae8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0eb0c`](#insn-00a0eb0c)

~~~json
{
  "source": "00a0eb0c",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0eb18`](#insn-00a0eb18)

~~~json
{
  "source": "00a0eb18",
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
- 参照命令 [`00a0eb20`](#insn-00a0eb20)

~~~json
{
  "source": "00a0eb20",
  "target": "Stack[-0xff]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0eb24`](#insn-00a0eb24)

~~~json
{
  "source": "00a0eb24",
  "target": "Stack[-0xf8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0eb34`](#insn-00a0eb34)

~~~json
{
  "source": "00a0eb34",
  "target": "Stack[-0x10f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0eb3c`](#insn-00a0eb3c)

~~~json
{
  "source": "00a0eb3c",
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
- 参照命令 [`00a0eb40`](#insn-00a0eb40)

~~~json
{
  "source": "00a0eb40",
  "target": "Stack[-0xdf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0eb48`](#insn-00a0eb48)

~~~json
{
  "source": "00a0eb48",
  "target": "Stack[-0xd8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0eb58`](#insn-00a0eb58)

~~~json
{
  "source": "00a0eb58",
  "target": "Stack[-0xef]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0eb5c`](#insn-00a0eb5c)

~~~json
{
  "source": "00a0eb5c",
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
- 参照命令 [`00a0eb60`](#insn-00a0eb60)

~~~json
{
  "source": "00a0eb60",
  "target": "Stack[-0xbf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0eb68`](#insn-00a0eb68)

~~~json
{
  "source": "00a0eb68",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0eb78`](#insn-00a0eb78)

~~~json
{
  "source": "00a0eb78",
  "target": "Stack[-0xcf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0eb7c`](#insn-00a0eb7c)

~~~json
{
  "source": "00a0eb7c",
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
- 参照命令 [`00a0eb80`](#insn-00a0eb80)

~~~json
{
  "source": "00a0eb80",
  "target": "Stack[-0x9f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0eb88`](#insn-00a0eb88)

~~~json
{
  "source": "00a0eb88",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0eb94`](#insn-00a0eb94)

~~~json
{
  "source": "00a0eb94",
  "target": "Stack[-0xaf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0eb98`](#insn-00a0eb98)

~~~json
{
  "source": "00a0eb98",
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
- 参照命令 [`00a0eba0`](#insn-00a0eba0)

~~~json
{
  "source": "00a0eba0",
  "target": "Stack[-0x7f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0eba8`](#insn-00a0eba8)

~~~json
{
  "source": "00a0eba8",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ebb4`](#insn-00a0ebb4)

~~~json
{
  "source": "00a0ebb4",
  "target": "Stack[-0x8f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ebb8`](#insn-00a0ebb8)

~~~json
{
  "source": "00a0ebb8",
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
- 参照命令 [`00a0ebc0`](#insn-00a0ebc0)

~~~json
{
  "source": "00a0ebc0",
  "target": "Stack[-0x5f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ebc8`](#insn-00a0ebc8)

~~~json
{
  "source": "00a0ebc8",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ebd4`](#insn-00a0ebd4)

~~~json
{
  "source": "00a0ebd4",
  "target": "Stack[-0x6f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ebd8`](#insn-00a0ebd8)

~~~json
{
  "source": "00a0ebd8",
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
- 参照命令 [`00a0ebdc`](#insn-00a0ebdc)

~~~json
{
  "source": "00a0ebdc",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ebe0`](#insn-00a0ebe0)

~~~json
{
  "source": "00a0ebe0",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ebe4`](#insn-00a0ebe4)

~~~json
{
  "source": "00a0ebe4",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ebe8`](#insn-00a0ebe8)

~~~json
{
  "source": "00a0ebe8",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ebec`](#insn-00a0ebec)

~~~json
{
  "source": "00a0ebec",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ebf0`](#insn-00a0ebf0)

~~~json
{
  "source": "00a0ebf0",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ebf4`](#insn-00a0ebf4)

~~~json
{
  "source": "00a0ebf4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ebfc`](#insn-00a0ebfc)

~~~json
{
  "source": "00a0ebfc",
  "target": "Stack[-0x118]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ec00`](#insn-00a0ec00)

~~~json
{
  "source": "00a0ec00",
  "target": "Stack[-0xfd]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ec04`](#insn-00a0ec04)

~~~json
{
  "source": "00a0ec04",
  "target": "Stack[-0xdd]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ec08`](#insn-00a0ec08)

~~~json
{
  "source": "00a0ec08",
  "target": "Stack[-0xbd]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ec0c`](#insn-00a0ec0c)

~~~json
{
  "source": "00a0ec0c",
  "target": "Stack[-0x9d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ec10`](#insn-00a0ec10)

~~~json
{
  "source": "00a0ec10",
  "target": "Stack[-0x7d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ec14`](#insn-00a0ec14)

~~~json
{
  "source": "00a0ec14",
  "target": "Stack[-0x5d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ec18`](#insn-00a0ec18)

~~~json
{
  "source": "00a0ec18",
  "target": "Stack[-0x3f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ec1c`](#insn-00a0ec1c)

~~~json
{
  "source": "00a0ec1c",
  "target": "Stack[-0x4f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ec20`](#insn-00a0ec20)

~~~json
{
  "source": "00a0ec20",
  "target": "Stack[-0x3d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ec24`](#insn-00a0ec24)

~~~json
{
  "source": "00a0ec24",
  "target": "0109edb8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109edb8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a0ec28`](#insn-00a0ec28)

~~~json
{
  "source": "00a0ec28",
  "target": "0109edb0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109edb0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a0ec2c`](#insn-00a0ec2c)

~~~json
{
  "source": "00a0ec2c",
  "target": "0109eda8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109eda8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a0ec2c`](#insn-00a0ec2c)

~~~json
{
  "source": "00a0ec2c",
  "target": "0109edb0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109edb0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a0ec38`](#insn-00a0ec38)

~~~json
{
  "source": "00a0ec38",
  "target": "0109eda8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109eda8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a0ec3c`](#insn-00a0ec3c)

~~~json
{
  "source": "00a0ec3c",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a0ec40`](#insn-00a0ec40)

~~~json
{
  "source": "00a0ec40",
  "target": "0109edb0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109edb0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a0ec4c`](#insn-00a0ec4c)

~~~json
{
  "source": "00a0ec4c",
  "target": "0109eda8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109eda8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a0ec50`](#insn-00a0ec50)

~~~json
{
  "source": "00a0ec50",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a0ec54`](#insn-00a0ec54)

~~~json
{
  "source": "00a0ec54",
  "target": "0109edb0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109edb0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a0ec60`](#insn-00a0ec60)

~~~json
{
  "source": "00a0ec60",
  "target": "0109eda8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109eda8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a0ec64`](#insn-00a0ec64)

~~~json
{
  "source": "00a0ec64",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a0ec68`](#insn-00a0ec68)

~~~json
{
  "source": "00a0ec68",
  "target": "0109edb0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109edb0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a0ec74`](#insn-00a0ec74)

~~~json
{
  "source": "00a0ec74",
  "target": "0109eda8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109eda8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a0ec78`](#insn-00a0ec78)

~~~json
{
  "source": "00a0ec78",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a0ec7c`](#insn-00a0ec7c)

~~~json
{
  "source": "00a0ec7c",
  "target": "0109edb0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109edb0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a0ec88`](#insn-00a0ec88)

~~~json
{
  "source": "00a0ec88",
  "target": "0109eda8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109eda8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a0ec8c`](#insn-00a0ec8c)

~~~json
{
  "source": "00a0ec8c",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a0ec90`](#insn-00a0ec90)

~~~json
{
  "source": "00a0ec90",
  "target": "0109edb0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109edb0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a0ec9c`](#insn-00a0ec9c)

~~~json
{
  "source": "00a0ec9c",
  "target": "0109eda8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109eda8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a0eca0`](#insn-00a0eca0)

~~~json
{
  "source": "00a0eca0",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a0eca4`](#insn-00a0eca4)

~~~json
{
  "source": "00a0eca4",
  "target": "0109edb0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109edb0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a0ecb0`](#insn-00a0ecb0)

~~~json
{
  "source": "00a0ecb0",
  "target": "0109eda8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109eda8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a0ecb4`](#insn-00a0ecb4)

~~~json
{
  "source": "00a0ecb4",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a0ecb8`](#insn-00a0ecb8)

~~~json
{
  "source": "00a0ecb8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ecbc`](#insn-00a0ecbc)

~~~json
{
  "source": "00a0ecbc",
  "target": "00a0ed38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ecc0`](#insn-00a0ecc0)

~~~json
{
  "source": "00a0ecc0",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ecc4`](#insn-00a0ecc4)

~~~json
{
  "source": "00a0ecc4",
  "target": "00a0ed48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ecc8`](#insn-00a0ecc8)

~~~json
{
  "source": "00a0ecc8",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0eccc`](#insn-00a0eccc)

~~~json
{
  "source": "00a0eccc",
  "target": "00a0ed58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ecd0`](#insn-00a0ecd0)

~~~json
{
  "source": "00a0ecd0",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ecd4`](#insn-00a0ecd4)

~~~json
{
  "source": "00a0ecd4",
  "target": "00a0ed68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ecd8`](#insn-00a0ecd8)

~~~json
{
  "source": "00a0ecd8",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ecdc`](#insn-00a0ecdc)

~~~json
{
  "source": "00a0ecdc",
  "target": "00a0ed78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ece0`](#insn-00a0ece0)

~~~json
{
  "source": "00a0ece0",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ece4`](#insn-00a0ece4)

~~~json
{
  "source": "00a0ece4",
  "target": "00a0ed88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ece8`](#insn-00a0ece8)

~~~json
{
  "source": "00a0ece8",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ecec`](#insn-00a0ecec)

~~~json
{
  "source": "00a0ecec",
  "target": "00a0ecf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ecf0`](#insn-00a0ecf0)

~~~json
{
  "source": "00a0ecf0",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ecf4`](#insn-00a0ecf4)

~~~json
{
  "source": "00a0ecf4",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a0ecfc`](#insn-00a0ecfc)

~~~json
{
  "source": "00a0ecfc",
  "target": "00418330",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a0ed04`](#insn-00a0ed04)

~~~json
{
  "source": "00a0ed04",
  "target": "0109eda8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109eda8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a0ed0c`](#insn-00a0ed0c)

~~~json
{
  "source": "00a0ed0c",
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
- 参照命令 [`00a0ed10`](#insn-00a0ed10)

~~~json
{
  "source": "00a0ed10",
  "target": "00bdafe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a0ed18`](#insn-00a0ed18)

~~~json
{
  "source": "00a0ed18",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ed20`](#insn-00a0ed20)

~~~json
{
  "source": "00a0ed20",
  "target": "00a0ee68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ed24`](#insn-00a0ed24)

~~~json
{
  "source": "00a0ed24",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ed28`](#insn-00a0ed28)

~~~json
{
  "source": "00a0ed28",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ed2c`](#insn-00a0ed2c)

~~~json
{
  "source": "00a0ed2c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ed38`](#insn-00a0ed38)

~~~json
{
  "source": "00a0ed38",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ed3c`](#insn-00a0ed3c)

~~~json
{
  "source": "00a0ed3c",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a0ed40`](#insn-00a0ed40)

~~~json
{
  "source": "00a0ed40",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ed44`](#insn-00a0ed44)

~~~json
{
  "source": "00a0ed44",
  "target": "00a0ecc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ed48`](#insn-00a0ed48)

~~~json
{
  "source": "00a0ed48",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ed4c`](#insn-00a0ed4c)

~~~json
{
  "source": "00a0ed4c",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a0ed50`](#insn-00a0ed50)

~~~json
{
  "source": "00a0ed50",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ed54`](#insn-00a0ed54)

~~~json
{
  "source": "00a0ed54",
  "target": "00a0ecd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ed58`](#insn-00a0ed58)

~~~json
{
  "source": "00a0ed58",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ed5c`](#insn-00a0ed5c)

~~~json
{
  "source": "00a0ed5c",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a0ed60`](#insn-00a0ed60)

~~~json
{
  "source": "00a0ed60",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ed64`](#insn-00a0ed64)

~~~json
{
  "source": "00a0ed64",
  "target": "00a0ecd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ed68`](#insn-00a0ed68)

~~~json
{
  "source": "00a0ed68",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ed6c`](#insn-00a0ed6c)

~~~json
{
  "source": "00a0ed6c",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a0ed70`](#insn-00a0ed70)

~~~json
{
  "source": "00a0ed70",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ed74`](#insn-00a0ed74)

~~~json
{
  "source": "00a0ed74",
  "target": "00a0ece0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ed78`](#insn-00a0ed78)

~~~json
{
  "source": "00a0ed78",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ed7c`](#insn-00a0ed7c)

~~~json
{
  "source": "00a0ed7c",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a0ed80`](#insn-00a0ed80)

~~~json
{
  "source": "00a0ed80",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ed84`](#insn-00a0ed84)

~~~json
{
  "source": "00a0ed84",
  "target": "00a0ece8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ed88`](#insn-00a0ed88)

~~~json
{
  "source": "00a0ed88",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ed8c`](#insn-00a0ed8c)

~~~json
{
  "source": "00a0ed8c",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a0ed90`](#insn-00a0ed90)

~~~json
{
  "source": "00a0ed90",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ed94`](#insn-00a0ed94)

~~~json
{
  "source": "00a0ed94",
  "target": "00a0ecf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ed98`](#insn-00a0ed98)

~~~json
{
  "source": "00a0ed98",
  "target": "00a0ecf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ee68`](#insn-00a0ee68)

~~~json
{
  "source": "00a0ee68",
  "target": "00bdb090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
