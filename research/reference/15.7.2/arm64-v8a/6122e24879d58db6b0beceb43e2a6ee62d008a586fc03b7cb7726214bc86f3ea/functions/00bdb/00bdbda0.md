# 00bdbda0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdbe50`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbe50.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0012.md#compare-353ba09c0ed3e4fe8814f5f53082e03a)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdbda0",
  "name": "_ZN5Botan6BigInt9randomizeERNS_21RandomNumberGeneratorEmb",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8ae313a2626b59f089484c3424cbc56c38cde0f6530be37c05cddc0d6f31789f",
  "source_text_sha256": "8ae313a2626b59f089484c3424cbc56c38cde0f6530be37c05cddc0d6f31789f",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdbda0",
        "00bdbdaf"
      ]
    ],
    "bytes_sha256": "5f728c6be1459a1ce0bf1813326cf3a09b23538cdb6611309fcc2fab9530fd77",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00497bf4](../00497/00497bf4.md)
- [0049811c](../00498/0049811c.md)

## 呼び出し先

- [00497a4c](../00497/00497a4c.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 173 bytes

~~~c

void _ZN5Botan6BigInt9randomizeERNS_21RandomNumberGeneratorEmb(void)

{
  (*(code *)PTR__ZN5Botan6BigInt9randomizeERNS_21RandomNumberGeneratorEmb_00c1c708)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdbda0"></a> `00bdbda0` | `10 02 00 b0` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdbda4"></a> `00bdbda4` | `11 86 43 f9` | ldr x17,[x16, #0x708] | `FALL_THROUGH`
<a id="insn-00bdbda8"></a> `00bdbda8` | `10 22 1c 91` | add x16,x16,#0x708 | `FALL_THROUGH`
<a id="insn-00bdbdac"></a> `00bdbdac` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdbda0`](#insn-00bdbda0) 範囲 `[['00bdbda0', '00bdbdaf']]`

## 命令位置別の参照

- [`00bdbda4`](#insn-00bdbda4) → `00c1c708`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdbdac`](#insn-00bdbdac) → [`00497a4c`](../00497/00497a4c.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00497a4c` · 推定シンボル `_ZN5Botan6BigInt9randomizeERNS_21RandomNumberGeneratorEmb` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdbda4`](#insn-00bdbda4)

~~~json
{
  "source": "00bdbda4",
  "target": "00c1c708",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c708",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdbdac`](#insn-00bdbdac)

~~~json
{
  "source": "00bdbdac",
  "target": "00497a4c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
