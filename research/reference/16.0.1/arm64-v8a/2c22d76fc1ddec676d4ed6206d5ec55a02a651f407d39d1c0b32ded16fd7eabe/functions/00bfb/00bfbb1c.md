# 00bfbb1c

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bfb6f4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb6f4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0041.md#compare-4ada2d074ccfd113ff0cb55898681b85)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bfbbb8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfbbb8.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0041.md#compare-5e2ea7d553b29713f1c914b5ba715a71)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfbb1c",
  "name": "FUN_00bfbb1c",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f93a32ab9cd8d6c513085c122397a812c86aaed3d0f0690c4ba1c7aaf5745589",
  "source_text_sha256": "f93a32ab9cd8d6c513085c122397a812c86aaed3d0f0690c4ba1c7aaf5745589",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfbb1c",
        "00bfbb47"
      ]
    ],
    "bytes_sha256": "eac729ef506ead2d55de05317e2920c33e347c28bc2bc41d3355fabad7fb9630",
    "instruction_count": 11,
    "instruction_bytes": 44,
    "body_bytes": 44,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57eb0](../00c57/00c57eb0.md)
- [00c5def0](../00c5d/00c5def0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 107 bytes

~~~c

void FUN_00bfbb1c(void *param_1)

{
  _ZNSt6__ndk114error_categoryD1Ev();
  _ZdlPv(param_1);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfbb1c"></a> `00bfbb1c` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfbb20"></a> `00bfbb20` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bfbb24"></a> `00bfbb24` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfbb28"></a> `00bfbb28` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bfbb2c"></a> `00bfbb2c` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bfbb30"></a> `00bfbb30` | `f0 88 01 94` | bl 0x00c5def0 | `UNCONDITIONAL_CALL`
<a id="insn-00bfbb34"></a> `00bfbb34` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bfbb38"></a> `00bfbb38` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfbb3c"></a> `00bfbb3c` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bfbb40"></a> `00bfbb40` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfbb44"></a> `00bfbb44` | `db 70 01 14` | b 0x00c57eb0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfbb1c`](#insn-00bfbb1c) 範囲 `[['00bfbb1c', '00bfbb47']]`

## 命令位置別の参照

- [`00bfbb20`](#insn-00bfbb20) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbb24`](#insn-00bfbb24) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbb30`](#insn-00bfbb30) → [`00c5def0`](../00c5d/00c5def0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5def0` · 推定シンボル `None` · 推定型 `None`
- [`00bfbb38`](#insn-00bfbb38) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbb3c`](#insn-00bfbb3c) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbb44`](#insn-00bfbb44) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfbb20`](#insn-00bfbb20)

~~~json
{
  "source": "00bfbb20",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbb24`](#insn-00bfbb24)

~~~json
{
  "source": "00bfbb24",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbb30`](#insn-00bfbb30)

~~~json
{
  "source": "00bfbb30",
  "target": "00c5def0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfbb38`](#insn-00bfbb38)

~~~json
{
  "source": "00bfbb38",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbb3c`](#insn-00bfbb3c)

~~~json
{
  "source": "00bfbb3c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbb44`](#insn-00bfbb44)

~~~json
{
  "source": "00bfbb44",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
