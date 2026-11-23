# 00bddbd0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bddc80`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddc80.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0016.md#compare-5043e32aa732abdac240f53c0d98c7a6)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bddbd0",
  "name": "_ZNK8firebase7Variant16assert_is_stringEv",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "77977e348d6dffc6e9f935fb233af530137f1474592e7eb3862ccd0f27529ec7",
  "source_text_sha256": "77977e348d6dffc6e9f935fb233af530137f1474592e7eb3862ccd0f27529ec7",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bddbd0",
        "00bddbdf"
      ]
    ],
    "bytes_sha256": "35f176c394f9b09e22f4279f59b8fca1f55f9b1cefe7c888eb8805a109e541f3",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [0084a9ec](../0084a/0084a9ec.md)
- [00ae1b58](../00ae1/00ae1b58.md)
- [00ae1d14](../00ae1/00ae1d14.md)
- [00af18f4](../00af1/00af18f4.md)
- [00b5732c](../00b57/00b5732c.md)

## 呼び出し先

- [00b044fc](../00b04/00b044fc.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 141 bytes

~~~c

void _ZNK8firebase7Variant16assert_is_stringEv(void)

{
  (*(code *)PTR__ZNK8firebase7Variant16assert_is_stringEv_00c1d620)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bddbd0"></a> `00bddbd0` | `10 02 00 90` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bddbd4"></a> `00bddbd4` | `11 12 43 f9` | ldr x17,[x16, #0x620] | `FALL_THROUGH`
<a id="insn-00bddbd8"></a> `00bddbd8` | `10 82 18 91` | add x16,x16,#0x620 | `FALL_THROUGH`
<a id="insn-00bddbdc"></a> `00bddbdc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bddbd0`](#insn-00bddbd0) 範囲 `[['00bddbd0', '00bddbdf']]`

## 命令位置別の参照

- [`00bddbd4`](#insn-00bddbd4) → `00c1d620`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bddbdc`](#insn-00bddbdc) → [`00b044fc`](../00b04/00b044fc.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00b044fc` · 推定シンボル `_ZNK8firebase7Variant16assert_is_stringEv` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bddbd4`](#insn-00bddbd4)

~~~json
{
  "source": "00bddbd4",
  "target": "00c1d620",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1d620",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bddbdc`](#insn-00bddbdc)

~~~json
{
  "source": "00bddbdc",
  "target": "00b044fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
