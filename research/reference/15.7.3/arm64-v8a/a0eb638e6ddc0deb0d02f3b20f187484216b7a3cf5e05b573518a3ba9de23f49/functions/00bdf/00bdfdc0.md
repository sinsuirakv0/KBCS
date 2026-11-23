# 00bdfdc0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bdfd10`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfd10.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0021.md#compare-b073f7600945863e898987991c79f9f9)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bdfe10`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfe10.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0023.md#compare-3c9543e18dfc46401a9adf39f89d0fd1)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdfdc0",
  "name": "_ZNSt6__ndk127__insertion_sort_incompleteIRPFbPKN11flatbuffers7EnumDefES4_EPPS2_EEbT0_SA_T_",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "db693ace31ddd9715aceb7293e39581bb7ac35e6c11a4aa4b9dc18a01743c2fa",
  "source_text_sha256": "db693ace31ddd9715aceb7293e39581bb7ac35e6c11a4aa4b9dc18a01743c2fa",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdfdc0",
        "00bdfdcf"
      ]
    ],
    "bytes_sha256": "3cc265ef9410a44357023c046108d7e3f2adf1f16cc328ced529943b62b37238",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00b456e4](../00b45/00b456e4.md)

## 呼び出し先

- [00b45fe4](../00b45/00b45fe4.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 265 bytes

~~~c

void _ZNSt6__ndk127__insertion_sort_incompleteIRPFbPKN11flatbuffers7EnumDefES4_EPPS2_EEbT0_SA_T_
               (void)

{
  (*(code *)
    PTR__ZNSt6__ndk127__insertion_sort_incompleteIRPFbPKN11flatbuffers7EnumDefES4_EPPS2_EEbT0_SA_T__00c1e770
  )();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdfdc0"></a> `00bdfdc0` | `f0 01 00 f0` | adrp x16,0xc1e000 | `FALL_THROUGH`
<a id="insn-00bdfdc4"></a> `00bdfdc4` | `11 ba 43 f9` | ldr x17,[x16, #0x770] | `FALL_THROUGH`
<a id="insn-00bdfdc8"></a> `00bdfdc8` | `10 c2 1d 91` | add x16,x16,#0x770 | `FALL_THROUGH`
<a id="insn-00bdfdcc"></a> `00bdfdcc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdfdc0`](#insn-00bdfdc0) 範囲 `[['00bdfdc0', '00bdfdcf']]`

## 命令位置別の参照

- [`00bdfdc4`](#insn-00bdfdc4) → `00c1e770`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdfdcc`](#insn-00bdfdcc) → [`00b45fe4`](../00b45/00b45fe4.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00b45fe4` · 推定シンボル `_ZNSt6__ndk127__insertion_sort_incompleteIRPFbPKN11flatbuffers7EnumDefES4_EPPS2_EEbT0_SA_T_` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdfdc4`](#insn-00bdfdc4)

~~~json
{
  "source": "00bdfdc4",
  "target": "00c1e770",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1e770",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdfdcc`](#insn-00bdfdcc)

~~~json
{
  "source": "00bdfdcc",
  "target": "00b45fe4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
