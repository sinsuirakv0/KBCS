# 004dfccc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `004dfccc`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004df/004dfccc.md) · 移動量 `+0x0`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/reference_unresolved-0004.md#compare-98078a1da19090b6ea6115f834220f58)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00502b64`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/00502b64.md) · 移動量 `+0x22e98`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/inspection-0007.md#compare-9addedb8a15098798160b558c1bf22aa)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "004dfccc",
  "name": "FUN_004dfccc",
  "size": 152,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5991f0165fcb863f4a3ae74a76d97312ee44e6b1532ab232602faddff22e663d",
  "source_text_sha256": "5991f0165fcb863f4a3ae74a76d97312ee44e6b1532ab232602faddff22e663d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "004dfccc",
        "004dfd63"
      ]
    ],
    "bytes_sha256": "fa3d7416cbc99a95799d9560947d2296fc5b55bd03707c526b0280068acacbfc",
    "instruction_count": 38,
    "instruction_bytes": 152,
    "body_bytes": 152,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bd6e90](../00bd6/00bd6e90.md)
- [00bdb030](../00bdb/00bdb030.md)
- [00bdb060](../00bdb/00bdb060.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 734 bytes

~~~c

void FUN_004dfccc(undefined8 *param_1)

{
  long lVar1;
  void *__ptr;
  long *plVar2;
  void *pvVar3;
  void *pvVar4;
  
  pvVar3 = (void *)*param_1;
  if (pvVar3 == (void *)0x0) {
    return;
  }
  pvVar4 = (void *)param_1[1];
  __ptr = pvVar3;
  if (pvVar4 != pvVar3) {
    do {
      plVar2 = *(long **)((long)pvVar4 + -8);
      if ((plVar2 != (long *)0x0) &&
         (lVar1 = FUN_00bd6e90(0xffffffffffffffff,plVar2 + 1), lVar1 == 0)) {
        (**(code **)(*plVar2 + 0x10))(plVar2);
        _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar2);
      }
      pvVar4 = (void *)((long)pvVar4 + -0x10);
    } while (pvVar4 != pvVar3);
    __ptr = (void *)*param_1;
  }
  param_1[1] = pvVar3;
  _ZdlPv(__ptr);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-004dfccc"></a> `004dfccc` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-004dfcd0"></a> `004dfcd0` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-004dfcd4"></a> `004dfcd4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-004dfcd8"></a> `004dfcd8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-004dfcdc"></a> `004dfcdc` | `15 00 40 f9` | ldr x21,[x0] | `FALL_THROUGH`
<a id="insn-004dfce0"></a> `004dfce0` | `b5 03 00 b4` | cbz x21,0x004dfd54 | `CONDITIONAL_JUMP`
<a id="insn-004dfce4"></a> `004dfce4` | `16 04 40 f9` | ldr x22,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-004dfce8"></a> `004dfce8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-004dfcec"></a> `004dfcec` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-004dfcf0"></a> `004dfcf0` | `df 02 15 eb` | cmp x22,x21 | `FALL_THROUGH`
<a id="insn-004dfcf4"></a> `004dfcf4` | `a1 00 00 54` | b.ne 0x004dfd08 | `CONDITIONAL_JUMP`
<a id="insn-004dfcf8"></a> `004dfcf8` | `12 00 00 14` | b 0x004dfd40 | `UNCONDITIONAL_JUMP`
<a id="insn-004dfcfc"></a> `004dfcfc` | `d6 42 00 d1` | sub x22,x22,#0x10 | `FALL_THROUGH`
<a id="insn-004dfd00"></a> `004dfd00` | `df 02 15 eb` | cmp x22,x21 | `FALL_THROUGH`
<a id="insn-004dfd04"></a> `004dfd04` | `c0 01 00 54` | b.eq 0x004dfd3c | `CONDITIONAL_JUMP`
<a id="insn-004dfd08"></a> `004dfd08` | `d4 82 5f f8` | ldur x20,[x22, #-0x8] | `FALL_THROUGH`
<a id="insn-004dfd0c"></a> `004dfd0c` | `94 ff ff b4` | cbz x20,0x004dfcfc | `CONDITIONAL_JUMP`
<a id="insn-004dfd10"></a> `004dfd10` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-004dfd14"></a> `004dfd14` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-004dfd18"></a> `004dfd18` | `5e dc 1b 94` | bl 0x00bd6e90 | `UNCONDITIONAL_CALL`
<a id="insn-004dfd1c"></a> `004dfd1c` | `00 ff ff b5` | cbnz x0,0x004dfcfc | `CONDITIONAL_JUMP`
<a id="insn-004dfd20"></a> `004dfd20` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-004dfd24"></a> `004dfd24` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-004dfd28"></a> `004dfd28` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-004dfd2c"></a> `004dfd2c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-004dfd30"></a> `004dfd30` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-004dfd34"></a> `004dfd34` | `bf ec 1b 94` | bl 0x00bdb030 | `UNCONDITIONAL_CALL`
<a id="insn-004dfd38"></a> `004dfd38` | `f1 ff ff 17` | b 0x004dfcfc | `UNCONDITIONAL_JUMP`
<a id="insn-004dfd3c"></a> `004dfd3c` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-004dfd40"></a> `004dfd40` | `75 06 00 f9` | str x21,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-004dfd44"></a> `004dfd44` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-004dfd48"></a> `004dfd48` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-004dfd4c"></a> `004dfd4c` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-004dfd50"></a> `004dfd50` | `c4 ec 1b 14` | b 0x00bdb060 | `CALL_TERMINATOR`
<a id="insn-004dfd54"></a> `004dfd54` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-004dfd58"></a> `004dfd58` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-004dfd5c"></a> `004dfd5c` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-004dfd60"></a> `004dfd60` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`004dfccc`](#insn-004dfccc) 範囲 `[['004dfccc', '004dfce3']]`
  - `CONDITIONAL_JUMP` [`004dfce0`](#insn-004dfce0) → [`004dfd54`](#insn-004dfd54)
  - `FALL_THROUGH` [`004dfce0`](#insn-004dfce0) → [`004dfce4`](#insn-004dfce4)
- ブロック [`004dfce4`](#insn-004dfce4) 範囲 `[['004dfce4', '004dfcf7']]`
  - `CONDITIONAL_JUMP` [`004dfcf4`](#insn-004dfcf4) → [`004dfd08`](#insn-004dfd08)
  - `FALL_THROUGH` [`004dfcf4`](#insn-004dfcf4) → [`004dfcf8`](#insn-004dfcf8)
- ブロック [`004dfcf8`](#insn-004dfcf8) 範囲 `[['004dfcf8', '004dfcfb']]`
  - `UNCONDITIONAL_JUMP` [`004dfcf8`](#insn-004dfcf8) → [`004dfd40`](#insn-004dfd40)
- ブロック [`004dfcfc`](#insn-004dfcfc) 範囲 `[['004dfcfc', '004dfd07']]`
  - `CONDITIONAL_JUMP` [`004dfd04`](#insn-004dfd04) → [`004dfd3c`](#insn-004dfd3c)
  - `FALL_THROUGH` [`004dfd04`](#insn-004dfd04) → [`004dfd08`](#insn-004dfd08)
- ブロック [`004dfd08`](#insn-004dfd08) 範囲 `[['004dfd08', '004dfd0f']]`
  - `CONDITIONAL_JUMP` [`004dfd0c`](#insn-004dfd0c) → [`004dfcfc`](#insn-004dfcfc)
  - `FALL_THROUGH` [`004dfd0c`](#insn-004dfd0c) → [`004dfd10`](#insn-004dfd10)
- ブロック [`004dfd10`](#insn-004dfd10) 範囲 `[['004dfd10', '004dfd1f']]`
  - `CONDITIONAL_JUMP` [`004dfd1c`](#insn-004dfd1c) → [`004dfcfc`](#insn-004dfcfc)
  - `FALL_THROUGH` [`004dfd1c`](#insn-004dfd1c) → [`004dfd20`](#insn-004dfd20)
- ブロック [`004dfd20`](#insn-004dfd20) 範囲 `[['004dfd20', '004dfd3b']]`
  - `UNCONDITIONAL_JUMP` [`004dfd38`](#insn-004dfd38) → [`004dfcfc`](#insn-004dfcfc)
- ブロック [`004dfd3c`](#insn-004dfd3c) 範囲 `[['004dfd3c', '004dfd3f']]`
  - `FALL_THROUGH` [`004dfd3c`](#insn-004dfd3c) → [`004dfd40`](#insn-004dfd40)
- ブロック [`004dfd40`](#insn-004dfd40) 範囲 `[['004dfd40', '004dfd53']]`
- ブロック [`004dfd54`](#insn-004dfd54) 範囲 `[['004dfd54', '004dfd63']]`

## 命令位置別の参照

- [`004dfccc`](#insn-004dfccc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dfcd0`](#insn-004dfcd0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dfcd4`](#insn-004dfcd4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dfce0`](#insn-004dfce0) → [`004dfd54`](#insn-004dfd54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dfcf4`](#insn-004dfcf4) → [`004dfd08`](#insn-004dfd08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dfcf8`](#insn-004dfcf8) → [`004dfd40`](#insn-004dfd40) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dfd04`](#insn-004dfd04) → [`004dfd3c`](#insn-004dfd3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dfd0c`](#insn-004dfd0c) → [`004dfcfc`](#insn-004dfcfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dfd18`](#insn-004dfd18) → [`00bd6e90`](../00bd6/00bd6e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd6e90` · 推定シンボル `None` · 推定型 `None`
- [`004dfd1c`](#insn-004dfd1c) → [`004dfcfc`](#insn-004dfcfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dfd34`](#insn-004dfd34) → [`00bdb030`](../00bdb/00bdb030.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb030` · 推定シンボル `None` · 推定型 `None`
- [`004dfd38`](#insn-004dfd38) → [`004dfcfc`](#insn-004dfcfc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dfd44`](#insn-004dfd44) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dfd48`](#insn-004dfd48) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dfd4c`](#insn-004dfd4c) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dfd50`](#insn-004dfd50) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`004dfd54`](#insn-004dfd54) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dfd58`](#insn-004dfd58) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dfd5c`](#insn-004dfd5c) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`004dfccc`](#insn-004dfccc)

~~~json
{
  "source": "004dfccc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dfcd0`](#insn-004dfcd0)

~~~json
{
  "source": "004dfcd0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dfcd4`](#insn-004dfcd4)

~~~json
{
  "source": "004dfcd4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dfce0`](#insn-004dfce0)

~~~json
{
  "source": "004dfce0",
  "target": "004dfd54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dfcf4`](#insn-004dfcf4)

~~~json
{
  "source": "004dfcf4",
  "target": "004dfd08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dfcf8`](#insn-004dfcf8)

~~~json
{
  "source": "004dfcf8",
  "target": "004dfd40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dfd04`](#insn-004dfd04)

~~~json
{
  "source": "004dfd04",
  "target": "004dfd3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dfd0c`](#insn-004dfd0c)

~~~json
{
  "source": "004dfd0c",
  "target": "004dfcfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dfd18`](#insn-004dfd18)

~~~json
{
  "source": "004dfd18",
  "target": "00bd6e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004dfd1c`](#insn-004dfd1c)

~~~json
{
  "source": "004dfd1c",
  "target": "004dfcfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dfd34`](#insn-004dfd34)

~~~json
{
  "source": "004dfd34",
  "target": "00bdb030",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004dfd38`](#insn-004dfd38)

~~~json
{
  "source": "004dfd38",
  "target": "004dfcfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dfd44`](#insn-004dfd44)

~~~json
{
  "source": "004dfd44",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dfd48`](#insn-004dfd48)

~~~json
{
  "source": "004dfd48",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dfd4c`](#insn-004dfd4c)

~~~json
{
  "source": "004dfd4c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dfd50`](#insn-004dfd50)

~~~json
{
  "source": "004dfd50",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004dfd54`](#insn-004dfd54)

~~~json
{
  "source": "004dfd54",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dfd58`](#insn-004dfd58)

~~~json
{
  "source": "004dfd58",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dfd5c`](#insn-004dfd5c)

~~~json
{
  "source": "004dfd5c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
