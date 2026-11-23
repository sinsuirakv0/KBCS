# 00bdeea0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdef50`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef50.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0019.md#compare-9e6a432fec408d11ced8e2be669d28a6)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdeea0",
  "name": "_Znam",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0934e8b1049e253d4e62af86cadc955e1c4efc6e57ced26569ab6b8a59c83eee",
  "source_text_sha256": "0934e8b1049e253d4e62af86cadc955e1c4efc6e57ced26569ab6b8a59c83eee",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdeea0",
        "00bdeeaf"
      ]
    ],
    "bytes_sha256": "48a708551db30d529964ddefe43ce6660a7af98e53f273b764ff33f92eb85619",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00b034b4](../00b03/00b034b4.md)
- [00b2e528](../00b2e/00b2e528.md)
- [00b47b50](../00b47/00b47b50.md)
- [00b47c40](../00b47/00b47c40.md)
- [00b5732c](../00b57/00b5732c.md)
- [00b58fa4](../00b58/00b58fa4.md)
- [00bd4dd4](../00bd4/00bd4dd4.md)

## 呼び出し先

- [00bdae08](../00bda/00bdae08.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 69 bytes

~~~c

void _Znam(void)

{
  (*(code *)PTR__Znam_00c1df88)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdeea0"></a> `00bdeea0` | `f0 01 00 f0` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bdeea4"></a> `00bdeea4` | `11 c6 47 f9` | ldr x17,[x16, #0xf88] | `FALL_THROUGH`
<a id="insn-00bdeea8"></a> `00bdeea8` | `10 22 3e 91` | add x16,x16,#0xf88 | `FALL_THROUGH`
<a id="insn-00bdeeac"></a> `00bdeeac` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdeea0`](#insn-00bdeea0) 範囲 `[['00bdeea0', '00bdeeaf']]`

## 命令位置別の参照

- [`00bdeea4`](#insn-00bdeea4) → `00c1df88`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdeeac`](#insn-00bdeeac) → [`00bdae08`](../00bda/00bdae08.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00bdae08` · 推定シンボル `_Znam` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdeea4`](#insn-00bdeea4)

~~~json
{
  "source": "00bdeea4",
  "target": "00c1df88",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1df88",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdeeac`](#insn-00bdeeac)

~~~json
{
  "source": "00bdeeac",
  "target": "00bdae08",
  "target_space": "ram",
  "resolution": "function"
}
~~~
