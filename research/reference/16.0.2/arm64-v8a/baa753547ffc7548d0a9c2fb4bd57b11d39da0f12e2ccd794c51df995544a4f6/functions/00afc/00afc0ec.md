# 00afc0ec

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00afc050`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afc/00afc050.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/alignment_unresolved-0007.md#compare-299875489e14212c242566248efe2810)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00afd0e0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00afd/00afd0e0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/alignment_unresolved-0013.md#compare-25a6720e15e60d562f87343f80d6d3f6)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afc0ec",
  "name": "FUN_00afc0ec",
  "size": 100,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f09bcdb535ae0ef8f847b593e03a53678e10f48b14fbe32e8e9ecf79ba78e429",
  "source_text_sha256": "f09bcdb535ae0ef8f847b593e03a53678e10f48b14fbe32e8e9ecf79ba78e429",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afc0ec",
        "00afc14f"
      ]
    ],
    "bytes_sha256": "ed514fdfdff4721e5a9ab804596dc270f7fc6dc4eadd0199eac6285f7903d9d3",
    "instruction_count": 25,
    "instruction_bytes": 100,
    "body_bytes": 100,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00710330](../00710/00710330.md)
- [00711a48](../00711/00711a48.md)

## 呼び出し先

- [00851550](../00851/00851550.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 307 bytes

~~~c

void FUN_00afc0ec(int param_1,int param_2)

{
  long lVar1;
  
  lVar1 = FUN_00851550();
  *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84a5c) = 0;
  lVar1 = FUN_00851550();
  *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84a60) = 1;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afc0ec"></a> `00afc0ec` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00afc0f0"></a> `00afc0f0` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afc0f4"></a> `00afc0f4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afc0f8"></a> `00afc0f8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00afc0fc"></a> `00afc0fc` | `f3 03 01 2a` | mov w19,w1 | `FALL_THROUGH`
<a id="insn-00afc100"></a> `00afc100` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00afc104"></a> `00afc104` | `13 55 f5 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-00afc108"></a> `00afc108` | `95 00 99 52` | mov w21,#0xc804 | `FALL_THROUGH`
<a id="insn-00afc10c"></a> `00afc10c` | `96 7d 80 52` | mov w22,#0x3ec | `FALL_THROUGH`
<a id="insn-00afc110"></a> `00afc110` | `89 4b 89 52` | mov w9,#0x4a5c | `FALL_THROUGH`
<a id="insn-00afc114"></a> `00afc114` | `88 02 35 9b` | smaddl x8,w20,w21,x0 | `FALL_THROUGH`
<a id="insn-00afc118"></a> `00afc118` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00afc11c"></a> `00afc11c` | `68 22 36 9b` | smaddl x8,w19,w22,x8 | `FALL_THROUGH`
<a id="insn-00afc120"></a> `00afc120` | `1f 69 29 b8` | str wzr,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afc124"></a> `00afc124` | `0b 55 f5 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-00afc128"></a> `00afc128` | `88 02 35 9b` | smaddl x8,w20,w21,x0 | `FALL_THROUGH`
<a id="insn-00afc12c"></a> `00afc12c` | `09 4c 89 52` | mov w9,#0x4a60 | `FALL_THROUGH`
<a id="insn-00afc130"></a> `00afc130` | `2a 00 80 52` | mov w10,#0x1 | `FALL_THROUGH`
<a id="insn-00afc134"></a> `00afc134` | `68 22 36 9b` | smaddl x8,w19,w22,x8 | `FALL_THROUGH`
<a id="insn-00afc138"></a> `00afc138` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00afc13c"></a> `00afc13c` | `0a 69 29 b8` | str w10,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afc140"></a> `00afc140` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afc144"></a> `00afc144` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afc148"></a> `00afc148` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00afc14c"></a> `00afc14c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afc0ec`](#insn-00afc0ec) 範囲 `[['00afc0ec', '00afc14f']]`

## 命令位置別の参照

- [`00afc0ec`](#insn-00afc0ec) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afc0f0`](#insn-00afc0f0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afc0f4`](#insn-00afc0f4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afc104`](#insn-00afc104) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`00afc124`](#insn-00afc124) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`00afc140`](#insn-00afc140) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afc144`](#insn-00afc144) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afc148`](#insn-00afc148) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afc0ec`](#insn-00afc0ec)

~~~json
{
  "source": "00afc0ec",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afc0f0`](#insn-00afc0f0)

~~~json
{
  "source": "00afc0f0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afc0f4`](#insn-00afc0f4)

~~~json
{
  "source": "00afc0f4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afc104`](#insn-00afc104)

~~~json
{
  "source": "00afc104",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afc124`](#insn-00afc124)

~~~json
{
  "source": "00afc124",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afc140`](#insn-00afc140)

~~~json
{
  "source": "00afc140",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afc144`](#insn-00afc144)

~~~json
{
  "source": "00afc144",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afc148`](#insn-00afc148)

~~~json
{
  "source": "00afc148",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
