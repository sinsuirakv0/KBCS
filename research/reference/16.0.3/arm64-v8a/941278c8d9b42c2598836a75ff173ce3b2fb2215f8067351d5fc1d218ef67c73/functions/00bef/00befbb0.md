# 00befbb0

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00beebbc`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bee/00beebbc.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/no_difference_in_scope-0014.md#compare-f8a55aa711d3806403fb8480de3e5191)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00befbb0",
  "name": "FUN_00befbb0",
  "size": 296,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "71c449da935a01c52233ffc56f432ef429393d2ca9fc55807b903566a57f1bfc",
  "source_text_sha256": "71c449da935a01c52233ffc56f432ef429393d2ca9fc55807b903566a57f1bfc",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00befbb0",
        "00befcd7"
      ]
    ],
    "bytes_sha256": "1310b151e1bb2d79a453346eb0cb7d6d1a67dfdb7c723b8625b531b3e54a45cb",
    "instruction_count": 74,
    "instruction_bytes": 296,
    "body_bytes": 296,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00be8fd0](../00be8/00be8fd0.md)
- [00bef910](../00bef/00bef910.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1529 bytes

~~~c

void FUN_00befbb0(double *param_1,double *param_2,double *param_3,double *param_4,double *param_5)

{
  double dVar1;
  double dVar2;
  double dVar3;
  
  dVar1 = *param_2;
  dVar2 = *param_1;
  dVar3 = *param_3;
  if (dVar2 <= dVar1) {
    if (dVar3 < dVar1) {
      *param_2 = dVar3;
      *param_3 = dVar1;
      dVar2 = *param_1;
      dVar3 = dVar1;
      if (*param_2 < dVar2) {
        *param_1 = *param_2;
        *param_2 = dVar2;
        dVar3 = *param_3;
      }
    }
  }
  else {
    if (dVar1 <= dVar3) {
      *param_1 = dVar1;
      *param_2 = dVar2;
      dVar3 = *param_3;
      if (dVar2 <= dVar3) goto LAB_00befc30;
      *param_2 = dVar3;
    }
    else {
      *param_1 = dVar3;
    }
    *param_3 = dVar2;
    dVar3 = dVar2;
  }
LAB_00befc30:
  if (*param_4 < dVar3) {
    *param_3 = *param_4;
    *param_4 = dVar3;
    dVar3 = *param_2;
    if (*param_3 < dVar3) {
      *param_2 = *param_3;
      *param_3 = dVar3;
      dVar3 = *param_1;
      if (*param_2 < dVar3) {
        *param_1 = *param_2;
        *param_2 = dVar3;
      }
    }
  }
  dVar3 = *param_4;
  if (*param_5 < dVar3) {
    *param_4 = *param_5;
    *param_5 = dVar3;
    dVar3 = *param_3;
    if (*param_4 < dVar3) {
      *param_3 = *param_4;
      *param_4 = dVar3;
      dVar3 = *param_2;
      if (*param_3 < dVar3) {
        *param_2 = *param_3;
        *param_3 = dVar3;
        dVar3 = *param_1;
        if (*param_2 < dVar3) {
          *param_1 = *param_2;
          *param_2 = dVar3;
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
<a id="insn-00befbb0"></a> `00befbb0` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00befbb4"></a> `00befbb4` | `20 00 40 fd` | ldr d0,[x1] | `FALL_THROUGH`
<a id="insn-00befbb8"></a> `00befbb8` | `01 00 40 fd` | ldr d1,[x0] | `FALL_THROUGH`
<a id="insn-00befbbc"></a> `00befbbc` | `42 00 40 fd` | ldr d2,[x2] | `FALL_THROUGH`
<a id="insn-00befbc0"></a> `00befbc0` | `00 20 61 1e` | fcmp d0,d1 | `FALL_THROUGH`
<a id="insn-00befbc4"></a> `00befbc4` | `a5 00 00 54` | b.pl 0x00befbd8 | `CONDITIONAL_JUMP`
<a id="insn-00befbc8"></a> `00befbc8` | `40 20 60 1e` | fcmp d2,d0 | `FALL_THROUGH`
<a id="insn-00befbcc"></a> `00befbcc` | `e5 01 00 54` | b.pl 0x00befc08 | `CONDITIONAL_JUMP`
<a id="insn-00befbd0"></a> `00befbd0` | `02 00 00 fd` | str d2,[x0] | `FALL_THROUGH`
<a id="insn-00befbd4"></a> `00befbd4` | `13 00 00 14` | b 0x00befc20 | `UNCONDITIONAL_JUMP`
<a id="insn-00befbd8"></a> `00befbd8` | `40 20 60 1e` | fcmp d2,d0 | `FALL_THROUGH`
<a id="insn-00befbdc"></a> `00befbdc` | `85 02 00 54` | b.pl 0x00befc2c | `CONDITIONAL_JUMP`
<a id="insn-00befbe0"></a> `00befbe0` | `22 00 00 fd` | str d2,[x1] | `FALL_THROUGH`
<a id="insn-00befbe4"></a> `00befbe4` | `40 00 00 fd` | str d0,[x2] | `FALL_THROUGH`
<a id="insn-00befbe8"></a> `00befbe8` | `21 00 40 fd` | ldr d1,[x1] | `FALL_THROUGH`
<a id="insn-00befbec"></a> `00befbec` | `02 00 40 fd` | ldr d2,[x0] | `FALL_THROUGH`
<a id="insn-00befbf0"></a> `00befbf0` | `20 20 62 1e` | fcmp d1,d2 | `FALL_THROUGH`
<a id="insn-00befbf4"></a> `00befbf4` | `e5 01 00 54` | b.pl 0x00befc30 | `CONDITIONAL_JUMP`
<a id="insn-00befbf8"></a> `00befbf8` | `01 00 00 fd` | str d1,[x0] | `FALL_THROUGH`
<a id="insn-00befbfc"></a> `00befbfc` | `22 00 00 fd` | str d2,[x1] | `FALL_THROUGH`
<a id="insn-00befc00"></a> `00befc00` | `40 00 40 fd` | ldr d0,[x2] | `FALL_THROUGH`
<a id="insn-00befc04"></a> `00befc04` | `0b 00 00 14` | b 0x00befc30 | `UNCONDITIONAL_JUMP`
<a id="insn-00befc08"></a> `00befc08` | `00 00 00 fd` | str d0,[x0] | `FALL_THROUGH`
<a id="insn-00befc0c"></a> `00befc0c` | `21 00 00 fd` | str d1,[x1] | `FALL_THROUGH`
<a id="insn-00befc10"></a> `00befc10` | `40 00 40 fd` | ldr d0,[x2] | `FALL_THROUGH`
<a id="insn-00befc14"></a> `00befc14` | `00 20 61 1e` | fcmp d0,d1 | `FALL_THROUGH`
<a id="insn-00befc18"></a> `00befc18` | `c5 00 00 54` | b.pl 0x00befc30 | `CONDITIONAL_JUMP`
<a id="insn-00befc1c"></a> `00befc1c` | `20 00 00 fd` | str d0,[x1] | `FALL_THROUGH`
<a id="insn-00befc20"></a> `00befc20` | `20 40 60 1e` | fmov d0,d1 | `FALL_THROUGH`
<a id="insn-00befc24"></a> `00befc24` | `41 00 00 fd` | str d1,[x2] | `FALL_THROUGH`
<a id="insn-00befc28"></a> `00befc28` | `02 00 00 14` | b 0x00befc30 | `UNCONDITIONAL_JUMP`
<a id="insn-00befc2c"></a> `00befc2c` | `40 40 60 1e` | fmov d0,d2 | `FALL_THROUGH`
<a id="insn-00befc30"></a> `00befc30` | `61 00 40 fd` | ldr d1,[x3] | `FALL_THROUGH`
<a id="insn-00befc34"></a> `00befc34` | `20 20 60 1e` | fcmp d1,d0 | `FALL_THROUGH`
<a id="insn-00befc38"></a> `00befc38` | `e5 01 00 54` | b.pl 0x00befc74 | `CONDITIONAL_JUMP`
<a id="insn-00befc3c"></a> `00befc3c` | `41 00 00 fd` | str d1,[x2] | `FALL_THROUGH`
<a id="insn-00befc40"></a> `00befc40` | `60 00 00 fd` | str d0,[x3] | `FALL_THROUGH`
<a id="insn-00befc44"></a> `00befc44` | `40 00 40 fd` | ldr d0,[x2] | `FALL_THROUGH`
<a id="insn-00befc48"></a> `00befc48` | `21 00 40 fd` | ldr d1,[x1] | `FALL_THROUGH`
<a id="insn-00befc4c"></a> `00befc4c` | `00 20 61 1e` | fcmp d0,d1 | `FALL_THROUGH`
<a id="insn-00befc50"></a> `00befc50` | `25 01 00 54` | b.pl 0x00befc74 | `CONDITIONAL_JUMP`
<a id="insn-00befc54"></a> `00befc54` | `20 00 00 fd` | str d0,[x1] | `FALL_THROUGH`
<a id="insn-00befc58"></a> `00befc58` | `41 00 00 fd` | str d1,[x2] | `FALL_THROUGH`
<a id="insn-00befc5c"></a> `00befc5c` | `20 00 40 fd` | ldr d0,[x1] | `FALL_THROUGH`
<a id="insn-00befc60"></a> `00befc60` | `01 00 40 fd` | ldr d1,[x0] | `FALL_THROUGH`
<a id="insn-00befc64"></a> `00befc64` | `00 20 61 1e` | fcmp d0,d1 | `FALL_THROUGH`
<a id="insn-00befc68"></a> `00befc68` | `65 00 00 54` | b.pl 0x00befc74 | `CONDITIONAL_JUMP`
<a id="insn-00befc6c"></a> `00befc6c` | `00 00 00 fd` | str d0,[x0] | `FALL_THROUGH`
<a id="insn-00befc70"></a> `00befc70` | `21 00 00 fd` | str d1,[x1] | `FALL_THROUGH`
<a id="insn-00befc74"></a> `00befc74` | `80 00 40 fd` | ldr d0,[x4] | `FALL_THROUGH`
<a id="insn-00befc78"></a> `00befc78` | `61 00 40 fd` | ldr d1,[x3] | `FALL_THROUGH`
<a id="insn-00befc7c"></a> `00befc7c` | `00 20 61 1e` | fcmp d0,d1 | `FALL_THROUGH`
<a id="insn-00befc80"></a> `00befc80` | `a5 02 00 54` | b.pl 0x00befcd4 | `CONDITIONAL_JUMP`
<a id="insn-00befc84"></a> `00befc84` | `60 00 00 fd` | str d0,[x3] | `FALL_THROUGH`
<a id="insn-00befc88"></a> `00befc88` | `81 00 00 fd` | str d1,[x4] | `FALL_THROUGH`
<a id="insn-00befc8c"></a> `00befc8c` | `60 00 40 fd` | ldr d0,[x3] | `FALL_THROUGH`
<a id="insn-00befc90"></a> `00befc90` | `41 00 40 fd` | ldr d1,[x2] | `FALL_THROUGH`
<a id="insn-00befc94"></a> `00befc94` | `00 20 61 1e` | fcmp d0,d1 | `FALL_THROUGH`
<a id="insn-00befc98"></a> `00befc98` | `e5 01 00 54` | b.pl 0x00befcd4 | `CONDITIONAL_JUMP`
<a id="insn-00befc9c"></a> `00befc9c` | `40 00 00 fd` | str d0,[x2] | `FALL_THROUGH`
<a id="insn-00befca0"></a> `00befca0` | `61 00 00 fd` | str d1,[x3] | `FALL_THROUGH`
<a id="insn-00befca4"></a> `00befca4` | `40 00 40 fd` | ldr d0,[x2] | `FALL_THROUGH`
<a id="insn-00befca8"></a> `00befca8` | `21 00 40 fd` | ldr d1,[x1] | `FALL_THROUGH`
<a id="insn-00befcac"></a> `00befcac` | `00 20 61 1e` | fcmp d0,d1 | `FALL_THROUGH`
<a id="insn-00befcb0"></a> `00befcb0` | `25 01 00 54` | b.pl 0x00befcd4 | `CONDITIONAL_JUMP`
<a id="insn-00befcb4"></a> `00befcb4` | `20 00 00 fd` | str d0,[x1] | `FALL_THROUGH`
<a id="insn-00befcb8"></a> `00befcb8` | `41 00 00 fd` | str d1,[x2] | `FALL_THROUGH`
<a id="insn-00befcbc"></a> `00befcbc` | `20 00 40 fd` | ldr d0,[x1] | `FALL_THROUGH`
<a id="insn-00befcc0"></a> `00befcc0` | `01 00 40 fd` | ldr d1,[x0] | `FALL_THROUGH`
<a id="insn-00befcc4"></a> `00befcc4` | `00 20 61 1e` | fcmp d0,d1 | `FALL_THROUGH`
<a id="insn-00befcc8"></a> `00befcc8` | `65 00 00 54` | b.pl 0x00befcd4 | `CONDITIONAL_JUMP`
<a id="insn-00befccc"></a> `00befccc` | `00 00 00 fd` | str d0,[x0] | `FALL_THROUGH`
<a id="insn-00befcd0"></a> `00befcd0` | `21 00 00 fd` | str d1,[x1] | `FALL_THROUGH`
<a id="insn-00befcd4"></a> `00befcd4` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00befbb0`](#insn-00befbb0) 範囲 `[['00befbb0', '00befbc7']]`
  - `CONDITIONAL_JUMP` [`00befbc4`](#insn-00befbc4) → [`00befbd8`](#insn-00befbd8)
  - `FALL_THROUGH` [`00befbc4`](#insn-00befbc4) → [`00befbc8`](#insn-00befbc8)
- ブロック [`00befbc8`](#insn-00befbc8) 範囲 `[['00befbc8', '00befbcf']]`
  - `CONDITIONAL_JUMP` [`00befbcc`](#insn-00befbcc) → [`00befc08`](#insn-00befc08)
  - `FALL_THROUGH` [`00befbcc`](#insn-00befbcc) → [`00befbd0`](#insn-00befbd0)
- ブロック [`00befbd0`](#insn-00befbd0) 範囲 `[['00befbd0', '00befbd7']]`
  - `UNCONDITIONAL_JUMP` [`00befbd4`](#insn-00befbd4) → [`00befc20`](#insn-00befc20)
- ブロック [`00befbd8`](#insn-00befbd8) 範囲 `[['00befbd8', '00befbdf']]`
  - `CONDITIONAL_JUMP` [`00befbdc`](#insn-00befbdc) → [`00befc2c`](#insn-00befc2c)
  - `FALL_THROUGH` [`00befbdc`](#insn-00befbdc) → [`00befbe0`](#insn-00befbe0)
- ブロック [`00befbe0`](#insn-00befbe0) 範囲 `[['00befbe0', '00befbf7']]`
  - `CONDITIONAL_JUMP` [`00befbf4`](#insn-00befbf4) → [`00befc30`](#insn-00befc30)
  - `FALL_THROUGH` [`00befbf4`](#insn-00befbf4) → [`00befbf8`](#insn-00befbf8)
- ブロック [`00befbf8`](#insn-00befbf8) 範囲 `[['00befbf8', '00befc07']]`
  - `UNCONDITIONAL_JUMP` [`00befc04`](#insn-00befc04) → [`00befc30`](#insn-00befc30)
- ブロック [`00befc08`](#insn-00befc08) 範囲 `[['00befc08', '00befc1b']]`
  - `CONDITIONAL_JUMP` [`00befc18`](#insn-00befc18) → [`00befc30`](#insn-00befc30)
  - `FALL_THROUGH` [`00befc18`](#insn-00befc18) → [`00befc1c`](#insn-00befc1c)
- ブロック [`00befc1c`](#insn-00befc1c) 範囲 `[['00befc1c', '00befc1f']]`
  - `FALL_THROUGH` [`00befc1c`](#insn-00befc1c) → [`00befc20`](#insn-00befc20)
- ブロック [`00befc20`](#insn-00befc20) 範囲 `[['00befc20', '00befc2b']]`
  - `UNCONDITIONAL_JUMP` [`00befc28`](#insn-00befc28) → [`00befc30`](#insn-00befc30)
- ブロック [`00befc2c`](#insn-00befc2c) 範囲 `[['00befc2c', '00befc2f']]`
  - `FALL_THROUGH` [`00befc2c`](#insn-00befc2c) → [`00befc30`](#insn-00befc30)
- ブロック [`00befc30`](#insn-00befc30) 範囲 `[['00befc30', '00befc3b']]`
  - `CONDITIONAL_JUMP` [`00befc38`](#insn-00befc38) → [`00befc74`](#insn-00befc74)
  - `FALL_THROUGH` [`00befc38`](#insn-00befc38) → [`00befc3c`](#insn-00befc3c)
- ブロック [`00befc3c`](#insn-00befc3c) 範囲 `[['00befc3c', '00befc53']]`
  - `CONDITIONAL_JUMP` [`00befc50`](#insn-00befc50) → [`00befc74`](#insn-00befc74)
  - `FALL_THROUGH` [`00befc50`](#insn-00befc50) → [`00befc54`](#insn-00befc54)
- ブロック [`00befc54`](#insn-00befc54) 範囲 `[['00befc54', '00befc6b']]`
  - `CONDITIONAL_JUMP` [`00befc68`](#insn-00befc68) → [`00befc74`](#insn-00befc74)
  - `FALL_THROUGH` [`00befc68`](#insn-00befc68) → [`00befc6c`](#insn-00befc6c)
- ブロック [`00befc6c`](#insn-00befc6c) 範囲 `[['00befc6c', '00befc73']]`
  - `FALL_THROUGH` [`00befc70`](#insn-00befc70) → [`00befc74`](#insn-00befc74)
- ブロック [`00befc74`](#insn-00befc74) 範囲 `[['00befc74', '00befc83']]`
  - `CONDITIONAL_JUMP` [`00befc80`](#insn-00befc80) → [`00befcd4`](#insn-00befcd4)
  - `FALL_THROUGH` [`00befc80`](#insn-00befc80) → [`00befc84`](#insn-00befc84)
- ブロック [`00befc84`](#insn-00befc84) 範囲 `[['00befc84', '00befc9b']]`
  - `CONDITIONAL_JUMP` [`00befc98`](#insn-00befc98) → [`00befcd4`](#insn-00befcd4)
  - `FALL_THROUGH` [`00befc98`](#insn-00befc98) → [`00befc9c`](#insn-00befc9c)
- ブロック [`00befc9c`](#insn-00befc9c) 範囲 `[['00befc9c', '00befcb3']]`
  - `CONDITIONAL_JUMP` [`00befcb0`](#insn-00befcb0) → [`00befcd4`](#insn-00befcd4)
  - `FALL_THROUGH` [`00befcb0`](#insn-00befcb0) → [`00befcb4`](#insn-00befcb4)
- ブロック [`00befcb4`](#insn-00befcb4) 範囲 `[['00befcb4', '00befccb']]`
  - `CONDITIONAL_JUMP` [`00befcc8`](#insn-00befcc8) → [`00befcd4`](#insn-00befcd4)
  - `FALL_THROUGH` [`00befcc8`](#insn-00befcc8) → [`00befccc`](#insn-00befccc)
- ブロック [`00befccc`](#insn-00befccc) 範囲 `[['00befccc', '00befcd3']]`
  - `FALL_THROUGH` [`00befcd0`](#insn-00befcd0) → [`00befcd4`](#insn-00befcd4)
- ブロック [`00befcd4`](#insn-00befcd4) 範囲 `[['00befcd4', '00befcd7']]`

## 命令位置別の参照

- [`00befbc4`](#insn-00befbc4) → [`00befbd8`](#insn-00befbd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00befbcc`](#insn-00befbcc) → [`00befc08`](#insn-00befc08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00befbd4`](#insn-00befbd4) → [`00befc20`](#insn-00befc20) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00befbdc`](#insn-00befbdc) → [`00befc2c`](#insn-00befc2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00befbf4`](#insn-00befbf4) → [`00befc30`](#insn-00befc30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00befc04`](#insn-00befc04) → [`00befc30`](#insn-00befc30) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00befc18`](#insn-00befc18) → [`00befc30`](#insn-00befc30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00befc28`](#insn-00befc28) → [`00befc30`](#insn-00befc30) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00befc38`](#insn-00befc38) → [`00befc74`](#insn-00befc74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00befc50`](#insn-00befc50) → [`00befc74`](#insn-00befc74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00befc68`](#insn-00befc68) → [`00befc74`](#insn-00befc74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00befc80`](#insn-00befc80) → [`00befcd4`](#insn-00befcd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00befc98`](#insn-00befc98) → [`00befcd4`](#insn-00befcd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00befcb0`](#insn-00befcb0) → [`00befcd4`](#insn-00befcd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00befcc8`](#insn-00befcc8) → [`00befcd4`](#insn-00befcd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00befbc4`](#insn-00befbc4)

~~~json
{
  "source": "00befbc4",
  "target": "00befbd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00befbcc`](#insn-00befbcc)

~~~json
{
  "source": "00befbcc",
  "target": "00befc08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00befbd4`](#insn-00befbd4)

~~~json
{
  "source": "00befbd4",
  "target": "00befc20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00befbdc`](#insn-00befbdc)

~~~json
{
  "source": "00befbdc",
  "target": "00befc2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00befbf4`](#insn-00befbf4)

~~~json
{
  "source": "00befbf4",
  "target": "00befc30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00befc04`](#insn-00befc04)

~~~json
{
  "source": "00befc04",
  "target": "00befc30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00befc18`](#insn-00befc18)

~~~json
{
  "source": "00befc18",
  "target": "00befc30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00befc28`](#insn-00befc28)

~~~json
{
  "source": "00befc28",
  "target": "00befc30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00befc38`](#insn-00befc38)

~~~json
{
  "source": "00befc38",
  "target": "00befc74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00befc50`](#insn-00befc50)

~~~json
{
  "source": "00befc50",
  "target": "00befc74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00befc68`](#insn-00befc68)

~~~json
{
  "source": "00befc68",
  "target": "00befc74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00befc80`](#insn-00befc80)

~~~json
{
  "source": "00befc80",
  "target": "00befcd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00befc98`](#insn-00befc98)

~~~json
{
  "source": "00befc98",
  "target": "00befcd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00befcb0`](#insn-00befcb0)

~~~json
{
  "source": "00befcb0",
  "target": "00befcd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00befcc8`](#insn-00befcc8)

~~~json
{
  "source": "00befcc8",
  "target": "00befcd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
