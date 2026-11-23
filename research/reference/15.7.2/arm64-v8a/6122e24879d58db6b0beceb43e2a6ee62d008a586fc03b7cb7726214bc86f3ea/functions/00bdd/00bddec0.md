# 00bddec0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bddf70`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf70.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0017.md#compare-2c071895d28a1855fe41e6bef37b0779)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bddec0",
  "name": "_ZN8firebase26ReferenceCountedFutureImpl13AllocInternalEiPvPFvS1_E",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6f7f3e34e31e9bd6796f308d8071849c76d0a09c9a216fdaec4c55548d4fa660",
  "source_text_sha256": "6f7f3e34e31e9bd6796f308d8071849c76d0a09c9a216fdaec4c55548d4fa660",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bddec0",
        "00bddecf"
      ]
    ],
    "bytes_sha256": "4335c93d01357725fa821fa7fa84ded1c078c44a9b22cce95da4ec77ab9cf36a",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00ae2b00](../00ae2/00ae2b00.md)
- [00ae2ec8](../00ae2/00ae2ec8.md)
- [00b00570](../00b00/00b00570.md)
- [00b01454](../00b01/00b01454.md)
- [00b0de68](../00b0d/00b0de68.md)
- [00b4b5c0](../00b4b/00b4b5c0.md)
- [00b4d13c](../00b4d/00b4d13c.md)
- [00b4d6e0](../00b4d/00b4d6e0.md)
- [00b4dd3c](../00b4d/00b4dd3c.md)
- [00b4e378](../00b4e/00b4e378.md)
- [00b563e8](../00b56/00b563e8.md)
- [00b56714](../00b56/00b56714.md)
- [00b56a40](../00b56/00b56a40.md)
- [00b56d6c](../00b56/00b56d6c.md)
- [00b57094](../00b57/00b57094.md)
- [00b5732c](../00b57/00b5732c.md)
- [00b57a40](../00b57/00b57a40.md)
- [00b57ffc](../00b57/00b57ffc.md)
- [00b5e17c](../00b5e/00b5e17c.md)
- [00b5e858](../00b5e/00b5e858.md)
- [00b5ec94](../00b5e/00b5ec94.md)
- [00b5fa7c](../00b5f/00b5fa7c.md)
- [00b6a9dc](../00b6a/00b6a9dc.md)
- [00b6c138](../00b6c/00b6c138.md)
- [00b6ede4](../00b6e/00b6ede4.md)
- [00b6fd1c](../00b6f/00b6fd1c.md)
- [00b6ff44](../00b6f/00b6ff44.md)
- [00b70a1c](../00b70/00b70a1c.md)
- [00b70c0c](../00b70/00b70c0c.md)
- [00b71060](../00b71/00b71060.md)
- [00b71250](../00b71/00b71250.md)
- [00b71478](../00b71/00b71478.md)

## 呼び出し先

- [00afec34](../00afe/00afec34.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 191 bytes

~~~c

void _ZN8firebase26ReferenceCountedFutureImpl13AllocInternalEiPvPFvS1_E(void)

{
  (*(code *)PTR__ZN8firebase26ReferenceCountedFutureImpl13AllocInternalEiPvPFvS1_E_00c1d798)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bddec0"></a> `00bddec0` | `10 02 00 90` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bddec4"></a> `00bddec4` | `11 ce 43 f9` | ldr x17,[x16, #0x798] | `FALL_THROUGH`
<a id="insn-00bddec8"></a> `00bddec8` | `10 62 1e 91` | add x16,x16,#0x798 | `FALL_THROUGH`
<a id="insn-00bddecc"></a> `00bddecc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bddec0`](#insn-00bddec0) 範囲 `[['00bddec0', '00bddecf']]`

## 命令位置別の参照

- [`00bddec4`](#insn-00bddec4) → `00c1d798`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bddecc`](#insn-00bddecc) → [`00afec34`](../00afe/00afec34.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00afec34` · 推定シンボル `_ZN8firebase26ReferenceCountedFutureImpl13AllocInternalEiPvPFvS1_E` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bddec4`](#insn-00bddec4)

~~~json
{
  "source": "00bddec4",
  "target": "00c1d798",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1d798",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bddecc`](#insn-00bddecc)

~~~json
{
  "source": "00bddecc",
  "target": "00afec34",
  "target_space": "ram",
  "resolution": "function"
}
~~~
