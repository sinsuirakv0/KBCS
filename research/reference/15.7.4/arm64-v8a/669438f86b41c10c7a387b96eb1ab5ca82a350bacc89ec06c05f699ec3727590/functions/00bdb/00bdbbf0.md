# 00bdbbf0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdbba0`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbba0.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0013.md#compare-42e4e875d460dea7ef64b6c61976d28e)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0094.md#review-eaecbda78e9a4d53dc2a662e277c1b7d)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdbbf0",
  "name": "_ZNSt9bad_allocC2Ev",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "44bcb762865be52c47fbf39889cc254497a55aa4b723416a755dc04215fda441",
  "source_text_sha256": "44bcb762865be52c47fbf39889cc254497a55aa4b723416a755dc04215fda441",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdbbf0",
        "00bdbbff"
      ]
    ],
    "bytes_sha256": "255eeb5e59c18736f1aec26cd94d9cfee74df01555f0a5f22ce3e2cd6a40c294",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [0048cd38](../0048c/0048cd38.md)
- [0048df5c](../0048d/0048df5c.md)
- [00490630](../00490/00490630.md)
- [00495978](../00495/00495978.md)
- [004a1040](../004a1/004a1040.md)
- [004a1190](../004a1/004a1190.md)
- [004a1328](../004a1/004a1328.md)
- [004a15d0](../004a1/004a15d0.md)
- [004a5bdc](../004a5/004a5bdc.md)
- [004a6378](../004a6/004a6378.md)
- [004a6590](../004a6/004a6590.md)
- [004a6c9c](../004a6/004a6c9c.md)
- [004a710c](../004a7/004a710c.md)
- [004a728c](../004a7/004a728c.md)
- [004a7444](../004a7/004a7444.md)
- [004a76c0](../004a7/004a76c0.md)
- [004a8854](../004a8/004a8854.md)
- [004a8a10](../004a8/004a8a10.md)
- [004a8bc4](../004a8/004a8bc4.md)
- [004a8d78](../004a8/004a8d78.md)
- [004b76d8](../004b7/004b76d8.md)
- [004bf57c](../004bf/004bf57c.md)
- [004d989c](../004d9/004d989c.md)
- [005132d4](../00513/005132d4.md)
- [00513e2c](../00513/00513e2c.md)
- [0051d3cc](../0051d/0051d3cc.md)
- [0051d4f0](../0051d/0051d4f0.md)
- [0051d614](../0051d/0051d614.md)
- [0051da48](../0051d/0051da48.md)
- [0051dbb0](../0051d/0051dbb0.md)
- [0051dca0](../0051d/0051dca0.md)
- [0051e054](../0051e/0051e054.md)
- [0051e2cc](../0051e/0051e2cc.md)
- [005204e8](../00520/005204e8.md)
- [00520804](../00520/00520804.md)
- [00520980](../00520/00520980.md)
- [00520afc](../00520/00520afc.md)
- [00521e04](../00521/00521e04.md)
- [00b736e8](../00b73/00b736e8.md)
- [00bdaea4](../00bda/00bdaea4.md)
- [00bdaf18](../00bda/00bdaf18.md)

## 呼び出し先

- [00bbadb4](../00bba/00bbadb4.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 97 bytes

~~~c

void _ZNSt9bad_allocC2Ev(void)

{
  (*(code *)PTR__ZNSt9bad_allocC2Ev_00c1c6b0)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdbbf0"></a> `00bdbbf0` | `10 02 00 b0` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdbbf4"></a> `00bdbbf4` | `11 5a 43 f9` | ldr x17,[x16, #0x6b0] | `FALL_THROUGH`
<a id="insn-00bdbbf8"></a> `00bdbbf8` | `10 c2 1a 91` | add x16,x16,#0x6b0 | `FALL_THROUGH`
<a id="insn-00bdbbfc"></a> `00bdbbfc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdbbf0`](#insn-00bdbbf0) 範囲 `[['00bdbbf0', '00bdbbff']]`

## 命令位置別の参照

- [`00bdbbf4`](#insn-00bdbbf4) → `00c1c6b0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdbbfc`](#insn-00bdbbfc) → [`00bbadb4`](../00bba/00bbadb4.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00bbadb4` · 推定シンボル `_ZNSt9bad_allocC2Ev` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdbbf4`](#insn-00bdbbf4)

~~~json
{
  "source": "00bdbbf4",
  "target": "00c1c6b0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c6b0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdbbfc`](#insn-00bdbbfc)

~~~json
{
  "source": "00bdbbfc",
  "target": "00bbadb4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
