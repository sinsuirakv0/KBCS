# 00c3dfcc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00c3cfd8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3cfd8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0090.md#compare-16735aa47d222e72a55c5f3c6d063687)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00c3dfcc",
  "name": "FUN_00c3dfcc",
  "size": 244,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d09e18a45cafc59f2c94541184fbf7ec026038d64ba3038730ce753708a8e2b6",
  "source_text_sha256": "d09e18a45cafc59f2c94541184fbf7ec026038d64ba3038730ce753708a8e2b6",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00c3dfcc",
        "00c3e0bf"
      ]
    ],
    "bytes_sha256": "39c873edd447e764637d69c3d0368827541cf5c03225a75b240a233b30d21bc9",
    "instruction_count": 61,
    "instruction_bytes": 244,
    "body_bytes": 244,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c3b208](../00c3b/00c3b208.md)

## 呼び出し先

- [00c590c0](../00c59/00c590c0.md)
- [00c5b0c0](../00c5b/00c5b0c0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1686 bytes

~~~c

void FUN_00c3dfcc(long param_1,undefined8 *param_2,undefined8 *param_3,undefined8 *param_4,
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
  *(undefined ***)((long)puVar3 + lVar4 + 0x10) = &PTR_FUN_00c9a810;
  uVar1 = *param_7;
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
<a id="insn-00c3dfcc"></a> `00c3dfcc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00c3dfd0"></a> `00c3dfd0` | `fd 7b ba a9` | stp x29,x30,[sp, #-0x60]! | `FALL_THROUGH`
<a id="insn-00c3dfd4"></a> `00c3dfd4` | `fb 0b 00 f9` | str x27,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00c3dfd8"></a> `00c3dfd8` | `fa 67 02 a9` | stp x26,x25,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00c3dfdc"></a> `00c3dfdc` | `f8 5f 03 a9` | stp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00c3dfe0"></a> `00c3dfe0` | `f6 57 04 a9` | stp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00c3dfe4"></a> `00c3dfe4` | `f4 4f 05 a9` | stp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00c3dfe8"></a> `00c3dfe8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00c3dfec"></a> `00c3dfec` | `1b 98 49 f9` | ldr x27,[x0, #0x1330] | `FALL_THROUGH`
<a id="insn-00c3dff0"></a> `00c3dff0` | `f4 03 07 aa` | mov x20,x7 | `FALL_THROUGH`
<a id="insn-00c3dff4"></a> `00c3dff4` | `f6 03 06 aa` | mov x22,x6 | `FALL_THROUGH`
<a id="insn-00c3dff8"></a> `00c3dff8` | `f3 03 05 aa` | mov x19,x5 | `FALL_THROUGH`
<a id="insn-00c3dffc"></a> `00c3dffc` | `f7 03 04 aa` | mov x23,x4 | `FALL_THROUGH`
<a id="insn-00c3e000"></a> `00c3e000` | `f5 03 03 aa` | mov x21,x3 | `FALL_THROUGH`
<a id="insn-00c3e004"></a> `00c3e004` | `68 07 40 f9` | ldr x8,[x27, #0x8] | `FALL_THROUGH`
<a id="insn-00c3e008"></a> `00c3e008` | `f8 03 02 aa` | mov x24,x2 | `FALL_THROUGH`
<a id="insn-00c3e00c"></a> `00c3e00c` | `f9 03 01 aa` | mov x25,x1 | `FALL_THROUGH`
<a id="insn-00c3e010"></a> `00c3e010` | `09 81 3e d1` | sub x9,x8,#0xfa0 | `FALL_THROUGH`
<a id="insn-00c3e014"></a> `00c3e014` | `3f c5 3f b1` | cmn x9,#0xff1 | `FALL_THROUGH`
<a id="insn-00c3e018"></a> `00c3e018` | `28 01 00 54` | b.hi 0x00c3e03c | `CONDITIONAL_JUMP`
<a id="insn-00c3e01c"></a> `00c3e01c` | `fa 03 00 aa` | mov x26,x0 | `FALL_THROUGH`
<a id="insn-00c3e020"></a> `00c3e020` | `00 00 82 52` | mov w0,#0x1000 | `FALL_THROUGH`
<a id="insn-00c3e024"></a> `00c3e024` | `27 74 00 94` | bl 0x00c5b0c0 | `UNCONDITIONAL_CALL`
<a id="insn-00c3e028"></a> `00c3e028` | `a0 04 00 b4` | cbz x0,0x00c3e0bc | `CONDITIONAL_JUMP`
<a id="insn-00c3e02c"></a> `00c3e02c` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00c3e030"></a> `00c3e030` | `1b 7c 00 a9` | stp x27,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00c3e034"></a> `00c3e034` | `fb 03 00 aa` | mov x27,x0 | `FALL_THROUGH`
<a id="insn-00c3e038"></a> `00c3e038` | `40 9b 09 f9` | str x0,[x26, #0x1330] | `FALL_THROUGH`
<a id="insn-00c3e03c"></a> `00c3e03c` | `09 41 01 91` | add x9,x8,#0x50 | `FALL_THROUGH`
<a id="insn-00c3e040"></a> `00c3e040` | `60 03 08 8b` | add x0,x27,x8 | `FALL_THROUGH`
<a id="insn-00c3e044"></a> `00c3e044` | `e8 02 00 90` | adrp x8,0xc9a000 | `FALL_THROUGH`
<a id="insn-00c3e048"></a> `00c3e048` | `08 41 20 91` | add x8,x8,#0x810 | `FALL_THROUGH`
<a id="insn-00c3e04c"></a> `00c3e04c` | `69 07 00 f9` | str x9,[x27, #0x8] | `FALL_THROUGH`
<a id="insn-00c3e050"></a> `00c3e050` | `6c 02 80 52` | mov w12,#0x13 | `FALL_THROUGH`
<a id="insn-00c3e054"></a> `00c3e054` | `08 0c 01 f8` | str x8,[x0, #0x10]! | `FALL_THROUGH`
<a id="insn-00c3e058"></a> `00c3e058` | `08 90 40 78` | ldurh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00c3e05c"></a> `00c3e05c` | `cd 02 40 b9` | ldr w13,[x22] | `FALL_THROUGH`
<a id="insn-00c3e060"></a> `00c3e060` | `8e 02 40 39` | ldrb w14,[x20] | `FALL_THROUGH`
<a id="insn-00c3e064"></a> `00c3e064` | `0c 20 00 39` | strb w12,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00c3e068"></a> `00c3e068` | `29 03 40 f9` | ldr x9,[x25] | `FALL_THROUGH`
<a id="insn-00c3e06c"></a> `00c3e06c` | `0a 03 40 f9` | ldr x10,[x24] | `FALL_THROUGH`
<a id="insn-00c3e070"></a> `00c3e070` | `eb 02 40 f9` | ldr x11,[x23] | `FALL_THROUGH`
<a id="insn-00c3e074"></a> `00c3e074` | `08 0d 14 12` | and w8,w8,#0xf000 | `FALL_THROUGH`
<a id="insn-00c3e078"></a> `00c3e078` | `6c 02 40 f9` | ldr x12,[x19] | `FALL_THROUGH`
<a id="insn-00c3e07c"></a> `00c3e07c` | `a0 02 c0 3d` | ldr q0,[x21] | `FALL_THROUGH`
<a id="insn-00c3e080"></a> `00c3e080` | `08 01 18 32` | orr w8,w8,#0x100 | `FALL_THROUGH`
<a id="insn-00c3e084"></a> `00c3e084` | `09 28 01 a9` | stp x9,x10,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00c3e088"></a> `00c3e088` | `08 90 00 78` | sturh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00c3e08c"></a> `00c3e08c` | `00 08 80 3d` | str q0,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00c3e090"></a> `00c3e090` | `0b 30 03 a9` | stp x11,x12,[x0, #0x30] | `FALL_THROUGH`
<a id="insn-00c3e094"></a> `00c3e094` | `0d 40 00 b9` | str w13,[x0, #0x40] | `FALL_THROUGH`
<a id="insn-00c3e098"></a> `00c3e098` | `0e 10 01 39` | strb w14,[x0, #0x44] | `FALL_THROUGH`
<a id="insn-00c3e09c"></a> `00c3e09c` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00c3e0a0"></a> `00c3e0a0` | `fb 0b 40 f9` | ldr x27,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00c3e0a4"></a> `00c3e0a4` | `f6 57 44 a9` | ldp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00c3e0a8"></a> `00c3e0a8` | `f8 5f 43 a9` | ldp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00c3e0ac"></a> `00c3e0ac` | `fa 67 42 a9` | ldp x26,x25,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00c3e0b0"></a> `00c3e0b0` | `fd 7b c6 a8` | ldp x29,x30,[sp], #0x60 | `FALL_THROUGH`
<a id="insn-00c3e0b4"></a> `00c3e0b4` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00c3e0b8"></a> `00c3e0b8` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00c3e0bc"></a> `00c3e0bc` | `01 6c 00 94` | bl 0x00c590c0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00c3dfcc`](#insn-00c3dfcc) 範囲 `[['00c3dfcc', '00c3e01b']]`
  - `CONDITIONAL_JUMP` [`00c3e018`](#insn-00c3e018) → [`00c3e03c`](#insn-00c3e03c)
  - `FALL_THROUGH` [`00c3e018`](#insn-00c3e018) → [`00c3e01c`](#insn-00c3e01c)
- ブロック [`00c3e01c`](#insn-00c3e01c) 範囲 `[['00c3e01c', '00c3e02b']]`
  - `CONDITIONAL_JUMP` [`00c3e028`](#insn-00c3e028) → [`00c3e0bc`](#insn-00c3e0bc)
  - `FALL_THROUGH` [`00c3e028`](#insn-00c3e028) → [`00c3e02c`](#insn-00c3e02c)
- ブロック [`00c3e02c`](#insn-00c3e02c) 範囲 `[['00c3e02c', '00c3e03b']]`
  - `FALL_THROUGH` [`00c3e038`](#insn-00c3e038) → [`00c3e03c`](#insn-00c3e03c)
- ブロック [`00c3e03c`](#insn-00c3e03c) 範囲 `[['00c3e03c', '00c3e0bb']]`
- ブロック [`00c3e0bc`](#insn-00c3e0bc) 範囲 `[['00c3e0bc', '00c3e0bf']]`

## 命令位置別の参照

- [`00c3dfd0`](#insn-00c3dfd0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3dfd4`](#insn-00c3dfd4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3dfd8`](#insn-00c3dfd8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3dfdc`](#insn-00c3dfdc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3dfe0`](#insn-00c3dfe0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3dfe4`](#insn-00c3dfe4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3e018`](#insn-00c3e018) → [`00c3e03c`](#insn-00c3e03c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3e024`](#insn-00c3e024) → [`00c5b0c0`](../00c5b/00c5b0c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b0c0` · 推定シンボル `None` · 推定型 `None`
- [`00c3e028`](#insn-00c3e028) → [`00c3e0bc`](#insn-00c3e0bc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3e054`](#insn-00c3e054) → `00c9a810`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00c3e09c`](#insn-00c3e09c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3e0a0`](#insn-00c3e0a0) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3e0a4`](#insn-00c3e0a4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3e0a8`](#insn-00c3e0a8) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3e0ac`](#insn-00c3e0ac) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3e0b0`](#insn-00c3e0b0) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3e0bc`](#insn-00c3e0bc) → [`00c590c0`](../00c59/00c590c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c590c0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00c3dfd0`](#insn-00c3dfd0)

~~~json
{
  "source": "00c3dfd0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3dfd4`](#insn-00c3dfd4)

~~~json
{
  "source": "00c3dfd4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3dfd8`](#insn-00c3dfd8)

~~~json
{
  "source": "00c3dfd8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3dfdc`](#insn-00c3dfdc)

~~~json
{
  "source": "00c3dfdc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3dfe0`](#insn-00c3dfe0)

~~~json
{
  "source": "00c3dfe0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3dfe4`](#insn-00c3dfe4)

~~~json
{
  "source": "00c3dfe4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3e018`](#insn-00c3e018)

~~~json
{
  "source": "00c3e018",
  "target": "00c3e03c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3e024`](#insn-00c3e024)

~~~json
{
  "source": "00c3e024",
  "target": "00c5b0c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c3e028`](#insn-00c3e028)

~~~json
{
  "source": "00c3e028",
  "target": "00c3e0bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3e054`](#insn-00c3e054)

~~~json
{
  "source": "00c3e054",
  "target": "00c9a810",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9a810",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00c3e09c`](#insn-00c3e09c)

~~~json
{
  "source": "00c3e09c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3e0a0`](#insn-00c3e0a0)

~~~json
{
  "source": "00c3e0a0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3e0a4`](#insn-00c3e0a4)

~~~json
{
  "source": "00c3e0a4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3e0a8`](#insn-00c3e0a8)

~~~json
{
  "source": "00c3e0a8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3e0ac`](#insn-00c3e0ac)

~~~json
{
  "source": "00c3e0ac",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3e0b0`](#insn-00c3e0b0)

~~~json
{
  "source": "00c3e0b0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3e0bc`](#insn-00c3e0bc)

~~~json
{
  "source": "00c3e0bc",
  "target": "00c590c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
