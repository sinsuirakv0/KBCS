# 00bdbbe0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdbc90`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbc90.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0012.md#compare-e40c5ab707d9beebb011a5b89c61b94d)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdbbe0",
  "name": "_ZN5Botan11DER_Encoder6encodeEPKhmNS_8ASN1_TagES3_S3_",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "aad0bff5251bca90dd25ebf885a22cd46eb903fe6165aa182bfad9b316ad8d85",
  "source_text_sha256": "aad0bff5251bca90dd25ebf885a22cd46eb903fe6165aa182bfad9b316ad8d85",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdbbe0",
        "00bdbbef"
      ]
    ],
    "bytes_sha256": "9d7eb7dd04fbbe13bc4aacfcc3de5844f4a7a5820c8de1db281fb5f07d61da74",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00490268](../00490/00490268.md)
- [00490d40](../00490/00490d40.md)
- [00490d5c](../00490/00490d5c.md)
- [004c6f64](../004c6/004c6f64.md)
- [004eebcc](../004ee/004eebcc.md)
- [004fc21c](../004fc/004fc21c.md)

## 呼び出し先

- [00490274](../00490/00490274.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 165 bytes

~~~c

void _ZN5Botan11DER_Encoder6encodeEPKhmNS_8ASN1_TagES3_S3_(void)

{
  (*(code *)PTR__ZN5Botan11DER_Encoder6encodeEPKhmNS_8ASN1_TagES3_S3__00c1c628)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdbbe0"></a> `00bdbbe0` | `10 02 00 b0` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdbbe4"></a> `00bdbbe4` | `11 16 43 f9` | ldr x17,[x16, #0x628] | `FALL_THROUGH`
<a id="insn-00bdbbe8"></a> `00bdbbe8` | `10 a2 18 91` | add x16,x16,#0x628 | `FALL_THROUGH`
<a id="insn-00bdbbec"></a> `00bdbbec` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdbbe0`](#insn-00bdbbe0) 範囲 `[['00bdbbe0', '00bdbbef']]`

## 命令位置別の参照

- [`00bdbbe4`](#insn-00bdbbe4) → `00c1c628`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdbbec`](#insn-00bdbbec) → [`00490274`](../00490/00490274.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00490274` · 推定シンボル `_ZN5Botan11DER_Encoder6encodeEPKhmNS_8ASN1_TagES3_S3_` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdbbe4`](#insn-00bdbbe4)

~~~json
{
  "source": "00bdbbe4",
  "target": "00c1c628",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c628",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdbbec`](#insn-00bdbbec)

~~~json
{
  "source": "00bdbbec",
  "target": "00490274",
  "target_space": "ram",
  "resolution": "function"
}
~~~
