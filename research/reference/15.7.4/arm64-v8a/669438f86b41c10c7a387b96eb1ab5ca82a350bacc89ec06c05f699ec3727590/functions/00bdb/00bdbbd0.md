# 00bdbbd0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdbb80`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbb80.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0013.md#compare-30de01551eadb49c8646bfdca1273323)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c58620`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58620.md) · 移動量 `+0x7ca50`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/high-0007.md#compare-72cda87c3fc8cc8a4a5d5abdbad7ccbd)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdbbd0",
  "name": "_ZN5Botan11BER_Decoder10verify_endEv",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4783cbf5720c78d1d544d4298b36d7e00ff95ee55f8820cf011866ba9ecacc35",
  "source_text_sha256": "4783cbf5720c78d1d544d4298b36d7e00ff95ee55f8820cf011866ba9ecacc35",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdbbd0",
        "00bdbbdf"
      ]
    ],
    "bytes_sha256": "b7d29897f34676b88d06db3625692a3a9574f1bebdcc0511ee85421fad392010",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [004c05ec](../004c0/004c05ec.md)
- [004c13f0](../004c1/004c13f0.md)
- [004c15a4](../004c1/004c15a4.md)
- [004dcf48](../004dc/004dcf48.md)
- [004e7c0c](../004e7/004e7c0c.md)
- [004e7de0](../004e7/004e7de0.md)
- [004e82ac](../004e8/004e82ac.md)
- [004ea2b0](../004ea/004ea2b0.md)
- [004eb16c](../004eb/004eb16c.md)
- [004f03d8](../004f0/004f03d8.md)
- [004f4778](../004f4/004f4778.md)
- [004f4ba8](../004f4/004f4ba8.md)
- [004f603c](../004f6/004f603c.md)
- [004fb0d8](../004fb/004fb0d8.md)
- [004fbe1c](../004fb/004fbe1c.md)
- [004fdfd8](../004fd/004fdfd8.md)
- [00513c60](../00513/00513c60.md)

## 呼び出し先

- [0048c9bc](../0048c/0048c9bc.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 131 bytes

~~~c

void _ZN5Botan11BER_Decoder10verify_endEv(void)

{
  (*(code *)PTR__ZN5Botan11BER_Decoder10verify_endEv_00c1c6a0)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdbbd0"></a> `00bdbbd0` | `10 02 00 b0` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdbbd4"></a> `00bdbbd4` | `11 52 43 f9` | ldr x17,[x16, #0x6a0] | `FALL_THROUGH`
<a id="insn-00bdbbd8"></a> `00bdbbd8` | `10 82 1a 91` | add x16,x16,#0x6a0 | `FALL_THROUGH`
<a id="insn-00bdbbdc"></a> `00bdbbdc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdbbd0`](#insn-00bdbbd0) 範囲 `[['00bdbbd0', '00bdbbdf']]`

## 命令位置別の参照

- [`00bdbbd4`](#insn-00bdbbd4) → `00c1c6a0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdbbdc`](#insn-00bdbbdc) → [`0048c9bc`](../0048c/0048c9bc.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `0048c9bc` · 推定シンボル `_ZN5Botan11BER_Decoder10verify_endEv` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdbbd4`](#insn-00bdbbd4)

~~~json
{
  "source": "00bdbbd4",
  "target": "00c1c6a0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c6a0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdbbdc`](#insn-00bdbbdc)

~~~json
{
  "source": "00bdbbdc",
  "target": "0048c9bc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
