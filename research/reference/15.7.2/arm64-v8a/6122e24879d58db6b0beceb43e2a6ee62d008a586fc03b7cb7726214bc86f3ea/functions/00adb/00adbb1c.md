# 00adbb1c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00adbbe4`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adb/00adbbe4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0057.md#compare-910496dd272d8ae56a237c6c7db9d801)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00adbb1c",
  "name": "_INIT_265",
  "size": 876,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6c1a4428eacffd4c576577bc31dd60ede3279789aa0bb170703d89f5b227afc2",
  "source_text_sha256": "6c1a4428eacffd4c576577bc31dd60ede3279789aa0bb170703d89f5b227afc2",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00adbb1c",
        "00adbe83"
      ],
      [
        "00adbf50",
        "00adbf53"
      ]
    ],
    "bytes_sha256": "1b5822660b6cefd7d52ab0b899933040aec5c14b7158d26fad32fbdc2cedc40f",
    "instruction_count": 219,
    "instruction_bytes": 876,
    "body_bytes": 876,
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

## 疑似コード / UTF-8 5573 bytes

~~~c

/* WARNING: Type propagation algorithm not settling */

void _INIT_265(void)

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
  DAT_0109fe30 = 0;
  DAT_0109fe28 = 0;
  DAT_0109fe20 = &DAT_0109fe28;
  FUN_00418cb8(&DAT_0109fe20,&DAT_0109fe28,local_118,local_118);
  FUN_00418cb8(&DAT_0109fe20,&DAT_0109fe28,local_f8,local_f8);
  FUN_00418cb8(&DAT_0109fe20,&DAT_0109fe28,local_d8,local_d8);
  FUN_00418cb8(&DAT_0109fe20,&DAT_0109fe28,local_b8,local_b8);
  FUN_00418cb8(&DAT_0109fe20,&DAT_0109fe28,local_98,local_98);
  FUN_00418cb8(&DAT_0109fe20,&DAT_0109fe28,local_78,local_78);
  FUN_00418cb8(&DAT_0109fe20,&DAT_0109fe28,local_58,local_58);
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
                    /* try { // try from 00adbe70 to 00bdbe7b has its CatchHandler @ 00adbf18 */
    _ZdlPv((void *)CONCAT44(uStack_dc,CONCAT13(uStack_dd,CONCAT21(uStack_df,cStack_e0))));
                    /* try { // try from 00adbe7c to 00bdbf3f has its CatchHandler @ 00adbd20 */
  }
  if ((local_110 & 1) != 0) {
    _ZdlPv((void *)CONCAT44(uStack_fc,CONCAT13(uStack_fd,CONCAT21(uStack_ff,cStack_100))));
  }
  __cxa_atexit(FUN_00418330,&DAT_0109fe20,&PTR_LOOP_00be5ed0);
  DAT_0109fe48 = 0;
  DAT_0109fe40 = 0;
  DAT_0109fe38 = &DAT_0109fe40;
  __cxa_atexit(FUN_00ad8ffc,&DAT_0109fe38,&PTR_LOOP_00be5ed0);
  DAT_0109fe60 = 0;
  DAT_0109fe58 = 0;
  DAT_0109fe50 = &DAT_0109fe58;
  __cxa_atexit(FUN_00ad9004,&DAT_0109fe50,&PTR_LOOP_00be5ed0);
  DAT_0109fe90 = 0;
  __cxa_atexit(FUN_00569da8,&DAT_0109fe70,&PTR_LOOP_00be5ed0);
  DAT_0109fec0 = 0;
  __cxa_atexit(FUN_0085e2f8,&DAT_0109fea0,&PTR_LOOP_00be5ed0);
  DAT_0109fef0 = 0;
  __cxa_atexit(FUN_0085e2f8,&DAT_0109fed0,&PTR_LOOP_00be5ed0);
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
<a id="insn-00adbb1c"></a> `00adbb1c` | `ff 83 04 d1` | sub sp,sp,#0x120 | `FALL_THROUGH`
<a id="insn-00adbb20"></a> `00adbb20` | `fd 7b 0f a9` | stp x29,x30,[sp, #0xf0] | `FALL_THROUGH`
<a id="insn-00adbb24"></a> `00adbb24` | `fc 57 10 a9` | stp x28,x21,[sp, #0x100] | `FALL_THROUGH`
<a id="insn-00adbb28"></a> `00adbb28` | `f4 4f 11 a9` | stp x20,x19,[sp, #0x110] | `FALL_THROUGH`
<a id="insn-00adbb2c"></a> `00adbb2c` | `fd c3 03 91` | add x29,sp,#0xf0 | `FALL_THROUGH`
<a id="insn-00adbb30"></a> `00adbb30` | `55 d0 3b d5` | mrs x21,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00adbb34"></a> `00adbb34` | `2a e8 8c 52` | mov w10,#0x6741 | `FALL_THROUGH`
<a id="insn-00adbb38"></a> `00adbb38` | `f4 23 00 91` | add x20,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00adbb3c"></a> `00adbb3c` | `a9 16 40 f9` | ldr x9,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00adbb40"></a> `00adbb40` | `88 04 80 52` | mov w8,#0x24 | `FALL_THROUGH`
<a id="insn-00adbb44"></a> `00adbb44` | `33 2e 00 90` | adrp x19,0x109f000 | `FALL_THROUGH`
<a id="insn-00adbb48"></a> `00adbb48` | `73 82 38 91` | add x19,x19,#0xe20 | `FALL_THROUGH`
<a id="insn-00adbb4c"></a> `00adbb4c` | `a9 83 1f f8` | stur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00adbb50"></a> `00adbb50` | `69 be ff 90` | adrp x9,0x2a7000 | `FALL_THROUGH`
<a id="insn-00adbb54"></a> `00adbb54` | `29 91 0b 91` | add x9,x9,#0x2e4 | `FALL_THROUGH`
<a id="insn-00adbb58"></a> `00adbb58` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00adbb5c"></a> `00adbb5c` | `29 00 80 52` | mov w9,#0x1 | `FALL_THROUGH`
<a id="insn-00adbb60"></a> `00adbb60` | `ea 13 02 78` | sturh w10,[sp, #0x21] | `FALL_THROUGH`
<a id="insn-00adbb64"></a> `00adbb64` | `e9 2b 00 b9` | str w9,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00adbb68"></a> `00adbb68` | `49 28 88 52` | mov w9,#0x4142 | `FALL_THROUGH`
<a id="insn-00adbb6c"></a> `00adbb6c` | `6a be ff 90` | adrp x10,0x2a7000 | `FALL_THROUGH`
<a id="insn-00adbb70"></a> `00adbb70` | `4a dd 0b 91` | add x10,x10,#0x2f7 | `FALL_THROUGH`
<a id="insn-00adbb74"></a> `00adbb74` | `e0 13 81 3c` | stur q0,[sp, #0x11] | `FALL_THROUGH`
<a id="insn-00adbb78"></a> `00adbb78` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00adbb7c"></a> `00adbb7c` | `40 01 c0 3d` | ldr q0,[x10] | `FALL_THROUGH`
<a id="insn-00adbb80"></a> `00adbb80` | `e9 13 04 78` | sturh w9,[sp, #0x41] | `FALL_THROUGH`
<a id="insn-00adbb84"></a> `00adbb84` | `49 00 80 52` | mov w9,#0x2 | `FALL_THROUGH`
<a id="insn-00adbb88"></a> `00adbb88` | `e9 4b 00 b9` | str w9,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00adbb8c"></a> `00adbb8c` | `49 e8 8c 52` | mov w9,#0x6742 | `FALL_THROUGH`
<a id="insn-00adbb90"></a> `00adbb90` | `6a be ff b0` | adrp x10,0x2a8000 | `FALL_THROUGH`
<a id="insn-00adbb94"></a> `00adbb94` | `4a 69 03 91` | add x10,x10,#0xda | `FALL_THROUGH`
<a id="insn-00adbb98"></a> `00adbb98` | `e0 13 83 3c` | stur q0,[sp, #0x31] | `FALL_THROUGH`
<a id="insn-00adbb9c"></a> `00adbb9c` | `40 01 c0 3d` | ldr q0,[x10] | `FALL_THROUGH`
<a id="insn-00adbba0"></a> `00adbba0` | `e9 13 06 78` | sturh w9,[sp, #0x61] | `FALL_THROUGH`
<a id="insn-00adbba4"></a> `00adbba4` | `69 00 80 52` | mov w9,#0x3 | `FALL_THROUGH`
<a id="insn-00adbba8"></a> `00adbba8` | `e9 6b 00 b9` | str w9,[sp, #0x68] | `FALL_THROUGH`
<a id="insn-00adbbac"></a> `00adbbac` | `29 e8 8e 52` | mov w9,#0x7741 | `FALL_THROUGH`
<a id="insn-00adbbb0"></a> `00adbbb0` | `ca bd ff 90` | adrp x10,0x293000 | `FALL_THROUGH`
<a id="insn-00adbbb4"></a> `00adbbb4` | `4a b9 1a 91` | add x10,x10,#0x6ae | `FALL_THROUGH`
<a id="insn-00adbbb8"></a> `00adbbb8` | `e0 13 85 3c` | stur q0,[sp, #0x51] | `FALL_THROUGH`
<a id="insn-00adbbbc"></a> `00adbbbc` | `40 01 c0 3d` | ldr q0,[x10] | `FALL_THROUGH`
<a id="insn-00adbbc0"></a> `00adbbc0` | `e9 13 08 78` | sturh w9,[sp, #0x81] | `FALL_THROUGH`
<a id="insn-00adbbc4"></a> `00adbbc4` | `89 00 80 52` | mov w9,#0x4 | `FALL_THROUGH`
<a id="insn-00adbbc8"></a> `00adbbc8` | `e9 8b 00 b9` | str w9,[sp, #0x88] | `FALL_THROUGH`
<a id="insn-00adbbcc"></a> `00adbbcc` | `09 be ff b0` | adrp x9,0x29c000 | `FALL_THROUGH`
<a id="insn-00adbbd0"></a> `00adbbd0` | `29 85 0b 91` | add x9,x9,#0x2e1 | `FALL_THROUGH`
<a id="insn-00adbbd4"></a> `00adbbd4` | `e0 13 87 3c` | stur q0,[sp, #0x71] | `FALL_THROUGH`
<a id="insn-00adbbd8"></a> `00adbbd8` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00adbbdc"></a> `00adbbdc` | `49 28 8a 52` | mov w9,#0x5142 | `FALL_THROUGH`
<a id="insn-00adbbe0"></a> `00adbbe0` | `89 92 09 78` | sturh w9,[x20, #0x99] | `FALL_THROUGH`
<a id="insn-00adbbe4"></a> `00adbbe4` | `a9 00 80 52` | mov w9,#0x5 | `FALL_THROUGH`
<a id="insn-00adbbe8"></a> `00adbbe8` | `e9 ab 00 b9` | str w9,[sp, #0xa8] | `FALL_THROUGH`
<a id="insn-00adbbec"></a> `00adbbec` | `a9 bd ff d0` | adrp x9,0x291000 | `FALL_THROUGH`
<a id="insn-00adbbf0"></a> `00adbbf0` | `29 dd 21 91` | add x9,x9,#0x877 | `FALL_THROUGH`
<a id="insn-00adbbf4"></a> `00adbbf4` | `80 92 88 3c` | stur q0,[x20, #0x89] | `FALL_THROUGH`
<a id="insn-00adbbf8"></a> `00adbbf8` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00adbbfc"></a> `00adbbfc` | `49 e8 8e 52` | mov w9,#0x7742 | `FALL_THROUGH`
<a id="insn-00adbc00"></a> `00adbc00` | `89 92 0b 78` | sturh w9,[x20, #0xb9] | `FALL_THROUGH`
<a id="insn-00adbc04"></a> `00adbc04` | `c9 00 80 52` | mov w9,#0x6 | `FALL_THROUGH`
<a id="insn-00adbc08"></a> `00adbc08` | `e9 cb 00 b9` | str w9,[sp, #0xc8] | `FALL_THROUGH`
<a id="insn-00adbc0c"></a> `00adbc0c` | `c9 bd ff b0` | adrp x9,0x294000 | `FALL_THROUGH`
<a id="insn-00adbc10"></a> `00adbc10` | `29 99 14 91` | add x9,x9,#0x526 | `FALL_THROUGH`
<a id="insn-00adbc14"></a> `00adbc14` | `80 92 8a 3c` | stur q0,[x20, #0xa9] | `FALL_THROUGH`
<a id="insn-00adbc18"></a> `00adbc18` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00adbc1c"></a> `00adbc1c` | `e8 43 00 39` | strb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00adbc20"></a> `00adbc20` | `e8 c3 00 39` | strb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00adbc24"></a> `00adbc24` | `e8 43 01 39` | strb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00adbc28"></a> `00adbc28` | `e8 c3 01 39` | strb w8,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00adbc2c"></a> `00adbc2c` | `e8 43 02 39` | strb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00adbc30"></a> `00adbc30` | `e8 c3 02 39` | strb w8,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00adbc34"></a> `00adbc34` | `e8 43 03 39` | strb w8,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-00adbc38"></a> `00adbc38` | `68 28 88 52` | mov w8,#0x4143 | `FALL_THROUGH`
<a id="insn-00adbc3c"></a> `00adbc3c` | `ff 0b 00 b9` | str wzr,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00adbc40"></a> `00adbc40` | `ff 8f 00 39` | strb wzr,[sp, #0x23] | `FALL_THROUGH`
<a id="insn-00adbc44"></a> `00adbc44` | `ff 0f 01 39` | strb wzr,[sp, #0x43] | `FALL_THROUGH`
<a id="insn-00adbc48"></a> `00adbc48` | `ff 8f 01 39` | strb wzr,[sp, #0x63] | `FALL_THROUGH`
<a id="insn-00adbc4c"></a> `00adbc4c` | `ff 0f 02 39` | strb wzr,[sp, #0x83] | `FALL_THROUGH`
<a id="insn-00adbc50"></a> `00adbc50` | `ff 8f 02 39` | strb wzr,[sp, #0xa3] | `FALL_THROUGH`
<a id="insn-00adbc54"></a> `00adbc54` | `ff 0f 03 39` | strb wzr,[sp, #0xc3] | `FALL_THROUGH`
<a id="insn-00adbc58"></a> `00adbc58` | `88 92 0d 78` | sturh w8,[x20, #0xd9] | `FALL_THROUGH`
<a id="insn-00adbc5c"></a> `00adbc5c` | `80 92 8c 3c` | stur q0,[x20, #0xc9] | `FALL_THROUGH`
<a id="insn-00adbc60"></a> `00adbc60` | `ff 8f 03 39` | strb wzr,[sp, #0xe3] | `FALL_THROUGH`
<a id="insn-00adbc64"></a> `00adbc64` | `7f 0a 00 f9` | str xzr,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00adbc68"></a> `00adbc68` | `3f 8c 00 f8` | str xzr,[x1, #0x8]! | `FALL_THROUGH`
<a id="insn-00adbc6c"></a> `00adbc6c` | `61 02 00 f9` | str x1,[x19] | `FALL_THROUGH`
<a id="insn-00adbc70"></a> `00adbc70` | `e2 23 00 91` | add x2,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00adbc74"></a> `00adbc74` | `e3 23 00 91` | add x3,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00adbc78"></a> `00adbc78` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00adbc7c"></a> `00adbc7c` | `0f f4 e4 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-00adbc80"></a> `00adbc80` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00adbc84"></a> `00adbc84` | `82 82 00 91` | add x2,x20,#0x20 | `FALL_THROUGH`
<a id="insn-00adbc88"></a> `00adbc88` | `83 82 00 91` | add x3,x20,#0x20 | `FALL_THROUGH`
<a id="insn-00adbc8c"></a> `00adbc8c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00adbc90"></a> `00adbc90` | `0a f4 e4 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-00adbc94"></a> `00adbc94` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00adbc98"></a> `00adbc98` | `82 02 01 91` | add x2,x20,#0x40 | `FALL_THROUGH`
<a id="insn-00adbc9c"></a> `00adbc9c` | `83 02 01 91` | add x3,x20,#0x40 | `FALL_THROUGH`
<a id="insn-00adbca0"></a> `00adbca0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00adbca4"></a> `00adbca4` | `05 f4 e4 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-00adbca8"></a> `00adbca8` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00adbcac"></a> `00adbcac` | `82 82 01 91` | add x2,x20,#0x60 | `FALL_THROUGH`
<a id="insn-00adbcb0"></a> `00adbcb0` | `83 82 01 91` | add x3,x20,#0x60 | `FALL_THROUGH`
<a id="insn-00adbcb4"></a> `00adbcb4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00adbcb8"></a> `00adbcb8` | `00 f4 e4 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-00adbcbc"></a> `00adbcbc` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00adbcc0"></a> `00adbcc0` | `82 02 02 91` | add x2,x20,#0x80 | `FALL_THROUGH`
<a id="insn-00adbcc4"></a> `00adbcc4` | `83 02 02 91` | add x3,x20,#0x80 | `FALL_THROUGH`
<a id="insn-00adbcc8"></a> `00adbcc8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00adbccc"></a> `00adbccc` | `fb f3 e4 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-00adbcd0"></a> `00adbcd0` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00adbcd4"></a> `00adbcd4` | `82 82 02 91` | add x2,x20,#0xa0 | `FALL_THROUGH`
<a id="insn-00adbcd8"></a> `00adbcd8` | `83 82 02 91` | add x3,x20,#0xa0 | `FALL_THROUGH`
<a id="insn-00adbcdc"></a> `00adbcdc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00adbce0"></a> `00adbce0` | `f6 f3 e4 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-00adbce4"></a> `00adbce4` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00adbce8"></a> `00adbce8` | `82 02 03 91` | add x2,x20,#0xc0 | `FALL_THROUGH`
<a id="insn-00adbcec"></a> `00adbcec` | `83 02 03 91` | add x3,x20,#0xc0 | `FALL_THROUGH`
<a id="insn-00adbcf0"></a> `00adbcf0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00adbcf4"></a> `00adbcf4` | `f1 f3 e4 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-00adbcf8"></a> `00adbcf8` | `e8 43 43 39` | ldrb w8,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-00adbcfc"></a> `00adbcfc` | `28 09 00 37` | tbnz w8,#0x0,0x00adbe20 | `CONDITIONAL_JUMP`
<a id="insn-00adbd00"></a> `00adbd00` | `e8 c3 42 39` | ldrb w8,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00adbd04"></a> `00adbd04` | `68 09 00 37` | tbnz w8,#0x0,0x00adbe30 | `CONDITIONAL_JUMP`
<a id="insn-00adbd08"></a> `00adbd08` | `e8 43 42 39` | ldrb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00adbd0c"></a> `00adbd0c` | `a8 09 00 37` | tbnz w8,#0x0,0x00adbe40 | `CONDITIONAL_JUMP`
<a id="insn-00adbd10"></a> `00adbd10` | `e8 c3 41 39` | ldrb w8,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00adbd14"></a> `00adbd14` | `e8 09 00 37` | tbnz w8,#0x0,0x00adbe50 | `CONDITIONAL_JUMP`
<a id="insn-00adbd18"></a> `00adbd18` | `e8 43 41 39` | ldrb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00adbd1c"></a> `00adbd1c` | `28 0a 00 37` | tbnz w8,#0x0,0x00adbe60 | `CONDITIONAL_JUMP`
<a id="insn-00adbd20"></a> `00adbd20` | `e8 c3 40 39` | ldrb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00adbd24"></a> `00adbd24` | `68 0a 00 37` | tbnz w8,#0x0,0x00adbe70 | `CONDITIONAL_JUMP`
<a id="insn-00adbd28"></a> `00adbd28` | `e8 43 40 39` | ldrb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00adbd2c"></a> `00adbd2c` | `68 00 00 36` | tbz w8,#0x0,0x00adbd38 | `CONDITIONAL_JUMP`
<a id="insn-00adbd30"></a> `00adbd30` | `e0 13 40 f9` | ldr x0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00adbd34"></a> `00adbd34` | `8b fc 03 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00adbd38"></a> `00adbd38` | `53 08 00 d0` | adrp x19,0xbe5000 | `FALL_THROUGH`
<a id="insn-00adbd3c"></a> `00adbd3c` | `73 42 3b 91` | add x19,x19,#0xed0 | `FALL_THROUGH`
<a id="insn-00adbd40"></a> `00adbd40` | `e0 c9 ff b0` | adrp x0,0x418000 | `FALL_THROUGH`
<a id="insn-00adbd44"></a> `00adbd44` | `00 c0 0c 91` | add x0,x0,#0x330 | `FALL_THROUGH`
<a id="insn-00adbd48"></a> `00adbd48` | `21 2e 00 90` | adrp x1,0x109f000 | `FALL_THROUGH`
<a id="insn-00adbd4c"></a> `00adbd4c` | `21 80 38 91` | add x1,x1,#0xe20 | `FALL_THROUGH`
<a id="insn-00adbd50"></a> `00adbd50` | `e2 03 13 aa` | mov x2,x19 | `FALL_THROUGH`
<a id="insn-00adbd54"></a> `00adbd54` | `63 fc 03 94` | bl 0x00bdaee0 | `UNCONDITIONAL_CALL`
<a id="insn-00adbd58"></a> `00adbd58` | `21 2e 00 90` | adrp x1,0x109f000 | `FALL_THROUGH`
<a id="insn-00adbd5c"></a> `00adbd5c` | `21 e0 38 91` | add x1,x1,#0xe38 | `FALL_THROUGH`
<a id="insn-00adbd60"></a> `00adbd60` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00adbd64"></a> `00adbd64` | `c0 94 fe 10` | adr x0,0xad8ffc | `FALL_THROUGH`
<a id="insn-00adbd68"></a> `00adbd68` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00adbd6c"></a> `00adbd6c` | `e2 03 13 aa` | mov x2,x19 | `FALL_THROUGH`
<a id="insn-00adbd70"></a> `00adbd70` | `3f 08 00 f9` | str xzr,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-00adbd74"></a> `00adbd74` | `1f 8d 00 f8` | str xzr,[x8, #0x8]! | `FALL_THROUGH`
<a id="insn-00adbd78"></a> `00adbd78` | `28 00 00 f9` | str x8,[x1] | `FALL_THROUGH`
<a id="insn-00adbd7c"></a> `00adbd7c` | `59 fc 03 94` | bl 0x00bdaee0 | `UNCONDITIONAL_CALL`
<a id="insn-00adbd80"></a> `00adbd80` | `21 2e 00 90` | adrp x1,0x109f000 | `FALL_THROUGH`
<a id="insn-00adbd84"></a> `00adbd84` | `21 40 39 91` | add x1,x1,#0xe50 | `FALL_THROUGH`
<a id="insn-00adbd88"></a> `00adbd88` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00adbd8c"></a> `00adbd8c` | `c0 93 fe 10` | adr x0,0xad9004 | `FALL_THROUGH`
<a id="insn-00adbd90"></a> `00adbd90` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00adbd94"></a> `00adbd94` | `e2 03 13 aa` | mov x2,x19 | `FALL_THROUGH`
<a id="insn-00adbd98"></a> `00adbd98` | `3f 08 00 f9` | str xzr,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-00adbd9c"></a> `00adbd9c` | `1f 8d 00 f8` | str xzr,[x8, #0x8]! | `FALL_THROUGH`
<a id="insn-00adbda0"></a> `00adbda0` | `28 00 00 f9` | str x8,[x1] | `FALL_THROUGH`
<a id="insn-00adbda4"></a> `00adbda4` | `4f fc 03 94` | bl 0x00bdaee0 | `UNCONDITIONAL_CALL`
<a id="insn-00adbda8"></a> `00adbda8` | `21 2e 00 90` | adrp x1,0x109f000 | `FALL_THROUGH`
<a id="insn-00adbdac"></a> `00adbdac` | `21 c0 39 91` | add x1,x1,#0xe70 | `FALL_THROUGH`
<a id="insn-00adbdb0"></a> `00adbdb0` | `60 d4 ff d0` | adrp x0,0x569000 | `FALL_THROUGH`
<a id="insn-00adbdb4"></a> `00adbdb4` | `00 a0 36 91` | add x0,x0,#0xda8 | `FALL_THROUGH`
<a id="insn-00adbdb8"></a> `00adbdb8` | `e2 03 13 aa` | mov x2,x19 | `FALL_THROUGH`
<a id="insn-00adbdbc"></a> `00adbdbc` | `3f 10 00 f9` | str xzr,[x1, #0x20] | `FALL_THROUGH`
<a id="insn-00adbdc0"></a> `00adbdc0` | `48 fc 03 94` | bl 0x00bdaee0 | `UNCONDITIONAL_CALL`
<a id="insn-00adbdc4"></a> `00adbdc4` | `14 ec ff f0` | adrp x20,0x85e000 | `FALL_THROUGH`
<a id="insn-00adbdc8"></a> `00adbdc8` | `94 e2 0b 91` | add x20,x20,#0x2f8 | `FALL_THROUGH`
<a id="insn-00adbdcc"></a> `00adbdcc` | `21 2e 00 90` | adrp x1,0x109f000 | `FALL_THROUGH`
<a id="insn-00adbdd0"></a> `00adbdd0` | `21 80 3a 91` | add x1,x1,#0xea0 | `FALL_THROUGH`
<a id="insn-00adbdd4"></a> `00adbdd4` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00adbdd8"></a> `00adbdd8` | `e2 03 13 aa` | mov x2,x19 | `FALL_THROUGH`
<a id="insn-00adbddc"></a> `00adbddc` | `3f 10 00 f9` | str xzr,[x1, #0x20] | `FALL_THROUGH`
<a id="insn-00adbde0"></a> `00adbde0` | `40 fc 03 94` | bl 0x00bdaee0 | `UNCONDITIONAL_CALL`
<a id="insn-00adbde4"></a> `00adbde4` | `21 2e 00 90` | adrp x1,0x109f000 | `FALL_THROUGH`
<a id="insn-00adbde8"></a> `00adbde8` | `21 40 3b 91` | add x1,x1,#0xed0 | `FALL_THROUGH`
<a id="insn-00adbdec"></a> `00adbdec` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00adbdf0"></a> `00adbdf0` | `e2 03 13 aa` | mov x2,x19 | `FALL_THROUGH`
<a id="insn-00adbdf4"></a> `00adbdf4` | `3f 10 00 f9` | str xzr,[x1, #0x20] | `FALL_THROUGH`
<a id="insn-00adbdf8"></a> `00adbdf8` | `3a fc 03 94` | bl 0x00bdaee0 | `UNCONDITIONAL_CALL`
<a id="insn-00adbdfc"></a> `00adbdfc` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00adbe00"></a> `00adbe00` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00adbe04"></a> `00adbe04` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00adbe08"></a> `00adbe08` | `41 0a 00 54` | b.ne 0x00adbf50 | `CONDITIONAL_JUMP`
<a id="insn-00adbe0c"></a> `00adbe0c` | `f4 4f 51 a9` | ldp x20,x19,[sp, #0x110] | `FALL_THROUGH`
<a id="insn-00adbe10"></a> `00adbe10` | `fc 57 50 a9` | ldp x28,x21,[sp, #0x100] | `FALL_THROUGH`
<a id="insn-00adbe14"></a> `00adbe14` | `fd 7b 4f a9` | ldp x29,x30,[sp, #0xf0] | `FALL_THROUGH`
<a id="insn-00adbe18"></a> `00adbe18` | `ff 83 04 91` | add sp,sp,#0x120 | `FALL_THROUGH`
<a id="insn-00adbe1c"></a> `00adbe1c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00adbe20"></a> `00adbe20` | `e0 73 40 f9` | ldr x0,[sp, #0xe0] | `FALL_THROUGH`
<a id="insn-00adbe24"></a> `00adbe24` | `4f fc 03 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00adbe28"></a> `00adbe28` | `e8 c3 42 39` | ldrb w8,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00adbe2c"></a> `00adbe2c` | `e8 f6 07 36` | tbz w8,#0x0,0x00adbd08 | `CONDITIONAL_JUMP`
<a id="insn-00adbe30"></a> `00adbe30` | `e0 63 40 f9` | ldr x0,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00adbe34"></a> `00adbe34` | `4b fc 03 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00adbe38"></a> `00adbe38` | `e8 43 42 39` | ldrb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00adbe3c"></a> `00adbe3c` | `a8 f6 07 36` | tbz w8,#0x0,0x00adbd10 | `CONDITIONAL_JUMP`
<a id="insn-00adbe40"></a> `00adbe40` | `e0 53 40 f9` | ldr x0,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00adbe44"></a> `00adbe44` | `47 fc 03 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00adbe48"></a> `00adbe48` | `e8 c3 41 39` | ldrb w8,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00adbe4c"></a> `00adbe4c` | `68 f6 07 36` | tbz w8,#0x0,0x00adbd18 | `CONDITIONAL_JUMP`
<a id="insn-00adbe50"></a> `00adbe50` | `e0 43 40 f9` | ldr x0,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00adbe54"></a> `00adbe54` | `43 fc 03 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00adbe58"></a> `00adbe58` | `e8 43 41 39` | ldrb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00adbe5c"></a> `00adbe5c` | `28 f6 07 36` | tbz w8,#0x0,0x00adbd20 | `CONDITIONAL_JUMP`
<a id="insn-00adbe60"></a> `00adbe60` | `e0 33 40 f9` | ldr x0,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00adbe64"></a> `00adbe64` | `3f fc 03 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00adbe68"></a> `00adbe68` | `e8 c3 40 39` | ldrb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00adbe6c"></a> `00adbe6c` | `e8 f5 07 36` | tbz w8,#0x0,0x00adbd28 | `CONDITIONAL_JUMP`
<a id="insn-00adbe70"></a> `00adbe70` | `e0 23 40 f9` | ldr x0,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00adbe74"></a> `00adbe74` | `3b fc 03 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00adbe78"></a> `00adbe78` | `e8 43 40 39` | ldrb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00adbe7c"></a> `00adbe7c` | `a8 f5 07 37` | tbnz w8,#0x0,0x00adbd30 | `CONDITIONAL_JUMP`
<a id="insn-00adbe80"></a> `00adbe80` | `ae ff ff 17` | b 0x00adbd38 | `UNCONDITIONAL_JUMP`
<a id="insn-00adbf50"></a> `00adbf50` | `10 fc 03 94` | bl 0x00bdaf90 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00adbb1c`](#insn-00adbb1c) 範囲 `[['00adbb1c', '00adbcff']]`
  - `CONDITIONAL_JUMP` [`00adbcfc`](#insn-00adbcfc) → [`00adbe20`](#insn-00adbe20)
  - `FALL_THROUGH` [`00adbcfc`](#insn-00adbcfc) → [`00adbd00`](#insn-00adbd00)
- ブロック [`00adbd00`](#insn-00adbd00) 範囲 `[['00adbd00', '00adbd07']]`
  - `CONDITIONAL_JUMP` [`00adbd04`](#insn-00adbd04) → [`00adbe30`](#insn-00adbe30)
  - `FALL_THROUGH` [`00adbd04`](#insn-00adbd04) → [`00adbd08`](#insn-00adbd08)
- ブロック [`00adbd08`](#insn-00adbd08) 範囲 `[['00adbd08', '00adbd0f']]`
  - `CONDITIONAL_JUMP` [`00adbd0c`](#insn-00adbd0c) → [`00adbe40`](#insn-00adbe40)
  - `FALL_THROUGH` [`00adbd0c`](#insn-00adbd0c) → [`00adbd10`](#insn-00adbd10)
- ブロック [`00adbd10`](#insn-00adbd10) 範囲 `[['00adbd10', '00adbd17']]`
  - `CONDITIONAL_JUMP` [`00adbd14`](#insn-00adbd14) → [`00adbe50`](#insn-00adbe50)
  - `FALL_THROUGH` [`00adbd14`](#insn-00adbd14) → [`00adbd18`](#insn-00adbd18)
- ブロック [`00adbd18`](#insn-00adbd18) 範囲 `[['00adbd18', '00adbd1f']]`
  - `CONDITIONAL_JUMP` [`00adbd1c`](#insn-00adbd1c) → [`00adbe60`](#insn-00adbe60)
  - `FALL_THROUGH` [`00adbd1c`](#insn-00adbd1c) → [`00adbd20`](#insn-00adbd20)
- ブロック [`00adbd20`](#insn-00adbd20) 範囲 `[['00adbd20', '00adbd27']]`
  - `CONDITIONAL_JUMP` [`00adbd24`](#insn-00adbd24) → [`00adbe70`](#insn-00adbe70)
  - `FALL_THROUGH` [`00adbd24`](#insn-00adbd24) → [`00adbd28`](#insn-00adbd28)
- ブロック [`00adbd28`](#insn-00adbd28) 範囲 `[['00adbd28', '00adbd2f']]`
  - `CONDITIONAL_JUMP` [`00adbd2c`](#insn-00adbd2c) → [`00adbd38`](#insn-00adbd38)
  - `FALL_THROUGH` [`00adbd2c`](#insn-00adbd2c) → [`00adbd30`](#insn-00adbd30)
- ブロック [`00adbd30`](#insn-00adbd30) 範囲 `[['00adbd30', '00adbd37']]`
  - `FALL_THROUGH` [`00adbd34`](#insn-00adbd34) → [`00adbd38`](#insn-00adbd38)
- ブロック [`00adbd38`](#insn-00adbd38) 範囲 `[['00adbd38', '00adbe0b']]`
  - `CONDITIONAL_JUMP` [`00adbe08`](#insn-00adbe08) → [`00adbf50`](#insn-00adbf50)
  - `FALL_THROUGH` [`00adbe08`](#insn-00adbe08) → [`00adbe0c`](#insn-00adbe0c)
- ブロック [`00adbe0c`](#insn-00adbe0c) 範囲 `[['00adbe0c', '00adbe1f']]`
- ブロック [`00adbe20`](#insn-00adbe20) 範囲 `[['00adbe20', '00adbe2f']]`
  - `CONDITIONAL_JUMP` [`00adbe2c`](#insn-00adbe2c) → [`00adbd08`](#insn-00adbd08)
  - `FALL_THROUGH` [`00adbe2c`](#insn-00adbe2c) → [`00adbe30`](#insn-00adbe30)
- ブロック [`00adbe30`](#insn-00adbe30) 範囲 `[['00adbe30', '00adbe3f']]`
  - `CONDITIONAL_JUMP` [`00adbe3c`](#insn-00adbe3c) → [`00adbd10`](#insn-00adbd10)
  - `FALL_THROUGH` [`00adbe3c`](#insn-00adbe3c) → [`00adbe40`](#insn-00adbe40)
- ブロック [`00adbe40`](#insn-00adbe40) 範囲 `[['00adbe40', '00adbe4f']]`
  - `CONDITIONAL_JUMP` [`00adbe4c`](#insn-00adbe4c) → [`00adbd18`](#insn-00adbd18)
  - `FALL_THROUGH` [`00adbe4c`](#insn-00adbe4c) → [`00adbe50`](#insn-00adbe50)
- ブロック [`00adbe50`](#insn-00adbe50) 範囲 `[['00adbe50', '00adbe5f']]`
  - `CONDITIONAL_JUMP` [`00adbe5c`](#insn-00adbe5c) → [`00adbd20`](#insn-00adbd20)
  - `FALL_THROUGH` [`00adbe5c`](#insn-00adbe5c) → [`00adbe60`](#insn-00adbe60)
- ブロック [`00adbe60`](#insn-00adbe60) 範囲 `[['00adbe60', '00adbe6f']]`
  - `CONDITIONAL_JUMP` [`00adbe6c`](#insn-00adbe6c) → [`00adbd28`](#insn-00adbd28)
  - `FALL_THROUGH` [`00adbe6c`](#insn-00adbe6c) → [`00adbe70`](#insn-00adbe70)
- ブロック [`00adbe70`](#insn-00adbe70) 範囲 `[['00adbe70', '00adbe7b']]`
  - `FALL_THROUGH` [`00adbe78`](#insn-00adbe78) → [`00adbe7c`](#insn-00adbe7c)
- ブロック [`00adbe7c`](#insn-00adbe7c) 範囲 `[['00adbe7c', '00adbe7f']]`
  - `CONDITIONAL_JUMP` [`00adbe7c`](#insn-00adbe7c) → [`00adbd30`](#insn-00adbd30)
  - `FALL_THROUGH` [`00adbe7c`](#insn-00adbe7c) → [`00adbe80`](#insn-00adbe80)
- ブロック [`00adbe80`](#insn-00adbe80) 範囲 `[['00adbe80', '00adbe83']]`
  - `UNCONDITIONAL_JUMP` [`00adbe80`](#insn-00adbe80) → [`00adbd38`](#insn-00adbd38)
- ブロック [`00adbf50`](#insn-00adbf50) 範囲 `[['00adbf50', '00adbf53']]`

## 命令位置別の参照

- [`00adbb20`](#insn-00adbb20) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbb24`](#insn-00adbb24) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbb28`](#insn-00adbb28) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbb4c`](#insn-00adbb4c) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbb58`](#insn-00adbb58) → `002a72e4`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00adbb60`](#insn-00adbb60) → `Stack[-0xff]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbb64`](#insn-00adbb64) → `Stack[-0xf8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbb74`](#insn-00adbb74) → `Stack[-0x10f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbb7c`](#insn-00adbb7c) → `002a72f7`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00adbb80`](#insn-00adbb80) → `Stack[-0xdf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbb88`](#insn-00adbb88) → `Stack[-0xd8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbb98`](#insn-00adbb98) → `Stack[-0xef]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbb9c`](#insn-00adbb9c) → `002a80da`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00adbba0`](#insn-00adbba0) → `Stack[-0xbf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbba8`](#insn-00adbba8) → `Stack[-0xb8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbbb8`](#insn-00adbbb8) → `Stack[-0xcf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbbbc`](#insn-00adbbbc) → `002936ae`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00adbbc0`](#insn-00adbbc0) → `Stack[-0x9f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbbc8`](#insn-00adbbc8) → `Stack[-0x98]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbbd4`](#insn-00adbbd4) → `Stack[-0xaf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbbd8`](#insn-00adbbd8) → `0029c2e1`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00adbbe0`](#insn-00adbbe0) → `Stack[-0x7f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbbe8`](#insn-00adbbe8) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbbf4`](#insn-00adbbf4) → `Stack[-0x8f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbbf8`](#insn-00adbbf8) → `00291877`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00adbc00`](#insn-00adbc00) → `Stack[-0x5f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbc08`](#insn-00adbc08) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbc14`](#insn-00adbc14) → `Stack[-0x6f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbc18`](#insn-00adbc18) → `00294526`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00adbc1c`](#insn-00adbc1c) → `Stack[-0x110]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbc20`](#insn-00adbc20) → `Stack[-0xf0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbc24`](#insn-00adbc24) → `Stack[-0xd0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbc28`](#insn-00adbc28) → `Stack[-0xb0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbc2c`](#insn-00adbc2c) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbc30`](#insn-00adbc30) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbc34`](#insn-00adbc34) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbc3c`](#insn-00adbc3c) → `Stack[-0x118]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbc40`](#insn-00adbc40) → `Stack[-0xfd]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbc44`](#insn-00adbc44) → `Stack[-0xdd]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbc48`](#insn-00adbc48) → `Stack[-0xbd]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbc4c`](#insn-00adbc4c) → `Stack[-0x9d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbc50`](#insn-00adbc50) → `Stack[-0x7d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbc54`](#insn-00adbc54) → `Stack[-0x5d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbc58`](#insn-00adbc58) → `Stack[-0x3f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbc5c`](#insn-00adbc5c) → `Stack[-0x4f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbc60`](#insn-00adbc60) → `Stack[-0x3d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbc64`](#insn-00adbc64) → `0109fe30`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adbc68`](#insn-00adbc68) → `0109fe28`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adbc6c`](#insn-00adbc6c) → `0109fe20`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adbc6c`](#insn-00adbc6c) → `0109fe28`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adbc78`](#insn-00adbc78) → `0109fe20`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adbc7c`](#insn-00adbc7c) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`00adbc80`](#insn-00adbc80) → `0109fe28`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adbc8c`](#insn-00adbc8c) → `0109fe20`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adbc90`](#insn-00adbc90) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`00adbc94`](#insn-00adbc94) → `0109fe28`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adbca0`](#insn-00adbca0) → `0109fe20`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adbca4`](#insn-00adbca4) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`00adbca8`](#insn-00adbca8) → `0109fe28`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adbcb4`](#insn-00adbcb4) → `0109fe20`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adbcb8`](#insn-00adbcb8) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`00adbcbc`](#insn-00adbcbc) → `0109fe28`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adbcc8`](#insn-00adbcc8) → `0109fe20`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adbccc`](#insn-00adbccc) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`00adbcd0`](#insn-00adbcd0) → `0109fe28`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adbcdc`](#insn-00adbcdc) → `0109fe20`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adbce0`](#insn-00adbce0) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`00adbce4`](#insn-00adbce4) → `0109fe28`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adbcf0`](#insn-00adbcf0) → `0109fe20`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adbcf4`](#insn-00adbcf4) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`00adbcf8`](#insn-00adbcf8) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbcfc`](#insn-00adbcfc) → [`00adbe20`](#insn-00adbe20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbd00`](#insn-00adbd00) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbd04`](#insn-00adbd04) → [`00adbe30`](#insn-00adbe30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbd08`](#insn-00adbd08) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbd0c`](#insn-00adbd0c) → [`00adbe40`](#insn-00adbe40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbd10`](#insn-00adbd10) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbd14`](#insn-00adbd14) → [`00adbe50`](#insn-00adbe50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbd18`](#insn-00adbd18) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbd1c`](#insn-00adbd1c) → [`00adbe60`](#insn-00adbe60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbd20`](#insn-00adbd20) → `Stack[-0xf0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbd24`](#insn-00adbd24) → [`00adbe70`](#insn-00adbe70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbd28`](#insn-00adbd28) → `Stack[-0x110]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbd2c`](#insn-00adbd2c) → [`00adbd38`](#insn-00adbd38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbd30`](#insn-00adbd30) → `Stack[-0x100]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbd34`](#insn-00adbd34) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00adbd44`](#insn-00adbd44) → [`00418330`](../00418/00418330.md) · `PARAM` · `ANALYSIS` · 関数 `00418330` · 推定シンボル `None` · 推定型 `None`
- [`00adbd4c`](#insn-00adbd4c) → `0109fe20`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adbd50`](#insn-00adbd50) → `00be5ed0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00adbd54`](#insn-00adbd54) → [`00bdaee0`](../00bda/00bdaee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaee0` · 推定シンボル `None` · 推定型 `None`
- [`00adbd5c`](#insn-00adbd5c) → `0109fe38`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adbd64`](#insn-00adbd64) → [`00ad8ffc`](../00ad8/00ad8ffc.md) · `PARAM` · `ANALYSIS` · 関数 `00ad8ffc` · 推定シンボル `None` · 推定型 `None`
- [`00adbd6c`](#insn-00adbd6c) → `00be5ed0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00adbd70`](#insn-00adbd70) → `0109fe48`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adbd74`](#insn-00adbd74) → `0109fe40`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adbd78`](#insn-00adbd78) → `0109fe38`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adbd78`](#insn-00adbd78) → `0109fe40`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adbd7c`](#insn-00adbd7c) → [`00bdaee0`](../00bda/00bdaee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaee0` · 推定シンボル `None` · 推定型 `None`
- [`00adbd84`](#insn-00adbd84) → `0109fe50`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adbd8c`](#insn-00adbd8c) → [`00ad9004`](../00ad9/00ad9004.md) · `PARAM` · `ANALYSIS` · 関数 `00ad9004` · 推定シンボル `None` · 推定型 `None`
- [`00adbd94`](#insn-00adbd94) → `00be5ed0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00adbd98`](#insn-00adbd98) → `0109fe60`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adbd9c`](#insn-00adbd9c) → `0109fe58`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adbda0`](#insn-00adbda0) → `0109fe50`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adbda0`](#insn-00adbda0) → `0109fe58`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adbda4`](#insn-00adbda4) → [`00bdaee0`](../00bda/00bdaee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaee0` · 推定シンボル `None` · 推定型 `None`
- [`00adbdac`](#insn-00adbdac) → `0109fe70`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbdb4`](#insn-00adbdb4) → [`00569da8`](../00569/00569da8.md) · `PARAM` · `ANALYSIS` · 関数 `00569da8` · 推定シンボル `None` · 推定型 `None`
- [`00adbdb8`](#insn-00adbdb8) → `00be5ed0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00adbdbc`](#insn-00adbdbc) → `0109fe90`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adbdc0`](#insn-00adbdc0) → [`00bdaee0`](../00bda/00bdaee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaee0` · 推定シンボル `None` · 推定型 `None`
- [`00adbdd0`](#insn-00adbdd0) → `0109fea0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbdd4`](#insn-00adbdd4) → [`0085e2f8`](../0085e/0085e2f8.md) · `PARAM` · `ANALYSIS` · 関数 `0085e2f8` · 推定シンボル `None` · 推定型 `None`
- [`00adbdd8`](#insn-00adbdd8) → `00be5ed0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00adbddc`](#insn-00adbddc) → `0109fec0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adbde0`](#insn-00adbde0) → [`00bdaee0`](../00bda/00bdaee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaee0` · 推定シンボル `None` · 推定型 `None`
- [`00adbde8`](#insn-00adbde8) → `0109fed0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbdec`](#insn-00adbdec) → [`0085e2f8`](../0085e/0085e2f8.md) · `PARAM` · `ANALYSIS` · 関数 `0085e2f8` · 推定シンボル `None` · 推定型 `None`
- [`00adbdf0`](#insn-00adbdf0) → `00be5ed0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00adbdf4`](#insn-00adbdf4) → `0109fef0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adbdf8`](#insn-00adbdf8) → [`00bdaee0`](../00bda/00bdaee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaee0` · 推定シンボル `None` · 推定型 `None`
- [`00adbe00`](#insn-00adbe00) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbe08`](#insn-00adbe08) → [`00adbf50`](#insn-00adbf50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbe0c`](#insn-00adbe0c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbe10`](#insn-00adbe10) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbe14`](#insn-00adbe14) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbe20`](#insn-00adbe20) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbe24`](#insn-00adbe24) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00adbe28`](#insn-00adbe28) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbe2c`](#insn-00adbe2c) → [`00adbd08`](#insn-00adbd08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbe30`](#insn-00adbe30) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbe34`](#insn-00adbe34) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00adbe38`](#insn-00adbe38) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbe3c`](#insn-00adbe3c) → [`00adbd10`](#insn-00adbd10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbe40`](#insn-00adbe40) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbe44`](#insn-00adbe44) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00adbe48`](#insn-00adbe48) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbe4c`](#insn-00adbe4c) → [`00adbd18`](#insn-00adbd18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbe50`](#insn-00adbe50) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbe54`](#insn-00adbe54) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00adbe58`](#insn-00adbe58) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbe5c`](#insn-00adbe5c) → [`00adbd20`](#insn-00adbd20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbe60`](#insn-00adbe60) → `Stack[-0xc0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbe64`](#insn-00adbe64) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00adbe68`](#insn-00adbe68) → `Stack[-0xf0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbe6c`](#insn-00adbe6c) → [`00adbd28`](#insn-00adbd28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbe70`](#insn-00adbe70) → `Stack[-0xe0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbe74`](#insn-00adbe74) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00adbe78`](#insn-00adbe78) → `Stack[-0x110]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbe7c`](#insn-00adbe7c) → [`00adbd30`](#insn-00adbd30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbe80`](#insn-00adbe80) → [`00adbd38`](#insn-00adbd38) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbf50`](#insn-00adbf50) → [`00bdaf90`](../00bda/00bdaf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf90` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00adbb20`](#insn-00adbb20)

~~~json
{
  "source": "00adbb20",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbb24`](#insn-00adbb24)

~~~json
{
  "source": "00adbb24",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbb28`](#insn-00adbb28)

~~~json
{
  "source": "00adbb28",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbb4c`](#insn-00adbb4c)

~~~json
{
  "source": "00adbb4c",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbb58`](#insn-00adbb58)

~~~json
{
  "source": "00adbb58",
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
- 参照命令 [`00adbb60`](#insn-00adbb60)

~~~json
{
  "source": "00adbb60",
  "target": "Stack[-0xff]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbb64`](#insn-00adbb64)

~~~json
{
  "source": "00adbb64",
  "target": "Stack[-0xf8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbb74`](#insn-00adbb74)

~~~json
{
  "source": "00adbb74",
  "target": "Stack[-0x10f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbb7c`](#insn-00adbb7c)

~~~json
{
  "source": "00adbb7c",
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
- 参照命令 [`00adbb80`](#insn-00adbb80)

~~~json
{
  "source": "00adbb80",
  "target": "Stack[-0xdf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbb88`](#insn-00adbb88)

~~~json
{
  "source": "00adbb88",
  "target": "Stack[-0xd8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbb98`](#insn-00adbb98)

~~~json
{
  "source": "00adbb98",
  "target": "Stack[-0xef]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbb9c`](#insn-00adbb9c)

~~~json
{
  "source": "00adbb9c",
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
- 参照命令 [`00adbba0`](#insn-00adbba0)

~~~json
{
  "source": "00adbba0",
  "target": "Stack[-0xbf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbba8`](#insn-00adbba8)

~~~json
{
  "source": "00adbba8",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbbb8`](#insn-00adbbb8)

~~~json
{
  "source": "00adbbb8",
  "target": "Stack[-0xcf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbbbc`](#insn-00adbbbc)

~~~json
{
  "source": "00adbbbc",
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
- 参照命令 [`00adbbc0`](#insn-00adbbc0)

~~~json
{
  "source": "00adbbc0",
  "target": "Stack[-0x9f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbbc8`](#insn-00adbbc8)

~~~json
{
  "source": "00adbbc8",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbbd4`](#insn-00adbbd4)

~~~json
{
  "source": "00adbbd4",
  "target": "Stack[-0xaf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbbd8`](#insn-00adbbd8)

~~~json
{
  "source": "00adbbd8",
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
- 参照命令 [`00adbbe0`](#insn-00adbbe0)

~~~json
{
  "source": "00adbbe0",
  "target": "Stack[-0x7f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbbe8`](#insn-00adbbe8)

~~~json
{
  "source": "00adbbe8",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbbf4`](#insn-00adbbf4)

~~~json
{
  "source": "00adbbf4",
  "target": "Stack[-0x8f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbbf8`](#insn-00adbbf8)

~~~json
{
  "source": "00adbbf8",
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
- 参照命令 [`00adbc00`](#insn-00adbc00)

~~~json
{
  "source": "00adbc00",
  "target": "Stack[-0x5f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbc08`](#insn-00adbc08)

~~~json
{
  "source": "00adbc08",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbc14`](#insn-00adbc14)

~~~json
{
  "source": "00adbc14",
  "target": "Stack[-0x6f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbc18`](#insn-00adbc18)

~~~json
{
  "source": "00adbc18",
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
- 参照命令 [`00adbc1c`](#insn-00adbc1c)

~~~json
{
  "source": "00adbc1c",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbc20`](#insn-00adbc20)

~~~json
{
  "source": "00adbc20",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbc24`](#insn-00adbc24)

~~~json
{
  "source": "00adbc24",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbc28`](#insn-00adbc28)

~~~json
{
  "source": "00adbc28",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbc2c`](#insn-00adbc2c)

~~~json
{
  "source": "00adbc2c",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbc30`](#insn-00adbc30)

~~~json
{
  "source": "00adbc30",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbc34`](#insn-00adbc34)

~~~json
{
  "source": "00adbc34",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbc3c`](#insn-00adbc3c)

~~~json
{
  "source": "00adbc3c",
  "target": "Stack[-0x118]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbc40`](#insn-00adbc40)

~~~json
{
  "source": "00adbc40",
  "target": "Stack[-0xfd]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbc44`](#insn-00adbc44)

~~~json
{
  "source": "00adbc44",
  "target": "Stack[-0xdd]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbc48`](#insn-00adbc48)

~~~json
{
  "source": "00adbc48",
  "target": "Stack[-0xbd]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbc4c`](#insn-00adbc4c)

~~~json
{
  "source": "00adbc4c",
  "target": "Stack[-0x9d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbc50`](#insn-00adbc50)

~~~json
{
  "source": "00adbc50",
  "target": "Stack[-0x7d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbc54`](#insn-00adbc54)

~~~json
{
  "source": "00adbc54",
  "target": "Stack[-0x5d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbc58`](#insn-00adbc58)

~~~json
{
  "source": "00adbc58",
  "target": "Stack[-0x3f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbc5c`](#insn-00adbc5c)

~~~json
{
  "source": "00adbc5c",
  "target": "Stack[-0x4f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbc60`](#insn-00adbc60)

~~~json
{
  "source": "00adbc60",
  "target": "Stack[-0x3d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbc64`](#insn-00adbc64)

~~~json
{
  "source": "00adbc64",
  "target": "0109fe30",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fe30",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adbc68`](#insn-00adbc68)

~~~json
{
  "source": "00adbc68",
  "target": "0109fe28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fe28",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adbc6c`](#insn-00adbc6c)

~~~json
{
  "source": "00adbc6c",
  "target": "0109fe20",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fe20",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adbc6c`](#insn-00adbc6c)

~~~json
{
  "source": "00adbc6c",
  "target": "0109fe28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fe28",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adbc78`](#insn-00adbc78)

~~~json
{
  "source": "00adbc78",
  "target": "0109fe20",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fe20",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adbc7c`](#insn-00adbc7c)

~~~json
{
  "source": "00adbc7c",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adbc80`](#insn-00adbc80)

~~~json
{
  "source": "00adbc80",
  "target": "0109fe28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fe28",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adbc8c`](#insn-00adbc8c)

~~~json
{
  "source": "00adbc8c",
  "target": "0109fe20",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fe20",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adbc90`](#insn-00adbc90)

~~~json
{
  "source": "00adbc90",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adbc94`](#insn-00adbc94)

~~~json
{
  "source": "00adbc94",
  "target": "0109fe28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fe28",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adbca0`](#insn-00adbca0)

~~~json
{
  "source": "00adbca0",
  "target": "0109fe20",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fe20",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adbca4`](#insn-00adbca4)

~~~json
{
  "source": "00adbca4",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adbca8`](#insn-00adbca8)

~~~json
{
  "source": "00adbca8",
  "target": "0109fe28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fe28",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adbcb4`](#insn-00adbcb4)

~~~json
{
  "source": "00adbcb4",
  "target": "0109fe20",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fe20",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adbcb8`](#insn-00adbcb8)

~~~json
{
  "source": "00adbcb8",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adbcbc`](#insn-00adbcbc)

~~~json
{
  "source": "00adbcbc",
  "target": "0109fe28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fe28",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adbcc8`](#insn-00adbcc8)

~~~json
{
  "source": "00adbcc8",
  "target": "0109fe20",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fe20",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adbccc`](#insn-00adbccc)

~~~json
{
  "source": "00adbccc",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adbcd0`](#insn-00adbcd0)

~~~json
{
  "source": "00adbcd0",
  "target": "0109fe28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fe28",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adbcdc`](#insn-00adbcdc)

~~~json
{
  "source": "00adbcdc",
  "target": "0109fe20",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fe20",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adbce0`](#insn-00adbce0)

~~~json
{
  "source": "00adbce0",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adbce4`](#insn-00adbce4)

~~~json
{
  "source": "00adbce4",
  "target": "0109fe28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fe28",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adbcf0`](#insn-00adbcf0)

~~~json
{
  "source": "00adbcf0",
  "target": "0109fe20",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fe20",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adbcf4`](#insn-00adbcf4)

~~~json
{
  "source": "00adbcf4",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adbcf8`](#insn-00adbcf8)

~~~json
{
  "source": "00adbcf8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbcfc`](#insn-00adbcfc)

~~~json
{
  "source": "00adbcfc",
  "target": "00adbe20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbd00`](#insn-00adbd00)

~~~json
{
  "source": "00adbd00",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbd04`](#insn-00adbd04)

~~~json
{
  "source": "00adbd04",
  "target": "00adbe30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbd08`](#insn-00adbd08)

~~~json
{
  "source": "00adbd08",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbd0c`](#insn-00adbd0c)

~~~json
{
  "source": "00adbd0c",
  "target": "00adbe40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbd10`](#insn-00adbd10)

~~~json
{
  "source": "00adbd10",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbd14`](#insn-00adbd14)

~~~json
{
  "source": "00adbd14",
  "target": "00adbe50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbd18`](#insn-00adbd18)

~~~json
{
  "source": "00adbd18",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbd1c`](#insn-00adbd1c)

~~~json
{
  "source": "00adbd1c",
  "target": "00adbe60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbd20`](#insn-00adbd20)

~~~json
{
  "source": "00adbd20",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbd24`](#insn-00adbd24)

~~~json
{
  "source": "00adbd24",
  "target": "00adbe70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbd28`](#insn-00adbd28)

~~~json
{
  "source": "00adbd28",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbd2c`](#insn-00adbd2c)

~~~json
{
  "source": "00adbd2c",
  "target": "00adbd38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbd30`](#insn-00adbd30)

~~~json
{
  "source": "00adbd30",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbd34`](#insn-00adbd34)

~~~json
{
  "source": "00adbd34",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adbd44`](#insn-00adbd44)

~~~json
{
  "source": "00adbd44",
  "target": "00418330",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adbd4c`](#insn-00adbd4c)

~~~json
{
  "source": "00adbd4c",
  "target": "0109fe20",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fe20",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adbd50`](#insn-00adbd50)

~~~json
{
  "source": "00adbd50",
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
- 参照命令 [`00adbd54`](#insn-00adbd54)

~~~json
{
  "source": "00adbd54",
  "target": "00bdaee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adbd5c`](#insn-00adbd5c)

~~~json
{
  "source": "00adbd5c",
  "target": "0109fe38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fe38",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adbd64`](#insn-00adbd64)

~~~json
{
  "source": "00adbd64",
  "target": "00ad8ffc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adbd6c`](#insn-00adbd6c)

~~~json
{
  "source": "00adbd6c",
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
- 参照命令 [`00adbd70`](#insn-00adbd70)

~~~json
{
  "source": "00adbd70",
  "target": "0109fe48",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fe48",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adbd74`](#insn-00adbd74)

~~~json
{
  "source": "00adbd74",
  "target": "0109fe40",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fe40",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adbd78`](#insn-00adbd78)

~~~json
{
  "source": "00adbd78",
  "target": "0109fe38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fe38",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adbd78`](#insn-00adbd78)

~~~json
{
  "source": "00adbd78",
  "target": "0109fe40",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fe40",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adbd7c`](#insn-00adbd7c)

~~~json
{
  "source": "00adbd7c",
  "target": "00bdaee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adbd84`](#insn-00adbd84)

~~~json
{
  "source": "00adbd84",
  "target": "0109fe50",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fe50",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adbd8c`](#insn-00adbd8c)

~~~json
{
  "source": "00adbd8c",
  "target": "00ad9004",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adbd94`](#insn-00adbd94)

~~~json
{
  "source": "00adbd94",
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
- 参照命令 [`00adbd98`](#insn-00adbd98)

~~~json
{
  "source": "00adbd98",
  "target": "0109fe60",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fe60",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adbd9c`](#insn-00adbd9c)

~~~json
{
  "source": "00adbd9c",
  "target": "0109fe58",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fe58",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adbda0`](#insn-00adbda0)

~~~json
{
  "source": "00adbda0",
  "target": "0109fe50",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fe50",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adbda0`](#insn-00adbda0)

~~~json
{
  "source": "00adbda0",
  "target": "0109fe58",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fe58",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adbda4`](#insn-00adbda4)

~~~json
{
  "source": "00adbda4",
  "target": "00bdaee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adbdac`](#insn-00adbdac)

~~~json
{
  "source": "00adbdac",
  "target": "0109fe70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbdb4`](#insn-00adbdb4)

~~~json
{
  "source": "00adbdb4",
  "target": "00569da8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adbdb8`](#insn-00adbdb8)

~~~json
{
  "source": "00adbdb8",
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
- 参照命令 [`00adbdbc`](#insn-00adbdbc)

~~~json
{
  "source": "00adbdbc",
  "target": "0109fe90",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fe90",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adbdc0`](#insn-00adbdc0)

~~~json
{
  "source": "00adbdc0",
  "target": "00bdaee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adbdd0`](#insn-00adbdd0)

~~~json
{
  "source": "00adbdd0",
  "target": "0109fea0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbdd4`](#insn-00adbdd4)

~~~json
{
  "source": "00adbdd4",
  "target": "0085e2f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adbdd8`](#insn-00adbdd8)

~~~json
{
  "source": "00adbdd8",
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
- 参照命令 [`00adbddc`](#insn-00adbddc)

~~~json
{
  "source": "00adbddc",
  "target": "0109fec0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fec0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adbde0`](#insn-00adbde0)

~~~json
{
  "source": "00adbde0",
  "target": "00bdaee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adbde8`](#insn-00adbde8)

~~~json
{
  "source": "00adbde8",
  "target": "0109fed0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbdec`](#insn-00adbdec)

~~~json
{
  "source": "00adbdec",
  "target": "0085e2f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adbdf0`](#insn-00adbdf0)

~~~json
{
  "source": "00adbdf0",
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
- 参照命令 [`00adbdf4`](#insn-00adbdf4)

~~~json
{
  "source": "00adbdf4",
  "target": "0109fef0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fef0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adbdf8`](#insn-00adbdf8)

~~~json
{
  "source": "00adbdf8",
  "target": "00bdaee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adbe00`](#insn-00adbe00)

~~~json
{
  "source": "00adbe00",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbe08`](#insn-00adbe08)

~~~json
{
  "source": "00adbe08",
  "target": "00adbf50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbe0c`](#insn-00adbe0c)

~~~json
{
  "source": "00adbe0c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbe10`](#insn-00adbe10)

~~~json
{
  "source": "00adbe10",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbe14`](#insn-00adbe14)

~~~json
{
  "source": "00adbe14",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbe20`](#insn-00adbe20)

~~~json
{
  "source": "00adbe20",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbe24`](#insn-00adbe24)

~~~json
{
  "source": "00adbe24",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adbe28`](#insn-00adbe28)

~~~json
{
  "source": "00adbe28",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbe2c`](#insn-00adbe2c)

~~~json
{
  "source": "00adbe2c",
  "target": "00adbd08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbe30`](#insn-00adbe30)

~~~json
{
  "source": "00adbe30",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbe34`](#insn-00adbe34)

~~~json
{
  "source": "00adbe34",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adbe38`](#insn-00adbe38)

~~~json
{
  "source": "00adbe38",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbe3c`](#insn-00adbe3c)

~~~json
{
  "source": "00adbe3c",
  "target": "00adbd10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbe40`](#insn-00adbe40)

~~~json
{
  "source": "00adbe40",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbe44`](#insn-00adbe44)

~~~json
{
  "source": "00adbe44",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adbe48`](#insn-00adbe48)

~~~json
{
  "source": "00adbe48",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbe4c`](#insn-00adbe4c)

~~~json
{
  "source": "00adbe4c",
  "target": "00adbd18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbe50`](#insn-00adbe50)

~~~json
{
  "source": "00adbe50",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbe54`](#insn-00adbe54)

~~~json
{
  "source": "00adbe54",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adbe58`](#insn-00adbe58)

~~~json
{
  "source": "00adbe58",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbe5c`](#insn-00adbe5c)

~~~json
{
  "source": "00adbe5c",
  "target": "00adbd20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbe60`](#insn-00adbe60)

~~~json
{
  "source": "00adbe60",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbe64`](#insn-00adbe64)

~~~json
{
  "source": "00adbe64",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adbe68`](#insn-00adbe68)

~~~json
{
  "source": "00adbe68",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbe6c`](#insn-00adbe6c)

~~~json
{
  "source": "00adbe6c",
  "target": "00adbd28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbe70`](#insn-00adbe70)

~~~json
{
  "source": "00adbe70",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbe74`](#insn-00adbe74)

~~~json
{
  "source": "00adbe74",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adbe78`](#insn-00adbe78)

~~~json
{
  "source": "00adbe78",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbe7c`](#insn-00adbe7c)

~~~json
{
  "source": "00adbe7c",
  "target": "00adbd30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbe80`](#insn-00adbe80)

~~~json
{
  "source": "00adbe80",
  "target": "00adbd38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbf50`](#insn-00adbf50)

~~~json
{
  "source": "00adbf50",
  "target": "00bdaf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
