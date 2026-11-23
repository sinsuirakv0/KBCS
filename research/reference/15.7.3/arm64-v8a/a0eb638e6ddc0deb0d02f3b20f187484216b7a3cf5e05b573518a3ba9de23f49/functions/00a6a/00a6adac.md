# 00a6adac

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00a6adac`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a6a/00a6adac.md) · 移動量 `+0x0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/no_difference_in_scope-0019.md#compare-afd826624b9c23e42217133c5c8ac925)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00a6adf0`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6a/00a6adf0.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/alignment_unresolved-0002.md#compare-280196b692cb20a204fbfb50c7bc192a)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00a6adac",
  "name": "FUN_00a6adac",
  "size": 316,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ab53e3631c6f62ab3eb46d0a8c5da5df417734eed1149703094c7e5fd2e98f4c",
  "source_text_sha256": "ab53e3631c6f62ab3eb46d0a8c5da5df417734eed1149703094c7e5fd2e98f4c",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00a6adac",
        "00a6aee7"
      ]
    ],
    "bytes_sha256": "cace17892af68ed40b02557ded15a245e14b0e036aa8e6f4216bca261068f9b6",
    "instruction_count": 79,
    "instruction_bytes": 316,
    "body_bytes": 316,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00a6ac88](../00a6a/00a6ac88.md)
- [00a6af0c](../00a6a/00a6af0c.md)

## 呼び出し先

- [0081f580](../0081f/0081f580.md)
- [00827b94](../00827/00827b94.md)
- [008292fc](../00829/008292fc.md)
- [00829304](../00829/00829304.md)
- [0082931c](../00829/0082931c.md)
- [00829328](../00829/00829328.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1821 bytes

~~~c

undefined8 FUN_00a6adac(long param_1)

{
  int iVar1;
  ulong uVar2;
  long lVar3;
  float fVar4;
  
  FUN_0081f580();
  uVar2 = FUN_00827b94();
  if ((uVar2 & 1) == 0) {
    FUN_0081f580();
    uVar2 = FUN_0082931c();
    if ((uVar2 & 1) == 0) {
      FUN_0081f580();
      uVar2 = FUN_00829328();
                    /* try { // try from 00a6addc to 00b6ae0b has its CatchHandler @ 00a6b6a4 */
      if (((uVar2 & 1) == 0) && (lVar3 = FUN_0081f580(), *(char *)(lVar3 + 0x347d) == '\0')) {
        return 0;
      }
    }
  }
  if (*(int *)(param_1 + 0x284) == 1) {
    FUN_0081f580();
    iVar1 = FUN_008292fc();
    if ((float)iVar1 < *(float *)(param_1 + 0x1e4)) {
      return 0;
    }
    FUN_0081f580();
    iVar1 = FUN_008292fc();
    if (*(float *)(param_1 + 0x1e4) + *(float *)(param_1 + 0x1ec) < (float)iVar1) {
      return 0;
    }
    FUN_0081f580();
    iVar1 = FUN_00829304();
    if ((float)iVar1 < *(float *)(param_1 + 0x1e8)) {
      return 0;
    }
    FUN_0081f580();
    iVar1 = FUN_00829304();
    fVar4 = *(float *)(param_1 + 0x1e8);
  }
  else {
    if (*(int *)(param_1 + 0x284) != 0) {
      return 0;
    }
    FUN_0081f580();
    iVar1 = FUN_00829304();
    if ((float)iVar1 < *(float *)(param_1 + 0x1e8)) {
      return 0;
    }
    FUN_0081f580();
    iVar1 = FUN_00829304();
    if (*(float *)(param_1 + 0x1e8) + *(float *)(param_1 + 0x1ec) < (float)iVar1) {
      return 0;
    }
    FUN_0081f580();
    iVar1 = FUN_008292fc();
                    /* try { // try from 00a6ae40 to 00b6b077 has its CatchHandler @ 00a6b6c0 */
    if ((float)iVar1 < *(float *)(param_1 + 0x1e4)) {
      return 0;
    }
    FUN_0081f580();
    iVar1 = FUN_008292fc();
    fVar4 = *(float *)(param_1 + 0x1e4);
  }
  if (fVar4 + *(float *)(param_1 + 0x1d8) < (float)iVar1) {
    return 0;
  }
  return 1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00a6adac"></a> `00a6adac` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00a6adb0"></a> `00a6adb0` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a6adb4"></a> `00a6adb4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00a6adb8"></a> `00a6adb8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00a6adbc"></a> `00a6adbc` | `f1 d1 f6 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00a6adc0"></a> `00a6adc0` | `75 f3 f6 97` | bl 0x00827b94 | `UNCONDITIONAL_CALL`
<a id="insn-00a6adc4"></a> `00a6adc4` | `60 01 00 37` | tbnz w0,#0x0,0x00a6adf0 | `CONDITIONAL_JUMP`
<a id="insn-00a6adc8"></a> `00a6adc8` | `ee d1 f6 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00a6adcc"></a> `00a6adcc` | `54 f9 f6 97` | bl 0x0082931c | `UNCONDITIONAL_CALL`
<a id="insn-00a6add0"></a> `00a6add0` | `00 01 00 37` | tbnz w0,#0x0,0x00a6adf0 | `CONDITIONAL_JUMP`
<a id="insn-00a6add4"></a> `00a6add4` | `eb d1 f6 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00a6add8"></a> `00a6add8` | `54 f9 f6 97` | bl 0x00829328 | `UNCONDITIONAL_CALL`
<a id="insn-00a6addc"></a> `00a6addc` | `a0 00 00 37` | tbnz w0,#0x0,0x00a6adf0 | `CONDITIONAL_JUMP`
<a id="insn-00a6ade0"></a> `00a6ade0` | `e8 d1 f6 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00a6ade4"></a> `00a6ade4` | `a8 8f 86 52` | mov w8,#0x347d | `FALL_THROUGH`
<a id="insn-00a6ade8"></a> `00a6ade8` | `08 68 68 38` | ldrb w8,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00a6adec"></a> `00a6adec` | `28 07 00 34` | cbz w8,0x00a6aed0 | `CONDITIONAL_JUMP`
<a id="insn-00a6adf0"></a> `00a6adf0` | `68 86 42 b9` | ldr w8,[x19, #0x284] | `FALL_THROUGH`
<a id="insn-00a6adf4"></a> `00a6adf4` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00a6adf8"></a> `00a6adf8` | `40 03 00 54` | b.eq 0x00a6ae60 | `CONDITIONAL_JUMP`
<a id="insn-00a6adfc"></a> `00a6adfc` | `a8 06 00 35` | cbnz w8,0x00a6aed0 | `CONDITIONAL_JUMP`
<a id="insn-00a6ae00"></a> `00a6ae00` | `e0 d1 f6 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00a6ae04"></a> `00a6ae04` | `40 f9 f6 97` | bl 0x00829304 | `UNCONDITIONAL_CALL`
<a id="insn-00a6ae08"></a> `00a6ae08` | `00 00 22 1e` | scvtf s0,w0 | `FALL_THROUGH`
<a id="insn-00a6ae0c"></a> `00a6ae0c` | `61 ea 41 bd` | ldr s1,[x19, #0x1e8] | `FALL_THROUGH`
<a id="insn-00a6ae10"></a> `00a6ae10` | `20 20 20 1e` | fcmp s1,s0 | `FALL_THROUGH`
<a id="insn-00a6ae14"></a> `00a6ae14` | `e8 05 00 54` | b.hi 0x00a6aed0 | `CONDITIONAL_JUMP`
<a id="insn-00a6ae18"></a> `00a6ae18` | `da d1 f6 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00a6ae1c"></a> `00a6ae1c` | `3a f9 f6 97` | bl 0x00829304 | `UNCONDITIONAL_CALL`
<a id="insn-00a6ae20"></a> `00a6ae20` | `60 ea 41 bd` | ldr s0,[x19, #0x1e8] | `FALL_THROUGH`
<a id="insn-00a6ae24"></a> `00a6ae24` | `61 ee 41 bd` | ldr s1,[x19, #0x1ec] | `FALL_THROUGH`
<a id="insn-00a6ae28"></a> `00a6ae28` | `02 00 22 1e` | scvtf s2,w0 | `FALL_THROUGH`
<a id="insn-00a6ae2c"></a> `00a6ae2c` | `00 28 21 1e` | fadd s0,s0,s1 | `FALL_THROUGH`
<a id="insn-00a6ae30"></a> `00a6ae30` | `00 20 22 1e` | fcmp s0,s2 | `FALL_THROUGH`
<a id="insn-00a6ae34"></a> `00a6ae34` | `eb 04 00 54` | b.lt 0x00a6aed0 | `CONDITIONAL_JUMP`
<a id="insn-00a6ae38"></a> `00a6ae38` | `d2 d1 f6 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00a6ae3c"></a> `00a6ae3c` | `30 f9 f6 97` | bl 0x008292fc | `UNCONDITIONAL_CALL`
<a id="insn-00a6ae40"></a> `00a6ae40` | `00 00 22 1e` | scvtf s0,w0 | `FALL_THROUGH`
<a id="insn-00a6ae44"></a> `00a6ae44` | `61 e6 41 bd` | ldr s1,[x19, #0x1e4] | `FALL_THROUGH`
<a id="insn-00a6ae48"></a> `00a6ae48` | `20 20 20 1e` | fcmp s1,s0 | `FALL_THROUGH`
<a id="insn-00a6ae4c"></a> `00a6ae4c` | `28 04 00 54` | b.hi 0x00a6aed0 | `CONDITIONAL_JUMP`
<a id="insn-00a6ae50"></a> `00a6ae50` | `cc d1 f6 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00a6ae54"></a> `00a6ae54` | `2a f9 f6 97` | bl 0x008292fc | `UNCONDITIONAL_CALL`
<a id="insn-00a6ae58"></a> `00a6ae58` | `60 e6 41 bd` | ldr s0,[x19, #0x1e4] | `FALL_THROUGH`
<a id="insn-00a6ae5c"></a> `00a6ae5c` | `18 00 00 14` | b 0x00a6aebc | `UNCONDITIONAL_JUMP`
<a id="insn-00a6ae60"></a> `00a6ae60` | `c8 d1 f6 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00a6ae64"></a> `00a6ae64` | `26 f9 f6 97` | bl 0x008292fc | `UNCONDITIONAL_CALL`
<a id="insn-00a6ae68"></a> `00a6ae68` | `00 00 22 1e` | scvtf s0,w0 | `FALL_THROUGH`
<a id="insn-00a6ae6c"></a> `00a6ae6c` | `61 e6 41 bd` | ldr s1,[x19, #0x1e4] | `FALL_THROUGH`
<a id="insn-00a6ae70"></a> `00a6ae70` | `20 20 20 1e` | fcmp s1,s0 | `FALL_THROUGH`
<a id="insn-00a6ae74"></a> `00a6ae74` | `e8 02 00 54` | b.hi 0x00a6aed0 | `CONDITIONAL_JUMP`
<a id="insn-00a6ae78"></a> `00a6ae78` | `c2 d1 f6 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00a6ae7c"></a> `00a6ae7c` | `20 f9 f6 97` | bl 0x008292fc | `UNCONDITIONAL_CALL`
<a id="insn-00a6ae80"></a> `00a6ae80` | `60 e6 41 bd` | ldr s0,[x19, #0x1e4] | `FALL_THROUGH`
<a id="insn-00a6ae84"></a> `00a6ae84` | `61 ee 41 bd` | ldr s1,[x19, #0x1ec] | `FALL_THROUGH`
<a id="insn-00a6ae88"></a> `00a6ae88` | `02 00 22 1e` | scvtf s2,w0 | `FALL_THROUGH`
<a id="insn-00a6ae8c"></a> `00a6ae8c` | `00 28 21 1e` | fadd s0,s0,s1 | `FALL_THROUGH`
<a id="insn-00a6ae90"></a> `00a6ae90` | `00 20 22 1e` | fcmp s0,s2 | `FALL_THROUGH`
<a id="insn-00a6ae94"></a> `00a6ae94` | `eb 01 00 54` | b.lt 0x00a6aed0 | `CONDITIONAL_JUMP`
<a id="insn-00a6ae98"></a> `00a6ae98` | `ba d1 f6 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00a6ae9c"></a> `00a6ae9c` | `1a f9 f6 97` | bl 0x00829304 | `UNCONDITIONAL_CALL`
<a id="insn-00a6aea0"></a> `00a6aea0` | `00 00 22 1e` | scvtf s0,w0 | `FALL_THROUGH`
<a id="insn-00a6aea4"></a> `00a6aea4` | `61 ea 41 bd` | ldr s1,[x19, #0x1e8] | `FALL_THROUGH`
<a id="insn-00a6aea8"></a> `00a6aea8` | `20 20 20 1e` | fcmp s1,s0 | `FALL_THROUGH`
<a id="insn-00a6aeac"></a> `00a6aeac` | `28 01 00 54` | b.hi 0x00a6aed0 | `CONDITIONAL_JUMP`
<a id="insn-00a6aeb0"></a> `00a6aeb0` | `b4 d1 f6 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00a6aeb4"></a> `00a6aeb4` | `14 f9 f6 97` | bl 0x00829304 | `UNCONDITIONAL_CALL`
<a id="insn-00a6aeb8"></a> `00a6aeb8` | `60 ea 41 bd` | ldr s0,[x19, #0x1e8] | `FALL_THROUGH`
<a id="insn-00a6aebc"></a> `00a6aebc` | `61 da 41 bd` | ldr s1,[x19, #0x1d8] | `FALL_THROUGH`
<a id="insn-00a6aec0"></a> `00a6aec0` | `02 00 22 1e` | scvtf s2,w0 | `FALL_THROUGH`
<a id="insn-00a6aec4"></a> `00a6aec4` | `00 28 21 1e` | fadd s0,s0,s1 | `FALL_THROUGH`
<a id="insn-00a6aec8"></a> `00a6aec8` | `00 20 22 1e` | fcmp s0,s2 | `FALL_THROUGH`
<a id="insn-00a6aecc"></a> `00a6aecc` | `aa 00 00 54` | b.ge 0x00a6aee0 | `CONDITIONAL_JUMP`
<a id="insn-00a6aed0"></a> `00a6aed0` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00a6aed4"></a> `00a6aed4` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a6aed8"></a> `00a6aed8` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00a6aedc"></a> `00a6aedc` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00a6aee0"></a> `00a6aee0` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00a6aee4"></a> `00a6aee4` | `fc ff ff 17` | b 0x00a6aed4 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00a6adac`](#insn-00a6adac) 範囲 `[['00a6adac', '00a6adc7']]`
  - `CONDITIONAL_JUMP` [`00a6adc4`](#insn-00a6adc4) → [`00a6adf0`](#insn-00a6adf0)
  - `FALL_THROUGH` [`00a6adc4`](#insn-00a6adc4) → [`00a6adc8`](#insn-00a6adc8)
- ブロック [`00a6adc8`](#insn-00a6adc8) 範囲 `[['00a6adc8', '00a6add3']]`
  - `CONDITIONAL_JUMP` [`00a6add0`](#insn-00a6add0) → [`00a6adf0`](#insn-00a6adf0)
  - `FALL_THROUGH` [`00a6add0`](#insn-00a6add0) → [`00a6add4`](#insn-00a6add4)
- ブロック [`00a6add4`](#insn-00a6add4) 範囲 `[['00a6add4', '00a6addb']]`
  - `FALL_THROUGH` [`00a6add8`](#insn-00a6add8) → [`00a6addc`](#insn-00a6addc)
- ブロック [`00a6addc`](#insn-00a6addc) 範囲 `[['00a6addc', '00a6addf']]`
  - `CONDITIONAL_JUMP` [`00a6addc`](#insn-00a6addc) → [`00a6adf0`](#insn-00a6adf0)
  - `FALL_THROUGH` [`00a6addc`](#insn-00a6addc) → [`00a6ade0`](#insn-00a6ade0)
- ブロック [`00a6ade0`](#insn-00a6ade0) 範囲 `[['00a6ade0', '00a6adef']]`
  - `CONDITIONAL_JUMP` [`00a6adec`](#insn-00a6adec) → [`00a6aed0`](#insn-00a6aed0)
  - `FALL_THROUGH` [`00a6adec`](#insn-00a6adec) → [`00a6adf0`](#insn-00a6adf0)
- ブロック [`00a6adf0`](#insn-00a6adf0) 範囲 `[['00a6adf0', '00a6adfb']]`
  - `CONDITIONAL_JUMP` [`00a6adf8`](#insn-00a6adf8) → [`00a6ae60`](#insn-00a6ae60)
  - `FALL_THROUGH` [`00a6adf8`](#insn-00a6adf8) → [`00a6adfc`](#insn-00a6adfc)
- ブロック [`00a6adfc`](#insn-00a6adfc) 範囲 `[['00a6adfc', '00a6adff']]`
  - `CONDITIONAL_JUMP` [`00a6adfc`](#insn-00a6adfc) → [`00a6aed0`](#insn-00a6aed0)
  - `FALL_THROUGH` [`00a6adfc`](#insn-00a6adfc) → [`00a6ae00`](#insn-00a6ae00)
- ブロック [`00a6ae00`](#insn-00a6ae00) 範囲 `[['00a6ae00', '00a6ae17']]`
  - `CONDITIONAL_JUMP` [`00a6ae14`](#insn-00a6ae14) → [`00a6aed0`](#insn-00a6aed0)
  - `FALL_THROUGH` [`00a6ae14`](#insn-00a6ae14) → [`00a6ae18`](#insn-00a6ae18)
- ブロック [`00a6ae18`](#insn-00a6ae18) 範囲 `[['00a6ae18', '00a6ae37']]`
  - `CONDITIONAL_JUMP` [`00a6ae34`](#insn-00a6ae34) → [`00a6aed0`](#insn-00a6aed0)
  - `FALL_THROUGH` [`00a6ae34`](#insn-00a6ae34) → [`00a6ae38`](#insn-00a6ae38)
- ブロック [`00a6ae38`](#insn-00a6ae38) 範囲 `[['00a6ae38', '00a6ae3f']]`
  - `FALL_THROUGH` [`00a6ae3c`](#insn-00a6ae3c) → [`00a6ae40`](#insn-00a6ae40)
- ブロック [`00a6ae40`](#insn-00a6ae40) 範囲 `[['00a6ae40', '00a6ae4f']]`
  - `CONDITIONAL_JUMP` [`00a6ae4c`](#insn-00a6ae4c) → [`00a6aed0`](#insn-00a6aed0)
  - `FALL_THROUGH` [`00a6ae4c`](#insn-00a6ae4c) → [`00a6ae50`](#insn-00a6ae50)
- ブロック [`00a6ae50`](#insn-00a6ae50) 範囲 `[['00a6ae50', '00a6ae5f']]`
  - `UNCONDITIONAL_JUMP` [`00a6ae5c`](#insn-00a6ae5c) → [`00a6aebc`](#insn-00a6aebc)
- ブロック [`00a6ae60`](#insn-00a6ae60) 範囲 `[['00a6ae60', '00a6ae77']]`
  - `CONDITIONAL_JUMP` [`00a6ae74`](#insn-00a6ae74) → [`00a6aed0`](#insn-00a6aed0)
  - `FALL_THROUGH` [`00a6ae74`](#insn-00a6ae74) → [`00a6ae78`](#insn-00a6ae78)
- ブロック [`00a6ae78`](#insn-00a6ae78) 範囲 `[['00a6ae78', '00a6ae97']]`
  - `CONDITIONAL_JUMP` [`00a6ae94`](#insn-00a6ae94) → [`00a6aed0`](#insn-00a6aed0)
  - `FALL_THROUGH` [`00a6ae94`](#insn-00a6ae94) → [`00a6ae98`](#insn-00a6ae98)
- ブロック [`00a6ae98`](#insn-00a6ae98) 範囲 `[['00a6ae98', '00a6aeaf']]`
  - `CONDITIONAL_JUMP` [`00a6aeac`](#insn-00a6aeac) → [`00a6aed0`](#insn-00a6aed0)
  - `FALL_THROUGH` [`00a6aeac`](#insn-00a6aeac) → [`00a6aeb0`](#insn-00a6aeb0)
- ブロック [`00a6aeb0`](#insn-00a6aeb0) 範囲 `[['00a6aeb0', '00a6aebb']]`
  - `FALL_THROUGH` [`00a6aeb8`](#insn-00a6aeb8) → [`00a6aebc`](#insn-00a6aebc)
- ブロック [`00a6aebc`](#insn-00a6aebc) 範囲 `[['00a6aebc', '00a6aecf']]`
  - `CONDITIONAL_JUMP` [`00a6aecc`](#insn-00a6aecc) → [`00a6aee0`](#insn-00a6aee0)
  - `FALL_THROUGH` [`00a6aecc`](#insn-00a6aecc) → [`00a6aed0`](#insn-00a6aed0)
- ブロック [`00a6aed0`](#insn-00a6aed0) 範囲 `[['00a6aed0', '00a6aed3']]`
  - `FALL_THROUGH` [`00a6aed0`](#insn-00a6aed0) → [`00a6aed4`](#insn-00a6aed4)
- ブロック [`00a6aed4`](#insn-00a6aed4) 範囲 `[['00a6aed4', '00a6aedf']]`
- ブロック [`00a6aee0`](#insn-00a6aee0) 範囲 `[['00a6aee0', '00a6aee7']]`
  - `UNCONDITIONAL_JUMP` [`00a6aee4`](#insn-00a6aee4) → [`00a6aed4`](#insn-00a6aed4)

## 命令位置別の参照

- [`00a6adac`](#insn-00a6adac) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6adb0`](#insn-00a6adb0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6adbc`](#insn-00a6adbc) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00a6adc0`](#insn-00a6adc0) → [`00827b94`](../00827/00827b94.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00827b94` · 推定シンボル `None` · 推定型 `None`
- [`00a6adc4`](#insn-00a6adc4) → [`00a6adf0`](#insn-00a6adf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6adc8`](#insn-00a6adc8) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00a6adcc`](#insn-00a6adcc) → [`0082931c`](../00829/0082931c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0082931c` · 推定シンボル `None` · 推定型 `None`
- [`00a6add0`](#insn-00a6add0) → [`00a6adf0`](#insn-00a6adf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6add4`](#insn-00a6add4) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00a6add8`](#insn-00a6add8) → [`00829328`](../00829/00829328.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00829328` · 推定シンボル `None` · 推定型 `None`
- [`00a6addc`](#insn-00a6addc) → [`00a6adf0`](#insn-00a6adf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ade0`](#insn-00a6ade0) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00a6adec`](#insn-00a6adec) → [`00a6aed0`](#insn-00a6aed0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6adf8`](#insn-00a6adf8) → [`00a6ae60`](#insn-00a6ae60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6adfc`](#insn-00a6adfc) → [`00a6aed0`](#insn-00a6aed0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ae00`](#insn-00a6ae00) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00a6ae04`](#insn-00a6ae04) → [`00829304`](../00829/00829304.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00829304` · 推定シンボル `None` · 推定型 `None`
- [`00a6ae14`](#insn-00a6ae14) → [`00a6aed0`](#insn-00a6aed0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ae18`](#insn-00a6ae18) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00a6ae1c`](#insn-00a6ae1c) → [`00829304`](../00829/00829304.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00829304` · 推定シンボル `None` · 推定型 `None`
- [`00a6ae34`](#insn-00a6ae34) → [`00a6aed0`](#insn-00a6aed0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ae38`](#insn-00a6ae38) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00a6ae3c`](#insn-00a6ae3c) → [`008292fc`](../00829/008292fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008292fc` · 推定シンボル `None` · 推定型 `None`
- [`00a6ae4c`](#insn-00a6ae4c) → [`00a6aed0`](#insn-00a6aed0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ae50`](#insn-00a6ae50) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00a6ae54`](#insn-00a6ae54) → [`008292fc`](../00829/008292fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008292fc` · 推定シンボル `None` · 推定型 `None`
- [`00a6ae5c`](#insn-00a6ae5c) → [`00a6aebc`](#insn-00a6aebc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ae60`](#insn-00a6ae60) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00a6ae64`](#insn-00a6ae64) → [`008292fc`](../00829/008292fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008292fc` · 推定シンボル `None` · 推定型 `None`
- [`00a6ae74`](#insn-00a6ae74) → [`00a6aed0`](#insn-00a6aed0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ae78`](#insn-00a6ae78) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00a6ae7c`](#insn-00a6ae7c) → [`008292fc`](../00829/008292fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008292fc` · 推定シンボル `None` · 推定型 `None`
- [`00a6ae94`](#insn-00a6ae94) → [`00a6aed0`](#insn-00a6aed0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ae98`](#insn-00a6ae98) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00a6ae9c`](#insn-00a6ae9c) → [`00829304`](../00829/00829304.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00829304` · 推定シンボル `None` · 推定型 `None`
- [`00a6aeac`](#insn-00a6aeac) → [`00a6aed0`](#insn-00a6aed0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6aeb0`](#insn-00a6aeb0) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00a6aeb4`](#insn-00a6aeb4) → [`00829304`](../00829/00829304.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00829304` · 推定シンボル `None` · 推定型 `None`
- [`00a6aecc`](#insn-00a6aecc) → [`00a6aee0`](#insn-00a6aee0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6aed4`](#insn-00a6aed4) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6aed8`](#insn-00a6aed8) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6aee4`](#insn-00a6aee4) → [`00a6aed4`](#insn-00a6aed4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00a6adac`](#insn-00a6adac)

~~~json
{
  "source": "00a6adac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6adb0`](#insn-00a6adb0)

~~~json
{
  "source": "00a6adb0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6adbc`](#insn-00a6adbc)

~~~json
{
  "source": "00a6adbc",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6adc0`](#insn-00a6adc0)

~~~json
{
  "source": "00a6adc0",
  "target": "00827b94",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6adc4`](#insn-00a6adc4)

~~~json
{
  "source": "00a6adc4",
  "target": "00a6adf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6adc8`](#insn-00a6adc8)

~~~json
{
  "source": "00a6adc8",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6adcc`](#insn-00a6adcc)

~~~json
{
  "source": "00a6adcc",
  "target": "0082931c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6add0`](#insn-00a6add0)

~~~json
{
  "source": "00a6add0",
  "target": "00a6adf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6add4`](#insn-00a6add4)

~~~json
{
  "source": "00a6add4",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6add8`](#insn-00a6add8)

~~~json
{
  "source": "00a6add8",
  "target": "00829328",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6addc`](#insn-00a6addc)

~~~json
{
  "source": "00a6addc",
  "target": "00a6adf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ade0`](#insn-00a6ade0)

~~~json
{
  "source": "00a6ade0",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6adec`](#insn-00a6adec)

~~~json
{
  "source": "00a6adec",
  "target": "00a6aed0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6adf8`](#insn-00a6adf8)

~~~json
{
  "source": "00a6adf8",
  "target": "00a6ae60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6adfc`](#insn-00a6adfc)

~~~json
{
  "source": "00a6adfc",
  "target": "00a6aed0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ae00`](#insn-00a6ae00)

~~~json
{
  "source": "00a6ae00",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6ae04`](#insn-00a6ae04)

~~~json
{
  "source": "00a6ae04",
  "target": "00829304",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6ae14`](#insn-00a6ae14)

~~~json
{
  "source": "00a6ae14",
  "target": "00a6aed0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ae18`](#insn-00a6ae18)

~~~json
{
  "source": "00a6ae18",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6ae1c`](#insn-00a6ae1c)

~~~json
{
  "source": "00a6ae1c",
  "target": "00829304",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6ae34`](#insn-00a6ae34)

~~~json
{
  "source": "00a6ae34",
  "target": "00a6aed0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ae38`](#insn-00a6ae38)

~~~json
{
  "source": "00a6ae38",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6ae3c`](#insn-00a6ae3c)

~~~json
{
  "source": "00a6ae3c",
  "target": "008292fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6ae4c`](#insn-00a6ae4c)

~~~json
{
  "source": "00a6ae4c",
  "target": "00a6aed0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ae50`](#insn-00a6ae50)

~~~json
{
  "source": "00a6ae50",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6ae54`](#insn-00a6ae54)

~~~json
{
  "source": "00a6ae54",
  "target": "008292fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6ae5c`](#insn-00a6ae5c)

~~~json
{
  "source": "00a6ae5c",
  "target": "00a6aebc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ae60`](#insn-00a6ae60)

~~~json
{
  "source": "00a6ae60",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6ae64`](#insn-00a6ae64)

~~~json
{
  "source": "00a6ae64",
  "target": "008292fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6ae74`](#insn-00a6ae74)

~~~json
{
  "source": "00a6ae74",
  "target": "00a6aed0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ae78`](#insn-00a6ae78)

~~~json
{
  "source": "00a6ae78",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6ae7c`](#insn-00a6ae7c)

~~~json
{
  "source": "00a6ae7c",
  "target": "008292fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6ae94`](#insn-00a6ae94)

~~~json
{
  "source": "00a6ae94",
  "target": "00a6aed0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ae98`](#insn-00a6ae98)

~~~json
{
  "source": "00a6ae98",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6ae9c`](#insn-00a6ae9c)

~~~json
{
  "source": "00a6ae9c",
  "target": "00829304",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6aeac`](#insn-00a6aeac)

~~~json
{
  "source": "00a6aeac",
  "target": "00a6aed0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6aeb0`](#insn-00a6aeb0)

~~~json
{
  "source": "00a6aeb0",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6aeb4`](#insn-00a6aeb4)

~~~json
{
  "source": "00a6aeb4",
  "target": "00829304",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6aecc`](#insn-00a6aecc)

~~~json
{
  "source": "00a6aecc",
  "target": "00a6aee0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6aed4`](#insn-00a6aed4)

~~~json
{
  "source": "00a6aed4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6aed8`](#insn-00a6aed8)

~~~json
{
  "source": "00a6aed8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6aee4`](#insn-00a6aee4)

~~~json
{
  "source": "00a6aee4",
  "target": "00a6aed4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
