# 00adbbe4

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00adbb1c`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00adb/00adbb1c.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0057.md#compare-910496dd272d8ae56a237c6c7db9d801)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00adbc28`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adbc28.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0060.md#compare-d52ae83f40e7a0fcef65928b7fd11b9b)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00adbbe4",
  "name": "_INIT_265",
  "size": 876,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4665fd88495f3201414a798970dcdd773f6628635a1fbb79cf0f9a1b42449499",
  "source_text_sha256": "4665fd88495f3201414a798970dcdd773f6628635a1fbb79cf0f9a1b42449499",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00adbbe4",
        "00adbf4b"
      ],
      [
        "00adc018",
        "00adc01b"
      ]
    ],
    "bytes_sha256": "4b5ed9643f1c35fa4ce0962128f8d397b1a73cb1c0ef66f15bb9d0819eb72589",
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

## 疑似コード / UTF-8 5925 bytes

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
                    /* try { // try from 00adbd20 to 00bdbe6f has its CatchHandler @ 00adbd20
                       catch() { ... } // from try @ 00adbd20 with catch @ 00adbd20
                       catch() { ... } // from try @ 00adbe7c with catch @ 00adbd20 */
  uStack_3f = 0x4143;
  uStack_47 = (undefined7)s_CgkIjM3y_ZQaEAIQCA_002945b3._8_8_;
  cStack_40 = SUB81(s_CgkIjM3y_ZQaEAIQCA_002945b3._8_8_,7);
  local_4f = (char  [8])s_CgkIjM3y_ZQaEAIQCA_002945b3._0_8_;
  uStack_3d = 0;
  DAT_0109fef0 = 0;
  DAT_0109fee8 = 0;
  DAT_0109fee0 = &DAT_0109fee8;
  FUN_00418cb8(&DAT_0109fee0,&DAT_0109fee8,local_118,local_118);
  FUN_00418cb8(&DAT_0109fee0,&DAT_0109fee8,local_f8,local_f8);
  FUN_00418cb8(&DAT_0109fee0,&DAT_0109fee8,local_d8,local_d8);
  FUN_00418cb8(&DAT_0109fee0,&DAT_0109fee8,local_b8,local_b8);
  FUN_00418cb8(&DAT_0109fee0,&DAT_0109fee8,local_98,local_98);
  FUN_00418cb8(&DAT_0109fee0,&DAT_0109fee8,local_78,local_78);
  FUN_00418cb8(&DAT_0109fee0,&DAT_0109fee8,local_58,local_58);
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
                    /* catch() { ... } // from try @ 00adbe70 with catch @ 00adbf18 */
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
  __cxa_atexit(FUN_00418330,&DAT_0109fee0,&PTR_LOOP_00be5f80);
  DAT_0109ff08 = 0;
  DAT_0109ff00 = 0;
  DAT_0109fef8 = &DAT_0109ff00;
  __cxa_atexit(FUN_00ad90c4,&DAT_0109fef8,&PTR_LOOP_00be5f80);
  DAT_0109ff20 = 0;
  DAT_0109ff18 = 0;
  DAT_0109ff10 = &DAT_0109ff18;
  __cxa_atexit(FUN_00ad90cc,&DAT_0109ff10,&PTR_LOOP_00be5f80);
                    /* try { // try from 00adbe70 to 00bdbe7b has its CatchHandler @ 00adbf18 */
                    /* try { // try from 00adbe7c to 00bdbf3f has its CatchHandler @ 00adbd20 */
  DAT_0109ff50 = 0;
  __cxa_atexit(FUN_00569da8,&DAT_0109ff30,&PTR_LOOP_00be5f80);
  DAT_0109ff80 = 0;
  __cxa_atexit(FUN_0085e2f8,&DAT_0109ff60,&PTR_LOOP_00be5f80);
  DAT_0109ffb0 = 0;
  __cxa_atexit(FUN_0085e2f8,&DAT_0109ff90,&PTR_LOOP_00be5f80);
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
<a id="insn-00adbbe4"></a> `00adbbe4` | `ff 83 04 d1` | sub sp,sp,#0x120 | `FALL_THROUGH`
<a id="insn-00adbbe8"></a> `00adbbe8` | `fd 7b 0f a9` | stp x29,x30,[sp, #0xf0] | `FALL_THROUGH`
<a id="insn-00adbbec"></a> `00adbbec` | `fc 57 10 a9` | stp x28,x21,[sp, #0x100] | `FALL_THROUGH`
<a id="insn-00adbbf0"></a> `00adbbf0` | `f4 4f 11 a9` | stp x20,x19,[sp, #0x110] | `FALL_THROUGH`
<a id="insn-00adbbf4"></a> `00adbbf4` | `fd c3 03 91` | add x29,sp,#0xf0 | `FALL_THROUGH`
<a id="insn-00adbbf8"></a> `00adbbf8` | `55 d0 3b d5` | mrs x21,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00adbbfc"></a> `00adbbfc` | `2a e8 8c 52` | mov w10,#0x6741 | `FALL_THROUGH`
<a id="insn-00adbc00"></a> `00adbc00` | `f4 23 00 91` | add x20,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00adbc04"></a> `00adbc04` | `a9 16 40 f9` | ldr x9,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00adbc08"></a> `00adbc08` | `88 04 80 52` | mov w8,#0x24 | `FALL_THROUGH`
<a id="insn-00adbc0c"></a> `00adbc0c` | `33 2e 00 90` | adrp x19,0x109f000 | `FALL_THROUGH`
<a id="insn-00adbc10"></a> `00adbc10` | `73 82 3b 91` | add x19,x19,#0xee0 | `FALL_THROUGH`
<a id="insn-00adbc14"></a> `00adbc14` | `a9 83 1f f8` | stur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00adbc18"></a> `00adbc18` | `69 be ff 90` | adrp x9,0x2a7000 | `FALL_THROUGH`
<a id="insn-00adbc1c"></a> `00adbc1c` | `29 75 0b 91` | add x9,x9,#0x2dd | `FALL_THROUGH`
<a id="insn-00adbc20"></a> `00adbc20` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00adbc24"></a> `00adbc24` | `29 00 80 52` | mov w9,#0x1 | `FALL_THROUGH`
<a id="insn-00adbc28"></a> `00adbc28` | `ea 13 02 78` | sturh w10,[sp, #0x21] | `FALL_THROUGH`
<a id="insn-00adbc2c"></a> `00adbc2c` | `e9 2b 00 b9` | str w9,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00adbc30"></a> `00adbc30` | `49 28 88 52` | mov w9,#0x4142 | `FALL_THROUGH`
<a id="insn-00adbc34"></a> `00adbc34` | `6a be ff 90` | adrp x10,0x2a7000 | `FALL_THROUGH`
<a id="insn-00adbc38"></a> `00adbc38` | `4a c1 0b 91` | add x10,x10,#0x2f0 | `FALL_THROUGH`
<a id="insn-00adbc3c"></a> `00adbc3c` | `e0 13 81 3c` | stur q0,[sp, #0x11] | `FALL_THROUGH`
<a id="insn-00adbc40"></a> `00adbc40` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00adbc44"></a> `00adbc44` | `40 01 c0 3d` | ldr q0,[x10] | `FALL_THROUGH`
<a id="insn-00adbc48"></a> `00adbc48` | `e9 13 04 78` | sturh w9,[sp, #0x41] | `FALL_THROUGH`
<a id="insn-00adbc4c"></a> `00adbc4c` | `49 00 80 52` | mov w9,#0x2 | `FALL_THROUGH`
<a id="insn-00adbc50"></a> `00adbc50` | `e9 4b 00 b9` | str w9,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00adbc54"></a> `00adbc54` | `49 e8 8c 52` | mov w9,#0x6742 | `FALL_THROUGH`
<a id="insn-00adbc58"></a> `00adbc58` | `6a be ff b0` | adrp x10,0x2a8000 | `FALL_THROUGH`
<a id="insn-00adbc5c"></a> `00adbc5c` | `4a 19 01 91` | add x10,x10,#0x46 | `FALL_THROUGH`
<a id="insn-00adbc60"></a> `00adbc60` | `e0 13 83 3c` | stur q0,[sp, #0x31] | `FALL_THROUGH`
<a id="insn-00adbc64"></a> `00adbc64` | `40 01 c0 3d` | ldr q0,[x10] | `FALL_THROUGH`
<a id="insn-00adbc68"></a> `00adbc68` | `e9 13 06 78` | sturh w9,[sp, #0x61] | `FALL_THROUGH`
<a id="insn-00adbc6c"></a> `00adbc6c` | `69 00 80 52` | mov w9,#0x3 | `FALL_THROUGH`
<a id="insn-00adbc70"></a> `00adbc70` | `e9 6b 00 b9` | str w9,[sp, #0x68] | `FALL_THROUGH`
<a id="insn-00adbc74"></a> `00adbc74` | `29 e8 8e 52` | mov w9,#0x7741 | `FALL_THROUGH`
<a id="insn-00adbc78"></a> `00adbc78` | `ca bd ff 90` | adrp x10,0x293000 | `FALL_THROUGH`
<a id="insn-00adbc7c"></a> `00adbc7c` | `4a ed 1c 91` | add x10,x10,#0x73b | `FALL_THROUGH`
<a id="insn-00adbc80"></a> `00adbc80` | `e0 13 85 3c` | stur q0,[sp, #0x51] | `FALL_THROUGH`
<a id="insn-00adbc84"></a> `00adbc84` | `40 01 c0 3d` | ldr q0,[x10] | `FALL_THROUGH`
<a id="insn-00adbc88"></a> `00adbc88` | `e9 13 08 78` | sturh w9,[sp, #0x81] | `FALL_THROUGH`
<a id="insn-00adbc8c"></a> `00adbc8c` | `89 00 80 52` | mov w9,#0x4 | `FALL_THROUGH`
<a id="insn-00adbc90"></a> `00adbc90` | `e9 8b 00 b9` | str w9,[sp, #0x88] | `FALL_THROUGH`
<a id="insn-00adbc94"></a> `00adbc94` | `09 be ff b0` | adrp x9,0x29c000 | `FALL_THROUGH`
<a id="insn-00adbc98"></a> `00adbc98` | `29 b9 0d 91` | add x9,x9,#0x36e | `FALL_THROUGH`
<a id="insn-00adbc9c"></a> `00adbc9c` | `e0 13 87 3c` | stur q0,[sp, #0x71] | `FALL_THROUGH`
<a id="insn-00adbca0"></a> `00adbca0` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00adbca4"></a> `00adbca4` | `49 28 8a 52` | mov w9,#0x5142 | `FALL_THROUGH`
<a id="insn-00adbca8"></a> `00adbca8` | `89 92 09 78` | sturh w9,[x20, #0x99] | `FALL_THROUGH`
<a id="insn-00adbcac"></a> `00adbcac` | `a9 00 80 52` | mov w9,#0x5 | `FALL_THROUGH`
<a id="insn-00adbcb0"></a> `00adbcb0` | `e9 ab 00 b9` | str w9,[sp, #0xa8] | `FALL_THROUGH`
<a id="insn-00adbcb4"></a> `00adbcb4` | `a9 bd ff d0` | adrp x9,0x291000 | `FALL_THROUGH`
<a id="insn-00adbcb8"></a> `00adbcb8` | `29 dd 21 91` | add x9,x9,#0x877 | `FALL_THROUGH`
<a id="insn-00adbcbc"></a> `00adbcbc` | `80 92 88 3c` | stur q0,[x20, #0x89] | `FALL_THROUGH`
<a id="insn-00adbcc0"></a> `00adbcc0` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00adbcc4"></a> `00adbcc4` | `49 e8 8e 52` | mov w9,#0x7742 | `FALL_THROUGH`
<a id="insn-00adbcc8"></a> `00adbcc8` | `89 92 0b 78` | sturh w9,[x20, #0xb9] | `FALL_THROUGH`
<a id="insn-00adbccc"></a> `00adbccc` | `c9 00 80 52` | mov w9,#0x6 | `FALL_THROUGH`
<a id="insn-00adbcd0"></a> `00adbcd0` | `e9 cb 00 b9` | str w9,[sp, #0xc8] | `FALL_THROUGH`
<a id="insn-00adbcd4"></a> `00adbcd4` | `c9 bd ff b0` | adrp x9,0x294000 | `FALL_THROUGH`
<a id="insn-00adbcd8"></a> `00adbcd8` | `29 cd 16 91` | add x9,x9,#0x5b3 | `FALL_THROUGH`
<a id="insn-00adbcdc"></a> `00adbcdc` | `80 92 8a 3c` | stur q0,[x20, #0xa9] | `FALL_THROUGH`
<a id="insn-00adbce0"></a> `00adbce0` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00adbce4"></a> `00adbce4` | `e8 43 00 39` | strb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00adbce8"></a> `00adbce8` | `e8 c3 00 39` | strb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00adbcec"></a> `00adbcec` | `e8 43 01 39` | strb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00adbcf0"></a> `00adbcf0` | `e8 c3 01 39` | strb w8,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00adbcf4"></a> `00adbcf4` | `e8 43 02 39` | strb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00adbcf8"></a> `00adbcf8` | `e8 c3 02 39` | strb w8,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00adbcfc"></a> `00adbcfc` | `e8 43 03 39` | strb w8,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-00adbd00"></a> `00adbd00` | `68 28 88 52` | mov w8,#0x4143 | `FALL_THROUGH`
<a id="insn-00adbd04"></a> `00adbd04` | `ff 0b 00 b9` | str wzr,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00adbd08"></a> `00adbd08` | `ff 8f 00 39` | strb wzr,[sp, #0x23] | `FALL_THROUGH`
<a id="insn-00adbd0c"></a> `00adbd0c` | `ff 0f 01 39` | strb wzr,[sp, #0x43] | `FALL_THROUGH`
<a id="insn-00adbd10"></a> `00adbd10` | `ff 8f 01 39` | strb wzr,[sp, #0x63] | `FALL_THROUGH`
<a id="insn-00adbd14"></a> `00adbd14` | `ff 0f 02 39` | strb wzr,[sp, #0x83] | `FALL_THROUGH`
<a id="insn-00adbd18"></a> `00adbd18` | `ff 8f 02 39` | strb wzr,[sp, #0xa3] | `FALL_THROUGH`
<a id="insn-00adbd1c"></a> `00adbd1c` | `ff 0f 03 39` | strb wzr,[sp, #0xc3] | `FALL_THROUGH`
<a id="insn-00adbd20"></a> `00adbd20` | `88 92 0d 78` | sturh w8,[x20, #0xd9] | `FALL_THROUGH`
<a id="insn-00adbd24"></a> `00adbd24` | `80 92 8c 3c` | stur q0,[x20, #0xc9] | `FALL_THROUGH`
<a id="insn-00adbd28"></a> `00adbd28` | `ff 8f 03 39` | strb wzr,[sp, #0xe3] | `FALL_THROUGH`
<a id="insn-00adbd2c"></a> `00adbd2c` | `7f 0a 00 f9` | str xzr,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00adbd30"></a> `00adbd30` | `3f 8c 00 f8` | str xzr,[x1, #0x8]! | `FALL_THROUGH`
<a id="insn-00adbd34"></a> `00adbd34` | `61 02 00 f9` | str x1,[x19] | `FALL_THROUGH`
<a id="insn-00adbd38"></a> `00adbd38` | `e2 23 00 91` | add x2,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00adbd3c"></a> `00adbd3c` | `e3 23 00 91` | add x3,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00adbd40"></a> `00adbd40` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00adbd44"></a> `00adbd44` | `dd f3 e4 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-00adbd48"></a> `00adbd48` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00adbd4c"></a> `00adbd4c` | `82 82 00 91` | add x2,x20,#0x20 | `FALL_THROUGH`
<a id="insn-00adbd50"></a> `00adbd50` | `83 82 00 91` | add x3,x20,#0x20 | `FALL_THROUGH`
<a id="insn-00adbd54"></a> `00adbd54` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00adbd58"></a> `00adbd58` | `d8 f3 e4 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-00adbd5c"></a> `00adbd5c` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00adbd60"></a> `00adbd60` | `82 02 01 91` | add x2,x20,#0x40 | `FALL_THROUGH`
<a id="insn-00adbd64"></a> `00adbd64` | `83 02 01 91` | add x3,x20,#0x40 | `FALL_THROUGH`
<a id="insn-00adbd68"></a> `00adbd68` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00adbd6c"></a> `00adbd6c` | `d3 f3 e4 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-00adbd70"></a> `00adbd70` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00adbd74"></a> `00adbd74` | `82 82 01 91` | add x2,x20,#0x60 | `FALL_THROUGH`
<a id="insn-00adbd78"></a> `00adbd78` | `83 82 01 91` | add x3,x20,#0x60 | `FALL_THROUGH`
<a id="insn-00adbd7c"></a> `00adbd7c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00adbd80"></a> `00adbd80` | `ce f3 e4 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-00adbd84"></a> `00adbd84` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00adbd88"></a> `00adbd88` | `82 02 02 91` | add x2,x20,#0x80 | `FALL_THROUGH`
<a id="insn-00adbd8c"></a> `00adbd8c` | `83 02 02 91` | add x3,x20,#0x80 | `FALL_THROUGH`
<a id="insn-00adbd90"></a> `00adbd90` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00adbd94"></a> `00adbd94` | `c9 f3 e4 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-00adbd98"></a> `00adbd98` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00adbd9c"></a> `00adbd9c` | `82 82 02 91` | add x2,x20,#0xa0 | `FALL_THROUGH`
<a id="insn-00adbda0"></a> `00adbda0` | `83 82 02 91` | add x3,x20,#0xa0 | `FALL_THROUGH`
<a id="insn-00adbda4"></a> `00adbda4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00adbda8"></a> `00adbda8` | `c4 f3 e4 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-00adbdac"></a> `00adbdac` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00adbdb0"></a> `00adbdb0` | `82 02 03 91` | add x2,x20,#0xc0 | `FALL_THROUGH`
<a id="insn-00adbdb4"></a> `00adbdb4` | `83 02 03 91` | add x3,x20,#0xc0 | `FALL_THROUGH`
<a id="insn-00adbdb8"></a> `00adbdb8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00adbdbc"></a> `00adbdbc` | `bf f3 e4 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-00adbdc0"></a> `00adbdc0` | `e8 43 43 39` | ldrb w8,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-00adbdc4"></a> `00adbdc4` | `28 09 00 37` | tbnz w8,#0x0,0x00adbee8 | `CONDITIONAL_JUMP`
<a id="insn-00adbdc8"></a> `00adbdc8` | `e8 c3 42 39` | ldrb w8,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00adbdcc"></a> `00adbdcc` | `68 09 00 37` | tbnz w8,#0x0,0x00adbef8 | `CONDITIONAL_JUMP`
<a id="insn-00adbdd0"></a> `00adbdd0` | `e8 43 42 39` | ldrb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00adbdd4"></a> `00adbdd4` | `a8 09 00 37` | tbnz w8,#0x0,0x00adbf08 | `CONDITIONAL_JUMP`
<a id="insn-00adbdd8"></a> `00adbdd8` | `e8 c3 41 39` | ldrb w8,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00adbddc"></a> `00adbddc` | `e8 09 00 37` | tbnz w8,#0x0,0x00adbf18 | `CONDITIONAL_JUMP`
<a id="insn-00adbde0"></a> `00adbde0` | `e8 43 41 39` | ldrb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00adbde4"></a> `00adbde4` | `28 0a 00 37` | tbnz w8,#0x0,0x00adbf28 | `CONDITIONAL_JUMP`
<a id="insn-00adbde8"></a> `00adbde8` | `e8 c3 40 39` | ldrb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00adbdec"></a> `00adbdec` | `68 0a 00 37` | tbnz w8,#0x0,0x00adbf38 | `CONDITIONAL_JUMP`
<a id="insn-00adbdf0"></a> `00adbdf0` | `e8 43 40 39` | ldrb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00adbdf4"></a> `00adbdf4` | `68 00 00 36` | tbz w8,#0x0,0x00adbe00 | `CONDITIONAL_JUMP`
<a id="insn-00adbdf8"></a> `00adbdf8` | `e0 13 40 f9` | ldr x0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00adbdfc"></a> `00adbdfc` | `85 fc 03 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00adbe00"></a> `00adbe00` | `53 08 00 d0` | adrp x19,0xbe5000 | `FALL_THROUGH`
<a id="insn-00adbe04"></a> `00adbe04` | `73 02 3e 91` | add x19,x19,#0xf80 | `FALL_THROUGH`
<a id="insn-00adbe08"></a> `00adbe08` | `e0 c9 ff b0` | adrp x0,0x418000 | `FALL_THROUGH`
<a id="insn-00adbe0c"></a> `00adbe0c` | `00 c0 0c 91` | add x0,x0,#0x330 | `FALL_THROUGH`
<a id="insn-00adbe10"></a> `00adbe10` | `21 2e 00 90` | adrp x1,0x109f000 | `FALL_THROUGH`
<a id="insn-00adbe14"></a> `00adbe14` | `21 80 3b 91` | add x1,x1,#0xee0 | `FALL_THROUGH`
<a id="insn-00adbe18"></a> `00adbe18` | `e2 03 13 aa` | mov x2,x19 | `FALL_THROUGH`
<a id="insn-00adbe1c"></a> `00adbe1c` | `5d fc 03 94` | bl 0x00bdaf90 | `UNCONDITIONAL_CALL`
<a id="insn-00adbe20"></a> `00adbe20` | `21 2e 00 90` | adrp x1,0x109f000 | `FALL_THROUGH`
<a id="insn-00adbe24"></a> `00adbe24` | `21 e0 3b 91` | add x1,x1,#0xef8 | `FALL_THROUGH`
<a id="insn-00adbe28"></a> `00adbe28` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00adbe2c"></a> `00adbe2c` | `c0 94 fe 10` | adr x0,0xad90c4 | `FALL_THROUGH`
<a id="insn-00adbe30"></a> `00adbe30` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00adbe34"></a> `00adbe34` | `e2 03 13 aa` | mov x2,x19 | `FALL_THROUGH`
<a id="insn-00adbe38"></a> `00adbe38` | `3f 08 00 f9` | str xzr,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-00adbe3c"></a> `00adbe3c` | `1f 8d 00 f8` | str xzr,[x8, #0x8]! | `FALL_THROUGH`
<a id="insn-00adbe40"></a> `00adbe40` | `28 00 00 f9` | str x8,[x1] | `FALL_THROUGH`
<a id="insn-00adbe44"></a> `00adbe44` | `53 fc 03 94` | bl 0x00bdaf90 | `UNCONDITIONAL_CALL`
<a id="insn-00adbe48"></a> `00adbe48` | `21 2e 00 90` | adrp x1,0x109f000 | `FALL_THROUGH`
<a id="insn-00adbe4c"></a> `00adbe4c` | `21 40 3c 91` | add x1,x1,#0xf10 | `FALL_THROUGH`
<a id="insn-00adbe50"></a> `00adbe50` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00adbe54"></a> `00adbe54` | `c0 93 fe 10` | adr x0,0xad90cc | `FALL_THROUGH`
<a id="insn-00adbe58"></a> `00adbe58` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00adbe5c"></a> `00adbe5c` | `e2 03 13 aa` | mov x2,x19 | `FALL_THROUGH`
<a id="insn-00adbe60"></a> `00adbe60` | `3f 08 00 f9` | str xzr,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-00adbe64"></a> `00adbe64` | `1f 8d 00 f8` | str xzr,[x8, #0x8]! | `FALL_THROUGH`
<a id="insn-00adbe68"></a> `00adbe68` | `28 00 00 f9` | str x8,[x1] | `FALL_THROUGH`
<a id="insn-00adbe6c"></a> `00adbe6c` | `49 fc 03 94` | bl 0x00bdaf90 | `UNCONDITIONAL_CALL`
<a id="insn-00adbe70"></a> `00adbe70` | `21 2e 00 90` | adrp x1,0x109f000 | `FALL_THROUGH`
<a id="insn-00adbe74"></a> `00adbe74` | `21 c0 3c 91` | add x1,x1,#0xf30 | `FALL_THROUGH`
<a id="insn-00adbe78"></a> `00adbe78` | `60 d4 ff d0` | adrp x0,0x569000 | `FALL_THROUGH`
<a id="insn-00adbe7c"></a> `00adbe7c` | `00 a0 36 91` | add x0,x0,#0xda8 | `FALL_THROUGH`
<a id="insn-00adbe80"></a> `00adbe80` | `e2 03 13 aa` | mov x2,x19 | `FALL_THROUGH`
<a id="insn-00adbe84"></a> `00adbe84` | `3f 10 00 f9` | str xzr,[x1, #0x20] | `FALL_THROUGH`
<a id="insn-00adbe88"></a> `00adbe88` | `42 fc 03 94` | bl 0x00bdaf90 | `UNCONDITIONAL_CALL`
<a id="insn-00adbe8c"></a> `00adbe8c` | `14 ec ff f0` | adrp x20,0x85e000 | `FALL_THROUGH`
<a id="insn-00adbe90"></a> `00adbe90` | `94 e2 0b 91` | add x20,x20,#0x2f8 | `FALL_THROUGH`
<a id="insn-00adbe94"></a> `00adbe94` | `21 2e 00 90` | adrp x1,0x109f000 | `FALL_THROUGH`
<a id="insn-00adbe98"></a> `00adbe98` | `21 80 3d 91` | add x1,x1,#0xf60 | `FALL_THROUGH`
<a id="insn-00adbe9c"></a> `00adbe9c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00adbea0"></a> `00adbea0` | `e2 03 13 aa` | mov x2,x19 | `FALL_THROUGH`
<a id="insn-00adbea4"></a> `00adbea4` | `3f 10 00 f9` | str xzr,[x1, #0x20] | `FALL_THROUGH`
<a id="insn-00adbea8"></a> `00adbea8` | `3a fc 03 94` | bl 0x00bdaf90 | `UNCONDITIONAL_CALL`
<a id="insn-00adbeac"></a> `00adbeac` | `21 2e 00 90` | adrp x1,0x109f000 | `FALL_THROUGH`
<a id="insn-00adbeb0"></a> `00adbeb0` | `21 40 3e 91` | add x1,x1,#0xf90 | `FALL_THROUGH`
<a id="insn-00adbeb4"></a> `00adbeb4` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00adbeb8"></a> `00adbeb8` | `e2 03 13 aa` | mov x2,x19 | `FALL_THROUGH`
<a id="insn-00adbebc"></a> `00adbebc` | `3f 10 00 f9` | str xzr,[x1, #0x20] | `FALL_THROUGH`
<a id="insn-00adbec0"></a> `00adbec0` | `34 fc 03 94` | bl 0x00bdaf90 | `UNCONDITIONAL_CALL`
<a id="insn-00adbec4"></a> `00adbec4` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00adbec8"></a> `00adbec8` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00adbecc"></a> `00adbecc` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00adbed0"></a> `00adbed0` | `41 0a 00 54` | b.ne 0x00adc018 | `CONDITIONAL_JUMP`
<a id="insn-00adbed4"></a> `00adbed4` | `f4 4f 51 a9` | ldp x20,x19,[sp, #0x110] | `FALL_THROUGH`
<a id="insn-00adbed8"></a> `00adbed8` | `fc 57 50 a9` | ldp x28,x21,[sp, #0x100] | `FALL_THROUGH`
<a id="insn-00adbedc"></a> `00adbedc` | `fd 7b 4f a9` | ldp x29,x30,[sp, #0xf0] | `FALL_THROUGH`
<a id="insn-00adbee0"></a> `00adbee0` | `ff 83 04 91` | add sp,sp,#0x120 | `FALL_THROUGH`
<a id="insn-00adbee4"></a> `00adbee4` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00adbee8"></a> `00adbee8` | `e0 73 40 f9` | ldr x0,[sp, #0xe0] | `FALL_THROUGH`
<a id="insn-00adbeec"></a> `00adbeec` | `49 fc 03 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00adbef0"></a> `00adbef0` | `e8 c3 42 39` | ldrb w8,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00adbef4"></a> `00adbef4` | `e8 f6 07 36` | tbz w8,#0x0,0x00adbdd0 | `CONDITIONAL_JUMP`
<a id="insn-00adbef8"></a> `00adbef8` | `e0 63 40 f9` | ldr x0,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00adbefc"></a> `00adbefc` | `45 fc 03 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00adbf00"></a> `00adbf00` | `e8 43 42 39` | ldrb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00adbf04"></a> `00adbf04` | `a8 f6 07 36` | tbz w8,#0x0,0x00adbdd8 | `CONDITIONAL_JUMP`
<a id="insn-00adbf08"></a> `00adbf08` | `e0 53 40 f9` | ldr x0,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00adbf0c"></a> `00adbf0c` | `41 fc 03 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00adbf10"></a> `00adbf10` | `e8 c3 41 39` | ldrb w8,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00adbf14"></a> `00adbf14` | `68 f6 07 36` | tbz w8,#0x0,0x00adbde0 | `CONDITIONAL_JUMP`
<a id="insn-00adbf18"></a> `00adbf18` | `e0 43 40 f9` | ldr x0,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00adbf1c"></a> `00adbf1c` | `3d fc 03 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00adbf20"></a> `00adbf20` | `e8 43 41 39` | ldrb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00adbf24"></a> `00adbf24` | `28 f6 07 36` | tbz w8,#0x0,0x00adbde8 | `CONDITIONAL_JUMP`
<a id="insn-00adbf28"></a> `00adbf28` | `e0 33 40 f9` | ldr x0,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00adbf2c"></a> `00adbf2c` | `39 fc 03 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00adbf30"></a> `00adbf30` | `e8 c3 40 39` | ldrb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00adbf34"></a> `00adbf34` | `e8 f5 07 36` | tbz w8,#0x0,0x00adbdf0 | `CONDITIONAL_JUMP`
<a id="insn-00adbf38"></a> `00adbf38` | `e0 23 40 f9` | ldr x0,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00adbf3c"></a> `00adbf3c` | `35 fc 03 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00adbf40"></a> `00adbf40` | `e8 43 40 39` | ldrb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00adbf44"></a> `00adbf44` | `a8 f5 07 37` | tbnz w8,#0x0,0x00adbdf8 | `CONDITIONAL_JUMP`
<a id="insn-00adbf48"></a> `00adbf48` | `ae ff ff 17` | b 0x00adbe00 | `UNCONDITIONAL_JUMP`
<a id="insn-00adc018"></a> `00adc018` | `0a fc 03 94` | bl 0x00bdb040 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00adbbe4`](#insn-00adbbe4) 範囲 `[['00adbbe4', '00adbd1f']]`
  - `FALL_THROUGH` [`00adbd1c`](#insn-00adbd1c) → [`00adbd20`](#insn-00adbd20)
- ブロック [`00adbd20`](#insn-00adbd20) 範囲 `[['00adbd20', '00adbdc7']]`
  - `CONDITIONAL_JUMP` [`00adbdc4`](#insn-00adbdc4) → [`00adbee8`](#insn-00adbee8)
  - `FALL_THROUGH` [`00adbdc4`](#insn-00adbdc4) → [`00adbdc8`](#insn-00adbdc8)
- ブロック [`00adbdc8`](#insn-00adbdc8) 範囲 `[['00adbdc8', '00adbdcf']]`
  - `CONDITIONAL_JUMP` [`00adbdcc`](#insn-00adbdcc) → [`00adbef8`](#insn-00adbef8)
  - `FALL_THROUGH` [`00adbdcc`](#insn-00adbdcc) → [`00adbdd0`](#insn-00adbdd0)
- ブロック [`00adbdd0`](#insn-00adbdd0) 範囲 `[['00adbdd0', '00adbdd7']]`
  - `CONDITIONAL_JUMP` [`00adbdd4`](#insn-00adbdd4) → [`00adbf08`](#insn-00adbf08)
  - `FALL_THROUGH` [`00adbdd4`](#insn-00adbdd4) → [`00adbdd8`](#insn-00adbdd8)
- ブロック [`00adbdd8`](#insn-00adbdd8) 範囲 `[['00adbdd8', '00adbddf']]`
  - `CONDITIONAL_JUMP` [`00adbddc`](#insn-00adbddc) → [`00adbf18`](#insn-00adbf18)
  - `FALL_THROUGH` [`00adbddc`](#insn-00adbddc) → [`00adbde0`](#insn-00adbde0)
- ブロック [`00adbde0`](#insn-00adbde0) 範囲 `[['00adbde0', '00adbde7']]`
  - `CONDITIONAL_JUMP` [`00adbde4`](#insn-00adbde4) → [`00adbf28`](#insn-00adbf28)
  - `FALL_THROUGH` [`00adbde4`](#insn-00adbde4) → [`00adbde8`](#insn-00adbde8)
- ブロック [`00adbde8`](#insn-00adbde8) 範囲 `[['00adbde8', '00adbdef']]`
  - `CONDITIONAL_JUMP` [`00adbdec`](#insn-00adbdec) → [`00adbf38`](#insn-00adbf38)
  - `FALL_THROUGH` [`00adbdec`](#insn-00adbdec) → [`00adbdf0`](#insn-00adbdf0)
- ブロック [`00adbdf0`](#insn-00adbdf0) 範囲 `[['00adbdf0', '00adbdf7']]`
  - `CONDITIONAL_JUMP` [`00adbdf4`](#insn-00adbdf4) → [`00adbe00`](#insn-00adbe00)
  - `FALL_THROUGH` [`00adbdf4`](#insn-00adbdf4) → [`00adbdf8`](#insn-00adbdf8)
- ブロック [`00adbdf8`](#insn-00adbdf8) 範囲 `[['00adbdf8', '00adbdff']]`
  - `FALL_THROUGH` [`00adbdfc`](#insn-00adbdfc) → [`00adbe00`](#insn-00adbe00)
- ブロック [`00adbe00`](#insn-00adbe00) 範囲 `[['00adbe00', '00adbe6f']]`
  - `FALL_THROUGH` [`00adbe6c`](#insn-00adbe6c) → [`00adbe70`](#insn-00adbe70)
- ブロック [`00adbe70`](#insn-00adbe70) 範囲 `[['00adbe70', '00adbe7b']]`
  - `FALL_THROUGH` [`00adbe78`](#insn-00adbe78) → [`00adbe7c`](#insn-00adbe7c)
- ブロック [`00adbe7c`](#insn-00adbe7c) 範囲 `[['00adbe7c', '00adbed3']]`
  - `CONDITIONAL_JUMP` [`00adbed0`](#insn-00adbed0) → [`00adc018`](#insn-00adc018)
  - `FALL_THROUGH` [`00adbed0`](#insn-00adbed0) → [`00adbed4`](#insn-00adbed4)
- ブロック [`00adbed4`](#insn-00adbed4) 範囲 `[['00adbed4', '00adbee7']]`
- ブロック [`00adbee8`](#insn-00adbee8) 範囲 `[['00adbee8', '00adbef7']]`
  - `CONDITIONAL_JUMP` [`00adbef4`](#insn-00adbef4) → [`00adbdd0`](#insn-00adbdd0)
  - `FALL_THROUGH` [`00adbef4`](#insn-00adbef4) → [`00adbef8`](#insn-00adbef8)
- ブロック [`00adbef8`](#insn-00adbef8) 範囲 `[['00adbef8', '00adbf07']]`
  - `CONDITIONAL_JUMP` [`00adbf04`](#insn-00adbf04) → [`00adbdd8`](#insn-00adbdd8)
  - `FALL_THROUGH` [`00adbf04`](#insn-00adbf04) → [`00adbf08`](#insn-00adbf08)
- ブロック [`00adbf08`](#insn-00adbf08) 範囲 `[['00adbf08', '00adbf17']]`
  - `CONDITIONAL_JUMP` [`00adbf14`](#insn-00adbf14) → [`00adbde0`](#insn-00adbde0)
  - `FALL_THROUGH` [`00adbf14`](#insn-00adbf14) → [`00adbf18`](#insn-00adbf18)
- ブロック [`00adbf18`](#insn-00adbf18) 範囲 `[['00adbf18', '00adbf27']]`
  - `CONDITIONAL_JUMP` [`00adbf24`](#insn-00adbf24) → [`00adbde8`](#insn-00adbde8)
  - `FALL_THROUGH` [`00adbf24`](#insn-00adbf24) → [`00adbf28`](#insn-00adbf28)
- ブロック [`00adbf28`](#insn-00adbf28) 範囲 `[['00adbf28', '00adbf37']]`
  - `CONDITIONAL_JUMP` [`00adbf34`](#insn-00adbf34) → [`00adbdf0`](#insn-00adbdf0)
  - `FALL_THROUGH` [`00adbf34`](#insn-00adbf34) → [`00adbf38`](#insn-00adbf38)
- ブロック [`00adbf38`](#insn-00adbf38) 範囲 `[['00adbf38', '00adbf47']]`
  - `CONDITIONAL_JUMP` [`00adbf44`](#insn-00adbf44) → [`00adbdf8`](#insn-00adbdf8)
  - `FALL_THROUGH` [`00adbf44`](#insn-00adbf44) → [`00adbf48`](#insn-00adbf48)
- ブロック [`00adbf48`](#insn-00adbf48) 範囲 `[['00adbf48', '00adbf4b']]`
  - `UNCONDITIONAL_JUMP` [`00adbf48`](#insn-00adbf48) → [`00adbe00`](#insn-00adbe00)
- ブロック [`00adc018`](#insn-00adc018) 範囲 `[['00adc018', '00adc01b']]`

## 命令位置別の参照

- [`00adbbe8`](#insn-00adbbe8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbbec`](#insn-00adbbec) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbbf0`](#insn-00adbbf0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbc14`](#insn-00adbc14) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbc20`](#insn-00adbc20) → `002a72dd`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00adbc28`](#insn-00adbc28) → `Stack[-0xff]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbc2c`](#insn-00adbc2c) → `Stack[-0xf8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbc3c`](#insn-00adbc3c) → `Stack[-0x10f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbc44`](#insn-00adbc44) → `002a72f0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00adbc48`](#insn-00adbc48) → `Stack[-0xdf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbc50`](#insn-00adbc50) → `Stack[-0xd8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbc60`](#insn-00adbc60) → `Stack[-0xef]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbc64`](#insn-00adbc64) → `002a8046`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00adbc68`](#insn-00adbc68) → `Stack[-0xbf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbc70`](#insn-00adbc70) → `Stack[-0xb8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbc80`](#insn-00adbc80) → `Stack[-0xcf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbc84`](#insn-00adbc84) → `0029373b`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00adbc88`](#insn-00adbc88) → `Stack[-0x9f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbc90`](#insn-00adbc90) → `Stack[-0x98]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbc9c`](#insn-00adbc9c) → `Stack[-0xaf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbca0`](#insn-00adbca0) → `0029c36e`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00adbca8`](#insn-00adbca8) → `Stack[-0x7f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbcb0`](#insn-00adbcb0) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbcbc`](#insn-00adbcbc) → `Stack[-0x8f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbcc0`](#insn-00adbcc0) → `00291877`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00adbcc8`](#insn-00adbcc8) → `Stack[-0x5f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbcd0`](#insn-00adbcd0) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbcdc`](#insn-00adbcdc) → `Stack[-0x6f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbce0`](#insn-00adbce0) → `002945b3`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00adbce4`](#insn-00adbce4) → `Stack[-0x110]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbce8`](#insn-00adbce8) → `Stack[-0xf0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbcec`](#insn-00adbcec) → `Stack[-0xd0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbcf0`](#insn-00adbcf0) → `Stack[-0xb0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbcf4`](#insn-00adbcf4) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbcf8`](#insn-00adbcf8) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbcfc`](#insn-00adbcfc) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbd04`](#insn-00adbd04) → `Stack[-0x118]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbd08`](#insn-00adbd08) → `Stack[-0xfd]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbd0c`](#insn-00adbd0c) → `Stack[-0xdd]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbd10`](#insn-00adbd10) → `Stack[-0xbd]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbd14`](#insn-00adbd14) → `Stack[-0x9d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbd18`](#insn-00adbd18) → `Stack[-0x7d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbd1c`](#insn-00adbd1c) → `Stack[-0x5d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbd20`](#insn-00adbd20) → `Stack[-0x3f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbd24`](#insn-00adbd24) → `Stack[-0x4f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbd28`](#insn-00adbd28) → `Stack[-0x3d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbd2c`](#insn-00adbd2c) → `0109fef0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adbd30`](#insn-00adbd30) → `0109fee8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adbd34`](#insn-00adbd34) → `0109fee0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adbd34`](#insn-00adbd34) → `0109fee8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adbd40`](#insn-00adbd40) → `0109fee0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adbd44`](#insn-00adbd44) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`00adbd48`](#insn-00adbd48) → `0109fee8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adbd54`](#insn-00adbd54) → `0109fee0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adbd58`](#insn-00adbd58) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`00adbd5c`](#insn-00adbd5c) → `0109fee8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adbd68`](#insn-00adbd68) → `0109fee0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adbd6c`](#insn-00adbd6c) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`00adbd70`](#insn-00adbd70) → `0109fee8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adbd7c`](#insn-00adbd7c) → `0109fee0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adbd80`](#insn-00adbd80) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`00adbd84`](#insn-00adbd84) → `0109fee8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adbd90`](#insn-00adbd90) → `0109fee0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adbd94`](#insn-00adbd94) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`00adbd98`](#insn-00adbd98) → `0109fee8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adbda4`](#insn-00adbda4) → `0109fee0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adbda8`](#insn-00adbda8) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`00adbdac`](#insn-00adbdac) → `0109fee8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adbdb8`](#insn-00adbdb8) → `0109fee0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adbdbc`](#insn-00adbdbc) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`00adbdc0`](#insn-00adbdc0) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbdc4`](#insn-00adbdc4) → [`00adbee8`](#insn-00adbee8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbdc8`](#insn-00adbdc8) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbdcc`](#insn-00adbdcc) → [`00adbef8`](#insn-00adbef8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbdd0`](#insn-00adbdd0) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbdd4`](#insn-00adbdd4) → [`00adbf08`](#insn-00adbf08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbdd8`](#insn-00adbdd8) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbddc`](#insn-00adbddc) → [`00adbf18`](#insn-00adbf18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbde0`](#insn-00adbde0) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbde4`](#insn-00adbde4) → [`00adbf28`](#insn-00adbf28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbde8`](#insn-00adbde8) → `Stack[-0xf0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbdec`](#insn-00adbdec) → [`00adbf38`](#insn-00adbf38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbdf0`](#insn-00adbdf0) → `Stack[-0x110]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbdf4`](#insn-00adbdf4) → [`00adbe00`](#insn-00adbe00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbdf8`](#insn-00adbdf8) → `Stack[-0x100]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbdfc`](#insn-00adbdfc) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00adbe0c`](#insn-00adbe0c) → [`00418330`](../00418/00418330.md) · `PARAM` · `ANALYSIS` · 関数 `00418330` · 推定シンボル `None` · 推定型 `None`
- [`00adbe14`](#insn-00adbe14) → `0109fee0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adbe18`](#insn-00adbe18) → `00be5f80`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00adbe1c`](#insn-00adbe1c) → [`00bdaf90`](../00bda/00bdaf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf90` · 推定シンボル `None` · 推定型 `None`
- [`00adbe24`](#insn-00adbe24) → `0109fef8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adbe2c`](#insn-00adbe2c) → [`00ad90c4`](../00ad9/00ad90c4.md) · `PARAM` · `ANALYSIS` · 関数 `00ad90c4` · 推定シンボル `None` · 推定型 `None`
- [`00adbe34`](#insn-00adbe34) → `00be5f80`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00adbe38`](#insn-00adbe38) → `0109ff08`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adbe3c`](#insn-00adbe3c) → `0109ff00`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adbe40`](#insn-00adbe40) → `0109fef8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adbe40`](#insn-00adbe40) → `0109ff00`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adbe44`](#insn-00adbe44) → [`00bdaf90`](../00bda/00bdaf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf90` · 推定シンボル `None` · 推定型 `None`
- [`00adbe4c`](#insn-00adbe4c) → `0109ff10`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adbe54`](#insn-00adbe54) → [`00ad90cc`](../00ad9/00ad90cc.md) · `PARAM` · `ANALYSIS` · 関数 `00ad90cc` · 推定シンボル `None` · 推定型 `None`
- [`00adbe5c`](#insn-00adbe5c) → `00be5f80`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00adbe60`](#insn-00adbe60) → `0109ff20`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adbe64`](#insn-00adbe64) → `0109ff18`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adbe68`](#insn-00adbe68) → `0109ff10`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adbe68`](#insn-00adbe68) → `0109ff18`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adbe6c`](#insn-00adbe6c) → [`00bdaf90`](../00bda/00bdaf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf90` · 推定シンボル `None` · 推定型 `None`
- [`00adbe74`](#insn-00adbe74) → `0109ff30`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbe7c`](#insn-00adbe7c) → [`00569da8`](../00569/00569da8.md) · `PARAM` · `ANALYSIS` · 関数 `00569da8` · 推定シンボル `None` · 推定型 `None`
- [`00adbe80`](#insn-00adbe80) → `00be5f80`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00adbe84`](#insn-00adbe84) → `0109ff50`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adbe88`](#insn-00adbe88) → [`00bdaf90`](../00bda/00bdaf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf90` · 推定シンボル `None` · 推定型 `None`
- [`00adbe98`](#insn-00adbe98) → `0109ff60`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbe9c`](#insn-00adbe9c) → [`0085e2f8`](../0085e/0085e2f8.md) · `PARAM` · `ANALYSIS` · 関数 `0085e2f8` · 推定シンボル `None` · 推定型 `None`
- [`00adbea0`](#insn-00adbea0) → `00be5f80`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00adbea4`](#insn-00adbea4) → `0109ff80`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adbea8`](#insn-00adbea8) → [`00bdaf90`](../00bda/00bdaf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf90` · 推定シンボル `None` · 推定型 `None`
- [`00adbeb0`](#insn-00adbeb0) → `0109ff90`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbeb4`](#insn-00adbeb4) → [`0085e2f8`](../0085e/0085e2f8.md) · `PARAM` · `ANALYSIS` · 関数 `0085e2f8` · 推定シンボル `None` · 推定型 `None`
- [`00adbeb8`](#insn-00adbeb8) → `00be5f80`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00adbebc`](#insn-00adbebc) → `0109ffb0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adbec0`](#insn-00adbec0) → [`00bdaf90`](../00bda/00bdaf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf90` · 推定シンボル `None` · 推定型 `None`
- [`00adbec8`](#insn-00adbec8) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbed0`](#insn-00adbed0) → [`00adc018`](#insn-00adc018) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbed4`](#insn-00adbed4) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbed8`](#insn-00adbed8) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbedc`](#insn-00adbedc) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbee8`](#insn-00adbee8) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbeec`](#insn-00adbeec) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00adbef0`](#insn-00adbef0) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbef4`](#insn-00adbef4) → [`00adbdd0`](#insn-00adbdd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbef8`](#insn-00adbef8) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbefc`](#insn-00adbefc) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00adbf00`](#insn-00adbf00) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbf04`](#insn-00adbf04) → [`00adbdd8`](#insn-00adbdd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbf08`](#insn-00adbf08) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbf0c`](#insn-00adbf0c) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00adbf10`](#insn-00adbf10) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbf14`](#insn-00adbf14) → [`00adbde0`](#insn-00adbde0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbf18`](#insn-00adbf18) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbf1c`](#insn-00adbf1c) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00adbf20`](#insn-00adbf20) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbf24`](#insn-00adbf24) → [`00adbde8`](#insn-00adbde8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbf28`](#insn-00adbf28) → `Stack[-0xc0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbf2c`](#insn-00adbf2c) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00adbf30`](#insn-00adbf30) → `Stack[-0xf0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbf34`](#insn-00adbf34) → [`00adbdf0`](#insn-00adbdf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbf38`](#insn-00adbf38) → `Stack[-0xe0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbf3c`](#insn-00adbf3c) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00adbf40`](#insn-00adbf40) → `Stack[-0x110]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbf44`](#insn-00adbf44) → [`00adbdf8`](#insn-00adbdf8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbf48`](#insn-00adbf48) → [`00adbe00`](#insn-00adbe00) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adc018`](#insn-00adc018) → [`00bdb040`](../00bdb/00bdb040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb040` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00adbbe8`](#insn-00adbbe8)

~~~json
{
  "source": "00adbbe8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbbec`](#insn-00adbbec)

~~~json
{
  "source": "00adbbec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbbf0`](#insn-00adbbf0)

~~~json
{
  "source": "00adbbf0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbc14`](#insn-00adbc14)

~~~json
{
  "source": "00adbc14",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbc20`](#insn-00adbc20)

~~~json
{
  "source": "00adbc20",
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
- 参照命令 [`00adbc28`](#insn-00adbc28)

~~~json
{
  "source": "00adbc28",
  "target": "Stack[-0xff]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbc2c`](#insn-00adbc2c)

~~~json
{
  "source": "00adbc2c",
  "target": "Stack[-0xf8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbc3c`](#insn-00adbc3c)

~~~json
{
  "source": "00adbc3c",
  "target": "Stack[-0x10f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbc44`](#insn-00adbc44)

~~~json
{
  "source": "00adbc44",
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
- 参照命令 [`00adbc48`](#insn-00adbc48)

~~~json
{
  "source": "00adbc48",
  "target": "Stack[-0xdf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbc50`](#insn-00adbc50)

~~~json
{
  "source": "00adbc50",
  "target": "Stack[-0xd8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbc60`](#insn-00adbc60)

~~~json
{
  "source": "00adbc60",
  "target": "Stack[-0xef]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbc64`](#insn-00adbc64)

~~~json
{
  "source": "00adbc64",
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
- 参照命令 [`00adbc68`](#insn-00adbc68)

~~~json
{
  "source": "00adbc68",
  "target": "Stack[-0xbf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbc70`](#insn-00adbc70)

~~~json
{
  "source": "00adbc70",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbc80`](#insn-00adbc80)

~~~json
{
  "source": "00adbc80",
  "target": "Stack[-0xcf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbc84`](#insn-00adbc84)

~~~json
{
  "source": "00adbc84",
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
- 参照命令 [`00adbc88`](#insn-00adbc88)

~~~json
{
  "source": "00adbc88",
  "target": "Stack[-0x9f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbc90`](#insn-00adbc90)

~~~json
{
  "source": "00adbc90",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbc9c`](#insn-00adbc9c)

~~~json
{
  "source": "00adbc9c",
  "target": "Stack[-0xaf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbca0`](#insn-00adbca0)

~~~json
{
  "source": "00adbca0",
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
- 参照命令 [`00adbca8`](#insn-00adbca8)

~~~json
{
  "source": "00adbca8",
  "target": "Stack[-0x7f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbcb0`](#insn-00adbcb0)

~~~json
{
  "source": "00adbcb0",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbcbc`](#insn-00adbcbc)

~~~json
{
  "source": "00adbcbc",
  "target": "Stack[-0x8f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbcc0`](#insn-00adbcc0)

~~~json
{
  "source": "00adbcc0",
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
- 参照命令 [`00adbcc8`](#insn-00adbcc8)

~~~json
{
  "source": "00adbcc8",
  "target": "Stack[-0x5f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbcd0`](#insn-00adbcd0)

~~~json
{
  "source": "00adbcd0",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbcdc`](#insn-00adbcdc)

~~~json
{
  "source": "00adbcdc",
  "target": "Stack[-0x6f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbce0`](#insn-00adbce0)

~~~json
{
  "source": "00adbce0",
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
- 参照命令 [`00adbce4`](#insn-00adbce4)

~~~json
{
  "source": "00adbce4",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbce8`](#insn-00adbce8)

~~~json
{
  "source": "00adbce8",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbcec`](#insn-00adbcec)

~~~json
{
  "source": "00adbcec",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbcf0`](#insn-00adbcf0)

~~~json
{
  "source": "00adbcf0",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbcf4`](#insn-00adbcf4)

~~~json
{
  "source": "00adbcf4",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbcf8`](#insn-00adbcf8)

~~~json
{
  "source": "00adbcf8",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbcfc`](#insn-00adbcfc)

~~~json
{
  "source": "00adbcfc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbd04`](#insn-00adbd04)

~~~json
{
  "source": "00adbd04",
  "target": "Stack[-0x118]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbd08`](#insn-00adbd08)

~~~json
{
  "source": "00adbd08",
  "target": "Stack[-0xfd]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbd0c`](#insn-00adbd0c)

~~~json
{
  "source": "00adbd0c",
  "target": "Stack[-0xdd]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbd10`](#insn-00adbd10)

~~~json
{
  "source": "00adbd10",
  "target": "Stack[-0xbd]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbd14`](#insn-00adbd14)

~~~json
{
  "source": "00adbd14",
  "target": "Stack[-0x9d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbd18`](#insn-00adbd18)

~~~json
{
  "source": "00adbd18",
  "target": "Stack[-0x7d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbd1c`](#insn-00adbd1c)

~~~json
{
  "source": "00adbd1c",
  "target": "Stack[-0x5d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbd20`](#insn-00adbd20)

~~~json
{
  "source": "00adbd20",
  "target": "Stack[-0x3f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbd24`](#insn-00adbd24)

~~~json
{
  "source": "00adbd24",
  "target": "Stack[-0x4f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbd28`](#insn-00adbd28)

~~~json
{
  "source": "00adbd28",
  "target": "Stack[-0x3d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbd2c`](#insn-00adbd2c)

~~~json
{
  "source": "00adbd2c",
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
- 参照命令 [`00adbd30`](#insn-00adbd30)

~~~json
{
  "source": "00adbd30",
  "target": "0109fee8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fee8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adbd34`](#insn-00adbd34)

~~~json
{
  "source": "00adbd34",
  "target": "0109fee0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fee0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adbd34`](#insn-00adbd34)

~~~json
{
  "source": "00adbd34",
  "target": "0109fee8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fee8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adbd40`](#insn-00adbd40)

~~~json
{
  "source": "00adbd40",
  "target": "0109fee0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fee0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adbd44`](#insn-00adbd44)

~~~json
{
  "source": "00adbd44",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adbd48`](#insn-00adbd48)

~~~json
{
  "source": "00adbd48",
  "target": "0109fee8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fee8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adbd54`](#insn-00adbd54)

~~~json
{
  "source": "00adbd54",
  "target": "0109fee0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fee0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adbd58`](#insn-00adbd58)

~~~json
{
  "source": "00adbd58",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adbd5c`](#insn-00adbd5c)

~~~json
{
  "source": "00adbd5c",
  "target": "0109fee8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fee8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adbd68`](#insn-00adbd68)

~~~json
{
  "source": "00adbd68",
  "target": "0109fee0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fee0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adbd6c`](#insn-00adbd6c)

~~~json
{
  "source": "00adbd6c",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adbd70`](#insn-00adbd70)

~~~json
{
  "source": "00adbd70",
  "target": "0109fee8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fee8",
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
  "target": "0109fee0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fee0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adbd80`](#insn-00adbd80)

~~~json
{
  "source": "00adbd80",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adbd84`](#insn-00adbd84)

~~~json
{
  "source": "00adbd84",
  "target": "0109fee8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fee8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adbd90`](#insn-00adbd90)

~~~json
{
  "source": "00adbd90",
  "target": "0109fee0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fee0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adbd94`](#insn-00adbd94)

~~~json
{
  "source": "00adbd94",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adbd98`](#insn-00adbd98)

~~~json
{
  "source": "00adbd98",
  "target": "0109fee8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fee8",
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
  "target": "0109fee0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fee0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adbda8`](#insn-00adbda8)

~~~json
{
  "source": "00adbda8",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adbdac`](#insn-00adbdac)

~~~json
{
  "source": "00adbdac",
  "target": "0109fee8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fee8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adbdb8`](#insn-00adbdb8)

~~~json
{
  "source": "00adbdb8",
  "target": "0109fee0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fee0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adbdbc`](#insn-00adbdbc)

~~~json
{
  "source": "00adbdbc",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adbdc0`](#insn-00adbdc0)

~~~json
{
  "source": "00adbdc0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbdc4`](#insn-00adbdc4)

~~~json
{
  "source": "00adbdc4",
  "target": "00adbee8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbdc8`](#insn-00adbdc8)

~~~json
{
  "source": "00adbdc8",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbdcc`](#insn-00adbdcc)

~~~json
{
  "source": "00adbdcc",
  "target": "00adbef8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbdd0`](#insn-00adbdd0)

~~~json
{
  "source": "00adbdd0",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbdd4`](#insn-00adbdd4)

~~~json
{
  "source": "00adbdd4",
  "target": "00adbf08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbdd8`](#insn-00adbdd8)

~~~json
{
  "source": "00adbdd8",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbddc`](#insn-00adbddc)

~~~json
{
  "source": "00adbddc",
  "target": "00adbf18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbde0`](#insn-00adbde0)

~~~json
{
  "source": "00adbde0",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbde4`](#insn-00adbde4)

~~~json
{
  "source": "00adbde4",
  "target": "00adbf28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbde8`](#insn-00adbde8)

~~~json
{
  "source": "00adbde8",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbdec`](#insn-00adbdec)

~~~json
{
  "source": "00adbdec",
  "target": "00adbf38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbdf0`](#insn-00adbdf0)

~~~json
{
  "source": "00adbdf0",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbdf4`](#insn-00adbdf4)

~~~json
{
  "source": "00adbdf4",
  "target": "00adbe00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbdf8`](#insn-00adbdf8)

~~~json
{
  "source": "00adbdf8",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbdfc`](#insn-00adbdfc)

~~~json
{
  "source": "00adbdfc",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adbe0c`](#insn-00adbe0c)

~~~json
{
  "source": "00adbe0c",
  "target": "00418330",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adbe14`](#insn-00adbe14)

~~~json
{
  "source": "00adbe14",
  "target": "0109fee0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fee0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adbe18`](#insn-00adbe18)

~~~json
{
  "source": "00adbe18",
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
- 参照命令 [`00adbe1c`](#insn-00adbe1c)

~~~json
{
  "source": "00adbe1c",
  "target": "00bdaf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adbe24`](#insn-00adbe24)

~~~json
{
  "source": "00adbe24",
  "target": "0109fef8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fef8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adbe2c`](#insn-00adbe2c)

~~~json
{
  "source": "00adbe2c",
  "target": "00ad90c4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adbe34`](#insn-00adbe34)

~~~json
{
  "source": "00adbe34",
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
- 参照命令 [`00adbe38`](#insn-00adbe38)

~~~json
{
  "source": "00adbe38",
  "target": "0109ff08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109ff08",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adbe3c`](#insn-00adbe3c)

~~~json
{
  "source": "00adbe3c",
  "target": "0109ff00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109ff00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adbe40`](#insn-00adbe40)

~~~json
{
  "source": "00adbe40",
  "target": "0109fef8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fef8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adbe40`](#insn-00adbe40)

~~~json
{
  "source": "00adbe40",
  "target": "0109ff00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109ff00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adbe44`](#insn-00adbe44)

~~~json
{
  "source": "00adbe44",
  "target": "00bdaf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adbe4c`](#insn-00adbe4c)

~~~json
{
  "source": "00adbe4c",
  "target": "0109ff10",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109ff10",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adbe54`](#insn-00adbe54)

~~~json
{
  "source": "00adbe54",
  "target": "00ad90cc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adbe5c`](#insn-00adbe5c)

~~~json
{
  "source": "00adbe5c",
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
- 参照命令 [`00adbe60`](#insn-00adbe60)

~~~json
{
  "source": "00adbe60",
  "target": "0109ff20",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109ff20",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adbe64`](#insn-00adbe64)

~~~json
{
  "source": "00adbe64",
  "target": "0109ff18",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109ff18",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adbe68`](#insn-00adbe68)

~~~json
{
  "source": "00adbe68",
  "target": "0109ff10",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109ff10",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adbe68`](#insn-00adbe68)

~~~json
{
  "source": "00adbe68",
  "target": "0109ff18",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109ff18",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adbe6c`](#insn-00adbe6c)

~~~json
{
  "source": "00adbe6c",
  "target": "00bdaf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adbe74`](#insn-00adbe74)

~~~json
{
  "source": "00adbe74",
  "target": "0109ff30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbe7c`](#insn-00adbe7c)

~~~json
{
  "source": "00adbe7c",
  "target": "00569da8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adbe80`](#insn-00adbe80)

~~~json
{
  "source": "00adbe80",
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
- 参照命令 [`00adbe84`](#insn-00adbe84)

~~~json
{
  "source": "00adbe84",
  "target": "0109ff50",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109ff50",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adbe88`](#insn-00adbe88)

~~~json
{
  "source": "00adbe88",
  "target": "00bdaf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adbe98`](#insn-00adbe98)

~~~json
{
  "source": "00adbe98",
  "target": "0109ff60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbe9c`](#insn-00adbe9c)

~~~json
{
  "source": "00adbe9c",
  "target": "0085e2f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adbea0`](#insn-00adbea0)

~~~json
{
  "source": "00adbea0",
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
- 参照命令 [`00adbea4`](#insn-00adbea4)

~~~json
{
  "source": "00adbea4",
  "target": "0109ff80",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109ff80",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adbea8`](#insn-00adbea8)

~~~json
{
  "source": "00adbea8",
  "target": "00bdaf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adbeb0`](#insn-00adbeb0)

~~~json
{
  "source": "00adbeb0",
  "target": "0109ff90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbeb4`](#insn-00adbeb4)

~~~json
{
  "source": "00adbeb4",
  "target": "0085e2f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adbeb8`](#insn-00adbeb8)

~~~json
{
  "source": "00adbeb8",
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
- 参照命令 [`00adbebc`](#insn-00adbebc)

~~~json
{
  "source": "00adbebc",
  "target": "0109ffb0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109ffb0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adbec0`](#insn-00adbec0)

~~~json
{
  "source": "00adbec0",
  "target": "00bdaf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adbec8`](#insn-00adbec8)

~~~json
{
  "source": "00adbec8",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbed0`](#insn-00adbed0)

~~~json
{
  "source": "00adbed0",
  "target": "00adc018",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbed4`](#insn-00adbed4)

~~~json
{
  "source": "00adbed4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbed8`](#insn-00adbed8)

~~~json
{
  "source": "00adbed8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbedc`](#insn-00adbedc)

~~~json
{
  "source": "00adbedc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbee8`](#insn-00adbee8)

~~~json
{
  "source": "00adbee8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbeec`](#insn-00adbeec)

~~~json
{
  "source": "00adbeec",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adbef0`](#insn-00adbef0)

~~~json
{
  "source": "00adbef0",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbef4`](#insn-00adbef4)

~~~json
{
  "source": "00adbef4",
  "target": "00adbdd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbef8`](#insn-00adbef8)

~~~json
{
  "source": "00adbef8",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbefc`](#insn-00adbefc)

~~~json
{
  "source": "00adbefc",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adbf00`](#insn-00adbf00)

~~~json
{
  "source": "00adbf00",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbf04`](#insn-00adbf04)

~~~json
{
  "source": "00adbf04",
  "target": "00adbdd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbf08`](#insn-00adbf08)

~~~json
{
  "source": "00adbf08",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbf0c`](#insn-00adbf0c)

~~~json
{
  "source": "00adbf0c",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adbf10`](#insn-00adbf10)

~~~json
{
  "source": "00adbf10",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbf14`](#insn-00adbf14)

~~~json
{
  "source": "00adbf14",
  "target": "00adbde0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbf18`](#insn-00adbf18)

~~~json
{
  "source": "00adbf18",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbf1c`](#insn-00adbf1c)

~~~json
{
  "source": "00adbf1c",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adbf20`](#insn-00adbf20)

~~~json
{
  "source": "00adbf20",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbf24`](#insn-00adbf24)

~~~json
{
  "source": "00adbf24",
  "target": "00adbde8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbf28`](#insn-00adbf28)

~~~json
{
  "source": "00adbf28",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbf2c`](#insn-00adbf2c)

~~~json
{
  "source": "00adbf2c",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adbf30`](#insn-00adbf30)

~~~json
{
  "source": "00adbf30",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbf34`](#insn-00adbf34)

~~~json
{
  "source": "00adbf34",
  "target": "00adbdf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbf38`](#insn-00adbf38)

~~~json
{
  "source": "00adbf38",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbf3c`](#insn-00adbf3c)

~~~json
{
  "source": "00adbf3c",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adbf40`](#insn-00adbf40)

~~~json
{
  "source": "00adbf40",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbf44`](#insn-00adbf44)

~~~json
{
  "source": "00adbf44",
  "target": "00adbdf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbf48`](#insn-00adbf48)

~~~json
{
  "source": "00adbf48",
  "target": "00adbe00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adc018`](#insn-00adc018)

~~~json
{
  "source": "00adc018",
  "target": "00bdb040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
