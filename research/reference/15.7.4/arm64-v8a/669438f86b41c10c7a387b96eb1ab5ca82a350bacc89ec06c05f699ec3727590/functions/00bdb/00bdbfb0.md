# 00bdbfb0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdbf60`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbf60.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0014.md#compare-2c37355c49e988cd24dad30eeda37815)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c58a00`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58a00.md) · 移動量 `+0x7ca50`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/high-0007.md#compare-32943aef9132bfd9c98e56847927210f)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdbfb0",
  "name": "_ZN5Botan9mgf1_maskERNS_12HashFunctionEPKhmPhm",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a4c7ecda38f84b3ce80bdf0da1d36f1d20e0f1ab788e16ab1182f9e8791a17fb",
  "source_text_sha256": "a4c7ecda38f84b3ce80bdf0da1d36f1d20e0f1ab788e16ab1182f9e8791a17fb",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdbfb0",
        "00bdbfbf"
      ]
    ],
    "bytes_sha256": "1ad9f0d67f548abc124248f8088a92142484b090f28116de75d384875ca83b31",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [0049eb38](../0049e/0049eb38.md)
- [0049ef6c](../0049e/0049ef6c.md)

## 呼び出し先

- [004acad0](../004ac/004acad0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 151 bytes

~~~c

void _ZN5Botan9mgf1_maskERNS_12HashFunctionEPKhmPhm(void)

{
  (*(code *)PTR__ZN5Botan9mgf1_maskERNS_12HashFunctionEPKhmPhm_00c1c890)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdbfb0"></a> `00bdbfb0` | `10 02 00 b0` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdbfb4"></a> `00bdbfb4` | `11 4a 44 f9` | ldr x17,[x16, #0x890] | `FALL_THROUGH`
<a id="insn-00bdbfb8"></a> `00bdbfb8` | `10 42 22 91` | add x16,x16,#0x890 | `FALL_THROUGH`
<a id="insn-00bdbfbc"></a> `00bdbfbc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdbfb0`](#insn-00bdbfb0) 範囲 `[['00bdbfb0', '00bdbfbf']]`

## 命令位置別の参照

- [`00bdbfb4`](#insn-00bdbfb4) → `00c1c890`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdbfbc`](#insn-00bdbfbc) → [`004acad0`](../004ac/004acad0.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `004acad0` · 推定シンボル `_ZN5Botan9mgf1_maskERNS_12HashFunctionEPKhmPhm` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdbfb4`](#insn-00bdbfb4)

~~~json
{
  "source": "00bdbfb4",
  "target": "00c1c890",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c890",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdbfbc`](#insn-00bdbfbc)

~~~json
{
  "source": "00bdbfbc",
  "target": "004acad0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
