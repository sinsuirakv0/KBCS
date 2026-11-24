# 00bbdda8

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bbdd64`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbdd64.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0078.md#compare-9bb6b7ed6e6db206a3f3a545fddb0c30)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c3a7f0`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a7f0.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/alignment_unresolved-0020.md#compare-6755e2b8bbfe84bf8dfe30b2fc0039c3)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbdda8",
  "name": "FUN_00bbdda8",
  "size": 180,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "00f27cd095b4476f2db0815c911732569118e349223c58c32c8728d9b9e55a55",
  "source_text_sha256": "00f27cd095b4476f2db0815c911732569118e349223c58c32c8728d9b9e55a55",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbdda8",
        "00bbde5b"
      ]
    ],
    "bytes_sha256": "bfc904ed395585a392538f839c5c454bd264f2282d58027b1d4a3b30e692502f",
    "instruction_count": 45,
    "instruction_bytes": 180,
    "body_bytes": 180,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bbcc10](../00bbc/00bbcc10.md)
- [00bbd308](../00bbd/00bbd308.md)

## 呼び出し先

- [00bdb190](../00bdb/00bdb190.md)
- [00bdb1d0](../00bdb/00bdb1d0.md)
- [00bdd1d0](../00bdd/00bdd1d0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1611 bytes

~~~c

undefined8 * FUN_00bbdda8(long param_1,char *param_2,undefined8 *param_3)

{
  undefined8 *puVar1;
  size_t sVar2;
  long lVar3;
  undefined8 uVar4;
  undefined8 *puVar5;
  void *pvVar6;
  
                    /* try { // try from 00bbddb8 to 00cbddbf has its CatchHandler @ 00bbe198 */
  pvVar6 = *(void **)(param_1 + 0x1330);
                    /* try { // try from 00bbddc0 to 00cbddc7 has its CatchHandler @ 00bbe02c */
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
                    /* try { // try from 00bbde04 to 00cbde0f has its CatchHandler @ 00bbe028 */
  *(long *)((long)puVar1 + 8) = lVar3 + 0x30;
  sVar2 = strlen(param_2);
                    /* try { // try from 00bbde10 to 00cbde1f has its CatchHandler @ 00bbe014 */
  uVar4 = *param_3;
  puVar5 = (undefined8 *)((long)puVar1 + lVar3 + 0x10);
  *puVar5 = &PTR_FUN_00c177a8;
                    /* try { // try from 00bbde20 to 00cbde33 has its CatchHandler @ 00bbdffc */
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
<a id="insn-00bbdda8"></a> `00bbdda8` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bbddac"></a> `00bbddac` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bbddb0"></a> `00bbddb0` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbddb4"></a> `00bbddb4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbddb8"></a> `00bbddb8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bbddbc"></a> `00bbddbc` | `16 98 49 f9` | ldr x22,[x0, #0x1330] | `FALL_THROUGH`
<a id="insn-00bbddc0"></a> `00bbddc0` | `f3 03 02 aa` | mov x19,x2 | `FALL_THROUGH`
<a id="insn-00bbddc4"></a> `00bbddc4` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00bbddc8"></a> `00bbddc8` | `c8 06 40 f9` | ldr x8,[x22, #0x8] | `FALL_THROUGH`
<a id="insn-00bbddcc"></a> `00bbddcc` | `09 01 3f d1` | sub x9,x8,#0xfc0 | `FALL_THROUGH`
<a id="insn-00bbddd0"></a> `00bbddd0` | `3f c5 3f b1` | cmn x9,#0xff1 | `FALL_THROUGH`
<a id="insn-00bbddd4"></a> `00bbddd4` | `28 01 00 54` | b.hi 0x00bbddf8 | `CONDITIONAL_JUMP`
<a id="insn-00bbddd8"></a> `00bbddd8` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bbdddc"></a> `00bbdddc` | `00 00 82 52` | mov w0,#0x1000 | `FALL_THROUGH`
<a id="insn-00bbdde0"></a> `00bbdde0` | `fc 7c 00 94` | bl 0x00bdd1d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbdde4"></a> `00bbdde4` | `a0 03 00 b4` | cbz x0,0x00bbde58 | `CONDITIONAL_JUMP`
<a id="insn-00bbdde8"></a> `00bbdde8` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbddec"></a> `00bbddec` | `16 7c 00 a9` | stp x22,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00bbddf0"></a> `00bbddf0` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bbddf4"></a> `00bbddf4` | `a0 9a 09 f9` | str x0,[x21, #0x1330] | `FALL_THROUGH`
<a id="insn-00bbddf8"></a> `00bbddf8` | `09 c1 00 91` | add x9,x8,#0x30 | `FALL_THROUGH`
<a id="insn-00bbddfc"></a> `00bbddfc` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbde00"></a> `00bbde00` | `d5 02 08 8b` | add x21,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbde04"></a> `00bbde04` | `c9 06 00 f9` | str x9,[x22, #0x8] | `FALL_THROUGH`
<a id="insn-00bbde08"></a> `00bbde08` | `e2 74 00 94` | bl 0x00bdb190 | `UNCONDITIONAL_CALL`
<a id="insn-00bbde0c"></a> `00bbde0c` | `c8 02 00 d0` | adrp x8,0xc17000 | `FALL_THROUGH`
<a id="insn-00bbde10"></a> `00bbde10` | `08 a1 1e 91` | add x8,x8,#0x7a8 | `FALL_THROUGH`
<a id="insn-00bbde14"></a> `00bbde14` | `6a 02 40 f9` | ldr x10,[x19] | `FALL_THROUGH`
<a id="insn-00bbde18"></a> `00bbde18` | `a8 0e 01 f8` | str x8,[x21, #0x10]! | `FALL_THROUGH`
<a id="insn-00bbde1c"></a> `00bbde1c` | `a9 92 40 78` | ldurh w9,[x21, #0x9] | `FALL_THROUGH`
<a id="insn-00bbde20"></a> `00bbde20` | `a8 02 80 52` | mov w8,#0x15 | `FALL_THROUGH`
<a id="insn-00bbde24"></a> `00bbde24` | `b4 02 01 a9` | stp x20,x0,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-00bbde28"></a> `00bbde28` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bbde2c"></a> `00bbde2c` | `a8 22 00 39` | strb w8,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00bbde30"></a> `00bbde30` | `28 0d 14 12` | and w8,w9,#0xf000 | `FALL_THROUGH`
<a id="insn-00bbde34"></a> `00bbde34` | `09 a8 80 52` | mov w9,#0x540 | `FALL_THROUGH`
<a id="insn-00bbde38"></a> `00bbde38` | `08 01 09 2a` | orr w8,w8,w9 | `FALL_THROUGH`
<a id="insn-00bbde3c"></a> `00bbde3c` | `a8 92 00 78` | sturh w8,[x21, #0x9] | `FALL_THROUGH`
<a id="insn-00bbde40"></a> `00bbde40` | `aa 12 00 f9` | str x10,[x21, #0x20] | `FALL_THROUGH`
<a id="insn-00bbde44"></a> `00bbde44` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbde48"></a> `00bbde48` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbde4c"></a> `00bbde4c` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bbde50"></a> `00bbde50` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bbde54"></a> `00bbde54` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bbde58"></a> `00bbde58` | `de 74 00 94` | bl 0x00bdb1d0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbdda8`](#insn-00bbdda8) 範囲 `[['00bbdda8', '00bbddb7']]`
  - `FALL_THROUGH` [`00bbddb4`](#insn-00bbddb4) → [`00bbddb8`](#insn-00bbddb8)
- ブロック [`00bbddb8`](#insn-00bbddb8) 範囲 `[['00bbddb8', '00bbddbf']]`
  - `FALL_THROUGH` [`00bbddbc`](#insn-00bbddbc) → [`00bbddc0`](#insn-00bbddc0)
- ブロック [`00bbddc0`](#insn-00bbddc0) 範囲 `[['00bbddc0', '00bbddd7']]`
  - `CONDITIONAL_JUMP` [`00bbddd4`](#insn-00bbddd4) → [`00bbddf8`](#insn-00bbddf8)
  - `FALL_THROUGH` [`00bbddd4`](#insn-00bbddd4) → [`00bbddd8`](#insn-00bbddd8)
- ブロック [`00bbddd8`](#insn-00bbddd8) 範囲 `[['00bbddd8', '00bbdde7']]`
  - `CONDITIONAL_JUMP` [`00bbdde4`](#insn-00bbdde4) → [`00bbde58`](#insn-00bbde58)
  - `FALL_THROUGH` [`00bbdde4`](#insn-00bbdde4) → [`00bbdde8`](#insn-00bbdde8)
- ブロック [`00bbdde8`](#insn-00bbdde8) 範囲 `[['00bbdde8', '00bbddf7']]`
  - `FALL_THROUGH` [`00bbddf4`](#insn-00bbddf4) → [`00bbddf8`](#insn-00bbddf8)
- ブロック [`00bbddf8`](#insn-00bbddf8) 範囲 `[['00bbddf8', '00bbde03']]`
  - `FALL_THROUGH` [`00bbde00`](#insn-00bbde00) → [`00bbde04`](#insn-00bbde04)
- ブロック [`00bbde04`](#insn-00bbde04) 範囲 `[['00bbde04', '00bbde0f']]`
  - `FALL_THROUGH` [`00bbde0c`](#insn-00bbde0c) → [`00bbde10`](#insn-00bbde10)
- ブロック [`00bbde10`](#insn-00bbde10) 範囲 `[['00bbde10', '00bbde1f']]`
  - `FALL_THROUGH` [`00bbde1c`](#insn-00bbde1c) → [`00bbde20`](#insn-00bbde20)
- ブロック [`00bbde20`](#insn-00bbde20) 範囲 `[['00bbde20', '00bbde57']]`
- ブロック [`00bbde58`](#insn-00bbde58) 範囲 `[['00bbde58', '00bbde5b']]`

## 命令位置別の参照

- [`00bbddac`](#insn-00bbddac) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbddb0`](#insn-00bbddb0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbddb4`](#insn-00bbddb4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbddd4`](#insn-00bbddd4) → [`00bbddf8`](#insn-00bbddf8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdde0`](#insn-00bbdde0) → [`00bdd1d0`](../00bdd/00bdd1d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd1d0` · 推定シンボル `None` · 推定型 `None`
- [`00bbdde4`](#insn-00bbdde4) → [`00bbde58`](#insn-00bbde58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbde08`](#insn-00bbde08) → [`00bdb190`](../00bdb/00bdb190.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb190` · 推定シンボル `None` · 推定型 `None`
- [`00bbde18`](#insn-00bbde18) → `00c177a8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00bbde44`](#insn-00bbde44) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbde48`](#insn-00bbde48) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbde4c`](#insn-00bbde4c) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbde58`](#insn-00bbde58) → [`00bdb1d0`](../00bdb/00bdb1d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb1d0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbddac`](#insn-00bbddac)

~~~json
{
  "source": "00bbddac",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbddb0`](#insn-00bbddb0)

~~~json
{
  "source": "00bbddb0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbddb4`](#insn-00bbddb4)

~~~json
{
  "source": "00bbddb4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbddd4`](#insn-00bbddd4)

~~~json
{
  "source": "00bbddd4",
  "target": "00bbddf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdde0`](#insn-00bbdde0)

~~~json
{
  "source": "00bbdde0",
  "target": "00bdd1d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbdde4`](#insn-00bbdde4)

~~~json
{
  "source": "00bbdde4",
  "target": "00bbde58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbde08`](#insn-00bbde08)

~~~json
{
  "source": "00bbde08",
  "target": "00bdb190",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbde18`](#insn-00bbde18)

~~~json
{
  "source": "00bbde18",
  "target": "00c177a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c177a8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbde44`](#insn-00bbde44)

~~~json
{
  "source": "00bbde44",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbde48`](#insn-00bbde48)

~~~json
{
  "source": "00bbde48",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbde4c`](#insn-00bbde4c)

~~~json
{
  "source": "00bbde4c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbde58`](#insn-00bbde58)

~~~json
{
  "source": "00bbde58",
  "target": "00bdb1d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
