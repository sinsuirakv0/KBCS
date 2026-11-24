# 00bdbcc0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdbc70`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbc70.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0013.md#compare-2f505e8e6a404fc5bad6bb684baf0743)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c58710`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58710.md) · 移動量 `+0x7ca50`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/high-0007.md#compare-db89cf8cf04cb4a952017c4b760c75d9)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdbcc0",
  "name": "_ZN5Botan11DER_Encoder6encodeERKNS_6BigIntENS_8ASN1_TagES4_",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a5822e1a2c8371cdf7035c25b2d9fea3467b2352c74f578a7ee138d441b1f051",
  "source_text_sha256": "a5822e1a2c8371cdf7035c25b2d9fea3467b2352c74f578a7ee138d441b1f051",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdbcc0",
        "00bdbccf"
      ]
    ],
    "bytes_sha256": "3550d60a8faff7accca59f06245fca9cc6485e4d47938c36797c75dab6dee63e",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [0048fe68](../0048f/0048fe68.md)
- [0049025c](../00490/0049025c.md)
- [00490480](../00490/00490480.md)
- [0049f624](../0049f/0049f624.md)
- [004bf57c](../004bf/004bf57c.md)
- [004c73c4](../004c7/004c73c4.md)
- [004ccf4c](../004cc/004ccf4c.md)
- [004cf1d8](../004cf/004cf1d8.md)
- [004cf634](../004cf/004cf634.md)
- [004e0734](../004e0/004e0734.md)
- [004e6aac](../004e6/004e6aac.md)
- [004e9d4c](../004e9/004e9d4c.md)
- [004ee7d8](../004ee/004ee7d8.md)
- [004ef204](../004ef/004ef204.md)
- [004f5078](../004f5/004f5078.md)
- [004fa9b0](../004fa/004fa9b0.md)
- [004faccc](../004fa/004faccc.md)
- [0050b45c](../0050b/0050b45c.md)

## 呼び出し先

- [0048ff2c](../0048f/0048ff2c.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 177 bytes

~~~c

void _ZN5Botan11DER_Encoder6encodeERKNS_6BigIntENS_8ASN1_TagES4_(void)

{
  (*(code *)PTR__ZN5Botan11DER_Encoder6encodeERKNS_6BigIntENS_8ASN1_TagES4__00c1c718)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdbcc0"></a> `00bdbcc0` | `10 02 00 b0` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdbcc4"></a> `00bdbcc4` | `11 8e 43 f9` | ldr x17,[x16, #0x718] | `FALL_THROUGH`
<a id="insn-00bdbcc8"></a> `00bdbcc8` | `10 62 1c 91` | add x16,x16,#0x718 | `FALL_THROUGH`
<a id="insn-00bdbccc"></a> `00bdbccc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdbcc0`](#insn-00bdbcc0) 範囲 `[['00bdbcc0', '00bdbccf']]`

## 命令位置別の参照

- [`00bdbcc4`](#insn-00bdbcc4) → `00c1c718`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdbccc`](#insn-00bdbccc) → [`0048ff2c`](../0048f/0048ff2c.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `0048ff2c` · 推定シンボル `_ZN5Botan11DER_Encoder6encodeERKNS_6BigIntENS_8ASN1_TagES4_` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdbcc4`](#insn-00bdbcc4)

~~~json
{
  "source": "00bdbcc4",
  "target": "00c1c718",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c718",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdbccc`](#insn-00bdbccc)

~~~json
{
  "source": "00bdbccc",
  "target": "0048ff2c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
