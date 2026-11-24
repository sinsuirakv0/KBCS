# 00aeec2c

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 要確認
  - [v16.0.1 → v16.0.2 候補と検査根拠](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/review-0080.md#review-f47bf31faade0d8e2425415928629d52)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 要確認
  - [v16.0.2 → v16.0.3 候補と検査根拠](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/review-0042.md#review-f47bf31faade0d8e2425415928629d52)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aeec2c",
  "name": "FUN_00aeec2c",
  "size": 12,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "71cdb9c07e7ac0937fea64519463eba0a4d9f477c6ef820988f9b769a5e87246",
  "source_text_sha256": "71cdb9c07e7ac0937fea64519463eba0a4d9f477c6ef820988f9b769a5e87246",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aeec2c",
        "00aeec37"
      ]
    ],
    "bytes_sha256": "64655925b4c94d3ed90be8f99bb9af9893f0411b59af91d7b50f534a462f3adc",
    "instruction_count": 3,
    "instruction_bytes": 12,
    "body_bytes": 12,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 121 bytes

~~~c

pointer_____offset_0x10___ * FUN_00aeec2c(void)

{
  return &PTR__ZTVN10__cxxabiv117__class_type_infoE_16__00c8df08;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aeec2c"></a> `00aeec2c` | `e0 0c 00 f0` | adrp x0,0xc8d000 | `FALL_THROUGH`
<a id="insn-00aeec30"></a> `00aeec30` | `00 20 3c 91` | add x0,x0,#0xf08 | `FALL_THROUGH`
<a id="insn-00aeec34"></a> `00aeec34` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aeec2c`](#insn-00aeec2c) 範囲 `[['00aeec2c', '00aeec37']]`

## 命令位置別の参照

- [`00aeec30`](#insn-00aeec30) → `00c8df08`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x10)))`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aeec30`](#insn-00aeec30)

~~~json
{
  "source": "00aeec30",
  "target": "00c8df08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8df08",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
