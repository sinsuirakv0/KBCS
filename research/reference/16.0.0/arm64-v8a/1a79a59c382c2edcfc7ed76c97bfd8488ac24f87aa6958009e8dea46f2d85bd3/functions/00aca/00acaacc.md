# 00acaacc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00a6cb38`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6c/00a6cb38.md) · 移動量 `+0x5df94`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0053.md#compare-c66c3596a503d389a26b91b025c04580)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00acacc8`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aca/00acacc8.md) · 移動量 `+0x1fc`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0035.md#compare-59bee5bd326d340a38aa6e5d6609e46a)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acaacc",
  "name": "FUN_00acaacc",
  "size": 228,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "655180e014d62fa3e0b6c30072214e8e53ae679e8ffc7c7d376b480c98455051",
  "source_text_sha256": "655180e014d62fa3e0b6c30072214e8e53ae679e8ffc7c7d376b480c98455051",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00acaacc",
        "00acabaf"
      ]
    ],
    "bytes_sha256": "8b174af125b4142d6abfd3d3dc7206d86c9e567f4d3ebdc8c254daf77fa7ddd9",
    "instruction_count": 57,
    "instruction_bytes": 228,
    "body_bytes": 228,
    "indirect": 3,
    "unresolved": 3
  }
}
~~~

## 呼び出し元

- [006af35c](../006af/006af35c.md)
- [00830e5c](../00830/00830e5c.md)

## 呼び出し先

- [0057be68](../0057b/0057be68.md)
- [00ac9398](../00ac9/00ac9398.md)
- [00c57ae0](../00c57/00c57ae0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1026 bytes

~~~c

void FUN_00acaacc(long param_1,long *param_2)

{
  long lVar1;
  long *plVar2;
  long *plVar3;
  long lVar4;
  long local_70 [4];
  long *local_50;
  long local_38;
  
  local_50 = local_70;
  plVar3 = local_70;
  lVar1 = tpidr_el0;
  local_38 = *(long *)(lVar1 + 0x28);
  plVar2 = (long *)param_2[4];
  *(undefined1 *)(param_1 + 0xa0) = 1;
  *(undefined4 *)(param_1 + 0xa4) = 0;
  if (plVar2 == (long *)0x0) {
    local_50 = (long *)0x0;
  }
  else if (plVar2 == param_2) {
    (**(code **)(*param_2 + 0x18))(param_2,local_70);
  }
  else {
    local_50 = (long *)(**(code **)(*plVar2 + 0x10))();
  }
  FUN_0057be68(local_70,param_1 + 0x140);
  if (local_50 == local_70) {
    lVar4 = 0x20;
  }
  else {
    if (local_50 == (long *)0x0) goto LAB_00acab80;
    lVar4 = 0x28;
    plVar3 = local_50;
  }
  (**(code **)(*plVar3 + lVar4))();
LAB_00acab80:
  FUN_00ac9398(param_1);
  if (*(long *)(lVar1 + 0x28) == local_38) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00acaacc"></a> `00acaacc` | `ff c3 01 d1` | sub sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00acaad0"></a> `00acaad0` | `fd 7b 04 a9` | stp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00acaad4"></a> `00acaad4` | `f5 2b 00 f9` | str x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00acaad8"></a> `00acaad8` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00acaadc"></a> `00acaadc` | `fd 03 01 91` | add x29,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00acaae0"></a> `00acaae0` | `54 d0 3b d5` | mrs x20,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00acaae4"></a> `00acaae4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00acaae8"></a> `00acaae8` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00acaaec"></a> `00acaaec` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00acaaf0"></a> `00acaaf0` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00acaaf4"></a> `00acaaf4` | `20 10 40 f9` | ldr x0,[x1, #0x20] | `FALL_THROUGH`
<a id="insn-00acaaf8"></a> `00acaaf8` | `68 82 02 39` | strb w8,[x19, #0xa0] | `FALL_THROUGH`
<a id="insn-00acaafc"></a> `00acaafc` | `7f a6 00 b9` | str wzr,[x19, #0xa4] | `FALL_THROUGH`
<a id="insn-00acab00"></a> `00acab00` | `00 01 00 b4` | cbz x0,0x00acab20 | `CONDITIONAL_JUMP`
<a id="insn-00acab04"></a> `00acab04` | `1f 00 01 eb` | cmp x0,x1 | `FALL_THROUGH`
<a id="insn-00acab08"></a> `00acab08` | `00 01 00 54` | b.eq 0x00acab28 | `CONDITIONAL_JUMP`
<a id="insn-00acab0c"></a> `00acab0c` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00acab10"></a> `00acab10` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00acab14"></a> `00acab14` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00acab18"></a> `00acab18` | `e0 13 00 f9` | str x0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00acab1c"></a> `00acab1c` | `0a 00 00 14` | b 0x00acab44 | `UNCONDITIONAL_JUMP`
<a id="insn-00acab20"></a> `00acab20` | `ff 13 00 f9` | str xzr,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00acab24"></a> `00acab24` | `08 00 00 14` | b 0x00acab44 | `UNCONDITIONAL_JUMP`
<a id="insn-00acab28"></a> `00acab28` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00acab2c"></a> `00acab2c` | `29 00 40 f9` | ldr x9,[x1] | `FALL_THROUGH`
<a id="insn-00acab30"></a> `00acab30` | `e0 03 01 aa` | mov x0,x1 | `FALL_THROUGH`
<a id="insn-00acab34"></a> `00acab34` | `e8 13 00 f9` | str x8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00acab38"></a> `00acab38` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00acab3c"></a> `00acab3c` | `28 0d 40 f9` | ldr x8,[x9, #0x18] | `FALL_THROUGH`
<a id="insn-00acab40"></a> `00acab40` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00acab44"></a> `00acab44` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00acab48"></a> `00acab48` | `61 02 05 91` | add x1,x19,#0x140 | `FALL_THROUGH`
<a id="insn-00acab4c"></a> `00acab4c` | `f5 03 00 91` | mov x21,sp | `FALL_THROUGH`
<a id="insn-00acab50"></a> `00acab50` | `c6 c4 ea 97` | bl 0x0057be68 | `UNCONDITIONAL_CALL`
<a id="insn-00acab54"></a> `00acab54` | `e0 13 40 f9` | ldr x0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00acab58"></a> `00acab58` | `1f 00 15 eb` | cmp x0,x21 | `FALL_THROUGH`
<a id="insn-00acab5c"></a> `00acab5c` | `80 00 00 54` | b.eq 0x00acab6c | `CONDITIONAL_JUMP`
<a id="insn-00acab60"></a> `00acab60` | `00 01 00 b4` | cbz x0,0x00acab80 | `CONDITIONAL_JUMP`
<a id="insn-00acab64"></a> `00acab64` | `08 05 80 52` | mov w8,#0x28 | `FALL_THROUGH`
<a id="insn-00acab68"></a> `00acab68` | `03 00 00 14` | b 0x00acab74 | `UNCONDITIONAL_JUMP`
<a id="insn-00acab6c"></a> `00acab6c` | `08 04 80 52` | mov w8,#0x20 | `FALL_THROUGH`
<a id="insn-00acab70"></a> `00acab70` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00acab74"></a> `00acab74` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-00acab78"></a> `00acab78` | `28 69 68 f8` | ldr x8,[x9, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00acab7c"></a> `00acab7c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00acab80"></a> `00acab80` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00acab84"></a> `00acab84` | `05 fa ff 97` | bl 0x00ac9398 | `UNCONDITIONAL_CALL`
<a id="insn-00acab88"></a> `00acab88` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00acab8c"></a> `00acab8c` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00acab90"></a> `00acab90` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00acab94"></a> `00acab94` | `c1 00 00 54` | b.ne 0x00acabac | `CONDITIONAL_JUMP`
<a id="insn-00acab98"></a> `00acab98` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00acab9c"></a> `00acab9c` | `f5 2b 40 f9` | ldr x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00acaba0"></a> `00acaba0` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00acaba4"></a> `00acaba4` | `ff c3 01 91` | add sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00acaba8"></a> `00acaba8` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00acabac"></a> `00acabac` | `cd 33 06 94` | bl 0x00c57ae0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00acaacc`](#insn-00acaacc) 範囲 `[['00acaacc', '00acab03']]`
  - `CONDITIONAL_JUMP` [`00acab00`](#insn-00acab00) → [`00acab20`](#insn-00acab20)
  - `FALL_THROUGH` [`00acab00`](#insn-00acab00) → [`00acab04`](#insn-00acab04)
- ブロック [`00acab04`](#insn-00acab04) 範囲 `[['00acab04', '00acab0b']]`
  - `CONDITIONAL_JUMP` [`00acab08`](#insn-00acab08) → [`00acab28`](#insn-00acab28)
  - `FALL_THROUGH` [`00acab08`](#insn-00acab08) → [`00acab0c`](#insn-00acab0c)
- ブロック [`00acab0c`](#insn-00acab0c) 範囲 `[['00acab0c', '00acab1f']]`
  - `UNCONDITIONAL_JUMP` [`00acab1c`](#insn-00acab1c) → [`00acab44`](#insn-00acab44)
- ブロック [`00acab20`](#insn-00acab20) 範囲 `[['00acab20', '00acab27']]`
  - `UNCONDITIONAL_JUMP` [`00acab24`](#insn-00acab24) → [`00acab44`](#insn-00acab44)
- ブロック [`00acab28`](#insn-00acab28) 範囲 `[['00acab28', '00acab43']]`
  - `FALL_THROUGH` [`00acab40`](#insn-00acab40) → [`00acab44`](#insn-00acab44)
- ブロック [`00acab44`](#insn-00acab44) 範囲 `[['00acab44', '00acab5f']]`
  - `CONDITIONAL_JUMP` [`00acab5c`](#insn-00acab5c) → [`00acab6c`](#insn-00acab6c)
  - `FALL_THROUGH` [`00acab5c`](#insn-00acab5c) → [`00acab60`](#insn-00acab60)
- ブロック [`00acab60`](#insn-00acab60) 範囲 `[['00acab60', '00acab63']]`
  - `CONDITIONAL_JUMP` [`00acab60`](#insn-00acab60) → [`00acab80`](#insn-00acab80)
  - `FALL_THROUGH` [`00acab60`](#insn-00acab60) → [`00acab64`](#insn-00acab64)
- ブロック [`00acab64`](#insn-00acab64) 範囲 `[['00acab64', '00acab6b']]`
  - `UNCONDITIONAL_JUMP` [`00acab68`](#insn-00acab68) → [`00acab74`](#insn-00acab74)
- ブロック [`00acab6c`](#insn-00acab6c) 範囲 `[['00acab6c', '00acab73']]`
  - `FALL_THROUGH` [`00acab70`](#insn-00acab70) → [`00acab74`](#insn-00acab74)
- ブロック [`00acab74`](#insn-00acab74) 範囲 `[['00acab74', '00acab7f']]`
  - `FALL_THROUGH` [`00acab7c`](#insn-00acab7c) → [`00acab80`](#insn-00acab80)
- ブロック [`00acab80`](#insn-00acab80) 範囲 `[['00acab80', '00acab97']]`
  - `CONDITIONAL_JUMP` [`00acab94`](#insn-00acab94) → [`00acabac`](#insn-00acabac)
  - `FALL_THROUGH` [`00acab94`](#insn-00acab94) → [`00acab98`](#insn-00acab98)
- ブロック [`00acab98`](#insn-00acab98) 範囲 `[['00acab98', '00acabab']]`
- ブロック [`00acabac`](#insn-00acabac) 範囲 `[['00acabac', '00acabaf']]`

## 命令位置別の参照

- [`00acaad0`](#insn-00acaad0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acaad4`](#insn-00acaad4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acaad8`](#insn-00acaad8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acaaec`](#insn-00acaaec) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acab00`](#insn-00acab00) → [`00acab20`](#insn-00acab20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acab08`](#insn-00acab08) → [`00acab28`](#insn-00acab28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acab18`](#insn-00acab18) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acab1c`](#insn-00acab1c) → [`00acab44`](#insn-00acab44) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acab20`](#insn-00acab20) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acab24`](#insn-00acab24) → [`00acab44`](#insn-00acab44) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acab34`](#insn-00acab34) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acab50`](#insn-00acab50) → [`0057be68`](../0057b/0057be68.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0057be68` · 推定シンボル `None` · 推定型 `None`
- [`00acab54`](#insn-00acab54) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acab5c`](#insn-00acab5c) → [`00acab6c`](#insn-00acab6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acab60`](#insn-00acab60) → [`00acab80`](#insn-00acab80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acab68`](#insn-00acab68) → [`00acab74`](#insn-00acab74) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acab74`](#insn-00acab74) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acab84`](#insn-00acab84) → [`00ac9398`](../00ac9/00ac9398.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ac9398` · 推定シンボル `None` · 推定型 `None`
- [`00acab8c`](#insn-00acab8c) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acab94`](#insn-00acab94) → [`00acabac`](#insn-00acabac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acab98`](#insn-00acab98) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acab9c`](#insn-00acab9c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acaba0`](#insn-00acaba0) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acabac`](#insn-00acabac) → [`00c57ae0`](../00c57/00c57ae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ae0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00acaad0`](#insn-00acaad0)

~~~json
{
  "source": "00acaad0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acaad4`](#insn-00acaad4)

~~~json
{
  "source": "00acaad4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acaad8`](#insn-00acaad8)

~~~json
{
  "source": "00acaad8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acaaec`](#insn-00acaaec)

~~~json
{
  "source": "00acaaec",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acab00`](#insn-00acab00)

~~~json
{
  "source": "00acab00",
  "target": "00acab20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acab08`](#insn-00acab08)

~~~json
{
  "source": "00acab08",
  "target": "00acab28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acab18`](#insn-00acab18)

~~~json
{
  "source": "00acab18",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acab1c`](#insn-00acab1c)

~~~json
{
  "source": "00acab1c",
  "target": "00acab44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acab20`](#insn-00acab20)

~~~json
{
  "source": "00acab20",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acab24`](#insn-00acab24)

~~~json
{
  "source": "00acab24",
  "target": "00acab44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acab34`](#insn-00acab34)

~~~json
{
  "source": "00acab34",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acab50`](#insn-00acab50)

~~~json
{
  "source": "00acab50",
  "target": "0057be68",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acab54`](#insn-00acab54)

~~~json
{
  "source": "00acab54",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acab5c`](#insn-00acab5c)

~~~json
{
  "source": "00acab5c",
  "target": "00acab6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acab60`](#insn-00acab60)

~~~json
{
  "source": "00acab60",
  "target": "00acab80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acab68`](#insn-00acab68)

~~~json
{
  "source": "00acab68",
  "target": "00acab74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acab74`](#insn-00acab74)

~~~json
{
  "source": "00acab74",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acab84`](#insn-00acab84)

~~~json
{
  "source": "00acab84",
  "target": "00ac9398",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acab8c`](#insn-00acab8c)

~~~json
{
  "source": "00acab8c",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acab94`](#insn-00acab94)

~~~json
{
  "source": "00acab94",
  "target": "00acabac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acab98`](#insn-00acab98)

~~~json
{
  "source": "00acab98",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acab9c`](#insn-00acab9c)

~~~json
{
  "source": "00acab9c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acaba0`](#insn-00acaba0)

~~~json
{
  "source": "00acaba0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acabac`](#insn-00acabac)

~~~json
{
  "source": "00acabac",
  "target": "00c57ae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
