# 00bdddd0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bddd80`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd80.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0018.md#compare-e6144d0298af08811f09a16840cc0d2b)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0094.md#review-3ce9ea4f6f907b2d7e6953c6e26c3026)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdddd0",
  "name": "_ZN8firebase15CleanupNotifierD2Ev",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "45cad2daa1d02c16ddf7fef005b24b94a4d8afd8af678a89711adbd0f510957f",
  "source_text_sha256": "45cad2daa1d02c16ddf7fef005b24b94a4d8afd8af678a89711adbd0f510957f",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdddd0",
        "00bddddf"
      ]
    ],
    "bytes_sha256": "c31d4328042e62cafb156c5231e4f76657a46717d554b705b7c220eeea55cdb8",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00af8e94](../00af8/00af8e94.md)
- [00afaecc](../00afa/00afaecc.md)
- [00afaf9c](../00afa/00afaf9c.md)
- [00afeb24](../00afe/00afeb24.md)
- [00b55838](../00b55/00b55838.md)

## 呼び出し先

- [00afc5f0](../00afc/00afc5f0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 125 bytes

~~~c

void _ZN8firebase15CleanupNotifierD2Ev(void)

{
  (*(code *)PTR__ZN8firebase15CleanupNotifierD2Ev_00c1d7a0)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdddd0"></a> `00bdddd0` | `10 02 00 90` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bdddd4"></a> `00bdddd4` | `11 d2 43 f9` | ldr x17,[x16, #0x7a0] | `FALL_THROUGH`
<a id="insn-00bdddd8"></a> `00bdddd8` | `10 82 1e 91` | add x16,x16,#0x7a0 | `FALL_THROUGH`
<a id="insn-00bddddc"></a> `00bddddc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdddd0`](#insn-00bdddd0) 範囲 `[['00bdddd0', '00bddddf']]`

## 命令位置別の参照

- [`00bdddd4`](#insn-00bdddd4) → `00c1d7a0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bddddc`](#insn-00bddddc) → [`00afc5f0`](../00afc/00afc5f0.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00afc5f0` · 推定シンボル `_ZN8firebase15CleanupNotifierD2Ev` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdddd4`](#insn-00bdddd4)

~~~json
{
  "source": "00bdddd4",
  "target": "00c1d7a0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1d7a0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bddddc`](#insn-00bddddc)

~~~json
{
  "source": "00bddddc",
  "target": "00afc5f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
