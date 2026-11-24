# 00acb4cc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00a6d538`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6d/00a6d538.md) · 移動量 `+0x5df94`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0053.md#compare-fa0a6b66204ad9df051bd660e98d89ab)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00acb6c8`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00acb/00acb6c8.md) · 移動量 `+0x1fc`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0064.md#compare-f730f4befa657c3444331bd8b266bb74)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acb4cc",
  "name": "_INIT_246",
  "size": 708,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ea07cab948dbc51caf4dd5e204ce4372af6b476ee927a0c646924f31ab9ff2d4",
  "source_text_sha256": "ea07cab948dbc51caf4dd5e204ce4372af6b476ee927a0c646924f31ab9ff2d4",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00acb4cc",
        "00acb78b"
      ],
      [
        "00acb858",
        "00acb85b"
      ]
    ],
    "bytes_sha256": "402751496b8e41c9bc7239df8913ee986bad54d86c2ff25e8f3f9ab563f75529",
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

## 疑似コード / UTF-8 4860 bytes

~~~c

/* WARNING: Type propagation algorithm not settling */

void _INIT_246(void)

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
  DAT_011248e8 = 0;
  DAT_011248e0 = 0;
  DAT_011248d8 = &DAT_011248e0;
  FUN_0043b7b8(&DAT_011248d8,&DAT_011248e0,local_118,local_118);
  FUN_0043b7b8(&DAT_011248d8,&DAT_011248e0,local_f8,local_f8);
  FUN_0043b7b8(&DAT_011248d8,&DAT_011248e0,local_d8,local_d8);
  FUN_0043b7b8(&DAT_011248d8,&DAT_011248e0,local_b8,local_b8);
  FUN_0043b7b8(&DAT_011248d8,&DAT_011248e0,local_98,local_98);
  FUN_0043b7b8(&DAT_011248d8,&DAT_011248e0,local_78,local_78);
  FUN_0043b7b8(&DAT_011248d8,&DAT_011248e0,local_58,local_58);
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
  __cxa_atexit(FUN_0043ae30,&DAT_011248d8,&PTR_LOOP_00c62b90);
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
<a id="insn-00acb4cc"></a> `00acb4cc` | `ff 83 04 d1` | sub sp,sp,#0x120 | `FALL_THROUGH`
<a id="insn-00acb4d0"></a> `00acb4d0` | `fd 7b 0f a9` | stp x29,x30,[sp, #0xf0] | `FALL_THROUGH`
<a id="insn-00acb4d4"></a> `00acb4d4` | `fc 57 10 a9` | stp x28,x21,[sp, #0x100] | `FALL_THROUGH`
<a id="insn-00acb4d8"></a> `00acb4d8` | `f4 4f 11 a9` | stp x20,x19,[sp, #0x110] | `FALL_THROUGH`
<a id="insn-00acb4dc"></a> `00acb4dc` | `fd c3 03 91` | add x29,sp,#0xf0 | `FALL_THROUGH`
<a id="insn-00acb4e0"></a> `00acb4e0` | `55 d0 3b d5` | mrs x21,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00acb4e4"></a> `00acb4e4` | `2a e8 8c 52` | mov w10,#0x6741 | `FALL_THROUGH`
<a id="insn-00acb4e8"></a> `00acb4e8` | `f4 23 00 91` | add x20,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00acb4ec"></a> `00acb4ec` | `a9 16 40 f9` | ldr x9,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00acb4f0"></a> `00acb4f0` | `88 04 80 52` | mov w8,#0x24 | `FALL_THROUGH`
<a id="insn-00acb4f4"></a> `00acb4f4` | `d3 32 00 b0` | adrp x19,0x1124000 | `FALL_THROUGH`
<a id="insn-00acb4f8"></a> `00acb4f8` | `73 62 23 91` | add x19,x19,#0x8d8 | `FALL_THROUGH`
<a id="insn-00acb4fc"></a> `00acb4fc` | `a9 83 1f f8` | stur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00acb500"></a> `00acb500` | `69 bf ff 90` | adrp x9,0x2b7000 | `FALL_THROUGH`
<a id="insn-00acb504"></a> `00acb504` | `29 99 3b 91` | add x9,x9,#0xee6 | `FALL_THROUGH`
<a id="insn-00acb508"></a> `00acb508` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00acb50c"></a> `00acb50c` | `29 00 80 52` | mov w9,#0x1 | `FALL_THROUGH`
<a id="insn-00acb510"></a> `00acb510` | `ea 13 02 78` | sturh w10,[sp, #0x21] | `FALL_THROUGH`
<a id="insn-00acb514"></a> `00acb514` | `e9 2b 00 b9` | str w9,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00acb518"></a> `00acb518` | `49 28 88 52` | mov w9,#0x4142 | `FALL_THROUGH`
<a id="insn-00acb51c"></a> `00acb51c` | `6a bf ff 90` | adrp x10,0x2b7000 | `FALL_THROUGH`
<a id="insn-00acb520"></a> `00acb520` | `4a e5 3b 91` | add x10,x10,#0xef9 | `FALL_THROUGH`
<a id="insn-00acb524"></a> `00acb524` | `e0 13 81 3c` | stur q0,[sp, #0x11] | `FALL_THROUGH`
<a id="insn-00acb528"></a> `00acb528` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00acb52c"></a> `00acb52c` | `40 01 c0 3d` | ldr q0,[x10] | `FALL_THROUGH`
<a id="insn-00acb530"></a> `00acb530` | `e9 13 04 78` | sturh w9,[sp, #0x41] | `FALL_THROUGH`
<a id="insn-00acb534"></a> `00acb534` | `49 00 80 52` | mov w9,#0x2 | `FALL_THROUGH`
<a id="insn-00acb538"></a> `00acb538` | `e9 4b 00 b9` | str w9,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00acb53c"></a> `00acb53c` | `49 e8 8c 52` | mov w9,#0x6742 | `FALL_THROUGH`
<a id="insn-00acb540"></a> `00acb540` | `6a bf ff b0` | adrp x10,0x2b8000 | `FALL_THROUGH`
<a id="insn-00acb544"></a> `00acb544` | `4a 09 36 91` | add x10,x10,#0xd82 | `FALL_THROUGH`
<a id="insn-00acb548"></a> `00acb548` | `e0 13 83 3c` | stur q0,[sp, #0x31] | `FALL_THROUGH`
<a id="insn-00acb54c"></a> `00acb54c` | `40 01 c0 3d` | ldr q0,[x10] | `FALL_THROUGH`
<a id="insn-00acb550"></a> `00acb550` | `e9 13 06 78` | sturh w9,[sp, #0x61] | `FALL_THROUGH`
<a id="insn-00acb554"></a> `00acb554` | `69 00 80 52` | mov w9,#0x3 | `FALL_THROUGH`
<a id="insn-00acb558"></a> `00acb558` | `e9 6b 00 b9` | str w9,[sp, #0x68] | `FALL_THROUGH`
<a id="insn-00acb55c"></a> `00acb55c` | `29 e8 8e 52` | mov w9,#0x7741 | `FALL_THROUGH`
<a id="insn-00acb560"></a> `00acb560` | `aa be ff f0` | adrp x10,0x2a2000 | `FALL_THROUGH`
<a id="insn-00acb564"></a> `00acb564` | `4a 55 3a 91` | add x10,x10,#0xe95 | `FALL_THROUGH`
<a id="insn-00acb568"></a> `00acb568` | `e0 13 85 3c` | stur q0,[sp, #0x51] | `FALL_THROUGH`
<a id="insn-00acb56c"></a> `00acb56c` | `40 01 c0 3d` | ldr q0,[x10] | `FALL_THROUGH`
<a id="insn-00acb570"></a> `00acb570` | `e9 13 08 78` | sturh w9,[sp, #0x81] | `FALL_THROUGH`
<a id="insn-00acb574"></a> `00acb574` | `89 00 80 52` | mov w9,#0x4 | `FALL_THROUGH`
<a id="insn-00acb578"></a> `00acb578` | `e9 8b 00 b9` | str w9,[sp, #0x88] | `FALL_THROUGH`
<a id="insn-00acb57c"></a> `00acb57c` | `09 bf ff b0` | adrp x9,0x2ac000 | `FALL_THROUGH`
<a id="insn-00acb580"></a> `00acb580` | `29 49 16 91` | add x9,x9,#0x592 | `FALL_THROUGH`
<a id="insn-00acb584"></a> `00acb584` | `e0 13 87 3c` | stur q0,[sp, #0x71] | `FALL_THROUGH`
<a id="insn-00acb588"></a> `00acb588` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00acb58c"></a> `00acb58c` | `49 28 8a 52` | mov w9,#0x5142 | `FALL_THROUGH`
<a id="insn-00acb590"></a> `00acb590` | `89 92 09 78` | sturh w9,[x20, #0x99] | `FALL_THROUGH`
<a id="insn-00acb594"></a> `00acb594` | `a9 00 80 52` | mov w9,#0x5 | `FALL_THROUGH`
<a id="insn-00acb598"></a> `00acb598` | `e9 ab 00 b9` | str w9,[sp, #0xa8] | `FALL_THROUGH`
<a id="insn-00acb59c"></a> `00acb59c` | `a9 be ff b0` | adrp x9,0x2a0000 | `FALL_THROUGH`
<a id="insn-00acb5a0"></a> `00acb5a0` | `29 41 3a 91` | add x9,x9,#0xe90 | `FALL_THROUGH`
<a id="insn-00acb5a4"></a> `00acb5a4` | `80 92 88 3c` | stur q0,[x20, #0x89] | `FALL_THROUGH`
<a id="insn-00acb5a8"></a> `00acb5a8` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00acb5ac"></a> `00acb5ac` | `49 e8 8e 52` | mov w9,#0x7742 | `FALL_THROUGH`
<a id="insn-00acb5b0"></a> `00acb5b0` | `89 92 0b 78` | sturh w9,[x20, #0xb9] | `FALL_THROUGH`
<a id="insn-00acb5b4"></a> `00acb5b4` | `c9 00 80 52` | mov w9,#0x6 | `FALL_THROUGH`
<a id="insn-00acb5b8"></a> `00acb5b8` | `e9 cb 00 b9` | str w9,[sp, #0xc8] | `FALL_THROUGH`
<a id="insn-00acb5bc"></a> `00acb5bc` | `c9 be ff 90` | adrp x9,0x2a3000 | `FALL_THROUGH`
<a id="insn-00acb5c0"></a> `00acb5c0` | `29 f1 38 91` | add x9,x9,#0xe3c | `FALL_THROUGH`
<a id="insn-00acb5c4"></a> `00acb5c4` | `80 92 8a 3c` | stur q0,[x20, #0xa9] | `FALL_THROUGH`
<a id="insn-00acb5c8"></a> `00acb5c8` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00acb5cc"></a> `00acb5cc` | `e8 43 00 39` | strb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acb5d0"></a> `00acb5d0` | `e8 c3 00 39` | strb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00acb5d4"></a> `00acb5d4` | `e8 43 01 39` | strb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00acb5d8"></a> `00acb5d8` | `e8 c3 01 39` | strb w8,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00acb5dc"></a> `00acb5dc` | `e8 43 02 39` | strb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00acb5e0"></a> `00acb5e0` | `e8 c3 02 39` | strb w8,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00acb5e4"></a> `00acb5e4` | `e8 43 03 39` | strb w8,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-00acb5e8"></a> `00acb5e8` | `68 28 88 52` | mov w8,#0x4143 | `FALL_THROUGH`
<a id="insn-00acb5ec"></a> `00acb5ec` | `ff 0b 00 b9` | str wzr,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00acb5f0"></a> `00acb5f0` | `ff 8f 00 39` | strb wzr,[sp, #0x23] | `FALL_THROUGH`
<a id="insn-00acb5f4"></a> `00acb5f4` | `ff 0f 01 39` | strb wzr,[sp, #0x43] | `FALL_THROUGH`
<a id="insn-00acb5f8"></a> `00acb5f8` | `ff 8f 01 39` | strb wzr,[sp, #0x63] | `FALL_THROUGH`
<a id="insn-00acb5fc"></a> `00acb5fc` | `ff 0f 02 39` | strb wzr,[sp, #0x83] | `FALL_THROUGH`
<a id="insn-00acb600"></a> `00acb600` | `ff 8f 02 39` | strb wzr,[sp, #0xa3] | `FALL_THROUGH`
<a id="insn-00acb604"></a> `00acb604` | `ff 0f 03 39` | strb wzr,[sp, #0xc3] | `FALL_THROUGH`
<a id="insn-00acb608"></a> `00acb608` | `88 92 0d 78` | sturh w8,[x20, #0xd9] | `FALL_THROUGH`
<a id="insn-00acb60c"></a> `00acb60c` | `80 92 8c 3c` | stur q0,[x20, #0xc9] | `FALL_THROUGH`
<a id="insn-00acb610"></a> `00acb610` | `ff 8f 03 39` | strb wzr,[sp, #0xe3] | `FALL_THROUGH`
<a id="insn-00acb614"></a> `00acb614` | `7f 0a 00 f9` | str xzr,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00acb618"></a> `00acb618` | `3f 8c 00 f8` | str xzr,[x1, #0x8]! | `FALL_THROUGH`
<a id="insn-00acb61c"></a> `00acb61c` | `61 02 00 f9` | str x1,[x19] | `FALL_THROUGH`
<a id="insn-00acb620"></a> `00acb620` | `e2 23 00 91` | add x2,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00acb624"></a> `00acb624` | `e3 23 00 91` | add x3,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00acb628"></a> `00acb628` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00acb62c"></a> `00acb62c` | `63 c0 e5 97` | bl 0x0043b7b8 | `UNCONDITIONAL_CALL`
<a id="insn-00acb630"></a> `00acb630` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00acb634"></a> `00acb634` | `82 82 00 91` | add x2,x20,#0x20 | `FALL_THROUGH`
<a id="insn-00acb638"></a> `00acb638` | `83 82 00 91` | add x3,x20,#0x20 | `FALL_THROUGH`
<a id="insn-00acb63c"></a> `00acb63c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00acb640"></a> `00acb640` | `5e c0 e5 97` | bl 0x0043b7b8 | `UNCONDITIONAL_CALL`
<a id="insn-00acb644"></a> `00acb644` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00acb648"></a> `00acb648` | `82 02 01 91` | add x2,x20,#0x40 | `FALL_THROUGH`
<a id="insn-00acb64c"></a> `00acb64c` | `83 02 01 91` | add x3,x20,#0x40 | `FALL_THROUGH`
<a id="insn-00acb650"></a> `00acb650` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00acb654"></a> `00acb654` | `59 c0 e5 97` | bl 0x0043b7b8 | `UNCONDITIONAL_CALL`
<a id="insn-00acb658"></a> `00acb658` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00acb65c"></a> `00acb65c` | `82 82 01 91` | add x2,x20,#0x60 | `FALL_THROUGH`
<a id="insn-00acb660"></a> `00acb660` | `83 82 01 91` | add x3,x20,#0x60 | `FALL_THROUGH`
<a id="insn-00acb664"></a> `00acb664` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00acb668"></a> `00acb668` | `54 c0 e5 97` | bl 0x0043b7b8 | `UNCONDITIONAL_CALL`
<a id="insn-00acb66c"></a> `00acb66c` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00acb670"></a> `00acb670` | `82 02 02 91` | add x2,x20,#0x80 | `FALL_THROUGH`
<a id="insn-00acb674"></a> `00acb674` | `83 02 02 91` | add x3,x20,#0x80 | `FALL_THROUGH`
<a id="insn-00acb678"></a> `00acb678` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00acb67c"></a> `00acb67c` | `4f c0 e5 97` | bl 0x0043b7b8 | `UNCONDITIONAL_CALL`
<a id="insn-00acb680"></a> `00acb680` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00acb684"></a> `00acb684` | `82 82 02 91` | add x2,x20,#0xa0 | `FALL_THROUGH`
<a id="insn-00acb688"></a> `00acb688` | `83 82 02 91` | add x3,x20,#0xa0 | `FALL_THROUGH`
<a id="insn-00acb68c"></a> `00acb68c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00acb690"></a> `00acb690` | `4a c0 e5 97` | bl 0x0043b7b8 | `UNCONDITIONAL_CALL`
<a id="insn-00acb694"></a> `00acb694` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00acb698"></a> `00acb698` | `82 02 03 91` | add x2,x20,#0xc0 | `FALL_THROUGH`
<a id="insn-00acb69c"></a> `00acb69c` | `83 02 03 91` | add x3,x20,#0xc0 | `FALL_THROUGH`
<a id="insn-00acb6a0"></a> `00acb6a0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00acb6a4"></a> `00acb6a4` | `45 c0 e5 97` | bl 0x0043b7b8 | `UNCONDITIONAL_CALL`
<a id="insn-00acb6a8"></a> `00acb6a8` | `e8 43 43 39` | ldrb w8,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-00acb6ac"></a> `00acb6ac` | `e8 03 00 37` | tbnz w8,#0x0,0x00acb728 | `CONDITIONAL_JUMP`
<a id="insn-00acb6b0"></a> `00acb6b0` | `e8 c3 42 39` | ldrb w8,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00acb6b4"></a> `00acb6b4` | `28 04 00 37` | tbnz w8,#0x0,0x00acb738 | `CONDITIONAL_JUMP`
<a id="insn-00acb6b8"></a> `00acb6b8` | `e8 43 42 39` | ldrb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00acb6bc"></a> `00acb6bc` | `68 04 00 37` | tbnz w8,#0x0,0x00acb748 | `CONDITIONAL_JUMP`
<a id="insn-00acb6c0"></a> `00acb6c0` | `e8 c3 41 39` | ldrb w8,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00acb6c4"></a> `00acb6c4` | `a8 04 00 37` | tbnz w8,#0x0,0x00acb758 | `CONDITIONAL_JUMP`
<a id="insn-00acb6c8"></a> `00acb6c8` | `e8 43 41 39` | ldrb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00acb6cc"></a> `00acb6cc` | `e8 04 00 37` | tbnz w8,#0x0,0x00acb768 | `CONDITIONAL_JUMP`
<a id="insn-00acb6d0"></a> `00acb6d0` | `e8 c3 40 39` | ldrb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00acb6d4"></a> `00acb6d4` | `28 05 00 37` | tbnz w8,#0x0,0x00acb778 | `CONDITIONAL_JUMP`
<a id="insn-00acb6d8"></a> `00acb6d8` | `e8 43 40 39` | ldrb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acb6dc"></a> `00acb6dc` | `68 00 00 36` | tbz w8,#0x0,0x00acb6e8 | `CONDITIONAL_JUMP`
<a id="insn-00acb6e0"></a> `00acb6e0` | `e0 13 40 f9` | ldr x0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00acb6e4"></a> `00acb6e4` | `f3 30 06 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00acb6e8"></a> `00acb6e8` | `60 cb ff f0` | adrp x0,0x43a000 | `FALL_THROUGH`
<a id="insn-00acb6ec"></a> `00acb6ec` | `00 c0 38 91` | add x0,x0,#0xe30 | `FALL_THROUGH`
<a id="insn-00acb6f0"></a> `00acb6f0` | `c1 32 00 b0` | adrp x1,0x1124000 | `FALL_THROUGH`
<a id="insn-00acb6f4"></a> `00acb6f4` | `21 60 23 91` | add x1,x1,#0x8d8 | `FALL_THROUGH`
<a id="insn-00acb6f8"></a> `00acb6f8` | `a2 0c 00 f0` | adrp x2,0xc62000 | `FALL_THROUGH`
<a id="insn-00acb6fc"></a> `00acb6fc` | `42 40 2e 91` | add x2,x2,#0xb90 | `FALL_THROUGH`
<a id="insn-00acb700"></a> `00acb700` | `cc 30 06 94` | bl 0x00c57a30 | `UNCONDITIONAL_CALL`
<a id="insn-00acb704"></a> `00acb704` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00acb708"></a> `00acb708` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00acb70c"></a> `00acb70c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00acb710"></a> `00acb710` | `41 0a 00 54` | b.ne 0x00acb858 | `CONDITIONAL_JUMP`
<a id="insn-00acb714"></a> `00acb714` | `f4 4f 51 a9` | ldp x20,x19,[sp, #0x110] | `FALL_THROUGH`
<a id="insn-00acb718"></a> `00acb718` | `fc 57 50 a9` | ldp x28,x21,[sp, #0x100] | `FALL_THROUGH`
<a id="insn-00acb71c"></a> `00acb71c` | `fd 7b 4f a9` | ldp x29,x30,[sp, #0xf0] | `FALL_THROUGH`
<a id="insn-00acb720"></a> `00acb720` | `ff 83 04 91` | add sp,sp,#0x120 | `FALL_THROUGH`
<a id="insn-00acb724"></a> `00acb724` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00acb728"></a> `00acb728` | `e0 73 40 f9` | ldr x0,[sp, #0xe0] | `FALL_THROUGH`
<a id="insn-00acb72c"></a> `00acb72c` | `e1 30 06 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00acb730"></a> `00acb730` | `e8 c3 42 39` | ldrb w8,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00acb734"></a> `00acb734` | `28 fc 07 36` | tbz w8,#0x0,0x00acb6b8 | `CONDITIONAL_JUMP`
<a id="insn-00acb738"></a> `00acb738` | `e0 63 40 f9` | ldr x0,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00acb73c"></a> `00acb73c` | `dd 30 06 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00acb740"></a> `00acb740` | `e8 43 42 39` | ldrb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00acb744"></a> `00acb744` | `e8 fb 07 36` | tbz w8,#0x0,0x00acb6c0 | `CONDITIONAL_JUMP`
<a id="insn-00acb748"></a> `00acb748` | `e0 53 40 f9` | ldr x0,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00acb74c"></a> `00acb74c` | `d9 30 06 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00acb750"></a> `00acb750` | `e8 c3 41 39` | ldrb w8,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00acb754"></a> `00acb754` | `a8 fb 07 36` | tbz w8,#0x0,0x00acb6c8 | `CONDITIONAL_JUMP`
<a id="insn-00acb758"></a> `00acb758` | `e0 43 40 f9` | ldr x0,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00acb75c"></a> `00acb75c` | `d5 30 06 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00acb760"></a> `00acb760` | `e8 43 41 39` | ldrb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00acb764"></a> `00acb764` | `68 fb 07 36` | tbz w8,#0x0,0x00acb6d0 | `CONDITIONAL_JUMP`
<a id="insn-00acb768"></a> `00acb768` | `e0 33 40 f9` | ldr x0,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00acb76c"></a> `00acb76c` | `d1 30 06 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00acb770"></a> `00acb770` | `e8 c3 40 39` | ldrb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00acb774"></a> `00acb774` | `28 fb 07 36` | tbz w8,#0x0,0x00acb6d8 | `CONDITIONAL_JUMP`
<a id="insn-00acb778"></a> `00acb778` | `e0 23 40 f9` | ldr x0,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00acb77c"></a> `00acb77c` | `cd 30 06 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00acb780"></a> `00acb780` | `e8 43 40 39` | ldrb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acb784"></a> `00acb784` | `e8 fa 07 37` | tbnz w8,#0x0,0x00acb6e0 | `CONDITIONAL_JUMP`
<a id="insn-00acb788"></a> `00acb788` | `d8 ff ff 17` | b 0x00acb6e8 | `UNCONDITIONAL_JUMP`
<a id="insn-00acb858"></a> `00acb858` | `a2 30 06 94` | bl 0x00c57ae0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00acb4cc`](#insn-00acb4cc) 範囲 `[['00acb4cc', '00acb6af']]`
  - `CONDITIONAL_JUMP` [`00acb6ac`](#insn-00acb6ac) → [`00acb728`](#insn-00acb728)
  - `FALL_THROUGH` [`00acb6ac`](#insn-00acb6ac) → [`00acb6b0`](#insn-00acb6b0)
- ブロック [`00acb6b0`](#insn-00acb6b0) 範囲 `[['00acb6b0', '00acb6b7']]`
  - `CONDITIONAL_JUMP` [`00acb6b4`](#insn-00acb6b4) → [`00acb738`](#insn-00acb738)
  - `FALL_THROUGH` [`00acb6b4`](#insn-00acb6b4) → [`00acb6b8`](#insn-00acb6b8)
- ブロック [`00acb6b8`](#insn-00acb6b8) 範囲 `[['00acb6b8', '00acb6bf']]`
  - `CONDITIONAL_JUMP` [`00acb6bc`](#insn-00acb6bc) → [`00acb748`](#insn-00acb748)
  - `FALL_THROUGH` [`00acb6bc`](#insn-00acb6bc) → [`00acb6c0`](#insn-00acb6c0)
- ブロック [`00acb6c0`](#insn-00acb6c0) 範囲 `[['00acb6c0', '00acb6c7']]`
  - `CONDITIONAL_JUMP` [`00acb6c4`](#insn-00acb6c4) → [`00acb758`](#insn-00acb758)
  - `FALL_THROUGH` [`00acb6c4`](#insn-00acb6c4) → [`00acb6c8`](#insn-00acb6c8)
- ブロック [`00acb6c8`](#insn-00acb6c8) 範囲 `[['00acb6c8', '00acb6cf']]`
  - `CONDITIONAL_JUMP` [`00acb6cc`](#insn-00acb6cc) → [`00acb768`](#insn-00acb768)
  - `FALL_THROUGH` [`00acb6cc`](#insn-00acb6cc) → [`00acb6d0`](#insn-00acb6d0)
- ブロック [`00acb6d0`](#insn-00acb6d0) 範囲 `[['00acb6d0', '00acb6d7']]`
  - `CONDITIONAL_JUMP` [`00acb6d4`](#insn-00acb6d4) → [`00acb778`](#insn-00acb778)
  - `FALL_THROUGH` [`00acb6d4`](#insn-00acb6d4) → [`00acb6d8`](#insn-00acb6d8)
- ブロック [`00acb6d8`](#insn-00acb6d8) 範囲 `[['00acb6d8', '00acb6df']]`
  - `CONDITIONAL_JUMP` [`00acb6dc`](#insn-00acb6dc) → [`00acb6e8`](#insn-00acb6e8)
  - `FALL_THROUGH` [`00acb6dc`](#insn-00acb6dc) → [`00acb6e0`](#insn-00acb6e0)
- ブロック [`00acb6e0`](#insn-00acb6e0) 範囲 `[['00acb6e0', '00acb6e7']]`
  - `FALL_THROUGH` [`00acb6e4`](#insn-00acb6e4) → [`00acb6e8`](#insn-00acb6e8)
- ブロック [`00acb6e8`](#insn-00acb6e8) 範囲 `[['00acb6e8', '00acb713']]`
  - `CONDITIONAL_JUMP` [`00acb710`](#insn-00acb710) → [`00acb858`](#insn-00acb858)
  - `FALL_THROUGH` [`00acb710`](#insn-00acb710) → [`00acb714`](#insn-00acb714)
- ブロック [`00acb714`](#insn-00acb714) 範囲 `[['00acb714', '00acb727']]`
- ブロック [`00acb728`](#insn-00acb728) 範囲 `[['00acb728', '00acb737']]`
  - `CONDITIONAL_JUMP` [`00acb734`](#insn-00acb734) → [`00acb6b8`](#insn-00acb6b8)
  - `FALL_THROUGH` [`00acb734`](#insn-00acb734) → [`00acb738`](#insn-00acb738)
- ブロック [`00acb738`](#insn-00acb738) 範囲 `[['00acb738', '00acb747']]`
  - `CONDITIONAL_JUMP` [`00acb744`](#insn-00acb744) → [`00acb6c0`](#insn-00acb6c0)
  - `FALL_THROUGH` [`00acb744`](#insn-00acb744) → [`00acb748`](#insn-00acb748)
- ブロック [`00acb748`](#insn-00acb748) 範囲 `[['00acb748', '00acb757']]`
  - `CONDITIONAL_JUMP` [`00acb754`](#insn-00acb754) → [`00acb6c8`](#insn-00acb6c8)
  - `FALL_THROUGH` [`00acb754`](#insn-00acb754) → [`00acb758`](#insn-00acb758)
- ブロック [`00acb758`](#insn-00acb758) 範囲 `[['00acb758', '00acb767']]`
  - `CONDITIONAL_JUMP` [`00acb764`](#insn-00acb764) → [`00acb6d0`](#insn-00acb6d0)
  - `FALL_THROUGH` [`00acb764`](#insn-00acb764) → [`00acb768`](#insn-00acb768)
- ブロック [`00acb768`](#insn-00acb768) 範囲 `[['00acb768', '00acb777']]`
  - `CONDITIONAL_JUMP` [`00acb774`](#insn-00acb774) → [`00acb6d8`](#insn-00acb6d8)
  - `FALL_THROUGH` [`00acb774`](#insn-00acb774) → [`00acb778`](#insn-00acb778)
- ブロック [`00acb778`](#insn-00acb778) 範囲 `[['00acb778', '00acb787']]`
  - `CONDITIONAL_JUMP` [`00acb784`](#insn-00acb784) → [`00acb6e0`](#insn-00acb6e0)
  - `FALL_THROUGH` [`00acb784`](#insn-00acb784) → [`00acb788`](#insn-00acb788)
- ブロック [`00acb788`](#insn-00acb788) 範囲 `[['00acb788', '00acb78b']]`
  - `UNCONDITIONAL_JUMP` [`00acb788`](#insn-00acb788) → [`00acb6e8`](#insn-00acb6e8)
- ブロック [`00acb858`](#insn-00acb858) 範囲 `[['00acb858', '00acb85b']]`

## 命令位置別の参照

- [`00acb4d0`](#insn-00acb4d0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb4d4`](#insn-00acb4d4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb4d8`](#insn-00acb4d8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb4fc`](#insn-00acb4fc) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb508`](#insn-00acb508) → `002b7ee6`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00acb510`](#insn-00acb510) → `Stack[-0xff]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb514`](#insn-00acb514) → `Stack[-0xf8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb524`](#insn-00acb524) → `Stack[-0x10f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb52c`](#insn-00acb52c) → `002b7ef9`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00acb530`](#insn-00acb530) → `Stack[-0xdf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb538`](#insn-00acb538) → `Stack[-0xd8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb548`](#insn-00acb548) → `Stack[-0xef]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb54c`](#insn-00acb54c) → `002b8d82`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00acb550`](#insn-00acb550) → `Stack[-0xbf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb558`](#insn-00acb558) → `Stack[-0xb8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb568`](#insn-00acb568) → `Stack[-0xcf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb56c`](#insn-00acb56c) → `002a2e95`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00acb570`](#insn-00acb570) → `Stack[-0x9f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb578`](#insn-00acb578) → `Stack[-0x98]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb584`](#insn-00acb584) → `Stack[-0xaf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb588`](#insn-00acb588) → `002ac592`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00acb590`](#insn-00acb590) → `Stack[-0x7f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb598`](#insn-00acb598) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb5a4`](#insn-00acb5a4) → `Stack[-0x8f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb5a8`](#insn-00acb5a8) → `002a0e90`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00acb5b0`](#insn-00acb5b0) → `Stack[-0x5f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb5b8`](#insn-00acb5b8) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb5c4`](#insn-00acb5c4) → `Stack[-0x6f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb5c8`](#insn-00acb5c8) → `002a3e3c`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00acb5cc`](#insn-00acb5cc) → `Stack[-0x110]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb5d0`](#insn-00acb5d0) → `Stack[-0xf0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb5d4`](#insn-00acb5d4) → `Stack[-0xd0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb5d8`](#insn-00acb5d8) → `Stack[-0xb0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb5dc`](#insn-00acb5dc) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb5e0`](#insn-00acb5e0) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb5e4`](#insn-00acb5e4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb5ec`](#insn-00acb5ec) → `Stack[-0x118]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb5f0`](#insn-00acb5f0) → `Stack[-0xfd]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb5f4`](#insn-00acb5f4) → `Stack[-0xdd]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb5f8`](#insn-00acb5f8) → `Stack[-0xbd]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb5fc`](#insn-00acb5fc) → `Stack[-0x9d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb600`](#insn-00acb600) → `Stack[-0x7d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb604`](#insn-00acb604) → `Stack[-0x5d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb608`](#insn-00acb608) → `Stack[-0x3f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb60c`](#insn-00acb60c) → `Stack[-0x4f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb610`](#insn-00acb610) → `Stack[-0x3d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb614`](#insn-00acb614) → `011248e8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acb618`](#insn-00acb618) → `011248e0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acb61c`](#insn-00acb61c) → `011248d8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acb61c`](#insn-00acb61c) → `011248e0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acb628`](#insn-00acb628) → `011248d8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acb62c`](#insn-00acb62c) → [`0043b7b8`](../0043b/0043b7b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043b7b8` · 推定シンボル `None` · 推定型 `None`
- [`00acb630`](#insn-00acb630) → `011248e0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acb63c`](#insn-00acb63c) → `011248d8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acb640`](#insn-00acb640) → [`0043b7b8`](../0043b/0043b7b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043b7b8` · 推定シンボル `None` · 推定型 `None`
- [`00acb644`](#insn-00acb644) → `011248e0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acb650`](#insn-00acb650) → `011248d8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acb654`](#insn-00acb654) → [`0043b7b8`](../0043b/0043b7b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043b7b8` · 推定シンボル `None` · 推定型 `None`
- [`00acb658`](#insn-00acb658) → `011248e0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acb664`](#insn-00acb664) → `011248d8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acb668`](#insn-00acb668) → [`0043b7b8`](../0043b/0043b7b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043b7b8` · 推定シンボル `None` · 推定型 `None`
- [`00acb66c`](#insn-00acb66c) → `011248e0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acb678`](#insn-00acb678) → `011248d8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acb67c`](#insn-00acb67c) → [`0043b7b8`](../0043b/0043b7b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043b7b8` · 推定シンボル `None` · 推定型 `None`
- [`00acb680`](#insn-00acb680) → `011248e0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acb68c`](#insn-00acb68c) → `011248d8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acb690`](#insn-00acb690) → [`0043b7b8`](../0043b/0043b7b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043b7b8` · 推定シンボル `None` · 推定型 `None`
- [`00acb694`](#insn-00acb694) → `011248e0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acb6a0`](#insn-00acb6a0) → `011248d8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acb6a4`](#insn-00acb6a4) → [`0043b7b8`](../0043b/0043b7b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043b7b8` · 推定シンボル `None` · 推定型 `None`
- [`00acb6a8`](#insn-00acb6a8) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb6ac`](#insn-00acb6ac) → [`00acb728`](#insn-00acb728) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb6b0`](#insn-00acb6b0) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb6b4`](#insn-00acb6b4) → [`00acb738`](#insn-00acb738) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb6b8`](#insn-00acb6b8) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb6bc`](#insn-00acb6bc) → [`00acb748`](#insn-00acb748) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb6c0`](#insn-00acb6c0) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb6c4`](#insn-00acb6c4) → [`00acb758`](#insn-00acb758) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb6c8`](#insn-00acb6c8) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb6cc`](#insn-00acb6cc) → [`00acb768`](#insn-00acb768) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb6d0`](#insn-00acb6d0) → `Stack[-0xf0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb6d4`](#insn-00acb6d4) → [`00acb778`](#insn-00acb778) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb6d8`](#insn-00acb6d8) → `Stack[-0x110]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb6dc`](#insn-00acb6dc) → [`00acb6e8`](#insn-00acb6e8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb6e0`](#insn-00acb6e0) → `Stack[-0x100]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb6e4`](#insn-00acb6e4) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00acb6ec`](#insn-00acb6ec) → [`0043ae30`](../0043a/0043ae30.md) · `PARAM` · `ANALYSIS` · 関数 `0043ae30` · 推定シンボル `None` · 推定型 `None`
- [`00acb6f4`](#insn-00acb6f4) → `011248d8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acb6fc`](#insn-00acb6fc) → `00c62b90`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00acb700`](#insn-00acb700) → [`00c57a30`](../00c57/00c57a30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a30` · 推定シンボル `None` · 推定型 `None`
- [`00acb708`](#insn-00acb708) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb710`](#insn-00acb710) → [`00acb858`](#insn-00acb858) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb714`](#insn-00acb714) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb718`](#insn-00acb718) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb71c`](#insn-00acb71c) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb728`](#insn-00acb728) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb72c`](#insn-00acb72c) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00acb730`](#insn-00acb730) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb734`](#insn-00acb734) → [`00acb6b8`](#insn-00acb6b8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb738`](#insn-00acb738) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb73c`](#insn-00acb73c) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00acb740`](#insn-00acb740) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb744`](#insn-00acb744) → [`00acb6c0`](#insn-00acb6c0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb748`](#insn-00acb748) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb74c`](#insn-00acb74c) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00acb750`](#insn-00acb750) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb754`](#insn-00acb754) → [`00acb6c8`](#insn-00acb6c8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb758`](#insn-00acb758) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb75c`](#insn-00acb75c) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00acb760`](#insn-00acb760) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb764`](#insn-00acb764) → [`00acb6d0`](#insn-00acb6d0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb768`](#insn-00acb768) → `Stack[-0xc0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb76c`](#insn-00acb76c) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00acb770`](#insn-00acb770) → `Stack[-0xf0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb774`](#insn-00acb774) → [`00acb6d8`](#insn-00acb6d8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb778`](#insn-00acb778) → `Stack[-0xe0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb77c`](#insn-00acb77c) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00acb780`](#insn-00acb780) → `Stack[-0x110]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb784`](#insn-00acb784) → [`00acb6e0`](#insn-00acb6e0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb788`](#insn-00acb788) → [`00acb6e8`](#insn-00acb6e8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb858`](#insn-00acb858) → [`00c57ae0`](../00c57/00c57ae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ae0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00acb4d0`](#insn-00acb4d0)

~~~json
{
  "source": "00acb4d0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb4d4`](#insn-00acb4d4)

~~~json
{
  "source": "00acb4d4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb4d8`](#insn-00acb4d8)

~~~json
{
  "source": "00acb4d8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb4fc`](#insn-00acb4fc)

~~~json
{
  "source": "00acb4fc",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb508`](#insn-00acb508)

~~~json
{
  "source": "00acb508",
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
- 参照命令 [`00acb510`](#insn-00acb510)

~~~json
{
  "source": "00acb510",
  "target": "Stack[-0xff]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb514`](#insn-00acb514)

~~~json
{
  "source": "00acb514",
  "target": "Stack[-0xf8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb524`](#insn-00acb524)

~~~json
{
  "source": "00acb524",
  "target": "Stack[-0x10f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb52c`](#insn-00acb52c)

~~~json
{
  "source": "00acb52c",
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
- 参照命令 [`00acb530`](#insn-00acb530)

~~~json
{
  "source": "00acb530",
  "target": "Stack[-0xdf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb538`](#insn-00acb538)

~~~json
{
  "source": "00acb538",
  "target": "Stack[-0xd8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb548`](#insn-00acb548)

~~~json
{
  "source": "00acb548",
  "target": "Stack[-0xef]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb54c`](#insn-00acb54c)

~~~json
{
  "source": "00acb54c",
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
- 参照命令 [`00acb550`](#insn-00acb550)

~~~json
{
  "source": "00acb550",
  "target": "Stack[-0xbf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb558`](#insn-00acb558)

~~~json
{
  "source": "00acb558",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb568`](#insn-00acb568)

~~~json
{
  "source": "00acb568",
  "target": "Stack[-0xcf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb56c`](#insn-00acb56c)

~~~json
{
  "source": "00acb56c",
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
- 参照命令 [`00acb570`](#insn-00acb570)

~~~json
{
  "source": "00acb570",
  "target": "Stack[-0x9f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb578`](#insn-00acb578)

~~~json
{
  "source": "00acb578",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb584`](#insn-00acb584)

~~~json
{
  "source": "00acb584",
  "target": "Stack[-0xaf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb588`](#insn-00acb588)

~~~json
{
  "source": "00acb588",
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
- 参照命令 [`00acb590`](#insn-00acb590)

~~~json
{
  "source": "00acb590",
  "target": "Stack[-0x7f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb598`](#insn-00acb598)

~~~json
{
  "source": "00acb598",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb5a4`](#insn-00acb5a4)

~~~json
{
  "source": "00acb5a4",
  "target": "Stack[-0x8f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb5a8`](#insn-00acb5a8)

~~~json
{
  "source": "00acb5a8",
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
- 参照命令 [`00acb5b0`](#insn-00acb5b0)

~~~json
{
  "source": "00acb5b0",
  "target": "Stack[-0x5f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb5b8`](#insn-00acb5b8)

~~~json
{
  "source": "00acb5b8",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb5c4`](#insn-00acb5c4)

~~~json
{
  "source": "00acb5c4",
  "target": "Stack[-0x6f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb5c8`](#insn-00acb5c8)

~~~json
{
  "source": "00acb5c8",
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
- 参照命令 [`00acb5cc`](#insn-00acb5cc)

~~~json
{
  "source": "00acb5cc",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb5d0`](#insn-00acb5d0)

~~~json
{
  "source": "00acb5d0",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb5d4`](#insn-00acb5d4)

~~~json
{
  "source": "00acb5d4",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb5d8`](#insn-00acb5d8)

~~~json
{
  "source": "00acb5d8",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb5dc`](#insn-00acb5dc)

~~~json
{
  "source": "00acb5dc",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb5e0`](#insn-00acb5e0)

~~~json
{
  "source": "00acb5e0",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb5e4`](#insn-00acb5e4)

~~~json
{
  "source": "00acb5e4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb5ec`](#insn-00acb5ec)

~~~json
{
  "source": "00acb5ec",
  "target": "Stack[-0x118]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb5f0`](#insn-00acb5f0)

~~~json
{
  "source": "00acb5f0",
  "target": "Stack[-0xfd]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb5f4`](#insn-00acb5f4)

~~~json
{
  "source": "00acb5f4",
  "target": "Stack[-0xdd]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb5f8`](#insn-00acb5f8)

~~~json
{
  "source": "00acb5f8",
  "target": "Stack[-0xbd]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb5fc`](#insn-00acb5fc)

~~~json
{
  "source": "00acb5fc",
  "target": "Stack[-0x9d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb600`](#insn-00acb600)

~~~json
{
  "source": "00acb600",
  "target": "Stack[-0x7d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb604`](#insn-00acb604)

~~~json
{
  "source": "00acb604",
  "target": "Stack[-0x5d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb608`](#insn-00acb608)

~~~json
{
  "source": "00acb608",
  "target": "Stack[-0x3f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb60c`](#insn-00acb60c)

~~~json
{
  "source": "00acb60c",
  "target": "Stack[-0x4f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb610`](#insn-00acb610)

~~~json
{
  "source": "00acb610",
  "target": "Stack[-0x3d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb614`](#insn-00acb614)

~~~json
{
  "source": "00acb614",
  "target": "011248e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011248e8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acb618`](#insn-00acb618)

~~~json
{
  "source": "00acb618",
  "target": "011248e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011248e0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acb61c`](#insn-00acb61c)

~~~json
{
  "source": "00acb61c",
  "target": "011248d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011248d8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acb61c`](#insn-00acb61c)

~~~json
{
  "source": "00acb61c",
  "target": "011248e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011248e0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acb628`](#insn-00acb628)

~~~json
{
  "source": "00acb628",
  "target": "011248d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011248d8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acb62c`](#insn-00acb62c)

~~~json
{
  "source": "00acb62c",
  "target": "0043b7b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb630`](#insn-00acb630)

~~~json
{
  "source": "00acb630",
  "target": "011248e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011248e0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acb63c`](#insn-00acb63c)

~~~json
{
  "source": "00acb63c",
  "target": "011248d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011248d8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acb640`](#insn-00acb640)

~~~json
{
  "source": "00acb640",
  "target": "0043b7b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb644`](#insn-00acb644)

~~~json
{
  "source": "00acb644",
  "target": "011248e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011248e0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acb650`](#insn-00acb650)

~~~json
{
  "source": "00acb650",
  "target": "011248d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011248d8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acb654`](#insn-00acb654)

~~~json
{
  "source": "00acb654",
  "target": "0043b7b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb658`](#insn-00acb658)

~~~json
{
  "source": "00acb658",
  "target": "011248e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011248e0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acb664`](#insn-00acb664)

~~~json
{
  "source": "00acb664",
  "target": "011248d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011248d8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acb668`](#insn-00acb668)

~~~json
{
  "source": "00acb668",
  "target": "0043b7b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb66c`](#insn-00acb66c)

~~~json
{
  "source": "00acb66c",
  "target": "011248e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011248e0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acb678`](#insn-00acb678)

~~~json
{
  "source": "00acb678",
  "target": "011248d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011248d8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acb67c`](#insn-00acb67c)

~~~json
{
  "source": "00acb67c",
  "target": "0043b7b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb680`](#insn-00acb680)

~~~json
{
  "source": "00acb680",
  "target": "011248e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011248e0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acb68c`](#insn-00acb68c)

~~~json
{
  "source": "00acb68c",
  "target": "011248d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011248d8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acb690`](#insn-00acb690)

~~~json
{
  "source": "00acb690",
  "target": "0043b7b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb694`](#insn-00acb694)

~~~json
{
  "source": "00acb694",
  "target": "011248e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011248e0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acb6a0`](#insn-00acb6a0)

~~~json
{
  "source": "00acb6a0",
  "target": "011248d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011248d8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acb6a4`](#insn-00acb6a4)

~~~json
{
  "source": "00acb6a4",
  "target": "0043b7b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb6a8`](#insn-00acb6a8)

~~~json
{
  "source": "00acb6a8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb6ac`](#insn-00acb6ac)

~~~json
{
  "source": "00acb6ac",
  "target": "00acb728",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb6b0`](#insn-00acb6b0)

~~~json
{
  "source": "00acb6b0",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb6b4`](#insn-00acb6b4)

~~~json
{
  "source": "00acb6b4",
  "target": "00acb738",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb6b8`](#insn-00acb6b8)

~~~json
{
  "source": "00acb6b8",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb6bc`](#insn-00acb6bc)

~~~json
{
  "source": "00acb6bc",
  "target": "00acb748",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb6c0`](#insn-00acb6c0)

~~~json
{
  "source": "00acb6c0",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb6c4`](#insn-00acb6c4)

~~~json
{
  "source": "00acb6c4",
  "target": "00acb758",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb6c8`](#insn-00acb6c8)

~~~json
{
  "source": "00acb6c8",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb6cc`](#insn-00acb6cc)

~~~json
{
  "source": "00acb6cc",
  "target": "00acb768",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb6d0`](#insn-00acb6d0)

~~~json
{
  "source": "00acb6d0",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb6d4`](#insn-00acb6d4)

~~~json
{
  "source": "00acb6d4",
  "target": "00acb778",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb6d8`](#insn-00acb6d8)

~~~json
{
  "source": "00acb6d8",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb6dc`](#insn-00acb6dc)

~~~json
{
  "source": "00acb6dc",
  "target": "00acb6e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb6e0`](#insn-00acb6e0)

~~~json
{
  "source": "00acb6e0",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb6e4`](#insn-00acb6e4)

~~~json
{
  "source": "00acb6e4",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb6ec`](#insn-00acb6ec)

~~~json
{
  "source": "00acb6ec",
  "target": "0043ae30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb6f4`](#insn-00acb6f4)

~~~json
{
  "source": "00acb6f4",
  "target": "011248d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011248d8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acb6fc`](#insn-00acb6fc)

~~~json
{
  "source": "00acb6fc",
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
- 参照命令 [`00acb700`](#insn-00acb700)

~~~json
{
  "source": "00acb700",
  "target": "00c57a30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb708`](#insn-00acb708)

~~~json
{
  "source": "00acb708",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb710`](#insn-00acb710)

~~~json
{
  "source": "00acb710",
  "target": "00acb858",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb714`](#insn-00acb714)

~~~json
{
  "source": "00acb714",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb718`](#insn-00acb718)

~~~json
{
  "source": "00acb718",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb71c`](#insn-00acb71c)

~~~json
{
  "source": "00acb71c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb728`](#insn-00acb728)

~~~json
{
  "source": "00acb728",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb72c`](#insn-00acb72c)

~~~json
{
  "source": "00acb72c",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb730`](#insn-00acb730)

~~~json
{
  "source": "00acb730",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb734`](#insn-00acb734)

~~~json
{
  "source": "00acb734",
  "target": "00acb6b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb738`](#insn-00acb738)

~~~json
{
  "source": "00acb738",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb73c`](#insn-00acb73c)

~~~json
{
  "source": "00acb73c",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb740`](#insn-00acb740)

~~~json
{
  "source": "00acb740",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb744`](#insn-00acb744)

~~~json
{
  "source": "00acb744",
  "target": "00acb6c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb748`](#insn-00acb748)

~~~json
{
  "source": "00acb748",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb74c`](#insn-00acb74c)

~~~json
{
  "source": "00acb74c",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb750`](#insn-00acb750)

~~~json
{
  "source": "00acb750",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb754`](#insn-00acb754)

~~~json
{
  "source": "00acb754",
  "target": "00acb6c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb758`](#insn-00acb758)

~~~json
{
  "source": "00acb758",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb75c`](#insn-00acb75c)

~~~json
{
  "source": "00acb75c",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb760`](#insn-00acb760)

~~~json
{
  "source": "00acb760",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb764`](#insn-00acb764)

~~~json
{
  "source": "00acb764",
  "target": "00acb6d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb768`](#insn-00acb768)

~~~json
{
  "source": "00acb768",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb76c`](#insn-00acb76c)

~~~json
{
  "source": "00acb76c",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb770`](#insn-00acb770)

~~~json
{
  "source": "00acb770",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb774`](#insn-00acb774)

~~~json
{
  "source": "00acb774",
  "target": "00acb6d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb778`](#insn-00acb778)

~~~json
{
  "source": "00acb778",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb77c`](#insn-00acb77c)

~~~json
{
  "source": "00acb77c",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb780`](#insn-00acb780)

~~~json
{
  "source": "00acb780",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb784`](#insn-00acb784)

~~~json
{
  "source": "00acb784",
  "target": "00acb6e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb788`](#insn-00acb788)

~~~json
{
  "source": "00acb788",
  "target": "00acb6e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb858`](#insn-00acb858)

~~~json
{
  "source": "00acb858",
  "target": "00c57ae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
