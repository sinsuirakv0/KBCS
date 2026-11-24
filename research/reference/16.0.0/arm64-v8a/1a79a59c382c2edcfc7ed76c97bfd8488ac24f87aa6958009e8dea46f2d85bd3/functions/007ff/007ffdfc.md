# 007ffdfc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0135.md#review-98596d65e679241eb64d5cc96060bb47)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `007ffe3c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ffe3c.md) · 移動量 `+0x40`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0041.md#compare-808a33e482360b45ee9e11e2b9039205)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "007ffdfc",
  "name": "_INIT_146",
  "size": 708,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8f2b95bd353a26f37677cd5d8778b0331386e900da221c8868cd78967155186f",
  "source_text_sha256": "8f2b95bd353a26f37677cd5d8778b0331386e900da221c8868cd78967155186f",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "007ffdfc",
        "008000bb"
      ],
      [
        "00800188",
        "0080018b"
      ]
    ],
    "bytes_sha256": "94519506b3d122debf3a7a3da3107a6752db06e492f1365d96103717b65664dd",
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

## 疑似コード / UTF-8 6130 bytes

~~~c

/* WARNING: Type propagation algorithm not settling */

void _INIT_146(void)

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
  DAT_00ca7bf8 = 0;
  DAT_00ca7bf0 = 0;
  DAT_00ca7be8 = &DAT_00ca7bf0;
  FUN_0043b7b8(&DAT_00ca7be8,&DAT_00ca7bf0,local_118,local_118);
  FUN_0043b7b8(&DAT_00ca7be8,&DAT_00ca7bf0,local_f8,local_f8);
                    /* try { // try from 007fff7c to 008fffc7 has its CatchHandler @ 007fff7c
                       catch() { ... } // from try @ 007fff7c with catch @ 007fff7c
                       catch() { ... } // from try @ 007fffd0 with catch @ 007fff7c
                       catch() { ... } // from try @ 00800008 with catch @ 007fff7c */
  FUN_0043b7b8(&DAT_00ca7be8,&DAT_00ca7bf0,local_d8,local_d8);
  FUN_0043b7b8(&DAT_00ca7be8,&DAT_00ca7bf0,local_b8,local_b8);
  FUN_0043b7b8(&DAT_00ca7be8,&DAT_00ca7bf0,local_98,local_98);
  FUN_0043b7b8(&DAT_00ca7be8,&DAT_00ca7bf0,local_78,local_78);
                    /* try { // try from 007fffc8 to 008fffcf has its CatchHandler @ 00800008 */
                    /* try { // try from 007fffd0 to 008fffff has its CatchHandler @ 007fff7c */
  FUN_0043b7b8(&DAT_00ca7be8,&DAT_00ca7bf0,local_58,local_58);
  if ((local_50 & 1) != 0) {
    _ZdlPv((void *)CONCAT44(uStack_3c,CONCAT13(uStack_3d,CONCAT21(uStack_3f,cStack_40))));
  }
  if ((local_70 & 1) != 0) {
    _ZdlPv((void *)CONCAT44(uStack_5c,CONCAT13(uStack_5d,CONCAT21(uStack_5f,cStack_60))));
                    /* try { // try from 00800070 to 00900077 has its CatchHandler @ 008000ac */
  }
  if ((local_90 & 1) != 0) {
                    /* try { // try from 00800078 to 009000a3 has its CatchHandler @ 00800030 */
    _ZdlPv((void *)CONCAT44(uStack_7c,CONCAT13(uStack_7d,CONCAT21(uStack_7f,cStack_80))));
  }
  if ((local_b0 & 1) != 0) {
    _ZdlPv((void *)CONCAT44(uStack_9c,CONCAT13(uStack_9d,CONCAT21(uStack_9f,cStack_a0))));
  }
  if ((local_d0 & 1) != 0) {
    _ZdlPv((void *)CONCAT44(uStack_bc,CONCAT13(uStack_bd,CONCAT21(uStack_bf,cStack_c0))));
  }
                    /* try { // try from 008000a4 to 009000ab has its CatchHandler @ 008000ac */
  if ((local_f0 & 1) != 0) {
                    /* catch() { ... } // from try @ 00800070 with catch @ 008000ac
                       catch() { ... } // from try @ 008000a4 with catch @ 008000ac
                       try { // try from 008000ac to 009000cb has its CatchHandler @ 00800030 */
    _ZdlPv((void *)CONCAT44(uStack_dc,CONCAT13(uStack_dd,CONCAT21(uStack_df,cStack_e0))));
  }
  if ((local_110 & 1) != 0) {
    _ZdlPv((void *)CONCAT44(uStack_fc,CONCAT13(uStack_fd,CONCAT21(uStack_ff,cStack_100))));
  }
                    /* catch() { ... } // from try @ 00800078 with catch @ 00800030
                       catch() { ... } // from try @ 008000ac with catch @ 00800030 */
  __cxa_atexit(FUN_0043ae30,&DAT_00ca7be8,&PTR_LOOP_00c62b90);
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
<a id="insn-007ffdfc"></a> `007ffdfc` | `ff 83 04 d1` | sub sp,sp,#0x120 | `FALL_THROUGH`
<a id="insn-007ffe00"></a> `007ffe00` | `fd 7b 0f a9` | stp x29,x30,[sp, #0xf0] | `FALL_THROUGH`
<a id="insn-007ffe04"></a> `007ffe04` | `fc 57 10 a9` | stp x28,x21,[sp, #0x100] | `FALL_THROUGH`
<a id="insn-007ffe08"></a> `007ffe08` | `f4 4f 11 a9` | stp x20,x19,[sp, #0x110] | `FALL_THROUGH`
<a id="insn-007ffe0c"></a> `007ffe0c` | `fd c3 03 91` | add x29,sp,#0xf0 | `FALL_THROUGH`
<a id="insn-007ffe10"></a> `007ffe10` | `55 d0 3b d5` | mrs x21,tpidr_el0 | `FALL_THROUGH`
<a id="insn-007ffe14"></a> `007ffe14` | `2a e8 8c 52` | mov w10,#0x6741 | `FALL_THROUGH`
<a id="insn-007ffe18"></a> `007ffe18` | `f4 23 00 91` | add x20,sp,#0x8 | `FALL_THROUGH`
<a id="insn-007ffe1c"></a> `007ffe1c` | `a9 16 40 f9` | ldr x9,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-007ffe20"></a> `007ffe20` | `88 04 80 52` | mov w8,#0x24 | `FALL_THROUGH`
<a id="insn-007ffe24"></a> `007ffe24` | `53 25 00 90` | adrp x19,0xca7000 | `FALL_THROUGH`
<a id="insn-007ffe28"></a> `007ffe28` | `73 a2 2f 91` | add x19,x19,#0xbe8 | `FALL_THROUGH`
<a id="insn-007ffe2c"></a> `007ffe2c` | `a9 83 1f f8` | stur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-007ffe30"></a> `007ffe30` | `c9 d5 ff 90` | adrp x9,0x2b7000 | `FALL_THROUGH`
<a id="insn-007ffe34"></a> `007ffe34` | `29 99 3b 91` | add x9,x9,#0xee6 | `FALL_THROUGH`
<a id="insn-007ffe38"></a> `007ffe38` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-007ffe3c"></a> `007ffe3c` | `29 00 80 52` | mov w9,#0x1 | `FALL_THROUGH`
<a id="insn-007ffe40"></a> `007ffe40` | `ea 13 02 78` | sturh w10,[sp, #0x21] | `FALL_THROUGH`
<a id="insn-007ffe44"></a> `007ffe44` | `e9 2b 00 b9` | str w9,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-007ffe48"></a> `007ffe48` | `49 28 88 52` | mov w9,#0x4142 | `FALL_THROUGH`
<a id="insn-007ffe4c"></a> `007ffe4c` | `ca d5 ff 90` | adrp x10,0x2b7000 | `FALL_THROUGH`
<a id="insn-007ffe50"></a> `007ffe50` | `4a e5 3b 91` | add x10,x10,#0xef9 | `FALL_THROUGH`
<a id="insn-007ffe54"></a> `007ffe54` | `e0 13 81 3c` | stur q0,[sp, #0x11] | `FALL_THROUGH`
<a id="insn-007ffe58"></a> `007ffe58` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-007ffe5c"></a> `007ffe5c` | `40 01 c0 3d` | ldr q0,[x10] | `FALL_THROUGH`
<a id="insn-007ffe60"></a> `007ffe60` | `e9 13 04 78` | sturh w9,[sp, #0x41] | `FALL_THROUGH`
<a id="insn-007ffe64"></a> `007ffe64` | `49 00 80 52` | mov w9,#0x2 | `FALL_THROUGH`
<a id="insn-007ffe68"></a> `007ffe68` | `e9 4b 00 b9` | str w9,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-007ffe6c"></a> `007ffe6c` | `49 e8 8c 52` | mov w9,#0x6742 | `FALL_THROUGH`
<a id="insn-007ffe70"></a> `007ffe70` | `ca d5 ff b0` | adrp x10,0x2b8000 | `FALL_THROUGH`
<a id="insn-007ffe74"></a> `007ffe74` | `4a 09 36 91` | add x10,x10,#0xd82 | `FALL_THROUGH`
<a id="insn-007ffe78"></a> `007ffe78` | `e0 13 83 3c` | stur q0,[sp, #0x31] | `FALL_THROUGH`
<a id="insn-007ffe7c"></a> `007ffe7c` | `40 01 c0 3d` | ldr q0,[x10] | `FALL_THROUGH`
<a id="insn-007ffe80"></a> `007ffe80` | `e9 13 06 78` | sturh w9,[sp, #0x61] | `FALL_THROUGH`
<a id="insn-007ffe84"></a> `007ffe84` | `69 00 80 52` | mov w9,#0x3 | `FALL_THROUGH`
<a id="insn-007ffe88"></a> `007ffe88` | `e9 6b 00 b9` | str w9,[sp, #0x68] | `FALL_THROUGH`
<a id="insn-007ffe8c"></a> `007ffe8c` | `29 e8 8e 52` | mov w9,#0x7741 | `FALL_THROUGH`
<a id="insn-007ffe90"></a> `007ffe90` | `0a d5 ff f0` | adrp x10,0x2a2000 | `FALL_THROUGH`
<a id="insn-007ffe94"></a> `007ffe94` | `4a 55 3a 91` | add x10,x10,#0xe95 | `FALL_THROUGH`
<a id="insn-007ffe98"></a> `007ffe98` | `e0 13 85 3c` | stur q0,[sp, #0x51] | `FALL_THROUGH`
<a id="insn-007ffe9c"></a> `007ffe9c` | `40 01 c0 3d` | ldr q0,[x10] | `FALL_THROUGH`
<a id="insn-007ffea0"></a> `007ffea0` | `e9 13 08 78` | sturh w9,[sp, #0x81] | `FALL_THROUGH`
<a id="insn-007ffea4"></a> `007ffea4` | `89 00 80 52` | mov w9,#0x4 | `FALL_THROUGH`
<a id="insn-007ffea8"></a> `007ffea8` | `e9 8b 00 b9` | str w9,[sp, #0x88] | `FALL_THROUGH`
<a id="insn-007ffeac"></a> `007ffeac` | `69 d5 ff b0` | adrp x9,0x2ac000 | `FALL_THROUGH`
<a id="insn-007ffeb0"></a> `007ffeb0` | `29 49 16 91` | add x9,x9,#0x592 | `FALL_THROUGH`
<a id="insn-007ffeb4"></a> `007ffeb4` | `e0 13 87 3c` | stur q0,[sp, #0x71] | `FALL_THROUGH`
<a id="insn-007ffeb8"></a> `007ffeb8` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-007ffebc"></a> `007ffebc` | `49 28 8a 52` | mov w9,#0x5142 | `FALL_THROUGH`
<a id="insn-007ffec0"></a> `007ffec0` | `89 92 09 78` | sturh w9,[x20, #0x99] | `FALL_THROUGH`
<a id="insn-007ffec4"></a> `007ffec4` | `a9 00 80 52` | mov w9,#0x5 | `FALL_THROUGH`
<a id="insn-007ffec8"></a> `007ffec8` | `e9 ab 00 b9` | str w9,[sp, #0xa8] | `FALL_THROUGH`
<a id="insn-007ffecc"></a> `007ffecc` | `09 d5 ff b0` | adrp x9,0x2a0000 | `FALL_THROUGH`
<a id="insn-007ffed0"></a> `007ffed0` | `29 41 3a 91` | add x9,x9,#0xe90 | `FALL_THROUGH`
<a id="insn-007ffed4"></a> `007ffed4` | `80 92 88 3c` | stur q0,[x20, #0x89] | `FALL_THROUGH`
<a id="insn-007ffed8"></a> `007ffed8` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-007ffedc"></a> `007ffedc` | `49 e8 8e 52` | mov w9,#0x7742 | `FALL_THROUGH`
<a id="insn-007ffee0"></a> `007ffee0` | `89 92 0b 78` | sturh w9,[x20, #0xb9] | `FALL_THROUGH`
<a id="insn-007ffee4"></a> `007ffee4` | `c9 00 80 52` | mov w9,#0x6 | `FALL_THROUGH`
<a id="insn-007ffee8"></a> `007ffee8` | `e9 cb 00 b9` | str w9,[sp, #0xc8] | `FALL_THROUGH`
<a id="insn-007ffeec"></a> `007ffeec` | `29 d5 ff 90` | adrp x9,0x2a3000 | `FALL_THROUGH`
<a id="insn-007ffef0"></a> `007ffef0` | `29 f1 38 91` | add x9,x9,#0xe3c | `FALL_THROUGH`
<a id="insn-007ffef4"></a> `007ffef4` | `80 92 8a 3c` | stur q0,[x20, #0xa9] | `FALL_THROUGH`
<a id="insn-007ffef8"></a> `007ffef8` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-007ffefc"></a> `007ffefc` | `e8 43 00 39` | strb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-007fff00"></a> `007fff00` | `e8 c3 00 39` | strb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-007fff04"></a> `007fff04` | `e8 43 01 39` | strb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-007fff08"></a> `007fff08` | `e8 c3 01 39` | strb w8,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-007fff0c"></a> `007fff0c` | `e8 43 02 39` | strb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-007fff10"></a> `007fff10` | `e8 c3 02 39` | strb w8,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-007fff14"></a> `007fff14` | `e8 43 03 39` | strb w8,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-007fff18"></a> `007fff18` | `68 28 88 52` | mov w8,#0x4143 | `FALL_THROUGH`
<a id="insn-007fff1c"></a> `007fff1c` | `ff 0b 00 b9` | str wzr,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-007fff20"></a> `007fff20` | `ff 8f 00 39` | strb wzr,[sp, #0x23] | `FALL_THROUGH`
<a id="insn-007fff24"></a> `007fff24` | `ff 0f 01 39` | strb wzr,[sp, #0x43] | `FALL_THROUGH`
<a id="insn-007fff28"></a> `007fff28` | `ff 8f 01 39` | strb wzr,[sp, #0x63] | `FALL_THROUGH`
<a id="insn-007fff2c"></a> `007fff2c` | `ff 0f 02 39` | strb wzr,[sp, #0x83] | `FALL_THROUGH`
<a id="insn-007fff30"></a> `007fff30` | `ff 8f 02 39` | strb wzr,[sp, #0xa3] | `FALL_THROUGH`
<a id="insn-007fff34"></a> `007fff34` | `ff 0f 03 39` | strb wzr,[sp, #0xc3] | `FALL_THROUGH`
<a id="insn-007fff38"></a> `007fff38` | `88 92 0d 78` | sturh w8,[x20, #0xd9] | `FALL_THROUGH`
<a id="insn-007fff3c"></a> `007fff3c` | `80 92 8c 3c` | stur q0,[x20, #0xc9] | `FALL_THROUGH`
<a id="insn-007fff40"></a> `007fff40` | `ff 8f 03 39` | strb wzr,[sp, #0xe3] | `FALL_THROUGH`
<a id="insn-007fff44"></a> `007fff44` | `7f 0a 00 f9` | str xzr,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-007fff48"></a> `007fff48` | `3f 8c 00 f8` | str xzr,[x1, #0x8]! | `FALL_THROUGH`
<a id="insn-007fff4c"></a> `007fff4c` | `61 02 00 f9` | str x1,[x19] | `FALL_THROUGH`
<a id="insn-007fff50"></a> `007fff50` | `e2 23 00 91` | add x2,sp,#0x8 | `FALL_THROUGH`
<a id="insn-007fff54"></a> `007fff54` | `e3 23 00 91` | add x3,sp,#0x8 | `FALL_THROUGH`
<a id="insn-007fff58"></a> `007fff58` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-007fff5c"></a> `007fff5c` | `17 ee f0 97` | bl 0x0043b7b8 | `UNCONDITIONAL_CALL`
<a id="insn-007fff60"></a> `007fff60` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-007fff64"></a> `007fff64` | `82 82 00 91` | add x2,x20,#0x20 | `FALL_THROUGH`
<a id="insn-007fff68"></a> `007fff68` | `83 82 00 91` | add x3,x20,#0x20 | `FALL_THROUGH`
<a id="insn-007fff6c"></a> `007fff6c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-007fff70"></a> `007fff70` | `12 ee f0 97` | bl 0x0043b7b8 | `UNCONDITIONAL_CALL`
<a id="insn-007fff74"></a> `007fff74` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-007fff78"></a> `007fff78` | `82 02 01 91` | add x2,x20,#0x40 | `FALL_THROUGH`
<a id="insn-007fff7c"></a> `007fff7c` | `83 02 01 91` | add x3,x20,#0x40 | `FALL_THROUGH`
<a id="insn-007fff80"></a> `007fff80` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-007fff84"></a> `007fff84` | `0d ee f0 97` | bl 0x0043b7b8 | `UNCONDITIONAL_CALL`
<a id="insn-007fff88"></a> `007fff88` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-007fff8c"></a> `007fff8c` | `82 82 01 91` | add x2,x20,#0x60 | `FALL_THROUGH`
<a id="insn-007fff90"></a> `007fff90` | `83 82 01 91` | add x3,x20,#0x60 | `FALL_THROUGH`
<a id="insn-007fff94"></a> `007fff94` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-007fff98"></a> `007fff98` | `08 ee f0 97` | bl 0x0043b7b8 | `UNCONDITIONAL_CALL`
<a id="insn-007fff9c"></a> `007fff9c` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-007fffa0"></a> `007fffa0` | `82 02 02 91` | add x2,x20,#0x80 | `FALL_THROUGH`
<a id="insn-007fffa4"></a> `007fffa4` | `83 02 02 91` | add x3,x20,#0x80 | `FALL_THROUGH`
<a id="insn-007fffa8"></a> `007fffa8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-007fffac"></a> `007fffac` | `03 ee f0 97` | bl 0x0043b7b8 | `UNCONDITIONAL_CALL`
<a id="insn-007fffb0"></a> `007fffb0` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-007fffb4"></a> `007fffb4` | `82 82 02 91` | add x2,x20,#0xa0 | `FALL_THROUGH`
<a id="insn-007fffb8"></a> `007fffb8` | `83 82 02 91` | add x3,x20,#0xa0 | `FALL_THROUGH`
<a id="insn-007fffbc"></a> `007fffbc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-007fffc0"></a> `007fffc0` | `fe ed f0 97` | bl 0x0043b7b8 | `UNCONDITIONAL_CALL`
<a id="insn-007fffc4"></a> `007fffc4` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-007fffc8"></a> `007fffc8` | `82 02 03 91` | add x2,x20,#0xc0 | `FALL_THROUGH`
<a id="insn-007fffcc"></a> `007fffcc` | `83 02 03 91` | add x3,x20,#0xc0 | `FALL_THROUGH`
<a id="insn-007fffd0"></a> `007fffd0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-007fffd4"></a> `007fffd4` | `f9 ed f0 97` | bl 0x0043b7b8 | `UNCONDITIONAL_CALL`
<a id="insn-007fffd8"></a> `007fffd8` | `e8 43 43 39` | ldrb w8,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-007fffdc"></a> `007fffdc` | `e8 03 00 37` | tbnz w8,#0x0,0x00800058 | `CONDITIONAL_JUMP`
<a id="insn-007fffe0"></a> `007fffe0` | `e8 c3 42 39` | ldrb w8,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-007fffe4"></a> `007fffe4` | `28 04 00 37` | tbnz w8,#0x0,0x00800068 | `CONDITIONAL_JUMP`
<a id="insn-007fffe8"></a> `007fffe8` | `e8 43 42 39` | ldrb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-007fffec"></a> `007fffec` | `68 04 00 37` | tbnz w8,#0x0,0x00800078 | `CONDITIONAL_JUMP`
<a id="insn-007ffff0"></a> `007ffff0` | `e8 c3 41 39` | ldrb w8,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-007ffff4"></a> `007ffff4` | `a8 04 00 37` | tbnz w8,#0x0,0x00800088 | `CONDITIONAL_JUMP`
<a id="insn-007ffff8"></a> `007ffff8` | `e8 43 41 39` | ldrb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-007ffffc"></a> `007ffffc` | `e8 04 00 37` | tbnz w8,#0x0,0x00800098 | `CONDITIONAL_JUMP`
<a id="insn-00800000"></a> `00800000` | `e8 c3 40 39` | ldrb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00800004"></a> `00800004` | `28 05 00 37` | tbnz w8,#0x0,0x008000a8 | `CONDITIONAL_JUMP`
<a id="insn-00800008"></a> `00800008` | `e8 43 40 39` | ldrb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-0080000c"></a> `0080000c` | `68 00 00 36` | tbz w8,#0x0,0x00800018 | `CONDITIONAL_JUMP`
<a id="insn-00800010"></a> `00800010` | `e0 13 40 f9` | ldr x0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00800014"></a> `00800014` | `a7 5e 11 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00800018"></a> `00800018` | `c0 e1 ff d0` | adrp x0,0x43a000 | `FALL_THROUGH`
<a id="insn-0080001c"></a> `0080001c` | `00 c0 38 91` | add x0,x0,#0xe30 | `FALL_THROUGH`
<a id="insn-00800020"></a> `00800020` | `21 25 00 f0` | adrp x1,0xca7000 | `FALL_THROUGH`
<a id="insn-00800024"></a> `00800024` | `21 a0 2f 91` | add x1,x1,#0xbe8 | `FALL_THROUGH`
<a id="insn-00800028"></a> `00800028` | `02 23 00 d0` | adrp x2,0xc62000 | `FALL_THROUGH`
<a id="insn-0080002c"></a> `0080002c` | `42 40 2e 91` | add x2,x2,#0xb90 | `FALL_THROUGH`
<a id="insn-00800030"></a> `00800030` | `80 5e 11 94` | bl 0x00c57a30 | `UNCONDITIONAL_CALL`
<a id="insn-00800034"></a> `00800034` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00800038"></a> `00800038` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-0080003c"></a> `0080003c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00800040"></a> `00800040` | `41 0a 00 54` | b.ne 0x00800188 | `CONDITIONAL_JUMP`
<a id="insn-00800044"></a> `00800044` | `f4 4f 51 a9` | ldp x20,x19,[sp, #0x110] | `FALL_THROUGH`
<a id="insn-00800048"></a> `00800048` | `fc 57 50 a9` | ldp x28,x21,[sp, #0x100] | `FALL_THROUGH`
<a id="insn-0080004c"></a> `0080004c` | `fd 7b 4f a9` | ldp x29,x30,[sp, #0xf0] | `FALL_THROUGH`
<a id="insn-00800050"></a> `00800050` | `ff 83 04 91` | add sp,sp,#0x120 | `FALL_THROUGH`
<a id="insn-00800054"></a> `00800054` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00800058"></a> `00800058` | `e0 73 40 f9` | ldr x0,[sp, #0xe0] | `FALL_THROUGH`
<a id="insn-0080005c"></a> `0080005c` | `95 5e 11 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00800060"></a> `00800060` | `e8 c3 42 39` | ldrb w8,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00800064"></a> `00800064` | `28 fc 07 36` | tbz w8,#0x0,0x007fffe8 | `CONDITIONAL_JUMP`
<a id="insn-00800068"></a> `00800068` | `e0 63 40 f9` | ldr x0,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-0080006c"></a> `0080006c` | `91 5e 11 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00800070"></a> `00800070` | `e8 43 42 39` | ldrb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00800074"></a> `00800074` | `e8 fb 07 36` | tbz w8,#0x0,0x007ffff0 | `CONDITIONAL_JUMP`
<a id="insn-00800078"></a> `00800078` | `e0 53 40 f9` | ldr x0,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-0080007c"></a> `0080007c` | `8d 5e 11 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00800080"></a> `00800080` | `e8 c3 41 39` | ldrb w8,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00800084"></a> `00800084` | `a8 fb 07 36` | tbz w8,#0x0,0x007ffff8 | `CONDITIONAL_JUMP`
<a id="insn-00800088"></a> `00800088` | `e0 43 40 f9` | ldr x0,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-0080008c"></a> `0080008c` | `89 5e 11 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00800090"></a> `00800090` | `e8 43 41 39` | ldrb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00800094"></a> `00800094` | `68 fb 07 36` | tbz w8,#0x0,0x00800000 | `CONDITIONAL_JUMP`
<a id="insn-00800098"></a> `00800098` | `e0 33 40 f9` | ldr x0,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-0080009c"></a> `0080009c` | `85 5e 11 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-008000a0"></a> `008000a0` | `e8 c3 40 39` | ldrb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-008000a4"></a> `008000a4` | `28 fb 07 36` | tbz w8,#0x0,0x00800008 | `CONDITIONAL_JUMP`
<a id="insn-008000a8"></a> `008000a8` | `e0 23 40 f9` | ldr x0,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-008000ac"></a> `008000ac` | `81 5e 11 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-008000b0"></a> `008000b0` | `e8 43 40 39` | ldrb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-008000b4"></a> `008000b4` | `e8 fa 07 37` | tbnz w8,#0x0,0x00800010 | `CONDITIONAL_JUMP`
<a id="insn-008000b8"></a> `008000b8` | `d8 ff ff 17` | b 0x00800018 | `UNCONDITIONAL_JUMP`
<a id="insn-00800188"></a> `00800188` | `56 5e 11 94` | bl 0x00c57ae0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`007ffdfc`](#insn-007ffdfc) 範囲 `[['007ffdfc', '007fff7b']]`
  - `FALL_THROUGH` [`007fff78`](#insn-007fff78) → [`007fff7c`](#insn-007fff7c)
- ブロック [`007fff7c`](#insn-007fff7c) 範囲 `[['007fff7c', '007fffc7']]`
  - `FALL_THROUGH` [`007fffc4`](#insn-007fffc4) → [`007fffc8`](#insn-007fffc8)
- ブロック [`007fffc8`](#insn-007fffc8) 範囲 `[['007fffc8', '007fffcf']]`
  - `FALL_THROUGH` [`007fffcc`](#insn-007fffcc) → [`007fffd0`](#insn-007fffd0)
- ブロック [`007fffd0`](#insn-007fffd0) 範囲 `[['007fffd0', '007fffdf']]`
  - `CONDITIONAL_JUMP` [`007fffdc`](#insn-007fffdc) → [`00800058`](#insn-00800058)
  - `FALL_THROUGH` [`007fffdc`](#insn-007fffdc) → [`007fffe0`](#insn-007fffe0)
- ブロック [`007fffe0`](#insn-007fffe0) 範囲 `[['007fffe0', '007fffe7']]`
  - `CONDITIONAL_JUMP` [`007fffe4`](#insn-007fffe4) → [`00800068`](#insn-00800068)
  - `FALL_THROUGH` [`007fffe4`](#insn-007fffe4) → [`007fffe8`](#insn-007fffe8)
- ブロック [`007fffe8`](#insn-007fffe8) 範囲 `[['007fffe8', '007fffef']]`
  - `CONDITIONAL_JUMP` [`007fffec`](#insn-007fffec) → [`00800078`](#insn-00800078)
  - `FALL_THROUGH` [`007fffec`](#insn-007fffec) → [`007ffff0`](#insn-007ffff0)
- ブロック [`007ffff0`](#insn-007ffff0) 範囲 `[['007ffff0', '007ffff7']]`
  - `CONDITIONAL_JUMP` [`007ffff4`](#insn-007ffff4) → [`00800088`](#insn-00800088)
  - `FALL_THROUGH` [`007ffff4`](#insn-007ffff4) → [`007ffff8`](#insn-007ffff8)
- ブロック [`007ffff8`](#insn-007ffff8) 範囲 `[['007ffff8', '007fffff']]`
  - `CONDITIONAL_JUMP` [`007ffffc`](#insn-007ffffc) → [`00800098`](#insn-00800098)
  - `FALL_THROUGH` [`007ffffc`](#insn-007ffffc) → [`00800000`](#insn-00800000)
- ブロック [`00800000`](#insn-00800000) 範囲 `[['00800000', '00800007']]`
  - `CONDITIONAL_JUMP` [`00800004`](#insn-00800004) → [`008000a8`](#insn-008000a8)
  - `FALL_THROUGH` [`00800004`](#insn-00800004) → [`00800008`](#insn-00800008)
- ブロック [`00800008`](#insn-00800008) 範囲 `[['00800008', '0080000f']]`
  - `CONDITIONAL_JUMP` [`0080000c`](#insn-0080000c) → [`00800018`](#insn-00800018)
  - `FALL_THROUGH` [`0080000c`](#insn-0080000c) → [`00800010`](#insn-00800010)
- ブロック [`00800010`](#insn-00800010) 範囲 `[['00800010', '00800017']]`
  - `FALL_THROUGH` [`00800014`](#insn-00800014) → [`00800018`](#insn-00800018)
- ブロック [`00800018`](#insn-00800018) 範囲 `[['00800018', '0080002f']]`
  - `FALL_THROUGH` [`0080002c`](#insn-0080002c) → [`00800030`](#insn-00800030)
- ブロック [`00800030`](#insn-00800030) 範囲 `[['00800030', '00800043']]`
  - `CONDITIONAL_JUMP` [`00800040`](#insn-00800040) → [`00800188`](#insn-00800188)
  - `FALL_THROUGH` [`00800040`](#insn-00800040) → [`00800044`](#insn-00800044)
- ブロック [`00800044`](#insn-00800044) 範囲 `[['00800044', '00800057']]`
- ブロック [`00800058`](#insn-00800058) 範囲 `[['00800058', '00800067']]`
  - `CONDITIONAL_JUMP` [`00800064`](#insn-00800064) → [`007fffe8`](#insn-007fffe8)
  - `FALL_THROUGH` [`00800064`](#insn-00800064) → [`00800068`](#insn-00800068)
- ブロック [`00800068`](#insn-00800068) 範囲 `[['00800068', '0080006f']]`
  - `FALL_THROUGH` [`0080006c`](#insn-0080006c) → [`00800070`](#insn-00800070)
- ブロック [`00800070`](#insn-00800070) 範囲 `[['00800070', '00800077']]`
  - `CONDITIONAL_JUMP` [`00800074`](#insn-00800074) → [`007ffff0`](#insn-007ffff0)
  - `FALL_THROUGH` [`00800074`](#insn-00800074) → [`00800078`](#insn-00800078)
- ブロック [`00800078`](#insn-00800078) 範囲 `[['00800078', '00800087']]`
  - `CONDITIONAL_JUMP` [`00800084`](#insn-00800084) → [`007ffff8`](#insn-007ffff8)
  - `FALL_THROUGH` [`00800084`](#insn-00800084) → [`00800088`](#insn-00800088)
- ブロック [`00800088`](#insn-00800088) 範囲 `[['00800088', '00800097']]`
  - `CONDITIONAL_JUMP` [`00800094`](#insn-00800094) → [`00800000`](#insn-00800000)
  - `FALL_THROUGH` [`00800094`](#insn-00800094) → [`00800098`](#insn-00800098)
- ブロック [`00800098`](#insn-00800098) 範囲 `[['00800098', '008000a3']]`
  - `FALL_THROUGH` [`008000a0`](#insn-008000a0) → [`008000a4`](#insn-008000a4)
- ブロック [`008000a4`](#insn-008000a4) 範囲 `[['008000a4', '008000a7']]`
  - `CONDITIONAL_JUMP` [`008000a4`](#insn-008000a4) → [`00800008`](#insn-00800008)
  - `FALL_THROUGH` [`008000a4`](#insn-008000a4) → [`008000a8`](#insn-008000a8)
- ブロック [`008000a8`](#insn-008000a8) 範囲 `[['008000a8', '008000ab']]`
  - `FALL_THROUGH` [`008000a8`](#insn-008000a8) → [`008000ac`](#insn-008000ac)
- ブロック [`008000ac`](#insn-008000ac) 範囲 `[['008000ac', '008000b7']]`
  - `CONDITIONAL_JUMP` [`008000b4`](#insn-008000b4) → [`00800010`](#insn-00800010)
  - `FALL_THROUGH` [`008000b4`](#insn-008000b4) → [`008000b8`](#insn-008000b8)
- ブロック [`008000b8`](#insn-008000b8) 範囲 `[['008000b8', '008000bb']]`
  - `UNCONDITIONAL_JUMP` [`008000b8`](#insn-008000b8) → [`00800018`](#insn-00800018)
- ブロック [`00800188`](#insn-00800188) 範囲 `[['00800188', '0080018b']]`

## 命令位置別の参照

- [`007ffe00`](#insn-007ffe00) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ffe04`](#insn-007ffe04) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ffe08`](#insn-007ffe08) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ffe2c`](#insn-007ffe2c) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ffe38`](#insn-007ffe38) → `002b7ee6`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`007ffe40`](#insn-007ffe40) → `Stack[-0xff]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ffe44`](#insn-007ffe44) → `Stack[-0xf8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ffe54`](#insn-007ffe54) → `Stack[-0x10f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ffe5c`](#insn-007ffe5c) → `002b7ef9`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`007ffe60`](#insn-007ffe60) → `Stack[-0xdf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ffe68`](#insn-007ffe68) → `Stack[-0xd8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ffe78`](#insn-007ffe78) → `Stack[-0xef]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ffe7c`](#insn-007ffe7c) → `002b8d82`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`007ffe80`](#insn-007ffe80) → `Stack[-0xbf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ffe88`](#insn-007ffe88) → `Stack[-0xb8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ffe98`](#insn-007ffe98) → `Stack[-0xcf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ffe9c`](#insn-007ffe9c) → `002a2e95`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`007ffea0`](#insn-007ffea0) → `Stack[-0x9f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ffea8`](#insn-007ffea8) → `Stack[-0x98]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ffeb4`](#insn-007ffeb4) → `Stack[-0xaf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ffeb8`](#insn-007ffeb8) → `002ac592`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`007ffec0`](#insn-007ffec0) → `Stack[-0x7f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ffec8`](#insn-007ffec8) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ffed4`](#insn-007ffed4) → `Stack[-0x8f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ffed8`](#insn-007ffed8) → `002a0e90`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`007ffee0`](#insn-007ffee0) → `Stack[-0x5f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ffee8`](#insn-007ffee8) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ffef4`](#insn-007ffef4) → `Stack[-0x6f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ffef8`](#insn-007ffef8) → `002a3e3c`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`007ffefc`](#insn-007ffefc) → `Stack[-0x110]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fff00`](#insn-007fff00) → `Stack[-0xf0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fff04`](#insn-007fff04) → `Stack[-0xd0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fff08`](#insn-007fff08) → `Stack[-0xb0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fff0c`](#insn-007fff0c) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fff10`](#insn-007fff10) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fff14`](#insn-007fff14) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fff1c`](#insn-007fff1c) → `Stack[-0x118]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fff20`](#insn-007fff20) → `Stack[-0xfd]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fff24`](#insn-007fff24) → `Stack[-0xdd]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fff28`](#insn-007fff28) → `Stack[-0xbd]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fff2c`](#insn-007fff2c) → `Stack[-0x9d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fff30`](#insn-007fff30) → `Stack[-0x7d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fff34`](#insn-007fff34) → `Stack[-0x5d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fff38`](#insn-007fff38) → `Stack[-0x3f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fff3c`](#insn-007fff3c) → `Stack[-0x4f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fff40`](#insn-007fff40) → `Stack[-0x3d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fff44`](#insn-007fff44) → `00ca7bf8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`007fff48`](#insn-007fff48) → `00ca7bf0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`007fff4c`](#insn-007fff4c) → `00ca7be8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`007fff4c`](#insn-007fff4c) → `00ca7bf0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`007fff58`](#insn-007fff58) → `00ca7be8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`007fff5c`](#insn-007fff5c) → [`0043b7b8`](../0043b/0043b7b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043b7b8` · 推定シンボル `None` · 推定型 `None`
- [`007fff60`](#insn-007fff60) → `00ca7bf0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`007fff6c`](#insn-007fff6c) → `00ca7be8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`007fff70`](#insn-007fff70) → [`0043b7b8`](../0043b/0043b7b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043b7b8` · 推定シンボル `None` · 推定型 `None`
- [`007fff74`](#insn-007fff74) → `00ca7bf0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`007fff80`](#insn-007fff80) → `00ca7be8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`007fff84`](#insn-007fff84) → [`0043b7b8`](../0043b/0043b7b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043b7b8` · 推定シンボル `None` · 推定型 `None`
- [`007fff88`](#insn-007fff88) → `00ca7bf0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`007fff94`](#insn-007fff94) → `00ca7be8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`007fff98`](#insn-007fff98) → [`0043b7b8`](../0043b/0043b7b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043b7b8` · 推定シンボル `None` · 推定型 `None`
- [`007fff9c`](#insn-007fff9c) → `00ca7bf0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`007fffa8`](#insn-007fffa8) → `00ca7be8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`007fffac`](#insn-007fffac) → [`0043b7b8`](../0043b/0043b7b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043b7b8` · 推定シンボル `None` · 推定型 `None`
- [`007fffb0`](#insn-007fffb0) → `00ca7bf0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`007fffbc`](#insn-007fffbc) → `00ca7be8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`007fffc0`](#insn-007fffc0) → [`0043b7b8`](../0043b/0043b7b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043b7b8` · 推定シンボル `None` · 推定型 `None`
- [`007fffc4`](#insn-007fffc4) → `00ca7bf0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`007fffd0`](#insn-007fffd0) → `00ca7be8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`007fffd4`](#insn-007fffd4) → [`0043b7b8`](../0043b/0043b7b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043b7b8` · 推定シンボル `None` · 推定型 `None`
- [`007fffd8`](#insn-007fffd8) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fffdc`](#insn-007fffdc) → [`00800058`](#insn-00800058) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fffe0`](#insn-007fffe0) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fffe4`](#insn-007fffe4) → [`00800068`](#insn-00800068) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fffe8`](#insn-007fffe8) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fffec`](#insn-007fffec) → [`00800078`](#insn-00800078) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ffff0`](#insn-007ffff0) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ffff4`](#insn-007ffff4) → [`00800088`](#insn-00800088) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ffff8`](#insn-007ffff8) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ffffc`](#insn-007ffffc) → [`00800098`](#insn-00800098) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00800000`](#insn-00800000) → `Stack[-0xf0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00800004`](#insn-00800004) → [`008000a8`](#insn-008000a8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00800008`](#insn-00800008) → `Stack[-0x110]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`0080000c`](#insn-0080000c) → [`00800018`](#insn-00800018) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00800010`](#insn-00800010) → `Stack[-0x100]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00800014`](#insn-00800014) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`0080001c`](#insn-0080001c) → [`0043ae30`](../0043a/0043ae30.md) · `PARAM` · `ANALYSIS` · 関数 `0043ae30` · 推定シンボル `None` · 推定型 `None`
- [`00800024`](#insn-00800024) → `00ca7be8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`0080002c`](#insn-0080002c) → `00c62b90`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00800030`](#insn-00800030) → [`00c57a30`](../00c57/00c57a30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a30` · 推定シンボル `None` · 推定型 `None`
- [`00800038`](#insn-00800038) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00800040`](#insn-00800040) → [`00800188`](#insn-00800188) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00800044`](#insn-00800044) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00800048`](#insn-00800048) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`0080004c`](#insn-0080004c) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00800058`](#insn-00800058) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`0080005c`](#insn-0080005c) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00800060`](#insn-00800060) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00800064`](#insn-00800064) → [`007fffe8`](#insn-007fffe8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00800068`](#insn-00800068) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`0080006c`](#insn-0080006c) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00800070`](#insn-00800070) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00800074`](#insn-00800074) → [`007ffff0`](#insn-007ffff0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00800078`](#insn-00800078) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`0080007c`](#insn-0080007c) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00800080`](#insn-00800080) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00800084`](#insn-00800084) → [`007ffff8`](#insn-007ffff8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00800088`](#insn-00800088) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`0080008c`](#insn-0080008c) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00800090`](#insn-00800090) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00800094`](#insn-00800094) → [`00800000`](#insn-00800000) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00800098`](#insn-00800098) → `Stack[-0xc0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`0080009c`](#insn-0080009c) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`008000a0`](#insn-008000a0) → `Stack[-0xf0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008000a4`](#insn-008000a4) → [`00800008`](#insn-00800008) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008000a8`](#insn-008000a8) → `Stack[-0xe0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008000ac`](#insn-008000ac) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`008000b0`](#insn-008000b0) → `Stack[-0x110]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008000b4`](#insn-008000b4) → [`00800010`](#insn-00800010) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008000b8`](#insn-008000b8) → [`00800018`](#insn-00800018) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00800188`](#insn-00800188) → [`00c57ae0`](../00c57/00c57ae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ae0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`007ffe00`](#insn-007ffe00)

~~~json
{
  "source": "007ffe00",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ffe04`](#insn-007ffe04)

~~~json
{
  "source": "007ffe04",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ffe08`](#insn-007ffe08)

~~~json
{
  "source": "007ffe08",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ffe2c`](#insn-007ffe2c)

~~~json
{
  "source": "007ffe2c",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ffe38`](#insn-007ffe38)

~~~json
{
  "source": "007ffe38",
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
- 参照命令 [`007ffe40`](#insn-007ffe40)

~~~json
{
  "source": "007ffe40",
  "target": "Stack[-0xff]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ffe44`](#insn-007ffe44)

~~~json
{
  "source": "007ffe44",
  "target": "Stack[-0xf8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ffe54`](#insn-007ffe54)

~~~json
{
  "source": "007ffe54",
  "target": "Stack[-0x10f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ffe5c`](#insn-007ffe5c)

~~~json
{
  "source": "007ffe5c",
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
- 参照命令 [`007ffe60`](#insn-007ffe60)

~~~json
{
  "source": "007ffe60",
  "target": "Stack[-0xdf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ffe68`](#insn-007ffe68)

~~~json
{
  "source": "007ffe68",
  "target": "Stack[-0xd8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ffe78`](#insn-007ffe78)

~~~json
{
  "source": "007ffe78",
  "target": "Stack[-0xef]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ffe7c`](#insn-007ffe7c)

~~~json
{
  "source": "007ffe7c",
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
- 参照命令 [`007ffe80`](#insn-007ffe80)

~~~json
{
  "source": "007ffe80",
  "target": "Stack[-0xbf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ffe88`](#insn-007ffe88)

~~~json
{
  "source": "007ffe88",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ffe98`](#insn-007ffe98)

~~~json
{
  "source": "007ffe98",
  "target": "Stack[-0xcf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ffe9c`](#insn-007ffe9c)

~~~json
{
  "source": "007ffe9c",
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
- 参照命令 [`007ffea0`](#insn-007ffea0)

~~~json
{
  "source": "007ffea0",
  "target": "Stack[-0x9f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ffea8`](#insn-007ffea8)

~~~json
{
  "source": "007ffea8",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ffeb4`](#insn-007ffeb4)

~~~json
{
  "source": "007ffeb4",
  "target": "Stack[-0xaf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ffeb8`](#insn-007ffeb8)

~~~json
{
  "source": "007ffeb8",
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
- 参照命令 [`007ffec0`](#insn-007ffec0)

~~~json
{
  "source": "007ffec0",
  "target": "Stack[-0x7f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ffec8`](#insn-007ffec8)

~~~json
{
  "source": "007ffec8",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ffed4`](#insn-007ffed4)

~~~json
{
  "source": "007ffed4",
  "target": "Stack[-0x8f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ffed8`](#insn-007ffed8)

~~~json
{
  "source": "007ffed8",
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
- 参照命令 [`007ffee0`](#insn-007ffee0)

~~~json
{
  "source": "007ffee0",
  "target": "Stack[-0x5f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ffee8`](#insn-007ffee8)

~~~json
{
  "source": "007ffee8",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ffef4`](#insn-007ffef4)

~~~json
{
  "source": "007ffef4",
  "target": "Stack[-0x6f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ffef8`](#insn-007ffef8)

~~~json
{
  "source": "007ffef8",
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
- 参照命令 [`007ffefc`](#insn-007ffefc)

~~~json
{
  "source": "007ffefc",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fff00`](#insn-007fff00)

~~~json
{
  "source": "007fff00",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fff04`](#insn-007fff04)

~~~json
{
  "source": "007fff04",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fff08`](#insn-007fff08)

~~~json
{
  "source": "007fff08",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fff0c`](#insn-007fff0c)

~~~json
{
  "source": "007fff0c",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fff10`](#insn-007fff10)

~~~json
{
  "source": "007fff10",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fff14`](#insn-007fff14)

~~~json
{
  "source": "007fff14",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fff1c`](#insn-007fff1c)

~~~json
{
  "source": "007fff1c",
  "target": "Stack[-0x118]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fff20`](#insn-007fff20)

~~~json
{
  "source": "007fff20",
  "target": "Stack[-0xfd]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fff24`](#insn-007fff24)

~~~json
{
  "source": "007fff24",
  "target": "Stack[-0xdd]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fff28`](#insn-007fff28)

~~~json
{
  "source": "007fff28",
  "target": "Stack[-0xbd]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fff2c`](#insn-007fff2c)

~~~json
{
  "source": "007fff2c",
  "target": "Stack[-0x9d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fff30`](#insn-007fff30)

~~~json
{
  "source": "007fff30",
  "target": "Stack[-0x7d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fff34`](#insn-007fff34)

~~~json
{
  "source": "007fff34",
  "target": "Stack[-0x5d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fff38`](#insn-007fff38)

~~~json
{
  "source": "007fff38",
  "target": "Stack[-0x3f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fff3c`](#insn-007fff3c)

~~~json
{
  "source": "007fff3c",
  "target": "Stack[-0x4f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fff40`](#insn-007fff40)

~~~json
{
  "source": "007fff40",
  "target": "Stack[-0x3d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fff44`](#insn-007fff44)

~~~json
{
  "source": "007fff44",
  "target": "00ca7bf8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca7bf8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`007fff48`](#insn-007fff48)

~~~json
{
  "source": "007fff48",
  "target": "00ca7bf0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca7bf0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`007fff4c`](#insn-007fff4c)

~~~json
{
  "source": "007fff4c",
  "target": "00ca7be8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca7be8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`007fff4c`](#insn-007fff4c)

~~~json
{
  "source": "007fff4c",
  "target": "00ca7bf0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca7bf0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`007fff58`](#insn-007fff58)

~~~json
{
  "source": "007fff58",
  "target": "00ca7be8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca7be8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`007fff5c`](#insn-007fff5c)

~~~json
{
  "source": "007fff5c",
  "target": "0043b7b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007fff60`](#insn-007fff60)

~~~json
{
  "source": "007fff60",
  "target": "00ca7bf0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca7bf0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`007fff6c`](#insn-007fff6c)

~~~json
{
  "source": "007fff6c",
  "target": "00ca7be8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca7be8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`007fff70`](#insn-007fff70)

~~~json
{
  "source": "007fff70",
  "target": "0043b7b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007fff74`](#insn-007fff74)

~~~json
{
  "source": "007fff74",
  "target": "00ca7bf0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca7bf0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`007fff80`](#insn-007fff80)

~~~json
{
  "source": "007fff80",
  "target": "00ca7be8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca7be8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`007fff84`](#insn-007fff84)

~~~json
{
  "source": "007fff84",
  "target": "0043b7b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007fff88`](#insn-007fff88)

~~~json
{
  "source": "007fff88",
  "target": "00ca7bf0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca7bf0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`007fff94`](#insn-007fff94)

~~~json
{
  "source": "007fff94",
  "target": "00ca7be8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca7be8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`007fff98`](#insn-007fff98)

~~~json
{
  "source": "007fff98",
  "target": "0043b7b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007fff9c`](#insn-007fff9c)

~~~json
{
  "source": "007fff9c",
  "target": "00ca7bf0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca7bf0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`007fffa8`](#insn-007fffa8)

~~~json
{
  "source": "007fffa8",
  "target": "00ca7be8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca7be8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`007fffac`](#insn-007fffac)

~~~json
{
  "source": "007fffac",
  "target": "0043b7b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007fffb0`](#insn-007fffb0)

~~~json
{
  "source": "007fffb0",
  "target": "00ca7bf0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca7bf0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`007fffbc`](#insn-007fffbc)

~~~json
{
  "source": "007fffbc",
  "target": "00ca7be8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca7be8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`007fffc0`](#insn-007fffc0)

~~~json
{
  "source": "007fffc0",
  "target": "0043b7b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007fffc4`](#insn-007fffc4)

~~~json
{
  "source": "007fffc4",
  "target": "00ca7bf0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca7bf0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`007fffd0`](#insn-007fffd0)

~~~json
{
  "source": "007fffd0",
  "target": "00ca7be8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca7be8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`007fffd4`](#insn-007fffd4)

~~~json
{
  "source": "007fffd4",
  "target": "0043b7b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007fffd8`](#insn-007fffd8)

~~~json
{
  "source": "007fffd8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fffdc`](#insn-007fffdc)

~~~json
{
  "source": "007fffdc",
  "target": "00800058",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fffe0`](#insn-007fffe0)

~~~json
{
  "source": "007fffe0",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fffe4`](#insn-007fffe4)

~~~json
{
  "source": "007fffe4",
  "target": "00800068",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fffe8`](#insn-007fffe8)

~~~json
{
  "source": "007fffe8",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fffec`](#insn-007fffec)

~~~json
{
  "source": "007fffec",
  "target": "00800078",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ffff0`](#insn-007ffff0)

~~~json
{
  "source": "007ffff0",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ffff4`](#insn-007ffff4)

~~~json
{
  "source": "007ffff4",
  "target": "00800088",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ffff8`](#insn-007ffff8)

~~~json
{
  "source": "007ffff8",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ffffc`](#insn-007ffffc)

~~~json
{
  "source": "007ffffc",
  "target": "00800098",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00800000`](#insn-00800000)

~~~json
{
  "source": "00800000",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00800004`](#insn-00800004)

~~~json
{
  "source": "00800004",
  "target": "008000a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00800008`](#insn-00800008)

~~~json
{
  "source": "00800008",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`0080000c`](#insn-0080000c)

~~~json
{
  "source": "0080000c",
  "target": "00800018",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00800010`](#insn-00800010)

~~~json
{
  "source": "00800010",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00800014`](#insn-00800014)

~~~json
{
  "source": "00800014",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`0080001c`](#insn-0080001c)

~~~json
{
  "source": "0080001c",
  "target": "0043ae30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00800024`](#insn-00800024)

~~~json
{
  "source": "00800024",
  "target": "00ca7be8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca7be8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`0080002c`](#insn-0080002c)

~~~json
{
  "source": "0080002c",
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
- 参照命令 [`00800030`](#insn-00800030)

~~~json
{
  "source": "00800030",
  "target": "00c57a30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00800038`](#insn-00800038)

~~~json
{
  "source": "00800038",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00800040`](#insn-00800040)

~~~json
{
  "source": "00800040",
  "target": "00800188",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00800044`](#insn-00800044)

~~~json
{
  "source": "00800044",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00800048`](#insn-00800048)

~~~json
{
  "source": "00800048",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`0080004c`](#insn-0080004c)

~~~json
{
  "source": "0080004c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00800058`](#insn-00800058)

~~~json
{
  "source": "00800058",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`0080005c`](#insn-0080005c)

~~~json
{
  "source": "0080005c",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00800060`](#insn-00800060)

~~~json
{
  "source": "00800060",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00800064`](#insn-00800064)

~~~json
{
  "source": "00800064",
  "target": "007fffe8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00800068`](#insn-00800068)

~~~json
{
  "source": "00800068",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`0080006c`](#insn-0080006c)

~~~json
{
  "source": "0080006c",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00800070`](#insn-00800070)

~~~json
{
  "source": "00800070",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00800074`](#insn-00800074)

~~~json
{
  "source": "00800074",
  "target": "007ffff0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00800078`](#insn-00800078)

~~~json
{
  "source": "00800078",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`0080007c`](#insn-0080007c)

~~~json
{
  "source": "0080007c",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00800080`](#insn-00800080)

~~~json
{
  "source": "00800080",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00800084`](#insn-00800084)

~~~json
{
  "source": "00800084",
  "target": "007ffff8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00800088`](#insn-00800088)

~~~json
{
  "source": "00800088",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`0080008c`](#insn-0080008c)

~~~json
{
  "source": "0080008c",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00800090`](#insn-00800090)

~~~json
{
  "source": "00800090",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00800094`](#insn-00800094)

~~~json
{
  "source": "00800094",
  "target": "00800000",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00800098`](#insn-00800098)

~~~json
{
  "source": "00800098",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`0080009c`](#insn-0080009c)

~~~json
{
  "source": "0080009c",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008000a0`](#insn-008000a0)

~~~json
{
  "source": "008000a0",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008000a4`](#insn-008000a4)

~~~json
{
  "source": "008000a4",
  "target": "00800008",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008000a8`](#insn-008000a8)

~~~json
{
  "source": "008000a8",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008000ac`](#insn-008000ac)

~~~json
{
  "source": "008000ac",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008000b0`](#insn-008000b0)

~~~json
{
  "source": "008000b0",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008000b4`](#insn-008000b4)

~~~json
{
  "source": "008000b4",
  "target": "00800010",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008000b8`](#insn-008000b8)

~~~json
{
  "source": "008000b8",
  "target": "00800018",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00800188`](#insn-00800188)

~~~json
{
  "source": "00800188",
  "target": "00c57ae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
