# 00bddff0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bddfa0`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddfa0.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0018.md#compare-d1eafa5968725722ef35192b85198237)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c5aa70`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa70.md) · 移動量 `+0x7ca80`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/high-0012.md#compare-bf3b56b42faddf9ffb99901aab67f121)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bddff0",
  "name": "_ZN8firebase26ReferenceCountedFutureImpl15SetBackingErrorEPNS_17FutureBackingDataEiPKc",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4f8058ac8889c38ed0c51d79a1d88dc382f509f86a2780b3aff2fa9cb5ae2fdf",
  "source_text_sha256": "4f8058ac8889c38ed0c51d79a1d88dc382f509f86a2780b3aff2fa9cb5ae2fdf",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bddff0",
        "00bddfff"
      ]
    ],
    "bytes_sha256": "d8adde1e776060a4c4a1f65a36fd6fafddd4ac142edb9737b75b9b80f41dcd9a",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00ae3598](../00ae3/00ae3598.md)
- [00ae3bc4](../00ae3/00ae3bc4.md)
- [00ae3ce8](../00ae3/00ae3ce8.md)
- [00ae3e50](../00ae3/00ae3e50.md)
- [00b5a09c](../00b5a/00b5a09c.md)
- [00b5a1c8](../00b5a/00b5a1c8.md)
- [00b5a2f8](../00b5a/00b5a2f8.md)
- [00b5a4ac](../00b5a/00b5a4ac.md)
- [00b5fffc](../00b5f/00b5fffc.md)
- [00b601d8](../00b60/00b601d8.md)
- [00b604f0](../00b60/00b604f0.md)
- [00b606dc](../00b60/00b606dc.md)
- [00b608b8](../00b60/00b608b8.md)
- [00b60a90](../00b60/00b60a90.md)
- [00b60c6c](../00b60/00b60c6c.md)
- [00b6cb2c](../00b6c/00b6cb2c.md)
- [00b6d330](../00b6d/00b6d330.md)
- [00b71984](../00b71/00b71984.md)
- [00b71b60](../00b71/00b71b60.md)

## 呼び出し先

- [00aff21c](../00aff/00aff21c.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 239 bytes

~~~c

void _ZN8firebase26ReferenceCountedFutureImpl15SetBackingErrorEPNS_17FutureBackingDataEiPKc(void)

{
  (*(code *)
    PTR__ZN8firebase26ReferenceCountedFutureImpl15SetBackingErrorEPNS_17FutureBackingDataEiPKc_00c1d8b0
  )();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bddff0"></a> `00bddff0` | `10 02 00 90` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bddff4"></a> `00bddff4` | `11 5a 44 f9` | ldr x17,[x16, #0x8b0] | `FALL_THROUGH`
<a id="insn-00bddff8"></a> `00bddff8` | `10 c2 22 91` | add x16,x16,#0x8b0 | `FALL_THROUGH`
<a id="insn-00bddffc"></a> `00bddffc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bddff0`](#insn-00bddff0) 範囲 `[['00bddff0', '00bddfff']]`

## 命令位置別の参照

- [`00bddff4`](#insn-00bddff4) → `00c1d8b0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bddffc`](#insn-00bddffc) → [`00aff21c`](../00aff/00aff21c.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00aff21c` · 推定シンボル `_ZN8firebase26ReferenceCountedFutureImpl15SetBackingErrorEPNS_17FutureBackingDataEiPKc` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bddff4`](#insn-00bddff4)

~~~json
{
  "source": "00bddff4",
  "target": "00c1d8b0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1d8b0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bddffc`](#insn-00bddffc)

~~~json
{
  "source": "00bddffc",
  "target": "00aff21c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
