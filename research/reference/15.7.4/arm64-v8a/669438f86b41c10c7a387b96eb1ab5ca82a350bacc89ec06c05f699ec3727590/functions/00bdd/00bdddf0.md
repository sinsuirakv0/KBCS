# 00bdddf0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bddda0`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddda0.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0018.md#compare-ca5aac789fdbd464d9b1f075e4b6c9b4)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0094.md#review-b56dd70c5a9b071b7a56ff376401e50e)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdddf0",
  "name": "_ZN8firebase26ReferenceCountedFutureImplD1Ev",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "133e716738d3f0f24fa2989b43a4b53eb12101f44f8c2205a1f81966d2f6b752",
  "source_text_sha256": "133e716738d3f0f24fa2989b43a4b53eb12101f44f8c2205a1f81966d2f6b752",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdddf0",
        "00bdddff"
      ]
    ],
    "bytes_sha256": "4e26d70cbe5ad9d1b51e70737eee38a5539eeb2a9aee5b0e06a90962823a41dd",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00ae0128](../00ae0/00ae0128.md)
- [00b013f4](../00b01/00b013f4.md)
- [00b01454](../00b01/00b01454.md)
- [00b02260](../00b02/00b02260.md)
- [00b0d784](../00b0d/00b0d784.md)
- [00b0db90](../00b0d/00b0db90.md)
- [00b494c0](../00b49/00b494c0.md)
- [00b5253c](../00b52/00b5253c.md)
- [00b55838](../00b55/00b55838.md)
- [00b5b370](../00b5b/00b5b370.md)

## 呼び出し先

- [00afeb24](../00afe/00afeb24.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 147 bytes

~~~c

void _ZN8firebase26ReferenceCountedFutureImplD1Ev(void)

{
  (*(code *)PTR__ZN8firebase26ReferenceCountedFutureImplD1Ev_00c1d7b0)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdddf0"></a> `00bdddf0` | `10 02 00 90` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bdddf4"></a> `00bdddf4` | `11 da 43 f9` | ldr x17,[x16, #0x7b0] | `FALL_THROUGH`
<a id="insn-00bdddf8"></a> `00bdddf8` | `10 c2 1e 91` | add x16,x16,#0x7b0 | `FALL_THROUGH`
<a id="insn-00bdddfc"></a> `00bdddfc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdddf0`](#insn-00bdddf0) 範囲 `[['00bdddf0', '00bdddff']]`

## 命令位置別の参照

- [`00bdddf4`](#insn-00bdddf4) → `00c1d7b0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdddfc`](#insn-00bdddfc) → [`00afeb24`](../00afe/00afeb24.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00afeb24` · 推定シンボル `_ZN8firebase26ReferenceCountedFutureImplD1Ev` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdddf4`](#insn-00bdddf4)

~~~json
{
  "source": "00bdddf4",
  "target": "00c1d7b0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1d7b0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdddfc`](#insn-00bdddfc)

~~~json
{
  "source": "00bdddfc",
  "target": "00afeb24",
  "target_space": "ram",
  "resolution": "function"
}
~~~
