# 00c4edac

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00c4ed10`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4ed10.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0091.md#compare-afb0a798488afdc7e71e777f2c4570d5)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00c4fda0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4f/00c4fda0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0091.md#compare-d1ab761e441c7e1c4479373da2018d0e)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00c4edac",
  "name": "FUN_00c4edac",
  "size": 172,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f3dbbdb49cb666cfbd75f2bd7c861913fda7d2bda95e922e7c0246989d3161ec",
  "source_text_sha256": "f3dbbdb49cb666cfbd75f2bd7c861913fda7d2bda95e922e7c0246989d3161ec",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00c4edac",
        "00c4ee57"
      ]
    ],
    "bytes_sha256": "43d8c1f8b980c10e3b04d8acf69b5f16836646583f6e1ff1c4bfc49a20a99be5",
    "instruction_count": 43,
    "instruction_bytes": 172,
    "body_bytes": 172,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c3ad68](../00c3a/00c3ad68.md)

## 呼び出し先

- [00c580f0](../00c58/00c580f0.md)
- [00c5a0f0](../00c5a/00c5a0f0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1025 bytes

~~~c

void FUN_00c4edac(long param_1,undefined8 *param_2,undefined1 *param_3)

{
  undefined1 uVar1;
  undefined8 *puVar2;
  long lVar3;
  undefined8 uVar4;
  void *pvVar5;
  
  pvVar5 = *(void **)(param_1 + 0x1330);
  lVar3 = *(long *)((long)pvVar5 + 8);
  puVar2 = pvVar5;
  if (lVar3 - 0xfd0U < 0xfffffffffffff010) {
    puVar2 = malloc(0x1000);
    if (puVar2 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
      _ZSt9terminatev();
    }
    lVar3 = 0;
    *puVar2 = pvVar5;
    puVar2[1] = 0;
    *(undefined8 **)(param_1 + 0x1330) = puVar2;
  }
  *(long *)((long)puVar2 + 8) = lVar3 + 0x20;
  *(undefined ***)((long)puVar2 + lVar3 + 0x10) = &PTR_FUN_00c99ca0;
  uVar4 = *param_2;
  *(undefined1 *)((long)puVar2 + lVar3 + 0x18) = 0x20;
  uVar1 = *param_3;
  *(undefined8 *)((long)puVar2 + lVar3 + 0x20) = uVar4;
  *(ushort *)((long)puVar2 + lVar3 + 0x19) =
       *(ushort *)((long)puVar2 + lVar3 + 0x19) & 0xf000 | 0x540;
  *(undefined1 *)((long)puVar2 + lVar3 + 0x28) = uVar1;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00c4edac"></a> `00c4edac` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00c4edb0"></a> `00c4edb0` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00c4edb4"></a> `00c4edb4` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00c4edb8"></a> `00c4edb8` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00c4edbc"></a> `00c4edbc` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00c4edc0"></a> `00c4edc0` | `16 98 49 f9` | ldr x22,[x0, #0x1330] | `FALL_THROUGH`
<a id="insn-00c4edc4"></a> `00c4edc4` | `f3 03 02 aa` | mov x19,x2 | `FALL_THROUGH`
<a id="insn-00c4edc8"></a> `00c4edc8` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00c4edcc"></a> `00c4edcc` | `c8 06 40 f9` | ldr x8,[x22, #0x8] | `FALL_THROUGH`
<a id="insn-00c4edd0"></a> `00c4edd0` | `09 41 3f d1` | sub x9,x8,#0xfd0 | `FALL_THROUGH`
<a id="insn-00c4edd4"></a> `00c4edd4` | `3f c5 3f b1` | cmn x9,#0xff1 | `FALL_THROUGH`
<a id="insn-00c4edd8"></a> `00c4edd8` | `28 01 00 54` | b.hi 0x00c4edfc | `CONDITIONAL_JUMP`
<a id="insn-00c4eddc"></a> `00c4eddc` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00c4ede0"></a> `00c4ede0` | `00 00 82 52` | mov w0,#0x1000 | `FALL_THROUGH`
<a id="insn-00c4ede4"></a> `00c4ede4` | `c3 2c 00 94` | bl 0x00c5a0f0 | `UNCONDITIONAL_CALL`
<a id="insn-00c4ede8"></a> `00c4ede8` | `60 03 00 b4` | cbz x0,0x00c4ee54 | `CONDITIONAL_JUMP`
<a id="insn-00c4edec"></a> `00c4edec` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00c4edf0"></a> `00c4edf0` | `16 7c 00 a9` | stp x22,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00c4edf4"></a> `00c4edf4` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00c4edf8"></a> `00c4edf8` | `a0 9a 09 f9` | str x0,[x21, #0x1330] | `FALL_THROUGH`
<a id="insn-00c4edfc"></a> `00c4edfc` | `09 81 00 91` | add x9,x8,#0x20 | `FALL_THROUGH`
<a id="insn-00c4ee00"></a> `00c4ee00` | `c0 02 08 8b` | add x0,x22,x8 | `FALL_THROUGH`
<a id="insn-00c4ee04"></a> `00c4ee04` | `48 02 00 f0` | adrp x8,0xc99000 | `FALL_THROUGH`
<a id="insn-00c4ee08"></a> `00c4ee08` | `08 81 32 91` | add x8,x8,#0xca0 | `FALL_THROUGH`
<a id="insn-00c4ee0c"></a> `00c4ee0c` | `c9 06 00 f9` | str x9,[x22, #0x8] | `FALL_THROUGH`
<a id="insn-00c4ee10"></a> `00c4ee10` | `0a 04 80 52` | mov w10,#0x20 | `FALL_THROUGH`
<a id="insn-00c4ee14"></a> `00c4ee14` | `08 0c 01 f8` | str x8,[x0, #0x10]! | `FALL_THROUGH`
<a id="insn-00c4ee18"></a> `00c4ee18` | `08 90 40 78` | ldurh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00c4ee1c"></a> `00c4ee1c` | `89 02 40 f9` | ldr x9,[x20] | `FALL_THROUGH`
<a id="insn-00c4ee20"></a> `00c4ee20` | `0a 20 00 39` | strb w10,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00c4ee24"></a> `00c4ee24` | `0a a8 80 52` | mov w10,#0x540 | `FALL_THROUGH`
<a id="insn-00c4ee28"></a> `00c4ee28` | `08 0d 14 12` | and w8,w8,#0xf000 | `FALL_THROUGH`
<a id="insn-00c4ee2c"></a> `00c4ee2c` | `6b 02 40 39` | ldrb w11,[x19] | `FALL_THROUGH`
<a id="insn-00c4ee30"></a> `00c4ee30` | `08 01 0a 2a` | orr w8,w8,w10 | `FALL_THROUGH`
<a id="insn-00c4ee34"></a> `00c4ee34` | `09 08 00 f9` | str x9,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00c4ee38"></a> `00c4ee38` | `08 90 00 78` | sturh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00c4ee3c"></a> `00c4ee3c` | `0b 60 00 39` | strb w11,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00c4ee40"></a> `00c4ee40` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00c4ee44"></a> `00c4ee44` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00c4ee48"></a> `00c4ee48` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00c4ee4c"></a> `00c4ee4c` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00c4ee50"></a> `00c4ee50` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00c4ee54"></a> `00c4ee54` | `a7 24 00 94` | bl 0x00c580f0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00c4edac`](#insn-00c4edac) 範囲 `[['00c4edac', '00c4eddb']]`
  - `CONDITIONAL_JUMP` [`00c4edd8`](#insn-00c4edd8) → [`00c4edfc`](#insn-00c4edfc)
  - `FALL_THROUGH` [`00c4edd8`](#insn-00c4edd8) → [`00c4eddc`](#insn-00c4eddc)
- ブロック [`00c4eddc`](#insn-00c4eddc) 範囲 `[['00c4eddc', '00c4edeb']]`
  - `CONDITIONAL_JUMP` [`00c4ede8`](#insn-00c4ede8) → [`00c4ee54`](#insn-00c4ee54)
  - `FALL_THROUGH` [`00c4ede8`](#insn-00c4ede8) → [`00c4edec`](#insn-00c4edec)
- ブロック [`00c4edec`](#insn-00c4edec) 範囲 `[['00c4edec', '00c4edfb']]`
  - `FALL_THROUGH` [`00c4edf8`](#insn-00c4edf8) → [`00c4edfc`](#insn-00c4edfc)
- ブロック [`00c4edfc`](#insn-00c4edfc) 範囲 `[['00c4edfc', '00c4ee53']]`
- ブロック [`00c4ee54`](#insn-00c4ee54) 範囲 `[['00c4ee54', '00c4ee57']]`

## 命令位置別の参照

- [`00c4edb0`](#insn-00c4edb0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4edb4`](#insn-00c4edb4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4edb8`](#insn-00c4edb8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4edd8`](#insn-00c4edd8) → [`00c4edfc`](#insn-00c4edfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4ede4`](#insn-00c4ede4) → [`00c5a0f0`](../00c5a/00c5a0f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a0f0` · 推定シンボル `None` · 推定型 `None`
- [`00c4ede8`](#insn-00c4ede8) → [`00c4ee54`](#insn-00c4ee54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4ee14`](#insn-00c4ee14) → `00c99ca0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00c4ee40`](#insn-00c4ee40) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4ee44`](#insn-00c4ee44) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4ee48`](#insn-00c4ee48) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4ee54`](#insn-00c4ee54) → [`00c580f0`](../00c58/00c580f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c580f0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00c4edb0`](#insn-00c4edb0)

~~~json
{
  "source": "00c4edb0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4edb4`](#insn-00c4edb4)

~~~json
{
  "source": "00c4edb4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4edb8`](#insn-00c4edb8)

~~~json
{
  "source": "00c4edb8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4edd8`](#insn-00c4edd8)

~~~json
{
  "source": "00c4edd8",
  "target": "00c4edfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4ede4`](#insn-00c4ede4)

~~~json
{
  "source": "00c4ede4",
  "target": "00c5a0f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c4ede8`](#insn-00c4ede8)

~~~json
{
  "source": "00c4ede8",
  "target": "00c4ee54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4ee14`](#insn-00c4ee14)

~~~json
{
  "source": "00c4ee14",
  "target": "00c99ca0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c99ca0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00c4ee40`](#insn-00c4ee40)

~~~json
{
  "source": "00c4ee40",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4ee44`](#insn-00c4ee44)

~~~json
{
  "source": "00c4ee44",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4ee48`](#insn-00c4ee48)

~~~json
{
  "source": "00c4ee48",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4ee54`](#insn-00c4ee54)

~~~json
{
  "source": "00c4ee54",
  "target": "00c580f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
