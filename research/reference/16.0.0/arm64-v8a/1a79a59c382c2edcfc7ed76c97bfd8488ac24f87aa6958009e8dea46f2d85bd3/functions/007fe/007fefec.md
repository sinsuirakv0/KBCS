# 007fefec

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `007cbdec`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cb/007cbdec.md) · 移動量 `+0x33200`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/alignment_unresolved-0007.md#compare-b3f572767c50d7f75e90e7bf035c45f1)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `007ff02c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ff02c.md) · 移動量 `+0x40`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0041.md#compare-a118e63a61c89e0d0fc996f25b1c075e)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "007fefec",
  "name": "FUN_007fefec",
  "size": 140,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7d7902b653466e6312cd5ef0a5e36f9089a46ac2e1b9a171c54109d46c85c4bf",
  "source_text_sha256": "7d7902b653466e6312cd5ef0a5e36f9089a46ac2e1b9a171c54109d46c85c4bf",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "007fefec",
        "007ff077"
      ]
    ],
    "bytes_sha256": "9bf7d5fc47aff8be8cc22e067485a45ad4066da3ecca0db3c5b9ebfd1639a086",
    "instruction_count": 35,
    "instruction_bytes": 140,
    "body_bytes": 140,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00470800](../00470/00470800.md)
- [00c57a90](../00c57/00c57a90.md)
- [00c57c00](../00c57/00c57c00.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 759 bytes

~~~c

undefined8 * FUN_007fefec(long param_1)

{
  undefined8 uVar1;
  void *__src;
  size_t __n;
  undefined8 *puVar2;
  void *__dest;
  long lVar3;
  
  puVar2 = (undefined8 *)_Znwm(0x28);
  uVar1 = *(undefined8 *)(param_1 + 8);
  __src = *(void **)(param_1 + 0x10);
  puVar2[3] = 0;
  puVar2[4] = 0;
  *puVar2 = &PTR_FUN_00c7dc30;
  puVar2[1] = uVar1;
  lVar3 = *(long *)(param_1 + 0x18);
  puVar2[2] = 0;
  __n = lVar3 - (long)__src;
  if (__n != 0) {
    if ((long)__n < 0) {
                    /* WARNING: Subroutine does not return */
      FUN_00470800(puVar2 + 2);
    }
    __dest = (void *)_Znwm(__n);
    puVar2[2] = __dest;
    puVar2[4] = (long)__dest + __n;
    memcpy(__dest,__src,__n);
    puVar2[3] = (long)__dest + __n;
  }
  return puVar2;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-007fefec"></a> `007fefec` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-007feff0"></a> `007feff0` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-007feff4"></a> `007feff4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-007feff8"></a> `007feff8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-007feffc"></a> `007feffc` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-007ff000"></a> `007ff000` | `00 05 80 52` | mov w0,#0x28 | `FALL_THROUGH`
<a id="insn-007ff004"></a> `007ff004` | `a3 62 11 94` | bl 0x00c57a90 | `UNCONDITIONAL_CALL`
<a id="insn-007ff008"></a> `007ff008` | `89 d6 40 a9` | ldp x9,x21,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-007ff00c"></a> `007ff00c` | `e8 23 00 d0` | adrp x8,0xc7d000 | `FALL_THROUGH`
<a id="insn-007ff010"></a> `007ff010` | `08 c1 30 91` | add x8,x8,#0xc30 | `FALL_THROUGH`
<a id="insn-007ff014"></a> `007ff014` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-007ff018"></a> `007ff018` | `1f fc 01 a9` | stp xzr,xzr,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-007ff01c"></a> `007ff01c` | `08 24 00 a9` | stp x8,x9,[x0] | `FALL_THROUGH`
<a id="insn-007ff020"></a> `007ff020` | `88 0e 40 f9` | ldr x8,[x20, #0x18] | `FALL_THROUGH`
<a id="insn-007ff024"></a> `007ff024` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-007ff028"></a> `007ff028` | `9f 0e 01 f8` | str xzr,[x20, #0x10]! | `FALL_THROUGH`
<a id="insn-007ff02c"></a> `007ff02c` | `16 01 15 eb` | subs x22,x8,x21 | `FALL_THROUGH`
<a id="insn-007ff030"></a> `007ff030` | `60 01 00 54` | b.eq 0x007ff05c | `CONDITIONAL_JUMP`
<a id="insn-007ff034"></a> `007ff034` | `f6 01 f8 b7` | tbnz x22,#0x3f,0x007ff070 | `CONDITIONAL_JUMP`
<a id="insn-007ff038"></a> `007ff038` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-007ff03c"></a> `007ff03c` | `95 62 11 94` | bl 0x00c57a90 | `UNCONDITIONAL_CALL`
<a id="insn-007ff040"></a> `007ff040` | `14 00 16 8b` | add x20,x0,x22 | `FALL_THROUGH`
<a id="insn-007ff044"></a> `007ff044` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-007ff048"></a> `007ff048` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-007ff04c"></a> `007ff04c` | `60 0a 00 f9` | str x0,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-007ff050"></a> `007ff050` | `74 12 00 f9` | str x20,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-007ff054"></a> `007ff054` | `eb 62 11 94` | bl 0x00c57c00 | `UNCONDITIONAL_CALL`
<a id="insn-007ff058"></a> `007ff058` | `74 0e 00 f9` | str x20,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-007ff05c"></a> `007ff05c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-007ff060"></a> `007ff060` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-007ff064"></a> `007ff064` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-007ff068"></a> `007ff068` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-007ff06c"></a> `007ff06c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-007ff070"></a> `007ff070` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-007ff074"></a> `007ff074` | `e3 c5 f1 97` | bl 0x00470800 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`007fefec`](#insn-007fefec) 範囲 `[['007fefec', '007ff033']]`
  - `CONDITIONAL_JUMP` [`007ff030`](#insn-007ff030) → [`007ff05c`](#insn-007ff05c)
  - `FALL_THROUGH` [`007ff030`](#insn-007ff030) → [`007ff034`](#insn-007ff034)
- ブロック [`007ff034`](#insn-007ff034) 範囲 `[['007ff034', '007ff037']]`
  - `CONDITIONAL_JUMP` [`007ff034`](#insn-007ff034) → [`007ff070`](#insn-007ff070)
  - `FALL_THROUGH` [`007ff034`](#insn-007ff034) → [`007ff038`](#insn-007ff038)
- ブロック [`007ff038`](#insn-007ff038) 範囲 `[['007ff038', '007ff05b']]`
  - `FALL_THROUGH` [`007ff058`](#insn-007ff058) → [`007ff05c`](#insn-007ff05c)
- ブロック [`007ff05c`](#insn-007ff05c) 範囲 `[['007ff05c', '007ff06f']]`
- ブロック [`007ff070`](#insn-007ff070) 範囲 `[['007ff070', '007ff077']]`

## 命令位置別の参照

- [`007fefec`](#insn-007fefec) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007feff0`](#insn-007feff0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007feff4`](#insn-007feff4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ff004`](#insn-007ff004) → [`00c57a90`](../00c57/00c57a90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a90` · 推定シンボル `None` · 推定型 `None`
- [`007ff01c`](#insn-007ff01c) → `00c7dc30`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`007ff030`](#insn-007ff030) → [`007ff05c`](#insn-007ff05c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ff034`](#insn-007ff034) → [`007ff070`](#insn-007ff070) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ff03c`](#insn-007ff03c) → [`00c57a90`](../00c57/00c57a90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a90` · 推定シンボル `None` · 推定型 `None`
- [`007ff054`](#insn-007ff054) → [`00c57c00`](../00c57/00c57c00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57c00` · 推定シンボル `None` · 推定型 `None`
- [`007ff060`](#insn-007ff060) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ff064`](#insn-007ff064) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ff068`](#insn-007ff068) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ff074`](#insn-007ff074) → [`00470800`](../00470/00470800.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00470800` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`007fefec`](#insn-007fefec)

~~~json
{
  "source": "007fefec",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007feff0`](#insn-007feff0)

~~~json
{
  "source": "007feff0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007feff4`](#insn-007feff4)

~~~json
{
  "source": "007feff4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ff004`](#insn-007ff004)

~~~json
{
  "source": "007ff004",
  "target": "00c57a90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007ff01c`](#insn-007ff01c)

~~~json
{
  "source": "007ff01c",
  "target": "00c7dc30",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c7dc30",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`007ff030`](#insn-007ff030)

~~~json
{
  "source": "007ff030",
  "target": "007ff05c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ff034`](#insn-007ff034)

~~~json
{
  "source": "007ff034",
  "target": "007ff070",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ff03c`](#insn-007ff03c)

~~~json
{
  "source": "007ff03c",
  "target": "00c57a90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007ff054`](#insn-007ff054)

~~~json
{
  "source": "007ff054",
  "target": "00c57c00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007ff060`](#insn-007ff060)

~~~json
{
  "source": "007ff060",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ff064`](#insn-007ff064)

~~~json
{
  "source": "007ff064",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ff068`](#insn-007ff068)

~~~json
{
  "source": "007ff068",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ff074`](#insn-007ff074)

~~~json
{
  "source": "007ff074",
  "target": "00470800",
  "target_space": "ram",
  "resolution": "function"
}
~~~
