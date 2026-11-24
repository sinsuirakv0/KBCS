# 00bbbba4

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 対応未確定
  - [v15.7.4 → v16.0.0 版の比較一覧](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/README.md)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bbbfcc`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbb/00bbbfcc.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/machine_only_observed-0022.md#compare-08af389c4bc3a30421d7d204de5af7e5)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbbba4",
  "name": "_ZN8firebase9messaging28SetRegistrationOnInitEnabledEb",
  "size": 8,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "efafa7f6aaecbe929c9386bbe04beb413ad294e119d9b5e85a851fa83ab4c1ea",
  "source_text_sha256": "efafa7f6aaecbe929c9386bbe04beb413ad294e119d9b5e85a851fa83ab4c1ea",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbbba4",
        "00bbbbab"
      ]
    ],
    "bytes_sha256": "eb694b922fef88867aeec6d37d4040abb71b298ec29be57c8f0797d712a6d579",
    "instruction_count": 2,
    "instruction_bytes": 8,
    "body_bytes": 8,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5a6e0](../00c5a/00c5a6e0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 167 bytes

~~~c

void _ZN8firebase9messaging28SetRegistrationOnInitEnabledEb(uint param_1)

{
  _ZN8firebase9messaging33SetTokenRegistrationOnInitEnabledEb(param_1 & 1);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbbba4"></a> `00bbbba4` | `00 00 00 12` | and w0,w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bbbba8"></a> `00bbbba8` | `ce 7a 02 14` | b 0x00c5a6e0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbbba4`](#insn-00bbbba4) 範囲 `[['00bbbba4', '00bbbbab']]`

## 命令位置別の参照

- [`00bbbba8`](#insn-00bbbba8) → [`00c5a6e0`](../00c5a/00c5a6e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a6e0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbbba8`](#insn-00bbbba8)

~~~json
{
  "source": "00bbbba8",
  "target": "00c5a6e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
