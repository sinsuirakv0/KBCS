# 00bdfaa0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bdf9f0`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf9f0.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0021.md#compare-5b7ade698aa23e408a6ac46ea5d4ca62)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bdfaf0`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfaf0.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0022.md#compare-189d6852a82204e8754c09aef9b718b1)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdfaa0",
  "name": "_ZN11flexbuffers7Builder10CreateBlobEPKvmmNS_4TypeE",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c373f6f4ab22f714946efa8d1a7af085e428eafa34523237e4a694b1166a68cd",
  "source_text_sha256": "c373f6f4ab22f714946efa8d1a7af085e428eafa34523237e4a694b1166a68cd",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdfaa0",
        "00bdfaaf"
      ]
    ],
    "bytes_sha256": "c5fdd6fc911db61ed0a8d100e6b26a196fe45228050e4c916b7a8af18e42f199",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00b33ac4](../00b33/00b33ac4.md)

## 呼び出し先

- [00b33c1c](../00b33/00b33c1c.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 161 bytes

~~~c

void _ZN11flexbuffers7Builder10CreateBlobEPKvmmNS_4TypeE(void)

{
  (*(code *)PTR__ZN11flexbuffers7Builder10CreateBlobEPKvmmNS_4TypeE_00c1e5e0)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdfaa0"></a> `00bdfaa0` | `f0 01 00 f0` | adrp x16,0xc1e000 | `FALL_THROUGH`
<a id="insn-00bdfaa4"></a> `00bdfaa4` | `11 f2 42 f9` | ldr x17,[x16, #0x5e0] | `FALL_THROUGH`
<a id="insn-00bdfaa8"></a> `00bdfaa8` | `10 82 17 91` | add x16,x16,#0x5e0 | `FALL_THROUGH`
<a id="insn-00bdfaac"></a> `00bdfaac` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdfaa0`](#insn-00bdfaa0) 範囲 `[['00bdfaa0', '00bdfaaf']]`

## 命令位置別の参照

- [`00bdfaa4`](#insn-00bdfaa4) → `00c1e5e0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdfaac`](#insn-00bdfaac) → [`00b33c1c`](../00b33/00b33c1c.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00b33c1c` · 推定シンボル `_ZN11flexbuffers7Builder10CreateBlobEPKvmmNS_4TypeE` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdfaa4`](#insn-00bdfaa4)

~~~json
{
  "source": "00bdfaa4",
  "target": "00c1e5e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1e5e0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdfaac`](#insn-00bdfaac)

~~~json
{
  "source": "00bdfaac",
  "target": "00b33c1c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
