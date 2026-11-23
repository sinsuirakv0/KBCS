# 00a6defc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00a6defc`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6d/00a6defc.md) · 移動量 `+0x0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/reference_unresolved-0017.md#compare-2d70c27dd2e7307d5321eba97416a7ba)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00a6defc",
  "name": "FUN_00a6defc",
  "size": 348,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6f58d058e4443fcb979bfda0854a09ff0afaf8516ce198c9b391ecbdcb15e480",
  "source_text_sha256": "6f58d058e4443fcb979bfda0854a09ff0afaf8516ce198c9b391ecbdcb15e480",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00a6defc",
        "00a6e057"
      ]
    ],
    "bytes_sha256": "3fe7e1dc15b40e23d652b015263838990c9346139bbf7447122ca6795afbda24",
    "instruction_count": 87,
    "instruction_bytes": 348,
    "body_bytes": 348,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

- [00a6db78](../00a6d/00a6db78.md)

## 呼び出し先

- [0041e380](../0041e/0041e380.md)
- [00a6e058](../00a6e/00a6e058.md)
- [00bd6d60](../00bd6/00bd6d60.md)
- [00bd6d90](../00bd6/00bd6d90.md)
- [00bdaf30](../00bda/00bdaf30.md)
- [00bdaf40](../00bda/00bdaf40.md)
- [00bdaf60](../00bda/00bdaf60.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2209 bytes

~~~c

undefined8 * FUN_00a6defc(long *param_1,undefined8 *param_2)

{
  ulong uVar1;
  undefined8 *puVar2;
  long lVar3;
  long lVar4;
  undefined8 *puVar5;
  undefined8 *puVar6;
  undefined8 *puVar7;
  ulong uVar8;
  undefined8 *__ptr;
  long *plVar9;
  undefined8 *puVar10;
  long lVar11;
  undefined8 uVar12;
  
  __ptr = (undefined8 *)*param_1;
  puVar10 = (undefined8 *)param_1[1];
  lVar11 = (long)puVar10 - (long)__ptr >> 4;
  uVar1 = lVar11 + 1;
  if (uVar1 >> 0x3c != 0) {
    FUN_00a6e058(param_1);
LAB_00a6e054:
                    /* WARNING: Subroutine does not return */
                    /* catch() { ... } // from try @ 00a6e230 with catch @ 00a6e054 */
    FUN_0041e380();
  }
  uVar8 = param_1[2] - (long)__ptr >> 3;
  if (uVar8 <= uVar1) {
    uVar8 = uVar1;
  }
  if (0x7fffffffffffffef < (ulong)(param_1[2] - (long)__ptr)) {
    uVar8 = 0xfffffffffffffff;
  }
  if (uVar8 == 0) {
    lVar3 = 0;
  }
  else {
    if (uVar8 >> 0x3c != 0) goto LAB_00a6e054;
    lVar3 = _Znwm(uVar8 << 4);
  }
  lVar4 = param_2[1];
  uVar12 = *param_2;
  puVar2 = (undefined8 *)(lVar3 + lVar11 * 0x10);
  puVar2[1] = lVar4;
  *puVar2 = uVar12;
  if (lVar4 != 0) {
    FUN_00bd6d60(1,lVar4 + 8);
    __ptr = (undefined8 *)*param_1;
    puVar10 = (undefined8 *)param_1[1];
    lVar11 = (long)puVar10 - (long)__ptr >> 4;
  }
  puVar5 = puVar2 + lVar11 * -2;
  puVar6 = __ptr;
  if (__ptr != puVar10) {
    do {
      uVar12 = *puVar6;
      puVar5[1] = puVar6[1];
      *puVar5 = uVar12;
      puVar7 = puVar6 + 2;
      *puVar6 = 0;
      puVar6[1] = 0;
      puVar5 = puVar5 + 2;
      puVar6 = puVar7;
    } while (puVar7 != puVar10);
    do {
      plVar9 = (long *)__ptr[1];
      if ((plVar9 != (long *)0x0) &&
         (lVar4 = FUN_00bd6d90(0xffffffffffffffff,plVar9 + 1), lVar4 == 0)) {
        (**(code **)(*plVar9 + 0x10))(plVar9);
        _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar9);
      }
      __ptr = __ptr + 2;
    } while (__ptr != puVar10);
    __ptr = (undefined8 *)*param_1;
  }
  *param_1 = (long)(puVar2 + lVar11 * -2);
  param_1[1] = (long)(puVar2 + 2);
  param_1[2] = lVar3 + uVar8 * 0x10;
  if (__ptr != (undefined8 *)0x0) {
    _ZdlPv(__ptr);
  }
  return puVar2 + 2;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00a6defc"></a> `00a6defc` | `fd 7b bb a9` | stp x29,x30,[sp, #-0x50]! | `FALL_THROUGH`
<a id="insn-00a6df00"></a> `00a6df00` | `f9 0b 00 f9` | str x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a6df04"></a> `00a6df04` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00a6df08"></a> `00a6df08` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00a6df0c"></a> `00a6df0c` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00a6df10"></a> `00a6df10` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00a6df14"></a> `00a6df14` | `14 5c 40 a9` | ldp x20,x23,[x0] | `FALL_THROUGH`
<a id="insn-00a6df18"></a> `00a6df18` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00a6df1c"></a> `00a6df1c` | `e8 02 14 cb` | sub x8,x23,x20 | `FALL_THROUGH`
<a id="insn-00a6df20"></a> `00a6df20` | `19 fd 44 93` | asr x25,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00a6df24"></a> `00a6df24` | `28 07 00 91` | add x8,x25,#0x1 | `FALL_THROUGH`
<a id="insn-00a6df28"></a> `00a6df28` | `09 fd 7c d3` | lsr x9,x8,#0x3c | `FALL_THROUGH`
<a id="insn-00a6df2c"></a> `00a6df2c` | `09 09 00 b5` | cbnz x9,0x00a6e04c | `CONDITIONAL_JUMP`
<a id="insn-00a6df30"></a> `00a6df30` | `69 0a 40 f9` | ldr x9,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00a6df34"></a> `00a6df34` | `eb eb 7c b2` | orr x11,xzr,#0x7ffffffffffffff0 | `FALL_THROUGH`
<a id="insn-00a6df38"></a> `00a6df38` | `f6 03 01 aa` | mov x22,x1 | `FALL_THROUGH`
<a id="insn-00a6df3c"></a> `00a6df3c` | `29 01 14 cb` | sub x9,x9,x20 | `FALL_THROUGH`
<a id="insn-00a6df40"></a> `00a6df40` | `2a fd 43 93` | asr x10,x9,#0x3 | `FALL_THROUGH`
<a id="insn-00a6df44"></a> `00a6df44` | `5f 01 08 eb` | cmp x10,x8 | `FALL_THROUGH`
<a id="insn-00a6df48"></a> `00a6df48` | `48 81 88 9a` | csel x8,x10,x8,hi | `FALL_THROUGH`
<a id="insn-00a6df4c"></a> `00a6df4c` | `3f 01 0b eb` | cmp x9,x11 | `FALL_THROUGH`
<a id="insn-00a6df50"></a> `00a6df50` | `09 00 fe 92` | mov x9,#0xfffffffffffffff | `FALL_THROUGH`
<a id="insn-00a6df54"></a> `00a6df54` | `18 31 89 9a` | csel x24,x8,x9,cc | `FALL_THROUGH`
<a id="insn-00a6df58"></a> `00a6df58` | `f8 00 00 b4` | cbz x24,0x00a6df74 | `CONDITIONAL_JUMP`
<a id="insn-00a6df5c"></a> `00a6df5c` | `08 ff 7c d3` | lsr x8,x24,#0x3c | `FALL_THROUGH`
<a id="insn-00a6df60"></a> `00a6df60` | `a8 07 00 b5` | cbnz x8,0x00a6e054 | `CONDITIONAL_JUMP`
<a id="insn-00a6df64"></a> `00a6df64` | `00 ef 7c d3` | lsl x0,x24,#0x4 | `FALL_THROUGH`
<a id="insn-00a6df68"></a> `00a6df68` | `f6 b3 05 94` | bl 0x00bdaf40 | `UNCONDITIONAL_CALL`
<a id="insn-00a6df6c"></a> `00a6df6c` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00a6df70"></a> `00a6df70` | `02 00 00 14` | b 0x00a6df78 | `UNCONDITIONAL_JUMP`
<a id="insn-00a6df74"></a> `00a6df74` | `f5 03 1f aa` | mov x21,xzr | `FALL_THROUGH`
<a id="insn-00a6df78"></a> `00a6df78` | `c0 02 c0 3d` | ldr q0,[x22] | `FALL_THROUGH`
<a id="insn-00a6df7c"></a> `00a6df7c` | `b6 12 19 8b` | add x22,x21,x25, LSL #0x4 | `FALL_THROUGH`
<a id="insn-00a6df80"></a> `00a6df80` | `08 3c 18 4e` | mov x8,v0.D[0x1] | `FALL_THROUGH`
<a id="insn-00a6df84"></a> `00a6df84` | `c0 02 80 3d` | str q0,[x22] | `FALL_THROUGH`
<a id="insn-00a6df88"></a> `00a6df88` | `e8 00 00 b4` | cbz x8,0x00a6dfa4 | `CONDITIONAL_JUMP`
<a id="insn-00a6df8c"></a> `00a6df8c` | `01 21 00 91` | add x1,x8,#0x8 | `FALL_THROUGH`
<a id="insn-00a6df90"></a> `00a6df90` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00a6df94"></a> `00a6df94` | `73 a3 05 94` | bl 0x00bd6d60 | `UNCONDITIONAL_CALL`
<a id="insn-00a6df98"></a> `00a6df98` | `74 5e 40 a9` | ldp x20,x23,[x19] | `FALL_THROUGH`
<a id="insn-00a6df9c"></a> `00a6df9c` | `e8 02 14 cb` | sub x8,x23,x20 | `FALL_THROUGH`
<a id="insn-00a6dfa0"></a> `00a6dfa0` | `19 fd 44 93` | asr x25,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00a6dfa4"></a> `00a6dfa4` | `b8 12 18 8b` | add x24,x21,x24, LSL #0x4 | `FALL_THROUGH`
<a id="insn-00a6dfa8"></a> `00a6dfa8` | `d9 12 19 cb` | sub x25,x22,x25, LSL #0x4 | `FALL_THROUGH`
<a id="insn-00a6dfac"></a> `00a6dfac` | `9f 02 17 eb` | cmp x20,x23 | `FALL_THROUGH`
<a id="insn-00a6dfb0"></a> `00a6dfb0` | `d5 42 00 91` | add x21,x22,#0x10 | `FALL_THROUGH`
<a id="insn-00a6dfb4"></a> `00a6dfb4` | `40 03 00 54` | b.eq 0x00a6e01c | `CONDITIONAL_JUMP`
<a id="insn-00a6dfb8"></a> `00a6dfb8` | `e8 03 19 aa` | mov x8,x25 | `FALL_THROUGH`
<a id="insn-00a6dfbc"></a> `00a6dfbc` | `e9 03 14 aa` | mov x9,x20 | `FALL_THROUGH`
<a id="insn-00a6dfc0"></a> `00a6dfc0` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00a6dfc4"></a> `00a6dfc4` | `00 05 81 3c` | str q0,[x8], #0x10 | `FALL_THROUGH`
<a id="insn-00a6dfc8"></a> `00a6dfc8` | `3f 7d 81 a8` | stp xzr,xzr,[x9], #0x10 | `FALL_THROUGH`
<a id="insn-00a6dfcc"></a> `00a6dfcc` | `3f 01 17 eb` | cmp x9,x23 | `FALL_THROUGH`
<a id="insn-00a6dfd0"></a> `00a6dfd0` | `81 ff ff 54` | b.ne 0x00a6dfc0 | `CONDITIONAL_JUMP`
<a id="insn-00a6dfd4"></a> `00a6dfd4` | `04 00 00 14` | b 0x00a6dfe4 | `UNCONDITIONAL_JUMP`
<a id="insn-00a6dfd8"></a> `00a6dfd8` | `94 42 00 91` | add x20,x20,#0x10 | `FALL_THROUGH`
<a id="insn-00a6dfdc"></a> `00a6dfdc` | `9f 02 17 eb` | cmp x20,x23 | `FALL_THROUGH`
<a id="insn-00a6dfe0"></a> `00a6dfe0` | `c0 01 00 54` | b.eq 0x00a6e018 | `CONDITIONAL_JUMP`
<a id="insn-00a6dfe4"></a> `00a6dfe4` | `96 06 40 f9` | ldr x22,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00a6dfe8"></a> `00a6dfe8` | `96 ff ff b4` | cbz x22,0x00a6dfd8 | `CONDITIONAL_JUMP`
<a id="insn-00a6dfec"></a> `00a6dfec` | `c1 22 00 91` | add x1,x22,#0x8 | `FALL_THROUGH`
<a id="insn-00a6dff0"></a> `00a6dff0` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00a6dff4"></a> `00a6dff4` | `67 a3 05 94` | bl 0x00bd6d90 | `UNCONDITIONAL_CALL`
<a id="insn-00a6dff8"></a> `00a6dff8` | `00 ff ff b5` | cbnz x0,0x00a6dfd8 | `CONDITIONAL_JUMP`
<a id="insn-00a6dffc"></a> `00a6dffc` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00a6e000"></a> `00a6e000` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00a6e004"></a> `00a6e004` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00a6e008"></a> `00a6e008` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00a6e00c"></a> `00a6e00c` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00a6e010"></a> `00a6e010` | `c8 b3 05 94` | bl 0x00bdaf30 | `UNCONDITIONAL_CALL`
<a id="insn-00a6e014"></a> `00a6e014` | `f1 ff ff 17` | b 0x00a6dfd8 | `UNCONDITIONAL_JUMP`
<a id="insn-00a6e018"></a> `00a6e018` | `74 02 40 f9` | ldr x20,[x19] | `FALL_THROUGH`
<a id="insn-00a6e01c"></a> `00a6e01c` | `79 56 00 a9` | stp x25,x21,[x19] | `FALL_THROUGH`
<a id="insn-00a6e020"></a> `00a6e020` | `78 0a 00 f9` | str x24,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00a6e024"></a> `00a6e024` | `74 00 00 b4` | cbz x20,0x00a6e030 | `CONDITIONAL_JUMP`
<a id="insn-00a6e028"></a> `00a6e028` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00a6e02c"></a> `00a6e02c` | `cd b3 05 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00a6e030"></a> `00a6e030` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00a6e034"></a> `00a6e034` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00a6e038"></a> `00a6e038` | `f9 0b 40 f9` | ldr x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a6e03c"></a> `00a6e03c` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00a6e040"></a> `00a6e040` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00a6e044"></a> `00a6e044` | `fd 7b c5 a8` | ldp x29,x30,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00a6e048"></a> `00a6e048` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00a6e04c"></a> `00a6e04c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00a6e050"></a> `00a6e050` | `02 00 00 94` | bl 0x00a6e058 | `UNCONDITIONAL_CALL`
<a id="insn-00a6e054"></a> `00a6e054` | `cb c0 e6 97` | bl 0x0041e380 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00a6defc`](#insn-00a6defc) 範囲 `[['00a6defc', '00a6df2f']]`
  - `CONDITIONAL_JUMP` [`00a6df2c`](#insn-00a6df2c) → [`00a6e04c`](#insn-00a6e04c)
  - `FALL_THROUGH` [`00a6df2c`](#insn-00a6df2c) → [`00a6df30`](#insn-00a6df30)
- ブロック [`00a6df30`](#insn-00a6df30) 範囲 `[['00a6df30', '00a6df5b']]`
  - `CONDITIONAL_JUMP` [`00a6df58`](#insn-00a6df58) → [`00a6df74`](#insn-00a6df74)
  - `FALL_THROUGH` [`00a6df58`](#insn-00a6df58) → [`00a6df5c`](#insn-00a6df5c)
- ブロック [`00a6df5c`](#insn-00a6df5c) 範囲 `[['00a6df5c', '00a6df63']]`
  - `CONDITIONAL_JUMP` [`00a6df60`](#insn-00a6df60) → [`00a6e054`](#insn-00a6e054)
  - `FALL_THROUGH` [`00a6df60`](#insn-00a6df60) → [`00a6df64`](#insn-00a6df64)
- ブロック [`00a6df64`](#insn-00a6df64) 範囲 `[['00a6df64', '00a6df73']]`
  - `UNCONDITIONAL_JUMP` [`00a6df70`](#insn-00a6df70) → [`00a6df78`](#insn-00a6df78)
- ブロック [`00a6df74`](#insn-00a6df74) 範囲 `[['00a6df74', '00a6df77']]`
  - `FALL_THROUGH` [`00a6df74`](#insn-00a6df74) → [`00a6df78`](#insn-00a6df78)
- ブロック [`00a6df78`](#insn-00a6df78) 範囲 `[['00a6df78', '00a6df8b']]`
  - `CONDITIONAL_JUMP` [`00a6df88`](#insn-00a6df88) → [`00a6dfa4`](#insn-00a6dfa4)
  - `FALL_THROUGH` [`00a6df88`](#insn-00a6df88) → [`00a6df8c`](#insn-00a6df8c)
- ブロック [`00a6df8c`](#insn-00a6df8c) 範囲 `[['00a6df8c', '00a6dfa3']]`
  - `FALL_THROUGH` [`00a6dfa0`](#insn-00a6dfa0) → [`00a6dfa4`](#insn-00a6dfa4)
- ブロック [`00a6dfa4`](#insn-00a6dfa4) 範囲 `[['00a6dfa4', '00a6dfb7']]`
  - `CONDITIONAL_JUMP` [`00a6dfb4`](#insn-00a6dfb4) → [`00a6e01c`](#insn-00a6e01c)
  - `FALL_THROUGH` [`00a6dfb4`](#insn-00a6dfb4) → [`00a6dfb8`](#insn-00a6dfb8)
- ブロック [`00a6dfb8`](#insn-00a6dfb8) 範囲 `[['00a6dfb8', '00a6dfbf']]`
  - `FALL_THROUGH` [`00a6dfbc`](#insn-00a6dfbc) → [`00a6dfc0`](#insn-00a6dfc0)
- ブロック [`00a6dfc0`](#insn-00a6dfc0) 範囲 `[['00a6dfc0', '00a6dfd3']]`
  - `CONDITIONAL_JUMP` [`00a6dfd0`](#insn-00a6dfd0) → [`00a6dfc0`](#insn-00a6dfc0)
  - `FALL_THROUGH` [`00a6dfd0`](#insn-00a6dfd0) → [`00a6dfd4`](#insn-00a6dfd4)
- ブロック [`00a6dfd4`](#insn-00a6dfd4) 範囲 `[['00a6dfd4', '00a6dfd7']]`
  - `UNCONDITIONAL_JUMP` [`00a6dfd4`](#insn-00a6dfd4) → [`00a6dfe4`](#insn-00a6dfe4)
- ブロック [`00a6dfd8`](#insn-00a6dfd8) 範囲 `[['00a6dfd8', '00a6dfe3']]`
  - `CONDITIONAL_JUMP` [`00a6dfe0`](#insn-00a6dfe0) → [`00a6e018`](#insn-00a6e018)
  - `FALL_THROUGH` [`00a6dfe0`](#insn-00a6dfe0) → [`00a6dfe4`](#insn-00a6dfe4)
- ブロック [`00a6dfe4`](#insn-00a6dfe4) 範囲 `[['00a6dfe4', '00a6dfeb']]`
  - `CONDITIONAL_JUMP` [`00a6dfe8`](#insn-00a6dfe8) → [`00a6dfd8`](#insn-00a6dfd8)
  - `FALL_THROUGH` [`00a6dfe8`](#insn-00a6dfe8) → [`00a6dfec`](#insn-00a6dfec)
- ブロック [`00a6dfec`](#insn-00a6dfec) 範囲 `[['00a6dfec', '00a6dffb']]`
  - `CONDITIONAL_JUMP` [`00a6dff8`](#insn-00a6dff8) → [`00a6dfd8`](#insn-00a6dfd8)
  - `FALL_THROUGH` [`00a6dff8`](#insn-00a6dff8) → [`00a6dffc`](#insn-00a6dffc)
- ブロック [`00a6dffc`](#insn-00a6dffc) 範囲 `[['00a6dffc', '00a6e017']]`
  - `UNCONDITIONAL_JUMP` [`00a6e014`](#insn-00a6e014) → [`00a6dfd8`](#insn-00a6dfd8)
- ブロック [`00a6e018`](#insn-00a6e018) 範囲 `[['00a6e018', '00a6e01b']]`
  - `FALL_THROUGH` [`00a6e018`](#insn-00a6e018) → [`00a6e01c`](#insn-00a6e01c)
- ブロック [`00a6e01c`](#insn-00a6e01c) 範囲 `[['00a6e01c', '00a6e027']]`
  - `CONDITIONAL_JUMP` [`00a6e024`](#insn-00a6e024) → [`00a6e030`](#insn-00a6e030)
  - `FALL_THROUGH` [`00a6e024`](#insn-00a6e024) → [`00a6e028`](#insn-00a6e028)
- ブロック [`00a6e028`](#insn-00a6e028) 範囲 `[['00a6e028', '00a6e02f']]`
  - `FALL_THROUGH` [`00a6e02c`](#insn-00a6e02c) → [`00a6e030`](#insn-00a6e030)
- ブロック [`00a6e030`](#insn-00a6e030) 範囲 `[['00a6e030', '00a6e04b']]`
- ブロック [`00a6e04c`](#insn-00a6e04c) 範囲 `[['00a6e04c', '00a6e053']]`
  - `FALL_THROUGH` [`00a6e050`](#insn-00a6e050) → [`00a6e054`](#insn-00a6e054)
- ブロック [`00a6e054`](#insn-00a6e054) 範囲 `[['00a6e054', '00a6e057']]`

## 命令位置別の参照

- [`00a6defc`](#insn-00a6defc) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6df00`](#insn-00a6df00) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6df04`](#insn-00a6df04) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6df08`](#insn-00a6df08) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6df0c`](#insn-00a6df0c) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6df2c`](#insn-00a6df2c) → [`00a6e04c`](#insn-00a6e04c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6df58`](#insn-00a6df58) → [`00a6df74`](#insn-00a6df74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6df60`](#insn-00a6df60) → [`00a6e054`](#insn-00a6e054) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6df68`](#insn-00a6df68) → [`00bdaf40`](../00bda/00bdaf40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf40` · 推定シンボル `None` · 推定型 `None`
- [`00a6df70`](#insn-00a6df70) → [`00a6df78`](#insn-00a6df78) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6df88`](#insn-00a6df88) → [`00a6dfa4`](#insn-00a6dfa4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6df94`](#insn-00a6df94) → [`00bd6d60`](../00bd6/00bd6d60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd6d60` · 推定シンボル `None` · 推定型 `None`
- [`00a6dfb4`](#insn-00a6dfb4) → [`00a6e01c`](#insn-00a6e01c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6dfd0`](#insn-00a6dfd0) → [`00a6dfc0`](#insn-00a6dfc0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6dfd4`](#insn-00a6dfd4) → [`00a6dfe4`](#insn-00a6dfe4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6dfe0`](#insn-00a6dfe0) → [`00a6e018`](#insn-00a6e018) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6dfe8`](#insn-00a6dfe8) → [`00a6dfd8`](#insn-00a6dfd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6dff4`](#insn-00a6dff4) → [`00bd6d90`](../00bd6/00bd6d90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd6d90` · 推定シンボル `None` · 推定型 `None`
- [`00a6dff8`](#insn-00a6dff8) → [`00a6dfd8`](#insn-00a6dfd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6e010`](#insn-00a6e010) → [`00bdaf30`](../00bda/00bdaf30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf30` · 推定シンボル `None` · 推定型 `None`
- [`00a6e014`](#insn-00a6e014) → [`00a6dfd8`](#insn-00a6dfd8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6e024`](#insn-00a6e024) → [`00a6e030`](#insn-00a6e030) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6e02c`](#insn-00a6e02c) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00a6e034`](#insn-00a6e034) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6e038`](#insn-00a6e038) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6e03c`](#insn-00a6e03c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6e040`](#insn-00a6e040) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6e044`](#insn-00a6e044) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6e050`](#insn-00a6e050) → [`00a6e058`](../00a6e/00a6e058.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a6e058` · 推定シンボル `None` · 推定型 `None`
- [`00a6e054`](#insn-00a6e054) → [`0041e380`](../0041e/0041e380.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0041e380` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00a6defc`](#insn-00a6defc)

~~~json
{
  "source": "00a6defc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6df00`](#insn-00a6df00)

~~~json
{
  "source": "00a6df00",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6df04`](#insn-00a6df04)

~~~json
{
  "source": "00a6df04",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6df08`](#insn-00a6df08)

~~~json
{
  "source": "00a6df08",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6df0c`](#insn-00a6df0c)

~~~json
{
  "source": "00a6df0c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6df2c`](#insn-00a6df2c)

~~~json
{
  "source": "00a6df2c",
  "target": "00a6e04c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6df58`](#insn-00a6df58)

~~~json
{
  "source": "00a6df58",
  "target": "00a6df74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6df60`](#insn-00a6df60)

~~~json
{
  "source": "00a6df60",
  "target": "00a6e054",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6df68`](#insn-00a6df68)

~~~json
{
  "source": "00a6df68",
  "target": "00bdaf40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6df70`](#insn-00a6df70)

~~~json
{
  "source": "00a6df70",
  "target": "00a6df78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6df88`](#insn-00a6df88)

~~~json
{
  "source": "00a6df88",
  "target": "00a6dfa4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6df94`](#insn-00a6df94)

~~~json
{
  "source": "00a6df94",
  "target": "00bd6d60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6dfb4`](#insn-00a6dfb4)

~~~json
{
  "source": "00a6dfb4",
  "target": "00a6e01c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6dfd0`](#insn-00a6dfd0)

~~~json
{
  "source": "00a6dfd0",
  "target": "00a6dfc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6dfd4`](#insn-00a6dfd4)

~~~json
{
  "source": "00a6dfd4",
  "target": "00a6dfe4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6dfe0`](#insn-00a6dfe0)

~~~json
{
  "source": "00a6dfe0",
  "target": "00a6e018",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6dfe8`](#insn-00a6dfe8)

~~~json
{
  "source": "00a6dfe8",
  "target": "00a6dfd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6dff4`](#insn-00a6dff4)

~~~json
{
  "source": "00a6dff4",
  "target": "00bd6d90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6dff8`](#insn-00a6dff8)

~~~json
{
  "source": "00a6dff8",
  "target": "00a6dfd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6e010`](#insn-00a6e010)

~~~json
{
  "source": "00a6e010",
  "target": "00bdaf30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6e014`](#insn-00a6e014)

~~~json
{
  "source": "00a6e014",
  "target": "00a6dfd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6e024`](#insn-00a6e024)

~~~json
{
  "source": "00a6e024",
  "target": "00a6e030",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6e02c`](#insn-00a6e02c)

~~~json
{
  "source": "00a6e02c",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6e034`](#insn-00a6e034)

~~~json
{
  "source": "00a6e034",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6e038`](#insn-00a6e038)

~~~json
{
  "source": "00a6e038",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6e03c`](#insn-00a6e03c)

~~~json
{
  "source": "00a6e03c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6e040`](#insn-00a6e040)

~~~json
{
  "source": "00a6e040",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6e044`](#insn-00a6e044)

~~~json
{
  "source": "00a6e044",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6e050`](#insn-00a6e050)

~~~json
{
  "source": "00a6e050",
  "target": "00a6e058",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6e054`](#insn-00a6e054)

~~~json
{
  "source": "00a6e054",
  "target": "0041e380",
  "target_space": "ram",
  "resolution": "function"
}
~~~
