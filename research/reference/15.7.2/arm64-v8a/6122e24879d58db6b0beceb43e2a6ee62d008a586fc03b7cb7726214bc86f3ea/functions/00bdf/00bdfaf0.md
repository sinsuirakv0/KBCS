# 00bdfaf0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdfba0`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfba0.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0021.md#compare-3d714348c2f252c8823b2f114a905b03)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdfaf0",
  "name": "_ZNK10reflection8KeyValue6VerifyERN11flatbuffers8VerifierE",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7994466c712403d72c147d8b05bc7b9ead616a3ceb8c54fd44984f11a539fa9e",
  "source_text_sha256": "7994466c712403d72c147d8b05bc7b9ead616a3ceb8c54fd44984f11a539fa9e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdfaf0",
        "00bdfaff"
      ]
    ],
    "bytes_sha256": "340efca901f04d3e1ae59885e0bb2965708c65b247c89b91affcdd20d60e0277",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00b359f8](../00b35/00b359f8.md)
- [00b36068](../00b36/00b36068.md)
- [00b36b18](../00b36/00b36b18.md)
- [00b37648](../00b37/00b37648.md)
- [00b37c10](../00b37/00b37c10.md)

## 呼び出し先

- [00b368a4](../00b36/00b368a4.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 175 bytes

~~~c

void _ZNK10reflection8KeyValue6VerifyERN11flatbuffers8VerifierE(void)

{
  (*(code *)PTR__ZNK10reflection8KeyValue6VerifyERN11flatbuffers8VerifierE_00c1e5b0)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdfaf0"></a> `00bdfaf0` | `f0 01 00 f0` | adrp x16,0xc1e000 | `FALL_THROUGH`
<a id="insn-00bdfaf4"></a> `00bdfaf4` | `11 da 42 f9` | ldr x17,[x16, #0x5b0] | `FALL_THROUGH`
<a id="insn-00bdfaf8"></a> `00bdfaf8` | `10 c2 16 91` | add x16,x16,#0x5b0 | `FALL_THROUGH`
<a id="insn-00bdfafc"></a> `00bdfafc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdfaf0`](#insn-00bdfaf0) 範囲 `[['00bdfaf0', '00bdfaff']]`

## 命令位置別の参照

- [`00bdfaf4`](#insn-00bdfaf4) → `00c1e5b0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdfafc`](#insn-00bdfafc) → [`00b368a4`](../00b36/00b368a4.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00b368a4` · 推定シンボル `_ZNK10reflection8KeyValue6VerifyERN11flatbuffers8VerifierE` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdfaf4`](#insn-00bdfaf4)

~~~json
{
  "source": "00bdfaf4",
  "target": "00c1e5b0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1e5b0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdfafc`](#insn-00bdfafc)

~~~json
{
  "source": "00bdfafc",
  "target": "00b368a4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
