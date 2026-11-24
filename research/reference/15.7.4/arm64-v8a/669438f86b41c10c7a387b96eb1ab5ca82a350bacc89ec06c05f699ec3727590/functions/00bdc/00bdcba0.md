# 00bdcba0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdcb50`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcb50.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0015.md#compare-620b4f586d1ccbf424bdaf2598420145)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c595f0`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595f0.md) · 移動量 `+0x7ca50`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/high-0009.md#compare-5f4e968887adc70ccf13fdfb57ffeb73)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdcba0",
  "name": "_ZNK5Botan16X509_Certificate4dataEv",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7d3f401dae6df84265be8a202dd379a077d675290a9351225fc90e76b1797928",
  "source_text_sha256": "7d3f401dae6df84265be8a202dd379a077d675290a9351225fc90e76b1797928",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdcba0",
        "00bdcbaf"
      ]
    ],
    "bytes_sha256": "772531a47c489f1135d32f4b89fae91e635075f479faf95bfe3ea6ad91261912",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [004de868](../004de/004de868.md)
- [004de908](../004de/004de908.md)
- [004de9a8](../004de/004de9a8.md)
- [004deb44](../004de/004deb44.md)
- [004ded14](../004de/004ded14.md)
- [004def78](../004de/004def78.md)
- [004df278](../004df/004df278.md)
- [004df290](../004df/004df290.md)
- [004df598](../004df/004df598.md)
- [004dfa64](../004df/004dfa64.md)
- [004dfc1c](../004df/004dfc1c.md)
- [004dfc4c](../004df/004dfc4c.md)
- [004e0038](../004e0/004e0038.md)
- [004e4494](../004e4/004e4494.md)
- [004e4bdc](../004e4/004e4bdc.md)
- [004e66d0](../004e6/004e66d0.md)
- [004e8a14](../004e8/004e8a14.md)
- [004e8fec](../004e8/004e8fec.md)
- [004e9100](../004e9/004e9100.md)
- [004e9148](../004e9/004e9148.md)
- [004e939c](../004e9/004e939c.md)
- [004e97e0](../004e9/004e97e0.md)
- [004e9d34](../004e9/004e9d34.md)
- [004ecb70](../004ec/004ecb70.md)
- [004ed038](../004ed/004ed038.md)
- [004edb24](../004ed/004edb24.md)
- [004ede80](../004ed/004ede80.md)
- [004ef204](../004ef/004ef204.md)
- [004f00b0](../004f0/004f00b0.md)
- [004f8244](../004f8/004f8244.md)
- [004f8990](../004f8/004f8990.md)
- [004ffa88](../004ff/004ffa88.md)
- [004ffaa0](../004ff/004ffaa0.md)
- [004ffab8](../004ff/004ffab8.md)
- [004ffad0](../004ff/004ffad0.md)
- [004ffae8](../004ff/004ffae8.md)
- [004ffb00](../004ff/004ffb00.md)
- [004ffb18](../004ff/004ffb18.md)
- [004ffb30](../004ff/004ffb30.md)
- [004ffb48](../004ff/004ffb48.md)
- [004ffb60](../004ff/004ffb60.md)
- [004ffb78](../004ff/004ffb78.md)
- [004ffb90](../004ff/004ffb90.md)
- [004ffba8](../004ff/004ffba8.md)
- [004ffbc0](../004ff/004ffbc0.md)
- [004ffbd8](../004ff/004ffbd8.md)
- [004ffbf0](../004ff/004ffbf0.md)
- [004ffc88](../004ff/004ffc88.md)
- [004ffed4](../004ff/004ffed4.md)
- [004fff1c](../004ff/004fff1c.md)
- [0050003c](../00500/0050003c.md)
- [005000cc](../00500/005000cc.md)
- [00500120](../00500/00500120.md)
- [00500168](../00500/00500168.md)
- [005001dc](../00500/005001dc.md)
- [005001f4](../00500/005001f4.md)
- [00500938](../00500/00500938.md)
- [00500f10](../00500/00500f10.md)
- [00501084](../00501/00501084.md)
- [00501274](../00501/00501274.md)
- [0050140c](../00501/0050140c.md)
- [00501664](../00501/00501664.md)
- [00501b08](../00501/00501b08.md)
- [00503af8](../00503/00503af8.md)
- [005054cc](../00505/005054cc.md)
- [0050645c](../00506/0050645c.md)
- [00506ee0](../00506/00506ee0.md)

## 呼び出し先

- [004ff98c](../004ff/004ff98c.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 129 bytes

~~~c

void _ZNK5Botan16X509_Certificate4dataEv(void)

{
  (*(code *)PTR__ZNK5Botan16X509_Certificate4dataEv_00c1ce88)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdcba0"></a> `00bdcba0` | `10 02 00 90` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdcba4"></a> `00bdcba4` | `11 46 47 f9` | ldr x17,[x16, #0xe88] | `FALL_THROUGH`
<a id="insn-00bdcba8"></a> `00bdcba8` | `10 22 3a 91` | add x16,x16,#0xe88 | `FALL_THROUGH`
<a id="insn-00bdcbac"></a> `00bdcbac` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdcba0`](#insn-00bdcba0) 範囲 `[['00bdcba0', '00bdcbaf']]`

## 命令位置別の参照

- [`00bdcba4`](#insn-00bdcba4) → `00c1ce88`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdcbac`](#insn-00bdcbac) → [`004ff98c`](../004ff/004ff98c.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `004ff98c` · 推定シンボル `_ZNK5Botan16X509_Certificate4dataEv` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdcba4`](#insn-00bdcba4)

~~~json
{
  "source": "00bdcba4",
  "target": "00c1ce88",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1ce88",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdcbac`](#insn-00bdcbac)

~~~json
{
  "source": "00bdcbac",
  "target": "004ff98c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
