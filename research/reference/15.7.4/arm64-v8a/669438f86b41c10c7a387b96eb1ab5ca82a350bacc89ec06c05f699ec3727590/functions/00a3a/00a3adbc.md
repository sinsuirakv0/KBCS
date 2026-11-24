# 00a3adbc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00a3ad78`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3a/00a3ad78.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/alignment_unresolved-0002.md#compare-81b8290bb4c8b4ce56c9f8bddf10c241)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00a98cb0`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a98/00a98cb0.md) · 移動量 `+0x5def4`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/alignment_unresolved-0013.md#compare-d484ef8cee0add24d4968cd79bd8775f)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00a3adbc",
  "name": "FUN_00a3adbc",
  "size": 56,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "35a78429e0ace9c42412fde99538ab910470c948d3a50c6871fc94bc0385436e",
  "source_text_sha256": "35a78429e0ace9c42412fde99538ab910470c948d3a50c6871fc94bc0385436e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00a3adbc",
        "00a3adf3"
      ]
    ],
    "bytes_sha256": "976f0123cb6c682bb35cda1fdc5a4f42bb22cd40aa4b3c03c455902b9be7c42f",
    "instruction_count": 14,
    "instruction_bytes": 56,
    "body_bytes": 56,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb040](../00bdb/00bdb040.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 502 bytes

~~~c

void FUN_00a3adbc(long param_1)

{
  undefined8 *puVar1;
  undefined8 uVar2;
  undefined8 uVar3;
  
  puVar1 = (undefined8 *)_Znwm(0x18);
  uVar3 = *(undefined8 *)(param_1 + 0x10);
  uVar2 = *(undefined8 *)(param_1 + 8);
                    /* try { // try from 00a3add8 to 00b3ade7 has its CatchHandler @ 00a421f8 */
  *puVar1 = &PTR_FUN_00c0cc38;
  puVar1[2] = uVar3;
  puVar1[1] = uVar2;
                    /* try { // try from 00a3ade8 to 00b3ae6f has its CatchHandler @ 00a2e43c */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00a3adbc"></a> `00a3adbc` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00a3adc0"></a> `00a3adc0` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a3adc4"></a> `00a3adc4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00a3adc8"></a> `00a3adc8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00a3adcc"></a> `00a3adcc` | `00 03 80 52` | mov w0,#0x18 | `FALL_THROUGH`
<a id="insn-00a3add0"></a> `00a3add0` | `9c 80 06 94` | bl 0x00bdb040 | `UNCONDITIONAL_CALL`
<a id="insn-00a3add4"></a> `00a3add4` | `60 82 c0 3c` | ldur q0,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00a3add8"></a> `00a3add8` | `88 0e 00 d0` | adrp x8,0xc0c000 | `FALL_THROUGH`
<a id="insn-00a3addc"></a> `00a3addc` | `08 e1 30 91` | add x8,x8,#0xc38 | `FALL_THROUGH`
<a id="insn-00a3ade0"></a> `00a3ade0` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-00a3ade4"></a> `00a3ade4` | `00 80 80 3c` | stur q0,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00a3ade8"></a> `00a3ade8` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a3adec"></a> `00a3adec` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00a3adf0"></a> `00a3adf0` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00a3adbc`](#insn-00a3adbc) 範囲 `[['00a3adbc', '00a3add7']]`
  - `FALL_THROUGH` [`00a3add4`](#insn-00a3add4) → [`00a3add8`](#insn-00a3add8)
- ブロック [`00a3add8`](#insn-00a3add8) 範囲 `[['00a3add8', '00a3ade7']]`
  - `FALL_THROUGH` [`00a3ade4`](#insn-00a3ade4) → [`00a3ade8`](#insn-00a3ade8)
- ブロック [`00a3ade8`](#insn-00a3ade8) 範囲 `[['00a3ade8', '00a3adf3']]`

## 命令位置別の参照

- [`00a3adbc`](#insn-00a3adbc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3adc0`](#insn-00a3adc0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3add0`](#insn-00a3add0) → [`00bdb040`](../00bdb/00bdb040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb040` · 推定シンボル `None` · 推定型 `None`
- [`00a3ade0`](#insn-00a3ade0) → `00c0cc38`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00a3ade8`](#insn-00a3ade8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3adec`](#insn-00a3adec) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00a3adbc`](#insn-00a3adbc)

~~~json
{
  "source": "00a3adbc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3adc0`](#insn-00a3adc0)

~~~json
{
  "source": "00a3adc0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3add0`](#insn-00a3add0)

~~~json
{
  "source": "00a3add0",
  "target": "00bdb040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3ade0`](#insn-00a3ade0)

~~~json
{
  "source": "00a3ade0",
  "target": "00c0cc38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c0cc38",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00a3ade8`](#insn-00a3ade8)

~~~json
{
  "source": "00a3ade8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3adec`](#insn-00a3adec)

~~~json
{
  "source": "00a3adec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
