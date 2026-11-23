# 00bdfdd0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bdfd20`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfd20.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/alignment_unresolved-0007.md#compare-4f9fe4537d13d9ef7c945db05fd6ad9b)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bdfe20`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfe20.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0023.md#compare-1313d955f08b9e9dbb00e5c6c62a3ad6)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdfdd0",
  "name": "_ZNSt6__ndk127__insertion_sort_incompleteIRPFbPKN11flatbuffers8FieldDefES4_EPPS2_EEbT0_SA_T_",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a517261d35af63cd83d449a8c611168d702814c0c8d0d894556ad68598be124d",
  "source_text_sha256": "a517261d35af63cd83d449a8c611168d702814c0c8d0d894556ad68598be124d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdfdd0",
        "00bdfddf"
      ]
    ],
    "bytes_sha256": "a1555685f1bfe9253e8586c7ccd5bae53ae4038efb3cbf52aefa0d98adace38e",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00b4307c](../00b43/00b4307c.md)

## 呼び出し先

- [00b4397c](../00b43/00b4397c.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 267 bytes

~~~c

void _ZNSt6__ndk127__insertion_sort_incompleteIRPFbPKN11flatbuffers8FieldDefES4_EPPS2_EEbT0_SA_T_
               (void)

{
  (*(code *)
    PTR__ZNSt6__ndk127__insertion_sort_incompleteIRPFbPKN11flatbuffers8FieldDefES4_EPPS2_EEbT0_SA_T__00c1e778
  )();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdfdd0"></a> `00bdfdd0` | `f0 01 00 f0` | adrp x16,0xc1e000 | `FALL_THROUGH`
<a id="insn-00bdfdd4"></a> `00bdfdd4` | `11 be 43 f9` | ldr x17,[x16, #0x778] | `FALL_THROUGH`
<a id="insn-00bdfdd8"></a> `00bdfdd8` | `10 e2 1d 91` | add x16,x16,#0x778 | `FALL_THROUGH`
<a id="insn-00bdfddc"></a> `00bdfddc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdfdd0`](#insn-00bdfdd0) 範囲 `[['00bdfdd0', '00bdfddf']]`

## 命令位置別の参照

- [`00bdfdd4`](#insn-00bdfdd4) → `00c1e778`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdfddc`](#insn-00bdfddc) → [`00b4397c`](../00b43/00b4397c.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00b4397c` · 推定シンボル `_ZNSt6__ndk127__insertion_sort_incompleteIRPFbPKN11flatbuffers8FieldDefES4_EPPS2_EEbT0_SA_T_` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdfdd4`](#insn-00bdfdd4)

~~~json
{
  "source": "00bdfdd4",
  "target": "00c1e778",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1e778",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdfddc`](#insn-00bdfddc)

~~~json
{
  "source": "00bdfddc",
  "target": "00b4397c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
