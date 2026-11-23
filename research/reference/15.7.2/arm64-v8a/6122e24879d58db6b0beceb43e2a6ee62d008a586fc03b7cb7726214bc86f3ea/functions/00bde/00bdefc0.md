# 00bdefc0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdf070`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf070.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0019.md#compare-64e0cdf25f24d1f5a7b7a89b00c87a28)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdefc0",
  "name": "_ZN10reflection11EnumBuilder12add_is_unionEb",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "cb594b40ec2b094e20b2f6b66e8c674babe67dd733e49e434feee6bb47f2903c",
  "source_text_sha256": "cb594b40ec2b094e20b2f6b66e8c674babe67dd733e49e434feee6bb47f2903c",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdefc0",
        "00bdefcf"
      ]
    ],
    "bytes_sha256": "bf51f788de0fb42d2e21bd511748ec980e25ddbc7332661188a384423a07517e",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00b29390](../00b29/00b29390.md)

## 呼び出し先

- [00b34f54](../00b34/00b34f54.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 147 bytes

~~~c

void _ZN10reflection11EnumBuilder12add_is_unionEb(void)

{
  (*(code *)PTR__ZN10reflection11EnumBuilder12add_is_unionEb_00c1e018)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdefc0"></a> `00bdefc0` | `10 02 00 90` | adrp x16,0xc1e000 | `FALL_THROUGH`
<a id="insn-00bdefc4"></a> `00bdefc4` | `11 0e 40 f9` | ldr x17,[x16, #0x18] | `FALL_THROUGH`
<a id="insn-00bdefc8"></a> `00bdefc8` | `10 62 00 91` | add x16,x16,#0x18 | `FALL_THROUGH`
<a id="insn-00bdefcc"></a> `00bdefcc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdefc0`](#insn-00bdefc0) 範囲 `[['00bdefc0', '00bdefcf']]`

## 命令位置別の参照

- [`00bdefc4`](#insn-00bdefc4) → `00c1e018`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdefcc`](#insn-00bdefcc) → [`00b34f54`](../00b34/00b34f54.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00b34f54` · 推定シンボル `_ZN10reflection11EnumBuilder12add_is_unionEb` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdefc4`](#insn-00bdefc4)

~~~json
{
  "source": "00bdefc4",
  "target": "00c1e018",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1e018",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdefcc`](#insn-00bdefcc)

~~~json
{
  "source": "00bdefcc",
  "target": "00b34f54",
  "target_space": "ram",
  "resolution": "function"
}
~~~
