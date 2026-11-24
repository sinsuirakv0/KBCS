# 00beebbc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00beeb20`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bee/00beeb20.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/no_difference_in_scope-0014.md#compare-6f7b1b123a1b3d1d9c294e07c4e0af70)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00befbb0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bef/00befbb0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/no_difference_in_scope-0014.md#compare-f8a55aa711d3806403fb8480de3e5191)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00beebbc",
  "name": "FUN_00beebbc",
  "size": 296,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "89d7d7b673f5c4ec03773ce4de799b86546055e615f2290bd3bd2ce20989c66a",
  "source_text_sha256": "89d7d7b673f5c4ec03773ce4de799b86546055e615f2290bd3bd2ce20989c66a",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00beebbc",
        "00beece3"
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

- [00be7fdc](../00be7/00be7fdc.md)
- [00bee91c](../00bee/00bee91c.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1529 bytes

~~~c

void FUN_00beebbc(double *param_1,double *param_2,double *param_3,double *param_4,double *param_5)

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
      if (dVar2 <= dVar3) goto LAB_00beec3c;
      *param_2 = dVar3;
    }
    else {
      *param_1 = dVar3;
    }
    *param_3 = dVar2;
    dVar3 = dVar2;
  }
LAB_00beec3c:
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
<a id="insn-00beebbc"></a> `00beebbc` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00beebc0"></a> `00beebc0` | `20 00 40 fd` | ldr d0,[x1] | `FALL_THROUGH`
<a id="insn-00beebc4"></a> `00beebc4` | `01 00 40 fd` | ldr d1,[x0] | `FALL_THROUGH`
<a id="insn-00beebc8"></a> `00beebc8` | `42 00 40 fd` | ldr d2,[x2] | `FALL_THROUGH`
<a id="insn-00beebcc"></a> `00beebcc` | `00 20 61 1e` | fcmp d0,d1 | `FALL_THROUGH`
<a id="insn-00beebd0"></a> `00beebd0` | `a5 00 00 54` | b.pl 0x00beebe4 | `CONDITIONAL_JUMP`
<a id="insn-00beebd4"></a> `00beebd4` | `40 20 60 1e` | fcmp d2,d0 | `FALL_THROUGH`
<a id="insn-00beebd8"></a> `00beebd8` | `e5 01 00 54` | b.pl 0x00beec14 | `CONDITIONAL_JUMP`
<a id="insn-00beebdc"></a> `00beebdc` | `02 00 00 fd` | str d2,[x0] | `FALL_THROUGH`
<a id="insn-00beebe0"></a> `00beebe0` | `13 00 00 14` | b 0x00beec2c | `UNCONDITIONAL_JUMP`
<a id="insn-00beebe4"></a> `00beebe4` | `40 20 60 1e` | fcmp d2,d0 | `FALL_THROUGH`
<a id="insn-00beebe8"></a> `00beebe8` | `85 02 00 54` | b.pl 0x00beec38 | `CONDITIONAL_JUMP`
<a id="insn-00beebec"></a> `00beebec` | `22 00 00 fd` | str d2,[x1] | `FALL_THROUGH`
<a id="insn-00beebf0"></a> `00beebf0` | `40 00 00 fd` | str d0,[x2] | `FALL_THROUGH`
<a id="insn-00beebf4"></a> `00beebf4` | `21 00 40 fd` | ldr d1,[x1] | `FALL_THROUGH`
<a id="insn-00beebf8"></a> `00beebf8` | `02 00 40 fd` | ldr d2,[x0] | `FALL_THROUGH`
<a id="insn-00beebfc"></a> `00beebfc` | `20 20 62 1e` | fcmp d1,d2 | `FALL_THROUGH`
<a id="insn-00beec00"></a> `00beec00` | `e5 01 00 54` | b.pl 0x00beec3c | `CONDITIONAL_JUMP`
<a id="insn-00beec04"></a> `00beec04` | `01 00 00 fd` | str d1,[x0] | `FALL_THROUGH`
<a id="insn-00beec08"></a> `00beec08` | `22 00 00 fd` | str d2,[x1] | `FALL_THROUGH`
<a id="insn-00beec0c"></a> `00beec0c` | `40 00 40 fd` | ldr d0,[x2] | `FALL_THROUGH`
<a id="insn-00beec10"></a> `00beec10` | `0b 00 00 14` | b 0x00beec3c | `UNCONDITIONAL_JUMP`
<a id="insn-00beec14"></a> `00beec14` | `00 00 00 fd` | str d0,[x0] | `FALL_THROUGH`
<a id="insn-00beec18"></a> `00beec18` | `21 00 00 fd` | str d1,[x1] | `FALL_THROUGH`
<a id="insn-00beec1c"></a> `00beec1c` | `40 00 40 fd` | ldr d0,[x2] | `FALL_THROUGH`
<a id="insn-00beec20"></a> `00beec20` | `00 20 61 1e` | fcmp d0,d1 | `FALL_THROUGH`
<a id="insn-00beec24"></a> `00beec24` | `c5 00 00 54` | b.pl 0x00beec3c | `CONDITIONAL_JUMP`
<a id="insn-00beec28"></a> `00beec28` | `20 00 00 fd` | str d0,[x1] | `FALL_THROUGH`
<a id="insn-00beec2c"></a> `00beec2c` | `20 40 60 1e` | fmov d0,d1 | `FALL_THROUGH`
<a id="insn-00beec30"></a> `00beec30` | `41 00 00 fd` | str d1,[x2] | `FALL_THROUGH`
<a id="insn-00beec34"></a> `00beec34` | `02 00 00 14` | b 0x00beec3c | `UNCONDITIONAL_JUMP`
<a id="insn-00beec38"></a> `00beec38` | `40 40 60 1e` | fmov d0,d2 | `FALL_THROUGH`
<a id="insn-00beec3c"></a> `00beec3c` | `61 00 40 fd` | ldr d1,[x3] | `FALL_THROUGH`
<a id="insn-00beec40"></a> `00beec40` | `20 20 60 1e` | fcmp d1,d0 | `FALL_THROUGH`
<a id="insn-00beec44"></a> `00beec44` | `e5 01 00 54` | b.pl 0x00beec80 | `CONDITIONAL_JUMP`
<a id="insn-00beec48"></a> `00beec48` | `41 00 00 fd` | str d1,[x2] | `FALL_THROUGH`
<a id="insn-00beec4c"></a> `00beec4c` | `60 00 00 fd` | str d0,[x3] | `FALL_THROUGH`
<a id="insn-00beec50"></a> `00beec50` | `40 00 40 fd` | ldr d0,[x2] | `FALL_THROUGH`
<a id="insn-00beec54"></a> `00beec54` | `21 00 40 fd` | ldr d1,[x1] | `FALL_THROUGH`
<a id="insn-00beec58"></a> `00beec58` | `00 20 61 1e` | fcmp d0,d1 | `FALL_THROUGH`
<a id="insn-00beec5c"></a> `00beec5c` | `25 01 00 54` | b.pl 0x00beec80 | `CONDITIONAL_JUMP`
<a id="insn-00beec60"></a> `00beec60` | `20 00 00 fd` | str d0,[x1] | `FALL_THROUGH`
<a id="insn-00beec64"></a> `00beec64` | `41 00 00 fd` | str d1,[x2] | `FALL_THROUGH`
<a id="insn-00beec68"></a> `00beec68` | `20 00 40 fd` | ldr d0,[x1] | `FALL_THROUGH`
<a id="insn-00beec6c"></a> `00beec6c` | `01 00 40 fd` | ldr d1,[x0] | `FALL_THROUGH`
<a id="insn-00beec70"></a> `00beec70` | `00 20 61 1e` | fcmp d0,d1 | `FALL_THROUGH`
<a id="insn-00beec74"></a> `00beec74` | `65 00 00 54` | b.pl 0x00beec80 | `CONDITIONAL_JUMP`
<a id="insn-00beec78"></a> `00beec78` | `00 00 00 fd` | str d0,[x0] | `FALL_THROUGH`
<a id="insn-00beec7c"></a> `00beec7c` | `21 00 00 fd` | str d1,[x1] | `FALL_THROUGH`
<a id="insn-00beec80"></a> `00beec80` | `80 00 40 fd` | ldr d0,[x4] | `FALL_THROUGH`
<a id="insn-00beec84"></a> `00beec84` | `61 00 40 fd` | ldr d1,[x3] | `FALL_THROUGH`
<a id="insn-00beec88"></a> `00beec88` | `00 20 61 1e` | fcmp d0,d1 | `FALL_THROUGH`
<a id="insn-00beec8c"></a> `00beec8c` | `a5 02 00 54` | b.pl 0x00beece0 | `CONDITIONAL_JUMP`
<a id="insn-00beec90"></a> `00beec90` | `60 00 00 fd` | str d0,[x3] | `FALL_THROUGH`
<a id="insn-00beec94"></a> `00beec94` | `81 00 00 fd` | str d1,[x4] | `FALL_THROUGH`
<a id="insn-00beec98"></a> `00beec98` | `60 00 40 fd` | ldr d0,[x3] | `FALL_THROUGH`
<a id="insn-00beec9c"></a> `00beec9c` | `41 00 40 fd` | ldr d1,[x2] | `FALL_THROUGH`
<a id="insn-00beeca0"></a> `00beeca0` | `00 20 61 1e` | fcmp d0,d1 | `FALL_THROUGH`
<a id="insn-00beeca4"></a> `00beeca4` | `e5 01 00 54` | b.pl 0x00beece0 | `CONDITIONAL_JUMP`
<a id="insn-00beeca8"></a> `00beeca8` | `40 00 00 fd` | str d0,[x2] | `FALL_THROUGH`
<a id="insn-00beecac"></a> `00beecac` | `61 00 00 fd` | str d1,[x3] | `FALL_THROUGH`
<a id="insn-00beecb0"></a> `00beecb0` | `40 00 40 fd` | ldr d0,[x2] | `FALL_THROUGH`
<a id="insn-00beecb4"></a> `00beecb4` | `21 00 40 fd` | ldr d1,[x1] | `FALL_THROUGH`
<a id="insn-00beecb8"></a> `00beecb8` | `00 20 61 1e` | fcmp d0,d1 | `FALL_THROUGH`
<a id="insn-00beecbc"></a> `00beecbc` | `25 01 00 54` | b.pl 0x00beece0 | `CONDITIONAL_JUMP`
<a id="insn-00beecc0"></a> `00beecc0` | `20 00 00 fd` | str d0,[x1] | `FALL_THROUGH`
<a id="insn-00beecc4"></a> `00beecc4` | `41 00 00 fd` | str d1,[x2] | `FALL_THROUGH`
<a id="insn-00beecc8"></a> `00beecc8` | `20 00 40 fd` | ldr d0,[x1] | `FALL_THROUGH`
<a id="insn-00beeccc"></a> `00beeccc` | `01 00 40 fd` | ldr d1,[x0] | `FALL_THROUGH`
<a id="insn-00beecd0"></a> `00beecd0` | `00 20 61 1e` | fcmp d0,d1 | `FALL_THROUGH`
<a id="insn-00beecd4"></a> `00beecd4` | `65 00 00 54` | b.pl 0x00beece0 | `CONDITIONAL_JUMP`
<a id="insn-00beecd8"></a> `00beecd8` | `00 00 00 fd` | str d0,[x0] | `FALL_THROUGH`
<a id="insn-00beecdc"></a> `00beecdc` | `21 00 00 fd` | str d1,[x1] | `FALL_THROUGH`
<a id="insn-00beece0"></a> `00beece0` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00beebbc`](#insn-00beebbc) 範囲 `[['00beebbc', '00beebd3']]`
  - `CONDITIONAL_JUMP` [`00beebd0`](#insn-00beebd0) → [`00beebe4`](#insn-00beebe4)
  - `FALL_THROUGH` [`00beebd0`](#insn-00beebd0) → [`00beebd4`](#insn-00beebd4)
- ブロック [`00beebd4`](#insn-00beebd4) 範囲 `[['00beebd4', '00beebdb']]`
  - `CONDITIONAL_JUMP` [`00beebd8`](#insn-00beebd8) → [`00beec14`](#insn-00beec14)
  - `FALL_THROUGH` [`00beebd8`](#insn-00beebd8) → [`00beebdc`](#insn-00beebdc)
- ブロック [`00beebdc`](#insn-00beebdc) 範囲 `[['00beebdc', '00beebe3']]`
  - `UNCONDITIONAL_JUMP` [`00beebe0`](#insn-00beebe0) → [`00beec2c`](#insn-00beec2c)
- ブロック [`00beebe4`](#insn-00beebe4) 範囲 `[['00beebe4', '00beebeb']]`
  - `CONDITIONAL_JUMP` [`00beebe8`](#insn-00beebe8) → [`00beec38`](#insn-00beec38)
  - `FALL_THROUGH` [`00beebe8`](#insn-00beebe8) → [`00beebec`](#insn-00beebec)
- ブロック [`00beebec`](#insn-00beebec) 範囲 `[['00beebec', '00beec03']]`
  - `CONDITIONAL_JUMP` [`00beec00`](#insn-00beec00) → [`00beec3c`](#insn-00beec3c)
  - `FALL_THROUGH` [`00beec00`](#insn-00beec00) → [`00beec04`](#insn-00beec04)
- ブロック [`00beec04`](#insn-00beec04) 範囲 `[['00beec04', '00beec13']]`
  - `UNCONDITIONAL_JUMP` [`00beec10`](#insn-00beec10) → [`00beec3c`](#insn-00beec3c)
- ブロック [`00beec14`](#insn-00beec14) 範囲 `[['00beec14', '00beec27']]`
  - `CONDITIONAL_JUMP` [`00beec24`](#insn-00beec24) → [`00beec3c`](#insn-00beec3c)
  - `FALL_THROUGH` [`00beec24`](#insn-00beec24) → [`00beec28`](#insn-00beec28)
- ブロック [`00beec28`](#insn-00beec28) 範囲 `[['00beec28', '00beec2b']]`
  - `FALL_THROUGH` [`00beec28`](#insn-00beec28) → [`00beec2c`](#insn-00beec2c)
- ブロック [`00beec2c`](#insn-00beec2c) 範囲 `[['00beec2c', '00beec37']]`
  - `UNCONDITIONAL_JUMP` [`00beec34`](#insn-00beec34) → [`00beec3c`](#insn-00beec3c)
- ブロック [`00beec38`](#insn-00beec38) 範囲 `[['00beec38', '00beec3b']]`
  - `FALL_THROUGH` [`00beec38`](#insn-00beec38) → [`00beec3c`](#insn-00beec3c)
- ブロック [`00beec3c`](#insn-00beec3c) 範囲 `[['00beec3c', '00beec47']]`
  - `CONDITIONAL_JUMP` [`00beec44`](#insn-00beec44) → [`00beec80`](#insn-00beec80)
  - `FALL_THROUGH` [`00beec44`](#insn-00beec44) → [`00beec48`](#insn-00beec48)
- ブロック [`00beec48`](#insn-00beec48) 範囲 `[['00beec48', '00beec5f']]`
  - `CONDITIONAL_JUMP` [`00beec5c`](#insn-00beec5c) → [`00beec80`](#insn-00beec80)
  - `FALL_THROUGH` [`00beec5c`](#insn-00beec5c) → [`00beec60`](#insn-00beec60)
- ブロック [`00beec60`](#insn-00beec60) 範囲 `[['00beec60', '00beec77']]`
  - `CONDITIONAL_JUMP` [`00beec74`](#insn-00beec74) → [`00beec80`](#insn-00beec80)
  - `FALL_THROUGH` [`00beec74`](#insn-00beec74) → [`00beec78`](#insn-00beec78)
- ブロック [`00beec78`](#insn-00beec78) 範囲 `[['00beec78', '00beec7f']]`
  - `FALL_THROUGH` [`00beec7c`](#insn-00beec7c) → [`00beec80`](#insn-00beec80)
- ブロック [`00beec80`](#insn-00beec80) 範囲 `[['00beec80', '00beec8f']]`
  - `CONDITIONAL_JUMP` [`00beec8c`](#insn-00beec8c) → [`00beece0`](#insn-00beece0)
  - `FALL_THROUGH` [`00beec8c`](#insn-00beec8c) → [`00beec90`](#insn-00beec90)
- ブロック [`00beec90`](#insn-00beec90) 範囲 `[['00beec90', '00beeca7']]`
  - `CONDITIONAL_JUMP` [`00beeca4`](#insn-00beeca4) → [`00beece0`](#insn-00beece0)
  - `FALL_THROUGH` [`00beeca4`](#insn-00beeca4) → [`00beeca8`](#insn-00beeca8)
- ブロック [`00beeca8`](#insn-00beeca8) 範囲 `[['00beeca8', '00beecbf']]`
  - `CONDITIONAL_JUMP` [`00beecbc`](#insn-00beecbc) → [`00beece0`](#insn-00beece0)
  - `FALL_THROUGH` [`00beecbc`](#insn-00beecbc) → [`00beecc0`](#insn-00beecc0)
- ブロック [`00beecc0`](#insn-00beecc0) 範囲 `[['00beecc0', '00beecd7']]`
  - `CONDITIONAL_JUMP` [`00beecd4`](#insn-00beecd4) → [`00beece0`](#insn-00beece0)
  - `FALL_THROUGH` [`00beecd4`](#insn-00beecd4) → [`00beecd8`](#insn-00beecd8)
- ブロック [`00beecd8`](#insn-00beecd8) 範囲 `[['00beecd8', '00beecdf']]`
  - `FALL_THROUGH` [`00beecdc`](#insn-00beecdc) → [`00beece0`](#insn-00beece0)
- ブロック [`00beece0`](#insn-00beece0) 範囲 `[['00beece0', '00beece3']]`

## 命令位置別の参照

- [`00beebd0`](#insn-00beebd0) → [`00beebe4`](#insn-00beebe4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beebd8`](#insn-00beebd8) → [`00beec14`](#insn-00beec14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beebe0`](#insn-00beebe0) → [`00beec2c`](#insn-00beec2c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beebe8`](#insn-00beebe8) → [`00beec38`](#insn-00beec38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beec00`](#insn-00beec00) → [`00beec3c`](#insn-00beec3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beec10`](#insn-00beec10) → [`00beec3c`](#insn-00beec3c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beec24`](#insn-00beec24) → [`00beec3c`](#insn-00beec3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beec34`](#insn-00beec34) → [`00beec3c`](#insn-00beec3c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beec44`](#insn-00beec44) → [`00beec80`](#insn-00beec80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beec5c`](#insn-00beec5c) → [`00beec80`](#insn-00beec80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beec74`](#insn-00beec74) → [`00beec80`](#insn-00beec80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beec8c`](#insn-00beec8c) → [`00beece0`](#insn-00beece0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beeca4`](#insn-00beeca4) → [`00beece0`](#insn-00beece0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beecbc`](#insn-00beecbc) → [`00beece0`](#insn-00beece0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beecd4`](#insn-00beecd4) → [`00beece0`](#insn-00beece0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00beebd0`](#insn-00beebd0)

~~~json
{
  "source": "00beebd0",
  "target": "00beebe4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beebd8`](#insn-00beebd8)

~~~json
{
  "source": "00beebd8",
  "target": "00beec14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beebe0`](#insn-00beebe0)

~~~json
{
  "source": "00beebe0",
  "target": "00beec2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beebe8`](#insn-00beebe8)

~~~json
{
  "source": "00beebe8",
  "target": "00beec38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beec00`](#insn-00beec00)

~~~json
{
  "source": "00beec00",
  "target": "00beec3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beec10`](#insn-00beec10)

~~~json
{
  "source": "00beec10",
  "target": "00beec3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beec24`](#insn-00beec24)

~~~json
{
  "source": "00beec24",
  "target": "00beec3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beec34`](#insn-00beec34)

~~~json
{
  "source": "00beec34",
  "target": "00beec3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beec44`](#insn-00beec44)

~~~json
{
  "source": "00beec44",
  "target": "00beec80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beec5c`](#insn-00beec5c)

~~~json
{
  "source": "00beec5c",
  "target": "00beec80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beec74`](#insn-00beec74)

~~~json
{
  "source": "00beec74",
  "target": "00beec80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beec8c`](#insn-00beec8c)

~~~json
{
  "source": "00beec8c",
  "target": "00beece0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beeca4`](#insn-00beeca4)

~~~json
{
  "source": "00beeca4",
  "target": "00beece0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beecbc`](#insn-00beecbc)

~~~json
{
  "source": "00beecbc",
  "target": "00beece0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beecd4`](#insn-00beecd4)

~~~json
{
  "source": "00beecd4",
  "target": "00beece0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
