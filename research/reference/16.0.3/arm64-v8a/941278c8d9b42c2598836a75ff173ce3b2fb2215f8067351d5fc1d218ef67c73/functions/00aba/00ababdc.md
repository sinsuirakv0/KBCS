# 00ababdc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00ab9be8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ab9/00ab9be8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0066.md#compare-8305ede60599410b29d6d37fd8f14d08)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ababdc",
  "name": "_INIT_240",
  "size": 708,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "83dbf8178a866e5a9d74912d95a74a4f016fe93468ac33ab6cd0bc2d7b6f5815",
  "source_text_sha256": "83dbf8178a866e5a9d74912d95a74a4f016fe93468ac33ab6cd0bc2d7b6f5815",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ababdc",
        "00abae9b"
      ],
      [
        "00abaf68",
        "00abaf6b"
      ]
    ],
    "bytes_sha256": "32d72502280c14f2f01919a7aed6ef267855af392bfc42a781c14dae35de26bf",
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

## 疑似コード / UTF-8 6650 bytes

~~~c

/* WARNING: Type propagation algorithm not settling */

void _INIT_240(void)

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
  
                    /* try { // try from 00ababec to 00bbabf7 has its CatchHandler @ 00abad7c */
  lVar1 = tpidr_el0;
  local_38 = *(long *)(lVar1 + 0x28);
                    /* try { // try from 00abac00 to 00bbac67 has its CatchHandler @ 00abada0 */
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
                    /* try { // try from 00abac74 to 00bbaca7 has its CatchHandler @ 00abad70 */
  local_cf = (char  [8])s_CgkIjM3y_ZQaEAIQBg_002b8e3d._0_8_;
  uStack_9f = 0x7741;
  local_98[0] = 4;
  uStack_a7 = (undefined7)s_CgkIjM3y_ZQaEAIQAw_002a2fe0._8_8_;
  cStack_a0 = SUB81(s_CgkIjM3y_ZQaEAIQAw_002a2fe0._8_8_,7);
  local_af = (char  [8])s_CgkIjM3y_ZQaEAIQAw_002a2fe0._0_8_;
  uStack_7f = 0x5142;
  local_78[0] = 5;
  uStack_87 = (undefined7)s_CgkIjM3y_ZQaEAIQBQ_002ac643._8_8_;
  cStack_80 = SUB81(s_CgkIjM3y_ZQaEAIQBQ_002ac643._8_8_,7);
                    /* try { // try from 00abacac to 00bbacfb has its CatchHandler @ 00abadc4 */
  local_8f = (char  [8])s_CgkIjM3y_ZQaEAIQBQ_002ac643._0_8_;
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
                    /* try { // try from 00abacfc to 00bbadff has its CatchHandler @ 00aba740 */
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
  DAT_01125d18 = 0;
  DAT_01125d10 = 0;
  DAT_01125d08 = &DAT_01125d10;
  FUN_0043bb58(&DAT_01125d08,&DAT_01125d10,local_118,local_118);
  FUN_0043bb58(&DAT_01125d08,&DAT_01125d10,local_f8,local_f8);
  FUN_0043bb58(&DAT_01125d08,&DAT_01125d10,local_d8,local_d8);
                    /* catch() { ... } // from try @ 00abac74 with catch @ 00abad70 */
                    /* catch() { ... } // from try @ 00aba7d4 with catch @ 00abad74 */
  FUN_0043bb58(&DAT_01125d08,&DAT_01125d10,local_b8,local_b8);
                    /* catch() { ... } // from try @ 00ababec with catch @ 00abad7c */
                    /* catch() { ... } // from try @ 00abab34 with catch @ 00abad80 */
                    /* catch() { ... } // from try @ 00aba8a4 with catch @ 00abad84 */
                    /* catch() { ... } // from try @ 00aba88c with catch @ 00abad88 */
                    /* catch() { ... } // from try @ 00aba844 with catch @ 00abad8c */
  FUN_0043bb58(&DAT_01125d08,&DAT_01125d10,local_98,local_98);
                    /* catch() { ... } // from try @ 00aba824 with catch @ 00abad90 */
                    /* catch() { ... } // from try @ 00aba7fc with catch @ 00abad94 */
                    /* catch() { ... } // from try @ 00aba7a4 with catch @ 00abad98 */
                    /* catch() { ... } // from try @ 00abac00 with catch @ 00abada0 */
  FUN_0043bb58(&DAT_01125d08,&DAT_01125d10,local_78,local_78);
                    /* catch() { ... } // from try @ 00abaaac with catch @ 00abada4 */
                    /* catch() { ... } // from try @ 00aba9cc with catch @ 00abada8 */
                    /* catch() { ... } // from try @ 00aba8ac with catch @ 00abadac */
  FUN_0043bb58(&DAT_01125d08,&DAT_01125d10,local_58,local_58);
                    /* catch() { ... } // from try @ 00abaa10 with catch @ 00abadbc */
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
  __cxa_atexit(FUN_0043b1d0,&DAT_01125d08,&PTR_LOOP_00c64030);
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
<a id="insn-00ababdc"></a> `00ababdc` | `ff 83 04 d1` | sub sp,sp,#0x120 | `FALL_THROUGH`
<a id="insn-00ababe0"></a> `00ababe0` | `fd 7b 0f a9` | stp x29,x30,[sp, #0xf0] | `FALL_THROUGH`
<a id="insn-00ababe4"></a> `00ababe4` | `fc 57 10 a9` | stp x28,x21,[sp, #0x100] | `FALL_THROUGH`
<a id="insn-00ababe8"></a> `00ababe8` | `f4 4f 11 a9` | stp x20,x19,[sp, #0x110] | `FALL_THROUGH`
<a id="insn-00ababec"></a> `00ababec` | `fd c3 03 91` | add x29,sp,#0xf0 | `FALL_THROUGH`
<a id="insn-00ababf0"></a> `00ababf0` | `55 d0 3b d5` | mrs x21,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00ababf4"></a> `00ababf4` | `2a e8 8c 52` | mov w10,#0x6741 | `FALL_THROUGH`
<a id="insn-00ababf8"></a> `00ababf8` | `f4 23 00 91` | add x20,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00ababfc"></a> `00ababfc` | `a9 16 40 f9` | ldr x9,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00abac00"></a> `00abac00` | `88 04 80 52` | mov w8,#0x24 | `FALL_THROUGH`
<a id="insn-00abac04"></a> `00abac04` | `53 33 00 f0` | adrp x19,0x1125000 | `FALL_THROUGH`
<a id="insn-00abac08"></a> `00abac08` | `73 22 34 91` | add x19,x19,#0xd08 | `FALL_THROUGH`
<a id="insn-00abac0c"></a> `00abac0c` | `a9 83 1f f8` | stur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00abac10"></a> `00abac10` | `e9 bf ff d0` | adrp x9,0x2b8000 | `FALL_THROUGH`
<a id="insn-00abac14"></a> `00abac14` | `29 d5 00 91` | add x9,x9,#0x35 | `FALL_THROUGH`
<a id="insn-00abac18"></a> `00abac18` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00abac1c"></a> `00abac1c` | `29 00 80 52` | mov w9,#0x1 | `FALL_THROUGH`
<a id="insn-00abac20"></a> `00abac20` | `ea 13 02 78` | sturh w10,[sp, #0x21] | `FALL_THROUGH`
<a id="insn-00abac24"></a> `00abac24` | `e9 2b 00 b9` | str w9,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00abac28"></a> `00abac28` | `49 28 88 52` | mov w9,#0x4142 | `FALL_THROUGH`
<a id="insn-00abac2c"></a> `00abac2c` | `ea bf ff d0` | adrp x10,0x2b8000 | `FALL_THROUGH`
<a id="insn-00abac30"></a> `00abac30` | `4a 21 01 91` | add x10,x10,#0x48 | `FALL_THROUGH`
<a id="insn-00abac34"></a> `00abac34` | `e0 13 81 3c` | stur q0,[sp, #0x11] | `FALL_THROUGH`
<a id="insn-00abac38"></a> `00abac38` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00abac3c"></a> `00abac3c` | `40 01 c0 3d` | ldr q0,[x10] | `FALL_THROUGH`
<a id="insn-00abac40"></a> `00abac40` | `e9 13 04 78` | sturh w9,[sp, #0x41] | `FALL_THROUGH`
<a id="insn-00abac44"></a> `00abac44` | `49 00 80 52` | mov w9,#0x2 | `FALL_THROUGH`
<a id="insn-00abac48"></a> `00abac48` | `e9 4b 00 b9` | str w9,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00abac4c"></a> `00abac4c` | `49 e8 8c 52` | mov w9,#0x6742 | `FALL_THROUGH`
<a id="insn-00abac50"></a> `00abac50` | `ea bf ff d0` | adrp x10,0x2b8000 | `FALL_THROUGH`
<a id="insn-00abac54"></a> `00abac54` | `4a f5 38 91` | add x10,x10,#0xe3d | `FALL_THROUGH`
<a id="insn-00abac58"></a> `00abac58` | `e0 13 83 3c` | stur q0,[sp, #0x31] | `FALL_THROUGH`
<a id="insn-00abac5c"></a> `00abac5c` | `40 01 c0 3d` | ldr q0,[x10] | `FALL_THROUGH`
<a id="insn-00abac60"></a> `00abac60` | `e9 13 06 78` | sturh w9,[sp, #0x61] | `FALL_THROUGH`
<a id="insn-00abac64"></a> `00abac64` | `69 00 80 52` | mov w9,#0x3 | `FALL_THROUGH`
<a id="insn-00abac68"></a> `00abac68` | `e9 6b 00 b9` | str w9,[sp, #0x68] | `FALL_THROUGH`
<a id="insn-00abac6c"></a> `00abac6c` | `29 e8 8e 52` | mov w9,#0x7741 | `FALL_THROUGH`
<a id="insn-00abac70"></a> `00abac70` | `4a bf ff 90` | adrp x10,0x2a2000 | `FALL_THROUGH`
<a id="insn-00abac74"></a> `00abac74` | `4a 81 3f 91` | add x10,x10,#0xfe0 | `FALL_THROUGH`
<a id="insn-00abac78"></a> `00abac78` | `e0 13 85 3c` | stur q0,[sp, #0x51] | `FALL_THROUGH`
<a id="insn-00abac7c"></a> `00abac7c` | `40 01 c0 3d` | ldr q0,[x10] | `FALL_THROUGH`
<a id="insn-00abac80"></a> `00abac80` | `e9 13 08 78` | sturh w9,[sp, #0x81] | `FALL_THROUGH`
<a id="insn-00abac84"></a> `00abac84` | `89 00 80 52` | mov w9,#0x4 | `FALL_THROUGH`
<a id="insn-00abac88"></a> `00abac88` | `e9 8b 00 b9` | str w9,[sp, #0x88] | `FALL_THROUGH`
<a id="insn-00abac8c"></a> `00abac8c` | `89 bf ff d0` | adrp x9,0x2ac000 | `FALL_THROUGH`
<a id="insn-00abac90"></a> `00abac90` | `29 0d 19 91` | add x9,x9,#0x643 | `FALL_THROUGH`
<a id="insn-00abac94"></a> `00abac94` | `e0 13 87 3c` | stur q0,[sp, #0x71] | `FALL_THROUGH`
<a id="insn-00abac98"></a> `00abac98` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00abac9c"></a> `00abac9c` | `49 28 8a 52` | mov w9,#0x5142 | `FALL_THROUGH`
<a id="insn-00abaca0"></a> `00abaca0` | `89 92 09 78` | sturh w9,[x20, #0x99] | `FALL_THROUGH`
<a id="insn-00abaca4"></a> `00abaca4` | `a9 00 80 52` | mov w9,#0x5 | `FALL_THROUGH`
<a id="insn-00abaca8"></a> `00abaca8` | `e9 ab 00 b9` | str w9,[sp, #0xa8] | `FALL_THROUGH`
<a id="insn-00abacac"></a> `00abacac` | `29 bf ff d0` | adrp x9,0x2a0000 | `FALL_THROUGH`
<a id="insn-00abacb0"></a> `00abacb0` | `29 41 3d 91` | add x9,x9,#0xf50 | `FALL_THROUGH`
<a id="insn-00abacb4"></a> `00abacb4` | `80 92 88 3c` | stur q0,[x20, #0x89] | `FALL_THROUGH`
<a id="insn-00abacb8"></a> `00abacb8` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00abacbc"></a> `00abacbc` | `49 e8 8e 52` | mov w9,#0x7742 | `FALL_THROUGH`
<a id="insn-00abacc0"></a> `00abacc0` | `89 92 0b 78` | sturh w9,[x20, #0xb9] | `FALL_THROUGH`
<a id="insn-00abacc4"></a> `00abacc4` | `c9 00 80 52` | mov w9,#0x6 | `FALL_THROUGH`
<a id="insn-00abacc8"></a> `00abacc8` | `e9 cb 00 b9` | str w9,[sp, #0xc8] | `FALL_THROUGH`
<a id="insn-00abaccc"></a> `00abaccc` | `49 bf ff b0` | adrp x9,0x2a3000 | `FALL_THROUGH`
<a id="insn-00abacd0"></a> `00abacd0` | `29 1d 3e 91` | add x9,x9,#0xf87 | `FALL_THROUGH`
<a id="insn-00abacd4"></a> `00abacd4` | `80 92 8a 3c` | stur q0,[x20, #0xa9] | `FALL_THROUGH`
<a id="insn-00abacd8"></a> `00abacd8` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00abacdc"></a> `00abacdc` | `e8 43 00 39` | strb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00abace0"></a> `00abace0` | `e8 c3 00 39` | strb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00abace4"></a> `00abace4` | `e8 43 01 39` | strb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00abace8"></a> `00abace8` | `e8 c3 01 39` | strb w8,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00abacec"></a> `00abacec` | `e8 43 02 39` | strb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00abacf0"></a> `00abacf0` | `e8 c3 02 39` | strb w8,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00abacf4"></a> `00abacf4` | `e8 43 03 39` | strb w8,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-00abacf8"></a> `00abacf8` | `68 28 88 52` | mov w8,#0x4143 | `FALL_THROUGH`
<a id="insn-00abacfc"></a> `00abacfc` | `ff 0b 00 b9` | str wzr,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00abad00"></a> `00abad00` | `ff 8f 00 39` | strb wzr,[sp, #0x23] | `FALL_THROUGH`
<a id="insn-00abad04"></a> `00abad04` | `ff 0f 01 39` | strb wzr,[sp, #0x43] | `FALL_THROUGH`
<a id="insn-00abad08"></a> `00abad08` | `ff 8f 01 39` | strb wzr,[sp, #0x63] | `FALL_THROUGH`
<a id="insn-00abad0c"></a> `00abad0c` | `ff 0f 02 39` | strb wzr,[sp, #0x83] | `FALL_THROUGH`
<a id="insn-00abad10"></a> `00abad10` | `ff 8f 02 39` | strb wzr,[sp, #0xa3] | `FALL_THROUGH`
<a id="insn-00abad14"></a> `00abad14` | `ff 0f 03 39` | strb wzr,[sp, #0xc3] | `FALL_THROUGH`
<a id="insn-00abad18"></a> `00abad18` | `88 92 0d 78` | sturh w8,[x20, #0xd9] | `FALL_THROUGH`
<a id="insn-00abad1c"></a> `00abad1c` | `80 92 8c 3c` | stur q0,[x20, #0xc9] | `FALL_THROUGH`
<a id="insn-00abad20"></a> `00abad20` | `ff 8f 03 39` | strb wzr,[sp, #0xe3] | `FALL_THROUGH`
<a id="insn-00abad24"></a> `00abad24` | `7f 0a 00 f9` | str xzr,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00abad28"></a> `00abad28` | `3f 8c 00 f8` | str xzr,[x1, #0x8]! | `FALL_THROUGH`
<a id="insn-00abad2c"></a> `00abad2c` | `61 02 00 f9` | str x1,[x19] | `FALL_THROUGH`
<a id="insn-00abad30"></a> `00abad30` | `e2 23 00 91` | add x2,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00abad34"></a> `00abad34` | `e3 23 00 91` | add x3,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00abad38"></a> `00abad38` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00abad3c"></a> `00abad3c` | `87 03 e6 97` | bl 0x0043bb58 | `UNCONDITIONAL_CALL`
<a id="insn-00abad40"></a> `00abad40` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00abad44"></a> `00abad44` | `82 82 00 91` | add x2,x20,#0x20 | `FALL_THROUGH`
<a id="insn-00abad48"></a> `00abad48` | `83 82 00 91` | add x3,x20,#0x20 | `FALL_THROUGH`
<a id="insn-00abad4c"></a> `00abad4c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00abad50"></a> `00abad50` | `82 03 e6 97` | bl 0x0043bb58 | `UNCONDITIONAL_CALL`
<a id="insn-00abad54"></a> `00abad54` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00abad58"></a> `00abad58` | `82 02 01 91` | add x2,x20,#0x40 | `FALL_THROUGH`
<a id="insn-00abad5c"></a> `00abad5c` | `83 02 01 91` | add x3,x20,#0x40 | `FALL_THROUGH`
<a id="insn-00abad60"></a> `00abad60` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00abad64"></a> `00abad64` | `7d 03 e6 97` | bl 0x0043bb58 | `UNCONDITIONAL_CALL`
<a id="insn-00abad68"></a> `00abad68` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00abad6c"></a> `00abad6c` | `82 82 01 91` | add x2,x20,#0x60 | `FALL_THROUGH`
<a id="insn-00abad70"></a> `00abad70` | `83 82 01 91` | add x3,x20,#0x60 | `FALL_THROUGH`
<a id="insn-00abad74"></a> `00abad74` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00abad78"></a> `00abad78` | `78 03 e6 97` | bl 0x0043bb58 | `UNCONDITIONAL_CALL`
<a id="insn-00abad7c"></a> `00abad7c` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00abad80"></a> `00abad80` | `82 02 02 91` | add x2,x20,#0x80 | `FALL_THROUGH`
<a id="insn-00abad84"></a> `00abad84` | `83 02 02 91` | add x3,x20,#0x80 | `FALL_THROUGH`
<a id="insn-00abad88"></a> `00abad88` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00abad8c"></a> `00abad8c` | `73 03 e6 97` | bl 0x0043bb58 | `UNCONDITIONAL_CALL`
<a id="insn-00abad90"></a> `00abad90` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00abad94"></a> `00abad94` | `82 82 02 91` | add x2,x20,#0xa0 | `FALL_THROUGH`
<a id="insn-00abad98"></a> `00abad98` | `83 82 02 91` | add x3,x20,#0xa0 | `FALL_THROUGH`
<a id="insn-00abad9c"></a> `00abad9c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00abada0"></a> `00abada0` | `6e 03 e6 97` | bl 0x0043bb58 | `UNCONDITIONAL_CALL`
<a id="insn-00abada4"></a> `00abada4` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00abada8"></a> `00abada8` | `82 02 03 91` | add x2,x20,#0xc0 | `FALL_THROUGH`
<a id="insn-00abadac"></a> `00abadac` | `83 02 03 91` | add x3,x20,#0xc0 | `FALL_THROUGH`
<a id="insn-00abadb0"></a> `00abadb0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00abadb4"></a> `00abadb4` | `69 03 e6 97` | bl 0x0043bb58 | `UNCONDITIONAL_CALL`
<a id="insn-00abadb8"></a> `00abadb8` | `e8 43 43 39` | ldrb w8,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-00abadbc"></a> `00abadbc` | `e8 03 00 37` | tbnz w8,#0x0,0x00abae38 | `CONDITIONAL_JUMP`
<a id="insn-00abadc0"></a> `00abadc0` | `e8 c3 42 39` | ldrb w8,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00abadc4"></a> `00abadc4` | `28 04 00 37` | tbnz w8,#0x0,0x00abae48 | `CONDITIONAL_JUMP`
<a id="insn-00abadc8"></a> `00abadc8` | `e8 43 42 39` | ldrb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00abadcc"></a> `00abadcc` | `68 04 00 37` | tbnz w8,#0x0,0x00abae58 | `CONDITIONAL_JUMP`
<a id="insn-00abadd0"></a> `00abadd0` | `e8 c3 41 39` | ldrb w8,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00abadd4"></a> `00abadd4` | `a8 04 00 37` | tbnz w8,#0x0,0x00abae68 | `CONDITIONAL_JUMP`
<a id="insn-00abadd8"></a> `00abadd8` | `e8 43 41 39` | ldrb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00abaddc"></a> `00abaddc` | `e8 04 00 37` | tbnz w8,#0x0,0x00abae78 | `CONDITIONAL_JUMP`
<a id="insn-00abade0"></a> `00abade0` | `e8 c3 40 39` | ldrb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00abade4"></a> `00abade4` | `28 05 00 37` | tbnz w8,#0x0,0x00abae88 | `CONDITIONAL_JUMP`
<a id="insn-00abade8"></a> `00abade8` | `e8 43 40 39` | ldrb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00abadec"></a> `00abadec` | `68 00 00 36` | tbz w8,#0x0,0x00abadf8 | `CONDITIONAL_JUMP`
<a id="insn-00abadf0"></a> `00abadf0` | `e0 13 40 f9` | ldr x0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00abadf4"></a> `00abadf4` | `57 78 06 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00abadf8"></a> `00abadf8` | `00 cc ff b0` | adrp x0,0x43b000 | `FALL_THROUGH`
<a id="insn-00abadfc"></a> `00abadfc` | `00 40 07 91` | add x0,x0,#0x1d0 | `FALL_THROUGH`
<a id="insn-00abae00"></a> `00abae00` | `41 33 00 f0` | adrp x1,0x1125000 | `FALL_THROUGH`
<a id="insn-00abae04"></a> `00abae04` | `21 20 34 91` | add x1,x1,#0xd08 | `FALL_THROUGH`
<a id="insn-00abae08"></a> `00abae08` | `42 0d 00 d0` | adrp x2,0xc64000 | `FALL_THROUGH`
<a id="insn-00abae0c"></a> `00abae0c` | `42 c0 00 91` | add x2,x2,#0x30 | `FALL_THROUGH`
<a id="insn-00abae10"></a> `00abae10` | `30 78 06 94` | bl 0x00c58ed0 | `UNCONDITIONAL_CALL`
<a id="insn-00abae14"></a> `00abae14` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00abae18"></a> `00abae18` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00abae1c"></a> `00abae1c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00abae20"></a> `00abae20` | `41 0a 00 54` | b.ne 0x00abaf68 | `CONDITIONAL_JUMP`
<a id="insn-00abae24"></a> `00abae24` | `f4 4f 51 a9` | ldp x20,x19,[sp, #0x110] | `FALL_THROUGH`
<a id="insn-00abae28"></a> `00abae28` | `fc 57 50 a9` | ldp x28,x21,[sp, #0x100] | `FALL_THROUGH`
<a id="insn-00abae2c"></a> `00abae2c` | `fd 7b 4f a9` | ldp x29,x30,[sp, #0xf0] | `FALL_THROUGH`
<a id="insn-00abae30"></a> `00abae30` | `ff 83 04 91` | add sp,sp,#0x120 | `FALL_THROUGH`
<a id="insn-00abae34"></a> `00abae34` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00abae38"></a> `00abae38` | `e0 73 40 f9` | ldr x0,[sp, #0xe0] | `FALL_THROUGH`
<a id="insn-00abae3c"></a> `00abae3c` | `45 78 06 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00abae40"></a> `00abae40` | `e8 c3 42 39` | ldrb w8,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00abae44"></a> `00abae44` | `28 fc 07 36` | tbz w8,#0x0,0x00abadc8 | `CONDITIONAL_JUMP`
<a id="insn-00abae48"></a> `00abae48` | `e0 63 40 f9` | ldr x0,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00abae4c"></a> `00abae4c` | `41 78 06 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00abae50"></a> `00abae50` | `e8 43 42 39` | ldrb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00abae54"></a> `00abae54` | `e8 fb 07 36` | tbz w8,#0x0,0x00abadd0 | `CONDITIONAL_JUMP`
<a id="insn-00abae58"></a> `00abae58` | `e0 53 40 f9` | ldr x0,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00abae5c"></a> `00abae5c` | `3d 78 06 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00abae60"></a> `00abae60` | `e8 c3 41 39` | ldrb w8,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00abae64"></a> `00abae64` | `a8 fb 07 36` | tbz w8,#0x0,0x00abadd8 | `CONDITIONAL_JUMP`
<a id="insn-00abae68"></a> `00abae68` | `e0 43 40 f9` | ldr x0,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00abae6c"></a> `00abae6c` | `39 78 06 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00abae70"></a> `00abae70` | `e8 43 41 39` | ldrb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00abae74"></a> `00abae74` | `68 fb 07 36` | tbz w8,#0x0,0x00abade0 | `CONDITIONAL_JUMP`
<a id="insn-00abae78"></a> `00abae78` | `e0 33 40 f9` | ldr x0,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00abae7c"></a> `00abae7c` | `35 78 06 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00abae80"></a> `00abae80` | `e8 c3 40 39` | ldrb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00abae84"></a> `00abae84` | `28 fb 07 36` | tbz w8,#0x0,0x00abade8 | `CONDITIONAL_JUMP`
<a id="insn-00abae88"></a> `00abae88` | `e0 23 40 f9` | ldr x0,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00abae8c"></a> `00abae8c` | `31 78 06 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00abae90"></a> `00abae90` | `e8 43 40 39` | ldrb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00abae94"></a> `00abae94` | `e8 fa 07 37` | tbnz w8,#0x0,0x00abadf0 | `CONDITIONAL_JUMP`
<a id="insn-00abae98"></a> `00abae98` | `d8 ff ff 17` | b 0x00abadf8 | `UNCONDITIONAL_JUMP`
<a id="insn-00abaf68"></a> `00abaf68` | `06 78 06 94` | bl 0x00c58f80 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00ababdc`](#insn-00ababdc) 範囲 `[['00ababdc', '00ababeb']]`
  - `FALL_THROUGH` [`00ababe8`](#insn-00ababe8) → [`00ababec`](#insn-00ababec)
- ブロック [`00ababec`](#insn-00ababec) 範囲 `[['00ababec', '00ababff']]`
  - `FALL_THROUGH` [`00ababfc`](#insn-00ababfc) → [`00abac00`](#insn-00abac00)
- ブロック [`00abac00`](#insn-00abac00) 範囲 `[['00abac00', '00abac73']]`
  - `FALL_THROUGH` [`00abac70`](#insn-00abac70) → [`00abac74`](#insn-00abac74)
- ブロック [`00abac74`](#insn-00abac74) 範囲 `[['00abac74', '00abacab']]`
  - `FALL_THROUGH` [`00abaca8`](#insn-00abaca8) → [`00abacac`](#insn-00abacac)
- ブロック [`00abacac`](#insn-00abacac) 範囲 `[['00abacac', '00abacfb']]`
  - `FALL_THROUGH` [`00abacf8`](#insn-00abacf8) → [`00abacfc`](#insn-00abacfc)
- ブロック [`00abacfc`](#insn-00abacfc) 範囲 `[['00abacfc', '00abad6f']]`
  - `FALL_THROUGH` [`00abad6c`](#insn-00abad6c) → [`00abad70`](#insn-00abad70)
- ブロック [`00abad70`](#insn-00abad70) 範囲 `[['00abad70', '00abad73']]`
  - `FALL_THROUGH` [`00abad70`](#insn-00abad70) → [`00abad74`](#insn-00abad74)
- ブロック [`00abad74`](#insn-00abad74) 範囲 `[['00abad74', '00abad7b']]`
  - `FALL_THROUGH` [`00abad78`](#insn-00abad78) → [`00abad7c`](#insn-00abad7c)
- ブロック [`00abad7c`](#insn-00abad7c) 範囲 `[['00abad7c', '00abad7f']]`
  - `FALL_THROUGH` [`00abad7c`](#insn-00abad7c) → [`00abad80`](#insn-00abad80)
- ブロック [`00abad80`](#insn-00abad80) 範囲 `[['00abad80', '00abad83']]`
  - `FALL_THROUGH` [`00abad80`](#insn-00abad80) → [`00abad84`](#insn-00abad84)
- ブロック [`00abad84`](#insn-00abad84) 範囲 `[['00abad84', '00abad87']]`
  - `FALL_THROUGH` [`00abad84`](#insn-00abad84) → [`00abad88`](#insn-00abad88)
- ブロック [`00abad88`](#insn-00abad88) 範囲 `[['00abad88', '00abad8b']]`
  - `FALL_THROUGH` [`00abad88`](#insn-00abad88) → [`00abad8c`](#insn-00abad8c)
- ブロック [`00abad8c`](#insn-00abad8c) 範囲 `[['00abad8c', '00abad8f']]`
  - `FALL_THROUGH` [`00abad8c`](#insn-00abad8c) → [`00abad90`](#insn-00abad90)
- ブロック [`00abad90`](#insn-00abad90) 範囲 `[['00abad90', '00abad93']]`
  - `FALL_THROUGH` [`00abad90`](#insn-00abad90) → [`00abad94`](#insn-00abad94)
- ブロック [`00abad94`](#insn-00abad94) 範囲 `[['00abad94', '00abad97']]`
  - `FALL_THROUGH` [`00abad94`](#insn-00abad94) → [`00abad98`](#insn-00abad98)
- ブロック [`00abad98`](#insn-00abad98) 範囲 `[['00abad98', '00abad9f']]`
  - `FALL_THROUGH` [`00abad9c`](#insn-00abad9c) → [`00abada0`](#insn-00abada0)
- ブロック [`00abada0`](#insn-00abada0) 範囲 `[['00abada0', '00abada3']]`
  - `FALL_THROUGH` [`00abada0`](#insn-00abada0) → [`00abada4`](#insn-00abada4)
- ブロック [`00abada4`](#insn-00abada4) 範囲 `[['00abada4', '00abada7']]`
  - `FALL_THROUGH` [`00abada4`](#insn-00abada4) → [`00abada8`](#insn-00abada8)
- ブロック [`00abada8`](#insn-00abada8) 範囲 `[['00abada8', '00abadab']]`
  - `FALL_THROUGH` [`00abada8`](#insn-00abada8) → [`00abadac`](#insn-00abadac)
- ブロック [`00abadac`](#insn-00abadac) 範囲 `[['00abadac', '00abadbb']]`
  - `FALL_THROUGH` [`00abadb8`](#insn-00abadb8) → [`00abadbc`](#insn-00abadbc)
- ブロック [`00abadbc`](#insn-00abadbc) 範囲 `[['00abadbc', '00abadbf']]`
  - `CONDITIONAL_JUMP` [`00abadbc`](#insn-00abadbc) → [`00abae38`](#insn-00abae38)
  - `FALL_THROUGH` [`00abadbc`](#insn-00abadbc) → [`00abadc0`](#insn-00abadc0)
- ブロック [`00abadc0`](#insn-00abadc0) 範囲 `[['00abadc0', '00abadc3']]`
  - `FALL_THROUGH` [`00abadc0`](#insn-00abadc0) → [`00abadc4`](#insn-00abadc4)
- ブロック [`00abadc4`](#insn-00abadc4) 範囲 `[['00abadc4', '00abadc7']]`
  - `CONDITIONAL_JUMP` [`00abadc4`](#insn-00abadc4) → [`00abae48`](#insn-00abae48)
  - `FALL_THROUGH` [`00abadc4`](#insn-00abadc4) → [`00abadc8`](#insn-00abadc8)
- ブロック [`00abadc8`](#insn-00abadc8) 範囲 `[['00abadc8', '00abadcf']]`
  - `CONDITIONAL_JUMP` [`00abadcc`](#insn-00abadcc) → [`00abae58`](#insn-00abae58)
  - `FALL_THROUGH` [`00abadcc`](#insn-00abadcc) → [`00abadd0`](#insn-00abadd0)
- ブロック [`00abadd0`](#insn-00abadd0) 範囲 `[['00abadd0', '00abadd7']]`
  - `CONDITIONAL_JUMP` [`00abadd4`](#insn-00abadd4) → [`00abae68`](#insn-00abae68)
  - `FALL_THROUGH` [`00abadd4`](#insn-00abadd4) → [`00abadd8`](#insn-00abadd8)
- ブロック [`00abadd8`](#insn-00abadd8) 範囲 `[['00abadd8', '00abaddf']]`
  - `CONDITIONAL_JUMP` [`00abaddc`](#insn-00abaddc) → [`00abae78`](#insn-00abae78)
  - `FALL_THROUGH` [`00abaddc`](#insn-00abaddc) → [`00abade0`](#insn-00abade0)
- ブロック [`00abade0`](#insn-00abade0) 範囲 `[['00abade0', '00abade7']]`
  - `CONDITIONAL_JUMP` [`00abade4`](#insn-00abade4) → [`00abae88`](#insn-00abae88)
  - `FALL_THROUGH` [`00abade4`](#insn-00abade4) → [`00abade8`](#insn-00abade8)
- ブロック [`00abade8`](#insn-00abade8) 範囲 `[['00abade8', '00abadef']]`
  - `CONDITIONAL_JUMP` [`00abadec`](#insn-00abadec) → [`00abadf8`](#insn-00abadf8)
  - `FALL_THROUGH` [`00abadec`](#insn-00abadec) → [`00abadf0`](#insn-00abadf0)
- ブロック [`00abadf0`](#insn-00abadf0) 範囲 `[['00abadf0', '00abadf7']]`
  - `FALL_THROUGH` [`00abadf4`](#insn-00abadf4) → [`00abadf8`](#insn-00abadf8)
- ブロック [`00abadf8`](#insn-00abadf8) 範囲 `[['00abadf8', '00abae23']]`
  - `CONDITIONAL_JUMP` [`00abae20`](#insn-00abae20) → [`00abaf68`](#insn-00abaf68)
  - `FALL_THROUGH` [`00abae20`](#insn-00abae20) → [`00abae24`](#insn-00abae24)
- ブロック [`00abae24`](#insn-00abae24) 範囲 `[['00abae24', '00abae37']]`
- ブロック [`00abae38`](#insn-00abae38) 範囲 `[['00abae38', '00abae47']]`
  - `CONDITIONAL_JUMP` [`00abae44`](#insn-00abae44) → [`00abadc8`](#insn-00abadc8)
  - `FALL_THROUGH` [`00abae44`](#insn-00abae44) → [`00abae48`](#insn-00abae48)
- ブロック [`00abae48`](#insn-00abae48) 範囲 `[['00abae48', '00abae57']]`
  - `CONDITIONAL_JUMP` [`00abae54`](#insn-00abae54) → [`00abadd0`](#insn-00abadd0)
  - `FALL_THROUGH` [`00abae54`](#insn-00abae54) → [`00abae58`](#insn-00abae58)
- ブロック [`00abae58`](#insn-00abae58) 範囲 `[['00abae58', '00abae67']]`
  - `CONDITIONAL_JUMP` [`00abae64`](#insn-00abae64) → [`00abadd8`](#insn-00abadd8)
  - `FALL_THROUGH` [`00abae64`](#insn-00abae64) → [`00abae68`](#insn-00abae68)
- ブロック [`00abae68`](#insn-00abae68) 範囲 `[['00abae68', '00abae77']]`
  - `CONDITIONAL_JUMP` [`00abae74`](#insn-00abae74) → [`00abade0`](#insn-00abade0)
  - `FALL_THROUGH` [`00abae74`](#insn-00abae74) → [`00abae78`](#insn-00abae78)
- ブロック [`00abae78`](#insn-00abae78) 範囲 `[['00abae78', '00abae87']]`
  - `CONDITIONAL_JUMP` [`00abae84`](#insn-00abae84) → [`00abade8`](#insn-00abade8)
  - `FALL_THROUGH` [`00abae84`](#insn-00abae84) → [`00abae88`](#insn-00abae88)
- ブロック [`00abae88`](#insn-00abae88) 範囲 `[['00abae88', '00abae97']]`
  - `CONDITIONAL_JUMP` [`00abae94`](#insn-00abae94) → [`00abadf0`](#insn-00abadf0)
  - `FALL_THROUGH` [`00abae94`](#insn-00abae94) → [`00abae98`](#insn-00abae98)
- ブロック [`00abae98`](#insn-00abae98) 範囲 `[['00abae98', '00abae9b']]`
  - `UNCONDITIONAL_JUMP` [`00abae98`](#insn-00abae98) → [`00abadf8`](#insn-00abadf8)
- ブロック [`00abaf68`](#insn-00abaf68) 範囲 `[['00abaf68', '00abaf6b']]`

## 命令位置別の参照

- [`00ababe0`](#insn-00ababe0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ababe4`](#insn-00ababe4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ababe8`](#insn-00ababe8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abac0c`](#insn-00abac0c) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abac18`](#insn-00abac18) → `002b8035`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00abac20`](#insn-00abac20) → `Stack[-0xff]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abac24`](#insn-00abac24) → `Stack[-0xf8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abac34`](#insn-00abac34) → `Stack[-0x10f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abac3c`](#insn-00abac3c) → `002b8048`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00abac40`](#insn-00abac40) → `Stack[-0xdf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abac48`](#insn-00abac48) → `Stack[-0xd8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abac58`](#insn-00abac58) → `Stack[-0xef]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abac5c`](#insn-00abac5c) → `002b8e3d`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00abac60`](#insn-00abac60) → `Stack[-0xbf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abac68`](#insn-00abac68) → `Stack[-0xb8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abac78`](#insn-00abac78) → `Stack[-0xcf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abac7c`](#insn-00abac7c) → `002a2fe0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00abac80`](#insn-00abac80) → `Stack[-0x9f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abac88`](#insn-00abac88) → `Stack[-0x98]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abac94`](#insn-00abac94) → `Stack[-0xaf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abac98`](#insn-00abac98) → `002ac643`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00abaca0`](#insn-00abaca0) → `Stack[-0x7f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abaca8`](#insn-00abaca8) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abacb4`](#insn-00abacb4) → `Stack[-0x8f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abacb8`](#insn-00abacb8) → `002a0f50`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00abacc0`](#insn-00abacc0) → `Stack[-0x5f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abacc8`](#insn-00abacc8) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abacd4`](#insn-00abacd4) → `Stack[-0x6f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abacd8`](#insn-00abacd8) → `002a3f87`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00abacdc`](#insn-00abacdc) → `Stack[-0x110]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abace0`](#insn-00abace0) → `Stack[-0xf0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abace4`](#insn-00abace4) → `Stack[-0xd0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abace8`](#insn-00abace8) → `Stack[-0xb0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abacec`](#insn-00abacec) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abacf0`](#insn-00abacf0) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abacf4`](#insn-00abacf4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abacfc`](#insn-00abacfc) → `Stack[-0x118]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abad00`](#insn-00abad00) → `Stack[-0xfd]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abad04`](#insn-00abad04) → `Stack[-0xdd]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abad08`](#insn-00abad08) → `Stack[-0xbd]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abad0c`](#insn-00abad0c) → `Stack[-0x9d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abad10`](#insn-00abad10) → `Stack[-0x7d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abad14`](#insn-00abad14) → `Stack[-0x5d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abad18`](#insn-00abad18) → `Stack[-0x3f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abad1c`](#insn-00abad1c) → `Stack[-0x4f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abad20`](#insn-00abad20) → `Stack[-0x3d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abad24`](#insn-00abad24) → `01125d18`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abad28`](#insn-00abad28) → `01125d10`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abad2c`](#insn-00abad2c) → `01125d08`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abad2c`](#insn-00abad2c) → `01125d10`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abad38`](#insn-00abad38) → `01125d08`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abad3c`](#insn-00abad3c) → [`0043bb58`](../0043b/0043bb58.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bb58` · 推定シンボル `None` · 推定型 `None`
- [`00abad40`](#insn-00abad40) → `01125d10`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abad4c`](#insn-00abad4c) → `01125d08`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abad50`](#insn-00abad50) → [`0043bb58`](../0043b/0043bb58.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bb58` · 推定シンボル `None` · 推定型 `None`
- [`00abad54`](#insn-00abad54) → `01125d10`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abad60`](#insn-00abad60) → `01125d08`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abad64`](#insn-00abad64) → [`0043bb58`](../0043b/0043bb58.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bb58` · 推定シンボル `None` · 推定型 `None`
- [`00abad68`](#insn-00abad68) → `01125d10`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abad74`](#insn-00abad74) → `01125d08`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abad78`](#insn-00abad78) → [`0043bb58`](../0043b/0043bb58.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bb58` · 推定シンボル `None` · 推定型 `None`
- [`00abad7c`](#insn-00abad7c) → `01125d10`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abad88`](#insn-00abad88) → `01125d08`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abad8c`](#insn-00abad8c) → [`0043bb58`](../0043b/0043bb58.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bb58` · 推定シンボル `None` · 推定型 `None`
- [`00abad90`](#insn-00abad90) → `01125d10`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abad9c`](#insn-00abad9c) → `01125d08`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abada0`](#insn-00abada0) → [`0043bb58`](../0043b/0043bb58.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bb58` · 推定シンボル `None` · 推定型 `None`
- [`00abada4`](#insn-00abada4) → `01125d10`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abadb0`](#insn-00abadb0) → `01125d08`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abadb4`](#insn-00abadb4) → [`0043bb58`](../0043b/0043bb58.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bb58` · 推定シンボル `None` · 推定型 `None`
- [`00abadb8`](#insn-00abadb8) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abadbc`](#insn-00abadbc) → [`00abae38`](#insn-00abae38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abadc0`](#insn-00abadc0) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abadc4`](#insn-00abadc4) → [`00abae48`](#insn-00abae48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abadc8`](#insn-00abadc8) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abadcc`](#insn-00abadcc) → [`00abae58`](#insn-00abae58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abadd0`](#insn-00abadd0) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abadd4`](#insn-00abadd4) → [`00abae68`](#insn-00abae68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abadd8`](#insn-00abadd8) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abaddc`](#insn-00abaddc) → [`00abae78`](#insn-00abae78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abade0`](#insn-00abade0) → `Stack[-0xf0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abade4`](#insn-00abade4) → [`00abae88`](#insn-00abae88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abade8`](#insn-00abade8) → `Stack[-0x110]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abadec`](#insn-00abadec) → [`00abadf8`](#insn-00abadf8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abadf0`](#insn-00abadf0) → `Stack[-0x100]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abadf4`](#insn-00abadf4) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00abadfc`](#insn-00abadfc) → [`0043b1d0`](../0043b/0043b1d0.md) · `PARAM` · `ANALYSIS` · 関数 `0043b1d0` · 推定シンボル `None` · 推定型 `None`
- [`00abae04`](#insn-00abae04) → `01125d08`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abae0c`](#insn-00abae0c) → `00c64030`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00abae10`](#insn-00abae10) → [`00c58ed0`](../00c58/00c58ed0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58ed0` · 推定シンボル `None` · 推定型 `None`
- [`00abae18`](#insn-00abae18) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abae20`](#insn-00abae20) → [`00abaf68`](#insn-00abaf68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abae24`](#insn-00abae24) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abae28`](#insn-00abae28) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abae2c`](#insn-00abae2c) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abae38`](#insn-00abae38) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abae3c`](#insn-00abae3c) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00abae40`](#insn-00abae40) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abae44`](#insn-00abae44) → [`00abadc8`](#insn-00abadc8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abae48`](#insn-00abae48) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abae4c`](#insn-00abae4c) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00abae50`](#insn-00abae50) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abae54`](#insn-00abae54) → [`00abadd0`](#insn-00abadd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abae58`](#insn-00abae58) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abae5c`](#insn-00abae5c) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00abae60`](#insn-00abae60) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abae64`](#insn-00abae64) → [`00abadd8`](#insn-00abadd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abae68`](#insn-00abae68) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abae6c`](#insn-00abae6c) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00abae70`](#insn-00abae70) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abae74`](#insn-00abae74) → [`00abade0`](#insn-00abade0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abae78`](#insn-00abae78) → `Stack[-0xc0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abae7c`](#insn-00abae7c) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00abae80`](#insn-00abae80) → `Stack[-0xf0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abae84`](#insn-00abae84) → [`00abade8`](#insn-00abade8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abae88`](#insn-00abae88) → `Stack[-0xe0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abae8c`](#insn-00abae8c) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00abae90`](#insn-00abae90) → `Stack[-0x110]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abae94`](#insn-00abae94) → [`00abadf0`](#insn-00abadf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abae98`](#insn-00abae98) → [`00abadf8`](#insn-00abadf8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abaf68`](#insn-00abaf68) → [`00c58f80`](../00c58/00c58f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f80` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00ababe0`](#insn-00ababe0)

~~~json
{
  "source": "00ababe0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ababe4`](#insn-00ababe4)

~~~json
{
  "source": "00ababe4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ababe8`](#insn-00ababe8)

~~~json
{
  "source": "00ababe8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abac0c`](#insn-00abac0c)

~~~json
{
  "source": "00abac0c",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abac18`](#insn-00abac18)

~~~json
{
  "source": "00abac18",
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
- 参照命令 [`00abac20`](#insn-00abac20)

~~~json
{
  "source": "00abac20",
  "target": "Stack[-0xff]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abac24`](#insn-00abac24)

~~~json
{
  "source": "00abac24",
  "target": "Stack[-0xf8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abac34`](#insn-00abac34)

~~~json
{
  "source": "00abac34",
  "target": "Stack[-0x10f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abac3c`](#insn-00abac3c)

~~~json
{
  "source": "00abac3c",
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
- 参照命令 [`00abac40`](#insn-00abac40)

~~~json
{
  "source": "00abac40",
  "target": "Stack[-0xdf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abac48`](#insn-00abac48)

~~~json
{
  "source": "00abac48",
  "target": "Stack[-0xd8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abac58`](#insn-00abac58)

~~~json
{
  "source": "00abac58",
  "target": "Stack[-0xef]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abac5c`](#insn-00abac5c)

~~~json
{
  "source": "00abac5c",
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
- 参照命令 [`00abac60`](#insn-00abac60)

~~~json
{
  "source": "00abac60",
  "target": "Stack[-0xbf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abac68`](#insn-00abac68)

~~~json
{
  "source": "00abac68",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abac78`](#insn-00abac78)

~~~json
{
  "source": "00abac78",
  "target": "Stack[-0xcf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abac7c`](#insn-00abac7c)

~~~json
{
  "source": "00abac7c",
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
- 参照命令 [`00abac80`](#insn-00abac80)

~~~json
{
  "source": "00abac80",
  "target": "Stack[-0x9f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abac88`](#insn-00abac88)

~~~json
{
  "source": "00abac88",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abac94`](#insn-00abac94)

~~~json
{
  "source": "00abac94",
  "target": "Stack[-0xaf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abac98`](#insn-00abac98)

~~~json
{
  "source": "00abac98",
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
- 参照命令 [`00abaca0`](#insn-00abaca0)

~~~json
{
  "source": "00abaca0",
  "target": "Stack[-0x7f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abaca8`](#insn-00abaca8)

~~~json
{
  "source": "00abaca8",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abacb4`](#insn-00abacb4)

~~~json
{
  "source": "00abacb4",
  "target": "Stack[-0x8f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abacb8`](#insn-00abacb8)

~~~json
{
  "source": "00abacb8",
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
- 参照命令 [`00abacc0`](#insn-00abacc0)

~~~json
{
  "source": "00abacc0",
  "target": "Stack[-0x5f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abacc8`](#insn-00abacc8)

~~~json
{
  "source": "00abacc8",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abacd4`](#insn-00abacd4)

~~~json
{
  "source": "00abacd4",
  "target": "Stack[-0x6f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abacd8`](#insn-00abacd8)

~~~json
{
  "source": "00abacd8",
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
- 参照命令 [`00abacdc`](#insn-00abacdc)

~~~json
{
  "source": "00abacdc",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abace0`](#insn-00abace0)

~~~json
{
  "source": "00abace0",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abace4`](#insn-00abace4)

~~~json
{
  "source": "00abace4",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abace8`](#insn-00abace8)

~~~json
{
  "source": "00abace8",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abacec`](#insn-00abacec)

~~~json
{
  "source": "00abacec",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abacf0`](#insn-00abacf0)

~~~json
{
  "source": "00abacf0",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abacf4`](#insn-00abacf4)

~~~json
{
  "source": "00abacf4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abacfc`](#insn-00abacfc)

~~~json
{
  "source": "00abacfc",
  "target": "Stack[-0x118]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abad00`](#insn-00abad00)

~~~json
{
  "source": "00abad00",
  "target": "Stack[-0xfd]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abad04`](#insn-00abad04)

~~~json
{
  "source": "00abad04",
  "target": "Stack[-0xdd]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abad08`](#insn-00abad08)

~~~json
{
  "source": "00abad08",
  "target": "Stack[-0xbd]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abad0c`](#insn-00abad0c)

~~~json
{
  "source": "00abad0c",
  "target": "Stack[-0x9d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abad10`](#insn-00abad10)

~~~json
{
  "source": "00abad10",
  "target": "Stack[-0x7d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abad14`](#insn-00abad14)

~~~json
{
  "source": "00abad14",
  "target": "Stack[-0x5d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abad18`](#insn-00abad18)

~~~json
{
  "source": "00abad18",
  "target": "Stack[-0x3f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abad1c`](#insn-00abad1c)

~~~json
{
  "source": "00abad1c",
  "target": "Stack[-0x4f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abad20`](#insn-00abad20)

~~~json
{
  "source": "00abad20",
  "target": "Stack[-0x3d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abad24`](#insn-00abad24)

~~~json
{
  "source": "00abad24",
  "target": "01125d18",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01125d18",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00abad28`](#insn-00abad28)

~~~json
{
  "source": "00abad28",
  "target": "01125d10",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01125d10",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00abad2c`](#insn-00abad2c)

~~~json
{
  "source": "00abad2c",
  "target": "01125d08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01125d08",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00abad2c`](#insn-00abad2c)

~~~json
{
  "source": "00abad2c",
  "target": "01125d10",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01125d10",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00abad38`](#insn-00abad38)

~~~json
{
  "source": "00abad38",
  "target": "01125d08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01125d08",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00abad3c`](#insn-00abad3c)

~~~json
{
  "source": "00abad3c",
  "target": "0043bb58",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abad40`](#insn-00abad40)

~~~json
{
  "source": "00abad40",
  "target": "01125d10",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01125d10",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00abad4c`](#insn-00abad4c)

~~~json
{
  "source": "00abad4c",
  "target": "01125d08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01125d08",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00abad50`](#insn-00abad50)

~~~json
{
  "source": "00abad50",
  "target": "0043bb58",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abad54`](#insn-00abad54)

~~~json
{
  "source": "00abad54",
  "target": "01125d10",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01125d10",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00abad60`](#insn-00abad60)

~~~json
{
  "source": "00abad60",
  "target": "01125d08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01125d08",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00abad64`](#insn-00abad64)

~~~json
{
  "source": "00abad64",
  "target": "0043bb58",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abad68`](#insn-00abad68)

~~~json
{
  "source": "00abad68",
  "target": "01125d10",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01125d10",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00abad74`](#insn-00abad74)

~~~json
{
  "source": "00abad74",
  "target": "01125d08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01125d08",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00abad78`](#insn-00abad78)

~~~json
{
  "source": "00abad78",
  "target": "0043bb58",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abad7c`](#insn-00abad7c)

~~~json
{
  "source": "00abad7c",
  "target": "01125d10",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01125d10",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00abad88`](#insn-00abad88)

~~~json
{
  "source": "00abad88",
  "target": "01125d08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01125d08",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00abad8c`](#insn-00abad8c)

~~~json
{
  "source": "00abad8c",
  "target": "0043bb58",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abad90`](#insn-00abad90)

~~~json
{
  "source": "00abad90",
  "target": "01125d10",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01125d10",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00abad9c`](#insn-00abad9c)

~~~json
{
  "source": "00abad9c",
  "target": "01125d08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01125d08",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00abada0`](#insn-00abada0)

~~~json
{
  "source": "00abada0",
  "target": "0043bb58",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abada4`](#insn-00abada4)

~~~json
{
  "source": "00abada4",
  "target": "01125d10",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01125d10",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00abadb0`](#insn-00abadb0)

~~~json
{
  "source": "00abadb0",
  "target": "01125d08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01125d08",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00abadb4`](#insn-00abadb4)

~~~json
{
  "source": "00abadb4",
  "target": "0043bb58",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abadb8`](#insn-00abadb8)

~~~json
{
  "source": "00abadb8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abadbc`](#insn-00abadbc)

~~~json
{
  "source": "00abadbc",
  "target": "00abae38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abadc0`](#insn-00abadc0)

~~~json
{
  "source": "00abadc0",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abadc4`](#insn-00abadc4)

~~~json
{
  "source": "00abadc4",
  "target": "00abae48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abadc8`](#insn-00abadc8)

~~~json
{
  "source": "00abadc8",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abadcc`](#insn-00abadcc)

~~~json
{
  "source": "00abadcc",
  "target": "00abae58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abadd0`](#insn-00abadd0)

~~~json
{
  "source": "00abadd0",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abadd4`](#insn-00abadd4)

~~~json
{
  "source": "00abadd4",
  "target": "00abae68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abadd8`](#insn-00abadd8)

~~~json
{
  "source": "00abadd8",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abaddc`](#insn-00abaddc)

~~~json
{
  "source": "00abaddc",
  "target": "00abae78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abade0`](#insn-00abade0)

~~~json
{
  "source": "00abade0",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abade4`](#insn-00abade4)

~~~json
{
  "source": "00abade4",
  "target": "00abae88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abade8`](#insn-00abade8)

~~~json
{
  "source": "00abade8",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abadec`](#insn-00abadec)

~~~json
{
  "source": "00abadec",
  "target": "00abadf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abadf0`](#insn-00abadf0)

~~~json
{
  "source": "00abadf0",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abadf4`](#insn-00abadf4)

~~~json
{
  "source": "00abadf4",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abadfc`](#insn-00abadfc)

~~~json
{
  "source": "00abadfc",
  "target": "0043b1d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abae04`](#insn-00abae04)

~~~json
{
  "source": "00abae04",
  "target": "01125d08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01125d08",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00abae0c`](#insn-00abae0c)

~~~json
{
  "source": "00abae0c",
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
- 参照命令 [`00abae10`](#insn-00abae10)

~~~json
{
  "source": "00abae10",
  "target": "00c58ed0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abae18`](#insn-00abae18)

~~~json
{
  "source": "00abae18",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abae20`](#insn-00abae20)

~~~json
{
  "source": "00abae20",
  "target": "00abaf68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abae24`](#insn-00abae24)

~~~json
{
  "source": "00abae24",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abae28`](#insn-00abae28)

~~~json
{
  "source": "00abae28",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abae2c`](#insn-00abae2c)

~~~json
{
  "source": "00abae2c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abae38`](#insn-00abae38)

~~~json
{
  "source": "00abae38",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abae3c`](#insn-00abae3c)

~~~json
{
  "source": "00abae3c",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abae40`](#insn-00abae40)

~~~json
{
  "source": "00abae40",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abae44`](#insn-00abae44)

~~~json
{
  "source": "00abae44",
  "target": "00abadc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abae48`](#insn-00abae48)

~~~json
{
  "source": "00abae48",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abae4c`](#insn-00abae4c)

~~~json
{
  "source": "00abae4c",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abae50`](#insn-00abae50)

~~~json
{
  "source": "00abae50",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abae54`](#insn-00abae54)

~~~json
{
  "source": "00abae54",
  "target": "00abadd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abae58`](#insn-00abae58)

~~~json
{
  "source": "00abae58",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abae5c`](#insn-00abae5c)

~~~json
{
  "source": "00abae5c",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abae60`](#insn-00abae60)

~~~json
{
  "source": "00abae60",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abae64`](#insn-00abae64)

~~~json
{
  "source": "00abae64",
  "target": "00abadd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abae68`](#insn-00abae68)

~~~json
{
  "source": "00abae68",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abae6c`](#insn-00abae6c)

~~~json
{
  "source": "00abae6c",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abae70`](#insn-00abae70)

~~~json
{
  "source": "00abae70",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abae74`](#insn-00abae74)

~~~json
{
  "source": "00abae74",
  "target": "00abade0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abae78`](#insn-00abae78)

~~~json
{
  "source": "00abae78",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abae7c`](#insn-00abae7c)

~~~json
{
  "source": "00abae7c",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abae80`](#insn-00abae80)

~~~json
{
  "source": "00abae80",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abae84`](#insn-00abae84)

~~~json
{
  "source": "00abae84",
  "target": "00abade8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abae88`](#insn-00abae88)

~~~json
{
  "source": "00abae88",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abae8c`](#insn-00abae8c)

~~~json
{
  "source": "00abae8c",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abae90`](#insn-00abae90)

~~~json
{
  "source": "00abae90",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abae94`](#insn-00abae94)

~~~json
{
  "source": "00abae94",
  "target": "00abadf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abae98`](#insn-00abae98)

~~~json
{
  "source": "00abae98",
  "target": "00abadf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abaf68`](#insn-00abaf68)

~~~json
{
  "source": "00abaf68",
  "target": "00c58f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
