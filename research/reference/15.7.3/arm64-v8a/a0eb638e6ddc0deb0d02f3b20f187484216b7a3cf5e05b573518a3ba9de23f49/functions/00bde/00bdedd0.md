# 00bdedd0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bded20`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bded20.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/alignment_unresolved-0007.md#compare-568e0146a18f0aae32a3a5259eef4e8d)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bdee20`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdee20.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/alignment_unresolved-0005.md#compare-a7f2d4c96989a5ec0ae427b0bd715c51)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdedd0",
  "name": "_ZN8firebase26ReferenceCountedFutureImplD1Ev",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4524ff36cc18d432e6b97feb8cbb45dde95ec0c85bb8eee505d4cf2314a1e08d",
  "source_text_sha256": "4524ff36cc18d432e6b97feb8cbb45dde95ec0c85bb8eee505d4cf2314a1e08d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdedd0",
        "00bdeddf"
      ]
    ],
    "bytes_sha256": "d5af4810462c6fb27a5b1c7cfafd834a8014c6db1af1bf092f7073896076f4f5",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00afecd8](../00afe/00afecd8.md)

## 呼び出し先

- [00afeae0](../00afe/00afeae0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 244 bytes

~~~c

void _ZN8firebase26ReferenceCountedFutureImplD1Ev(void)

{
                    /* try { // try from 00bdedd4 to 00cdeddf has its CatchHandler @ 00bdf63c */
  (*(code *)PTR__ZN8firebase26ReferenceCountedFutureImplD1Ev_00c1df78)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdedd0"></a> `00bdedd0` | `f0 01 00 f0` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bdedd4"></a> `00bdedd4` | `11 be 47 f9` | ldr x17,[x16, #0xf78] | `FALL_THROUGH`
<a id="insn-00bdedd8"></a> `00bdedd8` | `10 e2 3d 91` | add x16,x16,#0xf78 | `FALL_THROUGH`
<a id="insn-00bdeddc"></a> `00bdeddc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdedd0`](#insn-00bdedd0) 範囲 `[['00bdedd0', '00bdedd3']]`
  - `FALL_THROUGH` [`00bdedd0`](#insn-00bdedd0) → [`00bdedd4`](#insn-00bdedd4)
- ブロック [`00bdedd4`](#insn-00bdedd4) 範囲 `[['00bdedd4', '00bdeddf']]`

## 命令位置別の参照

- [`00bdedd4`](#insn-00bdedd4) → `00c1df78`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdeddc`](#insn-00bdeddc) → [`00afeae0`](../00afe/00afeae0.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00afeae0` · 推定シンボル `_ZN8firebase26ReferenceCountedFutureImplD1Ev` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdedd4`](#insn-00bdedd4)

~~~json
{
  "source": "00bdedd4",
  "target": "00c1df78",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1df78",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdeddc`](#insn-00bdeddc)

~~~json
{
  "source": "00bdeddc",
  "target": "00afeae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
