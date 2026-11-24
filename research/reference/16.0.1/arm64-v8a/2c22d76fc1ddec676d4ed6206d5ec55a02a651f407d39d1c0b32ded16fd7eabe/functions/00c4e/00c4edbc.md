# 00c4edbc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c4e994`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4e/00c4e994.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0090.md#compare-d35d6b63849869fadc9290343302a777)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00c4ee58`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4ee58.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0091.md#compare-593535b9d2b6996e1b563349f13817af)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00c4edbc",
  "name": "FUN_00c4edbc",
  "size": 172,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f58852b28c5a97a7dc52f09199fb23080dd554d53596a1e3d8de07995474f141",
  "source_text_sha256": "f58852b28c5a97a7dc52f09199fb23080dd554d53596a1e3d8de07995474f141",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00c4edbc",
        "00c4ee67"
      ]
    ],
    "bytes_sha256": "642362a8654acba13851c461a9d0c00c3aa8cbeb0dff02e0affdac56db0bbd57",
    "instruction_count": 43,
    "instruction_bytes": 172,
    "body_bytes": 172,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c3accc](../00c3a/00c3accc.md)

## 呼び出し先

- [00c58020](../00c58/00c58020.md)
- [00c5a020](../00c5a/00c5a020.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1083 bytes

~~~c

void FUN_00c4edbc(long param_1,undefined8 *param_2,undefined8 *param_3)

{
  undefined8 *puVar1;
  long lVar2;
  void *pvVar3;
  undefined8 uVar4;
  undefined8 uVar5;
  
  pvVar3 = *(void **)(param_1 + 0x1330);
  lVar2 = *(long *)((long)pvVar3 + 8);
  puVar1 = pvVar3;
  if (lVar2 - 0xfc0U < 0xfffffffffffff010) {
    puVar1 = malloc(0x1000);
    if (puVar1 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
      _ZSt9terminatev();
    }
    lVar2 = 0;
    *puVar1 = pvVar3;
    puVar1[1] = 0;
    *(undefined8 **)(param_1 + 0x1330) = puVar1;
  }
  *(long *)((long)puVar1 + 8) = lVar2 + 0x30;
  *(undefined ***)((long)puVar1 + lVar2 + 0x10) = &PTR_FUN_00c99c40;
  *(undefined1 *)((long)puVar1 + lVar2 + 0x18) = 5;
  uVar5 = param_3[1];
  uVar4 = *param_3;
  *(undefined8 *)((long)puVar1 + lVar2 + 0x20) = *param_2;
  *(ushort *)((long)puVar1 + lVar2 + 0x19) =
       *(ushort *)((long)puVar1 + lVar2 + 0x19) & 0xf000 | 0x540;
  *(undefined8 *)((long)puVar1 + lVar2 + 0x30) = uVar5;
  *(undefined8 *)((long)puVar1 + lVar2 + 0x28) = uVar4;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00c4edbc"></a> `00c4edbc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00c4edc0"></a> `00c4edc0` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00c4edc4"></a> `00c4edc4` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00c4edc8"></a> `00c4edc8` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00c4edcc"></a> `00c4edcc` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00c4edd0"></a> `00c4edd0` | `16 98 49 f9` | ldr x22,[x0, #0x1330] | `FALL_THROUGH`
<a id="insn-00c4edd4"></a> `00c4edd4` | `f3 03 02 aa` | mov x19,x2 | `FALL_THROUGH`
<a id="insn-00c4edd8"></a> `00c4edd8` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00c4eddc"></a> `00c4eddc` | `c8 06 40 f9` | ldr x8,[x22, #0x8] | `FALL_THROUGH`
<a id="insn-00c4ede0"></a> `00c4ede0` | `09 01 3f d1` | sub x9,x8,#0xfc0 | `FALL_THROUGH`
<a id="insn-00c4ede4"></a> `00c4ede4` | `3f c5 3f b1` | cmn x9,#0xff1 | `FALL_THROUGH`
<a id="insn-00c4ede8"></a> `00c4ede8` | `28 01 00 54` | b.hi 0x00c4ee0c | `CONDITIONAL_JUMP`
<a id="insn-00c4edec"></a> `00c4edec` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00c4edf0"></a> `00c4edf0` | `00 00 82 52` | mov w0,#0x1000 | `FALL_THROUGH`
<a id="insn-00c4edf4"></a> `00c4edf4` | `8b 2c 00 94` | bl 0x00c5a020 | `UNCONDITIONAL_CALL`
<a id="insn-00c4edf8"></a> `00c4edf8` | `60 03 00 b4` | cbz x0,0x00c4ee64 | `CONDITIONAL_JUMP`
<a id="insn-00c4edfc"></a> `00c4edfc` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00c4ee00"></a> `00c4ee00` | `16 7c 00 a9` | stp x22,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00c4ee04"></a> `00c4ee04` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00c4ee08"></a> `00c4ee08` | `a0 9a 09 f9` | str x0,[x21, #0x1330] | `FALL_THROUGH`
<a id="insn-00c4ee0c"></a> `00c4ee0c` | `09 c1 00 91` | add x9,x8,#0x30 | `FALL_THROUGH`
<a id="insn-00c4ee10"></a> `00c4ee10` | `c0 02 08 8b` | add x0,x22,x8 | `FALL_THROUGH`
<a id="insn-00c4ee14"></a> `00c4ee14` | `48 02 00 f0` | adrp x8,0xc99000 | `FALL_THROUGH`
<a id="insn-00c4ee18"></a> `00c4ee18` | `08 01 31 91` | add x8,x8,#0xc40 | `FALL_THROUGH`
<a id="insn-00c4ee1c"></a> `00c4ee1c` | `c9 06 00 f9` | str x9,[x22, #0x8] | `FALL_THROUGH`
<a id="insn-00c4ee20"></a> `00c4ee20` | `aa 00 80 52` | mov w10,#0x5 | `FALL_THROUGH`
<a id="insn-00c4ee24"></a> `00c4ee24` | `08 0c 01 f8` | str x8,[x0, #0x10]! | `FALL_THROUGH`
<a id="insn-00c4ee28"></a> `00c4ee28` | `08 90 40 78` | ldurh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00c4ee2c"></a> `00c4ee2c` | `0a 20 00 39` | strb w10,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00c4ee30"></a> `00c4ee30` | `89 02 40 f9` | ldr x9,[x20] | `FALL_THROUGH`
<a id="insn-00c4ee34"></a> `00c4ee34` | `0a a8 80 52` | mov w10,#0x540 | `FALL_THROUGH`
<a id="insn-00c4ee38"></a> `00c4ee38` | `08 0d 14 12` | and w8,w8,#0xf000 | `FALL_THROUGH`
<a id="insn-00c4ee3c"></a> `00c4ee3c` | `60 02 c0 3d` | ldr q0,[x19] | `FALL_THROUGH`
<a id="insn-00c4ee40"></a> `00c4ee40` | `08 01 0a 2a` | orr w8,w8,w10 | `FALL_THROUGH`
<a id="insn-00c4ee44"></a> `00c4ee44` | `09 08 00 f9` | str x9,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00c4ee48"></a> `00c4ee48` | `08 90 00 78` | sturh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00c4ee4c"></a> `00c4ee4c` | `00 80 81 3c` | stur q0,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00c4ee50"></a> `00c4ee50` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00c4ee54"></a> `00c4ee54` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00c4ee58"></a> `00c4ee58` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00c4ee5c"></a> `00c4ee5c` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00c4ee60"></a> `00c4ee60` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00c4ee64"></a> `00c4ee64` | `6f 24 00 94` | bl 0x00c58020 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00c4edbc`](#insn-00c4edbc) 範囲 `[['00c4edbc', '00c4edeb']]`
  - `CONDITIONAL_JUMP` [`00c4ede8`](#insn-00c4ede8) → [`00c4ee0c`](#insn-00c4ee0c)
  - `FALL_THROUGH` [`00c4ede8`](#insn-00c4ede8) → [`00c4edec`](#insn-00c4edec)
- ブロック [`00c4edec`](#insn-00c4edec) 範囲 `[['00c4edec', '00c4edfb']]`
  - `CONDITIONAL_JUMP` [`00c4edf8`](#insn-00c4edf8) → [`00c4ee64`](#insn-00c4ee64)
  - `FALL_THROUGH` [`00c4edf8`](#insn-00c4edf8) → [`00c4edfc`](#insn-00c4edfc)
- ブロック [`00c4edfc`](#insn-00c4edfc) 範囲 `[['00c4edfc', '00c4ee0b']]`
  - `FALL_THROUGH` [`00c4ee08`](#insn-00c4ee08) → [`00c4ee0c`](#insn-00c4ee0c)
- ブロック [`00c4ee0c`](#insn-00c4ee0c) 範囲 `[['00c4ee0c', '00c4ee63']]`
- ブロック [`00c4ee64`](#insn-00c4ee64) 範囲 `[['00c4ee64', '00c4ee67']]`

## 命令位置別の参照

- [`00c4edc0`](#insn-00c4edc0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4edc4`](#insn-00c4edc4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4edc8`](#insn-00c4edc8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4ede8`](#insn-00c4ede8) → [`00c4ee0c`](#insn-00c4ee0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4edf4`](#insn-00c4edf4) → [`00c5a020`](../00c5a/00c5a020.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a020` · 推定シンボル `None` · 推定型 `None`
- [`00c4edf8`](#insn-00c4edf8) → [`00c4ee64`](#insn-00c4ee64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4ee24`](#insn-00c4ee24) → `00c99c40`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00c4ee50`](#insn-00c4ee50) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4ee54`](#insn-00c4ee54) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4ee58`](#insn-00c4ee58) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4ee64`](#insn-00c4ee64) → [`00c58020`](../00c58/00c58020.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58020` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00c4edc0`](#insn-00c4edc0)

~~~json
{
  "source": "00c4edc0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4edc4`](#insn-00c4edc4)

~~~json
{
  "source": "00c4edc4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4edc8`](#insn-00c4edc8)

~~~json
{
  "source": "00c4edc8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4ede8`](#insn-00c4ede8)

~~~json
{
  "source": "00c4ede8",
  "target": "00c4ee0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4edf4`](#insn-00c4edf4)

~~~json
{
  "source": "00c4edf4",
  "target": "00c5a020",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c4edf8`](#insn-00c4edf8)

~~~json
{
  "source": "00c4edf8",
  "target": "00c4ee64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4ee24`](#insn-00c4ee24)

~~~json
{
  "source": "00c4ee24",
  "target": "00c99c40",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c99c40",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00c4ee50`](#insn-00c4ee50)

~~~json
{
  "source": "00c4ee50",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4ee54`](#insn-00c4ee54)

~~~json
{
  "source": "00c4ee54",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4ee58`](#insn-00c4ee58)

~~~json
{
  "source": "00c4ee58",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4ee64`](#insn-00c4ee64)

~~~json
{
  "source": "00c4ee64",
  "target": "00c58020",
  "target_space": "ram",
  "resolution": "function"
}
~~~
