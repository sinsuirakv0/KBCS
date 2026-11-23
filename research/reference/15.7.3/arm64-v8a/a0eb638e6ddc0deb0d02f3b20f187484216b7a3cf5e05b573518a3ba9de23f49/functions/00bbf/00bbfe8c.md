# 00bbfe8c

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bbfdc4`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbf/00bbfdc4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0078.md#compare-c156f642a8430bf631f5d6adecc39d99)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bbfed0`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbfed0.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0078.md#compare-e551a570f71c504018f3c9bfaba22e07)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbfe8c",
  "name": "FUN_00bbfe8c",
  "size": 160,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3d9bed1bf4dbe16b31b1b13184227038108b62e7a638929fdb61d331080f7186",
  "source_text_sha256": "3d9bed1bf4dbe16b31b1b13184227038108b62e7a638929fdb61d331080f7186",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbfe8c",
        "00bbff2b"
      ]
    ],
    "bytes_sha256": "89855184b7161267b09f5e5ea6789bab66742c8db1c3d19a820a7e81e5560c3e",
    "instruction_count": 40,
    "instruction_bytes": 160,
    "body_bytes": 160,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bbd2c4](../00bbd/00bbd2c4.md)

## 呼び出し先

- [00bdb180](../00bdb/00bdb180.md)
- [00bdd180](../00bdd/00bdd180.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1393 bytes

~~~c

void FUN_00bbfe8c(long param_1,undefined8 *param_2)

{
  undefined8 *puVar1;
  long lVar2;
  void *pvVar3;
  undefined8 uVar4;
  undefined8 uVar5;
  
  pvVar3 = *(void **)(param_1 + 0x1330);
                    /* try { // try from 00bbfea8 to 00cbfeb3 has its CatchHandler @ 00bc83b0 */
  lVar2 = *(long *)((long)pvVar3 + 8);
                    /* try { // try from 00bbfeb4 to 00cbfebf has its CatchHandler @ 00bc83a0 */
  puVar1 = pvVar3;
  if (lVar2 - 0xfd0U < 0xfffffffffffff010) {
                    /* try { // try from 00bbfec0 to 00cbfecb has its CatchHandler @ 00bc8390 */
    puVar1 = malloc(0x1000);
    if (puVar1 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
      _ZSt9terminatev();
    }
    lVar2 = 0;
                    /* try { // try from 00bbfecc to 00cbff33 has its CatchHandler @ 00bbf52c */
    *puVar1 = pvVar3;
    puVar1[1] = 0;
    *(undefined8 **)(param_1 + 0x1330) = puVar1;
  }
  *(long *)((long)puVar1 + 8) = lVar2 + 0x20;
  *(undefined ***)((long)puVar1 + lVar2 + 0x10) = &PTR_FUN_00c19898;
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
<a id="insn-00bbfe8c"></a> `00bbfe8c` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bbfe90"></a> `00bbfe90` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bbfe94"></a> `00bbfe94` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbfe98"></a> `00bbfe98` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbfe9c"></a> `00bbfe9c` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bbfea0"></a> `00bbfea0` | `15 98 49 f9` | ldr x21,[x0, #0x1330] | `FALL_THROUGH`
<a id="insn-00bbfea4"></a> `00bbfea4` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bbfea8"></a> `00bbfea8` | `a8 06 40 f9` | ldr x8,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00bbfeac"></a> `00bbfeac` | `09 41 3f d1` | sub x9,x8,#0xfd0 | `FALL_THROUGH`
<a id="insn-00bbfeb0"></a> `00bbfeb0` | `3f c5 3f b1` | cmn x9,#0xff1 | `FALL_THROUGH`
<a id="insn-00bbfeb4"></a> `00bbfeb4` | `28 01 00 54` | b.hi 0x00bbfed8 | `CONDITIONAL_JUMP`
<a id="insn-00bbfeb8"></a> `00bbfeb8` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bbfebc"></a> `00bbfebc` | `00 00 82 52` | mov w0,#0x1000 | `FALL_THROUGH`
<a id="insn-00bbfec0"></a> `00bbfec0` | `b0 74 00 94` | bl 0x00bdd180 | `UNCONDITIONAL_CALL`
<a id="insn-00bbfec4"></a> `00bbfec4` | `20 03 00 b4` | cbz x0,0x00bbff28 | `CONDITIONAL_JUMP`
<a id="insn-00bbfec8"></a> `00bbfec8` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbfecc"></a> `00bbfecc` | `15 7c 00 a9` | stp x21,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00bbfed0"></a> `00bbfed0` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bbfed4"></a> `00bbfed4` | `80 9a 09 f9` | str x0,[x20, #0x1330] | `FALL_THROUGH`
<a id="insn-00bbfed8"></a> `00bbfed8` | `09 81 00 91` | add x9,x8,#0x20 | `FALL_THROUGH`
<a id="insn-00bbfedc"></a> `00bbfedc` | `a0 02 08 8b` | add x0,x21,x8 | `FALL_THROUGH`
<a id="insn-00bbfee0"></a> `00bbfee0` | `c8 02 00 d0` | adrp x8,0xc19000 | `FALL_THROUGH`
<a id="insn-00bbfee4"></a> `00bbfee4` | `08 61 22 91` | add x8,x8,#0x898 | `FALL_THROUGH`
<a id="insn-00bbfee8"></a> `00bbfee8` | `a9 06 00 f9` | str x9,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00bbfeec"></a> `00bbfeec` | `49 01 80 52` | mov w9,#0xa | `FALL_THROUGH`
<a id="insn-00bbfef0"></a> `00bbfef0` | `08 0c 01 f8` | str x8,[x0, #0x10]! | `FALL_THROUGH`
<a id="insn-00bbfef4"></a> `00bbfef4` | `08 90 40 78` | ldurh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00bbfef8"></a> `00bbfef8` | `09 20 00 39` | strb w9,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bbfefc"></a> `00bbfefc` | `09 a8 80 52` | mov w9,#0x540 | `FALL_THROUGH`
<a id="insn-00bbff00"></a> `00bbff00` | `08 0d 14 12` | and w8,w8,#0xf000 | `FALL_THROUGH`
<a id="insn-00bbff04"></a> `00bbff04` | `60 02 c0 3d` | ldr q0,[x19] | `FALL_THROUGH`
<a id="insn-00bbff08"></a> `00bbff08` | `08 01 09 2a` | orr w8,w8,w9 | `FALL_THROUGH`
<a id="insn-00bbff0c"></a> `00bbff0c` | `08 90 00 78` | sturh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00bbff10"></a> `00bbff10` | `00 04 80 3d` | str q0,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bbff14"></a> `00bbff14` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbff18"></a> `00bbff18` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbff1c"></a> `00bbff1c` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bbff20"></a> `00bbff20` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bbff24"></a> `00bbff24` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bbff28"></a> `00bbff28` | `96 6c 00 94` | bl 0x00bdb180 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbfe8c`](#insn-00bbfe8c) 範囲 `[['00bbfe8c', '00bbfea7']]`
  - `FALL_THROUGH` [`00bbfea4`](#insn-00bbfea4) → [`00bbfea8`](#insn-00bbfea8)
- ブロック [`00bbfea8`](#insn-00bbfea8) 範囲 `[['00bbfea8', '00bbfeb3']]`
  - `FALL_THROUGH` [`00bbfeb0`](#insn-00bbfeb0) → [`00bbfeb4`](#insn-00bbfeb4)
- ブロック [`00bbfeb4`](#insn-00bbfeb4) 範囲 `[['00bbfeb4', '00bbfeb7']]`
  - `CONDITIONAL_JUMP` [`00bbfeb4`](#insn-00bbfeb4) → [`00bbfed8`](#insn-00bbfed8)
  - `FALL_THROUGH` [`00bbfeb4`](#insn-00bbfeb4) → [`00bbfeb8`](#insn-00bbfeb8)
- ブロック [`00bbfeb8`](#insn-00bbfeb8) 範囲 `[['00bbfeb8', '00bbfebf']]`
  - `FALL_THROUGH` [`00bbfebc`](#insn-00bbfebc) → [`00bbfec0`](#insn-00bbfec0)
- ブロック [`00bbfec0`](#insn-00bbfec0) 範囲 `[['00bbfec0', '00bbfec7']]`
  - `CONDITIONAL_JUMP` [`00bbfec4`](#insn-00bbfec4) → [`00bbff28`](#insn-00bbff28)
  - `FALL_THROUGH` [`00bbfec4`](#insn-00bbfec4) → [`00bbfec8`](#insn-00bbfec8)
- ブロック [`00bbfec8`](#insn-00bbfec8) 範囲 `[['00bbfec8', '00bbfecb']]`
  - `FALL_THROUGH` [`00bbfec8`](#insn-00bbfec8) → [`00bbfecc`](#insn-00bbfecc)
- ブロック [`00bbfecc`](#insn-00bbfecc) 範囲 `[['00bbfecc', '00bbfed7']]`
  - `FALL_THROUGH` [`00bbfed4`](#insn-00bbfed4) → [`00bbfed8`](#insn-00bbfed8)
- ブロック [`00bbfed8`](#insn-00bbfed8) 範囲 `[['00bbfed8', '00bbff27']]`
- ブロック [`00bbff28`](#insn-00bbff28) 範囲 `[['00bbff28', '00bbff2b']]`

## 命令位置別の参照

- [`00bbfe90`](#insn-00bbfe90) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfe94`](#insn-00bbfe94) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfe98`](#insn-00bbfe98) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfeb4`](#insn-00bbfeb4) → [`00bbfed8`](#insn-00bbfed8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfec0`](#insn-00bbfec0) → [`00bdd180`](../00bdd/00bdd180.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd180` · 推定シンボル `None` · 推定型 `None`
- [`00bbfec4`](#insn-00bbfec4) → [`00bbff28`](#insn-00bbff28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfef0`](#insn-00bbfef0) → `00c19898`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00bbff14`](#insn-00bbff14) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbff18`](#insn-00bbff18) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbff1c`](#insn-00bbff1c) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbff28`](#insn-00bbff28) → [`00bdb180`](../00bdb/00bdb180.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb180` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbfe90`](#insn-00bbfe90)

~~~json
{
  "source": "00bbfe90",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfe94`](#insn-00bbfe94)

~~~json
{
  "source": "00bbfe94",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfe98`](#insn-00bbfe98)

~~~json
{
  "source": "00bbfe98",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfeb4`](#insn-00bbfeb4)

~~~json
{
  "source": "00bbfeb4",
  "target": "00bbfed8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfec0`](#insn-00bbfec0)

~~~json
{
  "source": "00bbfec0",
  "target": "00bdd180",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbfec4`](#insn-00bbfec4)

~~~json
{
  "source": "00bbfec4",
  "target": "00bbff28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfef0`](#insn-00bbfef0)

~~~json
{
  "source": "00bbfef0",
  "target": "00c19898",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c19898",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbff14`](#insn-00bbff14)

~~~json
{
  "source": "00bbff14",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbff18`](#insn-00bbff18)

~~~json
{
  "source": "00bbff18",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbff1c`](#insn-00bbff1c)

~~~json
{
  "source": "00bbff1c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbff28`](#insn-00bbff28)

~~~json
{
  "source": "00bbff28",
  "target": "00bdb180",
  "target_space": "ram",
  "resolution": "function"
}
~~~
