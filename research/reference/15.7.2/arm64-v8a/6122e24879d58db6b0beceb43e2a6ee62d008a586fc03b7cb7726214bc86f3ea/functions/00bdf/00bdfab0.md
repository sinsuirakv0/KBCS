# 00bdfab0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdfb60`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfb60.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0021.md#compare-20acafe77c58f56f9111c4fcfa32c116)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdfab0",
  "name": "_ZNK10reflection6Schema6VerifyERN11flatbuffers8VerifierE",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "268c8a4dd7c3c95e50f3ef97a387240d847b00cf76983f76078d256b6a49ce06",
  "source_text_sha256": "268c8a4dd7c3c95e50f3ef97a387240d847b00cf76983f76078d256b6a49ce06",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdfab0",
        "00bdfabf"
      ]
    ],
    "bytes_sha256": "fc97f52297756cc0d9521f912460cea90bbf322aed55484f3915e26909f5089c",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00b2c7f0](../00b2c/00b2c7f0.md)
- [00b2c894](../00b2c/00b2c894.md)

## 呼び出し先

- [00b352f8](../00b35/00b352f8.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 171 bytes

~~~c

void _ZNK10reflection6Schema6VerifyERN11flatbuffers8VerifierE(void)

{
  (*(code *)PTR__ZNK10reflection6Schema6VerifyERN11flatbuffers8VerifierE_00c1e590)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdfab0"></a> `00bdfab0` | `f0 01 00 f0` | adrp x16,0xc1e000 | `FALL_THROUGH`
<a id="insn-00bdfab4"></a> `00bdfab4` | `11 ca 42 f9` | ldr x17,[x16, #0x590] | `FALL_THROUGH`
<a id="insn-00bdfab8"></a> `00bdfab8` | `10 42 16 91` | add x16,x16,#0x590 | `FALL_THROUGH`
<a id="insn-00bdfabc"></a> `00bdfabc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdfab0`](#insn-00bdfab0) 範囲 `[['00bdfab0', '00bdfabf']]`

## 命令位置別の参照

- [`00bdfab4`](#insn-00bdfab4) → `00c1e590`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdfabc`](#insn-00bdfabc) → [`00b352f8`](../00b35/00b352f8.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00b352f8` · 推定シンボル `_ZNK10reflection6Schema6VerifyERN11flatbuffers8VerifierE` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdfab4`](#insn-00bdfab4)

~~~json
{
  "source": "00bdfab4",
  "target": "00c1e590",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1e590",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdfabc`](#insn-00bdfabc)

~~~json
{
  "source": "00bdfabc",
  "target": "00b352f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
