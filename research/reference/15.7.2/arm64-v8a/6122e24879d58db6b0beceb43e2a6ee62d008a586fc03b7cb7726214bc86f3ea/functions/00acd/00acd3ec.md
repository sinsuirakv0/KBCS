# 00acd3ec

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00acd4b4`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acd4b4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0056.md#compare-deeaced18cc7445518e5bf051a6fc7df)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acd3ec",
  "name": "FUN_00acd3ec",
  "size": 36,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8428d688fe9b6ccb838a30d2791b52510484d6e74a97ca9f799837a8a7e427b2",
  "source_text_sha256": "8428d688fe9b6ccb838a30d2791b52510484d6e74a97ca9f799837a8a7e427b2",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00acd3ec",
        "00acd40f"
      ]
    ],
    "bytes_sha256": "9feae63817d4c0c85b1e64f56c891db3dc3ee1a5d7541b4b739236061ddd4c4a",
    "instruction_count": 9,
    "instruction_bytes": 36,
    "body_bytes": 36,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdaf40](../00bda/00bdaf40.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 135 bytes

~~~c

void FUN_00acd3ec(void)

{
  undefined8 *puVar1;
  
  puVar1 = (undefined8 *)_Znwm(0x10);
  *puVar1 = &PTR_FUN_00c0f648;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00acd3ec"></a> `00acd3ec` | `fd 7b bf a9` | stp x29,x30,[sp, #-0x10]! | `FALL_THROUGH`
<a id="insn-00acd3f0"></a> `00acd3f0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00acd3f4"></a> `00acd3f4` | `00 02 80 52` | mov w0,#0x10 | `FALL_THROUGH`
<a id="insn-00acd3f8"></a> `00acd3f8` | `d2 36 04 94` | bl 0x00bdaf40 | `UNCONDITIONAL_CALL`
<a id="insn-00acd3fc"></a> `00acd3fc` | `08 0a 00 d0` | adrp x8,0xc0f000 | `FALL_THROUGH`
<a id="insn-00acd400"></a> `00acd400` | `08 21 19 91` | add x8,x8,#0x648 | `FALL_THROUGH`
<a id="insn-00acd404"></a> `00acd404` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-00acd408"></a> `00acd408` | `fd 7b c1 a8` | ldp x29,x30,[sp], #0x10 | `FALL_THROUGH`
<a id="insn-00acd40c"></a> `00acd40c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00acd3ec`](#insn-00acd3ec) 範囲 `[['00acd3ec', '00acd40f']]`

## 命令位置別の参照

- [`00acd3ec`](#insn-00acd3ec) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acd3f8`](#insn-00acd3f8) → [`00bdaf40`](../00bda/00bdaf40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf40` · 推定シンボル `None` · 推定型 `None`
- [`00acd404`](#insn-00acd404) → `00c0f648`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00acd408`](#insn-00acd408) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00acd3ec`](#insn-00acd3ec)

~~~json
{
  "source": "00acd3ec",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acd3f8`](#insn-00acd3f8)

~~~json
{
  "source": "00acd3f8",
  "target": "00bdaf40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acd404`](#insn-00acd404)

~~~json
{
  "source": "00acd404",
  "target": "00c0f648",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c0f648",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00acd408`](#insn-00acd408)

~~~json
{
  "source": "00acd408",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
