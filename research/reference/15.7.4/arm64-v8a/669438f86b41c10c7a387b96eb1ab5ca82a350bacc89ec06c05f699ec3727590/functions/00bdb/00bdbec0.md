# 00bdbec0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdbe70`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbe70.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0014.md#compare-677499570b91420e89a383c51be37a86)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c58910`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58910.md) · 移動量 `+0x7ca50`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/high-0007.md#compare-9bd041a2cdd34155ad8477ee1f82e758)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdbec0",
  "name": "_ZNK5Botan6BigInt13get_substringEmm",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "50067eb2ae6aec2500f3bb82880f4fcfed406da5b655cbc293547e220fa1bbca",
  "source_text_sha256": "50067eb2ae6aec2500f3bb82880f4fcfed406da5b655cbc293547e220fa1bbca",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdbec0",
        "00bdbecf"
      ]
    ],
    "bytes_sha256": "133378d0bfa1ac8f92b0fe722aeb37430ebd9db6ca018ce678703c1a5654137d",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [004bc440](../004bc/004bc440.md)
- [004bd550](../004bd/004bd550.md)

## 呼び出し先

- [00498254](../00498/00498254.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 129 bytes

~~~c

void _ZNK5Botan6BigInt13get_substringEmm(void)

{
  (*(code *)PTR__ZNK5Botan6BigInt13get_substringEmm_00c1c818)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdbec0"></a> `00bdbec0` | `10 02 00 b0` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdbec4"></a> `00bdbec4` | `11 0e 44 f9` | ldr x17,[x16, #0x818] | `FALL_THROUGH`
<a id="insn-00bdbec8"></a> `00bdbec8` | `10 62 20 91` | add x16,x16,#0x818 | `FALL_THROUGH`
<a id="insn-00bdbecc"></a> `00bdbecc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdbec0`](#insn-00bdbec0) 範囲 `[['00bdbec0', '00bdbecf']]`

## 命令位置別の参照

- [`00bdbec4`](#insn-00bdbec4) → `00c1c818`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdbecc`](#insn-00bdbecc) → [`00498254`](../00498/00498254.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00498254` · 推定シンボル `_ZNK5Botan6BigInt13get_substringEmm` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdbec4`](#insn-00bdbec4)

~~~json
{
  "source": "00bdbec4",
  "target": "00c1c818",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c818",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdbecc`](#insn-00bdbecc)

~~~json
{
  "source": "00bdbecc",
  "target": "00498254",
  "target_space": "ram",
  "resolution": "function"
}
~~~
