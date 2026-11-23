# 00bdece0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bded90`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bded90.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0019.md#compare-efe3acdda4950fa2e178cdc03d8f6541)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdece0",
  "name": "_ZN8firebase26ReferenceCountedFutureImpl14SetContextDataERKNS_12FutureHandleEPvPFvS4_E",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "cf9cbf947ab696a42897754ad85439ee10704bff56884d1c81047b40392e0565",
  "source_text_sha256": "cf9cbf947ab696a42897754ad85439ee10704bff56884d1c81047b40392e0565",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdece0",
        "00bdecef"
      ]
    ],
    "bytes_sha256": "19e6999169ea209025f3b70fe9cc5b552831b8bca4e663cb3ef999fb9c3e20b0",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00b00570](../00b00/00b00570.md)

## 呼び出し先

- [00b004b0](../00b00/00b004b0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 239 bytes

~~~c

void _ZN8firebase26ReferenceCountedFutureImpl14SetContextDataERKNS_12FutureHandleEPvPFvS4_E(void)

{
  (*(code *)
    PTR__ZN8firebase26ReferenceCountedFutureImpl14SetContextDataERKNS_12FutureHandleEPvPFvS4_E_00c1dea8
  )();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdece0"></a> `00bdece0` | `f0 01 00 f0` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bdece4"></a> `00bdece4` | `11 56 47 f9` | ldr x17,[x16, #0xea8] | `FALL_THROUGH`
<a id="insn-00bdece8"></a> `00bdece8` | `10 a2 3a 91` | add x16,x16,#0xea8 | `FALL_THROUGH`
<a id="insn-00bdecec"></a> `00bdecec` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdece0`](#insn-00bdece0) 範囲 `[['00bdece0', '00bdecef']]`

## 命令位置別の参照

- [`00bdece4`](#insn-00bdece4) → `00c1dea8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdecec`](#insn-00bdecec) → [`00b004b0`](../00b00/00b004b0.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00b004b0` · 推定シンボル `_ZN8firebase26ReferenceCountedFutureImpl14SetContextDataERKNS_12FutureHandleEPvPFvS4_E` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdece4`](#insn-00bdece4)

~~~json
{
  "source": "00bdece4",
  "target": "00c1dea8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1dea8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdecec`](#insn-00bdecec)

~~~json
{
  "source": "00bdecec",
  "target": "00b004b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
