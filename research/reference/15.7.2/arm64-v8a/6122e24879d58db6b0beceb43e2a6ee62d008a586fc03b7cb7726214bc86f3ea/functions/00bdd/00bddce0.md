# 00bddce0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bddd90`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd90.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0017.md#compare-cec74b9c1b37ac8821c5285ad3878c37)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bddce0",
  "name": "_ZN8firebase26ReferenceCountedFutureImplC2Em",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "69fe124a7915716d19784baad4100efcd2cde0b6ae615ea8ec22e7e5c637ed33",
  "source_text_sha256": "69fe124a7915716d19784baad4100efcd2cde0b6ae615ea8ec22e7e5c637ed33",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bddce0",
        "00bddcef"
      ]
    ],
    "bytes_sha256": "70d74a5aae53e15b2c74e15a7d7f6bd99d449647ac2c98d2f7ea40aad83905c6",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00adffcc](../00adf/00adffcc.md)
- [00b01284](../00b01/00b01284.md)
- [00b02268](../00b02/00b02268.md)
- [00b02404](../00b02/00b02404.md)
- [00b0d678](../00b0d/00b0d678.md)
- [00b49364](../00b49/00b49364.md)
- [00b523e0](../00b52/00b523e0.md)
- [00b54a2c](../00b54/00b54a2c.md)
- [00b5ae80](../00b5a/00b5ae80.md)

## 呼び出し先

- [00ae0100](../00ae0/00ae0100.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 147 bytes

~~~c

void _ZN8firebase26ReferenceCountedFutureImplC2Em(void)

{
  (*(code *)PTR__ZN8firebase26ReferenceCountedFutureImplC2Em_00c1d6a8)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bddce0"></a> `00bddce0` | `10 02 00 90` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bddce4"></a> `00bddce4` | `11 56 43 f9` | ldr x17,[x16, #0x6a8] | `FALL_THROUGH`
<a id="insn-00bddce8"></a> `00bddce8` | `10 a2 1a 91` | add x16,x16,#0x6a8 | `FALL_THROUGH`
<a id="insn-00bddcec"></a> `00bddcec` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bddce0`](#insn-00bddce0) 範囲 `[['00bddce0', '00bddcef']]`

## 命令位置別の参照

- [`00bddce4`](#insn-00bddce4) → `00c1d6a8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bddcec`](#insn-00bddcec) → [`00ae0100`](../00ae0/00ae0100.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00ae0100` · 推定シンボル `_ZN8firebase26ReferenceCountedFutureImplC2Em` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bddce4`](#insn-00bddce4)

~~~json
{
  "source": "00bddce4",
  "target": "00c1d6a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1d6a8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bddcec`](#insn-00bddcec)

~~~json
{
  "source": "00bddcec",
  "target": "00ae0100",
  "target_space": "ram",
  "resolution": "function"
}
~~~
