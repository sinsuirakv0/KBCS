# 00a3abdc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00a39be8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a39/00a39be8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0026.md#compare-c536f1e056277a4749a2a0e532c3fd01)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00a3abdc",
  "name": "FUN_00a3abdc",
  "size": 168,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "471eb7a49fc555a6caafbff2d89c09bcc9310a1576dec1ae428c944f7bdf094e",
  "source_text_sha256": "471eb7a49fc555a6caafbff2d89c09bcc9310a1576dec1ae428c944f7bdf094e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00a3abdc",
        "00a3ac83"
      ]
    ],
    "bytes_sha256": "a183a418fc62cda93847f975c196a9a3d90708f3203f4c3fb0c9d3ac67a5b751",
    "instruction_count": 42,
    "instruction_bytes": 168,
    "body_bytes": 168,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00a3aa18](../00a3a/00a3aa18.md)

## 呼び出し先

- [00c58f50](../00c58/00c58f50.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1106 bytes

~~~c

void FUN_00a3abdc(undefined8 param_1,long param_2,long param_3)

{
  void *pvVar1;
  void *pvVar2;
  void *pvVar3;
  
  for (; param_2 != param_3; param_2 = param_2 + 0x80) {
    pvVar1 = *(void **)(param_2 + 0x60);
    if (pvVar1 != (void *)0x0) {
      *(void **)(param_2 + 0x68) = pvVar1;
      _ZdlPv(pvVar1);
    }
    pvVar1 = *(void **)(param_2 + 0x38);
    if (pvVar1 != (void *)0x0) {
      pvVar3 = *(void **)(param_2 + 0x40);
      pvVar2 = pvVar1;
      if (pvVar3 != pvVar1) {
        do {
          pvVar2 = *(void **)((long)pvVar3 + -0x18);
          if (pvVar2 != (void *)0x0) {
            *(void **)((long)pvVar3 + -0x10) = pvVar2;
            _ZdlPv(pvVar2);
          }
          pvVar2 = *(void **)((long)pvVar3 + -0x30);
          if (pvVar2 != (void *)0x0) {
            *(void **)((long)pvVar3 + -0x28) = pvVar2;
            _ZdlPv(pvVar2);
          }
          pvVar3 = (void *)((long)pvVar3 + -0x88);
        } while (pvVar3 != pvVar1);
        pvVar2 = *(void **)(param_2 + 0x38);
      }
      *(void **)(param_2 + 0x40) = pvVar1;
      _ZdlPv(pvVar2);
    }
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00a3abdc"></a> `00a3abdc` | `3f 00 02 eb` | cmp x1,x2 | `FALL_THROUGH`
<a id="insn-00a3abe0"></a> `00a3abe0` | `00 05 00 54` | b.eq 0x00a3ac80 | `CONDITIONAL_JUMP`
<a id="insn-00a3abe4"></a> `00a3abe4` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00a3abe8"></a> `00a3abe8` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a3abec"></a> `00a3abec` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00a3abf0"></a> `00a3abf0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00a3abf4"></a> `00a3abf4` | `f3 03 02 aa` | mov x19,x2 | `FALL_THROUGH`
<a id="insn-00a3abf8"></a> `00a3abf8` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00a3abfc"></a> `00a3abfc` | `07 00 00 14` | b 0x00a3ac18 | `UNCONDITIONAL_JUMP`
<a id="insn-00a3ac00"></a> `00a3ac00` | `80 1e 40 f9` | ldr x0,[x20, #0x38] | `FALL_THROUGH`
<a id="insn-00a3ac04"></a> `00a3ac04` | `95 22 00 f9` | str x21,[x20, #0x40] | `FALL_THROUGH`
<a id="insn-00a3ac08"></a> `00a3ac08` | `d2 78 08 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00a3ac0c"></a> `00a3ac0c` | `94 02 02 91` | add x20,x20,#0x80 | `FALL_THROUGH`
<a id="insn-00a3ac10"></a> `00a3ac10` | `9f 02 13 eb` | cmp x20,x19 | `FALL_THROUGH`
<a id="insn-00a3ac14"></a> `00a3ac14` | `00 03 00 54` | b.eq 0x00a3ac74 | `CONDITIONAL_JUMP`
<a id="insn-00a3ac18"></a> `00a3ac18` | `80 32 40 f9` | ldr x0,[x20, #0x60] | `FALL_THROUGH`
<a id="insn-00a3ac1c"></a> `00a3ac1c` | `60 00 00 b4` | cbz x0,0x00a3ac28 | `CONDITIONAL_JUMP`
<a id="insn-00a3ac20"></a> `00a3ac20` | `80 36 00 f9` | str x0,[x20, #0x68] | `FALL_THROUGH`
<a id="insn-00a3ac24"></a> `00a3ac24` | `cb 78 08 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00a3ac28"></a> `00a3ac28` | `95 1e 40 f9` | ldr x21,[x20, #0x38] | `FALL_THROUGH`
<a id="insn-00a3ac2c"></a> `00a3ac2c` | `15 ff ff b4` | cbz x21,0x00a3ac0c | `CONDITIONAL_JUMP`
<a id="insn-00a3ac30"></a> `00a3ac30` | `96 22 40 f9` | ldr x22,[x20, #0x40] | `FALL_THROUGH`
<a id="insn-00a3ac34"></a> `00a3ac34` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00a3ac38"></a> `00a3ac38` | `df 02 15 eb` | cmp x22,x21 | `FALL_THROUGH`
<a id="insn-00a3ac3c"></a> `00a3ac3c` | `a1 00 00 54` | b.ne 0x00a3ac50 | `CONDITIONAL_JUMP`
<a id="insn-00a3ac40"></a> `00a3ac40` | `f1 ff ff 17` | b 0x00a3ac04 | `UNCONDITIONAL_JUMP`
<a id="insn-00a3ac44"></a> `00a3ac44` | `d6 22 02 d1` | sub x22,x22,#0x88 | `FALL_THROUGH`
<a id="insn-00a3ac48"></a> `00a3ac48` | `df 02 15 eb` | cmp x22,x21 | `FALL_THROUGH`
<a id="insn-00a3ac4c"></a> `00a3ac4c` | `a0 fd ff 54` | b.eq 0x00a3ac00 | `CONDITIONAL_JUMP`
<a id="insn-00a3ac50"></a> `00a3ac50` | `c0 82 5e f8` | ldur x0,[x22, #-0x18] | `FALL_THROUGH`
<a id="insn-00a3ac54"></a> `00a3ac54` | `60 00 00 b4` | cbz x0,0x00a3ac60 | `CONDITIONAL_JUMP`
<a id="insn-00a3ac58"></a> `00a3ac58` | `c0 02 1f f8` | stur x0,[x22, #-0x10] | `FALL_THROUGH`
<a id="insn-00a3ac5c"></a> `00a3ac5c` | `bd 78 08 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00a3ac60"></a> `00a3ac60` | `c0 02 5d f8` | ldur x0,[x22, #-0x30] | `FALL_THROUGH`
<a id="insn-00a3ac64"></a> `00a3ac64` | `00 ff ff b4` | cbz x0,0x00a3ac44 | `CONDITIONAL_JUMP`
<a id="insn-00a3ac68"></a> `00a3ac68` | `c0 82 1d f8` | stur x0,[x22, #-0x28] | `FALL_THROUGH`
<a id="insn-00a3ac6c"></a> `00a3ac6c` | `b9 78 08 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00a3ac70"></a> `00a3ac70` | `f5 ff ff 17` | b 0x00a3ac44 | `UNCONDITIONAL_JUMP`
<a id="insn-00a3ac74"></a> `00a3ac74` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00a3ac78"></a> `00a3ac78` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a3ac7c"></a> `00a3ac7c` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00a3ac80"></a> `00a3ac80` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00a3abdc`](#insn-00a3abdc) 範囲 `[['00a3abdc', '00a3abe3']]`
  - `CONDITIONAL_JUMP` [`00a3abe0`](#insn-00a3abe0) → [`00a3ac80`](#insn-00a3ac80)
  - `FALL_THROUGH` [`00a3abe0`](#insn-00a3abe0) → [`00a3abe4`](#insn-00a3abe4)
- ブロック [`00a3abe4`](#insn-00a3abe4) 範囲 `[['00a3abe4', '00a3abff']]`
  - `UNCONDITIONAL_JUMP` [`00a3abfc`](#insn-00a3abfc) → [`00a3ac18`](#insn-00a3ac18)
- ブロック [`00a3ac00`](#insn-00a3ac00) 範囲 `[['00a3ac00', '00a3ac03']]`
  - `FALL_THROUGH` [`00a3ac00`](#insn-00a3ac00) → [`00a3ac04`](#insn-00a3ac04)
- ブロック [`00a3ac04`](#insn-00a3ac04) 範囲 `[['00a3ac04', '00a3ac0b']]`
  - `FALL_THROUGH` [`00a3ac08`](#insn-00a3ac08) → [`00a3ac0c`](#insn-00a3ac0c)
- ブロック [`00a3ac0c`](#insn-00a3ac0c) 範囲 `[['00a3ac0c', '00a3ac17']]`
  - `CONDITIONAL_JUMP` [`00a3ac14`](#insn-00a3ac14) → [`00a3ac74`](#insn-00a3ac74)
  - `FALL_THROUGH` [`00a3ac14`](#insn-00a3ac14) → [`00a3ac18`](#insn-00a3ac18)
- ブロック [`00a3ac18`](#insn-00a3ac18) 範囲 `[['00a3ac18', '00a3ac1f']]`
  - `CONDITIONAL_JUMP` [`00a3ac1c`](#insn-00a3ac1c) → [`00a3ac28`](#insn-00a3ac28)
  - `FALL_THROUGH` [`00a3ac1c`](#insn-00a3ac1c) → [`00a3ac20`](#insn-00a3ac20)
- ブロック [`00a3ac20`](#insn-00a3ac20) 範囲 `[['00a3ac20', '00a3ac27']]`
  - `FALL_THROUGH` [`00a3ac24`](#insn-00a3ac24) → [`00a3ac28`](#insn-00a3ac28)
- ブロック [`00a3ac28`](#insn-00a3ac28) 範囲 `[['00a3ac28', '00a3ac2f']]`
  - `CONDITIONAL_JUMP` [`00a3ac2c`](#insn-00a3ac2c) → [`00a3ac0c`](#insn-00a3ac0c)
  - `FALL_THROUGH` [`00a3ac2c`](#insn-00a3ac2c) → [`00a3ac30`](#insn-00a3ac30)
- ブロック [`00a3ac30`](#insn-00a3ac30) 範囲 `[['00a3ac30', '00a3ac3f']]`
  - `CONDITIONAL_JUMP` [`00a3ac3c`](#insn-00a3ac3c) → [`00a3ac50`](#insn-00a3ac50)
  - `FALL_THROUGH` [`00a3ac3c`](#insn-00a3ac3c) → [`00a3ac40`](#insn-00a3ac40)
- ブロック [`00a3ac40`](#insn-00a3ac40) 範囲 `[['00a3ac40', '00a3ac43']]`
  - `UNCONDITIONAL_JUMP` [`00a3ac40`](#insn-00a3ac40) → [`00a3ac04`](#insn-00a3ac04)
- ブロック [`00a3ac44`](#insn-00a3ac44) 範囲 `[['00a3ac44', '00a3ac4f']]`
  - `CONDITIONAL_JUMP` [`00a3ac4c`](#insn-00a3ac4c) → [`00a3ac00`](#insn-00a3ac00)
  - `FALL_THROUGH` [`00a3ac4c`](#insn-00a3ac4c) → [`00a3ac50`](#insn-00a3ac50)
- ブロック [`00a3ac50`](#insn-00a3ac50) 範囲 `[['00a3ac50', '00a3ac57']]`
  - `CONDITIONAL_JUMP` [`00a3ac54`](#insn-00a3ac54) → [`00a3ac60`](#insn-00a3ac60)
  - `FALL_THROUGH` [`00a3ac54`](#insn-00a3ac54) → [`00a3ac58`](#insn-00a3ac58)
- ブロック [`00a3ac58`](#insn-00a3ac58) 範囲 `[['00a3ac58', '00a3ac5f']]`
  - `FALL_THROUGH` [`00a3ac5c`](#insn-00a3ac5c) → [`00a3ac60`](#insn-00a3ac60)
- ブロック [`00a3ac60`](#insn-00a3ac60) 範囲 `[['00a3ac60', '00a3ac67']]`
  - `CONDITIONAL_JUMP` [`00a3ac64`](#insn-00a3ac64) → [`00a3ac44`](#insn-00a3ac44)
  - `FALL_THROUGH` [`00a3ac64`](#insn-00a3ac64) → [`00a3ac68`](#insn-00a3ac68)
- ブロック [`00a3ac68`](#insn-00a3ac68) 範囲 `[['00a3ac68', '00a3ac73']]`
  - `UNCONDITIONAL_JUMP` [`00a3ac70`](#insn-00a3ac70) → [`00a3ac44`](#insn-00a3ac44)
- ブロック [`00a3ac74`](#insn-00a3ac74) 範囲 `[['00a3ac74', '00a3ac7f']]`
  - `FALL_THROUGH` [`00a3ac7c`](#insn-00a3ac7c) → [`00a3ac80`](#insn-00a3ac80)
- ブロック [`00a3ac80`](#insn-00a3ac80) 範囲 `[['00a3ac80', '00a3ac83']]`

## 命令位置別の参照

- [`00a3abe0`](#insn-00a3abe0) → [`00a3ac80`](#insn-00a3ac80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3abe4`](#insn-00a3abe4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3abe8`](#insn-00a3abe8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3abec`](#insn-00a3abec) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3abfc`](#insn-00a3abfc) → [`00a3ac18`](#insn-00a3ac18) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3ac08`](#insn-00a3ac08) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00a3ac14`](#insn-00a3ac14) → [`00a3ac74`](#insn-00a3ac74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3ac1c`](#insn-00a3ac1c) → [`00a3ac28`](#insn-00a3ac28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3ac24`](#insn-00a3ac24) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00a3ac2c`](#insn-00a3ac2c) → [`00a3ac0c`](#insn-00a3ac0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3ac3c`](#insn-00a3ac3c) → [`00a3ac50`](#insn-00a3ac50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3ac40`](#insn-00a3ac40) → [`00a3ac04`](#insn-00a3ac04) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3ac4c`](#insn-00a3ac4c) → [`00a3ac00`](#insn-00a3ac00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3ac54`](#insn-00a3ac54) → [`00a3ac60`](#insn-00a3ac60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3ac5c`](#insn-00a3ac5c) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00a3ac64`](#insn-00a3ac64) → [`00a3ac44`](#insn-00a3ac44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3ac6c`](#insn-00a3ac6c) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00a3ac70`](#insn-00a3ac70) → [`00a3ac44`](#insn-00a3ac44) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3ac74`](#insn-00a3ac74) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3ac78`](#insn-00a3ac78) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3ac7c`](#insn-00a3ac7c) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00a3abe0`](#insn-00a3abe0)

~~~json
{
  "source": "00a3abe0",
  "target": "00a3ac80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3abe4`](#insn-00a3abe4)

~~~json
{
  "source": "00a3abe4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3abe8`](#insn-00a3abe8)

~~~json
{
  "source": "00a3abe8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3abec`](#insn-00a3abec)

~~~json
{
  "source": "00a3abec",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3abfc`](#insn-00a3abfc)

~~~json
{
  "source": "00a3abfc",
  "target": "00a3ac18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3ac08`](#insn-00a3ac08)

~~~json
{
  "source": "00a3ac08",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3ac14`](#insn-00a3ac14)

~~~json
{
  "source": "00a3ac14",
  "target": "00a3ac74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3ac1c`](#insn-00a3ac1c)

~~~json
{
  "source": "00a3ac1c",
  "target": "00a3ac28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3ac24`](#insn-00a3ac24)

~~~json
{
  "source": "00a3ac24",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3ac2c`](#insn-00a3ac2c)

~~~json
{
  "source": "00a3ac2c",
  "target": "00a3ac0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3ac3c`](#insn-00a3ac3c)

~~~json
{
  "source": "00a3ac3c",
  "target": "00a3ac50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3ac40`](#insn-00a3ac40)

~~~json
{
  "source": "00a3ac40",
  "target": "00a3ac04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3ac4c`](#insn-00a3ac4c)

~~~json
{
  "source": "00a3ac4c",
  "target": "00a3ac00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3ac54`](#insn-00a3ac54)

~~~json
{
  "source": "00a3ac54",
  "target": "00a3ac60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3ac5c`](#insn-00a3ac5c)

~~~json
{
  "source": "00a3ac5c",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3ac64`](#insn-00a3ac64)

~~~json
{
  "source": "00a3ac64",
  "target": "00a3ac44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3ac6c`](#insn-00a3ac6c)

~~~json
{
  "source": "00a3ac6c",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3ac70`](#insn-00a3ac70)

~~~json
{
  "source": "00a3ac70",
  "target": "00a3ac44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3ac74`](#insn-00a3ac74)

~~~json
{
  "source": "00a3ac74",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3ac78`](#insn-00a3ac78)

~~~json
{
  "source": "00a3ac78",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3ac7c`](#insn-00a3ac7c)

~~~json
{
  "source": "00a3ac7c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
