# 00bdbce0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdbd90`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbd90.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0012.md#compare-e66689739d89f9fb5c9fb9754fad14d7)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdbce0",
  "name": "_ZN5Botan6BigIntrSEm",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f04eb9007231774562bb60ce0cef336b59826ba0f110669a5bb91ffd93b7f5eb",
  "source_text_sha256": "f04eb9007231774562bb60ce0cef336b59826ba0f110669a5bb91ffd93b7f5eb",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdbce0",
        "00bdbcef"
      ]
    ],
    "bytes_sha256": "96660be0997802c9257f64d8163c32b7d827f42bf4c1d3742d1f5e42a18cde38",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00493850](../00493/00493850.md)
- [004963cc](../00496/004963cc.md)

## 呼び出し先

- [00496564](../00496/00496564.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 99 bytes

~~~c

void _ZN5Botan6BigIntrSEm(void)

{
  (*(code *)PTR__ZN5Botan6BigIntrSEm_00c1c6a8)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdbce0"></a> `00bdbce0` | `10 02 00 b0` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdbce4"></a> `00bdbce4` | `11 56 43 f9` | ldr x17,[x16, #0x6a8] | `FALL_THROUGH`
<a id="insn-00bdbce8"></a> `00bdbce8` | `10 a2 1a 91` | add x16,x16,#0x6a8 | `FALL_THROUGH`
<a id="insn-00bdbcec"></a> `00bdbcec` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdbce0`](#insn-00bdbce0) 範囲 `[['00bdbce0', '00bdbcef']]`

## 命令位置別の参照

- [`00bdbce4`](#insn-00bdbce4) → `00c1c6a8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdbcec`](#insn-00bdbcec) → [`00496564`](../00496/00496564.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00496564` · 推定シンボル `_ZN5Botan6BigIntrSEm` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdbce4`](#insn-00bdbce4)

~~~json
{
  "source": "00bdbce4",
  "target": "00c1c6a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c6a8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdbcec`](#insn-00bdbcec)

~~~json
{
  "source": "00bdbcec",
  "target": "00496564",
  "target_space": "ram",
  "resolution": "function"
}
~~~
