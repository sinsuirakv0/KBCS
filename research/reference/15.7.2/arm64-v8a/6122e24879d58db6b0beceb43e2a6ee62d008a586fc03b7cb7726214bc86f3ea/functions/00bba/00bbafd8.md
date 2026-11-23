# 00bbafd8

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bbb0a0`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb0a0.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0010.md#compare-9312c04caa5a035f93e3fe91ffa3deb9)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbafd8",
  "name": "_ZNSt8bad_castC1Ev",
  "size": 24,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a924d8fa41a617d23a3f4988c13f148765c8f20710ee742d597a07231c8eaf45",
  "source_text_sha256": "a924d8fa41a617d23a3f4988c13f148765c8f20710ee742d597a07231c8eaf45",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbafd8",
        "00bbafef"
      ]
    ],
    "bytes_sha256": "18cbb840d371fa74bf34310cf8bd04ad6c673670bdea87756a1b9fd830abadc7",
    "instruction_count": 6,
    "instruction_bytes": 24,
    "body_bytes": 24,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00be1380](../00be1/00be1380.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 114 bytes

~~~c

void _ZNSt8bad_castC1Ev(long *param_1)

{
  *param_1 = (long)(PTR__ZTVSt8bad_cast_00c1bf38 + 0x10);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbafd8"></a> `00bbafd8` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bbafdc"></a> `00bbafdc` | `08 03 00 b0` | adrp x8,0xc1b000 | `FALL_THROUGH`
<a id="insn-00bbafe0"></a> `00bbafe0` | `08 9d 47 f9` | ldr x8,[x8, #0xf38] | `FALL_THROUGH`
<a id="insn-00bbafe4"></a> `00bbafe4` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00bbafe8"></a> `00bbafe8` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-00bbafec"></a> `00bbafec` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbafd8`](#insn-00bbafd8) 範囲 `[['00bbafd8', '00bbafef']]`

## 命令位置別の参照

- [`00bbafe0`](#insn-00bbafe0) → `00c1bf38`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bbafe8`](#insn-00bbafe8) → `00c16a70`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[40]`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbafe0`](#insn-00bbafe0)

~~~json
{
  "source": "00bbafe0",
  "target": "00c1bf38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1bf38",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbafe8`](#insn-00bbafe8)

~~~json
{
  "source": "00bbafe8",
  "target": "00c16a70",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c16a60",
  "offset": 16,
  "size": 40,
  "datatype": "undefined1[40]",
  "capture_state": "contains_relocation"
}
~~~
