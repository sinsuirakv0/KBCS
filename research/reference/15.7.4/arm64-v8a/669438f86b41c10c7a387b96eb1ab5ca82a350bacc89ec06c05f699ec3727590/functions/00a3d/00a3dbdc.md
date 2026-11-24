# 00a3dbdc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00a3db98`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3d/00a3db98.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0055.md#compare-387944dba9c9ff296ff3515ca6a4451f)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00a9bad8`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a9b/00a9bad8.md) · 移動量 `+0x5defc`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0051.md#compare-17d0bf59a1494fab2ac4cb8a2e45724b)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00a3dbdc",
  "name": "_INIT_224",
  "size": 708,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "fd3ed6da49768c86171561f99a426e0428087eba9efa1ccb26d336edaa10694a",
  "source_text_sha256": "fd3ed6da49768c86171561f99a426e0428087eba9efa1ccb26d336edaa10694a",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00a3dbdc",
        "00a3de9b"
      ],
      [
        "00a3df68",
        "00a3df6b"
      ]
    ],
    "bytes_sha256": "c892e22fdf8a0cd0bb932dc2b0bf3d583d07cfaf06bb898471beb995fe740f28",
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

## 疑似コード / UTF-8 6897 bytes

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
  
                    /* try { // try from 00a3dbe4 to 00b3dbf3 has its CatchHandler @ 00a4232c */
  lVar1 = tpidr_el0;
                    /* try { // try from 00a3dbf4 to 00b3dc6f has its CatchHandler @ 00a2e43c */
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
                    /* try { // try from 00a3dc70 to 00b3dc7b has its CatchHandler @ 00a421f4 */
  local_cf = (char  [8])s_CgkIjM3y_ZQaEAIQBg_002a80e0._0_8_;
  uStack_9f = 0x7741;
                    /* try { // try from 00a3dc84 to 00b3dc8b has its CatchHandler @ 00a421e4 */
  local_98[0] = 4;
  uStack_a7 = (undefined7)s_CgkIjM3y_ZQaEAIQAw_002936ae._8_8_;
  cStack_a0 = SUB81(s_CgkIjM3y_ZQaEAIQAw_002936ae._8_8_,7);
                    /* try { // try from 00a3dc8c to 00b3dcab has its CatchHandler @ 00a2e43c */
  local_af = (char  [8])s_CgkIjM3y_ZQaEAIQAw_002936ae._0_8_;
  uStack_7f = 0x5142;
  local_78[0] = 5;
  uStack_87 = (undefined7)s_CgkIjM3y_ZQaEAIQBQ_0029c36c._8_8_;
  cStack_80 = SUB81(s_CgkIjM3y_ZQaEAIQBQ_0029c36c._8_8_,7);
                    /* try { // try from 00a3dcac to 00b3dcb7 has its CatchHandler @ 00a422cc */
  local_8f = (char  [8])s_CgkIjM3y_ZQaEAIQBQ_0029c36c._0_8_;
                    /* try { // try from 00a3dcb8 to 00b3dcc3 has its CatchHandler @ 00a422bc */
  uStack_5f = 0x7742;
  local_58[0] = 6;
  uStack_67 = (undefined7)s_CgkIjM3y_ZQaEAIQBw_00291877._8_8_;
  cStack_60 = SUB81(s_CgkIjM3y_ZQaEAIQBw_00291877._8_8_,7);
  local_6f = (char  [8])s_CgkIjM3y_ZQaEAIQBw_00291877._0_8_;
  local_110 = 0x24;
  local_f0 = 0x24;
  local_d0 = 0x24;
                    /* try { // try from 00a3dce8 to 00b3dceb has its CatchHandler @ 00a4239c */
  local_b0 = 0x24;
                    /* try { // try from 00a3dcec to 00b3dcff has its CatchHandler @ 00a42258 */
  local_90 = 0x24;
  local_70 = 0x24;
  local_50 = 0x24;
  local_118[0] = 0;
  uStack_fd = 0;
                    /* try { // try from 00a3dd04 to 00b3dd23 has its CatchHandler @ 00a422d0 */
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
                    /* try { // try from 00a3dd24 to 00b3dd37 has its CatchHandler @ 00a421dc */
  DAT_0109eea8 = 0;
  DAT_0109eea0 = 0;
  DAT_0109ee98 = &DAT_0109eea0;
                    /* try { // try from 00a3dd3c to 00b3dd47 has its CatchHandler @ 00a421c4 */
  FUN_00418cb8(&DAT_0109ee98,&DAT_0109eea0,local_118,local_118);
                    /* try { // try from 00a3dd48 to 00b3dd97 has its CatchHandler @ 00a2e43c */
  FUN_00418cb8(&DAT_0109ee98,&DAT_0109eea0,local_f8,local_f8);
  FUN_00418cb8(&DAT_0109ee98,&DAT_0109eea0,local_d8,local_d8);
  FUN_00418cb8(&DAT_0109ee98,&DAT_0109eea0,local_b8,local_b8);
  FUN_00418cb8(&DAT_0109ee98,&DAT_0109eea0,local_98,local_98);
                    /* try { // try from 00a3dd98 to 00b3dda3 has its CatchHandler @ 00a421a0 */
  FUN_00418cb8(&DAT_0109ee98,&DAT_0109eea0,local_78,local_78);
                    /* try { // try from 00a3dda4 to 00b3ddaf has its CatchHandler @ 00a42190 */
  FUN_00418cb8(&DAT_0109ee98,&DAT_0109eea0,local_58,local_58);
  if ((local_50 & 1) != 0) {
                    /* try { // try from 00a3de3c to 00b3de47 has its CatchHandler @ 00a420f4 */
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
                    /* try { // try from 00a3de78 to 00b3de87 has its CatchHandler @ 00a42158 */
    _ZdlPv((void *)CONCAT44(uStack_bc,CONCAT13(uStack_bd,CONCAT21(uStack_bf,cStack_c0))));
  }
  if ((local_f0 & 1) != 0) {
                    /* try { // try from 00a3de8c to 00b3de9b has its CatchHandler @ 00a420e0 */
    _ZdlPv((void *)CONCAT44(uStack_dc,CONCAT13(uStack_dd,CONCAT21(uStack_df,cStack_e0))));
  }
  if ((local_110 & 1) != 0) {
    _ZdlPv((void *)CONCAT44(uStack_fc,CONCAT13(uStack_fd,CONCAT21(uStack_ff,cStack_100))));
  }
                    /* try { // try from 00a3ddfc to 00b3de03 has its CatchHandler @ 00a4215c */
  __cxa_atexit(FUN_00418330,&DAT_0109ee98,&PTR_LOOP_00be5fd0);
                    /* try { // try from 00a3de1c to 00b3de2b has its CatchHandler @ 00a4218c */
  if (*(long *)(lVar1 + 0x28) == local_38) {
                    /* try { // try from 00a3de2c to 00b3de3b has its CatchHandler @ 00a42114 */
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
<a id="insn-00a3dbdc"></a> `00a3dbdc` | `ff 83 04 d1` | sub sp,sp,#0x120 | `FALL_THROUGH`
<a id="insn-00a3dbe0"></a> `00a3dbe0` | `fd 7b 0f a9` | stp x29,x30,[sp, #0xf0] | `FALL_THROUGH`
<a id="insn-00a3dbe4"></a> `00a3dbe4` | `fc 57 10 a9` | stp x28,x21,[sp, #0x100] | `FALL_THROUGH`
<a id="insn-00a3dbe8"></a> `00a3dbe8` | `f4 4f 11 a9` | stp x20,x19,[sp, #0x110] | `FALL_THROUGH`
<a id="insn-00a3dbec"></a> `00a3dbec` | `fd c3 03 91` | add x29,sp,#0xf0 | `FALL_THROUGH`
<a id="insn-00a3dbf0"></a> `00a3dbf0` | `55 d0 3b d5` | mrs x21,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00a3dbf4"></a> `00a3dbf4` | `2a e8 8c 52` | mov w10,#0x6741 | `FALL_THROUGH`
<a id="insn-00a3dbf8"></a> `00a3dbf8` | `f4 23 00 91` | add x20,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00a3dbfc"></a> `00a3dbfc` | `a9 16 40 f9` | ldr x9,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00a3dc00"></a> `00a3dc00` | `88 04 80 52` | mov w8,#0x24 | `FALL_THROUGH`
<a id="insn-00a3dc04"></a> `00a3dc04` | `13 33 00 b0` | adrp x19,0x109e000 | `FALL_THROUGH`
<a id="insn-00a3dc08"></a> `00a3dc08` | `73 62 3a 91` | add x19,x19,#0xe98 | `FALL_THROUGH`
<a id="insn-00a3dc0c"></a> `00a3dc0c` | `a9 83 1f f8` | stur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00a3dc10"></a> `00a3dc10` | `49 c3 ff d0` | adrp x9,0x2a7000 | `FALL_THROUGH`
<a id="insn-00a3dc14"></a> `00a3dc14` | `29 dd 0d 91` | add x9,x9,#0x377 | `FALL_THROUGH`
<a id="insn-00a3dc18"></a> `00a3dc18` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00a3dc1c"></a> `00a3dc1c` | `29 00 80 52` | mov w9,#0x1 | `FALL_THROUGH`
<a id="insn-00a3dc20"></a> `00a3dc20` | `ea 13 02 78` | sturh w10,[sp, #0x21] | `FALL_THROUGH`
<a id="insn-00a3dc24"></a> `00a3dc24` | `e9 2b 00 b9` | str w9,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00a3dc28"></a> `00a3dc28` | `49 28 88 52` | mov w9,#0x4142 | `FALL_THROUGH`
<a id="insn-00a3dc2c"></a> `00a3dc2c` | `4a c3 ff d0` | adrp x10,0x2a7000 | `FALL_THROUGH`
<a id="insn-00a3dc30"></a> `00a3dc30` | `4a 29 0e 91` | add x10,x10,#0x38a | `FALL_THROUGH`
<a id="insn-00a3dc34"></a> `00a3dc34` | `e0 13 81 3c` | stur q0,[sp, #0x11] | `FALL_THROUGH`
<a id="insn-00a3dc38"></a> `00a3dc38` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00a3dc3c"></a> `00a3dc3c` | `40 01 c0 3d` | ldr q0,[x10] | `FALL_THROUGH`
<a id="insn-00a3dc40"></a> `00a3dc40` | `e9 13 04 78` | sturh w9,[sp, #0x41] | `FALL_THROUGH`
<a id="insn-00a3dc44"></a> `00a3dc44` | `49 00 80 52` | mov w9,#0x2 | `FALL_THROUGH`
<a id="insn-00a3dc48"></a> `00a3dc48` | `e9 4b 00 b9` | str w9,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00a3dc4c"></a> `00a3dc4c` | `49 e8 8c 52` | mov w9,#0x6742 | `FALL_THROUGH`
<a id="insn-00a3dc50"></a> `00a3dc50` | `4a c3 ff f0` | adrp x10,0x2a8000 | `FALL_THROUGH`
<a id="insn-00a3dc54"></a> `00a3dc54` | `4a 81 03 91` | add x10,x10,#0xe0 | `FALL_THROUGH`
<a id="insn-00a3dc58"></a> `00a3dc58` | `e0 13 83 3c` | stur q0,[sp, #0x31] | `FALL_THROUGH`
<a id="insn-00a3dc5c"></a> `00a3dc5c` | `40 01 c0 3d` | ldr q0,[x10] | `FALL_THROUGH`
<a id="insn-00a3dc60"></a> `00a3dc60` | `e9 13 06 78` | sturh w9,[sp, #0x61] | `FALL_THROUGH`
<a id="insn-00a3dc64"></a> `00a3dc64` | `69 00 80 52` | mov w9,#0x3 | `FALL_THROUGH`
<a id="insn-00a3dc68"></a> `00a3dc68` | `e9 6b 00 b9` | str w9,[sp, #0x68] | `FALL_THROUGH`
<a id="insn-00a3dc6c"></a> `00a3dc6c` | `29 e8 8e 52` | mov w9,#0x7741 | `FALL_THROUGH`
<a id="insn-00a3dc70"></a> `00a3dc70` | `aa c2 ff d0` | adrp x10,0x293000 | `FALL_THROUGH`
<a id="insn-00a3dc74"></a> `00a3dc74` | `4a b9 1a 91` | add x10,x10,#0x6ae | `FALL_THROUGH`
<a id="insn-00a3dc78"></a> `00a3dc78` | `e0 13 85 3c` | stur q0,[sp, #0x51] | `FALL_THROUGH`
<a id="insn-00a3dc7c"></a> `00a3dc7c` | `40 01 c0 3d` | ldr q0,[x10] | `FALL_THROUGH`
<a id="insn-00a3dc80"></a> `00a3dc80` | `e9 13 08 78` | sturh w9,[sp, #0x81] | `FALL_THROUGH`
<a id="insn-00a3dc84"></a> `00a3dc84` | `89 00 80 52` | mov w9,#0x4 | `FALL_THROUGH`
<a id="insn-00a3dc88"></a> `00a3dc88` | `e9 8b 00 b9` | str w9,[sp, #0x88] | `FALL_THROUGH`
<a id="insn-00a3dc8c"></a> `00a3dc8c` | `e9 c2 ff f0` | adrp x9,0x29c000 | `FALL_THROUGH`
<a id="insn-00a3dc90"></a> `00a3dc90` | `29 b1 0d 91` | add x9,x9,#0x36c | `FALL_THROUGH`
<a id="insn-00a3dc94"></a> `00a3dc94` | `e0 13 87 3c` | stur q0,[sp, #0x71] | `FALL_THROUGH`
<a id="insn-00a3dc98"></a> `00a3dc98` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00a3dc9c"></a> `00a3dc9c` | `49 28 8a 52` | mov w9,#0x5142 | `FALL_THROUGH`
<a id="insn-00a3dca0"></a> `00a3dca0` | `89 92 09 78` | sturh w9,[x20, #0x99] | `FALL_THROUGH`
<a id="insn-00a3dca4"></a> `00a3dca4` | `a9 00 80 52` | mov w9,#0x5 | `FALL_THROUGH`
<a id="insn-00a3dca8"></a> `00a3dca8` | `e9 ab 00 b9` | str w9,[sp, #0xa8] | `FALL_THROUGH`
<a id="insn-00a3dcac"></a> `00a3dcac` | `a9 c2 ff 90` | adrp x9,0x291000 | `FALL_THROUGH`
<a id="insn-00a3dcb0"></a> `00a3dcb0` | `29 dd 21 91` | add x9,x9,#0x877 | `FALL_THROUGH`
<a id="insn-00a3dcb4"></a> `00a3dcb4` | `80 92 88 3c` | stur q0,[x20, #0x89] | `FALL_THROUGH`
<a id="insn-00a3dcb8"></a> `00a3dcb8` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00a3dcbc"></a> `00a3dcbc` | `49 e8 8e 52` | mov w9,#0x7742 | `FALL_THROUGH`
<a id="insn-00a3dcc0"></a> `00a3dcc0` | `89 92 0b 78` | sturh w9,[x20, #0xb9] | `FALL_THROUGH`
<a id="insn-00a3dcc4"></a> `00a3dcc4` | `c9 00 80 52` | mov w9,#0x6 | `FALL_THROUGH`
<a id="insn-00a3dcc8"></a> `00a3dcc8` | `e9 cb 00 b9` | str w9,[sp, #0xc8] | `FALL_THROUGH`
<a id="insn-00a3dccc"></a> `00a3dccc` | `a9 c2 ff f0` | adrp x9,0x294000 | `FALL_THROUGH`
<a id="insn-00a3dcd0"></a> `00a3dcd0` | `29 99 14 91` | add x9,x9,#0x526 | `FALL_THROUGH`
<a id="insn-00a3dcd4"></a> `00a3dcd4` | `80 92 8a 3c` | stur q0,[x20, #0xa9] | `FALL_THROUGH`
<a id="insn-00a3dcd8"></a> `00a3dcd8` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00a3dcdc"></a> `00a3dcdc` | `e8 43 00 39` | strb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a3dce0"></a> `00a3dce0` | `e8 c3 00 39` | strb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00a3dce4"></a> `00a3dce4` | `e8 43 01 39` | strb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00a3dce8"></a> `00a3dce8` | `e8 c3 01 39` | strb w8,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00a3dcec"></a> `00a3dcec` | `e8 43 02 39` | strb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00a3dcf0"></a> `00a3dcf0` | `e8 c3 02 39` | strb w8,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00a3dcf4"></a> `00a3dcf4` | `e8 43 03 39` | strb w8,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-00a3dcf8"></a> `00a3dcf8` | `68 28 88 52` | mov w8,#0x4143 | `FALL_THROUGH`
<a id="insn-00a3dcfc"></a> `00a3dcfc` | `ff 0b 00 b9` | str wzr,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00a3dd00"></a> `00a3dd00` | `ff 8f 00 39` | strb wzr,[sp, #0x23] | `FALL_THROUGH`
<a id="insn-00a3dd04"></a> `00a3dd04` | `ff 0f 01 39` | strb wzr,[sp, #0x43] | `FALL_THROUGH`
<a id="insn-00a3dd08"></a> `00a3dd08` | `ff 8f 01 39` | strb wzr,[sp, #0x63] | `FALL_THROUGH`
<a id="insn-00a3dd0c"></a> `00a3dd0c` | `ff 0f 02 39` | strb wzr,[sp, #0x83] | `FALL_THROUGH`
<a id="insn-00a3dd10"></a> `00a3dd10` | `ff 8f 02 39` | strb wzr,[sp, #0xa3] | `FALL_THROUGH`
<a id="insn-00a3dd14"></a> `00a3dd14` | `ff 0f 03 39` | strb wzr,[sp, #0xc3] | `FALL_THROUGH`
<a id="insn-00a3dd18"></a> `00a3dd18` | `88 92 0d 78` | sturh w8,[x20, #0xd9] | `FALL_THROUGH`
<a id="insn-00a3dd1c"></a> `00a3dd1c` | `80 92 8c 3c` | stur q0,[x20, #0xc9] | `FALL_THROUGH`
<a id="insn-00a3dd20"></a> `00a3dd20` | `ff 8f 03 39` | strb wzr,[sp, #0xe3] | `FALL_THROUGH`
<a id="insn-00a3dd24"></a> `00a3dd24` | `7f 0a 00 f9` | str xzr,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00a3dd28"></a> `00a3dd28` | `3f 8c 00 f8` | str xzr,[x1, #0x8]! | `FALL_THROUGH`
<a id="insn-00a3dd2c"></a> `00a3dd2c` | `61 02 00 f9` | str x1,[x19] | `FALL_THROUGH`
<a id="insn-00a3dd30"></a> `00a3dd30` | `e2 23 00 91` | add x2,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00a3dd34"></a> `00a3dd34` | `e3 23 00 91` | add x3,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00a3dd38"></a> `00a3dd38` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00a3dd3c"></a> `00a3dd3c` | `df 6b e7 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-00a3dd40"></a> `00a3dd40` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00a3dd44"></a> `00a3dd44` | `82 82 00 91` | add x2,x20,#0x20 | `FALL_THROUGH`
<a id="insn-00a3dd48"></a> `00a3dd48` | `83 82 00 91` | add x3,x20,#0x20 | `FALL_THROUGH`
<a id="insn-00a3dd4c"></a> `00a3dd4c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00a3dd50"></a> `00a3dd50` | `da 6b e7 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-00a3dd54"></a> `00a3dd54` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00a3dd58"></a> `00a3dd58` | `82 02 01 91` | add x2,x20,#0x40 | `FALL_THROUGH`
<a id="insn-00a3dd5c"></a> `00a3dd5c` | `83 02 01 91` | add x3,x20,#0x40 | `FALL_THROUGH`
<a id="insn-00a3dd60"></a> `00a3dd60` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00a3dd64"></a> `00a3dd64` | `d5 6b e7 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-00a3dd68"></a> `00a3dd68` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00a3dd6c"></a> `00a3dd6c` | `82 82 01 91` | add x2,x20,#0x60 | `FALL_THROUGH`
<a id="insn-00a3dd70"></a> `00a3dd70` | `83 82 01 91` | add x3,x20,#0x60 | `FALL_THROUGH`
<a id="insn-00a3dd74"></a> `00a3dd74` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00a3dd78"></a> `00a3dd78` | `d0 6b e7 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-00a3dd7c"></a> `00a3dd7c` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00a3dd80"></a> `00a3dd80` | `82 02 02 91` | add x2,x20,#0x80 | `FALL_THROUGH`
<a id="insn-00a3dd84"></a> `00a3dd84` | `83 02 02 91` | add x3,x20,#0x80 | `FALL_THROUGH`
<a id="insn-00a3dd88"></a> `00a3dd88` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00a3dd8c"></a> `00a3dd8c` | `cb 6b e7 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-00a3dd90"></a> `00a3dd90` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00a3dd94"></a> `00a3dd94` | `82 82 02 91` | add x2,x20,#0xa0 | `FALL_THROUGH`
<a id="insn-00a3dd98"></a> `00a3dd98` | `83 82 02 91` | add x3,x20,#0xa0 | `FALL_THROUGH`
<a id="insn-00a3dd9c"></a> `00a3dd9c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00a3dda0"></a> `00a3dda0` | `c6 6b e7 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-00a3dda4"></a> `00a3dda4` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00a3dda8"></a> `00a3dda8` | `82 02 03 91` | add x2,x20,#0xc0 | `FALL_THROUGH`
<a id="insn-00a3ddac"></a> `00a3ddac` | `83 02 03 91` | add x3,x20,#0xc0 | `FALL_THROUGH`
<a id="insn-00a3ddb0"></a> `00a3ddb0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00a3ddb4"></a> `00a3ddb4` | `c1 6b e7 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-00a3ddb8"></a> `00a3ddb8` | `e8 43 43 39` | ldrb w8,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-00a3ddbc"></a> `00a3ddbc` | `e8 03 00 37` | tbnz w8,#0x0,0x00a3de38 | `CONDITIONAL_JUMP`
<a id="insn-00a3ddc0"></a> `00a3ddc0` | `e8 c3 42 39` | ldrb w8,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00a3ddc4"></a> `00a3ddc4` | `28 04 00 37` | tbnz w8,#0x0,0x00a3de48 | `CONDITIONAL_JUMP`
<a id="insn-00a3ddc8"></a> `00a3ddc8` | `e8 43 42 39` | ldrb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00a3ddcc"></a> `00a3ddcc` | `68 04 00 37` | tbnz w8,#0x0,0x00a3de58 | `CONDITIONAL_JUMP`
<a id="insn-00a3ddd0"></a> `00a3ddd0` | `e8 c3 41 39` | ldrb w8,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00a3ddd4"></a> `00a3ddd4` | `a8 04 00 37` | tbnz w8,#0x0,0x00a3de68 | `CONDITIONAL_JUMP`
<a id="insn-00a3ddd8"></a> `00a3ddd8` | `e8 43 41 39` | ldrb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00a3dddc"></a> `00a3dddc` | `e8 04 00 37` | tbnz w8,#0x0,0x00a3de78 | `CONDITIONAL_JUMP`
<a id="insn-00a3dde0"></a> `00a3dde0` | `e8 c3 40 39` | ldrb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00a3dde4"></a> `00a3dde4` | `28 05 00 37` | tbnz w8,#0x0,0x00a3de88 | `CONDITIONAL_JUMP`
<a id="insn-00a3dde8"></a> `00a3dde8` | `e8 43 40 39` | ldrb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a3ddec"></a> `00a3ddec` | `68 00 00 36` | tbz w8,#0x0,0x00a3ddf8 | `CONDITIONAL_JUMP`
<a id="insn-00a3ddf0"></a> `00a3ddf0` | `e0 13 40 f9` | ldr x0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00a3ddf4"></a> `00a3ddf4` | `9b 74 06 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00a3ddf8"></a> `00a3ddf8` | `c0 ce ff f0` | adrp x0,0x418000 | `FALL_THROUGH`
<a id="insn-00a3ddfc"></a> `00a3ddfc` | `00 c0 0c 91` | add x0,x0,#0x330 | `FALL_THROUGH`
<a id="insn-00a3de00"></a> `00a3de00` | `01 33 00 b0` | adrp x1,0x109e000 | `FALL_THROUGH`
<a id="insn-00a3de04"></a> `00a3de04` | `21 60 3a 91` | add x1,x1,#0xe98 | `FALL_THROUGH`
<a id="insn-00a3de08"></a> `00a3de08` | `42 0d 00 90` | adrp x2,0xbe5000 | `FALL_THROUGH`
<a id="insn-00a3de0c"></a> `00a3de0c` | `42 40 3f 91` | add x2,x2,#0xfd0 | `FALL_THROUGH`
<a id="insn-00a3de10"></a> `00a3de10` | `74 74 06 94` | bl 0x00bdafe0 | `UNCONDITIONAL_CALL`
<a id="insn-00a3de14"></a> `00a3de14` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00a3de18"></a> `00a3de18` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00a3de1c"></a> `00a3de1c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00a3de20"></a> `00a3de20` | `41 0a 00 54` | b.ne 0x00a3df68 | `CONDITIONAL_JUMP`
<a id="insn-00a3de24"></a> `00a3de24` | `f4 4f 51 a9` | ldp x20,x19,[sp, #0x110] | `FALL_THROUGH`
<a id="insn-00a3de28"></a> `00a3de28` | `fc 57 50 a9` | ldp x28,x21,[sp, #0x100] | `FALL_THROUGH`
<a id="insn-00a3de2c"></a> `00a3de2c` | `fd 7b 4f a9` | ldp x29,x30,[sp, #0xf0] | `FALL_THROUGH`
<a id="insn-00a3de30"></a> `00a3de30` | `ff 83 04 91` | add sp,sp,#0x120 | `FALL_THROUGH`
<a id="insn-00a3de34"></a> `00a3de34` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00a3de38"></a> `00a3de38` | `e0 73 40 f9` | ldr x0,[sp, #0xe0] | `FALL_THROUGH`
<a id="insn-00a3de3c"></a> `00a3de3c` | `89 74 06 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00a3de40"></a> `00a3de40` | `e8 c3 42 39` | ldrb w8,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00a3de44"></a> `00a3de44` | `28 fc 07 36` | tbz w8,#0x0,0x00a3ddc8 | `CONDITIONAL_JUMP`
<a id="insn-00a3de48"></a> `00a3de48` | `e0 63 40 f9` | ldr x0,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00a3de4c"></a> `00a3de4c` | `85 74 06 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00a3de50"></a> `00a3de50` | `e8 43 42 39` | ldrb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00a3de54"></a> `00a3de54` | `e8 fb 07 36` | tbz w8,#0x0,0x00a3ddd0 | `CONDITIONAL_JUMP`
<a id="insn-00a3de58"></a> `00a3de58` | `e0 53 40 f9` | ldr x0,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00a3de5c"></a> `00a3de5c` | `81 74 06 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00a3de60"></a> `00a3de60` | `e8 c3 41 39` | ldrb w8,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00a3de64"></a> `00a3de64` | `a8 fb 07 36` | tbz w8,#0x0,0x00a3ddd8 | `CONDITIONAL_JUMP`
<a id="insn-00a3de68"></a> `00a3de68` | `e0 43 40 f9` | ldr x0,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00a3de6c"></a> `00a3de6c` | `7d 74 06 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00a3de70"></a> `00a3de70` | `e8 43 41 39` | ldrb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00a3de74"></a> `00a3de74` | `68 fb 07 36` | tbz w8,#0x0,0x00a3dde0 | `CONDITIONAL_JUMP`
<a id="insn-00a3de78"></a> `00a3de78` | `e0 33 40 f9` | ldr x0,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00a3de7c"></a> `00a3de7c` | `79 74 06 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00a3de80"></a> `00a3de80` | `e8 c3 40 39` | ldrb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00a3de84"></a> `00a3de84` | `28 fb 07 36` | tbz w8,#0x0,0x00a3dde8 | `CONDITIONAL_JUMP`
<a id="insn-00a3de88"></a> `00a3de88` | `e0 23 40 f9` | ldr x0,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00a3de8c"></a> `00a3de8c` | `75 74 06 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00a3de90"></a> `00a3de90` | `e8 43 40 39` | ldrb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a3de94"></a> `00a3de94` | `e8 fa 07 37` | tbnz w8,#0x0,0x00a3ddf0 | `CONDITIONAL_JUMP`
<a id="insn-00a3de98"></a> `00a3de98` | `d8 ff ff 17` | b 0x00a3ddf8 | `UNCONDITIONAL_JUMP`
<a id="insn-00a3df68"></a> `00a3df68` | `4a 74 06 94` | bl 0x00bdb090 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00a3dbdc`](#insn-00a3dbdc) 範囲 `[['00a3dbdc', '00a3dbe3']]`
  - `FALL_THROUGH` [`00a3dbe0`](#insn-00a3dbe0) → [`00a3dbe4`](#insn-00a3dbe4)
- ブロック [`00a3dbe4`](#insn-00a3dbe4) 範囲 `[['00a3dbe4', '00a3dbf3']]`
  - `FALL_THROUGH` [`00a3dbf0`](#insn-00a3dbf0) → [`00a3dbf4`](#insn-00a3dbf4)
- ブロック [`00a3dbf4`](#insn-00a3dbf4) 範囲 `[['00a3dbf4', '00a3dc6f']]`
  - `FALL_THROUGH` [`00a3dc6c`](#insn-00a3dc6c) → [`00a3dc70`](#insn-00a3dc70)
- ブロック [`00a3dc70`](#insn-00a3dc70) 範囲 `[['00a3dc70', '00a3dc83']]`
  - `FALL_THROUGH` [`00a3dc80`](#insn-00a3dc80) → [`00a3dc84`](#insn-00a3dc84)
- ブロック [`00a3dc84`](#insn-00a3dc84) 範囲 `[['00a3dc84', '00a3dc8b']]`
  - `FALL_THROUGH` [`00a3dc88`](#insn-00a3dc88) → [`00a3dc8c`](#insn-00a3dc8c)
- ブロック [`00a3dc8c`](#insn-00a3dc8c) 範囲 `[['00a3dc8c', '00a3dcab']]`
  - `FALL_THROUGH` [`00a3dca8`](#insn-00a3dca8) → [`00a3dcac`](#insn-00a3dcac)
- ブロック [`00a3dcac`](#insn-00a3dcac) 範囲 `[['00a3dcac', '00a3dcb7']]`
  - `FALL_THROUGH` [`00a3dcb4`](#insn-00a3dcb4) → [`00a3dcb8`](#insn-00a3dcb8)
- ブロック [`00a3dcb8`](#insn-00a3dcb8) 範囲 `[['00a3dcb8', '00a3dce7']]`
  - `FALL_THROUGH` [`00a3dce4`](#insn-00a3dce4) → [`00a3dce8`](#insn-00a3dce8)
- ブロック [`00a3dce8`](#insn-00a3dce8) 範囲 `[['00a3dce8', '00a3dceb']]`
  - `FALL_THROUGH` [`00a3dce8`](#insn-00a3dce8) → [`00a3dcec`](#insn-00a3dcec)
- ブロック [`00a3dcec`](#insn-00a3dcec) 範囲 `[['00a3dcec', '00a3dd03']]`
  - `FALL_THROUGH` [`00a3dd00`](#insn-00a3dd00) → [`00a3dd04`](#insn-00a3dd04)
- ブロック [`00a3dd04`](#insn-00a3dd04) 範囲 `[['00a3dd04', '00a3dd23']]`
  - `FALL_THROUGH` [`00a3dd20`](#insn-00a3dd20) → [`00a3dd24`](#insn-00a3dd24)
- ブロック [`00a3dd24`](#insn-00a3dd24) 範囲 `[['00a3dd24', '00a3dd3b']]`
  - `FALL_THROUGH` [`00a3dd38`](#insn-00a3dd38) → [`00a3dd3c`](#insn-00a3dd3c)
- ブロック [`00a3dd3c`](#insn-00a3dd3c) 範囲 `[['00a3dd3c', '00a3dd47']]`
  - `FALL_THROUGH` [`00a3dd44`](#insn-00a3dd44) → [`00a3dd48`](#insn-00a3dd48)
- ブロック [`00a3dd48`](#insn-00a3dd48) 範囲 `[['00a3dd48', '00a3dd97']]`
  - `FALL_THROUGH` [`00a3dd94`](#insn-00a3dd94) → [`00a3dd98`](#insn-00a3dd98)
- ブロック [`00a3dd98`](#insn-00a3dd98) 範囲 `[['00a3dd98', '00a3dda3']]`
  - `FALL_THROUGH` [`00a3dda0`](#insn-00a3dda0) → [`00a3dda4`](#insn-00a3dda4)
- ブロック [`00a3dda4`](#insn-00a3dda4) 範囲 `[['00a3dda4', '00a3ddbf']]`
  - `CONDITIONAL_JUMP` [`00a3ddbc`](#insn-00a3ddbc) → [`00a3de38`](#insn-00a3de38)
  - `FALL_THROUGH` [`00a3ddbc`](#insn-00a3ddbc) → [`00a3ddc0`](#insn-00a3ddc0)
- ブロック [`00a3ddc0`](#insn-00a3ddc0) 範囲 `[['00a3ddc0', '00a3ddc7']]`
  - `CONDITIONAL_JUMP` [`00a3ddc4`](#insn-00a3ddc4) → [`00a3de48`](#insn-00a3de48)
  - `FALL_THROUGH` [`00a3ddc4`](#insn-00a3ddc4) → [`00a3ddc8`](#insn-00a3ddc8)
- ブロック [`00a3ddc8`](#insn-00a3ddc8) 範囲 `[['00a3ddc8', '00a3ddcf']]`
  - `CONDITIONAL_JUMP` [`00a3ddcc`](#insn-00a3ddcc) → [`00a3de58`](#insn-00a3de58)
  - `FALL_THROUGH` [`00a3ddcc`](#insn-00a3ddcc) → [`00a3ddd0`](#insn-00a3ddd0)
- ブロック [`00a3ddd0`](#insn-00a3ddd0) 範囲 `[['00a3ddd0', '00a3ddd7']]`
  - `CONDITIONAL_JUMP` [`00a3ddd4`](#insn-00a3ddd4) → [`00a3de68`](#insn-00a3de68)
  - `FALL_THROUGH` [`00a3ddd4`](#insn-00a3ddd4) → [`00a3ddd8`](#insn-00a3ddd8)
- ブロック [`00a3ddd8`](#insn-00a3ddd8) 範囲 `[['00a3ddd8', '00a3dddf']]`
  - `CONDITIONAL_JUMP` [`00a3dddc`](#insn-00a3dddc) → [`00a3de78`](#insn-00a3de78)
  - `FALL_THROUGH` [`00a3dddc`](#insn-00a3dddc) → [`00a3dde0`](#insn-00a3dde0)
- ブロック [`00a3dde0`](#insn-00a3dde0) 範囲 `[['00a3dde0', '00a3dde3']]`
  - `FALL_THROUGH` [`00a3dde0`](#insn-00a3dde0) → [`00a3dde4`](#insn-00a3dde4)
- ブロック [`00a3dde4`](#insn-00a3dde4) 範囲 `[['00a3dde4', '00a3dde7']]`
  - `CONDITIONAL_JUMP` [`00a3dde4`](#insn-00a3dde4) → [`00a3de88`](#insn-00a3de88)
  - `FALL_THROUGH` [`00a3dde4`](#insn-00a3dde4) → [`00a3dde8`](#insn-00a3dde8)
- ブロック [`00a3dde8`](#insn-00a3dde8) 範囲 `[['00a3dde8', '00a3ddef']]`
  - `CONDITIONAL_JUMP` [`00a3ddec`](#insn-00a3ddec) → [`00a3ddf8`](#insn-00a3ddf8)
  - `FALL_THROUGH` [`00a3ddec`](#insn-00a3ddec) → [`00a3ddf0`](#insn-00a3ddf0)
- ブロック [`00a3ddf0`](#insn-00a3ddf0) 範囲 `[['00a3ddf0', '00a3ddf7']]`
  - `FALL_THROUGH` [`00a3ddf4`](#insn-00a3ddf4) → [`00a3ddf8`](#insn-00a3ddf8)
- ブロック [`00a3ddf8`](#insn-00a3ddf8) 範囲 `[['00a3ddf8', '00a3ddfb']]`
  - `FALL_THROUGH` [`00a3ddf8`](#insn-00a3ddf8) → [`00a3ddfc`](#insn-00a3ddfc)
- ブロック [`00a3ddfc`](#insn-00a3ddfc) 範囲 `[['00a3ddfc', '00a3de1b']]`
  - `FALL_THROUGH` [`00a3de18`](#insn-00a3de18) → [`00a3de1c`](#insn-00a3de1c)
- ブロック [`00a3de1c`](#insn-00a3de1c) 範囲 `[['00a3de1c', '00a3de23']]`
  - `CONDITIONAL_JUMP` [`00a3de20`](#insn-00a3de20) → [`00a3df68`](#insn-00a3df68)
  - `FALL_THROUGH` [`00a3de20`](#insn-00a3de20) → [`00a3de24`](#insn-00a3de24)
- ブロック [`00a3de24`](#insn-00a3de24) 範囲 `[['00a3de24', '00a3de2b']]`
  - `FALL_THROUGH` [`00a3de28`](#insn-00a3de28) → [`00a3de2c`](#insn-00a3de2c)
- ブロック [`00a3de2c`](#insn-00a3de2c) 範囲 `[['00a3de2c', '00a3de37']]`
- ブロック [`00a3de38`](#insn-00a3de38) 範囲 `[['00a3de38', '00a3de3b']]`
  - `FALL_THROUGH` [`00a3de38`](#insn-00a3de38) → [`00a3de3c`](#insn-00a3de3c)
- ブロック [`00a3de3c`](#insn-00a3de3c) 範囲 `[['00a3de3c', '00a3de47']]`
  - `CONDITIONAL_JUMP` [`00a3de44`](#insn-00a3de44) → [`00a3ddc8`](#insn-00a3ddc8)
  - `FALL_THROUGH` [`00a3de44`](#insn-00a3de44) → [`00a3de48`](#insn-00a3de48)
- ブロック [`00a3de48`](#insn-00a3de48) 範囲 `[['00a3de48', '00a3de57']]`
  - `CONDITIONAL_JUMP` [`00a3de54`](#insn-00a3de54) → [`00a3ddd0`](#insn-00a3ddd0)
  - `FALL_THROUGH` [`00a3de54`](#insn-00a3de54) → [`00a3de58`](#insn-00a3de58)
- ブロック [`00a3de58`](#insn-00a3de58) 範囲 `[['00a3de58', '00a3de67']]`
  - `CONDITIONAL_JUMP` [`00a3de64`](#insn-00a3de64) → [`00a3ddd8`](#insn-00a3ddd8)
  - `FALL_THROUGH` [`00a3de64`](#insn-00a3de64) → [`00a3de68`](#insn-00a3de68)
- ブロック [`00a3de68`](#insn-00a3de68) 範囲 `[['00a3de68', '00a3de77']]`
  - `CONDITIONAL_JUMP` [`00a3de74`](#insn-00a3de74) → [`00a3dde0`](#insn-00a3dde0)
  - `FALL_THROUGH` [`00a3de74`](#insn-00a3de74) → [`00a3de78`](#insn-00a3de78)
- ブロック [`00a3de78`](#insn-00a3de78) 範囲 `[['00a3de78', '00a3de87']]`
  - `CONDITIONAL_JUMP` [`00a3de84`](#insn-00a3de84) → [`00a3dde8`](#insn-00a3dde8)
  - `FALL_THROUGH` [`00a3de84`](#insn-00a3de84) → [`00a3de88`](#insn-00a3de88)
- ブロック [`00a3de88`](#insn-00a3de88) 範囲 `[['00a3de88', '00a3de8b']]`
  - `FALL_THROUGH` [`00a3de88`](#insn-00a3de88) → [`00a3de8c`](#insn-00a3de8c)
- ブロック [`00a3de8c`](#insn-00a3de8c) 範囲 `[['00a3de8c', '00a3de97']]`
  - `CONDITIONAL_JUMP` [`00a3de94`](#insn-00a3de94) → [`00a3ddf0`](#insn-00a3ddf0)
  - `FALL_THROUGH` [`00a3de94`](#insn-00a3de94) → [`00a3de98`](#insn-00a3de98)
- ブロック [`00a3de98`](#insn-00a3de98) 範囲 `[['00a3de98', '00a3de9b']]`
  - `UNCONDITIONAL_JUMP` [`00a3de98`](#insn-00a3de98) → [`00a3ddf8`](#insn-00a3ddf8)
- ブロック [`00a3df68`](#insn-00a3df68) 範囲 `[['00a3df68', '00a3df6b']]`

## 命令位置別の参照

- [`00a3dbe0`](#insn-00a3dbe0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3dbe4`](#insn-00a3dbe4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3dbe8`](#insn-00a3dbe8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3dc0c`](#insn-00a3dc0c) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3dc18`](#insn-00a3dc18) → `002a7377`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00a3dc20`](#insn-00a3dc20) → `Stack[-0xff]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3dc24`](#insn-00a3dc24) → `Stack[-0xf8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3dc34`](#insn-00a3dc34) → `Stack[-0x10f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3dc3c`](#insn-00a3dc3c) → `002a738a`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00a3dc40`](#insn-00a3dc40) → `Stack[-0xdf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3dc48`](#insn-00a3dc48) → `Stack[-0xd8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3dc58`](#insn-00a3dc58) → `Stack[-0xef]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3dc5c`](#insn-00a3dc5c) → `002a80e0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00a3dc60`](#insn-00a3dc60) → `Stack[-0xbf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3dc68`](#insn-00a3dc68) → `Stack[-0xb8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3dc78`](#insn-00a3dc78) → `Stack[-0xcf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3dc7c`](#insn-00a3dc7c) → `002936ae`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00a3dc80`](#insn-00a3dc80) → `Stack[-0x9f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3dc88`](#insn-00a3dc88) → `Stack[-0x98]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3dc94`](#insn-00a3dc94) → `Stack[-0xaf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3dc98`](#insn-00a3dc98) → `0029c36c`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00a3dca0`](#insn-00a3dca0) → `Stack[-0x7f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3dca8`](#insn-00a3dca8) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3dcb4`](#insn-00a3dcb4) → `Stack[-0x8f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3dcb8`](#insn-00a3dcb8) → `00291877`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00a3dcc0`](#insn-00a3dcc0) → `Stack[-0x5f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3dcc8`](#insn-00a3dcc8) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3dcd4`](#insn-00a3dcd4) → `Stack[-0x6f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3dcd8`](#insn-00a3dcd8) → `00294526`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00a3dcdc`](#insn-00a3dcdc) → `Stack[-0x110]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3dce0`](#insn-00a3dce0) → `Stack[-0xf0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3dce4`](#insn-00a3dce4) → `Stack[-0xd0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3dce8`](#insn-00a3dce8) → `Stack[-0xb0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3dcec`](#insn-00a3dcec) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3dcf0`](#insn-00a3dcf0) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3dcf4`](#insn-00a3dcf4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3dcfc`](#insn-00a3dcfc) → `Stack[-0x118]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3dd00`](#insn-00a3dd00) → `Stack[-0xfd]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3dd04`](#insn-00a3dd04) → `Stack[-0xdd]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3dd08`](#insn-00a3dd08) → `Stack[-0xbd]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3dd0c`](#insn-00a3dd0c) → `Stack[-0x9d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3dd10`](#insn-00a3dd10) → `Stack[-0x7d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3dd14`](#insn-00a3dd14) → `Stack[-0x5d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3dd18`](#insn-00a3dd18) → `Stack[-0x3f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3dd1c`](#insn-00a3dd1c) → `Stack[-0x4f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3dd20`](#insn-00a3dd20) → `Stack[-0x3d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3dd24`](#insn-00a3dd24) → `0109eea8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a3dd28`](#insn-00a3dd28) → `0109eea0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a3dd2c`](#insn-00a3dd2c) → `0109ee98`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a3dd2c`](#insn-00a3dd2c) → `0109eea0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a3dd38`](#insn-00a3dd38) → `0109ee98`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a3dd3c`](#insn-00a3dd3c) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`00a3dd40`](#insn-00a3dd40) → `0109eea0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a3dd4c`](#insn-00a3dd4c) → `0109ee98`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a3dd50`](#insn-00a3dd50) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`00a3dd54`](#insn-00a3dd54) → `0109eea0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a3dd60`](#insn-00a3dd60) → `0109ee98`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a3dd64`](#insn-00a3dd64) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`00a3dd68`](#insn-00a3dd68) → `0109eea0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a3dd74`](#insn-00a3dd74) → `0109ee98`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a3dd78`](#insn-00a3dd78) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`00a3dd7c`](#insn-00a3dd7c) → `0109eea0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a3dd88`](#insn-00a3dd88) → `0109ee98`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a3dd8c`](#insn-00a3dd8c) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`00a3dd90`](#insn-00a3dd90) → `0109eea0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a3dd9c`](#insn-00a3dd9c) → `0109ee98`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a3dda0`](#insn-00a3dda0) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`00a3dda4`](#insn-00a3dda4) → `0109eea0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a3ddb0`](#insn-00a3ddb0) → `0109ee98`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a3ddb4`](#insn-00a3ddb4) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`00a3ddb8`](#insn-00a3ddb8) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3ddbc`](#insn-00a3ddbc) → [`00a3de38`](#insn-00a3de38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3ddc0`](#insn-00a3ddc0) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3ddc4`](#insn-00a3ddc4) → [`00a3de48`](#insn-00a3de48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3ddc8`](#insn-00a3ddc8) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3ddcc`](#insn-00a3ddcc) → [`00a3de58`](#insn-00a3de58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3ddd0`](#insn-00a3ddd0) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3ddd4`](#insn-00a3ddd4) → [`00a3de68`](#insn-00a3de68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3ddd8`](#insn-00a3ddd8) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3dddc`](#insn-00a3dddc) → [`00a3de78`](#insn-00a3de78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3dde0`](#insn-00a3dde0) → `Stack[-0xf0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3dde4`](#insn-00a3dde4) → [`00a3de88`](#insn-00a3de88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3dde8`](#insn-00a3dde8) → `Stack[-0x110]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3ddec`](#insn-00a3ddec) → [`00a3ddf8`](#insn-00a3ddf8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3ddf0`](#insn-00a3ddf0) → `Stack[-0x100]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3ddf4`](#insn-00a3ddf4) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00a3ddfc`](#insn-00a3ddfc) → [`00418330`](../00418/00418330.md) · `PARAM` · `ANALYSIS` · 関数 `00418330` · 推定シンボル `None` · 推定型 `None`
- [`00a3de04`](#insn-00a3de04) → `0109ee98`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a3de0c`](#insn-00a3de0c) → `00be5fd0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00a3de10`](#insn-00a3de10) → [`00bdafe0`](../00bda/00bdafe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdafe0` · 推定シンボル `None` · 推定型 `None`
- [`00a3de18`](#insn-00a3de18) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3de20`](#insn-00a3de20) → [`00a3df68`](#insn-00a3df68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3de24`](#insn-00a3de24) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3de28`](#insn-00a3de28) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3de2c`](#insn-00a3de2c) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3de38`](#insn-00a3de38) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3de3c`](#insn-00a3de3c) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00a3de40`](#insn-00a3de40) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3de44`](#insn-00a3de44) → [`00a3ddc8`](#insn-00a3ddc8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3de48`](#insn-00a3de48) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3de4c`](#insn-00a3de4c) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00a3de50`](#insn-00a3de50) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3de54`](#insn-00a3de54) → [`00a3ddd0`](#insn-00a3ddd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3de58`](#insn-00a3de58) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3de5c`](#insn-00a3de5c) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00a3de60`](#insn-00a3de60) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3de64`](#insn-00a3de64) → [`00a3ddd8`](#insn-00a3ddd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3de68`](#insn-00a3de68) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3de6c`](#insn-00a3de6c) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00a3de70`](#insn-00a3de70) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3de74`](#insn-00a3de74) → [`00a3dde0`](#insn-00a3dde0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3de78`](#insn-00a3de78) → `Stack[-0xc0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3de7c`](#insn-00a3de7c) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00a3de80`](#insn-00a3de80) → `Stack[-0xf0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3de84`](#insn-00a3de84) → [`00a3dde8`](#insn-00a3dde8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3de88`](#insn-00a3de88) → `Stack[-0xe0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3de8c`](#insn-00a3de8c) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00a3de90`](#insn-00a3de90) → `Stack[-0x110]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3de94`](#insn-00a3de94) → [`00a3ddf0`](#insn-00a3ddf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3de98`](#insn-00a3de98) → [`00a3ddf8`](#insn-00a3ddf8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3df68`](#insn-00a3df68) → [`00bdb090`](../00bdb/00bdb090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb090` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00a3dbe0`](#insn-00a3dbe0)

~~~json
{
  "source": "00a3dbe0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3dbe4`](#insn-00a3dbe4)

~~~json
{
  "source": "00a3dbe4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3dbe8`](#insn-00a3dbe8)

~~~json
{
  "source": "00a3dbe8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3dc0c`](#insn-00a3dc0c)

~~~json
{
  "source": "00a3dc0c",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3dc18`](#insn-00a3dc18)

~~~json
{
  "source": "00a3dc18",
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
- 参照命令 [`00a3dc20`](#insn-00a3dc20)

~~~json
{
  "source": "00a3dc20",
  "target": "Stack[-0xff]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3dc24`](#insn-00a3dc24)

~~~json
{
  "source": "00a3dc24",
  "target": "Stack[-0xf8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3dc34`](#insn-00a3dc34)

~~~json
{
  "source": "00a3dc34",
  "target": "Stack[-0x10f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3dc3c`](#insn-00a3dc3c)

~~~json
{
  "source": "00a3dc3c",
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
- 参照命令 [`00a3dc40`](#insn-00a3dc40)

~~~json
{
  "source": "00a3dc40",
  "target": "Stack[-0xdf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3dc48`](#insn-00a3dc48)

~~~json
{
  "source": "00a3dc48",
  "target": "Stack[-0xd8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3dc58`](#insn-00a3dc58)

~~~json
{
  "source": "00a3dc58",
  "target": "Stack[-0xef]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3dc5c`](#insn-00a3dc5c)

~~~json
{
  "source": "00a3dc5c",
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
- 参照命令 [`00a3dc60`](#insn-00a3dc60)

~~~json
{
  "source": "00a3dc60",
  "target": "Stack[-0xbf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3dc68`](#insn-00a3dc68)

~~~json
{
  "source": "00a3dc68",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3dc78`](#insn-00a3dc78)

~~~json
{
  "source": "00a3dc78",
  "target": "Stack[-0xcf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3dc7c`](#insn-00a3dc7c)

~~~json
{
  "source": "00a3dc7c",
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
- 参照命令 [`00a3dc80`](#insn-00a3dc80)

~~~json
{
  "source": "00a3dc80",
  "target": "Stack[-0x9f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3dc88`](#insn-00a3dc88)

~~~json
{
  "source": "00a3dc88",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3dc94`](#insn-00a3dc94)

~~~json
{
  "source": "00a3dc94",
  "target": "Stack[-0xaf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3dc98`](#insn-00a3dc98)

~~~json
{
  "source": "00a3dc98",
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
- 参照命令 [`00a3dca0`](#insn-00a3dca0)

~~~json
{
  "source": "00a3dca0",
  "target": "Stack[-0x7f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3dca8`](#insn-00a3dca8)

~~~json
{
  "source": "00a3dca8",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3dcb4`](#insn-00a3dcb4)

~~~json
{
  "source": "00a3dcb4",
  "target": "Stack[-0x8f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3dcb8`](#insn-00a3dcb8)

~~~json
{
  "source": "00a3dcb8",
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
- 参照命令 [`00a3dcc0`](#insn-00a3dcc0)

~~~json
{
  "source": "00a3dcc0",
  "target": "Stack[-0x5f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3dcc8`](#insn-00a3dcc8)

~~~json
{
  "source": "00a3dcc8",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3dcd4`](#insn-00a3dcd4)

~~~json
{
  "source": "00a3dcd4",
  "target": "Stack[-0x6f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3dcd8`](#insn-00a3dcd8)

~~~json
{
  "source": "00a3dcd8",
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
- 参照命令 [`00a3dcdc`](#insn-00a3dcdc)

~~~json
{
  "source": "00a3dcdc",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3dce0`](#insn-00a3dce0)

~~~json
{
  "source": "00a3dce0",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3dce4`](#insn-00a3dce4)

~~~json
{
  "source": "00a3dce4",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3dce8`](#insn-00a3dce8)

~~~json
{
  "source": "00a3dce8",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3dcec`](#insn-00a3dcec)

~~~json
{
  "source": "00a3dcec",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3dcf0`](#insn-00a3dcf0)

~~~json
{
  "source": "00a3dcf0",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3dcf4`](#insn-00a3dcf4)

~~~json
{
  "source": "00a3dcf4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3dcfc`](#insn-00a3dcfc)

~~~json
{
  "source": "00a3dcfc",
  "target": "Stack[-0x118]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3dd00`](#insn-00a3dd00)

~~~json
{
  "source": "00a3dd00",
  "target": "Stack[-0xfd]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3dd04`](#insn-00a3dd04)

~~~json
{
  "source": "00a3dd04",
  "target": "Stack[-0xdd]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3dd08`](#insn-00a3dd08)

~~~json
{
  "source": "00a3dd08",
  "target": "Stack[-0xbd]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3dd0c`](#insn-00a3dd0c)

~~~json
{
  "source": "00a3dd0c",
  "target": "Stack[-0x9d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3dd10`](#insn-00a3dd10)

~~~json
{
  "source": "00a3dd10",
  "target": "Stack[-0x7d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3dd14`](#insn-00a3dd14)

~~~json
{
  "source": "00a3dd14",
  "target": "Stack[-0x5d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3dd18`](#insn-00a3dd18)

~~~json
{
  "source": "00a3dd18",
  "target": "Stack[-0x3f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3dd1c`](#insn-00a3dd1c)

~~~json
{
  "source": "00a3dd1c",
  "target": "Stack[-0x4f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3dd20`](#insn-00a3dd20)

~~~json
{
  "source": "00a3dd20",
  "target": "Stack[-0x3d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3dd24`](#insn-00a3dd24)

~~~json
{
  "source": "00a3dd24",
  "target": "0109eea8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109eea8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a3dd28`](#insn-00a3dd28)

~~~json
{
  "source": "00a3dd28",
  "target": "0109eea0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109eea0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a3dd2c`](#insn-00a3dd2c)

~~~json
{
  "source": "00a3dd2c",
  "target": "0109ee98",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109ee98",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a3dd2c`](#insn-00a3dd2c)

~~~json
{
  "source": "00a3dd2c",
  "target": "0109eea0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109eea0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a3dd38`](#insn-00a3dd38)

~~~json
{
  "source": "00a3dd38",
  "target": "0109ee98",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109ee98",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a3dd3c`](#insn-00a3dd3c)

~~~json
{
  "source": "00a3dd3c",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3dd40`](#insn-00a3dd40)

~~~json
{
  "source": "00a3dd40",
  "target": "0109eea0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109eea0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a3dd4c`](#insn-00a3dd4c)

~~~json
{
  "source": "00a3dd4c",
  "target": "0109ee98",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109ee98",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a3dd50`](#insn-00a3dd50)

~~~json
{
  "source": "00a3dd50",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3dd54`](#insn-00a3dd54)

~~~json
{
  "source": "00a3dd54",
  "target": "0109eea0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109eea0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a3dd60`](#insn-00a3dd60)

~~~json
{
  "source": "00a3dd60",
  "target": "0109ee98",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109ee98",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a3dd64`](#insn-00a3dd64)

~~~json
{
  "source": "00a3dd64",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3dd68`](#insn-00a3dd68)

~~~json
{
  "source": "00a3dd68",
  "target": "0109eea0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109eea0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a3dd74`](#insn-00a3dd74)

~~~json
{
  "source": "00a3dd74",
  "target": "0109ee98",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109ee98",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a3dd78`](#insn-00a3dd78)

~~~json
{
  "source": "00a3dd78",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3dd7c`](#insn-00a3dd7c)

~~~json
{
  "source": "00a3dd7c",
  "target": "0109eea0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109eea0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a3dd88`](#insn-00a3dd88)

~~~json
{
  "source": "00a3dd88",
  "target": "0109ee98",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109ee98",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a3dd8c`](#insn-00a3dd8c)

~~~json
{
  "source": "00a3dd8c",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3dd90`](#insn-00a3dd90)

~~~json
{
  "source": "00a3dd90",
  "target": "0109eea0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109eea0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a3dd9c`](#insn-00a3dd9c)

~~~json
{
  "source": "00a3dd9c",
  "target": "0109ee98",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109ee98",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a3dda0`](#insn-00a3dda0)

~~~json
{
  "source": "00a3dda0",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3dda4`](#insn-00a3dda4)

~~~json
{
  "source": "00a3dda4",
  "target": "0109eea0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109eea0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a3ddb0`](#insn-00a3ddb0)

~~~json
{
  "source": "00a3ddb0",
  "target": "0109ee98",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109ee98",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a3ddb4`](#insn-00a3ddb4)

~~~json
{
  "source": "00a3ddb4",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3ddb8`](#insn-00a3ddb8)

~~~json
{
  "source": "00a3ddb8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3ddbc`](#insn-00a3ddbc)

~~~json
{
  "source": "00a3ddbc",
  "target": "00a3de38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3ddc0`](#insn-00a3ddc0)

~~~json
{
  "source": "00a3ddc0",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3ddc4`](#insn-00a3ddc4)

~~~json
{
  "source": "00a3ddc4",
  "target": "00a3de48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3ddc8`](#insn-00a3ddc8)

~~~json
{
  "source": "00a3ddc8",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3ddcc`](#insn-00a3ddcc)

~~~json
{
  "source": "00a3ddcc",
  "target": "00a3de58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3ddd0`](#insn-00a3ddd0)

~~~json
{
  "source": "00a3ddd0",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3ddd4`](#insn-00a3ddd4)

~~~json
{
  "source": "00a3ddd4",
  "target": "00a3de68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3ddd8`](#insn-00a3ddd8)

~~~json
{
  "source": "00a3ddd8",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3dddc`](#insn-00a3dddc)

~~~json
{
  "source": "00a3dddc",
  "target": "00a3de78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3dde0`](#insn-00a3dde0)

~~~json
{
  "source": "00a3dde0",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3dde4`](#insn-00a3dde4)

~~~json
{
  "source": "00a3dde4",
  "target": "00a3de88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3dde8`](#insn-00a3dde8)

~~~json
{
  "source": "00a3dde8",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3ddec`](#insn-00a3ddec)

~~~json
{
  "source": "00a3ddec",
  "target": "00a3ddf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3ddf0`](#insn-00a3ddf0)

~~~json
{
  "source": "00a3ddf0",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3ddf4`](#insn-00a3ddf4)

~~~json
{
  "source": "00a3ddf4",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3ddfc`](#insn-00a3ddfc)

~~~json
{
  "source": "00a3ddfc",
  "target": "00418330",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3de04`](#insn-00a3de04)

~~~json
{
  "source": "00a3de04",
  "target": "0109ee98",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109ee98",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a3de0c`](#insn-00a3de0c)

~~~json
{
  "source": "00a3de0c",
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
- 参照命令 [`00a3de10`](#insn-00a3de10)

~~~json
{
  "source": "00a3de10",
  "target": "00bdafe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3de18`](#insn-00a3de18)

~~~json
{
  "source": "00a3de18",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3de20`](#insn-00a3de20)

~~~json
{
  "source": "00a3de20",
  "target": "00a3df68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3de24`](#insn-00a3de24)

~~~json
{
  "source": "00a3de24",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3de28`](#insn-00a3de28)

~~~json
{
  "source": "00a3de28",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3de2c`](#insn-00a3de2c)

~~~json
{
  "source": "00a3de2c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3de38`](#insn-00a3de38)

~~~json
{
  "source": "00a3de38",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3de3c`](#insn-00a3de3c)

~~~json
{
  "source": "00a3de3c",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3de40`](#insn-00a3de40)

~~~json
{
  "source": "00a3de40",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3de44`](#insn-00a3de44)

~~~json
{
  "source": "00a3de44",
  "target": "00a3ddc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3de48`](#insn-00a3de48)

~~~json
{
  "source": "00a3de48",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3de4c`](#insn-00a3de4c)

~~~json
{
  "source": "00a3de4c",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3de50`](#insn-00a3de50)

~~~json
{
  "source": "00a3de50",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3de54`](#insn-00a3de54)

~~~json
{
  "source": "00a3de54",
  "target": "00a3ddd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3de58`](#insn-00a3de58)

~~~json
{
  "source": "00a3de58",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3de5c`](#insn-00a3de5c)

~~~json
{
  "source": "00a3de5c",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3de60`](#insn-00a3de60)

~~~json
{
  "source": "00a3de60",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3de64`](#insn-00a3de64)

~~~json
{
  "source": "00a3de64",
  "target": "00a3ddd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3de68`](#insn-00a3de68)

~~~json
{
  "source": "00a3de68",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3de6c`](#insn-00a3de6c)

~~~json
{
  "source": "00a3de6c",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3de70`](#insn-00a3de70)

~~~json
{
  "source": "00a3de70",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3de74`](#insn-00a3de74)

~~~json
{
  "source": "00a3de74",
  "target": "00a3dde0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3de78`](#insn-00a3de78)

~~~json
{
  "source": "00a3de78",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3de7c`](#insn-00a3de7c)

~~~json
{
  "source": "00a3de7c",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3de80`](#insn-00a3de80)

~~~json
{
  "source": "00a3de80",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3de84`](#insn-00a3de84)

~~~json
{
  "source": "00a3de84",
  "target": "00a3dde8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3de88`](#insn-00a3de88)

~~~json
{
  "source": "00a3de88",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3de8c`](#insn-00a3de8c)

~~~json
{
  "source": "00a3de8c",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3de90`](#insn-00a3de90)

~~~json
{
  "source": "00a3de90",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3de94`](#insn-00a3de94)

~~~json
{
  "source": "00a3de94",
  "target": "00a3ddf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3de98`](#insn-00a3de98)

~~~json
{
  "source": "00a3de98",
  "target": "00a3ddf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3df68`](#insn-00a3df68)

~~~json
{
  "source": "00a3df68",
  "target": "00bdb090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
