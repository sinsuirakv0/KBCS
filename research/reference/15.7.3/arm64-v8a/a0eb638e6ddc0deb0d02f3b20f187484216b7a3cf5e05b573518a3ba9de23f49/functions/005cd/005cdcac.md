# 005cdcac

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `005cdcac`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005cd/005cdcac.md) · 移動量 `+0x0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0024.md#compare-812b1e26a90c072dafe1919303f0a04b)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `005cdcac`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005cd/005cdcac.md) · 移動量 `+0x0`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0024.md#compare-016676cedddff6a33f58ae16d07d306d)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "005cdcac",
  "name": "_INIT_72",
  "size": 708,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "fe5dc6d6702f4021ac542a59a43bc2081754ac9305d46340ed53f76e302bc88d",
  "source_text_sha256": "fe5dc6d6702f4021ac542a59a43bc2081754ac9305d46340ed53f76e302bc88d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "005cdcac",
        "005cdf6b"
      ],
      [
        "005ce038",
        "005ce03b"
      ]
    ],
    "bytes_sha256": "d913d411a2b405f026e7dae6fc2031b679c279cfb7d5d1a0254b90b256be8759",
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

## 疑似コード / UTF-8 5124 bytes

~~~c

/* WARNING: Type propagation algorithm not settling */

void _INIT_72(void)

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
  uStack_47 = (undefined7)s_CgkIjM3y_ZQaEAIQCA_002945b3._8_8_;
  cStack_40 = SUB81(s_CgkIjM3y_ZQaEAIQCA_002945b3._8_8_,7);
  local_4f = (char  [8])s_CgkIjM3y_ZQaEAIQCA_002945b3._0_8_;
  uStack_3d = 0;
  DAT_00c26a78 = 0;
  DAT_00c26a70 = 0;
  DAT_00c26a68 = &DAT_00c26a70;
  FUN_00418cb8(&DAT_00c26a68,&DAT_00c26a70,local_118,local_118);
  FUN_00418cb8(&DAT_00c26a68,&DAT_00c26a70,local_f8,local_f8);
  FUN_00418cb8(&DAT_00c26a68,&DAT_00c26a70,local_d8,local_d8);
  FUN_00418cb8(&DAT_00c26a68,&DAT_00c26a70,local_b8,local_b8);
  FUN_00418cb8(&DAT_00c26a68,&DAT_00c26a70,local_98,local_98);
  FUN_00418cb8(&DAT_00c26a68,&DAT_00c26a70,local_78,local_78);
  FUN_00418cb8(&DAT_00c26a68,&DAT_00c26a70,local_58,local_58);
  if ((local_50 & 1) != 0) {
    _ZdlPv((void *)CONCAT44(uStack_3c,CONCAT13(uStack_3d,CONCAT21(uStack_3f,cStack_40))));
  }
  if ((local_70 & 1) != 0) {
    _ZdlPv((void *)CONCAT44(uStack_5c,CONCAT13(uStack_5d,CONCAT21(uStack_5f,cStack_60))));
                    /* try { // try from 005cdf20 to 006cdf73 has its CatchHandler @ 005cdf20
                       catch() { ... } // from try @ 005cdf20 with catch @ 005cdf20
                       catch() { ... } // from try @ 005cdf84 with catch @ 005cdf20 */
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
  __cxa_atexit(FUN_00418330,&DAT_00c26a68,&PTR_LOOP_00be5f80);
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
<a id="insn-005cdcac"></a> `005cdcac` | `ff 83 04 d1` | sub sp,sp,#0x120 | `FALL_THROUGH`
<a id="insn-005cdcb0"></a> `005cdcb0` | `fd 7b 0f a9` | stp x29,x30,[sp, #0xf0] | `FALL_THROUGH`
<a id="insn-005cdcb4"></a> `005cdcb4` | `fc 57 10 a9` | stp x28,x21,[sp, #0x100] | `FALL_THROUGH`
<a id="insn-005cdcb8"></a> `005cdcb8` | `f4 4f 11 a9` | stp x20,x19,[sp, #0x110] | `FALL_THROUGH`
<a id="insn-005cdcbc"></a> `005cdcbc` | `fd c3 03 91` | add x29,sp,#0xf0 | `FALL_THROUGH`
<a id="insn-005cdcc0"></a> `005cdcc0` | `55 d0 3b d5` | mrs x21,tpidr_el0 | `FALL_THROUGH`
<a id="insn-005cdcc4"></a> `005cdcc4` | `2a e8 8c 52` | mov w10,#0x6741 | `FALL_THROUGH`
<a id="insn-005cdcc8"></a> `005cdcc8` | `f4 23 00 91` | add x20,sp,#0x8 | `FALL_THROUGH`
<a id="insn-005cdccc"></a> `005cdccc` | `a9 16 40 f9` | ldr x9,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-005cdcd0"></a> `005cdcd0` | `88 04 80 52` | mov w8,#0x24 | `FALL_THROUGH`
<a id="insn-005cdcd4"></a> `005cdcd4` | `d3 32 00 b0` | adrp x19,0xc26000 | `FALL_THROUGH`
<a id="insn-005cdcd8"></a> `005cdcd8` | `73 a2 29 91` | add x19,x19,#0xa68 | `FALL_THROUGH`
<a id="insn-005cdcdc"></a> `005cdcdc` | `a9 83 1f f8` | stur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-005cdce0"></a> `005cdce0` | `c9 e6 ff d0` | adrp x9,0x2a7000 | `FALL_THROUGH`
<a id="insn-005cdce4"></a> `005cdce4` | `29 75 0b 91` | add x9,x9,#0x2dd | `FALL_THROUGH`
<a id="insn-005cdce8"></a> `005cdce8` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-005cdcec"></a> `005cdcec` | `29 00 80 52` | mov w9,#0x1 | `FALL_THROUGH`
<a id="insn-005cdcf0"></a> `005cdcf0` | `ea 13 02 78` | sturh w10,[sp, #0x21] | `FALL_THROUGH`
<a id="insn-005cdcf4"></a> `005cdcf4` | `e9 2b 00 b9` | str w9,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-005cdcf8"></a> `005cdcf8` | `49 28 88 52` | mov w9,#0x4142 | `FALL_THROUGH`
<a id="insn-005cdcfc"></a> `005cdcfc` | `ca e6 ff d0` | adrp x10,0x2a7000 | `FALL_THROUGH`
<a id="insn-005cdd00"></a> `005cdd00` | `4a c1 0b 91` | add x10,x10,#0x2f0 | `FALL_THROUGH`
<a id="insn-005cdd04"></a> `005cdd04` | `e0 13 81 3c` | stur q0,[sp, #0x11] | `FALL_THROUGH`
<a id="insn-005cdd08"></a> `005cdd08` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-005cdd0c"></a> `005cdd0c` | `40 01 c0 3d` | ldr q0,[x10] | `FALL_THROUGH`
<a id="insn-005cdd10"></a> `005cdd10` | `e9 13 04 78` | sturh w9,[sp, #0x41] | `FALL_THROUGH`
<a id="insn-005cdd14"></a> `005cdd14` | `49 00 80 52` | mov w9,#0x2 | `FALL_THROUGH`
<a id="insn-005cdd18"></a> `005cdd18` | `e9 4b 00 b9` | str w9,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-005cdd1c"></a> `005cdd1c` | `49 e8 8c 52` | mov w9,#0x6742 | `FALL_THROUGH`
<a id="insn-005cdd20"></a> `005cdd20` | `ca e6 ff f0` | adrp x10,0x2a8000 | `FALL_THROUGH`
<a id="insn-005cdd24"></a> `005cdd24` | `4a 19 01 91` | add x10,x10,#0x46 | `FALL_THROUGH`
<a id="insn-005cdd28"></a> `005cdd28` | `e0 13 83 3c` | stur q0,[sp, #0x31] | `FALL_THROUGH`
<a id="insn-005cdd2c"></a> `005cdd2c` | `40 01 c0 3d` | ldr q0,[x10] | `FALL_THROUGH`
<a id="insn-005cdd30"></a> `005cdd30` | `e9 13 06 78` | sturh w9,[sp, #0x61] | `FALL_THROUGH`
<a id="insn-005cdd34"></a> `005cdd34` | `69 00 80 52` | mov w9,#0x3 | `FALL_THROUGH`
<a id="insn-005cdd38"></a> `005cdd38` | `e9 6b 00 b9` | str w9,[sp, #0x68] | `FALL_THROUGH`
<a id="insn-005cdd3c"></a> `005cdd3c` | `29 e8 8e 52` | mov w9,#0x7741 | `FALL_THROUGH`
<a id="insn-005cdd40"></a> `005cdd40` | `2a e6 ff d0` | adrp x10,0x293000 | `FALL_THROUGH`
<a id="insn-005cdd44"></a> `005cdd44` | `4a ed 1c 91` | add x10,x10,#0x73b | `FALL_THROUGH`
<a id="insn-005cdd48"></a> `005cdd48` | `e0 13 85 3c` | stur q0,[sp, #0x51] | `FALL_THROUGH`
<a id="insn-005cdd4c"></a> `005cdd4c` | `40 01 c0 3d` | ldr q0,[x10] | `FALL_THROUGH`
<a id="insn-005cdd50"></a> `005cdd50` | `e9 13 08 78` | sturh w9,[sp, #0x81] | `FALL_THROUGH`
<a id="insn-005cdd54"></a> `005cdd54` | `89 00 80 52` | mov w9,#0x4 | `FALL_THROUGH`
<a id="insn-005cdd58"></a> `005cdd58` | `e9 8b 00 b9` | str w9,[sp, #0x88] | `FALL_THROUGH`
<a id="insn-005cdd5c"></a> `005cdd5c` | `69 e6 ff f0` | adrp x9,0x29c000 | `FALL_THROUGH`
<a id="insn-005cdd60"></a> `005cdd60` | `29 b9 0d 91` | add x9,x9,#0x36e | `FALL_THROUGH`
<a id="insn-005cdd64"></a> `005cdd64` | `e0 13 87 3c` | stur q0,[sp, #0x71] | `FALL_THROUGH`
<a id="insn-005cdd68"></a> `005cdd68` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-005cdd6c"></a> `005cdd6c` | `49 28 8a 52` | mov w9,#0x5142 | `FALL_THROUGH`
<a id="insn-005cdd70"></a> `005cdd70` | `89 92 09 78` | sturh w9,[x20, #0x99] | `FALL_THROUGH`
<a id="insn-005cdd74"></a> `005cdd74` | `a9 00 80 52` | mov w9,#0x5 | `FALL_THROUGH`
<a id="insn-005cdd78"></a> `005cdd78` | `e9 ab 00 b9` | str w9,[sp, #0xa8] | `FALL_THROUGH`
<a id="insn-005cdd7c"></a> `005cdd7c` | `29 e6 ff 90` | adrp x9,0x291000 | `FALL_THROUGH`
<a id="insn-005cdd80"></a> `005cdd80` | `29 dd 21 91` | add x9,x9,#0x877 | `FALL_THROUGH`
<a id="insn-005cdd84"></a> `005cdd84` | `80 92 88 3c` | stur q0,[x20, #0x89] | `FALL_THROUGH`
<a id="insn-005cdd88"></a> `005cdd88` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-005cdd8c"></a> `005cdd8c` | `49 e8 8e 52` | mov w9,#0x7742 | `FALL_THROUGH`
<a id="insn-005cdd90"></a> `005cdd90` | `89 92 0b 78` | sturh w9,[x20, #0xb9] | `FALL_THROUGH`
<a id="insn-005cdd94"></a> `005cdd94` | `c9 00 80 52` | mov w9,#0x6 | `FALL_THROUGH`
<a id="insn-005cdd98"></a> `005cdd98` | `e9 cb 00 b9` | str w9,[sp, #0xc8] | `FALL_THROUGH`
<a id="insn-005cdd9c"></a> `005cdd9c` | `29 e6 ff f0` | adrp x9,0x294000 | `FALL_THROUGH`
<a id="insn-005cdda0"></a> `005cdda0` | `29 cd 16 91` | add x9,x9,#0x5b3 | `FALL_THROUGH`
<a id="insn-005cdda4"></a> `005cdda4` | `80 92 8a 3c` | stur q0,[x20, #0xa9] | `FALL_THROUGH`
<a id="insn-005cdda8"></a> `005cdda8` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-005cddac"></a> `005cddac` | `e8 43 00 39` | strb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-005cddb0"></a> `005cddb0` | `e8 c3 00 39` | strb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-005cddb4"></a> `005cddb4` | `e8 43 01 39` | strb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-005cddb8"></a> `005cddb8` | `e8 c3 01 39` | strb w8,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-005cddbc"></a> `005cddbc` | `e8 43 02 39` | strb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-005cddc0"></a> `005cddc0` | `e8 c3 02 39` | strb w8,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-005cddc4"></a> `005cddc4` | `e8 43 03 39` | strb w8,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-005cddc8"></a> `005cddc8` | `68 28 88 52` | mov w8,#0x4143 | `FALL_THROUGH`
<a id="insn-005cddcc"></a> `005cddcc` | `ff 0b 00 b9` | str wzr,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-005cddd0"></a> `005cddd0` | `ff 8f 00 39` | strb wzr,[sp, #0x23] | `FALL_THROUGH`
<a id="insn-005cddd4"></a> `005cddd4` | `ff 0f 01 39` | strb wzr,[sp, #0x43] | `FALL_THROUGH`
<a id="insn-005cddd8"></a> `005cddd8` | `ff 8f 01 39` | strb wzr,[sp, #0x63] | `FALL_THROUGH`
<a id="insn-005cdddc"></a> `005cdddc` | `ff 0f 02 39` | strb wzr,[sp, #0x83] | `FALL_THROUGH`
<a id="insn-005cdde0"></a> `005cdde0` | `ff 8f 02 39` | strb wzr,[sp, #0xa3] | `FALL_THROUGH`
<a id="insn-005cdde4"></a> `005cdde4` | `ff 0f 03 39` | strb wzr,[sp, #0xc3] | `FALL_THROUGH`
<a id="insn-005cdde8"></a> `005cdde8` | `88 92 0d 78` | sturh w8,[x20, #0xd9] | `FALL_THROUGH`
<a id="insn-005cddec"></a> `005cddec` | `80 92 8c 3c` | stur q0,[x20, #0xc9] | `FALL_THROUGH`
<a id="insn-005cddf0"></a> `005cddf0` | `ff 8f 03 39` | strb wzr,[sp, #0xe3] | `FALL_THROUGH`
<a id="insn-005cddf4"></a> `005cddf4` | `7f 0a 00 f9` | str xzr,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-005cddf8"></a> `005cddf8` | `3f 8c 00 f8` | str xzr,[x1, #0x8]! | `FALL_THROUGH`
<a id="insn-005cddfc"></a> `005cddfc` | `61 02 00 f9` | str x1,[x19] | `FALL_THROUGH`
<a id="insn-005cde00"></a> `005cde00` | `e2 23 00 91` | add x2,sp,#0x8 | `FALL_THROUGH`
<a id="insn-005cde04"></a> `005cde04` | `e3 23 00 91` | add x3,sp,#0x8 | `FALL_THROUGH`
<a id="insn-005cde08"></a> `005cde08` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-005cde0c"></a> `005cde0c` | `ab 2b f9 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-005cde10"></a> `005cde10` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-005cde14"></a> `005cde14` | `82 82 00 91` | add x2,x20,#0x20 | `FALL_THROUGH`
<a id="insn-005cde18"></a> `005cde18` | `83 82 00 91` | add x3,x20,#0x20 | `FALL_THROUGH`
<a id="insn-005cde1c"></a> `005cde1c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-005cde20"></a> `005cde20` | `a6 2b f9 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-005cde24"></a> `005cde24` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-005cde28"></a> `005cde28` | `82 02 01 91` | add x2,x20,#0x40 | `FALL_THROUGH`
<a id="insn-005cde2c"></a> `005cde2c` | `83 02 01 91` | add x3,x20,#0x40 | `FALL_THROUGH`
<a id="insn-005cde30"></a> `005cde30` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-005cde34"></a> `005cde34` | `a1 2b f9 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-005cde38"></a> `005cde38` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-005cde3c"></a> `005cde3c` | `82 82 01 91` | add x2,x20,#0x60 | `FALL_THROUGH`
<a id="insn-005cde40"></a> `005cde40` | `83 82 01 91` | add x3,x20,#0x60 | `FALL_THROUGH`
<a id="insn-005cde44"></a> `005cde44` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-005cde48"></a> `005cde48` | `9c 2b f9 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-005cde4c"></a> `005cde4c` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-005cde50"></a> `005cde50` | `82 02 02 91` | add x2,x20,#0x80 | `FALL_THROUGH`
<a id="insn-005cde54"></a> `005cde54` | `83 02 02 91` | add x3,x20,#0x80 | `FALL_THROUGH`
<a id="insn-005cde58"></a> `005cde58` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-005cde5c"></a> `005cde5c` | `97 2b f9 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-005cde60"></a> `005cde60` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-005cde64"></a> `005cde64` | `82 82 02 91` | add x2,x20,#0xa0 | `FALL_THROUGH`
<a id="insn-005cde68"></a> `005cde68` | `83 82 02 91` | add x3,x20,#0xa0 | `FALL_THROUGH`
<a id="insn-005cde6c"></a> `005cde6c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-005cde70"></a> `005cde70` | `92 2b f9 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-005cde74"></a> `005cde74` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-005cde78"></a> `005cde78` | `82 02 03 91` | add x2,x20,#0xc0 | `FALL_THROUGH`
<a id="insn-005cde7c"></a> `005cde7c` | `83 02 03 91` | add x3,x20,#0xc0 | `FALL_THROUGH`
<a id="insn-005cde80"></a> `005cde80` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-005cde84"></a> `005cde84` | `8d 2b f9 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-005cde88"></a> `005cde88` | `e8 43 43 39` | ldrb w8,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-005cde8c"></a> `005cde8c` | `e8 03 00 37` | tbnz w8,#0x0,0x005cdf08 | `CONDITIONAL_JUMP`
<a id="insn-005cde90"></a> `005cde90` | `e8 c3 42 39` | ldrb w8,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-005cde94"></a> `005cde94` | `28 04 00 37` | tbnz w8,#0x0,0x005cdf18 | `CONDITIONAL_JUMP`
<a id="insn-005cde98"></a> `005cde98` | `e8 43 42 39` | ldrb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-005cde9c"></a> `005cde9c` | `68 04 00 37` | tbnz w8,#0x0,0x005cdf28 | `CONDITIONAL_JUMP`
<a id="insn-005cdea0"></a> `005cdea0` | `e8 c3 41 39` | ldrb w8,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-005cdea4"></a> `005cdea4` | `a8 04 00 37` | tbnz w8,#0x0,0x005cdf38 | `CONDITIONAL_JUMP`
<a id="insn-005cdea8"></a> `005cdea8` | `e8 43 41 39` | ldrb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-005cdeac"></a> `005cdeac` | `e8 04 00 37` | tbnz w8,#0x0,0x005cdf48 | `CONDITIONAL_JUMP`
<a id="insn-005cdeb0"></a> `005cdeb0` | `e8 c3 40 39` | ldrb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-005cdeb4"></a> `005cdeb4` | `28 05 00 37` | tbnz w8,#0x0,0x005cdf58 | `CONDITIONAL_JUMP`
<a id="insn-005cdeb8"></a> `005cdeb8` | `e8 43 40 39` | ldrb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-005cdebc"></a> `005cdebc` | `68 00 00 36` | tbz w8,#0x0,0x005cdec8 | `CONDITIONAL_JUMP`
<a id="insn-005cdec0"></a> `005cdec0` | `e0 13 40 f9` | ldr x0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-005cdec4"></a> `005cdec4` | `53 34 18 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-005cdec8"></a> `005cdec8` | `40 f2 ff f0` | adrp x0,0x418000 | `FALL_THROUGH`
<a id="insn-005cdecc"></a> `005cdecc` | `00 c0 0c 91` | add x0,x0,#0x330 | `FALL_THROUGH`
<a id="insn-005cded0"></a> `005cded0` | `c1 32 00 b0` | adrp x1,0xc26000 | `FALL_THROUGH`
<a id="insn-005cded4"></a> `005cded4` | `21 a0 29 91` | add x1,x1,#0xa68 | `FALL_THROUGH`
<a id="insn-005cded8"></a> `005cded8` | `c2 30 00 90` | adrp x2,0xbe5000 | `FALL_THROUGH`
<a id="insn-005cdedc"></a> `005cdedc` | `42 00 3e 91` | add x2,x2,#0xf80 | `FALL_THROUGH`
<a id="insn-005cdee0"></a> `005cdee0` | `2c 34 18 94` | bl 0x00bdaf90 | `UNCONDITIONAL_CALL`
<a id="insn-005cdee4"></a> `005cdee4` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-005cdee8"></a> `005cdee8` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-005cdeec"></a> `005cdeec` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-005cdef0"></a> `005cdef0` | `41 0a 00 54` | b.ne 0x005ce038 | `CONDITIONAL_JUMP`
<a id="insn-005cdef4"></a> `005cdef4` | `f4 4f 51 a9` | ldp x20,x19,[sp, #0x110] | `FALL_THROUGH`
<a id="insn-005cdef8"></a> `005cdef8` | `fc 57 50 a9` | ldp x28,x21,[sp, #0x100] | `FALL_THROUGH`
<a id="insn-005cdefc"></a> `005cdefc` | `fd 7b 4f a9` | ldp x29,x30,[sp, #0xf0] | `FALL_THROUGH`
<a id="insn-005cdf00"></a> `005cdf00` | `ff 83 04 91` | add sp,sp,#0x120 | `FALL_THROUGH`
<a id="insn-005cdf04"></a> `005cdf04` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-005cdf08"></a> `005cdf08` | `e0 73 40 f9` | ldr x0,[sp, #0xe0] | `FALL_THROUGH`
<a id="insn-005cdf0c"></a> `005cdf0c` | `41 34 18 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-005cdf10"></a> `005cdf10` | `e8 c3 42 39` | ldrb w8,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-005cdf14"></a> `005cdf14` | `28 fc 07 36` | tbz w8,#0x0,0x005cde98 | `CONDITIONAL_JUMP`
<a id="insn-005cdf18"></a> `005cdf18` | `e0 63 40 f9` | ldr x0,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-005cdf1c"></a> `005cdf1c` | `3d 34 18 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-005cdf20"></a> `005cdf20` | `e8 43 42 39` | ldrb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-005cdf24"></a> `005cdf24` | `e8 fb 07 36` | tbz w8,#0x0,0x005cdea0 | `CONDITIONAL_JUMP`
<a id="insn-005cdf28"></a> `005cdf28` | `e0 53 40 f9` | ldr x0,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-005cdf2c"></a> `005cdf2c` | `39 34 18 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-005cdf30"></a> `005cdf30` | `e8 c3 41 39` | ldrb w8,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-005cdf34"></a> `005cdf34` | `a8 fb 07 36` | tbz w8,#0x0,0x005cdea8 | `CONDITIONAL_JUMP`
<a id="insn-005cdf38"></a> `005cdf38` | `e0 43 40 f9` | ldr x0,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-005cdf3c"></a> `005cdf3c` | `35 34 18 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-005cdf40"></a> `005cdf40` | `e8 43 41 39` | ldrb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-005cdf44"></a> `005cdf44` | `68 fb 07 36` | tbz w8,#0x0,0x005cdeb0 | `CONDITIONAL_JUMP`
<a id="insn-005cdf48"></a> `005cdf48` | `e0 33 40 f9` | ldr x0,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-005cdf4c"></a> `005cdf4c` | `31 34 18 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-005cdf50"></a> `005cdf50` | `e8 c3 40 39` | ldrb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-005cdf54"></a> `005cdf54` | `28 fb 07 36` | tbz w8,#0x0,0x005cdeb8 | `CONDITIONAL_JUMP`
<a id="insn-005cdf58"></a> `005cdf58` | `e0 23 40 f9` | ldr x0,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-005cdf5c"></a> `005cdf5c` | `2d 34 18 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-005cdf60"></a> `005cdf60` | `e8 43 40 39` | ldrb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-005cdf64"></a> `005cdf64` | `e8 fa 07 37` | tbnz w8,#0x0,0x005cdec0 | `CONDITIONAL_JUMP`
<a id="insn-005cdf68"></a> `005cdf68` | `d8 ff ff 17` | b 0x005cdec8 | `UNCONDITIONAL_JUMP`
<a id="insn-005ce038"></a> `005ce038` | `02 34 18 94` | bl 0x00bdb040 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`005cdcac`](#insn-005cdcac) 範囲 `[['005cdcac', '005cde8f']]`
  - `CONDITIONAL_JUMP` [`005cde8c`](#insn-005cde8c) → [`005cdf08`](#insn-005cdf08)
  - `FALL_THROUGH` [`005cde8c`](#insn-005cde8c) → [`005cde90`](#insn-005cde90)
- ブロック [`005cde90`](#insn-005cde90) 範囲 `[['005cde90', '005cde97']]`
  - `CONDITIONAL_JUMP` [`005cde94`](#insn-005cde94) → [`005cdf18`](#insn-005cdf18)
  - `FALL_THROUGH` [`005cde94`](#insn-005cde94) → [`005cde98`](#insn-005cde98)
- ブロック [`005cde98`](#insn-005cde98) 範囲 `[['005cde98', '005cde9f']]`
  - `CONDITIONAL_JUMP` [`005cde9c`](#insn-005cde9c) → [`005cdf28`](#insn-005cdf28)
  - `FALL_THROUGH` [`005cde9c`](#insn-005cde9c) → [`005cdea0`](#insn-005cdea0)
- ブロック [`005cdea0`](#insn-005cdea0) 範囲 `[['005cdea0', '005cdea7']]`
  - `CONDITIONAL_JUMP` [`005cdea4`](#insn-005cdea4) → [`005cdf38`](#insn-005cdf38)
  - `FALL_THROUGH` [`005cdea4`](#insn-005cdea4) → [`005cdea8`](#insn-005cdea8)
- ブロック [`005cdea8`](#insn-005cdea8) 範囲 `[['005cdea8', '005cdeaf']]`
  - `CONDITIONAL_JUMP` [`005cdeac`](#insn-005cdeac) → [`005cdf48`](#insn-005cdf48)
  - `FALL_THROUGH` [`005cdeac`](#insn-005cdeac) → [`005cdeb0`](#insn-005cdeb0)
- ブロック [`005cdeb0`](#insn-005cdeb0) 範囲 `[['005cdeb0', '005cdeb7']]`
  - `CONDITIONAL_JUMP` [`005cdeb4`](#insn-005cdeb4) → [`005cdf58`](#insn-005cdf58)
  - `FALL_THROUGH` [`005cdeb4`](#insn-005cdeb4) → [`005cdeb8`](#insn-005cdeb8)
- ブロック [`005cdeb8`](#insn-005cdeb8) 範囲 `[['005cdeb8', '005cdebf']]`
  - `CONDITIONAL_JUMP` [`005cdebc`](#insn-005cdebc) → [`005cdec8`](#insn-005cdec8)
  - `FALL_THROUGH` [`005cdebc`](#insn-005cdebc) → [`005cdec0`](#insn-005cdec0)
- ブロック [`005cdec0`](#insn-005cdec0) 範囲 `[['005cdec0', '005cdec7']]`
  - `FALL_THROUGH` [`005cdec4`](#insn-005cdec4) → [`005cdec8`](#insn-005cdec8)
- ブロック [`005cdec8`](#insn-005cdec8) 範囲 `[['005cdec8', '005cdef3']]`
  - `CONDITIONAL_JUMP` [`005cdef0`](#insn-005cdef0) → [`005ce038`](#insn-005ce038)
  - `FALL_THROUGH` [`005cdef0`](#insn-005cdef0) → [`005cdef4`](#insn-005cdef4)
- ブロック [`005cdef4`](#insn-005cdef4) 範囲 `[['005cdef4', '005cdf07']]`
- ブロック [`005cdf08`](#insn-005cdf08) 範囲 `[['005cdf08', '005cdf17']]`
  - `CONDITIONAL_JUMP` [`005cdf14`](#insn-005cdf14) → [`005cde98`](#insn-005cde98)
  - `FALL_THROUGH` [`005cdf14`](#insn-005cdf14) → [`005cdf18`](#insn-005cdf18)
- ブロック [`005cdf18`](#insn-005cdf18) 範囲 `[['005cdf18', '005cdf1f']]`
  - `FALL_THROUGH` [`005cdf1c`](#insn-005cdf1c) → [`005cdf20`](#insn-005cdf20)
- ブロック [`005cdf20`](#insn-005cdf20) 範囲 `[['005cdf20', '005cdf27']]`
  - `CONDITIONAL_JUMP` [`005cdf24`](#insn-005cdf24) → [`005cdea0`](#insn-005cdea0)
  - `FALL_THROUGH` [`005cdf24`](#insn-005cdf24) → [`005cdf28`](#insn-005cdf28)
- ブロック [`005cdf28`](#insn-005cdf28) 範囲 `[['005cdf28', '005cdf37']]`
  - `CONDITIONAL_JUMP` [`005cdf34`](#insn-005cdf34) → [`005cdea8`](#insn-005cdea8)
  - `FALL_THROUGH` [`005cdf34`](#insn-005cdf34) → [`005cdf38`](#insn-005cdf38)
- ブロック [`005cdf38`](#insn-005cdf38) 範囲 `[['005cdf38', '005cdf47']]`
  - `CONDITIONAL_JUMP` [`005cdf44`](#insn-005cdf44) → [`005cdeb0`](#insn-005cdeb0)
  - `FALL_THROUGH` [`005cdf44`](#insn-005cdf44) → [`005cdf48`](#insn-005cdf48)
- ブロック [`005cdf48`](#insn-005cdf48) 範囲 `[['005cdf48', '005cdf57']]`
  - `CONDITIONAL_JUMP` [`005cdf54`](#insn-005cdf54) → [`005cdeb8`](#insn-005cdeb8)
  - `FALL_THROUGH` [`005cdf54`](#insn-005cdf54) → [`005cdf58`](#insn-005cdf58)
- ブロック [`005cdf58`](#insn-005cdf58) 範囲 `[['005cdf58', '005cdf67']]`
  - `CONDITIONAL_JUMP` [`005cdf64`](#insn-005cdf64) → [`005cdec0`](#insn-005cdec0)
  - `FALL_THROUGH` [`005cdf64`](#insn-005cdf64) → [`005cdf68`](#insn-005cdf68)
- ブロック [`005cdf68`](#insn-005cdf68) 範囲 `[['005cdf68', '005cdf6b']]`
  - `UNCONDITIONAL_JUMP` [`005cdf68`](#insn-005cdf68) → [`005cdec8`](#insn-005cdec8)
- ブロック [`005ce038`](#insn-005ce038) 範囲 `[['005ce038', '005ce03b']]`

## 命令位置別の参照

- [`005cdcb0`](#insn-005cdcb0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cdcb4`](#insn-005cdcb4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cdcb8`](#insn-005cdcb8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cdcdc`](#insn-005cdcdc) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cdce8`](#insn-005cdce8) → `002a72dd`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`005cdcf0`](#insn-005cdcf0) → `Stack[-0xff]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cdcf4`](#insn-005cdcf4) → `Stack[-0xf8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cdd04`](#insn-005cdd04) → `Stack[-0x10f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cdd0c`](#insn-005cdd0c) → `002a72f0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`005cdd10`](#insn-005cdd10) → `Stack[-0xdf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cdd18`](#insn-005cdd18) → `Stack[-0xd8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cdd28`](#insn-005cdd28) → `Stack[-0xef]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cdd2c`](#insn-005cdd2c) → `002a8046`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`005cdd30`](#insn-005cdd30) → `Stack[-0xbf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cdd38`](#insn-005cdd38) → `Stack[-0xb8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cdd48`](#insn-005cdd48) → `Stack[-0xcf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cdd4c`](#insn-005cdd4c) → `0029373b`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`005cdd50`](#insn-005cdd50) → `Stack[-0x9f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cdd58`](#insn-005cdd58) → `Stack[-0x98]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cdd64`](#insn-005cdd64) → `Stack[-0xaf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cdd68`](#insn-005cdd68) → `0029c36e`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`005cdd70`](#insn-005cdd70) → `Stack[-0x7f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cdd78`](#insn-005cdd78) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cdd84`](#insn-005cdd84) → `Stack[-0x8f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cdd88`](#insn-005cdd88) → `00291877`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`005cdd90`](#insn-005cdd90) → `Stack[-0x5f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cdd98`](#insn-005cdd98) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cdda4`](#insn-005cdda4) → `Stack[-0x6f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cdda8`](#insn-005cdda8) → `002945b3`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`005cddac`](#insn-005cddac) → `Stack[-0x110]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cddb0`](#insn-005cddb0) → `Stack[-0xf0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cddb4`](#insn-005cddb4) → `Stack[-0xd0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cddb8`](#insn-005cddb8) → `Stack[-0xb0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cddbc`](#insn-005cddbc) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cddc0`](#insn-005cddc0) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cddc4`](#insn-005cddc4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cddcc`](#insn-005cddcc) → `Stack[-0x118]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cddd0`](#insn-005cddd0) → `Stack[-0xfd]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cddd4`](#insn-005cddd4) → `Stack[-0xdd]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cddd8`](#insn-005cddd8) → `Stack[-0xbd]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cdddc`](#insn-005cdddc) → `Stack[-0x9d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cdde0`](#insn-005cdde0) → `Stack[-0x7d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cdde4`](#insn-005cdde4) → `Stack[-0x5d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cdde8`](#insn-005cdde8) → `Stack[-0x3f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cddec`](#insn-005cddec) → `Stack[-0x4f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cddf0`](#insn-005cddf0) → `Stack[-0x3d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cddf4`](#insn-005cddf4) → `00c26a78`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`005cddf8`](#insn-005cddf8) → `00c26a70`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`005cddfc`](#insn-005cddfc) → `00c26a68`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`005cddfc`](#insn-005cddfc) → `00c26a70`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`005cde08`](#insn-005cde08) → `00c26a68`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`005cde0c`](#insn-005cde0c) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`005cde10`](#insn-005cde10) → `00c26a70`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`005cde1c`](#insn-005cde1c) → `00c26a68`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`005cde20`](#insn-005cde20) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`005cde24`](#insn-005cde24) → `00c26a70`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`005cde30`](#insn-005cde30) → `00c26a68`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`005cde34`](#insn-005cde34) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`005cde38`](#insn-005cde38) → `00c26a70`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`005cde44`](#insn-005cde44) → `00c26a68`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`005cde48`](#insn-005cde48) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`005cde4c`](#insn-005cde4c) → `00c26a70`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`005cde58`](#insn-005cde58) → `00c26a68`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`005cde5c`](#insn-005cde5c) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`005cde60`](#insn-005cde60) → `00c26a70`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`005cde6c`](#insn-005cde6c) → `00c26a68`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`005cde70`](#insn-005cde70) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`005cde74`](#insn-005cde74) → `00c26a70`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`005cde80`](#insn-005cde80) → `00c26a68`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`005cde84`](#insn-005cde84) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`005cde88`](#insn-005cde88) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cde8c`](#insn-005cde8c) → [`005cdf08`](#insn-005cdf08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cde90`](#insn-005cde90) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cde94`](#insn-005cde94) → [`005cdf18`](#insn-005cdf18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cde98`](#insn-005cde98) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cde9c`](#insn-005cde9c) → [`005cdf28`](#insn-005cdf28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cdea0`](#insn-005cdea0) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cdea4`](#insn-005cdea4) → [`005cdf38`](#insn-005cdf38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cdea8`](#insn-005cdea8) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cdeac`](#insn-005cdeac) → [`005cdf48`](#insn-005cdf48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cdeb0`](#insn-005cdeb0) → `Stack[-0xf0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cdeb4`](#insn-005cdeb4) → [`005cdf58`](#insn-005cdf58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cdeb8`](#insn-005cdeb8) → `Stack[-0x110]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cdebc`](#insn-005cdebc) → [`005cdec8`](#insn-005cdec8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cdec0`](#insn-005cdec0) → `Stack[-0x100]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cdec4`](#insn-005cdec4) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`005cdecc`](#insn-005cdecc) → [`00418330`](../00418/00418330.md) · `PARAM` · `ANALYSIS` · 関数 `00418330` · 推定シンボル `None` · 推定型 `None`
- [`005cded4`](#insn-005cded4) → `00c26a68`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`005cdedc`](#insn-005cdedc) → `00be5f80`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`005cdee0`](#insn-005cdee0) → [`00bdaf90`](../00bda/00bdaf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf90` · 推定シンボル `None` · 推定型 `None`
- [`005cdee8`](#insn-005cdee8) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cdef0`](#insn-005cdef0) → [`005ce038`](#insn-005ce038) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cdef4`](#insn-005cdef4) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cdef8`](#insn-005cdef8) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cdefc`](#insn-005cdefc) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cdf08`](#insn-005cdf08) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cdf0c`](#insn-005cdf0c) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`005cdf10`](#insn-005cdf10) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cdf14`](#insn-005cdf14) → [`005cde98`](#insn-005cde98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cdf18`](#insn-005cdf18) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cdf1c`](#insn-005cdf1c) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`005cdf20`](#insn-005cdf20) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cdf24`](#insn-005cdf24) → [`005cdea0`](#insn-005cdea0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cdf28`](#insn-005cdf28) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cdf2c`](#insn-005cdf2c) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`005cdf30`](#insn-005cdf30) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cdf34`](#insn-005cdf34) → [`005cdea8`](#insn-005cdea8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cdf38`](#insn-005cdf38) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cdf3c`](#insn-005cdf3c) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`005cdf40`](#insn-005cdf40) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cdf44`](#insn-005cdf44) → [`005cdeb0`](#insn-005cdeb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cdf48`](#insn-005cdf48) → `Stack[-0xc0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cdf4c`](#insn-005cdf4c) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`005cdf50`](#insn-005cdf50) → `Stack[-0xf0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cdf54`](#insn-005cdf54) → [`005cdeb8`](#insn-005cdeb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cdf58`](#insn-005cdf58) → `Stack[-0xe0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cdf5c`](#insn-005cdf5c) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`005cdf60`](#insn-005cdf60) → `Stack[-0x110]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cdf64`](#insn-005cdf64) → [`005cdec0`](#insn-005cdec0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cdf68`](#insn-005cdf68) → [`005cdec8`](#insn-005cdec8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005ce038`](#insn-005ce038) → [`00bdb040`](../00bdb/00bdb040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb040` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`005cdcb0`](#insn-005cdcb0)

~~~json
{
  "source": "005cdcb0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cdcb4`](#insn-005cdcb4)

~~~json
{
  "source": "005cdcb4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cdcb8`](#insn-005cdcb8)

~~~json
{
  "source": "005cdcb8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cdcdc`](#insn-005cdcdc)

~~~json
{
  "source": "005cdcdc",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cdce8`](#insn-005cdce8)

~~~json
{
  "source": "005cdce8",
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
- 参照命令 [`005cdcf0`](#insn-005cdcf0)

~~~json
{
  "source": "005cdcf0",
  "target": "Stack[-0xff]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cdcf4`](#insn-005cdcf4)

~~~json
{
  "source": "005cdcf4",
  "target": "Stack[-0xf8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cdd04`](#insn-005cdd04)

~~~json
{
  "source": "005cdd04",
  "target": "Stack[-0x10f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cdd0c`](#insn-005cdd0c)

~~~json
{
  "source": "005cdd0c",
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
- 参照命令 [`005cdd10`](#insn-005cdd10)

~~~json
{
  "source": "005cdd10",
  "target": "Stack[-0xdf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cdd18`](#insn-005cdd18)

~~~json
{
  "source": "005cdd18",
  "target": "Stack[-0xd8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cdd28`](#insn-005cdd28)

~~~json
{
  "source": "005cdd28",
  "target": "Stack[-0xef]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cdd2c`](#insn-005cdd2c)

~~~json
{
  "source": "005cdd2c",
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
- 参照命令 [`005cdd30`](#insn-005cdd30)

~~~json
{
  "source": "005cdd30",
  "target": "Stack[-0xbf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cdd38`](#insn-005cdd38)

~~~json
{
  "source": "005cdd38",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cdd48`](#insn-005cdd48)

~~~json
{
  "source": "005cdd48",
  "target": "Stack[-0xcf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cdd4c`](#insn-005cdd4c)

~~~json
{
  "source": "005cdd4c",
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
- 参照命令 [`005cdd50`](#insn-005cdd50)

~~~json
{
  "source": "005cdd50",
  "target": "Stack[-0x9f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cdd58`](#insn-005cdd58)

~~~json
{
  "source": "005cdd58",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cdd64`](#insn-005cdd64)

~~~json
{
  "source": "005cdd64",
  "target": "Stack[-0xaf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cdd68`](#insn-005cdd68)

~~~json
{
  "source": "005cdd68",
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
- 参照命令 [`005cdd70`](#insn-005cdd70)

~~~json
{
  "source": "005cdd70",
  "target": "Stack[-0x7f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cdd78`](#insn-005cdd78)

~~~json
{
  "source": "005cdd78",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cdd84`](#insn-005cdd84)

~~~json
{
  "source": "005cdd84",
  "target": "Stack[-0x8f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cdd88`](#insn-005cdd88)

~~~json
{
  "source": "005cdd88",
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
- 参照命令 [`005cdd90`](#insn-005cdd90)

~~~json
{
  "source": "005cdd90",
  "target": "Stack[-0x5f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cdd98`](#insn-005cdd98)

~~~json
{
  "source": "005cdd98",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cdda4`](#insn-005cdda4)

~~~json
{
  "source": "005cdda4",
  "target": "Stack[-0x6f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cdda8`](#insn-005cdda8)

~~~json
{
  "source": "005cdda8",
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
- 参照命令 [`005cddac`](#insn-005cddac)

~~~json
{
  "source": "005cddac",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cddb0`](#insn-005cddb0)

~~~json
{
  "source": "005cddb0",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cddb4`](#insn-005cddb4)

~~~json
{
  "source": "005cddb4",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cddb8`](#insn-005cddb8)

~~~json
{
  "source": "005cddb8",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cddbc`](#insn-005cddbc)

~~~json
{
  "source": "005cddbc",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cddc0`](#insn-005cddc0)

~~~json
{
  "source": "005cddc0",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cddc4`](#insn-005cddc4)

~~~json
{
  "source": "005cddc4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cddcc`](#insn-005cddcc)

~~~json
{
  "source": "005cddcc",
  "target": "Stack[-0x118]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cddd0`](#insn-005cddd0)

~~~json
{
  "source": "005cddd0",
  "target": "Stack[-0xfd]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cddd4`](#insn-005cddd4)

~~~json
{
  "source": "005cddd4",
  "target": "Stack[-0xdd]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cddd8`](#insn-005cddd8)

~~~json
{
  "source": "005cddd8",
  "target": "Stack[-0xbd]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cdddc`](#insn-005cdddc)

~~~json
{
  "source": "005cdddc",
  "target": "Stack[-0x9d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cdde0`](#insn-005cdde0)

~~~json
{
  "source": "005cdde0",
  "target": "Stack[-0x7d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cdde4`](#insn-005cdde4)

~~~json
{
  "source": "005cdde4",
  "target": "Stack[-0x5d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cdde8`](#insn-005cdde8)

~~~json
{
  "source": "005cdde8",
  "target": "Stack[-0x3f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cddec`](#insn-005cddec)

~~~json
{
  "source": "005cddec",
  "target": "Stack[-0x4f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cddf0`](#insn-005cddf0)

~~~json
{
  "source": "005cddf0",
  "target": "Stack[-0x3d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cddf4`](#insn-005cddf4)

~~~json
{
  "source": "005cddf4",
  "target": "00c26a78",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c26a78",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`005cddf8`](#insn-005cddf8)

~~~json
{
  "source": "005cddf8",
  "target": "00c26a70",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c26a70",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`005cddfc`](#insn-005cddfc)

~~~json
{
  "source": "005cddfc",
  "target": "00c26a68",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c26a68",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`005cddfc`](#insn-005cddfc)

~~~json
{
  "source": "005cddfc",
  "target": "00c26a70",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c26a70",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`005cde08`](#insn-005cde08)

~~~json
{
  "source": "005cde08",
  "target": "00c26a68",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c26a68",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`005cde0c`](#insn-005cde0c)

~~~json
{
  "source": "005cde0c",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005cde10`](#insn-005cde10)

~~~json
{
  "source": "005cde10",
  "target": "00c26a70",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c26a70",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`005cde1c`](#insn-005cde1c)

~~~json
{
  "source": "005cde1c",
  "target": "00c26a68",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c26a68",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`005cde20`](#insn-005cde20)

~~~json
{
  "source": "005cde20",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005cde24`](#insn-005cde24)

~~~json
{
  "source": "005cde24",
  "target": "00c26a70",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c26a70",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`005cde30`](#insn-005cde30)

~~~json
{
  "source": "005cde30",
  "target": "00c26a68",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c26a68",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`005cde34`](#insn-005cde34)

~~~json
{
  "source": "005cde34",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005cde38`](#insn-005cde38)

~~~json
{
  "source": "005cde38",
  "target": "00c26a70",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c26a70",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`005cde44`](#insn-005cde44)

~~~json
{
  "source": "005cde44",
  "target": "00c26a68",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c26a68",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`005cde48`](#insn-005cde48)

~~~json
{
  "source": "005cde48",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005cde4c`](#insn-005cde4c)

~~~json
{
  "source": "005cde4c",
  "target": "00c26a70",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c26a70",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`005cde58`](#insn-005cde58)

~~~json
{
  "source": "005cde58",
  "target": "00c26a68",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c26a68",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`005cde5c`](#insn-005cde5c)

~~~json
{
  "source": "005cde5c",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005cde60`](#insn-005cde60)

~~~json
{
  "source": "005cde60",
  "target": "00c26a70",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c26a70",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`005cde6c`](#insn-005cde6c)

~~~json
{
  "source": "005cde6c",
  "target": "00c26a68",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c26a68",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`005cde70`](#insn-005cde70)

~~~json
{
  "source": "005cde70",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005cde74`](#insn-005cde74)

~~~json
{
  "source": "005cde74",
  "target": "00c26a70",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c26a70",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`005cde80`](#insn-005cde80)

~~~json
{
  "source": "005cde80",
  "target": "00c26a68",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c26a68",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`005cde84`](#insn-005cde84)

~~~json
{
  "source": "005cde84",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005cde88`](#insn-005cde88)

~~~json
{
  "source": "005cde88",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cde8c`](#insn-005cde8c)

~~~json
{
  "source": "005cde8c",
  "target": "005cdf08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cde90`](#insn-005cde90)

~~~json
{
  "source": "005cde90",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cde94`](#insn-005cde94)

~~~json
{
  "source": "005cde94",
  "target": "005cdf18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cde98`](#insn-005cde98)

~~~json
{
  "source": "005cde98",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cde9c`](#insn-005cde9c)

~~~json
{
  "source": "005cde9c",
  "target": "005cdf28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cdea0`](#insn-005cdea0)

~~~json
{
  "source": "005cdea0",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cdea4`](#insn-005cdea4)

~~~json
{
  "source": "005cdea4",
  "target": "005cdf38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cdea8`](#insn-005cdea8)

~~~json
{
  "source": "005cdea8",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cdeac`](#insn-005cdeac)

~~~json
{
  "source": "005cdeac",
  "target": "005cdf48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cdeb0`](#insn-005cdeb0)

~~~json
{
  "source": "005cdeb0",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cdeb4`](#insn-005cdeb4)

~~~json
{
  "source": "005cdeb4",
  "target": "005cdf58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cdeb8`](#insn-005cdeb8)

~~~json
{
  "source": "005cdeb8",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cdebc`](#insn-005cdebc)

~~~json
{
  "source": "005cdebc",
  "target": "005cdec8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cdec0`](#insn-005cdec0)

~~~json
{
  "source": "005cdec0",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cdec4`](#insn-005cdec4)

~~~json
{
  "source": "005cdec4",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005cdecc`](#insn-005cdecc)

~~~json
{
  "source": "005cdecc",
  "target": "00418330",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005cded4`](#insn-005cded4)

~~~json
{
  "source": "005cded4",
  "target": "00c26a68",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c26a68",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`005cdedc`](#insn-005cdedc)

~~~json
{
  "source": "005cdedc",
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
- 参照命令 [`005cdee0`](#insn-005cdee0)

~~~json
{
  "source": "005cdee0",
  "target": "00bdaf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005cdee8`](#insn-005cdee8)

~~~json
{
  "source": "005cdee8",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cdef0`](#insn-005cdef0)

~~~json
{
  "source": "005cdef0",
  "target": "005ce038",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cdef4`](#insn-005cdef4)

~~~json
{
  "source": "005cdef4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cdef8`](#insn-005cdef8)

~~~json
{
  "source": "005cdef8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cdefc`](#insn-005cdefc)

~~~json
{
  "source": "005cdefc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cdf08`](#insn-005cdf08)

~~~json
{
  "source": "005cdf08",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cdf0c`](#insn-005cdf0c)

~~~json
{
  "source": "005cdf0c",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005cdf10`](#insn-005cdf10)

~~~json
{
  "source": "005cdf10",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cdf14`](#insn-005cdf14)

~~~json
{
  "source": "005cdf14",
  "target": "005cde98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cdf18`](#insn-005cdf18)

~~~json
{
  "source": "005cdf18",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cdf1c`](#insn-005cdf1c)

~~~json
{
  "source": "005cdf1c",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005cdf20`](#insn-005cdf20)

~~~json
{
  "source": "005cdf20",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cdf24`](#insn-005cdf24)

~~~json
{
  "source": "005cdf24",
  "target": "005cdea0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cdf28`](#insn-005cdf28)

~~~json
{
  "source": "005cdf28",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cdf2c`](#insn-005cdf2c)

~~~json
{
  "source": "005cdf2c",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005cdf30`](#insn-005cdf30)

~~~json
{
  "source": "005cdf30",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cdf34`](#insn-005cdf34)

~~~json
{
  "source": "005cdf34",
  "target": "005cdea8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cdf38`](#insn-005cdf38)

~~~json
{
  "source": "005cdf38",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cdf3c`](#insn-005cdf3c)

~~~json
{
  "source": "005cdf3c",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005cdf40`](#insn-005cdf40)

~~~json
{
  "source": "005cdf40",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cdf44`](#insn-005cdf44)

~~~json
{
  "source": "005cdf44",
  "target": "005cdeb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cdf48`](#insn-005cdf48)

~~~json
{
  "source": "005cdf48",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cdf4c`](#insn-005cdf4c)

~~~json
{
  "source": "005cdf4c",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005cdf50`](#insn-005cdf50)

~~~json
{
  "source": "005cdf50",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cdf54`](#insn-005cdf54)

~~~json
{
  "source": "005cdf54",
  "target": "005cdeb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cdf58`](#insn-005cdf58)

~~~json
{
  "source": "005cdf58",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cdf5c`](#insn-005cdf5c)

~~~json
{
  "source": "005cdf5c",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005cdf60`](#insn-005cdf60)

~~~json
{
  "source": "005cdf60",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cdf64`](#insn-005cdf64)

~~~json
{
  "source": "005cdf64",
  "target": "005cdec0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cdf68`](#insn-005cdf68)

~~~json
{
  "source": "005cdf68",
  "target": "005cdec8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005ce038`](#insn-005ce038)

~~~json
{
  "source": "005ce038",
  "target": "00bdb040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
