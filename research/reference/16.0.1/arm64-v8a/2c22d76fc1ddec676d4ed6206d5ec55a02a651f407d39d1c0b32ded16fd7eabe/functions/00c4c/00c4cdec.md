# 00c4cdec

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c4c9c4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4c9c4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0090.md#compare-b6207623b2dcd664d23dd321fe96d0e2)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00c4ce88`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4ce88.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0090.md#compare-e0388417e819e0b2b7eae8850189ff51)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00c4cdec",
  "name": "FUN_00c4cdec",
  "size": 280,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6fe8a631b7828fdd336ecd3605ad02af09b7449e1b36099a95015cfffc28de30",
  "source_text_sha256": "6fe8a631b7828fdd336ecd3605ad02af09b7449e1b36099a95015cfffc28de30",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00c4cdec",
        "00c4cf03"
      ]
    ],
    "bytes_sha256": "a2a730babc6944627a45700aa1ab2256aac8e24148221493534c4ba83a6b9214",
    "instruction_count": 70,
    "instruction_bytes": 280,
    "body_bytes": 280,
    "indirect": 4,
    "unresolved": 4
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5a0a0](../00c5a/00c5a0a0.md)
- [00c5b140](../00c5b/00c5b140.md)

## 関連文字列（未確認候補）

~~~text
"::friend "
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1356 bytes

~~~c

void FUN_00c4cdec(long param_1,undefined8 *param_2)

{
  ulong uVar1;
  undefined8 uVar2;
  void *__ptr;
  long lVar3;
  size_t __size;
  long *plVar4;
  
  plVar4 = *(long **)(param_1 + 0x10);
  (**(code **)(*plVar4 + 0x20))(plVar4);
  if ((*(ushort *)((long)plVar4 + 9) & 0xc0) != 0x40) {
    (**(code **)(*plVar4 + 0x28))(plVar4,param_2);
  }
  lVar3 = param_2[1];
  __ptr = (void *)*param_2;
  if ((ulong)param_2[2] < lVar3 + 9U) {
    __size = param_2[2] * 2;
    uVar1 = lVar3 + 0x3e9;
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
    lVar3 = param_2[1];
  }
  uVar2 = s___friend_002a5294._0_8_;
  ((char *)((long)__ptr + lVar3))[8] = ' ';
  *(undefined8 *)((long)__ptr + lVar3) = uVar2;
  plVar4 = *(long **)(param_1 + 0x18);
  lVar3 = *plVar4;
  param_2[1] = param_2[1] + 9;
  (**(code **)(lVar3 + 0x20))(plVar4,param_2);
  if ((*(ushort *)((long)plVar4 + 9) & 0xc0) == 0x40) {
    return;
  }
                    /* WARNING: Could not recover jumptable at 0x00c4cefc. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  (**(code **)(*plVar4 + 0x28))(plVar4,param_2);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00c4cdec"></a> `00c4cdec` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00c4cdf0"></a> `00c4cdf0` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00c4cdf4"></a> `00c4cdf4` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00c4cdf8"></a> `00c4cdf8` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00c4cdfc"></a> `00c4cdfc` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00c4ce00"></a> `00c4ce00` | `15 08 40 f9` | ldr x21,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00c4ce04"></a> `00c4ce04` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00c4ce08"></a> `00c4ce08` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00c4ce0c"></a> `00c4ce0c` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00c4ce10"></a> `00c4ce10` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00c4ce14"></a> `00c4ce14` | `08 11 40 f9` | ldr x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00c4ce18"></a> `00c4ce18` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00c4ce1c"></a> `00c4ce1c` | `a8 92 40 78` | ldurh w8,[x21, #0x9] | `FALL_THROUGH`
<a id="insn-00c4ce20"></a> `00c4ce20` | `08 05 1a 12` | and w8,w8,#0xc0 | `FALL_THROUGH`
<a id="insn-00c4ce24"></a> `00c4ce24` | `1f 01 01 71` | cmp w8,#0x40 | `FALL_THROUGH`
<a id="insn-00c4ce28"></a> `00c4ce28` | `c0 00 00 54` | b.eq 0x00c4ce40 | `CONDITIONAL_JUMP`
<a id="insn-00c4ce2c"></a> `00c4ce2c` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00c4ce30"></a> `00c4ce30` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00c4ce34"></a> `00c4ce34` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00c4ce38"></a> `00c4ce38` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00c4ce3c"></a> `00c4ce3c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00c4ce40"></a> `00c4ce40` | `68 a6 40 a9` | ldp x8,x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00c4ce44"></a> `00c4ce44` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00c4ce48"></a> `00c4ce48` | `0a 25 00 91` | add x10,x8,#0x9 | `FALL_THROUGH`
<a id="insn-00c4ce4c"></a> `00c4ce4c` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00c4ce50"></a> `00c4ce50` | `49 01 00 54` | b.ls 0x00c4ce78 | `CONDITIONAL_JUMP`
<a id="insn-00c4ce54"></a> `00c4ce54` | `29 f9 7f d3` | lsl x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00c4ce58"></a> `00c4ce58` | `08 a5 0f 91` | add x8,x8,#0x3e9 | `FALL_THROUGH`
<a id="insn-00c4ce5c"></a> `00c4ce5c` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00c4ce60"></a> `00c4ce60` | `21 81 88 9a` | csel x1,x9,x8,hi | `FALL_THROUGH`
<a id="insn-00c4ce64"></a> `00c4ce64` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00c4ce68"></a> `00c4ce68` | `8e 34 00 94` | bl 0x00c5a0a0 | `UNCONDITIONAL_CALL`
<a id="insn-00c4ce6c"></a> `00c4ce6c` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00c4ce70"></a> `00c4ce70` | `80 04 00 b4` | cbz x0,0x00c4cf00 | `CONDITIONAL_JUMP`
<a id="insn-00c4ce74"></a> `00c4ce74` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00c4ce78"></a> `00c4ce78` | `c9 b2 ff b0` | adrp x9,0x2a5000 | `FALL_THROUGH`
<a id="insn-00c4ce7c"></a> `00c4ce7c` | `29 51 0a 91` | add x9,x9,#0x294 | `FALL_THROUGH`
<a id="insn-00c4ce80"></a> `00c4ce80` | `08 00 08 8b` | add x8,x0,x8 | `FALL_THROUGH`
<a id="insn-00c4ce84"></a> `00c4ce84` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-00c4ce88"></a> `00c4ce88` | `0a 04 80 52` | mov w10,#0x20 | `FALL_THROUGH`
<a id="insn-00c4ce8c"></a> `00c4ce8c` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00c4ce90"></a> `00c4ce90` | `0a 21 00 39` | strb w10,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00c4ce94"></a> `00c4ce94` | `09 01 00 f9` | str x9,[x8] | `FALL_THROUGH`
<a id="insn-00c4ce98"></a> `00c4ce98` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00c4ce9c"></a> `00c4ce9c` | `94 0e 40 f9` | ldr x20,[x20, #0x18] | `FALL_THROUGH`
<a id="insn-00c4cea0"></a> `00c4cea0` | `08 25 00 91` | add x8,x8,#0x9 | `FALL_THROUGH`
<a id="insn-00c4cea4"></a> `00c4cea4` | `89 02 40 f9` | ldr x9,[x20] | `FALL_THROUGH`
<a id="insn-00c4cea8"></a> `00c4cea8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00c4ceac"></a> `00c4ceac` | `68 06 00 f9` | str x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00c4ceb0"></a> `00c4ceb0` | `28 11 40 f9` | ldr x8,[x9, #0x20] | `FALL_THROUGH`
<a id="insn-00c4ceb4"></a> `00c4ceb4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00c4ceb8"></a> `00c4ceb8` | `88 92 40 78` | ldurh w8,[x20, #0x9] | `FALL_THROUGH`
<a id="insn-00c4cebc"></a> `00c4cebc` | `08 05 1a 12` | and w8,w8,#0xc0 | `FALL_THROUGH`
<a id="insn-00c4cec0"></a> `00c4cec0` | `1f 01 01 71` | cmp w8,#0x40 | `FALL_THROUGH`
<a id="insn-00c4cec4"></a> `00c4cec4` | `c1 00 00 54` | b.ne 0x00c4cedc | `CONDITIONAL_JUMP`
<a id="insn-00c4cec8"></a> `00c4cec8` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00c4cecc"></a> `00c4cecc` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00c4ced0"></a> `00c4ced0` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00c4ced4"></a> `00c4ced4` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00c4ced8"></a> `00c4ced8` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00c4cedc"></a> `00c4cedc` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00c4cee0"></a> `00c4cee0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00c4cee4"></a> `00c4cee4` | `10 15 40 f9` | ldr x16,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00c4cee8"></a> `00c4cee8` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00c4ceec"></a> `00c4ceec` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00c4cef0"></a> `00c4cef0` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00c4cef4"></a> `00c4cef4` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00c4cef8"></a> `00c4cef8` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00c4cefc"></a> `00c4cefc` | `00 02 1f d6` | br x16 | `COMPUTED_JUMP`
<a id="insn-00c4cf00"></a> `00c4cf00` | `90 38 00 94` | bl 0x00c5b140 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00c4cdec`](#insn-00c4cdec) 範囲 `[['00c4cdec', '00c4ce2b']]`
  - `CONDITIONAL_JUMP` [`00c4ce28`](#insn-00c4ce28) → [`00c4ce40`](#insn-00c4ce40)
  - `FALL_THROUGH` [`00c4ce28`](#insn-00c4ce28) → [`00c4ce2c`](#insn-00c4ce2c)
- ブロック [`00c4ce2c`](#insn-00c4ce2c) 範囲 `[['00c4ce2c', '00c4ce3f']]`
  - `FALL_THROUGH` [`00c4ce3c`](#insn-00c4ce3c) → [`00c4ce40`](#insn-00c4ce40)
- ブロック [`00c4ce40`](#insn-00c4ce40) 範囲 `[['00c4ce40', '00c4ce53']]`
  - `CONDITIONAL_JUMP` [`00c4ce50`](#insn-00c4ce50) → [`00c4ce78`](#insn-00c4ce78)
  - `FALL_THROUGH` [`00c4ce50`](#insn-00c4ce50) → [`00c4ce54`](#insn-00c4ce54)
- ブロック [`00c4ce54`](#insn-00c4ce54) 範囲 `[['00c4ce54', '00c4ce73']]`
  - `CONDITIONAL_JUMP` [`00c4ce70`](#insn-00c4ce70) → [`00c4cf00`](#insn-00c4cf00)
  - `FALL_THROUGH` [`00c4ce70`](#insn-00c4ce70) → [`00c4ce74`](#insn-00c4ce74)
- ブロック [`00c4ce74`](#insn-00c4ce74) 範囲 `[['00c4ce74', '00c4ce77']]`
  - `FALL_THROUGH` [`00c4ce74`](#insn-00c4ce74) → [`00c4ce78`](#insn-00c4ce78)
- ブロック [`00c4ce78`](#insn-00c4ce78) 範囲 `[['00c4ce78', '00c4cec7']]`
  - `CONDITIONAL_JUMP` [`00c4cec4`](#insn-00c4cec4) → [`00c4cedc`](#insn-00c4cedc)
  - `FALL_THROUGH` [`00c4cec4`](#insn-00c4cec4) → [`00c4cec8`](#insn-00c4cec8)
- ブロック [`00c4cec8`](#insn-00c4cec8) 範囲 `[['00c4cec8', '00c4cedb']]`
- ブロック [`00c4cedc`](#insn-00c4cedc) 範囲 `[['00c4cedc', '00c4ceff']]`
- ブロック [`00c4cf00`](#insn-00c4cf00) 範囲 `[['00c4cf00', '00c4cf03']]`

## 命令位置別の参照

- [`00c4cdf0`](#insn-00c4cdf0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4cdf4`](#insn-00c4cdf4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4cdf8`](#insn-00c4cdf8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4ce28`](#insn-00c4ce28) → [`00c4ce40`](#insn-00c4ce40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4ce50`](#insn-00c4ce50) → [`00c4ce78`](#insn-00c4ce78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4ce68`](#insn-00c4ce68) → [`00c5a0a0`](../00c5a/00c5a0a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a0a0` · 推定シンボル `None` · 推定型 `None`
- [`00c4ce70`](#insn-00c4ce70) → [`00c4cf00`](#insn-00c4cf00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4ce84`](#insn-00c4ce84) → `002a5294`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00c4cec4`](#insn-00c4cec4) → [`00c4cedc`](#insn-00c4cedc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4cec8`](#insn-00c4cec8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4cecc`](#insn-00c4cecc) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4ced0`](#insn-00c4ced0) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4ceec`](#insn-00c4ceec) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4cef0`](#insn-00c4cef0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4cef4`](#insn-00c4cef4) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4cf00`](#insn-00c4cf00) → [`00c5b140`](../00c5b/00c5b140.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b140` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00c4cdf0`](#insn-00c4cdf0)

~~~json
{
  "source": "00c4cdf0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4cdf4`](#insn-00c4cdf4)

~~~json
{
  "source": "00c4cdf4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4cdf8`](#insn-00c4cdf8)

~~~json
{
  "source": "00c4cdf8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4ce28`](#insn-00c4ce28)

~~~json
{
  "source": "00c4ce28",
  "target": "00c4ce40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4ce50`](#insn-00c4ce50)

~~~json
{
  "source": "00c4ce50",
  "target": "00c4ce78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4ce68`](#insn-00c4ce68)

~~~json
{
  "source": "00c4ce68",
  "target": "00c5a0a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c4ce70`](#insn-00c4ce70)

~~~json
{
  "source": "00c4ce70",
  "target": "00c4cf00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4ce84`](#insn-00c4ce84)

~~~json
{
  "source": "00c4ce84",
  "target": "002a5294",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a5294",
  "offset": 0,
  "size": 10,
  "datatype": "string",
  "bytes": "3a3a667269656e642000",
  "capture_start": "002a5294",
  "capture_bytes": 10,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00c4cec4`](#insn-00c4cec4)

~~~json
{
  "source": "00c4cec4",
  "target": "00c4cedc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4cec8`](#insn-00c4cec8)

~~~json
{
  "source": "00c4cec8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4cecc`](#insn-00c4cecc)

~~~json
{
  "source": "00c4cecc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4ced0`](#insn-00c4ced0)

~~~json
{
  "source": "00c4ced0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4ceec`](#insn-00c4ceec)

~~~json
{
  "source": "00c4ceec",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4cef0`](#insn-00c4cef0)

~~~json
{
  "source": "00c4cef0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4cef4`](#insn-00c4cef4)

~~~json
{
  "source": "00c4cef4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4cf00`](#insn-00c4cf00)

~~~json
{
  "source": "00c4cf00",
  "target": "00c5b140",
  "target_space": "ram",
  "resolution": "function"
}
~~~
