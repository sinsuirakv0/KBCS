# 00bdbdc0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdbe70`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbe70.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0012.md#compare-53261d1d80bc459e1d5ec9b740b30a31)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdbdc0",
  "name": "_ZNK5Botan6BigInt13get_substringEmm",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d17e7fdbec8436d3a09e05029ef2a47f48263e53594b21bef386237c9201282c",
  "source_text_sha256": "d17e7fdbec8436d3a09e05029ef2a47f48263e53594b21bef386237c9201282c",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdbdc0",
        "00bdbdcf"
      ]
    ],
    "bytes_sha256": "3550d60a8faff7accca59f06245fca9cc6485e4d47938c36797c75dab6dee63e",
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
  (*(code *)PTR__ZNK5Botan6BigInt13get_substringEmm_00c1c718)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdbdc0"></a> `00bdbdc0` | `10 02 00 b0` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdbdc4"></a> `00bdbdc4` | `11 8e 43 f9` | ldr x17,[x16, #0x718] | `FALL_THROUGH`
<a id="insn-00bdbdc8"></a> `00bdbdc8` | `10 62 1c 91` | add x16,x16,#0x718 | `FALL_THROUGH`
<a id="insn-00bdbdcc"></a> `00bdbdcc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdbdc0`](#insn-00bdbdc0) 範囲 `[['00bdbdc0', '00bdbdcf']]`

## 命令位置別の参照

- [`00bdbdc4`](#insn-00bdbdc4) → `00c1c718`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdbdcc`](#insn-00bdbdcc) → [`00498254`](../00498/00498254.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00498254` · 推定シンボル `_ZNK5Botan6BigInt13get_substringEmm` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdbdc4`](#insn-00bdbdc4)

~~~json
{
  "source": "00bdbdc4",
  "target": "00c1c718",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c718",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdbdcc`](#insn-00bdbdcc)

~~~json
{
  "source": "00bdbdcc",
  "target": "00498254",
  "target_space": "ram",
  "resolution": "function"
}
~~~
