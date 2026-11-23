# 00bddcb0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bddd60`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd60.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0016.md#compare-4f1e8f12c5622fc232806b97dc49e71d)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bddcb0",
  "name": "_ZN8firebase15CleanupNotifier16UnregisterObjectEPv",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2f0101a0ef493dd18b330e8670149c27a1df276d0bc3c26304d64a946cc333bf",
  "source_text_sha256": "2f0101a0ef493dd18b330e8670149c27a1df276d0bc3c26304d64a946cc333bf",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bddcb0",
        "00bddcbf"
      ]
    ],
    "bytes_sha256": "61c9143b4a323f285aba449853d8571d6cd45d338ee97a08d7e78398e24886bc",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00ae00b4](../00ae0/00ae00b4.md)
- [00afc4e4](../00afc/00afc4e4.md)
- [00afc5cc](../00afc/00afc5cc.md)
- [00afe698](../00afe/00afe698.md)
- [00afec34](../00afe/00afec34.md)
- [00afef50](../00afe/00afef50.md)
- [00aff368](../00aff/00aff368.md)
- [00aff79c](../00aff/00aff79c.md)
- [00b00570](../00b00/00b00570.md)
- [00b00978](../00b00/00b00978.md)
- [00b00bfc](../00b00/00b00bfc.md)
- [00b00cac](../00b00/00b00cac.md)
- [00b00d38](../00b00/00b00d38.md)
- [00b00d98](../00b00/00b00d98.md)
- [00b00e2c](../00b00/00b00e2c.md)
- [00b00ff0](../00b00/00b00ff0.md)
- [00b011d4](../00b01/00b011d4.md)
- [00b48b3c](../00b48/00b48b3c.md)
- [00b5279c](../00b52/00b5279c.md)
- [00b5a6c0](../00b5a/00b5a6c0.md)
- [00b5a784](../00b5a/00b5a784.md)
- [00b5a7cc](../00b5a/00b5a7cc.md)
- [00b5a814](../00b5a/00b5a814.md)
- [00b5a878](../00b5a/00b5a878.md)
- [00b5b008](../00b5b/00b5b008.md)

## 呼び出し先

- [00afc830](../00afc/00afc830.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 159 bytes

~~~c

void _ZN8firebase15CleanupNotifier16UnregisterObjectEPv(void)

{
  (*(code *)PTR__ZN8firebase15CleanupNotifier16UnregisterObjectEPv_00c1d690)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bddcb0"></a> `00bddcb0` | `10 02 00 90` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bddcb4"></a> `00bddcb4` | `11 4a 43 f9` | ldr x17,[x16, #0x690] | `FALL_THROUGH`
<a id="insn-00bddcb8"></a> `00bddcb8` | `10 42 1a 91` | add x16,x16,#0x690 | `FALL_THROUGH`
<a id="insn-00bddcbc"></a> `00bddcbc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bddcb0`](#insn-00bddcb0) 範囲 `[['00bddcb0', '00bddcbf']]`

## 命令位置別の参照

- [`00bddcb4`](#insn-00bddcb4) → `00c1d690`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bddcbc`](#insn-00bddcbc) → [`00afc830`](../00afc/00afc830.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00afc830` · 推定シンボル `_ZN8firebase15CleanupNotifier16UnregisterObjectEPv` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bddcb4`](#insn-00bddcb4)

~~~json
{
  "source": "00bddcb4",
  "target": "00c1d690",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1d690",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bddcbc`](#insn-00bddcbc)

~~~json
{
  "source": "00bddcbc",
  "target": "00afc830",
  "target_space": "ram",
  "resolution": "function"
}
~~~
