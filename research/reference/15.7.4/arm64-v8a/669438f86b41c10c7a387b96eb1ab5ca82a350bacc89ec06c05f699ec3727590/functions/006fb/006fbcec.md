# 006fbcec

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `006fbcec`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006fb/006fbcec.md) · 移動量 `+0x0`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/machine_only_observed-0022.md#compare-82fa456da34d44f05350e17ff53f0be7)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00725dec`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00725/00725dec.md) · 移動量 `+0x2a100`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/alignment_unresolved-0005.md#compare-58b1834e2eaffdf7c52a9d906d2f68a5)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "006fbcec",
  "name": "FUN_006fbcec",
  "size": 136,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4cb8cf68fd69e8b34eff77943f0633469018559ed8ad1dc122543b6d9bc92dce",
  "source_text_sha256": "4cb8cf68fd69e8b34eff77943f0633469018559ed8ad1dc122543b6d9bc92dce",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "006fbcec",
        "006fbd73"
      ]
    ],
    "bytes_sha256": "1821a702566e66d395d846ddb64cf0e4ada665d8a221b4bb2eb0dadab80b5f17",
    "instruction_count": 34,
    "instruction_bytes": 136,
    "body_bytes": 136,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb060](../00bdb/00bdb060.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1182 bytes

~~~c

void FUN_006fbcec(long param_1)

{
  void *pvVar1;
  void *pvVar2;
  void *pvVar3;
  
                    /* try { // try from 006fbcf4 to 007fbd03 has its CatchHandler @ 006fbf70 */
  pvVar2 = *(void **)(param_1 + 0x38);
  if (pvVar2 == (void *)0x0) {
    return;
  }
                    /* try { // try from 006fbd04 to 007fbd13 has its CatchHandler @ 006fbf6c */
  pvVar3 = *(void **)(param_1 + 0x40);
  pvVar1 = pvVar2;
  if (pvVar3 != pvVar2) {
    do {
      pvVar1 = *(void **)((long)pvVar3 + -0x18);
      if (pvVar1 != (void *)0x0) {
        *(void **)((long)pvVar3 + -0x10) = pvVar1;
        _ZdlPv(pvVar1);
      }
      pvVar1 = *(void **)((long)pvVar3 + -0x30);
      if (pvVar1 != (void *)0x0) {
        *(void **)((long)pvVar3 + -0x28) = pvVar1;
                    /* try { // try from 006fbd44 to 007fbd57 has its CatchHandler @ 006fbfbc */
        _ZdlPv(pvVar1);
      }
      pvVar3 = (void *)((long)pvVar3 + -0x88);
    } while (pvVar3 != pvVar2);
    pvVar1 = *(void **)(param_1 + 0x38);
  }
  *(void **)(param_1 + 0x40) = pvVar2;
                    /* try { // try from 006fbd5c to 007fbdb3 has its CatchHandler @ 006fbff4 */
  _ZdlPv(pvVar1);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-006fbcec"></a> `006fbcec` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-006fbcf0"></a> `006fbcf0` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-006fbcf4"></a> `006fbcf4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-006fbcf8"></a> `006fbcf8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-006fbcfc"></a> `006fbcfc` | `14 1c 40 f9` | ldr x20,[x0, #0x38] | `FALL_THROUGH`
<a id="insn-006fbd00"></a> `006fbd00` | `34 03 00 b4` | cbz x20,0x006fbd64 | `CONDITIONAL_JUMP`
<a id="insn-006fbd04"></a> `006fbd04` | `15 20 40 f9` | ldr x21,[x0, #0x40] | `FALL_THROUGH`
<a id="insn-006fbd08"></a> `006fbd08` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-006fbd0c"></a> `006fbd0c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-006fbd10"></a> `006fbd10` | `bf 02 14 eb` | cmp x21,x20 | `FALL_THROUGH`
<a id="insn-006fbd14"></a> `006fbd14` | `a1 00 00 54` | b.ne 0x006fbd28 | `CONDITIONAL_JUMP`
<a id="insn-006fbd18"></a> `006fbd18` | `0e 00 00 14` | b 0x006fbd50 | `UNCONDITIONAL_JUMP`
<a id="insn-006fbd1c"></a> `006fbd1c` | `b5 22 02 d1` | sub x21,x21,#0x88 | `FALL_THROUGH`
<a id="insn-006fbd20"></a> `006fbd20` | `bf 02 14 eb` | cmp x21,x20 | `FALL_THROUGH`
<a id="insn-006fbd24"></a> `006fbd24` | `40 01 00 54` | b.eq 0x006fbd4c | `CONDITIONAL_JUMP`
<a id="insn-006fbd28"></a> `006fbd28` | `a0 82 5e f8` | ldur x0,[x21, #-0x18] | `FALL_THROUGH`
<a id="insn-006fbd2c"></a> `006fbd2c` | `60 00 00 b4` | cbz x0,0x006fbd38 | `CONDITIONAL_JUMP`
<a id="insn-006fbd30"></a> `006fbd30` | `a0 02 1f f8` | stur x0,[x21, #-0x10] | `FALL_THROUGH`
<a id="insn-006fbd34"></a> `006fbd34` | `cb 7c 13 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-006fbd38"></a> `006fbd38` | `a0 02 5d f8` | ldur x0,[x21, #-0x30] | `FALL_THROUGH`
<a id="insn-006fbd3c"></a> `006fbd3c` | `00 ff ff b4` | cbz x0,0x006fbd1c | `CONDITIONAL_JUMP`
<a id="insn-006fbd40"></a> `006fbd40` | `a0 82 1d f8` | stur x0,[x21, #-0x28] | `FALL_THROUGH`
<a id="insn-006fbd44"></a> `006fbd44` | `c7 7c 13 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-006fbd48"></a> `006fbd48` | `f5 ff ff 17` | b 0x006fbd1c | `UNCONDITIONAL_JUMP`
<a id="insn-006fbd4c"></a> `006fbd4c` | `60 1e 40 f9` | ldr x0,[x19, #0x38] | `FALL_THROUGH`
<a id="insn-006fbd50"></a> `006fbd50` | `74 22 00 f9` | str x20,[x19, #0x40] | `FALL_THROUGH`
<a id="insn-006fbd54"></a> `006fbd54` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-006fbd58"></a> `006fbd58` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-006fbd5c"></a> `006fbd5c` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-006fbd60"></a> `006fbd60` | `c0 7c 13 14` | b 0x00bdb060 | `CALL_TERMINATOR`
<a id="insn-006fbd64"></a> `006fbd64` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-006fbd68"></a> `006fbd68` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-006fbd6c"></a> `006fbd6c` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-006fbd70"></a> `006fbd70` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`006fbcec`](#insn-006fbcec) 範囲 `[['006fbcec', '006fbcf3']]`
  - `FALL_THROUGH` [`006fbcf0`](#insn-006fbcf0) → [`006fbcf4`](#insn-006fbcf4)
- ブロック [`006fbcf4`](#insn-006fbcf4) 範囲 `[['006fbcf4', '006fbd03']]`
  - `CONDITIONAL_JUMP` [`006fbd00`](#insn-006fbd00) → [`006fbd64`](#insn-006fbd64)
  - `FALL_THROUGH` [`006fbd00`](#insn-006fbd00) → [`006fbd04`](#insn-006fbd04)
- ブロック [`006fbd04`](#insn-006fbd04) 範囲 `[['006fbd04', '006fbd17']]`
  - `CONDITIONAL_JUMP` [`006fbd14`](#insn-006fbd14) → [`006fbd28`](#insn-006fbd28)
  - `FALL_THROUGH` [`006fbd14`](#insn-006fbd14) → [`006fbd18`](#insn-006fbd18)
- ブロック [`006fbd18`](#insn-006fbd18) 範囲 `[['006fbd18', '006fbd1b']]`
  - `UNCONDITIONAL_JUMP` [`006fbd18`](#insn-006fbd18) → [`006fbd50`](#insn-006fbd50)
- ブロック [`006fbd1c`](#insn-006fbd1c) 範囲 `[['006fbd1c', '006fbd27']]`
  - `CONDITIONAL_JUMP` [`006fbd24`](#insn-006fbd24) → [`006fbd4c`](#insn-006fbd4c)
  - `FALL_THROUGH` [`006fbd24`](#insn-006fbd24) → [`006fbd28`](#insn-006fbd28)
- ブロック [`006fbd28`](#insn-006fbd28) 範囲 `[['006fbd28', '006fbd2f']]`
  - `CONDITIONAL_JUMP` [`006fbd2c`](#insn-006fbd2c) → [`006fbd38`](#insn-006fbd38)
  - `FALL_THROUGH` [`006fbd2c`](#insn-006fbd2c) → [`006fbd30`](#insn-006fbd30)
- ブロック [`006fbd30`](#insn-006fbd30) 範囲 `[['006fbd30', '006fbd37']]`
  - `FALL_THROUGH` [`006fbd34`](#insn-006fbd34) → [`006fbd38`](#insn-006fbd38)
- ブロック [`006fbd38`](#insn-006fbd38) 範囲 `[['006fbd38', '006fbd3f']]`
  - `CONDITIONAL_JUMP` [`006fbd3c`](#insn-006fbd3c) → [`006fbd1c`](#insn-006fbd1c)
  - `FALL_THROUGH` [`006fbd3c`](#insn-006fbd3c) → [`006fbd40`](#insn-006fbd40)
- ブロック [`006fbd40`](#insn-006fbd40) 範囲 `[['006fbd40', '006fbd43']]`
  - `FALL_THROUGH` [`006fbd40`](#insn-006fbd40) → [`006fbd44`](#insn-006fbd44)
- ブロック [`006fbd44`](#insn-006fbd44) 範囲 `[['006fbd44', '006fbd4b']]`
  - `UNCONDITIONAL_JUMP` [`006fbd48`](#insn-006fbd48) → [`006fbd1c`](#insn-006fbd1c)
- ブロック [`006fbd4c`](#insn-006fbd4c) 範囲 `[['006fbd4c', '006fbd4f']]`
  - `FALL_THROUGH` [`006fbd4c`](#insn-006fbd4c) → [`006fbd50`](#insn-006fbd50)
- ブロック [`006fbd50`](#insn-006fbd50) 範囲 `[['006fbd50', '006fbd5b']]`
  - `FALL_THROUGH` [`006fbd58`](#insn-006fbd58) → [`006fbd5c`](#insn-006fbd5c)
- ブロック [`006fbd5c`](#insn-006fbd5c) 範囲 `[['006fbd5c', '006fbd63']]`
- ブロック [`006fbd64`](#insn-006fbd64) 範囲 `[['006fbd64', '006fbd73']]`

## 命令位置別の参照

- [`006fbcec`](#insn-006fbcec) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fbcf0`](#insn-006fbcf0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fbcf4`](#insn-006fbcf4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fbd00`](#insn-006fbd00) → [`006fbd64`](#insn-006fbd64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fbd14`](#insn-006fbd14) → [`006fbd28`](#insn-006fbd28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fbd18`](#insn-006fbd18) → [`006fbd50`](#insn-006fbd50) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fbd24`](#insn-006fbd24) → [`006fbd4c`](#insn-006fbd4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fbd2c`](#insn-006fbd2c) → [`006fbd38`](#insn-006fbd38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fbd34`](#insn-006fbd34) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`006fbd3c`](#insn-006fbd3c) → [`006fbd1c`](#insn-006fbd1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fbd44`](#insn-006fbd44) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`006fbd48`](#insn-006fbd48) → [`006fbd1c`](#insn-006fbd1c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fbd54`](#insn-006fbd54) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fbd58`](#insn-006fbd58) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fbd5c`](#insn-006fbd5c) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fbd60`](#insn-006fbd60) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`006fbd64`](#insn-006fbd64) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fbd68`](#insn-006fbd68) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fbd6c`](#insn-006fbd6c) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`006fbcec`](#insn-006fbcec)

~~~json
{
  "source": "006fbcec",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fbcf0`](#insn-006fbcf0)

~~~json
{
  "source": "006fbcf0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fbcf4`](#insn-006fbcf4)

~~~json
{
  "source": "006fbcf4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fbd00`](#insn-006fbd00)

~~~json
{
  "source": "006fbd00",
  "target": "006fbd64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fbd14`](#insn-006fbd14)

~~~json
{
  "source": "006fbd14",
  "target": "006fbd28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fbd18`](#insn-006fbd18)

~~~json
{
  "source": "006fbd18",
  "target": "006fbd50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fbd24`](#insn-006fbd24)

~~~json
{
  "source": "006fbd24",
  "target": "006fbd4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fbd2c`](#insn-006fbd2c)

~~~json
{
  "source": "006fbd2c",
  "target": "006fbd38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fbd34`](#insn-006fbd34)

~~~json
{
  "source": "006fbd34",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006fbd3c`](#insn-006fbd3c)

~~~json
{
  "source": "006fbd3c",
  "target": "006fbd1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fbd44`](#insn-006fbd44)

~~~json
{
  "source": "006fbd44",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006fbd48`](#insn-006fbd48)

~~~json
{
  "source": "006fbd48",
  "target": "006fbd1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fbd54`](#insn-006fbd54)

~~~json
{
  "source": "006fbd54",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fbd58`](#insn-006fbd58)

~~~json
{
  "source": "006fbd58",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fbd5c`](#insn-006fbd5c)

~~~json
{
  "source": "006fbd5c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fbd60`](#insn-006fbd60)

~~~json
{
  "source": "006fbd60",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006fbd64`](#insn-006fbd64)

~~~json
{
  "source": "006fbd64",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fbd68`](#insn-006fbd68)

~~~json
{
  "source": "006fbd68",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fbd6c`](#insn-006fbd6c)

~~~json
{
  "source": "006fbd6c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
