# 00c4cfbc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00c4cf20`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4cf20.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0045.md#compare-4d7e1b71af743535e016c3280cc3f9f0)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00c4dfb0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4d/00c4dfb0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0042.md#compare-49d40ff7c3a353d194e53d52630354e5)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00c4cfbc",
  "name": "FUN_00c4cfbc",
  "size": 260,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3621db4ded510631e2935d20362999c13747bb9adf96f4b7c208fc9f85b695e3",
  "source_text_sha256": "3621db4ded510631e2935d20362999c13747bb9adf96f4b7c208fc9f85b695e3",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00c4cfbc",
        "00c4d0bf"
      ]
    ],
    "bytes_sha256": "80b7deb7b16b1013ee7318c70dbccae3f606032fce6922652388c67cedf92b06",
    "instruction_count": 65,
    "instruction_bytes": 260,
    "body_bytes": 260,
    "indirect": 4,
    "unresolved": 4
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5a170](../00c5a/00c5a170.md)
- [00c5b210](../00c5b/00c5b210.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1256 bytes

~~~c

void FUN_00c4cfbc(long param_1,undefined8 *param_2)

{
  ulong uVar1;
  void *__ptr;
  long lVar2;
  size_t __size;
  long *plVar3;
  
  plVar3 = *(long **)(param_1 + 0x10);
  (**(code **)(*plVar3 + 0x20))(plVar3);
  if ((*(ushort *)((long)plVar3 + 9) & 0xc0) != 0x40) {
    (**(code **)(*plVar3 + 0x28))(plVar3,param_2);
  }
  lVar2 = param_2[1];
  __ptr = (void *)*param_2;
  if ((ulong)param_2[2] < lVar2 + 2U) {
    __size = param_2[2] * 2;
    uVar1 = lVar2 + 0x3e2;
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
  *(undefined2 *)((long)__ptr + lVar2) = 0x3a3a;
  plVar3 = *(long **)(param_1 + 0x18);
  lVar2 = *plVar3;
  param_2[1] = param_2[1] + 2;
  (**(code **)(lVar2 + 0x20))(plVar3,param_2);
  if ((*(ushort *)((long)plVar3 + 9) & 0xc0) == 0x40) {
    return;
  }
                    /* WARNING: Could not recover jumptable at 0x00c4d0b8. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  (**(code **)(*plVar3 + 0x28))(plVar3,param_2);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00c4cfbc"></a> `00c4cfbc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00c4cfc0"></a> `00c4cfc0` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00c4cfc4"></a> `00c4cfc4` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00c4cfc8"></a> `00c4cfc8` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00c4cfcc"></a> `00c4cfcc` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00c4cfd0"></a> `00c4cfd0` | `15 08 40 f9` | ldr x21,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00c4cfd4"></a> `00c4cfd4` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00c4cfd8"></a> `00c4cfd8` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00c4cfdc"></a> `00c4cfdc` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00c4cfe0"></a> `00c4cfe0` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00c4cfe4"></a> `00c4cfe4` | `08 11 40 f9` | ldr x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00c4cfe8"></a> `00c4cfe8` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00c4cfec"></a> `00c4cfec` | `a8 92 40 78` | ldurh w8,[x21, #0x9] | `FALL_THROUGH`
<a id="insn-00c4cff0"></a> `00c4cff0` | `08 05 1a 12` | and w8,w8,#0xc0 | `FALL_THROUGH`
<a id="insn-00c4cff4"></a> `00c4cff4` | `1f 01 01 71` | cmp w8,#0x40 | `FALL_THROUGH`
<a id="insn-00c4cff8"></a> `00c4cff8` | `c0 00 00 54` | b.eq 0x00c4d010 | `CONDITIONAL_JUMP`
<a id="insn-00c4cffc"></a> `00c4cffc` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00c4d000"></a> `00c4d000` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00c4d004"></a> `00c4d004` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00c4d008"></a> `00c4d008` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00c4d00c"></a> `00c4d00c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00c4d010"></a> `00c4d010` | `68 a6 40 a9` | ldp x8,x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00c4d014"></a> `00c4d014` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00c4d018"></a> `00c4d018` | `0a 09 00 91` | add x10,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00c4d01c"></a> `00c4d01c` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00c4d020"></a> `00c4d020` | `49 01 00 54` | b.ls 0x00c4d048 | `CONDITIONAL_JUMP`
<a id="insn-00c4d024"></a> `00c4d024` | `29 f9 7f d3` | lsl x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00c4d028"></a> `00c4d028` | `08 89 0f 91` | add x8,x8,#0x3e2 | `FALL_THROUGH`
<a id="insn-00c4d02c"></a> `00c4d02c` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00c4d030"></a> `00c4d030` | `21 81 88 9a` | csel x1,x9,x8,hi | `FALL_THROUGH`
<a id="insn-00c4d034"></a> `00c4d034` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00c4d038"></a> `00c4d038` | `4e 34 00 94` | bl 0x00c5a170 | `UNCONDITIONAL_CALL`
<a id="insn-00c4d03c"></a> `00c4d03c` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00c4d040"></a> `00c4d040` | `e0 03 00 b4` | cbz x0,0x00c4d0bc | `CONDITIONAL_JUMP`
<a id="insn-00c4d044"></a> `00c4d044` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00c4d048"></a> `00c4d048` | `49 47 87 52` | mov w9,#0x3a3a | `FALL_THROUGH`
<a id="insn-00c4d04c"></a> `00c4d04c` | `09 68 28 78` | strh w9,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00c4d050"></a> `00c4d050` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00c4d054"></a> `00c4d054` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00c4d058"></a> `00c4d058` | `94 0e 40 f9` | ldr x20,[x20, #0x18] | `FALL_THROUGH`
<a id="insn-00c4d05c"></a> `00c4d05c` | `08 09 00 91` | add x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00c4d060"></a> `00c4d060` | `89 02 40 f9` | ldr x9,[x20] | `FALL_THROUGH`
<a id="insn-00c4d064"></a> `00c4d064` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00c4d068"></a> `00c4d068` | `68 06 00 f9` | str x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00c4d06c"></a> `00c4d06c` | `28 11 40 f9` | ldr x8,[x9, #0x20] | `FALL_THROUGH`
<a id="insn-00c4d070"></a> `00c4d070` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00c4d074"></a> `00c4d074` | `88 92 40 78` | ldurh w8,[x20, #0x9] | `FALL_THROUGH`
<a id="insn-00c4d078"></a> `00c4d078` | `08 05 1a 12` | and w8,w8,#0xc0 | `FALL_THROUGH`
<a id="insn-00c4d07c"></a> `00c4d07c` | `1f 01 01 71` | cmp w8,#0x40 | `FALL_THROUGH`
<a id="insn-00c4d080"></a> `00c4d080` | `c1 00 00 54` | b.ne 0x00c4d098 | `CONDITIONAL_JUMP`
<a id="insn-00c4d084"></a> `00c4d084` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00c4d088"></a> `00c4d088` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00c4d08c"></a> `00c4d08c` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00c4d090"></a> `00c4d090` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00c4d094"></a> `00c4d094` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00c4d098"></a> `00c4d098` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00c4d09c"></a> `00c4d09c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00c4d0a0"></a> `00c4d0a0` | `10 15 40 f9` | ldr x16,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00c4d0a4"></a> `00c4d0a4` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00c4d0a8"></a> `00c4d0a8` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00c4d0ac"></a> `00c4d0ac` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00c4d0b0"></a> `00c4d0b0` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00c4d0b4"></a> `00c4d0b4` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00c4d0b8"></a> `00c4d0b8` | `00 02 1f d6` | br x16 | `COMPUTED_JUMP`
<a id="insn-00c4d0bc"></a> `00c4d0bc` | `55 38 00 94` | bl 0x00c5b210 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00c4cfbc`](#insn-00c4cfbc) 範囲 `[['00c4cfbc', '00c4cffb']]`
  - `CONDITIONAL_JUMP` [`00c4cff8`](#insn-00c4cff8) → [`00c4d010`](#insn-00c4d010)
  - `FALL_THROUGH` [`00c4cff8`](#insn-00c4cff8) → [`00c4cffc`](#insn-00c4cffc)
- ブロック [`00c4cffc`](#insn-00c4cffc) 範囲 `[['00c4cffc', '00c4d00f']]`
  - `FALL_THROUGH` [`00c4d00c`](#insn-00c4d00c) → [`00c4d010`](#insn-00c4d010)
- ブロック [`00c4d010`](#insn-00c4d010) 範囲 `[['00c4d010', '00c4d023']]`
  - `CONDITIONAL_JUMP` [`00c4d020`](#insn-00c4d020) → [`00c4d048`](#insn-00c4d048)
  - `FALL_THROUGH` [`00c4d020`](#insn-00c4d020) → [`00c4d024`](#insn-00c4d024)
- ブロック [`00c4d024`](#insn-00c4d024) 範囲 `[['00c4d024', '00c4d043']]`
  - `CONDITIONAL_JUMP` [`00c4d040`](#insn-00c4d040) → [`00c4d0bc`](#insn-00c4d0bc)
  - `FALL_THROUGH` [`00c4d040`](#insn-00c4d040) → [`00c4d044`](#insn-00c4d044)
- ブロック [`00c4d044`](#insn-00c4d044) 範囲 `[['00c4d044', '00c4d047']]`
  - `FALL_THROUGH` [`00c4d044`](#insn-00c4d044) → [`00c4d048`](#insn-00c4d048)
- ブロック [`00c4d048`](#insn-00c4d048) 範囲 `[['00c4d048', '00c4d083']]`
  - `CONDITIONAL_JUMP` [`00c4d080`](#insn-00c4d080) → [`00c4d098`](#insn-00c4d098)
  - `FALL_THROUGH` [`00c4d080`](#insn-00c4d080) → [`00c4d084`](#insn-00c4d084)
- ブロック [`00c4d084`](#insn-00c4d084) 範囲 `[['00c4d084', '00c4d097']]`
- ブロック [`00c4d098`](#insn-00c4d098) 範囲 `[['00c4d098', '00c4d0bb']]`
- ブロック [`00c4d0bc`](#insn-00c4d0bc) 範囲 `[['00c4d0bc', '00c4d0bf']]`

## 命令位置別の参照

- [`00c4cfc0`](#insn-00c4cfc0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4cfc4`](#insn-00c4cfc4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4cfc8`](#insn-00c4cfc8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4cff8`](#insn-00c4cff8) → [`00c4d010`](#insn-00c4d010) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4d020`](#insn-00c4d020) → [`00c4d048`](#insn-00c4d048) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4d038`](#insn-00c4d038) → [`00c5a170`](../00c5a/00c5a170.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a170` · 推定シンボル `None` · 推定型 `None`
- [`00c4d040`](#insn-00c4d040) → [`00c4d0bc`](#insn-00c4d0bc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4d080`](#insn-00c4d080) → [`00c4d098`](#insn-00c4d098) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4d084`](#insn-00c4d084) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4d088`](#insn-00c4d088) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4d08c`](#insn-00c4d08c) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4d0a8`](#insn-00c4d0a8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4d0ac`](#insn-00c4d0ac) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4d0b0`](#insn-00c4d0b0) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4d0bc`](#insn-00c4d0bc) → [`00c5b210`](../00c5b/00c5b210.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b210` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00c4cfc0`](#insn-00c4cfc0)

~~~json
{
  "source": "00c4cfc0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4cfc4`](#insn-00c4cfc4)

~~~json
{
  "source": "00c4cfc4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4cfc8`](#insn-00c4cfc8)

~~~json
{
  "source": "00c4cfc8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4cff8`](#insn-00c4cff8)

~~~json
{
  "source": "00c4cff8",
  "target": "00c4d010",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4d020`](#insn-00c4d020)

~~~json
{
  "source": "00c4d020",
  "target": "00c4d048",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4d038`](#insn-00c4d038)

~~~json
{
  "source": "00c4d038",
  "target": "00c5a170",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c4d040`](#insn-00c4d040)

~~~json
{
  "source": "00c4d040",
  "target": "00c4d0bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4d080`](#insn-00c4d080)

~~~json
{
  "source": "00c4d080",
  "target": "00c4d098",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4d084`](#insn-00c4d084)

~~~json
{
  "source": "00c4d084",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4d088`](#insn-00c4d088)

~~~json
{
  "source": "00c4d088",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4d08c`](#insn-00c4d08c)

~~~json
{
  "source": "00c4d08c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4d0a8`](#insn-00c4d0a8)

~~~json
{
  "source": "00c4d0a8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4d0ac`](#insn-00c4d0ac)

~~~json
{
  "source": "00c4d0ac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4d0b0`](#insn-00c4d0b0)

~~~json
{
  "source": "00c4d0b0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4d0bc`](#insn-00c4d0bc)

~~~json
{
  "source": "00c4d0bc",
  "target": "00c5b210",
  "target_space": "ram",
  "resolution": "function"
}
~~~
