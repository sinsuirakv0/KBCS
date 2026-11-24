# 005dddbc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `005b90ec`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b9/005b90ec.md) · 移動量 `+0x24cd0`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/no_difference_in_scope-0003.md#compare-f2150da8ac1b9ded23f58577688bb19b)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `005dddfc`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005dd/005dddfc.md) · 移動量 `+0x40`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/no_difference_in_scope-0003.md#compare-edd4577acc4da2bebe2184c72f926c45)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "005dddbc",
  "name": "FUN_005dddbc",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "368c67aa82ce90cd98969b6676ce19a0c9310110da88783d51b7eb54e87ea278",
  "source_text_sha256": "368c67aa82ce90cd98969b6676ce19a0c9310110da88783d51b7eb54e87ea278",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "005dddbc",
        "005ddde7"
      ]
    ],
    "bytes_sha256": "cd9632380879bedcbbecb2d33c7341565110b7f1de33d24608b8bd01062b07d6",
    "instruction_count": 11,
    "instruction_bytes": 44,
    "body_bytes": 44,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [005eba30](../005eb/005eba30.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 392 bytes

~~~c

void FUN_005dddbc(undefined1 *param_1)

{
  *param_1 = 0;
  param_1[0x24] = 0;
  *(undefined8 *)(param_1 + 0x28) = 0;
  param_1[0x30] = 0;
  *(undefined8 *)(param_1 + 0xc) = 0;
  *(undefined8 *)(param_1 + 4) = 0;
  *(undefined8 *)(param_1 + 0x1c) = 0;
  *(undefined8 *)(param_1 + 0x14) = 0;
  *(undefined8 *)(param_1 + 0x34) = 0;
  *(undefined4 *)(param_1 + 0x3c) = 0xffffffff;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-005dddbc"></a> `005dddbc` | `00 e4 00 6f` | movi v0.2D,#0x0 | `FALL_THROUGH`
<a id="insn-005dddc0"></a> `005dddc0` | `08 00 80 12` | mov w8,#0xffffffff | `FALL_THROUGH`
<a id="insn-005dddc4"></a> `005dddc4` | `1f 00 00 39` | strb wzr,[x0] | `FALL_THROUGH`
<a id="insn-005dddc8"></a> `005dddc8` | `1f 90 00 39` | strb wzr,[x0, #0x24] | `FALL_THROUGH`
<a id="insn-005dddcc"></a> `005dddcc` | `1f 14 00 f9` | str xzr,[x0, #0x28] | `FALL_THROUGH`
<a id="insn-005dddd0"></a> `005dddd0` | `1f c0 00 39` | strb wzr,[x0, #0x30] | `FALL_THROUGH`
<a id="insn-005dddd4"></a> `005dddd4` | `00 40 80 3c` | stur q0,[x0, #0x4] | `FALL_THROUGH`
<a id="insn-005dddd8"></a> `005dddd8` | `00 40 81 3c` | stur q0,[x0, #0x14] | `FALL_THROUGH`
<a id="insn-005ddddc"></a> `005ddddc` | `1f 40 03 f8` | stur xzr,[x0, #0x34] | `FALL_THROUGH`
<a id="insn-005ddde0"></a> `005ddde0` | `08 3c 00 b9` | str w8,[x0, #0x3c] | `FALL_THROUGH`
<a id="insn-005ddde4"></a> `005ddde4` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`005dddbc`](#insn-005dddbc) 範囲 `[['005dddbc', '005ddde7']]`

## 命令位置別の参照


## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

