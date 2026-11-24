# 00c4cacc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00c4bad8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4bad8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0042.md#compare-2d280d831599fb3a7c8d4dc0a08a0448)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00c4cacc",
  "name": "FUN_00c4cacc",
  "size": 260,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "272ba724af96e1ef10d5dcbc3c276e03fbefe831cdce4c39258a160d18ee8950",
  "source_text_sha256": "272ba724af96e1ef10d5dcbc3c276e03fbefe831cdce4c39258a160d18ee8950",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00c4cacc",
        "00c4cbcf"
      ]
    ],
    "bytes_sha256": "7352ebd67f9410a1e7beb9b9c5d108da2f416890032ccaa3812dd5370d9e16d4",
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

- [00c5b140](../00c5b/00c5b140.md)
- [00c5c1e0](../00c5c/00c5c1e0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1256 bytes

~~~c

void FUN_00c4cacc(long param_1,undefined8 *param_2)

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
                    /* WARNING: Could not recover jumptable at 0x00c4cbc8. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  (**(code **)(*plVar3 + 0x28))(plVar3,param_2);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00c4cacc"></a> `00c4cacc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00c4cad0"></a> `00c4cad0` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00c4cad4"></a> `00c4cad4` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00c4cad8"></a> `00c4cad8` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00c4cadc"></a> `00c4cadc` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00c4cae0"></a> `00c4cae0` | `15 08 40 f9` | ldr x21,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00c4cae4"></a> `00c4cae4` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00c4cae8"></a> `00c4cae8` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00c4caec"></a> `00c4caec` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00c4caf0"></a> `00c4caf0` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00c4caf4"></a> `00c4caf4` | `08 11 40 f9` | ldr x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00c4caf8"></a> `00c4caf8` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00c4cafc"></a> `00c4cafc` | `a8 92 40 78` | ldurh w8,[x21, #0x9] | `FALL_THROUGH`
<a id="insn-00c4cb00"></a> `00c4cb00` | `08 05 1a 12` | and w8,w8,#0xc0 | `FALL_THROUGH`
<a id="insn-00c4cb04"></a> `00c4cb04` | `1f 01 01 71` | cmp w8,#0x40 | `FALL_THROUGH`
<a id="insn-00c4cb08"></a> `00c4cb08` | `c0 00 00 54` | b.eq 0x00c4cb20 | `CONDITIONAL_JUMP`
<a id="insn-00c4cb0c"></a> `00c4cb0c` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00c4cb10"></a> `00c4cb10` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00c4cb14"></a> `00c4cb14` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00c4cb18"></a> `00c4cb18` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00c4cb1c"></a> `00c4cb1c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00c4cb20"></a> `00c4cb20` | `68 a6 40 a9` | ldp x8,x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00c4cb24"></a> `00c4cb24` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00c4cb28"></a> `00c4cb28` | `0a 09 00 91` | add x10,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00c4cb2c"></a> `00c4cb2c` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00c4cb30"></a> `00c4cb30` | `49 01 00 54` | b.ls 0x00c4cb58 | `CONDITIONAL_JUMP`
<a id="insn-00c4cb34"></a> `00c4cb34` | `29 f9 7f d3` | lsl x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00c4cb38"></a> `00c4cb38` | `08 89 0f 91` | add x8,x8,#0x3e2 | `FALL_THROUGH`
<a id="insn-00c4cb3c"></a> `00c4cb3c` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00c4cb40"></a> `00c4cb40` | `21 81 88 9a` | csel x1,x9,x8,hi | `FALL_THROUGH`
<a id="insn-00c4cb44"></a> `00c4cb44` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00c4cb48"></a> `00c4cb48` | `7e 39 00 94` | bl 0x00c5b140 | `UNCONDITIONAL_CALL`
<a id="insn-00c4cb4c"></a> `00c4cb4c` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00c4cb50"></a> `00c4cb50` | `e0 03 00 b4` | cbz x0,0x00c4cbcc | `CONDITIONAL_JUMP`
<a id="insn-00c4cb54"></a> `00c4cb54` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00c4cb58"></a> `00c4cb58` | `49 47 87 52` | mov w9,#0x3a3a | `FALL_THROUGH`
<a id="insn-00c4cb5c"></a> `00c4cb5c` | `09 68 28 78` | strh w9,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00c4cb60"></a> `00c4cb60` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00c4cb64"></a> `00c4cb64` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00c4cb68"></a> `00c4cb68` | `94 0e 40 f9` | ldr x20,[x20, #0x18] | `FALL_THROUGH`
<a id="insn-00c4cb6c"></a> `00c4cb6c` | `08 09 00 91` | add x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00c4cb70"></a> `00c4cb70` | `89 02 40 f9` | ldr x9,[x20] | `FALL_THROUGH`
<a id="insn-00c4cb74"></a> `00c4cb74` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00c4cb78"></a> `00c4cb78` | `68 06 00 f9` | str x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00c4cb7c"></a> `00c4cb7c` | `28 11 40 f9` | ldr x8,[x9, #0x20] | `FALL_THROUGH`
<a id="insn-00c4cb80"></a> `00c4cb80` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00c4cb84"></a> `00c4cb84` | `88 92 40 78` | ldurh w8,[x20, #0x9] | `FALL_THROUGH`
<a id="insn-00c4cb88"></a> `00c4cb88` | `08 05 1a 12` | and w8,w8,#0xc0 | `FALL_THROUGH`
<a id="insn-00c4cb8c"></a> `00c4cb8c` | `1f 01 01 71` | cmp w8,#0x40 | `FALL_THROUGH`
<a id="insn-00c4cb90"></a> `00c4cb90` | `c1 00 00 54` | b.ne 0x00c4cba8 | `CONDITIONAL_JUMP`
<a id="insn-00c4cb94"></a> `00c4cb94` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00c4cb98"></a> `00c4cb98` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00c4cb9c"></a> `00c4cb9c` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00c4cba0"></a> `00c4cba0` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00c4cba4"></a> `00c4cba4` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00c4cba8"></a> `00c4cba8` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00c4cbac"></a> `00c4cbac` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00c4cbb0"></a> `00c4cbb0` | `10 15 40 f9` | ldr x16,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00c4cbb4"></a> `00c4cbb4` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00c4cbb8"></a> `00c4cbb8` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00c4cbbc"></a> `00c4cbbc` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00c4cbc0"></a> `00c4cbc0` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00c4cbc4"></a> `00c4cbc4` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00c4cbc8"></a> `00c4cbc8` | `00 02 1f d6` | br x16 | `COMPUTED_JUMP`
<a id="insn-00c4cbcc"></a> `00c4cbcc` | `85 3d 00 94` | bl 0x00c5c1e0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00c4cacc`](#insn-00c4cacc) 範囲 `[['00c4cacc', '00c4cb0b']]`
  - `CONDITIONAL_JUMP` [`00c4cb08`](#insn-00c4cb08) → [`00c4cb20`](#insn-00c4cb20)
  - `FALL_THROUGH` [`00c4cb08`](#insn-00c4cb08) → [`00c4cb0c`](#insn-00c4cb0c)
- ブロック [`00c4cb0c`](#insn-00c4cb0c) 範囲 `[['00c4cb0c', '00c4cb1f']]`
  - `FALL_THROUGH` [`00c4cb1c`](#insn-00c4cb1c) → [`00c4cb20`](#insn-00c4cb20)
- ブロック [`00c4cb20`](#insn-00c4cb20) 範囲 `[['00c4cb20', '00c4cb33']]`
  - `CONDITIONAL_JUMP` [`00c4cb30`](#insn-00c4cb30) → [`00c4cb58`](#insn-00c4cb58)
  - `FALL_THROUGH` [`00c4cb30`](#insn-00c4cb30) → [`00c4cb34`](#insn-00c4cb34)
- ブロック [`00c4cb34`](#insn-00c4cb34) 範囲 `[['00c4cb34', '00c4cb53']]`
  - `CONDITIONAL_JUMP` [`00c4cb50`](#insn-00c4cb50) → [`00c4cbcc`](#insn-00c4cbcc)
  - `FALL_THROUGH` [`00c4cb50`](#insn-00c4cb50) → [`00c4cb54`](#insn-00c4cb54)
- ブロック [`00c4cb54`](#insn-00c4cb54) 範囲 `[['00c4cb54', '00c4cb57']]`
  - `FALL_THROUGH` [`00c4cb54`](#insn-00c4cb54) → [`00c4cb58`](#insn-00c4cb58)
- ブロック [`00c4cb58`](#insn-00c4cb58) 範囲 `[['00c4cb58', '00c4cb93']]`
  - `CONDITIONAL_JUMP` [`00c4cb90`](#insn-00c4cb90) → [`00c4cba8`](#insn-00c4cba8)
  - `FALL_THROUGH` [`00c4cb90`](#insn-00c4cb90) → [`00c4cb94`](#insn-00c4cb94)
- ブロック [`00c4cb94`](#insn-00c4cb94) 範囲 `[['00c4cb94', '00c4cba7']]`
- ブロック [`00c4cba8`](#insn-00c4cba8) 範囲 `[['00c4cba8', '00c4cbcb']]`
- ブロック [`00c4cbcc`](#insn-00c4cbcc) 範囲 `[['00c4cbcc', '00c4cbcf']]`

## 命令位置別の参照

- [`00c4cad0`](#insn-00c4cad0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4cad4`](#insn-00c4cad4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4cad8`](#insn-00c4cad8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4cb08`](#insn-00c4cb08) → [`00c4cb20`](#insn-00c4cb20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4cb30`](#insn-00c4cb30) → [`00c4cb58`](#insn-00c4cb58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4cb48`](#insn-00c4cb48) → [`00c5b140`](../00c5b/00c5b140.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b140` · 推定シンボル `None` · 推定型 `None`
- [`00c4cb50`](#insn-00c4cb50) → [`00c4cbcc`](#insn-00c4cbcc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4cb90`](#insn-00c4cb90) → [`00c4cba8`](#insn-00c4cba8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4cb94`](#insn-00c4cb94) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4cb98`](#insn-00c4cb98) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4cb9c`](#insn-00c4cb9c) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4cbb8`](#insn-00c4cbb8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4cbbc`](#insn-00c4cbbc) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4cbc0`](#insn-00c4cbc0) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4cbcc`](#insn-00c4cbcc) → [`00c5c1e0`](../00c5c/00c5c1e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c1e0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00c4cad0`](#insn-00c4cad0)

~~~json
{
  "source": "00c4cad0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4cad4`](#insn-00c4cad4)

~~~json
{
  "source": "00c4cad4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4cad8`](#insn-00c4cad8)

~~~json
{
  "source": "00c4cad8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4cb08`](#insn-00c4cb08)

~~~json
{
  "source": "00c4cb08",
  "target": "00c4cb20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4cb30`](#insn-00c4cb30)

~~~json
{
  "source": "00c4cb30",
  "target": "00c4cb58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4cb48`](#insn-00c4cb48)

~~~json
{
  "source": "00c4cb48",
  "target": "00c5b140",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c4cb50`](#insn-00c4cb50)

~~~json
{
  "source": "00c4cb50",
  "target": "00c4cbcc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4cb90`](#insn-00c4cb90)

~~~json
{
  "source": "00c4cb90",
  "target": "00c4cba8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4cb94`](#insn-00c4cb94)

~~~json
{
  "source": "00c4cb94",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4cb98`](#insn-00c4cb98)

~~~json
{
  "source": "00c4cb98",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4cb9c`](#insn-00c4cb9c)

~~~json
{
  "source": "00c4cb9c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4cbb8`](#insn-00c4cbb8)

~~~json
{
  "source": "00c4cbb8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4cbbc`](#insn-00c4cbbc)

~~~json
{
  "source": "00c4cbbc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4cbc0`](#insn-00c4cbc0)

~~~json
{
  "source": "00c4cbc0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4cbcc`](#insn-00c4cbcc)

~~~json
{
  "source": "00c4cbcc",
  "target": "00c5c1e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
