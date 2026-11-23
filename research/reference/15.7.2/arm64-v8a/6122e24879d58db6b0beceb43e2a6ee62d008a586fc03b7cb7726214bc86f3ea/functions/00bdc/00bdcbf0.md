# 00bdcbf0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdcca0`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcca0.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0014.md#compare-a56f003661a6cb50054d1812e8f4e663)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdcbf0",
  "name": "_ZN5Botan7X509_DN11decode_fromERNS_11BER_DecoderE",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5ef8f4e425ae91165654ffdab196626bedd74552872b2672463a6bc539a47dca",
  "source_text_sha256": "5ef8f4e425ae91165654ffdab196626bedd74552872b2672463a6bc539a47dca",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdcbf0",
        "00bdcbff"
      ]
    ],
    "bytes_sha256": "966cfe3ad07543070d348677b226f2ec8e5f4b2ec70fc99452fefa4be10b890f",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [004e3840](../004e3/004e3840.md)

## 呼び出し先

- [004e40b8](../004e4/004e40b8.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 157 bytes

~~~c

void _ZN5Botan7X509_DN11decode_fromERNS_11BER_DecoderE(void)

{
  (*(code *)PTR__ZN5Botan7X509_DN11decode_fromERNS_11BER_DecoderE_00c1ce30)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdcbf0"></a> `00bdcbf0` | `10 02 00 90` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdcbf4"></a> `00bdcbf4` | `11 1a 47 f9` | ldr x17,[x16, #0xe30] | `FALL_THROUGH`
<a id="insn-00bdcbf8"></a> `00bdcbf8` | `10 c2 38 91` | add x16,x16,#0xe30 | `FALL_THROUGH`
<a id="insn-00bdcbfc"></a> `00bdcbfc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdcbf0`](#insn-00bdcbf0) 範囲 `[['00bdcbf0', '00bdcbff']]`

## 命令位置別の参照

- [`00bdcbf4`](#insn-00bdcbf4) → `00c1ce30`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdcbfc`](#insn-00bdcbfc) → [`004e40b8`](../004e4/004e40b8.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `004e40b8` · 推定シンボル `_ZN5Botan7X509_DN11decode_fromERNS_11BER_DecoderE` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdcbf4`](#insn-00bdcbf4)

~~~json
{
  "source": "00bdcbf4",
  "target": "00c1ce30",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1ce30",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdcbfc`](#insn-00bdcbfc)

~~~json
{
  "source": "00bdcbfc",
  "target": "004e40b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
