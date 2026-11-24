# 00a6cbbc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00a6cb4c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a6c/00a6cb4c.md) · 移動量 `+0x70`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0062.md#compare-518d1fe2ce842dea833dfbf460d6675c)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00a6dbb0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a6d/00a6dbb0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0063.md#compare-1d9c08a6c621ab0c80d466d8c3466fba)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00a6cbbc",
  "name": "_INIT_224",
  "size": 708,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "eec7789faf352db64cc3b7eff282e877a1cc10e6c972f8d0e6d4b41a344903c6",
  "source_text_sha256": "eec7789faf352db64cc3b7eff282e877a1cc10e6c972f8d0e6d4b41a344903c6",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00a6cbbc",
        "00a6ce7b"
      ],
      [
        "00a6cf48",
        "00a6cf4b"
      ]
    ],
    "bytes_sha256": "13f092d6865e9dd88c47a1992dd56541c5bccaa3f781644c0d30cba7832769b0",
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

- [0043b838](../0043b/0043b838.md)
- [00c57f00](../00c57/00c57f00.md)
- [00c57f80](../00c57/00c57f80.md)
- [00c57fb0](../00c57/00c57fb0.md)

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

## 疑似コード / UTF-8 5345 bytes

~~~c

/* WARNING: Type propagation algorithm not settling */

void _INIT_224(void)

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
  uStack_107 = (undefined7)s_CgkIjM3y_ZQaEAIQAg_002b7f66._8_8_;
  cStack_100 = SUB81(s_CgkIjM3y_ZQaEAIQAg_002b7f66._8_8_,7);
  local_10f = (char  [8])s_CgkIjM3y_ZQaEAIQAg_002b7f66._0_8_;
  uStack_df = 0x4142;
  local_d8[0] = 2;
  uStack_e7 = (undefined7)s_CgkIjM3y_ZQaEAIQBA_002b7f79._8_8_;
  cStack_e0 = SUB81(s_CgkIjM3y_ZQaEAIQBA_002b7f79._8_8_,7);
  local_ef = (char  [8])s_CgkIjM3y_ZQaEAIQBA_002b7f79._0_8_;
  uStack_bf = 0x6742;
  local_b8[0] = 3;
  uStack_c7 = (undefined7)s_CgkIjM3y_ZQaEAIQBg_002b8d6e._8_8_;
  cStack_c0 = SUB81(s_CgkIjM3y_ZQaEAIQBg_002b8d6e._8_8_,7);
  local_cf = (char  [8])s_CgkIjM3y_ZQaEAIQBg_002b8d6e._0_8_;
  uStack_9f = 0x7741;
  local_98[0] = 4;
  uStack_a7 = (undefined7)s_CgkIjM3y_ZQaEAIQAw_002a2f15._8_8_;
  cStack_a0 = SUB81(s_CgkIjM3y_ZQaEAIQAw_002a2f15._8_8_,7);
  local_af = (char  [8])s_CgkIjM3y_ZQaEAIQAw_002a2f15._0_8_;
  uStack_7f = 0x5142;
  local_78[0] = 5;
  uStack_87 = (undefined7)s_CgkIjM3y_ZQaEAIQBQ_002ac576._8_8_;
  cStack_80 = SUB81(s_CgkIjM3y_ZQaEAIQBQ_002ac576._8_8_,7);
  local_8f = (char  [8])s_CgkIjM3y_ZQaEAIQBQ_002ac576._0_8_;
  uStack_5f = 0x7742;
  local_58[0] = 6;
  uStack_67 = (undefined7)s_CgkIjM3y_ZQaEAIQBw_002a0f10._8_8_;
  cStack_60 = SUB81(s_CgkIjM3y_ZQaEAIQBw_002a0f10._8_8_,7);
  local_6f = (char  [8])s_CgkIjM3y_ZQaEAIQBw_002a0f10._0_8_;
  local_110 = 0x24;
                    /* try { // try from 00a6ccc0 to 00b6cccb has its CatchHandler @ 00a77f00 */
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
  uStack_47 = (undefined7)s_CgkIjM3y_ZQaEAIQCA_002a3ebc._8_8_;
  cStack_40 = SUB81(s_CgkIjM3y_ZQaEAIQCA_002a3ebc._8_8_,7);
  local_4f = (char  [8])s_CgkIjM3y_ZQaEAIQCA_002a3ebc._0_8_;
  uStack_3d = 0;
  DAT_01124140 = 0;
  DAT_01124138 = 0;
  DAT_01124130 = &DAT_01124138;
  FUN_0043b838(&DAT_01124130,&DAT_01124138,local_118,local_118);
  FUN_0043b838(&DAT_01124130,&DAT_01124138,local_f8,local_f8);
                    /* try { // try from 00a6cd44 to 00b6cd53 has its CatchHandler @ 00a77f38 */
  FUN_0043b838(&DAT_01124130,&DAT_01124138,local_d8,local_d8);
  FUN_0043b838(&DAT_01124130,&DAT_01124138,local_b8,local_b8);
  FUN_0043b838(&DAT_01124130,&DAT_01124138,local_98,local_98);
  FUN_0043b838(&DAT_01124130,&DAT_01124138,local_78,local_78);
                    /* try { // try from 00a6cd94 to 00b6cda3 has its CatchHandler @ 00a77f30 */
  FUN_0043b838(&DAT_01124130,&DAT_01124138,local_58,local_58);
  if ((local_50 & 1) != 0) {
    _ZdlPv((void *)CONCAT44(uStack_3c,CONCAT13(uStack_3d,CONCAT21(uStack_3f,cStack_40))));
  }
  if ((local_70 & 1) != 0) {
    _ZdlPv((void *)CONCAT44(uStack_5c,CONCAT13(uStack_5d,CONCAT21(uStack_5f,cStack_60))));
  }
  if ((local_90 & 1) != 0) {
                    /* try { // try from 00a6ce38 to 00b6ce47 has its CatchHandler @ 00a77f2c */
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
                    /* try { // try from 00a6cde4 to 00b6cdf7 has its CatchHandler @ 00a77f40 */
  __cxa_atexit(FUN_0043aeb0,&DAT_01124130,&PTR_LOOP_00c63060);
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
<a id="insn-00a6cbbc"></a> `00a6cbbc` | `ff 83 04 d1` | sub sp,sp,#0x120 | `FALL_THROUGH`
<a id="insn-00a6cbc0"></a> `00a6cbc0` | `fd 7b 0f a9` | stp x29,x30,[sp, #0xf0] | `FALL_THROUGH`
<a id="insn-00a6cbc4"></a> `00a6cbc4` | `fc 57 10 a9` | stp x28,x21,[sp, #0x100] | `FALL_THROUGH`
<a id="insn-00a6cbc8"></a> `00a6cbc8` | `f4 4f 11 a9` | stp x20,x19,[sp, #0x110] | `FALL_THROUGH`
<a id="insn-00a6cbcc"></a> `00a6cbcc` | `fd c3 03 91` | add x29,sp,#0xf0 | `FALL_THROUGH`
<a id="insn-00a6cbd0"></a> `00a6cbd0` | `55 d0 3b d5` | mrs x21,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00a6cbd4"></a> `00a6cbd4` | `2a e8 8c 52` | mov w10,#0x6741 | `FALL_THROUGH`
<a id="insn-00a6cbd8"></a> `00a6cbd8` | `f4 23 00 91` | add x20,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00a6cbdc"></a> `00a6cbdc` | `a9 16 40 f9` | ldr x9,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00a6cbe0"></a> `00a6cbe0` | `88 04 80 52` | mov w8,#0x24 | `FALL_THROUGH`
<a id="insn-00a6cbe4"></a> `00a6cbe4` | `d3 35 00 90` | adrp x19,0x1124000 | `FALL_THROUGH`
<a id="insn-00a6cbe8"></a> `00a6cbe8` | `73 c2 04 91` | add x19,x19,#0x130 | `FALL_THROUGH`
<a id="insn-00a6cbec"></a> `00a6cbec` | `a9 83 1f f8` | stur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00a6cbf0"></a> `00a6cbf0` | `49 c2 ff f0` | adrp x9,0x2b7000 | `FALL_THROUGH`
<a id="insn-00a6cbf4"></a> `00a6cbf4` | `29 99 3d 91` | add x9,x9,#0xf66 | `FALL_THROUGH`
<a id="insn-00a6cbf8"></a> `00a6cbf8` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00a6cbfc"></a> `00a6cbfc` | `29 00 80 52` | mov w9,#0x1 | `FALL_THROUGH`
<a id="insn-00a6cc00"></a> `00a6cc00` | `ea 13 02 78` | sturh w10,[sp, #0x21] | `FALL_THROUGH`
<a id="insn-00a6cc04"></a> `00a6cc04` | `e9 2b 00 b9` | str w9,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00a6cc08"></a> `00a6cc08` | `49 28 88 52` | mov w9,#0x4142 | `FALL_THROUGH`
<a id="insn-00a6cc0c"></a> `00a6cc0c` | `4a c2 ff f0` | adrp x10,0x2b7000 | `FALL_THROUGH`
<a id="insn-00a6cc10"></a> `00a6cc10` | `4a e5 3d 91` | add x10,x10,#0xf79 | `FALL_THROUGH`
<a id="insn-00a6cc14"></a> `00a6cc14` | `e0 13 81 3c` | stur q0,[sp, #0x11] | `FALL_THROUGH`
<a id="insn-00a6cc18"></a> `00a6cc18` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00a6cc1c"></a> `00a6cc1c` | `40 01 c0 3d` | ldr q0,[x10] | `FALL_THROUGH`
<a id="insn-00a6cc20"></a> `00a6cc20` | `e9 13 04 78` | sturh w9,[sp, #0x41] | `FALL_THROUGH`
<a id="insn-00a6cc24"></a> `00a6cc24` | `49 00 80 52` | mov w9,#0x2 | `FALL_THROUGH`
<a id="insn-00a6cc28"></a> `00a6cc28` | `e9 4b 00 b9` | str w9,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00a6cc2c"></a> `00a6cc2c` | `49 e8 8c 52` | mov w9,#0x6742 | `FALL_THROUGH`
<a id="insn-00a6cc30"></a> `00a6cc30` | `6a c2 ff 90` | adrp x10,0x2b8000 | `FALL_THROUGH`
<a id="insn-00a6cc34"></a> `00a6cc34` | `4a b9 35 91` | add x10,x10,#0xd6e | `FALL_THROUGH`
<a id="insn-00a6cc38"></a> `00a6cc38` | `e0 13 83 3c` | stur q0,[sp, #0x31] | `FALL_THROUGH`
<a id="insn-00a6cc3c"></a> `00a6cc3c` | `40 01 c0 3d` | ldr q0,[x10] | `FALL_THROUGH`
<a id="insn-00a6cc40"></a> `00a6cc40` | `e9 13 06 78` | sturh w9,[sp, #0x61] | `FALL_THROUGH`
<a id="insn-00a6cc44"></a> `00a6cc44` | `69 00 80 52` | mov w9,#0x3 | `FALL_THROUGH`
<a id="insn-00a6cc48"></a> `00a6cc48` | `e9 6b 00 b9` | str w9,[sp, #0x68] | `FALL_THROUGH`
<a id="insn-00a6cc4c"></a> `00a6cc4c` | `29 e8 8e 52` | mov w9,#0x7741 | `FALL_THROUGH`
<a id="insn-00a6cc50"></a> `00a6cc50` | `aa c1 ff d0` | adrp x10,0x2a2000 | `FALL_THROUGH`
<a id="insn-00a6cc54"></a> `00a6cc54` | `4a 55 3c 91` | add x10,x10,#0xf15 | `FALL_THROUGH`
<a id="insn-00a6cc58"></a> `00a6cc58` | `e0 13 85 3c` | stur q0,[sp, #0x51] | `FALL_THROUGH`
<a id="insn-00a6cc5c"></a> `00a6cc5c` | `40 01 c0 3d` | ldr q0,[x10] | `FALL_THROUGH`
<a id="insn-00a6cc60"></a> `00a6cc60` | `e9 13 08 78` | sturh w9,[sp, #0x81] | `FALL_THROUGH`
<a id="insn-00a6cc64"></a> `00a6cc64` | `89 00 80 52` | mov w9,#0x4 | `FALL_THROUGH`
<a id="insn-00a6cc68"></a> `00a6cc68` | `e9 8b 00 b9` | str w9,[sp, #0x88] | `FALL_THROUGH`
<a id="insn-00a6cc6c"></a> `00a6cc6c` | `09 c2 ff 90` | adrp x9,0x2ac000 | `FALL_THROUGH`
<a id="insn-00a6cc70"></a> `00a6cc70` | `29 d9 15 91` | add x9,x9,#0x576 | `FALL_THROUGH`
<a id="insn-00a6cc74"></a> `00a6cc74` | `e0 13 87 3c` | stur q0,[sp, #0x71] | `FALL_THROUGH`
<a id="insn-00a6cc78"></a> `00a6cc78` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00a6cc7c"></a> `00a6cc7c` | `49 28 8a 52` | mov w9,#0x5142 | `FALL_THROUGH`
<a id="insn-00a6cc80"></a> `00a6cc80` | `89 92 09 78` | sturh w9,[x20, #0x99] | `FALL_THROUGH`
<a id="insn-00a6cc84"></a> `00a6cc84` | `a9 00 80 52` | mov w9,#0x5 | `FALL_THROUGH`
<a id="insn-00a6cc88"></a> `00a6cc88` | `e9 ab 00 b9` | str w9,[sp, #0xa8] | `FALL_THROUGH`
<a id="insn-00a6cc8c"></a> `00a6cc8c` | `a9 c1 ff 90` | adrp x9,0x2a0000 | `FALL_THROUGH`
<a id="insn-00a6cc90"></a> `00a6cc90` | `29 41 3c 91` | add x9,x9,#0xf10 | `FALL_THROUGH`
<a id="insn-00a6cc94"></a> `00a6cc94` | `80 92 88 3c` | stur q0,[x20, #0x89] | `FALL_THROUGH`
<a id="insn-00a6cc98"></a> `00a6cc98` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00a6cc9c"></a> `00a6cc9c` | `49 e8 8e 52` | mov w9,#0x7742 | `FALL_THROUGH`
<a id="insn-00a6cca0"></a> `00a6cca0` | `89 92 0b 78` | sturh w9,[x20, #0xb9] | `FALL_THROUGH`
<a id="insn-00a6cca4"></a> `00a6cca4` | `c9 00 80 52` | mov w9,#0x6 | `FALL_THROUGH`
<a id="insn-00a6cca8"></a> `00a6cca8` | `e9 cb 00 b9` | str w9,[sp, #0xc8] | `FALL_THROUGH`
<a id="insn-00a6ccac"></a> `00a6ccac` | `a9 c1 ff f0` | adrp x9,0x2a3000 | `FALL_THROUGH`
<a id="insn-00a6ccb0"></a> `00a6ccb0` | `29 f1 3a 91` | add x9,x9,#0xebc | `FALL_THROUGH`
<a id="insn-00a6ccb4"></a> `00a6ccb4` | `80 92 8a 3c` | stur q0,[x20, #0xa9] | `FALL_THROUGH`
<a id="insn-00a6ccb8"></a> `00a6ccb8` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00a6ccbc"></a> `00a6ccbc` | `e8 43 00 39` | strb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a6ccc0"></a> `00a6ccc0` | `e8 c3 00 39` | strb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00a6ccc4"></a> `00a6ccc4` | `e8 43 01 39` | strb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00a6ccc8"></a> `00a6ccc8` | `e8 c3 01 39` | strb w8,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00a6cccc"></a> `00a6cccc` | `e8 43 02 39` | strb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00a6ccd0"></a> `00a6ccd0` | `e8 c3 02 39` | strb w8,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00a6ccd4"></a> `00a6ccd4` | `e8 43 03 39` | strb w8,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-00a6ccd8"></a> `00a6ccd8` | `68 28 88 52` | mov w8,#0x4143 | `FALL_THROUGH`
<a id="insn-00a6ccdc"></a> `00a6ccdc` | `ff 0b 00 b9` | str wzr,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00a6cce0"></a> `00a6cce0` | `ff 8f 00 39` | strb wzr,[sp, #0x23] | `FALL_THROUGH`
<a id="insn-00a6cce4"></a> `00a6cce4` | `ff 0f 01 39` | strb wzr,[sp, #0x43] | `FALL_THROUGH`
<a id="insn-00a6cce8"></a> `00a6cce8` | `ff 8f 01 39` | strb wzr,[sp, #0x63] | `FALL_THROUGH`
<a id="insn-00a6ccec"></a> `00a6ccec` | `ff 0f 02 39` | strb wzr,[sp, #0x83] | `FALL_THROUGH`
<a id="insn-00a6ccf0"></a> `00a6ccf0` | `ff 8f 02 39` | strb wzr,[sp, #0xa3] | `FALL_THROUGH`
<a id="insn-00a6ccf4"></a> `00a6ccf4` | `ff 0f 03 39` | strb wzr,[sp, #0xc3] | `FALL_THROUGH`
<a id="insn-00a6ccf8"></a> `00a6ccf8` | `88 92 0d 78` | sturh w8,[x20, #0xd9] | `FALL_THROUGH`
<a id="insn-00a6ccfc"></a> `00a6ccfc` | `80 92 8c 3c` | stur q0,[x20, #0xc9] | `FALL_THROUGH`
<a id="insn-00a6cd00"></a> `00a6cd00` | `ff 8f 03 39` | strb wzr,[sp, #0xe3] | `FALL_THROUGH`
<a id="insn-00a6cd04"></a> `00a6cd04` | `7f 0a 00 f9` | str xzr,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00a6cd08"></a> `00a6cd08` | `3f 8c 00 f8` | str xzr,[x1, #0x8]! | `FALL_THROUGH`
<a id="insn-00a6cd0c"></a> `00a6cd0c` | `61 02 00 f9` | str x1,[x19] | `FALL_THROUGH`
<a id="insn-00a6cd10"></a> `00a6cd10` | `e2 23 00 91` | add x2,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00a6cd14"></a> `00a6cd14` | `e3 23 00 91` | add x3,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00a6cd18"></a> `00a6cd18` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00a6cd1c"></a> `00a6cd1c` | `c7 3a e7 97` | bl 0x0043b838 | `UNCONDITIONAL_CALL`
<a id="insn-00a6cd20"></a> `00a6cd20` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00a6cd24"></a> `00a6cd24` | `82 82 00 91` | add x2,x20,#0x20 | `FALL_THROUGH`
<a id="insn-00a6cd28"></a> `00a6cd28` | `83 82 00 91` | add x3,x20,#0x20 | `FALL_THROUGH`
<a id="insn-00a6cd2c"></a> `00a6cd2c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00a6cd30"></a> `00a6cd30` | `c2 3a e7 97` | bl 0x0043b838 | `UNCONDITIONAL_CALL`
<a id="insn-00a6cd34"></a> `00a6cd34` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00a6cd38"></a> `00a6cd38` | `82 02 01 91` | add x2,x20,#0x40 | `FALL_THROUGH`
<a id="insn-00a6cd3c"></a> `00a6cd3c` | `83 02 01 91` | add x3,x20,#0x40 | `FALL_THROUGH`
<a id="insn-00a6cd40"></a> `00a6cd40` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00a6cd44"></a> `00a6cd44` | `bd 3a e7 97` | bl 0x0043b838 | `UNCONDITIONAL_CALL`
<a id="insn-00a6cd48"></a> `00a6cd48` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00a6cd4c"></a> `00a6cd4c` | `82 82 01 91` | add x2,x20,#0x60 | `FALL_THROUGH`
<a id="insn-00a6cd50"></a> `00a6cd50` | `83 82 01 91` | add x3,x20,#0x60 | `FALL_THROUGH`
<a id="insn-00a6cd54"></a> `00a6cd54` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00a6cd58"></a> `00a6cd58` | `b8 3a e7 97` | bl 0x0043b838 | `UNCONDITIONAL_CALL`
<a id="insn-00a6cd5c"></a> `00a6cd5c` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00a6cd60"></a> `00a6cd60` | `82 02 02 91` | add x2,x20,#0x80 | `FALL_THROUGH`
<a id="insn-00a6cd64"></a> `00a6cd64` | `83 02 02 91` | add x3,x20,#0x80 | `FALL_THROUGH`
<a id="insn-00a6cd68"></a> `00a6cd68` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00a6cd6c"></a> `00a6cd6c` | `b3 3a e7 97` | bl 0x0043b838 | `UNCONDITIONAL_CALL`
<a id="insn-00a6cd70"></a> `00a6cd70` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00a6cd74"></a> `00a6cd74` | `82 82 02 91` | add x2,x20,#0xa0 | `FALL_THROUGH`
<a id="insn-00a6cd78"></a> `00a6cd78` | `83 82 02 91` | add x3,x20,#0xa0 | `FALL_THROUGH`
<a id="insn-00a6cd7c"></a> `00a6cd7c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00a6cd80"></a> `00a6cd80` | `ae 3a e7 97` | bl 0x0043b838 | `UNCONDITIONAL_CALL`
<a id="insn-00a6cd84"></a> `00a6cd84` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00a6cd88"></a> `00a6cd88` | `82 02 03 91` | add x2,x20,#0xc0 | `FALL_THROUGH`
<a id="insn-00a6cd8c"></a> `00a6cd8c` | `83 02 03 91` | add x3,x20,#0xc0 | `FALL_THROUGH`
<a id="insn-00a6cd90"></a> `00a6cd90` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00a6cd94"></a> `00a6cd94` | `a9 3a e7 97` | bl 0x0043b838 | `UNCONDITIONAL_CALL`
<a id="insn-00a6cd98"></a> `00a6cd98` | `e8 43 43 39` | ldrb w8,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-00a6cd9c"></a> `00a6cd9c` | `e8 03 00 37` | tbnz w8,#0x0,0x00a6ce18 | `CONDITIONAL_JUMP`
<a id="insn-00a6cda0"></a> `00a6cda0` | `e8 c3 42 39` | ldrb w8,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00a6cda4"></a> `00a6cda4` | `28 04 00 37` | tbnz w8,#0x0,0x00a6ce28 | `CONDITIONAL_JUMP`
<a id="insn-00a6cda8"></a> `00a6cda8` | `e8 43 42 39` | ldrb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00a6cdac"></a> `00a6cdac` | `68 04 00 37` | tbnz w8,#0x0,0x00a6ce38 | `CONDITIONAL_JUMP`
<a id="insn-00a6cdb0"></a> `00a6cdb0` | `e8 c3 41 39` | ldrb w8,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00a6cdb4"></a> `00a6cdb4` | `a8 04 00 37` | tbnz w8,#0x0,0x00a6ce48 | `CONDITIONAL_JUMP`
<a id="insn-00a6cdb8"></a> `00a6cdb8` | `e8 43 41 39` | ldrb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00a6cdbc"></a> `00a6cdbc` | `e8 04 00 37` | tbnz w8,#0x0,0x00a6ce58 | `CONDITIONAL_JUMP`
<a id="insn-00a6cdc0"></a> `00a6cdc0` | `e8 c3 40 39` | ldrb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00a6cdc4"></a> `00a6cdc4` | `28 05 00 37` | tbnz w8,#0x0,0x00a6ce68 | `CONDITIONAL_JUMP`
<a id="insn-00a6cdc8"></a> `00a6cdc8` | `e8 43 40 39` | ldrb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a6cdcc"></a> `00a6cdcc` | `68 00 00 36` | tbz w8,#0x0,0x00a6cdd8 | `CONDITIONAL_JUMP`
<a id="insn-00a6cdd0"></a> `00a6cdd0` | `e0 13 40 f9` | ldr x0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00a6cdd4"></a> `00a6cdd4` | `6b ac 07 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00a6cdd8"></a> `00a6cdd8` | `60 ce ff d0` | adrp x0,0x43a000 | `FALL_THROUGH`
<a id="insn-00a6cddc"></a> `00a6cddc` | `00 c0 3a 91` | add x0,x0,#0xeb0 | `FALL_THROUGH`
<a id="insn-00a6cde0"></a> `00a6cde0` | `c1 35 00 90` | adrp x1,0x1124000 | `FALL_THROUGH`
<a id="insn-00a6cde4"></a> `00a6cde4` | `21 c0 04 91` | add x1,x1,#0x130 | `FALL_THROUGH`
<a id="insn-00a6cde8"></a> `00a6cde8` | `a2 0f 00 f0` | adrp x2,0xc63000 | `FALL_THROUGH`
<a id="insn-00a6cdec"></a> `00a6cdec` | `42 80 01 91` | add x2,x2,#0x60 | `FALL_THROUGH`
<a id="insn-00a6cdf0"></a> `00a6cdf0` | `44 ac 07 94` | bl 0x00c57f00 | `UNCONDITIONAL_CALL`
<a id="insn-00a6cdf4"></a> `00a6cdf4` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00a6cdf8"></a> `00a6cdf8` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00a6cdfc"></a> `00a6cdfc` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00a6ce00"></a> `00a6ce00` | `41 0a 00 54` | b.ne 0x00a6cf48 | `CONDITIONAL_JUMP`
<a id="insn-00a6ce04"></a> `00a6ce04` | `f4 4f 51 a9` | ldp x20,x19,[sp, #0x110] | `FALL_THROUGH`
<a id="insn-00a6ce08"></a> `00a6ce08` | `fc 57 50 a9` | ldp x28,x21,[sp, #0x100] | `FALL_THROUGH`
<a id="insn-00a6ce0c"></a> `00a6ce0c` | `fd 7b 4f a9` | ldp x29,x30,[sp, #0xf0] | `FALL_THROUGH`
<a id="insn-00a6ce10"></a> `00a6ce10` | `ff 83 04 91` | add sp,sp,#0x120 | `FALL_THROUGH`
<a id="insn-00a6ce14"></a> `00a6ce14` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00a6ce18"></a> `00a6ce18` | `e0 73 40 f9` | ldr x0,[sp, #0xe0] | `FALL_THROUGH`
<a id="insn-00a6ce1c"></a> `00a6ce1c` | `59 ac 07 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00a6ce20"></a> `00a6ce20` | `e8 c3 42 39` | ldrb w8,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00a6ce24"></a> `00a6ce24` | `28 fc 07 36` | tbz w8,#0x0,0x00a6cda8 | `CONDITIONAL_JUMP`
<a id="insn-00a6ce28"></a> `00a6ce28` | `e0 63 40 f9` | ldr x0,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00a6ce2c"></a> `00a6ce2c` | `55 ac 07 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00a6ce30"></a> `00a6ce30` | `e8 43 42 39` | ldrb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00a6ce34"></a> `00a6ce34` | `e8 fb 07 36` | tbz w8,#0x0,0x00a6cdb0 | `CONDITIONAL_JUMP`
<a id="insn-00a6ce38"></a> `00a6ce38` | `e0 53 40 f9` | ldr x0,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00a6ce3c"></a> `00a6ce3c` | `51 ac 07 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00a6ce40"></a> `00a6ce40` | `e8 c3 41 39` | ldrb w8,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00a6ce44"></a> `00a6ce44` | `a8 fb 07 36` | tbz w8,#0x0,0x00a6cdb8 | `CONDITIONAL_JUMP`
<a id="insn-00a6ce48"></a> `00a6ce48` | `e0 43 40 f9` | ldr x0,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00a6ce4c"></a> `00a6ce4c` | `4d ac 07 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00a6ce50"></a> `00a6ce50` | `e8 43 41 39` | ldrb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00a6ce54"></a> `00a6ce54` | `68 fb 07 36` | tbz w8,#0x0,0x00a6cdc0 | `CONDITIONAL_JUMP`
<a id="insn-00a6ce58"></a> `00a6ce58` | `e0 33 40 f9` | ldr x0,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00a6ce5c"></a> `00a6ce5c` | `49 ac 07 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00a6ce60"></a> `00a6ce60` | `e8 c3 40 39` | ldrb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00a6ce64"></a> `00a6ce64` | `28 fb 07 36` | tbz w8,#0x0,0x00a6cdc8 | `CONDITIONAL_JUMP`
<a id="insn-00a6ce68"></a> `00a6ce68` | `e0 23 40 f9` | ldr x0,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00a6ce6c"></a> `00a6ce6c` | `45 ac 07 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00a6ce70"></a> `00a6ce70` | `e8 43 40 39` | ldrb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a6ce74"></a> `00a6ce74` | `e8 fa 07 37` | tbnz w8,#0x0,0x00a6cdd0 | `CONDITIONAL_JUMP`
<a id="insn-00a6ce78"></a> `00a6ce78` | `d8 ff ff 17` | b 0x00a6cdd8 | `UNCONDITIONAL_JUMP`
<a id="insn-00a6cf48"></a> `00a6cf48` | `1a ac 07 94` | bl 0x00c57fb0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00a6cbbc`](#insn-00a6cbbc) 範囲 `[['00a6cbbc', '00a6ccbf']]`
  - `FALL_THROUGH` [`00a6ccbc`](#insn-00a6ccbc) → [`00a6ccc0`](#insn-00a6ccc0)
- ブロック [`00a6ccc0`](#insn-00a6ccc0) 範囲 `[['00a6ccc0', '00a6cd43']]`
  - `FALL_THROUGH` [`00a6cd40`](#insn-00a6cd40) → [`00a6cd44`](#insn-00a6cd44)
- ブロック [`00a6cd44`](#insn-00a6cd44) 範囲 `[['00a6cd44', '00a6cd93']]`
  - `FALL_THROUGH` [`00a6cd90`](#insn-00a6cd90) → [`00a6cd94`](#insn-00a6cd94)
- ブロック [`00a6cd94`](#insn-00a6cd94) 範囲 `[['00a6cd94', '00a6cd9f']]`
  - `CONDITIONAL_JUMP` [`00a6cd9c`](#insn-00a6cd9c) → [`00a6ce18`](#insn-00a6ce18)
  - `FALL_THROUGH` [`00a6cd9c`](#insn-00a6cd9c) → [`00a6cda0`](#insn-00a6cda0)
- ブロック [`00a6cda0`](#insn-00a6cda0) 範囲 `[['00a6cda0', '00a6cda7']]`
  - `CONDITIONAL_JUMP` [`00a6cda4`](#insn-00a6cda4) → [`00a6ce28`](#insn-00a6ce28)
  - `FALL_THROUGH` [`00a6cda4`](#insn-00a6cda4) → [`00a6cda8`](#insn-00a6cda8)
- ブロック [`00a6cda8`](#insn-00a6cda8) 範囲 `[['00a6cda8', '00a6cdaf']]`
  - `CONDITIONAL_JUMP` [`00a6cdac`](#insn-00a6cdac) → [`00a6ce38`](#insn-00a6ce38)
  - `FALL_THROUGH` [`00a6cdac`](#insn-00a6cdac) → [`00a6cdb0`](#insn-00a6cdb0)
- ブロック [`00a6cdb0`](#insn-00a6cdb0) 範囲 `[['00a6cdb0', '00a6cdb7']]`
  - `CONDITIONAL_JUMP` [`00a6cdb4`](#insn-00a6cdb4) → [`00a6ce48`](#insn-00a6ce48)
  - `FALL_THROUGH` [`00a6cdb4`](#insn-00a6cdb4) → [`00a6cdb8`](#insn-00a6cdb8)
- ブロック [`00a6cdb8`](#insn-00a6cdb8) 範囲 `[['00a6cdb8', '00a6cdbf']]`
  - `CONDITIONAL_JUMP` [`00a6cdbc`](#insn-00a6cdbc) → [`00a6ce58`](#insn-00a6ce58)
  - `FALL_THROUGH` [`00a6cdbc`](#insn-00a6cdbc) → [`00a6cdc0`](#insn-00a6cdc0)
- ブロック [`00a6cdc0`](#insn-00a6cdc0) 範囲 `[['00a6cdc0', '00a6cdc7']]`
  - `CONDITIONAL_JUMP` [`00a6cdc4`](#insn-00a6cdc4) → [`00a6ce68`](#insn-00a6ce68)
  - `FALL_THROUGH` [`00a6cdc4`](#insn-00a6cdc4) → [`00a6cdc8`](#insn-00a6cdc8)
- ブロック [`00a6cdc8`](#insn-00a6cdc8) 範囲 `[['00a6cdc8', '00a6cdcf']]`
  - `CONDITIONAL_JUMP` [`00a6cdcc`](#insn-00a6cdcc) → [`00a6cdd8`](#insn-00a6cdd8)
  - `FALL_THROUGH` [`00a6cdcc`](#insn-00a6cdcc) → [`00a6cdd0`](#insn-00a6cdd0)
- ブロック [`00a6cdd0`](#insn-00a6cdd0) 範囲 `[['00a6cdd0', '00a6cdd7']]`
  - `FALL_THROUGH` [`00a6cdd4`](#insn-00a6cdd4) → [`00a6cdd8`](#insn-00a6cdd8)
- ブロック [`00a6cdd8`](#insn-00a6cdd8) 範囲 `[['00a6cdd8', '00a6cde3']]`
  - `FALL_THROUGH` [`00a6cde0`](#insn-00a6cde0) → [`00a6cde4`](#insn-00a6cde4)
- ブロック [`00a6cde4`](#insn-00a6cde4) 範囲 `[['00a6cde4', '00a6ce03']]`
  - `CONDITIONAL_JUMP` [`00a6ce00`](#insn-00a6ce00) → [`00a6cf48`](#insn-00a6cf48)
  - `FALL_THROUGH` [`00a6ce00`](#insn-00a6ce00) → [`00a6ce04`](#insn-00a6ce04)
- ブロック [`00a6ce04`](#insn-00a6ce04) 範囲 `[['00a6ce04', '00a6ce17']]`
- ブロック [`00a6ce18`](#insn-00a6ce18) 範囲 `[['00a6ce18', '00a6ce27']]`
  - `CONDITIONAL_JUMP` [`00a6ce24`](#insn-00a6ce24) → [`00a6cda8`](#insn-00a6cda8)
  - `FALL_THROUGH` [`00a6ce24`](#insn-00a6ce24) → [`00a6ce28`](#insn-00a6ce28)
- ブロック [`00a6ce28`](#insn-00a6ce28) 範囲 `[['00a6ce28', '00a6ce37']]`
  - `CONDITIONAL_JUMP` [`00a6ce34`](#insn-00a6ce34) → [`00a6cdb0`](#insn-00a6cdb0)
  - `FALL_THROUGH` [`00a6ce34`](#insn-00a6ce34) → [`00a6ce38`](#insn-00a6ce38)
- ブロック [`00a6ce38`](#insn-00a6ce38) 範囲 `[['00a6ce38', '00a6ce47']]`
  - `CONDITIONAL_JUMP` [`00a6ce44`](#insn-00a6ce44) → [`00a6cdb8`](#insn-00a6cdb8)
  - `FALL_THROUGH` [`00a6ce44`](#insn-00a6ce44) → [`00a6ce48`](#insn-00a6ce48)
- ブロック [`00a6ce48`](#insn-00a6ce48) 範囲 `[['00a6ce48', '00a6ce57']]`
  - `CONDITIONAL_JUMP` [`00a6ce54`](#insn-00a6ce54) → [`00a6cdc0`](#insn-00a6cdc0)
  - `FALL_THROUGH` [`00a6ce54`](#insn-00a6ce54) → [`00a6ce58`](#insn-00a6ce58)
- ブロック [`00a6ce58`](#insn-00a6ce58) 範囲 `[['00a6ce58', '00a6ce67']]`
  - `CONDITIONAL_JUMP` [`00a6ce64`](#insn-00a6ce64) → [`00a6cdc8`](#insn-00a6cdc8)
  - `FALL_THROUGH` [`00a6ce64`](#insn-00a6ce64) → [`00a6ce68`](#insn-00a6ce68)
- ブロック [`00a6ce68`](#insn-00a6ce68) 範囲 `[['00a6ce68', '00a6ce77']]`
  - `CONDITIONAL_JUMP` [`00a6ce74`](#insn-00a6ce74) → [`00a6cdd0`](#insn-00a6cdd0)
  - `FALL_THROUGH` [`00a6ce74`](#insn-00a6ce74) → [`00a6ce78`](#insn-00a6ce78)
- ブロック [`00a6ce78`](#insn-00a6ce78) 範囲 `[['00a6ce78', '00a6ce7b']]`
  - `UNCONDITIONAL_JUMP` [`00a6ce78`](#insn-00a6ce78) → [`00a6cdd8`](#insn-00a6cdd8)
- ブロック [`00a6cf48`](#insn-00a6cf48) 範囲 `[['00a6cf48', '00a6cf4b']]`

## 命令位置別の参照

- [`00a6cbc0`](#insn-00a6cbc0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6cbc4`](#insn-00a6cbc4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6cbc8`](#insn-00a6cbc8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6cbec`](#insn-00a6cbec) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6cbf8`](#insn-00a6cbf8) → `002b7f66`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00a6cc00`](#insn-00a6cc00) → `Stack[-0xff]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6cc04`](#insn-00a6cc04) → `Stack[-0xf8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6cc14`](#insn-00a6cc14) → `Stack[-0x10f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6cc1c`](#insn-00a6cc1c) → `002b7f79`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00a6cc20`](#insn-00a6cc20) → `Stack[-0xdf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6cc28`](#insn-00a6cc28) → `Stack[-0xd8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6cc38`](#insn-00a6cc38) → `Stack[-0xef]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6cc3c`](#insn-00a6cc3c) → `002b8d6e`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00a6cc40`](#insn-00a6cc40) → `Stack[-0xbf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6cc48`](#insn-00a6cc48) → `Stack[-0xb8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6cc58`](#insn-00a6cc58) → `Stack[-0xcf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6cc5c`](#insn-00a6cc5c) → `002a2f15`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00a6cc60`](#insn-00a6cc60) → `Stack[-0x9f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6cc68`](#insn-00a6cc68) → `Stack[-0x98]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6cc74`](#insn-00a6cc74) → `Stack[-0xaf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6cc78`](#insn-00a6cc78) → `002ac576`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00a6cc80`](#insn-00a6cc80) → `Stack[-0x7f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6cc88`](#insn-00a6cc88) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6cc94`](#insn-00a6cc94) → `Stack[-0x8f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6cc98`](#insn-00a6cc98) → `002a0f10`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00a6cca0`](#insn-00a6cca0) → `Stack[-0x5f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6cca8`](#insn-00a6cca8) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ccb4`](#insn-00a6ccb4) → `Stack[-0x6f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ccb8`](#insn-00a6ccb8) → `002a3ebc`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00a6ccbc`](#insn-00a6ccbc) → `Stack[-0x110]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ccc0`](#insn-00a6ccc0) → `Stack[-0xf0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ccc4`](#insn-00a6ccc4) → `Stack[-0xd0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ccc8`](#insn-00a6ccc8) → `Stack[-0xb0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6cccc`](#insn-00a6cccc) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ccd0`](#insn-00a6ccd0) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ccd4`](#insn-00a6ccd4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ccdc`](#insn-00a6ccdc) → `Stack[-0x118]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6cce0`](#insn-00a6cce0) → `Stack[-0xfd]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6cce4`](#insn-00a6cce4) → `Stack[-0xdd]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6cce8`](#insn-00a6cce8) → `Stack[-0xbd]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ccec`](#insn-00a6ccec) → `Stack[-0x9d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ccf0`](#insn-00a6ccf0) → `Stack[-0x7d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ccf4`](#insn-00a6ccf4) → `Stack[-0x5d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ccf8`](#insn-00a6ccf8) → `Stack[-0x3f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ccfc`](#insn-00a6ccfc) → `Stack[-0x4f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6cd00`](#insn-00a6cd00) → `Stack[-0x3d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6cd04`](#insn-00a6cd04) → `01124140`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a6cd08`](#insn-00a6cd08) → `01124138`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a6cd0c`](#insn-00a6cd0c) → `01124130`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a6cd0c`](#insn-00a6cd0c) → `01124138`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a6cd18`](#insn-00a6cd18) → `01124130`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a6cd1c`](#insn-00a6cd1c) → [`0043b838`](../0043b/0043b838.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043b838` · 推定シンボル `None` · 推定型 `None`
- [`00a6cd20`](#insn-00a6cd20) → `01124138`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a6cd2c`](#insn-00a6cd2c) → `01124130`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a6cd30`](#insn-00a6cd30) → [`0043b838`](../0043b/0043b838.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043b838` · 推定シンボル `None` · 推定型 `None`
- [`00a6cd34`](#insn-00a6cd34) → `01124138`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a6cd40`](#insn-00a6cd40) → `01124130`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a6cd44`](#insn-00a6cd44) → [`0043b838`](../0043b/0043b838.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043b838` · 推定シンボル `None` · 推定型 `None`
- [`00a6cd48`](#insn-00a6cd48) → `01124138`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a6cd54`](#insn-00a6cd54) → `01124130`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a6cd58`](#insn-00a6cd58) → [`0043b838`](../0043b/0043b838.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043b838` · 推定シンボル `None` · 推定型 `None`
- [`00a6cd5c`](#insn-00a6cd5c) → `01124138`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a6cd68`](#insn-00a6cd68) → `01124130`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a6cd6c`](#insn-00a6cd6c) → [`0043b838`](../0043b/0043b838.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043b838` · 推定シンボル `None` · 推定型 `None`
- [`00a6cd70`](#insn-00a6cd70) → `01124138`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a6cd7c`](#insn-00a6cd7c) → `01124130`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a6cd80`](#insn-00a6cd80) → [`0043b838`](../0043b/0043b838.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043b838` · 推定シンボル `None` · 推定型 `None`
- [`00a6cd84`](#insn-00a6cd84) → `01124138`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a6cd90`](#insn-00a6cd90) → `01124130`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a6cd94`](#insn-00a6cd94) → [`0043b838`](../0043b/0043b838.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043b838` · 推定シンボル `None` · 推定型 `None`
- [`00a6cd98`](#insn-00a6cd98) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6cd9c`](#insn-00a6cd9c) → [`00a6ce18`](#insn-00a6ce18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6cda0`](#insn-00a6cda0) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6cda4`](#insn-00a6cda4) → [`00a6ce28`](#insn-00a6ce28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6cda8`](#insn-00a6cda8) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6cdac`](#insn-00a6cdac) → [`00a6ce38`](#insn-00a6ce38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6cdb0`](#insn-00a6cdb0) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6cdb4`](#insn-00a6cdb4) → [`00a6ce48`](#insn-00a6ce48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6cdb8`](#insn-00a6cdb8) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6cdbc`](#insn-00a6cdbc) → [`00a6ce58`](#insn-00a6ce58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6cdc0`](#insn-00a6cdc0) → `Stack[-0xf0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6cdc4`](#insn-00a6cdc4) → [`00a6ce68`](#insn-00a6ce68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6cdc8`](#insn-00a6cdc8) → `Stack[-0x110]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6cdcc`](#insn-00a6cdcc) → [`00a6cdd8`](#insn-00a6cdd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6cdd0`](#insn-00a6cdd0) → `Stack[-0x100]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6cdd4`](#insn-00a6cdd4) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00a6cddc`](#insn-00a6cddc) → [`0043aeb0`](../0043a/0043aeb0.md) · `PARAM` · `ANALYSIS` · 関数 `0043aeb0` · 推定シンボル `None` · 推定型 `None`
- [`00a6cde4`](#insn-00a6cde4) → `01124130`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a6cdec`](#insn-00a6cdec) → `00c63060`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00a6cdf0`](#insn-00a6cdf0) → [`00c57f00`](../00c57/00c57f00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f00` · 推定シンボル `None` · 推定型 `None`
- [`00a6cdf8`](#insn-00a6cdf8) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ce00`](#insn-00a6ce00) → [`00a6cf48`](#insn-00a6cf48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ce04`](#insn-00a6ce04) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ce08`](#insn-00a6ce08) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ce0c`](#insn-00a6ce0c) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ce18`](#insn-00a6ce18) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ce1c`](#insn-00a6ce1c) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00a6ce20`](#insn-00a6ce20) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ce24`](#insn-00a6ce24) → [`00a6cda8`](#insn-00a6cda8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ce28`](#insn-00a6ce28) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ce2c`](#insn-00a6ce2c) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00a6ce30`](#insn-00a6ce30) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ce34`](#insn-00a6ce34) → [`00a6cdb0`](#insn-00a6cdb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ce38`](#insn-00a6ce38) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ce3c`](#insn-00a6ce3c) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00a6ce40`](#insn-00a6ce40) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ce44`](#insn-00a6ce44) → [`00a6cdb8`](#insn-00a6cdb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ce48`](#insn-00a6ce48) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ce4c`](#insn-00a6ce4c) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00a6ce50`](#insn-00a6ce50) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ce54`](#insn-00a6ce54) → [`00a6cdc0`](#insn-00a6cdc0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ce58`](#insn-00a6ce58) → `Stack[-0xc0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ce5c`](#insn-00a6ce5c) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00a6ce60`](#insn-00a6ce60) → `Stack[-0xf0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ce64`](#insn-00a6ce64) → [`00a6cdc8`](#insn-00a6cdc8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ce68`](#insn-00a6ce68) → `Stack[-0xe0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ce6c`](#insn-00a6ce6c) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00a6ce70`](#insn-00a6ce70) → `Stack[-0x110]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ce74`](#insn-00a6ce74) → [`00a6cdd0`](#insn-00a6cdd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ce78`](#insn-00a6ce78) → [`00a6cdd8`](#insn-00a6cdd8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6cf48`](#insn-00a6cf48) → [`00c57fb0`](../00c57/00c57fb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fb0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00a6cbc0`](#insn-00a6cbc0)

~~~json
{
  "source": "00a6cbc0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6cbc4`](#insn-00a6cbc4)

~~~json
{
  "source": "00a6cbc4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6cbc8`](#insn-00a6cbc8)

~~~json
{
  "source": "00a6cbc8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6cbec`](#insn-00a6cbec)

~~~json
{
  "source": "00a6cbec",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6cbf8`](#insn-00a6cbf8)

~~~json
{
  "source": "00a6cbf8",
  "target": "002b7f66",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b7f66",
  "offset": 0,
  "size": 19,
  "datatype": "string",
  "bytes": "43676b496a4d33795f5a516145414951416700",
  "capture_start": "002b7f66",
  "capture_bytes": 19,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a6cc00`](#insn-00a6cc00)

~~~json
{
  "source": "00a6cc00",
  "target": "Stack[-0xff]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6cc04`](#insn-00a6cc04)

~~~json
{
  "source": "00a6cc04",
  "target": "Stack[-0xf8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6cc14`](#insn-00a6cc14)

~~~json
{
  "source": "00a6cc14",
  "target": "Stack[-0x10f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6cc1c`](#insn-00a6cc1c)

~~~json
{
  "source": "00a6cc1c",
  "target": "002b7f79",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b7f79",
  "offset": 0,
  "size": 19,
  "datatype": "string",
  "bytes": "43676b496a4d33795f5a516145414951424100",
  "capture_start": "002b7f79",
  "capture_bytes": 19,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a6cc20`](#insn-00a6cc20)

~~~json
{
  "source": "00a6cc20",
  "target": "Stack[-0xdf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6cc28`](#insn-00a6cc28)

~~~json
{
  "source": "00a6cc28",
  "target": "Stack[-0xd8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6cc38`](#insn-00a6cc38)

~~~json
{
  "source": "00a6cc38",
  "target": "Stack[-0xef]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6cc3c`](#insn-00a6cc3c)

~~~json
{
  "source": "00a6cc3c",
  "target": "002b8d6e",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b8d6e",
  "offset": 0,
  "size": 19,
  "datatype": "string",
  "bytes": "43676b496a4d33795f5a516145414951426700",
  "capture_start": "002b8d6e",
  "capture_bytes": 19,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a6cc40`](#insn-00a6cc40)

~~~json
{
  "source": "00a6cc40",
  "target": "Stack[-0xbf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6cc48`](#insn-00a6cc48)

~~~json
{
  "source": "00a6cc48",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6cc58`](#insn-00a6cc58)

~~~json
{
  "source": "00a6cc58",
  "target": "Stack[-0xcf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6cc5c`](#insn-00a6cc5c)

~~~json
{
  "source": "00a6cc5c",
  "target": "002a2f15",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a2f15",
  "offset": 0,
  "size": 19,
  "datatype": "string",
  "bytes": "43676b496a4d33795f5a516145414951417700",
  "capture_start": "002a2f15",
  "capture_bytes": 19,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a6cc60`](#insn-00a6cc60)

~~~json
{
  "source": "00a6cc60",
  "target": "Stack[-0x9f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6cc68`](#insn-00a6cc68)

~~~json
{
  "source": "00a6cc68",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6cc74`](#insn-00a6cc74)

~~~json
{
  "source": "00a6cc74",
  "target": "Stack[-0xaf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6cc78`](#insn-00a6cc78)

~~~json
{
  "source": "00a6cc78",
  "target": "002ac576",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002ac576",
  "offset": 0,
  "size": 19,
  "datatype": "string",
  "bytes": "43676b496a4d33795f5a516145414951425100",
  "capture_start": "002ac576",
  "capture_bytes": 19,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a6cc80`](#insn-00a6cc80)

~~~json
{
  "source": "00a6cc80",
  "target": "Stack[-0x7f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6cc88`](#insn-00a6cc88)

~~~json
{
  "source": "00a6cc88",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6cc94`](#insn-00a6cc94)

~~~json
{
  "source": "00a6cc94",
  "target": "Stack[-0x8f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6cc98`](#insn-00a6cc98)

~~~json
{
  "source": "00a6cc98",
  "target": "002a0f10",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a0f10",
  "offset": 0,
  "size": 19,
  "datatype": "string",
  "bytes": "43676b496a4d33795f5a516145414951427700",
  "capture_start": "002a0f10",
  "capture_bytes": 19,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a6cca0`](#insn-00a6cca0)

~~~json
{
  "source": "00a6cca0",
  "target": "Stack[-0x5f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6cca8`](#insn-00a6cca8)

~~~json
{
  "source": "00a6cca8",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ccb4`](#insn-00a6ccb4)

~~~json
{
  "source": "00a6ccb4",
  "target": "Stack[-0x6f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ccb8`](#insn-00a6ccb8)

~~~json
{
  "source": "00a6ccb8",
  "target": "002a3ebc",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a3ebc",
  "offset": 0,
  "size": 19,
  "datatype": "string",
  "bytes": "43676b496a4d33795f5a516145414951434100",
  "capture_start": "002a3ebc",
  "capture_bytes": 19,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a6ccbc`](#insn-00a6ccbc)

~~~json
{
  "source": "00a6ccbc",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ccc0`](#insn-00a6ccc0)

~~~json
{
  "source": "00a6ccc0",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ccc4`](#insn-00a6ccc4)

~~~json
{
  "source": "00a6ccc4",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ccc8`](#insn-00a6ccc8)

~~~json
{
  "source": "00a6ccc8",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6cccc`](#insn-00a6cccc)

~~~json
{
  "source": "00a6cccc",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ccd0`](#insn-00a6ccd0)

~~~json
{
  "source": "00a6ccd0",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ccd4`](#insn-00a6ccd4)

~~~json
{
  "source": "00a6ccd4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ccdc`](#insn-00a6ccdc)

~~~json
{
  "source": "00a6ccdc",
  "target": "Stack[-0x118]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6cce0`](#insn-00a6cce0)

~~~json
{
  "source": "00a6cce0",
  "target": "Stack[-0xfd]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6cce4`](#insn-00a6cce4)

~~~json
{
  "source": "00a6cce4",
  "target": "Stack[-0xdd]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6cce8`](#insn-00a6cce8)

~~~json
{
  "source": "00a6cce8",
  "target": "Stack[-0xbd]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ccec`](#insn-00a6ccec)

~~~json
{
  "source": "00a6ccec",
  "target": "Stack[-0x9d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ccf0`](#insn-00a6ccf0)

~~~json
{
  "source": "00a6ccf0",
  "target": "Stack[-0x7d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ccf4`](#insn-00a6ccf4)

~~~json
{
  "source": "00a6ccf4",
  "target": "Stack[-0x5d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ccf8`](#insn-00a6ccf8)

~~~json
{
  "source": "00a6ccf8",
  "target": "Stack[-0x3f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ccfc`](#insn-00a6ccfc)

~~~json
{
  "source": "00a6ccfc",
  "target": "Stack[-0x4f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6cd00`](#insn-00a6cd00)

~~~json
{
  "source": "00a6cd00",
  "target": "Stack[-0x3d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6cd04`](#insn-00a6cd04)

~~~json
{
  "source": "00a6cd04",
  "target": "01124140",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01124140",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a6cd08`](#insn-00a6cd08)

~~~json
{
  "source": "00a6cd08",
  "target": "01124138",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01124138",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a6cd0c`](#insn-00a6cd0c)

~~~json
{
  "source": "00a6cd0c",
  "target": "01124130",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01124130",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a6cd0c`](#insn-00a6cd0c)

~~~json
{
  "source": "00a6cd0c",
  "target": "01124138",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01124138",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a6cd18`](#insn-00a6cd18)

~~~json
{
  "source": "00a6cd18",
  "target": "01124130",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01124130",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a6cd1c`](#insn-00a6cd1c)

~~~json
{
  "source": "00a6cd1c",
  "target": "0043b838",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6cd20`](#insn-00a6cd20)

~~~json
{
  "source": "00a6cd20",
  "target": "01124138",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01124138",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a6cd2c`](#insn-00a6cd2c)

~~~json
{
  "source": "00a6cd2c",
  "target": "01124130",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01124130",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a6cd30`](#insn-00a6cd30)

~~~json
{
  "source": "00a6cd30",
  "target": "0043b838",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6cd34`](#insn-00a6cd34)

~~~json
{
  "source": "00a6cd34",
  "target": "01124138",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01124138",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a6cd40`](#insn-00a6cd40)

~~~json
{
  "source": "00a6cd40",
  "target": "01124130",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01124130",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a6cd44`](#insn-00a6cd44)

~~~json
{
  "source": "00a6cd44",
  "target": "0043b838",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6cd48`](#insn-00a6cd48)

~~~json
{
  "source": "00a6cd48",
  "target": "01124138",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01124138",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a6cd54`](#insn-00a6cd54)

~~~json
{
  "source": "00a6cd54",
  "target": "01124130",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01124130",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a6cd58`](#insn-00a6cd58)

~~~json
{
  "source": "00a6cd58",
  "target": "0043b838",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6cd5c`](#insn-00a6cd5c)

~~~json
{
  "source": "00a6cd5c",
  "target": "01124138",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01124138",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a6cd68`](#insn-00a6cd68)

~~~json
{
  "source": "00a6cd68",
  "target": "01124130",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01124130",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a6cd6c`](#insn-00a6cd6c)

~~~json
{
  "source": "00a6cd6c",
  "target": "0043b838",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6cd70`](#insn-00a6cd70)

~~~json
{
  "source": "00a6cd70",
  "target": "01124138",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01124138",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a6cd7c`](#insn-00a6cd7c)

~~~json
{
  "source": "00a6cd7c",
  "target": "01124130",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01124130",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a6cd80`](#insn-00a6cd80)

~~~json
{
  "source": "00a6cd80",
  "target": "0043b838",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6cd84`](#insn-00a6cd84)

~~~json
{
  "source": "00a6cd84",
  "target": "01124138",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01124138",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a6cd90`](#insn-00a6cd90)

~~~json
{
  "source": "00a6cd90",
  "target": "01124130",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01124130",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a6cd94`](#insn-00a6cd94)

~~~json
{
  "source": "00a6cd94",
  "target": "0043b838",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6cd98`](#insn-00a6cd98)

~~~json
{
  "source": "00a6cd98",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6cd9c`](#insn-00a6cd9c)

~~~json
{
  "source": "00a6cd9c",
  "target": "00a6ce18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6cda0`](#insn-00a6cda0)

~~~json
{
  "source": "00a6cda0",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6cda4`](#insn-00a6cda4)

~~~json
{
  "source": "00a6cda4",
  "target": "00a6ce28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6cda8`](#insn-00a6cda8)

~~~json
{
  "source": "00a6cda8",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6cdac`](#insn-00a6cdac)

~~~json
{
  "source": "00a6cdac",
  "target": "00a6ce38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6cdb0`](#insn-00a6cdb0)

~~~json
{
  "source": "00a6cdb0",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6cdb4`](#insn-00a6cdb4)

~~~json
{
  "source": "00a6cdb4",
  "target": "00a6ce48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6cdb8`](#insn-00a6cdb8)

~~~json
{
  "source": "00a6cdb8",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6cdbc`](#insn-00a6cdbc)

~~~json
{
  "source": "00a6cdbc",
  "target": "00a6ce58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6cdc0`](#insn-00a6cdc0)

~~~json
{
  "source": "00a6cdc0",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6cdc4`](#insn-00a6cdc4)

~~~json
{
  "source": "00a6cdc4",
  "target": "00a6ce68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6cdc8`](#insn-00a6cdc8)

~~~json
{
  "source": "00a6cdc8",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6cdcc`](#insn-00a6cdcc)

~~~json
{
  "source": "00a6cdcc",
  "target": "00a6cdd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6cdd0`](#insn-00a6cdd0)

~~~json
{
  "source": "00a6cdd0",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6cdd4`](#insn-00a6cdd4)

~~~json
{
  "source": "00a6cdd4",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6cddc`](#insn-00a6cddc)

~~~json
{
  "source": "00a6cddc",
  "target": "0043aeb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6cde4`](#insn-00a6cde4)

~~~json
{
  "source": "00a6cde4",
  "target": "01124130",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01124130",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a6cdec`](#insn-00a6cdec)

~~~json
{
  "source": "00a6cdec",
  "target": "00c63060",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c63060",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00a6cdf0`](#insn-00a6cdf0)

~~~json
{
  "source": "00a6cdf0",
  "target": "00c57f00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6cdf8`](#insn-00a6cdf8)

~~~json
{
  "source": "00a6cdf8",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ce00`](#insn-00a6ce00)

~~~json
{
  "source": "00a6ce00",
  "target": "00a6cf48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ce04`](#insn-00a6ce04)

~~~json
{
  "source": "00a6ce04",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ce08`](#insn-00a6ce08)

~~~json
{
  "source": "00a6ce08",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ce0c`](#insn-00a6ce0c)

~~~json
{
  "source": "00a6ce0c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ce18`](#insn-00a6ce18)

~~~json
{
  "source": "00a6ce18",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ce1c`](#insn-00a6ce1c)

~~~json
{
  "source": "00a6ce1c",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6ce20`](#insn-00a6ce20)

~~~json
{
  "source": "00a6ce20",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ce24`](#insn-00a6ce24)

~~~json
{
  "source": "00a6ce24",
  "target": "00a6cda8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ce28`](#insn-00a6ce28)

~~~json
{
  "source": "00a6ce28",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ce2c`](#insn-00a6ce2c)

~~~json
{
  "source": "00a6ce2c",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6ce30`](#insn-00a6ce30)

~~~json
{
  "source": "00a6ce30",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ce34`](#insn-00a6ce34)

~~~json
{
  "source": "00a6ce34",
  "target": "00a6cdb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ce38`](#insn-00a6ce38)

~~~json
{
  "source": "00a6ce38",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ce3c`](#insn-00a6ce3c)

~~~json
{
  "source": "00a6ce3c",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6ce40`](#insn-00a6ce40)

~~~json
{
  "source": "00a6ce40",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ce44`](#insn-00a6ce44)

~~~json
{
  "source": "00a6ce44",
  "target": "00a6cdb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ce48`](#insn-00a6ce48)

~~~json
{
  "source": "00a6ce48",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ce4c`](#insn-00a6ce4c)

~~~json
{
  "source": "00a6ce4c",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6ce50`](#insn-00a6ce50)

~~~json
{
  "source": "00a6ce50",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ce54`](#insn-00a6ce54)

~~~json
{
  "source": "00a6ce54",
  "target": "00a6cdc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ce58`](#insn-00a6ce58)

~~~json
{
  "source": "00a6ce58",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ce5c`](#insn-00a6ce5c)

~~~json
{
  "source": "00a6ce5c",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6ce60`](#insn-00a6ce60)

~~~json
{
  "source": "00a6ce60",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ce64`](#insn-00a6ce64)

~~~json
{
  "source": "00a6ce64",
  "target": "00a6cdc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ce68`](#insn-00a6ce68)

~~~json
{
  "source": "00a6ce68",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ce6c`](#insn-00a6ce6c)

~~~json
{
  "source": "00a6ce6c",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6ce70`](#insn-00a6ce70)

~~~json
{
  "source": "00a6ce70",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ce74`](#insn-00a6ce74)

~~~json
{
  "source": "00a6ce74",
  "target": "00a6cdd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ce78`](#insn-00a6ce78)

~~~json
{
  "source": "00a6ce78",
  "target": "00a6cdd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6cf48`](#insn-00a6cf48)

~~~json
{
  "source": "00a6cf48",
  "target": "00c57fb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
