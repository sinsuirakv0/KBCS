# 00bdbdd0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdbd80`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbd80.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0013.md#compare-b9933821b8dce1809077ef41172e8295)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0094.md#review-f22d60120dfe410c7a9585bd8c55b82c)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdbdd0",
  "name": "_ZN5Botan6BigIntC2ENS0_4SignEm",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2161789b8e2c70861265ce341b48ecd2362ef304d21a6b17f14d0501365620bd",
  "source_text_sha256": "2161789b8e2c70861265ce341b48ecd2362ef304d21a6b17f14d0501365620bd",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdbdd0",
        "00bdbddf"
      ]
    ],
    "bytes_sha256": "d48f1893c001e6b7dbf8a2e7762bb9d551dce2f2c9327a11e32004e4fe4c5c00",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00493850](../00493/00493850.md)
- [00496ee0](../00496/00496ee0.md)
- [00497068](../00497/00497068.md)
- [0049731c](../00497/0049731c.md)
- [00497724](../00497/00497724.md)
- [00497874](../00497/00497874.md)
- [004b77d0](../004b7/004b77d0.md)
- [004b8210](../004b8/004b8210.md)
- [004b868c](../004b8/004b868c.md)
- [004b87c8](../004b8/004b87c8.md)
- [004bc804](../004bc/004bc804.md)
- [004bd550](../004bd/004bd550.md)
- [004be0f4](../004be/004be0f4.md)

## 呼び出し先

- [00497d5c](../00497/00497d5c.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 119 bytes

~~~c

void _ZN5Botan6BigIntC2ENS0_4SignEm(void)

{
  (*(code *)PTR__ZN5Botan6BigIntC2ENS0_4SignEm_00c1c7a0)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdbdd0"></a> `00bdbdd0` | `10 02 00 b0` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdbdd4"></a> `00bdbdd4` | `11 d2 43 f9` | ldr x17,[x16, #0x7a0] | `FALL_THROUGH`
<a id="insn-00bdbdd8"></a> `00bdbdd8` | `10 82 1e 91` | add x16,x16,#0x7a0 | `FALL_THROUGH`
<a id="insn-00bdbddc"></a> `00bdbddc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdbdd0`](#insn-00bdbdd0) 範囲 `[['00bdbdd0', '00bdbddf']]`

## 命令位置別の参照

- [`00bdbdd4`](#insn-00bdbdd4) → `00c1c7a0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdbddc`](#insn-00bdbddc) → [`00497d5c`](../00497/00497d5c.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00497d5c` · 推定シンボル `_ZN5Botan6BigIntC2ENS0_4SignEm` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdbdd4`](#insn-00bdbdd4)

~~~json
{
  "source": "00bdbdd4",
  "target": "00c1c7a0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c7a0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdbddc`](#insn-00bdbddc)

~~~json
{
  "source": "00bdbddc",
  "target": "00497d5c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
