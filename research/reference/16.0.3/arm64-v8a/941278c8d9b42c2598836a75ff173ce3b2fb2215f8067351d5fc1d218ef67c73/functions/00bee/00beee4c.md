# 00beee4c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 要確認
  - [v16.0.2 → v16.0.3 候補と検査根拠](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/review-0083.md#review-5214a46c8896ff5eb5f567b11b84ef16)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00beee4c",
  "name": "FUN_00beee4c",
  "size": 296,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9e9ef1dff563ca7edf5e4e7825493857b5bb548a3f8dd8fd5d973de2a20d2da2",
  "source_text_sha256": "9e9ef1dff563ca7edf5e4e7825493857b5bb548a3f8dd8fd5d973de2a20d2da2",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00beee4c",
        "00beef73"
      ]
    ],
    "bytes_sha256": "f8f1254738e345e86b10579253658224786fe5f1e21a43e34379cd1a22852dc9",
    "instruction_count": 74,
    "instruction_bytes": 296,
    "body_bytes": 296,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00be81a0](../00be8/00be81a0.md)
- [00beebac](../00bee/00beebac.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2090 bytes

~~~c

void FUN_00beee4c(ulong *param_1,ulong *param_2,ulong *param_3,ulong *param_4,ulong *param_5)

{
  ulong uVar1;
  ulong uVar2;
  ulong uVar3;
  
  uVar1 = *param_2;
  uVar2 = *param_1;
  uVar3 = *param_3;
  if (uVar1 < uVar2) {
    if (uVar3 < uVar1) {
      *param_1 = uVar3;
                    /* try { // try from 00beee70 to 00ceefcb has its CatchHandler @ 00beee70
                       catch() { ... } // from try @ 00beee70 with catch @ 00beee70
                       catch() { ... } // from try @ 00bef018 with catch @ 00beee70
                       catch() { ... } // from try @ 00bef0f4 with catch @ 00beee70
                       catch() { ... } // from try @ 00bef1c0 with catch @ 00beee70
                       catch() { ... } // from try @ 00bef2e8 with catch @ 00beee70
                       catch() { ... } // from try @ 00bef54c with catch @ 00beee70 */
    }
    else {
      *param_1 = uVar1;
      *param_2 = uVar2;
      uVar3 = *param_3;
      if (uVar2 <= uVar3) goto LAB_00beeecc;
      *param_2 = uVar3;
    }
    *param_3 = uVar2;
    uVar3 = uVar2;
  }
  else if (uVar3 < uVar1) {
    *param_2 = uVar3;
    *param_3 = uVar1;
    uVar2 = *param_1;
    uVar3 = uVar1;
    if (*param_2 < uVar2) {
      *param_1 = *param_2;
      *param_2 = uVar2;
      uVar3 = *param_3;
    }
  }
LAB_00beeecc:
  if (*param_4 < uVar3) {
    *param_3 = *param_4;
    *param_4 = uVar3;
    uVar3 = *param_2;
    if (*param_3 < uVar3) {
      *param_2 = *param_3;
      *param_3 = uVar3;
      uVar3 = *param_1;
      if (*param_2 < uVar3) {
        *param_1 = *param_2;
        *param_2 = uVar3;
      }
    }
  }
  uVar3 = *param_4;
  if (*param_5 < uVar3) {
    *param_4 = *param_5;
    *param_5 = uVar3;
    uVar3 = *param_3;
    if (*param_4 < uVar3) {
      *param_3 = *param_4;
      *param_4 = uVar3;
      uVar3 = *param_2;
      if (*param_3 < uVar3) {
        *param_2 = *param_3;
        *param_3 = uVar3;
        uVar3 = *param_1;
        if (*param_2 < uVar3) {
          *param_1 = *param_2;
          *param_2 = uVar3;
        }
      }
    }
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00beee4c"></a> `00beee4c` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00beee50"></a> `00beee50` | `28 00 40 f9` | ldr x8,[x1] | `FALL_THROUGH`
<a id="insn-00beee54"></a> `00beee54` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-00beee58"></a> `00beee58` | `4a 00 40 f9` | ldr x10,[x2] | `FALL_THROUGH`
<a id="insn-00beee5c"></a> `00beee5c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00beee60"></a> `00beee60` | `a2 00 00 54` | b.cs 0x00beee74 | `CONDITIONAL_JUMP`
<a id="insn-00beee64"></a> `00beee64` | `5f 01 08 eb` | cmp x10,x8 | `FALL_THROUGH`
<a id="insn-00beee68"></a> `00beee68` | `e2 01 00 54` | b.cs 0x00beeea4 | `CONDITIONAL_JUMP`
<a id="insn-00beee6c"></a> `00beee6c` | `0a 00 00 f9` | str x10,[x0] | `FALL_THROUGH`
<a id="insn-00beee70"></a> `00beee70` | `13 00 00 14` | b 0x00beeebc | `UNCONDITIONAL_JUMP`
<a id="insn-00beee74"></a> `00beee74` | `5f 01 08 eb` | cmp x10,x8 | `FALL_THROUGH`
<a id="insn-00beee78"></a> `00beee78` | `82 02 00 54` | b.cs 0x00beeec8 | `CONDITIONAL_JUMP`
<a id="insn-00beee7c"></a> `00beee7c` | `2a 00 00 f9` | str x10,[x1] | `FALL_THROUGH`
<a id="insn-00beee80"></a> `00beee80` | `48 00 00 f9` | str x8,[x2] | `FALL_THROUGH`
<a id="insn-00beee84"></a> `00beee84` | `29 00 40 f9` | ldr x9,[x1] | `FALL_THROUGH`
<a id="insn-00beee88"></a> `00beee88` | `0a 00 40 f9` | ldr x10,[x0] | `FALL_THROUGH`
<a id="insn-00beee8c"></a> `00beee8c` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00beee90"></a> `00beee90` | `e2 01 00 54` | b.cs 0x00beeecc | `CONDITIONAL_JUMP`
<a id="insn-00beee94"></a> `00beee94` | `09 00 00 f9` | str x9,[x0] | `FALL_THROUGH`
<a id="insn-00beee98"></a> `00beee98` | `2a 00 00 f9` | str x10,[x1] | `FALL_THROUGH`
<a id="insn-00beee9c"></a> `00beee9c` | `48 00 40 f9` | ldr x8,[x2] | `FALL_THROUGH`
<a id="insn-00beeea0"></a> `00beeea0` | `0b 00 00 14` | b 0x00beeecc | `UNCONDITIONAL_JUMP`
<a id="insn-00beeea4"></a> `00beeea4` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-00beeea8"></a> `00beeea8` | `29 00 00 f9` | str x9,[x1] | `FALL_THROUGH`
<a id="insn-00beeeac"></a> `00beeeac` | `48 00 40 f9` | ldr x8,[x2] | `FALL_THROUGH`
<a id="insn-00beeeb0"></a> `00beeeb0` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00beeeb4"></a> `00beeeb4` | `c2 00 00 54` | b.cs 0x00beeecc | `CONDITIONAL_JUMP`
<a id="insn-00beeeb8"></a> `00beeeb8` | `28 00 00 f9` | str x8,[x1] | `FALL_THROUGH`
<a id="insn-00beeebc"></a> `00beeebc` | `e8 03 09 aa` | mov x8,x9 | `FALL_THROUGH`
<a id="insn-00beeec0"></a> `00beeec0` | `49 00 00 f9` | str x9,[x2] | `FALL_THROUGH`
<a id="insn-00beeec4"></a> `00beeec4` | `02 00 00 14` | b 0x00beeecc | `UNCONDITIONAL_JUMP`
<a id="insn-00beeec8"></a> `00beeec8` | `e8 03 0a aa` | mov x8,x10 | `FALL_THROUGH`
<a id="insn-00beeecc"></a> `00beeecc` | `69 00 40 f9` | ldr x9,[x3] | `FALL_THROUGH`
<a id="insn-00beeed0"></a> `00beeed0` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00beeed4"></a> `00beeed4` | `e2 01 00 54` | b.cs 0x00beef10 | `CONDITIONAL_JUMP`
<a id="insn-00beeed8"></a> `00beeed8` | `49 00 00 f9` | str x9,[x2] | `FALL_THROUGH`
<a id="insn-00beeedc"></a> `00beeedc` | `68 00 00 f9` | str x8,[x3] | `FALL_THROUGH`
<a id="insn-00beeee0"></a> `00beeee0` | `48 00 40 f9` | ldr x8,[x2] | `FALL_THROUGH`
<a id="insn-00beeee4"></a> `00beeee4` | `29 00 40 f9` | ldr x9,[x1] | `FALL_THROUGH`
<a id="insn-00beeee8"></a> `00beeee8` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00beeeec"></a> `00beeeec` | `22 01 00 54` | b.cs 0x00beef10 | `CONDITIONAL_JUMP`
<a id="insn-00beeef0"></a> `00beeef0` | `28 00 00 f9` | str x8,[x1] | `FALL_THROUGH`
<a id="insn-00beeef4"></a> `00beeef4` | `49 00 00 f9` | str x9,[x2] | `FALL_THROUGH`
<a id="insn-00beeef8"></a> `00beeef8` | `28 00 40 f9` | ldr x8,[x1] | `FALL_THROUGH`
<a id="insn-00beeefc"></a> `00beeefc` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-00beef00"></a> `00beef00` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00beef04"></a> `00beef04` | `62 00 00 54` | b.cs 0x00beef10 | `CONDITIONAL_JUMP`
<a id="insn-00beef08"></a> `00beef08` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-00beef0c"></a> `00beef0c` | `29 00 00 f9` | str x9,[x1] | `FALL_THROUGH`
<a id="insn-00beef10"></a> `00beef10` | `88 00 40 f9` | ldr x8,[x4] | `FALL_THROUGH`
<a id="insn-00beef14"></a> `00beef14` | `69 00 40 f9` | ldr x9,[x3] | `FALL_THROUGH`
<a id="insn-00beef18"></a> `00beef18` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00beef1c"></a> `00beef1c` | `a2 02 00 54` | b.cs 0x00beef70 | `CONDITIONAL_JUMP`
<a id="insn-00beef20"></a> `00beef20` | `68 00 00 f9` | str x8,[x3] | `FALL_THROUGH`
<a id="insn-00beef24"></a> `00beef24` | `89 00 00 f9` | str x9,[x4] | `FALL_THROUGH`
<a id="insn-00beef28"></a> `00beef28` | `68 00 40 f9` | ldr x8,[x3] | `FALL_THROUGH`
<a id="insn-00beef2c"></a> `00beef2c` | `49 00 40 f9` | ldr x9,[x2] | `FALL_THROUGH`
<a id="insn-00beef30"></a> `00beef30` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00beef34"></a> `00beef34` | `e2 01 00 54` | b.cs 0x00beef70 | `CONDITIONAL_JUMP`
<a id="insn-00beef38"></a> `00beef38` | `48 00 00 f9` | str x8,[x2] | `FALL_THROUGH`
<a id="insn-00beef3c"></a> `00beef3c` | `69 00 00 f9` | str x9,[x3] | `FALL_THROUGH`
<a id="insn-00beef40"></a> `00beef40` | `48 00 40 f9` | ldr x8,[x2] | `FALL_THROUGH`
<a id="insn-00beef44"></a> `00beef44` | `29 00 40 f9` | ldr x9,[x1] | `FALL_THROUGH`
<a id="insn-00beef48"></a> `00beef48` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00beef4c"></a> `00beef4c` | `22 01 00 54` | b.cs 0x00beef70 | `CONDITIONAL_JUMP`
<a id="insn-00beef50"></a> `00beef50` | `28 00 00 f9` | str x8,[x1] | `FALL_THROUGH`
<a id="insn-00beef54"></a> `00beef54` | `49 00 00 f9` | str x9,[x2] | `FALL_THROUGH`
<a id="insn-00beef58"></a> `00beef58` | `28 00 40 f9` | ldr x8,[x1] | `FALL_THROUGH`
<a id="insn-00beef5c"></a> `00beef5c` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-00beef60"></a> `00beef60` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00beef64"></a> `00beef64` | `62 00 00 54` | b.cs 0x00beef70 | `CONDITIONAL_JUMP`
<a id="insn-00beef68"></a> `00beef68` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-00beef6c"></a> `00beef6c` | `29 00 00 f9` | str x9,[x1] | `FALL_THROUGH`
<a id="insn-00beef70"></a> `00beef70` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00beee4c`](#insn-00beee4c) 範囲 `[['00beee4c', '00beee63']]`
  - `CONDITIONAL_JUMP` [`00beee60`](#insn-00beee60) → [`00beee74`](#insn-00beee74)
  - `FALL_THROUGH` [`00beee60`](#insn-00beee60) → [`00beee64`](#insn-00beee64)
- ブロック [`00beee64`](#insn-00beee64) 範囲 `[['00beee64', '00beee6b']]`
  - `CONDITIONAL_JUMP` [`00beee68`](#insn-00beee68) → [`00beeea4`](#insn-00beeea4)
  - `FALL_THROUGH` [`00beee68`](#insn-00beee68) → [`00beee6c`](#insn-00beee6c)
- ブロック [`00beee6c`](#insn-00beee6c) 範囲 `[['00beee6c', '00beee6f']]`
  - `FALL_THROUGH` [`00beee6c`](#insn-00beee6c) → [`00beee70`](#insn-00beee70)
- ブロック [`00beee70`](#insn-00beee70) 範囲 `[['00beee70', '00beee73']]`
  - `UNCONDITIONAL_JUMP` [`00beee70`](#insn-00beee70) → [`00beeebc`](#insn-00beeebc)
- ブロック [`00beee74`](#insn-00beee74) 範囲 `[['00beee74', '00beee7b']]`
  - `CONDITIONAL_JUMP` [`00beee78`](#insn-00beee78) → [`00beeec8`](#insn-00beeec8)
  - `FALL_THROUGH` [`00beee78`](#insn-00beee78) → [`00beee7c`](#insn-00beee7c)
- ブロック [`00beee7c`](#insn-00beee7c) 範囲 `[['00beee7c', '00beee93']]`
  - `CONDITIONAL_JUMP` [`00beee90`](#insn-00beee90) → [`00beeecc`](#insn-00beeecc)
  - `FALL_THROUGH` [`00beee90`](#insn-00beee90) → [`00beee94`](#insn-00beee94)
- ブロック [`00beee94`](#insn-00beee94) 範囲 `[['00beee94', '00beeea3']]`
  - `UNCONDITIONAL_JUMP` [`00beeea0`](#insn-00beeea0) → [`00beeecc`](#insn-00beeecc)
- ブロック [`00beeea4`](#insn-00beeea4) 範囲 `[['00beeea4', '00beeeb7']]`
  - `CONDITIONAL_JUMP` [`00beeeb4`](#insn-00beeeb4) → [`00beeecc`](#insn-00beeecc)
  - `FALL_THROUGH` [`00beeeb4`](#insn-00beeeb4) → [`00beeeb8`](#insn-00beeeb8)
- ブロック [`00beeeb8`](#insn-00beeeb8) 範囲 `[['00beeeb8', '00beeebb']]`
  - `FALL_THROUGH` [`00beeeb8`](#insn-00beeeb8) → [`00beeebc`](#insn-00beeebc)
- ブロック [`00beeebc`](#insn-00beeebc) 範囲 `[['00beeebc', '00beeec7']]`
  - `UNCONDITIONAL_JUMP` [`00beeec4`](#insn-00beeec4) → [`00beeecc`](#insn-00beeecc)
- ブロック [`00beeec8`](#insn-00beeec8) 範囲 `[['00beeec8', '00beeecb']]`
  - `FALL_THROUGH` [`00beeec8`](#insn-00beeec8) → [`00beeecc`](#insn-00beeecc)
- ブロック [`00beeecc`](#insn-00beeecc) 範囲 `[['00beeecc', '00beeed7']]`
  - `CONDITIONAL_JUMP` [`00beeed4`](#insn-00beeed4) → [`00beef10`](#insn-00beef10)
  - `FALL_THROUGH` [`00beeed4`](#insn-00beeed4) → [`00beeed8`](#insn-00beeed8)
- ブロック [`00beeed8`](#insn-00beeed8) 範囲 `[['00beeed8', '00beeeef']]`
  - `CONDITIONAL_JUMP` [`00beeeec`](#insn-00beeeec) → [`00beef10`](#insn-00beef10)
  - `FALL_THROUGH` [`00beeeec`](#insn-00beeeec) → [`00beeef0`](#insn-00beeef0)
- ブロック [`00beeef0`](#insn-00beeef0) 範囲 `[['00beeef0', '00beef07']]`
  - `CONDITIONAL_JUMP` [`00beef04`](#insn-00beef04) → [`00beef10`](#insn-00beef10)
  - `FALL_THROUGH` [`00beef04`](#insn-00beef04) → [`00beef08`](#insn-00beef08)
- ブロック [`00beef08`](#insn-00beef08) 範囲 `[['00beef08', '00beef0f']]`
  - `FALL_THROUGH` [`00beef0c`](#insn-00beef0c) → [`00beef10`](#insn-00beef10)
- ブロック [`00beef10`](#insn-00beef10) 範囲 `[['00beef10', '00beef1f']]`
  - `CONDITIONAL_JUMP` [`00beef1c`](#insn-00beef1c) → [`00beef70`](#insn-00beef70)
  - `FALL_THROUGH` [`00beef1c`](#insn-00beef1c) → [`00beef20`](#insn-00beef20)
- ブロック [`00beef20`](#insn-00beef20) 範囲 `[['00beef20', '00beef37']]`
  - `CONDITIONAL_JUMP` [`00beef34`](#insn-00beef34) → [`00beef70`](#insn-00beef70)
  - `FALL_THROUGH` [`00beef34`](#insn-00beef34) → [`00beef38`](#insn-00beef38)
- ブロック [`00beef38`](#insn-00beef38) 範囲 `[['00beef38', '00beef4f']]`
  - `CONDITIONAL_JUMP` [`00beef4c`](#insn-00beef4c) → [`00beef70`](#insn-00beef70)
  - `FALL_THROUGH` [`00beef4c`](#insn-00beef4c) → [`00beef50`](#insn-00beef50)
- ブロック [`00beef50`](#insn-00beef50) 範囲 `[['00beef50', '00beef67']]`
  - `CONDITIONAL_JUMP` [`00beef64`](#insn-00beef64) → [`00beef70`](#insn-00beef70)
  - `FALL_THROUGH` [`00beef64`](#insn-00beef64) → [`00beef68`](#insn-00beef68)
- ブロック [`00beef68`](#insn-00beef68) 範囲 `[['00beef68', '00beef6f']]`
  - `FALL_THROUGH` [`00beef6c`](#insn-00beef6c) → [`00beef70`](#insn-00beef70)
- ブロック [`00beef70`](#insn-00beef70) 範囲 `[['00beef70', '00beef73']]`

## 命令位置別の参照

- [`00beee60`](#insn-00beee60) → [`00beee74`](#insn-00beee74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beee68`](#insn-00beee68) → [`00beeea4`](#insn-00beeea4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beee70`](#insn-00beee70) → [`00beeebc`](#insn-00beeebc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beee78`](#insn-00beee78) → [`00beeec8`](#insn-00beeec8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beee90`](#insn-00beee90) → [`00beeecc`](#insn-00beeecc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beeea0`](#insn-00beeea0) → [`00beeecc`](#insn-00beeecc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beeeb4`](#insn-00beeeb4) → [`00beeecc`](#insn-00beeecc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beeec4`](#insn-00beeec4) → [`00beeecc`](#insn-00beeecc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beeed4`](#insn-00beeed4) → [`00beef10`](#insn-00beef10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beeeec`](#insn-00beeeec) → [`00beef10`](#insn-00beef10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beef04`](#insn-00beef04) → [`00beef10`](#insn-00beef10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beef1c`](#insn-00beef1c) → [`00beef70`](#insn-00beef70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beef34`](#insn-00beef34) → [`00beef70`](#insn-00beef70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beef4c`](#insn-00beef4c) → [`00beef70`](#insn-00beef70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beef64`](#insn-00beef64) → [`00beef70`](#insn-00beef70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00beee60`](#insn-00beee60)

~~~json
{
  "source": "00beee60",
  "target": "00beee74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beee68`](#insn-00beee68)

~~~json
{
  "source": "00beee68",
  "target": "00beeea4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beee70`](#insn-00beee70)

~~~json
{
  "source": "00beee70",
  "target": "00beeebc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beee78`](#insn-00beee78)

~~~json
{
  "source": "00beee78",
  "target": "00beeec8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beee90`](#insn-00beee90)

~~~json
{
  "source": "00beee90",
  "target": "00beeecc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beeea0`](#insn-00beeea0)

~~~json
{
  "source": "00beeea0",
  "target": "00beeecc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beeeb4`](#insn-00beeeb4)

~~~json
{
  "source": "00beeeb4",
  "target": "00beeecc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beeec4`](#insn-00beeec4)

~~~json
{
  "source": "00beeec4",
  "target": "00beeecc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beeed4`](#insn-00beeed4)

~~~json
{
  "source": "00beeed4",
  "target": "00beef10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beeeec`](#insn-00beeeec)

~~~json
{
  "source": "00beeeec",
  "target": "00beef10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beef04`](#insn-00beef04)

~~~json
{
  "source": "00beef04",
  "target": "00beef10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beef1c`](#insn-00beef1c)

~~~json
{
  "source": "00beef1c",
  "target": "00beef70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beef34`](#insn-00beef34)

~~~json
{
  "source": "00beef34",
  "target": "00beef70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beef4c`](#insn-00beef4c)

~~~json
{
  "source": "00beef4c",
  "target": "00beef70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beef64`](#insn-00beef64)

~~~json
{
  "source": "00beef64",
  "target": "00beef70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
