# 00bdbcd0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bdbc20`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdbc20.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0012.md#compare-90c99618b8f9be7e9b326e85671e5714)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bdbd20`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbd20.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0013.md#compare-7dbaf2776d33d8e6a10ab1e921913754)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdbcd0",
  "name": "_ZN5Botan11DER_Encoder9encode_ifEbRS0_",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "85dcc20208f9a31949d7c797099658a1901a6ff347236ad93e6951df4bad0e88",
  "source_text_sha256": "85dcc20208f9a31949d7c797099658a1901a6ff347236ad93e6951df4bad0e88",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdbcd0",
        "00bdbcdf"
      ]
    ],
    "bytes_sha256": "e28c340f546f82ac3557da99d90a9a9e3c2ad0a9f56b274fb7e0ed1a83ad07c5",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [004ef204](../004ef/004ef204.md)
- [004f5078](../004f5/004f5078.md)

## 呼び出し先

- [00490d78](../00490/00490d78.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 135 bytes

~~~c

void _ZN5Botan11DER_Encoder9encode_ifEbRS0_(void)

{
  (*(code *)PTR__ZN5Botan11DER_Encoder9encode_ifEbRS0__00c1c6f8)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdbcd0"></a> `00bdbcd0` | `10 02 00 b0` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdbcd4"></a> `00bdbcd4` | `11 7e 43 f9` | ldr x17,[x16, #0x6f8] | `FALL_THROUGH`
<a id="insn-00bdbcd8"></a> `00bdbcd8` | `10 e2 1b 91` | add x16,x16,#0x6f8 | `FALL_THROUGH`
<a id="insn-00bdbcdc"></a> `00bdbcdc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdbcd0`](#insn-00bdbcd0) 範囲 `[['00bdbcd0', '00bdbcdf']]`

## 命令位置別の参照

- [`00bdbcd4`](#insn-00bdbcd4) → `00c1c6f8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdbcdc`](#insn-00bdbcdc) → [`00490d78`](../00490/00490d78.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00490d78` · 推定シンボル `_ZN5Botan11DER_Encoder9encode_ifEbRS0_` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdbcd4`](#insn-00bdbcd4)

~~~json
{
  "source": "00bdbcd4",
  "target": "00c1c6f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c6f8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdbcdc`](#insn-00bdbcdc)

~~~json
{
  "source": "00bdbcdc",
  "target": "00490d78",
  "target_space": "ram",
  "resolution": "function"
}
~~~
