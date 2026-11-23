# 00acf3cc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00acf494`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acf/00acf494.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0056.md#compare-263900beb4296e5a1f6b360ff98d1cf4)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acf3cc",
  "name": "_INIT_253",
  "size": 708,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1e0b2ce12da56acd15cf01f7507c0be088d68c4363c6c647eefb73e832f21454",
  "source_text_sha256": "1e0b2ce12da56acd15cf01f7507c0be088d68c4363c6c647eefb73e832f21454",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00acf3cc",
        "00acf68b"
      ],
      [
        "00acf758",
        "00acf75b"
      ]
    ],
    "bytes_sha256": "cf5d7cf97b9c3a4f6584166eab81569487ffb8fcdb4e3572e270d8bcdb13b7c3",
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
- [00bdaee0](../00bda/00bdaee0.md)
- [00bdaf60](../00bda/00bdaf60.md)
- [00bdaf90](../00bda/00bdaf90.md)

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

## 疑似コード / UTF-8 4860 bytes

~~~c

/* WARNING: Type propagation algorithm not settling */

void _INIT_253(void)

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
  uStack_107 = (undefined7)s_CgkIjM3y_ZQaEAIQAg_002a72e4._8_8_;
  cStack_100 = SUB81(s_CgkIjM3y_ZQaEAIQAg_002a72e4._8_8_,7);
  local_10f = (char  [8])s_CgkIjM3y_ZQaEAIQAg_002a72e4._0_8_;
  uStack_df = 0x4142;
  local_d8[0] = 2;
  uStack_e7 = (undefined7)s_CgkIjM3y_ZQaEAIQBA_002a72f7._8_8_;
  cStack_e0 = SUB81(s_CgkIjM3y_ZQaEAIQBA_002a72f7._8_8_,7);
  local_ef = (char  [8])s_CgkIjM3y_ZQaEAIQBA_002a72f7._0_8_;
  uStack_bf = 0x6742;
  local_b8[0] = 3;
  uStack_c7 = (undefined7)s_CgkIjM3y_ZQaEAIQBg_002a80da._8_8_;
  cStack_c0 = SUB81(s_CgkIjM3y_ZQaEAIQBg_002a80da._8_8_,7);
  local_cf = (char  [8])s_CgkIjM3y_ZQaEAIQBg_002a80da._0_8_;
  uStack_9f = 0x7741;
  local_98[0] = 4;
  uStack_a7 = (undefined7)s_CgkIjM3y_ZQaEAIQAw_002936ae._8_8_;
  cStack_a0 = SUB81(s_CgkIjM3y_ZQaEAIQAw_002936ae._8_8_,7);
  local_af = (char  [8])s_CgkIjM3y_ZQaEAIQAw_002936ae._0_8_;
  uStack_7f = 0x5142;
  local_78[0] = 5;
  uStack_87 = (undefined7)s_CgkIjM3y_ZQaEAIQBQ_0029c2e1._8_8_;
  cStack_80 = SUB81(s_CgkIjM3y_ZQaEAIQBQ_0029c2e1._8_8_,7);
  local_8f = (char  [8])s_CgkIjM3y_ZQaEAIQBQ_0029c2e1._0_8_;
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
  DAT_0109faf8 = 0;
  DAT_0109faf0 = 0;
  DAT_0109fae8 = &DAT_0109faf0;
  FUN_00418cb8(&DAT_0109fae8,&DAT_0109faf0,local_118,local_118);
  FUN_00418cb8(&DAT_0109fae8,&DAT_0109faf0,local_f8,local_f8);
  FUN_00418cb8(&DAT_0109fae8,&DAT_0109faf0,local_d8,local_d8);
  FUN_00418cb8(&DAT_0109fae8,&DAT_0109faf0,local_b8,local_b8);
  FUN_00418cb8(&DAT_0109fae8,&DAT_0109faf0,local_98,local_98);
  FUN_00418cb8(&DAT_0109fae8,&DAT_0109faf0,local_78,local_78);
  FUN_00418cb8(&DAT_0109fae8,&DAT_0109faf0,local_58,local_58);
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
  __cxa_atexit(FUN_00418330,&DAT_0109fae8,&PTR_LOOP_00be5ed0);
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
<a id="insn-00acf3cc"></a> `00acf3cc` | `ff 83 04 d1` | sub sp,sp,#0x120 | `FALL_THROUGH`
<a id="insn-00acf3d0"></a> `00acf3d0` | `fd 7b 0f a9` | stp x29,x30,[sp, #0xf0] | `FALL_THROUGH`
<a id="insn-00acf3d4"></a> `00acf3d4` | `fc 57 10 a9` | stp x28,x21,[sp, #0x100] | `FALL_THROUGH`
<a id="insn-00acf3d8"></a> `00acf3d8` | `f4 4f 11 a9` | stp x20,x19,[sp, #0x110] | `FALL_THROUGH`
<a id="insn-00acf3dc"></a> `00acf3dc` | `fd c3 03 91` | add x29,sp,#0xf0 | `FALL_THROUGH`
<a id="insn-00acf3e0"></a> `00acf3e0` | `55 d0 3b d5` | mrs x21,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00acf3e4"></a> `00acf3e4` | `2a e8 8c 52` | mov w10,#0x6741 | `FALL_THROUGH`
<a id="insn-00acf3e8"></a> `00acf3e8` | `f4 23 00 91` | add x20,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00acf3ec"></a> `00acf3ec` | `a9 16 40 f9` | ldr x9,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00acf3f0"></a> `00acf3f0` | `88 04 80 52` | mov w8,#0x24 | `FALL_THROUGH`
<a id="insn-00acf3f4"></a> `00acf3f4` | `93 2e 00 90` | adrp x19,0x109f000 | `FALL_THROUGH`
<a id="insn-00acf3f8"></a> `00acf3f8` | `73 a2 2b 91` | add x19,x19,#0xae8 | `FALL_THROUGH`
<a id="insn-00acf3fc"></a> `00acf3fc` | `a9 83 1f f8` | stur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00acf400"></a> `00acf400` | `c9 be ff 90` | adrp x9,0x2a7000 | `FALL_THROUGH`
<a id="insn-00acf404"></a> `00acf404` | `29 91 0b 91` | add x9,x9,#0x2e4 | `FALL_THROUGH`
<a id="insn-00acf408"></a> `00acf408` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00acf40c"></a> `00acf40c` | `29 00 80 52` | mov w9,#0x1 | `FALL_THROUGH`
<a id="insn-00acf410"></a> `00acf410` | `ea 13 02 78` | sturh w10,[sp, #0x21] | `FALL_THROUGH`
<a id="insn-00acf414"></a> `00acf414` | `e9 2b 00 b9` | str w9,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00acf418"></a> `00acf418` | `49 28 88 52` | mov w9,#0x4142 | `FALL_THROUGH`
<a id="insn-00acf41c"></a> `00acf41c` | `ca be ff 90` | adrp x10,0x2a7000 | `FALL_THROUGH`
<a id="insn-00acf420"></a> `00acf420` | `4a dd 0b 91` | add x10,x10,#0x2f7 | `FALL_THROUGH`
<a id="insn-00acf424"></a> `00acf424` | `e0 13 81 3c` | stur q0,[sp, #0x11] | `FALL_THROUGH`
<a id="insn-00acf428"></a> `00acf428` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00acf42c"></a> `00acf42c` | `40 01 c0 3d` | ldr q0,[x10] | `FALL_THROUGH`
<a id="insn-00acf430"></a> `00acf430` | `e9 13 04 78` | sturh w9,[sp, #0x41] | `FALL_THROUGH`
<a id="insn-00acf434"></a> `00acf434` | `49 00 80 52` | mov w9,#0x2 | `FALL_THROUGH`
<a id="insn-00acf438"></a> `00acf438` | `e9 4b 00 b9` | str w9,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00acf43c"></a> `00acf43c` | `49 e8 8c 52` | mov w9,#0x6742 | `FALL_THROUGH`
<a id="insn-00acf440"></a> `00acf440` | `ca be ff b0` | adrp x10,0x2a8000 | `FALL_THROUGH`
<a id="insn-00acf444"></a> `00acf444` | `4a 69 03 91` | add x10,x10,#0xda | `FALL_THROUGH`
<a id="insn-00acf448"></a> `00acf448` | `e0 13 83 3c` | stur q0,[sp, #0x31] | `FALL_THROUGH`
<a id="insn-00acf44c"></a> `00acf44c` | `40 01 c0 3d` | ldr q0,[x10] | `FALL_THROUGH`
<a id="insn-00acf450"></a> `00acf450` | `e9 13 06 78` | sturh w9,[sp, #0x61] | `FALL_THROUGH`
<a id="insn-00acf454"></a> `00acf454` | `69 00 80 52` | mov w9,#0x3 | `FALL_THROUGH`
<a id="insn-00acf458"></a> `00acf458` | `e9 6b 00 b9` | str w9,[sp, #0x68] | `FALL_THROUGH`
<a id="insn-00acf45c"></a> `00acf45c` | `29 e8 8e 52` | mov w9,#0x7741 | `FALL_THROUGH`
<a id="insn-00acf460"></a> `00acf460` | `2a be ff 90` | adrp x10,0x293000 | `FALL_THROUGH`
<a id="insn-00acf464"></a> `00acf464` | `4a b9 1a 91` | add x10,x10,#0x6ae | `FALL_THROUGH`
<a id="insn-00acf468"></a> `00acf468` | `e0 13 85 3c` | stur q0,[sp, #0x51] | `FALL_THROUGH`
<a id="insn-00acf46c"></a> `00acf46c` | `40 01 c0 3d` | ldr q0,[x10] | `FALL_THROUGH`
<a id="insn-00acf470"></a> `00acf470` | `e9 13 08 78` | sturh w9,[sp, #0x81] | `FALL_THROUGH`
<a id="insn-00acf474"></a> `00acf474` | `89 00 80 52` | mov w9,#0x4 | `FALL_THROUGH`
<a id="insn-00acf478"></a> `00acf478` | `e9 8b 00 b9` | str w9,[sp, #0x88] | `FALL_THROUGH`
<a id="insn-00acf47c"></a> `00acf47c` | `69 be ff b0` | adrp x9,0x29c000 | `FALL_THROUGH`
<a id="insn-00acf480"></a> `00acf480` | `29 85 0b 91` | add x9,x9,#0x2e1 | `FALL_THROUGH`
<a id="insn-00acf484"></a> `00acf484` | `e0 13 87 3c` | stur q0,[sp, #0x71] | `FALL_THROUGH`
<a id="insn-00acf488"></a> `00acf488` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00acf48c"></a> `00acf48c` | `49 28 8a 52` | mov w9,#0x5142 | `FALL_THROUGH`
<a id="insn-00acf490"></a> `00acf490` | `89 92 09 78` | sturh w9,[x20, #0x99] | `FALL_THROUGH`
<a id="insn-00acf494"></a> `00acf494` | `a9 00 80 52` | mov w9,#0x5 | `FALL_THROUGH`
<a id="insn-00acf498"></a> `00acf498` | `e9 ab 00 b9` | str w9,[sp, #0xa8] | `FALL_THROUGH`
<a id="insn-00acf49c"></a> `00acf49c` | `09 be ff d0` | adrp x9,0x291000 | `FALL_THROUGH`
<a id="insn-00acf4a0"></a> `00acf4a0` | `29 dd 21 91` | add x9,x9,#0x877 | `FALL_THROUGH`
<a id="insn-00acf4a4"></a> `00acf4a4` | `80 92 88 3c` | stur q0,[x20, #0x89] | `FALL_THROUGH`
<a id="insn-00acf4a8"></a> `00acf4a8` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00acf4ac"></a> `00acf4ac` | `49 e8 8e 52` | mov w9,#0x7742 | `FALL_THROUGH`
<a id="insn-00acf4b0"></a> `00acf4b0` | `89 92 0b 78` | sturh w9,[x20, #0xb9] | `FALL_THROUGH`
<a id="insn-00acf4b4"></a> `00acf4b4` | `c9 00 80 52` | mov w9,#0x6 | `FALL_THROUGH`
<a id="insn-00acf4b8"></a> `00acf4b8` | `e9 cb 00 b9` | str w9,[sp, #0xc8] | `FALL_THROUGH`
<a id="insn-00acf4bc"></a> `00acf4bc` | `29 be ff b0` | adrp x9,0x294000 | `FALL_THROUGH`
<a id="insn-00acf4c0"></a> `00acf4c0` | `29 99 14 91` | add x9,x9,#0x526 | `FALL_THROUGH`
<a id="insn-00acf4c4"></a> `00acf4c4` | `80 92 8a 3c` | stur q0,[x20, #0xa9] | `FALL_THROUGH`
<a id="insn-00acf4c8"></a> `00acf4c8` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00acf4cc"></a> `00acf4cc` | `e8 43 00 39` | strb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acf4d0"></a> `00acf4d0` | `e8 c3 00 39` | strb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00acf4d4"></a> `00acf4d4` | `e8 43 01 39` | strb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00acf4d8"></a> `00acf4d8` | `e8 c3 01 39` | strb w8,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00acf4dc"></a> `00acf4dc` | `e8 43 02 39` | strb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00acf4e0"></a> `00acf4e0` | `e8 c3 02 39` | strb w8,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00acf4e4"></a> `00acf4e4` | `e8 43 03 39` | strb w8,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-00acf4e8"></a> `00acf4e8` | `68 28 88 52` | mov w8,#0x4143 | `FALL_THROUGH`
<a id="insn-00acf4ec"></a> `00acf4ec` | `ff 0b 00 b9` | str wzr,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00acf4f0"></a> `00acf4f0` | `ff 8f 00 39` | strb wzr,[sp, #0x23] | `FALL_THROUGH`
<a id="insn-00acf4f4"></a> `00acf4f4` | `ff 0f 01 39` | strb wzr,[sp, #0x43] | `FALL_THROUGH`
<a id="insn-00acf4f8"></a> `00acf4f8` | `ff 8f 01 39` | strb wzr,[sp, #0x63] | `FALL_THROUGH`
<a id="insn-00acf4fc"></a> `00acf4fc` | `ff 0f 02 39` | strb wzr,[sp, #0x83] | `FALL_THROUGH`
<a id="insn-00acf500"></a> `00acf500` | `ff 8f 02 39` | strb wzr,[sp, #0xa3] | `FALL_THROUGH`
<a id="insn-00acf504"></a> `00acf504` | `ff 0f 03 39` | strb wzr,[sp, #0xc3] | `FALL_THROUGH`
<a id="insn-00acf508"></a> `00acf508` | `88 92 0d 78` | sturh w8,[x20, #0xd9] | `FALL_THROUGH`
<a id="insn-00acf50c"></a> `00acf50c` | `80 92 8c 3c` | stur q0,[x20, #0xc9] | `FALL_THROUGH`
<a id="insn-00acf510"></a> `00acf510` | `ff 8f 03 39` | strb wzr,[sp, #0xe3] | `FALL_THROUGH`
<a id="insn-00acf514"></a> `00acf514` | `7f 0a 00 f9` | str xzr,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00acf518"></a> `00acf518` | `3f 8c 00 f8` | str xzr,[x1, #0x8]! | `FALL_THROUGH`
<a id="insn-00acf51c"></a> `00acf51c` | `61 02 00 f9` | str x1,[x19] | `FALL_THROUGH`
<a id="insn-00acf520"></a> `00acf520` | `e2 23 00 91` | add x2,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00acf524"></a> `00acf524` | `e3 23 00 91` | add x3,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00acf528"></a> `00acf528` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00acf52c"></a> `00acf52c` | `e3 25 e5 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-00acf530"></a> `00acf530` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00acf534"></a> `00acf534` | `82 82 00 91` | add x2,x20,#0x20 | `FALL_THROUGH`
<a id="insn-00acf538"></a> `00acf538` | `83 82 00 91` | add x3,x20,#0x20 | `FALL_THROUGH`
<a id="insn-00acf53c"></a> `00acf53c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00acf540"></a> `00acf540` | `de 25 e5 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-00acf544"></a> `00acf544` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00acf548"></a> `00acf548` | `82 02 01 91` | add x2,x20,#0x40 | `FALL_THROUGH`
<a id="insn-00acf54c"></a> `00acf54c` | `83 02 01 91` | add x3,x20,#0x40 | `FALL_THROUGH`
<a id="insn-00acf550"></a> `00acf550` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00acf554"></a> `00acf554` | `d9 25 e5 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-00acf558"></a> `00acf558` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00acf55c"></a> `00acf55c` | `82 82 01 91` | add x2,x20,#0x60 | `FALL_THROUGH`
<a id="insn-00acf560"></a> `00acf560` | `83 82 01 91` | add x3,x20,#0x60 | `FALL_THROUGH`
<a id="insn-00acf564"></a> `00acf564` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00acf568"></a> `00acf568` | `d4 25 e5 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-00acf56c"></a> `00acf56c` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00acf570"></a> `00acf570` | `82 02 02 91` | add x2,x20,#0x80 | `FALL_THROUGH`
<a id="insn-00acf574"></a> `00acf574` | `83 02 02 91` | add x3,x20,#0x80 | `FALL_THROUGH`
<a id="insn-00acf578"></a> `00acf578` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00acf57c"></a> `00acf57c` | `cf 25 e5 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-00acf580"></a> `00acf580` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00acf584"></a> `00acf584` | `82 82 02 91` | add x2,x20,#0xa0 | `FALL_THROUGH`
<a id="insn-00acf588"></a> `00acf588` | `83 82 02 91` | add x3,x20,#0xa0 | `FALL_THROUGH`
<a id="insn-00acf58c"></a> `00acf58c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00acf590"></a> `00acf590` | `ca 25 e5 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-00acf594"></a> `00acf594` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00acf598"></a> `00acf598` | `82 02 03 91` | add x2,x20,#0xc0 | `FALL_THROUGH`
<a id="insn-00acf59c"></a> `00acf59c` | `83 02 03 91` | add x3,x20,#0xc0 | `FALL_THROUGH`
<a id="insn-00acf5a0"></a> `00acf5a0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00acf5a4"></a> `00acf5a4` | `c5 25 e5 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-00acf5a8"></a> `00acf5a8` | `e8 43 43 39` | ldrb w8,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-00acf5ac"></a> `00acf5ac` | `e8 03 00 37` | tbnz w8,#0x0,0x00acf628 | `CONDITIONAL_JUMP`
<a id="insn-00acf5b0"></a> `00acf5b0` | `e8 c3 42 39` | ldrb w8,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00acf5b4"></a> `00acf5b4` | `28 04 00 37` | tbnz w8,#0x0,0x00acf638 | `CONDITIONAL_JUMP`
<a id="insn-00acf5b8"></a> `00acf5b8` | `e8 43 42 39` | ldrb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00acf5bc"></a> `00acf5bc` | `68 04 00 37` | tbnz w8,#0x0,0x00acf648 | `CONDITIONAL_JUMP`
<a id="insn-00acf5c0"></a> `00acf5c0` | `e8 c3 41 39` | ldrb w8,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00acf5c4"></a> `00acf5c4` | `a8 04 00 37` | tbnz w8,#0x0,0x00acf658 | `CONDITIONAL_JUMP`
<a id="insn-00acf5c8"></a> `00acf5c8` | `e8 43 41 39` | ldrb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00acf5cc"></a> `00acf5cc` | `e8 04 00 37` | tbnz w8,#0x0,0x00acf668 | `CONDITIONAL_JUMP`
<a id="insn-00acf5d0"></a> `00acf5d0` | `e8 c3 40 39` | ldrb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00acf5d4"></a> `00acf5d4` | `28 05 00 37` | tbnz w8,#0x0,0x00acf678 | `CONDITIONAL_JUMP`
<a id="insn-00acf5d8"></a> `00acf5d8` | `e8 43 40 39` | ldrb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acf5dc"></a> `00acf5dc` | `68 00 00 36` | tbz w8,#0x0,0x00acf5e8 | `CONDITIONAL_JUMP`
<a id="insn-00acf5e0"></a> `00acf5e0` | `e0 13 40 f9` | ldr x0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00acf5e4"></a> `00acf5e4` | `5f 2e 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00acf5e8"></a> `00acf5e8` | `40 ca ff b0` | adrp x0,0x418000 | `FALL_THROUGH`
<a id="insn-00acf5ec"></a> `00acf5ec` | `00 c0 0c 91` | add x0,x0,#0x330 | `FALL_THROUGH`
<a id="insn-00acf5f0"></a> `00acf5f0` | `81 2e 00 90` | adrp x1,0x109f000 | `FALL_THROUGH`
<a id="insn-00acf5f4"></a> `00acf5f4` | `21 a0 2b 91` | add x1,x1,#0xae8 | `FALL_THROUGH`
<a id="insn-00acf5f8"></a> `00acf5f8` | `a2 08 00 d0` | adrp x2,0xbe5000 | `FALL_THROUGH`
<a id="insn-00acf5fc"></a> `00acf5fc` | `42 40 3b 91` | add x2,x2,#0xed0 | `FALL_THROUGH`
<a id="insn-00acf600"></a> `00acf600` | `38 2e 04 94` | bl 0x00bdaee0 | `UNCONDITIONAL_CALL`
<a id="insn-00acf604"></a> `00acf604` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00acf608"></a> `00acf608` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00acf60c"></a> `00acf60c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00acf610"></a> `00acf610` | `41 0a 00 54` | b.ne 0x00acf758 | `CONDITIONAL_JUMP`
<a id="insn-00acf614"></a> `00acf614` | `f4 4f 51 a9` | ldp x20,x19,[sp, #0x110] | `FALL_THROUGH`
<a id="insn-00acf618"></a> `00acf618` | `fc 57 50 a9` | ldp x28,x21,[sp, #0x100] | `FALL_THROUGH`
<a id="insn-00acf61c"></a> `00acf61c` | `fd 7b 4f a9` | ldp x29,x30,[sp, #0xf0] | `FALL_THROUGH`
<a id="insn-00acf620"></a> `00acf620` | `ff 83 04 91` | add sp,sp,#0x120 | `FALL_THROUGH`
<a id="insn-00acf624"></a> `00acf624` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00acf628"></a> `00acf628` | `e0 73 40 f9` | ldr x0,[sp, #0xe0] | `FALL_THROUGH`
<a id="insn-00acf62c"></a> `00acf62c` | `4d 2e 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00acf630"></a> `00acf630` | `e8 c3 42 39` | ldrb w8,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00acf634"></a> `00acf634` | `28 fc 07 36` | tbz w8,#0x0,0x00acf5b8 | `CONDITIONAL_JUMP`
<a id="insn-00acf638"></a> `00acf638` | `e0 63 40 f9` | ldr x0,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00acf63c"></a> `00acf63c` | `49 2e 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00acf640"></a> `00acf640` | `e8 43 42 39` | ldrb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00acf644"></a> `00acf644` | `e8 fb 07 36` | tbz w8,#0x0,0x00acf5c0 | `CONDITIONAL_JUMP`
<a id="insn-00acf648"></a> `00acf648` | `e0 53 40 f9` | ldr x0,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00acf64c"></a> `00acf64c` | `45 2e 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00acf650"></a> `00acf650` | `e8 c3 41 39` | ldrb w8,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00acf654"></a> `00acf654` | `a8 fb 07 36` | tbz w8,#0x0,0x00acf5c8 | `CONDITIONAL_JUMP`
<a id="insn-00acf658"></a> `00acf658` | `e0 43 40 f9` | ldr x0,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00acf65c"></a> `00acf65c` | `41 2e 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00acf660"></a> `00acf660` | `e8 43 41 39` | ldrb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00acf664"></a> `00acf664` | `68 fb 07 36` | tbz w8,#0x0,0x00acf5d0 | `CONDITIONAL_JUMP`
<a id="insn-00acf668"></a> `00acf668` | `e0 33 40 f9` | ldr x0,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00acf66c"></a> `00acf66c` | `3d 2e 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00acf670"></a> `00acf670` | `e8 c3 40 39` | ldrb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00acf674"></a> `00acf674` | `28 fb 07 36` | tbz w8,#0x0,0x00acf5d8 | `CONDITIONAL_JUMP`
<a id="insn-00acf678"></a> `00acf678` | `e0 23 40 f9` | ldr x0,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00acf67c"></a> `00acf67c` | `39 2e 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00acf680"></a> `00acf680` | `e8 43 40 39` | ldrb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acf684"></a> `00acf684` | `e8 fa 07 37` | tbnz w8,#0x0,0x00acf5e0 | `CONDITIONAL_JUMP`
<a id="insn-00acf688"></a> `00acf688` | `d8 ff ff 17` | b 0x00acf5e8 | `UNCONDITIONAL_JUMP`
<a id="insn-00acf758"></a> `00acf758` | `0e 2e 04 94` | bl 0x00bdaf90 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00acf3cc`](#insn-00acf3cc) 範囲 `[['00acf3cc', '00acf5af']]`
  - `CONDITIONAL_JUMP` [`00acf5ac`](#insn-00acf5ac) → [`00acf628`](#insn-00acf628)
  - `FALL_THROUGH` [`00acf5ac`](#insn-00acf5ac) → [`00acf5b0`](#insn-00acf5b0)
- ブロック [`00acf5b0`](#insn-00acf5b0) 範囲 `[['00acf5b0', '00acf5b7']]`
  - `CONDITIONAL_JUMP` [`00acf5b4`](#insn-00acf5b4) → [`00acf638`](#insn-00acf638)
  - `FALL_THROUGH` [`00acf5b4`](#insn-00acf5b4) → [`00acf5b8`](#insn-00acf5b8)
- ブロック [`00acf5b8`](#insn-00acf5b8) 範囲 `[['00acf5b8', '00acf5bf']]`
  - `CONDITIONAL_JUMP` [`00acf5bc`](#insn-00acf5bc) → [`00acf648`](#insn-00acf648)
  - `FALL_THROUGH` [`00acf5bc`](#insn-00acf5bc) → [`00acf5c0`](#insn-00acf5c0)
- ブロック [`00acf5c0`](#insn-00acf5c0) 範囲 `[['00acf5c0', '00acf5c7']]`
  - `CONDITIONAL_JUMP` [`00acf5c4`](#insn-00acf5c4) → [`00acf658`](#insn-00acf658)
  - `FALL_THROUGH` [`00acf5c4`](#insn-00acf5c4) → [`00acf5c8`](#insn-00acf5c8)
- ブロック [`00acf5c8`](#insn-00acf5c8) 範囲 `[['00acf5c8', '00acf5cf']]`
  - `CONDITIONAL_JUMP` [`00acf5cc`](#insn-00acf5cc) → [`00acf668`](#insn-00acf668)
  - `FALL_THROUGH` [`00acf5cc`](#insn-00acf5cc) → [`00acf5d0`](#insn-00acf5d0)
- ブロック [`00acf5d0`](#insn-00acf5d0) 範囲 `[['00acf5d0', '00acf5d7']]`
  - `CONDITIONAL_JUMP` [`00acf5d4`](#insn-00acf5d4) → [`00acf678`](#insn-00acf678)
  - `FALL_THROUGH` [`00acf5d4`](#insn-00acf5d4) → [`00acf5d8`](#insn-00acf5d8)
- ブロック [`00acf5d8`](#insn-00acf5d8) 範囲 `[['00acf5d8', '00acf5df']]`
  - `CONDITIONAL_JUMP` [`00acf5dc`](#insn-00acf5dc) → [`00acf5e8`](#insn-00acf5e8)
  - `FALL_THROUGH` [`00acf5dc`](#insn-00acf5dc) → [`00acf5e0`](#insn-00acf5e0)
- ブロック [`00acf5e0`](#insn-00acf5e0) 範囲 `[['00acf5e0', '00acf5e7']]`
  - `FALL_THROUGH` [`00acf5e4`](#insn-00acf5e4) → [`00acf5e8`](#insn-00acf5e8)
- ブロック [`00acf5e8`](#insn-00acf5e8) 範囲 `[['00acf5e8', '00acf613']]`
  - `CONDITIONAL_JUMP` [`00acf610`](#insn-00acf610) → [`00acf758`](#insn-00acf758)
  - `FALL_THROUGH` [`00acf610`](#insn-00acf610) → [`00acf614`](#insn-00acf614)
- ブロック [`00acf614`](#insn-00acf614) 範囲 `[['00acf614', '00acf627']]`
- ブロック [`00acf628`](#insn-00acf628) 範囲 `[['00acf628', '00acf637']]`
  - `CONDITIONAL_JUMP` [`00acf634`](#insn-00acf634) → [`00acf5b8`](#insn-00acf5b8)
  - `FALL_THROUGH` [`00acf634`](#insn-00acf634) → [`00acf638`](#insn-00acf638)
- ブロック [`00acf638`](#insn-00acf638) 範囲 `[['00acf638', '00acf647']]`
  - `CONDITIONAL_JUMP` [`00acf644`](#insn-00acf644) → [`00acf5c0`](#insn-00acf5c0)
  - `FALL_THROUGH` [`00acf644`](#insn-00acf644) → [`00acf648`](#insn-00acf648)
- ブロック [`00acf648`](#insn-00acf648) 範囲 `[['00acf648', '00acf657']]`
  - `CONDITIONAL_JUMP` [`00acf654`](#insn-00acf654) → [`00acf5c8`](#insn-00acf5c8)
  - `FALL_THROUGH` [`00acf654`](#insn-00acf654) → [`00acf658`](#insn-00acf658)
- ブロック [`00acf658`](#insn-00acf658) 範囲 `[['00acf658', '00acf667']]`
  - `CONDITIONAL_JUMP` [`00acf664`](#insn-00acf664) → [`00acf5d0`](#insn-00acf5d0)
  - `FALL_THROUGH` [`00acf664`](#insn-00acf664) → [`00acf668`](#insn-00acf668)
- ブロック [`00acf668`](#insn-00acf668) 範囲 `[['00acf668', '00acf677']]`
  - `CONDITIONAL_JUMP` [`00acf674`](#insn-00acf674) → [`00acf5d8`](#insn-00acf5d8)
  - `FALL_THROUGH` [`00acf674`](#insn-00acf674) → [`00acf678`](#insn-00acf678)
- ブロック [`00acf678`](#insn-00acf678) 範囲 `[['00acf678', '00acf687']]`
  - `CONDITIONAL_JUMP` [`00acf684`](#insn-00acf684) → [`00acf5e0`](#insn-00acf5e0)
  - `FALL_THROUGH` [`00acf684`](#insn-00acf684) → [`00acf688`](#insn-00acf688)
- ブロック [`00acf688`](#insn-00acf688) 範囲 `[['00acf688', '00acf68b']]`
  - `UNCONDITIONAL_JUMP` [`00acf688`](#insn-00acf688) → [`00acf5e8`](#insn-00acf5e8)
- ブロック [`00acf758`](#insn-00acf758) 範囲 `[['00acf758', '00acf75b']]`

## 命令位置別の参照

- [`00acf3d0`](#insn-00acf3d0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf3d4`](#insn-00acf3d4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf3d8`](#insn-00acf3d8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf3fc`](#insn-00acf3fc) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf408`](#insn-00acf408) → `002a72e4`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00acf410`](#insn-00acf410) → `Stack[-0xff]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf414`](#insn-00acf414) → `Stack[-0xf8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf424`](#insn-00acf424) → `Stack[-0x10f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf42c`](#insn-00acf42c) → `002a72f7`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00acf430`](#insn-00acf430) → `Stack[-0xdf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf438`](#insn-00acf438) → `Stack[-0xd8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf448`](#insn-00acf448) → `Stack[-0xef]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf44c`](#insn-00acf44c) → `002a80da`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00acf450`](#insn-00acf450) → `Stack[-0xbf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf458`](#insn-00acf458) → `Stack[-0xb8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf468`](#insn-00acf468) → `Stack[-0xcf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf46c`](#insn-00acf46c) → `002936ae`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00acf470`](#insn-00acf470) → `Stack[-0x9f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf478`](#insn-00acf478) → `Stack[-0x98]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf484`](#insn-00acf484) → `Stack[-0xaf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf488`](#insn-00acf488) → `0029c2e1`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00acf490`](#insn-00acf490) → `Stack[-0x7f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf498`](#insn-00acf498) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf4a4`](#insn-00acf4a4) → `Stack[-0x8f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf4a8`](#insn-00acf4a8) → `00291877`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00acf4b0`](#insn-00acf4b0) → `Stack[-0x5f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf4b8`](#insn-00acf4b8) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf4c4`](#insn-00acf4c4) → `Stack[-0x6f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf4c8`](#insn-00acf4c8) → `00294526`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00acf4cc`](#insn-00acf4cc) → `Stack[-0x110]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf4d0`](#insn-00acf4d0) → `Stack[-0xf0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf4d4`](#insn-00acf4d4) → `Stack[-0xd0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf4d8`](#insn-00acf4d8) → `Stack[-0xb0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf4dc`](#insn-00acf4dc) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf4e0`](#insn-00acf4e0) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf4e4`](#insn-00acf4e4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf4ec`](#insn-00acf4ec) → `Stack[-0x118]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf4f0`](#insn-00acf4f0) → `Stack[-0xfd]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf4f4`](#insn-00acf4f4) → `Stack[-0xdd]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf4f8`](#insn-00acf4f8) → `Stack[-0xbd]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf4fc`](#insn-00acf4fc) → `Stack[-0x9d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf500`](#insn-00acf500) → `Stack[-0x7d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf504`](#insn-00acf504) → `Stack[-0x5d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf508`](#insn-00acf508) → `Stack[-0x3f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf50c`](#insn-00acf50c) → `Stack[-0x4f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf510`](#insn-00acf510) → `Stack[-0x3d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf514`](#insn-00acf514) → `0109faf8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acf518`](#insn-00acf518) → `0109faf0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acf51c`](#insn-00acf51c) → `0109fae8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acf51c`](#insn-00acf51c) → `0109faf0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acf528`](#insn-00acf528) → `0109fae8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acf52c`](#insn-00acf52c) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`00acf530`](#insn-00acf530) → `0109faf0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acf53c`](#insn-00acf53c) → `0109fae8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acf540`](#insn-00acf540) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`00acf544`](#insn-00acf544) → `0109faf0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acf550`](#insn-00acf550) → `0109fae8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acf554`](#insn-00acf554) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`00acf558`](#insn-00acf558) → `0109faf0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acf564`](#insn-00acf564) → `0109fae8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acf568`](#insn-00acf568) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`00acf56c`](#insn-00acf56c) → `0109faf0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acf578`](#insn-00acf578) → `0109fae8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acf57c`](#insn-00acf57c) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`00acf580`](#insn-00acf580) → `0109faf0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acf58c`](#insn-00acf58c) → `0109fae8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acf590`](#insn-00acf590) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`00acf594`](#insn-00acf594) → `0109faf0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acf5a0`](#insn-00acf5a0) → `0109fae8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acf5a4`](#insn-00acf5a4) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`00acf5a8`](#insn-00acf5a8) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf5ac`](#insn-00acf5ac) → [`00acf628`](#insn-00acf628) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf5b0`](#insn-00acf5b0) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf5b4`](#insn-00acf5b4) → [`00acf638`](#insn-00acf638) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf5b8`](#insn-00acf5b8) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf5bc`](#insn-00acf5bc) → [`00acf648`](#insn-00acf648) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf5c0`](#insn-00acf5c0) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf5c4`](#insn-00acf5c4) → [`00acf658`](#insn-00acf658) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf5c8`](#insn-00acf5c8) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf5cc`](#insn-00acf5cc) → [`00acf668`](#insn-00acf668) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf5d0`](#insn-00acf5d0) → `Stack[-0xf0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf5d4`](#insn-00acf5d4) → [`00acf678`](#insn-00acf678) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf5d8`](#insn-00acf5d8) → `Stack[-0x110]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf5dc`](#insn-00acf5dc) → [`00acf5e8`](#insn-00acf5e8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf5e0`](#insn-00acf5e0) → `Stack[-0x100]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf5e4`](#insn-00acf5e4) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00acf5ec`](#insn-00acf5ec) → [`00418330`](../00418/00418330.md) · `PARAM` · `ANALYSIS` · 関数 `00418330` · 推定シンボル `None` · 推定型 `None`
- [`00acf5f4`](#insn-00acf5f4) → `0109fae8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acf5fc`](#insn-00acf5fc) → `00be5ed0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00acf600`](#insn-00acf600) → [`00bdaee0`](../00bda/00bdaee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaee0` · 推定シンボル `None` · 推定型 `None`
- [`00acf608`](#insn-00acf608) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf610`](#insn-00acf610) → [`00acf758`](#insn-00acf758) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf614`](#insn-00acf614) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf618`](#insn-00acf618) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf61c`](#insn-00acf61c) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf628`](#insn-00acf628) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf62c`](#insn-00acf62c) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00acf630`](#insn-00acf630) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf634`](#insn-00acf634) → [`00acf5b8`](#insn-00acf5b8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf638`](#insn-00acf638) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf63c`](#insn-00acf63c) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00acf640`](#insn-00acf640) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf644`](#insn-00acf644) → [`00acf5c0`](#insn-00acf5c0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf648`](#insn-00acf648) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf64c`](#insn-00acf64c) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00acf650`](#insn-00acf650) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf654`](#insn-00acf654) → [`00acf5c8`](#insn-00acf5c8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf658`](#insn-00acf658) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf65c`](#insn-00acf65c) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00acf660`](#insn-00acf660) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf664`](#insn-00acf664) → [`00acf5d0`](#insn-00acf5d0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf668`](#insn-00acf668) → `Stack[-0xc0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf66c`](#insn-00acf66c) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00acf670`](#insn-00acf670) → `Stack[-0xf0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf674`](#insn-00acf674) → [`00acf5d8`](#insn-00acf5d8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf678`](#insn-00acf678) → `Stack[-0xe0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf67c`](#insn-00acf67c) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00acf680`](#insn-00acf680) → `Stack[-0x110]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf684`](#insn-00acf684) → [`00acf5e0`](#insn-00acf5e0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf688`](#insn-00acf688) → [`00acf5e8`](#insn-00acf5e8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf758`](#insn-00acf758) → [`00bdaf90`](../00bda/00bdaf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf90` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00acf3d0`](#insn-00acf3d0)

~~~json
{
  "source": "00acf3d0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf3d4`](#insn-00acf3d4)

~~~json
{
  "source": "00acf3d4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf3d8`](#insn-00acf3d8)

~~~json
{
  "source": "00acf3d8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf3fc`](#insn-00acf3fc)

~~~json
{
  "source": "00acf3fc",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf408`](#insn-00acf408)

~~~json
{
  "source": "00acf408",
  "target": "002a72e4",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a72e4",
  "offset": 0,
  "size": 19,
  "datatype": "string",
  "bytes": "43676b496a4d33795f5a516145414951416700",
  "capture_start": "002a72e4",
  "capture_bytes": 19,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00acf410`](#insn-00acf410)

~~~json
{
  "source": "00acf410",
  "target": "Stack[-0xff]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf414`](#insn-00acf414)

~~~json
{
  "source": "00acf414",
  "target": "Stack[-0xf8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf424`](#insn-00acf424)

~~~json
{
  "source": "00acf424",
  "target": "Stack[-0x10f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf42c`](#insn-00acf42c)

~~~json
{
  "source": "00acf42c",
  "target": "002a72f7",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a72f7",
  "offset": 0,
  "size": 19,
  "datatype": "string",
  "bytes": "43676b496a4d33795f5a516145414951424100",
  "capture_start": "002a72f7",
  "capture_bytes": 19,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00acf430`](#insn-00acf430)

~~~json
{
  "source": "00acf430",
  "target": "Stack[-0xdf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf438`](#insn-00acf438)

~~~json
{
  "source": "00acf438",
  "target": "Stack[-0xd8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf448`](#insn-00acf448)

~~~json
{
  "source": "00acf448",
  "target": "Stack[-0xef]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf44c`](#insn-00acf44c)

~~~json
{
  "source": "00acf44c",
  "target": "002a80da",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a80da",
  "offset": 0,
  "size": 19,
  "datatype": "string",
  "bytes": "43676b496a4d33795f5a516145414951426700",
  "capture_start": "002a80da",
  "capture_bytes": 19,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00acf450`](#insn-00acf450)

~~~json
{
  "source": "00acf450",
  "target": "Stack[-0xbf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf458`](#insn-00acf458)

~~~json
{
  "source": "00acf458",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf468`](#insn-00acf468)

~~~json
{
  "source": "00acf468",
  "target": "Stack[-0xcf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf46c`](#insn-00acf46c)

~~~json
{
  "source": "00acf46c",
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
- 参照命令 [`00acf470`](#insn-00acf470)

~~~json
{
  "source": "00acf470",
  "target": "Stack[-0x9f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf478`](#insn-00acf478)

~~~json
{
  "source": "00acf478",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf484`](#insn-00acf484)

~~~json
{
  "source": "00acf484",
  "target": "Stack[-0xaf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf488`](#insn-00acf488)

~~~json
{
  "source": "00acf488",
  "target": "0029c2e1",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029c2e1",
  "offset": 0,
  "size": 19,
  "datatype": "string",
  "bytes": "43676b496a4d33795f5a516145414951425100",
  "capture_start": "0029c2e1",
  "capture_bytes": 19,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00acf490`](#insn-00acf490)

~~~json
{
  "source": "00acf490",
  "target": "Stack[-0x7f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf498`](#insn-00acf498)

~~~json
{
  "source": "00acf498",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf4a4`](#insn-00acf4a4)

~~~json
{
  "source": "00acf4a4",
  "target": "Stack[-0x8f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf4a8`](#insn-00acf4a8)

~~~json
{
  "source": "00acf4a8",
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
- 参照命令 [`00acf4b0`](#insn-00acf4b0)

~~~json
{
  "source": "00acf4b0",
  "target": "Stack[-0x5f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf4b8`](#insn-00acf4b8)

~~~json
{
  "source": "00acf4b8",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf4c4`](#insn-00acf4c4)

~~~json
{
  "source": "00acf4c4",
  "target": "Stack[-0x6f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf4c8`](#insn-00acf4c8)

~~~json
{
  "source": "00acf4c8",
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
- 参照命令 [`00acf4cc`](#insn-00acf4cc)

~~~json
{
  "source": "00acf4cc",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf4d0`](#insn-00acf4d0)

~~~json
{
  "source": "00acf4d0",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf4d4`](#insn-00acf4d4)

~~~json
{
  "source": "00acf4d4",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf4d8`](#insn-00acf4d8)

~~~json
{
  "source": "00acf4d8",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf4dc`](#insn-00acf4dc)

~~~json
{
  "source": "00acf4dc",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf4e0`](#insn-00acf4e0)

~~~json
{
  "source": "00acf4e0",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf4e4`](#insn-00acf4e4)

~~~json
{
  "source": "00acf4e4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf4ec`](#insn-00acf4ec)

~~~json
{
  "source": "00acf4ec",
  "target": "Stack[-0x118]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf4f0`](#insn-00acf4f0)

~~~json
{
  "source": "00acf4f0",
  "target": "Stack[-0xfd]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf4f4`](#insn-00acf4f4)

~~~json
{
  "source": "00acf4f4",
  "target": "Stack[-0xdd]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf4f8`](#insn-00acf4f8)

~~~json
{
  "source": "00acf4f8",
  "target": "Stack[-0xbd]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf4fc`](#insn-00acf4fc)

~~~json
{
  "source": "00acf4fc",
  "target": "Stack[-0x9d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf500`](#insn-00acf500)

~~~json
{
  "source": "00acf500",
  "target": "Stack[-0x7d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf504`](#insn-00acf504)

~~~json
{
  "source": "00acf504",
  "target": "Stack[-0x5d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf508`](#insn-00acf508)

~~~json
{
  "source": "00acf508",
  "target": "Stack[-0x3f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf50c`](#insn-00acf50c)

~~~json
{
  "source": "00acf50c",
  "target": "Stack[-0x4f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf510`](#insn-00acf510)

~~~json
{
  "source": "00acf510",
  "target": "Stack[-0x3d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf514`](#insn-00acf514)

~~~json
{
  "source": "00acf514",
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
- 参照命令 [`00acf518`](#insn-00acf518)

~~~json
{
  "source": "00acf518",
  "target": "0109faf0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109faf0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acf51c`](#insn-00acf51c)

~~~json
{
  "source": "00acf51c",
  "target": "0109fae8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fae8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acf51c`](#insn-00acf51c)

~~~json
{
  "source": "00acf51c",
  "target": "0109faf0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109faf0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acf528`](#insn-00acf528)

~~~json
{
  "source": "00acf528",
  "target": "0109fae8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fae8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acf52c`](#insn-00acf52c)

~~~json
{
  "source": "00acf52c",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acf530`](#insn-00acf530)

~~~json
{
  "source": "00acf530",
  "target": "0109faf0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109faf0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acf53c`](#insn-00acf53c)

~~~json
{
  "source": "00acf53c",
  "target": "0109fae8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fae8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acf540`](#insn-00acf540)

~~~json
{
  "source": "00acf540",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acf544`](#insn-00acf544)

~~~json
{
  "source": "00acf544",
  "target": "0109faf0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109faf0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acf550`](#insn-00acf550)

~~~json
{
  "source": "00acf550",
  "target": "0109fae8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fae8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acf554`](#insn-00acf554)

~~~json
{
  "source": "00acf554",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acf558`](#insn-00acf558)

~~~json
{
  "source": "00acf558",
  "target": "0109faf0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109faf0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acf564`](#insn-00acf564)

~~~json
{
  "source": "00acf564",
  "target": "0109fae8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fae8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acf568`](#insn-00acf568)

~~~json
{
  "source": "00acf568",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acf56c`](#insn-00acf56c)

~~~json
{
  "source": "00acf56c",
  "target": "0109faf0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109faf0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acf578`](#insn-00acf578)

~~~json
{
  "source": "00acf578",
  "target": "0109fae8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fae8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acf57c`](#insn-00acf57c)

~~~json
{
  "source": "00acf57c",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acf580`](#insn-00acf580)

~~~json
{
  "source": "00acf580",
  "target": "0109faf0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109faf0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acf58c`](#insn-00acf58c)

~~~json
{
  "source": "00acf58c",
  "target": "0109fae8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fae8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acf590`](#insn-00acf590)

~~~json
{
  "source": "00acf590",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acf594`](#insn-00acf594)

~~~json
{
  "source": "00acf594",
  "target": "0109faf0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109faf0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acf5a0`](#insn-00acf5a0)

~~~json
{
  "source": "00acf5a0",
  "target": "0109fae8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fae8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acf5a4`](#insn-00acf5a4)

~~~json
{
  "source": "00acf5a4",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acf5a8`](#insn-00acf5a8)

~~~json
{
  "source": "00acf5a8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf5ac`](#insn-00acf5ac)

~~~json
{
  "source": "00acf5ac",
  "target": "00acf628",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf5b0`](#insn-00acf5b0)

~~~json
{
  "source": "00acf5b0",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf5b4`](#insn-00acf5b4)

~~~json
{
  "source": "00acf5b4",
  "target": "00acf638",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf5b8`](#insn-00acf5b8)

~~~json
{
  "source": "00acf5b8",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf5bc`](#insn-00acf5bc)

~~~json
{
  "source": "00acf5bc",
  "target": "00acf648",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf5c0`](#insn-00acf5c0)

~~~json
{
  "source": "00acf5c0",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf5c4`](#insn-00acf5c4)

~~~json
{
  "source": "00acf5c4",
  "target": "00acf658",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf5c8`](#insn-00acf5c8)

~~~json
{
  "source": "00acf5c8",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf5cc`](#insn-00acf5cc)

~~~json
{
  "source": "00acf5cc",
  "target": "00acf668",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf5d0`](#insn-00acf5d0)

~~~json
{
  "source": "00acf5d0",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf5d4`](#insn-00acf5d4)

~~~json
{
  "source": "00acf5d4",
  "target": "00acf678",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf5d8`](#insn-00acf5d8)

~~~json
{
  "source": "00acf5d8",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf5dc`](#insn-00acf5dc)

~~~json
{
  "source": "00acf5dc",
  "target": "00acf5e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf5e0`](#insn-00acf5e0)

~~~json
{
  "source": "00acf5e0",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf5e4`](#insn-00acf5e4)

~~~json
{
  "source": "00acf5e4",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acf5ec`](#insn-00acf5ec)

~~~json
{
  "source": "00acf5ec",
  "target": "00418330",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acf5f4`](#insn-00acf5f4)

~~~json
{
  "source": "00acf5f4",
  "target": "0109fae8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fae8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acf5fc`](#insn-00acf5fc)

~~~json
{
  "source": "00acf5fc",
  "target": "00be5ed0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00be5ed0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00acf600`](#insn-00acf600)

~~~json
{
  "source": "00acf600",
  "target": "00bdaee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acf608`](#insn-00acf608)

~~~json
{
  "source": "00acf608",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf610`](#insn-00acf610)

~~~json
{
  "source": "00acf610",
  "target": "00acf758",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf614`](#insn-00acf614)

~~~json
{
  "source": "00acf614",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf618`](#insn-00acf618)

~~~json
{
  "source": "00acf618",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf61c`](#insn-00acf61c)

~~~json
{
  "source": "00acf61c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf628`](#insn-00acf628)

~~~json
{
  "source": "00acf628",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf62c`](#insn-00acf62c)

~~~json
{
  "source": "00acf62c",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acf630`](#insn-00acf630)

~~~json
{
  "source": "00acf630",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf634`](#insn-00acf634)

~~~json
{
  "source": "00acf634",
  "target": "00acf5b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf638`](#insn-00acf638)

~~~json
{
  "source": "00acf638",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf63c`](#insn-00acf63c)

~~~json
{
  "source": "00acf63c",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acf640`](#insn-00acf640)

~~~json
{
  "source": "00acf640",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf644`](#insn-00acf644)

~~~json
{
  "source": "00acf644",
  "target": "00acf5c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf648`](#insn-00acf648)

~~~json
{
  "source": "00acf648",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf64c`](#insn-00acf64c)

~~~json
{
  "source": "00acf64c",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acf650`](#insn-00acf650)

~~~json
{
  "source": "00acf650",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf654`](#insn-00acf654)

~~~json
{
  "source": "00acf654",
  "target": "00acf5c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf658`](#insn-00acf658)

~~~json
{
  "source": "00acf658",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf65c`](#insn-00acf65c)

~~~json
{
  "source": "00acf65c",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acf660`](#insn-00acf660)

~~~json
{
  "source": "00acf660",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf664`](#insn-00acf664)

~~~json
{
  "source": "00acf664",
  "target": "00acf5d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf668`](#insn-00acf668)

~~~json
{
  "source": "00acf668",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf66c`](#insn-00acf66c)

~~~json
{
  "source": "00acf66c",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acf670`](#insn-00acf670)

~~~json
{
  "source": "00acf670",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf674`](#insn-00acf674)

~~~json
{
  "source": "00acf674",
  "target": "00acf5d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf678`](#insn-00acf678)

~~~json
{
  "source": "00acf678",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf67c`](#insn-00acf67c)

~~~json
{
  "source": "00acf67c",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acf680`](#insn-00acf680)

~~~json
{
  "source": "00acf680",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf684`](#insn-00acf684)

~~~json
{
  "source": "00acf684",
  "target": "00acf5e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf688`](#insn-00acf688)

~~~json
{
  "source": "00acf688",
  "target": "00acf5e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf758`](#insn-00acf758)

~~~json
{
  "source": "00acf758",
  "target": "00bdaf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
