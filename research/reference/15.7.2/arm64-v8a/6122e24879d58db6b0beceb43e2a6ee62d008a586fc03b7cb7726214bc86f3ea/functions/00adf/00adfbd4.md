# 00adfbd4

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00adfc9c`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adf/00adfc9c.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0057.md#compare-70782906235216062f0d645a567b24a7)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00adfbd4",
  "name": "_INIT_268",
  "size": 708,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "caca72796c60144a14ddc0b5c563c05993397282c93f135e8fee388118a85a7f",
  "source_text_sha256": "caca72796c60144a14ddc0b5c563c05993397282c93f135e8fee388118a85a7f",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00adfbd4",
        "00adfe93"
      ],
      [
        "00adff60",
        "00adff63"
      ]
    ],
    "bytes_sha256": "8e87dcf5d83b045c91cd8466bb2e9bfcf5f015862272787a8fb151994ed243bf",
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

## 疑似コード / UTF-8 8791 bytes

~~~c

/* WARNING: Type propagation algorithm not settling */

void _INIT_268(void)

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
  
                    /* catch() { ... } // from try @ 00adf1e4 with catch @ 00adfbe0
                       catch() { ... } // from try @ 00adf2f4 with catch @ 00adfbe0
                       catch() { ... } // from try @ 00adf3f0 with catch @ 00adfbe0
                       try { // try from 00adfbe0 to 00bdfcdf has its CatchHandler @ 00adec0c */
                    /* catch() { ... } // from try @ 00adfb8c with catch @ 00adfbe4 */
                    /* catch() { ... } // from try @ 00adf030 with catch @ 00adfbe8 */
  lVar1 = tpidr_el0;
                    /* catch() { ... } // from try @ 00adf02c with catch @ 00adfbec */
                    /* catch() { ... } // from try @ 00adefdc with catch @ 00adfbf0 */
                    /* catch() { ... } // from try @ 00adef1c with catch @ 00adfbf4 */
  local_38 = *(long *)(lVar1 + 0x28);
                    /* catch() { ... } // from try @ 00adef58 with catch @ 00adfbf8
                       catch() { ... } // from try @ 00adf238 with catch @ 00adfbf8 */
                    /* catch() { ... } // from try @ 00adfb54 with catch @ 00adfbfc
                       catch() { ... } // from try @ 00adfbc0 with catch @ 00adfbfc */
                    /* catch() { ... } // from try @ 00adfb38 with catch @ 00adfc00
                       catch() { ... } // from try @ 00adfb70 with catch @ 00adfc00
                       catch() { ... } // from try @ 00adfba8 with catch @ 00adfc00 */
                    /* catch() { ... } // from try @ 00adf0c8 with catch @ 00adfc04 */
                    /* catch() { ... } // from try @ 00adf5bc with catch @ 00adfc08 */
                    /* catch() { ... } // from try @ 00adfab4 with catch @ 00adfc0c
                       catch() { ... } // from try @ 00adfaec with catch @ 00adfc0c */
                    /* catch() { ... } // from try @ 00adee1c with catch @ 00adfc10 */
                    /* catch() { ... } // from try @ 00adec80 with catch @ 00adfc14
                       catch() { ... } // from try @ 00adfa98 with catch @ 00adfc14 */
  uStack_ff = 0x6741;
  local_f8[0] = 1;
  uStack_107 = (undefined7)s_CgkIjM3y_ZQaEAIQAg_002a72e4._8_8_;
  cStack_100 = SUB81(s_CgkIjM3y_ZQaEAIQAg_002a72e4._8_8_,7);
  local_10f = (char  [8])s_CgkIjM3y_ZQaEAIQAg_002a72e4._0_8_;
                    /* catch() { ... } // from try @ 00adfa80 with catch @ 00adfc30
                       catch() { ... } // from try @ 00adfad0 with catch @ 00adfc30
                       catch() { ... } // from try @ 00adfb20 with catch @ 00adfc30 */
                    /* catch() { ... } // from try @ 00aded74 with catch @ 00adfc34 */
                    /* catch() { ... } // from try @ 00adfa4c with catch @ 00adfc38 */
  uStack_df = 0x4142;
  local_d8[0] = 2;
  uStack_e7 = (undefined7)s_CgkIjM3y_ZQaEAIQBA_002a72f7._8_8_;
  cStack_e0 = SUB81(s_CgkIjM3y_ZQaEAIQBA_002a72f7._8_8_,7);
                    /* catch() { ... } // from try @ 00adfa30 with catch @ 00adfc44
                       catch() { ... } // from try @ 00adfa68 with catch @ 00adfc44 */
  local_ef = (char  [8])s_CgkIjM3y_ZQaEAIQBA_002a72f7._0_8_;
                    /* catch() { ... } // from try @ 00adf9fc with catch @ 00adfc58 */
  uStack_bf = 0x6742;
                    /* catch() { ... } // from try @ 00adf85c with catch @ 00adfc5c */
                    /* catch() { ... } // from try @ 00adf80c with catch @ 00adfc60
                       catch() { ... } // from try @ 00adf894 with catch @ 00adfc60 */
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
                    /* try { // try from 00adfce0 to 00bdfd77 has its CatchHandler @ 00adfce0
                       catch() { ... } // from try @ 00adfce0 with catch @ 00adfce0
                       catch() { ... } // from try @ 00adfd88 with catch @ 00adfce0
                       catch() { ... } // from try @ 00adff44 with catch @ 00adfce0
                       catch() { ... } // from try @ 00ae0334 with catch @ 00adfce0
                       catch() { ... } // from try @ 00ae0410 with catch @ 00adfce0 */
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
  DAT_0109ff40 = 0;
  DAT_0109ff38 = 0;
  DAT_0109ff30 = &DAT_0109ff38;
  FUN_00418cb8(&DAT_0109ff30,&DAT_0109ff38,local_118,local_118);
  FUN_00418cb8(&DAT_0109ff30,&DAT_0109ff38,local_f8,local_f8);
  FUN_00418cb8(&DAT_0109ff30,&DAT_0109ff38,local_d8,local_d8);
  FUN_00418cb8(&DAT_0109ff30,&DAT_0109ff38,local_b8,local_b8);
                    /* try { // try from 00adfd78 to 00bdfd87 has its CatchHandler @ 00ae081c */
  FUN_00418cb8(&DAT_0109ff30,&DAT_0109ff38,local_98,local_98);
                    /* try { // try from 00adfd88 to 00bdfe5f has its CatchHandler @ 00adfce0 */
  FUN_00418cb8(&DAT_0109ff30,&DAT_0109ff38,local_78,local_78);
  FUN_00418cb8(&DAT_0109ff30,&DAT_0109ff38,local_58,local_58);
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
                    /* try { // try from 00adfe60 to 00bdfe6b has its CatchHandler @ 00ae088c */
    _ZdlPv((void *)CONCAT44(uStack_9c,CONCAT13(uStack_9d,CONCAT21(uStack_9f,cStack_a0))));
  }
  if ((local_d0 & 1) != 0) {
    _ZdlPv((void *)CONCAT44(uStack_bc,CONCAT13(uStack_bd,CONCAT21(uStack_bf,cStack_c0))));
  }
                    /* try { // try from 00adfe7c to 00bdfe8b has its CatchHandler @ 00ae06b8 */
  if ((local_f0 & 1) != 0) {
    _ZdlPv((void *)CONCAT44(uStack_dc,CONCAT13(uStack_dd,CONCAT21(uStack_df,cStack_e0))));
                    /* try { // try from 00adfe8c to 00bdfe97 has its CatchHandler @ 00ae069c */
  }
  if ((local_110 & 1) != 0) {
    _ZdlPv((void *)CONCAT44(uStack_fc,CONCAT13(uStack_fd,CONCAT21(uStack_ff,cStack_100))));
  }
  __cxa_atexit(FUN_00418330,&DAT_0109ff30,&PTR_LOOP_00be5ed0);
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
<a id="insn-00adfbd4"></a> `00adfbd4` | `ff 83 04 d1` | sub sp,sp,#0x120 | `FALL_THROUGH`
<a id="insn-00adfbd8"></a> `00adfbd8` | `fd 7b 0f a9` | stp x29,x30,[sp, #0xf0] | `FALL_THROUGH`
<a id="insn-00adfbdc"></a> `00adfbdc` | `fc 57 10 a9` | stp x28,x21,[sp, #0x100] | `FALL_THROUGH`
<a id="insn-00adfbe0"></a> `00adfbe0` | `f4 4f 11 a9` | stp x20,x19,[sp, #0x110] | `FALL_THROUGH`
<a id="insn-00adfbe4"></a> `00adfbe4` | `fd c3 03 91` | add x29,sp,#0xf0 | `FALL_THROUGH`
<a id="insn-00adfbe8"></a> `00adfbe8` | `55 d0 3b d5` | mrs x21,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00adfbec"></a> `00adfbec` | `2a e8 8c 52` | mov w10,#0x6741 | `FALL_THROUGH`
<a id="insn-00adfbf0"></a> `00adfbf0` | `f4 23 00 91` | add x20,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00adfbf4"></a> `00adfbf4` | `a9 16 40 f9` | ldr x9,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00adfbf8"></a> `00adfbf8` | `88 04 80 52` | mov w8,#0x24 | `FALL_THROUGH`
<a id="insn-00adfbfc"></a> `00adfbfc` | `13 2e 00 90` | adrp x19,0x109f000 | `FALL_THROUGH`
<a id="insn-00adfc00"></a> `00adfc00` | `73 c2 3c 91` | add x19,x19,#0xf30 | `FALL_THROUGH`
<a id="insn-00adfc04"></a> `00adfc04` | `a9 83 1f f8` | stur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00adfc08"></a> `00adfc08` | `49 be ff 90` | adrp x9,0x2a7000 | `FALL_THROUGH`
<a id="insn-00adfc0c"></a> `00adfc0c` | `29 91 0b 91` | add x9,x9,#0x2e4 | `FALL_THROUGH`
<a id="insn-00adfc10"></a> `00adfc10` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00adfc14"></a> `00adfc14` | `29 00 80 52` | mov w9,#0x1 | `FALL_THROUGH`
<a id="insn-00adfc18"></a> `00adfc18` | `ea 13 02 78` | sturh w10,[sp, #0x21] | `FALL_THROUGH`
<a id="insn-00adfc1c"></a> `00adfc1c` | `e9 2b 00 b9` | str w9,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00adfc20"></a> `00adfc20` | `49 28 88 52` | mov w9,#0x4142 | `FALL_THROUGH`
<a id="insn-00adfc24"></a> `00adfc24` | `4a be ff 90` | adrp x10,0x2a7000 | `FALL_THROUGH`
<a id="insn-00adfc28"></a> `00adfc28` | `4a dd 0b 91` | add x10,x10,#0x2f7 | `FALL_THROUGH`
<a id="insn-00adfc2c"></a> `00adfc2c` | `e0 13 81 3c` | stur q0,[sp, #0x11] | `FALL_THROUGH`
<a id="insn-00adfc30"></a> `00adfc30` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00adfc34"></a> `00adfc34` | `40 01 c0 3d` | ldr q0,[x10] | `FALL_THROUGH`
<a id="insn-00adfc38"></a> `00adfc38` | `e9 13 04 78` | sturh w9,[sp, #0x41] | `FALL_THROUGH`
<a id="insn-00adfc3c"></a> `00adfc3c` | `49 00 80 52` | mov w9,#0x2 | `FALL_THROUGH`
<a id="insn-00adfc40"></a> `00adfc40` | `e9 4b 00 b9` | str w9,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00adfc44"></a> `00adfc44` | `49 e8 8c 52` | mov w9,#0x6742 | `FALL_THROUGH`
<a id="insn-00adfc48"></a> `00adfc48` | `4a be ff b0` | adrp x10,0x2a8000 | `FALL_THROUGH`
<a id="insn-00adfc4c"></a> `00adfc4c` | `4a 69 03 91` | add x10,x10,#0xda | `FALL_THROUGH`
<a id="insn-00adfc50"></a> `00adfc50` | `e0 13 83 3c` | stur q0,[sp, #0x31] | `FALL_THROUGH`
<a id="insn-00adfc54"></a> `00adfc54` | `40 01 c0 3d` | ldr q0,[x10] | `FALL_THROUGH`
<a id="insn-00adfc58"></a> `00adfc58` | `e9 13 06 78` | sturh w9,[sp, #0x61] | `FALL_THROUGH`
<a id="insn-00adfc5c"></a> `00adfc5c` | `69 00 80 52` | mov w9,#0x3 | `FALL_THROUGH`
<a id="insn-00adfc60"></a> `00adfc60` | `e9 6b 00 b9` | str w9,[sp, #0x68] | `FALL_THROUGH`
<a id="insn-00adfc64"></a> `00adfc64` | `29 e8 8e 52` | mov w9,#0x7741 | `FALL_THROUGH`
<a id="insn-00adfc68"></a> `00adfc68` | `aa bd ff 90` | adrp x10,0x293000 | `FALL_THROUGH`
<a id="insn-00adfc6c"></a> `00adfc6c` | `4a b9 1a 91` | add x10,x10,#0x6ae | `FALL_THROUGH`
<a id="insn-00adfc70"></a> `00adfc70` | `e0 13 85 3c` | stur q0,[sp, #0x51] | `FALL_THROUGH`
<a id="insn-00adfc74"></a> `00adfc74` | `40 01 c0 3d` | ldr q0,[x10] | `FALL_THROUGH`
<a id="insn-00adfc78"></a> `00adfc78` | `e9 13 08 78` | sturh w9,[sp, #0x81] | `FALL_THROUGH`
<a id="insn-00adfc7c"></a> `00adfc7c` | `89 00 80 52` | mov w9,#0x4 | `FALL_THROUGH`
<a id="insn-00adfc80"></a> `00adfc80` | `e9 8b 00 b9` | str w9,[sp, #0x88] | `FALL_THROUGH`
<a id="insn-00adfc84"></a> `00adfc84` | `e9 bd ff b0` | adrp x9,0x29c000 | `FALL_THROUGH`
<a id="insn-00adfc88"></a> `00adfc88` | `29 85 0b 91` | add x9,x9,#0x2e1 | `FALL_THROUGH`
<a id="insn-00adfc8c"></a> `00adfc8c` | `e0 13 87 3c` | stur q0,[sp, #0x71] | `FALL_THROUGH`
<a id="insn-00adfc90"></a> `00adfc90` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00adfc94"></a> `00adfc94` | `49 28 8a 52` | mov w9,#0x5142 | `FALL_THROUGH`
<a id="insn-00adfc98"></a> `00adfc98` | `89 92 09 78` | sturh w9,[x20, #0x99] | `FALL_THROUGH`
<a id="insn-00adfc9c"></a> `00adfc9c` | `a9 00 80 52` | mov w9,#0x5 | `FALL_THROUGH`
<a id="insn-00adfca0"></a> `00adfca0` | `e9 ab 00 b9` | str w9,[sp, #0xa8] | `FALL_THROUGH`
<a id="insn-00adfca4"></a> `00adfca4` | `89 bd ff d0` | adrp x9,0x291000 | `FALL_THROUGH`
<a id="insn-00adfca8"></a> `00adfca8` | `29 dd 21 91` | add x9,x9,#0x877 | `FALL_THROUGH`
<a id="insn-00adfcac"></a> `00adfcac` | `80 92 88 3c` | stur q0,[x20, #0x89] | `FALL_THROUGH`
<a id="insn-00adfcb0"></a> `00adfcb0` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00adfcb4"></a> `00adfcb4` | `49 e8 8e 52` | mov w9,#0x7742 | `FALL_THROUGH`
<a id="insn-00adfcb8"></a> `00adfcb8` | `89 92 0b 78` | sturh w9,[x20, #0xb9] | `FALL_THROUGH`
<a id="insn-00adfcbc"></a> `00adfcbc` | `c9 00 80 52` | mov w9,#0x6 | `FALL_THROUGH`
<a id="insn-00adfcc0"></a> `00adfcc0` | `e9 cb 00 b9` | str w9,[sp, #0xc8] | `FALL_THROUGH`
<a id="insn-00adfcc4"></a> `00adfcc4` | `a9 bd ff b0` | adrp x9,0x294000 | `FALL_THROUGH`
<a id="insn-00adfcc8"></a> `00adfcc8` | `29 99 14 91` | add x9,x9,#0x526 | `FALL_THROUGH`
<a id="insn-00adfccc"></a> `00adfccc` | `80 92 8a 3c` | stur q0,[x20, #0xa9] | `FALL_THROUGH`
<a id="insn-00adfcd0"></a> `00adfcd0` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00adfcd4"></a> `00adfcd4` | `e8 43 00 39` | strb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00adfcd8"></a> `00adfcd8` | `e8 c3 00 39` | strb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00adfcdc"></a> `00adfcdc` | `e8 43 01 39` | strb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00adfce0"></a> `00adfce0` | `e8 c3 01 39` | strb w8,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00adfce4"></a> `00adfce4` | `e8 43 02 39` | strb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00adfce8"></a> `00adfce8` | `e8 c3 02 39` | strb w8,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00adfcec"></a> `00adfcec` | `e8 43 03 39` | strb w8,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-00adfcf0"></a> `00adfcf0` | `68 28 88 52` | mov w8,#0x4143 | `FALL_THROUGH`
<a id="insn-00adfcf4"></a> `00adfcf4` | `ff 0b 00 b9` | str wzr,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00adfcf8"></a> `00adfcf8` | `ff 8f 00 39` | strb wzr,[sp, #0x23] | `FALL_THROUGH`
<a id="insn-00adfcfc"></a> `00adfcfc` | `ff 0f 01 39` | strb wzr,[sp, #0x43] | `FALL_THROUGH`
<a id="insn-00adfd00"></a> `00adfd00` | `ff 8f 01 39` | strb wzr,[sp, #0x63] | `FALL_THROUGH`
<a id="insn-00adfd04"></a> `00adfd04` | `ff 0f 02 39` | strb wzr,[sp, #0x83] | `FALL_THROUGH`
<a id="insn-00adfd08"></a> `00adfd08` | `ff 8f 02 39` | strb wzr,[sp, #0xa3] | `FALL_THROUGH`
<a id="insn-00adfd0c"></a> `00adfd0c` | `ff 0f 03 39` | strb wzr,[sp, #0xc3] | `FALL_THROUGH`
<a id="insn-00adfd10"></a> `00adfd10` | `88 92 0d 78` | sturh w8,[x20, #0xd9] | `FALL_THROUGH`
<a id="insn-00adfd14"></a> `00adfd14` | `80 92 8c 3c` | stur q0,[x20, #0xc9] | `FALL_THROUGH`
<a id="insn-00adfd18"></a> `00adfd18` | `ff 8f 03 39` | strb wzr,[sp, #0xe3] | `FALL_THROUGH`
<a id="insn-00adfd1c"></a> `00adfd1c` | `7f 0a 00 f9` | str xzr,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00adfd20"></a> `00adfd20` | `3f 8c 00 f8` | str xzr,[x1, #0x8]! | `FALL_THROUGH`
<a id="insn-00adfd24"></a> `00adfd24` | `61 02 00 f9` | str x1,[x19] | `FALL_THROUGH`
<a id="insn-00adfd28"></a> `00adfd28` | `e2 23 00 91` | add x2,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00adfd2c"></a> `00adfd2c` | `e3 23 00 91` | add x3,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00adfd30"></a> `00adfd30` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00adfd34"></a> `00adfd34` | `e1 e3 e4 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-00adfd38"></a> `00adfd38` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00adfd3c"></a> `00adfd3c` | `82 82 00 91` | add x2,x20,#0x20 | `FALL_THROUGH`
<a id="insn-00adfd40"></a> `00adfd40` | `83 82 00 91` | add x3,x20,#0x20 | `FALL_THROUGH`
<a id="insn-00adfd44"></a> `00adfd44` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00adfd48"></a> `00adfd48` | `dc e3 e4 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-00adfd4c"></a> `00adfd4c` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00adfd50"></a> `00adfd50` | `82 02 01 91` | add x2,x20,#0x40 | `FALL_THROUGH`
<a id="insn-00adfd54"></a> `00adfd54` | `83 02 01 91` | add x3,x20,#0x40 | `FALL_THROUGH`
<a id="insn-00adfd58"></a> `00adfd58` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00adfd5c"></a> `00adfd5c` | `d7 e3 e4 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-00adfd60"></a> `00adfd60` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00adfd64"></a> `00adfd64` | `82 82 01 91` | add x2,x20,#0x60 | `FALL_THROUGH`
<a id="insn-00adfd68"></a> `00adfd68` | `83 82 01 91` | add x3,x20,#0x60 | `FALL_THROUGH`
<a id="insn-00adfd6c"></a> `00adfd6c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00adfd70"></a> `00adfd70` | `d2 e3 e4 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-00adfd74"></a> `00adfd74` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00adfd78"></a> `00adfd78` | `82 02 02 91` | add x2,x20,#0x80 | `FALL_THROUGH`
<a id="insn-00adfd7c"></a> `00adfd7c` | `83 02 02 91` | add x3,x20,#0x80 | `FALL_THROUGH`
<a id="insn-00adfd80"></a> `00adfd80` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00adfd84"></a> `00adfd84` | `cd e3 e4 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-00adfd88"></a> `00adfd88` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00adfd8c"></a> `00adfd8c` | `82 82 02 91` | add x2,x20,#0xa0 | `FALL_THROUGH`
<a id="insn-00adfd90"></a> `00adfd90` | `83 82 02 91` | add x3,x20,#0xa0 | `FALL_THROUGH`
<a id="insn-00adfd94"></a> `00adfd94` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00adfd98"></a> `00adfd98` | `c8 e3 e4 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-00adfd9c"></a> `00adfd9c` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00adfda0"></a> `00adfda0` | `82 02 03 91` | add x2,x20,#0xc0 | `FALL_THROUGH`
<a id="insn-00adfda4"></a> `00adfda4` | `83 02 03 91` | add x3,x20,#0xc0 | `FALL_THROUGH`
<a id="insn-00adfda8"></a> `00adfda8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00adfdac"></a> `00adfdac` | `c3 e3 e4 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-00adfdb0"></a> `00adfdb0` | `e8 43 43 39` | ldrb w8,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-00adfdb4"></a> `00adfdb4` | `e8 03 00 37` | tbnz w8,#0x0,0x00adfe30 | `CONDITIONAL_JUMP`
<a id="insn-00adfdb8"></a> `00adfdb8` | `e8 c3 42 39` | ldrb w8,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00adfdbc"></a> `00adfdbc` | `28 04 00 37` | tbnz w8,#0x0,0x00adfe40 | `CONDITIONAL_JUMP`
<a id="insn-00adfdc0"></a> `00adfdc0` | `e8 43 42 39` | ldrb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00adfdc4"></a> `00adfdc4` | `68 04 00 37` | tbnz w8,#0x0,0x00adfe50 | `CONDITIONAL_JUMP`
<a id="insn-00adfdc8"></a> `00adfdc8` | `e8 c3 41 39` | ldrb w8,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00adfdcc"></a> `00adfdcc` | `a8 04 00 37` | tbnz w8,#0x0,0x00adfe60 | `CONDITIONAL_JUMP`
<a id="insn-00adfdd0"></a> `00adfdd0` | `e8 43 41 39` | ldrb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00adfdd4"></a> `00adfdd4` | `e8 04 00 37` | tbnz w8,#0x0,0x00adfe70 | `CONDITIONAL_JUMP`
<a id="insn-00adfdd8"></a> `00adfdd8` | `e8 c3 40 39` | ldrb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00adfddc"></a> `00adfddc` | `28 05 00 37` | tbnz w8,#0x0,0x00adfe80 | `CONDITIONAL_JUMP`
<a id="insn-00adfde0"></a> `00adfde0` | `e8 43 40 39` | ldrb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00adfde4"></a> `00adfde4` | `68 00 00 36` | tbz w8,#0x0,0x00adfdf0 | `CONDITIONAL_JUMP`
<a id="insn-00adfde8"></a> `00adfde8` | `e0 13 40 f9` | ldr x0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00adfdec"></a> `00adfdec` | `5d ec 03 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00adfdf0"></a> `00adfdf0` | `c0 c9 ff b0` | adrp x0,0x418000 | `FALL_THROUGH`
<a id="insn-00adfdf4"></a> `00adfdf4` | `00 c0 0c 91` | add x0,x0,#0x330 | `FALL_THROUGH`
<a id="insn-00adfdf8"></a> `00adfdf8` | `01 2e 00 90` | adrp x1,0x109f000 | `FALL_THROUGH`
<a id="insn-00adfdfc"></a> `00adfdfc` | `21 c0 3c 91` | add x1,x1,#0xf30 | `FALL_THROUGH`
<a id="insn-00adfe00"></a> `00adfe00` | `22 08 00 d0` | adrp x2,0xbe5000 | `FALL_THROUGH`
<a id="insn-00adfe04"></a> `00adfe04` | `42 40 3b 91` | add x2,x2,#0xed0 | `FALL_THROUGH`
<a id="insn-00adfe08"></a> `00adfe08` | `36 ec 03 94` | bl 0x00bdaee0 | `UNCONDITIONAL_CALL`
<a id="insn-00adfe0c"></a> `00adfe0c` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00adfe10"></a> `00adfe10` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00adfe14"></a> `00adfe14` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00adfe18"></a> `00adfe18` | `41 0a 00 54` | b.ne 0x00adff60 | `CONDITIONAL_JUMP`
<a id="insn-00adfe1c"></a> `00adfe1c` | `f4 4f 51 a9` | ldp x20,x19,[sp, #0x110] | `FALL_THROUGH`
<a id="insn-00adfe20"></a> `00adfe20` | `fc 57 50 a9` | ldp x28,x21,[sp, #0x100] | `FALL_THROUGH`
<a id="insn-00adfe24"></a> `00adfe24` | `fd 7b 4f a9` | ldp x29,x30,[sp, #0xf0] | `FALL_THROUGH`
<a id="insn-00adfe28"></a> `00adfe28` | `ff 83 04 91` | add sp,sp,#0x120 | `FALL_THROUGH`
<a id="insn-00adfe2c"></a> `00adfe2c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00adfe30"></a> `00adfe30` | `e0 73 40 f9` | ldr x0,[sp, #0xe0] | `FALL_THROUGH`
<a id="insn-00adfe34"></a> `00adfe34` | `4b ec 03 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00adfe38"></a> `00adfe38` | `e8 c3 42 39` | ldrb w8,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00adfe3c"></a> `00adfe3c` | `28 fc 07 36` | tbz w8,#0x0,0x00adfdc0 | `CONDITIONAL_JUMP`
<a id="insn-00adfe40"></a> `00adfe40` | `e0 63 40 f9` | ldr x0,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00adfe44"></a> `00adfe44` | `47 ec 03 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00adfe48"></a> `00adfe48` | `e8 43 42 39` | ldrb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00adfe4c"></a> `00adfe4c` | `e8 fb 07 36` | tbz w8,#0x0,0x00adfdc8 | `CONDITIONAL_JUMP`
<a id="insn-00adfe50"></a> `00adfe50` | `e0 53 40 f9` | ldr x0,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00adfe54"></a> `00adfe54` | `43 ec 03 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00adfe58"></a> `00adfe58` | `e8 c3 41 39` | ldrb w8,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00adfe5c"></a> `00adfe5c` | `a8 fb 07 36` | tbz w8,#0x0,0x00adfdd0 | `CONDITIONAL_JUMP`
<a id="insn-00adfe60"></a> `00adfe60` | `e0 43 40 f9` | ldr x0,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00adfe64"></a> `00adfe64` | `3f ec 03 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00adfe68"></a> `00adfe68` | `e8 43 41 39` | ldrb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00adfe6c"></a> `00adfe6c` | `68 fb 07 36` | tbz w8,#0x0,0x00adfdd8 | `CONDITIONAL_JUMP`
<a id="insn-00adfe70"></a> `00adfe70` | `e0 33 40 f9` | ldr x0,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00adfe74"></a> `00adfe74` | `3b ec 03 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00adfe78"></a> `00adfe78` | `e8 c3 40 39` | ldrb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00adfe7c"></a> `00adfe7c` | `28 fb 07 36` | tbz w8,#0x0,0x00adfde0 | `CONDITIONAL_JUMP`
<a id="insn-00adfe80"></a> `00adfe80` | `e0 23 40 f9` | ldr x0,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00adfe84"></a> `00adfe84` | `37 ec 03 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00adfe88"></a> `00adfe88` | `e8 43 40 39` | ldrb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00adfe8c"></a> `00adfe8c` | `e8 fa 07 37` | tbnz w8,#0x0,0x00adfde8 | `CONDITIONAL_JUMP`
<a id="insn-00adfe90"></a> `00adfe90` | `d8 ff ff 17` | b 0x00adfdf0 | `UNCONDITIONAL_JUMP`
<a id="insn-00adff60"></a> `00adff60` | `0c ec 03 94` | bl 0x00bdaf90 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00adfbd4`](#insn-00adfbd4) 範囲 `[['00adfbd4', '00adfbdf']]`
  - `FALL_THROUGH` [`00adfbdc`](#insn-00adfbdc) → [`00adfbe0`](#insn-00adfbe0)
- ブロック [`00adfbe0`](#insn-00adfbe0) 範囲 `[['00adfbe0', '00adfbe3']]`
  - `FALL_THROUGH` [`00adfbe0`](#insn-00adfbe0) → [`00adfbe4`](#insn-00adfbe4)
- ブロック [`00adfbe4`](#insn-00adfbe4) 範囲 `[['00adfbe4', '00adfbe7']]`
  - `FALL_THROUGH` [`00adfbe4`](#insn-00adfbe4) → [`00adfbe8`](#insn-00adfbe8)
- ブロック [`00adfbe8`](#insn-00adfbe8) 範囲 `[['00adfbe8', '00adfbeb']]`
  - `FALL_THROUGH` [`00adfbe8`](#insn-00adfbe8) → [`00adfbec`](#insn-00adfbec)
- ブロック [`00adfbec`](#insn-00adfbec) 範囲 `[['00adfbec', '00adfbef']]`
  - `FALL_THROUGH` [`00adfbec`](#insn-00adfbec) → [`00adfbf0`](#insn-00adfbf0)
- ブロック [`00adfbf0`](#insn-00adfbf0) 範囲 `[['00adfbf0', '00adfbf3']]`
  - `FALL_THROUGH` [`00adfbf0`](#insn-00adfbf0) → [`00adfbf4`](#insn-00adfbf4)
- ブロック [`00adfbf4`](#insn-00adfbf4) 範囲 `[['00adfbf4', '00adfbf7']]`
  - `FALL_THROUGH` [`00adfbf4`](#insn-00adfbf4) → [`00adfbf8`](#insn-00adfbf8)
- ブロック [`00adfbf8`](#insn-00adfbf8) 範囲 `[['00adfbf8', '00adfbfb']]`
  - `FALL_THROUGH` [`00adfbf8`](#insn-00adfbf8) → [`00adfbfc`](#insn-00adfbfc)
- ブロック [`00adfbfc`](#insn-00adfbfc) 範囲 `[['00adfbfc', '00adfbff']]`
  - `FALL_THROUGH` [`00adfbfc`](#insn-00adfbfc) → [`00adfc00`](#insn-00adfc00)
- ブロック [`00adfc00`](#insn-00adfc00) 範囲 `[['00adfc00', '00adfc03']]`
  - `FALL_THROUGH` [`00adfc00`](#insn-00adfc00) → [`00adfc04`](#insn-00adfc04)
- ブロック [`00adfc04`](#insn-00adfc04) 範囲 `[['00adfc04', '00adfc07']]`
  - `FALL_THROUGH` [`00adfc04`](#insn-00adfc04) → [`00adfc08`](#insn-00adfc08)
- ブロック [`00adfc08`](#insn-00adfc08) 範囲 `[['00adfc08', '00adfc0b']]`
  - `FALL_THROUGH` [`00adfc08`](#insn-00adfc08) → [`00adfc0c`](#insn-00adfc0c)
- ブロック [`00adfc0c`](#insn-00adfc0c) 範囲 `[['00adfc0c', '00adfc0f']]`
  - `FALL_THROUGH` [`00adfc0c`](#insn-00adfc0c) → [`00adfc10`](#insn-00adfc10)
- ブロック [`00adfc10`](#insn-00adfc10) 範囲 `[['00adfc10', '00adfc13']]`
  - `FALL_THROUGH` [`00adfc10`](#insn-00adfc10) → [`00adfc14`](#insn-00adfc14)
- ブロック [`00adfc14`](#insn-00adfc14) 範囲 `[['00adfc14', '00adfc2f']]`
  - `FALL_THROUGH` [`00adfc2c`](#insn-00adfc2c) → [`00adfc30`](#insn-00adfc30)
- ブロック [`00adfc30`](#insn-00adfc30) 範囲 `[['00adfc30', '00adfc33']]`
  - `FALL_THROUGH` [`00adfc30`](#insn-00adfc30) → [`00adfc34`](#insn-00adfc34)
- ブロック [`00adfc34`](#insn-00adfc34) 範囲 `[['00adfc34', '00adfc37']]`
  - `FALL_THROUGH` [`00adfc34`](#insn-00adfc34) → [`00adfc38`](#insn-00adfc38)
- ブロック [`00adfc38`](#insn-00adfc38) 範囲 `[['00adfc38', '00adfc43']]`
  - `FALL_THROUGH` [`00adfc40`](#insn-00adfc40) → [`00adfc44`](#insn-00adfc44)
- ブロック [`00adfc44`](#insn-00adfc44) 範囲 `[['00adfc44', '00adfc57']]`
  - `FALL_THROUGH` [`00adfc54`](#insn-00adfc54) → [`00adfc58`](#insn-00adfc58)
- ブロック [`00adfc58`](#insn-00adfc58) 範囲 `[['00adfc58', '00adfc5b']]`
  - `FALL_THROUGH` [`00adfc58`](#insn-00adfc58) → [`00adfc5c`](#insn-00adfc5c)
- ブロック [`00adfc5c`](#insn-00adfc5c) 範囲 `[['00adfc5c', '00adfc5f']]`
  - `FALL_THROUGH` [`00adfc5c`](#insn-00adfc5c) → [`00adfc60`](#insn-00adfc60)
- ブロック [`00adfc60`](#insn-00adfc60) 範囲 `[['00adfc60', '00adfcdf']]`
  - `FALL_THROUGH` [`00adfcdc`](#insn-00adfcdc) → [`00adfce0`](#insn-00adfce0)
- ブロック [`00adfce0`](#insn-00adfce0) 範囲 `[['00adfce0', '00adfd77']]`
  - `FALL_THROUGH` [`00adfd74`](#insn-00adfd74) → [`00adfd78`](#insn-00adfd78)
- ブロック [`00adfd78`](#insn-00adfd78) 範囲 `[['00adfd78', '00adfd87']]`
  - `FALL_THROUGH` [`00adfd84`](#insn-00adfd84) → [`00adfd88`](#insn-00adfd88)
- ブロック [`00adfd88`](#insn-00adfd88) 範囲 `[['00adfd88', '00adfdb7']]`
  - `CONDITIONAL_JUMP` [`00adfdb4`](#insn-00adfdb4) → [`00adfe30`](#insn-00adfe30)
  - `FALL_THROUGH` [`00adfdb4`](#insn-00adfdb4) → [`00adfdb8`](#insn-00adfdb8)
- ブロック [`00adfdb8`](#insn-00adfdb8) 範囲 `[['00adfdb8', '00adfdbf']]`
  - `CONDITIONAL_JUMP` [`00adfdbc`](#insn-00adfdbc) → [`00adfe40`](#insn-00adfe40)
  - `FALL_THROUGH` [`00adfdbc`](#insn-00adfdbc) → [`00adfdc0`](#insn-00adfdc0)
- ブロック [`00adfdc0`](#insn-00adfdc0) 範囲 `[['00adfdc0', '00adfdc7']]`
  - `CONDITIONAL_JUMP` [`00adfdc4`](#insn-00adfdc4) → [`00adfe50`](#insn-00adfe50)
  - `FALL_THROUGH` [`00adfdc4`](#insn-00adfdc4) → [`00adfdc8`](#insn-00adfdc8)
- ブロック [`00adfdc8`](#insn-00adfdc8) 範囲 `[['00adfdc8', '00adfdcf']]`
  - `CONDITIONAL_JUMP` [`00adfdcc`](#insn-00adfdcc) → [`00adfe60`](#insn-00adfe60)
  - `FALL_THROUGH` [`00adfdcc`](#insn-00adfdcc) → [`00adfdd0`](#insn-00adfdd0)
- ブロック [`00adfdd0`](#insn-00adfdd0) 範囲 `[['00adfdd0', '00adfdd7']]`
  - `CONDITIONAL_JUMP` [`00adfdd4`](#insn-00adfdd4) → [`00adfe70`](#insn-00adfe70)
  - `FALL_THROUGH` [`00adfdd4`](#insn-00adfdd4) → [`00adfdd8`](#insn-00adfdd8)
- ブロック [`00adfdd8`](#insn-00adfdd8) 範囲 `[['00adfdd8', '00adfddf']]`
  - `CONDITIONAL_JUMP` [`00adfddc`](#insn-00adfddc) → [`00adfe80`](#insn-00adfe80)
  - `FALL_THROUGH` [`00adfddc`](#insn-00adfddc) → [`00adfde0`](#insn-00adfde0)
- ブロック [`00adfde0`](#insn-00adfde0) 範囲 `[['00adfde0', '00adfde7']]`
  - `CONDITIONAL_JUMP` [`00adfde4`](#insn-00adfde4) → [`00adfdf0`](#insn-00adfdf0)
  - `FALL_THROUGH` [`00adfde4`](#insn-00adfde4) → [`00adfde8`](#insn-00adfde8)
- ブロック [`00adfde8`](#insn-00adfde8) 範囲 `[['00adfde8', '00adfdef']]`
  - `FALL_THROUGH` [`00adfdec`](#insn-00adfdec) → [`00adfdf0`](#insn-00adfdf0)
- ブロック [`00adfdf0`](#insn-00adfdf0) 範囲 `[['00adfdf0', '00adfe1b']]`
  - `CONDITIONAL_JUMP` [`00adfe18`](#insn-00adfe18) → [`00adff60`](#insn-00adff60)
  - `FALL_THROUGH` [`00adfe18`](#insn-00adfe18) → [`00adfe1c`](#insn-00adfe1c)
- ブロック [`00adfe1c`](#insn-00adfe1c) 範囲 `[['00adfe1c', '00adfe2f']]`
- ブロック [`00adfe30`](#insn-00adfe30) 範囲 `[['00adfe30', '00adfe3f']]`
  - `CONDITIONAL_JUMP` [`00adfe3c`](#insn-00adfe3c) → [`00adfdc0`](#insn-00adfdc0)
  - `FALL_THROUGH` [`00adfe3c`](#insn-00adfe3c) → [`00adfe40`](#insn-00adfe40)
- ブロック [`00adfe40`](#insn-00adfe40) 範囲 `[['00adfe40', '00adfe4f']]`
  - `CONDITIONAL_JUMP` [`00adfe4c`](#insn-00adfe4c) → [`00adfdc8`](#insn-00adfdc8)
  - `FALL_THROUGH` [`00adfe4c`](#insn-00adfe4c) → [`00adfe50`](#insn-00adfe50)
- ブロック [`00adfe50`](#insn-00adfe50) 範囲 `[['00adfe50', '00adfe5f']]`
  - `CONDITIONAL_JUMP` [`00adfe5c`](#insn-00adfe5c) → [`00adfdd0`](#insn-00adfdd0)
  - `FALL_THROUGH` [`00adfe5c`](#insn-00adfe5c) → [`00adfe60`](#insn-00adfe60)
- ブロック [`00adfe60`](#insn-00adfe60) 範囲 `[['00adfe60', '00adfe6f']]`
  - `CONDITIONAL_JUMP` [`00adfe6c`](#insn-00adfe6c) → [`00adfdd8`](#insn-00adfdd8)
  - `FALL_THROUGH` [`00adfe6c`](#insn-00adfe6c) → [`00adfe70`](#insn-00adfe70)
- ブロック [`00adfe70`](#insn-00adfe70) 範囲 `[['00adfe70', '00adfe7b']]`
  - `FALL_THROUGH` [`00adfe78`](#insn-00adfe78) → [`00adfe7c`](#insn-00adfe7c)
- ブロック [`00adfe7c`](#insn-00adfe7c) 範囲 `[['00adfe7c', '00adfe7f']]`
  - `CONDITIONAL_JUMP` [`00adfe7c`](#insn-00adfe7c) → [`00adfde0`](#insn-00adfde0)
  - `FALL_THROUGH` [`00adfe7c`](#insn-00adfe7c) → [`00adfe80`](#insn-00adfe80)
- ブロック [`00adfe80`](#insn-00adfe80) 範囲 `[['00adfe80', '00adfe8b']]`
  - `FALL_THROUGH` [`00adfe88`](#insn-00adfe88) → [`00adfe8c`](#insn-00adfe8c)
- ブロック [`00adfe8c`](#insn-00adfe8c) 範囲 `[['00adfe8c', '00adfe8f']]`
  - `CONDITIONAL_JUMP` [`00adfe8c`](#insn-00adfe8c) → [`00adfde8`](#insn-00adfde8)
  - `FALL_THROUGH` [`00adfe8c`](#insn-00adfe8c) → [`00adfe90`](#insn-00adfe90)
- ブロック [`00adfe90`](#insn-00adfe90) 範囲 `[['00adfe90', '00adfe93']]`
  - `UNCONDITIONAL_JUMP` [`00adfe90`](#insn-00adfe90) → [`00adfdf0`](#insn-00adfdf0)
- ブロック [`00adff60`](#insn-00adff60) 範囲 `[['00adff60', '00adff63']]`

## 命令位置別の参照

- [`00adfbd8`](#insn-00adfbd8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfbdc`](#insn-00adfbdc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfbe0`](#insn-00adfbe0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfc04`](#insn-00adfc04) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfc10`](#insn-00adfc10) → `002a72e4`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00adfc18`](#insn-00adfc18) → `Stack[-0xff]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfc1c`](#insn-00adfc1c) → `Stack[-0xf8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfc2c`](#insn-00adfc2c) → `Stack[-0x10f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfc34`](#insn-00adfc34) → `002a72f7`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00adfc38`](#insn-00adfc38) → `Stack[-0xdf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfc40`](#insn-00adfc40) → `Stack[-0xd8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfc50`](#insn-00adfc50) → `Stack[-0xef]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfc54`](#insn-00adfc54) → `002a80da`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00adfc58`](#insn-00adfc58) → `Stack[-0xbf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfc60`](#insn-00adfc60) → `Stack[-0xb8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfc70`](#insn-00adfc70) → `Stack[-0xcf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfc74`](#insn-00adfc74) → `002936ae`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00adfc78`](#insn-00adfc78) → `Stack[-0x9f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfc80`](#insn-00adfc80) → `Stack[-0x98]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfc8c`](#insn-00adfc8c) → `Stack[-0xaf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfc90`](#insn-00adfc90) → `0029c2e1`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00adfc98`](#insn-00adfc98) → `Stack[-0x7f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfca0`](#insn-00adfca0) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfcac`](#insn-00adfcac) → `Stack[-0x8f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfcb0`](#insn-00adfcb0) → `00291877`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00adfcb8`](#insn-00adfcb8) → `Stack[-0x5f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfcc0`](#insn-00adfcc0) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfccc`](#insn-00adfccc) → `Stack[-0x6f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfcd0`](#insn-00adfcd0) → `00294526`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00adfcd4`](#insn-00adfcd4) → `Stack[-0x110]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfcd8`](#insn-00adfcd8) → `Stack[-0xf0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfcdc`](#insn-00adfcdc) → `Stack[-0xd0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfce0`](#insn-00adfce0) → `Stack[-0xb0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfce4`](#insn-00adfce4) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfce8`](#insn-00adfce8) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfcec`](#insn-00adfcec) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfcf4`](#insn-00adfcf4) → `Stack[-0x118]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfcf8`](#insn-00adfcf8) → `Stack[-0xfd]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfcfc`](#insn-00adfcfc) → `Stack[-0xdd]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfd00`](#insn-00adfd00) → `Stack[-0xbd]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfd04`](#insn-00adfd04) → `Stack[-0x9d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfd08`](#insn-00adfd08) → `Stack[-0x7d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfd0c`](#insn-00adfd0c) → `Stack[-0x5d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfd10`](#insn-00adfd10) → `Stack[-0x3f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfd14`](#insn-00adfd14) → `Stack[-0x4f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfd18`](#insn-00adfd18) → `Stack[-0x3d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfd1c`](#insn-00adfd1c) → `0109ff40`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adfd20`](#insn-00adfd20) → `0109ff38`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adfd24`](#insn-00adfd24) → `0109ff30`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adfd24`](#insn-00adfd24) → `0109ff38`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adfd30`](#insn-00adfd30) → `0109ff30`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adfd34`](#insn-00adfd34) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`00adfd38`](#insn-00adfd38) → `0109ff38`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adfd44`](#insn-00adfd44) → `0109ff30`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adfd48`](#insn-00adfd48) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`00adfd4c`](#insn-00adfd4c) → `0109ff38`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adfd58`](#insn-00adfd58) → `0109ff30`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adfd5c`](#insn-00adfd5c) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`00adfd60`](#insn-00adfd60) → `0109ff38`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adfd6c`](#insn-00adfd6c) → `0109ff30`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adfd70`](#insn-00adfd70) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`00adfd74`](#insn-00adfd74) → `0109ff38`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adfd80`](#insn-00adfd80) → `0109ff30`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adfd84`](#insn-00adfd84) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`00adfd88`](#insn-00adfd88) → `0109ff38`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adfd94`](#insn-00adfd94) → `0109ff30`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adfd98`](#insn-00adfd98) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`00adfd9c`](#insn-00adfd9c) → `0109ff38`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adfda8`](#insn-00adfda8) → `0109ff30`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adfdac`](#insn-00adfdac) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`00adfdb0`](#insn-00adfdb0) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfdb4`](#insn-00adfdb4) → [`00adfe30`](#insn-00adfe30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfdb8`](#insn-00adfdb8) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfdbc`](#insn-00adfdbc) → [`00adfe40`](#insn-00adfe40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfdc0`](#insn-00adfdc0) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfdc4`](#insn-00adfdc4) → [`00adfe50`](#insn-00adfe50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfdc8`](#insn-00adfdc8) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfdcc`](#insn-00adfdcc) → [`00adfe60`](#insn-00adfe60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfdd0`](#insn-00adfdd0) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfdd4`](#insn-00adfdd4) → [`00adfe70`](#insn-00adfe70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfdd8`](#insn-00adfdd8) → `Stack[-0xf0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfddc`](#insn-00adfddc) → [`00adfe80`](#insn-00adfe80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfde0`](#insn-00adfde0) → `Stack[-0x110]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfde4`](#insn-00adfde4) → [`00adfdf0`](#insn-00adfdf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfde8`](#insn-00adfde8) → `Stack[-0x100]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfdec`](#insn-00adfdec) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00adfdf4`](#insn-00adfdf4) → [`00418330`](../00418/00418330.md) · `PARAM` · `ANALYSIS` · 関数 `00418330` · 推定シンボル `None` · 推定型 `None`
- [`00adfdfc`](#insn-00adfdfc) → `0109ff30`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adfe04`](#insn-00adfe04) → `00be5ed0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00adfe08`](#insn-00adfe08) → [`00bdaee0`](../00bda/00bdaee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaee0` · 推定シンボル `None` · 推定型 `None`
- [`00adfe10`](#insn-00adfe10) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfe18`](#insn-00adfe18) → [`00adff60`](#insn-00adff60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfe1c`](#insn-00adfe1c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfe20`](#insn-00adfe20) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfe24`](#insn-00adfe24) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfe30`](#insn-00adfe30) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfe34`](#insn-00adfe34) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00adfe38`](#insn-00adfe38) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfe3c`](#insn-00adfe3c) → [`00adfdc0`](#insn-00adfdc0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfe40`](#insn-00adfe40) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfe44`](#insn-00adfe44) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00adfe48`](#insn-00adfe48) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfe4c`](#insn-00adfe4c) → [`00adfdc8`](#insn-00adfdc8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfe50`](#insn-00adfe50) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfe54`](#insn-00adfe54) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00adfe58`](#insn-00adfe58) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfe5c`](#insn-00adfe5c) → [`00adfdd0`](#insn-00adfdd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfe60`](#insn-00adfe60) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfe64`](#insn-00adfe64) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00adfe68`](#insn-00adfe68) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfe6c`](#insn-00adfe6c) → [`00adfdd8`](#insn-00adfdd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfe70`](#insn-00adfe70) → `Stack[-0xc0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfe74`](#insn-00adfe74) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00adfe78`](#insn-00adfe78) → `Stack[-0xf0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfe7c`](#insn-00adfe7c) → [`00adfde0`](#insn-00adfde0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfe80`](#insn-00adfe80) → `Stack[-0xe0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfe84`](#insn-00adfe84) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00adfe88`](#insn-00adfe88) → `Stack[-0x110]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfe8c`](#insn-00adfe8c) → [`00adfde8`](#insn-00adfde8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfe90`](#insn-00adfe90) → [`00adfdf0`](#insn-00adfdf0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adff60`](#insn-00adff60) → [`00bdaf90`](../00bda/00bdaf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf90` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00adfbd8`](#insn-00adfbd8)

~~~json
{
  "source": "00adfbd8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfbdc`](#insn-00adfbdc)

~~~json
{
  "source": "00adfbdc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfbe0`](#insn-00adfbe0)

~~~json
{
  "source": "00adfbe0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfc04`](#insn-00adfc04)

~~~json
{
  "source": "00adfc04",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfc10`](#insn-00adfc10)

~~~json
{
  "source": "00adfc10",
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
- 参照命令 [`00adfc18`](#insn-00adfc18)

~~~json
{
  "source": "00adfc18",
  "target": "Stack[-0xff]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfc1c`](#insn-00adfc1c)

~~~json
{
  "source": "00adfc1c",
  "target": "Stack[-0xf8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfc2c`](#insn-00adfc2c)

~~~json
{
  "source": "00adfc2c",
  "target": "Stack[-0x10f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfc34`](#insn-00adfc34)

~~~json
{
  "source": "00adfc34",
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
- 参照命令 [`00adfc38`](#insn-00adfc38)

~~~json
{
  "source": "00adfc38",
  "target": "Stack[-0xdf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfc40`](#insn-00adfc40)

~~~json
{
  "source": "00adfc40",
  "target": "Stack[-0xd8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfc50`](#insn-00adfc50)

~~~json
{
  "source": "00adfc50",
  "target": "Stack[-0xef]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfc54`](#insn-00adfc54)

~~~json
{
  "source": "00adfc54",
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
- 参照命令 [`00adfc58`](#insn-00adfc58)

~~~json
{
  "source": "00adfc58",
  "target": "Stack[-0xbf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfc60`](#insn-00adfc60)

~~~json
{
  "source": "00adfc60",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfc70`](#insn-00adfc70)

~~~json
{
  "source": "00adfc70",
  "target": "Stack[-0xcf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfc74`](#insn-00adfc74)

~~~json
{
  "source": "00adfc74",
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
- 参照命令 [`00adfc78`](#insn-00adfc78)

~~~json
{
  "source": "00adfc78",
  "target": "Stack[-0x9f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfc80`](#insn-00adfc80)

~~~json
{
  "source": "00adfc80",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfc8c`](#insn-00adfc8c)

~~~json
{
  "source": "00adfc8c",
  "target": "Stack[-0xaf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfc90`](#insn-00adfc90)

~~~json
{
  "source": "00adfc90",
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
- 参照命令 [`00adfc98`](#insn-00adfc98)

~~~json
{
  "source": "00adfc98",
  "target": "Stack[-0x7f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfca0`](#insn-00adfca0)

~~~json
{
  "source": "00adfca0",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfcac`](#insn-00adfcac)

~~~json
{
  "source": "00adfcac",
  "target": "Stack[-0x8f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfcb0`](#insn-00adfcb0)

~~~json
{
  "source": "00adfcb0",
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
- 参照命令 [`00adfcb8`](#insn-00adfcb8)

~~~json
{
  "source": "00adfcb8",
  "target": "Stack[-0x5f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfcc0`](#insn-00adfcc0)

~~~json
{
  "source": "00adfcc0",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfccc`](#insn-00adfccc)

~~~json
{
  "source": "00adfccc",
  "target": "Stack[-0x6f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfcd0`](#insn-00adfcd0)

~~~json
{
  "source": "00adfcd0",
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
- 参照命令 [`00adfcd4`](#insn-00adfcd4)

~~~json
{
  "source": "00adfcd4",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfcd8`](#insn-00adfcd8)

~~~json
{
  "source": "00adfcd8",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfcdc`](#insn-00adfcdc)

~~~json
{
  "source": "00adfcdc",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfce0`](#insn-00adfce0)

~~~json
{
  "source": "00adfce0",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfce4`](#insn-00adfce4)

~~~json
{
  "source": "00adfce4",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfce8`](#insn-00adfce8)

~~~json
{
  "source": "00adfce8",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfcec`](#insn-00adfcec)

~~~json
{
  "source": "00adfcec",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfcf4`](#insn-00adfcf4)

~~~json
{
  "source": "00adfcf4",
  "target": "Stack[-0x118]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfcf8`](#insn-00adfcf8)

~~~json
{
  "source": "00adfcf8",
  "target": "Stack[-0xfd]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfcfc`](#insn-00adfcfc)

~~~json
{
  "source": "00adfcfc",
  "target": "Stack[-0xdd]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfd00`](#insn-00adfd00)

~~~json
{
  "source": "00adfd00",
  "target": "Stack[-0xbd]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfd04`](#insn-00adfd04)

~~~json
{
  "source": "00adfd04",
  "target": "Stack[-0x9d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfd08`](#insn-00adfd08)

~~~json
{
  "source": "00adfd08",
  "target": "Stack[-0x7d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfd0c`](#insn-00adfd0c)

~~~json
{
  "source": "00adfd0c",
  "target": "Stack[-0x5d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfd10`](#insn-00adfd10)

~~~json
{
  "source": "00adfd10",
  "target": "Stack[-0x3f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfd14`](#insn-00adfd14)

~~~json
{
  "source": "00adfd14",
  "target": "Stack[-0x4f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfd18`](#insn-00adfd18)

~~~json
{
  "source": "00adfd18",
  "target": "Stack[-0x3d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfd1c`](#insn-00adfd1c)

~~~json
{
  "source": "00adfd1c",
  "target": "0109ff40",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109ff40",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adfd20`](#insn-00adfd20)

~~~json
{
  "source": "00adfd20",
  "target": "0109ff38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109ff38",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adfd24`](#insn-00adfd24)

~~~json
{
  "source": "00adfd24",
  "target": "0109ff30",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109ff30",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adfd24`](#insn-00adfd24)

~~~json
{
  "source": "00adfd24",
  "target": "0109ff38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109ff38",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adfd30`](#insn-00adfd30)

~~~json
{
  "source": "00adfd30",
  "target": "0109ff30",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109ff30",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adfd34`](#insn-00adfd34)

~~~json
{
  "source": "00adfd34",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adfd38`](#insn-00adfd38)

~~~json
{
  "source": "00adfd38",
  "target": "0109ff38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109ff38",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adfd44`](#insn-00adfd44)

~~~json
{
  "source": "00adfd44",
  "target": "0109ff30",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109ff30",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adfd48`](#insn-00adfd48)

~~~json
{
  "source": "00adfd48",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adfd4c`](#insn-00adfd4c)

~~~json
{
  "source": "00adfd4c",
  "target": "0109ff38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109ff38",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adfd58`](#insn-00adfd58)

~~~json
{
  "source": "00adfd58",
  "target": "0109ff30",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109ff30",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adfd5c`](#insn-00adfd5c)

~~~json
{
  "source": "00adfd5c",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adfd60`](#insn-00adfd60)

~~~json
{
  "source": "00adfd60",
  "target": "0109ff38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109ff38",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adfd6c`](#insn-00adfd6c)

~~~json
{
  "source": "00adfd6c",
  "target": "0109ff30",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109ff30",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adfd70`](#insn-00adfd70)

~~~json
{
  "source": "00adfd70",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adfd74`](#insn-00adfd74)

~~~json
{
  "source": "00adfd74",
  "target": "0109ff38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109ff38",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adfd80`](#insn-00adfd80)

~~~json
{
  "source": "00adfd80",
  "target": "0109ff30",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109ff30",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adfd84`](#insn-00adfd84)

~~~json
{
  "source": "00adfd84",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adfd88`](#insn-00adfd88)

~~~json
{
  "source": "00adfd88",
  "target": "0109ff38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109ff38",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adfd94`](#insn-00adfd94)

~~~json
{
  "source": "00adfd94",
  "target": "0109ff30",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109ff30",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adfd98`](#insn-00adfd98)

~~~json
{
  "source": "00adfd98",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adfd9c`](#insn-00adfd9c)

~~~json
{
  "source": "00adfd9c",
  "target": "0109ff38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109ff38",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adfda8`](#insn-00adfda8)

~~~json
{
  "source": "00adfda8",
  "target": "0109ff30",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109ff30",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adfdac`](#insn-00adfdac)

~~~json
{
  "source": "00adfdac",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adfdb0`](#insn-00adfdb0)

~~~json
{
  "source": "00adfdb0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfdb4`](#insn-00adfdb4)

~~~json
{
  "source": "00adfdb4",
  "target": "00adfe30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfdb8`](#insn-00adfdb8)

~~~json
{
  "source": "00adfdb8",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfdbc`](#insn-00adfdbc)

~~~json
{
  "source": "00adfdbc",
  "target": "00adfe40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfdc0`](#insn-00adfdc0)

~~~json
{
  "source": "00adfdc0",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfdc4`](#insn-00adfdc4)

~~~json
{
  "source": "00adfdc4",
  "target": "00adfe50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfdc8`](#insn-00adfdc8)

~~~json
{
  "source": "00adfdc8",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfdcc`](#insn-00adfdcc)

~~~json
{
  "source": "00adfdcc",
  "target": "00adfe60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfdd0`](#insn-00adfdd0)

~~~json
{
  "source": "00adfdd0",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfdd4`](#insn-00adfdd4)

~~~json
{
  "source": "00adfdd4",
  "target": "00adfe70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfdd8`](#insn-00adfdd8)

~~~json
{
  "source": "00adfdd8",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfddc`](#insn-00adfddc)

~~~json
{
  "source": "00adfddc",
  "target": "00adfe80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfde0`](#insn-00adfde0)

~~~json
{
  "source": "00adfde0",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfde4`](#insn-00adfde4)

~~~json
{
  "source": "00adfde4",
  "target": "00adfdf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfde8`](#insn-00adfde8)

~~~json
{
  "source": "00adfde8",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfdec`](#insn-00adfdec)

~~~json
{
  "source": "00adfdec",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adfdf4`](#insn-00adfdf4)

~~~json
{
  "source": "00adfdf4",
  "target": "00418330",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adfdfc`](#insn-00adfdfc)

~~~json
{
  "source": "00adfdfc",
  "target": "0109ff30",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109ff30",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adfe04`](#insn-00adfe04)

~~~json
{
  "source": "00adfe04",
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
- 参照命令 [`00adfe08`](#insn-00adfe08)

~~~json
{
  "source": "00adfe08",
  "target": "00bdaee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adfe10`](#insn-00adfe10)

~~~json
{
  "source": "00adfe10",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfe18`](#insn-00adfe18)

~~~json
{
  "source": "00adfe18",
  "target": "00adff60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfe1c`](#insn-00adfe1c)

~~~json
{
  "source": "00adfe1c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfe20`](#insn-00adfe20)

~~~json
{
  "source": "00adfe20",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfe24`](#insn-00adfe24)

~~~json
{
  "source": "00adfe24",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfe30`](#insn-00adfe30)

~~~json
{
  "source": "00adfe30",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfe34`](#insn-00adfe34)

~~~json
{
  "source": "00adfe34",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adfe38`](#insn-00adfe38)

~~~json
{
  "source": "00adfe38",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfe3c`](#insn-00adfe3c)

~~~json
{
  "source": "00adfe3c",
  "target": "00adfdc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfe40`](#insn-00adfe40)

~~~json
{
  "source": "00adfe40",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfe44`](#insn-00adfe44)

~~~json
{
  "source": "00adfe44",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adfe48`](#insn-00adfe48)

~~~json
{
  "source": "00adfe48",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfe4c`](#insn-00adfe4c)

~~~json
{
  "source": "00adfe4c",
  "target": "00adfdc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfe50`](#insn-00adfe50)

~~~json
{
  "source": "00adfe50",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfe54`](#insn-00adfe54)

~~~json
{
  "source": "00adfe54",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adfe58`](#insn-00adfe58)

~~~json
{
  "source": "00adfe58",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfe5c`](#insn-00adfe5c)

~~~json
{
  "source": "00adfe5c",
  "target": "00adfdd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfe60`](#insn-00adfe60)

~~~json
{
  "source": "00adfe60",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfe64`](#insn-00adfe64)

~~~json
{
  "source": "00adfe64",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adfe68`](#insn-00adfe68)

~~~json
{
  "source": "00adfe68",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfe6c`](#insn-00adfe6c)

~~~json
{
  "source": "00adfe6c",
  "target": "00adfdd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfe70`](#insn-00adfe70)

~~~json
{
  "source": "00adfe70",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfe74`](#insn-00adfe74)

~~~json
{
  "source": "00adfe74",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adfe78`](#insn-00adfe78)

~~~json
{
  "source": "00adfe78",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfe7c`](#insn-00adfe7c)

~~~json
{
  "source": "00adfe7c",
  "target": "00adfde0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfe80`](#insn-00adfe80)

~~~json
{
  "source": "00adfe80",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfe84`](#insn-00adfe84)

~~~json
{
  "source": "00adfe84",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adfe88`](#insn-00adfe88)

~~~json
{
  "source": "00adfe88",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfe8c`](#insn-00adfe8c)

~~~json
{
  "source": "00adfe8c",
  "target": "00adfde8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfe90`](#insn-00adfe90)

~~~json
{
  "source": "00adfe90",
  "target": "00adfdf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adff60`](#insn-00adff60)

~~~json
{
  "source": "00adff60",
  "target": "00bdaf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
