# 00bcbeb0

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b5c9b0`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c9b0.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/inspection-0019.md#compare-43ade96bd95729efa387ef77804cd81d)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bcc2d8`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc2d8.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0039.md#compare-84ae7ad3a1feaa207ce9f60f152eb97a)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcbeb0",
  "name": "_ZNK8firebase4auth4UserneERKS1_",
  "size": 52,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2913831d54303c2433eff895af8bc88f8fb5d1ca167486668c33f8c0ee299d7a",
  "source_text_sha256": "2913831d54303c2433eff895af8bc88f8fb5d1ca167486668c33f8c0ee299d7a",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcbeb0",
        "00bcbee3"
      ]
    ],
    "bytes_sha256": "ee9745d0e2b4a9e3f5a340124e19a3f633ffab25eb148336e9307fe28f1e8b0b",
    "instruction_count": 13,
    "instruction_bytes": 52,
    "body_bytes": 52,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5a660](../00c5a/00c5a660.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 247 bytes

~~~c

uint _ZNK8firebase4auth4UserneERKS1_(undefined8 param_1,undefined8 param_2)

{
  uint uVar1;
  uint uVar2;
  
  uVar1 = _ZNK8firebase4auth4User8is_validEv();
  uVar2 = _ZNK8firebase4auth4User8is_validEv(param_2);
  return (uVar1 ^ uVar2) & 1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcbeb0"></a> `00bcbeb0` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bcbeb4"></a> `00bcbeb4` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbeb8"></a> `00bcbeb8` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bcbebc"></a> `00bcbebc` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bcbec0"></a> `00bcbec0` | `e8 39 02 94` | bl 0x00c5a660 | `UNCONDITIONAL_CALL`
<a id="insn-00bcbec4"></a> `00bcbec4` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00bcbec8"></a> `00bcbec8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcbecc"></a> `00bcbecc` | `e5 39 02 94` | bl 0x00c5a660 | `UNCONDITIONAL_CALL`
<a id="insn-00bcbed0"></a> `00bcbed0` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbed4"></a> `00bcbed4` | `88 02 00 4a` | eor w8,w20,w0 | `FALL_THROUGH`
<a id="insn-00bcbed8"></a> `00bcbed8` | `00 01 00 12` | and w0,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bcbedc"></a> `00bcbedc` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bcbee0"></a> `00bcbee0` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcbeb0`](#insn-00bcbeb0) 範囲 `[['00bcbeb0', '00bcbee3']]`

## 命令位置別の参照

- [`00bcbeb0`](#insn-00bcbeb0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbeb4`](#insn-00bcbeb4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbec0`](#insn-00bcbec0) → [`00c5a660`](../00c5a/00c5a660.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a660` · 推定シンボル `None` · 推定型 `None`
- [`00bcbecc`](#insn-00bcbecc) → [`00c5a660`](../00c5a/00c5a660.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a660` · 推定シンボル `None` · 推定型 `None`
- [`00bcbed0`](#insn-00bcbed0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcbeb0`](#insn-00bcbeb0)

~~~json
{
  "source": "00bcbeb0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbeb4`](#insn-00bcbeb4)

~~~json
{
  "source": "00bcbeb4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbec0`](#insn-00bcbec0)

~~~json
{
  "source": "00bcbec0",
  "target": "00c5a660",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbecc`](#insn-00bcbecc)

~~~json
{
  "source": "00bcbecc",
  "target": "00c5a660",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbed0`](#insn-00bcbed0)

~~~json
{
  "source": "00bcbed0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
