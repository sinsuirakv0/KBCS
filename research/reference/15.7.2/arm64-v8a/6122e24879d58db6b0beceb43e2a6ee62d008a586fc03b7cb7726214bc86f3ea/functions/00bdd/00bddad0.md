# 00bddad0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bddb80`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddb80.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0016.md#compare-4c8a21d6572bf811293574d08abf2ef0)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bddad0",
  "name": "_ZN8firebase4auth4UserC1ERKS1_",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d11ae5c53c09e0f9c57c60d8b95ba23ca234e7f50504c909ca55c166215d4ab1",
  "source_text_sha256": "d11ae5c53c09e0f9c57c60d8b95ba23ca234e7f50504c909ca55c166215d4ab1",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bddad0",
        "00bddadf"
      ]
    ],
    "bytes_sha256": "ba1cfae0f64632bc15897b22989a41e891441aed36eb4886ff10880e20c2691e",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [008480ec](../00848/008480ec.md)
- [0084914c](../00849/0084914c.md)
- [00ad4f2c](../00ad4/00ad4f2c.md)
- [00b5f770](../00b5f/00b5f770.md)
- [00b6cbc8](../00b6c/00b6cbc8.md)

## 呼び出し先

- [00b6e7d8](../00b6e/00b6e7d8.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 119 bytes

~~~c

void _ZN8firebase4auth4UserC1ERKS1_(void)

{
  (*(code *)PTR__ZN8firebase4auth4UserC1ERKS1__00c1d5a0)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bddad0"></a> `00bddad0` | `10 02 00 90` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bddad4"></a> `00bddad4` | `11 d2 42 f9` | ldr x17,[x16, #0x5a0] | `FALL_THROUGH`
<a id="insn-00bddad8"></a> `00bddad8` | `10 82 16 91` | add x16,x16,#0x5a0 | `FALL_THROUGH`
<a id="insn-00bddadc"></a> `00bddadc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bddad0`](#insn-00bddad0) 範囲 `[['00bddad0', '00bddadf']]`

## 命令位置別の参照

- [`00bddad4`](#insn-00bddad4) → `00c1d5a0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bddadc`](#insn-00bddadc) → [`00b6e7d8`](../00b6e/00b6e7d8.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00b6e7d8` · 推定シンボル `_ZN8firebase4auth4UserC1ERKS1_` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bddad4`](#insn-00bddad4)

~~~json
{
  "source": "00bddad4",
  "target": "00c1d5a0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1d5a0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bddadc`](#insn-00bddadc)

~~~json
{
  "source": "00bddadc",
  "target": "00b6e7d8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
