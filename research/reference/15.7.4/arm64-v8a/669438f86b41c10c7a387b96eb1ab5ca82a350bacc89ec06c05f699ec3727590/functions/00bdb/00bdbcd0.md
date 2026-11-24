# 00bdbcd0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdbc80`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbc80.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0013.md#compare-e9cffb4b8d9814cffa2c75e28c00822a)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c58720`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58720.md) · 移動量 `+0x7ca50`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/high-0007.md#compare-aab3d36f2d8f2357e17a58af0f551f5c)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdbcd0",
  "name": "_ZNK5Botan6BigInt3cmpERKS0_b",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0a32c78a1b033456e90b3f6ca8dd5a9c5fb6e2c28236b6a5b33af1e53f09e400",
  "source_text_sha256": "0a32c78a1b033456e90b3f6ca8dd5a9c5fb6e2c28236b6a5b33af1e53f09e400",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdbcd0",
        "00bdbcdf"
      ]
    ],
    "bytes_sha256": "311689e71a24155a5335c63857760da56e781f5ef096fa0431ceec8e1df68a99",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [0048ff2c](../0048f/0048ff2c.md)
- [00493850](../00493/00493850.md)
- [00495378](../00495/00495378.md)
- [004967a4](../00496/004967a4.md)
- [00497bf4](../00497/00497bf4.md)
- [004b5c14](../004b5/004b5c14.md)
- [004b6640](../004b6/004b6640.md)
- [004b6d50](../004b6/004b6d50.md)
- [004b77d0](../004b7/004b77d0.md)
- [004b8e58](../004b8/004b8e58.md)
- [004b9948](../004b9/004b9948.md)
- [004ba430](../004ba/004ba430.md)
- [004bb928](../004bb/004bb928.md)
- [004bbdd8](../004bb/004bbdd8.md)
- [004bcf24](../004bc/004bcf24.md)
- [004bdd7c](../004bd/004bdd7c.md)
- [004be0f4](../004be/004be0f4.md)
- [004cf4d8](../004cf/004cf4d8.md)
- [004cfcb0](../004cf/004cfcb0.md)
- [004d04c0](../004d0/004d04c0.md)
- [004d1904](../004d1/004d1904.md)
- [004e939c](../004e9/004e939c.md)
- [00513fc4](../00513/00513fc4.md)
- [00514cc0](../00514/00514cc0.md)
- [00516464](../00516/00516464.md)
- [005168d8](../00516/005168d8.md)

## 呼び出し先

- [00498160](../00498/00498160.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 115 bytes

~~~c

void _ZNK5Botan6BigInt3cmpERKS0_b(void)

{
  (*(code *)PTR__ZNK5Botan6BigInt3cmpERKS0_b_00c1c720)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdbcd0"></a> `00bdbcd0` | `10 02 00 b0` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdbcd4"></a> `00bdbcd4` | `11 92 43 f9` | ldr x17,[x16, #0x720] | `FALL_THROUGH`
<a id="insn-00bdbcd8"></a> `00bdbcd8` | `10 82 1c 91` | add x16,x16,#0x720 | `FALL_THROUGH`
<a id="insn-00bdbcdc"></a> `00bdbcdc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdbcd0`](#insn-00bdbcd0) 範囲 `[['00bdbcd0', '00bdbcdf']]`

## 命令位置別の参照

- [`00bdbcd4`](#insn-00bdbcd4) → `00c1c720`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdbcdc`](#insn-00bdbcdc) → [`00498160`](../00498/00498160.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00498160` · 推定シンボル `_ZNK5Botan6BigInt3cmpERKS0_b` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdbcd4`](#insn-00bdbcd4)

~~~json
{
  "source": "00bdbcd4",
  "target": "00c1c720",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c720",
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
  "target": "00498160",
  "target_space": "ram",
  "resolution": "function"
}
~~~
