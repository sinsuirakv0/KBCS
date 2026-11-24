# 00aeef3c

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00aeeea0`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aee/00aeeea0.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/alignment_unresolved-0005.md#compare-11481389296ef1fe0364d7fa3e6a9040)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00aeff30`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aef/00aeff30.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/alignment_unresolved-0011.md#compare-12c5c98abf2d311f8c5c8a38f694c098)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aeef3c",
  "name": "FUN_00aeef3c",
  "size": 56,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "01433974e8fcfdea6a655ddf880a581a6f166268b17ce418eb9c01d1e6e11fed",
  "source_text_sha256": "01433974e8fcfdea6a655ddf880a581a6f166268b17ce418eb9c01d1e6e11fed",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aeef3c",
        "00aeef73"
      ]
    ],
    "bytes_sha256": "dbd7f9e112bc6f7eb423523192810a1fa3a1d5640305e80cb00e079d521b095e",
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

- [00c57f60](../00c57/00c57f60.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 502 bytes

~~~c

void FUN_00aeef3c(long param_1)

{
  undefined8 *puVar1;
  undefined8 uVar2;
  undefined8 uVar3;
  
  puVar1 = (undefined8 *)_Znwm(0x18);
                    /* try { // try from 00aeef54 to 00beef5b has its CatchHandler @ 00aef048 */
  uVar3 = *(undefined8 *)(param_1 + 0x10);
  uVar2 = *(undefined8 *)(param_1 + 8);
                    /* try { // try from 00aeef5c to 00bef077 has its CatchHandler @ 00aeee7c */
  *puVar1 = &PTR_FUN_00c8dfc8;
  puVar1[2] = uVar3;
  puVar1[1] = uVar2;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aeef3c"></a> `00aeef3c` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aeef40"></a> `00aeef40` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aeef44"></a> `00aeef44` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00aeef48"></a> `00aeef48` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aeef4c"></a> `00aeef4c` | `00 03 80 52` | mov w0,#0x18 | `FALL_THROUGH`
<a id="insn-00aeef50"></a> `00aeef50` | `04 a4 05 94` | bl 0x00c57f60 | `UNCONDITIONAL_CALL`
<a id="insn-00aeef54"></a> `00aeef54` | `60 82 c0 3c` | ldur q0,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00aeef58"></a> `00aeef58` | `e8 0c 00 f0` | adrp x8,0xc8d000 | `FALL_THROUGH`
<a id="insn-00aeef5c"></a> `00aeef5c` | `08 21 3f 91` | add x8,x8,#0xfc8 | `FALL_THROUGH`
<a id="insn-00aeef60"></a> `00aeef60` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-00aeef64"></a> `00aeef64` | `00 80 80 3c` | stur q0,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00aeef68"></a> `00aeef68` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aeef6c"></a> `00aeef6c` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aeef70"></a> `00aeef70` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aeef3c`](#insn-00aeef3c) 範囲 `[['00aeef3c', '00aeef53']]`
  - `FALL_THROUGH` [`00aeef50`](#insn-00aeef50) → [`00aeef54`](#insn-00aeef54)
- ブロック [`00aeef54`](#insn-00aeef54) 範囲 `[['00aeef54', '00aeef5b']]`
  - `FALL_THROUGH` [`00aeef58`](#insn-00aeef58) → [`00aeef5c`](#insn-00aeef5c)
- ブロック [`00aeef5c`](#insn-00aeef5c) 範囲 `[['00aeef5c', '00aeef73']]`

## 命令位置別の参照

- [`00aeef3c`](#insn-00aeef3c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeef40`](#insn-00aeef40) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeef50`](#insn-00aeef50) → [`00c57f60`](../00c57/00c57f60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f60` · 推定シンボル `None` · 推定型 `None`
- [`00aeef60`](#insn-00aeef60) → `00c8dfc8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00aeef68`](#insn-00aeef68) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeef6c`](#insn-00aeef6c) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aeef3c`](#insn-00aeef3c)

~~~json
{
  "source": "00aeef3c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeef40`](#insn-00aeef40)

~~~json
{
  "source": "00aeef40",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeef50`](#insn-00aeef50)

~~~json
{
  "source": "00aeef50",
  "target": "00c57f60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeef60`](#insn-00aeef60)

~~~json
{
  "source": "00aeef60",
  "target": "00c8dfc8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8dfc8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aeef68`](#insn-00aeef68)

~~~json
{
  "source": "00aeef68",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeef6c`](#insn-00aeef6c)

~~~json
{
  "source": "00aeef6c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
