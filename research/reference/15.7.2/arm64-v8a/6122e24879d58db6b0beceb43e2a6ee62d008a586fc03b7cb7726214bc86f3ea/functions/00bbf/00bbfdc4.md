# 00bbfdc4

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bbfe8c`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbfe8c.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0078.md#compare-c156f642a8430bf631f5d6adecc39d99)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbfdc4",
  "name": "FUN_00bbfdc4",
  "size": 160,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c6ee217db0878d958655067299c7be2cc79b4c07451c004b84673c658e91d3ab",
  "source_text_sha256": "c6ee217db0878d958655067299c7be2cc79b4c07451c004b84673c658e91d3ab",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbfdc4",
        "00bbfe63"
      ]
    ],
    "bytes_sha256": "bb3a277947063ae79ac95e5e110f4f6231ae71db3eb11333f4f47fe02a435d77",
    "instruction_count": 40,
    "instruction_bytes": 160,
    "body_bytes": 160,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bbd1fc](../00bbd/00bbd1fc.md)

## 呼び出し先

- [00bdb0d0](../00bdb/00bdb0d0.md)
- [00bdd0d0](../00bdd/00bdd0d0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1393 bytes

~~~c

void FUN_00bbfdc4(long param_1,undefined8 *param_2)

{
  undefined8 *puVar1;
  long lVar2;
  void *pvVar3;
  undefined8 uVar4;
  undefined8 uVar5;
  
  pvVar3 = *(void **)(param_1 + 0x1330);
                    /* try { // try from 00bbfde0 to 00cbfdeb has its CatchHandler @ 00bc82e8 */
  lVar2 = *(long *)((long)pvVar3 + 8);
                    /* try { // try from 00bbfdec to 00cbfdf7 has its CatchHandler @ 00bc82d8 */
  puVar1 = pvVar3;
  if (lVar2 - 0xfd0U < 0xfffffffffffff010) {
                    /* try { // try from 00bbfdf8 to 00cbfe03 has its CatchHandler @ 00bc82c8 */
    puVar1 = malloc(0x1000);
    if (puVar1 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
      _ZSt9terminatev();
    }
    lVar2 = 0;
                    /* try { // try from 00bbfe04 to 00cbfe6b has its CatchHandler @ 00bbf464 */
    *puVar1 = pvVar3;
    puVar1[1] = 0;
    *(undefined8 **)(param_1 + 0x1330) = puVar1;
  }
  *(long *)((long)puVar1 + 8) = lVar2 + 0x20;
  *(undefined ***)((long)puVar1 + lVar2 + 0x10) = &PTR_FUN_00c197e8;
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
<a id="insn-00bbfdc4"></a> `00bbfdc4` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bbfdc8"></a> `00bbfdc8` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bbfdcc"></a> `00bbfdcc` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbfdd0"></a> `00bbfdd0` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbfdd4"></a> `00bbfdd4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bbfdd8"></a> `00bbfdd8` | `15 98 49 f9` | ldr x21,[x0, #0x1330] | `FALL_THROUGH`
<a id="insn-00bbfddc"></a> `00bbfddc` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bbfde0"></a> `00bbfde0` | `a8 06 40 f9` | ldr x8,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00bbfde4"></a> `00bbfde4` | `09 41 3f d1` | sub x9,x8,#0xfd0 | `FALL_THROUGH`
<a id="insn-00bbfde8"></a> `00bbfde8` | `3f c5 3f b1` | cmn x9,#0xff1 | `FALL_THROUGH`
<a id="insn-00bbfdec"></a> `00bbfdec` | `28 01 00 54` | b.hi 0x00bbfe10 | `CONDITIONAL_JUMP`
<a id="insn-00bbfdf0"></a> `00bbfdf0` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bbfdf4"></a> `00bbfdf4` | `00 00 82 52` | mov w0,#0x1000 | `FALL_THROUGH`
<a id="insn-00bbfdf8"></a> `00bbfdf8` | `b6 74 00 94` | bl 0x00bdd0d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbfdfc"></a> `00bbfdfc` | `20 03 00 b4` | cbz x0,0x00bbfe60 | `CONDITIONAL_JUMP`
<a id="insn-00bbfe00"></a> `00bbfe00` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbfe04"></a> `00bbfe04` | `15 7c 00 a9` | stp x21,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00bbfe08"></a> `00bbfe08` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bbfe0c"></a> `00bbfe0c` | `80 9a 09 f9` | str x0,[x20, #0x1330] | `FALL_THROUGH`
<a id="insn-00bbfe10"></a> `00bbfe10` | `09 81 00 91` | add x9,x8,#0x20 | `FALL_THROUGH`
<a id="insn-00bbfe14"></a> `00bbfe14` | `a0 02 08 8b` | add x0,x21,x8 | `FALL_THROUGH`
<a id="insn-00bbfe18"></a> `00bbfe18` | `c8 02 00 d0` | adrp x8,0xc19000 | `FALL_THROUGH`
<a id="insn-00bbfe1c"></a> `00bbfe1c` | `08 a1 1f 91` | add x8,x8,#0x7e8 | `FALL_THROUGH`
<a id="insn-00bbfe20"></a> `00bbfe20` | `a9 06 00 f9` | str x9,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00bbfe24"></a> `00bbfe24` | `49 01 80 52` | mov w9,#0xa | `FALL_THROUGH`
<a id="insn-00bbfe28"></a> `00bbfe28` | `08 0c 01 f8` | str x8,[x0, #0x10]! | `FALL_THROUGH`
<a id="insn-00bbfe2c"></a> `00bbfe2c` | `08 90 40 78` | ldurh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00bbfe30"></a> `00bbfe30` | `09 20 00 39` | strb w9,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bbfe34"></a> `00bbfe34` | `09 a8 80 52` | mov w9,#0x540 | `FALL_THROUGH`
<a id="insn-00bbfe38"></a> `00bbfe38` | `08 0d 14 12` | and w8,w8,#0xf000 | `FALL_THROUGH`
<a id="insn-00bbfe3c"></a> `00bbfe3c` | `60 02 c0 3d` | ldr q0,[x19] | `FALL_THROUGH`
<a id="insn-00bbfe40"></a> `00bbfe40` | `08 01 09 2a` | orr w8,w8,w9 | `FALL_THROUGH`
<a id="insn-00bbfe44"></a> `00bbfe44` | `08 90 00 78` | sturh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00bbfe48"></a> `00bbfe48` | `00 04 80 3d` | str q0,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bbfe4c"></a> `00bbfe4c` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbfe50"></a> `00bbfe50` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbfe54"></a> `00bbfe54` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bbfe58"></a> `00bbfe58` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bbfe5c"></a> `00bbfe5c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bbfe60"></a> `00bbfe60` | `9c 6c 00 94` | bl 0x00bdb0d0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbfdc4`](#insn-00bbfdc4) 範囲 `[['00bbfdc4', '00bbfddf']]`
  - `FALL_THROUGH` [`00bbfddc`](#insn-00bbfddc) → [`00bbfde0`](#insn-00bbfde0)
- ブロック [`00bbfde0`](#insn-00bbfde0) 範囲 `[['00bbfde0', '00bbfdeb']]`
  - `FALL_THROUGH` [`00bbfde8`](#insn-00bbfde8) → [`00bbfdec`](#insn-00bbfdec)
- ブロック [`00bbfdec`](#insn-00bbfdec) 範囲 `[['00bbfdec', '00bbfdef']]`
  - `CONDITIONAL_JUMP` [`00bbfdec`](#insn-00bbfdec) → [`00bbfe10`](#insn-00bbfe10)
  - `FALL_THROUGH` [`00bbfdec`](#insn-00bbfdec) → [`00bbfdf0`](#insn-00bbfdf0)
- ブロック [`00bbfdf0`](#insn-00bbfdf0) 範囲 `[['00bbfdf0', '00bbfdf7']]`
  - `FALL_THROUGH` [`00bbfdf4`](#insn-00bbfdf4) → [`00bbfdf8`](#insn-00bbfdf8)
- ブロック [`00bbfdf8`](#insn-00bbfdf8) 範囲 `[['00bbfdf8', '00bbfdff']]`
  - `CONDITIONAL_JUMP` [`00bbfdfc`](#insn-00bbfdfc) → [`00bbfe60`](#insn-00bbfe60)
  - `FALL_THROUGH` [`00bbfdfc`](#insn-00bbfdfc) → [`00bbfe00`](#insn-00bbfe00)
- ブロック [`00bbfe00`](#insn-00bbfe00) 範囲 `[['00bbfe00', '00bbfe03']]`
  - `FALL_THROUGH` [`00bbfe00`](#insn-00bbfe00) → [`00bbfe04`](#insn-00bbfe04)
- ブロック [`00bbfe04`](#insn-00bbfe04) 範囲 `[['00bbfe04', '00bbfe0f']]`
  - `FALL_THROUGH` [`00bbfe0c`](#insn-00bbfe0c) → [`00bbfe10`](#insn-00bbfe10)
- ブロック [`00bbfe10`](#insn-00bbfe10) 範囲 `[['00bbfe10', '00bbfe5f']]`
- ブロック [`00bbfe60`](#insn-00bbfe60) 範囲 `[['00bbfe60', '00bbfe63']]`

## 命令位置別の参照

- [`00bbfdc8`](#insn-00bbfdc8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfdcc`](#insn-00bbfdcc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfdd0`](#insn-00bbfdd0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfdec`](#insn-00bbfdec) → [`00bbfe10`](#insn-00bbfe10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfdf8`](#insn-00bbfdf8) → [`00bdd0d0`](../00bdd/00bdd0d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd0d0` · 推定シンボル `None` · 推定型 `None`
- [`00bbfdfc`](#insn-00bbfdfc) → [`00bbfe60`](#insn-00bbfe60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfe28`](#insn-00bbfe28) → `00c197e8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00bbfe4c`](#insn-00bbfe4c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfe50`](#insn-00bbfe50) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfe54`](#insn-00bbfe54) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfe60`](#insn-00bbfe60) → [`00bdb0d0`](../00bdb/00bdb0d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb0d0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbfdc8`](#insn-00bbfdc8)

~~~json
{
  "source": "00bbfdc8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfdcc`](#insn-00bbfdcc)

~~~json
{
  "source": "00bbfdcc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfdd0`](#insn-00bbfdd0)

~~~json
{
  "source": "00bbfdd0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfdec`](#insn-00bbfdec)

~~~json
{
  "source": "00bbfdec",
  "target": "00bbfe10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfdf8`](#insn-00bbfdf8)

~~~json
{
  "source": "00bbfdf8",
  "target": "00bdd0d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbfdfc`](#insn-00bbfdfc)

~~~json
{
  "source": "00bbfdfc",
  "target": "00bbfe60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfe28`](#insn-00bbfe28)

~~~json
{
  "source": "00bbfe28",
  "target": "00c197e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c197e8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbfe4c`](#insn-00bbfe4c)

~~~json
{
  "source": "00bbfe4c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfe50`](#insn-00bbfe50)

~~~json
{
  "source": "00bbfe50",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfe54`](#insn-00bbfe54)

~~~json
{
  "source": "00bbfe54",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfe60`](#insn-00bbfe60)

~~~json
{
  "source": "00bbfe60",
  "target": "00bdb0d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
