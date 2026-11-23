# 00bddbb0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bddc60`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddc60.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0016.md#compare-4ce53d473b1c9dca65c8462d9c29fc47)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bddbb0",
  "name": "_ZNK8firebase7Variant14assert_is_typeENS0_4TypeE",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c332afb5366236319e16874fb65683caf8ff60abb925c5a0e936ad3d20cadc49",
  "source_text_sha256": "c332afb5366236319e16874fb65683caf8ff60abb925c5a0e936ad3d20cadc49",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bddbb0",
        "00bddbbf"
      ]
    ],
    "bytes_sha256": "a7af47f782b7e25cdcf356ddf5bca2734ab68a2ba5904233b369e1e22f59eb13",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [0084a918](../0084a/0084a918.md)
- [00ae1a54](../00ae1/00ae1a54.md)
- [00ae1d14](../00ae1/00ae1d14.md)
- [00af18f4](../00af1/00af18f4.md)
- [00b5732c](../00b57/00b5732c.md)

## 呼び出し先

- [00b04448](../00b04/00b04448.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 155 bytes

~~~c

void _ZNK8firebase7Variant14assert_is_typeENS0_4TypeE(void)

{
  (*(code *)PTR__ZNK8firebase7Variant14assert_is_typeENS0_4TypeE_00c1d610)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bddbb0"></a> `00bddbb0` | `10 02 00 90` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bddbb4"></a> `00bddbb4` | `11 0a 43 f9` | ldr x17,[x16, #0x610] | `FALL_THROUGH`
<a id="insn-00bddbb8"></a> `00bddbb8` | `10 42 18 91` | add x16,x16,#0x610 | `FALL_THROUGH`
<a id="insn-00bddbbc"></a> `00bddbbc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bddbb0`](#insn-00bddbb0) 範囲 `[['00bddbb0', '00bddbbf']]`

## 命令位置別の参照

- [`00bddbb4`](#insn-00bddbb4) → `00c1d610`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bddbbc`](#insn-00bddbbc) → [`00b04448`](../00b04/00b04448.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00b04448` · 推定シンボル `_ZNK8firebase7Variant14assert_is_typeENS0_4TypeE` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bddbb4`](#insn-00bddbb4)

~~~json
{
  "source": "00bddbb4",
  "target": "00c1d610",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1d610",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bddbbc`](#insn-00bddbbc)

~~~json
{
  "source": "00bddbbc",
  "target": "00b04448",
  "target_space": "ram",
  "resolution": "function"
}
~~~
