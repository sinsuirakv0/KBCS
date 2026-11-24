# 00bddef0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bddea0`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddea0.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0018.md#compare-4a30a2ebc50e5f5a7dc8aed0187661f2)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c5a950`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a950.md) · 移動量 `+0x7ca60`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/high-0012.md#compare-b0c27d337c3e92411edb2faf70b8cdc5)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bddef0",
  "name": "_ZN8firebase10FutureBaseaSERKS0_",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "af0bd6a9ecb30863388cd82f3419ecaff963e88f01482ea3656b31b0076c0491",
  "source_text_sha256": "af0bd6a9ecb30863388cd82f3419ecaff963e88f01482ea3656b31b0076c0491",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bddef0",
        "00bddeff"
      ]
    ],
    "bytes_sha256": "0179272879a8b72b433a1e39787941b96ba765454edf0ea709fa2e84b62f2df3",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00ae2e60](../00ae2/00ae2e60.md)
- [00ae329c](../00ae3/00ae329c.md)
- [00b0067c](../00b00/00b0067c.md)
- [00b01560](../00b01/00b01560.md)
- [00b018f0](../00b01/00b018f0.md)
- [00b0e198](../00b0e/00b0e198.md)
- [00b4b7f4](../00b4b/00b4b7f4.md)
- [00b4d714](../00b4d/00b4d714.md)
- [00b4dcb8](../00b4d/00b4dcb8.md)
- [00b4e3ac](../00b4e/00b4e3ac.md)
- [00b4e804](../00b4e/00b4e804.md)
- [00b56790](../00b56/00b56790.md)
- [00b56abc](../00b56/00b56abc.md)
- [00b56de8](../00b56/00b56de8.md)
- [00b57110](../00b57/00b57110.md)
- [00b58078](../00b58/00b58078.md)
- [00b584cc](../00b58/00b584cc.md)
- [00b5c07c](../00b5c/00b5c07c.md)
- [00b5c10c](../00b5c/00b5c10c.md)
- [00b5c19c](../00b5c/00b5c19c.md)
- [00b5c22c](../00b5c/00b5c22c.md)
- [00b5c2bc](../00b5c/00b5c2bc.md)
- [00b5c34c](../00b5c/00b5c34c.md)
- [00b5c3dc](../00b5c/00b5c3dc.md)
- [00b6ac0c](../00b6a/00b6ac0c.md)
- [00b71fb0](../00b71/00b71fb0.md)
- [00b72040](../00b72/00b72040.md)
- [00b720d0](../00b72/00b720d0.md)
- [00b72160](../00b72/00b72160.md)
- [00b721f0](../00b72/00b721f0.md)
- [00b72280](../00b72/00b72280.md)
- [00b72310](../00b72/00b72310.md)
- [00b723a0](../00b72/00b723a0.md)
- [00b72430](../00b72/00b72430.md)
- [00b724c0](../00b72/00b724c0.md)
- [00b72550](../00b72/00b72550.md)
- [00b725e0](../00b72/00b725e0.md)
- [00b72670](../00b72/00b72670.md)

## 呼び出し先

- [00ae38d8](../00ae3/00ae38d8.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 123 bytes

~~~c

void _ZN8firebase10FutureBaseaSERKS0_(void)

{
  (*(code *)PTR__ZN8firebase10FutureBaseaSERKS0__00c1d830)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bddef0"></a> `00bddef0` | `10 02 00 90` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bddef4"></a> `00bddef4` | `11 1a 44 f9` | ldr x17,[x16, #0x830] | `FALL_THROUGH`
<a id="insn-00bddef8"></a> `00bddef8` | `10 c2 20 91` | add x16,x16,#0x830 | `FALL_THROUGH`
<a id="insn-00bddefc"></a> `00bddefc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bddef0`](#insn-00bddef0) 範囲 `[['00bddef0', '00bddeff']]`

## 命令位置別の参照

- [`00bddef4`](#insn-00bddef4) → `00c1d830`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bddefc`](#insn-00bddefc) → [`00ae38d8`](../00ae3/00ae38d8.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00ae38d8` · 推定シンボル `_ZN8firebase10FutureBaseaSERKS0_` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bddef4`](#insn-00bddef4)

~~~json
{
  "source": "00bddef4",
  "target": "00c1d830",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1d830",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bddefc`](#insn-00bddefc)

~~~json
{
  "source": "00bddefc",
  "target": "00ae38d8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
