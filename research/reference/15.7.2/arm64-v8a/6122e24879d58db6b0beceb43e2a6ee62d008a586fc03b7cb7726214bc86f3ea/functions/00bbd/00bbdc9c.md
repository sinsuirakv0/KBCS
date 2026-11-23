# 00bbdc9c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bbdd64`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbdd64.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0078.md#compare-f76374fa903a446d9d21da74a7270880)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbdc9c",
  "name": "FUN_00bbdc9c",
  "size": 180,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "001132af4c1b3497b7128052689e0c4e0d4e4c1e3e7241f0383f529215293338",
  "source_text_sha256": "001132af4c1b3497b7128052689e0c4e0d4e4c1e3e7241f0383f529215293338",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbdc9c",
        "00bbdd4f"
      ]
    ],
    "bytes_sha256": "cfac76fccdca0f0b9de66d7508a63386ceeceadb0b81aebf7acb94ab458159a8",
    "instruction_count": 45,
    "instruction_bytes": 180,
    "body_bytes": 180,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bbcb04](../00bbc/00bbcb04.md)
- [00bbd1fc](../00bbd/00bbd1fc.md)

## 呼び出し先

- [00bdb090](../00bdb/00bdb090.md)
- [00bdb0d0](../00bdb/00bdb0d0.md)
- [00bdd0d0](../00bdd/00bdd0d0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1611 bytes

~~~c

undefined8 * FUN_00bbdc9c(long param_1,char *param_2,undefined8 *param_3)

{
  undefined8 *puVar1;
  size_t sVar2;
  long lVar3;
  undefined8 uVar4;
  undefined8 *puVar5;
  void *pvVar6;
  
                    /* try { // try from 00bbdcac to 00cbdcb3 has its CatchHandler @ 00bbe08c */
  pvVar6 = *(void **)(param_1 + 0x1330);
                    /* try { // try from 00bbdcb4 to 00cbdcbb has its CatchHandler @ 00bbdf20 */
  lVar3 = *(long *)((long)pvVar6 + 8);
  puVar1 = pvVar6;
  if (lVar3 - 0xfc0U < 0xfffffffffffff010) {
    puVar1 = malloc(0x1000);
    if (puVar1 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
      _ZSt9terminatev();
    }
    lVar3 = 0;
    *puVar1 = pvVar6;
    puVar1[1] = 0;
    *(undefined8 **)(param_1 + 0x1330) = puVar1;
  }
                    /* try { // try from 00bbdcf8 to 00cbdd03 has its CatchHandler @ 00bbdf1c */
  *(long *)((long)puVar1 + 8) = lVar3 + 0x30;
  sVar2 = strlen(param_2);
                    /* try { // try from 00bbdd04 to 00cbdd13 has its CatchHandler @ 00bbdf08 */
  uVar4 = *param_3;
  puVar5 = (undefined8 *)((long)puVar1 + lVar3 + 0x10);
  *puVar5 = &PTR_FUN_00c176a8;
                    /* try { // try from 00bbdd14 to 00cbdd27 has its CatchHandler @ 00bbdef0 */
  *(char **)((long)puVar1 + lVar3 + 0x20) = param_2;
  *(size_t *)((long)puVar1 + lVar3 + 0x28) = sVar2;
  *(undefined1 *)((long)puVar1 + lVar3 + 0x18) = 0x15;
  *(ushort *)((long)puVar1 + lVar3 + 0x19) =
       *(ushort *)((long)puVar1 + lVar3 + 0x19) & 0xf000 | 0x540;
  *(undefined8 *)((long)puVar1 + lVar3 + 0x30) = uVar4;
  return puVar5;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbdc9c"></a> `00bbdc9c` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bbdca0"></a> `00bbdca0` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bbdca4"></a> `00bbdca4` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbdca8"></a> `00bbdca8` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbdcac"></a> `00bbdcac` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bbdcb0"></a> `00bbdcb0` | `16 98 49 f9` | ldr x22,[x0, #0x1330] | `FALL_THROUGH`
<a id="insn-00bbdcb4"></a> `00bbdcb4` | `f3 03 02 aa` | mov x19,x2 | `FALL_THROUGH`
<a id="insn-00bbdcb8"></a> `00bbdcb8` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00bbdcbc"></a> `00bbdcbc` | `c8 06 40 f9` | ldr x8,[x22, #0x8] | `FALL_THROUGH`
<a id="insn-00bbdcc0"></a> `00bbdcc0` | `09 01 3f d1` | sub x9,x8,#0xfc0 | `FALL_THROUGH`
<a id="insn-00bbdcc4"></a> `00bbdcc4` | `3f c5 3f b1` | cmn x9,#0xff1 | `FALL_THROUGH`
<a id="insn-00bbdcc8"></a> `00bbdcc8` | `28 01 00 54` | b.hi 0x00bbdcec | `CONDITIONAL_JUMP`
<a id="insn-00bbdccc"></a> `00bbdccc` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bbdcd0"></a> `00bbdcd0` | `00 00 82 52` | mov w0,#0x1000 | `FALL_THROUGH`
<a id="insn-00bbdcd4"></a> `00bbdcd4` | `ff 7c 00 94` | bl 0x00bdd0d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbdcd8"></a> `00bbdcd8` | `a0 03 00 b4` | cbz x0,0x00bbdd4c | `CONDITIONAL_JUMP`
<a id="insn-00bbdcdc"></a> `00bbdcdc` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbdce0"></a> `00bbdce0` | `16 7c 00 a9` | stp x22,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00bbdce4"></a> `00bbdce4` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bbdce8"></a> `00bbdce8` | `a0 9a 09 f9` | str x0,[x21, #0x1330] | `FALL_THROUGH`
<a id="insn-00bbdcec"></a> `00bbdcec` | `09 c1 00 91` | add x9,x8,#0x30 | `FALL_THROUGH`
<a id="insn-00bbdcf0"></a> `00bbdcf0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbdcf4"></a> `00bbdcf4` | `d5 02 08 8b` | add x21,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbdcf8"></a> `00bbdcf8` | `c9 06 00 f9` | str x9,[x22, #0x8] | `FALL_THROUGH`
<a id="insn-00bbdcfc"></a> `00bbdcfc` | `e5 74 00 94` | bl 0x00bdb090 | `UNCONDITIONAL_CALL`
<a id="insn-00bbdd00"></a> `00bbdd00` | `c8 02 00 d0` | adrp x8,0xc17000 | `FALL_THROUGH`
<a id="insn-00bbdd04"></a> `00bbdd04` | `08 a1 1a 91` | add x8,x8,#0x6a8 | `FALL_THROUGH`
<a id="insn-00bbdd08"></a> `00bbdd08` | `6a 02 40 f9` | ldr x10,[x19] | `FALL_THROUGH`
<a id="insn-00bbdd0c"></a> `00bbdd0c` | `a8 0e 01 f8` | str x8,[x21, #0x10]! | `FALL_THROUGH`
<a id="insn-00bbdd10"></a> `00bbdd10` | `a9 92 40 78` | ldurh w9,[x21, #0x9] | `FALL_THROUGH`
<a id="insn-00bbdd14"></a> `00bbdd14` | `a8 02 80 52` | mov w8,#0x15 | `FALL_THROUGH`
<a id="insn-00bbdd18"></a> `00bbdd18` | `b4 02 01 a9` | stp x20,x0,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-00bbdd1c"></a> `00bbdd1c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bbdd20"></a> `00bbdd20` | `a8 22 00 39` | strb w8,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00bbdd24"></a> `00bbdd24` | `28 0d 14 12` | and w8,w9,#0xf000 | `FALL_THROUGH`
<a id="insn-00bbdd28"></a> `00bbdd28` | `09 a8 80 52` | mov w9,#0x540 | `FALL_THROUGH`
<a id="insn-00bbdd2c"></a> `00bbdd2c` | `08 01 09 2a` | orr w8,w8,w9 | `FALL_THROUGH`
<a id="insn-00bbdd30"></a> `00bbdd30` | `a8 92 00 78` | sturh w8,[x21, #0x9] | `FALL_THROUGH`
<a id="insn-00bbdd34"></a> `00bbdd34` | `aa 12 00 f9` | str x10,[x21, #0x20] | `FALL_THROUGH`
<a id="insn-00bbdd38"></a> `00bbdd38` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbdd3c"></a> `00bbdd3c` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbdd40"></a> `00bbdd40` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bbdd44"></a> `00bbdd44` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bbdd48"></a> `00bbdd48` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bbdd4c"></a> `00bbdd4c` | `e1 74 00 94` | bl 0x00bdb0d0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbdc9c`](#insn-00bbdc9c) 範囲 `[['00bbdc9c', '00bbdcab']]`
  - `FALL_THROUGH` [`00bbdca8`](#insn-00bbdca8) → [`00bbdcac`](#insn-00bbdcac)
- ブロック [`00bbdcac`](#insn-00bbdcac) 範囲 `[['00bbdcac', '00bbdcb3']]`
  - `FALL_THROUGH` [`00bbdcb0`](#insn-00bbdcb0) → [`00bbdcb4`](#insn-00bbdcb4)
- ブロック [`00bbdcb4`](#insn-00bbdcb4) 範囲 `[['00bbdcb4', '00bbdccb']]`
  - `CONDITIONAL_JUMP` [`00bbdcc8`](#insn-00bbdcc8) → [`00bbdcec`](#insn-00bbdcec)
  - `FALL_THROUGH` [`00bbdcc8`](#insn-00bbdcc8) → [`00bbdccc`](#insn-00bbdccc)
- ブロック [`00bbdccc`](#insn-00bbdccc) 範囲 `[['00bbdccc', '00bbdcdb']]`
  - `CONDITIONAL_JUMP` [`00bbdcd8`](#insn-00bbdcd8) → [`00bbdd4c`](#insn-00bbdd4c)
  - `FALL_THROUGH` [`00bbdcd8`](#insn-00bbdcd8) → [`00bbdcdc`](#insn-00bbdcdc)
- ブロック [`00bbdcdc`](#insn-00bbdcdc) 範囲 `[['00bbdcdc', '00bbdceb']]`
  - `FALL_THROUGH` [`00bbdce8`](#insn-00bbdce8) → [`00bbdcec`](#insn-00bbdcec)
- ブロック [`00bbdcec`](#insn-00bbdcec) 範囲 `[['00bbdcec', '00bbdcf7']]`
  - `FALL_THROUGH` [`00bbdcf4`](#insn-00bbdcf4) → [`00bbdcf8`](#insn-00bbdcf8)
- ブロック [`00bbdcf8`](#insn-00bbdcf8) 範囲 `[['00bbdcf8', '00bbdd03']]`
  - `FALL_THROUGH` [`00bbdd00`](#insn-00bbdd00) → [`00bbdd04`](#insn-00bbdd04)
- ブロック [`00bbdd04`](#insn-00bbdd04) 範囲 `[['00bbdd04', '00bbdd13']]`
  - `FALL_THROUGH` [`00bbdd10`](#insn-00bbdd10) → [`00bbdd14`](#insn-00bbdd14)
- ブロック [`00bbdd14`](#insn-00bbdd14) 範囲 `[['00bbdd14', '00bbdd4b']]`
- ブロック [`00bbdd4c`](#insn-00bbdd4c) 範囲 `[['00bbdd4c', '00bbdd4f']]`

## 命令位置別の参照

- [`00bbdca0`](#insn-00bbdca0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdca4`](#insn-00bbdca4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdca8`](#insn-00bbdca8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdcc8`](#insn-00bbdcc8) → [`00bbdcec`](#insn-00bbdcec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdcd4`](#insn-00bbdcd4) → [`00bdd0d0`](../00bdd/00bdd0d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd0d0` · 推定シンボル `None` · 推定型 `None`
- [`00bbdcd8`](#insn-00bbdcd8) → [`00bbdd4c`](#insn-00bbdd4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdcfc`](#insn-00bbdcfc) → [`00bdb090`](../00bdb/00bdb090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb090` · 推定シンボル `None` · 推定型 `None`
- [`00bbdd0c`](#insn-00bbdd0c) → `00c176a8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00bbdd38`](#insn-00bbdd38) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdd3c`](#insn-00bbdd3c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdd40`](#insn-00bbdd40) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdd4c`](#insn-00bbdd4c) → [`00bdb0d0`](../00bdb/00bdb0d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb0d0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbdca0`](#insn-00bbdca0)

~~~json
{
  "source": "00bbdca0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdca4`](#insn-00bbdca4)

~~~json
{
  "source": "00bbdca4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdca8`](#insn-00bbdca8)

~~~json
{
  "source": "00bbdca8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdcc8`](#insn-00bbdcc8)

~~~json
{
  "source": "00bbdcc8",
  "target": "00bbdcec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdcd4`](#insn-00bbdcd4)

~~~json
{
  "source": "00bbdcd4",
  "target": "00bdd0d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbdcd8`](#insn-00bbdcd8)

~~~json
{
  "source": "00bbdcd8",
  "target": "00bbdd4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdcfc`](#insn-00bbdcfc)

~~~json
{
  "source": "00bbdcfc",
  "target": "00bdb090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbdd0c`](#insn-00bbdd0c)

~~~json
{
  "source": "00bbdd0c",
  "target": "00c176a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c176a8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbdd38`](#insn-00bbdd38)

~~~json
{
  "source": "00bbdd38",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdd3c`](#insn-00bbdd3c)

~~~json
{
  "source": "00bbdd3c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdd40`](#insn-00bbdd40)

~~~json
{
  "source": "00bbdd40",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdd4c`](#insn-00bbdd4c)

~~~json
{
  "source": "00bbdd4c",
  "target": "00bdb0d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
