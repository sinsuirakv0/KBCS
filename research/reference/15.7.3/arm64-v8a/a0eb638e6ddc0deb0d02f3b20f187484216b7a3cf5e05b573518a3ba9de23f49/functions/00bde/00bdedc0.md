# 00bdedc0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bded10`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bded10.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0019.md#compare-6ef7739416e05da50ef45640885130c4)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bdee10`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdee10.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/alignment_unresolved-0005.md#compare-e5a541be745ca022979f786196a8de7e)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdedc0",
  "name": "_ZN8firebase26ReferenceCountedFutureImpl18ForceReleaseFutureERKNS_12FutureHandleE",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c15f75b665cbefee33487c12b5aada1e6d09b1a7f124a213de4a4b2c35c598bf",
  "source_text_sha256": "c15f75b665cbefee33487c12b5aada1e6d09b1a7f124a213de4a4b2c35c598bf",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdedc0",
        "00bdedcf"
      ]
    ],
    "bytes_sha256": "ee39c756404d2b7ccc2de1c20b54324a82188794047dcbae0ba2311581fab849",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00afe760](../00afe/00afe760.md)

## 呼び出し先

- [00b00b70](../00b00/00b00b70.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 239 bytes

~~~c

void _ZN8firebase26ReferenceCountedFutureImpl18ForceReleaseFutureERKNS_12FutureHandleE(void)

{
  (*(code *)
    PTR__ZN8firebase26ReferenceCountedFutureImpl18ForceReleaseFutureERKNS_12FutureHandleE_00c1df70)
            ();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdedc0"></a> `00bdedc0` | `f0 01 00 f0` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bdedc4"></a> `00bdedc4` | `11 ba 47 f9` | ldr x17,[x16, #0xf70] | `FALL_THROUGH`
<a id="insn-00bdedc8"></a> `00bdedc8` | `10 c2 3d 91` | add x16,x16,#0xf70 | `FALL_THROUGH`
<a id="insn-00bdedcc"></a> `00bdedcc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdedc0`](#insn-00bdedc0) 範囲 `[['00bdedc0', '00bdedcf']]`

## 命令位置別の参照

- [`00bdedc4`](#insn-00bdedc4) → `00c1df70`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdedcc`](#insn-00bdedcc) → [`00b00b70`](../00b00/00b00b70.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00b00b70` · 推定シンボル `_ZN8firebase26ReferenceCountedFutureImpl18ForceReleaseFutureERKNS_12FutureHandleE` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdedc4`](#insn-00bdedc4)

~~~json
{
  "source": "00bdedc4",
  "target": "00c1df70",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1df70",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdedcc`](#insn-00bdedcc)

~~~json
{
  "source": "00bdedcc",
  "target": "00b00b70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
