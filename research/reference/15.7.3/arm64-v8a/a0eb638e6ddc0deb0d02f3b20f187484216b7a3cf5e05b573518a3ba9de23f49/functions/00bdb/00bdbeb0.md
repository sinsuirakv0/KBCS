# 00bdbeb0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bdbe00`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdbe00.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0012.md#compare-a6e62185ad46aabc3c6ef1255f3a9a9b)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bdbf00`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbf00.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0014.md#compare-9f98f5128073422b0c997d6784cbbfe6)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdbeb0",
  "name": "_ZN5Botan12Lookup_ErrorC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_S9_",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b90acdd99dbb69e56ff35e408348cf6d7f2f9cd296cf471627b54ec63beaa9a3",
  "source_text_sha256": "b90acdd99dbb69e56ff35e408348cf6d7f2f9cd296cf471627b54ec63beaa9a3",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdbeb0",
        "00bdbebf"
      ]
    ],
    "bytes_sha256": "7c6a26ef8b0e7dda949871378966f5afc575dd76a5aa7391e5bd63b7b22233ca",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00499128](../00499/00499128.md)
- [004a14bc](../004a1/004a14bc.md)
- [004a19c4](../004a1/004a19c4.md)
- [004a1d20](../004a1/004a1d20.md)
- [004aa79c](../004aa/004aa79c.md)
- [004c1c00](../004c1/004c1c00.md)

## 呼び出し先

- [004d7984](../004d7/004d7984.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 285 bytes

~~~c

void _ZN5Botan12Lookup_ErrorC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_S9_
               (void)

{
  (*(code *)
    PTR__ZN5Botan12Lookup_ErrorC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_S9__00c1c7e8
  )();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdbeb0"></a> `00bdbeb0` | `10 02 00 b0` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdbeb4"></a> `00bdbeb4` | `11 f6 43 f9` | ldr x17,[x16, #0x7e8] | `FALL_THROUGH`
<a id="insn-00bdbeb8"></a> `00bdbeb8` | `10 a2 1f 91` | add x16,x16,#0x7e8 | `FALL_THROUGH`
<a id="insn-00bdbebc"></a> `00bdbebc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdbeb0`](#insn-00bdbeb0) 範囲 `[['00bdbeb0', '00bdbebf']]`

## 命令位置別の参照

- [`00bdbeb4`](#insn-00bdbeb4) → `00c1c7e8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdbebc`](#insn-00bdbebc) → [`004d7984`](../004d7/004d7984.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `004d7984` · 推定シンボル `_ZN5Botan12Lookup_ErrorC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_S9_` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdbeb4`](#insn-00bdbeb4)

~~~json
{
  "source": "00bdbeb4",
  "target": "00c1c7e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c7e8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdbebc`](#insn-00bdbebc)

~~~json
{
  "source": "00bdbebc",
  "target": "004d7984",
  "target_space": "ram",
  "resolution": "function"
}
~~~
