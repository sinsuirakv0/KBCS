# 00aadcbc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aadc78`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aadc78.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0059.md#compare-28bf7cd4a5d7ef20ce17d2edaeb9e78c)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b0d74c`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0d/00b0d74c.md) · 移動量 `+0x5fa90`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0053.md#compare-0b262cb821729e394e7cb864be059282)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aadcbc",
  "name": "_INIT_246",
  "size": 708,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b697e054381474c10fab0d982003a3a64042fb76a12844f3a2f50dcd130e94dd",
  "source_text_sha256": "b697e054381474c10fab0d982003a3a64042fb76a12844f3a2f50dcd130e94dd",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aadcbc",
        "00aadf7b"
      ],
      [
        "00aae048",
        "00aae04b"
      ]
    ],
    "bytes_sha256": "18101c4d7f143b5bd156da87936ca8df1648c4a74e2dce82dca7efa0e109cdd0",
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
  DAT_0109faf0 = 0;
  DAT_0109fae8 = 0;
  DAT_0109fae0 = &DAT_0109fae8;
  FUN_00418cb8(&DAT_0109fae0,&DAT_0109fae8,local_118,local_118);
  FUN_00418cb8(&DAT_0109fae0,&DAT_0109fae8,local_f8,local_f8);
  FUN_00418cb8(&DAT_0109fae0,&DAT_0109fae8,local_d8,local_d8);
  FUN_00418cb8(&DAT_0109fae0,&DAT_0109fae8,local_b8,local_b8);
  FUN_00418cb8(&DAT_0109fae0,&DAT_0109fae8,local_98,local_98);
  FUN_00418cb8(&DAT_0109fae0,&DAT_0109fae8,local_78,local_78);
  FUN_00418cb8(&DAT_0109fae0,&DAT_0109fae8,local_58,local_58);
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
  __cxa_atexit(FUN_00418330,&DAT_0109fae0,&PTR_LOOP_00be5fd0);
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
<a id="insn-00aadcbc"></a> `00aadcbc` | `ff 83 04 d1` | sub sp,sp,#0x120 | `FALL_THROUGH`
<a id="insn-00aadcc0"></a> `00aadcc0` | `fd 7b 0f a9` | stp x29,x30,[sp, #0xf0] | `FALL_THROUGH`
<a id="insn-00aadcc4"></a> `00aadcc4` | `fc 57 10 a9` | stp x28,x21,[sp, #0x100] | `FALL_THROUGH`
<a id="insn-00aadcc8"></a> `00aadcc8` | `f4 4f 11 a9` | stp x20,x19,[sp, #0x110] | `FALL_THROUGH`
<a id="insn-00aadccc"></a> `00aadccc` | `fd c3 03 91` | add x29,sp,#0xf0 | `FALL_THROUGH`
<a id="insn-00aadcd0"></a> `00aadcd0` | `55 d0 3b d5` | mrs x21,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00aadcd4"></a> `00aadcd4` | `2a e8 8c 52` | mov w10,#0x6741 | `FALL_THROUGH`
<a id="insn-00aadcd8"></a> `00aadcd8` | `f4 23 00 91` | add x20,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00aadcdc"></a> `00aadcdc` | `a9 16 40 f9` | ldr x9,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00aadce0"></a> `00aadce0` | `88 04 80 52` | mov w8,#0x24 | `FALL_THROUGH`
<a id="insn-00aadce4"></a> `00aadce4` | `93 2f 00 d0` | adrp x19,0x109f000 | `FALL_THROUGH`
<a id="insn-00aadce8"></a> `00aadce8` | `73 82 2b 91` | add x19,x19,#0xae0 | `FALL_THROUGH`
<a id="insn-00aadcec"></a> `00aadcec` | `a9 83 1f f8` | stur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aadcf0"></a> `00aadcf0` | `c9 bf ff d0` | adrp x9,0x2a7000 | `FALL_THROUGH`
<a id="insn-00aadcf4"></a> `00aadcf4` | `29 dd 0d 91` | add x9,x9,#0x377 | `FALL_THROUGH`
<a id="insn-00aadcf8"></a> `00aadcf8` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00aadcfc"></a> `00aadcfc` | `29 00 80 52` | mov w9,#0x1 | `FALL_THROUGH`
<a id="insn-00aadd00"></a> `00aadd00` | `ea 13 02 78` | sturh w10,[sp, #0x21] | `FALL_THROUGH`
<a id="insn-00aadd04"></a> `00aadd04` | `e9 2b 00 b9` | str w9,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00aadd08"></a> `00aadd08` | `49 28 88 52` | mov w9,#0x4142 | `FALL_THROUGH`
<a id="insn-00aadd0c"></a> `00aadd0c` | `ca bf ff d0` | adrp x10,0x2a7000 | `FALL_THROUGH`
<a id="insn-00aadd10"></a> `00aadd10` | `4a 29 0e 91` | add x10,x10,#0x38a | `FALL_THROUGH`
<a id="insn-00aadd14"></a> `00aadd14` | `e0 13 81 3c` | stur q0,[sp, #0x11] | `FALL_THROUGH`
<a id="insn-00aadd18"></a> `00aadd18` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00aadd1c"></a> `00aadd1c` | `40 01 c0 3d` | ldr q0,[x10] | `FALL_THROUGH`
<a id="insn-00aadd20"></a> `00aadd20` | `e9 13 04 78` | sturh w9,[sp, #0x41] | `FALL_THROUGH`
<a id="insn-00aadd24"></a> `00aadd24` | `49 00 80 52` | mov w9,#0x2 | `FALL_THROUGH`
<a id="insn-00aadd28"></a> `00aadd28` | `e9 4b 00 b9` | str w9,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00aadd2c"></a> `00aadd2c` | `49 e8 8c 52` | mov w9,#0x6742 | `FALL_THROUGH`
<a id="insn-00aadd30"></a> `00aadd30` | `ca bf ff f0` | adrp x10,0x2a8000 | `FALL_THROUGH`
<a id="insn-00aadd34"></a> `00aadd34` | `4a 81 03 91` | add x10,x10,#0xe0 | `FALL_THROUGH`
<a id="insn-00aadd38"></a> `00aadd38` | `e0 13 83 3c` | stur q0,[sp, #0x31] | `FALL_THROUGH`
<a id="insn-00aadd3c"></a> `00aadd3c` | `40 01 c0 3d` | ldr q0,[x10] | `FALL_THROUGH`
<a id="insn-00aadd40"></a> `00aadd40` | `e9 13 06 78` | sturh w9,[sp, #0x61] | `FALL_THROUGH`
<a id="insn-00aadd44"></a> `00aadd44` | `69 00 80 52` | mov w9,#0x3 | `FALL_THROUGH`
<a id="insn-00aadd48"></a> `00aadd48` | `e9 6b 00 b9` | str w9,[sp, #0x68] | `FALL_THROUGH`
<a id="insn-00aadd4c"></a> `00aadd4c` | `29 e8 8e 52` | mov w9,#0x7741 | `FALL_THROUGH`
<a id="insn-00aadd50"></a> `00aadd50` | `2a bf ff d0` | adrp x10,0x293000 | `FALL_THROUGH`
<a id="insn-00aadd54"></a> `00aadd54` | `4a b9 1a 91` | add x10,x10,#0x6ae | `FALL_THROUGH`
<a id="insn-00aadd58"></a> `00aadd58` | `e0 13 85 3c` | stur q0,[sp, #0x51] | `FALL_THROUGH`
<a id="insn-00aadd5c"></a> `00aadd5c` | `40 01 c0 3d` | ldr q0,[x10] | `FALL_THROUGH`
<a id="insn-00aadd60"></a> `00aadd60` | `e9 13 08 78` | sturh w9,[sp, #0x81] | `FALL_THROUGH`
<a id="insn-00aadd64"></a> `00aadd64` | `89 00 80 52` | mov w9,#0x4 | `FALL_THROUGH`
<a id="insn-00aadd68"></a> `00aadd68` | `e9 8b 00 b9` | str w9,[sp, #0x88] | `FALL_THROUGH`
<a id="insn-00aadd6c"></a> `00aadd6c` | `69 bf ff f0` | adrp x9,0x29c000 | `FALL_THROUGH`
<a id="insn-00aadd70"></a> `00aadd70` | `29 b1 0d 91` | add x9,x9,#0x36c | `FALL_THROUGH`
<a id="insn-00aadd74"></a> `00aadd74` | `e0 13 87 3c` | stur q0,[sp, #0x71] | `FALL_THROUGH`
<a id="insn-00aadd78"></a> `00aadd78` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00aadd7c"></a> `00aadd7c` | `49 28 8a 52` | mov w9,#0x5142 | `FALL_THROUGH`
<a id="insn-00aadd80"></a> `00aadd80` | `89 92 09 78` | sturh w9,[x20, #0x99] | `FALL_THROUGH`
<a id="insn-00aadd84"></a> `00aadd84` | `a9 00 80 52` | mov w9,#0x5 | `FALL_THROUGH`
<a id="insn-00aadd88"></a> `00aadd88` | `e9 ab 00 b9` | str w9,[sp, #0xa8] | `FALL_THROUGH`
<a id="insn-00aadd8c"></a> `00aadd8c` | `29 bf ff 90` | adrp x9,0x291000 | `FALL_THROUGH`
<a id="insn-00aadd90"></a> `00aadd90` | `29 dd 21 91` | add x9,x9,#0x877 | `FALL_THROUGH`
<a id="insn-00aadd94"></a> `00aadd94` | `80 92 88 3c` | stur q0,[x20, #0x89] | `FALL_THROUGH`
<a id="insn-00aadd98"></a> `00aadd98` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00aadd9c"></a> `00aadd9c` | `49 e8 8e 52` | mov w9,#0x7742 | `FALL_THROUGH`
<a id="insn-00aadda0"></a> `00aadda0` | `89 92 0b 78` | sturh w9,[x20, #0xb9] | `FALL_THROUGH`
<a id="insn-00aadda4"></a> `00aadda4` | `c9 00 80 52` | mov w9,#0x6 | `FALL_THROUGH`
<a id="insn-00aadda8"></a> `00aadda8` | `e9 cb 00 b9` | str w9,[sp, #0xc8] | `FALL_THROUGH`
<a id="insn-00aaddac"></a> `00aaddac` | `29 bf ff f0` | adrp x9,0x294000 | `FALL_THROUGH`
<a id="insn-00aaddb0"></a> `00aaddb0` | `29 99 14 91` | add x9,x9,#0x526 | `FALL_THROUGH`
<a id="insn-00aaddb4"></a> `00aaddb4` | `80 92 8a 3c` | stur q0,[x20, #0xa9] | `FALL_THROUGH`
<a id="insn-00aaddb8"></a> `00aaddb8` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00aaddbc"></a> `00aaddbc` | `e8 43 00 39` | strb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aaddc0"></a> `00aaddc0` | `e8 c3 00 39` | strb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aaddc4"></a> `00aaddc4` | `e8 43 01 39` | strb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00aaddc8"></a> `00aaddc8` | `e8 c3 01 39` | strb w8,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00aaddcc"></a> `00aaddcc` | `e8 43 02 39` | strb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00aaddd0"></a> `00aaddd0` | `e8 c3 02 39` | strb w8,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00aaddd4"></a> `00aaddd4` | `e8 43 03 39` | strb w8,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-00aaddd8"></a> `00aaddd8` | `68 28 88 52` | mov w8,#0x4143 | `FALL_THROUGH`
<a id="insn-00aadddc"></a> `00aadddc` | `ff 0b 00 b9` | str wzr,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00aadde0"></a> `00aadde0` | `ff 8f 00 39` | strb wzr,[sp, #0x23] | `FALL_THROUGH`
<a id="insn-00aadde4"></a> `00aadde4` | `ff 0f 01 39` | strb wzr,[sp, #0x43] | `FALL_THROUGH`
<a id="insn-00aadde8"></a> `00aadde8` | `ff 8f 01 39` | strb wzr,[sp, #0x63] | `FALL_THROUGH`
<a id="insn-00aaddec"></a> `00aaddec` | `ff 0f 02 39` | strb wzr,[sp, #0x83] | `FALL_THROUGH`
<a id="insn-00aaddf0"></a> `00aaddf0` | `ff 8f 02 39` | strb wzr,[sp, #0xa3] | `FALL_THROUGH`
<a id="insn-00aaddf4"></a> `00aaddf4` | `ff 0f 03 39` | strb wzr,[sp, #0xc3] | `FALL_THROUGH`
<a id="insn-00aaddf8"></a> `00aaddf8` | `88 92 0d 78` | sturh w8,[x20, #0xd9] | `FALL_THROUGH`
<a id="insn-00aaddfc"></a> `00aaddfc` | `80 92 8c 3c` | stur q0,[x20, #0xc9] | `FALL_THROUGH`
<a id="insn-00aade00"></a> `00aade00` | `ff 8f 03 39` | strb wzr,[sp, #0xe3] | `FALL_THROUGH`
<a id="insn-00aade04"></a> `00aade04` | `7f 0a 00 f9` | str xzr,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00aade08"></a> `00aade08` | `3f 8c 00 f8` | str xzr,[x1, #0x8]! | `FALL_THROUGH`
<a id="insn-00aade0c"></a> `00aade0c` | `61 02 00 f9` | str x1,[x19] | `FALL_THROUGH`
<a id="insn-00aade10"></a> `00aade10` | `e2 23 00 91` | add x2,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00aade14"></a> `00aade14` | `e3 23 00 91` | add x3,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00aade18"></a> `00aade18` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aade1c"></a> `00aade1c` | `a7 ab e5 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-00aade20"></a> `00aade20` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00aade24"></a> `00aade24` | `82 82 00 91` | add x2,x20,#0x20 | `FALL_THROUGH`
<a id="insn-00aade28"></a> `00aade28` | `83 82 00 91` | add x3,x20,#0x20 | `FALL_THROUGH`
<a id="insn-00aade2c"></a> `00aade2c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aade30"></a> `00aade30` | `a2 ab e5 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-00aade34"></a> `00aade34` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00aade38"></a> `00aade38` | `82 02 01 91` | add x2,x20,#0x40 | `FALL_THROUGH`
<a id="insn-00aade3c"></a> `00aade3c` | `83 02 01 91` | add x3,x20,#0x40 | `FALL_THROUGH`
<a id="insn-00aade40"></a> `00aade40` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aade44"></a> `00aade44` | `9d ab e5 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-00aade48"></a> `00aade48` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00aade4c"></a> `00aade4c` | `82 82 01 91` | add x2,x20,#0x60 | `FALL_THROUGH`
<a id="insn-00aade50"></a> `00aade50` | `83 82 01 91` | add x3,x20,#0x60 | `FALL_THROUGH`
<a id="insn-00aade54"></a> `00aade54` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aade58"></a> `00aade58` | `98 ab e5 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-00aade5c"></a> `00aade5c` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00aade60"></a> `00aade60` | `82 02 02 91` | add x2,x20,#0x80 | `FALL_THROUGH`
<a id="insn-00aade64"></a> `00aade64` | `83 02 02 91` | add x3,x20,#0x80 | `FALL_THROUGH`
<a id="insn-00aade68"></a> `00aade68` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aade6c"></a> `00aade6c` | `93 ab e5 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-00aade70"></a> `00aade70` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00aade74"></a> `00aade74` | `82 82 02 91` | add x2,x20,#0xa0 | `FALL_THROUGH`
<a id="insn-00aade78"></a> `00aade78` | `83 82 02 91` | add x3,x20,#0xa0 | `FALL_THROUGH`
<a id="insn-00aade7c"></a> `00aade7c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aade80"></a> `00aade80` | `8e ab e5 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-00aade84"></a> `00aade84` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00aade88"></a> `00aade88` | `82 02 03 91` | add x2,x20,#0xc0 | `FALL_THROUGH`
<a id="insn-00aade8c"></a> `00aade8c` | `83 02 03 91` | add x3,x20,#0xc0 | `FALL_THROUGH`
<a id="insn-00aade90"></a> `00aade90` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aade94"></a> `00aade94` | `89 ab e5 97` | bl 0x00418cb8 | `UNCONDITIONAL_CALL`
<a id="insn-00aade98"></a> `00aade98` | `e8 43 43 39` | ldrb w8,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-00aade9c"></a> `00aade9c` | `e8 03 00 37` | tbnz w8,#0x0,0x00aadf18 | `CONDITIONAL_JUMP`
<a id="insn-00aadea0"></a> `00aadea0` | `e8 c3 42 39` | ldrb w8,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00aadea4"></a> `00aadea4` | `28 04 00 37` | tbnz w8,#0x0,0x00aadf28 | `CONDITIONAL_JUMP`
<a id="insn-00aadea8"></a> `00aadea8` | `e8 43 42 39` | ldrb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00aadeac"></a> `00aadeac` | `68 04 00 37` | tbnz w8,#0x0,0x00aadf38 | `CONDITIONAL_JUMP`
<a id="insn-00aadeb0"></a> `00aadeb0` | `e8 c3 41 39` | ldrb w8,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00aadeb4"></a> `00aadeb4` | `a8 04 00 37` | tbnz w8,#0x0,0x00aadf48 | `CONDITIONAL_JUMP`
<a id="insn-00aadeb8"></a> `00aadeb8` | `e8 43 41 39` | ldrb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00aadebc"></a> `00aadebc` | `e8 04 00 37` | tbnz w8,#0x0,0x00aadf58 | `CONDITIONAL_JUMP`
<a id="insn-00aadec0"></a> `00aadec0` | `e8 c3 40 39` | ldrb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aadec4"></a> `00aadec4` | `28 05 00 37` | tbnz w8,#0x0,0x00aadf68 | `CONDITIONAL_JUMP`
<a id="insn-00aadec8"></a> `00aadec8` | `e8 43 40 39` | ldrb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aadecc"></a> `00aadecc` | `68 00 00 36` | tbz w8,#0x0,0x00aaded8 | `CONDITIONAL_JUMP`
<a id="insn-00aaded0"></a> `00aaded0` | `e0 13 40 f9` | ldr x0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aaded4"></a> `00aaded4` | `63 b4 04 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00aaded8"></a> `00aaded8` | `40 cb ff f0` | adrp x0,0x418000 | `FALL_THROUGH`
<a id="insn-00aadedc"></a> `00aadedc` | `00 c0 0c 91` | add x0,x0,#0x330 | `FALL_THROUGH`
<a id="insn-00aadee0"></a> `00aadee0` | `81 2f 00 d0` | adrp x1,0x109f000 | `FALL_THROUGH`
<a id="insn-00aadee4"></a> `00aadee4` | `21 80 2b 91` | add x1,x1,#0xae0 | `FALL_THROUGH`
<a id="insn-00aadee8"></a> `00aadee8` | `c2 09 00 90` | adrp x2,0xbe5000 | `FALL_THROUGH`
<a id="insn-00aadeec"></a> `00aadeec` | `42 40 3f 91` | add x2,x2,#0xfd0 | `FALL_THROUGH`
<a id="insn-00aadef0"></a> `00aadef0` | `3c b4 04 94` | bl 0x00bdafe0 | `UNCONDITIONAL_CALL`
<a id="insn-00aadef4"></a> `00aadef4` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00aadef8"></a> `00aadef8` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aadefc"></a> `00aadefc` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00aadf00"></a> `00aadf00` | `41 0a 00 54` | b.ne 0x00aae048 | `CONDITIONAL_JUMP`
<a id="insn-00aadf04"></a> `00aadf04` | `f4 4f 51 a9` | ldp x20,x19,[sp, #0x110] | `FALL_THROUGH`
<a id="insn-00aadf08"></a> `00aadf08` | `fc 57 50 a9` | ldp x28,x21,[sp, #0x100] | `FALL_THROUGH`
<a id="insn-00aadf0c"></a> `00aadf0c` | `fd 7b 4f a9` | ldp x29,x30,[sp, #0xf0] | `FALL_THROUGH`
<a id="insn-00aadf10"></a> `00aadf10` | `ff 83 04 91` | add sp,sp,#0x120 | `FALL_THROUGH`
<a id="insn-00aadf14"></a> `00aadf14` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00aadf18"></a> `00aadf18` | `e0 73 40 f9` | ldr x0,[sp, #0xe0] | `FALL_THROUGH`
<a id="insn-00aadf1c"></a> `00aadf1c` | `51 b4 04 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00aadf20"></a> `00aadf20` | `e8 c3 42 39` | ldrb w8,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00aadf24"></a> `00aadf24` | `28 fc 07 36` | tbz w8,#0x0,0x00aadea8 | `CONDITIONAL_JUMP`
<a id="insn-00aadf28"></a> `00aadf28` | `e0 63 40 f9` | ldr x0,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00aadf2c"></a> `00aadf2c` | `4d b4 04 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00aadf30"></a> `00aadf30` | `e8 43 42 39` | ldrb w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00aadf34"></a> `00aadf34` | `e8 fb 07 36` | tbz w8,#0x0,0x00aadeb0 | `CONDITIONAL_JUMP`
<a id="insn-00aadf38"></a> `00aadf38` | `e0 53 40 f9` | ldr x0,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00aadf3c"></a> `00aadf3c` | `49 b4 04 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00aadf40"></a> `00aadf40` | `e8 c3 41 39` | ldrb w8,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00aadf44"></a> `00aadf44` | `a8 fb 07 36` | tbz w8,#0x0,0x00aadeb8 | `CONDITIONAL_JUMP`
<a id="insn-00aadf48"></a> `00aadf48` | `e0 43 40 f9` | ldr x0,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00aadf4c"></a> `00aadf4c` | `45 b4 04 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00aadf50"></a> `00aadf50` | `e8 43 41 39` | ldrb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00aadf54"></a> `00aadf54` | `68 fb 07 36` | tbz w8,#0x0,0x00aadec0 | `CONDITIONAL_JUMP`
<a id="insn-00aadf58"></a> `00aadf58` | `e0 33 40 f9` | ldr x0,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00aadf5c"></a> `00aadf5c` | `41 b4 04 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00aadf60"></a> `00aadf60` | `e8 c3 40 39` | ldrb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aadf64"></a> `00aadf64` | `28 fb 07 36` | tbz w8,#0x0,0x00aadec8 | `CONDITIONAL_JUMP`
<a id="insn-00aadf68"></a> `00aadf68` | `e0 23 40 f9` | ldr x0,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00aadf6c"></a> `00aadf6c` | `3d b4 04 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00aadf70"></a> `00aadf70` | `e8 43 40 39` | ldrb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aadf74"></a> `00aadf74` | `e8 fa 07 37` | tbnz w8,#0x0,0x00aaded0 | `CONDITIONAL_JUMP`
<a id="insn-00aadf78"></a> `00aadf78` | `d8 ff ff 17` | b 0x00aaded8 | `UNCONDITIONAL_JUMP`
<a id="insn-00aae048"></a> `00aae048` | `12 b4 04 94` | bl 0x00bdb090 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aadcbc`](#insn-00aadcbc) 範囲 `[['00aadcbc', '00aade9f']]`
  - `CONDITIONAL_JUMP` [`00aade9c`](#insn-00aade9c) → [`00aadf18`](#insn-00aadf18)
  - `FALL_THROUGH` [`00aade9c`](#insn-00aade9c) → [`00aadea0`](#insn-00aadea0)
- ブロック [`00aadea0`](#insn-00aadea0) 範囲 `[['00aadea0', '00aadea7']]`
  - `CONDITIONAL_JUMP` [`00aadea4`](#insn-00aadea4) → [`00aadf28`](#insn-00aadf28)
  - `FALL_THROUGH` [`00aadea4`](#insn-00aadea4) → [`00aadea8`](#insn-00aadea8)
- ブロック [`00aadea8`](#insn-00aadea8) 範囲 `[['00aadea8', '00aadeaf']]`
  - `CONDITIONAL_JUMP` [`00aadeac`](#insn-00aadeac) → [`00aadf38`](#insn-00aadf38)
  - `FALL_THROUGH` [`00aadeac`](#insn-00aadeac) → [`00aadeb0`](#insn-00aadeb0)
- ブロック [`00aadeb0`](#insn-00aadeb0) 範囲 `[['00aadeb0', '00aadeb7']]`
  - `CONDITIONAL_JUMP` [`00aadeb4`](#insn-00aadeb4) → [`00aadf48`](#insn-00aadf48)
  - `FALL_THROUGH` [`00aadeb4`](#insn-00aadeb4) → [`00aadeb8`](#insn-00aadeb8)
- ブロック [`00aadeb8`](#insn-00aadeb8) 範囲 `[['00aadeb8', '00aadebf']]`
  - `CONDITIONAL_JUMP` [`00aadebc`](#insn-00aadebc) → [`00aadf58`](#insn-00aadf58)
  - `FALL_THROUGH` [`00aadebc`](#insn-00aadebc) → [`00aadec0`](#insn-00aadec0)
- ブロック [`00aadec0`](#insn-00aadec0) 範囲 `[['00aadec0', '00aadec7']]`
  - `CONDITIONAL_JUMP` [`00aadec4`](#insn-00aadec4) → [`00aadf68`](#insn-00aadf68)
  - `FALL_THROUGH` [`00aadec4`](#insn-00aadec4) → [`00aadec8`](#insn-00aadec8)
- ブロック [`00aadec8`](#insn-00aadec8) 範囲 `[['00aadec8', '00aadecf']]`
  - `CONDITIONAL_JUMP` [`00aadecc`](#insn-00aadecc) → [`00aaded8`](#insn-00aaded8)
  - `FALL_THROUGH` [`00aadecc`](#insn-00aadecc) → [`00aaded0`](#insn-00aaded0)
- ブロック [`00aaded0`](#insn-00aaded0) 範囲 `[['00aaded0', '00aaded7']]`
  - `FALL_THROUGH` [`00aaded4`](#insn-00aaded4) → [`00aaded8`](#insn-00aaded8)
- ブロック [`00aaded8`](#insn-00aaded8) 範囲 `[['00aaded8', '00aadf03']]`
  - `CONDITIONAL_JUMP` [`00aadf00`](#insn-00aadf00) → [`00aae048`](#insn-00aae048)
  - `FALL_THROUGH` [`00aadf00`](#insn-00aadf00) → [`00aadf04`](#insn-00aadf04)
- ブロック [`00aadf04`](#insn-00aadf04) 範囲 `[['00aadf04', '00aadf17']]`
- ブロック [`00aadf18`](#insn-00aadf18) 範囲 `[['00aadf18', '00aadf27']]`
  - `CONDITIONAL_JUMP` [`00aadf24`](#insn-00aadf24) → [`00aadea8`](#insn-00aadea8)
  - `FALL_THROUGH` [`00aadf24`](#insn-00aadf24) → [`00aadf28`](#insn-00aadf28)
- ブロック [`00aadf28`](#insn-00aadf28) 範囲 `[['00aadf28', '00aadf37']]`
  - `CONDITIONAL_JUMP` [`00aadf34`](#insn-00aadf34) → [`00aadeb0`](#insn-00aadeb0)
  - `FALL_THROUGH` [`00aadf34`](#insn-00aadf34) → [`00aadf38`](#insn-00aadf38)
- ブロック [`00aadf38`](#insn-00aadf38) 範囲 `[['00aadf38', '00aadf47']]`
  - `CONDITIONAL_JUMP` [`00aadf44`](#insn-00aadf44) → [`00aadeb8`](#insn-00aadeb8)
  - `FALL_THROUGH` [`00aadf44`](#insn-00aadf44) → [`00aadf48`](#insn-00aadf48)
- ブロック [`00aadf48`](#insn-00aadf48) 範囲 `[['00aadf48', '00aadf57']]`
  - `CONDITIONAL_JUMP` [`00aadf54`](#insn-00aadf54) → [`00aadec0`](#insn-00aadec0)
  - `FALL_THROUGH` [`00aadf54`](#insn-00aadf54) → [`00aadf58`](#insn-00aadf58)
- ブロック [`00aadf58`](#insn-00aadf58) 範囲 `[['00aadf58', '00aadf67']]`
  - `CONDITIONAL_JUMP` [`00aadf64`](#insn-00aadf64) → [`00aadec8`](#insn-00aadec8)
  - `FALL_THROUGH` [`00aadf64`](#insn-00aadf64) → [`00aadf68`](#insn-00aadf68)
- ブロック [`00aadf68`](#insn-00aadf68) 範囲 `[['00aadf68', '00aadf77']]`
  - `CONDITIONAL_JUMP` [`00aadf74`](#insn-00aadf74) → [`00aaded0`](#insn-00aaded0)
  - `FALL_THROUGH` [`00aadf74`](#insn-00aadf74) → [`00aadf78`](#insn-00aadf78)
- ブロック [`00aadf78`](#insn-00aadf78) 範囲 `[['00aadf78', '00aadf7b']]`
  - `UNCONDITIONAL_JUMP` [`00aadf78`](#insn-00aadf78) → [`00aaded8`](#insn-00aaded8)
- ブロック [`00aae048`](#insn-00aae048) 範囲 `[['00aae048', '00aae04b']]`

## 命令位置別の参照

- [`00aadcc0`](#insn-00aadcc0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadcc4`](#insn-00aadcc4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadcc8`](#insn-00aadcc8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadcec`](#insn-00aadcec) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadcf8`](#insn-00aadcf8) → `002a7377`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aadd00`](#insn-00aadd00) → `Stack[-0xff]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadd04`](#insn-00aadd04) → `Stack[-0xf8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadd14`](#insn-00aadd14) → `Stack[-0x10f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadd1c`](#insn-00aadd1c) → `002a738a`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aadd20`](#insn-00aadd20) → `Stack[-0xdf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadd28`](#insn-00aadd28) → `Stack[-0xd8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadd38`](#insn-00aadd38) → `Stack[-0xef]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadd3c`](#insn-00aadd3c) → `002a80e0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aadd40`](#insn-00aadd40) → `Stack[-0xbf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadd48`](#insn-00aadd48) → `Stack[-0xb8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadd58`](#insn-00aadd58) → `Stack[-0xcf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadd5c`](#insn-00aadd5c) → `002936ae`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aadd60`](#insn-00aadd60) → `Stack[-0x9f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadd68`](#insn-00aadd68) → `Stack[-0x98]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadd74`](#insn-00aadd74) → `Stack[-0xaf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadd78`](#insn-00aadd78) → `0029c36c`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aadd80`](#insn-00aadd80) → `Stack[-0x7f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadd88`](#insn-00aadd88) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadd94`](#insn-00aadd94) → `Stack[-0x8f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadd98`](#insn-00aadd98) → `00291877`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aadda0`](#insn-00aadda0) → `Stack[-0x5f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadda8`](#insn-00aadda8) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaddb4`](#insn-00aaddb4) → `Stack[-0x6f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaddb8`](#insn-00aaddb8) → `00294526`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aaddbc`](#insn-00aaddbc) → `Stack[-0x110]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaddc0`](#insn-00aaddc0) → `Stack[-0xf0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaddc4`](#insn-00aaddc4) → `Stack[-0xd0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaddc8`](#insn-00aaddc8) → `Stack[-0xb0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaddcc`](#insn-00aaddcc) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaddd0`](#insn-00aaddd0) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaddd4`](#insn-00aaddd4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadddc`](#insn-00aadddc) → `Stack[-0x118]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadde0`](#insn-00aadde0) → `Stack[-0xfd]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadde4`](#insn-00aadde4) → `Stack[-0xdd]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadde8`](#insn-00aadde8) → `Stack[-0xbd]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaddec`](#insn-00aaddec) → `Stack[-0x9d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaddf0`](#insn-00aaddf0) → `Stack[-0x7d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaddf4`](#insn-00aaddf4) → `Stack[-0x5d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaddf8`](#insn-00aaddf8) → `Stack[-0x3f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaddfc`](#insn-00aaddfc) → `Stack[-0x4f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aade00`](#insn-00aade00) → `Stack[-0x3d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aade04`](#insn-00aade04) → `0109faf0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aade08`](#insn-00aade08) → `0109fae8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aade0c`](#insn-00aade0c) → `0109fae0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aade0c`](#insn-00aade0c) → `0109fae8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aade18`](#insn-00aade18) → `0109fae0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aade1c`](#insn-00aade1c) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`00aade20`](#insn-00aade20) → `0109fae8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aade2c`](#insn-00aade2c) → `0109fae0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aade30`](#insn-00aade30) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`00aade34`](#insn-00aade34) → `0109fae8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aade40`](#insn-00aade40) → `0109fae0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aade44`](#insn-00aade44) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`00aade48`](#insn-00aade48) → `0109fae8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aade54`](#insn-00aade54) → `0109fae0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aade58`](#insn-00aade58) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`00aade5c`](#insn-00aade5c) → `0109fae8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aade68`](#insn-00aade68) → `0109fae0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aade6c`](#insn-00aade6c) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`00aade70`](#insn-00aade70) → `0109fae8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aade7c`](#insn-00aade7c) → `0109fae0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aade80`](#insn-00aade80) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`00aade84`](#insn-00aade84) → `0109fae8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aade90`](#insn-00aade90) → `0109fae0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aade94`](#insn-00aade94) → [`00418cb8`](../00418/00418cb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418cb8` · 推定シンボル `None` · 推定型 `None`
- [`00aade98`](#insn-00aade98) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aade9c`](#insn-00aade9c) → [`00aadf18`](#insn-00aadf18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadea0`](#insn-00aadea0) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadea4`](#insn-00aadea4) → [`00aadf28`](#insn-00aadf28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadea8`](#insn-00aadea8) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadeac`](#insn-00aadeac) → [`00aadf38`](#insn-00aadf38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadeb0`](#insn-00aadeb0) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadeb4`](#insn-00aadeb4) → [`00aadf48`](#insn-00aadf48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadeb8`](#insn-00aadeb8) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadebc`](#insn-00aadebc) → [`00aadf58`](#insn-00aadf58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadec0`](#insn-00aadec0) → `Stack[-0xf0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadec4`](#insn-00aadec4) → [`00aadf68`](#insn-00aadf68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadec8`](#insn-00aadec8) → `Stack[-0x110]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadecc`](#insn-00aadecc) → [`00aaded8`](#insn-00aaded8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaded0`](#insn-00aaded0) → `Stack[-0x100]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaded4`](#insn-00aaded4) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00aadedc`](#insn-00aadedc) → [`00418330`](../00418/00418330.md) · `PARAM` · `ANALYSIS` · 関数 `00418330` · 推定シンボル `None` · 推定型 `None`
- [`00aadee4`](#insn-00aadee4) → `0109fae0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aadeec`](#insn-00aadeec) → `00be5fd0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00aadef0`](#insn-00aadef0) → [`00bdafe0`](../00bda/00bdafe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdafe0` · 推定シンボル `None` · 推定型 `None`
- [`00aadef8`](#insn-00aadef8) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadf00`](#insn-00aadf00) → [`00aae048`](#insn-00aae048) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadf04`](#insn-00aadf04) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadf08`](#insn-00aadf08) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadf0c`](#insn-00aadf0c) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadf18`](#insn-00aadf18) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadf1c`](#insn-00aadf1c) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00aadf20`](#insn-00aadf20) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadf24`](#insn-00aadf24) → [`00aadea8`](#insn-00aadea8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadf28`](#insn-00aadf28) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadf2c`](#insn-00aadf2c) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00aadf30`](#insn-00aadf30) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadf34`](#insn-00aadf34) → [`00aadeb0`](#insn-00aadeb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadf38`](#insn-00aadf38) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadf3c`](#insn-00aadf3c) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00aadf40`](#insn-00aadf40) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadf44`](#insn-00aadf44) → [`00aadeb8`](#insn-00aadeb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadf48`](#insn-00aadf48) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadf4c`](#insn-00aadf4c) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00aadf50`](#insn-00aadf50) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadf54`](#insn-00aadf54) → [`00aadec0`](#insn-00aadec0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadf58`](#insn-00aadf58) → `Stack[-0xc0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadf5c`](#insn-00aadf5c) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00aadf60`](#insn-00aadf60) → `Stack[-0xf0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadf64`](#insn-00aadf64) → [`00aadec8`](#insn-00aadec8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadf68`](#insn-00aadf68) → `Stack[-0xe0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadf6c`](#insn-00aadf6c) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00aadf70`](#insn-00aadf70) → `Stack[-0x110]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadf74`](#insn-00aadf74) → [`00aaded0`](#insn-00aaded0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadf78`](#insn-00aadf78) → [`00aaded8`](#insn-00aaded8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae048`](#insn-00aae048) → [`00bdb090`](../00bdb/00bdb090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb090` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aadcc0`](#insn-00aadcc0)

~~~json
{
  "source": "00aadcc0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadcc4`](#insn-00aadcc4)

~~~json
{
  "source": "00aadcc4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadcc8`](#insn-00aadcc8)

~~~json
{
  "source": "00aadcc8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadcec`](#insn-00aadcec)

~~~json
{
  "source": "00aadcec",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadcf8`](#insn-00aadcf8)

~~~json
{
  "source": "00aadcf8",
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
- 参照命令 [`00aadd00`](#insn-00aadd00)

~~~json
{
  "source": "00aadd00",
  "target": "Stack[-0xff]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadd04`](#insn-00aadd04)

~~~json
{
  "source": "00aadd04",
  "target": "Stack[-0xf8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadd14`](#insn-00aadd14)

~~~json
{
  "source": "00aadd14",
  "target": "Stack[-0x10f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadd1c`](#insn-00aadd1c)

~~~json
{
  "source": "00aadd1c",
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
- 参照命令 [`00aadd20`](#insn-00aadd20)

~~~json
{
  "source": "00aadd20",
  "target": "Stack[-0xdf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadd28`](#insn-00aadd28)

~~~json
{
  "source": "00aadd28",
  "target": "Stack[-0xd8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadd38`](#insn-00aadd38)

~~~json
{
  "source": "00aadd38",
  "target": "Stack[-0xef]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadd3c`](#insn-00aadd3c)

~~~json
{
  "source": "00aadd3c",
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
- 参照命令 [`00aadd40`](#insn-00aadd40)

~~~json
{
  "source": "00aadd40",
  "target": "Stack[-0xbf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadd48`](#insn-00aadd48)

~~~json
{
  "source": "00aadd48",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadd58`](#insn-00aadd58)

~~~json
{
  "source": "00aadd58",
  "target": "Stack[-0xcf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadd5c`](#insn-00aadd5c)

~~~json
{
  "source": "00aadd5c",
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
- 参照命令 [`00aadd60`](#insn-00aadd60)

~~~json
{
  "source": "00aadd60",
  "target": "Stack[-0x9f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadd68`](#insn-00aadd68)

~~~json
{
  "source": "00aadd68",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadd74`](#insn-00aadd74)

~~~json
{
  "source": "00aadd74",
  "target": "Stack[-0xaf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadd78`](#insn-00aadd78)

~~~json
{
  "source": "00aadd78",
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
- 参照命令 [`00aadd80`](#insn-00aadd80)

~~~json
{
  "source": "00aadd80",
  "target": "Stack[-0x7f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadd88`](#insn-00aadd88)

~~~json
{
  "source": "00aadd88",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadd94`](#insn-00aadd94)

~~~json
{
  "source": "00aadd94",
  "target": "Stack[-0x8f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadd98`](#insn-00aadd98)

~~~json
{
  "source": "00aadd98",
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
- 参照命令 [`00aadda0`](#insn-00aadda0)

~~~json
{
  "source": "00aadda0",
  "target": "Stack[-0x5f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadda8`](#insn-00aadda8)

~~~json
{
  "source": "00aadda8",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaddb4`](#insn-00aaddb4)

~~~json
{
  "source": "00aaddb4",
  "target": "Stack[-0x6f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaddb8`](#insn-00aaddb8)

~~~json
{
  "source": "00aaddb8",
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
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaddc4`](#insn-00aaddc4)

~~~json
{
  "source": "00aaddc4",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaddc8`](#insn-00aaddc8)

~~~json
{
  "source": "00aaddc8",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaddcc`](#insn-00aaddcc)

~~~json
{
  "source": "00aaddcc",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaddd0`](#insn-00aaddd0)

~~~json
{
  "source": "00aaddd0",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaddd4`](#insn-00aaddd4)

~~~json
{
  "source": "00aaddd4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadddc`](#insn-00aadddc)

~~~json
{
  "source": "00aadddc",
  "target": "Stack[-0x118]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadde0`](#insn-00aadde0)

~~~json
{
  "source": "00aadde0",
  "target": "Stack[-0xfd]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadde4`](#insn-00aadde4)

~~~json
{
  "source": "00aadde4",
  "target": "Stack[-0xdd]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadde8`](#insn-00aadde8)

~~~json
{
  "source": "00aadde8",
  "target": "Stack[-0xbd]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaddec`](#insn-00aaddec)

~~~json
{
  "source": "00aaddec",
  "target": "Stack[-0x9d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaddf0`](#insn-00aaddf0)

~~~json
{
  "source": "00aaddf0",
  "target": "Stack[-0x7d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaddf4`](#insn-00aaddf4)

~~~json
{
  "source": "00aaddf4",
  "target": "Stack[-0x5d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaddf8`](#insn-00aaddf8)

~~~json
{
  "source": "00aaddf8",
  "target": "Stack[-0x3f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaddfc`](#insn-00aaddfc)

~~~json
{
  "source": "00aaddfc",
  "target": "Stack[-0x4f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aade00`](#insn-00aade00)

~~~json
{
  "source": "00aade00",
  "target": "Stack[-0x3d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aade04`](#insn-00aade04)

~~~json
{
  "source": "00aade04",
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
- 参照命令 [`00aade08`](#insn-00aade08)

~~~json
{
  "source": "00aade08",
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
- 参照命令 [`00aade0c`](#insn-00aade0c)

~~~json
{
  "source": "00aade0c",
  "target": "0109fae0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fae0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aade0c`](#insn-00aade0c)

~~~json
{
  "source": "00aade0c",
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
- 参照命令 [`00aade18`](#insn-00aade18)

~~~json
{
  "source": "00aade18",
  "target": "0109fae0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fae0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aade1c`](#insn-00aade1c)

~~~json
{
  "source": "00aade1c",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aade20`](#insn-00aade20)

~~~json
{
  "source": "00aade20",
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
- 参照命令 [`00aade2c`](#insn-00aade2c)

~~~json
{
  "source": "00aade2c",
  "target": "0109fae0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fae0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aade30`](#insn-00aade30)

~~~json
{
  "source": "00aade30",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aade34`](#insn-00aade34)

~~~json
{
  "source": "00aade34",
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
- 参照命令 [`00aade40`](#insn-00aade40)

~~~json
{
  "source": "00aade40",
  "target": "0109fae0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fae0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aade44`](#insn-00aade44)

~~~json
{
  "source": "00aade44",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aade48`](#insn-00aade48)

~~~json
{
  "source": "00aade48",
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
- 参照命令 [`00aade54`](#insn-00aade54)

~~~json
{
  "source": "00aade54",
  "target": "0109fae0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fae0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aade58`](#insn-00aade58)

~~~json
{
  "source": "00aade58",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aade5c`](#insn-00aade5c)

~~~json
{
  "source": "00aade5c",
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
- 参照命令 [`00aade68`](#insn-00aade68)

~~~json
{
  "source": "00aade68",
  "target": "0109fae0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fae0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aade6c`](#insn-00aade6c)

~~~json
{
  "source": "00aade6c",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aade70`](#insn-00aade70)

~~~json
{
  "source": "00aade70",
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
- 参照命令 [`00aade7c`](#insn-00aade7c)

~~~json
{
  "source": "00aade7c",
  "target": "0109fae0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fae0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aade80`](#insn-00aade80)

~~~json
{
  "source": "00aade80",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aade84`](#insn-00aade84)

~~~json
{
  "source": "00aade84",
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
- 参照命令 [`00aade90`](#insn-00aade90)

~~~json
{
  "source": "00aade90",
  "target": "0109fae0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fae0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aade94`](#insn-00aade94)

~~~json
{
  "source": "00aade94",
  "target": "00418cb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aade98`](#insn-00aade98)

~~~json
{
  "source": "00aade98",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aade9c`](#insn-00aade9c)

~~~json
{
  "source": "00aade9c",
  "target": "00aadf18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadea0`](#insn-00aadea0)

~~~json
{
  "source": "00aadea0",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadea4`](#insn-00aadea4)

~~~json
{
  "source": "00aadea4",
  "target": "00aadf28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadea8`](#insn-00aadea8)

~~~json
{
  "source": "00aadea8",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadeac`](#insn-00aadeac)

~~~json
{
  "source": "00aadeac",
  "target": "00aadf38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadeb0`](#insn-00aadeb0)

~~~json
{
  "source": "00aadeb0",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadeb4`](#insn-00aadeb4)

~~~json
{
  "source": "00aadeb4",
  "target": "00aadf48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadeb8`](#insn-00aadeb8)

~~~json
{
  "source": "00aadeb8",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadebc`](#insn-00aadebc)

~~~json
{
  "source": "00aadebc",
  "target": "00aadf58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadec0`](#insn-00aadec0)

~~~json
{
  "source": "00aadec0",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadec4`](#insn-00aadec4)

~~~json
{
  "source": "00aadec4",
  "target": "00aadf68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadec8`](#insn-00aadec8)

~~~json
{
  "source": "00aadec8",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadecc`](#insn-00aadecc)

~~~json
{
  "source": "00aadecc",
  "target": "00aaded8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaded0`](#insn-00aaded0)

~~~json
{
  "source": "00aaded0",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaded4`](#insn-00aaded4)

~~~json
{
  "source": "00aaded4",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aadedc`](#insn-00aadedc)

~~~json
{
  "source": "00aadedc",
  "target": "00418330",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aadee4`](#insn-00aadee4)

~~~json
{
  "source": "00aadee4",
  "target": "0109fae0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fae0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aadeec`](#insn-00aadeec)

~~~json
{
  "source": "00aadeec",
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
- 参照命令 [`00aadef0`](#insn-00aadef0)

~~~json
{
  "source": "00aadef0",
  "target": "00bdafe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aadef8`](#insn-00aadef8)

~~~json
{
  "source": "00aadef8",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadf00`](#insn-00aadf00)

~~~json
{
  "source": "00aadf00",
  "target": "00aae048",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadf04`](#insn-00aadf04)

~~~json
{
  "source": "00aadf04",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadf08`](#insn-00aadf08)

~~~json
{
  "source": "00aadf08",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadf0c`](#insn-00aadf0c)

~~~json
{
  "source": "00aadf0c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadf18`](#insn-00aadf18)

~~~json
{
  "source": "00aadf18",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadf1c`](#insn-00aadf1c)

~~~json
{
  "source": "00aadf1c",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aadf20`](#insn-00aadf20)

~~~json
{
  "source": "00aadf20",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadf24`](#insn-00aadf24)

~~~json
{
  "source": "00aadf24",
  "target": "00aadea8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadf28`](#insn-00aadf28)

~~~json
{
  "source": "00aadf28",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadf2c`](#insn-00aadf2c)

~~~json
{
  "source": "00aadf2c",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aadf30`](#insn-00aadf30)

~~~json
{
  "source": "00aadf30",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadf34`](#insn-00aadf34)

~~~json
{
  "source": "00aadf34",
  "target": "00aadeb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadf38`](#insn-00aadf38)

~~~json
{
  "source": "00aadf38",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadf3c`](#insn-00aadf3c)

~~~json
{
  "source": "00aadf3c",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aadf40`](#insn-00aadf40)

~~~json
{
  "source": "00aadf40",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadf44`](#insn-00aadf44)

~~~json
{
  "source": "00aadf44",
  "target": "00aadeb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadf48`](#insn-00aadf48)

~~~json
{
  "source": "00aadf48",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadf4c`](#insn-00aadf4c)

~~~json
{
  "source": "00aadf4c",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aadf50`](#insn-00aadf50)

~~~json
{
  "source": "00aadf50",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadf54`](#insn-00aadf54)

~~~json
{
  "source": "00aadf54",
  "target": "00aadec0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadf58`](#insn-00aadf58)

~~~json
{
  "source": "00aadf58",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadf5c`](#insn-00aadf5c)

~~~json
{
  "source": "00aadf5c",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aadf60`](#insn-00aadf60)

~~~json
{
  "source": "00aadf60",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadf64`](#insn-00aadf64)

~~~json
{
  "source": "00aadf64",
  "target": "00aadec8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadf68`](#insn-00aadf68)

~~~json
{
  "source": "00aadf68",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadf6c`](#insn-00aadf6c)

~~~json
{
  "source": "00aadf6c",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aadf70`](#insn-00aadf70)

~~~json
{
  "source": "00aadf70",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadf74`](#insn-00aadf74)

~~~json
{
  "source": "00aadf74",
  "target": "00aaded0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadf78`](#insn-00aadf78)

~~~json
{
  "source": "00aadf78",
  "target": "00aaded8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae048`](#insn-00aae048)

~~~json
{
  "source": "00aae048",
  "target": "00bdb090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
