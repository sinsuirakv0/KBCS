# 00bbfed0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bbfe8c`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbfe8c.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0078.md#compare-e551a570f71c504018f3c9bfaba22e07)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c3c918`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3c918.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0077.md#compare-b5f69acc7bcecb73d69f8689fbd647fb)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbfed0",
  "name": "FUN_00bbfed0",
  "size": 160,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3a076499b2e3d4d36f5d9d55310a49b54f375b48bff3064adac33b08af09b8bb",
  "source_text_sha256": "3a076499b2e3d4d36f5d9d55310a49b54f375b48bff3064adac33b08af09b8bb",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbfed0",
        "00bbff6f"
      ]
    ],
    "bytes_sha256": "e793c4e2707b3bfcd6dcbb8c377c0b77386235869ad20f327e2bf81167199cc5",
    "instruction_count": 40,
    "instruction_bytes": 160,
    "body_bytes": 160,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bbd308](../00bbd/00bbd308.md)

## 呼び出し先

- [00bdb1d0](../00bdb/00bdb1d0.md)
- [00bdd1d0](../00bdd/00bdd1d0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1393 bytes

~~~c

void FUN_00bbfed0(long param_1,undefined8 *param_2)

{
  undefined8 *puVar1;
  long lVar2;
  void *pvVar3;
  undefined8 uVar4;
  undefined8 uVar5;
  
  pvVar3 = *(void **)(param_1 + 0x1330);
                    /* try { // try from 00bbfeec to 00cbfef7 has its CatchHandler @ 00bc83f4 */
  lVar2 = *(long *)((long)pvVar3 + 8);
                    /* try { // try from 00bbfef8 to 00cbff03 has its CatchHandler @ 00bc83e4 */
  puVar1 = pvVar3;
  if (lVar2 - 0xfd0U < 0xfffffffffffff010) {
                    /* try { // try from 00bbff04 to 00cbff0f has its CatchHandler @ 00bc83d4 */
    puVar1 = malloc(0x1000);
    if (puVar1 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
      _ZSt9terminatev();
    }
    lVar2 = 0;
                    /* try { // try from 00bbff10 to 00cbff77 has its CatchHandler @ 00bbf570 */
    *puVar1 = pvVar3;
    puVar1[1] = 0;
    *(undefined8 **)(param_1 + 0x1330) = puVar1;
  }
  *(long *)((long)puVar1 + 8) = lVar2 + 0x20;
  *(undefined ***)((long)puVar1 + lVar2 + 0x10) = &PTR_FUN_00c198e8;
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
<a id="insn-00bbfed0"></a> `00bbfed0` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bbfed4"></a> `00bbfed4` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bbfed8"></a> `00bbfed8` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbfedc"></a> `00bbfedc` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbfee0"></a> `00bbfee0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bbfee4"></a> `00bbfee4` | `15 98 49 f9` | ldr x21,[x0, #0x1330] | `FALL_THROUGH`
<a id="insn-00bbfee8"></a> `00bbfee8` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bbfeec"></a> `00bbfeec` | `a8 06 40 f9` | ldr x8,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00bbfef0"></a> `00bbfef0` | `09 41 3f d1` | sub x9,x8,#0xfd0 | `FALL_THROUGH`
<a id="insn-00bbfef4"></a> `00bbfef4` | `3f c5 3f b1` | cmn x9,#0xff1 | `FALL_THROUGH`
<a id="insn-00bbfef8"></a> `00bbfef8` | `28 01 00 54` | b.hi 0x00bbff1c | `CONDITIONAL_JUMP`
<a id="insn-00bbfefc"></a> `00bbfefc` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bbff00"></a> `00bbff00` | `00 00 82 52` | mov w0,#0x1000 | `FALL_THROUGH`
<a id="insn-00bbff04"></a> `00bbff04` | `b3 74 00 94` | bl 0x00bdd1d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbff08"></a> `00bbff08` | `20 03 00 b4` | cbz x0,0x00bbff6c | `CONDITIONAL_JUMP`
<a id="insn-00bbff0c"></a> `00bbff0c` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbff10"></a> `00bbff10` | `15 7c 00 a9` | stp x21,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00bbff14"></a> `00bbff14` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bbff18"></a> `00bbff18` | `80 9a 09 f9` | str x0,[x20, #0x1330] | `FALL_THROUGH`
<a id="insn-00bbff1c"></a> `00bbff1c` | `09 81 00 91` | add x9,x8,#0x20 | `FALL_THROUGH`
<a id="insn-00bbff20"></a> `00bbff20` | `a0 02 08 8b` | add x0,x21,x8 | `FALL_THROUGH`
<a id="insn-00bbff24"></a> `00bbff24` | `c8 02 00 d0` | adrp x8,0xc19000 | `FALL_THROUGH`
<a id="insn-00bbff28"></a> `00bbff28` | `08 a1 23 91` | add x8,x8,#0x8e8 | `FALL_THROUGH`
<a id="insn-00bbff2c"></a> `00bbff2c` | `a9 06 00 f9` | str x9,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00bbff30"></a> `00bbff30` | `49 01 80 52` | mov w9,#0xa | `FALL_THROUGH`
<a id="insn-00bbff34"></a> `00bbff34` | `08 0c 01 f8` | str x8,[x0, #0x10]! | `FALL_THROUGH`
<a id="insn-00bbff38"></a> `00bbff38` | `08 90 40 78` | ldurh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00bbff3c"></a> `00bbff3c` | `09 20 00 39` | strb w9,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bbff40"></a> `00bbff40` | `09 a8 80 52` | mov w9,#0x540 | `FALL_THROUGH`
<a id="insn-00bbff44"></a> `00bbff44` | `08 0d 14 12` | and w8,w8,#0xf000 | `FALL_THROUGH`
<a id="insn-00bbff48"></a> `00bbff48` | `60 02 c0 3d` | ldr q0,[x19] | `FALL_THROUGH`
<a id="insn-00bbff4c"></a> `00bbff4c` | `08 01 09 2a` | orr w8,w8,w9 | `FALL_THROUGH`
<a id="insn-00bbff50"></a> `00bbff50` | `08 90 00 78` | sturh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00bbff54"></a> `00bbff54` | `00 04 80 3d` | str q0,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bbff58"></a> `00bbff58` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbff5c"></a> `00bbff5c` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbff60"></a> `00bbff60` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bbff64"></a> `00bbff64` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bbff68"></a> `00bbff68` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bbff6c"></a> `00bbff6c` | `99 6c 00 94` | bl 0x00bdb1d0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbfed0`](#insn-00bbfed0) 範囲 `[['00bbfed0', '00bbfeeb']]`
  - `FALL_THROUGH` [`00bbfee8`](#insn-00bbfee8) → [`00bbfeec`](#insn-00bbfeec)
- ブロック [`00bbfeec`](#insn-00bbfeec) 範囲 `[['00bbfeec', '00bbfef7']]`
  - `FALL_THROUGH` [`00bbfef4`](#insn-00bbfef4) → [`00bbfef8`](#insn-00bbfef8)
- ブロック [`00bbfef8`](#insn-00bbfef8) 範囲 `[['00bbfef8', '00bbfefb']]`
  - `CONDITIONAL_JUMP` [`00bbfef8`](#insn-00bbfef8) → [`00bbff1c`](#insn-00bbff1c)
  - `FALL_THROUGH` [`00bbfef8`](#insn-00bbfef8) → [`00bbfefc`](#insn-00bbfefc)
- ブロック [`00bbfefc`](#insn-00bbfefc) 範囲 `[['00bbfefc', '00bbff03']]`
  - `FALL_THROUGH` [`00bbff00`](#insn-00bbff00) → [`00bbff04`](#insn-00bbff04)
- ブロック [`00bbff04`](#insn-00bbff04) 範囲 `[['00bbff04', '00bbff0b']]`
  - `CONDITIONAL_JUMP` [`00bbff08`](#insn-00bbff08) → [`00bbff6c`](#insn-00bbff6c)
  - `FALL_THROUGH` [`00bbff08`](#insn-00bbff08) → [`00bbff0c`](#insn-00bbff0c)
- ブロック [`00bbff0c`](#insn-00bbff0c) 範囲 `[['00bbff0c', '00bbff0f']]`
  - `FALL_THROUGH` [`00bbff0c`](#insn-00bbff0c) → [`00bbff10`](#insn-00bbff10)
- ブロック [`00bbff10`](#insn-00bbff10) 範囲 `[['00bbff10', '00bbff1b']]`
  - `FALL_THROUGH` [`00bbff18`](#insn-00bbff18) → [`00bbff1c`](#insn-00bbff1c)
- ブロック [`00bbff1c`](#insn-00bbff1c) 範囲 `[['00bbff1c', '00bbff6b']]`
- ブロック [`00bbff6c`](#insn-00bbff6c) 範囲 `[['00bbff6c', '00bbff6f']]`

## 命令位置別の参照

- [`00bbfed4`](#insn-00bbfed4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfed8`](#insn-00bbfed8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfedc`](#insn-00bbfedc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfef8`](#insn-00bbfef8) → [`00bbff1c`](#insn-00bbff1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbff04`](#insn-00bbff04) → [`00bdd1d0`](../00bdd/00bdd1d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd1d0` · 推定シンボル `None` · 推定型 `None`
- [`00bbff08`](#insn-00bbff08) → [`00bbff6c`](#insn-00bbff6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbff34`](#insn-00bbff34) → `00c198e8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00bbff58`](#insn-00bbff58) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbff5c`](#insn-00bbff5c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbff60`](#insn-00bbff60) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbff6c`](#insn-00bbff6c) → [`00bdb1d0`](../00bdb/00bdb1d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb1d0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbfed4`](#insn-00bbfed4)

~~~json
{
  "source": "00bbfed4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfed8`](#insn-00bbfed8)

~~~json
{
  "source": "00bbfed8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfedc`](#insn-00bbfedc)

~~~json
{
  "source": "00bbfedc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfef8`](#insn-00bbfef8)

~~~json
{
  "source": "00bbfef8",
  "target": "00bbff1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbff04`](#insn-00bbff04)

~~~json
{
  "source": "00bbff04",
  "target": "00bdd1d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbff08`](#insn-00bbff08)

~~~json
{
  "source": "00bbff08",
  "target": "00bbff6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbff34`](#insn-00bbff34)

~~~json
{
  "source": "00bbff34",
  "target": "00c198e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c198e8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbff58`](#insn-00bbff58)

~~~json
{
  "source": "00bbff58",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbff5c`](#insn-00bbff5c)

~~~json
{
  "source": "00bbff5c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbff60`](#insn-00bbff60)

~~~json
{
  "source": "00bbff60",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbff6c`](#insn-00bbff6c)

~~~json
{
  "source": "00bbff6c",
  "target": "00bdb1d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
