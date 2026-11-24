# 00bf5ffc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bf5bd4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf5/00bf5bd4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0086.md#compare-cde5ae7c74afa1d835269314da6c5c92)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bf6098`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf6/00bf6098.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0086.md#compare-c03f1ebf535248f51f8a4353d0213b61)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bf5ffc",
  "name": "_ZNSt6__ndk15stoldERKNS_12basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEEEPm",
  "size": 360,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "236138efbfa73b35b89d5cc98d19fc07db3e37a469369ad5ac92670090c6f90d",
  "source_text_sha256": "236138efbfa73b35b89d5cc98d19fc07db3e37a469369ad5ac92670090c6f90d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bf5ffc",
        "00bf6153"
      ],
      [
        "00bf6158",
        "00bf6167"
      ]
    ],
    "bytes_sha256": "b94e7bd51764dd974d57ed9b3ff9657a4a66e7d1399787224ddb584e3fac13e6",
    "instruction_count": 90,
    "instruction_bytes": 360,
    "body_bytes": 360,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00442930](../00442/00442930.md)
- [00bf81cc](../00bf8/00bf81cc.md)
- [00c53f5c](../00c53/00c53f5c.md)
- [00c580c0](../00c58/00c580c0.md)
- [00c5e050](../00c5e/00c5e050.md)
- [00c5e0f0](../00c5e/00c5e0f0.md)

## 関連文字列（未確認候補）

~~~text
": no conversion"
": out of range"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2811 bytes

~~~c

undefined1  [16]
_ZNSt6__ndk15stoldERKNS_12basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEEEPm
          (byte *param_1,long *param_2)

{
  wchar_t *__nptr;
  int iVar1;
  int iVar2;
  undefined1 auVar3 [16];
  int *piVar4;
  undefined8 uVar5;
  undefined4 *puVar6;
  double dVar7;
  undefined8 extraout_var;
  undefined1 local_68;
  undefined4 local_67;
  undefined2 local_63;
  wchar_t *local_50;
  undefined1 local_48;
  undefined4 local_47;
  undefined1 local_43;
  undefined6 local_42;
  char cStack_3c;
  char cStack_3b;
  undefined2 uStack_3a;
  undefined4 local_38;
  uint uStack_34;
  
  local_68 = 10;
  local_50 = (wchar_t *)0x0;
  local_67 = 0x6c6f7473;
  local_63 = 100;
  __nptr = (wchar_t *)(param_1 + 4);
  if ((*param_1 & 1) != 0) {
    __nptr = *(wchar_t **)(param_1 + 0x10);
  }
  piVar4 = (int *)__errno();
  iVar1 = *piVar4;
  *piVar4 = 0;
  dVar7 = wcstold(__nptr,&local_50);
  iVar2 = *piVar4;
  *piVar4 = iVar1;
  puVar6 = (undefined4 *)((ulong)&local_68 | 1);
  if (iVar2 != 0x22) {
    if ((long)local_50 - (long)__nptr != 0) {
      if (param_2 != (long *)0x0) {
        *param_2 = (long)local_50 - (long)__nptr >> 2;
      }
      _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEED1Ev(&local_68);
      auVar3._8_8_ = extraout_var;
      auVar3._0_8_ = dVar7;
      return auVar3;
    }
    local_47 = *puVar6;
    local_43 = *(undefined1 *)(puVar6 + 1);
    local_48 = 0x28;
    local_42 = (undefined6)s___no_conversion_002a750a._0_7_;
    cStack_3c = SUB71(s___no_conversion_002a750a._0_7_,6);
    cStack_3b = s___no_conversion_002a750a[7];
    uStack_3a = (undefined2)s___no_conversion_002a750a._8_7_;
    local_38 = SUB74(s___no_conversion_002a750a._8_7_,2);
    uStack_34 = (uint)SUB71(s___no_conversion_002a750a._8_7_,6);
    uVar5 = FUN_00bf81cc((ulong)&local_48 | 1);
    _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEED1Ev(&local_48);
    _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEED1Ev(&local_68);
                    /* WARNING: Subroutine does not return */
    FUN_00c53f5c(uVar5);
  }
  local_47 = *puVar6;
  local_43 = *(undefined1 *)(puVar6 + 1);
  local_48 = 0x26;
  uStack_34 = 0;
  local_42._0_1_ = s___out_of_range_002b9dc6[0];
  local_42._1_1_ = s___out_of_range_002b9dc6[1];
  local_42._2_1_ = s___out_of_range_002b9dc6[2];
  local_42._3_1_ = s___out_of_range_002b9dc6[3];
  local_42._4_1_ = s___out_of_range_002b9dc6[4];
  local_42._5_1_ = s___out_of_range_002b9dc6[5];
  cStack_3c = (char)s___out_of_range_002b9dc6._6_2_;
  cStack_3b = SUB21(s___out_of_range_002b9dc6._6_2_,1);
  uStack_3a = (undefined2)s___out_of_range_002b9dc6._8_6_;
  local_38 = SUB64(s___out_of_range_002b9dc6._8_6_,2);
                    /* WARNING: Subroutine does not return */
  FUN_00442930((ulong)&local_48 | 1);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bf5ffc"></a> `00bf5ffc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bf6000"></a> `00bf6000` | `ff 03 02 d1` | sub sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00bf6004"></a> `00bf6004` | `fd 7b 05 a9` | stp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bf6008"></a> `00bf6008` | `f6 57 06 a9` | stp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bf600c"></a> `00bf600c` | `f4 4f 07 a9` | stp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bf6010"></a> `00bf6010` | `fd 43 01 91` | add x29,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00bf6014"></a> `00bf6014` | `48 01 80 52` | mov w8,#0xa | `FALL_THROUGH`
<a id="insn-00bf6018"></a> `00bf6018` | `09 00 40 39` | ldrb w9,[x0] | `FALL_THROUGH`
<a id="insn-00bf601c"></a> `00bf601c` | `0a 08 40 f9` | ldr x10,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bf6020"></a> `00bf6020` | `e8 63 00 39` | strb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bf6024"></a> `00bf6024` | `68 8e 8e 52` | mov w8,#0x7473 | `FALL_THROUGH`
<a id="insn-00bf6028"></a> `00bf6028` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bf602c"></a> `00bf602c` | `e8 8d ad 72` | movk w8,#0x6c6f, LSL #16 | `FALL_THROUGH`
<a id="insn-00bf6030"></a> `00bf6030` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bf6034"></a> `00bf6034` | `bf 03 1e f8` | stur xzr,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00bf6038"></a> `00bf6038` | `e8 93 01 b8` | stur w8,[sp, #0x19] | `FALL_THROUGH`
<a id="insn-00bf603c"></a> `00bf603c` | `88 0c 80 52` | mov w8,#0x64 | `FALL_THROUGH`
<a id="insn-00bf6040"></a> `00bf6040` | `e8 d3 01 78` | sturh w8,[sp, #0x1d] | `FALL_THROUGH`
<a id="insn-00bf6044"></a> `00bf6044` | `08 10 00 91` | add x8,x0,#0x4 | `FALL_THROUGH`
<a id="insn-00bf6048"></a> `00bf6048` | `14 01 8a 9a` | csel x20,x8,x10,eq | `FALL_THROUGH`
<a id="insn-00bf604c"></a> `00bf604c` | `1d 88 01 94` | bl 0x00c580c0 | `UNCONDITIONAL_CALL`
<a id="insn-00bf6050"></a> `00bf6050` | `16 00 40 b9` | ldr w22,[x0] | `FALL_THROUGH`
<a id="insn-00bf6054"></a> `00bf6054` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bf6058"></a> `00bf6058` | `1f 00 00 b9` | str wzr,[x0] | `FALL_THROUGH`
<a id="insn-00bf605c"></a> `00bf605c` | `a1 83 00 d1` | sub x1,x29,#0x20 | `FALL_THROUGH`
<a id="insn-00bf6060"></a> `00bf6060` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bf6064"></a> `00bf6064` | `23 a0 01 94` | bl 0x00c5e0f0 | `UNCONDITIONAL_CALL`
<a id="insn-00bf6068"></a> `00bf6068` | `a8 02 40 b9` | ldr w8,[x21] | `FALL_THROUGH`
<a id="insn-00bf606c"></a> `00bf606c` | `e9 63 00 91` | add x9,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bf6070"></a> `00bf6070` | `b6 02 00 b9` | str w22,[x21] | `FALL_THROUGH`
<a id="insn-00bf6074"></a> `00bf6074` | `1f 89 00 71` | cmp w8,#0x22 | `FALL_THROUGH`
<a id="insn-00bf6078"></a> `00bf6078` | `28 01 40 b2` | orr x8,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bf607c"></a> `00bf607c` | `20 02 00 54` | b.eq 0x00bf60c0 | `CONDITIONAL_JUMP`
<a id="insn-00bf6080"></a> `00bf6080` | `a9 03 5e f8` | ldur x9,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00bf6084"></a> `00bf6084` | `29 01 14 eb` | subs x9,x9,x20 | `FALL_THROUGH`
<a id="insn-00bf6088"></a> `00bf6088` | `c0 03 00 54` | b.eq 0x00bf6100 | `CONDITIONAL_JUMP`
<a id="insn-00bf608c"></a> `00bf608c` | `e0 03 80 3d` | str q0,[sp] | `FALL_THROUGH`
<a id="insn-00bf6090"></a> `00bf6090` | `73 00 00 b4` | cbz x19,0x00bf609c | `CONDITIONAL_JUMP`
<a id="insn-00bf6094"></a> `00bf6094` | `28 fd 42 93` | asr x8,x9,#0x2 | `FALL_THROUGH`
<a id="insn-00bf6098"></a> `00bf6098` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bf609c"></a> `00bf609c` | `e0 63 00 91` | add x0,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bf60a0"></a> `00bf60a0` | `ec 9f 01 94` | bl 0x00c5e050 | `UNCONDITIONAL_CALL`
<a id="insn-00bf60a4"></a> `00bf60a4` | `e0 03 c0 3d` | ldr q0,[sp] | `FALL_THROUGH`
<a id="insn-00bf60a8"></a> `00bf60a8` | `f4 4f 47 a9` | ldp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bf60ac"></a> `00bf60ac` | `f6 57 46 a9` | ldp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bf60b0"></a> `00bf60b0` | `fd 7b 45 a9` | ldp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bf60b4"></a> `00bf60b4` | `ff 03 02 91` | add sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00bf60b8"></a> `00bf60b8` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bf60bc"></a> `00bf60bc` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bf60c0"></a> `00bf60c0` | `c9 04 80 52` | mov w9,#0x26 | `FALL_THROUGH`
<a id="insn-00bf60c4"></a> `00bf60c4` | `0a 01 40 b9` | ldr w10,[x8] | `FALL_THROUGH`
<a id="insn-00bf60c8"></a> `00bf60c8` | `08 11 40 39` | ldrb w8,[x8, #0x4] | `FALL_THROUGH`
<a id="insn-00bf60cc"></a> `00bf60cc` | `a9 83 1e 38` | sturb w9,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-00bf60d0"></a> `00bf60d0` | `09 b6 ff f0` | adrp x9,0x2b9000 | `FALL_THROUGH`
<a id="insn-00bf60d4"></a> `00bf60d4` | `29 19 37 91` | add x9,x9,#0xdc6 | `FALL_THROUGH`
<a id="insn-00bf60d8"></a> `00bf60d8` | `2b 01 40 f9` | ldr x11,[x9] | `FALL_THROUGH`
<a id="insn-00bf60dc"></a> `00bf60dc` | `a8 d3 1e 38` | sturb w8,[x29, #-0x13] | `FALL_THROUGH`
<a id="insn-00bf60e0"></a> `00bf60e0` | `28 61 40 f8` | ldur x8,[x9, #0x6] | `FALL_THROUGH`
<a id="insn-00bf60e4"></a> `00bf60e4` | `bf 83 1f f8` | stur xzr,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00bf60e8"></a> `00bf60e8` | `a9 63 00 d1` | sub x9,x29,#0x18 | `FALL_THROUGH`
<a id="insn-00bf60ec"></a> `00bf60ec` | `aa 93 1e b8` | stur w10,[x29, #-0x17] | `FALL_THROUGH`
<a id="insn-00bf60f0"></a> `00bf60f0` | `ab e3 1e f8` | stur x11,[x29, #-0x12] | `FALL_THROUGH`
<a id="insn-00bf60f4"></a> `00bf60f4` | `a8 43 1f f8` | stur x8,[x29, #-0xc] | `FALL_THROUGH`
<a id="insn-00bf60f8"></a> `00bf60f8` | `20 01 40 b2` | orr x0,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bf60fc"></a> `00bf60fc` | `0d 32 e1 97` | bl 0x00442930 | `CALL_TERMINATOR`
<a id="insn-00bf6100"></a> `00bf6100` | `09 05 80 52` | mov w9,#0x28 | `FALL_THROUGH`
<a id="insn-00bf6104"></a> `00bf6104` | `0a 01 40 b9` | ldr w10,[x8] | `FALL_THROUGH`
<a id="insn-00bf6108"></a> `00bf6108` | `08 11 40 39` | ldrb w8,[x8, #0x4] | `FALL_THROUGH`
<a id="insn-00bf610c"></a> `00bf610c` | `a9 83 1e 38` | sturb w9,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-00bf6110"></a> `00bf6110` | `89 b5 ff b0` | adrp x9,0x2a7000 | `FALL_THROUGH`
<a id="insn-00bf6114"></a> `00bf6114` | `29 29 14 91` | add x9,x9,#0x50a | `FALL_THROUGH`
<a id="insn-00bf6118"></a> `00bf6118` | `2b 01 40 f9` | ldr x11,[x9] | `FALL_THROUGH`
<a id="insn-00bf611c"></a> `00bf611c` | `a8 d3 1e 38` | sturb w8,[x29, #-0x13] | `FALL_THROUGH`
<a id="insn-00bf6120"></a> `00bf6120` | `28 71 40 f8` | ldur x8,[x9, #0x7] | `FALL_THROUGH`
<a id="insn-00bf6124"></a> `00bf6124` | `bf 83 1f f8` | stur xzr,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00bf6128"></a> `00bf6128` | `a9 63 00 d1` | sub x9,x29,#0x18 | `FALL_THROUGH`
<a id="insn-00bf612c"></a> `00bf612c` | `aa 93 1e b8` | stur w10,[x29, #-0x17] | `FALL_THROUGH`
<a id="insn-00bf6130"></a> `00bf6130` | `ab e3 1e f8` | stur x11,[x29, #-0x12] | `FALL_THROUGH`
<a id="insn-00bf6134"></a> `00bf6134` | `a8 53 1f f8` | stur x8,[x29, #-0xb] | `FALL_THROUGH`
<a id="insn-00bf6138"></a> `00bf6138` | `20 01 40 b2` | orr x0,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bf613c"></a> `00bf613c` | `24 08 00 94` | bl 0x00bf81cc | `UNCONDITIONAL_CALL`
<a id="insn-00bf6140"></a> `00bf6140` | `01 00 00 14` | b 0x00bf6144 | `UNCONDITIONAL_JUMP`
<a id="insn-00bf6144"></a> `00bf6144` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bf6148"></a> `00bf6148` | `a0 63 00 d1` | sub x0,x29,#0x18 | `FALL_THROUGH`
<a id="insn-00bf614c"></a> `00bf614c` | `c1 9f 01 94` | bl 0x00c5e050 | `UNCONDITIONAL_CALL`
<a id="insn-00bf6150"></a> `00bf6150` | `02 00 00 14` | b 0x00bf6158 | `UNCONDITIONAL_JUMP`
<a id="insn-00bf6158"></a> `00bf6158` | `e0 63 00 91` | add x0,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bf615c"></a> `00bf615c` | `bd 9f 01 94` | bl 0x00c5e050 | `UNCONDITIONAL_CALL`
<a id="insn-00bf6160"></a> `00bf6160` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bf6164"></a> `00bf6164` | `7e 77 01 94` | bl 0x00c53f5c | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bf5ffc`](#insn-00bf5ffc) 範囲 `[['00bf5ffc', '00bf607f']]`
  - `CONDITIONAL_JUMP` [`00bf607c`](#insn-00bf607c) → [`00bf60c0`](#insn-00bf60c0)
  - `FALL_THROUGH` [`00bf607c`](#insn-00bf607c) → [`00bf6080`](#insn-00bf6080)
- ブロック [`00bf6080`](#insn-00bf6080) 範囲 `[['00bf6080', '00bf608b']]`
  - `CONDITIONAL_JUMP` [`00bf6088`](#insn-00bf6088) → [`00bf6100`](#insn-00bf6100)
  - `FALL_THROUGH` [`00bf6088`](#insn-00bf6088) → [`00bf608c`](#insn-00bf608c)
- ブロック [`00bf608c`](#insn-00bf608c) 範囲 `[['00bf608c', '00bf6093']]`
  - `CONDITIONAL_JUMP` [`00bf6090`](#insn-00bf6090) → [`00bf609c`](#insn-00bf609c)
  - `FALL_THROUGH` [`00bf6090`](#insn-00bf6090) → [`00bf6094`](#insn-00bf6094)
- ブロック [`00bf6094`](#insn-00bf6094) 範囲 `[['00bf6094', '00bf609b']]`
  - `FALL_THROUGH` [`00bf6098`](#insn-00bf6098) → [`00bf609c`](#insn-00bf609c)
- ブロック [`00bf609c`](#insn-00bf609c) 範囲 `[['00bf609c', '00bf60bf']]`
- ブロック [`00bf60c0`](#insn-00bf60c0) 範囲 `[['00bf60c0', '00bf60ff']]`
- ブロック [`00bf6100`](#insn-00bf6100) 範囲 `[['00bf6100', '00bf6143']]`
  - `UNCONDITIONAL_JUMP` [`00bf6140`](#insn-00bf6140) → [`00bf6144`](#insn-00bf6144)
- ブロック [`00bf6144`](#insn-00bf6144) 範囲 `[['00bf6144', '00bf6153']]`
  - `UNCONDITIONAL_JUMP` [`00bf6150`](#insn-00bf6150) → [`00bf6158`](#insn-00bf6158)
- ブロック [`00bf6158`](#insn-00bf6158) 範囲 `[['00bf6158', '00bf6167']]`

## 命令位置別の参照

- [`00bf6004`](#insn-00bf6004) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf6008`](#insn-00bf6008) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf600c`](#insn-00bf600c) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf6020`](#insn-00bf6020) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf6034`](#insn-00bf6034) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf6038`](#insn-00bf6038) → `Stack[-0x67]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf6040`](#insn-00bf6040) → `Stack[-0x63]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf604c`](#insn-00bf604c) → [`00c580c0`](../00c58/00c580c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c580c0` · 推定シンボル `None` · 推定型 `None`
- [`00bf6064`](#insn-00bf6064) → [`00c5e0f0`](../00c5e/00c5e0f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e0f0` · 推定シンボル `None` · 推定型 `None`
- [`00bf607c`](#insn-00bf607c) → [`00bf60c0`](#insn-00bf60c0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf6080`](#insn-00bf6080) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf6088`](#insn-00bf6088) → [`00bf6100`](#insn-00bf6100) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf608c`](#insn-00bf608c) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf6090`](#insn-00bf6090) → [`00bf609c`](#insn-00bf609c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf60a0`](#insn-00bf60a0) → [`00c5e050`](../00c5e/00c5e050.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e050` · 推定シンボル `None` · 推定型 `None`
- [`00bf60a4`](#insn-00bf60a4) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf60a8`](#insn-00bf60a8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf60ac`](#insn-00bf60ac) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf60b0`](#insn-00bf60b0) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf60cc`](#insn-00bf60cc) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf60d8`](#insn-00bf60d8) → `002b9dc6`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bf60dc`](#insn-00bf60dc) → `Stack[-0x43]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf60e0`](#insn-00bf60e0) → `002b9dcc`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bf60e4`](#insn-00bf60e4) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf60ec`](#insn-00bf60ec) → `Stack[-0x47]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf60f0`](#insn-00bf60f0) → `Stack[-0x42]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf60f4`](#insn-00bf60f4) → `Stack[-0x3c]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf60fc`](#insn-00bf60fc) → [`00442930`](../00442/00442930.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00442930` · 推定シンボル `None` · 推定型 `None`
- [`00bf610c`](#insn-00bf610c) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf6118`](#insn-00bf6118) → `002a750a`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bf611c`](#insn-00bf611c) → `Stack[-0x43]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf6120`](#insn-00bf6120) → `002a7511`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bf6124`](#insn-00bf6124) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf612c`](#insn-00bf612c) → `Stack[-0x47]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf6130`](#insn-00bf6130) → `Stack[-0x42]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf6134`](#insn-00bf6134) → `Stack[-0x3b]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf613c`](#insn-00bf613c) → [`00bf81cc`](../00bf8/00bf81cc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bf81cc` · 推定シンボル `None` · 推定型 `None`
- [`00bf6140`](#insn-00bf6140) → [`00bf6144`](#insn-00bf6144) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf614c`](#insn-00bf614c) → [`00c5e050`](../00c5e/00c5e050.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e050` · 推定シンボル `None` · 推定型 `None`
- [`00bf6150`](#insn-00bf6150) → [`00bf6158`](#insn-00bf6158) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf615c`](#insn-00bf615c) → [`00c5e050`](../00c5e/00c5e050.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e050` · 推定シンボル `None` · 推定型 `None`
- [`00bf6164`](#insn-00bf6164) → [`00c53f5c`](../00c53/00c53f5c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53f5c` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bf6004`](#insn-00bf6004)

~~~json
{
  "source": "00bf6004",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf6008`](#insn-00bf6008)

~~~json
{
  "source": "00bf6008",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf600c`](#insn-00bf600c)

~~~json
{
  "source": "00bf600c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf6020`](#insn-00bf6020)

~~~json
{
  "source": "00bf6020",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf6034`](#insn-00bf6034)

~~~json
{
  "source": "00bf6034",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf6038`](#insn-00bf6038)

~~~json
{
  "source": "00bf6038",
  "target": "Stack[-0x67]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf6040`](#insn-00bf6040)

~~~json
{
  "source": "00bf6040",
  "target": "Stack[-0x63]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf604c`](#insn-00bf604c)

~~~json
{
  "source": "00bf604c",
  "target": "00c580c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf6064`](#insn-00bf6064)

~~~json
{
  "source": "00bf6064",
  "target": "00c5e0f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf607c`](#insn-00bf607c)

~~~json
{
  "source": "00bf607c",
  "target": "00bf60c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf6080`](#insn-00bf6080)

~~~json
{
  "source": "00bf6080",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf6088`](#insn-00bf6088)

~~~json
{
  "source": "00bf6088",
  "target": "00bf6100",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf608c`](#insn-00bf608c)

~~~json
{
  "source": "00bf608c",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf6090`](#insn-00bf6090)

~~~json
{
  "source": "00bf6090",
  "target": "00bf609c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf60a0`](#insn-00bf60a0)

~~~json
{
  "source": "00bf60a0",
  "target": "00c5e050",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf60a4`](#insn-00bf60a4)

~~~json
{
  "source": "00bf60a4",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf60a8`](#insn-00bf60a8)

~~~json
{
  "source": "00bf60a8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf60ac`](#insn-00bf60ac)

~~~json
{
  "source": "00bf60ac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf60b0`](#insn-00bf60b0)

~~~json
{
  "source": "00bf60b0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf60cc`](#insn-00bf60cc)

~~~json
{
  "source": "00bf60cc",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf60d8`](#insn-00bf60d8)

~~~json
{
  "source": "00bf60d8",
  "target": "002b9dc6",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b9dc6",
  "offset": 0,
  "size": 15,
  "datatype": "string",
  "bytes": "3a206f7574206f662072616e676500",
  "capture_start": "002b9dc6",
  "capture_bytes": 15,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bf60dc`](#insn-00bf60dc)

~~~json
{
  "source": "00bf60dc",
  "target": "Stack[-0x43]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf60e0`](#insn-00bf60e0)

~~~json
{
  "source": "00bf60e0",
  "target": "002b9dcc",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b9dc6",
  "offset": 6,
  "size": 15,
  "datatype": "string",
  "bytes": "3a206f7574206f662072616e676500",
  "capture_start": "002b9dc6",
  "capture_bytes": 15,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bf60e4`](#insn-00bf60e4)

~~~json
{
  "source": "00bf60e4",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf60ec`](#insn-00bf60ec)

~~~json
{
  "source": "00bf60ec",
  "target": "Stack[-0x47]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf60f0`](#insn-00bf60f0)

~~~json
{
  "source": "00bf60f0",
  "target": "Stack[-0x42]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf60f4`](#insn-00bf60f4)

~~~json
{
  "source": "00bf60f4",
  "target": "Stack[-0x3c]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf60fc`](#insn-00bf60fc)

~~~json
{
  "source": "00bf60fc",
  "target": "00442930",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf610c`](#insn-00bf610c)

~~~json
{
  "source": "00bf610c",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf6118`](#insn-00bf6118)

~~~json
{
  "source": "00bf6118",
  "target": "002a750a",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a750a",
  "offset": 0,
  "size": 16,
  "datatype": "string",
  "bytes": "3a206e6f20636f6e76657273696f6e00",
  "capture_start": "002a750a",
  "capture_bytes": 16,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bf611c`](#insn-00bf611c)

~~~json
{
  "source": "00bf611c",
  "target": "Stack[-0x43]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf6120`](#insn-00bf6120)

~~~json
{
  "source": "00bf6120",
  "target": "002a7511",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a750a",
  "offset": 7,
  "size": 16,
  "datatype": "string",
  "bytes": "3a206e6f20636f6e76657273696f6e00",
  "capture_start": "002a750a",
  "capture_bytes": 16,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bf6124`](#insn-00bf6124)

~~~json
{
  "source": "00bf6124",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf612c`](#insn-00bf612c)

~~~json
{
  "source": "00bf612c",
  "target": "Stack[-0x47]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf6130`](#insn-00bf6130)

~~~json
{
  "source": "00bf6130",
  "target": "Stack[-0x42]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf6134`](#insn-00bf6134)

~~~json
{
  "source": "00bf6134",
  "target": "Stack[-0x3b]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf613c`](#insn-00bf613c)

~~~json
{
  "source": "00bf613c",
  "target": "00bf81cc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf6140`](#insn-00bf6140)

~~~json
{
  "source": "00bf6140",
  "target": "00bf6144",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf614c`](#insn-00bf614c)

~~~json
{
  "source": "00bf614c",
  "target": "00c5e050",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf6150`](#insn-00bf6150)

~~~json
{
  "source": "00bf6150",
  "target": "00bf6158",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf615c`](#insn-00bf615c)

~~~json
{
  "source": "00bf615c",
  "target": "00c5e050",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf6164`](#insn-00bf6164)

~~~json
{
  "source": "00bf6164",
  "target": "00c53f5c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
