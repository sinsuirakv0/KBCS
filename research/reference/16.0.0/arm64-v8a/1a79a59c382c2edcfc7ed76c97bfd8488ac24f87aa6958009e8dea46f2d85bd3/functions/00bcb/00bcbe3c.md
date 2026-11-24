# 00bcbe3c

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b5c93c`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c93c.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/high-0004.md#compare-238a1cdfc8f82dc73770a076c07d1ada)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bcc264`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc264.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/high-0009.md#compare-8277f0b5db902a0198386c941645d3bd)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcbe3c",
  "name": "_ZN8firebase4auth4UserC2Ev",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "277cbbc2c7f76a0deee2f1d75531ef11945adec78b263674431b7dccc2bccf2b",
  "source_text_sha256": "277cbbc2c7f76a0deee2f1d75531ef11945adec78b263674431b7dccc2bccf2b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcbe3c",
        "00bcbe7b"
      ]
    ],
    "bytes_sha256": "4d137e862dcbcbd6490473daedcdaa9119e38c0c6cc52db8fd0db35d6b0077df",
    "instruction_count": 16,
    "instruction_bytes": 64,
    "body_bytes": 64,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5d760](../00c5d/00c5d760.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 540 bytes

~~~c

void _ZN8firebase4auth4UserC2Ev(long *param_1)

{
  undefined *puVar1;
  
  puVar1 = PTR__ZTVN8firebase4auth4UserE_00c9b5c0;
  param_1[0x12] = 0;
  param_1[0x11] = 0;
  param_1[0x10] = 0;
  param_1[0xf] = 0;
  param_1[0xe] = 0;
  param_1[0xd] = 0;
  param_1[0xc] = 0;
  param_1[0xb] = 0;
  param_1[10] = 0;
  param_1[9] = 0;
  param_1[8] = 0;
  param_1[7] = 0;
  param_1[6] = 0;
  param_1[5] = 0;
  param_1[4] = 0;
  param_1[3] = 0;
  param_1[2] = 0;
  param_1[1] = 0;
  *param_1 = (long)(puVar1 + 0x10);
  param_1[0x13] = 0;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcbe3c"></a> `00bcbe3c` | `88 06 00 90` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bcbe40"></a> `00bcbe40` | `08 e1 42 f9` | ldr x8,[x8, #0x5c0] | `FALL_THROUGH`
<a id="insn-00bcbe44"></a> `00bcbe44` | `00 e4 00 6f` | movi v0.2D,#0x0 | `FALL_THROUGH`
<a id="insn-00bcbe48"></a> `00bcbe48` | `00 80 88 3c` | stur q0,[x0, #0x88] | `FALL_THROUGH`
<a id="insn-00bcbe4c"></a> `00bcbe4c` | `00 80 87 3c` | stur q0,[x0, #0x78] | `FALL_THROUGH`
<a id="insn-00bcbe50"></a> `00bcbe50` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00bcbe54"></a> `00bcbe54` | `00 80 86 3c` | stur q0,[x0, #0x68] | `FALL_THROUGH`
<a id="insn-00bcbe58"></a> `00bcbe58` | `00 80 85 3c` | stur q0,[x0, #0x58] | `FALL_THROUGH`
<a id="insn-00bcbe5c"></a> `00bcbe5c` | `00 80 84 3c` | stur q0,[x0, #0x48] | `FALL_THROUGH`
<a id="insn-00bcbe60"></a> `00bcbe60` | `00 80 83 3c` | stur q0,[x0, #0x38] | `FALL_THROUGH`
<a id="insn-00bcbe64"></a> `00bcbe64` | `00 80 82 3c` | stur q0,[x0, #0x28] | `FALL_THROUGH`
<a id="insn-00bcbe68"></a> `00bcbe68` | `00 80 81 3c` | stur q0,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00bcbe6c"></a> `00bcbe6c` | `00 80 80 3c` | stur q0,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bcbe70"></a> `00bcbe70` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-00bcbe74"></a> `00bcbe74` | `1f 4c 00 f9` | str xzr,[x0, #0x98] | `FALL_THROUGH`
<a id="insn-00bcbe78"></a> `00bcbe78` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcbe3c`](#insn-00bcbe3c) 範囲 `[['00bcbe3c', '00bcbe7b']]`

## 命令位置別の参照

- [`00bcbe40`](#insn-00bcbe40) → `00c9b5c0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bcbe70`](#insn-00bcbe70) → `00c924a8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[80]`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcbe40`](#insn-00bcbe40)

~~~json
{
  "source": "00bcbe40",
  "target": "00c9b5c0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b5c0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bcbe70`](#insn-00bcbe70)

~~~json
{
  "source": "00bcbe70",
  "target": "00c924a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c92498",
  "offset": 16,
  "size": 80,
  "datatype": "undefined1[80]",
  "capture_state": "contains_relocation"
}
~~~
