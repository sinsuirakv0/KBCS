# 00bddda0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bddd50`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd50.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0018.md#compare-8521be9801eaeb671caaca7c2ee14ac7)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c5a800`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a800.md) · 移動量 `+0x7ca60`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/high-0011.md#compare-91d113a163fbc5a6f22dd360d4ba3fad)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bddda0",
  "name": "_ZN8firebase15CleanupNotifier14RegisterObjectEPvPFvS1_E",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7d7fa9a941de74a2123a6aa4ea03cadf04f9db78edf0c254982f7f389225d5c6",
  "source_text_sha256": "7d7fa9a941de74a2123a6aa4ea03cadf04f9db78edf0c254982f7f389225d5c6",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bddda0",
        "00bdddaf"
      ]
    ],
    "bytes_sha256": "fd42c33e27925947ebb74012be34cd9c61b8b78f8aa20e0af6c4104631b5dccc",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00ae0174](../00ae0/00ae0174.md)
- [00afe7a4](../00afe/00afe7a4.md)
- [00afed40](../00afe/00afed40.md)
- [00aff05c](../00aff/00aff05c.md)
- [00aff474](../00aff/00aff474.md)
- [00aff844](../00aff/00aff844.md)
- [00b0067c](../00b00/00b0067c.md)
- [00b00a84](../00b00/00b00a84.md)
- [00b00ca8](../00b00/00b00ca8.md)
- [00b00d58](../00b00/00b00d58.md)
- [00b00db8](../00b00/00b00db8.md)
- [00b00e44](../00b00/00b00e44.md)
- [00b00ea4](../00b00/00b00ea4.md)
- [00b010fc](../00b01/00b010fc.md)
- [00b48c08](../00b48/00b48c08.md)
- [00b525c0](../00b52/00b525c0.md)
- [00b598cc](../00b59/00b598cc.md)
- [00b5a790](../00b5a/00b5a790.md)
- [00b5a7cc](../00b5a/00b5a7cc.md)
- [00b5a84c](../00b5a/00b5a84c.md)
- [00b5a920](../00b5a/00b5a920.md)
- [00b5a984](../00b5a/00b5a984.md)
- [00b5ae68](../00b5a/00b5ae68.md)

## 呼び出し先

- [00afc80c](../00afc/00afc80c.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 169 bytes

~~~c

void _ZN8firebase15CleanupNotifier14RegisterObjectEPvPFvS1_E(void)

{
  (*(code *)PTR__ZN8firebase15CleanupNotifier14RegisterObjectEPvPFvS1_E_00c1d788)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bddda0"></a> `00bddda0` | `10 02 00 90` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bddda4"></a> `00bddda4` | `11 c6 43 f9` | ldr x17,[x16, #0x788] | `FALL_THROUGH`
<a id="insn-00bddda8"></a> `00bddda8` | `10 22 1e 91` | add x16,x16,#0x788 | `FALL_THROUGH`
<a id="insn-00bdddac"></a> `00bdddac` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bddda0`](#insn-00bddda0) 範囲 `[['00bddda0', '00bdddaf']]`

## 命令位置別の参照

- [`00bddda4`](#insn-00bddda4) → `00c1d788`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdddac`](#insn-00bdddac) → [`00afc80c`](../00afc/00afc80c.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00afc80c` · 推定シンボル `_ZN8firebase15CleanupNotifier14RegisterObjectEPvPFvS1_E` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bddda4`](#insn-00bddda4)

~~~json
{
  "source": "00bddda4",
  "target": "00c1d788",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1d788",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdddac`](#insn-00bdddac)

~~~json
{
  "source": "00bdddac",
  "target": "00afc80c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
