# 00c3ddcc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00c3dd30`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3dd30.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0045.md#compare-4b585d378703cb5b748d2e9f450e38f3)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00c3edc0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3e/00c3edc0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0042.md#compare-c400c304327d586a547016df9a5592e9)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00c3ddcc",
  "name": "FUN_00c3ddcc",
  "size": 224,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f6eb2a6d90fdef19364a8c0296141aacb248ac1eb1812367065455ef3d58d18f",
  "source_text_sha256": "f6eb2a6d90fdef19364a8c0296141aacb248ac1eb1812367065455ef3d58d18f",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00c3ddcc",
        "00c3deab"
      ]
    ],
    "bytes_sha256": "10a8857d0946726125105c4d3f2af3dd4c43c0066e0a04ba06d7e97c14fc0421",
    "instruction_count": 56,
    "instruction_bytes": 224,
    "body_bytes": 224,
    "indirect": 2,
    "unresolved": 2
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c580d0](../00c58/00c580d0.md)
- [00c5a170](../00c5a/00c5a170.md)
- [00c5b210](../00c5b/00c5b210.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1223 bytes

~~~c

void FUN_00c3ddcc(long param_1,undefined8 *param_2)

{
  ulong uVar1;
  void *__ptr;
  size_t __size;
  long lVar2;
  long *plVar3;
  size_t __n;
  void *__src;
  
  __n = *(size_t *)(param_1 + 0x18);
  if (__n != 0) {
    lVar2 = param_2[1];
    __ptr = (void *)*param_2;
    __src = *(void **)(param_1 + 0x10);
    if ((ulong)param_2[2] < lVar2 + __n) {
      __size = param_2[2] * 2;
      uVar1 = lVar2 + __n + 0x3e0;
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
    memcpy((void *)((long)__ptr + lVar2),__src,__n);
    param_2[1] = param_2[1] + __n;
  }
  plVar3 = *(long **)(param_1 + 0x20);
  (**(code **)(*plVar3 + 0x20))(plVar3,param_2);
  if ((*(ushort *)((long)plVar3 + 9) & 0xc0) == 0x40) {
    return;
  }
                    /* WARNING: Could not recover jumptable at 0x00c3dea4. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  (**(code **)(*plVar3 + 0x28))(plVar3,param_2);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00c3ddcc"></a> `00c3ddcc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00c3ddd0"></a> `00c3ddd0` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00c3ddd4"></a> `00c3ddd4` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00c3ddd8"></a> `00c3ddd8` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00c3dddc"></a> `00c3dddc` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00c3dde0"></a> `00c3dde0` | `15 0c 40 f9` | ldr x21,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00c3dde4"></a> `00c3dde4` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00c3dde8"></a> `00c3dde8` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00c3ddec"></a> `00c3ddec` | `f5 02 00 b4` | cbz x21,0x00c3de48 | `CONDITIONAL_JUMP`
<a id="insn-00c3ddf0"></a> `00c3ddf0` | `68 a6 40 a9` | ldp x8,x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00c3ddf4"></a> `00c3ddf4` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00c3ddf8"></a> `00c3ddf8` | `96 0a 40 f9` | ldr x22,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00c3ddfc"></a> `00c3ddfc` | `0a 01 15 8b` | add x10,x8,x21 | `FALL_THROUGH`
<a id="insn-00c3de00"></a> `00c3de00` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00c3de04"></a> `00c3de04` | `49 01 00 54` | b.ls 0x00c3de2c | `CONDITIONAL_JUMP`
<a id="insn-00c3de08"></a> `00c3de08` | `28 f9 7f d3` | lsl x8,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00c3de0c"></a> `00c3de0c` | `49 81 0f 91` | add x9,x10,#0x3e0 | `FALL_THROUGH`
<a id="insn-00c3de10"></a> `00c3de10` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00c3de14"></a> `00c3de14` | `01 81 89 9a` | csel x1,x8,x9,hi | `FALL_THROUGH`
<a id="insn-00c3de18"></a> `00c3de18` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00c3de1c"></a> `00c3de1c` | `d5 70 00 94` | bl 0x00c5a170 | `UNCONDITIONAL_CALL`
<a id="insn-00c3de20"></a> `00c3de20` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00c3de24"></a> `00c3de24` | `20 04 00 b4` | cbz x0,0x00c3dea8 | `CONDITIONAL_JUMP`
<a id="insn-00c3de28"></a> `00c3de28` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00c3de2c"></a> `00c3de2c` | `00 00 08 8b` | add x0,x0,x8 | `FALL_THROUGH`
<a id="insn-00c3de30"></a> `00c3de30` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00c3de34"></a> `00c3de34` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-00c3de38"></a> `00c3de38` | `a6 68 00 94` | bl 0x00c580d0 | `UNCONDITIONAL_CALL`
<a id="insn-00c3de3c"></a> `00c3de3c` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00c3de40"></a> `00c3de40` | `08 01 15 8b` | add x8,x8,x21 | `FALL_THROUGH`
<a id="insn-00c3de44"></a> `00c3de44` | `68 06 00 f9` | str x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00c3de48"></a> `00c3de48` | `94 12 40 f9` | ldr x20,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-00c3de4c"></a> `00c3de4c` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00c3de50"></a> `00c3de50` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00c3de54"></a> `00c3de54` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00c3de58"></a> `00c3de58` | `08 11 40 f9` | ldr x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00c3de5c"></a> `00c3de5c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00c3de60"></a> `00c3de60` | `88 92 40 78` | ldurh w8,[x20, #0x9] | `FALL_THROUGH`
<a id="insn-00c3de64"></a> `00c3de64` | `08 05 1a 12` | and w8,w8,#0xc0 | `FALL_THROUGH`
<a id="insn-00c3de68"></a> `00c3de68` | `1f 01 01 71` | cmp w8,#0x40 | `FALL_THROUGH`
<a id="insn-00c3de6c"></a> `00c3de6c` | `c1 00 00 54` | b.ne 0x00c3de84 | `CONDITIONAL_JUMP`
<a id="insn-00c3de70"></a> `00c3de70` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00c3de74"></a> `00c3de74` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00c3de78"></a> `00c3de78` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00c3de7c"></a> `00c3de7c` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00c3de80"></a> `00c3de80` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00c3de84"></a> `00c3de84` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00c3de88"></a> `00c3de88` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00c3de8c"></a> `00c3de8c` | `10 15 40 f9` | ldr x16,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00c3de90"></a> `00c3de90` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00c3de94"></a> `00c3de94` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00c3de98"></a> `00c3de98` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00c3de9c"></a> `00c3de9c` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00c3dea0"></a> `00c3dea0` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00c3dea4"></a> `00c3dea4` | `00 02 1f d6` | br x16 | `COMPUTED_JUMP`
<a id="insn-00c3dea8"></a> `00c3dea8` | `da 74 00 94` | bl 0x00c5b210 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00c3ddcc`](#insn-00c3ddcc) 範囲 `[['00c3ddcc', '00c3ddef']]`
  - `CONDITIONAL_JUMP` [`00c3ddec`](#insn-00c3ddec) → [`00c3de48`](#insn-00c3de48)
  - `FALL_THROUGH` [`00c3ddec`](#insn-00c3ddec) → [`00c3ddf0`](#insn-00c3ddf0)
- ブロック [`00c3ddf0`](#insn-00c3ddf0) 範囲 `[['00c3ddf0', '00c3de07']]`
  - `CONDITIONAL_JUMP` [`00c3de04`](#insn-00c3de04) → [`00c3de2c`](#insn-00c3de2c)
  - `FALL_THROUGH` [`00c3de04`](#insn-00c3de04) → [`00c3de08`](#insn-00c3de08)
- ブロック [`00c3de08`](#insn-00c3de08) 範囲 `[['00c3de08', '00c3de27']]`
  - `CONDITIONAL_JUMP` [`00c3de24`](#insn-00c3de24) → [`00c3dea8`](#insn-00c3dea8)
  - `FALL_THROUGH` [`00c3de24`](#insn-00c3de24) → [`00c3de28`](#insn-00c3de28)
- ブロック [`00c3de28`](#insn-00c3de28) 範囲 `[['00c3de28', '00c3de2b']]`
  - `FALL_THROUGH` [`00c3de28`](#insn-00c3de28) → [`00c3de2c`](#insn-00c3de2c)
- ブロック [`00c3de2c`](#insn-00c3de2c) 範囲 `[['00c3de2c', '00c3de47']]`
  - `FALL_THROUGH` [`00c3de44`](#insn-00c3de44) → [`00c3de48`](#insn-00c3de48)
- ブロック [`00c3de48`](#insn-00c3de48) 範囲 `[['00c3de48', '00c3de6f']]`
  - `CONDITIONAL_JUMP` [`00c3de6c`](#insn-00c3de6c) → [`00c3de84`](#insn-00c3de84)
  - `FALL_THROUGH` [`00c3de6c`](#insn-00c3de6c) → [`00c3de70`](#insn-00c3de70)
- ブロック [`00c3de70`](#insn-00c3de70) 範囲 `[['00c3de70', '00c3de83']]`
- ブロック [`00c3de84`](#insn-00c3de84) 範囲 `[['00c3de84', '00c3dea7']]`
- ブロック [`00c3dea8`](#insn-00c3dea8) 範囲 `[['00c3dea8', '00c3deab']]`

## 命令位置別の参照

- [`00c3ddd0`](#insn-00c3ddd0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3ddd4`](#insn-00c3ddd4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3ddd8`](#insn-00c3ddd8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3ddec`](#insn-00c3ddec) → [`00c3de48`](#insn-00c3de48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3de04`](#insn-00c3de04) → [`00c3de2c`](#insn-00c3de2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3de1c`](#insn-00c3de1c) → [`00c5a170`](../00c5a/00c5a170.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a170` · 推定シンボル `None` · 推定型 `None`
- [`00c3de24`](#insn-00c3de24) → [`00c3dea8`](#insn-00c3dea8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3de38`](#insn-00c3de38) → [`00c580d0`](../00c58/00c580d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c580d0` · 推定シンボル `None` · 推定型 `None`
- [`00c3de6c`](#insn-00c3de6c) → [`00c3de84`](#insn-00c3de84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3de70`](#insn-00c3de70) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3de74`](#insn-00c3de74) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3de78`](#insn-00c3de78) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3de94`](#insn-00c3de94) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3de98`](#insn-00c3de98) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3de9c`](#insn-00c3de9c) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3dea8`](#insn-00c3dea8) → [`00c5b210`](../00c5b/00c5b210.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b210` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00c3ddd0`](#insn-00c3ddd0)

~~~json
{
  "source": "00c3ddd0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3ddd4`](#insn-00c3ddd4)

~~~json
{
  "source": "00c3ddd4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3ddd8`](#insn-00c3ddd8)

~~~json
{
  "source": "00c3ddd8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3ddec`](#insn-00c3ddec)

~~~json
{
  "source": "00c3ddec",
  "target": "00c3de48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3de04`](#insn-00c3de04)

~~~json
{
  "source": "00c3de04",
  "target": "00c3de2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3de1c`](#insn-00c3de1c)

~~~json
{
  "source": "00c3de1c",
  "target": "00c5a170",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c3de24`](#insn-00c3de24)

~~~json
{
  "source": "00c3de24",
  "target": "00c3dea8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3de38`](#insn-00c3de38)

~~~json
{
  "source": "00c3de38",
  "target": "00c580d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c3de6c`](#insn-00c3de6c)

~~~json
{
  "source": "00c3de6c",
  "target": "00c3de84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3de70`](#insn-00c3de70)

~~~json
{
  "source": "00c3de70",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3de74`](#insn-00c3de74)

~~~json
{
  "source": "00c3de74",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3de78`](#insn-00c3de78)

~~~json
{
  "source": "00c3de78",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3de94`](#insn-00c3de94)

~~~json
{
  "source": "00c3de94",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3de98`](#insn-00c3de98)

~~~json
{
  "source": "00c3de98",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3de9c`](#insn-00c3de9c)

~~~json
{
  "source": "00c3de9c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3dea8`](#insn-00c3dea8)

~~~json
{
  "source": "00c3dea8",
  "target": "00c5b210",
  "target_space": "ram",
  "resolution": "function"
}
~~~
