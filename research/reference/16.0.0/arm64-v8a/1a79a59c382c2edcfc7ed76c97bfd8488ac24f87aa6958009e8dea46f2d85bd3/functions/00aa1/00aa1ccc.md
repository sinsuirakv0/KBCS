# 00aa1ccc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00a43dc8`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a43/00a43dc8.md) · 移動量 `+0x5df04`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0051.md#compare-e4e9b47860a41907fd3e91aee9d20f92)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00aa1ec8`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aa1/00aa1ec8.md) · 移動量 `+0x1fc`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0062.md#compare-63bf7f2e03b5af389c133003254acf55)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aa1ccc",
  "name": "_INIT_233",
  "size": 708,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "330d1656e5e6d91d12f2255d41e85bb5f1787d475e328d095a5971078d0ef2e5",
  "source_text_sha256": "330d1656e5e6d91d12f2255d41e85bb5f1787d475e328d095a5971078d0ef2e5",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aa1ccc",
        "00aa1f8b"
      ],
      [
        "00aa2058",
        "00aa205b"
      ]
    ],
    "bytes_sha256": "3d4d12fcf0c6012dfa3cf0b1ea8f0bf70555e54ef873c59cc2d1b46e9a6396ad",
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

## 疑似コード / UTF-8 5054 bytes

~~~c

/* WARNING: Type propagation algorithm not settling */

void _INIT_233(void)

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
                    /* try { // try from 00aa1dc8 to 00ba1dcb has its CatchHandler @ 00aa28ec */
                    /* try { // try from 00aa1dcc to 00ba1ed3 has its CatchHandler @ 00aa1464 */
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
  DAT_01123d48 = 0;
  DAT_01123d40 = 0;
  DAT_01123d38 = &DAT_01123d40;
  FUN_0043b7b8(&DAT_01123d38,&DAT_01123d40,local_118,local_118);
  FUN_0043b7b8(&DAT_01123d38,&DAT_01123d40,local_f8,local_f8);
  FUN_0043b7b8(&DAT_01123d38,&DAT_01123d40,local_d8,local_d8);
  FUN_0043b7b8(&DAT_01123d38,&DAT_01123d40,local_b8,local_b8);
  FUN_0043b7b8(&DAT_01123d38,&DAT_01123d40,local_98,local_98);
  FUN_0043b7b8(&DAT_01123d38,&DAT_01123d40,local_78,local_78);
  FUN_0043b7b8(&DAT_01123d38,&DAT_01123d40,local_58,local_58);
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
    _ZdlPv((void *)CONCAT44(uStack_dc,CONCAT13(uStack_dd,CONCAT21(uStack_df,cStack_e0))));
  }
  if ((local_110 & 1) != 0) {
    _ZdlPv((void *)CONCAT44(uStack_fc,CONCAT13(uStack_fd,CONCAT21(uStack_ff,cStack_100))));
  }
  __cxa_atexit(FUN_0043ae30,&DAT_01123d38,&PTR_LOOP_00c62b90);
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
<a id="insn-00aa1ccc"></a> `00aa1ccc` | `ff 83 04 d1` | sub sp,sp,#0x120 | `FALL_THROUGH`
<a id="insn-00aa1cd0"></a> `00aa1cd0` | `fd 7b 0f a9` | stp x29,x30,[sp, #0xf0] | `FALL_THROUGH`
<a id="insn-00aa1cd4"></a> `00aa1cd4` | `fc 57 10 a9` | stp x28,x21,[sp, #0x100] | `FALL_THROUGH`
<a id="insn-00aa1cd8"></a> `00aa1cd8` | `f4 4f 11 a9` | stp x20,x19,[sp, #0x110] | `FALL_THROUGH`
<a id="insn-00aa1cdc"></a> `00aa1cdc` | `fd c3 03 91` | add x29,sp,#0xf0 | `FALL_THROUGH`
<a id="insn-00aa1ce0"></a> `00aa1ce0` | `55 d0 3b d5` | mrs x21,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00aa1ce4"></a> `00aa1ce4` | `2a e8 8c 52` | mov w10,#0x6741 | `FALL_THROUGH`
<a id="insn-00aa1ce8"></a> `00aa1ce8` | `f4 23 00 91` | add x20,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00aa1cec"></a> `00aa1cec` | `a9 16 40 f9` | ldr x9,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00aa1cf0"></a> `00aa1cf0` | `88 04 80 52` | mov w8,#0x24 | `FALL_THROUGH`
<a id="insn-00aa1cf4"></a> `00aa1cf4` | `13 34 00 d0` | adrp x19,0x1123000 | `FALL_THROUGH`
<a id="insn-00aa1cf8"></a> `00aa1cf8` | `73 e2 34 91` | add x19,x19,#0xd38 | `FALL_THROUGH`
<a id="insn-00aa1cfc"></a> `00aa1cfc` | `a9 83 1f f8` | stur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aa1d00"></a> `00aa1d00` | `a9 c0 ff d0` | adrp x9,0x2b7000 | `FALL_THROUGH`
<a id="insn-00aa1d04"></a> `00aa1d04` | `29 99 3b 91` | add x9,x9,#0xee6 | `FALL_THROUGH`
<a id="insn-00aa1d08"></a> `00aa1d08` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00aa1d0c"></a> `00aa1d0c` | `29 00 80 52` | mov w9,#0x1 | `FALL_THROUGH`
<a id="insn-00aa1d10"></a> `00aa1d10` | `ea 13 02 78` | sturh w10,[sp, #0x21] | `FALL_THROUGH`
<a id="insn-00aa1d14"></a> `00aa1d14` | `e9 2b 00 b9` | str w9,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00aa1d18"></a> `00aa1d18` | `49 28 88 52` | mov w9,#0x4142 | `FALL_THROUGH`
<a id="insn-00aa1d1c"></a> `00aa1d1c` | `aa c0 ff d0` | adrp x10,0x2b7000 | `FALL_THROUGH`
<a id="insn-00aa1d20"></a> `00aa1d20` | `4a e5 3b 91` | add x10,x10,#0xef9 | `FALL_THROUGH`
<a id="insn-00aa1d24"></a> `00aa1d24` | `e0 13 81 3c` | stur q0,[sp, #0x11] | `FALL_THROUGH`
<a id="insn-00aa1d28"></a> `00aa1d28` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00aa1d2c"></a> `00aa1d2c` | `40 01 c0 3d` | ldr q0,[x10] | `FALL_THROUGH`
<a id="insn-00aa1d30"></a> `00aa1d30` | `e9 13 04 78` | sturh w9,[sp, #0x41] | `FALL_THROUGH`
<a id="insn-00aa1d34"></a> `00aa1d34` | `49 00 80 52` | mov w9,#0x2 | `FALL_THROUGH`
<a id="insn-00aa1d38"></a> `00aa1d38` | `e9 4b 00 b9` | str w9,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00aa1d3c"></a> `00aa1d3c` | `49 e8 8c 52` | mov w9,#0x6742 | `FALL_THROUGH`
<a id="insn-00aa1d40"></a> `00aa1d40` | `aa c0 ff f0` | adrp x10,0x2b8000 | `FALL_THROUGH`
<a id="insn-00aa1d44"></a> `00aa1d44` | `4a 09 36 91` | add x10,x10,#0xd82 | `FALL_THROUGH`
<a id="insn-00aa1d48"></a> `00aa1d48` | `e0 13 83 3c` | stur q0,[sp, #0x31] | `FALL_THROUGH`
<a id="insn-00aa1d4c"></a> `00aa1d4c` | `40 01 c0 3d` | ldr q0,[x10] | `FALL_THROUGH`
<a id="insn-00aa1d50"></a> `00aa1d50` | `e9 13 06 78` | sturh w9,[sp, #0x61] | `FALL_THROUGH`
<a id="insn-00aa1d54"></a> `00aa1d54` | `69 00 80 52` | mov w9,#0x3 | `FALL_THROUGH`
<a id="insn-00aa1d58"></a> `00aa1d58` | `e9 6b 00 b9` | str w9,[sp, #0x68] | `FALL_THROUGH`
<a id="insn-00aa1d5c"></a> `00aa1d5c` | `29 e8 8e 52` | mov w9,#0x7741 | `FALL_THROUGH`
<a id="insn-00aa1d60"></a> `00aa1d60` | `0a c0 ff b0` | adrp x10,0x2a2000 | `FALL_THROUGH`
<a id="insn-00aa1d64"></a> `00aa1d64` | `4a 55 3a 91` | add x10,x10,#0xe95 | `FALL_THROUGH`
<a id="insn-00aa1d68"></a> `00aa1d68` | `e0 13 85 3c` | stur q0,[sp, #0x51] | `FALL_THROUGH`
<a id="insn-00aa1d6c"></a> `00aa1d6c` | `40 01 c0 3d` | ldr q0,[x10] | `FALL_THROUGH`
<a id="insn-00aa1d70"></a> `00aa1d70` | `e9 13 08 78` | sturh w9,[sp, #0x81] | `FALL_THROUGH`
<a id="insn-00aa1d74"></a> `00aa1d74` | `89 00 80 52` | mov w9,#0x4 | `FALL_THROUGH`
<a id="insn-00aa1d78"></a> `00aa1d78` | `e9 8b 00 b9` | str w9,[sp, #0x88] | `FALL_THROUGH`
<a id="insn-00aa1d7c"></a> `00aa1d7c` | `49 c0 ff f0` | adrp x9,0x2ac000 | `FALL_THROUGH`
<a id="insn-00aa1d80"></a> `00aa1d80` | `29 49 16 91` | add x9,x9,#0x592 | `FALL_THROUGH`
<a id="insn-00aa1d84"></a> `00aa1d84` | `e0 13 87 3c` | stur q0,[sp, #0x71] | `FALL_THROUGH`
<a id="insn-00aa1d88"></a> `00aa1d88` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00aa1d8c"></a> `00aa1d8c` | `49 28 8a 52` | mov w9,#0x5142 | `FALL_THROUGH`
<a id="insn-00aa1d90"></a> `00aa1d90` | `89 92 09 78` | sturh w9,[x20, #0x99] | `FALL_THROUGH`
<a id="insn-00aa1d94"></a> `00aa1d94` | `a9 00 80 52` | mov w9,#0x5 | `FALL_THROUGH`
<a id="insn-00aa1d98"></a> `00aa1d98` | `e9 ab 00 b9` | str w9,[sp, #0xa8] | `FALL_THROUGH`
<a id="insn-00aa1d9c"></a> `00aa1d9c` | `e9 bf ff f0` | adrp x9,0x2a0000 | `FALL_THROUGH`
<a id="insn-00aa1da0"></a> `00aa1da0` | `29 41 3a 91` | add x9,x9,#0xe90 | `FALL_THROUGH`
<a id="insn-00aa1da4"></a> `00aa1da4` | `80 92 88 3c` | stur q0,[x20, #0x89] | `FALL_THROUGH`
<a id="insn-00aa1da8"></a> `00aa1da8` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00aa1dac"></a> `00aa1dac` | `49 e8 8e 52` | mov w9,#0x7742 | `FALL_THROUGH`
<a id="insn-00aa1db0"></a> `00aa1db0` | `89 92 0b 78` | sturh w9,[x20, #0xb9] | `FALL_THROUGH`
<a id="insn-00aa1db4"></a> `00aa1db4` | `c9 00 80 52` | mov w9,#0x6 | `FALL_THROUGH`
<a id="insn-00aa1db8"></a> `00aa1db8` | `e9 cb 00 b9` | str w9,[sp, #0xc8] | `FALL_THROUGH`
<a id="insn-00aa1dbc"></a> `00aa1dbc` | `09 c0 ff d0` | adrp x9,0x2a3000 | `FALL_THROUGH`
<a id="insn-00aa1dc0"></a> `00aa1dc0` | `29 f1 38 91` | add x9,x9,#0xe3c | `FALL_THROUGH`
<a id="insn-00aa1dc4"></a> `00aa1dc4` | `80 92 8a 3c` | stur q0,[x20, #0xa9] | `FALL_THROUGH`
<a id="insn-00aa1dc8"></a> `00aa1dc8` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00aa1dcc"></a> `00aa1dcc` | `e8 43 00 39` | strb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aa1dd0"></a> `00aa1dd0` | `e8 c3 00 39` | strb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aa1dd4"></a> `00aa1dd4` | `e8 43 01 39` | strb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00aa1dd8"></a> `00aa1dd8` | `e8 c3 01 39` | strb w8,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00aa1ddc"></a> `00aa1ddc` | `e8 43 02 39` | strb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00aa1de0"></a> `00aa1de0` | `e8 c3 02 39` | strb w8,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00aa1de4"></a> `00aa1de4` | `e8 43 03 39` | strb w8,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-00aa1de8"></a> `00aa1de8` | `68 28 88 52` | mov w8,#0x4143 | `FALL_THROUGH`
<a id="insn-00aa1dec"></a> `00aa1dec` | `ff 0b 00 b9` | str wzr,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00aa1df0"></a> `00aa1df0` | `ff 8f 00 39` | strb wzr,[sp, #0x23] | `FALL_THROUGH`
<a id="insn-00aa1df4"></a> `00aa1df4` | `ff 0f 01 39` | strb wzr,[sp, #0x43] | `FALL_THROUGH`
<a id="insn-00aa1df8"></a> `00aa1df8` | `ff 8f 01 39` | strb wzr,[sp, #0x63] | `FALL_THROUGH`
<a id="insn-00aa1dfc"></a> `00aa1dfc` | `ff 0f 02 39` | strb wzr,[sp, #0x83] | `FALL_THROUGH`
<a id="insn-00aa1e00"></a> `00aa1e00` | `ff 8f 02 39` | strb wzr,[sp, #0xa3] | `FALL_THROUGH`
<a id="insn-00aa1e04"></a> `00aa1e04` | `ff 0f 03 39` | strb wzr,[sp, #0xc3] | `FALL_THROUGH`
<a id="insn-00aa1e08"></a> `00aa1e08` | `88 92 0d 78` | sturh w8,[x20, #0xd9] | `FALL_THROUGH`
<a id="insn-00aa1e0c"></a> `00aa1e0c` | `80 92 8c 3c` | stur q0,[x20, #0xc9] | `FALL_THROUGH`
<a id="insn-00aa1e10"></a> `00aa1e10` | `ff 8f 03 39` | strb wzr,[sp, #0xe3] | `FALL_THROUGH`
<a id="insn-00aa1e14"></a> `00aa1e14` | `7f 0a 00 f9` | str xzr,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00aa1e18"></a> `00aa1e18` | `3f 8c 00 f8` | str xzr,[x1, #0x8]! | `FALL_THROUGH`
<a id="insn-00aa1e1c"></a> `00aa1e1c` | `61 02 00 f9` | str x1,[x19] | `FALL_THROUGH`
<a id="insn-00aa1e20"></a> `00aa1e20` | `e2 23 00 91` | add x2,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00aa1e24"></a> `00aa1e24` | `e3 23 00 91` | add x3,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00aa1e28"></a> `00aa1e28` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aa1e2c"></a> `00aa1e2c` | `63 66 e6 97` | bl 0x0043b7b8 | `UNCONDITIONAL_CALL`
<a id="insn-00aa1e30"></a> `00aa1e30` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00aa1e34"></a> `00aa1e34` | `82 82 00 91` | add x2,x20,#0x20 | `FALL_THROUGH`
<a id="insn-00aa1e38"></a> `00aa1e38` | `83 82 00 91` | add x3,x20,#0x20 | `FALL_THROUGH`
<a id="insn-00aa1e3c"></a> `00aa1e3c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aa1e40"></a> `00aa1e40` | `5e 66 e6 97` | bl 0x0043b7b8 | `UNCONDITIONAL_CALL`
<a id="insn-00aa1e44"></a> `00aa1e44` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00aa1e48"></a> `00aa1e48` | `82 02 01 91` | add x2,x20,#0x40 | `FALL_THROUGH`
<a id="insn-00aa1e4c"></a> `00aa1e4c` | `83 02 01 91` | add x3,x20,#0x40 | `FALL_THROUGH`
<a id="insn-00aa1e50"></a> `00aa1e50` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aa1e54"></a> `00aa1e54` | `59 66 e6 97` | bl 0x0043b7b8 | `UNCONDITIONAL_CALL`
<a id="insn-00aa1e58"></a> `00aa1e58` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00aa1e5c"></a> `00aa1e5c` | `82 82 01 91` | add x2,x20,#0x60 | `FALL_THROUGH`
<a id="insn-00aa1e60"></a> `00aa1e60` | `83 82 01 91` | add x3,x20,#0x60 | `FALL_THROUGH`
<a id="insn-00aa1e64"></a> `00aa1e64` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aa1e68"></a> `00aa1e68` | `54 66 e6 97` | bl 0x0043b7b8 | `UNCONDITIONAL_CALL`
<a id="insn-00aa1e6c"></a> `00aa1e6c` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00aa1e70"></a> `00aa1e70` | `82 02 02 91` | add x2,x20,#0x80 | `FALL_THROUGH`
<a id="insn-00aa1e74"></a> `00aa1e74` | `83 02 02 91` | add x3,x20,#0x80 | `FALL_THROUGH`
<a id="insn-00aa1e78"></a> `00aa1e78` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aa1e7c"></a> `00aa1e7c` | `4f 66 e6 97` | bl 0x0043b7b8 | `UNCONDITIONAL_CALL`
<a id="insn-00aa1e80"></a> `00aa1e80` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00aa1e84"></a> `00aa1e84` | `82 82 02 91` | add x2,x20,#0xa0 | `FALL_THROUGH`
<a id="insn-00aa1e88"></a> `00aa1e88` | `83 82 02 91` | add x3,x20,#0xa0 | `FALL_THROUGH`
<a id="insn-00aa1e8c"></a> `00aa1e8c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aa1e90"></a> `00aa1e90` | `4a 66 e6 97` | bl 0x0043b7b8 | `UNCONDITIONAL_CALL`
<a id="insn-00aa1e94"></a> `00aa1e94` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00aa1e98"></a> `00aa1e98` | `82 02 03 91` | add x2,x20,#0xc0 | `FALL_THROUGH`
<a id="insn-00aa1e9c"></a> `00aa1e9c` | `83 02 03 91` | add x3,x20,#0xc0 | `FALL_THROUGH`
<a id="insn-00aa1ea0"></a> `00aa1ea0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aa1ea4"></a> `00aa1ea4` | `45 66 e6 97` | bl 0x0043b7b8 | `UNCONDITIONAL_CALL`
<a id="insn-00aa1ea8"></a> `00aa1ea8` | `e8 43 43 39` | ldrb w8,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-00aa1eac"></a> `00aa1eac` | `e8 03 00 37` | tbnz w8,#0x0,0x00aa1f28 | `CONDITIONAL_JUMP`
<a id="insn-00aa1eb0"></a> `00aa1eb0` | `e8 c3 42 39` | ldrb w8,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00aa1eb4"></a> `00aa1eb4` | `28 04 00 37` | tbnz w8,#0x0,0x00aa1f38 | `CONDITIONAL_JUMP`
<a id="insn-00aa1eb8"></a> `00aa1eb8` | `e8 43 42 39` | ldrb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00aa1ebc"></a> `00aa1ebc` | `68 04 00 37` | tbnz w8,#0x0,0x00aa1f48 | `CONDITIONAL_JUMP`
<a id="insn-00aa1ec0"></a> `00aa1ec0` | `e8 c3 41 39` | ldrb w8,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00aa1ec4"></a> `00aa1ec4` | `a8 04 00 37` | tbnz w8,#0x0,0x00aa1f58 | `CONDITIONAL_JUMP`
<a id="insn-00aa1ec8"></a> `00aa1ec8` | `e8 43 41 39` | ldrb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00aa1ecc"></a> `00aa1ecc` | `e8 04 00 37` | tbnz w8,#0x0,0x00aa1f68 | `CONDITIONAL_JUMP`
<a id="insn-00aa1ed0"></a> `00aa1ed0` | `e8 c3 40 39` | ldrb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aa1ed4"></a> `00aa1ed4` | `28 05 00 37` | tbnz w8,#0x0,0x00aa1f78 | `CONDITIONAL_JUMP`
<a id="insn-00aa1ed8"></a> `00aa1ed8` | `e8 43 40 39` | ldrb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aa1edc"></a> `00aa1edc` | `68 00 00 36` | tbz w8,#0x0,0x00aa1ee8 | `CONDITIONAL_JUMP`
<a id="insn-00aa1ee0"></a> `00aa1ee0` | `e0 13 40 f9` | ldr x0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aa1ee4"></a> `00aa1ee4` | `f3 d6 06 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00aa1ee8"></a> `00aa1ee8` | `c0 cc ff b0` | adrp x0,0x43a000 | `FALL_THROUGH`
<a id="insn-00aa1eec"></a> `00aa1eec` | `00 c0 38 91` | add x0,x0,#0xe30 | `FALL_THROUGH`
<a id="insn-00aa1ef0"></a> `00aa1ef0` | `01 34 00 d0` | adrp x1,0x1123000 | `FALL_THROUGH`
<a id="insn-00aa1ef4"></a> `00aa1ef4` | `21 e0 34 91` | add x1,x1,#0xd38 | `FALL_THROUGH`
<a id="insn-00aa1ef8"></a> `00aa1ef8` | `02 0e 00 b0` | adrp x2,0xc62000 | `FALL_THROUGH`
<a id="insn-00aa1efc"></a> `00aa1efc` | `42 40 2e 91` | add x2,x2,#0xb90 | `FALL_THROUGH`
<a id="insn-00aa1f00"></a> `00aa1f00` | `cc d6 06 94` | bl 0x00c57a30 | `UNCONDITIONAL_CALL`
<a id="insn-00aa1f04"></a> `00aa1f04` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00aa1f08"></a> `00aa1f08` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aa1f0c"></a> `00aa1f0c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00aa1f10"></a> `00aa1f10` | `41 0a 00 54` | b.ne 0x00aa2058 | `CONDITIONAL_JUMP`
<a id="insn-00aa1f14"></a> `00aa1f14` | `f4 4f 51 a9` | ldp x20,x19,[sp, #0x110] | `FALL_THROUGH`
<a id="insn-00aa1f18"></a> `00aa1f18` | `fc 57 50 a9` | ldp x28,x21,[sp, #0x100] | `FALL_THROUGH`
<a id="insn-00aa1f1c"></a> `00aa1f1c` | `fd 7b 4f a9` | ldp x29,x30,[sp, #0xf0] | `FALL_THROUGH`
<a id="insn-00aa1f20"></a> `00aa1f20` | `ff 83 04 91` | add sp,sp,#0x120 | `FALL_THROUGH`
<a id="insn-00aa1f24"></a> `00aa1f24` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00aa1f28"></a> `00aa1f28` | `e0 73 40 f9` | ldr x0,[sp, #0xe0] | `FALL_THROUGH`
<a id="insn-00aa1f2c"></a> `00aa1f2c` | `e1 d6 06 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00aa1f30"></a> `00aa1f30` | `e8 c3 42 39` | ldrb w8,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00aa1f34"></a> `00aa1f34` | `28 fc 07 36` | tbz w8,#0x0,0x00aa1eb8 | `CONDITIONAL_JUMP`
<a id="insn-00aa1f38"></a> `00aa1f38` | `e0 63 40 f9` | ldr x0,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00aa1f3c"></a> `00aa1f3c` | `dd d6 06 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00aa1f40"></a> `00aa1f40` | `e8 43 42 39` | ldrb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00aa1f44"></a> `00aa1f44` | `e8 fb 07 36` | tbz w8,#0x0,0x00aa1ec0 | `CONDITIONAL_JUMP`
<a id="insn-00aa1f48"></a> `00aa1f48` | `e0 53 40 f9` | ldr x0,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00aa1f4c"></a> `00aa1f4c` | `d9 d6 06 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00aa1f50"></a> `00aa1f50` | `e8 c3 41 39` | ldrb w8,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00aa1f54"></a> `00aa1f54` | `a8 fb 07 36` | tbz w8,#0x0,0x00aa1ec8 | `CONDITIONAL_JUMP`
<a id="insn-00aa1f58"></a> `00aa1f58` | `e0 43 40 f9` | ldr x0,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00aa1f5c"></a> `00aa1f5c` | `d5 d6 06 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00aa1f60"></a> `00aa1f60` | `e8 43 41 39` | ldrb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00aa1f64"></a> `00aa1f64` | `68 fb 07 36` | tbz w8,#0x0,0x00aa1ed0 | `CONDITIONAL_JUMP`
<a id="insn-00aa1f68"></a> `00aa1f68` | `e0 33 40 f9` | ldr x0,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00aa1f6c"></a> `00aa1f6c` | `d1 d6 06 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00aa1f70"></a> `00aa1f70` | `e8 c3 40 39` | ldrb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aa1f74"></a> `00aa1f74` | `28 fb 07 36` | tbz w8,#0x0,0x00aa1ed8 | `CONDITIONAL_JUMP`
<a id="insn-00aa1f78"></a> `00aa1f78` | `e0 23 40 f9` | ldr x0,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00aa1f7c"></a> `00aa1f7c` | `cd d6 06 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00aa1f80"></a> `00aa1f80` | `e8 43 40 39` | ldrb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aa1f84"></a> `00aa1f84` | `e8 fa 07 37` | tbnz w8,#0x0,0x00aa1ee0 | `CONDITIONAL_JUMP`
<a id="insn-00aa1f88"></a> `00aa1f88` | `d8 ff ff 17` | b 0x00aa1ee8 | `UNCONDITIONAL_JUMP`
<a id="insn-00aa2058"></a> `00aa2058` | `a2 d6 06 94` | bl 0x00c57ae0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aa1ccc`](#insn-00aa1ccc) 範囲 `[['00aa1ccc', '00aa1dc7']]`
  - `FALL_THROUGH` [`00aa1dc4`](#insn-00aa1dc4) → [`00aa1dc8`](#insn-00aa1dc8)
- ブロック [`00aa1dc8`](#insn-00aa1dc8) 範囲 `[['00aa1dc8', '00aa1dcb']]`
  - `FALL_THROUGH` [`00aa1dc8`](#insn-00aa1dc8) → [`00aa1dcc`](#insn-00aa1dcc)
- ブロック [`00aa1dcc`](#insn-00aa1dcc) 範囲 `[['00aa1dcc', '00aa1eaf']]`
  - `CONDITIONAL_JUMP` [`00aa1eac`](#insn-00aa1eac) → [`00aa1f28`](#insn-00aa1f28)
  - `FALL_THROUGH` [`00aa1eac`](#insn-00aa1eac) → [`00aa1eb0`](#insn-00aa1eb0)
- ブロック [`00aa1eb0`](#insn-00aa1eb0) 範囲 `[['00aa1eb0', '00aa1eb7']]`
  - `CONDITIONAL_JUMP` [`00aa1eb4`](#insn-00aa1eb4) → [`00aa1f38`](#insn-00aa1f38)
  - `FALL_THROUGH` [`00aa1eb4`](#insn-00aa1eb4) → [`00aa1eb8`](#insn-00aa1eb8)
- ブロック [`00aa1eb8`](#insn-00aa1eb8) 範囲 `[['00aa1eb8', '00aa1ebf']]`
  - `CONDITIONAL_JUMP` [`00aa1ebc`](#insn-00aa1ebc) → [`00aa1f48`](#insn-00aa1f48)
  - `FALL_THROUGH` [`00aa1ebc`](#insn-00aa1ebc) → [`00aa1ec0`](#insn-00aa1ec0)
- ブロック [`00aa1ec0`](#insn-00aa1ec0) 範囲 `[['00aa1ec0', '00aa1ec7']]`
  - `CONDITIONAL_JUMP` [`00aa1ec4`](#insn-00aa1ec4) → [`00aa1f58`](#insn-00aa1f58)
  - `FALL_THROUGH` [`00aa1ec4`](#insn-00aa1ec4) → [`00aa1ec8`](#insn-00aa1ec8)
- ブロック [`00aa1ec8`](#insn-00aa1ec8) 範囲 `[['00aa1ec8', '00aa1ecf']]`
  - `CONDITIONAL_JUMP` [`00aa1ecc`](#insn-00aa1ecc) → [`00aa1f68`](#insn-00aa1f68)
  - `FALL_THROUGH` [`00aa1ecc`](#insn-00aa1ecc) → [`00aa1ed0`](#insn-00aa1ed0)
- ブロック [`00aa1ed0`](#insn-00aa1ed0) 範囲 `[['00aa1ed0', '00aa1ed3']]`
  - `FALL_THROUGH` [`00aa1ed0`](#insn-00aa1ed0) → [`00aa1ed4`](#insn-00aa1ed4)
- ブロック [`00aa1ed4`](#insn-00aa1ed4) 範囲 `[['00aa1ed4', '00aa1ed7']]`
  - `CONDITIONAL_JUMP` [`00aa1ed4`](#insn-00aa1ed4) → [`00aa1f78`](#insn-00aa1f78)
  - `FALL_THROUGH` [`00aa1ed4`](#insn-00aa1ed4) → [`00aa1ed8`](#insn-00aa1ed8)
- ブロック [`00aa1ed8`](#insn-00aa1ed8) 範囲 `[['00aa1ed8', '00aa1edf']]`
  - `CONDITIONAL_JUMP` [`00aa1edc`](#insn-00aa1edc) → [`00aa1ee8`](#insn-00aa1ee8)
  - `FALL_THROUGH` [`00aa1edc`](#insn-00aa1edc) → [`00aa1ee0`](#insn-00aa1ee0)
- ブロック [`00aa1ee0`](#insn-00aa1ee0) 範囲 `[['00aa1ee0', '00aa1ee7']]`
  - `FALL_THROUGH` [`00aa1ee4`](#insn-00aa1ee4) → [`00aa1ee8`](#insn-00aa1ee8)
- ブロック [`00aa1ee8`](#insn-00aa1ee8) 範囲 `[['00aa1ee8', '00aa1f13']]`
  - `CONDITIONAL_JUMP` [`00aa1f10`](#insn-00aa1f10) → [`00aa2058`](#insn-00aa2058)
  - `FALL_THROUGH` [`00aa1f10`](#insn-00aa1f10) → [`00aa1f14`](#insn-00aa1f14)
- ブロック [`00aa1f14`](#insn-00aa1f14) 範囲 `[['00aa1f14', '00aa1f27']]`
- ブロック [`00aa1f28`](#insn-00aa1f28) 範囲 `[['00aa1f28', '00aa1f37']]`
  - `CONDITIONAL_JUMP` [`00aa1f34`](#insn-00aa1f34) → [`00aa1eb8`](#insn-00aa1eb8)
  - `FALL_THROUGH` [`00aa1f34`](#insn-00aa1f34) → [`00aa1f38`](#insn-00aa1f38)
- ブロック [`00aa1f38`](#insn-00aa1f38) 範囲 `[['00aa1f38', '00aa1f47']]`
  - `CONDITIONAL_JUMP` [`00aa1f44`](#insn-00aa1f44) → [`00aa1ec0`](#insn-00aa1ec0)
  - `FALL_THROUGH` [`00aa1f44`](#insn-00aa1f44) → [`00aa1f48`](#insn-00aa1f48)
- ブロック [`00aa1f48`](#insn-00aa1f48) 範囲 `[['00aa1f48', '00aa1f57']]`
  - `CONDITIONAL_JUMP` [`00aa1f54`](#insn-00aa1f54) → [`00aa1ec8`](#insn-00aa1ec8)
  - `FALL_THROUGH` [`00aa1f54`](#insn-00aa1f54) → [`00aa1f58`](#insn-00aa1f58)
- ブロック [`00aa1f58`](#insn-00aa1f58) 範囲 `[['00aa1f58', '00aa1f67']]`
  - `CONDITIONAL_JUMP` [`00aa1f64`](#insn-00aa1f64) → [`00aa1ed0`](#insn-00aa1ed0)
  - `FALL_THROUGH` [`00aa1f64`](#insn-00aa1f64) → [`00aa1f68`](#insn-00aa1f68)
- ブロック [`00aa1f68`](#insn-00aa1f68) 範囲 `[['00aa1f68', '00aa1f77']]`
  - `CONDITIONAL_JUMP` [`00aa1f74`](#insn-00aa1f74) → [`00aa1ed8`](#insn-00aa1ed8)
  - `FALL_THROUGH` [`00aa1f74`](#insn-00aa1f74) → [`00aa1f78`](#insn-00aa1f78)
- ブロック [`00aa1f78`](#insn-00aa1f78) 範囲 `[['00aa1f78', '00aa1f87']]`
  - `CONDITIONAL_JUMP` [`00aa1f84`](#insn-00aa1f84) → [`00aa1ee0`](#insn-00aa1ee0)
  - `FALL_THROUGH` [`00aa1f84`](#insn-00aa1f84) → [`00aa1f88`](#insn-00aa1f88)
- ブロック [`00aa1f88`](#insn-00aa1f88) 範囲 `[['00aa1f88', '00aa1f8b']]`
  - `UNCONDITIONAL_JUMP` [`00aa1f88`](#insn-00aa1f88) → [`00aa1ee8`](#insn-00aa1ee8)
- ブロック [`00aa2058`](#insn-00aa2058) 範囲 `[['00aa2058', '00aa205b']]`

## 命令位置別の参照

- [`00aa1cd0`](#insn-00aa1cd0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1cd4`](#insn-00aa1cd4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1cd8`](#insn-00aa1cd8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1cfc`](#insn-00aa1cfc) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1d08`](#insn-00aa1d08) → `002b7ee6`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aa1d10`](#insn-00aa1d10) → `Stack[-0xff]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1d14`](#insn-00aa1d14) → `Stack[-0xf8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1d24`](#insn-00aa1d24) → `Stack[-0x10f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1d2c`](#insn-00aa1d2c) → `002b7ef9`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aa1d30`](#insn-00aa1d30) → `Stack[-0xdf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1d38`](#insn-00aa1d38) → `Stack[-0xd8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1d48`](#insn-00aa1d48) → `Stack[-0xef]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1d4c`](#insn-00aa1d4c) → `002b8d82`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aa1d50`](#insn-00aa1d50) → `Stack[-0xbf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1d58`](#insn-00aa1d58) → `Stack[-0xb8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1d68`](#insn-00aa1d68) → `Stack[-0xcf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1d6c`](#insn-00aa1d6c) → `002a2e95`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aa1d70`](#insn-00aa1d70) → `Stack[-0x9f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1d78`](#insn-00aa1d78) → `Stack[-0x98]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1d84`](#insn-00aa1d84) → `Stack[-0xaf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1d88`](#insn-00aa1d88) → `002ac592`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aa1d90`](#insn-00aa1d90) → `Stack[-0x7f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1d98`](#insn-00aa1d98) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1da4`](#insn-00aa1da4) → `Stack[-0x8f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1da8`](#insn-00aa1da8) → `002a0e90`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aa1db0`](#insn-00aa1db0) → `Stack[-0x5f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1db8`](#insn-00aa1db8) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1dc4`](#insn-00aa1dc4) → `Stack[-0x6f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1dc8`](#insn-00aa1dc8) → `002a3e3c`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aa1dcc`](#insn-00aa1dcc) → `Stack[-0x110]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1dd0`](#insn-00aa1dd0) → `Stack[-0xf0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1dd4`](#insn-00aa1dd4) → `Stack[-0xd0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1dd8`](#insn-00aa1dd8) → `Stack[-0xb0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1ddc`](#insn-00aa1ddc) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1de0`](#insn-00aa1de0) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1de4`](#insn-00aa1de4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1dec`](#insn-00aa1dec) → `Stack[-0x118]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1df0`](#insn-00aa1df0) → `Stack[-0xfd]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1df4`](#insn-00aa1df4) → `Stack[-0xdd]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1df8`](#insn-00aa1df8) → `Stack[-0xbd]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1dfc`](#insn-00aa1dfc) → `Stack[-0x9d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1e00`](#insn-00aa1e00) → `Stack[-0x7d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1e04`](#insn-00aa1e04) → `Stack[-0x5d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1e08`](#insn-00aa1e08) → `Stack[-0x3f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1e0c`](#insn-00aa1e0c) → `Stack[-0x4f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1e10`](#insn-00aa1e10) → `Stack[-0x3d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1e14`](#insn-00aa1e14) → `01123d48`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aa1e18`](#insn-00aa1e18) → `01123d40`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aa1e1c`](#insn-00aa1e1c) → `01123d38`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aa1e1c`](#insn-00aa1e1c) → `01123d40`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aa1e28`](#insn-00aa1e28) → `01123d38`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aa1e2c`](#insn-00aa1e2c) → [`0043b7b8`](../0043b/0043b7b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043b7b8` · 推定シンボル `None` · 推定型 `None`
- [`00aa1e30`](#insn-00aa1e30) → `01123d40`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aa1e3c`](#insn-00aa1e3c) → `01123d38`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aa1e40`](#insn-00aa1e40) → [`0043b7b8`](../0043b/0043b7b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043b7b8` · 推定シンボル `None` · 推定型 `None`
- [`00aa1e44`](#insn-00aa1e44) → `01123d40`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aa1e50`](#insn-00aa1e50) → `01123d38`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aa1e54`](#insn-00aa1e54) → [`0043b7b8`](../0043b/0043b7b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043b7b8` · 推定シンボル `None` · 推定型 `None`
- [`00aa1e58`](#insn-00aa1e58) → `01123d40`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aa1e64`](#insn-00aa1e64) → `01123d38`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aa1e68`](#insn-00aa1e68) → [`0043b7b8`](../0043b/0043b7b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043b7b8` · 推定シンボル `None` · 推定型 `None`
- [`00aa1e6c`](#insn-00aa1e6c) → `01123d40`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aa1e78`](#insn-00aa1e78) → `01123d38`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aa1e7c`](#insn-00aa1e7c) → [`0043b7b8`](../0043b/0043b7b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043b7b8` · 推定シンボル `None` · 推定型 `None`
- [`00aa1e80`](#insn-00aa1e80) → `01123d40`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aa1e8c`](#insn-00aa1e8c) → `01123d38`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aa1e90`](#insn-00aa1e90) → [`0043b7b8`](../0043b/0043b7b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043b7b8` · 推定シンボル `None` · 推定型 `None`
- [`00aa1e94`](#insn-00aa1e94) → `01123d40`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aa1ea0`](#insn-00aa1ea0) → `01123d38`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aa1ea4`](#insn-00aa1ea4) → [`0043b7b8`](../0043b/0043b7b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043b7b8` · 推定シンボル `None` · 推定型 `None`
- [`00aa1ea8`](#insn-00aa1ea8) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1eac`](#insn-00aa1eac) → [`00aa1f28`](#insn-00aa1f28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1eb0`](#insn-00aa1eb0) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1eb4`](#insn-00aa1eb4) → [`00aa1f38`](#insn-00aa1f38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1eb8`](#insn-00aa1eb8) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1ebc`](#insn-00aa1ebc) → [`00aa1f48`](#insn-00aa1f48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1ec0`](#insn-00aa1ec0) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1ec4`](#insn-00aa1ec4) → [`00aa1f58`](#insn-00aa1f58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1ec8`](#insn-00aa1ec8) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1ecc`](#insn-00aa1ecc) → [`00aa1f68`](#insn-00aa1f68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1ed0`](#insn-00aa1ed0) → `Stack[-0xf0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1ed4`](#insn-00aa1ed4) → [`00aa1f78`](#insn-00aa1f78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1ed8`](#insn-00aa1ed8) → `Stack[-0x110]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1edc`](#insn-00aa1edc) → [`00aa1ee8`](#insn-00aa1ee8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1ee0`](#insn-00aa1ee0) → `Stack[-0x100]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1ee4`](#insn-00aa1ee4) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00aa1eec`](#insn-00aa1eec) → [`0043ae30`](../0043a/0043ae30.md) · `PARAM` · `ANALYSIS` · 関数 `0043ae30` · 推定シンボル `None` · 推定型 `None`
- [`00aa1ef4`](#insn-00aa1ef4) → `01123d38`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aa1efc`](#insn-00aa1efc) → `00c62b90`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00aa1f00`](#insn-00aa1f00) → [`00c57a30`](../00c57/00c57a30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a30` · 推定シンボル `None` · 推定型 `None`
- [`00aa1f08`](#insn-00aa1f08) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1f10`](#insn-00aa1f10) → [`00aa2058`](#insn-00aa2058) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1f14`](#insn-00aa1f14) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1f18`](#insn-00aa1f18) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1f1c`](#insn-00aa1f1c) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1f28`](#insn-00aa1f28) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1f2c`](#insn-00aa1f2c) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00aa1f30`](#insn-00aa1f30) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1f34`](#insn-00aa1f34) → [`00aa1eb8`](#insn-00aa1eb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1f38`](#insn-00aa1f38) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1f3c`](#insn-00aa1f3c) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00aa1f40`](#insn-00aa1f40) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1f44`](#insn-00aa1f44) → [`00aa1ec0`](#insn-00aa1ec0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1f48`](#insn-00aa1f48) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1f4c`](#insn-00aa1f4c) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00aa1f50`](#insn-00aa1f50) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1f54`](#insn-00aa1f54) → [`00aa1ec8`](#insn-00aa1ec8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1f58`](#insn-00aa1f58) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1f5c`](#insn-00aa1f5c) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00aa1f60`](#insn-00aa1f60) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1f64`](#insn-00aa1f64) → [`00aa1ed0`](#insn-00aa1ed0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1f68`](#insn-00aa1f68) → `Stack[-0xc0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1f6c`](#insn-00aa1f6c) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00aa1f70`](#insn-00aa1f70) → `Stack[-0xf0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1f74`](#insn-00aa1f74) → [`00aa1ed8`](#insn-00aa1ed8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1f78`](#insn-00aa1f78) → `Stack[-0xe0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1f7c`](#insn-00aa1f7c) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00aa1f80`](#insn-00aa1f80) → `Stack[-0x110]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1f84`](#insn-00aa1f84) → [`00aa1ee0`](#insn-00aa1ee0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1f88`](#insn-00aa1f88) → [`00aa1ee8`](#insn-00aa1ee8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa2058`](#insn-00aa2058) → [`00c57ae0`](../00c57/00c57ae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ae0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aa1cd0`](#insn-00aa1cd0)

~~~json
{
  "source": "00aa1cd0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1cd4`](#insn-00aa1cd4)

~~~json
{
  "source": "00aa1cd4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1cd8`](#insn-00aa1cd8)

~~~json
{
  "source": "00aa1cd8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1cfc`](#insn-00aa1cfc)

~~~json
{
  "source": "00aa1cfc",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1d08`](#insn-00aa1d08)

~~~json
{
  "source": "00aa1d08",
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
- 参照命令 [`00aa1d10`](#insn-00aa1d10)

~~~json
{
  "source": "00aa1d10",
  "target": "Stack[-0xff]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1d14`](#insn-00aa1d14)

~~~json
{
  "source": "00aa1d14",
  "target": "Stack[-0xf8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1d24`](#insn-00aa1d24)

~~~json
{
  "source": "00aa1d24",
  "target": "Stack[-0x10f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1d2c`](#insn-00aa1d2c)

~~~json
{
  "source": "00aa1d2c",
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
- 参照命令 [`00aa1d30`](#insn-00aa1d30)

~~~json
{
  "source": "00aa1d30",
  "target": "Stack[-0xdf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1d38`](#insn-00aa1d38)

~~~json
{
  "source": "00aa1d38",
  "target": "Stack[-0xd8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1d48`](#insn-00aa1d48)

~~~json
{
  "source": "00aa1d48",
  "target": "Stack[-0xef]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1d4c`](#insn-00aa1d4c)

~~~json
{
  "source": "00aa1d4c",
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
- 参照命令 [`00aa1d50`](#insn-00aa1d50)

~~~json
{
  "source": "00aa1d50",
  "target": "Stack[-0xbf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1d58`](#insn-00aa1d58)

~~~json
{
  "source": "00aa1d58",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1d68`](#insn-00aa1d68)

~~~json
{
  "source": "00aa1d68",
  "target": "Stack[-0xcf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1d6c`](#insn-00aa1d6c)

~~~json
{
  "source": "00aa1d6c",
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
- 参照命令 [`00aa1d70`](#insn-00aa1d70)

~~~json
{
  "source": "00aa1d70",
  "target": "Stack[-0x9f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1d78`](#insn-00aa1d78)

~~~json
{
  "source": "00aa1d78",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1d84`](#insn-00aa1d84)

~~~json
{
  "source": "00aa1d84",
  "target": "Stack[-0xaf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1d88`](#insn-00aa1d88)

~~~json
{
  "source": "00aa1d88",
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
- 参照命令 [`00aa1d90`](#insn-00aa1d90)

~~~json
{
  "source": "00aa1d90",
  "target": "Stack[-0x7f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1d98`](#insn-00aa1d98)

~~~json
{
  "source": "00aa1d98",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1da4`](#insn-00aa1da4)

~~~json
{
  "source": "00aa1da4",
  "target": "Stack[-0x8f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1da8`](#insn-00aa1da8)

~~~json
{
  "source": "00aa1da8",
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
- 参照命令 [`00aa1db0`](#insn-00aa1db0)

~~~json
{
  "source": "00aa1db0",
  "target": "Stack[-0x5f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1db8`](#insn-00aa1db8)

~~~json
{
  "source": "00aa1db8",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1dc4`](#insn-00aa1dc4)

~~~json
{
  "source": "00aa1dc4",
  "target": "Stack[-0x6f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1dc8`](#insn-00aa1dc8)

~~~json
{
  "source": "00aa1dc8",
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
- 参照命令 [`00aa1dcc`](#insn-00aa1dcc)

~~~json
{
  "source": "00aa1dcc",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1dd0`](#insn-00aa1dd0)

~~~json
{
  "source": "00aa1dd0",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1dd4`](#insn-00aa1dd4)

~~~json
{
  "source": "00aa1dd4",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1dd8`](#insn-00aa1dd8)

~~~json
{
  "source": "00aa1dd8",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1ddc`](#insn-00aa1ddc)

~~~json
{
  "source": "00aa1ddc",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1de0`](#insn-00aa1de0)

~~~json
{
  "source": "00aa1de0",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1de4`](#insn-00aa1de4)

~~~json
{
  "source": "00aa1de4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1dec`](#insn-00aa1dec)

~~~json
{
  "source": "00aa1dec",
  "target": "Stack[-0x118]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1df0`](#insn-00aa1df0)

~~~json
{
  "source": "00aa1df0",
  "target": "Stack[-0xfd]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1df4`](#insn-00aa1df4)

~~~json
{
  "source": "00aa1df4",
  "target": "Stack[-0xdd]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1df8`](#insn-00aa1df8)

~~~json
{
  "source": "00aa1df8",
  "target": "Stack[-0xbd]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1dfc`](#insn-00aa1dfc)

~~~json
{
  "source": "00aa1dfc",
  "target": "Stack[-0x9d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1e00`](#insn-00aa1e00)

~~~json
{
  "source": "00aa1e00",
  "target": "Stack[-0x7d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1e04`](#insn-00aa1e04)

~~~json
{
  "source": "00aa1e04",
  "target": "Stack[-0x5d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1e08`](#insn-00aa1e08)

~~~json
{
  "source": "00aa1e08",
  "target": "Stack[-0x3f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1e0c`](#insn-00aa1e0c)

~~~json
{
  "source": "00aa1e0c",
  "target": "Stack[-0x4f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1e10`](#insn-00aa1e10)

~~~json
{
  "source": "00aa1e10",
  "target": "Stack[-0x3d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1e14`](#insn-00aa1e14)

~~~json
{
  "source": "00aa1e14",
  "target": "01123d48",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01123d48",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aa1e18`](#insn-00aa1e18)

~~~json
{
  "source": "00aa1e18",
  "target": "01123d40",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01123d40",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aa1e1c`](#insn-00aa1e1c)

~~~json
{
  "source": "00aa1e1c",
  "target": "01123d38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01123d38",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aa1e1c`](#insn-00aa1e1c)

~~~json
{
  "source": "00aa1e1c",
  "target": "01123d40",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01123d40",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aa1e28`](#insn-00aa1e28)

~~~json
{
  "source": "00aa1e28",
  "target": "01123d38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01123d38",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aa1e2c`](#insn-00aa1e2c)

~~~json
{
  "source": "00aa1e2c",
  "target": "0043b7b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa1e30`](#insn-00aa1e30)

~~~json
{
  "source": "00aa1e30",
  "target": "01123d40",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01123d40",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aa1e3c`](#insn-00aa1e3c)

~~~json
{
  "source": "00aa1e3c",
  "target": "01123d38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01123d38",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aa1e40`](#insn-00aa1e40)

~~~json
{
  "source": "00aa1e40",
  "target": "0043b7b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa1e44`](#insn-00aa1e44)

~~~json
{
  "source": "00aa1e44",
  "target": "01123d40",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01123d40",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aa1e50`](#insn-00aa1e50)

~~~json
{
  "source": "00aa1e50",
  "target": "01123d38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01123d38",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aa1e54`](#insn-00aa1e54)

~~~json
{
  "source": "00aa1e54",
  "target": "0043b7b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa1e58`](#insn-00aa1e58)

~~~json
{
  "source": "00aa1e58",
  "target": "01123d40",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01123d40",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aa1e64`](#insn-00aa1e64)

~~~json
{
  "source": "00aa1e64",
  "target": "01123d38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01123d38",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aa1e68`](#insn-00aa1e68)

~~~json
{
  "source": "00aa1e68",
  "target": "0043b7b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa1e6c`](#insn-00aa1e6c)

~~~json
{
  "source": "00aa1e6c",
  "target": "01123d40",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01123d40",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aa1e78`](#insn-00aa1e78)

~~~json
{
  "source": "00aa1e78",
  "target": "01123d38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01123d38",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aa1e7c`](#insn-00aa1e7c)

~~~json
{
  "source": "00aa1e7c",
  "target": "0043b7b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa1e80`](#insn-00aa1e80)

~~~json
{
  "source": "00aa1e80",
  "target": "01123d40",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01123d40",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aa1e8c`](#insn-00aa1e8c)

~~~json
{
  "source": "00aa1e8c",
  "target": "01123d38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01123d38",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aa1e90`](#insn-00aa1e90)

~~~json
{
  "source": "00aa1e90",
  "target": "0043b7b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa1e94`](#insn-00aa1e94)

~~~json
{
  "source": "00aa1e94",
  "target": "01123d40",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01123d40",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aa1ea0`](#insn-00aa1ea0)

~~~json
{
  "source": "00aa1ea0",
  "target": "01123d38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01123d38",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aa1ea4`](#insn-00aa1ea4)

~~~json
{
  "source": "00aa1ea4",
  "target": "0043b7b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa1ea8`](#insn-00aa1ea8)

~~~json
{
  "source": "00aa1ea8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1eac`](#insn-00aa1eac)

~~~json
{
  "source": "00aa1eac",
  "target": "00aa1f28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1eb0`](#insn-00aa1eb0)

~~~json
{
  "source": "00aa1eb0",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1eb4`](#insn-00aa1eb4)

~~~json
{
  "source": "00aa1eb4",
  "target": "00aa1f38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1eb8`](#insn-00aa1eb8)

~~~json
{
  "source": "00aa1eb8",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1ebc`](#insn-00aa1ebc)

~~~json
{
  "source": "00aa1ebc",
  "target": "00aa1f48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1ec0`](#insn-00aa1ec0)

~~~json
{
  "source": "00aa1ec0",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1ec4`](#insn-00aa1ec4)

~~~json
{
  "source": "00aa1ec4",
  "target": "00aa1f58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1ec8`](#insn-00aa1ec8)

~~~json
{
  "source": "00aa1ec8",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1ecc`](#insn-00aa1ecc)

~~~json
{
  "source": "00aa1ecc",
  "target": "00aa1f68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1ed0`](#insn-00aa1ed0)

~~~json
{
  "source": "00aa1ed0",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1ed4`](#insn-00aa1ed4)

~~~json
{
  "source": "00aa1ed4",
  "target": "00aa1f78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1ed8`](#insn-00aa1ed8)

~~~json
{
  "source": "00aa1ed8",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1edc`](#insn-00aa1edc)

~~~json
{
  "source": "00aa1edc",
  "target": "00aa1ee8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1ee0`](#insn-00aa1ee0)

~~~json
{
  "source": "00aa1ee0",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1ee4`](#insn-00aa1ee4)

~~~json
{
  "source": "00aa1ee4",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa1eec`](#insn-00aa1eec)

~~~json
{
  "source": "00aa1eec",
  "target": "0043ae30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa1ef4`](#insn-00aa1ef4)

~~~json
{
  "source": "00aa1ef4",
  "target": "01123d38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01123d38",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aa1efc`](#insn-00aa1efc)

~~~json
{
  "source": "00aa1efc",
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
- 参照命令 [`00aa1f00`](#insn-00aa1f00)

~~~json
{
  "source": "00aa1f00",
  "target": "00c57a30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa1f08`](#insn-00aa1f08)

~~~json
{
  "source": "00aa1f08",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1f10`](#insn-00aa1f10)

~~~json
{
  "source": "00aa1f10",
  "target": "00aa2058",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1f14`](#insn-00aa1f14)

~~~json
{
  "source": "00aa1f14",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1f18`](#insn-00aa1f18)

~~~json
{
  "source": "00aa1f18",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1f1c`](#insn-00aa1f1c)

~~~json
{
  "source": "00aa1f1c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1f28`](#insn-00aa1f28)

~~~json
{
  "source": "00aa1f28",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1f2c`](#insn-00aa1f2c)

~~~json
{
  "source": "00aa1f2c",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa1f30`](#insn-00aa1f30)

~~~json
{
  "source": "00aa1f30",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1f34`](#insn-00aa1f34)

~~~json
{
  "source": "00aa1f34",
  "target": "00aa1eb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1f38`](#insn-00aa1f38)

~~~json
{
  "source": "00aa1f38",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1f3c`](#insn-00aa1f3c)

~~~json
{
  "source": "00aa1f3c",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa1f40`](#insn-00aa1f40)

~~~json
{
  "source": "00aa1f40",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1f44`](#insn-00aa1f44)

~~~json
{
  "source": "00aa1f44",
  "target": "00aa1ec0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1f48`](#insn-00aa1f48)

~~~json
{
  "source": "00aa1f48",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1f4c`](#insn-00aa1f4c)

~~~json
{
  "source": "00aa1f4c",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa1f50`](#insn-00aa1f50)

~~~json
{
  "source": "00aa1f50",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1f54`](#insn-00aa1f54)

~~~json
{
  "source": "00aa1f54",
  "target": "00aa1ec8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1f58`](#insn-00aa1f58)

~~~json
{
  "source": "00aa1f58",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1f5c`](#insn-00aa1f5c)

~~~json
{
  "source": "00aa1f5c",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa1f60`](#insn-00aa1f60)

~~~json
{
  "source": "00aa1f60",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1f64`](#insn-00aa1f64)

~~~json
{
  "source": "00aa1f64",
  "target": "00aa1ed0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1f68`](#insn-00aa1f68)

~~~json
{
  "source": "00aa1f68",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1f6c`](#insn-00aa1f6c)

~~~json
{
  "source": "00aa1f6c",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa1f70`](#insn-00aa1f70)

~~~json
{
  "source": "00aa1f70",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1f74`](#insn-00aa1f74)

~~~json
{
  "source": "00aa1f74",
  "target": "00aa1ed8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1f78`](#insn-00aa1f78)

~~~json
{
  "source": "00aa1f78",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1f7c`](#insn-00aa1f7c)

~~~json
{
  "source": "00aa1f7c",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa1f80`](#insn-00aa1f80)

~~~json
{
  "source": "00aa1f80",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1f84`](#insn-00aa1f84)

~~~json
{
  "source": "00aa1f84",
  "target": "00aa1ee0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1f88`](#insn-00aa1f88)

~~~json
{
  "source": "00aa1f88",
  "target": "00aa1ee8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa2058`](#insn-00aa2058)

~~~json
{
  "source": "00aa2058",
  "target": "00c57ae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
