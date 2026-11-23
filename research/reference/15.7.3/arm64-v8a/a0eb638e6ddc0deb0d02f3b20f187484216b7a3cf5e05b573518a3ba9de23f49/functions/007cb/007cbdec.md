# 007cbdec

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `007cbdec`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cb/007cbdec.md) · 移動量 `+0x0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0037.md#compare-2d6ba9e1ee029e523b76753cd0e9a67f)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `007cbdec`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cb/007cbdec.md) · 移動量 `+0x0`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0037.md#compare-576c18f2ee76cf1c50e5d8534fd28241)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "007cbdec",
  "name": "FUN_007cbdec",
  "size": 140,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "57e5ea6438b61251689a00fac8808fb3ffc55f4c7fc9fd7d7dee4278785ceb55",
  "source_text_sha256": "57e5ea6438b61251689a00fac8808fb3ffc55f4c7fc9fd7d7dee4278785ceb55",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "007cbdec",
        "007cbe77"
      ]
    ],
    "bytes_sha256": "ec74c60f42bf6fadd44d7c06c4527a3e74a26ffcfd9316f639fae33307a0ec7d",
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

- [0044d968](../0044d/0044d968.md)
- [00bdaff0](../00bda/00bdaff0.md)
- [00bdb160](../00bdb/00bdb160.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 856 bytes

~~~c

undefined8 * FUN_007cbdec(long param_1)

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
  *puVar2 = &PTR_FUN_00bfffa8;
  puVar2[1] = uVar1;
  lVar3 = *(long *)(param_1 + 0x18);
  puVar2[2] = 0;
                    /* try { // try from 007cbe2c to 008cbe4f has its CatchHandler @ 007cdafc */
  __n = lVar3 - (long)__src;
  if (__n != 0) {
    if ((long)__n < 0) {
                    /* WARNING: Subroutine does not return */
      FUN_0044d968(puVar2 + 2);
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
<a id="insn-007cbdec"></a> `007cbdec` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-007cbdf0"></a> `007cbdf0` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-007cbdf4"></a> `007cbdf4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-007cbdf8"></a> `007cbdf8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-007cbdfc"></a> `007cbdfc` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-007cbe00"></a> `007cbe00` | `00 05 80 52` | mov w0,#0x28 | `FALL_THROUGH`
<a id="insn-007cbe04"></a> `007cbe04` | `7b 3c 10 94` | bl 0x00bdaff0 | `UNCONDITIONAL_CALL`
<a id="insn-007cbe08"></a> `007cbe08` | `89 d6 40 a9` | ldp x9,x21,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-007cbe0c"></a> `007cbe0c` | `a8 21 00 90` | adrp x8,0xbff000 | `FALL_THROUGH`
<a id="insn-007cbe10"></a> `007cbe10` | `08 a1 3e 91` | add x8,x8,#0xfa8 | `FALL_THROUGH`
<a id="insn-007cbe14"></a> `007cbe14` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-007cbe18"></a> `007cbe18` | `1f fc 01 a9` | stp xzr,xzr,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-007cbe1c"></a> `007cbe1c` | `08 24 00 a9` | stp x8,x9,[x0] | `FALL_THROUGH`
<a id="insn-007cbe20"></a> `007cbe20` | `88 0e 40 f9` | ldr x8,[x20, #0x18] | `FALL_THROUGH`
<a id="insn-007cbe24"></a> `007cbe24` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-007cbe28"></a> `007cbe28` | `9f 0e 01 f8` | str xzr,[x20, #0x10]! | `FALL_THROUGH`
<a id="insn-007cbe2c"></a> `007cbe2c` | `16 01 15 eb` | subs x22,x8,x21 | `FALL_THROUGH`
<a id="insn-007cbe30"></a> `007cbe30` | `60 01 00 54` | b.eq 0x007cbe5c | `CONDITIONAL_JUMP`
<a id="insn-007cbe34"></a> `007cbe34` | `f6 01 f8 b7` | tbnz x22,#0x3f,0x007cbe70 | `CONDITIONAL_JUMP`
<a id="insn-007cbe38"></a> `007cbe38` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-007cbe3c"></a> `007cbe3c` | `6d 3c 10 94` | bl 0x00bdaff0 | `UNCONDITIONAL_CALL`
<a id="insn-007cbe40"></a> `007cbe40` | `14 00 16 8b` | add x20,x0,x22 | `FALL_THROUGH`
<a id="insn-007cbe44"></a> `007cbe44` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-007cbe48"></a> `007cbe48` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-007cbe4c"></a> `007cbe4c` | `60 0a 00 f9` | str x0,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-007cbe50"></a> `007cbe50` | `74 12 00 f9` | str x20,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-007cbe54"></a> `007cbe54` | `c3 3c 10 94` | bl 0x00bdb160 | `UNCONDITIONAL_CALL`
<a id="insn-007cbe58"></a> `007cbe58` | `74 0e 00 f9` | str x20,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-007cbe5c"></a> `007cbe5c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-007cbe60"></a> `007cbe60` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-007cbe64"></a> `007cbe64` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-007cbe68"></a> `007cbe68` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-007cbe6c"></a> `007cbe6c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-007cbe70"></a> `007cbe70` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-007cbe74"></a> `007cbe74` | `bd 06 f2 97` | bl 0x0044d968 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`007cbdec`](#insn-007cbdec) 範囲 `[['007cbdec', '007cbe2b']]`
  - `FALL_THROUGH` [`007cbe28`](#insn-007cbe28) → [`007cbe2c`](#insn-007cbe2c)
- ブロック [`007cbe2c`](#insn-007cbe2c) 範囲 `[['007cbe2c', '007cbe33']]`
  - `CONDITIONAL_JUMP` [`007cbe30`](#insn-007cbe30) → [`007cbe5c`](#insn-007cbe5c)
  - `FALL_THROUGH` [`007cbe30`](#insn-007cbe30) → [`007cbe34`](#insn-007cbe34)
- ブロック [`007cbe34`](#insn-007cbe34) 範囲 `[['007cbe34', '007cbe37']]`
  - `CONDITIONAL_JUMP` [`007cbe34`](#insn-007cbe34) → [`007cbe70`](#insn-007cbe70)
  - `FALL_THROUGH` [`007cbe34`](#insn-007cbe34) → [`007cbe38`](#insn-007cbe38)
- ブロック [`007cbe38`](#insn-007cbe38) 範囲 `[['007cbe38', '007cbe5b']]`
  - `FALL_THROUGH` [`007cbe58`](#insn-007cbe58) → [`007cbe5c`](#insn-007cbe5c)
- ブロック [`007cbe5c`](#insn-007cbe5c) 範囲 `[['007cbe5c', '007cbe6f']]`
- ブロック [`007cbe70`](#insn-007cbe70) 範囲 `[['007cbe70', '007cbe77']]`

## 命令位置別の参照

- [`007cbdec`](#insn-007cbdec) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007cbdf0`](#insn-007cbdf0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007cbdf4`](#insn-007cbdf4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007cbe04`](#insn-007cbe04) → [`00bdaff0`](../00bda/00bdaff0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaff0` · 推定シンボル `None` · 推定型 `None`
- [`007cbe1c`](#insn-007cbe1c) → `00bfffa8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`007cbe30`](#insn-007cbe30) → [`007cbe5c`](#insn-007cbe5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007cbe34`](#insn-007cbe34) → [`007cbe70`](#insn-007cbe70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007cbe3c`](#insn-007cbe3c) → [`00bdaff0`](../00bda/00bdaff0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaff0` · 推定シンボル `None` · 推定型 `None`
- [`007cbe54`](#insn-007cbe54) → [`00bdb160`](../00bdb/00bdb160.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb160` · 推定シンボル `None` · 推定型 `None`
- [`007cbe60`](#insn-007cbe60) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007cbe64`](#insn-007cbe64) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007cbe68`](#insn-007cbe68) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007cbe74`](#insn-007cbe74) → [`0044d968`](../0044d/0044d968.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0044d968` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`007cbdec`](#insn-007cbdec)

~~~json
{
  "source": "007cbdec",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007cbdf0`](#insn-007cbdf0)

~~~json
{
  "source": "007cbdf0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007cbdf4`](#insn-007cbdf4)

~~~json
{
  "source": "007cbdf4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007cbe04`](#insn-007cbe04)

~~~json
{
  "source": "007cbe04",
  "target": "00bdaff0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007cbe1c`](#insn-007cbe1c)

~~~json
{
  "source": "007cbe1c",
  "target": "00bfffa8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00bfffa8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`007cbe30`](#insn-007cbe30)

~~~json
{
  "source": "007cbe30",
  "target": "007cbe5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007cbe34`](#insn-007cbe34)

~~~json
{
  "source": "007cbe34",
  "target": "007cbe70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007cbe3c`](#insn-007cbe3c)

~~~json
{
  "source": "007cbe3c",
  "target": "00bdaff0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007cbe54`](#insn-007cbe54)

~~~json
{
  "source": "007cbe54",
  "target": "00bdb160",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007cbe60`](#insn-007cbe60)

~~~json
{
  "source": "007cbe60",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007cbe64`](#insn-007cbe64)

~~~json
{
  "source": "007cbe64",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007cbe68`](#insn-007cbe68)

~~~json
{
  "source": "007cbe68",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007cbe74`](#insn-007cbe74)

~~~json
{
  "source": "007cbe74",
  "target": "0044d968",
  "target_space": "ram",
  "resolution": "function"
}
~~~
