# 009fffdc

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
  - 採用 · [関数詳細 `00a00178`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a00/00a00178.md) · 移動量 `+0x19c`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0058.md#compare-418737b97a10c2ac5a8333f520545c74)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "009fffdc",
  "name": "FUN_009fffdc",
  "size": 32,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "77fbe527e088aa149f3e51a5a106d5762fed6770664bc6f0ce8fef1338d1ecb4",
  "source_text_sha256": "77fbe527e088aa149f3e51a5a106d5762fed6770664bc6f0ce8fef1338d1ecb4",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "009fffdc",
        "009ffffb"
      ]
    ],
    "bytes_sha256": "afca2e9abbf37261c119b9948326697066c253bb7a1815313837dba5931e8fdb",
    "instruction_count": 8,
    "instruction_bytes": 32,
    "body_bytes": 32,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 252 bytes

~~~c

void FUN_009fffdc(long param_1,undefined8 *param_2)

{
  undefined8 uVar1;
  
  *param_2 = &PTR_FUN_00c8a490;
  uVar1 = *(undefined8 *)(param_1 + 8);
  *(undefined4 *)(param_2 + 2) = *(undefined4 *)(param_1 + 0x10);
  param_2[1] = uVar1;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-009fffdc"></a> `009fffdc` | `48 14 00 f0` | adrp x8,0xc8a000 | `FALL_THROUGH`
<a id="insn-009fffe0"></a> `009fffe0` | `08 41 12 91` | add x8,x8,#0x490 | `FALL_THROUGH`
<a id="insn-009fffe4"></a> `009fffe4` | `28 00 00 f9` | str x8,[x1] | `FALL_THROUGH`
<a id="insn-009fffe8"></a> `009fffe8` | `08 10 40 b9` | ldr w8,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-009fffec"></a> `009fffec` | `09 04 40 f9` | ldr x9,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-009ffff0"></a> `009ffff0` | `28 10 00 b9` | str w8,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-009ffff4"></a> `009ffff4` | `29 04 00 f9` | str x9,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-009ffff8"></a> `009ffff8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`009fffdc`](#insn-009fffdc) 範囲 `[['009fffdc', '009ffffb']]`

## 命令位置別の参照

- [`009fffe4`](#insn-009fffe4) → `00c8a490`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`009fffe4`](#insn-009fffe4)

~~~json
{
  "source": "009fffe4",
  "target": "00c8a490",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8a490",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
