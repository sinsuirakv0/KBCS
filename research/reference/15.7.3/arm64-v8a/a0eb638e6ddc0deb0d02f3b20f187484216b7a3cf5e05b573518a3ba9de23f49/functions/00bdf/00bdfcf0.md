# 00bdfcf0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bdfc40`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfc40.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0021.md#compare-c7d40d0cd0ac07911c0e95e6d3ae2997)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bdfd40`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfd40.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0022.md#compare-c64cf381d9b343cc90a8600c2160e8c9)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdfcf0",
  "name": "_ZNSt6__ndk118__insertion_sort_3IRN11flatbuffers17FlatBufferBuilder18TableKeyComparatorIN10reflection5FieldEEEPNS1_6OffsetIS5_EEEEvT0_SB_T_",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0efe714b3147d251df45a9e56c1f0aef07dd62fbd4e5f8d3795b306d5403b578",
  "source_text_sha256": "0efe714b3147d251df45a9e56c1f0aef07dd62fbd4e5f8d3795b306d5403b578",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdfcf0",
        "00bdfcff"
      ]
    ],
    "bytes_sha256": "408f0c71b0cb3377738cac32f5163199ef1bd23cb74def45ba6895b613b444cb",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00b39dcc](../00b39/00b39dcc.md)

## 呼び出し先

- [00b3abb8](../00b3a/00b3abb8.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 361 bytes

~~~c

void _ZNSt6__ndk118__insertion_sort_3IRN11flatbuffers17FlatBufferBuilder18TableKeyComparatorIN10reflection5FieldEEEPNS1_6OffsetIS5_EEEEvT0_SB_T_
               (void)

{
  (*(code *)
    PTR__ZNSt6__ndk118__insertion_sort_3IRN11flatbuffers17FlatBufferBuilder18TableKeyComparatorIN10reflection5FieldEEEPNS1_6OffsetIS5_EEEEvT0_SB_T__00c1e708
  )();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdfcf0"></a> `00bdfcf0` | `f0 01 00 f0` | adrp x16,0xc1e000 | `FALL_THROUGH`
<a id="insn-00bdfcf4"></a> `00bdfcf4` | `11 86 43 f9` | ldr x17,[x16, #0x708] | `FALL_THROUGH`
<a id="insn-00bdfcf8"></a> `00bdfcf8` | `10 22 1c 91` | add x16,x16,#0x708 | `FALL_THROUGH`
<a id="insn-00bdfcfc"></a> `00bdfcfc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdfcf0`](#insn-00bdfcf0) 範囲 `[['00bdfcf0', '00bdfcff']]`

## 命令位置別の参照

- [`00bdfcf4`](#insn-00bdfcf4) → `00c1e708`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdfcfc`](#insn-00bdfcfc) → [`00b3abb8`](../00b3a/00b3abb8.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00b3abb8` · 推定シンボル `_ZNSt6__ndk118__insertion_sort_3IRN11flatbuffers17FlatBufferBuilder18TableKeyComparatorIN10reflection5FieldEEEPNS1_6OffsetIS5_EEEEvT0_SB_T_` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdfcf4`](#insn-00bdfcf4)

~~~json
{
  "source": "00bdfcf4",
  "target": "00c1e708",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1e708",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdfcfc`](#insn-00bdfcfc)

~~~json
{
  "source": "00bdfcfc",
  "target": "00b3abb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
