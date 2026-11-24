# 00c4bedc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c4bab4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4bab4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0045.md#compare-6b72b1a082e8e0465ae787025fdf7f16)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00c4bf78`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4bf78.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0045.md#compare-c9f69236ada7c286e4b9d51dd30e9ed7)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00c4bedc",
  "name": "FUN_00c4bedc",
  "size": 148,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8636c54673b85131900c1529c43738eb2f40f2451ebbb0051b1832809f848c1c",
  "source_text_sha256": "8636c54673b85131900c1529c43738eb2f40f2451ebbb0051b1832809f848c1c",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00c4bedc",
        "00c4bf6f"
      ]
    ],
    "bytes_sha256": "9c5f1d572c0bd58653cd27e16a1db6525b34b7d2085d2ab9978a3ba20d64f648",
    "instruction_count": 37,
    "instruction_bytes": 148,
    "body_bytes": 148,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5a0a0](../00c5a/00c5a0a0.md)
- [00c5b140](../00c5b/00c5b140.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 893 bytes

~~~c

void FUN_00c4bedc(long param_1,undefined8 *param_2)

{
  ulong uVar1;
  void *__ptr;
  long lVar2;
  size_t __size;
  
  lVar2 = param_2[1];
  __ptr = (void *)*param_2;
  if ((ulong)param_2[2] < lVar2 + 1U) {
    __size = param_2[2] * 2;
    uVar1 = lVar2 + 0x3e1;
    if (__size < uVar1 || __size - uVar1 == 0) {
      __size = uVar1;
    }
    param_2[2] = __size;
    __ptr = realloc(__ptr,__size);
    *param_2 = __ptr;
    if (__ptr == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
      abort();
    }
    lVar2 = param_2[1];
  }
  *(undefined1 *)((long)__ptr + lVar2) = 0x7e;
  lVar2 = **(long **)(param_1 + 0x10);
  param_2[1] = param_2[1] + 1;
                    /* WARNING: Could not recover jumptable at 0x00c4bf68. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  (**(code **)(lVar2 + 0x20))();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00c4bedc"></a> `00c4bedc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00c4bee0"></a> `00c4bee0` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00c4bee4"></a> `00c4bee4` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00c4bee8"></a> `00c4bee8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00c4beec"></a> `00c4beec` | `29 a8 40 a9` | ldp x9,x10,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00c4bef0"></a> `00c4bef0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00c4bef4"></a> `00c4bef4` | `28 00 40 f9` | ldr x8,[x1] | `FALL_THROUGH`
<a id="insn-00c4bef8"></a> `00c4bef8` | `2b 05 00 91` | add x11,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00c4befc"></a> `00c4befc` | `7f 01 0a eb` | cmp x11,x10 | `FALL_THROUGH`
<a id="insn-00c4bf00"></a> `00c4bf00` | `e9 01 00 54` | b.ls 0x00c4bf3c | `CONDITIONAL_JUMP`
<a id="insn-00c4bf04"></a> `00c4bf04` | `4a f9 7f d3` | lsl x10,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00c4bf08"></a> `00c4bf08` | `29 85 0f 91` | add x9,x9,#0x3e1 | `FALL_THROUGH`
<a id="insn-00c4bf0c"></a> `00c4bf0c` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00c4bf10"></a> `00c4bf10` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00c4bf14"></a> `00c4bf14` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00c4bf18"></a> `00c4bf18` | `49 81 89 9a` | csel x9,x10,x9,hi | `FALL_THROUGH`
<a id="insn-00c4bf1c"></a> `00c4bf1c` | `29 08 00 f9` | str x9,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-00c4bf20"></a> `00c4bf20` | `e1 03 09 aa` | mov x1,x9 | `FALL_THROUGH`
<a id="insn-00c4bf24"></a> `00c4bf24` | `5f 38 00 94` | bl 0x00c5a0a0 | `UNCONDITIONAL_CALL`
<a id="insn-00c4bf28"></a> `00c4bf28` | `80 02 00 f9` | str x0,[x20] | `FALL_THROUGH`
<a id="insn-00c4bf2c"></a> `00c4bf2c` | `00 02 00 b4` | cbz x0,0x00c4bf6c | `CONDITIONAL_JUMP`
<a id="insn-00c4bf30"></a> `00c4bf30` | `89 06 40 f9` | ldr x9,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00c4bf34"></a> `00c4bf34` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00c4bf38"></a> `00c4bf38` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00c4bf3c"></a> `00c4bf3c` | `ca 0f 80 52` | mov w10,#0x7e | `FALL_THROUGH`
<a id="insn-00c4bf40"></a> `00c4bf40` | `0a 69 29 38` | strb w10,[x8, x9, LSL ] | `FALL_THROUGH`
<a id="insn-00c4bf44"></a> `00c4bf44` | `60 0a 40 f9` | ldr x0,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00c4bf48"></a> `00c4bf48` | `28 04 40 f9` | ldr x8,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00c4bf4c"></a> `00c4bf4c` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-00c4bf50"></a> `00c4bf50` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00c4bf54"></a> `00c4bf54` | `28 04 00 f9` | str x8,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00c4bf58"></a> `00c4bf58` | `30 11 40 f9` | ldr x16,[x9, #0x20] | `FALL_THROUGH`
<a id="insn-00c4bf5c"></a> `00c4bf5c` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00c4bf60"></a> `00c4bf60` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00c4bf64"></a> `00c4bf64` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00c4bf68"></a> `00c4bf68` | `00 02 1f d6` | br x16 | `COMPUTED_JUMP`
<a id="insn-00c4bf6c"></a> `00c4bf6c` | `75 3c 00 94` | bl 0x00c5b140 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00c4bedc`](#insn-00c4bedc) 範囲 `[['00c4bedc', '00c4bf03']]`
  - `CONDITIONAL_JUMP` [`00c4bf00`](#insn-00c4bf00) → [`00c4bf3c`](#insn-00c4bf3c)
  - `FALL_THROUGH` [`00c4bf00`](#insn-00c4bf00) → [`00c4bf04`](#insn-00c4bf04)
- ブロック [`00c4bf04`](#insn-00c4bf04) 範囲 `[['00c4bf04', '00c4bf2f']]`
  - `CONDITIONAL_JUMP` [`00c4bf2c`](#insn-00c4bf2c) → [`00c4bf6c`](#insn-00c4bf6c)
  - `FALL_THROUGH` [`00c4bf2c`](#insn-00c4bf2c) → [`00c4bf30`](#insn-00c4bf30)
- ブロック [`00c4bf30`](#insn-00c4bf30) 範囲 `[['00c4bf30', '00c4bf3b']]`
  - `FALL_THROUGH` [`00c4bf38`](#insn-00c4bf38) → [`00c4bf3c`](#insn-00c4bf3c)
- ブロック [`00c4bf3c`](#insn-00c4bf3c) 範囲 `[['00c4bf3c', '00c4bf6b']]`
- ブロック [`00c4bf6c`](#insn-00c4bf6c) 範囲 `[['00c4bf6c', '00c4bf6f']]`

## 命令位置別の参照

- [`00c4bee0`](#insn-00c4bee0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4bee4`](#insn-00c4bee4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4bf00`](#insn-00c4bf00) → [`00c4bf3c`](#insn-00c4bf3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4bf24`](#insn-00c4bf24) → [`00c5a0a0`](../00c5a/00c5a0a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a0a0` · 推定シンボル `None` · 推定型 `None`
- [`00c4bf2c`](#insn-00c4bf2c) → [`00c4bf6c`](#insn-00c4bf6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4bf5c`](#insn-00c4bf5c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4bf60`](#insn-00c4bf60) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4bf6c`](#insn-00c4bf6c) → [`00c5b140`](../00c5b/00c5b140.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b140` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00c4bee0`](#insn-00c4bee0)

~~~json
{
  "source": "00c4bee0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4bee4`](#insn-00c4bee4)

~~~json
{
  "source": "00c4bee4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4bf00`](#insn-00c4bf00)

~~~json
{
  "source": "00c4bf00",
  "target": "00c4bf3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4bf24`](#insn-00c4bf24)

~~~json
{
  "source": "00c4bf24",
  "target": "00c5a0a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c4bf2c`](#insn-00c4bf2c)

~~~json
{
  "source": "00c4bf2c",
  "target": "00c4bf6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4bf5c`](#insn-00c4bf5c)

~~~json
{
  "source": "00c4bf5c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4bf60`](#insn-00c4bf60)

~~~json
{
  "source": "00c4bf60",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4bf6c`](#insn-00c4bf6c)

~~~json
{
  "source": "00c4bf6c",
  "target": "00c5b140",
  "target_space": "ram",
  "resolution": "function"
}
~~~
