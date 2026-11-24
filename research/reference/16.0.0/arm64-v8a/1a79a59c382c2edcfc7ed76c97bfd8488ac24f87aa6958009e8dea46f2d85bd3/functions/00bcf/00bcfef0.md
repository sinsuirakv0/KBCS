# 00bcfef0

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b609f0`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b609f0.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/alignment_unresolved-0017.md#compare-e5905677e4efead60e72dfc240b79bb5)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bd0318`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd0/00bd0318.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0082.md#compare-884799160ba2090897eb00b28b2c0a3e)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcfef0",
  "name": "_ZN8firebase6FutureINS_4auth4UserEEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE",
  "size": 124,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4f5959084491e868f9ae074070ee72b2d66fb689cd5118b55cb0c78065665764",
  "source_text_sha256": "4f5959084491e868f9ae074070ee72b2d66fb689cd5118b55cb0c78065665764",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcfef0",
        "00bcff6b"
      ]
    ],
    "bytes_sha256": "0db3c85ff83823993acaa43717c3c2b3bb4708d7f5dae221b8f6ca0954158f2d",
    "instruction_count": 31,
    "instruction_bytes": 124,
    "body_bytes": 124,
    "indirect": 2,
    "unresolved": 2
  }
}
~~~

## 呼び出し元

- [00c5d950](../00c5d/00c5d950.md)

## 呼び出し先

- [00c5a870](../00c5a/00c5a870.md)
- [00c5a9f0](../00c5a/00c5a9f0.md)
- [00c5aa00](../00c5a/00c5aa00.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 739 bytes

~~~c

void _ZN8firebase6FutureINS_4auth4UserEEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE
               (long param_1,undefined8 param_2,undefined8 param_3)

{
  long lVar1;
  long *plVar2;
  
  _ZN8firebase5MutexC1ENS0_4ModeE(param_1,0);
  *(undefined8 *)(param_1 + 0x28) = param_2;
  lVar1 = param_1 + 0x30;
  _ZN8firebase12FutureHandleC1ERKS0_(lVar1,param_3);
  (**(code **)(**(long **)(param_1 + 0x28) + 0x10))(*(long **)(param_1 + 0x28),lVar1);
  _ZN8firebase12FutureHandle6DetachEv(lVar1);
  plVar2 = *(long **)(param_1 + 0x28);
  if (plVar2 != (long *)0x0) {
                    /* try { // try from 00bcff54 to 00ccff6b has its CatchHandler @ 00bd0170 */
    (**(code **)(*plVar2 + 0x58))(plVar2,param_1);
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcfef0"></a> `00bcfef0` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bcfef4"></a> `00bcfef4` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcfef8"></a> `00bcfef8` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcfefc"></a> `00bcfefc` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bcff00"></a> `00bcff00` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00bcff04"></a> `00bcff04` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00bcff08"></a> `00bcff08` | `f5 03 02 aa` | mov x21,x2 | `FALL_THROUGH`
<a id="insn-00bcff0c"></a> `00bcff0c` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bcff10"></a> `00bcff10` | `58 2a 02 94` | bl 0x00c5a870 | `UNCONDITIONAL_CALL`
<a id="insn-00bcff14"></a> `00bcff14` | `74 16 00 f9` | str x20,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00bcff18"></a> `00bcff18` | `74 c2 00 91` | add x20,x19,#0x30 | `FALL_THROUGH`
<a id="insn-00bcff1c"></a> `00bcff1c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bcff20"></a> `00bcff20` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bcff24"></a> `00bcff24` | `b7 2a 02 94` | bl 0x00c5aa00 | `UNCONDITIONAL_CALL`
<a id="insn-00bcff28"></a> `00bcff28` | `60 16 40 f9` | ldr x0,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00bcff2c"></a> `00bcff2c` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bcff30"></a> `00bcff30` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00bcff34"></a> `00bcff34` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bcff38"></a> `00bcff38` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcff3c"></a> `00bcff3c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bcff40"></a> `00bcff40` | `ac 2a 02 94` | bl 0x00c5a9f0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcff44"></a> `00bcff44` | `60 16 40 f9` | ldr x0,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00bcff48"></a> `00bcff48` | `a0 00 00 b4` | cbz x0,0x00bcff5c | `CONDITIONAL_JUMP`
<a id="insn-00bcff4c"></a> `00bcff4c` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bcff50"></a> `00bcff50` | `08 2d 40 f9` | ldr x8,[x8, #0x58] | `FALL_THROUGH`
<a id="insn-00bcff54"></a> `00bcff54` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bcff58"></a> `00bcff58` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcff5c"></a> `00bcff5c` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcff60"></a> `00bcff60` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcff64"></a> `00bcff64` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bcff68"></a> `00bcff68` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcfef0`](#insn-00bcfef0) 範囲 `[['00bcfef0', '00bcff4b']]`
  - `CONDITIONAL_JUMP` [`00bcff48`](#insn-00bcff48) → [`00bcff5c`](#insn-00bcff5c)
  - `FALL_THROUGH` [`00bcff48`](#insn-00bcff48) → [`00bcff4c`](#insn-00bcff4c)
- ブロック [`00bcff4c`](#insn-00bcff4c) 範囲 `[['00bcff4c', '00bcff53']]`
  - `FALL_THROUGH` [`00bcff50`](#insn-00bcff50) → [`00bcff54`](#insn-00bcff54)
- ブロック [`00bcff54`](#insn-00bcff54) 範囲 `[['00bcff54', '00bcff5b']]`
  - `FALL_THROUGH` [`00bcff58`](#insn-00bcff58) → [`00bcff5c`](#insn-00bcff5c)
- ブロック [`00bcff5c`](#insn-00bcff5c) 範囲 `[['00bcff5c', '00bcff6b']]`

## 命令位置別の参照

- [`00bcfef0`](#insn-00bcfef0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfef4`](#insn-00bcfef4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfef8`](#insn-00bcfef8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcff10`](#insn-00bcff10) → [`00c5a870`](../00c5a/00c5a870.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a870` · 推定シンボル `None` · 推定型 `None`
- [`00bcff24`](#insn-00bcff24) → [`00c5aa00`](../00c5a/00c5aa00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa00` · 推定シンボル `None` · 推定型 `None`
- [`00bcff40`](#insn-00bcff40) → [`00c5a9f0`](../00c5a/00c5a9f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a9f0` · 推定シンボル `None` · 推定型 `None`
- [`00bcff48`](#insn-00bcff48) → [`00bcff5c`](#insn-00bcff5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcff5c`](#insn-00bcff5c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcff60`](#insn-00bcff60) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcfef0`](#insn-00bcfef0)

~~~json
{
  "source": "00bcfef0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfef4`](#insn-00bcfef4)

~~~json
{
  "source": "00bcfef4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfef8`](#insn-00bcfef8)

~~~json
{
  "source": "00bcfef8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcff10`](#insn-00bcff10)

~~~json
{
  "source": "00bcff10",
  "target": "00c5a870",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcff24`](#insn-00bcff24)

~~~json
{
  "source": "00bcff24",
  "target": "00c5aa00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcff40`](#insn-00bcff40)

~~~json
{
  "source": "00bcff40",
  "target": "00c5a9f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcff48`](#insn-00bcff48)

~~~json
{
  "source": "00bcff48",
  "target": "00bcff5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcff5c`](#insn-00bcff5c)

~~~json
{
  "source": "00bcff5c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcff60`](#insn-00bcff60)

~~~json
{
  "source": "00bcff60",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
