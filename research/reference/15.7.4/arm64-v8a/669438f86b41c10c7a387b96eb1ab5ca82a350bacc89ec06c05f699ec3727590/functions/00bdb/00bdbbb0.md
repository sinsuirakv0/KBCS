# 00bdbbb0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdbb60`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbb60.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0013.md#compare-419f87e83d3de7690eb956ae8fa11fb1)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c58600`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58600.md) · 移動量 `+0x7ca50`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/high-0007.md#compare-6bbfe647f871cf25e06d1a92b0d12f3a)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdbbb0",
  "name": "_ZNK5Botan14calendar_point16to_std_timepointEv",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "193e06a7bc474996f8dbd4241f7367ce09761c6f90e891ca15aaa3bcfecf4095",
  "source_text_sha256": "193e06a7bc474996f8dbd4241f7367ce09761c6f90e891ca15aaa3bcfecf4095",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdbbb0",
        "00bdbbbf"
      ]
    ],
    "bytes_sha256": "edf87e17a5bf153b4223b6c8eb1ef8424fc9999c73b3a79ff8ca22ffbefa6d1a",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [0048c288](../0048c/0048c288.md)

## 呼び出し先

- [0048c2e0](../0048c/0048c2e0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 151 bytes

~~~c

void _ZNK5Botan14calendar_point16to_std_timepointEv(void)

{
  (*(code *)PTR__ZNK5Botan14calendar_point16to_std_timepointEv_00c1c690)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdbbb0"></a> `00bdbbb0` | `10 02 00 b0` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdbbb4"></a> `00bdbbb4` | `11 4a 43 f9` | ldr x17,[x16, #0x690] | `FALL_THROUGH`
<a id="insn-00bdbbb8"></a> `00bdbbb8` | `10 42 1a 91` | add x16,x16,#0x690 | `FALL_THROUGH`
<a id="insn-00bdbbbc"></a> `00bdbbbc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdbbb0`](#insn-00bdbbb0) 範囲 `[['00bdbbb0', '00bdbbbf']]`

## 命令位置別の参照

- [`00bdbbb4`](#insn-00bdbbb4) → `00c1c690`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdbbbc`](#insn-00bdbbbc) → [`0048c2e0`](../0048c/0048c2e0.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `0048c2e0` · 推定シンボル `_ZNK5Botan14calendar_point16to_std_timepointEv` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdbbb4`](#insn-00bdbbb4)

~~~json
{
  "source": "00bdbbb4",
  "target": "00c1c690",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c690",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdbbbc`](#insn-00bdbbbc)

~~~json
{
  "source": "00bdbbbc",
  "target": "0048c2e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
