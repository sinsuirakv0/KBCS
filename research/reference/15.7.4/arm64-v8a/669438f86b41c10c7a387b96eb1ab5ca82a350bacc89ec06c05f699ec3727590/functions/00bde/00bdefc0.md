# 00bdefc0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdef70`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef70.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0021.md#compare-5b2944c15843281f5717e706706e3b23)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c5ba70`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5ba70.md) · 移動量 `+0x7cab0`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/high-0014.md#compare-ee28b6cadd6a342c9ee2b25a358568a9)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdefc0",
  "name": "_ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEmc",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6fdd7ab834eba7bd6ec144f621952614cab522517c3f867b3626eae888e73b8e",
  "source_text_sha256": "6fdd7ab834eba7bd6ec144f621952614cab522517c3f867b3626eae888e73b8e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdefc0",
        "00bdefcf"
      ]
    ],
    "bytes_sha256": "46670832dfa56be92152d9da7f80417f7d331b12611c64eb90f46fc8a1b49f7d",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00b0f410](../00b0f/00b0f410.md)
- [00b10eac](../00b10/00b10eac.md)
- [00b13e3c](../00b13/00b13e3c.md)
- [00b1e1b0](../00b1e/00b1e1b0.md)
- [00b2353c](../00b23/00b2353c.md)
- [00b2b454](../00b2b/00b2b454.md)
- [00b31bb0](../00b31/00b31bb0.md)
- [00b4675c](../00b46/00b4675c.md)
- [00b4b8c8](../00b4b/00b4b8c8.md)
- [00b757f4](../00b75/00b757f4.md)
- [00b7aa80](../00b7a/00b7aa80.md)
- [00b7ac1c](../00b7a/00b7ac1c.md)
- [00b7adb4](../00b7a/00b7adb4.md)
- [00b8b11c](../00b8b/00b8b11c.md)
- [00b8b558](../00b8b/00b8b558.md)
- [00b8b994](../00b8b/00b8b994.md)
- [00b8bdd0](../00b8b/00b8bdd0.md)
- [00b8c20c](../00b8c/00b8c20c.md)
- [00b8c648](../00b8c/00b8c648.md)
- [00b8ca84](../00b8c/00b8ca84.md)
- [00b8ce9c](../00b8c/00b8ce9c.md)
- [00b8d2b4](../00b8d/00b8d2b4.md)
- [00b8d6c4](../00b8d/00b8d6c4.md)
- [00b8e5fc](../00b8e/00b8e5fc.md)
- [00b8ea2c](../00b8e/00b8ea2c.md)
- [00b8ee5c](../00b8e/00b8ee5c.md)
- [00b8f28c](../00b8f/00b8f28c.md)
- [00b8f6bc](../00b8f/00b8f6bc.md)
- [00b8faec](../00b8f/00b8faec.md)
- [00b8ff1c](../00b8f/00b8ff1c.md)
- [00b90328](../00b90/00b90328.md)
- [00b90734](../00b90/00b90734.md)
- [00b90b38](../00b90/00b90b38.md)

## 呼び出し先

- [00b2e1b4](../00b2e/00b2e1b4.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 216 bytes

~~~c

void _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEmc(void)

{
  (*(code *)
    PTR__ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEmc_00c1e098)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdefc0"></a> `00bdefc0` | `10 02 00 90` | adrp x16,0xc1e000 | `FALL_THROUGH`
<a id="insn-00bdefc4"></a> `00bdefc4` | `11 4e 40 f9` | ldr x17,[x16, #0x98] | `FALL_THROUGH`
<a id="insn-00bdefc8"></a> `00bdefc8` | `10 62 02 91` | add x16,x16,#0x98 | `FALL_THROUGH`
<a id="insn-00bdefcc"></a> `00bdefcc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdefc0`](#insn-00bdefc0) 範囲 `[['00bdefc0', '00bdefcf']]`

## 命令位置別の参照

- [`00bdefc4`](#insn-00bdefc4) → `00c1e098`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdefcc`](#insn-00bdefcc) → [`00b2e1b4`](../00b2e/00b2e1b4.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00b2e1b4` · 推定シンボル `_ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEmc` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdefc4`](#insn-00bdefc4)

~~~json
{
  "source": "00bdefc4",
  "target": "00c1e098",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1e098",
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
  "target": "00b2e1b4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
