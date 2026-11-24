# 00bcffec

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bcff50`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcff50.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0082.md#compare-8affffe5b4238b2f0f2b75c763f3f5c9)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bd0fe0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd0/00bd0fe0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0036.md#compare-9152ec0f4eaf945c387c789b2d727e1e)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcffec",
  "name": "_ZN8firebase6FutureINS_4auth10AuthResultEEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE",
  "size": 124,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c978b6a19a360d3ead809f673307e1ee601625444d56061f63f61acb6b8b78f3",
  "source_text_sha256": "c978b6a19a360d3ead809f673307e1ee601625444d56061f63f61acb6b8b78f3",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcffec",
        "00bd0067"
      ]
    ],
    "bytes_sha256": "640d8eedd5b5cdcd42186b0e40e64954c77d76561b3f5d5a8db8d5d40b7be93c",
    "instruction_count": 31,
    "instruction_bytes": 124,
    "body_bytes": 124,
    "indirect": 2,
    "unresolved": 2
  }
}
~~~

## 呼び出し元

- [00c5de00](../00c5d/00c5de00.md)

## 呼び出し先

- [00c5ad40](../00c5a/00c5ad40.md)
- [00c5aec0](../00c5a/00c5aec0.md)
- [00c5aed0](../00c5a/00c5aed0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 843 bytes

~~~c

void _ZN8firebase6FutureINS_4auth10AuthResultEEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE
               (long param_1,undefined8 param_2,undefined8 param_3)

{
  long lVar1;
  long *plVar2;
  
                    /* try { // try from 00bcffec to 00ccfff7 has its CatchHandler @ 00bd03e4 */
                    /* try { // try from 00bcfff8 to 00cd01bf has its CatchHandler @ 00bcfd30 */
  _ZN8firebase5MutexC1ENS0_4ModeE(param_1,0);
  *(undefined8 *)(param_1 + 0x28) = param_2;
  lVar1 = param_1 + 0x30;
  _ZN8firebase12FutureHandleC1ERKS0_(lVar1,param_3);
  (**(code **)(**(long **)(param_1 + 0x28) + 0x10))(*(long **)(param_1 + 0x28),lVar1);
  _ZN8firebase12FutureHandle6DetachEv(lVar1);
  plVar2 = *(long **)(param_1 + 0x28);
  if (plVar2 != (long *)0x0) {
    (**(code **)(*plVar2 + 0x58))(plVar2,param_1);
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcffec"></a> `00bcffec` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bcfff0"></a> `00bcfff0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcfff4"></a> `00bcfff4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcfff8"></a> `00bcfff8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bcfffc"></a> `00bcfffc` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00bd0000"></a> `00bd0000` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00bd0004"></a> `00bd0004` | `f5 03 02 aa` | mov x21,x2 | `FALL_THROUGH`
<a id="insn-00bd0008"></a> `00bd0008` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bd000c"></a> `00bd000c` | `4d 2b 02 94` | bl 0x00c5ad40 | `UNCONDITIONAL_CALL`
<a id="insn-00bd0010"></a> `00bd0010` | `74 16 00 f9` | str x20,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00bd0014"></a> `00bd0014` | `74 c2 00 91` | add x20,x19,#0x30 | `FALL_THROUGH`
<a id="insn-00bd0018"></a> `00bd0018` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bd001c"></a> `00bd001c` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bd0020"></a> `00bd0020` | `ac 2b 02 94` | bl 0x00c5aed0 | `UNCONDITIONAL_CALL`
<a id="insn-00bd0024"></a> `00bd0024` | `60 16 40 f9` | ldr x0,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00bd0028"></a> `00bd0028` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bd002c"></a> `00bd002c` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00bd0030"></a> `00bd0030` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bd0034"></a> `00bd0034` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bd0038"></a> `00bd0038` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bd003c"></a> `00bd003c` | `a1 2b 02 94` | bl 0x00c5aec0 | `UNCONDITIONAL_CALL`
<a id="insn-00bd0040"></a> `00bd0040` | `60 16 40 f9` | ldr x0,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00bd0044"></a> `00bd0044` | `a0 00 00 b4` | cbz x0,0x00bd0058 | `CONDITIONAL_JUMP`
<a id="insn-00bd0048"></a> `00bd0048` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bd004c"></a> `00bd004c` | `08 2d 40 f9` | ldr x8,[x8, #0x58] | `FALL_THROUGH`
<a id="insn-00bd0050"></a> `00bd0050` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bd0054"></a> `00bd0054` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bd0058"></a> `00bd0058` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bd005c"></a> `00bd005c` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd0060"></a> `00bd0060` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bd0064"></a> `00bd0064` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcffec`](#insn-00bcffec) 範囲 `[['00bcffec', '00bcfff7']]`
  - `FALL_THROUGH` [`00bcfff4`](#insn-00bcfff4) → [`00bcfff8`](#insn-00bcfff8)
- ブロック [`00bcfff8`](#insn-00bcfff8) 範囲 `[['00bcfff8', '00bd0047']]`
  - `CONDITIONAL_JUMP` [`00bd0044`](#insn-00bd0044) → [`00bd0058`](#insn-00bd0058)
  - `FALL_THROUGH` [`00bd0044`](#insn-00bd0044) → [`00bd0048`](#insn-00bd0048)
- ブロック [`00bd0048`](#insn-00bd0048) 範囲 `[['00bd0048', '00bd0057']]`
  - `FALL_THROUGH` [`00bd0054`](#insn-00bd0054) → [`00bd0058`](#insn-00bd0058)
- ブロック [`00bd0058`](#insn-00bd0058) 範囲 `[['00bd0058', '00bd0067']]`

## 命令位置別の参照

- [`00bcffec`](#insn-00bcffec) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfff0`](#insn-00bcfff0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfff4`](#insn-00bcfff4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd000c`](#insn-00bd000c) → [`00c5ad40`](../00c5a/00c5ad40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ad40` · 推定シンボル `None` · 推定型 `None`
- [`00bd0020`](#insn-00bd0020) → [`00c5aed0`](../00c5a/00c5aed0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aed0` · 推定シンボル `None` · 推定型 `None`
- [`00bd003c`](#insn-00bd003c) → [`00c5aec0`](../00c5a/00c5aec0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aec0` · 推定シンボル `None` · 推定型 `None`
- [`00bd0044`](#insn-00bd0044) → [`00bd0058`](#insn-00bd0058) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd0058`](#insn-00bd0058) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd005c`](#insn-00bd005c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcffec`](#insn-00bcffec)

~~~json
{
  "source": "00bcffec",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfff0`](#insn-00bcfff0)

~~~json
{
  "source": "00bcfff0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfff4`](#insn-00bcfff4)

~~~json
{
  "source": "00bcfff4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd000c`](#insn-00bd000c)

~~~json
{
  "source": "00bd000c",
  "target": "00c5ad40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd0020`](#insn-00bd0020)

~~~json
{
  "source": "00bd0020",
  "target": "00c5aed0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd003c`](#insn-00bd003c)

~~~json
{
  "source": "00bd003c",
  "target": "00c5aec0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd0044`](#insn-00bd0044)

~~~json
{
  "source": "00bd0044",
  "target": "00bd0058",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd0058`](#insn-00bd0058)

~~~json
{
  "source": "00bd0058",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd005c`](#insn-00bd005c)

~~~json
{
  "source": "00bd005c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
