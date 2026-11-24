# 00aadd7c

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00a4fd58`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4f/00a4fd58.md) · 移動量 `+0x5e024`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/machine_only_observed-0016.md#compare-3cfb831b3ba9a98430e9769a4a4b31f6)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00aadf78`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aad/00aadf78.md) · 移動量 `+0x1fc`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/machine_only_observed-0020.md#compare-efb970947fca9187a2a3cb74e2c5c3a8)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aadd7c",
  "name": "FUN_00aadd7c",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "50897b265d83518061236eef6845c805772ffebc0f71ada29f3d25cd57f478eb",
  "source_text_sha256": "50897b265d83518061236eef6845c805772ffebc0f71ada29f3d25cd57f478eb",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aadd7c",
        "00aadd8f"
      ]
    ],
    "bytes_sha256": "5aecec29f794424255cedd34ba08727b4edb88f56c323c8ecb532ba60e08d31e",
    "instruction_count": 5,
    "instruction_bytes": 20,
    "body_bytes": 20,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [007965f4](../00796/007965f4.md)

## 呼び出し先

- [00b32ef8](../00b32/00b32ef8.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 198 bytes

~~~c

void FUN_00aadd7c(undefined8 param_1,undefined8 param_2,undefined8 param_3,undefined8 param_4,
                 undefined8 param_5)

{
  FUN_00b32ef8(param_2,param_3,param_4,param_5);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aadd7c"></a> `00aadd7c` | `e0 03 01 aa` | mov x0,x1 | `FALL_THROUGH`
<a id="insn-00aadd80"></a> `00aadd80` | `e1 03 02 aa` | mov x1,x2 | `FALL_THROUGH`
<a id="insn-00aadd84"></a> `00aadd84` | `e2 03 03 aa` | mov x2,x3 | `FALL_THROUGH`
<a id="insn-00aadd88"></a> `00aadd88` | `e3 03 04 aa` | mov x3,x4 | `FALL_THROUGH`
<a id="insn-00aadd8c"></a> `00aadd8c` | `5b 14 02 14` | b 0x00b32ef8 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aadd7c`](#insn-00aadd7c) 範囲 `[['00aadd7c', '00aadd8f']]`

## 命令位置別の参照

- [`00aadd8c`](#insn-00aadd8c) → [`00b32ef8`](../00b32/00b32ef8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00b32ef8` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aadd8c`](#insn-00aadd8c)

~~~json
{
  "source": "00aadd8c",
  "target": "00b32ef8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
