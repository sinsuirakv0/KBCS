# 00bdceb0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdcf60`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcf60.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0014.md#compare-30c8db0a152f1c1e9c5276d2e1e5205a)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdceb0",
  "name": "_ZNK5Botan10Extensions10extensionsEv",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c9b337f1d5eed2fee339bd95a650628fdbc58ee72db3c43f6b75cc6abaf4237b",
  "source_text_sha256": "c9b337f1d5eed2fee339bd95a650628fdbc58ee72db3c43f6b75cc6abaf4237b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdceb0",
        "00bdcebf"
      ]
    ],
    "bytes_sha256": "6831154d50b7ce290eb3f7011870e5b754f247f862d0450e64f271d5b4e93634",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00503af8](../00503/00503af8.md)
- [005054cc](../00505/005054cc.md)

## 呼び出し先

- [004f4030](../004f4/004f4030.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 131 bytes

~~~c

void _ZNK5Botan10Extensions10extensionsEv(void)

{
  (*(code *)PTR__ZNK5Botan10Extensions10extensionsEv_00c1cf90)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdceb0"></a> `00bdceb0` | `10 02 00 90` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdceb4"></a> `00bdceb4` | `11 ca 47 f9` | ldr x17,[x16, #0xf90] | `FALL_THROUGH`
<a id="insn-00bdceb8"></a> `00bdceb8` | `10 42 3e 91` | add x16,x16,#0xf90 | `FALL_THROUGH`
<a id="insn-00bdcebc"></a> `00bdcebc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdceb0`](#insn-00bdceb0) 範囲 `[['00bdceb0', '00bdcebf']]`

## 命令位置別の参照

- [`00bdceb4`](#insn-00bdceb4) → `00c1cf90`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdcebc`](#insn-00bdcebc) → [`004f4030`](../004f4/004f4030.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `004f4030` · 推定シンボル `_ZNK5Botan10Extensions10extensionsEv` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdceb4`](#insn-00bdceb4)

~~~json
{
  "source": "00bdceb4",
  "target": "00c1cf90",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1cf90",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdcebc`](#insn-00bdcebc)

~~~json
{
  "source": "00bdcebc",
  "target": "004f4030",
  "target_space": "ram",
  "resolution": "function"
}
~~~
