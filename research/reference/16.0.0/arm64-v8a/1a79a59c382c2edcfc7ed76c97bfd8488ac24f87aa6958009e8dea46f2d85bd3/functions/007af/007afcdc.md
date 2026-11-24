# 007afcdc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0128.md#review-445b63e2e43706415dc967cecc1689db)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `007afd1c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007afd1c.md) · 移動量 `+0x40`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0039.md#compare-0b5dbac88624ca8876ea7c8f2d2728ad)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "007afcdc",
  "name": "FUN_007afcdc",
  "size": 116,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f47577fac5f00ce324f62d22771ffe5cba2b7d0af4213df029d1700e3f4a6bf5",
  "source_text_sha256": "f47577fac5f00ce324f62d22771ffe5cba2b7d0af4213df029d1700e3f4a6bf5",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "007afcdc",
        "007afd4f"
      ]
    ],
    "bytes_sha256": "bf943ac01677f0c4c37ba75893f20b10148ff341096957023e16e0fa7750a2fa",
    "instruction_count": 29,
    "instruction_bytes": 116,
    "body_bytes": 116,
    "indirect": 2,
    "unresolved": 2
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57a90](../00c57/00c57a90.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 524 bytes

~~~c

undefined8 * FUN_007afcdc(long param_1)

{
  undefined8 *puVar1;
  long *plVar2;
  undefined8 uVar3;
  long lVar4;
  
  puVar1 = (undefined8 *)_Znwm(0x40);
  plVar2 = *(long **)(param_1 + 0x30);
  *puVar1 = &PTR_FUN_00c7a618;
  uVar3 = 0;
  if (plVar2 != (long *)0x0) {
    if (plVar2 == (long *)(param_1 + 0x10)) {
      lVar4 = *plVar2;
      puVar1[6] = puVar1 + 2;
      (**(code **)(lVar4 + 0x18))();
      return puVar1;
    }
    uVar3 = (**(code **)(*plVar2 + 0x10))();
  }
  puVar1[6] = uVar3;
  return puVar1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-007afcdc"></a> `007afcdc` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-007afce0"></a> `007afce0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-007afce4"></a> `007afce4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-007afce8"></a> `007afce8` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-007afcec"></a> `007afcec` | `00 08 80 52` | mov w0,#0x40 | `FALL_THROUGH`
<a id="insn-007afcf0"></a> `007afcf0` | `68 9f 12 94` | bl 0x00c57a90 | `UNCONDITIONAL_CALL`
<a id="insn-007afcf4"></a> `007afcf4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-007afcf8"></a> `007afcf8` | `80 1a 40 f9` | ldr x0,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-007afcfc"></a> `007afcfc` | `48 26 00 f0` | adrp x8,0xc7a000 | `FALL_THROUGH`
<a id="insn-007afd00"></a> `007afd00` | `08 61 18 91` | add x8,x8,#0x618 | `FALL_THROUGH`
<a id="insn-007afd04"></a> `007afd04` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-007afd08"></a> `007afd08` | `28 04 01 f8` | str x8,[x1], #0x10 | `FALL_THROUGH`
<a id="insn-007afd0c"></a> `007afd0c` | `e0 00 00 b4` | cbz x0,0x007afd28 | `CONDITIONAL_JUMP`
<a id="insn-007afd10"></a> `007afd10` | `88 42 00 91` | add x8,x20,#0x10 | `FALL_THROUGH`
<a id="insn-007afd14"></a> `007afd14` | `1f 00 08 eb` | cmp x0,x8 | `FALL_THROUGH`
<a id="insn-007afd18"></a> `007afd18` | `c0 00 00 54` | b.eq 0x007afd30 | `CONDITIONAL_JUMP`
<a id="insn-007afd1c"></a> `007afd1c` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-007afd20"></a> `007afd20` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-007afd24"></a> `007afd24` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-007afd28"></a> `007afd28` | `60 1a 00 f9` | str x0,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-007afd2c"></a> `007afd2c` | `05 00 00 14` | b 0x007afd40 | `UNCONDITIONAL_JUMP`
<a id="insn-007afd30"></a> `007afd30` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-007afd34"></a> `007afd34` | `61 1a 00 f9` | str x1,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-007afd38"></a> `007afd38` | `08 0d 40 f9` | ldr x8,[x8, #0x18] | `FALL_THROUGH`
<a id="insn-007afd3c"></a> `007afd3c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-007afd40"></a> `007afd40` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-007afd44"></a> `007afd44` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-007afd48"></a> `007afd48` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-007afd4c"></a> `007afd4c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`007afcdc`](#insn-007afcdc) 範囲 `[['007afcdc', '007afd0f']]`
  - `CONDITIONAL_JUMP` [`007afd0c`](#insn-007afd0c) → [`007afd28`](#insn-007afd28)
  - `FALL_THROUGH` [`007afd0c`](#insn-007afd0c) → [`007afd10`](#insn-007afd10)
- ブロック [`007afd10`](#insn-007afd10) 範囲 `[['007afd10', '007afd1b']]`
  - `CONDITIONAL_JUMP` [`007afd18`](#insn-007afd18) → [`007afd30`](#insn-007afd30)
  - `FALL_THROUGH` [`007afd18`](#insn-007afd18) → [`007afd1c`](#insn-007afd1c)
- ブロック [`007afd1c`](#insn-007afd1c) 範囲 `[['007afd1c', '007afd27']]`
  - `FALL_THROUGH` [`007afd24`](#insn-007afd24) → [`007afd28`](#insn-007afd28)
- ブロック [`007afd28`](#insn-007afd28) 範囲 `[['007afd28', '007afd2f']]`
  - `UNCONDITIONAL_JUMP` [`007afd2c`](#insn-007afd2c) → [`007afd40`](#insn-007afd40)
- ブロック [`007afd30`](#insn-007afd30) 範囲 `[['007afd30', '007afd3f']]`
  - `FALL_THROUGH` [`007afd3c`](#insn-007afd3c) → [`007afd40`](#insn-007afd40)
- ブロック [`007afd40`](#insn-007afd40) 範囲 `[['007afd40', '007afd4f']]`

## 命令位置別の参照

- [`007afcdc`](#insn-007afcdc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007afce0`](#insn-007afce0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007afcf0`](#insn-007afcf0) → [`00c57a90`](../00c57/00c57a90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a90` · 推定シンボル `None` · 推定型 `None`
- [`007afd08`](#insn-007afd08) → `00c7a618`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`007afd0c`](#insn-007afd0c) → [`007afd28`](#insn-007afd28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007afd18`](#insn-007afd18) → [`007afd30`](#insn-007afd30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007afd2c`](#insn-007afd2c) → [`007afd40`](#insn-007afd40) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007afd44`](#insn-007afd44) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007afd48`](#insn-007afd48) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`007afcdc`](#insn-007afcdc)

~~~json
{
  "source": "007afcdc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007afce0`](#insn-007afce0)

~~~json
{
  "source": "007afce0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007afcf0`](#insn-007afcf0)

~~~json
{
  "source": "007afcf0",
  "target": "00c57a90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007afd08`](#insn-007afd08)

~~~json
{
  "source": "007afd08",
  "target": "00c7a618",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c7a618",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`007afd0c`](#insn-007afd0c)

~~~json
{
  "source": "007afd0c",
  "target": "007afd28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007afd18`](#insn-007afd18)

~~~json
{
  "source": "007afd18",
  "target": "007afd30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007afd2c`](#insn-007afd2c)

~~~json
{
  "source": "007afd2c",
  "target": "007afd40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007afd44`](#insn-007afd44)

~~~json
{
  "source": "007afd44",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007afd48`](#insn-007afd48)

~~~json
{
  "source": "007afd48",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
