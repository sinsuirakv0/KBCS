# 00bdcea0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdce50`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdce50.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0016.md#compare-6f20916894c55693b55408290d85c595)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c598f0`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c598f0.md) · 移動量 `+0x7ca50`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/high-0009.md#compare-c7e4f301ee28dd1ebd520aa9f26642c4)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdcea0",
  "name": "_ZNK5Botan14PKCS10_Request14ex_constraintsEv",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "badac66f9fcbb0aef199e27f74564353161d6f9ae6cb161071b3b121c474cd65",
  "source_text_sha256": "badac66f9fcbb0aef199e27f74564353161d6f9ae6cb161071b3b121c474cd65",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdcea0",
        "00bdceaf"
      ]
    ],
    "bytes_sha256": "d20c56700dd87c9c04d095950c1c8f7215d28bffae199db21d4ab851eacf6d71",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [004ede80](../004ed/004ede80.md)

## 呼び出し先

- [004ec514](../004ec/004ec514.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 147 bytes

~~~c

void _ZNK5Botan14PKCS10_Request14ex_constraintsEv(void)

{
  (*(code *)PTR__ZNK5Botan14PKCS10_Request14ex_constraintsEv_00c1d008)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdcea0"></a> `00bdcea0` | `10 02 00 b0` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bdcea4"></a> `00bdcea4` | `11 06 40 f9` | ldr x17,[x16, #0x8] | `FALL_THROUGH`
<a id="insn-00bdcea8"></a> `00bdcea8` | `10 22 00 91` | add x16,x16,#0x8 | `FALL_THROUGH`
<a id="insn-00bdceac"></a> `00bdceac` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdcea0`](#insn-00bdcea0) 範囲 `[['00bdcea0', '00bdceaf']]`

## 命令位置別の参照

- [`00bdcea4`](#insn-00bdcea4) → `00c1d008`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdceac`](#insn-00bdceac) → [`004ec514`](../004ec/004ec514.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `004ec514` · 推定シンボル `_ZNK5Botan14PKCS10_Request14ex_constraintsEv` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdcea4`](#insn-00bdcea4)

~~~json
{
  "source": "00bdcea4",
  "target": "00c1d008",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1d008",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdceac`](#insn-00bdceac)

~~~json
{
  "source": "00bdceac",
  "target": "004ec514",
  "target_space": "ram",
  "resolution": "function"
}
~~~
