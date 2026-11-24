# 00bfac7c

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bfa854`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa854.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0041.md#compare-34f227b980e42878892784c9e6e3e88d)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bfad18`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfad18.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0041.md#compare-4d3e5eb3e8839b77c8553f759854bd82)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfac7c",
  "name": "FUN_00bfac7c",
  "size": 56,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "63193a515845a80aa2671131870c97eed581f9440fa308e67de54f5e28ab3d4e",
  "source_text_sha256": "63193a515845a80aa2671131870c97eed581f9440fa308e67de54f5e28ab3d4e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfac7c",
        "00bfacb3"
      ]
    ],
    "bytes_sha256": "f1c0c54f5f90384225c7d8fe8fb4d2b287f39f5abe4e448f2621a838492b190a",
    "instruction_count": 14,
    "instruction_bytes": 56,
    "body_bytes": 56,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57eb0](../00c57/00c57eb0.md)
- [00c58150](../00c58/00c58150.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 160 bytes

~~~c

void FUN_00bfac7c(void *param_1)

{
  if (param_1 != (void *)0x0) {
    _ZNSt6__ndk115__thread_structD1Ev();
    _ZdlPv(param_1);
    return;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfac7c"></a> `00bfac7c` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bfac80"></a> `00bfac80` | `80 01 00 b4` | cbz x0,0x00bfacb0 | `CONDITIONAL_JUMP`
<a id="insn-00bfac84"></a> `00bfac84` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfac88"></a> `00bfac88` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bfac8c"></a> `00bfac8c` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfac90"></a> `00bfac90` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bfac94"></a> `00bfac94` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bfac98"></a> `00bfac98` | `2e 75 01 94` | bl 0x00c58150 | `UNCONDITIONAL_CALL`
<a id="insn-00bfac9c"></a> `00bfac9c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bfaca0"></a> `00bfaca0` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfaca4"></a> `00bfaca4` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bfaca8"></a> `00bfaca8` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfacac"></a> `00bfacac` | `81 74 01 14` | b 0x00c57eb0 | `CALL_TERMINATOR`
<a id="insn-00bfacb0"></a> `00bfacb0` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfac7c`](#insn-00bfac7c) 範囲 `[['00bfac7c', '00bfac83']]`
  - `CONDITIONAL_JUMP` [`00bfac80`](#insn-00bfac80) → [`00bfacb0`](#insn-00bfacb0)
  - `FALL_THROUGH` [`00bfac80`](#insn-00bfac80) → [`00bfac84`](#insn-00bfac84)
- ブロック [`00bfac84`](#insn-00bfac84) 範囲 `[['00bfac84', '00bfacaf']]`
- ブロック [`00bfacb0`](#insn-00bfacb0) 範囲 `[['00bfacb0', '00bfacb3']]`

## 命令位置別の参照

- [`00bfac80`](#insn-00bfac80) → [`00bfacb0`](#insn-00bfacb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfac88`](#insn-00bfac88) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfac8c`](#insn-00bfac8c) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfac98`](#insn-00bfac98) → [`00c58150`](../00c58/00c58150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58150` · 推定シンボル `None` · 推定型 `None`
- [`00bfaca0`](#insn-00bfaca0) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfaca4`](#insn-00bfaca4) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfacac`](#insn-00bfacac) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfac80`](#insn-00bfac80)

~~~json
{
  "source": "00bfac80",
  "target": "00bfacb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfac88`](#insn-00bfac88)

~~~json
{
  "source": "00bfac88",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfac8c`](#insn-00bfac8c)

~~~json
{
  "source": "00bfac8c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfac98`](#insn-00bfac98)

~~~json
{
  "source": "00bfac98",
  "target": "00c58150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfaca0`](#insn-00bfaca0)

~~~json
{
  "source": "00bfaca0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfaca4`](#insn-00bfaca4)

~~~json
{
  "source": "00bfaca4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfacac`](#insn-00bfacac)

~~~json
{
  "source": "00bfacac",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
