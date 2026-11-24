# 00c3decc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00c3de30`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3de30.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0090.md#compare-7c6e2e34e7ed2c6f913b73d2f15e80ee)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00c3eec0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3e/00c3eec0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0090.md#compare-f11857ebc8b6f747474280bc0cc78aec)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00c3decc",
  "name": "FUN_00c3decc",
  "size": 376,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ec3d8d1da4547b22035e7bb72ab272b1a2038addac1f1e8a4036f6bccb1abfc4",
  "source_text_sha256": "ec3d8d1da4547b22035e7bb72ab272b1a2038addac1f1e8a4036f6bccb1abfc4",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00c3decc",
        "00c3e043"
      ]
    ],
    "bytes_sha256": "6b20bd54f0de209527da5d5c033ad973f038e7cff7095e04ff40238e6cbc0f67",
    "instruction_count": 94,
    "instruction_bytes": 376,
    "body_bytes": 376,
    "indirect": 4,
    "unresolved": 4
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5a170](../00c5a/00c5a170.md)
- [00c5b210](../00c5b/00c5b210.md)

## 関連文字列（未確認候補）

~~~text
"construction vtable for "
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2122 bytes

~~~c

void FUN_00c3decc(long param_1,undefined8 *param_2)

{
  ulong uVar1;
  char *pcVar2;
  undefined8 uVar3;
  undefined8 uVar4;
  void *pvVar5;
  long lVar6;
  size_t sVar7;
  long *plVar8;
  
  lVar6 = param_2[1];
  pvVar5 = (void *)*param_2;
  if ((ulong)param_2[2] < lVar6 + 0x18U) {
    sVar7 = param_2[2] * 2;
    uVar1 = lVar6 + 0x3f8;
    if (sVar7 < uVar1 || sVar7 - uVar1 == 0) {
      sVar7 = uVar1;
    }
    param_2[2] = sVar7;
    pvVar5 = realloc(pvVar5,sVar7);
    *param_2 = pvVar5;
    if (pvVar5 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
      abort();
    }
    lVar6 = param_2[1];
  }
  uVar4 = s_construction_vtable_for_002bb108._16_8_;
  uVar3 = s_construction_vtable_for_002bb108._0_8_;
  pcVar2 = (char *)((long)pvVar5 + lVar6);
  *(undefined8 *)(pcVar2 + 8) = s_construction_vtable_for_002bb108._8_8_;
  *(undefined8 *)pcVar2 = uVar3;
  *(undefined8 *)(pcVar2 + 0x10) = uVar4;
  plVar8 = *(long **)(param_1 + 0x10);
  lVar6 = *plVar8;
  param_2[1] = param_2[1] + 0x18;
  (**(code **)(lVar6 + 0x20))(plVar8,param_2);
  if ((*(ushort *)((long)plVar8 + 9) & 0xc0) != 0x40) {
    (**(code **)(*plVar8 + 0x28))(plVar8,param_2);
  }
  lVar6 = param_2[1];
  pvVar5 = (void *)*param_2;
  if ((ulong)param_2[2] < lVar6 + 4U) {
    sVar7 = param_2[2] * 2;
    uVar1 = lVar6 + 0x3e4;
    if (sVar7 < uVar1 || sVar7 - uVar1 == 0) {
      sVar7 = uVar1;
    }
    param_2[2] = sVar7;
    pvVar5 = realloc(pvVar5,sVar7);
    *param_2 = pvVar5;
    if (pvVar5 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
      abort();
    }
    lVar6 = param_2[1];
  }
  *(undefined4 *)((long)pvVar5 + lVar6) = 0x2d6e692d;
  plVar8 = *(long **)(param_1 + 0x18);
  lVar6 = *plVar8;
  param_2[1] = param_2[1] + 4;
  (**(code **)(lVar6 + 0x20))(plVar8,param_2);
  if ((*(ushort *)((long)plVar8 + 9) & 0xc0) == 0x40) {
    return;
  }
                    /* WARNING: Could not recover jumptable at 0x00c3e038. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  (**(code **)(*plVar8 + 0x28))(plVar8,param_2);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00c3decc"></a> `00c3decc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00c3ded0"></a> `00c3ded0` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00c3ded4"></a> `00c3ded4` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00c3ded8"></a> `00c3ded8` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00c3dedc"></a> `00c3dedc` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00c3dee0"></a> `00c3dee0` | `29 a8 40 a9` | ldp x9,x10,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00c3dee4"></a> `00c3dee4` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00c3dee8"></a> `00c3dee8` | `28 00 40 f9` | ldr x8,[x1] | `FALL_THROUGH`
<a id="insn-00c3deec"></a> `00c3deec` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00c3def0"></a> `00c3def0` | `2b 61 00 91` | add x11,x9,#0x18 | `FALL_THROUGH`
<a id="insn-00c3def4"></a> `00c3def4` | `7f 01 0a eb` | cmp x11,x10 | `FALL_THROUGH`
<a id="insn-00c3def8"></a> `00c3def8` | `89 01 00 54` | b.ls 0x00c3df28 | `CONDITIONAL_JUMP`
<a id="insn-00c3defc"></a> `00c3defc` | `4a f9 7f d3` | lsl x10,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00c3df00"></a> `00c3df00` | `29 e1 0f 91` | add x9,x9,#0x3f8 | `FALL_THROUGH`
<a id="insn-00c3df04"></a> `00c3df04` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00c3df08"></a> `00c3df08` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00c3df0c"></a> `00c3df0c` | `41 81 89 9a` | csel x1,x10,x9,hi | `FALL_THROUGH`
<a id="insn-00c3df10"></a> `00c3df10` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00c3df14"></a> `00c3df14` | `97 70 00 94` | bl 0x00c5a170 | `UNCONDITIONAL_CALL`
<a id="insn-00c3df18"></a> `00c3df18` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00c3df1c"></a> `00c3df1c` | `00 09 00 b4` | cbz x0,0x00c3e03c | `CONDITIONAL_JUMP`
<a id="insn-00c3df20"></a> `00c3df20` | `69 06 40 f9` | ldr x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00c3df24"></a> `00c3df24` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00c3df28"></a> `00c3df28` | `ea b3 ff d0` | adrp x10,0x2bb000 | `FALL_THROUGH`
<a id="insn-00c3df2c"></a> `00c3df2c` | `4a 21 04 91` | add x10,x10,#0x108 | `FALL_THROUGH`
<a id="insn-00c3df30"></a> `00c3df30` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00c3df34"></a> `00c3df34` | `40 01 c0 3d` | ldr q0,[x10] | `FALL_THROUGH`
<a id="insn-00c3df38"></a> `00c3df38` | `49 09 40 f9` | ldr x9,[x10, #0x10] | `FALL_THROUGH`
<a id="insn-00c3df3c"></a> `00c3df3c` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00c3df40"></a> `00c3df40` | `00 01 80 3d` | str q0,[x8] | `FALL_THROUGH`
<a id="insn-00c3df44"></a> `00c3df44` | `09 09 00 f9` | str x9,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00c3df48"></a> `00c3df48` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00c3df4c"></a> `00c3df4c` | `95 0a 40 f9` | ldr x21,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00c3df50"></a> `00c3df50` | `08 61 00 91` | add x8,x8,#0x18 | `FALL_THROUGH`
<a id="insn-00c3df54"></a> `00c3df54` | `a9 02 40 f9` | ldr x9,[x21] | `FALL_THROUGH`
<a id="insn-00c3df58"></a> `00c3df58` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00c3df5c"></a> `00c3df5c` | `68 06 00 f9` | str x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00c3df60"></a> `00c3df60` | `28 11 40 f9` | ldr x8,[x9, #0x20] | `FALL_THROUGH`
<a id="insn-00c3df64"></a> `00c3df64` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00c3df68"></a> `00c3df68` | `a8 92 40 78` | ldurh w8,[x21, #0x9] | `FALL_THROUGH`
<a id="insn-00c3df6c"></a> `00c3df6c` | `08 05 1a 12` | and w8,w8,#0xc0 | `FALL_THROUGH`
<a id="insn-00c3df70"></a> `00c3df70` | `1f 01 01 71` | cmp w8,#0x40 | `FALL_THROUGH`
<a id="insn-00c3df74"></a> `00c3df74` | `c0 00 00 54` | b.eq 0x00c3df8c | `CONDITIONAL_JUMP`
<a id="insn-00c3df78"></a> `00c3df78` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00c3df7c"></a> `00c3df7c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00c3df80"></a> `00c3df80` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00c3df84"></a> `00c3df84` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00c3df88"></a> `00c3df88` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00c3df8c"></a> `00c3df8c` | `68 a6 40 a9` | ldp x8,x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00c3df90"></a> `00c3df90` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00c3df94"></a> `00c3df94` | `0a 11 00 91` | add x10,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00c3df98"></a> `00c3df98` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00c3df9c"></a> `00c3df9c` | `49 01 00 54` | b.ls 0x00c3dfc4 | `CONDITIONAL_JUMP`
<a id="insn-00c3dfa0"></a> `00c3dfa0` | `29 f9 7f d3` | lsl x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00c3dfa4"></a> `00c3dfa4` | `08 91 0f 91` | add x8,x8,#0x3e4 | `FALL_THROUGH`
<a id="insn-00c3dfa8"></a> `00c3dfa8` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00c3dfac"></a> `00c3dfac` | `21 81 88 9a` | csel x1,x9,x8,hi | `FALL_THROUGH`
<a id="insn-00c3dfb0"></a> `00c3dfb0` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00c3dfb4"></a> `00c3dfb4` | `6f 70 00 94` | bl 0x00c5a170 | `UNCONDITIONAL_CALL`
<a id="insn-00c3dfb8"></a> `00c3dfb8` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00c3dfbc"></a> `00c3dfbc` | `20 04 00 b4` | cbz x0,0x00c3e040 | `CONDITIONAL_JUMP`
<a id="insn-00c3dfc0"></a> `00c3dfc0` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00c3dfc4"></a> `00c3dfc4` | `a9 25 8d 52` | mov w9,#0x692d | `FALL_THROUGH`
<a id="insn-00c3dfc8"></a> `00c3dfc8` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00c3dfcc"></a> `00c3dfcc` | `c9 ad a5 72` | movk w9,#0x2d6e, LSL #16 | `FALL_THROUGH`
<a id="insn-00c3dfd0"></a> `00c3dfd0` | `09 68 28 b8` | str w9,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00c3dfd4"></a> `00c3dfd4` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00c3dfd8"></a> `00c3dfd8` | `94 0e 40 f9` | ldr x20,[x20, #0x18] | `FALL_THROUGH`
<a id="insn-00c3dfdc"></a> `00c3dfdc` | `08 11 00 91` | add x8,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00c3dfe0"></a> `00c3dfe0` | `89 02 40 f9` | ldr x9,[x20] | `FALL_THROUGH`
<a id="insn-00c3dfe4"></a> `00c3dfe4` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00c3dfe8"></a> `00c3dfe8` | `68 06 00 f9` | str x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00c3dfec"></a> `00c3dfec` | `28 11 40 f9` | ldr x8,[x9, #0x20] | `FALL_THROUGH`
<a id="insn-00c3dff0"></a> `00c3dff0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00c3dff4"></a> `00c3dff4` | `88 92 40 78` | ldurh w8,[x20, #0x9] | `FALL_THROUGH`
<a id="insn-00c3dff8"></a> `00c3dff8` | `08 05 1a 12` | and w8,w8,#0xc0 | `FALL_THROUGH`
<a id="insn-00c3dffc"></a> `00c3dffc` | `1f 01 01 71` | cmp w8,#0x40 | `FALL_THROUGH`
<a id="insn-00c3e000"></a> `00c3e000` | `c1 00 00 54` | b.ne 0x00c3e018 | `CONDITIONAL_JUMP`
<a id="insn-00c3e004"></a> `00c3e004` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00c3e008"></a> `00c3e008` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00c3e00c"></a> `00c3e00c` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00c3e010"></a> `00c3e010` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00c3e014"></a> `00c3e014` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00c3e018"></a> `00c3e018` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00c3e01c"></a> `00c3e01c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00c3e020"></a> `00c3e020` | `10 15 40 f9` | ldr x16,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00c3e024"></a> `00c3e024` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00c3e028"></a> `00c3e028` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00c3e02c"></a> `00c3e02c` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00c3e030"></a> `00c3e030` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00c3e034"></a> `00c3e034` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00c3e038"></a> `00c3e038` | `00 02 1f d6` | br x16 | `COMPUTED_JUMP`
<a id="insn-00c3e03c"></a> `00c3e03c` | `75 74 00 94` | bl 0x00c5b210 | `CALL_TERMINATOR`
<a id="insn-00c3e040"></a> `00c3e040` | `74 74 00 94` | bl 0x00c5b210 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00c3decc`](#insn-00c3decc) 範囲 `[['00c3decc', '00c3defb']]`
  - `CONDITIONAL_JUMP` [`00c3def8`](#insn-00c3def8) → [`00c3df28`](#insn-00c3df28)
  - `FALL_THROUGH` [`00c3def8`](#insn-00c3def8) → [`00c3defc`](#insn-00c3defc)
- ブロック [`00c3defc`](#insn-00c3defc) 範囲 `[['00c3defc', '00c3df1f']]`
  - `CONDITIONAL_JUMP` [`00c3df1c`](#insn-00c3df1c) → [`00c3e03c`](#insn-00c3e03c)
  - `FALL_THROUGH` [`00c3df1c`](#insn-00c3df1c) → [`00c3df20`](#insn-00c3df20)
- ブロック [`00c3df20`](#insn-00c3df20) 範囲 `[['00c3df20', '00c3df27']]`
  - `FALL_THROUGH` [`00c3df24`](#insn-00c3df24) → [`00c3df28`](#insn-00c3df28)
- ブロック [`00c3df28`](#insn-00c3df28) 範囲 `[['00c3df28', '00c3df77']]`
  - `CONDITIONAL_JUMP` [`00c3df74`](#insn-00c3df74) → [`00c3df8c`](#insn-00c3df8c)
  - `FALL_THROUGH` [`00c3df74`](#insn-00c3df74) → [`00c3df78`](#insn-00c3df78)
- ブロック [`00c3df78`](#insn-00c3df78) 範囲 `[['00c3df78', '00c3df8b']]`
  - `FALL_THROUGH` [`00c3df88`](#insn-00c3df88) → [`00c3df8c`](#insn-00c3df8c)
- ブロック [`00c3df8c`](#insn-00c3df8c) 範囲 `[['00c3df8c', '00c3df9f']]`
  - `CONDITIONAL_JUMP` [`00c3df9c`](#insn-00c3df9c) → [`00c3dfc4`](#insn-00c3dfc4)
  - `FALL_THROUGH` [`00c3df9c`](#insn-00c3df9c) → [`00c3dfa0`](#insn-00c3dfa0)
- ブロック [`00c3dfa0`](#insn-00c3dfa0) 範囲 `[['00c3dfa0', '00c3dfbf']]`
  - `CONDITIONAL_JUMP` [`00c3dfbc`](#insn-00c3dfbc) → [`00c3e040`](#insn-00c3e040)
  - `FALL_THROUGH` [`00c3dfbc`](#insn-00c3dfbc) → [`00c3dfc0`](#insn-00c3dfc0)
- ブロック [`00c3dfc0`](#insn-00c3dfc0) 範囲 `[['00c3dfc0', '00c3dfc3']]`
  - `FALL_THROUGH` [`00c3dfc0`](#insn-00c3dfc0) → [`00c3dfc4`](#insn-00c3dfc4)
- ブロック [`00c3dfc4`](#insn-00c3dfc4) 範囲 `[['00c3dfc4', '00c3e003']]`
  - `CONDITIONAL_JUMP` [`00c3e000`](#insn-00c3e000) → [`00c3e018`](#insn-00c3e018)
  - `FALL_THROUGH` [`00c3e000`](#insn-00c3e000) → [`00c3e004`](#insn-00c3e004)
- ブロック [`00c3e004`](#insn-00c3e004) 範囲 `[['00c3e004', '00c3e017']]`
- ブロック [`00c3e018`](#insn-00c3e018) 範囲 `[['00c3e018', '00c3e03b']]`
- ブロック [`00c3e03c`](#insn-00c3e03c) 範囲 `[['00c3e03c', '00c3e03f']]`
- ブロック [`00c3e040`](#insn-00c3e040) 範囲 `[['00c3e040', '00c3e043']]`

## 命令位置別の参照

- [`00c3ded0`](#insn-00c3ded0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3ded4`](#insn-00c3ded4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3ded8`](#insn-00c3ded8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3def8`](#insn-00c3def8) → [`00c3df28`](#insn-00c3df28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3df14`](#insn-00c3df14) → [`00c5a170`](../00c5a/00c5a170.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a170` · 推定シンボル `None` · 推定型 `None`
- [`00c3df1c`](#insn-00c3df1c) → [`00c3e03c`](#insn-00c3e03c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3df34`](#insn-00c3df34) → `002bb108`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00c3df38`](#insn-00c3df38) → `002bb118`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00c3df74`](#insn-00c3df74) → [`00c3df8c`](#insn-00c3df8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3df9c`](#insn-00c3df9c) → [`00c3dfc4`](#insn-00c3dfc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3dfb4`](#insn-00c3dfb4) → [`00c5a170`](../00c5a/00c5a170.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a170` · 推定シンボル `None` · 推定型 `None`
- [`00c3dfbc`](#insn-00c3dfbc) → [`00c3e040`](#insn-00c3e040) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3e000`](#insn-00c3e000) → [`00c3e018`](#insn-00c3e018) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3e004`](#insn-00c3e004) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3e008`](#insn-00c3e008) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3e00c`](#insn-00c3e00c) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3e028`](#insn-00c3e028) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3e02c`](#insn-00c3e02c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3e030`](#insn-00c3e030) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3e03c`](#insn-00c3e03c) → [`00c5b210`](../00c5b/00c5b210.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b210` · 推定シンボル `None` · 推定型 `None`
- [`00c3e040`](#insn-00c3e040) → [`00c5b210`](../00c5b/00c5b210.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b210` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00c3ded0`](#insn-00c3ded0)

~~~json
{
  "source": "00c3ded0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3ded4`](#insn-00c3ded4)

~~~json
{
  "source": "00c3ded4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3ded8`](#insn-00c3ded8)

~~~json
{
  "source": "00c3ded8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3def8`](#insn-00c3def8)

~~~json
{
  "source": "00c3def8",
  "target": "00c3df28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3df14`](#insn-00c3df14)

~~~json
{
  "source": "00c3df14",
  "target": "00c5a170",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c3df1c`](#insn-00c3df1c)

~~~json
{
  "source": "00c3df1c",
  "target": "00c3e03c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3df34`](#insn-00c3df34)

~~~json
{
  "source": "00c3df34",
  "target": "002bb108",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002bb108",
  "offset": 0,
  "size": 25,
  "datatype": "string",
  "bytes": "636f6e737472756374696f6e20767461626c6520666f722000",
  "capture_start": "002bb108",
  "capture_bytes": 25,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00c3df38`](#insn-00c3df38)

~~~json
{
  "source": "00c3df38",
  "target": "002bb118",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002bb108",
  "offset": 16,
  "size": 25,
  "datatype": "string",
  "bytes": "636f6e737472756374696f6e20767461626c6520666f722000",
  "capture_start": "002bb108",
  "capture_bytes": 25,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00c3df74`](#insn-00c3df74)

~~~json
{
  "source": "00c3df74",
  "target": "00c3df8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3df9c`](#insn-00c3df9c)

~~~json
{
  "source": "00c3df9c",
  "target": "00c3dfc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3dfb4`](#insn-00c3dfb4)

~~~json
{
  "source": "00c3dfb4",
  "target": "00c5a170",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c3dfbc`](#insn-00c3dfbc)

~~~json
{
  "source": "00c3dfbc",
  "target": "00c3e040",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3e000`](#insn-00c3e000)

~~~json
{
  "source": "00c3e000",
  "target": "00c3e018",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3e004`](#insn-00c3e004)

~~~json
{
  "source": "00c3e004",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3e008`](#insn-00c3e008)

~~~json
{
  "source": "00c3e008",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3e00c`](#insn-00c3e00c)

~~~json
{
  "source": "00c3e00c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3e028`](#insn-00c3e028)

~~~json
{
  "source": "00c3e028",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3e02c`](#insn-00c3e02c)

~~~json
{
  "source": "00c3e02c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3e030`](#insn-00c3e030)

~~~json
{
  "source": "00c3e030",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3e03c`](#insn-00c3e03c)

~~~json
{
  "source": "00c3e03c",
  "target": "00c5b210",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c3e040`](#insn-00c3e040)

~~~json
{
  "source": "00c3e040",
  "target": "00c5b210",
  "target_space": "ram",
  "resolution": "function"
}
~~~
