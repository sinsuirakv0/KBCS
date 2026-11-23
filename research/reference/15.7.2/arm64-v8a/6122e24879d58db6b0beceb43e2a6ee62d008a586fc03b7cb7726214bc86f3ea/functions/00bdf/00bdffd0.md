# 00bdffd0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00be0080`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0080.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0022.md#compare-f5a18eb8b1f82fe3a253fde5a6b1e56e)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdffd0",
  "name": "_ZNSt6__ndk16vectorIhNS_9allocatorIhEEE6insertENS_11__wrap_iterIPKhEEmRS5_",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d0c061558eebd7523d783883d2569abe11ddb0d3d112192e71a31f0d3388b5ae",
  "source_text_sha256": "d0c061558eebd7523d783883d2569abe11ddb0d3d112192e71a31f0d3388b5ae",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdffd0",
        "00bdffdf"
      ]
    ],
    "bytes_sha256": "e88d7522a8e7dad5c538c87b18db61516df409a97f51506ec1332817f0195d02",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00b261c4](../00b26/00b261c4.md)
- [00b3203c](../00b32/00b3203c.md)
- [00b33b54](../00b33/00b33b54.md)

## 呼び出し先

- [00b33294](../00b33/00b33294.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 220 bytes

~~~c

void _ZNSt6__ndk16vectorIhNS_9allocatorIhEEE6insertENS_11__wrap_iterIPKhEEmRS5_(void)

{
  (*(code *)PTR__ZNSt6__ndk16vectorIhNS_9allocatorIhEEE6insertENS_11__wrap_iterIPKhEEmRS5__00c1e820)
            ();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdffd0"></a> `00bdffd0` | `f0 01 00 f0` | adrp x16,0xc1e000 | `FALL_THROUGH`
<a id="insn-00bdffd4"></a> `00bdffd4` | `11 12 44 f9` | ldr x17,[x16, #0x820] | `FALL_THROUGH`
<a id="insn-00bdffd8"></a> `00bdffd8` | `10 82 20 91` | add x16,x16,#0x820 | `FALL_THROUGH`
<a id="insn-00bdffdc"></a> `00bdffdc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdffd0`](#insn-00bdffd0) 範囲 `[['00bdffd0', '00bdffdf']]`

## 命令位置別の参照

- [`00bdffd4`](#insn-00bdffd4) → `00c1e820`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdffdc`](#insn-00bdffdc) → [`00b33294`](../00b33/00b33294.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00b33294` · 推定シンボル `_ZNSt6__ndk16vectorIhNS_9allocatorIhEEE6insertENS_11__wrap_iterIPKhEEmRS5_` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdffd4`](#insn-00bdffd4)

~~~json
{
  "source": "00bdffd4",
  "target": "00c1e820",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1e820",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdffdc`](#insn-00bdffdc)

~~~json
{
  "source": "00bdffdc",
  "target": "00b33294",
  "target_space": "ram",
  "resolution": "function"
}
~~~
