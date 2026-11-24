# 00bfaffc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b7e5b4`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e5b4.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0072.md#compare-034d67c6e895d627b5fbf005c169f8c0)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bfb424`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb424.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0086.md#compare-03728a4fe95c5cc072cddef1c0891eb1)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfaffc",
  "name": "_ZNSt6__ndk18ios_baseD1Ev",
  "size": 176,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c75c54f5477b9b61cdb86d55c1f490bd99cffa6d4bc65a9c6e38b963ec01493a",
  "source_text_sha256": "c75c54f5477b9b61cdb86d55c1f490bd99cffa6d4bc65a9c6e38b963ec01493a",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfaffc",
        "00bfb0ab"
      ]
    ],
    "bytes_sha256": "4ec450cfd9a24fd710f0a17ff5912f358b60597c917d44b0f7b8c4cc34afd562",
    "instruction_count": 44,
    "instruction_bytes": 176,
    "body_bytes": 176,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

- [00c5cce0](../00c5c/00c5cce0.md)
- [00c5def0](../00c5d/00c5def0.md)

## 呼び出し先

- [00c57e90](../00c57/00c57e90.md)
- [00c58260](../00c58/00c58260.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 584 bytes

~~~c

void _ZNSt6__ndk18ios_baseD1Ev(long *param_1)

{
  long lVar1;
  
  *param_1 = (long)(PTR__ZTVNSt6__ndk18ios_baseE_00c9b700 + 0x10);
  if (param_1[6] != 0) {
    if (param_1[9] != 0) {
      lVar1 = param_1[9] + -1;
      do {
        (**(code **)(param_1[7] + lVar1 * 8))(0,param_1,*(undefined4 *)(param_1[8] + lVar1 * 4));
        lVar1 = lVar1 + -1;
      } while (lVar1 != -1);
    }
    _ZNSt6__ndk16localeD1Ev(param_1 + 6);
    free((void *)param_1[7]);
    free((void *)param_1[8]);
    free((void *)param_1[0xb]);
    free((void *)param_1[0xe]);
    return;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfaffc"></a> `00bfaffc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfb000"></a> `00bfb000` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bfb004"></a> `00bfb004` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfb008"></a> `00bfb008` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfb00c"></a> `00bfb00c` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bfb010"></a> `00bfb010` | `08 05 00 90` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bfb014"></a> `00bfb014` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bfb018"></a> `00bfb018` | `08 81 43 f9` | ldr x8,[x8, #0x700] | `FALL_THROUGH`
<a id="insn-00bfb01c"></a> `00bfb01c` | `89 0e 43 f8` | ldr x9,[x20, #0x30]! | `FALL_THROUGH`
<a id="insn-00bfb020"></a> `00bfb020` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00bfb024"></a> `00bfb024` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-00bfb028"></a> `00bfb028` | `89 03 00 b4` | cbz x9,0x00bfb098 | `CONDITIONAL_JUMP`
<a id="insn-00bfb02c"></a> `00bfb02c` | `08 24 40 f9` | ldr x8,[x0, #0x48] | `FALL_THROUGH`
<a id="insn-00bfb030"></a> `00bfb030` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bfb034"></a> `00bfb034` | `68 01 00 b4` | cbz x8,0x00bfb060 | `CONDITIONAL_JUMP`
<a id="insn-00bfb038"></a> `00bfb038` | `15 05 00 d1` | sub x21,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bfb03c"></a> `00bfb03c` | `68 a6 43 a9` | ldp x8,x9,[x19, #0x38] | `FALL_THROUGH`
<a id="insn-00bfb040"></a> `00bfb040` | `08 79 75 f8` | ldr x8,[x8, x21, LSL #0x3] | `FALL_THROUGH`
<a id="insn-00bfb044"></a> `00bfb044` | `22 79 75 b8` | ldr w2,[x9, x21, LSL #0x2] | `FALL_THROUGH`
<a id="insn-00bfb048"></a> `00bfb048` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bfb04c"></a> `00bfb04c` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bfb050"></a> `00bfb050` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bfb054"></a> `00bfb054` | `b5 06 00 d1` | sub x21,x21,#0x1 | `FALL_THROUGH`
<a id="insn-00bfb058"></a> `00bfb058` | `bf 06 00 b1` | cmn x21,#0x1 | `FALL_THROUGH`
<a id="insn-00bfb05c"></a> `00bfb05c` | `01 ff ff 54` | b.ne 0x00bfb03c | `CONDITIONAL_JUMP`
<a id="insn-00bfb060"></a> `00bfb060` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bfb064"></a> `00bfb064` | `8b 73 01 94` | bl 0x00c57e90 | `UNCONDITIONAL_CALL`
<a id="insn-00bfb068"></a> `00bfb068` | `60 1e 40 f9` | ldr x0,[x19, #0x38] | `FALL_THROUGH`
<a id="insn-00bfb06c"></a> `00bfb06c` | `7d 74 01 94` | bl 0x00c58260 | `UNCONDITIONAL_CALL`
<a id="insn-00bfb070"></a> `00bfb070` | `60 22 40 f9` | ldr x0,[x19, #0x40] | `FALL_THROUGH`
<a id="insn-00bfb074"></a> `00bfb074` | `7b 74 01 94` | bl 0x00c58260 | `UNCONDITIONAL_CALL`
<a id="insn-00bfb078"></a> `00bfb078` | `60 2e 40 f9` | ldr x0,[x19, #0x58] | `FALL_THROUGH`
<a id="insn-00bfb07c"></a> `00bfb07c` | `79 74 01 94` | bl 0x00c58260 | `UNCONDITIONAL_CALL`
<a id="insn-00bfb080"></a> `00bfb080` | `60 3a 40 f9` | ldr x0,[x19, #0x70] | `FALL_THROUGH`
<a id="insn-00bfb084"></a> `00bfb084` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfb088"></a> `00bfb088` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfb08c"></a> `00bfb08c` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bfb090"></a> `00bfb090` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfb094"></a> `00bfb094` | `73 74 01 14` | b 0x00c58260 | `CALL_TERMINATOR`
<a id="insn-00bfb098"></a> `00bfb098` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfb09c"></a> `00bfb09c` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfb0a0"></a> `00bfb0a0` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bfb0a4"></a> `00bfb0a4` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfb0a8"></a> `00bfb0a8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfaffc`](#insn-00bfaffc) 範囲 `[['00bfaffc', '00bfb02b']]`
  - `CONDITIONAL_JUMP` [`00bfb028`](#insn-00bfb028) → [`00bfb098`](#insn-00bfb098)
  - `FALL_THROUGH` [`00bfb028`](#insn-00bfb028) → [`00bfb02c`](#insn-00bfb02c)
- ブロック [`00bfb02c`](#insn-00bfb02c) 範囲 `[['00bfb02c', '00bfb037']]`
  - `CONDITIONAL_JUMP` [`00bfb034`](#insn-00bfb034) → [`00bfb060`](#insn-00bfb060)
  - `FALL_THROUGH` [`00bfb034`](#insn-00bfb034) → [`00bfb038`](#insn-00bfb038)
- ブロック [`00bfb038`](#insn-00bfb038) 範囲 `[['00bfb038', '00bfb03b']]`
  - `FALL_THROUGH` [`00bfb038`](#insn-00bfb038) → [`00bfb03c`](#insn-00bfb03c)
- ブロック [`00bfb03c`](#insn-00bfb03c) 範囲 `[['00bfb03c', '00bfb05f']]`
  - `CONDITIONAL_JUMP` [`00bfb05c`](#insn-00bfb05c) → [`00bfb03c`](#insn-00bfb03c)
  - `FALL_THROUGH` [`00bfb05c`](#insn-00bfb05c) → [`00bfb060`](#insn-00bfb060)
- ブロック [`00bfb060`](#insn-00bfb060) 範囲 `[['00bfb060', '00bfb097']]`
- ブロック [`00bfb098`](#insn-00bfb098) 範囲 `[['00bfb098', '00bfb0ab']]`

## 命令位置別の参照

- [`00bfb000`](#insn-00bfb000) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb004`](#insn-00bfb004) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb008`](#insn-00bfb008) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb018`](#insn-00bfb018) → `00c9b700`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bfb024`](#insn-00bfb024) → `00c929a8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[32]`
- [`00bfb028`](#insn-00bfb028) → [`00bfb098`](#insn-00bfb098) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb034`](#insn-00bfb034) → [`00bfb060`](#insn-00bfb060) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb05c`](#insn-00bfb05c) → [`00bfb03c`](#insn-00bfb03c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb064`](#insn-00bfb064) → [`00c57e90`](../00c57/00c57e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e90` · 推定シンボル `None` · 推定型 `None`
- [`00bfb06c`](#insn-00bfb06c) → [`00c58260`](../00c58/00c58260.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58260` · 推定シンボル `None` · 推定型 `None`
- [`00bfb074`](#insn-00bfb074) → [`00c58260`](../00c58/00c58260.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58260` · 推定シンボル `None` · 推定型 `None`
- [`00bfb07c`](#insn-00bfb07c) → [`00c58260`](../00c58/00c58260.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58260` · 推定シンボル `None` · 推定型 `None`
- [`00bfb084`](#insn-00bfb084) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb088`](#insn-00bfb088) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb08c`](#insn-00bfb08c) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb094`](#insn-00bfb094) → [`00c58260`](../00c58/00c58260.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58260` · 推定シンボル `None` · 推定型 `None`
- [`00bfb098`](#insn-00bfb098) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb09c`](#insn-00bfb09c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb0a0`](#insn-00bfb0a0) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfb000`](#insn-00bfb000)

~~~json
{
  "source": "00bfb000",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb004`](#insn-00bfb004)

~~~json
{
  "source": "00bfb004",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb008`](#insn-00bfb008)

~~~json
{
  "source": "00bfb008",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb018`](#insn-00bfb018)

~~~json
{
  "source": "00bfb018",
  "target": "00c9b700",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b700",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bfb024`](#insn-00bfb024)

~~~json
{
  "source": "00bfb024",
  "target": "00c929a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c92998",
  "offset": 16,
  "size": 32,
  "datatype": "undefined1[32]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`00bfb028`](#insn-00bfb028)

~~~json
{
  "source": "00bfb028",
  "target": "00bfb098",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb034`](#insn-00bfb034)

~~~json
{
  "source": "00bfb034",
  "target": "00bfb060",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb05c`](#insn-00bfb05c)

~~~json
{
  "source": "00bfb05c",
  "target": "00bfb03c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb064`](#insn-00bfb064)

~~~json
{
  "source": "00bfb064",
  "target": "00c57e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfb06c`](#insn-00bfb06c)

~~~json
{
  "source": "00bfb06c",
  "target": "00c58260",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfb074`](#insn-00bfb074)

~~~json
{
  "source": "00bfb074",
  "target": "00c58260",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfb07c`](#insn-00bfb07c)

~~~json
{
  "source": "00bfb07c",
  "target": "00c58260",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfb084`](#insn-00bfb084)

~~~json
{
  "source": "00bfb084",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb088`](#insn-00bfb088)

~~~json
{
  "source": "00bfb088",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb08c`](#insn-00bfb08c)

~~~json
{
  "source": "00bfb08c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb094`](#insn-00bfb094)

~~~json
{
  "source": "00bfb094",
  "target": "00c58260",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfb098`](#insn-00bfb098)

~~~json
{
  "source": "00bfb098",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb09c`](#insn-00bfb09c)

~~~json
{
  "source": "00bfb09c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb0a0`](#insn-00bfb0a0)

~~~json
{
  "source": "00bfb0a0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
