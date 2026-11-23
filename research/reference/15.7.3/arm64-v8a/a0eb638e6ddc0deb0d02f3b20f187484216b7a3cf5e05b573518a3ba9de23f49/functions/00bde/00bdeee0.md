# 00bdeee0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bdee30`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdee30.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0019.md#compare-ab6c854bb8f8f2ecbbff1c6335617406)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bdef30`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdef30.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0020.md#compare-cb511c80cccfe7717699ddc4e12e68c7)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdeee0",
  "name": "_ZNK8firebase7Variant14mutable_stringEv",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3b898b1675f231edf302c3967cc9d04cac010ca2c5b8ec0658e7847dc982ed20",
  "source_text_sha256": "3b898b1675f231edf302c3967cc9d04cac010ca2c5b8ec0658e7847dc982ed20",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdeee0",
        "00bdeeef"
      ]
    ],
    "bytes_sha256": "6c76baf6ea53f54c25f40afc66926ff836fdbac79a1dccb409d433840db82477",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00b02e7c](../00b02/00b02e7c.md)

## 呼び出し先

- [00b0347c](../00b03/00b0347c.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 137 bytes

~~~c

void _ZNK8firebase7Variant14mutable_stringEv(void)

{
  (*(code *)PTR__ZNK8firebase7Variant14mutable_stringEv_00c1e000)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdeee0"></a> `00bdeee0` | `10 02 00 90` | adrp x16,0xc1e000 | `FALL_THROUGH`
<a id="insn-00bdeee4"></a> `00bdeee4` | `11 02 40 f9` | ldr x17,[x16] | `FALL_THROUGH`
<a id="insn-00bdeee8"></a> `00bdeee8` | `10 02 00 91` | add x16,x16,#0x0 | `FALL_THROUGH`
<a id="insn-00bdeeec"></a> `00bdeeec` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdeee0`](#insn-00bdeee0) 範囲 `[['00bdeee0', '00bdeeef']]`

## 命令位置別の参照

- [`00bdeee4`](#insn-00bdeee4) → `00c1e000`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdeeec`](#insn-00bdeeec) → [`00b0347c`](../00b03/00b0347c.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00b0347c` · 推定シンボル `_ZNK8firebase7Variant14mutable_stringEv` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdeee4`](#insn-00bdeee4)

~~~json
{
  "source": "00bdeee4",
  "target": "00c1e000",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1e000",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdeeec`](#insn-00bdeeec)

~~~json
{
  "source": "00bdeeec",
  "target": "00b0347c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
