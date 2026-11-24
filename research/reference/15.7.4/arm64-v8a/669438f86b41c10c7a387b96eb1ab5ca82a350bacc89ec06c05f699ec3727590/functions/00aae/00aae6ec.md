# 00aae6ec

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aae6a8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aae/00aae6a8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0059.md#compare-2e08938ae6e01feda0cfe7c7dd1f1d78)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b0e17c`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0e/00b0e17c.md) · 移動量 `+0x5fa90`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0053.md#compare-6216ea85ee0b7faa74600ca12f9c0f4d)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aae6ec",
  "name": "_INIT_247",
  "size": 708,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9a51ff643f7df522c244ba39db6ba356b74f6dcba9851b4c2c3be7148ef12f2f",
  "source_text_sha256": "9a51ff643f7df522c244ba39db6ba356b74f6dcba9851b4c2c3be7148ef12f2f",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aae6ec",
        "00aae9ab"
      ],
      [
        "00aaea78",
        "00aaea7b"
      ]
    ],
    "bytes_sha256": "9718c6797589ee10b3a4d98c2ada8264e6579efd42a802470333fa215a3f9c74",
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

## 疑似コード / UTF-8 5151 bytes

~~~c

/* WARNING: Type propagation algorithm not settling */

void _INIT_247(void)

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
  DAT_0109fb08 = 0;
  DAT_0109fb00 = 0;
  DAT_0109faf8 = &DAT_0109fb00;
  FUN_00418cb8(&DAT_0109faf8,&DAT_0109fb00,local_118,local_118);
  FUN_00418cb8(&DAT_0109faf8,&DAT_0109fb00,local_f8,local_f8);
  FUN_00418cb8(&DAT_0109faf8,&DAT_0109fb00,local_d8,local_d8);
  FUN_00418cb8(&DAT_0109faf8,&DAT_0109fb00,local_b8,local_b8);
  FUN_00418cb8(&DAT_0109faf8,&DAT_0109fb00,local_98,local_98);
  FUN_00418cb8(&DAT_0109faf8,&DAT_0109fb00,local_78,local_78);
  FUN_00418cb8(&DAT_0109faf8,&DAT_0109fb00,local_58,local_58);
  if ((local_50 & 1) != 0) {
    _ZdlPv((void *)CONCAT44(uStack_3c,CONCAT13(uStack_3d,CONCAT21(uStack_3f,cStack_40))));
  }
  if ((local_70 & 1) != 0) {
                    /* try { // try from 00aae958 to 00bae963 has its CatchHandler @ 00ab7638 */
    _ZdlPv((void *)CONCAT44(uStack_5c,CONCAT13(uStack_5d,CONCAT21(uStack_5f,cStack_60))));
  }
  if ((local_90 & 1) != 0) {
                    /* try { // try from 00aae96c to 00bae973 has its CatchHandler @ 00ab762c */
    _ZdlPv((void *)CONCAT44(uStack_7c,CONCAT13(uStack_7d,CONCAT21(uStack_7f,cStack_80))));
  }
                    /* try { // try from 00aae974 to 00bb11f3 has its CatchHandler @ 00aa9ce0 */
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
  __cxa_atexit(FUN_00418330,&DAT_0109faf8,&PTR_LOOP_00be5fd0);
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
<a id="insn-00aae6ec"></a> `00aae6ec` | `ff 83 04 d1` | sub sp,sp,#0x120 | `FALL_THROUGH`
<a id="insn-00aae6f0"></a> `00aae6f0` | `fd 7b 0f a9` | stp x29,x30,[sp, #0xf0] | `FALL_THROUGH`
<a id="insn-00aae6f4"></a> `00aae6f4` | `fc 57 10 a9` | stp x28,x21,[sp, #0x100] | `FALL_THROUGH`
<a id="insn-00aae6f8"></a> `00aae6f8` | `f4 4f 11 a9` | stp x20,x19,[sp, #0x110] | `FALL_THROUGH`
<a id="insn-00aae6fc"></a> `00aae6fc` | `fd c3 03 91` | add x29,sp,#0xf0 | `FALL_THROUGH`
<a id="insn-00aae700"></a> `00aae700` | `55 d0 3b d5` | mrs x21,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00aae704"></a> `00aae704` | `2a e8 8c 52` | mov w10,#0x6741 | `FALL_THROUGH`
<a id="insn-00aae708"></a> `00aae708` | `f4 23 00 91` | add x20,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00aae70c"></a> `00aae70c` | `a9 16 40 f9` | ldr x9,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00aae710"></a> `00aae710` | `88 04 80 52` | mov w8,#0x24 | `FALL_THROUGH`
<a id="insn-00aae714"></a> `00aae714` | `93 2f 00 b0` | adrp x19,0x109f000 | `FALL_THROUGH`
<a id="insn-00aae718"></a> `00aae718` | `73 e2 2b 91` | add x19,x19,#0xaf8 | `FALL_THROUGH`
<a id="insn-00aae71c"></a> `00aae71c` | `a9 83 1f f8` | stur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aae720"></a> `00aae720` | `c9 bf ff b0` | adrp x9,0x2a7000 | `FALL_THROUGH`
<a id="insn-00aae724"></a> `00aae724` | `29 dd 0d 91` | add x9,x9,#0x377 | `FALL_THROUGH`
<a id="insn-00aae728"></a> `00aae728` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00aae72c"></a> `00aae72c` | `29 00 80 52` | mov w9,#0x1 | `FALL_THROUGH`
<a id="insn-00aae730"></a> `00aae730` | `ea 13 02 78` | sturh w10,[sp, #0x21] | `FALL_THROUGH`
<a id="insn-00aae734"></a> `00aae734` | `e9 2b 00 b9` | str w9,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00aae738"></a> `00aae738` | `49 28 88 52` | mov w9,#0x4142 | `FALL_THROUGH`
<a id="insn-00aae73c"></a> `00aae73c` | `ca bf ff b0` | adrp x10,0x2a7000 | `FALL_THROUGH`
<a id="insn-00aae740"></a> `00aae740` | `4a 29 0e 91` | add x10,x10,#0x38a | `FALL_THROUGH`
<a id="insn-00aae744"></a> `00aae744` | `e0 13 81 3c` | stur q0,[sp, #0x11] | `FALL_THROUGH`
<a id="insn-00aae748"></a> `00aae748` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00aae74c"></a> `00aae74c` | `40 01 c0 3d` | ldr q0,[x10] | `FALL_THROUGH`
<a id="insn-00aae750"></a> `00aae750` | `e9 13 04 78` | sturh w9,[sp, #0x41] | `FALL_THROUGH`
<a id="insn-00aae754"></a> `00aae754` | `49 00 80 52` | mov w9,#0x2 | `FALL_THROUGH`
<a id="insn-00aae758"></a> `00aae758` | `e9 4b 00 b9` | str w9,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00aae75c"></a> `00aae75c` | `49 e8 8c 52` | mov w9,#0x6742 | `FALL_THROUGH`
<a id="insn-00aae760"></a> `00aae760` | `ca bf ff d0` | adrp x10,0x2a8000 | `FALL_THROUGH`
<a id="insn-00aae764"></a> `00aae764` | `4a 81 03 91` | add x10,x10,#0xe0 | `FALL_THROUGH`
<a id="insn-00aae768"></a> `00aae768` | `e0 13 83 3c` | stur q0,[sp, #0x31] | `FALL_THROUGH`
<a id="insn-00aae76c"></a> `00aae76c` | `40 01 c0 3d` | ldr q0,[x10] | `FALL_THROUGH`
<a id="insn-00aae770"></a> `00aae770` | `e9 13 06 78` | sturh w9,[sp, #0x61] | `FALL_THROUGH`
<a id="insn-00aae774"></a> `00aae774` | `69 00 80 52` | mov w9,#0x3 | `FALL_THROUGH`
<a id="insn-00aae778"></a> `00aae778` | `e9 6b 00 b9` | str w9,[sp, #0x68] | `FALL_THROUGH`
<a id="insn-00aae77c"></a> `00aae77c` | `29 e8 8e 52` | mov w9,#0x7741 | `FALL_THROUGH`
<a id="insn-00aae780"></a> `00aae780` | `2a bf ff b0` | adrp x10,0x293000 | `FALL_THROUGH`
<a id="insn-00aae784"></a> `00aae784` | `4a b9 1a 91` | add x10,x10,#0x6ae | `FALL_THROUGH`
<a id="insn-00aae788"></a> `00aae788` | `e0 13 85 3c` | stur q0,[sp, #0x51] | `FALL_THROUGH`
<a id="insn-00aae78c"></a> `00aae78c` | `40 01 c0 3d` | ldr q0,[x10] | `FALL_THROUGH`
<a id="insn-00aae790"></a> `00aae790` | `e9 13 08 78` | sturh w9,[sp, #0x81] | `FALL_THROUGH`
<a id="insn-00aae794"></a> `00aae794` | `89 00 80 52` | mov w9,#0x4 | `FALL_THROUGH`
<a id="insn-00aae798"></a> `00aae798` | `e9 8b 00 b9` | str w9,[sp, #0x88] | `FALL_THROUGH`
<a id="insn-00aae79c"></a> `00aae79c` | `69 bf ff d0` | adrp x9,0x29c000 | `FALL_THROUGH`
<a id="insn-00aae7a0"></a> `00aae7a0` | `29 b1 0d 91` | add x9,x9,#0x36c | `FALL_THROUGH`
<a id="insn-00aae7a4"></a> `00aae7a4` | `e0 13 87 3c` | stur q0,[sp, #0x71] | `FALL_THROUGH`
<a id="insn-00aae7a8"></a> `00aae7a8` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00aae7ac"></a> `00aae7ac` | `49 28 8a 52` | mov w9,#0x5142 | `FALL_THROUGH`
<a id="insn-00aae7b0"></a> `00aae7b0` | `89 92 09 78` | sturh w9,[x20, #0x99] | `FALL_THROUGH`
<a id="insn-00aae7b4"></a> `00aae7b4` | `a9 00 80 52` | mov w9,#0x5 | `FALL_THROUGH`
<a id="insn-00aae7b8"></a> `00aae7b8` | `e9 ab 00 b9` | str w9,[sp, #0xa8] | `FALL_THROUGH`
<a id="insn-00aae7bc"></a> `00aae7bc` | `09 bf ff f0` | adrp x9,0x291000 | `FALL_THROUGH`
<a id="insn-00aae7c0"></a> `00aae7c0` | `29 dd 21 91` | add x9,x9,#0x877 | `FALL_THROUGH`
<a id="insn-00aae7c4"></a> `00aae7c4` | `80 92 88 3c` | stur q0,[x20, #0x89] | `FALL_THROUGH`
<a id="insn-00aae7c8"></a> `00aae7c8` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00aae7cc"></a> `00aae7cc` | `49 e8 8e 52` | mov w9,#0x7742 | `FALL_THROUGH`
<a id="insn-00aae7d0"></a> `00aae7d0` | `89 92 0b 78` | sturh w9,[x20, #0xb9] | `FALL_THROUGH`
<a id="insn-00aae7d4"></a> `00aae7d4` | `c9 00 80 52` | mov w9,#0x6 | `FALL_THROUGH`
<a id="insn-00aae7d8"></a> `00aae7d8` | `e9 cb 00 b9` | str w9,[sp, #0xc8] | `FALL_THROUGH`
<a id="insn-00aae7dc"></a> `00aae7dc` | `29 bf ff d0` | adrp x9,0x294000 | `FALL_THROUGH`
<a id="insn-00aae7e0"></a> `00aae7e0` | `29 99 14 91` | add x9,x9,#0x526 | `FALL_THROUGH`
<a id="insn-00aae7e4"></a> `00aae7e4` | `80 92 8a 3c` | stur q0,[x20, #0xa9] | `FALL_THROUGH`
<a id="insn-00aae7e8"></a> `00aae7e8` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00aae7ec"></a> `00aae7ec` | `e8 43 00 39` | strb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aae7f0"></a> `00aae7f0` | `e8 c3 00 39` | strb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aae7f4"></a> `00aae7f4` | `e8 43 01 39` | strb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00aae7f8"></a> `00aae7f8` | `e8 c3 01 39` | strb w8,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00aae7fc"></a> `00aae7fc` | `e8 43 02 39` | strb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00aae800"></a> `00aae800` | `e8 c3 02 39` | strb w8,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00aae804"></a> `00aae804` | `e8 43 03 39` | strb w8,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-00aae808"></a> `00aae808` | `68 28 88 52` | mov w8,#0x4143 | `FALL_THROUGH`
<a id="insn-00aae80c"></a> `00aae80c` | `ff 0b 00 b9` | str wzr,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00aae810"></a> `00aae810` | `ff 8f 00 39` | strb wzr,[sp, #0x23] | `FALL_THROUGH`
<a id="insn-00aae814"></a> `00aae814` | `ff 0f 01 39` | strb wzr,[sp, #0x43] | `FALL_THROUGH`
<a id="insn-00aae818"></a> `00aae818` | `ff 8f 01 39` | strb wzr,[sp, #0x63] | `FALL_THROUGH`
<a id="insn-00aae81c"></a> `00aae81c` | `ff 0f 02 39` | strb wzr,[sp, #0x83] | `FALL_THROUGH`
<a id="insn-00aae820"></a> `00aae820` | `ff 8f 02 39` | strb wzr,[sp, #0xa3] | `FALL_THROUGH`
<a id="insn-00aae824"></a> `00aae824` | `ff 0f 03 39` | strb wzr,[sp, #0xc3] | `FALL_THROUGH`
<a id="insn-00aae828"></a> `00aae828` | `88 92 0d 78` | sturh w8,[x20, #0xd9] | `FALL_THROUGH`
<a id="insn-00aae82c"></a> `00aae82c` | `80 92 8c 3c` | stur q0,[x20, #0xc9] | `FALL_THROUGH`
<a id="insn-00aae830"></a> `00aae830` | `ff 8f 03 39` | strb wzr,[sp, #0xe3] | `FALL_THROUGH`
<a id="insn-00aae834"></a> `00aae834` | `7f 0a 00 f9` | str xzr,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00aae838"></a> `00aae838` | `3f 8c 00 f8` | str xzr,[x1, #0x8]! | `FALL_THROUGH`
<a id="insn-00aae83c"></a> `00aae83c` | `61 02 00 f9` | str x1,[x19] | `FALL_THROUGH`
<a id="insn-00aae840"></a> `00aae840` | `e2 23 00 91` | add x2,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00aae844"></a> `00aae844` | `e3 23 00 91` | add x3,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00aae848"></a> `00aae848` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aae84c"></a> `00aae84c` | `1b a9 e5 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-00aae850"></a> `00aae850` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00aae854"></a> `00aae854` | `82 82 00 91` | add x2,x20,#0x20 | `FALL_THROUGH`
<a id="insn-00aae858"></a> `00aae858` | `83 82 00 91` | add x3,x20,#0x20 | `FALL_THROUGH`
<a id="insn-00aae85c"></a> `00aae85c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aae860"></a> `00aae860` | `16 a9 e5 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-00aae864"></a> `00aae864` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00aae868"></a> `00aae868` | `82 02 01 91` | add x2,x20,#0x40 | `FALL_THROUGH`
<a id="insn-00aae86c"></a> `00aae86c` | `83 02 01 91` | add x3,x20,#0x40 | `FALL_THROUGH`
<a id="insn-00aae870"></a> `00aae870` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aae874"></a> `00aae874` | `11 a9 e5 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-00aae878"></a> `00aae878` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00aae87c"></a> `00aae87c` | `82 82 01 91` | add x2,x20,#0x60 | `FALL_THROUGH`
<a id="insn-00aae880"></a> `00aae880` | `83 82 01 91` | add x3,x20,#0x60 | `FALL_THROUGH`
<a id="insn-00aae884"></a> `00aae884` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aae888"></a> `00aae888` | `0c a9 e5 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-00aae88c"></a> `00aae88c` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00aae890"></a> `00aae890` | `82 02 02 91` | add x2,x20,#0x80 | `FALL_THROUGH`
<a id="insn-00aae894"></a> `00aae894` | `83 02 02 91` | add x3,x20,#0x80 | `FALL_THROUGH`
<a id="insn-00aae898"></a> `00aae898` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aae89c"></a> `00aae89c` | `07 a9 e5 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-00aae8a0"></a> `00aae8a0` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00aae8a4"></a> `00aae8a4` | `82 82 02 91` | add x2,x20,#0xa0 | `FALL_THROUGH`
<a id="insn-00aae8a8"></a> `00aae8a8` | `83 82 02 91` | add x3,x20,#0xa0 | `FALL_THROUGH`
<a id="insn-00aae8ac"></a> `00aae8ac` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aae8b0"></a> `00aae8b0` | `02 a9 e5 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-00aae8b4"></a> `00aae8b4` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00aae8b8"></a> `00aae8b8` | `82 02 03 91` | add x2,x20,#0xc0 | `FALL_THROUGH`
<a id="insn-00aae8bc"></a> `00aae8bc` | `83 02 03 91` | add x3,x20,#0xc0 | `FALL_THROUGH`
<a id="insn-00aae8c0"></a> `00aae8c0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aae8c4"></a> `00aae8c4` | `fd a8 e5 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-00aae8c8"></a> `00aae8c8` | `e8 43 43 39` | ldrb w8,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-00aae8cc"></a> `00aae8cc` | `e8 03 00 37` | tbnz w8,#0x0,0x00aae948 | `CONDITIONAL_JUMP`
<a id="insn-00aae8d0"></a> `00aae8d0` | `e8 c3 42 39` | ldrb w8,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00aae8d4"></a> `00aae8d4` | `28 04 00 37` | tbnz w8,#0x0,0x00aae958 | `CONDITIONAL_JUMP`
<a id="insn-00aae8d8"></a> `00aae8d8` | `e8 43 42 39` | ldrb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00aae8dc"></a> `00aae8dc` | `68 04 00 37` | tbnz w8,#0x0,0x00aae968 | `CONDITIONAL_JUMP`
<a id="insn-00aae8e0"></a> `00aae8e0` | `e8 c3 41 39` | ldrb w8,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00aae8e4"></a> `00aae8e4` | `a8 04 00 37` | tbnz w8,#0x0,0x00aae978 | `CONDITIONAL_JUMP`
<a id="insn-00aae8e8"></a> `00aae8e8` | `e8 43 41 39` | ldrb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00aae8ec"></a> `00aae8ec` | `e8 04 00 37` | tbnz w8,#0x0,0x00aae988 | `CONDITIONAL_JUMP`
<a id="insn-00aae8f0"></a> `00aae8f0` | `e8 c3 40 39` | ldrb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aae8f4"></a> `00aae8f4` | `28 05 00 37` | tbnz w8,#0x0,0x00aae998 | `CONDITIONAL_JUMP`
<a id="insn-00aae8f8"></a> `00aae8f8` | `e8 43 40 39` | ldrb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aae8fc"></a> `00aae8fc` | `68 00 00 36` | tbz w8,#0x0,0x00aae908 | `CONDITIONAL_JUMP`
<a id="insn-00aae900"></a> `00aae900` | `e0 13 40 f9` | ldr x0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aae904"></a> `00aae904` | `d7 b1 04 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00aae908"></a> `00aae908` | `40 cb ff d0` | adrp x0,0x418000 | `FALL_THROUGH`
<a id="insn-00aae90c"></a> `00aae90c` | `00 c0 0c 91` | add x0,x0,#0x330 | `FALL_THROUGH`
<a id="insn-00aae910"></a> `00aae910` | `81 2f 00 b0` | adrp x1,0x109f000 | `FALL_THROUGH`
<a id="insn-00aae914"></a> `00aae914` | `21 e0 2b 91` | add x1,x1,#0xaf8 | `FALL_THROUGH`
<a id="insn-00aae918"></a> `00aae918` | `a2 09 00 f0` | adrp x2,0xbe5000 | `FALL_THROUGH`
<a id="insn-00aae91c"></a> `00aae91c` | `42 40 3f 91` | add x2,x2,#0xfd0 | `FALL_THROUGH`
<a id="insn-00aae920"></a> `00aae920` | `b0 b1 04 94` | bl 0x00bdafe0 | `UNCONDITIONAL_CALL`
<a id="insn-00aae924"></a> `00aae924` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00aae928"></a> `00aae928` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aae92c"></a> `00aae92c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00aae930"></a> `00aae930` | `41 0a 00 54` | b.ne 0x00aaea78 | `CONDITIONAL_JUMP`
<a id="insn-00aae934"></a> `00aae934` | `f4 4f 51 a9` | ldp x20,x19,[sp, #0x110] | `FALL_THROUGH`
<a id="insn-00aae938"></a> `00aae938` | `fc 57 50 a9` | ldp x28,x21,[sp, #0x100] | `FALL_THROUGH`
<a id="insn-00aae93c"></a> `00aae93c` | `fd 7b 4f a9` | ldp x29,x30,[sp, #0xf0] | `FALL_THROUGH`
<a id="insn-00aae940"></a> `00aae940` | `ff 83 04 91` | add sp,sp,#0x120 | `FALL_THROUGH`
<a id="insn-00aae944"></a> `00aae944` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00aae948"></a> `00aae948` | `e0 73 40 f9` | ldr x0,[sp, #0xe0] | `FALL_THROUGH`
<a id="insn-00aae94c"></a> `00aae94c` | `c5 b1 04 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00aae950"></a> `00aae950` | `e8 c3 42 39` | ldrb w8,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00aae954"></a> `00aae954` | `28 fc 07 36` | tbz w8,#0x0,0x00aae8d8 | `CONDITIONAL_JUMP`
<a id="insn-00aae958"></a> `00aae958` | `e0 63 40 f9` | ldr x0,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00aae95c"></a> `00aae95c` | `c1 b1 04 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00aae960"></a> `00aae960` | `e8 43 42 39` | ldrb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00aae964"></a> `00aae964` | `e8 fb 07 36` | tbz w8,#0x0,0x00aae8e0 | `CONDITIONAL_JUMP`
<a id="insn-00aae968"></a> `00aae968` | `e0 53 40 f9` | ldr x0,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00aae96c"></a> `00aae96c` | `bd b1 04 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00aae970"></a> `00aae970` | `e8 c3 41 39` | ldrb w8,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00aae974"></a> `00aae974` | `a8 fb 07 36` | tbz w8,#0x0,0x00aae8e8 | `CONDITIONAL_JUMP`
<a id="insn-00aae978"></a> `00aae978` | `e0 43 40 f9` | ldr x0,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00aae97c"></a> `00aae97c` | `b9 b1 04 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00aae980"></a> `00aae980` | `e8 43 41 39` | ldrb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00aae984"></a> `00aae984` | `68 fb 07 36` | tbz w8,#0x0,0x00aae8f0 | `CONDITIONAL_JUMP`
<a id="insn-00aae988"></a> `00aae988` | `e0 33 40 f9` | ldr x0,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00aae98c"></a> `00aae98c` | `b5 b1 04 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00aae990"></a> `00aae990` | `e8 c3 40 39` | ldrb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aae994"></a> `00aae994` | `28 fb 07 36` | tbz w8,#0x0,0x00aae8f8 | `CONDITIONAL_JUMP`
<a id="insn-00aae998"></a> `00aae998` | `e0 23 40 f9` | ldr x0,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00aae99c"></a> `00aae99c` | `b1 b1 04 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00aae9a0"></a> `00aae9a0` | `e8 43 40 39` | ldrb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aae9a4"></a> `00aae9a4` | `e8 fa 07 37` | tbnz w8,#0x0,0x00aae900 | `CONDITIONAL_JUMP`
<a id="insn-00aae9a8"></a> `00aae9a8` | `d8 ff ff 17` | b 0x00aae908 | `UNCONDITIONAL_JUMP`
<a id="insn-00aaea78"></a> `00aaea78` | `86 b1 04 94` | bl 0x00bdb090 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aae6ec`](#insn-00aae6ec) 範囲 `[['00aae6ec', '00aae8cf']]`
  - `CONDITIONAL_JUMP` [`00aae8cc`](#insn-00aae8cc) → [`00aae948`](#insn-00aae948)
  - `FALL_THROUGH` [`00aae8cc`](#insn-00aae8cc) → [`00aae8d0`](#insn-00aae8d0)
- ブロック [`00aae8d0`](#insn-00aae8d0) 範囲 `[['00aae8d0', '00aae8d7']]`
  - `CONDITIONAL_JUMP` [`00aae8d4`](#insn-00aae8d4) → [`00aae958`](#insn-00aae958)
  - `FALL_THROUGH` [`00aae8d4`](#insn-00aae8d4) → [`00aae8d8`](#insn-00aae8d8)
- ブロック [`00aae8d8`](#insn-00aae8d8) 範囲 `[['00aae8d8', '00aae8df']]`
  - `CONDITIONAL_JUMP` [`00aae8dc`](#insn-00aae8dc) → [`00aae968`](#insn-00aae968)
  - `FALL_THROUGH` [`00aae8dc`](#insn-00aae8dc) → [`00aae8e0`](#insn-00aae8e0)
- ブロック [`00aae8e0`](#insn-00aae8e0) 範囲 `[['00aae8e0', '00aae8e7']]`
  - `CONDITIONAL_JUMP` [`00aae8e4`](#insn-00aae8e4) → [`00aae978`](#insn-00aae978)
  - `FALL_THROUGH` [`00aae8e4`](#insn-00aae8e4) → [`00aae8e8`](#insn-00aae8e8)
- ブロック [`00aae8e8`](#insn-00aae8e8) 範囲 `[['00aae8e8', '00aae8ef']]`
  - `CONDITIONAL_JUMP` [`00aae8ec`](#insn-00aae8ec) → [`00aae988`](#insn-00aae988)
  - `FALL_THROUGH` [`00aae8ec`](#insn-00aae8ec) → [`00aae8f0`](#insn-00aae8f0)
- ブロック [`00aae8f0`](#insn-00aae8f0) 範囲 `[['00aae8f0', '00aae8f7']]`
  - `CONDITIONAL_JUMP` [`00aae8f4`](#insn-00aae8f4) → [`00aae998`](#insn-00aae998)
  - `FALL_THROUGH` [`00aae8f4`](#insn-00aae8f4) → [`00aae8f8`](#insn-00aae8f8)
- ブロック [`00aae8f8`](#insn-00aae8f8) 範囲 `[['00aae8f8', '00aae8ff']]`
  - `CONDITIONAL_JUMP` [`00aae8fc`](#insn-00aae8fc) → [`00aae908`](#insn-00aae908)
  - `FALL_THROUGH` [`00aae8fc`](#insn-00aae8fc) → [`00aae900`](#insn-00aae900)
- ブロック [`00aae900`](#insn-00aae900) 範囲 `[['00aae900', '00aae907']]`
  - `FALL_THROUGH` [`00aae904`](#insn-00aae904) → [`00aae908`](#insn-00aae908)
- ブロック [`00aae908`](#insn-00aae908) 範囲 `[['00aae908', '00aae933']]`
  - `CONDITIONAL_JUMP` [`00aae930`](#insn-00aae930) → [`00aaea78`](#insn-00aaea78)
  - `FALL_THROUGH` [`00aae930`](#insn-00aae930) → [`00aae934`](#insn-00aae934)
- ブロック [`00aae934`](#insn-00aae934) 範囲 `[['00aae934', '00aae947']]`
- ブロック [`00aae948`](#insn-00aae948) 範囲 `[['00aae948', '00aae957']]`
  - `CONDITIONAL_JUMP` [`00aae954`](#insn-00aae954) → [`00aae8d8`](#insn-00aae8d8)
  - `FALL_THROUGH` [`00aae954`](#insn-00aae954) → [`00aae958`](#insn-00aae958)
- ブロック [`00aae958`](#insn-00aae958) 範囲 `[['00aae958', '00aae967']]`
  - `CONDITIONAL_JUMP` [`00aae964`](#insn-00aae964) → [`00aae8e0`](#insn-00aae8e0)
  - `FALL_THROUGH` [`00aae964`](#insn-00aae964) → [`00aae968`](#insn-00aae968)
- ブロック [`00aae968`](#insn-00aae968) 範囲 `[['00aae968', '00aae96b']]`
  - `FALL_THROUGH` [`00aae968`](#insn-00aae968) → [`00aae96c`](#insn-00aae96c)
- ブロック [`00aae96c`](#insn-00aae96c) 範囲 `[['00aae96c', '00aae973']]`
  - `FALL_THROUGH` [`00aae970`](#insn-00aae970) → [`00aae974`](#insn-00aae974)
- ブロック [`00aae974`](#insn-00aae974) 範囲 `[['00aae974', '00aae977']]`
  - `CONDITIONAL_JUMP` [`00aae974`](#insn-00aae974) → [`00aae8e8`](#insn-00aae8e8)
  - `FALL_THROUGH` [`00aae974`](#insn-00aae974) → [`00aae978`](#insn-00aae978)
- ブロック [`00aae978`](#insn-00aae978) 範囲 `[['00aae978', '00aae987']]`
  - `CONDITIONAL_JUMP` [`00aae984`](#insn-00aae984) → [`00aae8f0`](#insn-00aae8f0)
  - `FALL_THROUGH` [`00aae984`](#insn-00aae984) → [`00aae988`](#insn-00aae988)
- ブロック [`00aae988`](#insn-00aae988) 範囲 `[['00aae988', '00aae997']]`
  - `CONDITIONAL_JUMP` [`00aae994`](#insn-00aae994) → [`00aae8f8`](#insn-00aae8f8)
  - `FALL_THROUGH` [`00aae994`](#insn-00aae994) → [`00aae998`](#insn-00aae998)
- ブロック [`00aae998`](#insn-00aae998) 範囲 `[['00aae998', '00aae9a7']]`
  - `CONDITIONAL_JUMP` [`00aae9a4`](#insn-00aae9a4) → [`00aae900`](#insn-00aae900)
  - `FALL_THROUGH` [`00aae9a4`](#insn-00aae9a4) → [`00aae9a8`](#insn-00aae9a8)
- ブロック [`00aae9a8`](#insn-00aae9a8) 範囲 `[['00aae9a8', '00aae9ab']]`
  - `UNCONDITIONAL_JUMP` [`00aae9a8`](#insn-00aae9a8) → [`00aae908`](#insn-00aae908)
- ブロック [`00aaea78`](#insn-00aaea78) 範囲 `[['00aaea78', '00aaea7b']]`

## 命令位置別の参照

- [`00aae6f0`](#insn-00aae6f0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae6f4`](#insn-00aae6f4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae6f8`](#insn-00aae6f8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae71c`](#insn-00aae71c) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae728`](#insn-00aae728) → `002a7377`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aae730`](#insn-00aae730) → `Stack[-0xff]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae734`](#insn-00aae734) → `Stack[-0xf8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae744`](#insn-00aae744) → `Stack[-0x10f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae74c`](#insn-00aae74c) → `002a738a`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aae750`](#insn-00aae750) → `Stack[-0xdf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae758`](#insn-00aae758) → `Stack[-0xd8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae768`](#insn-00aae768) → `Stack[-0xef]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae76c`](#insn-00aae76c) → `002a80e0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aae770`](#insn-00aae770) → `Stack[-0xbf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae778`](#insn-00aae778) → `Stack[-0xb8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae788`](#insn-00aae788) → `Stack[-0xcf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae78c`](#insn-00aae78c) → `002936ae`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aae790`](#insn-00aae790) → `Stack[-0x9f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae798`](#insn-00aae798) → `Stack[-0x98]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae7a4`](#insn-00aae7a4) → `Stack[-0xaf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae7a8`](#insn-00aae7a8) → `0029c36c`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aae7b0`](#insn-00aae7b0) → `Stack[-0x7f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae7b8`](#insn-00aae7b8) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae7c4`](#insn-00aae7c4) → `Stack[-0x8f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae7c8`](#insn-00aae7c8) → `00291877`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aae7d0`](#insn-00aae7d0) → `Stack[-0x5f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae7d8`](#insn-00aae7d8) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae7e4`](#insn-00aae7e4) → `Stack[-0x6f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae7e8`](#insn-00aae7e8) → `00294526`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aae7ec`](#insn-00aae7ec) → `Stack[-0x110]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae7f0`](#insn-00aae7f0) → `Stack[-0xf0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae7f4`](#insn-00aae7f4) → `Stack[-0xd0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae7f8`](#insn-00aae7f8) → `Stack[-0xb0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae7fc`](#insn-00aae7fc) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae800`](#insn-00aae800) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae804`](#insn-00aae804) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae80c`](#insn-00aae80c) → `Stack[-0x118]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae810`](#insn-00aae810) → `Stack[-0xfd]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae814`](#insn-00aae814) → `Stack[-0xdd]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae818`](#insn-00aae818) → `Stack[-0xbd]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae81c`](#insn-00aae81c) → `Stack[-0x9d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae820`](#insn-00aae820) → `Stack[-0x7d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae824`](#insn-00aae824) → `Stack[-0x5d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae828`](#insn-00aae828) → `Stack[-0x3f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae82c`](#insn-00aae82c) → `Stack[-0x4f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae830`](#insn-00aae830) → `Stack[-0x3d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae834`](#insn-00aae834) → `0109fb08`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aae838`](#insn-00aae838) → `0109fb00`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aae83c`](#insn-00aae83c) → `0109faf8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aae83c`](#insn-00aae83c) → `0109fb00`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aae848`](#insn-00aae848) → `0109faf8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aae84c`](#insn-00aae84c) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`00aae850`](#insn-00aae850) → `0109fb00`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aae85c`](#insn-00aae85c) → `0109faf8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aae860`](#insn-00aae860) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`00aae864`](#insn-00aae864) → `0109fb00`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aae870`](#insn-00aae870) → `0109faf8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aae874`](#insn-00aae874) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`00aae878`](#insn-00aae878) → `0109fb00`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aae884`](#insn-00aae884) → `0109faf8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aae888`](#insn-00aae888) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`00aae88c`](#insn-00aae88c) → `0109fb00`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aae898`](#insn-00aae898) → `0109faf8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aae89c`](#insn-00aae89c) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`00aae8a0`](#insn-00aae8a0) → `0109fb00`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aae8ac`](#insn-00aae8ac) → `0109faf8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aae8b0`](#insn-00aae8b0) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`00aae8b4`](#insn-00aae8b4) → `0109fb00`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aae8c0`](#insn-00aae8c0) → `0109faf8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aae8c4`](#insn-00aae8c4) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`00aae8c8`](#insn-00aae8c8) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae8cc`](#insn-00aae8cc) → [`00aae948`](#insn-00aae948) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae8d0`](#insn-00aae8d0) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae8d4`](#insn-00aae8d4) → [`00aae958`](#insn-00aae958) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae8d8`](#insn-00aae8d8) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae8dc`](#insn-00aae8dc) → [`00aae968`](#insn-00aae968) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae8e0`](#insn-00aae8e0) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae8e4`](#insn-00aae8e4) → [`00aae978`](#insn-00aae978) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae8e8`](#insn-00aae8e8) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae8ec`](#insn-00aae8ec) → [`00aae988`](#insn-00aae988) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae8f0`](#insn-00aae8f0) → `Stack[-0xf0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae8f4`](#insn-00aae8f4) → [`00aae998`](#insn-00aae998) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae8f8`](#insn-00aae8f8) → `Stack[-0x110]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae8fc`](#insn-00aae8fc) → [`00aae908`](#insn-00aae908) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae900`](#insn-00aae900) → `Stack[-0x100]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae904`](#insn-00aae904) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00aae90c`](#insn-00aae90c) → [`00418330`](../00418/00418330.md) · `PARAM` · `ANALYSIS` · 関数 `00418330` · 推定シンボル `None` · 推定型 `None`
- [`00aae914`](#insn-00aae914) → `0109faf8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aae91c`](#insn-00aae91c) → `00be5fd0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00aae920`](#insn-00aae920) → [`00bdafe0`](../00bda/00bdafe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdafe0` · 推定シンボル `None` · 推定型 `None`
- [`00aae928`](#insn-00aae928) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae930`](#insn-00aae930) → [`00aaea78`](#insn-00aaea78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae934`](#insn-00aae934) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae938`](#insn-00aae938) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae93c`](#insn-00aae93c) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae948`](#insn-00aae948) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae94c`](#insn-00aae94c) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00aae950`](#insn-00aae950) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae954`](#insn-00aae954) → [`00aae8d8`](#insn-00aae8d8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae958`](#insn-00aae958) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae95c`](#insn-00aae95c) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00aae960`](#insn-00aae960) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae964`](#insn-00aae964) → [`00aae8e0`](#insn-00aae8e0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae968`](#insn-00aae968) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae96c`](#insn-00aae96c) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00aae970`](#insn-00aae970) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae974`](#insn-00aae974) → [`00aae8e8`](#insn-00aae8e8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae978`](#insn-00aae978) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae97c`](#insn-00aae97c) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00aae980`](#insn-00aae980) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae984`](#insn-00aae984) → [`00aae8f0`](#insn-00aae8f0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae988`](#insn-00aae988) → `Stack[-0xc0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae98c`](#insn-00aae98c) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00aae990`](#insn-00aae990) → `Stack[-0xf0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae994`](#insn-00aae994) → [`00aae8f8`](#insn-00aae8f8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae998`](#insn-00aae998) → `Stack[-0xe0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae99c`](#insn-00aae99c) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00aae9a0`](#insn-00aae9a0) → `Stack[-0x110]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae9a4`](#insn-00aae9a4) → [`00aae900`](#insn-00aae900) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae9a8`](#insn-00aae9a8) → [`00aae908`](#insn-00aae908) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaea78`](#insn-00aaea78) → [`00bdb090`](../00bdb/00bdb090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb090` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aae6f0`](#insn-00aae6f0)

~~~json
{
  "source": "00aae6f0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae6f4`](#insn-00aae6f4)

~~~json
{
  "source": "00aae6f4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae6f8`](#insn-00aae6f8)

~~~json
{
  "source": "00aae6f8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae71c`](#insn-00aae71c)

~~~json
{
  "source": "00aae71c",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae728`](#insn-00aae728)

~~~json
{
  "source": "00aae728",
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
- 参照命令 [`00aae730`](#insn-00aae730)

~~~json
{
  "source": "00aae730",
  "target": "Stack[-0xff]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae734`](#insn-00aae734)

~~~json
{
  "source": "00aae734",
  "target": "Stack[-0xf8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae744`](#insn-00aae744)

~~~json
{
  "source": "00aae744",
  "target": "Stack[-0x10f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae74c`](#insn-00aae74c)

~~~json
{
  "source": "00aae74c",
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
- 参照命令 [`00aae750`](#insn-00aae750)

~~~json
{
  "source": "00aae750",
  "target": "Stack[-0xdf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae758`](#insn-00aae758)

~~~json
{
  "source": "00aae758",
  "target": "Stack[-0xd8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae768`](#insn-00aae768)

~~~json
{
  "source": "00aae768",
  "target": "Stack[-0xef]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae76c`](#insn-00aae76c)

~~~json
{
  "source": "00aae76c",
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
- 参照命令 [`00aae770`](#insn-00aae770)

~~~json
{
  "source": "00aae770",
  "target": "Stack[-0xbf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae778`](#insn-00aae778)

~~~json
{
  "source": "00aae778",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae788`](#insn-00aae788)

~~~json
{
  "source": "00aae788",
  "target": "Stack[-0xcf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae78c`](#insn-00aae78c)

~~~json
{
  "source": "00aae78c",
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
- 参照命令 [`00aae790`](#insn-00aae790)

~~~json
{
  "source": "00aae790",
  "target": "Stack[-0x9f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae798`](#insn-00aae798)

~~~json
{
  "source": "00aae798",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae7a4`](#insn-00aae7a4)

~~~json
{
  "source": "00aae7a4",
  "target": "Stack[-0xaf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae7a8`](#insn-00aae7a8)

~~~json
{
  "source": "00aae7a8",
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
- 参照命令 [`00aae7b0`](#insn-00aae7b0)

~~~json
{
  "source": "00aae7b0",
  "target": "Stack[-0x7f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae7b8`](#insn-00aae7b8)

~~~json
{
  "source": "00aae7b8",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae7c4`](#insn-00aae7c4)

~~~json
{
  "source": "00aae7c4",
  "target": "Stack[-0x8f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae7c8`](#insn-00aae7c8)

~~~json
{
  "source": "00aae7c8",
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
- 参照命令 [`00aae7d0`](#insn-00aae7d0)

~~~json
{
  "source": "00aae7d0",
  "target": "Stack[-0x5f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae7d8`](#insn-00aae7d8)

~~~json
{
  "source": "00aae7d8",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae7e4`](#insn-00aae7e4)

~~~json
{
  "source": "00aae7e4",
  "target": "Stack[-0x6f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae7e8`](#insn-00aae7e8)

~~~json
{
  "source": "00aae7e8",
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
- 参照命令 [`00aae7ec`](#insn-00aae7ec)

~~~json
{
  "source": "00aae7ec",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae7f0`](#insn-00aae7f0)

~~~json
{
  "source": "00aae7f0",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae7f4`](#insn-00aae7f4)

~~~json
{
  "source": "00aae7f4",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae7f8`](#insn-00aae7f8)

~~~json
{
  "source": "00aae7f8",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae7fc`](#insn-00aae7fc)

~~~json
{
  "source": "00aae7fc",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae800`](#insn-00aae800)

~~~json
{
  "source": "00aae800",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae804`](#insn-00aae804)

~~~json
{
  "source": "00aae804",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae80c`](#insn-00aae80c)

~~~json
{
  "source": "00aae80c",
  "target": "Stack[-0x118]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae810`](#insn-00aae810)

~~~json
{
  "source": "00aae810",
  "target": "Stack[-0xfd]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae814`](#insn-00aae814)

~~~json
{
  "source": "00aae814",
  "target": "Stack[-0xdd]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae818`](#insn-00aae818)

~~~json
{
  "source": "00aae818",
  "target": "Stack[-0xbd]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae81c`](#insn-00aae81c)

~~~json
{
  "source": "00aae81c",
  "target": "Stack[-0x9d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae820`](#insn-00aae820)

~~~json
{
  "source": "00aae820",
  "target": "Stack[-0x7d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae824`](#insn-00aae824)

~~~json
{
  "source": "00aae824",
  "target": "Stack[-0x5d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae828`](#insn-00aae828)

~~~json
{
  "source": "00aae828",
  "target": "Stack[-0x3f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae82c`](#insn-00aae82c)

~~~json
{
  "source": "00aae82c",
  "target": "Stack[-0x4f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae830`](#insn-00aae830)

~~~json
{
  "source": "00aae830",
  "target": "Stack[-0x3d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae834`](#insn-00aae834)

~~~json
{
  "source": "00aae834",
  "target": "0109fb08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fb08",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aae838`](#insn-00aae838)

~~~json
{
  "source": "00aae838",
  "target": "0109fb00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fb00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aae83c`](#insn-00aae83c)

~~~json
{
  "source": "00aae83c",
  "target": "0109faf8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109faf8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aae83c`](#insn-00aae83c)

~~~json
{
  "source": "00aae83c",
  "target": "0109fb00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fb00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aae848`](#insn-00aae848)

~~~json
{
  "source": "00aae848",
  "target": "0109faf8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109faf8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aae84c`](#insn-00aae84c)

~~~json
{
  "source": "00aae84c",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aae850`](#insn-00aae850)

~~~json
{
  "source": "00aae850",
  "target": "0109fb00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fb00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aae85c`](#insn-00aae85c)

~~~json
{
  "source": "00aae85c",
  "target": "0109faf8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109faf8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aae860`](#insn-00aae860)

~~~json
{
  "source": "00aae860",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aae864`](#insn-00aae864)

~~~json
{
  "source": "00aae864",
  "target": "0109fb00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fb00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aae870`](#insn-00aae870)

~~~json
{
  "source": "00aae870",
  "target": "0109faf8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109faf8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aae874`](#insn-00aae874)

~~~json
{
  "source": "00aae874",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aae878`](#insn-00aae878)

~~~json
{
  "source": "00aae878",
  "target": "0109fb00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fb00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aae884`](#insn-00aae884)

~~~json
{
  "source": "00aae884",
  "target": "0109faf8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109faf8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aae888`](#insn-00aae888)

~~~json
{
  "source": "00aae888",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aae88c`](#insn-00aae88c)

~~~json
{
  "source": "00aae88c",
  "target": "0109fb00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fb00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aae898`](#insn-00aae898)

~~~json
{
  "source": "00aae898",
  "target": "0109faf8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109faf8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aae89c`](#insn-00aae89c)

~~~json
{
  "source": "00aae89c",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aae8a0`](#insn-00aae8a0)

~~~json
{
  "source": "00aae8a0",
  "target": "0109fb00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fb00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aae8ac`](#insn-00aae8ac)

~~~json
{
  "source": "00aae8ac",
  "target": "0109faf8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109faf8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aae8b0`](#insn-00aae8b0)

~~~json
{
  "source": "00aae8b0",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aae8b4`](#insn-00aae8b4)

~~~json
{
  "source": "00aae8b4",
  "target": "0109fb00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fb00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aae8c0`](#insn-00aae8c0)

~~~json
{
  "source": "00aae8c0",
  "target": "0109faf8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109faf8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aae8c4`](#insn-00aae8c4)

~~~json
{
  "source": "00aae8c4",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aae8c8`](#insn-00aae8c8)

~~~json
{
  "source": "00aae8c8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae8cc`](#insn-00aae8cc)

~~~json
{
  "source": "00aae8cc",
  "target": "00aae948",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae8d0`](#insn-00aae8d0)

~~~json
{
  "source": "00aae8d0",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae8d4`](#insn-00aae8d4)

~~~json
{
  "source": "00aae8d4",
  "target": "00aae958",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae8d8`](#insn-00aae8d8)

~~~json
{
  "source": "00aae8d8",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae8dc`](#insn-00aae8dc)

~~~json
{
  "source": "00aae8dc",
  "target": "00aae968",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae8e0`](#insn-00aae8e0)

~~~json
{
  "source": "00aae8e0",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae8e4`](#insn-00aae8e4)

~~~json
{
  "source": "00aae8e4",
  "target": "00aae978",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae8e8`](#insn-00aae8e8)

~~~json
{
  "source": "00aae8e8",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae8ec`](#insn-00aae8ec)

~~~json
{
  "source": "00aae8ec",
  "target": "00aae988",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae8f0`](#insn-00aae8f0)

~~~json
{
  "source": "00aae8f0",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae8f4`](#insn-00aae8f4)

~~~json
{
  "source": "00aae8f4",
  "target": "00aae998",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae8f8`](#insn-00aae8f8)

~~~json
{
  "source": "00aae8f8",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae8fc`](#insn-00aae8fc)

~~~json
{
  "source": "00aae8fc",
  "target": "00aae908",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae900`](#insn-00aae900)

~~~json
{
  "source": "00aae900",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae904`](#insn-00aae904)

~~~json
{
  "source": "00aae904",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aae90c`](#insn-00aae90c)

~~~json
{
  "source": "00aae90c",
  "target": "00418330",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aae914`](#insn-00aae914)

~~~json
{
  "source": "00aae914",
  "target": "0109faf8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109faf8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aae91c`](#insn-00aae91c)

~~~json
{
  "source": "00aae91c",
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
- 参照命令 [`00aae920`](#insn-00aae920)

~~~json
{
  "source": "00aae920",
  "target": "00bdafe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aae928`](#insn-00aae928)

~~~json
{
  "source": "00aae928",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae930`](#insn-00aae930)

~~~json
{
  "source": "00aae930",
  "target": "00aaea78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae934`](#insn-00aae934)

~~~json
{
  "source": "00aae934",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae938`](#insn-00aae938)

~~~json
{
  "source": "00aae938",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae93c`](#insn-00aae93c)

~~~json
{
  "source": "00aae93c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae948`](#insn-00aae948)

~~~json
{
  "source": "00aae948",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae94c`](#insn-00aae94c)

~~~json
{
  "source": "00aae94c",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aae950`](#insn-00aae950)

~~~json
{
  "source": "00aae950",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae954`](#insn-00aae954)

~~~json
{
  "source": "00aae954",
  "target": "00aae8d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae958`](#insn-00aae958)

~~~json
{
  "source": "00aae958",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae95c`](#insn-00aae95c)

~~~json
{
  "source": "00aae95c",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aae960`](#insn-00aae960)

~~~json
{
  "source": "00aae960",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae964`](#insn-00aae964)

~~~json
{
  "source": "00aae964",
  "target": "00aae8e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae968`](#insn-00aae968)

~~~json
{
  "source": "00aae968",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae96c`](#insn-00aae96c)

~~~json
{
  "source": "00aae96c",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aae970`](#insn-00aae970)

~~~json
{
  "source": "00aae970",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae974`](#insn-00aae974)

~~~json
{
  "source": "00aae974",
  "target": "00aae8e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae978`](#insn-00aae978)

~~~json
{
  "source": "00aae978",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae97c`](#insn-00aae97c)

~~~json
{
  "source": "00aae97c",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aae980`](#insn-00aae980)

~~~json
{
  "source": "00aae980",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae984`](#insn-00aae984)

~~~json
{
  "source": "00aae984",
  "target": "00aae8f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae988`](#insn-00aae988)

~~~json
{
  "source": "00aae988",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae98c`](#insn-00aae98c)

~~~json
{
  "source": "00aae98c",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aae990`](#insn-00aae990)

~~~json
{
  "source": "00aae990",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae994`](#insn-00aae994)

~~~json
{
  "source": "00aae994",
  "target": "00aae8f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae998`](#insn-00aae998)

~~~json
{
  "source": "00aae998",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae99c`](#insn-00aae99c)

~~~json
{
  "source": "00aae99c",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aae9a0`](#insn-00aae9a0)

~~~json
{
  "source": "00aae9a0",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae9a4`](#insn-00aae9a4)

~~~json
{
  "source": "00aae9a4",
  "target": "00aae900",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae9a8`](#insn-00aae9a8)

~~~json
{
  "source": "00aae9a8",
  "target": "00aae908",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaea78`](#insn-00aaea78)

~~~json
{
  "source": "00aaea78",
  "target": "00bdb090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
