# 00bddad0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 要確認
  - [v15.7.3 → v15.7.4 候補と検査根拠](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/review-0039.md#review-0c0dfa8ab26f9a1689b94d2566e333ff)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0094.md#review-0c0dfa8ab26f9a1689b94d2566e333ff)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bddad0",
  "name": "<EXTERNAL>::cosf",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0ba9a34e10348d3e5e729add6dde9cf70dd03b0cbe96291dc2e360fb625ea0ec",
  "source_text_sha256": "0ba9a34e10348d3e5e729add6dde9cf70dd03b0cbe96291dc2e360fb625ea0ec",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bddad0",
        "00bddadf"
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

- [007acf88](../007ac/007acf88.md)

## 呼び出し先

- [010a5558](../010a5/010a5558.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 190 bytes

~~~c

/* WARNING: Unknown calling convention -- yet parameter storage is locked */

float cosf(float __x)

{
  float fVar1;
  
  fVar1 = (float)(*(code *)PTR_cosf_00c1d620)();
  return fVar1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bddad0"></a> `00bddad0` | `10 02 00 90` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bddad4"></a> `00bddad4` | `11 12 43 f9` | ldr x17,[x16, #0x620] | `FALL_THROUGH`
<a id="insn-00bddad8"></a> `00bddad8` | `10 82 18 91` | add x16,x16,#0x620 | `FALL_THROUGH`
<a id="insn-00bddadc"></a> `00bddadc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bddad0`](#insn-00bddad0) 範囲 `[['00bddad0', '00bddadf']]`

## 命令位置別の参照

- [`00bddad4`](#insn-00bddad4) → `00c1d620`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bddadc`](#insn-00bddadc) → [`010a5558`](../010a5/010a5558.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `010a5558` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bddad4`](#insn-00bddad4)

~~~json
{
  "source": "00bddad4",
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
- 参照命令 [`00bddadc`](#insn-00bddadc)

~~~json
{
  "source": "00bddadc",
  "target": "010a5558",
  "target_space": "ram",
  "resolution": "function"
}
~~~
