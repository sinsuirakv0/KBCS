# 00b1ddcc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00b1de94`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1d/00b1de94.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0064.md#compare-41004b0d913d8d1146f7fb11a25f2f80)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b1ddcc",
  "name": "_ZN11flatbuffers11NumToStringIsEENSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEET_",
  "size": 364,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c3939e43a52431355417c539f8eb930c58825d255132f7d304d46ce15549cca0",
  "source_text_sha256": "c3939e43a52431355417c539f8eb930c58825d255132f7d304d46ce15549cca0",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b1ddcc",
        "00b1df37"
      ]
    ],
    "bytes_sha256": "309e8d84bc2b46188346f4ec1973a477ef94643a397715b4c86dcf3ee2f077d3",
    "instruction_count": 91,
    "instruction_bytes": 364,
    "body_bytes": 364,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bdf0e0](../00bdf/00bdf0e0.md)

## 呼び出し先

- [00bdaf60](../00bda/00bdaf60.md)
- [00bdaf90](../00bda/00bdaf90.md)
- [00bdb260](../00bdb/00bdb260.md)
- [00bdb290](../00bdb/00bdb290.md)
- [00bdb340](../00bdb/00bdb340.md)
- [00bdd850](../00bdd/00bdd850.md)
- [00bdfc00](../00bdf/00bdfc00.md)
- [00be00e0](../00be0/00be00e0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2753 bytes

~~~c

void _ZN11flatbuffers11NumToStringIsEENSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEET_
               (undefined8 param_1,undefined4 param_2)

{
  undefined *puVar1;
  undefined *puVar2;
  undefined *puVar3;
  undefined *puVar4;
  long lVar5;
  undefined *local_180;
  undefined *puStack_178;
  undefined1 auStack_170 [8];
  undefined8 local_168;
  undefined8 uStack_160;
  undefined8 local_158;
  undefined8 uStack_150;
  undefined8 local_148;
  undefined8 uStack_140;
  ulong local_138;
  undefined8 uStack_130;
  void *local_128;
  undefined8 uStack_120;
  undefined4 local_118;
  undefined *local_110 [17];
  undefined8 local_88;
  undefined4 local_80;
  long local_70;
  
  puVar2 = PTR__ZTVNSt6__ndk118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c1ad28;
  lVar5 = tpidr_el0;
                    /* try { // try from 00b1de00 to 00c1df17 has its CatchHandler @ 00b1de00
                       catch() { ... } // from try @ 00b1de00 with catch @ 00b1de00
                       catch() { ... } // from try @ 00b1df58 with catch @ 00b1de00 */
  local_70 = *(long *)(lVar5 + 0x28);
  puVar1 = PTR__ZTVNSt6__ndk118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c1ad28
           + 0x40;
  local_110[0] = PTR__ZTCNSt6__ndk118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE0_NS_13basic_istreamIcS2_EE_00c1b948
                 + 0x40;
  local_180 = puVar1;
  _ZNSt6__ndk18ios_base4initEPv(local_110,&puStack_178);
  puVar2 = puVar2 + 0x68;
  puVar3 = PTR__ZTVNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEEE_00c1b950 + 0x10;
  local_80 = 0xffffffff;
  local_88 = 0;
  local_180 = puVar1;
  puStack_178 = puVar3;
  local_110[0] = puVar2;
  _ZNSt6__ndk16localeC1Ev(auStack_170);
  uStack_140 = 0;
  local_148 = 0;
  uStack_150 = 0;
  local_158 = 0;
  uStack_160 = 0;
  local_168 = 0;
  puVar4 = PTR__ZTVNSt6__ndk115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c1acd0 +
           0x10;
  uStack_130 = 0;
  local_138 = 0;
  uStack_120 = 0;
  local_128 = (void *)0x0;
  local_118 = 0x18;
  puStack_178 = puVar4;
  _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEs(&local_180,param_2);
  _ZNKSt6__ndk115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE3strEv(param_1,&puStack_178)
  ;
  local_180 = puVar1;
  local_110[0] = puVar2;
  if ((local_138 & 1) != 0) {
    puStack_178 = puVar4;
    _ZdlPv(local_128);
  }
  puStack_178 = puVar3;
  _ZNSt6__ndk16localeD2Ev(auStack_170);
  _ZNSt6__ndk18ios_baseD1Ev(local_110);
  if (*(long *)(lVar5 + 0x28) == local_70) {
                    /* try { // try from 00b1df18 to 00c1df23 has its CatchHandler @ 00b1e04c */
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
<a id="insn-00b1ddcc"></a> `00b1ddcc` | `ff 83 06 d1` | sub sp,sp,#0x1a0 | `FALL_THROUGH`
<a id="insn-00b1ddd0"></a> `00b1ddd0` | `fc 6f 14 a9` | stp x28,x27,[sp, #0x140] | `FALL_THROUGH`
<a id="insn-00b1ddd4"></a> `00b1ddd4` | `fa 67 15 a9` | stp x26,x25,[sp, #0x150] | `FALL_THROUGH`
<a id="insn-00b1ddd8"></a> `00b1ddd8` | `f8 5f 16 a9` | stp x24,x23,[sp, #0x160] | `FALL_THROUGH`
<a id="insn-00b1dddc"></a> `00b1dddc` | `f6 57 17 a9` | stp x22,x21,[sp, #0x170] | `FALL_THROUGH`
<a id="insn-00b1dde0"></a> `00b1dde0` | `f4 4f 18 a9` | stp x20,x19,[sp, #0x180] | `FALL_THROUGH`
<a id="insn-00b1dde4"></a> `00b1dde4` | `fd 7b 19 a9` | stp x29,x30,[sp, #0x190] | `FALL_THROUGH`
<a id="insn-00b1dde8"></a> `00b1dde8` | `fd 43 06 91` | add x29,sp,#0x190 | `FALL_THROUGH`
<a id="insn-00b1ddec"></a> `00b1ddec` | `e8 07 00 f9` | str x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00b1ddf0"></a> `00b1ddf0` | `fa 07 00 b0` | adrp x26,0xc1a000 | `FALL_THROUGH`
<a id="insn-00b1ddf4"></a> `00b1ddf4` | `e8 07 00 d0` | adrp x8,0xc1b000 | `FALL_THROUGH`
<a id="insn-00b1ddf8"></a> `00b1ddf8` | `e0 07 00 b9` | str w0,[sp, #0x4] | `FALL_THROUGH`
<a id="insn-00b1ddfc"></a> `00b1ddfc` | `59 d0 3b d5` | mrs x25,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00b1de00"></a> `00b1de00` | `5a 97 46 f9` | ldr x26,[x26, #0xd28] | `FALL_THROUGH`
<a id="insn-00b1de04"></a> `00b1de04` | `08 a5 44 f9` | ldr x8,[x8, #0x948] | `FALL_THROUGH`
<a id="insn-00b1de08"></a> `00b1de08` | `29 17 40 f9` | ldr x9,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-00b1de0c"></a> `00b1de0c` | `f4 43 00 91` | add x20,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00b1de10"></a> `00b1de10` | `00 e4 00 6f` | movi v0.2D,#0x0 | `FALL_THROUGH`
<a id="insn-00b1de14"></a> `00b1de14` | `93 02 02 91` | add x19,x20,#0x80 | `FALL_THROUGH`
<a id="insn-00b1de18"></a> `00b1de18` | `0a 61 00 91` | add x10,x8,#0x18 | `FALL_THROUGH`
<a id="insn-00b1de1c"></a> `00b1de1c` | `98 62 00 91` | add x24,x20,#0x18 | `FALL_THROUGH`
<a id="insn-00b1de20"></a> `00b1de20` | `5b 03 01 91` | add x27,x26,#0x40 | `FALL_THROUGH`
<a id="insn-00b1de24"></a> `00b1de24` | `40 1d 08 4e` | mov v0.D[0x0],x10 | `FALL_THROUGH`
<a id="insn-00b1de28"></a> `00b1de28` | `08 01 01 91` | add x8,x8,#0x40 | `FALL_THROUGH`
<a id="insn-00b1de2c"></a> `00b1de2c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b1de30"></a> `00b1de30` | `e1 03 18 aa` | mov x1,x24 | `FALL_THROUGH`
<a id="insn-00b1de34"></a> `00b1de34` | `97 42 00 91` | add x23,x20,#0x10 | `FALL_THROUGH`
<a id="insn-00b1de38"></a> `00b1de38` | `a9 03 1a f8` | stur x9,[x29, #-0x60] | `FALL_THROUGH`
<a id="insn-00b1de3c"></a> `00b1de3c` | `e8 4b 00 f9` | str x8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00b1de40"></a> `00b1de40` | `fb 13 00 f9` | str x27,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b1de44"></a> `00b1de44` | `e0 07 80 3d` | str q0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b1de48"></a> `00b1de48` | `12 f5 02 94` | bl 0x00bdb290 | `UNCONDITIONAL_CALL`
<a id="insn-00b1de4c"></a> `00b1de4c` | `e9 07 00 d0` | adrp x9,0xc1b000 | `FALL_THROUGH`
<a id="insn-00b1de50"></a> `00b1de50` | `29 a9 44 f9` | ldr x9,[x9, #0x950] | `FALL_THROUGH`
<a id="insn-00b1de54"></a> `00b1de54` | `5c 63 00 91` | add x28,x26,#0x18 | `FALL_THROUGH`
<a id="insn-00b1de58"></a> `00b1de58` | `56 a3 01 91` | add x22,x26,#0x68 | `FALL_THROUGH`
<a id="insn-00b1de5c"></a> `00b1de5c` | `60 03 67 9e` | fmov d0,x27 | `FALL_THROUGH`
<a id="insn-00b1de60"></a> `00b1de60` | `3a 41 00 91` | add x26,x9,#0x10 | `FALL_THROUGH`
<a id="insn-00b1de64"></a> `00b1de64` | `94 82 00 91` | add x20,x20,#0x20 | `FALL_THROUGH`
<a id="insn-00b1de68"></a> `00b1de68` | `08 00 80 12` | mov w8,#0xffffffff | `FALL_THROUGH`
<a id="insn-00b1de6c"></a> `00b1de6c` | `40 1f 18 4e` | mov v0.D[0x1],x26 | `FALL_THROUGH`
<a id="insn-00b1de70"></a> `00b1de70` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b1de74"></a> `00b1de74` | `e8 23 01 b9` | str w8,[sp, #0x120] | `FALL_THROUGH`
<a id="insn-00b1de78"></a> `00b1de78` | `fc 0b 00 f9` | str x28,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b1de7c"></a> `00b1de7c` | `ff 8f 00 f9` | str xzr,[sp, #0x118] | `FALL_THROUGH`
<a id="insn-00b1de80"></a> `00b1de80` | `f6 4b 00 f9` | str x22,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00b1de84"></a> `00b1de84` | `e0 0b 80 3d` | str q0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b1de88"></a> `00b1de88` | `72 fe 02 94` | bl 0x00bdd850 | `UNCONDITIONAL_CALL`
<a id="insn-00b1de8c"></a> `00b1de8c` | `00 e4 00 6f` | movi v0.2D,#0x0 | `FALL_THROUGH`
<a id="insn-00b1de90"></a> `00b1de90` | `e0 83 85 3c` | stur q0,[sp, #0x58] | `FALL_THROUGH`
<a id="insn-00b1de94"></a> `00b1de94` | `e0 83 84 3c` | stur q0,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00b1de98"></a> `00b1de98` | `e0 83 83 3c` | stur q0,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00b1de9c"></a> `00b1de9c` | `e8 07 00 b0` | adrp x8,0xc1a000 | `FALL_THROUGH`
<a id="insn-00b1dea0"></a> `00b1dea0` | `08 69 46 f9` | ldr x8,[x8, #0xcd0] | `FALL_THROUGH`
<a id="insn-00b1dea4"></a> `00b1dea4` | `e1 07 40 b9` | ldr w1,[sp, #0x4] | `FALL_THROUGH`
<a id="insn-00b1dea8"></a> `00b1dea8` | `09 03 80 52` | mov w9,#0x18 | `FALL_THROUGH`
<a id="insn-00b1deac"></a> `00b1deac` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00b1deb0"></a> `00b1deb0` | `15 41 00 91` | add x21,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00b1deb4"></a> `00b1deb4` | `e0 83 86 3c` | stur q0,[sp, #0x68] | `FALL_THROUGH`
<a id="insn-00b1deb8"></a> `00b1deb8` | `e0 83 87 3c` | stur q0,[sp, #0x78] | `FALL_THROUGH`
<a id="insn-00b1debc"></a> `00b1debc` | `f5 17 00 f9` | str x21,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00b1dec0"></a> `00b1dec0` | `e9 8b 00 b9` | str w9,[sp, #0x88] | `FALL_THROUGH`
<a id="insn-00b1dec4"></a> `00b1dec4` | `4f 07 03 94` | bl 0x00bdfc00 | `UNCONDITIONAL_CALL`
<a id="insn-00b1dec8"></a> `00b1dec8` | `e8 07 40 f9` | ldr x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00b1decc"></a> `00b1decc` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00b1ded0"></a> `00b1ded0` | `e4 f4 02 94` | bl 0x00bdb260 | `UNCONDITIONAL_CALL`
<a id="insn-00b1ded4"></a> `00b1ded4` | `e8 a3 41 39` | ldrb w8,[sp, #0x68] | `FALL_THROUGH`
<a id="insn-00b1ded8"></a> `00b1ded8` | `fb 57 02 a9` | stp x27,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b1dedc"></a> `00b1dedc` | `fc 0b 00 f9` | str x28,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b1dee0"></a> `00b1dee0` | `f6 4b 00 f9` | str x22,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00b1dee4"></a> `00b1dee4` | `68 00 00 36` | tbz w8,#0x0,0x00b1def0 | `CONDITIONAL_JUMP`
<a id="insn-00b1dee8"></a> `00b1dee8` | `e0 3f 40 f9` | ldr x0,[sp, #0x78] | `FALL_THROUGH`
<a id="insn-00b1deec"></a> `00b1deec` | `1d f4 02 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00b1def0"></a> `00b1def0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b1def4"></a> `00b1def4` | `fa 17 00 f9` | str x26,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00b1def8"></a> `00b1def8` | `12 f5 02 94` | bl 0x00bdb340 | `UNCONDITIONAL_CALL`
<a id="insn-00b1defc"></a> `00b1defc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b1df00"></a> `00b1df00` | `78 08 03 94` | bl 0x00be00e0 | `UNCONDITIONAL_CALL`
<a id="insn-00b1df04"></a> `00b1df04` | `28 17 40 f9` | ldr x8,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-00b1df08"></a> `00b1df08` | `a9 03 5a f8` | ldur x9,[x29, #-0x60] | `FALL_THROUGH`
<a id="insn-00b1df0c"></a> `00b1df0c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00b1df10"></a> `00b1df10` | `21 01 00 54` | b.ne 0x00b1df34 | `CONDITIONAL_JUMP`
<a id="insn-00b1df14"></a> `00b1df14` | `fd 7b 59 a9` | ldp x29,x30,[sp, #0x190] | `FALL_THROUGH`
<a id="insn-00b1df18"></a> `00b1df18` | `f4 4f 58 a9` | ldp x20,x19,[sp, #0x180] | `FALL_THROUGH`
<a id="insn-00b1df1c"></a> `00b1df1c` | `f6 57 57 a9` | ldp x22,x21,[sp, #0x170] | `FALL_THROUGH`
<a id="insn-00b1df20"></a> `00b1df20` | `f8 5f 56 a9` | ldp x24,x23,[sp, #0x160] | `FALL_THROUGH`
<a id="insn-00b1df24"></a> `00b1df24` | `fa 67 55 a9` | ldp x26,x25,[sp, #0x150] | `FALL_THROUGH`
<a id="insn-00b1df28"></a> `00b1df28` | `fc 6f 54 a9` | ldp x28,x27,[sp, #0x140] | `FALL_THROUGH`
<a id="insn-00b1df2c"></a> `00b1df2c` | `ff 83 06 91` | add sp,sp,#0x1a0 | `FALL_THROUGH`
<a id="insn-00b1df30"></a> `00b1df30` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00b1df34"></a> `00b1df34` | `17 f4 02 94` | bl 0x00bdaf90 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b1ddcc`](#insn-00b1ddcc) 範囲 `[['00b1ddcc', '00b1ddff']]`
  - `FALL_THROUGH` [`00b1ddfc`](#insn-00b1ddfc) → [`00b1de00`](#insn-00b1de00)
- ブロック [`00b1de00`](#insn-00b1de00) 範囲 `[['00b1de00', '00b1dee7']]`
  - `CONDITIONAL_JUMP` [`00b1dee4`](#insn-00b1dee4) → [`00b1def0`](#insn-00b1def0)
  - `FALL_THROUGH` [`00b1dee4`](#insn-00b1dee4) → [`00b1dee8`](#insn-00b1dee8)
- ブロック [`00b1dee8`](#insn-00b1dee8) 範囲 `[['00b1dee8', '00b1deef']]`
  - `FALL_THROUGH` [`00b1deec`](#insn-00b1deec) → [`00b1def0`](#insn-00b1def0)
- ブロック [`00b1def0`](#insn-00b1def0) 範囲 `[['00b1def0', '00b1df13']]`
  - `CONDITIONAL_JUMP` [`00b1df10`](#insn-00b1df10) → [`00b1df34`](#insn-00b1df34)
  - `FALL_THROUGH` [`00b1df10`](#insn-00b1df10) → [`00b1df14`](#insn-00b1df14)
- ブロック [`00b1df14`](#insn-00b1df14) 範囲 `[['00b1df14', '00b1df17']]`
  - `FALL_THROUGH` [`00b1df14`](#insn-00b1df14) → [`00b1df18`](#insn-00b1df18)
- ブロック [`00b1df18`](#insn-00b1df18) 範囲 `[['00b1df18', '00b1df33']]`
- ブロック [`00b1df34`](#insn-00b1df34) 範囲 `[['00b1df34', '00b1df37']]`

## 命令位置別の参照

- [`00b1ddd0`](#insn-00b1ddd0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1ddd4`](#insn-00b1ddd4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1ddd8`](#insn-00b1ddd8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1dddc`](#insn-00b1dddc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1dde0`](#insn-00b1dde0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1dde4`](#insn-00b1dde4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1ddec`](#insn-00b1ddec) → `Stack[-0x198]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1ddf8`](#insn-00b1ddf8) → `Stack[-0x19c]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1de00`](#insn-00b1de00) → `00c1ad28`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00b1de04`](#insn-00b1de04) → `00c1b948`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00b1de38`](#insn-00b1de38) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1de3c`](#insn-00b1de3c) → `00c11040`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00b1de3c`](#insn-00b1de3c) → `Stack[-0x110]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1de40`](#insn-00b1de40) → `00c10f28`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00b1de40`](#insn-00b1de40) → `Stack[-0x180]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1de44`](#insn-00b1de44) → `00c11018`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00b1de44`](#insn-00b1de44) → `Stack[-0x190]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1de48`](#insn-00b1de48) → [`00bdb290`](../00bdb/00bdb290.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb290` · 推定シンボル `None` · 推定型 `None`
- [`00b1de50`](#insn-00b1de50) → `00c1b950`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00b1de74`](#insn-00b1de74) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1de78`](#insn-00b1de78) → `00c10f00`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00b1de78`](#insn-00b1de78) → `Stack[-0x190]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1de7c`](#insn-00b1de7c) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1de80`](#insn-00b1de80) → `00c10f50`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00b1de80`](#insn-00b1de80) → `Stack[-0x110]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1de84`](#insn-00b1de84) → `00c11f28`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00b1de84`](#insn-00b1de84) → `Stack[-0x180]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1de88`](#insn-00b1de88) → [`00bdd850`](../00bdd/00bdd850.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd850` · 推定シンボル `None` · 推定型 `None`
- [`00b1de90`](#insn-00b1de90) → `Stack[-0x148]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1de94`](#insn-00b1de94) → `Stack[-0x158]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1de98`](#insn-00b1de98) → `Stack[-0x168]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1dea0`](#insn-00b1dea0) → `00c1acd0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00b1dea4`](#insn-00b1dea4) → `Stack[-0x19c]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1deb4`](#insn-00b1deb4) → `Stack[-0x138]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1deb8`](#insn-00b1deb8) → `Stack[-0x128]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1debc`](#insn-00b1debc) → `00c11078`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[128]`
- [`00b1debc`](#insn-00b1debc) → `Stack[-0x178]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1dec0`](#insn-00b1dec0) → `Stack[-0x118]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1dec4`](#insn-00b1dec4) → [`00bdfc00`](../00bdf/00bdfc00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdfc00` · 推定シンボル `None` · 推定型 `None`
- [`00b1dec8`](#insn-00b1dec8) → `Stack[-0x198]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1ded0`](#insn-00b1ded0) → [`00bdb260`](../00bdb/00bdb260.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb260` · 推定シンボル `None` · 推定型 `None`
- [`00b1ded4`](#insn-00b1ded4) → `Stack[-0x138]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1ded8`](#insn-00b1ded8) → `00c10f28`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00b1ded8`](#insn-00b1ded8) → `00c11078`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[128]`
- [`00b1ded8`](#insn-00b1ded8) → `Stack[-0x180]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1dedc`](#insn-00b1dedc) → `00c10f00`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00b1dedc`](#insn-00b1dedc) → `Stack[-0x190]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1dee0`](#insn-00b1dee0) → `00c10f50`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00b1dee0`](#insn-00b1dee0) → `Stack[-0x110]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1dee4`](#insn-00b1dee4) → [`00b1def0`](#insn-00b1def0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1dee8`](#insn-00b1dee8) → `Stack[-0x128]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1deec`](#insn-00b1deec) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00b1def4`](#insn-00b1def4) → `00c11120`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[128]`
- [`00b1def4`](#insn-00b1def4) → `Stack[-0x178]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1def8`](#insn-00b1def8) → [`00bdb340`](../00bdb/00bdb340.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb340` · 推定シンボル `None` · 推定型 `None`
- [`00b1df00`](#insn-00b1df00) → [`00be00e0`](../00be0/00be00e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be00e0` · 推定シンボル `None` · 推定型 `None`
- [`00b1df08`](#insn-00b1df08) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1df10`](#insn-00b1df10) → [`00b1df34`](#insn-00b1df34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1df14`](#insn-00b1df14) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1df18`](#insn-00b1df18) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1df1c`](#insn-00b1df1c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1df20`](#insn-00b1df20) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1df24`](#insn-00b1df24) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1df28`](#insn-00b1df28) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b1df34`](#insn-00b1df34) → [`00bdaf90`](../00bda/00bdaf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf90` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b1ddd0`](#insn-00b1ddd0)

~~~json
{
  "source": "00b1ddd0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1ddd4`](#insn-00b1ddd4)

~~~json
{
  "source": "00b1ddd4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1ddd8`](#insn-00b1ddd8)

~~~json
{
  "source": "00b1ddd8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1dddc`](#insn-00b1dddc)

~~~json
{
  "source": "00b1dddc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1dde0`](#insn-00b1dde0)

~~~json
{
  "source": "00b1dde0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1dde4`](#insn-00b1dde4)

~~~json
{
  "source": "00b1dde4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1ddec`](#insn-00b1ddec)

~~~json
{
  "source": "00b1ddec",
  "target": "Stack[-0x198]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1ddf8`](#insn-00b1ddf8)

~~~json
{
  "source": "00b1ddf8",
  "target": "Stack[-0x19c]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1de00`](#insn-00b1de00)

~~~json
{
  "source": "00b1de00",
  "target": "00c1ad28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1ad28",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00b1de04`](#insn-00b1de04)

~~~json
{
  "source": "00b1de04",
  "target": "00c1b948",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1b948",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00b1de38`](#insn-00b1de38)

~~~json
{
  "source": "00b1de38",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1de3c`](#insn-00b1de3c)

~~~json
{
  "source": "00b1de3c",
  "target": "00c11040",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c11040",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00b1de3c`](#insn-00b1de3c)

~~~json
{
  "source": "00b1de3c",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1de40`](#insn-00b1de40)

~~~json
{
  "source": "00b1de40",
  "target": "00c10f28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c10f28",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00b1de40`](#insn-00b1de40)

~~~json
{
  "source": "00b1de40",
  "target": "Stack[-0x180]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1de44`](#insn-00b1de44)

~~~json
{
  "source": "00b1de44",
  "target": "00c11018",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c11018",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00b1de44`](#insn-00b1de44)

~~~json
{
  "source": "00b1de44",
  "target": "Stack[-0x190]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1de48`](#insn-00b1de48)

~~~json
{
  "source": "00b1de48",
  "target": "00bdb290",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1de50`](#insn-00b1de50)

~~~json
{
  "source": "00b1de50",
  "target": "00c1b950",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1b950",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00b1de74`](#insn-00b1de74)

~~~json
{
  "source": "00b1de74",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1de78`](#insn-00b1de78)

~~~json
{
  "source": "00b1de78",
  "target": "00c10f00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c10f00",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00b1de78`](#insn-00b1de78)

~~~json
{
  "source": "00b1de78",
  "target": "Stack[-0x190]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1de7c`](#insn-00b1de7c)

~~~json
{
  "source": "00b1de7c",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1de80`](#insn-00b1de80)

~~~json
{
  "source": "00b1de80",
  "target": "00c10f50",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c10f50",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00b1de80`](#insn-00b1de80)

~~~json
{
  "source": "00b1de80",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1de84`](#insn-00b1de84)

~~~json
{
  "source": "00b1de84",
  "target": "00c11f28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c11f28",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00b1de84`](#insn-00b1de84)

~~~json
{
  "source": "00b1de84",
  "target": "Stack[-0x180]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1de88`](#insn-00b1de88)

~~~json
{
  "source": "00b1de88",
  "target": "00bdd850",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1de90`](#insn-00b1de90)

~~~json
{
  "source": "00b1de90",
  "target": "Stack[-0x148]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1de94`](#insn-00b1de94)

~~~json
{
  "source": "00b1de94",
  "target": "Stack[-0x158]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1de98`](#insn-00b1de98)

~~~json
{
  "source": "00b1de98",
  "target": "Stack[-0x168]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1dea0`](#insn-00b1dea0)

~~~json
{
  "source": "00b1dea0",
  "target": "00c1acd0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1acd0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00b1dea4`](#insn-00b1dea4)

~~~json
{
  "source": "00b1dea4",
  "target": "Stack[-0x19c]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1deb4`](#insn-00b1deb4)

~~~json
{
  "source": "00b1deb4",
  "target": "Stack[-0x138]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1deb8`](#insn-00b1deb8)

~~~json
{
  "source": "00b1deb8",
  "target": "Stack[-0x128]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1debc`](#insn-00b1debc)

~~~json
{
  "source": "00b1debc",
  "target": "00c11078",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c11068",
  "offset": 16,
  "size": 128,
  "datatype": "undefined1[128]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`00b1debc`](#insn-00b1debc)

~~~json
{
  "source": "00b1debc",
  "target": "Stack[-0x178]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1dec0`](#insn-00b1dec0)

~~~json
{
  "source": "00b1dec0",
  "target": "Stack[-0x118]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1dec4`](#insn-00b1dec4)

~~~json
{
  "source": "00b1dec4",
  "target": "00bdfc00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1dec8`](#insn-00b1dec8)

~~~json
{
  "source": "00b1dec8",
  "target": "Stack[-0x198]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1ded0`](#insn-00b1ded0)

~~~json
{
  "source": "00b1ded0",
  "target": "00bdb260",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1ded4`](#insn-00b1ded4)

~~~json
{
  "source": "00b1ded4",
  "target": "Stack[-0x138]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1ded8`](#insn-00b1ded8)

~~~json
{
  "source": "00b1ded8",
  "target": "00c10f28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c10f28",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00b1ded8`](#insn-00b1ded8)

~~~json
{
  "source": "00b1ded8",
  "target": "00c11078",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c11068",
  "offset": 16,
  "size": 128,
  "datatype": "undefined1[128]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`00b1ded8`](#insn-00b1ded8)

~~~json
{
  "source": "00b1ded8",
  "target": "Stack[-0x180]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1dedc`](#insn-00b1dedc)

~~~json
{
  "source": "00b1dedc",
  "target": "00c10f00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c10f00",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00b1dedc`](#insn-00b1dedc)

~~~json
{
  "source": "00b1dedc",
  "target": "Stack[-0x190]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1dee0`](#insn-00b1dee0)

~~~json
{
  "source": "00b1dee0",
  "target": "00c10f50",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c10f50",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00b1dee0`](#insn-00b1dee0)

~~~json
{
  "source": "00b1dee0",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1dee4`](#insn-00b1dee4)

~~~json
{
  "source": "00b1dee4",
  "target": "00b1def0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1dee8`](#insn-00b1dee8)

~~~json
{
  "source": "00b1dee8",
  "target": "Stack[-0x128]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1deec`](#insn-00b1deec)

~~~json
{
  "source": "00b1deec",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1def4`](#insn-00b1def4)

~~~json
{
  "source": "00b1def4",
  "target": "00c11120",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c11110",
  "offset": 16,
  "size": 128,
  "datatype": "undefined1[128]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`00b1def4`](#insn-00b1def4)

~~~json
{
  "source": "00b1def4",
  "target": "Stack[-0x178]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1def8`](#insn-00b1def8)

~~~json
{
  "source": "00b1def8",
  "target": "00bdb340",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1df00`](#insn-00b1df00)

~~~json
{
  "source": "00b1df00",
  "target": "00be00e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b1df08`](#insn-00b1df08)

~~~json
{
  "source": "00b1df08",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1df10`](#insn-00b1df10)

~~~json
{
  "source": "00b1df10",
  "target": "00b1df34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1df14`](#insn-00b1df14)

~~~json
{
  "source": "00b1df14",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1df18`](#insn-00b1df18)

~~~json
{
  "source": "00b1df18",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1df1c`](#insn-00b1df1c)

~~~json
{
  "source": "00b1df1c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1df20`](#insn-00b1df20)

~~~json
{
  "source": "00b1df20",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1df24`](#insn-00b1df24)

~~~json
{
  "source": "00b1df24",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1df28`](#insn-00b1df28)

~~~json
{
  "source": "00b1df28",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b1df34`](#insn-00b1df34)

~~~json
{
  "source": "00b1df34",
  "target": "00bdaf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
