# 00bcc6ec

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bcc6a8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcc/00bcc6a8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0079.md#compare-164d5ad5c89d3b6309a4f3f49fae2e43)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c49134`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c49/00c49134.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0078.md#compare-ccc6f8d97e3803b05b1a5d2430e107ff)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcc6ec",
  "name": "FUN_00bcc6ec",
  "size": 160,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e70532fc187c86329377f399f5407916192d6d58ba7b2b5f77a3a3878993ae03",
  "source_text_sha256": "e70532fc187c86329377f399f5407916192d6d58ba7b2b5f77a3a3878993ae03",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcc6ec",
        "00bcc78b"
      ]
    ],
    "bytes_sha256": "b571b1f5a03c42d91defc740e89c33dec2336e126d260d327cb925a54cce1823",
    "instruction_count": 40,
    "instruction_bytes": 160,
    "body_bytes": 160,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bc5260](../00bc5/00bc5260.md)

## 呼び出し先

- [00bdb1d0](../00bdb/00bdb1d0.md)
- [00bdd1d0](../00bdd/00bdd1d0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1201 bytes

~~~c

void FUN_00bcc6ec(long param_1,undefined8 *param_2)

{
  undefined8 *puVar1;
  long lVar2;
  void *pvVar3;
  undefined8 uVar4;
  undefined8 uVar5;
  
                    /* try { // try from 00bcc6f8 to 00ccc777 has its CatchHandler @ 00bcc598 */
  pvVar3 = *(void **)(param_1 + 0x1330);
  lVar2 = *(long *)((long)pvVar3 + 8);
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
  *(undefined ***)((long)puVar1 + lVar2 + 0x10) = &PTR_FUN_00c18a08;
  *(undefined1 *)((long)puVar1 + lVar2 + 0x18) = 0x43;
  uVar5 = param_2[1];
  uVar4 = *param_2;
  *(ushort *)((long)puVar1 + lVar2 + 0x19) =
       *(ushort *)((long)puVar1 + lVar2 + 0x19) & 0xf000 | 0x540;
  *(undefined8 *)((long)puVar1 + lVar2 + 0x28) = uVar5;
  *(undefined8 *)((long)puVar1 + lVar2 + 0x20) = uVar4;
                    /* try { // try from 00bcc778 to 00ccc77f has its CatchHandler @ 00bcceec */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcc6ec"></a> `00bcc6ec` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bcc6f0"></a> `00bcc6f0` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bcc6f4"></a> `00bcc6f4` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcc6f8"></a> `00bcc6f8` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcc6fc"></a> `00bcc6fc` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bcc700"></a> `00bcc700` | `15 98 49 f9` | ldr x21,[x0, #0x1330] | `FALL_THROUGH`
<a id="insn-00bcc704"></a> `00bcc704` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bcc708"></a> `00bcc708` | `a8 06 40 f9` | ldr x8,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00bcc70c"></a> `00bcc70c` | `09 41 3f d1` | sub x9,x8,#0xfd0 | `FALL_THROUGH`
<a id="insn-00bcc710"></a> `00bcc710` | `3f c5 3f b1` | cmn x9,#0xff1 | `FALL_THROUGH`
<a id="insn-00bcc714"></a> `00bcc714` | `28 01 00 54` | b.hi 0x00bcc738 | `CONDITIONAL_JUMP`
<a id="insn-00bcc718"></a> `00bcc718` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bcc71c"></a> `00bcc71c` | `00 00 82 52` | mov w0,#0x1000 | `FALL_THROUGH`
<a id="insn-00bcc720"></a> `00bcc720` | `ac 42 00 94` | bl 0x00bdd1d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcc724"></a> `00bcc724` | `20 03 00 b4` | cbz x0,0x00bcc788 | `CONDITIONAL_JUMP`
<a id="insn-00bcc728"></a> `00bcc728` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bcc72c"></a> `00bcc72c` | `15 7c 00 a9` | stp x21,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00bcc730"></a> `00bcc730` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bcc734"></a> `00bcc734` | `80 9a 09 f9` | str x0,[x20, #0x1330] | `FALL_THROUGH`
<a id="insn-00bcc738"></a> `00bcc738` | `09 81 00 91` | add x9,x8,#0x20 | `FALL_THROUGH`
<a id="insn-00bcc73c"></a> `00bcc73c` | `a0 02 08 8b` | add x0,x21,x8 | `FALL_THROUGH`
<a id="insn-00bcc740"></a> `00bcc740` | `68 02 00 90` | adrp x8,0xc18000 | `FALL_THROUGH`
<a id="insn-00bcc744"></a> `00bcc744` | `08 21 28 91` | add x8,x8,#0xa08 | `FALL_THROUGH`
<a id="insn-00bcc748"></a> `00bcc748` | `a9 06 00 f9` | str x9,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00bcc74c"></a> `00bcc74c` | `69 08 80 52` | mov w9,#0x43 | `FALL_THROUGH`
<a id="insn-00bcc750"></a> `00bcc750` | `08 0c 01 f8` | str x8,[x0, #0x10]! | `FALL_THROUGH`
<a id="insn-00bcc754"></a> `00bcc754` | `08 90 40 78` | ldurh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00bcc758"></a> `00bcc758` | `09 20 00 39` | strb w9,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bcc75c"></a> `00bcc75c` | `09 a8 80 52` | mov w9,#0x540 | `FALL_THROUGH`
<a id="insn-00bcc760"></a> `00bcc760` | `08 0d 14 12` | and w8,w8,#0xf000 | `FALL_THROUGH`
<a id="insn-00bcc764"></a> `00bcc764` | `60 02 c0 3d` | ldr q0,[x19] | `FALL_THROUGH`
<a id="insn-00bcc768"></a> `00bcc768` | `08 01 09 2a` | orr w8,w8,w9 | `FALL_THROUGH`
<a id="insn-00bcc76c"></a> `00bcc76c` | `08 90 00 78` | sturh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00bcc770"></a> `00bcc770` | `00 04 80 3d` | str q0,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bcc774"></a> `00bcc774` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcc778"></a> `00bcc778` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcc77c"></a> `00bcc77c` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bcc780"></a> `00bcc780` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bcc784"></a> `00bcc784` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bcc788"></a> `00bcc788` | `92 3a 00 94` | bl 0x00bdb1d0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcc6ec`](#insn-00bcc6ec) 範囲 `[['00bcc6ec', '00bcc6f7']]`
  - `FALL_THROUGH` [`00bcc6f4`](#insn-00bcc6f4) → [`00bcc6f8`](#insn-00bcc6f8)
- ブロック [`00bcc6f8`](#insn-00bcc6f8) 範囲 `[['00bcc6f8', '00bcc717']]`
  - `CONDITIONAL_JUMP` [`00bcc714`](#insn-00bcc714) → [`00bcc738`](#insn-00bcc738)
  - `FALL_THROUGH` [`00bcc714`](#insn-00bcc714) → [`00bcc718`](#insn-00bcc718)
- ブロック [`00bcc718`](#insn-00bcc718) 範囲 `[['00bcc718', '00bcc727']]`
  - `CONDITIONAL_JUMP` [`00bcc724`](#insn-00bcc724) → [`00bcc788`](#insn-00bcc788)
  - `FALL_THROUGH` [`00bcc724`](#insn-00bcc724) → [`00bcc728`](#insn-00bcc728)
- ブロック [`00bcc728`](#insn-00bcc728) 範囲 `[['00bcc728', '00bcc737']]`
  - `FALL_THROUGH` [`00bcc734`](#insn-00bcc734) → [`00bcc738`](#insn-00bcc738)
- ブロック [`00bcc738`](#insn-00bcc738) 範囲 `[['00bcc738', '00bcc777']]`
  - `FALL_THROUGH` [`00bcc774`](#insn-00bcc774) → [`00bcc778`](#insn-00bcc778)
- ブロック [`00bcc778`](#insn-00bcc778) 範囲 `[['00bcc778', '00bcc787']]`
- ブロック [`00bcc788`](#insn-00bcc788) 範囲 `[['00bcc788', '00bcc78b']]`

## 命令位置別の参照

- [`00bcc6f0`](#insn-00bcc6f0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcc6f4`](#insn-00bcc6f4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcc6f8`](#insn-00bcc6f8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcc714`](#insn-00bcc714) → [`00bcc738`](#insn-00bcc738) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcc720`](#insn-00bcc720) → [`00bdd1d0`](../00bdd/00bdd1d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd1d0` · 推定シンボル `None` · 推定型 `None`
- [`00bcc724`](#insn-00bcc724) → [`00bcc788`](#insn-00bcc788) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcc750`](#insn-00bcc750) → `00c18a08`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00bcc774`](#insn-00bcc774) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcc778`](#insn-00bcc778) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcc77c`](#insn-00bcc77c) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcc788`](#insn-00bcc788) → [`00bdb1d0`](../00bdb/00bdb1d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb1d0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcc6f0`](#insn-00bcc6f0)

~~~json
{
  "source": "00bcc6f0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcc6f4`](#insn-00bcc6f4)

~~~json
{
  "source": "00bcc6f4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcc6f8`](#insn-00bcc6f8)

~~~json
{
  "source": "00bcc6f8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcc714`](#insn-00bcc714)

~~~json
{
  "source": "00bcc714",
  "target": "00bcc738",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcc720`](#insn-00bcc720)

~~~json
{
  "source": "00bcc720",
  "target": "00bdd1d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcc724`](#insn-00bcc724)

~~~json
{
  "source": "00bcc724",
  "target": "00bcc788",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcc750`](#insn-00bcc750)

~~~json
{
  "source": "00bcc750",
  "target": "00c18a08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c18a08",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bcc774`](#insn-00bcc774)

~~~json
{
  "source": "00bcc774",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcc778`](#insn-00bcc778)

~~~json
{
  "source": "00bcc778",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcc77c`](#insn-00bcc77c)

~~~json
{
  "source": "00bcc77c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcc788`](#insn-00bcc788)

~~~json
{
  "source": "00bcc788",
  "target": "00bdb1d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
