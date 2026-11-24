# 00bcbac4

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bcba80`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcba80.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0018.md#compare-33bf2d4b3a0e884273f29ef4a3749818)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c4850c`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c4850c.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/inspection-0021.md#compare-6521e501e8c6c08ba1f56ebbb929285d)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcbac4",
  "name": "FUN_00bcbac4",
  "size": 188,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "18bf49f8154c85981da466cb02e34c046ec0ec8fc0e1335cbb8ff428030c944d",
  "source_text_sha256": "18bf49f8154c85981da466cb02e34c046ec0ec8fc0e1335cbb8ff428030c944d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcbac4",
        "00bcbb7f"
      ]
    ],
    "bytes_sha256": "e5bc3abddd378c39a3f224c76b2045e45816f4de9ff5e9e2b4b29bfe2b6f955f",
    "instruction_count": 47,
    "instruction_bytes": 188,
    "body_bytes": 188,
    "indirect": 2,
    "unresolved": 2
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdd250](../00bdd/00bdd250.md)
- [00bde2c0](../00bde/00bde2c0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1099 bytes

~~~c

void FUN_00bcbac4(long param_1,undefined8 *param_2)

{
  undefined8 *puVar1;
  ulong uVar2;
  void *__ptr;
  long lVar3;
  size_t __size;
  
  (**(code **)(**(long **)(param_1 + 0x18) + 0x20))();
  puVar1 = *(undefined8 **)(param_1 + 0x18);
  if ((*(byte *)((long)puVar1 + 9) & 0xc0) == 0x80) {
    uVar2 = (**(code **)*puVar1)(puVar1,param_2);
    if ((uVar2 & 1) != 0) {
      return;
    }
  }
  else if (*(byte *)((long)puVar1 + 9) < 0x40) {
    return;
  }
                    /* try { // try from 00bcbb20 to 00ccbc43 has its CatchHandler @ 00bcba3c */
  lVar3 = param_2[1];
  __ptr = (void *)*param_2;
  if ((ulong)param_2[2] < lVar3 + 1U) {
    __size = param_2[2] * 2;
    uVar2 = lVar3 + 0x3e1;
    if (__size < uVar2 || __size - uVar2 == 0) {
      __size = uVar2;
    }
    param_2[2] = __size;
    __ptr = realloc(__ptr,__size);
    *param_2 = __ptr;
    if (__ptr == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
      abort();
    }
    lVar3 = param_2[1];
  }
  *(undefined1 *)((long)__ptr + lVar3) = 0x20;
  param_2[1] = param_2[1] + 1;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcbac4"></a> `00bcbac4` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bcbac8"></a> `00bcbac8` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bcbacc"></a> `00bcbacc` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbad0"></a> `00bcbad0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bcbad4"></a> `00bcbad4` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bcbad8"></a> `00bcbad8` | `00 0c 40 f9` | ldr x0,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00bcbadc"></a> `00bcbadc` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bcbae0"></a> `00bcbae0` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bcbae4"></a> `00bcbae4` | `08 11 40 f9` | ldr x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00bcbae8"></a> `00bcbae8` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcbaec"></a> `00bcbaec` | `80 0e 40 f9` | ldr x0,[x20, #0x18] | `FALL_THROUGH`
<a id="insn-00bcbaf0"></a> `00bcbaf0` | `08 24 40 39` | ldrb w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00bcbaf4"></a> `00bcbaf4` | `09 05 1a 12` | and w9,w8,#0xc0 | `FALL_THROUGH`
<a id="insn-00bcbaf8"></a> `00bcbaf8` | `3f 01 02 71` | cmp w9,#0x80 | `FALL_THROUGH`
<a id="insn-00bcbafc"></a> `00bcbafc` | `e1 00 00 54` | b.ne 0x00bcbb18 | `CONDITIONAL_JUMP`
<a id="insn-00bcbb00"></a> `00bcbb00` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bcbb04"></a> `00bcbb04` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bcbb08"></a> `00bcbb08` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00bcbb0c"></a> `00bcbb0c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcbb10"></a> `00bcbb10` | `80 00 00 36` | tbz w0,#0x0,0x00bcbb20 | `CONDITIONAL_JUMP`
<a id="insn-00bcbb14"></a> `00bcbb14` | `16 00 00 14` | b 0x00bcbb6c | `UNCONDITIONAL_JUMP`
<a id="insn-00bcbb18"></a> `00bcbb18` | `1f 01 01 71` | cmp w8,#0x40 | `FALL_THROUGH`
<a id="insn-00bcbb1c"></a> `00bcbb1c` | `83 02 00 54` | b.cc 0x00bcbb6c | `CONDITIONAL_JUMP`
<a id="insn-00bcbb20"></a> `00bcbb20` | `68 a6 40 a9` | ldp x8,x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcbb24"></a> `00bcbb24` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00bcbb28"></a> `00bcbb28` | `0a 05 00 91` | add x10,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bcbb2c"></a> `00bcbb2c` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00bcbb30"></a> `00bcbb30` | `49 01 00 54` | b.ls 0x00bcbb58 | `CONDITIONAL_JUMP`
<a id="insn-00bcbb34"></a> `00bcbb34` | `29 f9 7f d3` | lsl x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bcbb38"></a> `00bcbb38` | `08 85 0f 91` | add x8,x8,#0x3e1 | `FALL_THROUGH`
<a id="insn-00bcbb3c"></a> `00bcbb3c` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bcbb40"></a> `00bcbb40` | `21 81 88 9a` | csel x1,x9,x8,hi | `FALL_THROUGH`
<a id="insn-00bcbb44"></a> `00bcbb44` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbb48"></a> `00bcbb48` | `c2 45 00 94` | bl 0x00bdd250 | `UNCONDITIONAL_CALL`
<a id="insn-00bcbb4c"></a> `00bcbb4c` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00bcbb50"></a> `00bcbb50` | `60 01 00 b4` | cbz x0,0x00bcbb7c | `CONDITIONAL_JUMP`
<a id="insn-00bcbb54"></a> `00bcbb54` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcbb58"></a> `00bcbb58` | `09 04 80 52` | mov w9,#0x20 | `FALL_THROUGH`
<a id="insn-00bcbb5c"></a> `00bcbb5c` | `09 68 28 38` | strb w9,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bcbb60"></a> `00bcbb60` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcbb64"></a> `00bcbb64` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bcbb68"></a> `00bcbb68` | `68 06 00 f9` | str x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcbb6c"></a> `00bcbb6c` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbb70"></a> `00bcbb70` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bcbb74"></a> `00bcbb74` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bcbb78"></a> `00bcbb78` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bcbb7c"></a> `00bcbb7c` | `d1 49 00 94` | bl 0x00bde2c0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcbac4`](#insn-00bcbac4) 範囲 `[['00bcbac4', '00bcbaff']]`
  - `CONDITIONAL_JUMP` [`00bcbafc`](#insn-00bcbafc) → [`00bcbb18`](#insn-00bcbb18)
  - `FALL_THROUGH` [`00bcbafc`](#insn-00bcbafc) → [`00bcbb00`](#insn-00bcbb00)
- ブロック [`00bcbb00`](#insn-00bcbb00) 範囲 `[['00bcbb00', '00bcbb13']]`
  - `CONDITIONAL_JUMP` [`00bcbb10`](#insn-00bcbb10) → [`00bcbb20`](#insn-00bcbb20)
  - `FALL_THROUGH` [`00bcbb10`](#insn-00bcbb10) → [`00bcbb14`](#insn-00bcbb14)
- ブロック [`00bcbb14`](#insn-00bcbb14) 範囲 `[['00bcbb14', '00bcbb17']]`
  - `UNCONDITIONAL_JUMP` [`00bcbb14`](#insn-00bcbb14) → [`00bcbb6c`](#insn-00bcbb6c)
- ブロック [`00bcbb18`](#insn-00bcbb18) 範囲 `[['00bcbb18', '00bcbb1f']]`
  - `CONDITIONAL_JUMP` [`00bcbb1c`](#insn-00bcbb1c) → [`00bcbb6c`](#insn-00bcbb6c)
  - `FALL_THROUGH` [`00bcbb1c`](#insn-00bcbb1c) → [`00bcbb20`](#insn-00bcbb20)
- ブロック [`00bcbb20`](#insn-00bcbb20) 範囲 `[['00bcbb20', '00bcbb33']]`
  - `CONDITIONAL_JUMP` [`00bcbb30`](#insn-00bcbb30) → [`00bcbb58`](#insn-00bcbb58)
  - `FALL_THROUGH` [`00bcbb30`](#insn-00bcbb30) → [`00bcbb34`](#insn-00bcbb34)
- ブロック [`00bcbb34`](#insn-00bcbb34) 範囲 `[['00bcbb34', '00bcbb53']]`
  - `CONDITIONAL_JUMP` [`00bcbb50`](#insn-00bcbb50) → [`00bcbb7c`](#insn-00bcbb7c)
  - `FALL_THROUGH` [`00bcbb50`](#insn-00bcbb50) → [`00bcbb54`](#insn-00bcbb54)
- ブロック [`00bcbb54`](#insn-00bcbb54) 範囲 `[['00bcbb54', '00bcbb57']]`
  - `FALL_THROUGH` [`00bcbb54`](#insn-00bcbb54) → [`00bcbb58`](#insn-00bcbb58)
- ブロック [`00bcbb58`](#insn-00bcbb58) 範囲 `[['00bcbb58', '00bcbb6b']]`
  - `FALL_THROUGH` [`00bcbb68`](#insn-00bcbb68) → [`00bcbb6c`](#insn-00bcbb6c)
- ブロック [`00bcbb6c`](#insn-00bcbb6c) 範囲 `[['00bcbb6c', '00bcbb7b']]`
- ブロック [`00bcbb7c`](#insn-00bcbb7c) 範囲 `[['00bcbb7c', '00bcbb7f']]`

## 命令位置別の参照

- [`00bcbac8`](#insn-00bcbac8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbacc`](#insn-00bcbacc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbafc`](#insn-00bcbafc) → [`00bcbb18`](#insn-00bcbb18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbb10`](#insn-00bcbb10) → [`00bcbb20`](#insn-00bcbb20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbb14`](#insn-00bcbb14) → [`00bcbb6c`](#insn-00bcbb6c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbb1c`](#insn-00bcbb1c) → [`00bcbb6c`](#insn-00bcbb6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbb30`](#insn-00bcbb30) → [`00bcbb58`](#insn-00bcbb58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbb48`](#insn-00bcbb48) → [`00bdd250`](../00bdd/00bdd250.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd250` · 推定シンボル `None` · 推定型 `None`
- [`00bcbb50`](#insn-00bcbb50) → [`00bcbb7c`](#insn-00bcbb7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbb6c`](#insn-00bcbb6c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbb70`](#insn-00bcbb70) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbb7c`](#insn-00bcbb7c) → [`00bde2c0`](../00bde/00bde2c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde2c0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcbac8`](#insn-00bcbac8)

~~~json
{
  "source": "00bcbac8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbacc`](#insn-00bcbacc)

~~~json
{
  "source": "00bcbacc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbafc`](#insn-00bcbafc)

~~~json
{
  "source": "00bcbafc",
  "target": "00bcbb18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbb10`](#insn-00bcbb10)

~~~json
{
  "source": "00bcbb10",
  "target": "00bcbb20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbb14`](#insn-00bcbb14)

~~~json
{
  "source": "00bcbb14",
  "target": "00bcbb6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbb1c`](#insn-00bcbb1c)

~~~json
{
  "source": "00bcbb1c",
  "target": "00bcbb6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbb30`](#insn-00bcbb30)

~~~json
{
  "source": "00bcbb30",
  "target": "00bcbb58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbb48`](#insn-00bcbb48)

~~~json
{
  "source": "00bcbb48",
  "target": "00bdd250",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbb50`](#insn-00bcbb50)

~~~json
{
  "source": "00bcbb50",
  "target": "00bcbb7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbb6c`](#insn-00bcbb6c)

~~~json
{
  "source": "00bcbb6c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbb70`](#insn-00bcbb70)

~~~json
{
  "source": "00bcbb70",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbb7c`](#insn-00bcbb7c)

~~~json
{
  "source": "00bcbb7c",
  "target": "00bde2c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
