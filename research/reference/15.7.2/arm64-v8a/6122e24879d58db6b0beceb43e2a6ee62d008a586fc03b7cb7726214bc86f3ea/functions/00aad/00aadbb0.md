# 00aadbb0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aadc78`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aadc78.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0056.md#compare-9cf9567f16260a7aabf8a91159f86133)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aadbb0",
  "name": "_INIT_246",
  "size": 708,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b2637211b9c069454ff0c5a27dba7a61d0ba840be60464bea636076610f45aad",
  "source_text_sha256": "b2637211b9c069454ff0c5a27dba7a61d0ba840be60464bea636076610f45aad",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aadbb0",
        "00aade6f"
      ],
      [
        "00aadf3c",
        "00aadf3f"
      ]
    ],
    "bytes_sha256": "1175a18dc4de53663e70f35f3491ba2554a240f1f91f76dc7061288598199a2e",
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
  DAT_0109f9f0 = 0;
  DAT_0109f9e8 = 0;
  DAT_0109f9e0 = &DAT_0109f9e8;
  FUN_00418cb8(&DAT_0109f9e0,&DAT_0109f9e8,local_118,local_118);
  FUN_00418cb8(&DAT_0109f9e0,&DAT_0109f9e8,local_f8,local_f8);
  FUN_00418cb8(&DAT_0109f9e0,&DAT_0109f9e8,local_d8,local_d8);
  FUN_00418cb8(&DAT_0109f9e0,&DAT_0109f9e8,local_b8,local_b8);
  FUN_00418cb8(&DAT_0109f9e0,&DAT_0109f9e8,local_98,local_98);
  FUN_00418cb8(&DAT_0109f9e0,&DAT_0109f9e8,local_78,local_78);
  FUN_00418cb8(&DAT_0109f9e0,&DAT_0109f9e8,local_58,local_58);
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
  __cxa_atexit(FUN_00418330,&DAT_0109f9e0,&PTR_LOOP_00be5ed0);
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
<a id="insn-00aadbb0"></a> `00aadbb0` | `ff 83 04 d1` | sub sp,sp,#0x120 | `FALL_THROUGH`
<a id="insn-00aadbb4"></a> `00aadbb4` | `fd 7b 0f a9` | stp x29,x30,[sp, #0xf0] | `FALL_THROUGH`
<a id="insn-00aadbb8"></a> `00aadbb8` | `fc 57 10 a9` | stp x28,x21,[sp, #0x100] | `FALL_THROUGH`
<a id="insn-00aadbbc"></a> `00aadbbc` | `f4 4f 11 a9` | stp x20,x19,[sp, #0x110] | `FALL_THROUGH`
<a id="insn-00aadbc0"></a> `00aadbc0` | `fd c3 03 91` | add x29,sp,#0xf0 | `FALL_THROUGH`
<a id="insn-00aadbc4"></a> `00aadbc4` | `55 d0 3b d5` | mrs x21,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00aadbc8"></a> `00aadbc8` | `2a e8 8c 52` | mov w10,#0x6741 | `FALL_THROUGH`
<a id="insn-00aadbcc"></a> `00aadbcc` | `f4 23 00 91` | add x20,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00aadbd0"></a> `00aadbd0` | `a9 16 40 f9` | ldr x9,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00aadbd4"></a> `00aadbd4` | `88 04 80 52` | mov w8,#0x24 | `FALL_THROUGH`
<a id="insn-00aadbd8"></a> `00aadbd8` | `93 2f 00 d0` | adrp x19,0x109f000 | `FALL_THROUGH`
<a id="insn-00aadbdc"></a> `00aadbdc` | `73 82 27 91` | add x19,x19,#0x9e0 | `FALL_THROUGH`
<a id="insn-00aadbe0"></a> `00aadbe0` | `a9 83 1f f8` | stur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aadbe4"></a> `00aadbe4` | `c9 bf ff d0` | adrp x9,0x2a7000 | `FALL_THROUGH`
<a id="insn-00aadbe8"></a> `00aadbe8` | `29 91 0b 91` | add x9,x9,#0x2e4 | `FALL_THROUGH`
<a id="insn-00aadbec"></a> `00aadbec` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00aadbf0"></a> `00aadbf0` | `29 00 80 52` | mov w9,#0x1 | `FALL_THROUGH`
<a id="insn-00aadbf4"></a> `00aadbf4` | `ea 13 02 78` | sturh w10,[sp, #0x21] | `FALL_THROUGH`
<a id="insn-00aadbf8"></a> `00aadbf8` | `e9 2b 00 b9` | str w9,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00aadbfc"></a> `00aadbfc` | `49 28 88 52` | mov w9,#0x4142 | `FALL_THROUGH`
<a id="insn-00aadc00"></a> `00aadc00` | `ca bf ff d0` | adrp x10,0x2a7000 | `FALL_THROUGH`
<a id="insn-00aadc04"></a> `00aadc04` | `4a dd 0b 91` | add x10,x10,#0x2f7 | `FALL_THROUGH`
<a id="insn-00aadc08"></a> `00aadc08` | `e0 13 81 3c` | stur q0,[sp, #0x11] | `FALL_THROUGH`
<a id="insn-00aadc0c"></a> `00aadc0c` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00aadc10"></a> `00aadc10` | `40 01 c0 3d` | ldr q0,[x10] | `FALL_THROUGH`
<a id="insn-00aadc14"></a> `00aadc14` | `e9 13 04 78` | sturh w9,[sp, #0x41] | `FALL_THROUGH`
<a id="insn-00aadc18"></a> `00aadc18` | `49 00 80 52` | mov w9,#0x2 | `FALL_THROUGH`
<a id="insn-00aadc1c"></a> `00aadc1c` | `e9 4b 00 b9` | str w9,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00aadc20"></a> `00aadc20` | `49 e8 8c 52` | mov w9,#0x6742 | `FALL_THROUGH`
<a id="insn-00aadc24"></a> `00aadc24` | `ca bf ff f0` | adrp x10,0x2a8000 | `FALL_THROUGH`
<a id="insn-00aadc28"></a> `00aadc28` | `4a 69 03 91` | add x10,x10,#0xda | `FALL_THROUGH`
<a id="insn-00aadc2c"></a> `00aadc2c` | `e0 13 83 3c` | stur q0,[sp, #0x31] | `FALL_THROUGH`
<a id="insn-00aadc30"></a> `00aadc30` | `40 01 c0 3d` | ldr q0,[x10] | `FALL_THROUGH`
<a id="insn-00aadc34"></a> `00aadc34` | `e9 13 06 78` | sturh w9,[sp, #0x61] | `FALL_THROUGH`
<a id="insn-00aadc38"></a> `00aadc38` | `69 00 80 52` | mov w9,#0x3 | `FALL_THROUGH`
<a id="insn-00aadc3c"></a> `00aadc3c` | `e9 6b 00 b9` | str w9,[sp, #0x68] | `FALL_THROUGH`
<a id="insn-00aadc40"></a> `00aadc40` | `29 e8 8e 52` | mov w9,#0x7741 | `FALL_THROUGH`
<a id="insn-00aadc44"></a> `00aadc44` | `2a bf ff d0` | adrp x10,0x293000 | `FALL_THROUGH`
<a id="insn-00aadc48"></a> `00aadc48` | `4a b9 1a 91` | add x10,x10,#0x6ae | `FALL_THROUGH`
<a id="insn-00aadc4c"></a> `00aadc4c` | `e0 13 85 3c` | stur q0,[sp, #0x51] | `FALL_THROUGH`
<a id="insn-00aadc50"></a> `00aadc50` | `40 01 c0 3d` | ldr q0,[x10] | `FALL_THROUGH`
<a id="insn-00aadc54"></a> `00aadc54` | `e9 13 08 78` | sturh w9,[sp, #0x81] | `FALL_THROUGH`
<a id="insn-00aadc58"></a> `00aadc58` | `89 00 80 52` | mov w9,#0x4 | `FALL_THROUGH`
<a id="insn-00aadc5c"></a> `00aadc5c` | `e9 8b 00 b9` | str w9,[sp, #0x88] | `FALL_THROUGH`
<a id="insn-00aadc60"></a> `00aadc60` | `69 bf ff f0` | adrp x9,0x29c000 | `FALL_THROUGH`
<a id="insn-00aadc64"></a> `00aadc64` | `29 85 0b 91` | add x9,x9,#0x2e1 | `FALL_THROUGH`
<a id="insn-00aadc68"></a> `00aadc68` | `e0 13 87 3c` | stur q0,[sp, #0x71] | `FALL_THROUGH`
<a id="insn-00aadc6c"></a> `00aadc6c` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00aadc70"></a> `00aadc70` | `49 28 8a 52` | mov w9,#0x5142 | `FALL_THROUGH`
<a id="insn-00aadc74"></a> `00aadc74` | `89 92 09 78` | sturh w9,[x20, #0x99] | `FALL_THROUGH`
<a id="insn-00aadc78"></a> `00aadc78` | `a9 00 80 52` | mov w9,#0x5 | `FALL_THROUGH`
<a id="insn-00aadc7c"></a> `00aadc7c` | `e9 ab 00 b9` | str w9,[sp, #0xa8] | `FALL_THROUGH`
<a id="insn-00aadc80"></a> `00aadc80` | `29 bf ff 90` | adrp x9,0x291000 | `FALL_THROUGH`
<a id="insn-00aadc84"></a> `00aadc84` | `29 dd 21 91` | add x9,x9,#0x877 | `FALL_THROUGH`
<a id="insn-00aadc88"></a> `00aadc88` | `80 92 88 3c` | stur q0,[x20, #0x89] | `FALL_THROUGH`
<a id="insn-00aadc8c"></a> `00aadc8c` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00aadc90"></a> `00aadc90` | `49 e8 8e 52` | mov w9,#0x7742 | `FALL_THROUGH`
<a id="insn-00aadc94"></a> `00aadc94` | `89 92 0b 78` | sturh w9,[x20, #0xb9] | `FALL_THROUGH`
<a id="insn-00aadc98"></a> `00aadc98` | `c9 00 80 52` | mov w9,#0x6 | `FALL_THROUGH`
<a id="insn-00aadc9c"></a> `00aadc9c` | `e9 cb 00 b9` | str w9,[sp, #0xc8] | `FALL_THROUGH`
<a id="insn-00aadca0"></a> `00aadca0` | `29 bf ff f0` | adrp x9,0x294000 | `FALL_THROUGH`
<a id="insn-00aadca4"></a> `00aadca4` | `29 99 14 91` | add x9,x9,#0x526 | `FALL_THROUGH`
<a id="insn-00aadca8"></a> `00aadca8` | `80 92 8a 3c` | stur q0,[x20, #0xa9] | `FALL_THROUGH`
<a id="insn-00aadcac"></a> `00aadcac` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00aadcb0"></a> `00aadcb0` | `e8 43 00 39` | strb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aadcb4"></a> `00aadcb4` | `e8 c3 00 39` | strb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aadcb8"></a> `00aadcb8` | `e8 43 01 39` | strb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00aadcbc"></a> `00aadcbc` | `e8 c3 01 39` | strb w8,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00aadcc0"></a> `00aadcc0` | `e8 43 02 39` | strb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00aadcc4"></a> `00aadcc4` | `e8 c3 02 39` | strb w8,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00aadcc8"></a> `00aadcc8` | `e8 43 03 39` | strb w8,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-00aadccc"></a> `00aadccc` | `68 28 88 52` | mov w8,#0x4143 | `FALL_THROUGH`
<a id="insn-00aadcd0"></a> `00aadcd0` | `ff 0b 00 b9` | str wzr,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00aadcd4"></a> `00aadcd4` | `ff 8f 00 39` | strb wzr,[sp, #0x23] | `FALL_THROUGH`
<a id="insn-00aadcd8"></a> `00aadcd8` | `ff 0f 01 39` | strb wzr,[sp, #0x43] | `FALL_THROUGH`
<a id="insn-00aadcdc"></a> `00aadcdc` | `ff 8f 01 39` | strb wzr,[sp, #0x63] | `FALL_THROUGH`
<a id="insn-00aadce0"></a> `00aadce0` | `ff 0f 02 39` | strb wzr,[sp, #0x83] | `FALL_THROUGH`
<a id="insn-00aadce4"></a> `00aadce4` | `ff 8f 02 39` | strb wzr,[sp, #0xa3] | `FALL_THROUGH`
<a id="insn-00aadce8"></a> `00aadce8` | `ff 0f 03 39` | strb wzr,[sp, #0xc3] | `FALL_THROUGH`
<a id="insn-00aadcec"></a> `00aadcec` | `88 92 0d 78` | sturh w8,[x20, #0xd9] | `FALL_THROUGH`
<a id="insn-00aadcf0"></a> `00aadcf0` | `80 92 8c 3c` | stur q0,[x20, #0xc9] | `FALL_THROUGH`
<a id="insn-00aadcf4"></a> `00aadcf4` | `ff 8f 03 39` | strb wzr,[sp, #0xe3] | `FALL_THROUGH`
<a id="insn-00aadcf8"></a> `00aadcf8` | `7f 0a 00 f9` | str xzr,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00aadcfc"></a> `00aadcfc` | `3f 8c 00 f8` | str xzr,[x1, #0x8]! | `FALL_THROUGH`
<a id="insn-00aadd00"></a> `00aadd00` | `61 02 00 f9` | str x1,[x19] | `FALL_THROUGH`
<a id="insn-00aadd04"></a> `00aadd04` | `e2 23 00 91` | add x2,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00aadd08"></a> `00aadd08` | `e3 23 00 91` | add x3,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00aadd0c"></a> `00aadd0c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aadd10"></a> `00aadd10` | `ea ab e5 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-00aadd14"></a> `00aadd14` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00aadd18"></a> `00aadd18` | `82 82 00 91` | add x2,x20,#0x20 | `FALL_THROUGH`
<a id="insn-00aadd1c"></a> `00aadd1c` | `83 82 00 91` | add x3,x20,#0x20 | `FALL_THROUGH`
<a id="insn-00aadd20"></a> `00aadd20` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aadd24"></a> `00aadd24` | `e5 ab e5 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-00aadd28"></a> `00aadd28` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00aadd2c"></a> `00aadd2c` | `82 02 01 91` | add x2,x20,#0x40 | `FALL_THROUGH`
<a id="insn-00aadd30"></a> `00aadd30` | `83 02 01 91` | add x3,x20,#0x40 | `FALL_THROUGH`
<a id="insn-00aadd34"></a> `00aadd34` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aadd38"></a> `00aadd38` | `e0 ab e5 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-00aadd3c"></a> `00aadd3c` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00aadd40"></a> `00aadd40` | `82 82 01 91` | add x2,x20,#0x60 | `FALL_THROUGH`
<a id="insn-00aadd44"></a> `00aadd44` | `83 82 01 91` | add x3,x20,#0x60 | `FALL_THROUGH`
<a id="insn-00aadd48"></a> `00aadd48` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aadd4c"></a> `00aadd4c` | `db ab e5 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-00aadd50"></a> `00aadd50` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00aadd54"></a> `00aadd54` | `82 02 02 91` | add x2,x20,#0x80 | `FALL_THROUGH`
<a id="insn-00aadd58"></a> `00aadd58` | `83 02 02 91` | add x3,x20,#0x80 | `FALL_THROUGH`
<a id="insn-00aadd5c"></a> `00aadd5c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aadd60"></a> `00aadd60` | `d6 ab e5 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-00aadd64"></a> `00aadd64` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00aadd68"></a> `00aadd68` | `82 82 02 91` | add x2,x20,#0xa0 | `FALL_THROUGH`
<a id="insn-00aadd6c"></a> `00aadd6c` | `83 82 02 91` | add x3,x20,#0xa0 | `FALL_THROUGH`
<a id="insn-00aadd70"></a> `00aadd70` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aadd74"></a> `00aadd74` | `d1 ab e5 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-00aadd78"></a> `00aadd78` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00aadd7c"></a> `00aadd7c` | `82 02 03 91` | add x2,x20,#0xc0 | `FALL_THROUGH`
<a id="insn-00aadd80"></a> `00aadd80` | `83 02 03 91` | add x3,x20,#0xc0 | `FALL_THROUGH`
<a id="insn-00aadd84"></a> `00aadd84` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aadd88"></a> `00aadd88` | `cc ab e5 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-00aadd8c"></a> `00aadd8c` | `e8 43 43 39` | ldrb w8,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-00aadd90"></a> `00aadd90` | `e8 03 00 37` | tbnz w8,#0x0,0x00aade0c | `CONDITIONAL_JUMP`
<a id="insn-00aadd94"></a> `00aadd94` | `e8 c3 42 39` | ldrb w8,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00aadd98"></a> `00aadd98` | `28 04 00 37` | tbnz w8,#0x0,0x00aade1c | `CONDITIONAL_JUMP`
<a id="insn-00aadd9c"></a> `00aadd9c` | `e8 43 42 39` | ldrb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00aadda0"></a> `00aadda0` | `68 04 00 37` | tbnz w8,#0x0,0x00aade2c | `CONDITIONAL_JUMP`
<a id="insn-00aadda4"></a> `00aadda4` | `e8 c3 41 39` | ldrb w8,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00aadda8"></a> `00aadda8` | `a8 04 00 37` | tbnz w8,#0x0,0x00aade3c | `CONDITIONAL_JUMP`
<a id="insn-00aaddac"></a> `00aaddac` | `e8 43 41 39` | ldrb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00aaddb0"></a> `00aaddb0` | `e8 04 00 37` | tbnz w8,#0x0,0x00aade4c | `CONDITIONAL_JUMP`
<a id="insn-00aaddb4"></a> `00aaddb4` | `e8 c3 40 39` | ldrb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aaddb8"></a> `00aaddb8` | `28 05 00 37` | tbnz w8,#0x0,0x00aade5c | `CONDITIONAL_JUMP`
<a id="insn-00aaddbc"></a> `00aaddbc` | `e8 43 40 39` | ldrb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aaddc0"></a> `00aaddc0` | `68 00 00 36` | tbz w8,#0x0,0x00aaddcc | `CONDITIONAL_JUMP`
<a id="insn-00aaddc4"></a> `00aaddc4` | `e0 13 40 f9` | ldr x0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aaddc8"></a> `00aaddc8` | `66 b4 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00aaddcc"></a> `00aaddcc` | `40 cb ff f0` | adrp x0,0x418000 | `FALL_THROUGH`
<a id="insn-00aaddd0"></a> `00aaddd0` | `00 c0 0c 91` | add x0,x0,#0x330 | `FALL_THROUGH`
<a id="insn-00aaddd4"></a> `00aaddd4` | `81 2f 00 d0` | adrp x1,0x109f000 | `FALL_THROUGH`
<a id="insn-00aaddd8"></a> `00aaddd8` | `21 80 27 91` | add x1,x1,#0x9e0 | `FALL_THROUGH`
<a id="insn-00aadddc"></a> `00aadddc` | `c2 09 00 90` | adrp x2,0xbe5000 | `FALL_THROUGH`
<a id="insn-00aadde0"></a> `00aadde0` | `42 40 3b 91` | add x2,x2,#0xed0 | `FALL_THROUGH`
<a id="insn-00aadde4"></a> `00aadde4` | `3f b4 04 94` | bl 0x00bdaee0 | `UNCONDITIONAL_CALL`
<a id="insn-00aadde8"></a> `00aadde8` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00aaddec"></a> `00aaddec` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aaddf0"></a> `00aaddf0` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00aaddf4"></a> `00aaddf4` | `41 0a 00 54` | b.ne 0x00aadf3c | `CONDITIONAL_JUMP`
<a id="insn-00aaddf8"></a> `00aaddf8` | `f4 4f 51 a9` | ldp x20,x19,[sp, #0x110] | `FALL_THROUGH`
<a id="insn-00aaddfc"></a> `00aaddfc` | `fc 57 50 a9` | ldp x28,x21,[sp, #0x100] | `FALL_THROUGH`
<a id="insn-00aade00"></a> `00aade00` | `fd 7b 4f a9` | ldp x29,x30,[sp, #0xf0] | `FALL_THROUGH`
<a id="insn-00aade04"></a> `00aade04` | `ff 83 04 91` | add sp,sp,#0x120 | `FALL_THROUGH`
<a id="insn-00aade08"></a> `00aade08` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00aade0c"></a> `00aade0c` | `e0 73 40 f9` | ldr x0,[sp, #0xe0] | `FALL_THROUGH`
<a id="insn-00aade10"></a> `00aade10` | `54 b4 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00aade14"></a> `00aade14` | `e8 c3 42 39` | ldrb w8,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00aade18"></a> `00aade18` | `28 fc 07 36` | tbz w8,#0x0,0x00aadd9c | `CONDITIONAL_JUMP`
<a id="insn-00aade1c"></a> `00aade1c` | `e0 63 40 f9` | ldr x0,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00aade20"></a> `00aade20` | `50 b4 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00aade24"></a> `00aade24` | `e8 43 42 39` | ldrb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00aade28"></a> `00aade28` | `e8 fb 07 36` | tbz w8,#0x0,0x00aadda4 | `CONDITIONAL_JUMP`
<a id="insn-00aade2c"></a> `00aade2c` | `e0 53 40 f9` | ldr x0,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00aade30"></a> `00aade30` | `4c b4 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00aade34"></a> `00aade34` | `e8 c3 41 39` | ldrb w8,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00aade38"></a> `00aade38` | `a8 fb 07 36` | tbz w8,#0x0,0x00aaddac | `CONDITIONAL_JUMP`
<a id="insn-00aade3c"></a> `00aade3c` | `e0 43 40 f9` | ldr x0,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00aade40"></a> `00aade40` | `48 b4 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00aade44"></a> `00aade44` | `e8 43 41 39` | ldrb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00aade48"></a> `00aade48` | `68 fb 07 36` | tbz w8,#0x0,0x00aaddb4 | `CONDITIONAL_JUMP`
<a id="insn-00aade4c"></a> `00aade4c` | `e0 33 40 f9` | ldr x0,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00aade50"></a> `00aade50` | `44 b4 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00aade54"></a> `00aade54` | `e8 c3 40 39` | ldrb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aade58"></a> `00aade58` | `28 fb 07 36` | tbz w8,#0x0,0x00aaddbc | `CONDITIONAL_JUMP`
<a id="insn-00aade5c"></a> `00aade5c` | `e0 23 40 f9` | ldr x0,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00aade60"></a> `00aade60` | `40 b4 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00aade64"></a> `00aade64` | `e8 43 40 39` | ldrb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aade68"></a> `00aade68` | `e8 fa 07 37` | tbnz w8,#0x0,0x00aaddc4 | `CONDITIONAL_JUMP`
<a id="insn-00aade6c"></a> `00aade6c` | `d8 ff ff 17` | b 0x00aaddcc | `UNCONDITIONAL_JUMP`
<a id="insn-00aadf3c"></a> `00aadf3c` | `15 b4 04 94` | bl 0x00bdaf90 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aadbb0`](#insn-00aadbb0) 範囲 `[['00aadbb0', '00aadd93']]`
  - `CONDITIONAL_JUMP` [`00aadd90`](#insn-00aadd90) → [`00aade0c`](#insn-00aade0c)
  - `FALL_THROUGH` [`00aadd90`](#insn-00aadd90) → [`00aadd94`](#insn-00aadd94)
- ブロック [`00aadd94`](#insn-00aadd94) 範囲 `[['00aadd94', '00aadd9b']]`
  - `CONDITIONAL_JUMP` [`00aadd98`](#insn-00aadd98) → [`00aade1c`](#insn-00aade1c)
  - `FALL_THROUGH` [`00aadd98`](#insn-00aadd98) → [`00aadd9c`](#insn-00aadd9c)
- ブロック [`00aadd9c`](#insn-00aadd9c) 範囲 `[['00aadd9c', '00aadda3']]`
  - `CONDITIONAL_JUMP` [`00aadda0`](#insn-00aadda0) → [`00aade2c`](#insn-00aade2c)
  - `FALL_THROUGH` [`00aadda0`](#insn-00aadda0) → [`00aadda4`](#insn-00aadda4)
- ブロック [`00aadda4`](#insn-00aadda4) 範囲 `[['00aadda4', '00aaddab']]`
  - `CONDITIONAL_JUMP` [`00aadda8`](#insn-00aadda8) → [`00aade3c`](#insn-00aade3c)
  - `FALL_THROUGH` [`00aadda8`](#insn-00aadda8) → [`00aaddac`](#insn-00aaddac)
- ブロック [`00aaddac`](#insn-00aaddac) 範囲 `[['00aaddac', '00aaddb3']]`
  - `CONDITIONAL_JUMP` [`00aaddb0`](#insn-00aaddb0) → [`00aade4c`](#insn-00aade4c)
  - `FALL_THROUGH` [`00aaddb0`](#insn-00aaddb0) → [`00aaddb4`](#insn-00aaddb4)
- ブロック [`00aaddb4`](#insn-00aaddb4) 範囲 `[['00aaddb4', '00aaddbb']]`
  - `CONDITIONAL_JUMP` [`00aaddb8`](#insn-00aaddb8) → [`00aade5c`](#insn-00aade5c)
  - `FALL_THROUGH` [`00aaddb8`](#insn-00aaddb8) → [`00aaddbc`](#insn-00aaddbc)
- ブロック [`00aaddbc`](#insn-00aaddbc) 範囲 `[['00aaddbc', '00aaddc3']]`
  - `CONDITIONAL_JUMP` [`00aaddc0`](#insn-00aaddc0) → [`00aaddcc`](#insn-00aaddcc)
  - `FALL_THROUGH` [`00aaddc0`](#insn-00aaddc0) → [`00aaddc4`](#insn-00aaddc4)
- ブロック [`00aaddc4`](#insn-00aaddc4) 範囲 `[['00aaddc4', '00aaddcb']]`
  - `FALL_THROUGH` [`00aaddc8`](#insn-00aaddc8) → [`00aaddcc`](#insn-00aaddcc)
- ブロック [`00aaddcc`](#insn-00aaddcc) 範囲 `[['00aaddcc', '00aaddf7']]`
  - `CONDITIONAL_JUMP` [`00aaddf4`](#insn-00aaddf4) → [`00aadf3c`](#insn-00aadf3c)
  - `FALL_THROUGH` [`00aaddf4`](#insn-00aaddf4) → [`00aaddf8`](#insn-00aaddf8)
- ブロック [`00aaddf8`](#insn-00aaddf8) 範囲 `[['00aaddf8', '00aade0b']]`
- ブロック [`00aade0c`](#insn-00aade0c) 範囲 `[['00aade0c', '00aade1b']]`
  - `CONDITIONAL_JUMP` [`00aade18`](#insn-00aade18) → [`00aadd9c`](#insn-00aadd9c)
  - `FALL_THROUGH` [`00aade18`](#insn-00aade18) → [`00aade1c`](#insn-00aade1c)
- ブロック [`00aade1c`](#insn-00aade1c) 範囲 `[['00aade1c', '00aade2b']]`
  - `CONDITIONAL_JUMP` [`00aade28`](#insn-00aade28) → [`00aadda4`](#insn-00aadda4)
  - `FALL_THROUGH` [`00aade28`](#insn-00aade28) → [`00aade2c`](#insn-00aade2c)
- ブロック [`00aade2c`](#insn-00aade2c) 範囲 `[['00aade2c', '00aade3b']]`
  - `CONDITIONAL_JUMP` [`00aade38`](#insn-00aade38) → [`00aaddac`](#insn-00aaddac)
  - `FALL_THROUGH` [`00aade38`](#insn-00aade38) → [`00aade3c`](#insn-00aade3c)
- ブロック [`00aade3c`](#insn-00aade3c) 範囲 `[['00aade3c', '00aade4b']]`
  - `CONDITIONAL_JUMP` [`00aade48`](#insn-00aade48) → [`00aaddb4`](#insn-00aaddb4)
  - `FALL_THROUGH` [`00aade48`](#insn-00aade48) → [`00aade4c`](#insn-00aade4c)
- ブロック [`00aade4c`](#insn-00aade4c) 範囲 `[['00aade4c', '00aade5b']]`
  - `CONDITIONAL_JUMP` [`00aade58`](#insn-00aade58) → [`00aaddbc`](#insn-00aaddbc)
  - `FALL_THROUGH` [`00aade58`](#insn-00aade58) → [`00aade5c`](#insn-00aade5c)
- ブロック [`00aade5c`](#insn-00aade5c) 範囲 `[['00aade5c', '00aade6b']]`
  - `CONDITIONAL_JUMP` [`00aade68`](#insn-00aade68) → [`00aaddc4`](#insn-00aaddc4)
  - `FALL_THROUGH` [`00aade68`](#insn-00aade68) → [`00aade6c`](#insn-00aade6c)
- ブロック [`00aade6c`](#insn-00aade6c) 範囲 `[['00aade6c', '00aade6f']]`
  - `UNCONDITIONAL_JUMP` [`00aade6c`](#insn-00aade6c) → [`00aaddcc`](#insn-00aaddcc)
- ブロック [`00aadf3c`](#insn-00aadf3c) 範囲 `[['00aadf3c', '00aadf3f']]`

## 命令位置別の参照

- [`00aadbb4`](#insn-00aadbb4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadbb8`](#insn-00aadbb8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadbbc`](#insn-00aadbbc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadbe0`](#insn-00aadbe0) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadbec`](#insn-00aadbec) → `002a72e4`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aadbf4`](#insn-00aadbf4) → `Stack[-0xff]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadbf8`](#insn-00aadbf8) → `Stack[-0xf8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadc08`](#insn-00aadc08) → `Stack[-0x10f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadc10`](#insn-00aadc10) → `002a72f7`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aadc14`](#insn-00aadc14) → `Stack[-0xdf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadc1c`](#insn-00aadc1c) → `Stack[-0xd8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadc2c`](#insn-00aadc2c) → `Stack[-0xef]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadc30`](#insn-00aadc30) → `002a80da`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aadc34`](#insn-00aadc34) → `Stack[-0xbf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadc3c`](#insn-00aadc3c) → `Stack[-0xb8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadc4c`](#insn-00aadc4c) → `Stack[-0xcf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadc50`](#insn-00aadc50) → `002936ae`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aadc54`](#insn-00aadc54) → `Stack[-0x9f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadc5c`](#insn-00aadc5c) → `Stack[-0x98]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadc68`](#insn-00aadc68) → `Stack[-0xaf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadc6c`](#insn-00aadc6c) → `0029c2e1`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aadc74`](#insn-00aadc74) → `Stack[-0x7f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadc7c`](#insn-00aadc7c) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadc88`](#insn-00aadc88) → `Stack[-0x8f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadc8c`](#insn-00aadc8c) → `00291877`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aadc94`](#insn-00aadc94) → `Stack[-0x5f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadc9c`](#insn-00aadc9c) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadca8`](#insn-00aadca8) → `Stack[-0x6f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadcac`](#insn-00aadcac) → `00294526`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aadcb0`](#insn-00aadcb0) → `Stack[-0x110]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadcb4`](#insn-00aadcb4) → `Stack[-0xf0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadcb8`](#insn-00aadcb8) → `Stack[-0xd0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadcbc`](#insn-00aadcbc) → `Stack[-0xb0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadcc0`](#insn-00aadcc0) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadcc4`](#insn-00aadcc4) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadcc8`](#insn-00aadcc8) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadcd0`](#insn-00aadcd0) → `Stack[-0x118]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadcd4`](#insn-00aadcd4) → `Stack[-0xfd]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadcd8`](#insn-00aadcd8) → `Stack[-0xdd]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadcdc`](#insn-00aadcdc) → `Stack[-0xbd]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadce0`](#insn-00aadce0) → `Stack[-0x9d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadce4`](#insn-00aadce4) → `Stack[-0x7d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadce8`](#insn-00aadce8) → `Stack[-0x5d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadcec`](#insn-00aadcec) → `Stack[-0x3f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadcf0`](#insn-00aadcf0) → `Stack[-0x4f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadcf4`](#insn-00aadcf4) → `Stack[-0x3d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadcf8`](#insn-00aadcf8) → `0109f9f0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aadcfc`](#insn-00aadcfc) → `0109f9e8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aadd00`](#insn-00aadd00) → `0109f9e0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aadd00`](#insn-00aadd00) → `0109f9e8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aadd0c`](#insn-00aadd0c) → `0109f9e0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aadd10`](#insn-00aadd10) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`00aadd14`](#insn-00aadd14) → `0109f9e8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aadd20`](#insn-00aadd20) → `0109f9e0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aadd24`](#insn-00aadd24) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`00aadd28`](#insn-00aadd28) → `0109f9e8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aadd34`](#insn-00aadd34) → `0109f9e0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aadd38`](#insn-00aadd38) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`00aadd3c`](#insn-00aadd3c) → `0109f9e8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aadd48`](#insn-00aadd48) → `0109f9e0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aadd4c`](#insn-00aadd4c) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`00aadd50`](#insn-00aadd50) → `0109f9e8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aadd5c`](#insn-00aadd5c) → `0109f9e0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aadd60`](#insn-00aadd60) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`00aadd64`](#insn-00aadd64) → `0109f9e8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aadd70`](#insn-00aadd70) → `0109f9e0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aadd74`](#insn-00aadd74) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`00aadd78`](#insn-00aadd78) → `0109f9e8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aadd84`](#insn-00aadd84) → `0109f9e0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aadd88`](#insn-00aadd88) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`00aadd8c`](#insn-00aadd8c) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadd90`](#insn-00aadd90) → [`00aade0c`](#insn-00aade0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadd94`](#insn-00aadd94) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadd98`](#insn-00aadd98) → [`00aade1c`](#insn-00aade1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadd9c`](#insn-00aadd9c) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadda0`](#insn-00aadda0) → [`00aade2c`](#insn-00aade2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadda4`](#insn-00aadda4) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadda8`](#insn-00aadda8) → [`00aade3c`](#insn-00aade3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaddac`](#insn-00aaddac) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaddb0`](#insn-00aaddb0) → [`00aade4c`](#insn-00aade4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaddb4`](#insn-00aaddb4) → `Stack[-0xf0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaddb8`](#insn-00aaddb8) → [`00aade5c`](#insn-00aade5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaddbc`](#insn-00aaddbc) → `Stack[-0x110]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaddc0`](#insn-00aaddc0) → [`00aaddcc`](#insn-00aaddcc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaddc4`](#insn-00aaddc4) → `Stack[-0x100]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaddc8`](#insn-00aaddc8) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00aaddd0`](#insn-00aaddd0) → [`00418330`](../00418/00418330.md) · `PARAM` · `ANALYSIS` · 関数 `00418330` · 推定シンボル `None` · 推定型 `None`
- [`00aaddd8`](#insn-00aaddd8) → `0109f9e0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aadde0`](#insn-00aadde0) → `00be5ed0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00aadde4`](#insn-00aadde4) → [`00bdaee0`](../00bda/00bdaee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaee0` · 推定シンボル `None` · 推定型 `None`
- [`00aaddec`](#insn-00aaddec) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaddf4`](#insn-00aaddf4) → [`00aadf3c`](#insn-00aadf3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaddf8`](#insn-00aaddf8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaddfc`](#insn-00aaddfc) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aade00`](#insn-00aade00) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aade0c`](#insn-00aade0c) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aade10`](#insn-00aade10) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00aade14`](#insn-00aade14) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aade18`](#insn-00aade18) → [`00aadd9c`](#insn-00aadd9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aade1c`](#insn-00aade1c) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aade20`](#insn-00aade20) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00aade24`](#insn-00aade24) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aade28`](#insn-00aade28) → [`00aadda4`](#insn-00aadda4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aade2c`](#insn-00aade2c) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aade30`](#insn-00aade30) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00aade34`](#insn-00aade34) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aade38`](#insn-00aade38) → [`00aaddac`](#insn-00aaddac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aade3c`](#insn-00aade3c) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aade40`](#insn-00aade40) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00aade44`](#insn-00aade44) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aade48`](#insn-00aade48) → [`00aaddb4`](#insn-00aaddb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aade4c`](#insn-00aade4c) → `Stack[-0xc0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aade50`](#insn-00aade50) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00aade54`](#insn-00aade54) → `Stack[-0xf0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aade58`](#insn-00aade58) → [`00aaddbc`](#insn-00aaddbc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aade5c`](#insn-00aade5c) → `Stack[-0xe0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aade60`](#insn-00aade60) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00aade64`](#insn-00aade64) → `Stack[-0x110]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aade68`](#insn-00aade68) → [`00aaddc4`](#insn-00aaddc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aade6c`](#insn-00aade6c) → [`00aaddcc`](#insn-00aaddcc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadf3c`](#insn-00aadf3c) → [`00bdaf90`](../00bda/00bdaf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf90` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aadbb4`](#insn-00aadbb4)

~~~json
{
  "source": "00aadbb4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadbb8`](#insn-00aadbb8)

~~~json
{
  "source": "00aadbb8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadbbc`](#insn-00aadbbc)

~~~json
{
  "source": "00aadbbc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadbe0`](#insn-00aadbe0)

~~~json
{
  "source": "00aadbe0",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadbec`](#insn-00aadbec)

~~~json
{
  "source": "00aadbec",
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
- 参照命令 [`00aadbf4`](#insn-00aadbf4)

~~~json
{
  "source": "00aadbf4",
  "target": "Stack[-0xff]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadbf8`](#insn-00aadbf8)

~~~json
{
  "source": "00aadbf8",
  "target": "Stack[-0xf8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadc08`](#insn-00aadc08)

~~~json
{
  "source": "00aadc08",
  "target": "Stack[-0x10f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadc10`](#insn-00aadc10)

~~~json
{
  "source": "00aadc10",
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
- 参照命令 [`00aadc14`](#insn-00aadc14)

~~~json
{
  "source": "00aadc14",
  "target": "Stack[-0xdf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadc1c`](#insn-00aadc1c)

~~~json
{
  "source": "00aadc1c",
  "target": "Stack[-0xd8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadc2c`](#insn-00aadc2c)

~~~json
{
  "source": "00aadc2c",
  "target": "Stack[-0xef]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadc30`](#insn-00aadc30)

~~~json
{
  "source": "00aadc30",
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
- 参照命令 [`00aadc34`](#insn-00aadc34)

~~~json
{
  "source": "00aadc34",
  "target": "Stack[-0xbf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadc3c`](#insn-00aadc3c)

~~~json
{
  "source": "00aadc3c",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadc4c`](#insn-00aadc4c)

~~~json
{
  "source": "00aadc4c",
  "target": "Stack[-0xcf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadc50`](#insn-00aadc50)

~~~json
{
  "source": "00aadc50",
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
- 参照命令 [`00aadc54`](#insn-00aadc54)

~~~json
{
  "source": "00aadc54",
  "target": "Stack[-0x9f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadc5c`](#insn-00aadc5c)

~~~json
{
  "source": "00aadc5c",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadc68`](#insn-00aadc68)

~~~json
{
  "source": "00aadc68",
  "target": "Stack[-0xaf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadc6c`](#insn-00aadc6c)

~~~json
{
  "source": "00aadc6c",
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
- 参照命令 [`00aadc74`](#insn-00aadc74)

~~~json
{
  "source": "00aadc74",
  "target": "Stack[-0x7f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadc7c`](#insn-00aadc7c)

~~~json
{
  "source": "00aadc7c",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadc88`](#insn-00aadc88)

~~~json
{
  "source": "00aadc88",
  "target": "Stack[-0x8f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadc8c`](#insn-00aadc8c)

~~~json
{
  "source": "00aadc8c",
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
- 参照命令 [`00aadc94`](#insn-00aadc94)

~~~json
{
  "source": "00aadc94",
  "target": "Stack[-0x5f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadc9c`](#insn-00aadc9c)

~~~json
{
  "source": "00aadc9c",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadca8`](#insn-00aadca8)

~~~json
{
  "source": "00aadca8",
  "target": "Stack[-0x6f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadcac`](#insn-00aadcac)

~~~json
{
  "source": "00aadcac",
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
- 参照命令 [`00aadcb0`](#insn-00aadcb0)

~~~json
{
  "source": "00aadcb0",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadcb4`](#insn-00aadcb4)

~~~json
{
  "source": "00aadcb4",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadcb8`](#insn-00aadcb8)

~~~json
{
  "source": "00aadcb8",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadcbc`](#insn-00aadcbc)

~~~json
{
  "source": "00aadcbc",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadcc0`](#insn-00aadcc0)

~~~json
{
  "source": "00aadcc0",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadcc4`](#insn-00aadcc4)

~~~json
{
  "source": "00aadcc4",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadcc8`](#insn-00aadcc8)

~~~json
{
  "source": "00aadcc8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadcd0`](#insn-00aadcd0)

~~~json
{
  "source": "00aadcd0",
  "target": "Stack[-0x118]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadcd4`](#insn-00aadcd4)

~~~json
{
  "source": "00aadcd4",
  "target": "Stack[-0xfd]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadcd8`](#insn-00aadcd8)

~~~json
{
  "source": "00aadcd8",
  "target": "Stack[-0xdd]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadcdc`](#insn-00aadcdc)

~~~json
{
  "source": "00aadcdc",
  "target": "Stack[-0xbd]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadce0`](#insn-00aadce0)

~~~json
{
  "source": "00aadce0",
  "target": "Stack[-0x9d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadce4`](#insn-00aadce4)

~~~json
{
  "source": "00aadce4",
  "target": "Stack[-0x7d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadce8`](#insn-00aadce8)

~~~json
{
  "source": "00aadce8",
  "target": "Stack[-0x5d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadcec`](#insn-00aadcec)

~~~json
{
  "source": "00aadcec",
  "target": "Stack[-0x3f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadcf0`](#insn-00aadcf0)

~~~json
{
  "source": "00aadcf0",
  "target": "Stack[-0x4f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadcf4`](#insn-00aadcf4)

~~~json
{
  "source": "00aadcf4",
  "target": "Stack[-0x3d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadcf8`](#insn-00aadcf8)

~~~json
{
  "source": "00aadcf8",
  "target": "0109f9f0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109f9f0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aadcfc`](#insn-00aadcfc)

~~~json
{
  "source": "00aadcfc",
  "target": "0109f9e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109f9e8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aadd00`](#insn-00aadd00)

~~~json
{
  "source": "00aadd00",
  "target": "0109f9e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109f9e0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aadd00`](#insn-00aadd00)

~~~json
{
  "source": "00aadd00",
  "target": "0109f9e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109f9e8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aadd0c`](#insn-00aadd0c)

~~~json
{
  "source": "00aadd0c",
  "target": "0109f9e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109f9e0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aadd10`](#insn-00aadd10)

~~~json
{
  "source": "00aadd10",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aadd14`](#insn-00aadd14)

~~~json
{
  "source": "00aadd14",
  "target": "0109f9e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109f9e8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aadd20`](#insn-00aadd20)

~~~json
{
  "source": "00aadd20",
  "target": "0109f9e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109f9e0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aadd24`](#insn-00aadd24)

~~~json
{
  "source": "00aadd24",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aadd28`](#insn-00aadd28)

~~~json
{
  "source": "00aadd28",
  "target": "0109f9e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109f9e8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aadd34`](#insn-00aadd34)

~~~json
{
  "source": "00aadd34",
  "target": "0109f9e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109f9e0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aadd38`](#insn-00aadd38)

~~~json
{
  "source": "00aadd38",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aadd3c`](#insn-00aadd3c)

~~~json
{
  "source": "00aadd3c",
  "target": "0109f9e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109f9e8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aadd48`](#insn-00aadd48)

~~~json
{
  "source": "00aadd48",
  "target": "0109f9e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109f9e0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aadd4c`](#insn-00aadd4c)

~~~json
{
  "source": "00aadd4c",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aadd50`](#insn-00aadd50)

~~~json
{
  "source": "00aadd50",
  "target": "0109f9e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109f9e8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aadd5c`](#insn-00aadd5c)

~~~json
{
  "source": "00aadd5c",
  "target": "0109f9e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109f9e0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aadd60`](#insn-00aadd60)

~~~json
{
  "source": "00aadd60",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aadd64`](#insn-00aadd64)

~~~json
{
  "source": "00aadd64",
  "target": "0109f9e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109f9e8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aadd70`](#insn-00aadd70)

~~~json
{
  "source": "00aadd70",
  "target": "0109f9e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109f9e0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aadd74`](#insn-00aadd74)

~~~json
{
  "source": "00aadd74",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aadd78`](#insn-00aadd78)

~~~json
{
  "source": "00aadd78",
  "target": "0109f9e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109f9e8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aadd84`](#insn-00aadd84)

~~~json
{
  "source": "00aadd84",
  "target": "0109f9e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109f9e0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aadd88`](#insn-00aadd88)

~~~json
{
  "source": "00aadd88",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aadd8c`](#insn-00aadd8c)

~~~json
{
  "source": "00aadd8c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadd90`](#insn-00aadd90)

~~~json
{
  "source": "00aadd90",
  "target": "00aade0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadd94`](#insn-00aadd94)

~~~json
{
  "source": "00aadd94",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadd98`](#insn-00aadd98)

~~~json
{
  "source": "00aadd98",
  "target": "00aade1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadd9c`](#insn-00aadd9c)

~~~json
{
  "source": "00aadd9c",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadda0`](#insn-00aadda0)

~~~json
{
  "source": "00aadda0",
  "target": "00aade2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadda4`](#insn-00aadda4)

~~~json
{
  "source": "00aadda4",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadda8`](#insn-00aadda8)

~~~json
{
  "source": "00aadda8",
  "target": "00aade3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaddac`](#insn-00aaddac)

~~~json
{
  "source": "00aaddac",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaddb0`](#insn-00aaddb0)

~~~json
{
  "source": "00aaddb0",
  "target": "00aade4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaddb4`](#insn-00aaddb4)

~~~json
{
  "source": "00aaddb4",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaddb8`](#insn-00aaddb8)

~~~json
{
  "source": "00aaddb8",
  "target": "00aade5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaddbc`](#insn-00aaddbc)

~~~json
{
  "source": "00aaddbc",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaddc0`](#insn-00aaddc0)

~~~json
{
  "source": "00aaddc0",
  "target": "00aaddcc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaddc4`](#insn-00aaddc4)

~~~json
{
  "source": "00aaddc4",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaddc8`](#insn-00aaddc8)

~~~json
{
  "source": "00aaddc8",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaddd0`](#insn-00aaddd0)

~~~json
{
  "source": "00aaddd0",
  "target": "00418330",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaddd8`](#insn-00aaddd8)

~~~json
{
  "source": "00aaddd8",
  "target": "0109f9e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109f9e0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aadde0`](#insn-00aadde0)

~~~json
{
  "source": "00aadde0",
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
- 参照命令 [`00aadde4`](#insn-00aadde4)

~~~json
{
  "source": "00aadde4",
  "target": "00bdaee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaddec`](#insn-00aaddec)

~~~json
{
  "source": "00aaddec",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaddf4`](#insn-00aaddf4)

~~~json
{
  "source": "00aaddf4",
  "target": "00aadf3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaddf8`](#insn-00aaddf8)

~~~json
{
  "source": "00aaddf8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaddfc`](#insn-00aaddfc)

~~~json
{
  "source": "00aaddfc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aade00`](#insn-00aade00)

~~~json
{
  "source": "00aade00",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aade0c`](#insn-00aade0c)

~~~json
{
  "source": "00aade0c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aade10`](#insn-00aade10)

~~~json
{
  "source": "00aade10",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aade14`](#insn-00aade14)

~~~json
{
  "source": "00aade14",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aade18`](#insn-00aade18)

~~~json
{
  "source": "00aade18",
  "target": "00aadd9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aade1c`](#insn-00aade1c)

~~~json
{
  "source": "00aade1c",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aade20`](#insn-00aade20)

~~~json
{
  "source": "00aade20",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aade24`](#insn-00aade24)

~~~json
{
  "source": "00aade24",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aade28`](#insn-00aade28)

~~~json
{
  "source": "00aade28",
  "target": "00aadda4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aade2c`](#insn-00aade2c)

~~~json
{
  "source": "00aade2c",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aade30`](#insn-00aade30)

~~~json
{
  "source": "00aade30",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aade34`](#insn-00aade34)

~~~json
{
  "source": "00aade34",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aade38`](#insn-00aade38)

~~~json
{
  "source": "00aade38",
  "target": "00aaddac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aade3c`](#insn-00aade3c)

~~~json
{
  "source": "00aade3c",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aade40`](#insn-00aade40)

~~~json
{
  "source": "00aade40",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aade44`](#insn-00aade44)

~~~json
{
  "source": "00aade44",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aade48`](#insn-00aade48)

~~~json
{
  "source": "00aade48",
  "target": "00aaddb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aade4c`](#insn-00aade4c)

~~~json
{
  "source": "00aade4c",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aade50`](#insn-00aade50)

~~~json
{
  "source": "00aade50",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aade54`](#insn-00aade54)

~~~json
{
  "source": "00aade54",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aade58`](#insn-00aade58)

~~~json
{
  "source": "00aade58",
  "target": "00aaddbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aade5c`](#insn-00aade5c)

~~~json
{
  "source": "00aade5c",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aade60`](#insn-00aade60)

~~~json
{
  "source": "00aade60",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aade64`](#insn-00aade64)

~~~json
{
  "source": "00aade64",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aade68`](#insn-00aade68)

~~~json
{
  "source": "00aade68",
  "target": "00aaddc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aade6c`](#insn-00aade6c)

~~~json
{
  "source": "00aade6c",
  "target": "00aaddcc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadf3c`](#insn-00aadf3c)

~~~json
{
  "source": "00aadf3c",
  "target": "00bdaf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
