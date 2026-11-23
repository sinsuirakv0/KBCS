# 00bdbbc0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bdbb10`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdbb10.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/alignment_unresolved-0006.md#compare-14f5033073de8574e5babc3ea4614591)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bdbc10`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbc10.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0013.md#compare-eafbc8f3811b884887771975edec5d56)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdbbc0",
  "name": "_ZN5Botan11BER_Decoder9push_backERKNS_10BER_ObjectE",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "801d78617738392f2683a75a4b1a6e96e05d340252f0861f197cc5adf7ae236a",
  "source_text_sha256": "801d78617738392f2683a75a4b1a6e96e05d340252f0861f197cc5adf7ae236a",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdbbc0",
        "00bdbbcf"
      ]
    ],
    "bytes_sha256": "f42a4760a1c8319bb4825a2fd15064b225e4d00293f3467631085ef7a0c87d82",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [004c13f0](../004c1/004c13f0.md)
- [004c15a4](../004c1/004c15a4.md)
- [004e6d3c](../004e6/004e6d3c.md)
- [004e7c0c](../004e7/004e7c0c.md)
- [004e7de0](../004e7/004e7de0.md)
- [004e82ac](../004e8/004e82ac.md)
- [004ea2b0](../004ea/004ea2b0.md)
- [004f4ba8](../004f4/004f4ba8.md)
- [004f73a8](../004f7/004f73a8.md)
- [004fbbe8](../004fb/004fbbe8.md)

## 呼び出し先

- [0048d518](../0048d/0048d518.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 161 bytes

~~~c

void _ZN5Botan11BER_Decoder9push_backERKNS_10BER_ObjectE(void)

{
  (*(code *)PTR__ZN5Botan11BER_Decoder9push_backERKNS_10BER_ObjectE_00c1c670)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdbbc0"></a> `00bdbbc0` | `10 02 00 b0` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdbbc4"></a> `00bdbbc4` | `11 3a 43 f9` | ldr x17,[x16, #0x670] | `FALL_THROUGH`
<a id="insn-00bdbbc8"></a> `00bdbbc8` | `10 c2 19 91` | add x16,x16,#0x670 | `FALL_THROUGH`
<a id="insn-00bdbbcc"></a> `00bdbbcc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdbbc0`](#insn-00bdbbc0) 範囲 `[['00bdbbc0', '00bdbbcf']]`

## 命令位置別の参照

- [`00bdbbc4`](#insn-00bdbbc4) → `00c1c670`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdbbcc`](#insn-00bdbbcc) → [`0048d518`](../0048d/0048d518.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `0048d518` · 推定シンボル `_ZN5Botan11BER_Decoder9push_backERKNS_10BER_ObjectE` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdbbc4`](#insn-00bdbbc4)

~~~json
{
  "source": "00bdbbc4",
  "target": "00c1c670",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c670",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdbbcc`](#insn-00bdbbcc)

~~~json
{
  "source": "00bdbbcc",
  "target": "0048d518",
  "target_space": "ram",
  "resolution": "function"
}
~~~
