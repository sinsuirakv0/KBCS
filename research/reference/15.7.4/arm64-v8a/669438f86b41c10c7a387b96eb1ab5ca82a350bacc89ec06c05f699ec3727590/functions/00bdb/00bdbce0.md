# 00bdbce0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdbc90`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbc90.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0013.md#compare-625d2f94d37e1bae7b2dab9be8ede2a8)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c58730`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58730.md) · 移動量 `+0x7ca50`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/high-0007.md#compare-4daf07403d678f5bf9333de167301d53)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdbce0",
  "name": "_ZN5Botan11DER_Encoder6encodeEPKhmNS_8ASN1_TagES3_S3_",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "890d9ad8533da7bb460c58c7694ad6b5bc631c0852a558286f5885d9643ebf7e",
  "source_text_sha256": "890d9ad8533da7bb460c58c7694ad6b5bc631c0852a558286f5885d9643ebf7e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdbce0",
        "00bdbcef"
      ]
    ],
    "bytes_sha256": "bdb68c06cce365bcd5ac6228bd5458e7726c719471dc7b96cfa8db798b3464d2",
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
  (*(code *)PTR__ZN5Botan11DER_Encoder6encodeEPKhmNS_8ASN1_TagES3_S3__00c1c728)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdbce0"></a> `00bdbce0` | `10 02 00 b0` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdbce4"></a> `00bdbce4` | `11 96 43 f9` | ldr x17,[x16, #0x728] | `FALL_THROUGH`
<a id="insn-00bdbce8"></a> `00bdbce8` | `10 a2 1c 91` | add x16,x16,#0x728 | `FALL_THROUGH`
<a id="insn-00bdbcec"></a> `00bdbcec` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdbce0`](#insn-00bdbce0) 範囲 `[['00bdbce0', '00bdbcef']]`

## 命令位置別の参照

- [`00bdbce4`](#insn-00bdbce4) → `00c1c728`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdbcec`](#insn-00bdbcec) → [`00490274`](../00490/00490274.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00490274` · 推定シンボル `_ZN5Botan11DER_Encoder6encodeEPKhmNS_8ASN1_TagES3_S3_` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdbce4`](#insn-00bdbce4)

~~~json
{
  "source": "00bdbce4",
  "target": "00c1c728",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c728",
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
  "target": "00490274",
  "target_space": "ram",
  "resolution": "function"
}
~~~
