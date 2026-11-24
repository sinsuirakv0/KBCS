# 00bdbea0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdbe50`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbe50.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0014.md#compare-b07acfefcda4d2a8a2796518cb5bcca5)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c588f0`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c588f0.md) · 移動量 `+0x7ca50`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/high-0007.md#compare-dda1de127aa6e4947060d9ae73decc52)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdbea0",
  "name": "_ZN5Botan6BigInt9randomizeERNS_21RandomNumberGeneratorEmb",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5b664253f19ef937f9ef82515c223f0ddba4a7d55b8aa182ecbe9465c57f6057",
  "source_text_sha256": "5b664253f19ef937f9ef82515c223f0ddba4a7d55b8aa182ecbe9465c57f6057",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdbea0",
        "00bdbeaf"
      ]
    ],
    "bytes_sha256": "b77ed1ecf5602d353a53fdf364be5d04ed22945cfbaf923066bacf470ca9a171",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00497bf4](../00497/00497bf4.md)
- [0049811c](../00498/0049811c.md)

## 呼び出し先

- [00497a4c](../00497/00497a4c.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 173 bytes

~~~c

void _ZN5Botan6BigInt9randomizeERNS_21RandomNumberGeneratorEmb(void)

{
  (*(code *)PTR__ZN5Botan6BigInt9randomizeERNS_21RandomNumberGeneratorEmb_00c1c808)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdbea0"></a> `00bdbea0` | `10 02 00 b0` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdbea4"></a> `00bdbea4` | `11 06 44 f9` | ldr x17,[x16, #0x808] | `FALL_THROUGH`
<a id="insn-00bdbea8"></a> `00bdbea8` | `10 22 20 91` | add x16,x16,#0x808 | `FALL_THROUGH`
<a id="insn-00bdbeac"></a> `00bdbeac` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdbea0`](#insn-00bdbea0) 範囲 `[['00bdbea0', '00bdbeaf']]`

## 命令位置別の参照

- [`00bdbea4`](#insn-00bdbea4) → `00c1c808`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdbeac`](#insn-00bdbeac) → [`00497a4c`](../00497/00497a4c.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00497a4c` · 推定シンボル `_ZN5Botan6BigInt9randomizeERNS_21RandomNumberGeneratorEmb` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdbea4`](#insn-00bdbea4)

~~~json
{
  "source": "00bdbea4",
  "target": "00c1c808",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c808",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdbeac`](#insn-00bdbeac)

~~~json
{
  "source": "00bdbeac",
  "target": "00497a4c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
