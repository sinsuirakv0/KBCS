# 00b3cffc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00b3c008`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3c/00b3c008.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0071.md#compare-b05459d34398dda5b2eeff6a4db70d57)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b3cffc",
  "name": "_INIT_274",
  "size": 708,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f54f1083f5b9d3556e05758af12b879830ebcc0f1f44cca1e500faa783796fd0",
  "source_text_sha256": "f54f1083f5b9d3556e05758af12b879830ebcc0f1f44cca1e500faa783796fd0",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b3cffc",
        "00b3d2bb"
      ],
      [
        "00b3d388",
        "00b3d38b"
      ]
    ],
    "bytes_sha256": "de6ff7dd6d249fb78b667d49fb5de9b46a2fa1c7690aceaa64da534caaa200ca",
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

- [0043bb58](../0043b/0043bb58.md)
- [00c58ed0](../00c58/00c58ed0.md)
- [00c58f50](../00c58/00c58f50.md)
- [00c58f80](../00c58/00c58f80.md)

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

## 疑似コード / UTF-8 5636 bytes

~~~c

/* WARNING: Type propagation algorithm not settling */

void _INIT_274(void)

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
                    /* try { // try from 00b3d018 to 00c3d09b has its CatchHandler @ 00b3cd8c */
  local_38 = *(long *)(lVar1 + 0x28);
  uStack_ff = 0x6741;
  local_f8[0] = 1;
  uStack_107 = (undefined7)s_CgkIjM3y_ZQaEAIQAg_002b8035._8_8_;
  cStack_100 = SUB81(s_CgkIjM3y_ZQaEAIQAg_002b8035._8_8_,7);
  local_10f = (char  [8])s_CgkIjM3y_ZQaEAIQAg_002b8035._0_8_;
  uStack_df = 0x4142;
  local_d8[0] = 2;
  uStack_e7 = (undefined7)s_CgkIjM3y_ZQaEAIQBA_002b8048._8_8_;
  cStack_e0 = SUB81(s_CgkIjM3y_ZQaEAIQBA_002b8048._8_8_,7);
  local_ef = (char  [8])s_CgkIjM3y_ZQaEAIQBA_002b8048._0_8_;
  uStack_bf = 0x6742;
  local_b8[0] = 3;
  uStack_c7 = (undefined7)s_CgkIjM3y_ZQaEAIQBg_002b8e3d._8_8_;
  cStack_c0 = SUB81(s_CgkIjM3y_ZQaEAIQBg_002b8e3d._8_8_,7);
  local_cf = (char  [8])s_CgkIjM3y_ZQaEAIQBg_002b8e3d._0_8_;
                    /* try { // try from 00b3d09c to 00c3d09f has its CatchHandler @ 00b3dd74 */
  uStack_9f = 0x7741;
  local_98[0] = 4;
  uStack_a7 = (undefined7)s_CgkIjM3y_ZQaEAIQAw_002a2fe0._8_8_;
  cStack_a0 = SUB81(s_CgkIjM3y_ZQaEAIQAw_002a2fe0._8_8_,7);
  local_af = (char  [8])s_CgkIjM3y_ZQaEAIQAw_002a2fe0._0_8_;
  uStack_7f = 0x5142;
  local_78[0] = 5;
  uStack_87 = (undefined7)s_CgkIjM3y_ZQaEAIQBQ_002ac643._8_8_;
  cStack_80 = SUB81(s_CgkIjM3y_ZQaEAIQBQ_002ac643._8_8_,7);
  local_8f = (char  [8])s_CgkIjM3y_ZQaEAIQBQ_002ac643._0_8_;
                    /* try { // try from 00b3d0d8 to 00c3d0ff has its CatchHandler @ 00b3dd78 */
  uStack_5f = 0x7742;
  local_58[0] = 6;
  uStack_67 = (undefined7)s_CgkIjM3y_ZQaEAIQBw_002a0f50._8_8_;
  cStack_60 = SUB81(s_CgkIjM3y_ZQaEAIQBw_002a0f50._8_8_,7);
  local_6f = (char  [8])s_CgkIjM3y_ZQaEAIQBw_002a0f50._0_8_;
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
  uStack_47 = (undefined7)s_CgkIjM3y_ZQaEAIQCA_002a3f87._8_8_;
  cStack_40 = SUB81(s_CgkIjM3y_ZQaEAIQCA_002a3f87._8_8_,7);
  local_4f = (char  [8])s_CgkIjM3y_ZQaEAIQCA_002a3f87._0_8_;
  uStack_3d = 0;
  DAT_01126390 = 0;
  DAT_01126388 = 0;
  DAT_01126380 = &DAT_01126388;
                    /* try { // try from 00b3d15c to 00c3d15f has its CatchHandler @ 00b3dd70 */
  FUN_0043bb58(&DAT_01126380,&DAT_01126388,local_118,local_118);
                    /* try { // try from 00b3d160 to 00c3d1ab has its CatchHandler @ 00b3cd8c */
  FUN_0043bb58(&DAT_01126380,&DAT_01126388,local_f8,local_f8);
  FUN_0043bb58(&DAT_01126380,&DAT_01126388,local_d8,local_d8);
  FUN_0043bb58(&DAT_01126380,&DAT_01126388,local_b8,local_b8);
                    /* try { // try from 00b3d1ac to 00c3d1af has its CatchHandler @ 00b3dd6c */
  FUN_0043bb58(&DAT_01126380,&DAT_01126388,local_98,local_98);
                    /* try { // try from 00b3d1b0 to 00c3d1bb has its CatchHandler @ 00b3dd68 */
  FUN_0043bb58(&DAT_01126380,&DAT_01126388,local_78,local_78);
  FUN_0043bb58(&DAT_01126380,&DAT_01126388,local_58,local_58);
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
  __cxa_atexit(FUN_0043b1d0,&DAT_01126380,&PTR_LOOP_00c64030);
  if (*(long *)(lVar1 + 0x28) == local_38) {
                    /* try { // try from 00b3d248 to 00c3d2c3 has its CatchHandler @ 00b3dd84 */
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
<a id="insn-00b3cffc"></a> `00b3cffc` | `ff 83 04 d1` | sub sp,sp,#0x120 | `FALL_THROUGH`
<a id="insn-00b3d000"></a> `00b3d000` | `fd 7b 0f a9` | stp x29,x30,[sp, #0xf0] | `FALL_THROUGH`
<a id="insn-00b3d004"></a> `00b3d004` | `fc 57 10 a9` | stp x28,x21,[sp, #0x100] | `FALL_THROUGH`
<a id="insn-00b3d008"></a> `00b3d008` | `f4 4f 11 a9` | stp x20,x19,[sp, #0x110] | `FALL_THROUGH`
<a id="insn-00b3d00c"></a> `00b3d00c` | `fd c3 03 91` | add x29,sp,#0xf0 | `FALL_THROUGH`
<a id="insn-00b3d010"></a> `00b3d010` | `55 d0 3b d5` | mrs x21,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00b3d014"></a> `00b3d014` | `2a e8 8c 52` | mov w10,#0x6741 | `FALL_THROUGH`
<a id="insn-00b3d018"></a> `00b3d018` | `f4 23 00 91` | add x20,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00b3d01c"></a> `00b3d01c` | `a9 16 40 f9` | ldr x9,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00b3d020"></a> `00b3d020` | `88 04 80 52` | mov w8,#0x24 | `FALL_THROUGH`
<a id="insn-00b3d024"></a> `00b3d024` | `53 2f 00 b0` | adrp x19,0x1126000 | `FALL_THROUGH`
<a id="insn-00b3d028"></a> `00b3d028` | `73 02 0e 91` | add x19,x19,#0x380 | `FALL_THROUGH`
<a id="insn-00b3d02c"></a> `00b3d02c` | `a9 83 1f f8` | stur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00b3d030"></a> `00b3d030` | `c9 bb ff f0` | adrp x9,0x2b8000 | `FALL_THROUGH`
<a id="insn-00b3d034"></a> `00b3d034` | `29 d5 00 91` | add x9,x9,#0x35 | `FALL_THROUGH`
<a id="insn-00b3d038"></a> `00b3d038` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00b3d03c"></a> `00b3d03c` | `29 00 80 52` | mov w9,#0x1 | `FALL_THROUGH`
<a id="insn-00b3d040"></a> `00b3d040` | `ea 13 02 78` | sturh w10,[sp, #0x21] | `FALL_THROUGH`
<a id="insn-00b3d044"></a> `00b3d044` | `e9 2b 00 b9` | str w9,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00b3d048"></a> `00b3d048` | `49 28 88 52` | mov w9,#0x4142 | `FALL_THROUGH`
<a id="insn-00b3d04c"></a> `00b3d04c` | `ca bb ff f0` | adrp x10,0x2b8000 | `FALL_THROUGH`
<a id="insn-00b3d050"></a> `00b3d050` | `4a 21 01 91` | add x10,x10,#0x48 | `FALL_THROUGH`
<a id="insn-00b3d054"></a> `00b3d054` | `e0 13 81 3c` | stur q0,[sp, #0x11] | `FALL_THROUGH`
<a id="insn-00b3d058"></a> `00b3d058` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00b3d05c"></a> `00b3d05c` | `40 01 c0 3d` | ldr q0,[x10] | `FALL_THROUGH`
<a id="insn-00b3d060"></a> `00b3d060` | `e9 13 04 78` | sturh w9,[sp, #0x41] | `FALL_THROUGH`
<a id="insn-00b3d064"></a> `00b3d064` | `49 00 80 52` | mov w9,#0x2 | `FALL_THROUGH`
<a id="insn-00b3d068"></a> `00b3d068` | `e9 4b 00 b9` | str w9,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00b3d06c"></a> `00b3d06c` | `49 e8 8c 52` | mov w9,#0x6742 | `FALL_THROUGH`
<a id="insn-00b3d070"></a> `00b3d070` | `ca bb ff f0` | adrp x10,0x2b8000 | `FALL_THROUGH`
<a id="insn-00b3d074"></a> `00b3d074` | `4a f5 38 91` | add x10,x10,#0xe3d | `FALL_THROUGH`
<a id="insn-00b3d078"></a> `00b3d078` | `e0 13 83 3c` | stur q0,[sp, #0x31] | `FALL_THROUGH`
<a id="insn-00b3d07c"></a> `00b3d07c` | `40 01 c0 3d` | ldr q0,[x10] | `FALL_THROUGH`
<a id="insn-00b3d080"></a> `00b3d080` | `e9 13 06 78` | sturh w9,[sp, #0x61] | `FALL_THROUGH`
<a id="insn-00b3d084"></a> `00b3d084` | `69 00 80 52` | mov w9,#0x3 | `FALL_THROUGH`
<a id="insn-00b3d088"></a> `00b3d088` | `e9 6b 00 b9` | str w9,[sp, #0x68] | `FALL_THROUGH`
<a id="insn-00b3d08c"></a> `00b3d08c` | `29 e8 8e 52` | mov w9,#0x7741 | `FALL_THROUGH`
<a id="insn-00b3d090"></a> `00b3d090` | `2a bb ff b0` | adrp x10,0x2a2000 | `FALL_THROUGH`
<a id="insn-00b3d094"></a> `00b3d094` | `4a 81 3f 91` | add x10,x10,#0xfe0 | `FALL_THROUGH`
<a id="insn-00b3d098"></a> `00b3d098` | `e0 13 85 3c` | stur q0,[sp, #0x51] | `FALL_THROUGH`
<a id="insn-00b3d09c"></a> `00b3d09c` | `40 01 c0 3d` | ldr q0,[x10] | `FALL_THROUGH`
<a id="insn-00b3d0a0"></a> `00b3d0a0` | `e9 13 08 78` | sturh w9,[sp, #0x81] | `FALL_THROUGH`
<a id="insn-00b3d0a4"></a> `00b3d0a4` | `89 00 80 52` | mov w9,#0x4 | `FALL_THROUGH`
<a id="insn-00b3d0a8"></a> `00b3d0a8` | `e9 8b 00 b9` | str w9,[sp, #0x88] | `FALL_THROUGH`
<a id="insn-00b3d0ac"></a> `00b3d0ac` | `69 bb ff f0` | adrp x9,0x2ac000 | `FALL_THROUGH`
<a id="insn-00b3d0b0"></a> `00b3d0b0` | `29 0d 19 91` | add x9,x9,#0x643 | `FALL_THROUGH`
<a id="insn-00b3d0b4"></a> `00b3d0b4` | `e0 13 87 3c` | stur q0,[sp, #0x71] | `FALL_THROUGH`
<a id="insn-00b3d0b8"></a> `00b3d0b8` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00b3d0bc"></a> `00b3d0bc` | `49 28 8a 52` | mov w9,#0x5142 | `FALL_THROUGH`
<a id="insn-00b3d0c0"></a> `00b3d0c0` | `89 92 09 78` | sturh w9,[x20, #0x99] | `FALL_THROUGH`
<a id="insn-00b3d0c4"></a> `00b3d0c4` | `a9 00 80 52` | mov w9,#0x5 | `FALL_THROUGH`
<a id="insn-00b3d0c8"></a> `00b3d0c8` | `e9 ab 00 b9` | str w9,[sp, #0xa8] | `FALL_THROUGH`
<a id="insn-00b3d0cc"></a> `00b3d0cc` | `09 bb ff f0` | adrp x9,0x2a0000 | `FALL_THROUGH`
<a id="insn-00b3d0d0"></a> `00b3d0d0` | `29 41 3d 91` | add x9,x9,#0xf50 | `FALL_THROUGH`
<a id="insn-00b3d0d4"></a> `00b3d0d4` | `80 92 88 3c` | stur q0,[x20, #0x89] | `FALL_THROUGH`
<a id="insn-00b3d0d8"></a> `00b3d0d8` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00b3d0dc"></a> `00b3d0dc` | `49 e8 8e 52` | mov w9,#0x7742 | `FALL_THROUGH`
<a id="insn-00b3d0e0"></a> `00b3d0e0` | `89 92 0b 78` | sturh w9,[x20, #0xb9] | `FALL_THROUGH`
<a id="insn-00b3d0e4"></a> `00b3d0e4` | `c9 00 80 52` | mov w9,#0x6 | `FALL_THROUGH`
<a id="insn-00b3d0e8"></a> `00b3d0e8` | `e9 cb 00 b9` | str w9,[sp, #0xc8] | `FALL_THROUGH`
<a id="insn-00b3d0ec"></a> `00b3d0ec` | `29 bb ff d0` | adrp x9,0x2a3000 | `FALL_THROUGH`
<a id="insn-00b3d0f0"></a> `00b3d0f0` | `29 1d 3e 91` | add x9,x9,#0xf87 | `FALL_THROUGH`
<a id="insn-00b3d0f4"></a> `00b3d0f4` | `80 92 8a 3c` | stur q0,[x20, #0xa9] | `FALL_THROUGH`
<a id="insn-00b3d0f8"></a> `00b3d0f8` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00b3d0fc"></a> `00b3d0fc` | `e8 43 00 39` | strb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b3d100"></a> `00b3d100` | `e8 c3 00 39` | strb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b3d104"></a> `00b3d104` | `e8 43 01 39` | strb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00b3d108"></a> `00b3d108` | `e8 c3 01 39` | strb w8,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00b3d10c"></a> `00b3d10c` | `e8 43 02 39` | strb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00b3d110"></a> `00b3d110` | `e8 c3 02 39` | strb w8,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00b3d114"></a> `00b3d114` | `e8 43 03 39` | strb w8,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-00b3d118"></a> `00b3d118` | `68 28 88 52` | mov w8,#0x4143 | `FALL_THROUGH`
<a id="insn-00b3d11c"></a> `00b3d11c` | `ff 0b 00 b9` | str wzr,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00b3d120"></a> `00b3d120` | `ff 8f 00 39` | strb wzr,[sp, #0x23] | `FALL_THROUGH`
<a id="insn-00b3d124"></a> `00b3d124` | `ff 0f 01 39` | strb wzr,[sp, #0x43] | `FALL_THROUGH`
<a id="insn-00b3d128"></a> `00b3d128` | `ff 8f 01 39` | strb wzr,[sp, #0x63] | `FALL_THROUGH`
<a id="insn-00b3d12c"></a> `00b3d12c` | `ff 0f 02 39` | strb wzr,[sp, #0x83] | `FALL_THROUGH`
<a id="insn-00b3d130"></a> `00b3d130` | `ff 8f 02 39` | strb wzr,[sp, #0xa3] | `FALL_THROUGH`
<a id="insn-00b3d134"></a> `00b3d134` | `ff 0f 03 39` | strb wzr,[sp, #0xc3] | `FALL_THROUGH`
<a id="insn-00b3d138"></a> `00b3d138` | `88 92 0d 78` | sturh w8,[x20, #0xd9] | `FALL_THROUGH`
<a id="insn-00b3d13c"></a> `00b3d13c` | `80 92 8c 3c` | stur q0,[x20, #0xc9] | `FALL_THROUGH`
<a id="insn-00b3d140"></a> `00b3d140` | `ff 8f 03 39` | strb wzr,[sp, #0xe3] | `FALL_THROUGH`
<a id="insn-00b3d144"></a> `00b3d144` | `7f 0a 00 f9` | str xzr,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00b3d148"></a> `00b3d148` | `3f 8c 00 f8` | str xzr,[x1, #0x8]! | `FALL_THROUGH`
<a id="insn-00b3d14c"></a> `00b3d14c` | `61 02 00 f9` | str x1,[x19] | `FALL_THROUGH`
<a id="insn-00b3d150"></a> `00b3d150` | `e2 23 00 91` | add x2,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00b3d154"></a> `00b3d154` | `e3 23 00 91` | add x3,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00b3d158"></a> `00b3d158` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b3d15c"></a> `00b3d15c` | `7f fa e3 97` | bl 0x0043bb58 | `UNCONDITIONAL_CALL`
<a id="insn-00b3d160"></a> `00b3d160` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00b3d164"></a> `00b3d164` | `82 82 00 91` | add x2,x20,#0x20 | `FALL_THROUGH`
<a id="insn-00b3d168"></a> `00b3d168` | `83 82 00 91` | add x3,x20,#0x20 | `FALL_THROUGH`
<a id="insn-00b3d16c"></a> `00b3d16c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b3d170"></a> `00b3d170` | `7a fa e3 97` | bl 0x0043bb58 | `UNCONDITIONAL_CALL`
<a id="insn-00b3d174"></a> `00b3d174` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00b3d178"></a> `00b3d178` | `82 02 01 91` | add x2,x20,#0x40 | `FALL_THROUGH`
<a id="insn-00b3d17c"></a> `00b3d17c` | `83 02 01 91` | add x3,x20,#0x40 | `FALL_THROUGH`
<a id="insn-00b3d180"></a> `00b3d180` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b3d184"></a> `00b3d184` | `75 fa e3 97` | bl 0x0043bb58 | `UNCONDITIONAL_CALL`
<a id="insn-00b3d188"></a> `00b3d188` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00b3d18c"></a> `00b3d18c` | `82 82 01 91` | add x2,x20,#0x60 | `FALL_THROUGH`
<a id="insn-00b3d190"></a> `00b3d190` | `83 82 01 91` | add x3,x20,#0x60 | `FALL_THROUGH`
<a id="insn-00b3d194"></a> `00b3d194` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b3d198"></a> `00b3d198` | `70 fa e3 97` | bl 0x0043bb58 | `UNCONDITIONAL_CALL`
<a id="insn-00b3d19c"></a> `00b3d19c` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00b3d1a0"></a> `00b3d1a0` | `82 02 02 91` | add x2,x20,#0x80 | `FALL_THROUGH`
<a id="insn-00b3d1a4"></a> `00b3d1a4` | `83 02 02 91` | add x3,x20,#0x80 | `FALL_THROUGH`
<a id="insn-00b3d1a8"></a> `00b3d1a8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b3d1ac"></a> `00b3d1ac` | `6b fa e3 97` | bl 0x0043bb58 | `UNCONDITIONAL_CALL`
<a id="insn-00b3d1b0"></a> `00b3d1b0` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00b3d1b4"></a> `00b3d1b4` | `82 82 02 91` | add x2,x20,#0xa0 | `FALL_THROUGH`
<a id="insn-00b3d1b8"></a> `00b3d1b8` | `83 82 02 91` | add x3,x20,#0xa0 | `FALL_THROUGH`
<a id="insn-00b3d1bc"></a> `00b3d1bc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b3d1c0"></a> `00b3d1c0` | `66 fa e3 97` | bl 0x0043bb58 | `UNCONDITIONAL_CALL`
<a id="insn-00b3d1c4"></a> `00b3d1c4` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00b3d1c8"></a> `00b3d1c8` | `82 02 03 91` | add x2,x20,#0xc0 | `FALL_THROUGH`
<a id="insn-00b3d1cc"></a> `00b3d1cc` | `83 02 03 91` | add x3,x20,#0xc0 | `FALL_THROUGH`
<a id="insn-00b3d1d0"></a> `00b3d1d0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b3d1d4"></a> `00b3d1d4` | `61 fa e3 97` | bl 0x0043bb58 | `UNCONDITIONAL_CALL`
<a id="insn-00b3d1d8"></a> `00b3d1d8` | `e8 43 43 39` | ldrb w8,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-00b3d1dc"></a> `00b3d1dc` | `e8 03 00 37` | tbnz w8,#0x0,0x00b3d258 | `CONDITIONAL_JUMP`
<a id="insn-00b3d1e0"></a> `00b3d1e0` | `e8 c3 42 39` | ldrb w8,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00b3d1e4"></a> `00b3d1e4` | `28 04 00 37` | tbnz w8,#0x0,0x00b3d268 | `CONDITIONAL_JUMP`
<a id="insn-00b3d1e8"></a> `00b3d1e8` | `e8 43 42 39` | ldrb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00b3d1ec"></a> `00b3d1ec` | `68 04 00 37` | tbnz w8,#0x0,0x00b3d278 | `CONDITIONAL_JUMP`
<a id="insn-00b3d1f0"></a> `00b3d1f0` | `e8 c3 41 39` | ldrb w8,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00b3d1f4"></a> `00b3d1f4` | `a8 04 00 37` | tbnz w8,#0x0,0x00b3d288 | `CONDITIONAL_JUMP`
<a id="insn-00b3d1f8"></a> `00b3d1f8` | `e8 43 41 39` | ldrb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00b3d1fc"></a> `00b3d1fc` | `e8 04 00 37` | tbnz w8,#0x0,0x00b3d298 | `CONDITIONAL_JUMP`
<a id="insn-00b3d200"></a> `00b3d200` | `e8 c3 40 39` | ldrb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b3d204"></a> `00b3d204` | `28 05 00 37` | tbnz w8,#0x0,0x00b3d2a8 | `CONDITIONAL_JUMP`
<a id="insn-00b3d208"></a> `00b3d208` | `e8 43 40 39` | ldrb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b3d20c"></a> `00b3d20c` | `68 00 00 36` | tbz w8,#0x0,0x00b3d218 | `CONDITIONAL_JUMP`
<a id="insn-00b3d210"></a> `00b3d210` | `e0 13 40 f9` | ldr x0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b3d214"></a> `00b3d214` | `4f 6f 04 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00b3d218"></a> `00b3d218` | `e0 c7 ff d0` | adrp x0,0x43b000 | `FALL_THROUGH`
<a id="insn-00b3d21c"></a> `00b3d21c` | `00 40 07 91` | add x0,x0,#0x1d0 | `FALL_THROUGH`
<a id="insn-00b3d220"></a> `00b3d220` | `41 2f 00 b0` | adrp x1,0x1126000 | `FALL_THROUGH`
<a id="insn-00b3d224"></a> `00b3d224` | `21 00 0e 91` | add x1,x1,#0x380 | `FALL_THROUGH`
<a id="insn-00b3d228"></a> `00b3d228` | `22 09 00 f0` | adrp x2,0xc64000 | `FALL_THROUGH`
<a id="insn-00b3d22c"></a> `00b3d22c` | `42 c0 00 91` | add x2,x2,#0x30 | `FALL_THROUGH`
<a id="insn-00b3d230"></a> `00b3d230` | `28 6f 04 94` | bl 0x00c58ed0 | `UNCONDITIONAL_CALL`
<a id="insn-00b3d234"></a> `00b3d234` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00b3d238"></a> `00b3d238` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00b3d23c"></a> `00b3d23c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00b3d240"></a> `00b3d240` | `41 0a 00 54` | b.ne 0x00b3d388 | `CONDITIONAL_JUMP`
<a id="insn-00b3d244"></a> `00b3d244` | `f4 4f 51 a9` | ldp x20,x19,[sp, #0x110] | `FALL_THROUGH`
<a id="insn-00b3d248"></a> `00b3d248` | `fc 57 50 a9` | ldp x28,x21,[sp, #0x100] | `FALL_THROUGH`
<a id="insn-00b3d24c"></a> `00b3d24c` | `fd 7b 4f a9` | ldp x29,x30,[sp, #0xf0] | `FALL_THROUGH`
<a id="insn-00b3d250"></a> `00b3d250` | `ff 83 04 91` | add sp,sp,#0x120 | `FALL_THROUGH`
<a id="insn-00b3d254"></a> `00b3d254` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00b3d258"></a> `00b3d258` | `e0 73 40 f9` | ldr x0,[sp, #0xe0] | `FALL_THROUGH`
<a id="insn-00b3d25c"></a> `00b3d25c` | `3d 6f 04 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00b3d260"></a> `00b3d260` | `e8 c3 42 39` | ldrb w8,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00b3d264"></a> `00b3d264` | `28 fc 07 36` | tbz w8,#0x0,0x00b3d1e8 | `CONDITIONAL_JUMP`
<a id="insn-00b3d268"></a> `00b3d268` | `e0 63 40 f9` | ldr x0,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00b3d26c"></a> `00b3d26c` | `39 6f 04 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00b3d270"></a> `00b3d270` | `e8 43 42 39` | ldrb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00b3d274"></a> `00b3d274` | `e8 fb 07 36` | tbz w8,#0x0,0x00b3d1f0 | `CONDITIONAL_JUMP`
<a id="insn-00b3d278"></a> `00b3d278` | `e0 53 40 f9` | ldr x0,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00b3d27c"></a> `00b3d27c` | `35 6f 04 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00b3d280"></a> `00b3d280` | `e8 c3 41 39` | ldrb w8,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00b3d284"></a> `00b3d284` | `a8 fb 07 36` | tbz w8,#0x0,0x00b3d1f8 | `CONDITIONAL_JUMP`
<a id="insn-00b3d288"></a> `00b3d288` | `e0 43 40 f9` | ldr x0,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00b3d28c"></a> `00b3d28c` | `31 6f 04 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00b3d290"></a> `00b3d290` | `e8 43 41 39` | ldrb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00b3d294"></a> `00b3d294` | `68 fb 07 36` | tbz w8,#0x0,0x00b3d200 | `CONDITIONAL_JUMP`
<a id="insn-00b3d298"></a> `00b3d298` | `e0 33 40 f9` | ldr x0,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00b3d29c"></a> `00b3d29c` | `2d 6f 04 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00b3d2a0"></a> `00b3d2a0` | `e8 c3 40 39` | ldrb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b3d2a4"></a> `00b3d2a4` | `28 fb 07 36` | tbz w8,#0x0,0x00b3d208 | `CONDITIONAL_JUMP`
<a id="insn-00b3d2a8"></a> `00b3d2a8` | `e0 23 40 f9` | ldr x0,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b3d2ac"></a> `00b3d2ac` | `29 6f 04 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00b3d2b0"></a> `00b3d2b0` | `e8 43 40 39` | ldrb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b3d2b4"></a> `00b3d2b4` | `e8 fa 07 37` | tbnz w8,#0x0,0x00b3d210 | `CONDITIONAL_JUMP`
<a id="insn-00b3d2b8"></a> `00b3d2b8` | `d8 ff ff 17` | b 0x00b3d218 | `UNCONDITIONAL_JUMP`
<a id="insn-00b3d388"></a> `00b3d388` | `fe 6e 04 94` | bl 0x00c58f80 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b3cffc`](#insn-00b3cffc) 範囲 `[['00b3cffc', '00b3d017']]`
  - `FALL_THROUGH` [`00b3d014`](#insn-00b3d014) → [`00b3d018`](#insn-00b3d018)
- ブロック [`00b3d018`](#insn-00b3d018) 範囲 `[['00b3d018', '00b3d09b']]`
  - `FALL_THROUGH` [`00b3d098`](#insn-00b3d098) → [`00b3d09c`](#insn-00b3d09c)
- ブロック [`00b3d09c`](#insn-00b3d09c) 範囲 `[['00b3d09c', '00b3d0d7']]`
  - `FALL_THROUGH` [`00b3d0d4`](#insn-00b3d0d4) → [`00b3d0d8`](#insn-00b3d0d8)
- ブロック [`00b3d0d8`](#insn-00b3d0d8) 範囲 `[['00b3d0d8', '00b3d15b']]`
  - `FALL_THROUGH` [`00b3d158`](#insn-00b3d158) → [`00b3d15c`](#insn-00b3d15c)
- ブロック [`00b3d15c`](#insn-00b3d15c) 範囲 `[['00b3d15c', '00b3d15f']]`
  - `FALL_THROUGH` [`00b3d15c`](#insn-00b3d15c) → [`00b3d160`](#insn-00b3d160)
- ブロック [`00b3d160`](#insn-00b3d160) 範囲 `[['00b3d160', '00b3d1ab']]`
  - `FALL_THROUGH` [`00b3d1a8`](#insn-00b3d1a8) → [`00b3d1ac`](#insn-00b3d1ac)
- ブロック [`00b3d1ac`](#insn-00b3d1ac) 範囲 `[['00b3d1ac', '00b3d1af']]`
  - `FALL_THROUGH` [`00b3d1ac`](#insn-00b3d1ac) → [`00b3d1b0`](#insn-00b3d1b0)
- ブロック [`00b3d1b0`](#insn-00b3d1b0) 範囲 `[['00b3d1b0', '00b3d1df']]`
  - `CONDITIONAL_JUMP` [`00b3d1dc`](#insn-00b3d1dc) → [`00b3d258`](#insn-00b3d258)
  - `FALL_THROUGH` [`00b3d1dc`](#insn-00b3d1dc) → [`00b3d1e0`](#insn-00b3d1e0)
- ブロック [`00b3d1e0`](#insn-00b3d1e0) 範囲 `[['00b3d1e0', '00b3d1e7']]`
  - `CONDITIONAL_JUMP` [`00b3d1e4`](#insn-00b3d1e4) → [`00b3d268`](#insn-00b3d268)
  - `FALL_THROUGH` [`00b3d1e4`](#insn-00b3d1e4) → [`00b3d1e8`](#insn-00b3d1e8)
- ブロック [`00b3d1e8`](#insn-00b3d1e8) 範囲 `[['00b3d1e8', '00b3d1ef']]`
  - `CONDITIONAL_JUMP` [`00b3d1ec`](#insn-00b3d1ec) → [`00b3d278`](#insn-00b3d278)
  - `FALL_THROUGH` [`00b3d1ec`](#insn-00b3d1ec) → [`00b3d1f0`](#insn-00b3d1f0)
- ブロック [`00b3d1f0`](#insn-00b3d1f0) 範囲 `[['00b3d1f0', '00b3d1f7']]`
  - `CONDITIONAL_JUMP` [`00b3d1f4`](#insn-00b3d1f4) → [`00b3d288`](#insn-00b3d288)
  - `FALL_THROUGH` [`00b3d1f4`](#insn-00b3d1f4) → [`00b3d1f8`](#insn-00b3d1f8)
- ブロック [`00b3d1f8`](#insn-00b3d1f8) 範囲 `[['00b3d1f8', '00b3d1ff']]`
  - `CONDITIONAL_JUMP` [`00b3d1fc`](#insn-00b3d1fc) → [`00b3d298`](#insn-00b3d298)
  - `FALL_THROUGH` [`00b3d1fc`](#insn-00b3d1fc) → [`00b3d200`](#insn-00b3d200)
- ブロック [`00b3d200`](#insn-00b3d200) 範囲 `[['00b3d200', '00b3d207']]`
  - `CONDITIONAL_JUMP` [`00b3d204`](#insn-00b3d204) → [`00b3d2a8`](#insn-00b3d2a8)
  - `FALL_THROUGH` [`00b3d204`](#insn-00b3d204) → [`00b3d208`](#insn-00b3d208)
- ブロック [`00b3d208`](#insn-00b3d208) 範囲 `[['00b3d208', '00b3d20f']]`
  - `CONDITIONAL_JUMP` [`00b3d20c`](#insn-00b3d20c) → [`00b3d218`](#insn-00b3d218)
  - `FALL_THROUGH` [`00b3d20c`](#insn-00b3d20c) → [`00b3d210`](#insn-00b3d210)
- ブロック [`00b3d210`](#insn-00b3d210) 範囲 `[['00b3d210', '00b3d217']]`
  - `FALL_THROUGH` [`00b3d214`](#insn-00b3d214) → [`00b3d218`](#insn-00b3d218)
- ブロック [`00b3d218`](#insn-00b3d218) 範囲 `[['00b3d218', '00b3d243']]`
  - `CONDITIONAL_JUMP` [`00b3d240`](#insn-00b3d240) → [`00b3d388`](#insn-00b3d388)
  - `FALL_THROUGH` [`00b3d240`](#insn-00b3d240) → [`00b3d244`](#insn-00b3d244)
- ブロック [`00b3d244`](#insn-00b3d244) 範囲 `[['00b3d244', '00b3d247']]`
  - `FALL_THROUGH` [`00b3d244`](#insn-00b3d244) → [`00b3d248`](#insn-00b3d248)
- ブロック [`00b3d248`](#insn-00b3d248) 範囲 `[['00b3d248', '00b3d257']]`
- ブロック [`00b3d258`](#insn-00b3d258) 範囲 `[['00b3d258', '00b3d267']]`
  - `CONDITIONAL_JUMP` [`00b3d264`](#insn-00b3d264) → [`00b3d1e8`](#insn-00b3d1e8)
  - `FALL_THROUGH` [`00b3d264`](#insn-00b3d264) → [`00b3d268`](#insn-00b3d268)
- ブロック [`00b3d268`](#insn-00b3d268) 範囲 `[['00b3d268', '00b3d277']]`
  - `CONDITIONAL_JUMP` [`00b3d274`](#insn-00b3d274) → [`00b3d1f0`](#insn-00b3d1f0)
  - `FALL_THROUGH` [`00b3d274`](#insn-00b3d274) → [`00b3d278`](#insn-00b3d278)
- ブロック [`00b3d278`](#insn-00b3d278) 範囲 `[['00b3d278', '00b3d287']]`
  - `CONDITIONAL_JUMP` [`00b3d284`](#insn-00b3d284) → [`00b3d1f8`](#insn-00b3d1f8)
  - `FALL_THROUGH` [`00b3d284`](#insn-00b3d284) → [`00b3d288`](#insn-00b3d288)
- ブロック [`00b3d288`](#insn-00b3d288) 範囲 `[['00b3d288', '00b3d297']]`
  - `CONDITIONAL_JUMP` [`00b3d294`](#insn-00b3d294) → [`00b3d200`](#insn-00b3d200)
  - `FALL_THROUGH` [`00b3d294`](#insn-00b3d294) → [`00b3d298`](#insn-00b3d298)
- ブロック [`00b3d298`](#insn-00b3d298) 範囲 `[['00b3d298', '00b3d2a7']]`
  - `CONDITIONAL_JUMP` [`00b3d2a4`](#insn-00b3d2a4) → [`00b3d208`](#insn-00b3d208)
  - `FALL_THROUGH` [`00b3d2a4`](#insn-00b3d2a4) → [`00b3d2a8`](#insn-00b3d2a8)
- ブロック [`00b3d2a8`](#insn-00b3d2a8) 範囲 `[['00b3d2a8', '00b3d2b7']]`
  - `CONDITIONAL_JUMP` [`00b3d2b4`](#insn-00b3d2b4) → [`00b3d210`](#insn-00b3d210)
  - `FALL_THROUGH` [`00b3d2b4`](#insn-00b3d2b4) → [`00b3d2b8`](#insn-00b3d2b8)
- ブロック [`00b3d2b8`](#insn-00b3d2b8) 範囲 `[['00b3d2b8', '00b3d2bb']]`
  - `UNCONDITIONAL_JUMP` [`00b3d2b8`](#insn-00b3d2b8) → [`00b3d218`](#insn-00b3d218)
- ブロック [`00b3d388`](#insn-00b3d388) 範囲 `[['00b3d388', '00b3d38b']]`

## 命令位置別の参照

- [`00b3d000`](#insn-00b3d000) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3d004`](#insn-00b3d004) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3d008`](#insn-00b3d008) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3d02c`](#insn-00b3d02c) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3d038`](#insn-00b3d038) → `002b8035`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b3d040`](#insn-00b3d040) → `Stack[-0xff]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3d044`](#insn-00b3d044) → `Stack[-0xf8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3d054`](#insn-00b3d054) → `Stack[-0x10f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3d05c`](#insn-00b3d05c) → `002b8048`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b3d060`](#insn-00b3d060) → `Stack[-0xdf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3d068`](#insn-00b3d068) → `Stack[-0xd8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3d078`](#insn-00b3d078) → `Stack[-0xef]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3d07c`](#insn-00b3d07c) → `002b8e3d`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b3d080`](#insn-00b3d080) → `Stack[-0xbf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3d088`](#insn-00b3d088) → `Stack[-0xb8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3d098`](#insn-00b3d098) → `Stack[-0xcf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3d09c`](#insn-00b3d09c) → `002a2fe0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b3d0a0`](#insn-00b3d0a0) → `Stack[-0x9f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3d0a8`](#insn-00b3d0a8) → `Stack[-0x98]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3d0b4`](#insn-00b3d0b4) → `Stack[-0xaf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3d0b8`](#insn-00b3d0b8) → `002ac643`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b3d0c0`](#insn-00b3d0c0) → `Stack[-0x7f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3d0c8`](#insn-00b3d0c8) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3d0d4`](#insn-00b3d0d4) → `Stack[-0x8f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3d0d8`](#insn-00b3d0d8) → `002a0f50`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b3d0e0`](#insn-00b3d0e0) → `Stack[-0x5f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3d0e8`](#insn-00b3d0e8) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3d0f4`](#insn-00b3d0f4) → `Stack[-0x6f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3d0f8`](#insn-00b3d0f8) → `002a3f87`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b3d0fc`](#insn-00b3d0fc) → `Stack[-0x110]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3d100`](#insn-00b3d100) → `Stack[-0xf0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3d104`](#insn-00b3d104) → `Stack[-0xd0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3d108`](#insn-00b3d108) → `Stack[-0xb0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3d10c`](#insn-00b3d10c) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3d110`](#insn-00b3d110) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3d114`](#insn-00b3d114) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3d11c`](#insn-00b3d11c) → `Stack[-0x118]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3d120`](#insn-00b3d120) → `Stack[-0xfd]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3d124`](#insn-00b3d124) → `Stack[-0xdd]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3d128`](#insn-00b3d128) → `Stack[-0xbd]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3d12c`](#insn-00b3d12c) → `Stack[-0x9d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3d130`](#insn-00b3d130) → `Stack[-0x7d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3d134`](#insn-00b3d134) → `Stack[-0x5d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3d138`](#insn-00b3d138) → `Stack[-0x3f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3d13c`](#insn-00b3d13c) → `Stack[-0x4f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3d140`](#insn-00b3d140) → `Stack[-0x3d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3d144`](#insn-00b3d144) → `01126390`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b3d148`](#insn-00b3d148) → `01126388`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b3d14c`](#insn-00b3d14c) → `01126380`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b3d14c`](#insn-00b3d14c) → `01126388`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b3d158`](#insn-00b3d158) → `01126380`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b3d15c`](#insn-00b3d15c) → [`0043bb58`](../0043b/0043bb58.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bb58` · 推定シンボル `None` · 推定型 `None`
- [`00b3d160`](#insn-00b3d160) → `01126388`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b3d16c`](#insn-00b3d16c) → `01126380`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b3d170`](#insn-00b3d170) → [`0043bb58`](../0043b/0043bb58.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bb58` · 推定シンボル `None` · 推定型 `None`
- [`00b3d174`](#insn-00b3d174) → `01126388`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b3d180`](#insn-00b3d180) → `01126380`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b3d184`](#insn-00b3d184) → [`0043bb58`](../0043b/0043bb58.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bb58` · 推定シンボル `None` · 推定型 `None`
- [`00b3d188`](#insn-00b3d188) → `01126388`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b3d194`](#insn-00b3d194) → `01126380`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b3d198`](#insn-00b3d198) → [`0043bb58`](../0043b/0043bb58.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bb58` · 推定シンボル `None` · 推定型 `None`
- [`00b3d19c`](#insn-00b3d19c) → `01126388`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b3d1a8`](#insn-00b3d1a8) → `01126380`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b3d1ac`](#insn-00b3d1ac) → [`0043bb58`](../0043b/0043bb58.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bb58` · 推定シンボル `None` · 推定型 `None`
- [`00b3d1b0`](#insn-00b3d1b0) → `01126388`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b3d1bc`](#insn-00b3d1bc) → `01126380`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b3d1c0`](#insn-00b3d1c0) → [`0043bb58`](../0043b/0043bb58.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bb58` · 推定シンボル `None` · 推定型 `None`
- [`00b3d1c4`](#insn-00b3d1c4) → `01126388`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b3d1d0`](#insn-00b3d1d0) → `01126380`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b3d1d4`](#insn-00b3d1d4) → [`0043bb58`](../0043b/0043bb58.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bb58` · 推定シンボル `None` · 推定型 `None`
- [`00b3d1d8`](#insn-00b3d1d8) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3d1dc`](#insn-00b3d1dc) → [`00b3d258`](#insn-00b3d258) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3d1e0`](#insn-00b3d1e0) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3d1e4`](#insn-00b3d1e4) → [`00b3d268`](#insn-00b3d268) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3d1e8`](#insn-00b3d1e8) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3d1ec`](#insn-00b3d1ec) → [`00b3d278`](#insn-00b3d278) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3d1f0`](#insn-00b3d1f0) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3d1f4`](#insn-00b3d1f4) → [`00b3d288`](#insn-00b3d288) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3d1f8`](#insn-00b3d1f8) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3d1fc`](#insn-00b3d1fc) → [`00b3d298`](#insn-00b3d298) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3d200`](#insn-00b3d200) → `Stack[-0xf0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3d204`](#insn-00b3d204) → [`00b3d2a8`](#insn-00b3d2a8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3d208`](#insn-00b3d208) → `Stack[-0x110]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3d20c`](#insn-00b3d20c) → [`00b3d218`](#insn-00b3d218) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3d210`](#insn-00b3d210) → `Stack[-0x100]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3d214`](#insn-00b3d214) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00b3d21c`](#insn-00b3d21c) → [`0043b1d0`](../0043b/0043b1d0.md) · `PARAM` · `ANALYSIS` · 関数 `0043b1d0` · 推定シンボル `None` · 推定型 `None`
- [`00b3d224`](#insn-00b3d224) → `01126380`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b3d22c`](#insn-00b3d22c) → `00c64030`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00b3d230`](#insn-00b3d230) → [`00c58ed0`](../00c58/00c58ed0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58ed0` · 推定シンボル `None` · 推定型 `None`
- [`00b3d238`](#insn-00b3d238) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3d240`](#insn-00b3d240) → [`00b3d388`](#insn-00b3d388) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3d244`](#insn-00b3d244) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3d248`](#insn-00b3d248) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3d24c`](#insn-00b3d24c) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3d258`](#insn-00b3d258) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3d25c`](#insn-00b3d25c) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00b3d260`](#insn-00b3d260) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3d264`](#insn-00b3d264) → [`00b3d1e8`](#insn-00b3d1e8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3d268`](#insn-00b3d268) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3d26c`](#insn-00b3d26c) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00b3d270`](#insn-00b3d270) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3d274`](#insn-00b3d274) → [`00b3d1f0`](#insn-00b3d1f0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3d278`](#insn-00b3d278) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3d27c`](#insn-00b3d27c) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00b3d280`](#insn-00b3d280) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3d284`](#insn-00b3d284) → [`00b3d1f8`](#insn-00b3d1f8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3d288`](#insn-00b3d288) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3d28c`](#insn-00b3d28c) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00b3d290`](#insn-00b3d290) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3d294`](#insn-00b3d294) → [`00b3d200`](#insn-00b3d200) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3d298`](#insn-00b3d298) → `Stack[-0xc0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3d29c`](#insn-00b3d29c) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00b3d2a0`](#insn-00b3d2a0) → `Stack[-0xf0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3d2a4`](#insn-00b3d2a4) → [`00b3d208`](#insn-00b3d208) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3d2a8`](#insn-00b3d2a8) → `Stack[-0xe0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3d2ac`](#insn-00b3d2ac) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00b3d2b0`](#insn-00b3d2b0) → `Stack[-0x110]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3d2b4`](#insn-00b3d2b4) → [`00b3d210`](#insn-00b3d210) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3d2b8`](#insn-00b3d2b8) → [`00b3d218`](#insn-00b3d218) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3d388`](#insn-00b3d388) → [`00c58f80`](../00c58/00c58f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f80` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b3d000`](#insn-00b3d000)

~~~json
{
  "source": "00b3d000",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3d004`](#insn-00b3d004)

~~~json
{
  "source": "00b3d004",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3d008`](#insn-00b3d008)

~~~json
{
  "source": "00b3d008",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3d02c`](#insn-00b3d02c)

~~~json
{
  "source": "00b3d02c",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3d038`](#insn-00b3d038)

~~~json
{
  "source": "00b3d038",
  "target": "002b8035",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b8035",
  "offset": 0,
  "size": 19,
  "datatype": "string",
  "bytes": "43676b496a4d33795f5a516145414951416700",
  "capture_start": "002b8035",
  "capture_bytes": 19,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b3d040`](#insn-00b3d040)

~~~json
{
  "source": "00b3d040",
  "target": "Stack[-0xff]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3d044`](#insn-00b3d044)

~~~json
{
  "source": "00b3d044",
  "target": "Stack[-0xf8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3d054`](#insn-00b3d054)

~~~json
{
  "source": "00b3d054",
  "target": "Stack[-0x10f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3d05c`](#insn-00b3d05c)

~~~json
{
  "source": "00b3d05c",
  "target": "002b8048",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b8048",
  "offset": 0,
  "size": 19,
  "datatype": "string",
  "bytes": "43676b496a4d33795f5a516145414951424100",
  "capture_start": "002b8048",
  "capture_bytes": 19,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b3d060`](#insn-00b3d060)

~~~json
{
  "source": "00b3d060",
  "target": "Stack[-0xdf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3d068`](#insn-00b3d068)

~~~json
{
  "source": "00b3d068",
  "target": "Stack[-0xd8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3d078`](#insn-00b3d078)

~~~json
{
  "source": "00b3d078",
  "target": "Stack[-0xef]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3d07c`](#insn-00b3d07c)

~~~json
{
  "source": "00b3d07c",
  "target": "002b8e3d",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b8e3d",
  "offset": 0,
  "size": 19,
  "datatype": "string",
  "bytes": "43676b496a4d33795f5a516145414951426700",
  "capture_start": "002b8e3d",
  "capture_bytes": 19,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b3d080`](#insn-00b3d080)

~~~json
{
  "source": "00b3d080",
  "target": "Stack[-0xbf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3d088`](#insn-00b3d088)

~~~json
{
  "source": "00b3d088",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3d098`](#insn-00b3d098)

~~~json
{
  "source": "00b3d098",
  "target": "Stack[-0xcf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3d09c`](#insn-00b3d09c)

~~~json
{
  "source": "00b3d09c",
  "target": "002a2fe0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a2fe0",
  "offset": 0,
  "size": 19,
  "datatype": "string",
  "bytes": "43676b496a4d33795f5a516145414951417700",
  "capture_start": "002a2fe0",
  "capture_bytes": 19,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b3d0a0`](#insn-00b3d0a0)

~~~json
{
  "source": "00b3d0a0",
  "target": "Stack[-0x9f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3d0a8`](#insn-00b3d0a8)

~~~json
{
  "source": "00b3d0a8",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3d0b4`](#insn-00b3d0b4)

~~~json
{
  "source": "00b3d0b4",
  "target": "Stack[-0xaf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3d0b8`](#insn-00b3d0b8)

~~~json
{
  "source": "00b3d0b8",
  "target": "002ac643",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002ac643",
  "offset": 0,
  "size": 19,
  "datatype": "string",
  "bytes": "43676b496a4d33795f5a516145414951425100",
  "capture_start": "002ac643",
  "capture_bytes": 19,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b3d0c0`](#insn-00b3d0c0)

~~~json
{
  "source": "00b3d0c0",
  "target": "Stack[-0x7f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3d0c8`](#insn-00b3d0c8)

~~~json
{
  "source": "00b3d0c8",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3d0d4`](#insn-00b3d0d4)

~~~json
{
  "source": "00b3d0d4",
  "target": "Stack[-0x8f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3d0d8`](#insn-00b3d0d8)

~~~json
{
  "source": "00b3d0d8",
  "target": "002a0f50",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a0f50",
  "offset": 0,
  "size": 19,
  "datatype": "string",
  "bytes": "43676b496a4d33795f5a516145414951427700",
  "capture_start": "002a0f50",
  "capture_bytes": 19,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b3d0e0`](#insn-00b3d0e0)

~~~json
{
  "source": "00b3d0e0",
  "target": "Stack[-0x5f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3d0e8`](#insn-00b3d0e8)

~~~json
{
  "source": "00b3d0e8",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3d0f4`](#insn-00b3d0f4)

~~~json
{
  "source": "00b3d0f4",
  "target": "Stack[-0x6f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3d0f8`](#insn-00b3d0f8)

~~~json
{
  "source": "00b3d0f8",
  "target": "002a3f87",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a3f87",
  "offset": 0,
  "size": 19,
  "datatype": "string",
  "bytes": "43676b496a4d33795f5a516145414951434100",
  "capture_start": "002a3f87",
  "capture_bytes": 19,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b3d0fc`](#insn-00b3d0fc)

~~~json
{
  "source": "00b3d0fc",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3d100`](#insn-00b3d100)

~~~json
{
  "source": "00b3d100",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3d104`](#insn-00b3d104)

~~~json
{
  "source": "00b3d104",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3d108`](#insn-00b3d108)

~~~json
{
  "source": "00b3d108",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3d10c`](#insn-00b3d10c)

~~~json
{
  "source": "00b3d10c",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3d110`](#insn-00b3d110)

~~~json
{
  "source": "00b3d110",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3d114`](#insn-00b3d114)

~~~json
{
  "source": "00b3d114",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3d11c`](#insn-00b3d11c)

~~~json
{
  "source": "00b3d11c",
  "target": "Stack[-0x118]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3d120`](#insn-00b3d120)

~~~json
{
  "source": "00b3d120",
  "target": "Stack[-0xfd]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3d124`](#insn-00b3d124)

~~~json
{
  "source": "00b3d124",
  "target": "Stack[-0xdd]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3d128`](#insn-00b3d128)

~~~json
{
  "source": "00b3d128",
  "target": "Stack[-0xbd]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3d12c`](#insn-00b3d12c)

~~~json
{
  "source": "00b3d12c",
  "target": "Stack[-0x9d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3d130`](#insn-00b3d130)

~~~json
{
  "source": "00b3d130",
  "target": "Stack[-0x7d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3d134`](#insn-00b3d134)

~~~json
{
  "source": "00b3d134",
  "target": "Stack[-0x5d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3d138`](#insn-00b3d138)

~~~json
{
  "source": "00b3d138",
  "target": "Stack[-0x3f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3d13c`](#insn-00b3d13c)

~~~json
{
  "source": "00b3d13c",
  "target": "Stack[-0x4f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3d140`](#insn-00b3d140)

~~~json
{
  "source": "00b3d140",
  "target": "Stack[-0x3d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3d144`](#insn-00b3d144)

~~~json
{
  "source": "00b3d144",
  "target": "01126390",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126390",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b3d148`](#insn-00b3d148)

~~~json
{
  "source": "00b3d148",
  "target": "01126388",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126388",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b3d14c`](#insn-00b3d14c)

~~~json
{
  "source": "00b3d14c",
  "target": "01126380",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126380",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b3d14c`](#insn-00b3d14c)

~~~json
{
  "source": "00b3d14c",
  "target": "01126388",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126388",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b3d158`](#insn-00b3d158)

~~~json
{
  "source": "00b3d158",
  "target": "01126380",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126380",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b3d15c`](#insn-00b3d15c)

~~~json
{
  "source": "00b3d15c",
  "target": "0043bb58",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b3d160`](#insn-00b3d160)

~~~json
{
  "source": "00b3d160",
  "target": "01126388",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126388",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b3d16c`](#insn-00b3d16c)

~~~json
{
  "source": "00b3d16c",
  "target": "01126380",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126380",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b3d170`](#insn-00b3d170)

~~~json
{
  "source": "00b3d170",
  "target": "0043bb58",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b3d174`](#insn-00b3d174)

~~~json
{
  "source": "00b3d174",
  "target": "01126388",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126388",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b3d180`](#insn-00b3d180)

~~~json
{
  "source": "00b3d180",
  "target": "01126380",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126380",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b3d184`](#insn-00b3d184)

~~~json
{
  "source": "00b3d184",
  "target": "0043bb58",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b3d188`](#insn-00b3d188)

~~~json
{
  "source": "00b3d188",
  "target": "01126388",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126388",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b3d194`](#insn-00b3d194)

~~~json
{
  "source": "00b3d194",
  "target": "01126380",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126380",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b3d198`](#insn-00b3d198)

~~~json
{
  "source": "00b3d198",
  "target": "0043bb58",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b3d19c`](#insn-00b3d19c)

~~~json
{
  "source": "00b3d19c",
  "target": "01126388",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126388",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b3d1a8`](#insn-00b3d1a8)

~~~json
{
  "source": "00b3d1a8",
  "target": "01126380",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126380",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b3d1ac`](#insn-00b3d1ac)

~~~json
{
  "source": "00b3d1ac",
  "target": "0043bb58",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b3d1b0`](#insn-00b3d1b0)

~~~json
{
  "source": "00b3d1b0",
  "target": "01126388",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126388",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b3d1bc`](#insn-00b3d1bc)

~~~json
{
  "source": "00b3d1bc",
  "target": "01126380",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126380",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b3d1c0`](#insn-00b3d1c0)

~~~json
{
  "source": "00b3d1c0",
  "target": "0043bb58",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b3d1c4`](#insn-00b3d1c4)

~~~json
{
  "source": "00b3d1c4",
  "target": "01126388",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126388",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b3d1d0`](#insn-00b3d1d0)

~~~json
{
  "source": "00b3d1d0",
  "target": "01126380",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126380",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b3d1d4`](#insn-00b3d1d4)

~~~json
{
  "source": "00b3d1d4",
  "target": "0043bb58",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b3d1d8`](#insn-00b3d1d8)

~~~json
{
  "source": "00b3d1d8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3d1dc`](#insn-00b3d1dc)

~~~json
{
  "source": "00b3d1dc",
  "target": "00b3d258",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3d1e0`](#insn-00b3d1e0)

~~~json
{
  "source": "00b3d1e0",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3d1e4`](#insn-00b3d1e4)

~~~json
{
  "source": "00b3d1e4",
  "target": "00b3d268",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3d1e8`](#insn-00b3d1e8)

~~~json
{
  "source": "00b3d1e8",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3d1ec`](#insn-00b3d1ec)

~~~json
{
  "source": "00b3d1ec",
  "target": "00b3d278",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3d1f0`](#insn-00b3d1f0)

~~~json
{
  "source": "00b3d1f0",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3d1f4`](#insn-00b3d1f4)

~~~json
{
  "source": "00b3d1f4",
  "target": "00b3d288",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3d1f8`](#insn-00b3d1f8)

~~~json
{
  "source": "00b3d1f8",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3d1fc`](#insn-00b3d1fc)

~~~json
{
  "source": "00b3d1fc",
  "target": "00b3d298",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3d200`](#insn-00b3d200)

~~~json
{
  "source": "00b3d200",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3d204`](#insn-00b3d204)

~~~json
{
  "source": "00b3d204",
  "target": "00b3d2a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3d208`](#insn-00b3d208)

~~~json
{
  "source": "00b3d208",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3d20c`](#insn-00b3d20c)

~~~json
{
  "source": "00b3d20c",
  "target": "00b3d218",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3d210`](#insn-00b3d210)

~~~json
{
  "source": "00b3d210",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3d214`](#insn-00b3d214)

~~~json
{
  "source": "00b3d214",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b3d21c`](#insn-00b3d21c)

~~~json
{
  "source": "00b3d21c",
  "target": "0043b1d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b3d224`](#insn-00b3d224)

~~~json
{
  "source": "00b3d224",
  "target": "01126380",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126380",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b3d22c`](#insn-00b3d22c)

~~~json
{
  "source": "00b3d22c",
  "target": "00c64030",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c64030",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00b3d230`](#insn-00b3d230)

~~~json
{
  "source": "00b3d230",
  "target": "00c58ed0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b3d238`](#insn-00b3d238)

~~~json
{
  "source": "00b3d238",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3d240`](#insn-00b3d240)

~~~json
{
  "source": "00b3d240",
  "target": "00b3d388",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3d244`](#insn-00b3d244)

~~~json
{
  "source": "00b3d244",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3d248`](#insn-00b3d248)

~~~json
{
  "source": "00b3d248",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3d24c`](#insn-00b3d24c)

~~~json
{
  "source": "00b3d24c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3d258`](#insn-00b3d258)

~~~json
{
  "source": "00b3d258",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3d25c`](#insn-00b3d25c)

~~~json
{
  "source": "00b3d25c",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b3d260`](#insn-00b3d260)

~~~json
{
  "source": "00b3d260",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3d264`](#insn-00b3d264)

~~~json
{
  "source": "00b3d264",
  "target": "00b3d1e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3d268`](#insn-00b3d268)

~~~json
{
  "source": "00b3d268",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3d26c`](#insn-00b3d26c)

~~~json
{
  "source": "00b3d26c",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b3d270`](#insn-00b3d270)

~~~json
{
  "source": "00b3d270",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3d274`](#insn-00b3d274)

~~~json
{
  "source": "00b3d274",
  "target": "00b3d1f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3d278`](#insn-00b3d278)

~~~json
{
  "source": "00b3d278",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3d27c`](#insn-00b3d27c)

~~~json
{
  "source": "00b3d27c",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b3d280`](#insn-00b3d280)

~~~json
{
  "source": "00b3d280",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3d284`](#insn-00b3d284)

~~~json
{
  "source": "00b3d284",
  "target": "00b3d1f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3d288`](#insn-00b3d288)

~~~json
{
  "source": "00b3d288",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3d28c`](#insn-00b3d28c)

~~~json
{
  "source": "00b3d28c",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b3d290`](#insn-00b3d290)

~~~json
{
  "source": "00b3d290",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3d294`](#insn-00b3d294)

~~~json
{
  "source": "00b3d294",
  "target": "00b3d200",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3d298`](#insn-00b3d298)

~~~json
{
  "source": "00b3d298",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3d29c`](#insn-00b3d29c)

~~~json
{
  "source": "00b3d29c",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b3d2a0`](#insn-00b3d2a0)

~~~json
{
  "source": "00b3d2a0",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3d2a4`](#insn-00b3d2a4)

~~~json
{
  "source": "00b3d2a4",
  "target": "00b3d208",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3d2a8`](#insn-00b3d2a8)

~~~json
{
  "source": "00b3d2a8",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3d2ac`](#insn-00b3d2ac)

~~~json
{
  "source": "00b3d2ac",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b3d2b0`](#insn-00b3d2b0)

~~~json
{
  "source": "00b3d2b0",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3d2b4`](#insn-00b3d2b4)

~~~json
{
  "source": "00b3d2b4",
  "target": "00b3d210",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3d2b8`](#insn-00b3d2b8)

~~~json
{
  "source": "00b3d2b8",
  "target": "00b3d218",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3d388`](#insn-00b3d388)

~~~json
{
  "source": "00b3d388",
  "target": "00c58f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
