# 00bddcd0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bddd80`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd80.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0017.md#compare-47338ffc9584e60b94ecbd2d334e70b6)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bddcd0",
  "name": "_ZN8firebase15CleanupNotifierD2Ev",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a831d1188ebc314711cba6dfdb34869ba94338619b8cd61b1f5643d72d50c401",
  "source_text_sha256": "a831d1188ebc314711cba6dfdb34869ba94338619b8cd61b1f5643d72d50c401",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bddcd0",
        "00bddcdf"
      ]
    ],
    "bytes_sha256": "b9ba492dff2c6d62014f589714d2cd6e72721f033a848183c412635a5534cc93",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00af8d88](../00af8/00af8d88.md)
- [00afadc0](../00afa/00afadc0.md)
- [00afae90](../00afa/00afae90.md)
- [00afea18](../00afe/00afea18.md)
- [00b5572c](../00b55/00b5572c.md)

## 呼び出し先

- [00afc4e4](../00afc/00afc4e4.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 125 bytes

~~~c

void _ZN8firebase15CleanupNotifierD2Ev(void)

{
  (*(code *)PTR__ZN8firebase15CleanupNotifierD2Ev_00c1d6a0)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bddcd0"></a> `00bddcd0` | `10 02 00 90` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bddcd4"></a> `00bddcd4` | `11 52 43 f9` | ldr x17,[x16, #0x6a0] | `FALL_THROUGH`
<a id="insn-00bddcd8"></a> `00bddcd8` | `10 82 1a 91` | add x16,x16,#0x6a0 | `FALL_THROUGH`
<a id="insn-00bddcdc"></a> `00bddcdc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bddcd0`](#insn-00bddcd0) 範囲 `[['00bddcd0', '00bddcdf']]`

## 命令位置別の参照

- [`00bddcd4`](#insn-00bddcd4) → `00c1d6a0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bddcdc`](#insn-00bddcdc) → [`00afc4e4`](../00afc/00afc4e4.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00afc4e4` · 推定シンボル `_ZN8firebase15CleanupNotifierD2Ev` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bddcd4`](#insn-00bddcd4)

~~~json
{
  "source": "00bddcd4",
  "target": "00c1d6a0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1d6a0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bddcdc`](#insn-00bddcdc)

~~~json
{
  "source": "00bddcdc",
  "target": "00afc4e4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
