# 00bbffc0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bc0088`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc0088.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0078.md#compare-4bbd5180f94a0c1f78e8e84752431530)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbffc0",
  "name": "FUN_00bbffc0",
  "size": 244,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "25350aaa2cb660a5cd9242d1e143e85b1c59033d8784838d18dec57a4fb775a7",
  "source_text_sha256": "25350aaa2cb660a5cd9242d1e143e85b1c59033d8784838d18dec57a4fb775a7",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbffc0",
        "00bc00b3"
      ]
    ],
    "bytes_sha256": "e06c2b8d4a7d27052da40b89895f24699c7f65dde6ad611632a84cdf05a34c6d",
    "instruction_count": 61,
    "instruction_bytes": 244,
    "body_bytes": 244,
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

## 疑似コード / UTF-8 1880 bytes

~~~c

void FUN_00bbffc0(long param_1,undefined8 *param_2,undefined8 *param_3,undefined8 *param_4,
                 undefined8 *param_5,undefined8 *param_6,undefined4 *param_7,undefined1 *param_8)

{
  undefined4 uVar1;
  undefined1 uVar2;
  undefined8 *puVar3;
  long lVar4;
  undefined8 uVar5;
  undefined8 uVar6;
  undefined8 uVar7;
  void *pvVar8;
  undefined8 uVar9;
  undefined8 uVar10;
  
                    /* try { // try from 00bbffd0 to 00cbffdb has its CatchHandler @ 00bc8b70 */
  pvVar8 = *(void **)(param_1 + 0x1330);
  lVar4 = *(long *)((long)pvVar8 + 8);
  puVar3 = pvVar8;
  if (lVar4 - 4000U < 0xfffffffffffff010) {
    puVar3 = malloc(0x1000);
    if (puVar3 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
      _ZSt9terminatev();
    }
    lVar4 = 0;
    *puVar3 = pvVar8;
    puVar3[1] = 0;
    *(undefined8 **)(param_1 + 0x1330) = puVar3;
  }
  *(long *)((long)puVar3 + 8) = lVar4 + 0x50;
  *(undefined ***)((long)puVar3 + lVar4 + 0x10) = &PTR_FUN_00c198c8;
  uVar1 = *param_7;
                    /* try { // try from 00bc0054 to 00cc005b has its CatchHandler @ 00bc8b44 */
  uVar2 = *param_8;
  *(undefined1 *)((long)puVar3 + lVar4 + 0x18) = 0x13;
  uVar5 = *param_3;
  uVar6 = *param_5;
  uVar7 = *param_6;
  uVar10 = param_4[1];
  uVar9 = *param_4;
  *(undefined8 *)((long)puVar3 + lVar4 + 0x20) = *param_2;
  *(undefined8 *)((long)puVar3 + lVar4 + 0x28) = uVar5;
  *(ushort *)((long)puVar3 + lVar4 + 0x19) =
       *(ushort *)((long)puVar3 + lVar4 + 0x19) & 0xf000 | 0x100;
  *(undefined8 *)((long)puVar3 + lVar4 + 0x38) = uVar10;
  *(undefined8 *)((long)puVar3 + lVar4 + 0x30) = uVar9;
  *(undefined8 *)((long)puVar3 + lVar4 + 0x40) = uVar6;
  *(undefined8 *)((long)puVar3 + lVar4 + 0x48) = uVar7;
  *(undefined4 *)((long)puVar3 + lVar4 + 0x50) = uVar1;
  *(undefined1 *)((long)puVar3 + lVar4 + 0x54) = uVar2;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbffc0"></a> `00bbffc0` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bbffc4"></a> `00bbffc4` | `fd 7b ba a9` | stp x29,x30,[sp, #-0x60]! | `FALL_THROUGH`
<a id="insn-00bbffc8"></a> `00bbffc8` | `fb 0b 00 f9` | str x27,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbffcc"></a> `00bbffcc` | `fa 67 02 a9` | stp x26,x25,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbffd0"></a> `00bbffd0` | `f8 5f 03 a9` | stp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bbffd4"></a> `00bbffd4` | `f6 57 04 a9` | stp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bbffd8"></a> `00bbffd8` | `f4 4f 05 a9` | stp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bbffdc"></a> `00bbffdc` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bbffe0"></a> `00bbffe0` | `1b 98 49 f9` | ldr x27,[x0, #0x1330] | `FALL_THROUGH`
<a id="insn-00bbffe4"></a> `00bbffe4` | `f4 03 07 aa` | mov x20,x7 | `FALL_THROUGH`
<a id="insn-00bbffe8"></a> `00bbffe8` | `f6 03 06 aa` | mov x22,x6 | `FALL_THROUGH`
<a id="insn-00bbffec"></a> `00bbffec` | `f3 03 05 aa` | mov x19,x5 | `FALL_THROUGH`
<a id="insn-00bbfff0"></a> `00bbfff0` | `f7 03 04 aa` | mov x23,x4 | `FALL_THROUGH`
<a id="insn-00bbfff4"></a> `00bbfff4` | `f5 03 03 aa` | mov x21,x3 | `FALL_THROUGH`
<a id="insn-00bbfff8"></a> `00bbfff8` | `68 07 40 f9` | ldr x8,[x27, #0x8] | `FALL_THROUGH`
<a id="insn-00bbfffc"></a> `00bbfffc` | `f8 03 02 aa` | mov x24,x2 | `FALL_THROUGH`
<a id="insn-00bc0000"></a> `00bc0000` | `f9 03 01 aa` | mov x25,x1 | `FALL_THROUGH`
<a id="insn-00bc0004"></a> `00bc0004` | `09 81 3e d1` | sub x9,x8,#0xfa0 | `FALL_THROUGH`
<a id="insn-00bc0008"></a> `00bc0008` | `3f c5 3f b1` | cmn x9,#0xff1 | `FALL_THROUGH`
<a id="insn-00bc000c"></a> `00bc000c` | `28 01 00 54` | b.hi 0x00bc0030 | `CONDITIONAL_JUMP`
<a id="insn-00bc0010"></a> `00bc0010` | `fa 03 00 aa` | mov x26,x0 | `FALL_THROUGH`
<a id="insn-00bc0014"></a> `00bc0014` | `00 00 82 52` | mov w0,#0x1000 | `FALL_THROUGH`
<a id="insn-00bc0018"></a> `00bc0018` | `2e 74 00 94` | bl 0x00bdd0d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bc001c"></a> `00bc001c` | `a0 04 00 b4` | cbz x0,0x00bc00b0 | `CONDITIONAL_JUMP`
<a id="insn-00bc0020"></a> `00bc0020` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bc0024"></a> `00bc0024` | `1b 7c 00 a9` | stp x27,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00bc0028"></a> `00bc0028` | `fb 03 00 aa` | mov x27,x0 | `FALL_THROUGH`
<a id="insn-00bc002c"></a> `00bc002c` | `40 9b 09 f9` | str x0,[x26, #0x1330] | `FALL_THROUGH`
<a id="insn-00bc0030"></a> `00bc0030` | `09 41 01 91` | add x9,x8,#0x50 | `FALL_THROUGH`
<a id="insn-00bc0034"></a> `00bc0034` | `60 03 08 8b` | add x0,x27,x8 | `FALL_THROUGH`
<a id="insn-00bc0038"></a> `00bc0038` | `c8 02 00 b0` | adrp x8,0xc19000 | `FALL_THROUGH`
<a id="insn-00bc003c"></a> `00bc003c` | `08 21 23 91` | add x8,x8,#0x8c8 | `FALL_THROUGH`
<a id="insn-00bc0040"></a> `00bc0040` | `69 07 00 f9` | str x9,[x27, #0x8] | `FALL_THROUGH`
<a id="insn-00bc0044"></a> `00bc0044` | `6c 02 80 52` | mov w12,#0x13 | `FALL_THROUGH`
<a id="insn-00bc0048"></a> `00bc0048` | `08 0c 01 f8` | str x8,[x0, #0x10]! | `FALL_THROUGH`
<a id="insn-00bc004c"></a> `00bc004c` | `08 90 40 78` | ldurh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00bc0050"></a> `00bc0050` | `cd 02 40 b9` | ldr w13,[x22] | `FALL_THROUGH`
<a id="insn-00bc0054"></a> `00bc0054` | `8e 02 40 39` | ldrb w14,[x20] | `FALL_THROUGH`
<a id="insn-00bc0058"></a> `00bc0058` | `0c 20 00 39` | strb w12,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bc005c"></a> `00bc005c` | `29 03 40 f9` | ldr x9,[x25] | `FALL_THROUGH`
<a id="insn-00bc0060"></a> `00bc0060` | `0a 03 40 f9` | ldr x10,[x24] | `FALL_THROUGH`
<a id="insn-00bc0064"></a> `00bc0064` | `eb 02 40 f9` | ldr x11,[x23] | `FALL_THROUGH`
<a id="insn-00bc0068"></a> `00bc0068` | `08 0d 14 12` | and w8,w8,#0xf000 | `FALL_THROUGH`
<a id="insn-00bc006c"></a> `00bc006c` | `6c 02 40 f9` | ldr x12,[x19] | `FALL_THROUGH`
<a id="insn-00bc0070"></a> `00bc0070` | `a0 02 c0 3d` | ldr q0,[x21] | `FALL_THROUGH`
<a id="insn-00bc0074"></a> `00bc0074` | `08 01 18 32` | orr w8,w8,#0x100 | `FALL_THROUGH`
<a id="insn-00bc0078"></a> `00bc0078` | `09 28 01 a9` | stp x9,x10,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bc007c"></a> `00bc007c` | `08 90 00 78` | sturh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00bc0080"></a> `00bc0080` | `00 08 80 3d` | str q0,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00bc0084"></a> `00bc0084` | `0b 30 03 a9` | stp x11,x12,[x0, #0x30] | `FALL_THROUGH`
<a id="insn-00bc0088"></a> `00bc0088` | `0d 40 00 b9` | str w13,[x0, #0x40] | `FALL_THROUGH`
<a id="insn-00bc008c"></a> `00bc008c` | `0e 10 01 39` | strb w14,[x0, #0x44] | `FALL_THROUGH`
<a id="insn-00bc0090"></a> `00bc0090` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bc0094"></a> `00bc0094` | `fb 0b 40 f9` | ldr x27,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bc0098"></a> `00bc0098` | `f6 57 44 a9` | ldp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bc009c"></a> `00bc009c` | `f8 5f 43 a9` | ldp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bc00a0"></a> `00bc00a0` | `fa 67 42 a9` | ldp x26,x25,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bc00a4"></a> `00bc00a4` | `fd 7b c6 a8` | ldp x29,x30,[sp], #0x60 | `FALL_THROUGH`
<a id="insn-00bc00a8"></a> `00bc00a8` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bc00ac"></a> `00bc00ac` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bc00b0"></a> `00bc00b0` | `08 6c 00 94` | bl 0x00bdb0d0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbffc0`](#insn-00bbffc0) 範囲 `[['00bbffc0', '00bbffcf']]`
  - `FALL_THROUGH` [`00bbffcc`](#insn-00bbffcc) → [`00bbffd0`](#insn-00bbffd0)
- ブロック [`00bbffd0`](#insn-00bbffd0) 範囲 `[['00bbffd0', '00bc000f']]`
  - `CONDITIONAL_JUMP` [`00bc000c`](#insn-00bc000c) → [`00bc0030`](#insn-00bc0030)
  - `FALL_THROUGH` [`00bc000c`](#insn-00bc000c) → [`00bc0010`](#insn-00bc0010)
- ブロック [`00bc0010`](#insn-00bc0010) 範囲 `[['00bc0010', '00bc001f']]`
  - `CONDITIONAL_JUMP` [`00bc001c`](#insn-00bc001c) → [`00bc00b0`](#insn-00bc00b0)
  - `FALL_THROUGH` [`00bc001c`](#insn-00bc001c) → [`00bc0020`](#insn-00bc0020)
- ブロック [`00bc0020`](#insn-00bc0020) 範囲 `[['00bc0020', '00bc002f']]`
  - `FALL_THROUGH` [`00bc002c`](#insn-00bc002c) → [`00bc0030`](#insn-00bc0030)
- ブロック [`00bc0030`](#insn-00bc0030) 範囲 `[['00bc0030', '00bc0053']]`
  - `FALL_THROUGH` [`00bc0050`](#insn-00bc0050) → [`00bc0054`](#insn-00bc0054)
- ブロック [`00bc0054`](#insn-00bc0054) 範囲 `[['00bc0054', '00bc00af']]`
- ブロック [`00bc00b0`](#insn-00bc00b0) 範囲 `[['00bc00b0', '00bc00b3']]`

## 命令位置別の参照

- [`00bbffc4`](#insn-00bbffc4) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbffc8`](#insn-00bbffc8) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbffcc`](#insn-00bbffcc) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbffd0`](#insn-00bbffd0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbffd4`](#insn-00bbffd4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbffd8`](#insn-00bbffd8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc000c`](#insn-00bc000c) → [`00bc0030`](#insn-00bc0030) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc0018`](#insn-00bc0018) → [`00bdd0d0`](../00bdd/00bdd0d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd0d0` · 推定シンボル `None` · 推定型 `None`
- [`00bc001c`](#insn-00bc001c) → [`00bc00b0`](#insn-00bc00b0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc0048`](#insn-00bc0048) → `00c198c8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00bc0090`](#insn-00bc0090) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc0094`](#insn-00bc0094) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc0098`](#insn-00bc0098) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc009c`](#insn-00bc009c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc00a0`](#insn-00bc00a0) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc00a4`](#insn-00bc00a4) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc00b0`](#insn-00bc00b0) → [`00bdb0d0`](../00bdb/00bdb0d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb0d0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbffc4`](#insn-00bbffc4)

~~~json
{
  "source": "00bbffc4",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbffc8`](#insn-00bbffc8)

~~~json
{
  "source": "00bbffc8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbffcc`](#insn-00bbffcc)

~~~json
{
  "source": "00bbffcc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbffd0`](#insn-00bbffd0)

~~~json
{
  "source": "00bbffd0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbffd4`](#insn-00bbffd4)

~~~json
{
  "source": "00bbffd4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbffd8`](#insn-00bbffd8)

~~~json
{
  "source": "00bbffd8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc000c`](#insn-00bc000c)

~~~json
{
  "source": "00bc000c",
  "target": "00bc0030",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc0018`](#insn-00bc0018)

~~~json
{
  "source": "00bc0018",
  "target": "00bdd0d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc001c`](#insn-00bc001c)

~~~json
{
  "source": "00bc001c",
  "target": "00bc00b0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc0048`](#insn-00bc0048)

~~~json
{
  "source": "00bc0048",
  "target": "00c198c8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c198c8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bc0090`](#insn-00bc0090)

~~~json
{
  "source": "00bc0090",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc0094`](#insn-00bc0094)

~~~json
{
  "source": "00bc0094",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc0098`](#insn-00bc0098)

~~~json
{
  "source": "00bc0098",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc009c`](#insn-00bc009c)

~~~json
{
  "source": "00bc009c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc00a0`](#insn-00bc00a0)

~~~json
{
  "source": "00bc00a0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc00a4`](#insn-00bc00a4)

~~~json
{
  "source": "00bc00a4",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc00b0`](#insn-00bc00b0)

~~~json
{
  "source": "00bc00b0",
  "target": "00bdb0d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
