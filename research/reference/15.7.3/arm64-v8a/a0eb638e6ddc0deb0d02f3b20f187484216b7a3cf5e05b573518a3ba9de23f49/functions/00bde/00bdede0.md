# 00bdede0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bded30`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bded30.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0019.md#compare-109f92d3223cde09f0613926871c1e3f)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bdee30`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdee30.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0020.md#compare-e513e016a3b440e4809cb8e9f49c3ad0)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdede0",
  "name": "_ZNK8firebase26ReferenceCountedFutureImpl14IsSafeToDeleteEv",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "43036376820f7c70e9802c1ceba3fb488d0ff8544059c830bdc019780c87b5e0",
  "source_text_sha256": "43036376820f7c70e9802c1ceba3fb488d0ff8544059c830bdc019780c87b5e0",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdede0",
        "00bdedef"
      ]
    ],
    "bytes_sha256": "7bf0bc6f8c8639aa43e96f9983e9293f88e7e60e5440e80d6b62e3eb6ab8be10",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00b5b0d0](../00b5b/00b5b0d0.md)

## 呼び出し先

- [00b0032c](../00b00/00b0032c.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 177 bytes

~~~c

void _ZNK8firebase26ReferenceCountedFutureImpl14IsSafeToDeleteEv(void)

{
  (*(code *)PTR__ZNK8firebase26ReferenceCountedFutureImpl14IsSafeToDeleteEv_00c1df80)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdede0"></a> `00bdede0` | `f0 01 00 f0` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bdede4"></a> `00bdede4` | `11 c2 47 f9` | ldr x17,[x16, #0xf80] | `FALL_THROUGH`
<a id="insn-00bdede8"></a> `00bdede8` | `10 02 3e 91` | add x16,x16,#0xf80 | `FALL_THROUGH`
<a id="insn-00bdedec"></a> `00bdedec` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdede0`](#insn-00bdede0) 範囲 `[['00bdede0', '00bdedef']]`

## 命令位置別の参照

- [`00bdede4`](#insn-00bdede4) → `00c1df80`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdedec`](#insn-00bdedec) → [`00b0032c`](../00b00/00b0032c.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00b0032c` · 推定シンボル `_ZNK8firebase26ReferenceCountedFutureImpl14IsSafeToDeleteEv` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdede4`](#insn-00bdede4)

~~~json
{
  "source": "00bdede4",
  "target": "00c1df80",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1df80",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdedec`](#insn-00bdedec)

~~~json
{
  "source": "00bdedec",
  "target": "00b0032c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
