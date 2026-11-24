# 00afcfe4

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00afcf48`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afc/00afcf48.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0036.md#compare-aca541b8721ac23deac61cd15c5dbcac)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00afdfd8`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00afd/00afdfd8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0029.md#compare-12cb23c5405abc370b8445c4fed03614)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afcfe4",
  "name": "FUN_00afcfe4",
  "size": 104,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e6deece89a109367fa955d8d4c833ea215c00f6308dad03b0b4ce200b7e249fa",
  "source_text_sha256": "e6deece89a109367fa955d8d4c833ea215c00f6308dad03b0b4ce200b7e249fa",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afcfe4",
        "00afd04b"
      ]
    ],
    "bytes_sha256": "96ba723c58c46562af1e5cb95d9313324910054c2a59cde6de7bd0b05248b71b",
    "instruction_count": 26,
    "instruction_bytes": 104,
    "body_bytes": 104,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00700b50](../00700/00700b50.md)

## 呼び出し先

- [005e7460](../005e7/005e7460.md)
- [00851550](../00851/00851550.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 395 bytes

~~~c

undefined4 FUN_00afcfe4(int param_1,int param_2)

{
  undefined4 uVar1;
  long lVar2;
  ulong uVar3;
  
  lVar2 = FUN_00851550();
  uVar3 = FUN_005e7460(lVar2 + (long)param_1 * 0x1f0 + 0x2768);
  if ((uVar3 & 1) == 0) {
    lVar2 = FUN_00851550();
    uVar1 = *(undefined4 *)(lVar2 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84a4c);
  }
  else {
    uVar1 = 0;
  }
  return uVar1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afcfe4"></a> `00afcfe4` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00afcfe8"></a> `00afcfe8` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afcfec"></a> `00afcfec` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00afcff0"></a> `00afcff0` | `f3 03 01 2a` | mov w19,w1 | `FALL_THROUGH`
<a id="insn-00afcff4"></a> `00afcff4` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00afcff8"></a> `00afcff8` | `56 51 f5 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-00afcffc"></a> `00afcffc` | `08 3e 80 52` | mov w8,#0x1f0 | `FALL_THROUGH`
<a id="insn-00afd000"></a> `00afd000` | `09 ed 84 52` | mov w9,#0x2768 | `FALL_THROUGH`
<a id="insn-00afd004"></a> `00afd004` | `88 02 28 9b` | smaddl x8,w20,w8,x0 | `FALL_THROUGH`
<a id="insn-00afd008"></a> `00afd008` | `00 01 09 8b` | add x0,x8,x9 | `FALL_THROUGH`
<a id="insn-00afd00c"></a> `00afd00c` | `15 a9 eb 97` | bl 0x005e7460 | `UNCONDITIONAL_CALL`
<a id="insn-00afd010"></a> `00afd010` | `60 01 00 37` | tbnz w0,#0x0,0x00afd03c | `CONDITIONAL_JUMP`
<a id="insn-00afd014"></a> `00afd014` | `94 7e 40 93` | sxtw x20,w20 | `FALL_THROUGH`
<a id="insn-00afd018"></a> `00afd018` | `4e 51 f5 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-00afd01c"></a> `00afd01c` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00afd020"></a> `00afd020` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00afd024"></a> `00afd024` | `88 02 28 9b` | smaddl x8,w20,w8,x0 | `FALL_THROUGH`
<a id="insn-00afd028"></a> `00afd028` | `68 22 29 9b` | smaddl x8,w19,w9,x8 | `FALL_THROUGH`
<a id="insn-00afd02c"></a> `00afd02c` | `89 49 89 52` | mov w9,#0x4a4c | `FALL_THROUGH`
<a id="insn-00afd030"></a> `00afd030` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00afd034"></a> `00afd034` | `00 69 69 b8` | ldr w0,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afd038"></a> `00afd038` | `02 00 00 14` | b 0x00afd040 | `UNCONDITIONAL_JUMP`
<a id="insn-00afd03c"></a> `00afd03c` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00afd040"></a> `00afd040` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afd044"></a> `00afd044` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00afd048"></a> `00afd048` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afcfe4`](#insn-00afcfe4) 範囲 `[['00afcfe4', '00afd013']]`
  - `CONDITIONAL_JUMP` [`00afd010`](#insn-00afd010) → [`00afd03c`](#insn-00afd03c)
  - `FALL_THROUGH` [`00afd010`](#insn-00afd010) → [`00afd014`](#insn-00afd014)
- ブロック [`00afd014`](#insn-00afd014) 範囲 `[['00afd014', '00afd03b']]`
  - `UNCONDITIONAL_JUMP` [`00afd038`](#insn-00afd038) → [`00afd040`](#insn-00afd040)
- ブロック [`00afd03c`](#insn-00afd03c) 範囲 `[['00afd03c', '00afd03f']]`
  - `FALL_THROUGH` [`00afd03c`](#insn-00afd03c) → [`00afd040`](#insn-00afd040)
- ブロック [`00afd040`](#insn-00afd040) 範囲 `[['00afd040', '00afd04b']]`

## 命令位置別の参照

- [`00afcfe4`](#insn-00afcfe4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcfe8`](#insn-00afcfe8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcff8`](#insn-00afcff8) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`00afd00c`](#insn-00afd00c) → [`005e7460`](../005e7/005e7460.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005e7460` · 推定シンボル `None` · 推定型 `None`
- [`00afd010`](#insn-00afd010) → [`00afd03c`](#insn-00afd03c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afd018`](#insn-00afd018) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`00afd038`](#insn-00afd038) → [`00afd040`](#insn-00afd040) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afd040`](#insn-00afd040) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afd044`](#insn-00afd044) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afcfe4`](#insn-00afcfe4)

~~~json
{
  "source": "00afcfe4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcfe8`](#insn-00afcfe8)

~~~json
{
  "source": "00afcfe8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcff8`](#insn-00afcff8)

~~~json
{
  "source": "00afcff8",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afd00c`](#insn-00afd00c)

~~~json
{
  "source": "00afd00c",
  "target": "005e7460",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afd010`](#insn-00afd010)

~~~json
{
  "source": "00afd010",
  "target": "00afd03c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afd018`](#insn-00afd018)

~~~json
{
  "source": "00afd018",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afd038`](#insn-00afd038)

~~~json
{
  "source": "00afd038",
  "target": "00afd040",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afd040`](#insn-00afd040)

~~~json
{
  "source": "00afd040",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afd044`](#insn-00afd044)

~~~json
{
  "source": "00afd044",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
