# 00bcb2ec

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bcb224`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcb/00bcb224.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0079.md#compare-e68d0db7620a0c915e89cfaf6c8e7197)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bcb330`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcb330.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0079.md#compare-6299d918dcca427cdc7ceb11cd251c98)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcb2ec",
  "name": "FUN_00bcb2ec",
  "size": 224,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3cdd9387c10d8510b0fd24fb950efa8587843107828640257ce4f9ba6e5217c3",
  "source_text_sha256": "3cdd9387c10d8510b0fd24fb950efa8587843107828640257ce4f9ba6e5217c3",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcb2ec",
        "00bcb3cb"
      ]
    ],
    "bytes_sha256": "a1962aae7624c46fbb33c2b9877b9ab28262bdd3c7e818970034d7226e8034d8",
    "instruction_count": 56,
    "instruction_bytes": 224,
    "body_bytes": 224,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bc966c](../00bc9/00bc966c.md)

## 呼び出し先

- [00bdb180](../00bdb/00bdb180.md)
- [00bdd180](../00bdd/00bdd180.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2226 bytes

~~~c

void FUN_00bcb2ec(long param_1,undefined8 *param_2,undefined8 *param_3,undefined8 *param_4,
                 undefined8 *param_5,undefined8 *param_6)

{
  undefined8 *puVar1;
  long lVar2;
  undefined8 uVar3;
  undefined8 uVar4;
  void *pvVar5;
  undefined8 uVar6;
  undefined8 uVar7;
  undefined8 uVar8;
  undefined8 uVar9;
  undefined8 uVar10;
  undefined8 uVar11;
  
  pvVar5 = *(void **)(param_1 + 0x1330);
  lVar2 = *(long *)((long)pvVar5 + 8);
  puVar1 = pvVar5;
  if (lVar2 - 4000U < 0xfffffffffffff010) {
    puVar1 = malloc(0x1000);
    if (puVar1 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
                    /* catch() { ... } // from try @ 00bcb274 with catch @ 00bcb3c8
                       catch() { ... } // from try @ 00bcb3ac with catch @ 00bcb3c8 */
      _ZSt9terminatev();
    }
    lVar2 = 0;
    *puVar1 = pvVar5;
    puVar1[1] = 0;
    *(undefined8 **)(param_1 + 0x1330) = puVar1;
  }
  *(long *)((long)puVar1 + 8) = lVar2 + 0x50;
  uVar3 = *param_3;
  *(undefined ***)((long)puVar1 + lVar2 + 0x10) = &PTR_FUN_00c18868;
  *(undefined1 *)((long)puVar1 + lVar2 + 0x18) = 0x34;
  uVar4 = *param_5;
  uVar7 = param_2[1];
  uVar6 = *param_2;
  uVar9 = param_4[1];
  uVar8 = *param_4;
  uVar11 = param_6[1];
  uVar10 = *param_6;
  *(undefined8 *)((long)puVar1 + lVar2 + 0x30) = uVar3;
  *(undefined8 *)((long)puVar1 + lVar2 + 0x28) = uVar7;
  *(undefined8 *)((long)puVar1 + lVar2 + 0x20) = uVar6;
  *(ushort *)((long)puVar1 + lVar2 + 0x19) =
       *(ushort *)((long)puVar1 + lVar2 + 0x19) & 0xf000 | 0x540;
  *(undefined8 *)((long)puVar1 + lVar2 + 0x40) = uVar9;
  *(undefined8 *)((long)puVar1 + lVar2 + 0x38) = uVar8;
  *(undefined8 *)((long)puVar1 + lVar2 + 0x48) = uVar4;
  *(undefined8 *)((long)puVar1 + lVar2 + 0x58) = uVar11;
  *(undefined8 *)((long)puVar1 + lVar2 + 0x50) = uVar10;
                    /* try { // try from 00bcb3ac to 00ccb3b3 has its CatchHandler @ 00bcb3c8 */
                    /* catch() { ... } // from try @ 00bcb28c with catch @ 00bcb3b4
                       try { // try from 00bcb3b4 to 00ccb3f7 has its CatchHandler @ 00bcb174 */
                    /* catch() { ... } // from try @ 00bcb2b0 with catch @ 00bcb3c0 */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcb2ec"></a> `00bcb2ec` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bcb2f0"></a> `00bcb2f0` | `fd 7b bb a9` | stp x29,x30,[sp, #-0x50]! | `FALL_THROUGH`
<a id="insn-00bcb2f4"></a> `00bcb2f4` | `f9 0b 00 f9` | str x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcb2f8"></a> `00bcb2f8` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcb2fc"></a> `00bcb2fc` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bcb300"></a> `00bcb300` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bcb304"></a> `00bcb304` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bcb308"></a> `00bcb308` | `19 98 49 f9` | ldr x25,[x0, #0x1330] | `FALL_THROUGH`
<a id="insn-00bcb30c"></a> `00bcb30c` | `f3 03 05 aa` | mov x19,x5 | `FALL_THROUGH`
<a id="insn-00bcb310"></a> `00bcb310` | `f5 03 04 aa` | mov x21,x4 | `FALL_THROUGH`
<a id="insn-00bcb314"></a> `00bcb314` | `f4 03 03 aa` | mov x20,x3 | `FALL_THROUGH`
<a id="insn-00bcb318"></a> `00bcb318` | `f6 03 02 aa` | mov x22,x2 | `FALL_THROUGH`
<a id="insn-00bcb31c"></a> `00bcb31c` | `f7 03 01 aa` | mov x23,x1 | `FALL_THROUGH`
<a id="insn-00bcb320"></a> `00bcb320` | `28 07 40 f9` | ldr x8,[x25, #0x8] | `FALL_THROUGH`
<a id="insn-00bcb324"></a> `00bcb324` | `09 81 3e d1` | sub x9,x8,#0xfa0 | `FALL_THROUGH`
<a id="insn-00bcb328"></a> `00bcb328` | `3f c5 3f b1` | cmn x9,#0xff1 | `FALL_THROUGH`
<a id="insn-00bcb32c"></a> `00bcb32c` | `28 01 00 54` | b.hi 0x00bcb350 | `CONDITIONAL_JUMP`
<a id="insn-00bcb330"></a> `00bcb330` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-00bcb334"></a> `00bcb334` | `00 00 82 52` | mov w0,#0x1000 | `FALL_THROUGH`
<a id="insn-00bcb338"></a> `00bcb338` | `92 47 00 94` | bl 0x00bdd180 | `UNCONDITIONAL_CALL`
<a id="insn-00bcb33c"></a> `00bcb33c` | `60 04 00 b4` | cbz x0,0x00bcb3c8 | `CONDITIONAL_JUMP`
<a id="insn-00bcb340"></a> `00bcb340` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bcb344"></a> `00bcb344` | `19 7c 00 a9` | stp x25,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00bcb348"></a> `00bcb348` | `f9 03 00 aa` | mov x25,x0 | `FALL_THROUGH`
<a id="insn-00bcb34c"></a> `00bcb34c` | `00 9b 09 f9` | str x0,[x24, #0x1330] | `FALL_THROUGH`
<a id="insn-00bcb350"></a> `00bcb350` | `09 41 01 91` | add x9,x8,#0x50 | `FALL_THROUGH`
<a id="insn-00bcb354"></a> `00bcb354` | `20 03 08 8b` | add x0,x25,x8 | `FALL_THROUGH`
<a id="insn-00bcb358"></a> `00bcb358` | `68 02 00 b0` | adrp x8,0xc18000 | `FALL_THROUGH`
<a id="insn-00bcb35c"></a> `00bcb35c` | `08 a1 21 91` | add x8,x8,#0x868 | `FALL_THROUGH`
<a id="insn-00bcb360"></a> `00bcb360` | `29 07 00 f9` | str x9,[x25, #0x8] | `FALL_THROUGH`
<a id="insn-00bcb364"></a> `00bcb364` | `c9 02 40 f9` | ldr x9,[x22] | `FALL_THROUGH`
<a id="insn-00bcb368"></a> `00bcb368` | `08 0c 01 f8` | str x8,[x0, #0x10]! | `FALL_THROUGH`
<a id="insn-00bcb36c"></a> `00bcb36c` | `88 06 80 52` | mov w8,#0x34 | `FALL_THROUGH`
<a id="insn-00bcb370"></a> `00bcb370` | `08 20 00 39` | strb w8,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bcb374"></a> `00bcb374` | `08 90 40 78` | ldurh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00bcb378"></a> `00bcb378` | `aa 02 40 f9` | ldr x10,[x21] | `FALL_THROUGH`
<a id="insn-00bcb37c"></a> `00bcb37c` | `e0 02 c0 3d` | ldr q0,[x23] | `FALL_THROUGH`
<a id="insn-00bcb380"></a> `00bcb380` | `0b a8 80 52` | mov w11,#0x540 | `FALL_THROUGH`
<a id="insn-00bcb384"></a> `00bcb384` | `81 02 c0 3d` | ldr q1,[x20] | `FALL_THROUGH`
<a id="insn-00bcb388"></a> `00bcb388` | `08 0d 14 12` | and w8,w8,#0xf000 | `FALL_THROUGH`
<a id="insn-00bcb38c"></a> `00bcb38c` | `62 02 c0 3d` | ldr q2,[x19] | `FALL_THROUGH`
<a id="insn-00bcb390"></a> `00bcb390` | `09 10 00 f9` | str x9,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00bcb394"></a> `00bcb394` | `08 01 0b 2a` | orr w8,w8,w11 | `FALL_THROUGH`
<a id="insn-00bcb398"></a> `00bcb398` | `00 04 80 3d` | str q0,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bcb39c"></a> `00bcb39c` | `08 90 00 78` | sturh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00bcb3a0"></a> `00bcb3a0` | `01 80 82 3c` | stur q1,[x0, #0x28] | `FALL_THROUGH`
<a id="insn-00bcb3a4"></a> `00bcb3a4` | `0a 1c 00 f9` | str x10,[x0, #0x38] | `FALL_THROUGH`
<a id="insn-00bcb3a8"></a> `00bcb3a8` | `02 10 80 3d` | str q2,[x0, #0x40] | `FALL_THROUGH`
<a id="insn-00bcb3ac"></a> `00bcb3ac` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bcb3b0"></a> `00bcb3b0` | `f9 0b 40 f9` | ldr x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcb3b4"></a> `00bcb3b4` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bcb3b8"></a> `00bcb3b8` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcb3bc"></a> `00bcb3bc` | `fd 7b c5 a8` | ldp x29,x30,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00bcb3c0"></a> `00bcb3c0` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bcb3c4"></a> `00bcb3c4` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bcb3c8"></a> `00bcb3c8` | `6e 3f 00 94` | bl 0x00bdb180 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcb2ec`](#insn-00bcb2ec) 範囲 `[['00bcb2ec', '00bcb32f']]`
  - `CONDITIONAL_JUMP` [`00bcb32c`](#insn-00bcb32c) → [`00bcb350`](#insn-00bcb350)
  - `FALL_THROUGH` [`00bcb32c`](#insn-00bcb32c) → [`00bcb330`](#insn-00bcb330)
- ブロック [`00bcb330`](#insn-00bcb330) 範囲 `[['00bcb330', '00bcb33f']]`
  - `CONDITIONAL_JUMP` [`00bcb33c`](#insn-00bcb33c) → [`00bcb3c8`](#insn-00bcb3c8)
  - `FALL_THROUGH` [`00bcb33c`](#insn-00bcb33c) → [`00bcb340`](#insn-00bcb340)
- ブロック [`00bcb340`](#insn-00bcb340) 範囲 `[['00bcb340', '00bcb34f']]`
  - `FALL_THROUGH` [`00bcb34c`](#insn-00bcb34c) → [`00bcb350`](#insn-00bcb350)
- ブロック [`00bcb350`](#insn-00bcb350) 範囲 `[['00bcb350', '00bcb3ab']]`
  - `FALL_THROUGH` [`00bcb3a8`](#insn-00bcb3a8) → [`00bcb3ac`](#insn-00bcb3ac)
- ブロック [`00bcb3ac`](#insn-00bcb3ac) 範囲 `[['00bcb3ac', '00bcb3b3']]`
  - `FALL_THROUGH` [`00bcb3b0`](#insn-00bcb3b0) → [`00bcb3b4`](#insn-00bcb3b4)
- ブロック [`00bcb3b4`](#insn-00bcb3b4) 範囲 `[['00bcb3b4', '00bcb3bf']]`
  - `FALL_THROUGH` [`00bcb3bc`](#insn-00bcb3bc) → [`00bcb3c0`](#insn-00bcb3c0)
- ブロック [`00bcb3c0`](#insn-00bcb3c0) 範囲 `[['00bcb3c0', '00bcb3c7']]`
- ブロック [`00bcb3c8`](#insn-00bcb3c8) 範囲 `[['00bcb3c8', '00bcb3cb']]`

## 命令位置別の参照

- [`00bcb2f0`](#insn-00bcb2f0) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb2f4`](#insn-00bcb2f4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb2f8`](#insn-00bcb2f8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb2fc`](#insn-00bcb2fc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb300`](#insn-00bcb300) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb32c`](#insn-00bcb32c) → [`00bcb350`](#insn-00bcb350) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb338`](#insn-00bcb338) → [`00bdd180`](../00bdd/00bdd180.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd180` · 推定シンボル `None` · 推定型 `None`
- [`00bcb33c`](#insn-00bcb33c) → [`00bcb3c8`](#insn-00bcb3c8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb368`](#insn-00bcb368) → `00c18868`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00bcb3ac`](#insn-00bcb3ac) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb3b0`](#insn-00bcb3b0) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb3b4`](#insn-00bcb3b4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb3b8`](#insn-00bcb3b8) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb3bc`](#insn-00bcb3bc) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb3c8`](#insn-00bcb3c8) → [`00bdb180`](../00bdb/00bdb180.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb180` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcb2f0`](#insn-00bcb2f0)

~~~json
{
  "source": "00bcb2f0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb2f4`](#insn-00bcb2f4)

~~~json
{
  "source": "00bcb2f4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb2f8`](#insn-00bcb2f8)

~~~json
{
  "source": "00bcb2f8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb2fc`](#insn-00bcb2fc)

~~~json
{
  "source": "00bcb2fc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb300`](#insn-00bcb300)

~~~json
{
  "source": "00bcb300",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb32c`](#insn-00bcb32c)

~~~json
{
  "source": "00bcb32c",
  "target": "00bcb350",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb338`](#insn-00bcb338)

~~~json
{
  "source": "00bcb338",
  "target": "00bdd180",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcb33c`](#insn-00bcb33c)

~~~json
{
  "source": "00bcb33c",
  "target": "00bcb3c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb368`](#insn-00bcb368)

~~~json
{
  "source": "00bcb368",
  "target": "00c18868",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c18868",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bcb3ac`](#insn-00bcb3ac)

~~~json
{
  "source": "00bcb3ac",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb3b0`](#insn-00bcb3b0)

~~~json
{
  "source": "00bcb3b0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb3b4`](#insn-00bcb3b4)

~~~json
{
  "source": "00bcb3b4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb3b8`](#insn-00bcb3b8)

~~~json
{
  "source": "00bcb3b8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb3bc`](#insn-00bcb3bc)

~~~json
{
  "source": "00bcb3bc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb3c8`](#insn-00bcb3c8)

~~~json
{
  "source": "00bcb3c8",
  "target": "00bdb180",
  "target_space": "ram",
  "resolution": "function"
}
~~~
