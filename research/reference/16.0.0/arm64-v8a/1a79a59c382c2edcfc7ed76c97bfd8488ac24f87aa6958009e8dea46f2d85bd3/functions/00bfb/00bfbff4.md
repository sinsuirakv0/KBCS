# 00bfbff4

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b7f5ac`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f5ac.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0072.md#compare-c2150d99161d3f6c9ce0503236ee3675)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bfc41c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfc41c.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0041.md#compare-9cec2485bf4918c70c2bdd45ade6f918)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfbff4",
  "name": "_ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEErsEPNS_15basic_streambufIcS2_EE",
  "size": 344,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "12e9ee9e58086e4d6c02119e934d964aa1db42503e5e86bcbd17af440971ffdd",
  "source_text_sha256": "12e9ee9e58086e4d6c02119e934d964aa1db42503e5e86bcbd17af440971ffdd",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfbff4",
        "00bfc14b"
      ]
    ],
    "bytes_sha256": "059f3591754b8d42abe2c223e61ffdc48d0d063c8fbf36886a65996dcc3ef57b",
    "instruction_count": 86,
    "instruction_bytes": 344,
    "body_bytes": 344,
    "indirect": 3,
    "unresolved": 3
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57ea0](../00c57/00c57ea0.md)
- [00c599d0](../00c59/00c599d0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1697 bytes

~~~c

long * _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEErsEPNS_15basic_streambufIcS2_EE
                 (long *param_1,long *param_2)

{
  long lVar1;
  undefined1 *puVar2;
  uint uVar3;
  int iVar4;
  long *plVar5;
  uint uVar6;
  char local_34 [4];
  
  param_1[1] = 0;
  _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE6sentryC1ERS3_b(local_34,param_1,1);
  if (local_34[0] == '\0') {
    return param_1;
  }
  if (param_2 != (long *)0x0) {
LAB_00bfc060:
    plVar5 = *(long **)((long)param_1 + *(long *)(*param_1 + -0x18) + 0x28);
    if ((byte *)plVar5[3] == (byte *)plVar5[4]) {
      uVar3 = (**(code **)(*plVar5 + 0x48))();
      if (uVar3 == 0xffffffff) {
        uVar3 = 2;
        goto LAB_00bfc108;
      }
    }
    else {
      uVar3 = (uint)*(byte *)plVar5[3];
    }
    puVar2 = (undefined1 *)param_2[6];
    if (puVar2 == (undefined1 *)param_2[7]) {
      iVar4 = (**(code **)(*param_2 + 0x68))(param_2,uVar3 & 0xff);
      if (iVar4 == -1) goto LAB_00bfc104;
    }
    else {
      param_2[6] = (long)(puVar2 + 1);
      *puVar2 = (char)uVar3;
    }
    if (param_1[1] != 0x7fffffffffffffff) {
      param_1[1] = param_1[1] + 1;
    }
    plVar5 = *(long **)((long)param_1 + *(long *)(*param_1 + -0x18) + 0x28);
    if (plVar5[3] == plVar5[4]) {
      (**(code **)(*plVar5 + 0x50))();
    }
    else {
      plVar5[3] = plVar5[3] + 1;
    }
    goto LAB_00bfc060;
  }
  uVar6 = 4;
LAB_00bfc118:
  lVar1 = (long)param_1 + *(long *)(*param_1 + -0x18);
  _ZNSt6__ndk18ios_base5clearEj(lVar1,*(uint *)(lVar1 + 0x20) | uVar6);
  return param_1;
LAB_00bfc104:
  uVar3 = 0;
LAB_00bfc108:
  uVar6 = uVar3 | 4;
  if (param_1[1] != 0) {
    uVar6 = uVar3;
  }
  goto LAB_00bfc118;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfbff4"></a> `00bfbff4` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfbff8"></a> `00bfbff8` | `ff 03 01 d1` | sub sp,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00bfbffc"></a> `00bfbffc` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfc000"></a> `00bfc000` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfc004"></a> `00bfc004` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bfc008"></a> `00bfc008` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bfc00c"></a> `00bfc00c` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bfc010"></a> `00bfc010` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00bfc014"></a> `00bfc014` | `1f 04 00 f9` | str xzr,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bfc018"></a> `00bfc018` | `a0 13 00 d1` | sub x0,x29,#0x4 | `FALL_THROUGH`
<a id="insn-00bfc01c"></a> `00bfc01c` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bfc020"></a> `00bfc020` | `22 00 80 52` | mov w2,#0x1 | `FALL_THROUGH`
<a id="insn-00bfc024"></a> `00bfc024` | `6b 76 01 94` | bl 0x00c599d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bfc028"></a> `00bfc028` | `a8 c3 5f 38` | ldurb w8,[x29, #-0x4] | `FALL_THROUGH`
<a id="insn-00bfc02c"></a> `00bfc02c` | `28 08 00 34` | cbz w8,0x00bfc130 | `CONDITIONAL_JUMP`
<a id="insn-00bfc030"></a> `00bfc030` | `34 06 00 b4` | cbz x20,0x00bfc0f4 | `CONDITIONAL_JUMP`
<a id="insn-00bfc034"></a> `00bfc034` | `75 a2 00 91` | add x21,x19,#0x28 | `FALL_THROUGH`
<a id="insn-00bfc038"></a> `00bfc038` | `16 00 f0 92` | mov x22,#0x7fffffffffffffff | `FALL_THROUGH`
<a id="insn-00bfc03c"></a> `00bfc03c` | `09 00 00 14` | b 0x00bfc060 | `UNCONDITIONAL_JUMP`
<a id="insn-00bfc040"></a> `00bfc040` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bfc044"></a> `00bfc044` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfc048"></a> `00bfc048` | `a0 6a 68 f8` | ldr x0,[x21, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00bfc04c"></a> `00bfc04c` | `08 a4 41 a9` | ldp x8,x9,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00bfc050"></a> `00bfc050` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bfc054"></a> `00bfc054` | `80 04 00 54` | b.eq 0x00bfc0e4 | `CONDITIONAL_JUMP`
<a id="insn-00bfc058"></a> `00bfc058` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bfc05c"></a> `00bfc05c` | `08 0c 00 f9` | str x8,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00bfc060"></a> `00bfc060` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bfc064"></a> `00bfc064` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfc068"></a> `00bfc068` | `a0 6a 68 f8` | ldr x0,[x21, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00bfc06c"></a> `00bfc06c` | `08 a4 41 a9` | ldp x8,x9,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00bfc070"></a> `00bfc070` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bfc074"></a> `00bfc074` | `60 00 00 54` | b.eq 0x00bfc080 | `CONDITIONAL_JUMP`
<a id="insn-00bfc078"></a> `00bfc078` | `00 01 40 39` | ldrb w0,[x8] | `FALL_THROUGH`
<a id="insn-00bfc07c"></a> `00bfc07c` | `06 00 00 14` | b 0x00bfc094 | `UNCONDITIONAL_JUMP`
<a id="insn-00bfc080"></a> `00bfc080` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bfc084"></a> `00bfc084` | `08 25 40 f9` | ldr x8,[x8, #0x48] | `FALL_THROUGH`
<a id="insn-00bfc088"></a> `00bfc088` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bfc08c"></a> `00bfc08c` | `1f 04 00 31` | cmn w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bfc090"></a> `00bfc090` | `60 03 00 54` | b.eq 0x00bfc0fc | `CONDITIONAL_JUMP`
<a id="insn-00bfc094"></a> `00bfc094` | `88 26 43 a9` | ldp x8,x9,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-00bfc098"></a> `00bfc098` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bfc09c"></a> `00bfc09c` | `a0 00 00 54` | b.eq 0x00bfc0b0 | `CONDITIONAL_JUMP`
<a id="insn-00bfc0a0"></a> `00bfc0a0` | `09 05 00 91` | add x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bfc0a4"></a> `00bfc0a4` | `89 1a 00 f9` | str x9,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-00bfc0a8"></a> `00bfc0a8` | `00 01 00 39` | strb w0,[x8] | `FALL_THROUGH`
<a id="insn-00bfc0ac"></a> `00bfc0ac` | `08 00 00 14` | b 0x00bfc0cc | `UNCONDITIONAL_JUMP`
<a id="insn-00bfc0b0"></a> `00bfc0b0` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bfc0b4"></a> `00bfc0b4` | `08 35 40 f9` | ldr x8,[x8, #0x68] | `FALL_THROUGH`
<a id="insn-00bfc0b8"></a> `00bfc0b8` | `01 1c 00 12` | and w1,w0,#0xff | `FALL_THROUGH`
<a id="insn-00bfc0bc"></a> `00bfc0bc` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bfc0c0"></a> `00bfc0c0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bfc0c4"></a> `00bfc0c4` | `1f 04 00 31` | cmn w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bfc0c8"></a> `00bfc0c8` | `e0 01 00 54` | b.eq 0x00bfc104 | `CONDITIONAL_JUMP`
<a id="insn-00bfc0cc"></a> `00bfc0cc` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bfc0d0"></a> `00bfc0d0` | `1f 01 16 eb` | cmp x8,x22 | `FALL_THROUGH`
<a id="insn-00bfc0d4"></a> `00bfc0d4` | `60 fb ff 54` | b.eq 0x00bfc040 | `CONDITIONAL_JUMP`
<a id="insn-00bfc0d8"></a> `00bfc0d8` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bfc0dc"></a> `00bfc0dc` | `68 06 00 f9` | str x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bfc0e0"></a> `00bfc0e0` | `d8 ff ff 17` | b 0x00bfc040 | `UNCONDITIONAL_JUMP`
<a id="insn-00bfc0e4"></a> `00bfc0e4` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bfc0e8"></a> `00bfc0e8` | `08 29 40 f9` | ldr x8,[x8, #0x50] | `FALL_THROUGH`
<a id="insn-00bfc0ec"></a> `00bfc0ec` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bfc0f0"></a> `00bfc0f0` | `dc ff ff 17` | b 0x00bfc060 | `UNCONDITIONAL_JUMP`
<a id="insn-00bfc0f4"></a> `00bfc0f4` | `94 00 80 52` | mov w20,#0x4 | `FALL_THROUGH`
<a id="insn-00bfc0f8"></a> `00bfc0f8` | `08 00 00 14` | b 0x00bfc118 | `UNCONDITIONAL_JUMP`
<a id="insn-00bfc0fc"></a> `00bfc0fc` | `48 00 80 52` | mov w8,#0x2 | `FALL_THROUGH`
<a id="insn-00bfc100"></a> `00bfc100` | `02 00 00 14` | b 0x00bfc108 | `UNCONDITIONAL_JUMP`
<a id="insn-00bfc104"></a> `00bfc104` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bfc108"></a> `00bfc108` | `69 06 40 f9` | ldr x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bfc10c"></a> `00bfc10c` | `0a 01 1e 32` | orr w10,w8,#0x4 | `FALL_THROUGH`
<a id="insn-00bfc110"></a> `00bfc110` | `3f 01 00 f1` | cmp x9,#0x0 | `FALL_THROUGH`
<a id="insn-00bfc114"></a> `00bfc114` | `54 01 88 1a` | csel w20,w10,w8,eq | `FALL_THROUGH`
<a id="insn-00bfc118"></a> `00bfc118` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bfc11c"></a> `00bfc11c` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfc120"></a> `00bfc120` | `60 02 08 8b` | add x0,x19,x8 | `FALL_THROUGH`
<a id="insn-00bfc124"></a> `00bfc124` | `08 20 40 b9` | ldr w8,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00bfc128"></a> `00bfc128` | `01 01 14 2a` | orr w1,w8,w20 | `FALL_THROUGH`
<a id="insn-00bfc12c"></a> `00bfc12c` | `5d 6f 01 94` | bl 0x00c57ea0 | `UNCONDITIONAL_CALL`
<a id="insn-00bfc130"></a> `00bfc130` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bfc134"></a> `00bfc134` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bfc138"></a> `00bfc138` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfc13c"></a> `00bfc13c` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfc140"></a> `00bfc140` | `ff 03 01 91` | add sp,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00bfc144"></a> `00bfc144` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfc148"></a> `00bfc148` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfbff4`](#insn-00bfbff4) 範囲 `[['00bfbff4', '00bfc02f']]`
  - `CONDITIONAL_JUMP` [`00bfc02c`](#insn-00bfc02c) → [`00bfc130`](#insn-00bfc130)
  - `FALL_THROUGH` [`00bfc02c`](#insn-00bfc02c) → [`00bfc030`](#insn-00bfc030)
- ブロック [`00bfc030`](#insn-00bfc030) 範囲 `[['00bfc030', '00bfc033']]`
  - `CONDITIONAL_JUMP` [`00bfc030`](#insn-00bfc030) → [`00bfc0f4`](#insn-00bfc0f4)
  - `FALL_THROUGH` [`00bfc030`](#insn-00bfc030) → [`00bfc034`](#insn-00bfc034)
- ブロック [`00bfc034`](#insn-00bfc034) 範囲 `[['00bfc034', '00bfc03f']]`
  - `UNCONDITIONAL_JUMP` [`00bfc03c`](#insn-00bfc03c) → [`00bfc060`](#insn-00bfc060)
- ブロック [`00bfc040`](#insn-00bfc040) 範囲 `[['00bfc040', '00bfc057']]`
  - `CONDITIONAL_JUMP` [`00bfc054`](#insn-00bfc054) → [`00bfc0e4`](#insn-00bfc0e4)
  - `FALL_THROUGH` [`00bfc054`](#insn-00bfc054) → [`00bfc058`](#insn-00bfc058)
- ブロック [`00bfc058`](#insn-00bfc058) 範囲 `[['00bfc058', '00bfc05f']]`
  - `FALL_THROUGH` [`00bfc05c`](#insn-00bfc05c) → [`00bfc060`](#insn-00bfc060)
- ブロック [`00bfc060`](#insn-00bfc060) 範囲 `[['00bfc060', '00bfc077']]`
  - `CONDITIONAL_JUMP` [`00bfc074`](#insn-00bfc074) → [`00bfc080`](#insn-00bfc080)
  - `FALL_THROUGH` [`00bfc074`](#insn-00bfc074) → [`00bfc078`](#insn-00bfc078)
- ブロック [`00bfc078`](#insn-00bfc078) 範囲 `[['00bfc078', '00bfc07f']]`
  - `UNCONDITIONAL_JUMP` [`00bfc07c`](#insn-00bfc07c) → [`00bfc094`](#insn-00bfc094)
- ブロック [`00bfc080`](#insn-00bfc080) 範囲 `[['00bfc080', '00bfc093']]`
  - `CONDITIONAL_JUMP` [`00bfc090`](#insn-00bfc090) → [`00bfc0fc`](#insn-00bfc0fc)
  - `FALL_THROUGH` [`00bfc090`](#insn-00bfc090) → [`00bfc094`](#insn-00bfc094)
- ブロック [`00bfc094`](#insn-00bfc094) 範囲 `[['00bfc094', '00bfc09f']]`
  - `CONDITIONAL_JUMP` [`00bfc09c`](#insn-00bfc09c) → [`00bfc0b0`](#insn-00bfc0b0)
  - `FALL_THROUGH` [`00bfc09c`](#insn-00bfc09c) → [`00bfc0a0`](#insn-00bfc0a0)
- ブロック [`00bfc0a0`](#insn-00bfc0a0) 範囲 `[['00bfc0a0', '00bfc0af']]`
  - `UNCONDITIONAL_JUMP` [`00bfc0ac`](#insn-00bfc0ac) → [`00bfc0cc`](#insn-00bfc0cc)
- ブロック [`00bfc0b0`](#insn-00bfc0b0) 範囲 `[['00bfc0b0', '00bfc0cb']]`
  - `CONDITIONAL_JUMP` [`00bfc0c8`](#insn-00bfc0c8) → [`00bfc104`](#insn-00bfc104)
  - `FALL_THROUGH` [`00bfc0c8`](#insn-00bfc0c8) → [`00bfc0cc`](#insn-00bfc0cc)
- ブロック [`00bfc0cc`](#insn-00bfc0cc) 範囲 `[['00bfc0cc', '00bfc0d7']]`
  - `CONDITIONAL_JUMP` [`00bfc0d4`](#insn-00bfc0d4) → [`00bfc040`](#insn-00bfc040)
  - `FALL_THROUGH` [`00bfc0d4`](#insn-00bfc0d4) → [`00bfc0d8`](#insn-00bfc0d8)
- ブロック [`00bfc0d8`](#insn-00bfc0d8) 範囲 `[['00bfc0d8', '00bfc0e3']]`
  - `UNCONDITIONAL_JUMP` [`00bfc0e0`](#insn-00bfc0e0) → [`00bfc040`](#insn-00bfc040)
- ブロック [`00bfc0e4`](#insn-00bfc0e4) 範囲 `[['00bfc0e4', '00bfc0f3']]`
  - `UNCONDITIONAL_JUMP` [`00bfc0f0`](#insn-00bfc0f0) → [`00bfc060`](#insn-00bfc060)
- ブロック [`00bfc0f4`](#insn-00bfc0f4) 範囲 `[['00bfc0f4', '00bfc0fb']]`
  - `UNCONDITIONAL_JUMP` [`00bfc0f8`](#insn-00bfc0f8) → [`00bfc118`](#insn-00bfc118)
- ブロック [`00bfc0fc`](#insn-00bfc0fc) 範囲 `[['00bfc0fc', '00bfc103']]`
  - `UNCONDITIONAL_JUMP` [`00bfc100`](#insn-00bfc100) → [`00bfc108`](#insn-00bfc108)
- ブロック [`00bfc104`](#insn-00bfc104) 範囲 `[['00bfc104', '00bfc107']]`
  - `FALL_THROUGH` [`00bfc104`](#insn-00bfc104) → [`00bfc108`](#insn-00bfc108)
- ブロック [`00bfc108`](#insn-00bfc108) 範囲 `[['00bfc108', '00bfc117']]`
  - `FALL_THROUGH` [`00bfc114`](#insn-00bfc114) → [`00bfc118`](#insn-00bfc118)
- ブロック [`00bfc118`](#insn-00bfc118) 範囲 `[['00bfc118', '00bfc12f']]`
  - `FALL_THROUGH` [`00bfc12c`](#insn-00bfc12c) → [`00bfc130`](#insn-00bfc130)
- ブロック [`00bfc130`](#insn-00bfc130) 範囲 `[['00bfc130', '00bfc14b']]`

## 命令位置別の参照

- [`00bfbffc`](#insn-00bfbffc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfc000`](#insn-00bfc000) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfc004`](#insn-00bfc004) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfc024`](#insn-00bfc024) → [`00c599d0`](../00c59/00c599d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c599d0` · 推定シンボル `None` · 推定型 `None`
- [`00bfc028`](#insn-00bfc028) → `Stack[-0x34]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfc02c`](#insn-00bfc02c) → [`00bfc130`](#insn-00bfc130) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfc030`](#insn-00bfc030) → [`00bfc0f4`](#insn-00bfc0f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfc03c`](#insn-00bfc03c) → [`00bfc060`](#insn-00bfc060) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfc054`](#insn-00bfc054) → [`00bfc0e4`](#insn-00bfc0e4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfc074`](#insn-00bfc074) → [`00bfc080`](#insn-00bfc080) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfc07c`](#insn-00bfc07c) → [`00bfc094`](#insn-00bfc094) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfc090`](#insn-00bfc090) → [`00bfc0fc`](#insn-00bfc0fc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfc09c`](#insn-00bfc09c) → [`00bfc0b0`](#insn-00bfc0b0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfc0ac`](#insn-00bfc0ac) → [`00bfc0cc`](#insn-00bfc0cc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfc0c8`](#insn-00bfc0c8) → [`00bfc104`](#insn-00bfc104) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfc0d4`](#insn-00bfc0d4) → [`00bfc040`](#insn-00bfc040) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfc0e0`](#insn-00bfc0e0) → [`00bfc040`](#insn-00bfc040) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfc0f0`](#insn-00bfc0f0) → [`00bfc060`](#insn-00bfc060) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfc0f8`](#insn-00bfc0f8) → [`00bfc118`](#insn-00bfc118) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfc100`](#insn-00bfc100) → [`00bfc108`](#insn-00bfc108) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfc12c`](#insn-00bfc12c) → [`00c57ea0`](../00c57/00c57ea0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ea0` · 推定シンボル `None` · 推定型 `None`
- [`00bfc134`](#insn-00bfc134) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfc138`](#insn-00bfc138) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfc13c`](#insn-00bfc13c) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfbffc`](#insn-00bfbffc)

~~~json
{
  "source": "00bfbffc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfc000`](#insn-00bfc000)

~~~json
{
  "source": "00bfc000",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfc004`](#insn-00bfc004)

~~~json
{
  "source": "00bfc004",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfc024`](#insn-00bfc024)

~~~json
{
  "source": "00bfc024",
  "target": "00c599d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfc028`](#insn-00bfc028)

~~~json
{
  "source": "00bfc028",
  "target": "Stack[-0x34]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfc02c`](#insn-00bfc02c)

~~~json
{
  "source": "00bfc02c",
  "target": "00bfc130",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfc030`](#insn-00bfc030)

~~~json
{
  "source": "00bfc030",
  "target": "00bfc0f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfc03c`](#insn-00bfc03c)

~~~json
{
  "source": "00bfc03c",
  "target": "00bfc060",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfc054`](#insn-00bfc054)

~~~json
{
  "source": "00bfc054",
  "target": "00bfc0e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfc074`](#insn-00bfc074)

~~~json
{
  "source": "00bfc074",
  "target": "00bfc080",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfc07c`](#insn-00bfc07c)

~~~json
{
  "source": "00bfc07c",
  "target": "00bfc094",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfc090`](#insn-00bfc090)

~~~json
{
  "source": "00bfc090",
  "target": "00bfc0fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfc09c`](#insn-00bfc09c)

~~~json
{
  "source": "00bfc09c",
  "target": "00bfc0b0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfc0ac`](#insn-00bfc0ac)

~~~json
{
  "source": "00bfc0ac",
  "target": "00bfc0cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfc0c8`](#insn-00bfc0c8)

~~~json
{
  "source": "00bfc0c8",
  "target": "00bfc104",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfc0d4`](#insn-00bfc0d4)

~~~json
{
  "source": "00bfc0d4",
  "target": "00bfc040",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfc0e0`](#insn-00bfc0e0)

~~~json
{
  "source": "00bfc0e0",
  "target": "00bfc040",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfc0f0`](#insn-00bfc0f0)

~~~json
{
  "source": "00bfc0f0",
  "target": "00bfc060",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfc0f8`](#insn-00bfc0f8)

~~~json
{
  "source": "00bfc0f8",
  "target": "00bfc118",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfc100`](#insn-00bfc100)

~~~json
{
  "source": "00bfc100",
  "target": "00bfc108",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfc12c`](#insn-00bfc12c)

~~~json
{
  "source": "00bfc12c",
  "target": "00c57ea0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfc134`](#insn-00bfc134)

~~~json
{
  "source": "00bfc134",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfc138`](#insn-00bfc138)

~~~json
{
  "source": "00bfc138",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfc13c`](#insn-00bfc13c)

~~~json
{
  "source": "00bfc13c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
