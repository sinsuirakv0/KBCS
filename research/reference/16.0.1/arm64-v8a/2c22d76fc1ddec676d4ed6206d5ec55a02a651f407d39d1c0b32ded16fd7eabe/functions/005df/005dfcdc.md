# 005dfcdc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `005dfc9c`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005df/005dfc9c.md) · 移動量 `+0x40`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0025.md#compare-0302a247372beff9eea38c140d772ecb)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `005dfd1c`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005df/005dfd1c.md) · 移動量 `+0x40`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0025.md#compare-69c700ba06819f1a8136f3c58acfa972)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "005dfcdc",
  "name": "_INIT_66",
  "size": 708,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "cec47a64e3ba327b03389085f3a7cbd6c473f1d1c11958cca30bd32f236d84c4",
  "source_text_sha256": "cec47a64e3ba327b03389085f3a7cbd6c473f1d1c11958cca30bd32f236d84c4",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "005dfcdc",
        "005dff9b"
      ],
      [
        "005e0068",
        "005e006b"
      ]
    ],
    "bytes_sha256": "d07696b3f3fd30fc62f9a270daa6ebf74391f5debd680ad385d7c6696c4452e8",
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

- [0043b7f8](../0043b/0043b7f8.md)
- [00c57e30](../00c57/00c57e30.md)
- [00c57eb0](../00c57/00c57eb0.md)
- [00c57ee0](../00c57/00c57ee0.md)

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

## 疑似コード / UTF-8 6963 bytes

~~~c

/* WARNING: Type propagation algorithm not settling */

void _INIT_66(void)

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
  uStack_107 = (undefined7)s_CgkIjM3y_ZQaEAIQAg_002b7f26._8_8_;
  cStack_100 = SUB81(s_CgkIjM3y_ZQaEAIQAg_002b7f26._8_8_,7);
  local_10f = (char  [8])s_CgkIjM3y_ZQaEAIQAg_002b7f26._0_8_;
                    /* try { // try from 005dfd40 to 006dfdfb has its CatchHandler @ 005df6dc */
  uStack_df = 0x4142;
  local_d8[0] = 2;
  uStack_e7 = (undefined7)s_CgkIjM3y_ZQaEAIQBA_002b7f39._8_8_;
  cStack_e0 = SUB81(s_CgkIjM3y_ZQaEAIQBA_002b7f39._8_8_,7);
  local_ef = (char  [8])s_CgkIjM3y_ZQaEAIQBA_002b7f39._0_8_;
  uStack_bf = 0x6742;
  local_b8[0] = 3;
  uStack_c7 = (undefined7)s_CgkIjM3y_ZQaEAIQBg_002b8dc2._8_8_;
  cStack_c0 = SUB81(s_CgkIjM3y_ZQaEAIQBg_002b8dc2._8_8_,7);
  local_cf = (char  [8])s_CgkIjM3y_ZQaEAIQBg_002b8dc2._0_8_;
  uStack_9f = 0x7741;
  local_98[0] = 4;
  uStack_a7 = (undefined7)s_CgkIjM3y_ZQaEAIQAw_002a2f62._8_8_;
  cStack_a0 = SUB81(s_CgkIjM3y_ZQaEAIQAw_002a2f62._8_8_,7);
  local_af = (char  [8])s_CgkIjM3y_ZQaEAIQAw_002a2f62._0_8_;
  uStack_7f = 0x5142;
                    /* catch(type#1 @ 00000000) { ... } // from try @ 005dfbb0 with catch @ 005dfda4
                        */
                    /* catch(type#1 @ 00000000) { ... } // from try @ 005dfb80 with catch @ 005dfda8
                        */
  local_78[0] = 5;
  uStack_87 = (undefined7)s_CgkIjM3y_ZQaEAIQBQ_002ac5d2._8_8_;
  cStack_80 = SUB81(s_CgkIjM3y_ZQaEAIQBQ_002ac5d2._8_8_,7);
                    /* catch(type#1 @ 00000000) { ... } // from try @ 005dfa70 with catch @ 005dfdac
                        */
                    /* catch(type#1 @ 00000000) { ... } // from try @ 005df924 with catch @ 005dfdb0
                        */
                    /* catch(type#1 @ 00000000) { ... } // from try @ 005dfa00 with catch @ 005dfdb4
                        */
  local_8f = (char  [8])s_CgkIjM3y_ZQaEAIQBQ_002ac5d2._0_8_;
                    /* catch(type#1 @ 00000000) { ... } // from try @ 005df8b4 with catch @ 005dfdb8
                        */
                    /* catch(type#1 @ 00000000) { ... } // from try @ 005df8ac with catch @ 005dfdbc
                        */
  uStack_5f = 0x7742;
                    /* catch(type#1 @ 00000000) { ... } // from try @ 005df86c with catch @ 005dfdc4
                        */
                    /* catch(type#1 @ 00000000) { ... } // from try @ 005df9b4 with catch @ 005dfdc8
                       catch(type#1 @ 00000000) { ... } // from try @ 005dfb00 with catch @ 005dfdc8
                        */
  local_58[0] = 6;
  uStack_67 = (undefined7)s_CgkIjM3y_ZQaEAIQBw_002a0f5d._8_8_;
  cStack_60 = SUB81(s_CgkIjM3y_ZQaEAIQBw_002a0f5d._8_8_,7);
                    /* catch(type#1 @ 00000000) { ... } // from try @ 005dfc08 with catch @ 005dfdcc
                        */
  local_6f = (char  [8])s_CgkIjM3y_ZQaEAIQBw_002a0f5d._0_8_;
  local_110 = 0x24;
  local_f0 = 0x24;
  local_d0 = 0x24;
  local_b0 = 0x24;
  local_90 = 0x24;
  local_70 = 0x24;
  local_50 = 0x24;
                    /* try { // try from 005dfdfc to 006e0023 has its CatchHandler @ 005dfdfc
                       catch(type#1 @ 00000000) { ... } // from try @ 005dfdfc with catch @ 005dfdfc
                       catch(type#1 @ 00000000) { ... } // from try @ 005e00c0 with catch @ 005dfdfc
                       catch(type#1 @ 00000000) { ... } // from try @ 005e0138 with catch @ 005dfdfc
                       catch(type#1 @ 00000000) { ... } // from try @ 005e0304 with catch @ 005dfdfc
                       catch(type#1 @ 00000000) { ... } // from try @ 005e0390 with catch @ 005dfdfc
                        */
  local_118[0] = 0;
  uStack_fd = 0;
  uStack_dd = 0;
  uStack_bd = 0;
  uStack_9d = 0;
  uStack_7d = 0;
  uStack_5d = 0;
  uStack_3f = 0x4143;
  uStack_47 = (undefined7)s_CgkIjM3y_ZQaEAIQCA_002a3f09._8_8_;
  cStack_40 = SUB81(s_CgkIjM3y_ZQaEAIQCA_002a3f09._8_8_,7);
  local_4f = (char  [8])s_CgkIjM3y_ZQaEAIQCA_002a3f09._0_8_;
  uStack_3d = 0;
  DAT_00ca68e0 = 0;
  DAT_00ca68d8 = 0;
  DAT_00ca68d0 = &DAT_00ca68d8;
  FUN_0043b7f8(&DAT_00ca68d0,&DAT_00ca68d8,local_118,local_118);
  FUN_0043b7f8(&DAT_00ca68d0,&DAT_00ca68d8,local_f8,local_f8);
  FUN_0043b7f8(&DAT_00ca68d0,&DAT_00ca68d8,local_d8,local_d8);
  FUN_0043b7f8(&DAT_00ca68d0,&DAT_00ca68d8,local_b8,local_b8);
  FUN_0043b7f8(&DAT_00ca68d0,&DAT_00ca68d8,local_98,local_98);
  FUN_0043b7f8(&DAT_00ca68d0,&DAT_00ca68d8,local_78,local_78);
  FUN_0043b7f8(&DAT_00ca68d0,&DAT_00ca68d8,local_58,local_58);
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
  __cxa_atexit(FUN_0043ae70,&DAT_00ca68d0,&PTR_LOOP_00c62f90);
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
<a id="insn-005dfcdc"></a> `005dfcdc` | `ff 83 04 d1` | sub sp,sp,#0x120 | `FALL_THROUGH`
<a id="insn-005dfce0"></a> `005dfce0` | `fd 7b 0f a9` | stp x29,x30,[sp, #0xf0] | `FALL_THROUGH`
<a id="insn-005dfce4"></a> `005dfce4` | `fc 57 10 a9` | stp x28,x21,[sp, #0x100] | `FALL_THROUGH`
<a id="insn-005dfce8"></a> `005dfce8` | `f4 4f 11 a9` | stp x20,x19,[sp, #0x110] | `FALL_THROUGH`
<a id="insn-005dfcec"></a> `005dfcec` | `fd c3 03 91` | add x29,sp,#0xf0 | `FALL_THROUGH`
<a id="insn-005dfcf0"></a> `005dfcf0` | `55 d0 3b d5` | mrs x21,tpidr_el0 | `FALL_THROUGH`
<a id="insn-005dfcf4"></a> `005dfcf4` | `2a e8 8c 52` | mov w10,#0x6741 | `FALL_THROUGH`
<a id="insn-005dfcf8"></a> `005dfcf8` | `f4 23 00 91` | add x20,sp,#0x8 | `FALL_THROUGH`
<a id="insn-005dfcfc"></a> `005dfcfc` | `a9 16 40 f9` | ldr x9,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-005dfd00"></a> `005dfd00` | `88 04 80 52` | mov w8,#0x24 | `FALL_THROUGH`
<a id="insn-005dfd04"></a> `005dfd04` | `33 36 00 f0` | adrp x19,0xca6000 | `FALL_THROUGH`
<a id="insn-005dfd08"></a> `005dfd08` | `73 42 23 91` | add x19,x19,#0x8d0 | `FALL_THROUGH`
<a id="insn-005dfd0c"></a> `005dfd0c` | `a9 83 1f f8` | stur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-005dfd10"></a> `005dfd10` | `c9 e6 ff 90` | adrp x9,0x2b7000 | `FALL_THROUGH`
<a id="insn-005dfd14"></a> `005dfd14` | `29 99 3c 91` | add x9,x9,#0xf26 | `FALL_THROUGH`
<a id="insn-005dfd18"></a> `005dfd18` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-005dfd1c"></a> `005dfd1c` | `29 00 80 52` | mov w9,#0x1 | `FALL_THROUGH`
<a id="insn-005dfd20"></a> `005dfd20` | `ea 13 02 78` | sturh w10,[sp, #0x21] | `FALL_THROUGH`
<a id="insn-005dfd24"></a> `005dfd24` | `e9 2b 00 b9` | str w9,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-005dfd28"></a> `005dfd28` | `49 28 88 52` | mov w9,#0x4142 | `FALL_THROUGH`
<a id="insn-005dfd2c"></a> `005dfd2c` | `ca e6 ff 90` | adrp x10,0x2b7000 | `FALL_THROUGH`
<a id="insn-005dfd30"></a> `005dfd30` | `4a e5 3c 91` | add x10,x10,#0xf39 | `FALL_THROUGH`
<a id="insn-005dfd34"></a> `005dfd34` | `e0 13 81 3c` | stur q0,[sp, #0x11] | `FALL_THROUGH`
<a id="insn-005dfd38"></a> `005dfd38` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-005dfd3c"></a> `005dfd3c` | `40 01 c0 3d` | ldr q0,[x10] | `FALL_THROUGH`
<a id="insn-005dfd40"></a> `005dfd40` | `e9 13 04 78` | sturh w9,[sp, #0x41] | `FALL_THROUGH`
<a id="insn-005dfd44"></a> `005dfd44` | `49 00 80 52` | mov w9,#0x2 | `FALL_THROUGH`
<a id="insn-005dfd48"></a> `005dfd48` | `e9 4b 00 b9` | str w9,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-005dfd4c"></a> `005dfd4c` | `49 e8 8c 52` | mov w9,#0x6742 | `FALL_THROUGH`
<a id="insn-005dfd50"></a> `005dfd50` | `ca e6 ff b0` | adrp x10,0x2b8000 | `FALL_THROUGH`
<a id="insn-005dfd54"></a> `005dfd54` | `4a 09 37 91` | add x10,x10,#0xdc2 | `FALL_THROUGH`
<a id="insn-005dfd58"></a> `005dfd58` | `e0 13 83 3c` | stur q0,[sp, #0x31] | `FALL_THROUGH`
<a id="insn-005dfd5c"></a> `005dfd5c` | `40 01 c0 3d` | ldr q0,[x10] | `FALL_THROUGH`
<a id="insn-005dfd60"></a> `005dfd60` | `e9 13 06 78` | sturh w9,[sp, #0x61] | `FALL_THROUGH`
<a id="insn-005dfd64"></a> `005dfd64` | `69 00 80 52` | mov w9,#0x3 | `FALL_THROUGH`
<a id="insn-005dfd68"></a> `005dfd68` | `e9 6b 00 b9` | str w9,[sp, #0x68] | `FALL_THROUGH`
<a id="insn-005dfd6c"></a> `005dfd6c` | `29 e8 8e 52` | mov w9,#0x7741 | `FALL_THROUGH`
<a id="insn-005dfd70"></a> `005dfd70` | `0a e6 ff f0` | adrp x10,0x2a2000 | `FALL_THROUGH`
<a id="insn-005dfd74"></a> `005dfd74` | `4a 89 3d 91` | add x10,x10,#0xf62 | `FALL_THROUGH`
<a id="insn-005dfd78"></a> `005dfd78` | `e0 13 85 3c` | stur q0,[sp, #0x51] | `FALL_THROUGH`
<a id="insn-005dfd7c"></a> `005dfd7c` | `40 01 c0 3d` | ldr q0,[x10] | `FALL_THROUGH`
<a id="insn-005dfd80"></a> `005dfd80` | `e9 13 08 78` | sturh w9,[sp, #0x81] | `FALL_THROUGH`
<a id="insn-005dfd84"></a> `005dfd84` | `89 00 80 52` | mov w9,#0x4 | `FALL_THROUGH`
<a id="insn-005dfd88"></a> `005dfd88` | `e9 8b 00 b9` | str w9,[sp, #0x88] | `FALL_THROUGH`
<a id="insn-005dfd8c"></a> `005dfd8c` | `69 e6 ff b0` | adrp x9,0x2ac000 | `FALL_THROUGH`
<a id="insn-005dfd90"></a> `005dfd90` | `29 49 17 91` | add x9,x9,#0x5d2 | `FALL_THROUGH`
<a id="insn-005dfd94"></a> `005dfd94` | `e0 13 87 3c` | stur q0,[sp, #0x71] | `FALL_THROUGH`
<a id="insn-005dfd98"></a> `005dfd98` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-005dfd9c"></a> `005dfd9c` | `49 28 8a 52` | mov w9,#0x5142 | `FALL_THROUGH`
<a id="insn-005dfda0"></a> `005dfda0` | `89 92 09 78` | sturh w9,[x20, #0x99] | `FALL_THROUGH`
<a id="insn-005dfda4"></a> `005dfda4` | `a9 00 80 52` | mov w9,#0x5 | `FALL_THROUGH`
<a id="insn-005dfda8"></a> `005dfda8` | `e9 ab 00 b9` | str w9,[sp, #0xa8] | `FALL_THROUGH`
<a id="insn-005dfdac"></a> `005dfdac` | `09 e6 ff b0` | adrp x9,0x2a0000 | `FALL_THROUGH`
<a id="insn-005dfdb0"></a> `005dfdb0` | `29 75 3d 91` | add x9,x9,#0xf5d | `FALL_THROUGH`
<a id="insn-005dfdb4"></a> `005dfdb4` | `80 92 88 3c` | stur q0,[x20, #0x89] | `FALL_THROUGH`
<a id="insn-005dfdb8"></a> `005dfdb8` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-005dfdbc"></a> `005dfdbc` | `49 e8 8e 52` | mov w9,#0x7742 | `FALL_THROUGH`
<a id="insn-005dfdc0"></a> `005dfdc0` | `89 92 0b 78` | sturh w9,[x20, #0xb9] | `FALL_THROUGH`
<a id="insn-005dfdc4"></a> `005dfdc4` | `c9 00 80 52` | mov w9,#0x6 | `FALL_THROUGH`
<a id="insn-005dfdc8"></a> `005dfdc8` | `e9 cb 00 b9` | str w9,[sp, #0xc8] | `FALL_THROUGH`
<a id="insn-005dfdcc"></a> `005dfdcc` | `29 e6 ff 90` | adrp x9,0x2a3000 | `FALL_THROUGH`
<a id="insn-005dfdd0"></a> `005dfdd0` | `29 25 3c 91` | add x9,x9,#0xf09 | `FALL_THROUGH`
<a id="insn-005dfdd4"></a> `005dfdd4` | `80 92 8a 3c` | stur q0,[x20, #0xa9] | `FALL_THROUGH`
<a id="insn-005dfdd8"></a> `005dfdd8` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-005dfddc"></a> `005dfddc` | `e8 43 00 39` | strb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-005dfde0"></a> `005dfde0` | `e8 c3 00 39` | strb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-005dfde4"></a> `005dfde4` | `e8 43 01 39` | strb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-005dfde8"></a> `005dfde8` | `e8 c3 01 39` | strb w8,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-005dfdec"></a> `005dfdec` | `e8 43 02 39` | strb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-005dfdf0"></a> `005dfdf0` | `e8 c3 02 39` | strb w8,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-005dfdf4"></a> `005dfdf4` | `e8 43 03 39` | strb w8,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-005dfdf8"></a> `005dfdf8` | `68 28 88 52` | mov w8,#0x4143 | `FALL_THROUGH`
<a id="insn-005dfdfc"></a> `005dfdfc` | `ff 0b 00 b9` | str wzr,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-005dfe00"></a> `005dfe00` | `ff 8f 00 39` | strb wzr,[sp, #0x23] | `FALL_THROUGH`
<a id="insn-005dfe04"></a> `005dfe04` | `ff 0f 01 39` | strb wzr,[sp, #0x43] | `FALL_THROUGH`
<a id="insn-005dfe08"></a> `005dfe08` | `ff 8f 01 39` | strb wzr,[sp, #0x63] | `FALL_THROUGH`
<a id="insn-005dfe0c"></a> `005dfe0c` | `ff 0f 02 39` | strb wzr,[sp, #0x83] | `FALL_THROUGH`
<a id="insn-005dfe10"></a> `005dfe10` | `ff 8f 02 39` | strb wzr,[sp, #0xa3] | `FALL_THROUGH`
<a id="insn-005dfe14"></a> `005dfe14` | `ff 0f 03 39` | strb wzr,[sp, #0xc3] | `FALL_THROUGH`
<a id="insn-005dfe18"></a> `005dfe18` | `88 92 0d 78` | sturh w8,[x20, #0xd9] | `FALL_THROUGH`
<a id="insn-005dfe1c"></a> `005dfe1c` | `80 92 8c 3c` | stur q0,[x20, #0xc9] | `FALL_THROUGH`
<a id="insn-005dfe20"></a> `005dfe20` | `ff 8f 03 39` | strb wzr,[sp, #0xe3] | `FALL_THROUGH`
<a id="insn-005dfe24"></a> `005dfe24` | `7f 0a 00 f9` | str xzr,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-005dfe28"></a> `005dfe28` | `3f 8c 00 f8` | str xzr,[x1, #0x8]! | `FALL_THROUGH`
<a id="insn-005dfe2c"></a> `005dfe2c` | `61 02 00 f9` | str x1,[x19] | `FALL_THROUGH`
<a id="insn-005dfe30"></a> `005dfe30` | `e2 23 00 91` | add x2,sp,#0x8 | `FALL_THROUGH`
<a id="insn-005dfe34"></a> `005dfe34` | `e3 23 00 91` | add x3,sp,#0x8 | `FALL_THROUGH`
<a id="insn-005dfe38"></a> `005dfe38` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-005dfe3c"></a> `005dfe3c` | `6f 6e f9 97` | bl 0x0043b7f8 | `UNCONDITIONAL_CALL`
<a id="insn-005dfe40"></a> `005dfe40` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-005dfe44"></a> `005dfe44` | `82 82 00 91` | add x2,x20,#0x20 | `FALL_THROUGH`
<a id="insn-005dfe48"></a> `005dfe48` | `83 82 00 91` | add x3,x20,#0x20 | `FALL_THROUGH`
<a id="insn-005dfe4c"></a> `005dfe4c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-005dfe50"></a> `005dfe50` | `6a 6e f9 97` | bl 0x0043b7f8 | `UNCONDITIONAL_CALL`
<a id="insn-005dfe54"></a> `005dfe54` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-005dfe58"></a> `005dfe58` | `82 02 01 91` | add x2,x20,#0x40 | `FALL_THROUGH`
<a id="insn-005dfe5c"></a> `005dfe5c` | `83 02 01 91` | add x3,x20,#0x40 | `FALL_THROUGH`
<a id="insn-005dfe60"></a> `005dfe60` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-005dfe64"></a> `005dfe64` | `65 6e f9 97` | bl 0x0043b7f8 | `UNCONDITIONAL_CALL`
<a id="insn-005dfe68"></a> `005dfe68` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-005dfe6c"></a> `005dfe6c` | `82 82 01 91` | add x2,x20,#0x60 | `FALL_THROUGH`
<a id="insn-005dfe70"></a> `005dfe70` | `83 82 01 91` | add x3,x20,#0x60 | `FALL_THROUGH`
<a id="insn-005dfe74"></a> `005dfe74` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-005dfe78"></a> `005dfe78` | `60 6e f9 97` | bl 0x0043b7f8 | `UNCONDITIONAL_CALL`
<a id="insn-005dfe7c"></a> `005dfe7c` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-005dfe80"></a> `005dfe80` | `82 02 02 91` | add x2,x20,#0x80 | `FALL_THROUGH`
<a id="insn-005dfe84"></a> `005dfe84` | `83 02 02 91` | add x3,x20,#0x80 | `FALL_THROUGH`
<a id="insn-005dfe88"></a> `005dfe88` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-005dfe8c"></a> `005dfe8c` | `5b 6e f9 97` | bl 0x0043b7f8 | `UNCONDITIONAL_CALL`
<a id="insn-005dfe90"></a> `005dfe90` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-005dfe94"></a> `005dfe94` | `82 82 02 91` | add x2,x20,#0xa0 | `FALL_THROUGH`
<a id="insn-005dfe98"></a> `005dfe98` | `83 82 02 91` | add x3,x20,#0xa0 | `FALL_THROUGH`
<a id="insn-005dfe9c"></a> `005dfe9c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-005dfea0"></a> `005dfea0` | `56 6e f9 97` | bl 0x0043b7f8 | `UNCONDITIONAL_CALL`
<a id="insn-005dfea4"></a> `005dfea4` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-005dfea8"></a> `005dfea8` | `82 02 03 91` | add x2,x20,#0xc0 | `FALL_THROUGH`
<a id="insn-005dfeac"></a> `005dfeac` | `83 02 03 91` | add x3,x20,#0xc0 | `FALL_THROUGH`
<a id="insn-005dfeb0"></a> `005dfeb0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-005dfeb4"></a> `005dfeb4` | `51 6e f9 97` | bl 0x0043b7f8 | `UNCONDITIONAL_CALL`
<a id="insn-005dfeb8"></a> `005dfeb8` | `e8 43 43 39` | ldrb w8,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-005dfebc"></a> `005dfebc` | `e8 03 00 37` | tbnz w8,#0x0,0x005dff38 | `CONDITIONAL_JUMP`
<a id="insn-005dfec0"></a> `005dfec0` | `e8 c3 42 39` | ldrb w8,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-005dfec4"></a> `005dfec4` | `28 04 00 37` | tbnz w8,#0x0,0x005dff48 | `CONDITIONAL_JUMP`
<a id="insn-005dfec8"></a> `005dfec8` | `e8 43 42 39` | ldrb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-005dfecc"></a> `005dfecc` | `68 04 00 37` | tbnz w8,#0x0,0x005dff58 | `CONDITIONAL_JUMP`
<a id="insn-005dfed0"></a> `005dfed0` | `e8 c3 41 39` | ldrb w8,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-005dfed4"></a> `005dfed4` | `a8 04 00 37` | tbnz w8,#0x0,0x005dff68 | `CONDITIONAL_JUMP`
<a id="insn-005dfed8"></a> `005dfed8` | `e8 43 41 39` | ldrb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-005dfedc"></a> `005dfedc` | `e8 04 00 37` | tbnz w8,#0x0,0x005dff78 | `CONDITIONAL_JUMP`
<a id="insn-005dfee0"></a> `005dfee0` | `e8 c3 40 39` | ldrb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-005dfee4"></a> `005dfee4` | `28 05 00 37` | tbnz w8,#0x0,0x005dff88 | `CONDITIONAL_JUMP`
<a id="insn-005dfee8"></a> `005dfee8` | `e8 43 40 39` | ldrb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-005dfeec"></a> `005dfeec` | `68 00 00 36` | tbz w8,#0x0,0x005dfef8 | `CONDITIONAL_JUMP`
<a id="insn-005dfef0"></a> `005dfef0` | `e0 13 40 f9` | ldr x0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-005dfef4"></a> `005dfef4` | `ef df 19 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-005dfef8"></a> `005dfef8` | `c0 f2 ff f0` | adrp x0,0x43a000 | `FALL_THROUGH`
<a id="insn-005dfefc"></a> `005dfefc` | `00 c0 39 91` | add x0,x0,#0xe70 | `FALL_THROUGH`
<a id="insn-005dff00"></a> `005dff00` | `21 36 00 f0` | adrp x1,0xca6000 | `FALL_THROUGH`
<a id="insn-005dff04"></a> `005dff04` | `21 40 23 91` | add x1,x1,#0x8d0 | `FALL_THROUGH`
<a id="insn-005dff08"></a> `005dff08` | `02 34 00 f0` | adrp x2,0xc62000 | `FALL_THROUGH`
<a id="insn-005dff0c"></a> `005dff0c` | `42 40 3e 91` | add x2,x2,#0xf90 | `FALL_THROUGH`
<a id="insn-005dff10"></a> `005dff10` | `c8 df 19 94` | bl 0x00c57e30 | `UNCONDITIONAL_CALL`
<a id="insn-005dff14"></a> `005dff14` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-005dff18"></a> `005dff18` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-005dff1c"></a> `005dff1c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-005dff20"></a> `005dff20` | `41 0a 00 54` | b.ne 0x005e0068 | `CONDITIONAL_JUMP`
<a id="insn-005dff24"></a> `005dff24` | `f4 4f 51 a9` | ldp x20,x19,[sp, #0x110] | `FALL_THROUGH`
<a id="insn-005dff28"></a> `005dff28` | `fc 57 50 a9` | ldp x28,x21,[sp, #0x100] | `FALL_THROUGH`
<a id="insn-005dff2c"></a> `005dff2c` | `fd 7b 4f a9` | ldp x29,x30,[sp, #0xf0] | `FALL_THROUGH`
<a id="insn-005dff30"></a> `005dff30` | `ff 83 04 91` | add sp,sp,#0x120 | `FALL_THROUGH`
<a id="insn-005dff34"></a> `005dff34` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-005dff38"></a> `005dff38` | `e0 73 40 f9` | ldr x0,[sp, #0xe0] | `FALL_THROUGH`
<a id="insn-005dff3c"></a> `005dff3c` | `dd df 19 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-005dff40"></a> `005dff40` | `e8 c3 42 39` | ldrb w8,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-005dff44"></a> `005dff44` | `28 fc 07 36` | tbz w8,#0x0,0x005dfec8 | `CONDITIONAL_JUMP`
<a id="insn-005dff48"></a> `005dff48` | `e0 63 40 f9` | ldr x0,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-005dff4c"></a> `005dff4c` | `d9 df 19 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-005dff50"></a> `005dff50` | `e8 43 42 39` | ldrb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-005dff54"></a> `005dff54` | `e8 fb 07 36` | tbz w8,#0x0,0x005dfed0 | `CONDITIONAL_JUMP`
<a id="insn-005dff58"></a> `005dff58` | `e0 53 40 f9` | ldr x0,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-005dff5c"></a> `005dff5c` | `d5 df 19 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-005dff60"></a> `005dff60` | `e8 c3 41 39` | ldrb w8,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-005dff64"></a> `005dff64` | `a8 fb 07 36` | tbz w8,#0x0,0x005dfed8 | `CONDITIONAL_JUMP`
<a id="insn-005dff68"></a> `005dff68` | `e0 43 40 f9` | ldr x0,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-005dff6c"></a> `005dff6c` | `d1 df 19 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-005dff70"></a> `005dff70` | `e8 43 41 39` | ldrb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-005dff74"></a> `005dff74` | `68 fb 07 36` | tbz w8,#0x0,0x005dfee0 | `CONDITIONAL_JUMP`
<a id="insn-005dff78"></a> `005dff78` | `e0 33 40 f9` | ldr x0,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-005dff7c"></a> `005dff7c` | `cd df 19 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-005dff80"></a> `005dff80` | `e8 c3 40 39` | ldrb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-005dff84"></a> `005dff84` | `28 fb 07 36` | tbz w8,#0x0,0x005dfee8 | `CONDITIONAL_JUMP`
<a id="insn-005dff88"></a> `005dff88` | `e0 23 40 f9` | ldr x0,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-005dff8c"></a> `005dff8c` | `c9 df 19 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-005dff90"></a> `005dff90` | `e8 43 40 39` | ldrb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-005dff94"></a> `005dff94` | `e8 fa 07 37` | tbnz w8,#0x0,0x005dfef0 | `CONDITIONAL_JUMP`
<a id="insn-005dff98"></a> `005dff98` | `d8 ff ff 17` | b 0x005dfef8 | `UNCONDITIONAL_JUMP`
<a id="insn-005e0068"></a> `005e0068` | `9e df 19 94` | bl 0x00c57ee0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`005dfcdc`](#insn-005dfcdc) 範囲 `[['005dfcdc', '005dfd3f']]`
  - `FALL_THROUGH` [`005dfd3c`](#insn-005dfd3c) → [`005dfd40`](#insn-005dfd40)
- ブロック [`005dfd40`](#insn-005dfd40) 範囲 `[['005dfd40', '005dfda3']]`
  - `FALL_THROUGH` [`005dfda0`](#insn-005dfda0) → [`005dfda4`](#insn-005dfda4)
- ブロック [`005dfda4`](#insn-005dfda4) 範囲 `[['005dfda4', '005dfda7']]`
  - `FALL_THROUGH` [`005dfda4`](#insn-005dfda4) → [`005dfda8`](#insn-005dfda8)
- ブロック [`005dfda8`](#insn-005dfda8) 範囲 `[['005dfda8', '005dfdab']]`
  - `FALL_THROUGH` [`005dfda8`](#insn-005dfda8) → [`005dfdac`](#insn-005dfdac)
- ブロック [`005dfdac`](#insn-005dfdac) 範囲 `[['005dfdac', '005dfdaf']]`
  - `FALL_THROUGH` [`005dfdac`](#insn-005dfdac) → [`005dfdb0`](#insn-005dfdb0)
- ブロック [`005dfdb0`](#insn-005dfdb0) 範囲 `[['005dfdb0', '005dfdb3']]`
  - `FALL_THROUGH` [`005dfdb0`](#insn-005dfdb0) → [`005dfdb4`](#insn-005dfdb4)
- ブロック [`005dfdb4`](#insn-005dfdb4) 範囲 `[['005dfdb4', '005dfdb7']]`
  - `FALL_THROUGH` [`005dfdb4`](#insn-005dfdb4) → [`005dfdb8`](#insn-005dfdb8)
- ブロック [`005dfdb8`](#insn-005dfdb8) 範囲 `[['005dfdb8', '005dfdbb']]`
  - `FALL_THROUGH` [`005dfdb8`](#insn-005dfdb8) → [`005dfdbc`](#insn-005dfdbc)
- ブロック [`005dfdbc`](#insn-005dfdbc) 範囲 `[['005dfdbc', '005dfdc3']]`
  - `FALL_THROUGH` [`005dfdc0`](#insn-005dfdc0) → [`005dfdc4`](#insn-005dfdc4)
- ブロック [`005dfdc4`](#insn-005dfdc4) 範囲 `[['005dfdc4', '005dfdc7']]`
  - `FALL_THROUGH` [`005dfdc4`](#insn-005dfdc4) → [`005dfdc8`](#insn-005dfdc8)
- ブロック [`005dfdc8`](#insn-005dfdc8) 範囲 `[['005dfdc8', '005dfdcb']]`
  - `FALL_THROUGH` [`005dfdc8`](#insn-005dfdc8) → [`005dfdcc`](#insn-005dfdcc)
- ブロック [`005dfdcc`](#insn-005dfdcc) 範囲 `[['005dfdcc', '005dfdfb']]`
  - `FALL_THROUGH` [`005dfdf8`](#insn-005dfdf8) → [`005dfdfc`](#insn-005dfdfc)
- ブロック [`005dfdfc`](#insn-005dfdfc) 範囲 `[['005dfdfc', '005dfebf']]`
  - `CONDITIONAL_JUMP` [`005dfebc`](#insn-005dfebc) → [`005dff38`](#insn-005dff38)
  - `FALL_THROUGH` [`005dfebc`](#insn-005dfebc) → [`005dfec0`](#insn-005dfec0)
- ブロック [`005dfec0`](#insn-005dfec0) 範囲 `[['005dfec0', '005dfec7']]`
  - `CONDITIONAL_JUMP` [`005dfec4`](#insn-005dfec4) → [`005dff48`](#insn-005dff48)
  - `FALL_THROUGH` [`005dfec4`](#insn-005dfec4) → [`005dfec8`](#insn-005dfec8)
- ブロック [`005dfec8`](#insn-005dfec8) 範囲 `[['005dfec8', '005dfecf']]`
  - `CONDITIONAL_JUMP` [`005dfecc`](#insn-005dfecc) → [`005dff58`](#insn-005dff58)
  - `FALL_THROUGH` [`005dfecc`](#insn-005dfecc) → [`005dfed0`](#insn-005dfed0)
- ブロック [`005dfed0`](#insn-005dfed0) 範囲 `[['005dfed0', '005dfed7']]`
  - `CONDITIONAL_JUMP` [`005dfed4`](#insn-005dfed4) → [`005dff68`](#insn-005dff68)
  - `FALL_THROUGH` [`005dfed4`](#insn-005dfed4) → [`005dfed8`](#insn-005dfed8)
- ブロック [`005dfed8`](#insn-005dfed8) 範囲 `[['005dfed8', '005dfedf']]`
  - `CONDITIONAL_JUMP` [`005dfedc`](#insn-005dfedc) → [`005dff78`](#insn-005dff78)
  - `FALL_THROUGH` [`005dfedc`](#insn-005dfedc) → [`005dfee0`](#insn-005dfee0)
- ブロック [`005dfee0`](#insn-005dfee0) 範囲 `[['005dfee0', '005dfee7']]`
  - `CONDITIONAL_JUMP` [`005dfee4`](#insn-005dfee4) → [`005dff88`](#insn-005dff88)
  - `FALL_THROUGH` [`005dfee4`](#insn-005dfee4) → [`005dfee8`](#insn-005dfee8)
- ブロック [`005dfee8`](#insn-005dfee8) 範囲 `[['005dfee8', '005dfeef']]`
  - `CONDITIONAL_JUMP` [`005dfeec`](#insn-005dfeec) → [`005dfef8`](#insn-005dfef8)
  - `FALL_THROUGH` [`005dfeec`](#insn-005dfeec) → [`005dfef0`](#insn-005dfef0)
- ブロック [`005dfef0`](#insn-005dfef0) 範囲 `[['005dfef0', '005dfef7']]`
  - `FALL_THROUGH` [`005dfef4`](#insn-005dfef4) → [`005dfef8`](#insn-005dfef8)
- ブロック [`005dfef8`](#insn-005dfef8) 範囲 `[['005dfef8', '005dff23']]`
  - `CONDITIONAL_JUMP` [`005dff20`](#insn-005dff20) → [`005e0068`](#insn-005e0068)
  - `FALL_THROUGH` [`005dff20`](#insn-005dff20) → [`005dff24`](#insn-005dff24)
- ブロック [`005dff24`](#insn-005dff24) 範囲 `[['005dff24', '005dff37']]`
- ブロック [`005dff38`](#insn-005dff38) 範囲 `[['005dff38', '005dff47']]`
  - `CONDITIONAL_JUMP` [`005dff44`](#insn-005dff44) → [`005dfec8`](#insn-005dfec8)
  - `FALL_THROUGH` [`005dff44`](#insn-005dff44) → [`005dff48`](#insn-005dff48)
- ブロック [`005dff48`](#insn-005dff48) 範囲 `[['005dff48', '005dff57']]`
  - `CONDITIONAL_JUMP` [`005dff54`](#insn-005dff54) → [`005dfed0`](#insn-005dfed0)
  - `FALL_THROUGH` [`005dff54`](#insn-005dff54) → [`005dff58`](#insn-005dff58)
- ブロック [`005dff58`](#insn-005dff58) 範囲 `[['005dff58', '005dff67']]`
  - `CONDITIONAL_JUMP` [`005dff64`](#insn-005dff64) → [`005dfed8`](#insn-005dfed8)
  - `FALL_THROUGH` [`005dff64`](#insn-005dff64) → [`005dff68`](#insn-005dff68)
- ブロック [`005dff68`](#insn-005dff68) 範囲 `[['005dff68', '005dff77']]`
  - `CONDITIONAL_JUMP` [`005dff74`](#insn-005dff74) → [`005dfee0`](#insn-005dfee0)
  - `FALL_THROUGH` [`005dff74`](#insn-005dff74) → [`005dff78`](#insn-005dff78)
- ブロック [`005dff78`](#insn-005dff78) 範囲 `[['005dff78', '005dff87']]`
  - `CONDITIONAL_JUMP` [`005dff84`](#insn-005dff84) → [`005dfee8`](#insn-005dfee8)
  - `FALL_THROUGH` [`005dff84`](#insn-005dff84) → [`005dff88`](#insn-005dff88)
- ブロック [`005dff88`](#insn-005dff88) 範囲 `[['005dff88', '005dff97']]`
  - `CONDITIONAL_JUMP` [`005dff94`](#insn-005dff94) → [`005dfef0`](#insn-005dfef0)
  - `FALL_THROUGH` [`005dff94`](#insn-005dff94) → [`005dff98`](#insn-005dff98)
- ブロック [`005dff98`](#insn-005dff98) 範囲 `[['005dff98', '005dff9b']]`
  - `UNCONDITIONAL_JUMP` [`005dff98`](#insn-005dff98) → [`005dfef8`](#insn-005dfef8)
- ブロック [`005e0068`](#insn-005e0068) 範囲 `[['005e0068', '005e006b']]`

## 命令位置別の参照

- [`005dfce0`](#insn-005dfce0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfce4`](#insn-005dfce4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfce8`](#insn-005dfce8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfd0c`](#insn-005dfd0c) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfd18`](#insn-005dfd18) → `002b7f26`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`005dfd20`](#insn-005dfd20) → `Stack[-0xff]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfd24`](#insn-005dfd24) → `Stack[-0xf8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfd34`](#insn-005dfd34) → `Stack[-0x10f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfd3c`](#insn-005dfd3c) → `002b7f39`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`005dfd40`](#insn-005dfd40) → `Stack[-0xdf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfd48`](#insn-005dfd48) → `Stack[-0xd8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfd58`](#insn-005dfd58) → `Stack[-0xef]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfd5c`](#insn-005dfd5c) → `002b8dc2`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`005dfd60`](#insn-005dfd60) → `Stack[-0xbf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfd68`](#insn-005dfd68) → `Stack[-0xb8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfd78`](#insn-005dfd78) → `Stack[-0xcf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfd7c`](#insn-005dfd7c) → `002a2f62`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`005dfd80`](#insn-005dfd80) → `Stack[-0x9f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfd88`](#insn-005dfd88) → `Stack[-0x98]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfd94`](#insn-005dfd94) → `Stack[-0xaf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfd98`](#insn-005dfd98) → `002ac5d2`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`005dfda0`](#insn-005dfda0) → `Stack[-0x7f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfda8`](#insn-005dfda8) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfdb4`](#insn-005dfdb4) → `Stack[-0x8f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfdb8`](#insn-005dfdb8) → `002a0f5d`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`005dfdc0`](#insn-005dfdc0) → `Stack[-0x5f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfdc8`](#insn-005dfdc8) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfdd4`](#insn-005dfdd4) → `Stack[-0x6f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfdd8`](#insn-005dfdd8) → `002a3f09`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`005dfddc`](#insn-005dfddc) → `Stack[-0x110]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfde0`](#insn-005dfde0) → `Stack[-0xf0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfde4`](#insn-005dfde4) → `Stack[-0xd0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfde8`](#insn-005dfde8) → `Stack[-0xb0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfdec`](#insn-005dfdec) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfdf0`](#insn-005dfdf0) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfdf4`](#insn-005dfdf4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfdfc`](#insn-005dfdfc) → `Stack[-0x118]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfe00`](#insn-005dfe00) → `Stack[-0xfd]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfe04`](#insn-005dfe04) → `Stack[-0xdd]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfe08`](#insn-005dfe08) → `Stack[-0xbd]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfe0c`](#insn-005dfe0c) → `Stack[-0x9d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfe10`](#insn-005dfe10) → `Stack[-0x7d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfe14`](#insn-005dfe14) → `Stack[-0x5d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfe18`](#insn-005dfe18) → `Stack[-0x3f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfe1c`](#insn-005dfe1c) → `Stack[-0x4f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfe20`](#insn-005dfe20) → `Stack[-0x3d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfe24`](#insn-005dfe24) → `00ca68e0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`005dfe28`](#insn-005dfe28) → `00ca68d8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`005dfe2c`](#insn-005dfe2c) → `00ca68d0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`005dfe2c`](#insn-005dfe2c) → `00ca68d8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`005dfe38`](#insn-005dfe38) → `00ca68d0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`005dfe3c`](#insn-005dfe3c) → [`0043b7f8`](../0043b/0043b7f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043b7f8` · 推定シンボル `None` · 推定型 `None`
- [`005dfe40`](#insn-005dfe40) → `00ca68d8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`005dfe4c`](#insn-005dfe4c) → `00ca68d0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`005dfe50`](#insn-005dfe50) → [`0043b7f8`](../0043b/0043b7f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043b7f8` · 推定シンボル `None` · 推定型 `None`
- [`005dfe54`](#insn-005dfe54) → `00ca68d8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`005dfe60`](#insn-005dfe60) → `00ca68d0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`005dfe64`](#insn-005dfe64) → [`0043b7f8`](../0043b/0043b7f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043b7f8` · 推定シンボル `None` · 推定型 `None`
- [`005dfe68`](#insn-005dfe68) → `00ca68d8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`005dfe74`](#insn-005dfe74) → `00ca68d0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`005dfe78`](#insn-005dfe78) → [`0043b7f8`](../0043b/0043b7f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043b7f8` · 推定シンボル `None` · 推定型 `None`
- [`005dfe7c`](#insn-005dfe7c) → `00ca68d8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`005dfe88`](#insn-005dfe88) → `00ca68d0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`005dfe8c`](#insn-005dfe8c) → [`0043b7f8`](../0043b/0043b7f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043b7f8` · 推定シンボル `None` · 推定型 `None`
- [`005dfe90`](#insn-005dfe90) → `00ca68d8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`005dfe9c`](#insn-005dfe9c) → `00ca68d0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`005dfea0`](#insn-005dfea0) → [`0043b7f8`](../0043b/0043b7f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043b7f8` · 推定シンボル `None` · 推定型 `None`
- [`005dfea4`](#insn-005dfea4) → `00ca68d8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`005dfeb0`](#insn-005dfeb0) → `00ca68d0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`005dfeb4`](#insn-005dfeb4) → [`0043b7f8`](../0043b/0043b7f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043b7f8` · 推定シンボル `None` · 推定型 `None`
- [`005dfeb8`](#insn-005dfeb8) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfebc`](#insn-005dfebc) → [`005dff38`](#insn-005dff38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfec0`](#insn-005dfec0) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfec4`](#insn-005dfec4) → [`005dff48`](#insn-005dff48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfec8`](#insn-005dfec8) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfecc`](#insn-005dfecc) → [`005dff58`](#insn-005dff58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfed0`](#insn-005dfed0) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfed4`](#insn-005dfed4) → [`005dff68`](#insn-005dff68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfed8`](#insn-005dfed8) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfedc`](#insn-005dfedc) → [`005dff78`](#insn-005dff78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfee0`](#insn-005dfee0) → `Stack[-0xf0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfee4`](#insn-005dfee4) → [`005dff88`](#insn-005dff88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfee8`](#insn-005dfee8) → `Stack[-0x110]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfeec`](#insn-005dfeec) → [`005dfef8`](#insn-005dfef8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfef0`](#insn-005dfef0) → `Stack[-0x100]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfef4`](#insn-005dfef4) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`005dfefc`](#insn-005dfefc) → [`0043ae70`](../0043a/0043ae70.md) · `PARAM` · `ANALYSIS` · 関数 `0043ae70` · 推定シンボル `None` · 推定型 `None`
- [`005dff04`](#insn-005dff04) → `00ca68d0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`005dff0c`](#insn-005dff0c) → `00c62f90`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`005dff10`](#insn-005dff10) → [`00c57e30`](../00c57/00c57e30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e30` · 推定シンボル `None` · 推定型 `None`
- [`005dff18`](#insn-005dff18) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dff20`](#insn-005dff20) → [`005e0068`](#insn-005e0068) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dff24`](#insn-005dff24) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dff28`](#insn-005dff28) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dff2c`](#insn-005dff2c) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dff38`](#insn-005dff38) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dff3c`](#insn-005dff3c) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`005dff40`](#insn-005dff40) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dff44`](#insn-005dff44) → [`005dfec8`](#insn-005dfec8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dff48`](#insn-005dff48) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dff4c`](#insn-005dff4c) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`005dff50`](#insn-005dff50) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dff54`](#insn-005dff54) → [`005dfed0`](#insn-005dfed0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dff58`](#insn-005dff58) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dff5c`](#insn-005dff5c) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`005dff60`](#insn-005dff60) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dff64`](#insn-005dff64) → [`005dfed8`](#insn-005dfed8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dff68`](#insn-005dff68) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dff6c`](#insn-005dff6c) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`005dff70`](#insn-005dff70) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dff74`](#insn-005dff74) → [`005dfee0`](#insn-005dfee0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dff78`](#insn-005dff78) → `Stack[-0xc0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dff7c`](#insn-005dff7c) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`005dff80`](#insn-005dff80) → `Stack[-0xf0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dff84`](#insn-005dff84) → [`005dfee8`](#insn-005dfee8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dff88`](#insn-005dff88) → `Stack[-0xe0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dff8c`](#insn-005dff8c) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`005dff90`](#insn-005dff90) → `Stack[-0x110]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dff94`](#insn-005dff94) → [`005dfef0`](#insn-005dfef0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dff98`](#insn-005dff98) → [`005dfef8`](#insn-005dfef8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005e0068`](#insn-005e0068) → [`00c57ee0`](../00c57/00c57ee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ee0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`005dfce0`](#insn-005dfce0)

~~~json
{
  "source": "005dfce0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfce4`](#insn-005dfce4)

~~~json
{
  "source": "005dfce4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfce8`](#insn-005dfce8)

~~~json
{
  "source": "005dfce8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfd0c`](#insn-005dfd0c)

~~~json
{
  "source": "005dfd0c",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfd18`](#insn-005dfd18)

~~~json
{
  "source": "005dfd18",
  "target": "002b7f26",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b7f26",
  "offset": 0,
  "size": 19,
  "datatype": "string",
  "bytes": "43676b496a4d33795f5a516145414951416700",
  "capture_start": "002b7f26",
  "capture_bytes": 19,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`005dfd20`](#insn-005dfd20)

~~~json
{
  "source": "005dfd20",
  "target": "Stack[-0xff]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfd24`](#insn-005dfd24)

~~~json
{
  "source": "005dfd24",
  "target": "Stack[-0xf8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfd34`](#insn-005dfd34)

~~~json
{
  "source": "005dfd34",
  "target": "Stack[-0x10f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfd3c`](#insn-005dfd3c)

~~~json
{
  "source": "005dfd3c",
  "target": "002b7f39",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b7f39",
  "offset": 0,
  "size": 19,
  "datatype": "string",
  "bytes": "43676b496a4d33795f5a516145414951424100",
  "capture_start": "002b7f39",
  "capture_bytes": 19,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`005dfd40`](#insn-005dfd40)

~~~json
{
  "source": "005dfd40",
  "target": "Stack[-0xdf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfd48`](#insn-005dfd48)

~~~json
{
  "source": "005dfd48",
  "target": "Stack[-0xd8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfd58`](#insn-005dfd58)

~~~json
{
  "source": "005dfd58",
  "target": "Stack[-0xef]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfd5c`](#insn-005dfd5c)

~~~json
{
  "source": "005dfd5c",
  "target": "002b8dc2",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b8dc2",
  "offset": 0,
  "size": 19,
  "datatype": "string",
  "bytes": "43676b496a4d33795f5a516145414951426700",
  "capture_start": "002b8dc2",
  "capture_bytes": 19,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`005dfd60`](#insn-005dfd60)

~~~json
{
  "source": "005dfd60",
  "target": "Stack[-0xbf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfd68`](#insn-005dfd68)

~~~json
{
  "source": "005dfd68",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfd78`](#insn-005dfd78)

~~~json
{
  "source": "005dfd78",
  "target": "Stack[-0xcf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfd7c`](#insn-005dfd7c)

~~~json
{
  "source": "005dfd7c",
  "target": "002a2f62",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a2f62",
  "offset": 0,
  "size": 19,
  "datatype": "string",
  "bytes": "43676b496a4d33795f5a516145414951417700",
  "capture_start": "002a2f62",
  "capture_bytes": 19,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`005dfd80`](#insn-005dfd80)

~~~json
{
  "source": "005dfd80",
  "target": "Stack[-0x9f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfd88`](#insn-005dfd88)

~~~json
{
  "source": "005dfd88",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfd94`](#insn-005dfd94)

~~~json
{
  "source": "005dfd94",
  "target": "Stack[-0xaf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfd98`](#insn-005dfd98)

~~~json
{
  "source": "005dfd98",
  "target": "002ac5d2",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002ac5d2",
  "offset": 0,
  "size": 19,
  "datatype": "string",
  "bytes": "43676b496a4d33795f5a516145414951425100",
  "capture_start": "002ac5d2",
  "capture_bytes": 19,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`005dfda0`](#insn-005dfda0)

~~~json
{
  "source": "005dfda0",
  "target": "Stack[-0x7f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfda8`](#insn-005dfda8)

~~~json
{
  "source": "005dfda8",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfdb4`](#insn-005dfdb4)

~~~json
{
  "source": "005dfdb4",
  "target": "Stack[-0x8f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfdb8`](#insn-005dfdb8)

~~~json
{
  "source": "005dfdb8",
  "target": "002a0f5d",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a0f5d",
  "offset": 0,
  "size": 19,
  "datatype": "string",
  "bytes": "43676b496a4d33795f5a516145414951427700",
  "capture_start": "002a0f5d",
  "capture_bytes": 19,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`005dfdc0`](#insn-005dfdc0)

~~~json
{
  "source": "005dfdc0",
  "target": "Stack[-0x5f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfdc8`](#insn-005dfdc8)

~~~json
{
  "source": "005dfdc8",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfdd4`](#insn-005dfdd4)

~~~json
{
  "source": "005dfdd4",
  "target": "Stack[-0x6f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfdd8`](#insn-005dfdd8)

~~~json
{
  "source": "005dfdd8",
  "target": "002a3f09",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a3f09",
  "offset": 0,
  "size": 19,
  "datatype": "string",
  "bytes": "43676b496a4d33795f5a516145414951434100",
  "capture_start": "002a3f09",
  "capture_bytes": 19,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`005dfddc`](#insn-005dfddc)

~~~json
{
  "source": "005dfddc",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfde0`](#insn-005dfde0)

~~~json
{
  "source": "005dfde0",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfde4`](#insn-005dfde4)

~~~json
{
  "source": "005dfde4",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfde8`](#insn-005dfde8)

~~~json
{
  "source": "005dfde8",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfdec`](#insn-005dfdec)

~~~json
{
  "source": "005dfdec",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfdf0`](#insn-005dfdf0)

~~~json
{
  "source": "005dfdf0",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfdf4`](#insn-005dfdf4)

~~~json
{
  "source": "005dfdf4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfdfc`](#insn-005dfdfc)

~~~json
{
  "source": "005dfdfc",
  "target": "Stack[-0x118]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfe00`](#insn-005dfe00)

~~~json
{
  "source": "005dfe00",
  "target": "Stack[-0xfd]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfe04`](#insn-005dfe04)

~~~json
{
  "source": "005dfe04",
  "target": "Stack[-0xdd]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfe08`](#insn-005dfe08)

~~~json
{
  "source": "005dfe08",
  "target": "Stack[-0xbd]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfe0c`](#insn-005dfe0c)

~~~json
{
  "source": "005dfe0c",
  "target": "Stack[-0x9d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfe10`](#insn-005dfe10)

~~~json
{
  "source": "005dfe10",
  "target": "Stack[-0x7d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfe14`](#insn-005dfe14)

~~~json
{
  "source": "005dfe14",
  "target": "Stack[-0x5d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfe18`](#insn-005dfe18)

~~~json
{
  "source": "005dfe18",
  "target": "Stack[-0x3f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfe1c`](#insn-005dfe1c)

~~~json
{
  "source": "005dfe1c",
  "target": "Stack[-0x4f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfe20`](#insn-005dfe20)

~~~json
{
  "source": "005dfe20",
  "target": "Stack[-0x3d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfe24`](#insn-005dfe24)

~~~json
{
  "source": "005dfe24",
  "target": "00ca68e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca68e0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`005dfe28`](#insn-005dfe28)

~~~json
{
  "source": "005dfe28",
  "target": "00ca68d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca68d8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`005dfe2c`](#insn-005dfe2c)

~~~json
{
  "source": "005dfe2c",
  "target": "00ca68d0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca68d0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`005dfe2c`](#insn-005dfe2c)

~~~json
{
  "source": "005dfe2c",
  "target": "00ca68d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca68d8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`005dfe38`](#insn-005dfe38)

~~~json
{
  "source": "005dfe38",
  "target": "00ca68d0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca68d0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`005dfe3c`](#insn-005dfe3c)

~~~json
{
  "source": "005dfe3c",
  "target": "0043b7f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005dfe40`](#insn-005dfe40)

~~~json
{
  "source": "005dfe40",
  "target": "00ca68d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca68d8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`005dfe4c`](#insn-005dfe4c)

~~~json
{
  "source": "005dfe4c",
  "target": "00ca68d0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca68d0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`005dfe50`](#insn-005dfe50)

~~~json
{
  "source": "005dfe50",
  "target": "0043b7f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005dfe54`](#insn-005dfe54)

~~~json
{
  "source": "005dfe54",
  "target": "00ca68d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca68d8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`005dfe60`](#insn-005dfe60)

~~~json
{
  "source": "005dfe60",
  "target": "00ca68d0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca68d0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`005dfe64`](#insn-005dfe64)

~~~json
{
  "source": "005dfe64",
  "target": "0043b7f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005dfe68`](#insn-005dfe68)

~~~json
{
  "source": "005dfe68",
  "target": "00ca68d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca68d8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`005dfe74`](#insn-005dfe74)

~~~json
{
  "source": "005dfe74",
  "target": "00ca68d0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca68d0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`005dfe78`](#insn-005dfe78)

~~~json
{
  "source": "005dfe78",
  "target": "0043b7f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005dfe7c`](#insn-005dfe7c)

~~~json
{
  "source": "005dfe7c",
  "target": "00ca68d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca68d8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`005dfe88`](#insn-005dfe88)

~~~json
{
  "source": "005dfe88",
  "target": "00ca68d0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca68d0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`005dfe8c`](#insn-005dfe8c)

~~~json
{
  "source": "005dfe8c",
  "target": "0043b7f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005dfe90`](#insn-005dfe90)

~~~json
{
  "source": "005dfe90",
  "target": "00ca68d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca68d8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`005dfe9c`](#insn-005dfe9c)

~~~json
{
  "source": "005dfe9c",
  "target": "00ca68d0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca68d0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`005dfea0`](#insn-005dfea0)

~~~json
{
  "source": "005dfea0",
  "target": "0043b7f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005dfea4`](#insn-005dfea4)

~~~json
{
  "source": "005dfea4",
  "target": "00ca68d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca68d8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`005dfeb0`](#insn-005dfeb0)

~~~json
{
  "source": "005dfeb0",
  "target": "00ca68d0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca68d0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`005dfeb4`](#insn-005dfeb4)

~~~json
{
  "source": "005dfeb4",
  "target": "0043b7f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005dfeb8`](#insn-005dfeb8)

~~~json
{
  "source": "005dfeb8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfebc`](#insn-005dfebc)

~~~json
{
  "source": "005dfebc",
  "target": "005dff38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfec0`](#insn-005dfec0)

~~~json
{
  "source": "005dfec0",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfec4`](#insn-005dfec4)

~~~json
{
  "source": "005dfec4",
  "target": "005dff48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfec8`](#insn-005dfec8)

~~~json
{
  "source": "005dfec8",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfecc`](#insn-005dfecc)

~~~json
{
  "source": "005dfecc",
  "target": "005dff58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfed0`](#insn-005dfed0)

~~~json
{
  "source": "005dfed0",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfed4`](#insn-005dfed4)

~~~json
{
  "source": "005dfed4",
  "target": "005dff68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfed8`](#insn-005dfed8)

~~~json
{
  "source": "005dfed8",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfedc`](#insn-005dfedc)

~~~json
{
  "source": "005dfedc",
  "target": "005dff78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfee0`](#insn-005dfee0)

~~~json
{
  "source": "005dfee0",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfee4`](#insn-005dfee4)

~~~json
{
  "source": "005dfee4",
  "target": "005dff88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfee8`](#insn-005dfee8)

~~~json
{
  "source": "005dfee8",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfeec`](#insn-005dfeec)

~~~json
{
  "source": "005dfeec",
  "target": "005dfef8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfef0`](#insn-005dfef0)

~~~json
{
  "source": "005dfef0",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfef4`](#insn-005dfef4)

~~~json
{
  "source": "005dfef4",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005dfefc`](#insn-005dfefc)

~~~json
{
  "source": "005dfefc",
  "target": "0043ae70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005dff04`](#insn-005dff04)

~~~json
{
  "source": "005dff04",
  "target": "00ca68d0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca68d0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`005dff0c`](#insn-005dff0c)

~~~json
{
  "source": "005dff0c",
  "target": "00c62f90",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c62f90",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`005dff10`](#insn-005dff10)

~~~json
{
  "source": "005dff10",
  "target": "00c57e30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005dff18`](#insn-005dff18)

~~~json
{
  "source": "005dff18",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dff20`](#insn-005dff20)

~~~json
{
  "source": "005dff20",
  "target": "005e0068",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dff24`](#insn-005dff24)

~~~json
{
  "source": "005dff24",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dff28`](#insn-005dff28)

~~~json
{
  "source": "005dff28",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dff2c`](#insn-005dff2c)

~~~json
{
  "source": "005dff2c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dff38`](#insn-005dff38)

~~~json
{
  "source": "005dff38",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dff3c`](#insn-005dff3c)

~~~json
{
  "source": "005dff3c",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005dff40`](#insn-005dff40)

~~~json
{
  "source": "005dff40",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dff44`](#insn-005dff44)

~~~json
{
  "source": "005dff44",
  "target": "005dfec8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dff48`](#insn-005dff48)

~~~json
{
  "source": "005dff48",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dff4c`](#insn-005dff4c)

~~~json
{
  "source": "005dff4c",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005dff50`](#insn-005dff50)

~~~json
{
  "source": "005dff50",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dff54`](#insn-005dff54)

~~~json
{
  "source": "005dff54",
  "target": "005dfed0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dff58`](#insn-005dff58)

~~~json
{
  "source": "005dff58",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dff5c`](#insn-005dff5c)

~~~json
{
  "source": "005dff5c",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005dff60`](#insn-005dff60)

~~~json
{
  "source": "005dff60",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dff64`](#insn-005dff64)

~~~json
{
  "source": "005dff64",
  "target": "005dfed8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dff68`](#insn-005dff68)

~~~json
{
  "source": "005dff68",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dff6c`](#insn-005dff6c)

~~~json
{
  "source": "005dff6c",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005dff70`](#insn-005dff70)

~~~json
{
  "source": "005dff70",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dff74`](#insn-005dff74)

~~~json
{
  "source": "005dff74",
  "target": "005dfee0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dff78`](#insn-005dff78)

~~~json
{
  "source": "005dff78",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dff7c`](#insn-005dff7c)

~~~json
{
  "source": "005dff7c",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005dff80`](#insn-005dff80)

~~~json
{
  "source": "005dff80",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dff84`](#insn-005dff84)

~~~json
{
  "source": "005dff84",
  "target": "005dfee8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dff88`](#insn-005dff88)

~~~json
{
  "source": "005dff88",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dff8c`](#insn-005dff8c)

~~~json
{
  "source": "005dff8c",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005dff90`](#insn-005dff90)

~~~json
{
  "source": "005dff90",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dff94`](#insn-005dff94)

~~~json
{
  "source": "005dff94",
  "target": "005dfef0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dff98`](#insn-005dff98)

~~~json
{
  "source": "005dff98",
  "target": "005dfef8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005e0068`](#insn-005e0068)

~~~json
{
  "source": "005e0068",
  "target": "00c57ee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
