# 00bddcc0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bddc10`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddc10.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0016.md#compare-e8b6f92826fdd8f946e05e32e01b56fc)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bddd10`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddd10.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0018.md#compare-86ed04642d9cce2a93586d408580c1e1)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bddcc0",
  "name": "<EXTERNAL>::__umask_chk",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "84428188beee9535ce525bc0af16da85cdee8389e36a7238b37b14b0a335540d",
  "source_text_sha256": "84428188beee9535ce525bc0af16da85cdee8389e36a7238b37b14b0a335540d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bddcc0",
        "00bddccf"
      ]
    ],
    "bytes_sha256": "f137ae9389c985512b2cca827917a125e348dd3d17e2bf3b005d584f00c274e2",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00acc304](../00acc/00acc304.md)
- [00b4b4dc](../00b4b/00b4b4dc.md)

## 呼び出し先

- [010a5570](../010a5/010a5570.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 81 bytes

~~~c

void __umask_chk(void)

{
  (*(code *)PTR___umask_chk_00c1d6f0)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bddcc0"></a> `00bddcc0` | `10 02 00 90` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bddcc4"></a> `00bddcc4` | `11 7a 43 f9` | ldr x17,[x16, #0x6f0] | `FALL_THROUGH`
<a id="insn-00bddcc8"></a> `00bddcc8` | `10 c2 1b 91` | add x16,x16,#0x6f0 | `FALL_THROUGH`
<a id="insn-00bddccc"></a> `00bddccc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bddcc0`](#insn-00bddcc0) 範囲 `[['00bddcc0', '00bddccf']]`

## 命令位置別の参照

- [`00bddcc4`](#insn-00bddcc4) → `00c1d6f0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bddccc`](#insn-00bddccc) → [`010a5570`](../010a5/010a5570.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `010a5570` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bddcc4`](#insn-00bddcc4)

~~~json
{
  "source": "00bddcc4",
  "target": "00c1d6f0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1d6f0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bddccc`](#insn-00bddccc)

~~~json
{
  "source": "00bddccc",
  "target": "010a5570",
  "target_space": "ram",
  "resolution": "function"
}
~~~
