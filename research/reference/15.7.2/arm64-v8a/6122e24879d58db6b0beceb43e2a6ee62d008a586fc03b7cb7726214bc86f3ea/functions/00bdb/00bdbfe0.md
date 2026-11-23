# 00bdbfe0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdc090`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc090.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0012.md#compare-3345d5574bdfd22e92cc64e0c4028093)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdbfe0",
  "name": "_ZN5Botan15DataSink_StreamD2Ev",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b44b1a2b2f9a02af0076cf184bd12270b5fe24cc4d1672adff00013f2799b060",
  "source_text_sha256": "b44b1a2b2f9a02af0076cf184bd12270b5fe24cc4d1672adff00013f2799b060",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdbfe0",
        "00bdbfef"
      ]
    ],
    "bytes_sha256": "68da4bf5d3546fb0b24c85bf56efe173a6fbab6a7c128be93cb6655f01bf091a",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [004a38b0](../004a3/004a38b0.md)

## 呼び出し先

- [004a3810](../004a3/004a3810.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 119 bytes

~~~c

void _ZN5Botan15DataSink_StreamD2Ev(void)

{
  (*(code *)PTR__ZN5Botan15DataSink_StreamD2Ev_00c1c828)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdbfe0"></a> `00bdbfe0` | `10 02 00 b0` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdbfe4"></a> `00bdbfe4` | `11 16 44 f9` | ldr x17,[x16, #0x828] | `FALL_THROUGH`
<a id="insn-00bdbfe8"></a> `00bdbfe8` | `10 a2 20 91` | add x16,x16,#0x828 | `FALL_THROUGH`
<a id="insn-00bdbfec"></a> `00bdbfec` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdbfe0`](#insn-00bdbfe0) 範囲 `[['00bdbfe0', '00bdbfef']]`

## 命令位置別の参照

- [`00bdbfe4`](#insn-00bdbfe4) → `00c1c828`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdbfec`](#insn-00bdbfec) → [`004a3810`](../004a3/004a3810.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `004a3810` · 推定シンボル `_ZN5Botan15DataSink_StreamD2Ev` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdbfe4`](#insn-00bdbfe4)

~~~json
{
  "source": "00bdbfe4",
  "target": "00c1c828",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c828",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdbfec`](#insn-00bdbfec)

~~~json
{
  "source": "00bdbfec",
  "target": "004a3810",
  "target_space": "ram",
  "resolution": "function"
}
~~~
