# 00ab8fbc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00a5b004`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5b/00a5b004.md) · 移動量 `+0x5dfb8`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0052.md#compare-9724b385daf124e27cd2a442c9180c01)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00ab91b8`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ab9/00ab91b8.md) · 移動量 `+0x1fc`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/alignment_unresolved-0004.md#compare-b1f462f7bc02750734f2d95e0e313192)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ab8fbc",
  "name": "FUN_00ab8fbc",
  "size": 164,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6a89265f755f2ec7b68420b643e3b35834b36db690593185111fb82b49144d8b",
  "source_text_sha256": "6a89265f755f2ec7b68420b643e3b35834b36db690593185111fb82b49144d8b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ab8fbc",
        "00ab905f"
      ]
    ],
    "bytes_sha256": "d0461a4e5c42b1615ec387a0abb59a9c944fe03f039abb5ad3b59861f060999e",
    "instruction_count": 41,
    "instruction_bytes": 164,
    "body_bytes": 164,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [005fe62c](../005fe/005fe62c.md)
- [0085bec8](../0085b/0085bec8.md)
- [00ab28dc](../00ab2/00ab28dc.md)
- [00ab2fa8](../00ab2/00ab2fa8.md)
- [00ab4b04](../00ab4/00ab4b04.md)
- [00ab6544](../00ab6/00ab6544.md)
- [00ab7cac](../00ab7/00ab7cac.md)
- [00ab7f44](../00ab7/00ab7f44.md)
- [00aba964](../00aba/00aba964.md)
- [00abaadc](../00aba/00abaadc.md)

## 呼び出し先

- [00470800](../00470/00470800.md)
- [00c57a90](../00c57/00c57a90.md)
- [00c57c00](../00c57/00c57c00.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1673 bytes

~~~c

void FUN_00ab8fbc(undefined4 *param_1,long param_2,int param_3,int param_4)

{
  void *__src;
  long lVar1;
  undefined4 uVar2;
  size_t __n;
  void *__dest;
  undefined8 uVar3;
  undefined4 *puVar4;
  
                    /* catch() { ... } // from try @ 00ab8b7c with catch @ 00ab8fd0 */
                    /* catch() { ... } // from try @ 00ab8ba4 with catch @ 00ab8fe8 */
  puVar4 = (undefined4 *)(*(long *)(param_2 + (long)param_3 * 0x18) + (long)param_4 * 0x30);
  uVar2 = *puVar4;
  *(undefined8 *)(param_1 + 2) = 0;
  *(undefined8 *)(param_1 + 4) = 0;
  *(undefined8 *)(param_1 + 6) = 0;
  __src = *(void **)(puVar4 + 2);
  lVar1 = *(long *)(puVar4 + 4);
  *param_1 = uVar2;
  __n = lVar1 - (long)__src;
  if (__n != 0) {
    if ((long)__n < 0) {
                    /* WARNING: Subroutine does not return */
      FUN_00470800(param_1 + 2);
    }
                    /* catch() { ... } // from try @ 00ab8b48 with catch @ 00ab9010 */
    __dest = (void *)_Znwm(__n);
    *(void **)(param_1 + 2) = __dest;
    *(size_t *)(param_1 + 6) = (long)__dest + __n;
    memcpy(__dest,__src,__n);
    *(size_t *)(param_1 + 4) = (long)__dest + __n;
  }
  uVar3 = *(undefined8 *)(puVar4 + 8);
  *(undefined8 *)((long)param_1 + 0x25) = *(undefined8 *)((long)puVar4 + 0x25);
  *(undefined8 *)(param_1 + 8) = uVar3;
                    /* try { // try from 00ab9050 to 00bb910b has its CatchHandler @ 00ab9050
                       catch() { ... } // from try @ 00ab9050 with catch @ 00ab9050
                       catch() { ... } // from try @ 00ab9184 with catch @ 00ab9050
                       catch() { ... } // from try @ 00ab91ec with catch @ 00ab9050 */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00ab8fbc"></a> `00ab8fbc` | `fd 7b bc a9` | stp x29,x30,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00ab8fc0"></a> `00ab8fc0` | `f7 0b 00 f9` | str x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ab8fc4"></a> `00ab8fc4` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ab8fc8"></a> `00ab8fc8` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00ab8fcc"></a> `00ab8fcc` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00ab8fd0"></a> `00ab8fd0` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00ab8fd4"></a> `00ab8fd4` | `08 03 80 52` | mov w8,#0x18 | `FALL_THROUGH`
<a id="insn-00ab8fd8"></a> `00ab8fd8` | `09 06 80 52` | mov w9,#0x30 | `FALL_THROUGH`
<a id="insn-00ab8fdc"></a> `00ab8fdc` | `28 7c 28 9b` | smull x8,w1,w8 | `FALL_THROUGH`
<a id="insn-00ab8fe0"></a> `00ab8fe0` | `f4 03 13 aa` | mov x20,x19 | `FALL_THROUGH`
<a id="insn-00ab8fe4"></a> `00ab8fe4` | `08 68 68 f8` | ldr x8,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ab8fe8"></a> `00ab8fe8` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00ab8fec"></a> `00ab8fec` | `57 20 29 9b` | smaddl x23,w2,w9,x8 | `FALL_THROUGH`
<a id="insn-00ab8ff0"></a> `00ab8ff0` | `e8 02 40 b9` | ldr w8,[x23] | `FALL_THROUGH`
<a id="insn-00ab8ff4"></a> `00ab8ff4` | `9f 8e 00 f8` | str xzr,[x20, #0x8]! | `FALL_THROUGH`
<a id="insn-00ab8ff8"></a> `00ab8ff8` | `7f 7e 01 a9` | stp xzr,xzr,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00ab8ffc"></a> `00ab8ffc` | `f5 a6 40 a9` | ldp x21,x9,[x23, #0x8] | `FALL_THROUGH`
<a id="insn-00ab9000"></a> `00ab9000` | `68 02 00 b9` | str w8,[x19] | `FALL_THROUGH`
<a id="insn-00ab9004"></a> `00ab9004` | `36 01 15 eb` | subs x22,x9,x21 | `FALL_THROUGH`
<a id="insn-00ab9008"></a> `00ab9008` | `60 01 00 54` | b.eq 0x00ab9034 | `CONDITIONAL_JUMP`
<a id="insn-00ab900c"></a> `00ab900c` | `76 02 f8 b7` | tbnz x22,#0x3f,0x00ab9058 | `CONDITIONAL_JUMP`
<a id="insn-00ab9010"></a> `00ab9010` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00ab9014"></a> `00ab9014` | `9f 7a 06 94` | bl 0x00c57a90 | `UNCONDITIONAL_CALL`
<a id="insn-00ab9018"></a> `00ab9018` | `14 00 16 8b` | add x20,x0,x22 | `FALL_THROUGH`
<a id="insn-00ab901c"></a> `00ab901c` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00ab9020"></a> `00ab9020` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00ab9024"></a> `00ab9024` | `60 06 00 f9` | str x0,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00ab9028"></a> `00ab9028` | `74 0e 00 f9` | str x20,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00ab902c"></a> `00ab902c` | `f5 7a 06 94` | bl 0x00c57c00 | `UNCONDITIONAL_CALL`
<a id="insn-00ab9030"></a> `00ab9030` | `74 0a 00 f9` | str x20,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00ab9034"></a> `00ab9034` | `e8 52 42 f8` | ldur x8,[x23, #0x25] | `FALL_THROUGH`
<a id="insn-00ab9038"></a> `00ab9038` | `e9 12 40 f9` | ldr x9,[x23, #0x20] | `FALL_THROUGH`
<a id="insn-00ab903c"></a> `00ab903c` | `68 52 02 f8` | stur x8,[x19, #0x25] | `FALL_THROUGH`
<a id="insn-00ab9040"></a> `00ab9040` | `69 12 00 f9` | str x9,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00ab9044"></a> `00ab9044` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00ab9048"></a> `00ab9048` | `f7 0b 40 f9` | ldr x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ab904c"></a> `00ab904c` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ab9050"></a> `00ab9050` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00ab9054"></a> `00ab9054` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00ab9058"></a> `00ab9058` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00ab905c"></a> `00ab905c` | `e9 dd e6 97` | bl 0x00470800 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00ab8fbc`](#insn-00ab8fbc) 範囲 `[['00ab8fbc', '00ab8fcf']]`
  - `FALL_THROUGH` [`00ab8fcc`](#insn-00ab8fcc) → [`00ab8fd0`](#insn-00ab8fd0)
- ブロック [`00ab8fd0`](#insn-00ab8fd0) 範囲 `[['00ab8fd0', '00ab8fe7']]`
  - `FALL_THROUGH` [`00ab8fe4`](#insn-00ab8fe4) → [`00ab8fe8`](#insn-00ab8fe8)
- ブロック [`00ab8fe8`](#insn-00ab8fe8) 範囲 `[['00ab8fe8', '00ab900b']]`
  - `CONDITIONAL_JUMP` [`00ab9008`](#insn-00ab9008) → [`00ab9034`](#insn-00ab9034)
  - `FALL_THROUGH` [`00ab9008`](#insn-00ab9008) → [`00ab900c`](#insn-00ab900c)
- ブロック [`00ab900c`](#insn-00ab900c) 範囲 `[['00ab900c', '00ab900f']]`
  - `CONDITIONAL_JUMP` [`00ab900c`](#insn-00ab900c) → [`00ab9058`](#insn-00ab9058)
  - `FALL_THROUGH` [`00ab900c`](#insn-00ab900c) → [`00ab9010`](#insn-00ab9010)
- ブロック [`00ab9010`](#insn-00ab9010) 範囲 `[['00ab9010', '00ab9033']]`
  - `FALL_THROUGH` [`00ab9030`](#insn-00ab9030) → [`00ab9034`](#insn-00ab9034)
- ブロック [`00ab9034`](#insn-00ab9034) 範囲 `[['00ab9034', '00ab904f']]`
  - `FALL_THROUGH` [`00ab904c`](#insn-00ab904c) → [`00ab9050`](#insn-00ab9050)
- ブロック [`00ab9050`](#insn-00ab9050) 範囲 `[['00ab9050', '00ab9057']]`
- ブロック [`00ab9058`](#insn-00ab9058) 範囲 `[['00ab9058', '00ab905f']]`

## 命令位置別の参照

- [`00ab8fbc`](#insn-00ab8fbc) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab8fc0`](#insn-00ab8fc0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab8fc4`](#insn-00ab8fc4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab8fc8`](#insn-00ab8fc8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab9008`](#insn-00ab9008) → [`00ab9034`](#insn-00ab9034) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab900c`](#insn-00ab900c) → [`00ab9058`](#insn-00ab9058) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab9014`](#insn-00ab9014) → [`00c57a90`](../00c57/00c57a90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a90` · 推定シンボル `None` · 推定型 `None`
- [`00ab902c`](#insn-00ab902c) → [`00c57c00`](../00c57/00c57c00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57c00` · 推定シンボル `None` · 推定型 `None`
- [`00ab9044`](#insn-00ab9044) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab9048`](#insn-00ab9048) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab904c`](#insn-00ab904c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab9050`](#insn-00ab9050) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab905c`](#insn-00ab905c) → [`00470800`](../00470/00470800.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00470800` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00ab8fbc`](#insn-00ab8fbc)

~~~json
{
  "source": "00ab8fbc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab8fc0`](#insn-00ab8fc0)

~~~json
{
  "source": "00ab8fc0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab8fc4`](#insn-00ab8fc4)

~~~json
{
  "source": "00ab8fc4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab8fc8`](#insn-00ab8fc8)

~~~json
{
  "source": "00ab8fc8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab9008`](#insn-00ab9008)

~~~json
{
  "source": "00ab9008",
  "target": "00ab9034",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab900c`](#insn-00ab900c)

~~~json
{
  "source": "00ab900c",
  "target": "00ab9058",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab9014`](#insn-00ab9014)

~~~json
{
  "source": "00ab9014",
  "target": "00c57a90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab902c`](#insn-00ab902c)

~~~json
{
  "source": "00ab902c",
  "target": "00c57c00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab9044`](#insn-00ab9044)

~~~json
{
  "source": "00ab9044",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab9048`](#insn-00ab9048)

~~~json
{
  "source": "00ab9048",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab904c`](#insn-00ab904c)

~~~json
{
  "source": "00ab904c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab9050`](#insn-00ab9050)

~~~json
{
  "source": "00ab9050",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab905c`](#insn-00ab905c)

~~~json
{
  "source": "00ab905c",
  "target": "00470800",
  "target_space": "ram",
  "resolution": "function"
}
~~~
