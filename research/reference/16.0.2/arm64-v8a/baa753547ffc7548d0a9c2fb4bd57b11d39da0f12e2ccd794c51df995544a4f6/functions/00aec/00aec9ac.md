# 00aec9ac

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00aec910`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aec/00aec910.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/alignment_unresolved-0005.md#compare-c5b62f075a71cbd89c12681704a294ee)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00aed9a0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aed/00aed9a0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0067.md#compare-6d6cef5cdd62c4076648a123a84581f3)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aec9ac",
  "name": "FUN_00aec9ac",
  "size": 52,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2082b525469a91b690cedfde74da6dcf684d336738dfa5483f80fb422b896541",
  "source_text_sha256": "2082b525469a91b690cedfde74da6dcf684d336738dfa5483f80fb422b896541",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aec9ac",
        "00aec9df"
      ]
    ],
    "bytes_sha256": "d9701c63f125ca2cccb7008b154e1d1fcaa1250c21ece75a24b46e6eb2af375d",
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

- [00c57f60](../00c57/00c57f60.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 657 bytes

~~~c

void FUN_00aec9ac(long param_1)

{
  undefined8 *puVar1;
  undefined8 uVar2;
  
                    /* try { // try from 00aec9b0 to 00bec9f7 has its CatchHandler @ 00aec9b0
                       catch() { ... } // from try @ 00aec9b0 with catch @ 00aec9b0
                       catch() { ... } // from try @ 00aecaf8 with catch @ 00aec9b0
                       catch() { ... } // from try @ 00aecc8c with catch @ 00aec9b0
                       catch() { ... } // from try @ 00aecdcc with catch @ 00aec9b0 */
  puVar1 = (undefined8 *)_Znwm(0x10);
  uVar2 = *(undefined8 *)(param_1 + 8);
  *puVar1 = &PTR_FUN_00c8dac8;
  puVar1[1] = uVar2;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aec9ac"></a> `00aec9ac` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aec9b0"></a> `00aec9b0` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aec9b4"></a> `00aec9b4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00aec9b8"></a> `00aec9b8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aec9bc"></a> `00aec9bc` | `00 02 80 52` | mov w0,#0x10 | `FALL_THROUGH`
<a id="insn-00aec9c0"></a> `00aec9c0` | `68 ad 05 94` | bl 0x00c57f60 | `UNCONDITIONAL_CALL`
<a id="insn-00aec9c4"></a> `00aec9c4` | `69 06 40 f9` | ldr x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00aec9c8"></a> `00aec9c8` | `08 0d 00 b0` | adrp x8,0xc8d000 | `FALL_THROUGH`
<a id="insn-00aec9cc"></a> `00aec9cc` | `08 21 2b 91` | add x8,x8,#0xac8 | `FALL_THROUGH`
<a id="insn-00aec9d0"></a> `00aec9d0` | `08 24 00 a9` | stp x8,x9,[x0] | `FALL_THROUGH`
<a id="insn-00aec9d4"></a> `00aec9d4` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aec9d8"></a> `00aec9d8` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aec9dc"></a> `00aec9dc` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aec9ac`](#insn-00aec9ac) 範囲 `[['00aec9ac', '00aec9af']]`
  - `FALL_THROUGH` [`00aec9ac`](#insn-00aec9ac) → [`00aec9b0`](#insn-00aec9b0)
- ブロック [`00aec9b0`](#insn-00aec9b0) 範囲 `[['00aec9b0', '00aec9df']]`

## 命令位置別の参照

- [`00aec9ac`](#insn-00aec9ac) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aec9b0`](#insn-00aec9b0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aec9c0`](#insn-00aec9c0) → [`00c57f60`](../00c57/00c57f60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f60` · 推定シンボル `None` · 推定型 `None`
- [`00aec9d0`](#insn-00aec9d0) → `00c8dac8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00aec9d4`](#insn-00aec9d4) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aec9d8`](#insn-00aec9d8) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aec9ac`](#insn-00aec9ac)

~~~json
{
  "source": "00aec9ac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aec9b0`](#insn-00aec9b0)

~~~json
{
  "source": "00aec9b0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aec9c0`](#insn-00aec9c0)

~~~json
{
  "source": "00aec9c0",
  "target": "00c57f60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aec9d0`](#insn-00aec9d0)

~~~json
{
  "source": "00aec9d0",
  "target": "00c8dac8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8dac8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aec9d4`](#insn-00aec9d4)

~~~json
{
  "source": "00aec9d4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aec9d8`](#insn-00aec9d8)

~~~json
{
  "source": "00aec9d8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
