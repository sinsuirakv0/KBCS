# 00c3cddc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00c3cd40`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3cd40.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0090.md#compare-0ca3dab5e7540935dfe761ac33973005)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00c3ddd0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3ddd0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0090.md#compare-d4a036e29545fc0cf65bc3263b7aa2b8)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00c3cddc",
  "name": "FUN_00c3cddc",
  "size": 160,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f565b9ac631e6ef9ce58d928405b84b1bb76969478079c9eabffecccd10c9194",
  "source_text_sha256": "f565b9ac631e6ef9ce58d928405b84b1bb76969478079c9eabffecccd10c9194",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00c3cddc",
        "00c3ce7b"
      ]
    ],
    "bytes_sha256": "7bc971d80161679bf3c13abfde961d11bcb3510a98d83d6de3dacbdaa68a7bed",
    "instruction_count": 40,
    "instruction_bytes": 160,
    "body_bytes": 160,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c3a214](../00c3a/00c3a214.md)

## 呼び出し先

- [00c580f0](../00c58/00c580f0.md)
- [00c5a0f0](../00c5a/00c5a0f0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1296 bytes

~~~c

void FUN_00c3cddc(long param_1,undefined8 *param_2)

{
  undefined8 *puVar1;
  long lVar2;
  void *pvVar3;
  undefined8 uVar4;
  undefined8 uVar5;
  
                    /* try { // try from 00c3cde4 to 00d3cdeb has its CatchHandler @ 00c3d174 */
  pvVar3 = *(void **)(param_1 + 0x1330);
                    /* try { // try from 00c3cdf4 to 00d3cdff has its CatchHandler @ 00c3d118 */
  lVar2 = *(long *)((long)pvVar3 + 8);
                    /* try { // try from 00c3ce00 to 00d3ce9b has its CatchHandler @ 00c3cb74 */
  puVar1 = pvVar3;
  if (lVar2 - 0xfd0U < 0xfffffffffffff010) {
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
  *(long *)((long)puVar1 + 8) = lVar2 + 0x20;
  *(undefined ***)((long)puVar1 + lVar2 + 0x10) = &PTR_FUN_00c99760;
  *(undefined1 *)((long)puVar1 + lVar2 + 0x18) = 10;
  uVar5 = param_2[1];
  uVar4 = *param_2;
  *(ushort *)((long)puVar1 + lVar2 + 0x19) =
       *(ushort *)((long)puVar1 + lVar2 + 0x19) & 0xf000 | 0x540;
  *(undefined8 *)((long)puVar1 + lVar2 + 0x28) = uVar5;
  *(undefined8 *)((long)puVar1 + lVar2 + 0x20) = uVar4;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00c3cddc"></a> `00c3cddc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00c3cde0"></a> `00c3cde0` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00c3cde4"></a> `00c3cde4` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00c3cde8"></a> `00c3cde8` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00c3cdec"></a> `00c3cdec` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00c3cdf0"></a> `00c3cdf0` | `15 98 49 f9` | ldr x21,[x0, #0x1330] | `FALL_THROUGH`
<a id="insn-00c3cdf4"></a> `00c3cdf4` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00c3cdf8"></a> `00c3cdf8` | `a8 06 40 f9` | ldr x8,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00c3cdfc"></a> `00c3cdfc` | `09 41 3f d1` | sub x9,x8,#0xfd0 | `FALL_THROUGH`
<a id="insn-00c3ce00"></a> `00c3ce00` | `3f c5 3f b1` | cmn x9,#0xff1 | `FALL_THROUGH`
<a id="insn-00c3ce04"></a> `00c3ce04` | `28 01 00 54` | b.hi 0x00c3ce28 | `CONDITIONAL_JUMP`
<a id="insn-00c3ce08"></a> `00c3ce08` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00c3ce0c"></a> `00c3ce0c` | `00 00 82 52` | mov w0,#0x1000 | `FALL_THROUGH`
<a id="insn-00c3ce10"></a> `00c3ce10` | `b8 74 00 94` | bl 0x00c5a0f0 | `UNCONDITIONAL_CALL`
<a id="insn-00c3ce14"></a> `00c3ce14` | `20 03 00 b4` | cbz x0,0x00c3ce78 | `CONDITIONAL_JUMP`
<a id="insn-00c3ce18"></a> `00c3ce18` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00c3ce1c"></a> `00c3ce1c` | `15 7c 00 a9` | stp x21,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00c3ce20"></a> `00c3ce20` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00c3ce24"></a> `00c3ce24` | `80 9a 09 f9` | str x0,[x20, #0x1330] | `FALL_THROUGH`
<a id="insn-00c3ce28"></a> `00c3ce28` | `09 81 00 91` | add x9,x8,#0x20 | `FALL_THROUGH`
<a id="insn-00c3ce2c"></a> `00c3ce2c` | `a0 02 08 8b` | add x0,x21,x8 | `FALL_THROUGH`
<a id="insn-00c3ce30"></a> `00c3ce30` | `e8 02 00 b0` | adrp x8,0xc99000 | `FALL_THROUGH`
<a id="insn-00c3ce34"></a> `00c3ce34` | `08 81 1d 91` | add x8,x8,#0x760 | `FALL_THROUGH`
<a id="insn-00c3ce38"></a> `00c3ce38` | `a9 06 00 f9` | str x9,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00c3ce3c"></a> `00c3ce3c` | `49 01 80 52` | mov w9,#0xa | `FALL_THROUGH`
<a id="insn-00c3ce40"></a> `00c3ce40` | `08 0c 01 f8` | str x8,[x0, #0x10]! | `FALL_THROUGH`
<a id="insn-00c3ce44"></a> `00c3ce44` | `08 90 40 78` | ldurh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00c3ce48"></a> `00c3ce48` | `09 20 00 39` | strb w9,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00c3ce4c"></a> `00c3ce4c` | `09 a8 80 52` | mov w9,#0x540 | `FALL_THROUGH`
<a id="insn-00c3ce50"></a> `00c3ce50` | `08 0d 14 12` | and w8,w8,#0xf000 | `FALL_THROUGH`
<a id="insn-00c3ce54"></a> `00c3ce54` | `60 02 c0 3d` | ldr q0,[x19] | `FALL_THROUGH`
<a id="insn-00c3ce58"></a> `00c3ce58` | `08 01 09 2a` | orr w8,w8,w9 | `FALL_THROUGH`
<a id="insn-00c3ce5c"></a> `00c3ce5c` | `08 90 00 78` | sturh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00c3ce60"></a> `00c3ce60` | `00 04 80 3d` | str q0,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00c3ce64"></a> `00c3ce64` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00c3ce68"></a> `00c3ce68` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00c3ce6c"></a> `00c3ce6c` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00c3ce70"></a> `00c3ce70` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00c3ce74"></a> `00c3ce74` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00c3ce78"></a> `00c3ce78` | `9e 6c 00 94` | bl 0x00c580f0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00c3cddc`](#insn-00c3cddc) 範囲 `[['00c3cddc', '00c3cde3']]`
  - `FALL_THROUGH` [`00c3cde0`](#insn-00c3cde0) → [`00c3cde4`](#insn-00c3cde4)
- ブロック [`00c3cde4`](#insn-00c3cde4) 範囲 `[['00c3cde4', '00c3cdf3']]`
  - `FALL_THROUGH` [`00c3cdf0`](#insn-00c3cdf0) → [`00c3cdf4`](#insn-00c3cdf4)
- ブロック [`00c3cdf4`](#insn-00c3cdf4) 範囲 `[['00c3cdf4', '00c3cdff']]`
  - `FALL_THROUGH` [`00c3cdfc`](#insn-00c3cdfc) → [`00c3ce00`](#insn-00c3ce00)
- ブロック [`00c3ce00`](#insn-00c3ce00) 範囲 `[['00c3ce00', '00c3ce07']]`
  - `CONDITIONAL_JUMP` [`00c3ce04`](#insn-00c3ce04) → [`00c3ce28`](#insn-00c3ce28)
  - `FALL_THROUGH` [`00c3ce04`](#insn-00c3ce04) → [`00c3ce08`](#insn-00c3ce08)
- ブロック [`00c3ce08`](#insn-00c3ce08) 範囲 `[['00c3ce08', '00c3ce17']]`
  - `CONDITIONAL_JUMP` [`00c3ce14`](#insn-00c3ce14) → [`00c3ce78`](#insn-00c3ce78)
  - `FALL_THROUGH` [`00c3ce14`](#insn-00c3ce14) → [`00c3ce18`](#insn-00c3ce18)
- ブロック [`00c3ce18`](#insn-00c3ce18) 範囲 `[['00c3ce18', '00c3ce27']]`
  - `FALL_THROUGH` [`00c3ce24`](#insn-00c3ce24) → [`00c3ce28`](#insn-00c3ce28)
- ブロック [`00c3ce28`](#insn-00c3ce28) 範囲 `[['00c3ce28', '00c3ce77']]`
- ブロック [`00c3ce78`](#insn-00c3ce78) 範囲 `[['00c3ce78', '00c3ce7b']]`

## 命令位置別の参照

- [`00c3cde0`](#insn-00c3cde0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3cde4`](#insn-00c3cde4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3cde8`](#insn-00c3cde8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3ce04`](#insn-00c3ce04) → [`00c3ce28`](#insn-00c3ce28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3ce10`](#insn-00c3ce10) → [`00c5a0f0`](../00c5a/00c5a0f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a0f0` · 推定シンボル `None` · 推定型 `None`
- [`00c3ce14`](#insn-00c3ce14) → [`00c3ce78`](#insn-00c3ce78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3ce40`](#insn-00c3ce40) → `00c99760`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00c3ce64`](#insn-00c3ce64) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3ce68`](#insn-00c3ce68) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3ce6c`](#insn-00c3ce6c) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3ce78`](#insn-00c3ce78) → [`00c580f0`](../00c58/00c580f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c580f0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00c3cde0`](#insn-00c3cde0)

~~~json
{
  "source": "00c3cde0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3cde4`](#insn-00c3cde4)

~~~json
{
  "source": "00c3cde4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3cde8`](#insn-00c3cde8)

~~~json
{
  "source": "00c3cde8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3ce04`](#insn-00c3ce04)

~~~json
{
  "source": "00c3ce04",
  "target": "00c3ce28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3ce10`](#insn-00c3ce10)

~~~json
{
  "source": "00c3ce10",
  "target": "00c5a0f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c3ce14`](#insn-00c3ce14)

~~~json
{
  "source": "00c3ce14",
  "target": "00c3ce78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3ce40`](#insn-00c3ce40)

~~~json
{
  "source": "00c3ce40",
  "target": "00c99760",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c99760",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00c3ce64`](#insn-00c3ce64)

~~~json
{
  "source": "00c3ce64",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3ce68`](#insn-00c3ce68)

~~~json
{
  "source": "00c3ce68",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3ce6c`](#insn-00c3ce6c)

~~~json
{
  "source": "00c3ce6c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3ce78`](#insn-00c3ce78)

~~~json
{
  "source": "00c3ce78",
  "target": "00c580f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
