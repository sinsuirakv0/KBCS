# 00adacc0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00adad88`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ada/00adad88.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0057.md#compare-2b0d7564fa25f3295a7e5f26b333ea77)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00adacc0",
  "name": "Java_jp_co_ponos_battlecats_TapjoyImplementation_onTapjoyPlacementRequestFailure",
  "size": 200,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e998201a0327453958c72549312310395f1deaf81954482f383ff310f0706af3",
  "source_text_sha256": "e998201a0327453958c72549312310395f1deaf81954482f383ff310f0706af3",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00adacc0",
        "00adad83"
      ],
      [
        "00adadc8",
        "00adadcb"
      ]
    ],
    "bytes_sha256": "d8cecdd97ed30f21db1ad4f3ad197f325eaad69e2b8bc83065ce5ab715455b8e",
    "instruction_count": 50,
    "instruction_bytes": 200,
    "body_bytes": 200,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00566a7c](../00566/00566a7c.md)
- [00adb914](../00adb/00adb914.md)
- [00bdaf60](../00bda/00bdaf60.md)
- [00bdaf90](../00bda/00bdaf90.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1490 bytes

~~~c

void Java_jp_co_ponos_battlecats_TapjoyImplementation_onTapjoyPlacementRequestFailure
               (undefined8 param_1,undefined8 param_2,undefined8 param_3)

{
  long lVar1;
  undefined8 *puVar2;
  long *plVar3;
  byte local_68 [16];
  void *local_58;
  byte local_50 [16];
  void *local_40;
  long local_38;
  
                    /* try { // try from 00adaccc to 00bdad0b has its CatchHandler @ 00adaccc
                       catch() { ... } // from try @ 00adaccc with catch @ 00adaccc
                       catch() { ... } // from try @ 00adad1c with catch @ 00adaccc */
  lVar1 = tpidr_el0;
  local_38 = *(long *)(lVar1 + 0x28);
  FUN_00566a7c(local_50,param_1,param_3);
  FUN_00566a7c(local_68,param_1,param_3);
                    /* try { // try from 00adad0c to 00bdad1b has its CatchHandler @ 00adad5c */
  puVar2 = (undefined8 *)FUN_00adb914(&DAT_0109fe38,local_50);
                    /* try { // try from 00adad1c to 00bdad9b has its CatchHandler @ 00adaccc */
  if ((puVar2 != &DAT_0109fe40) && (plVar3 = (long *)puVar2[0x12], plVar3 != (long *)0x0)) {
    (**(code **)(*plVar3 + 0x30))(plVar3,local_50,local_68);
  }
  if ((local_68[0] & 1) != 0) {
    _ZdlPv(local_58);
  }
  if ((local_50[0] & 1) != 0) {
                    /* catch() { ... } // from try @ 00adad0c with catch @ 00adad5c */
    _ZdlPv(local_40);
  }
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
<a id="insn-00adacc0"></a> `00adacc0` | `ff c3 01 d1` | sub sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00adacc4"></a> `00adacc4` | `fd 7b 04 a9` | stp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00adacc8"></a> `00adacc8` | `f5 2b 00 f9` | str x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00adaccc"></a> `00adaccc` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00adacd0"></a> `00adacd0` | `fd 03 01 91` | add x29,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00adacd4"></a> `00adacd4` | `55 d0 3b d5` | mrs x21,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00adacd8"></a> `00adacd8` | `e1 03 02 aa` | mov x1,x2 | `FALL_THROUGH`
<a id="insn-00adacdc"></a> `00adacdc` | `f3 03 02 aa` | mov x19,x2 | `FALL_THROUGH`
<a id="insn-00adace0"></a> `00adace0` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00adace4"></a> `00adace4` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00adace8"></a> `00adace8` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00adacec"></a> `00adacec` | `e8 83 00 91` | add x8,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00adacf0"></a> `00adacf0` | `63 2f ea 97` | bl 0x00566a7c | `UNCONDITIONAL_CALL`
<a id="insn-00adacf4"></a> `00adacf4` | `e8 23 00 91` | add x8,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00adacf8"></a> `00adacf8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00adacfc"></a> `00adacfc` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00adad00"></a> `00adad00` | `5f 2f ea 97` | bl 0x00566a7c | `UNCONDITIONAL_CALL`
<a id="insn-00adad04"></a> `00adad04` | `20 2e 00 b0` | adrp x0,0x109f000 | `FALL_THROUGH`
<a id="insn-00adad08"></a> `00adad08` | `00 e0 38 91` | add x0,x0,#0xe38 | `FALL_THROUGH`
<a id="insn-00adad0c"></a> `00adad0c` | `e1 83 00 91` | add x1,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00adad10"></a> `00adad10` | `01 03 00 94` | bl 0x00adb914 | `UNCONDITIONAL_CALL`
<a id="insn-00adad14"></a> `00adad14` | `28 2e 00 b0` | adrp x8,0x109f000 | `FALL_THROUGH`
<a id="insn-00adad18"></a> `00adad18` | `08 01 39 91` | add x8,x8,#0xe40 | `FALL_THROUGH`
<a id="insn-00adad1c"></a> `00adad1c` | `1f 00 08 eb` | cmp x0,x8 | `FALL_THROUGH`
<a id="insn-00adad20"></a> `00adad20` | `00 01 00 54` | b.eq 0x00adad40 | `CONDITIONAL_JUMP`
<a id="insn-00adad24"></a> `00adad24` | `00 48 40 f9` | ldr x0,[x0, #0x90] | `FALL_THROUGH`
<a id="insn-00adad28"></a> `00adad28` | `c0 00 00 b4` | cbz x0,0x00adad40 | `CONDITIONAL_JUMP`
<a id="insn-00adad2c"></a> `00adad2c` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00adad30"></a> `00adad30` | `08 19 40 f9` | ldr x8,[x8, #0x30] | `FALL_THROUGH`
<a id="insn-00adad34"></a> `00adad34` | `e1 83 00 91` | add x1,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00adad38"></a> `00adad38` | `e2 23 00 91` | add x2,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00adad3c"></a> `00adad3c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00adad40"></a> `00adad40` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00adad44"></a> `00adad44` | `68 00 00 36` | tbz w8,#0x0,0x00adad50 | `CONDITIONAL_JUMP`
<a id="insn-00adad48"></a> `00adad48` | `e0 0f 40 f9` | ldr x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00adad4c"></a> `00adad4c` | `85 00 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00adad50"></a> `00adad50` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00adad54"></a> `00adad54` | `68 00 00 36` | tbz w8,#0x0,0x00adad60 | `CONDITIONAL_JUMP`
<a id="insn-00adad58"></a> `00adad58` | `e0 1b 40 f9` | ldr x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00adad5c"></a> `00adad5c` | `81 00 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00adad60"></a> `00adad60` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00adad64"></a> `00adad64` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00adad68"></a> `00adad68` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00adad6c"></a> `00adad6c` | `e1 02 00 54` | b.ne 0x00adadc8 | `CONDITIONAL_JUMP`
<a id="insn-00adad70"></a> `00adad70` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00adad74"></a> `00adad74` | `f5 2b 40 f9` | ldr x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00adad78"></a> `00adad78` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00adad7c"></a> `00adad7c` | `ff c3 01 91` | add sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00adad80"></a> `00adad80` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00adadc8"></a> `00adadc8` | `72 00 04 94` | bl 0x00bdaf90 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00adacc0`](#insn-00adacc0) 範囲 `[['00adacc0', '00adaccb']]`
  - `FALL_THROUGH` [`00adacc8`](#insn-00adacc8) → [`00adaccc`](#insn-00adaccc)
- ブロック [`00adaccc`](#insn-00adaccc) 範囲 `[['00adaccc', '00adad0b']]`
  - `FALL_THROUGH` [`00adad08`](#insn-00adad08) → [`00adad0c`](#insn-00adad0c)
- ブロック [`00adad0c`](#insn-00adad0c) 範囲 `[['00adad0c', '00adad1b']]`
  - `FALL_THROUGH` [`00adad18`](#insn-00adad18) → [`00adad1c`](#insn-00adad1c)
- ブロック [`00adad1c`](#insn-00adad1c) 範囲 `[['00adad1c', '00adad23']]`
  - `CONDITIONAL_JUMP` [`00adad20`](#insn-00adad20) → [`00adad40`](#insn-00adad40)
  - `FALL_THROUGH` [`00adad20`](#insn-00adad20) → [`00adad24`](#insn-00adad24)
- ブロック [`00adad24`](#insn-00adad24) 範囲 `[['00adad24', '00adad2b']]`
  - `CONDITIONAL_JUMP` [`00adad28`](#insn-00adad28) → [`00adad40`](#insn-00adad40)
  - `FALL_THROUGH` [`00adad28`](#insn-00adad28) → [`00adad2c`](#insn-00adad2c)
- ブロック [`00adad2c`](#insn-00adad2c) 範囲 `[['00adad2c', '00adad3f']]`
  - `FALL_THROUGH` [`00adad3c`](#insn-00adad3c) → [`00adad40`](#insn-00adad40)
- ブロック [`00adad40`](#insn-00adad40) 範囲 `[['00adad40', '00adad47']]`
  - `CONDITIONAL_JUMP` [`00adad44`](#insn-00adad44) → [`00adad50`](#insn-00adad50)
  - `FALL_THROUGH` [`00adad44`](#insn-00adad44) → [`00adad48`](#insn-00adad48)
- ブロック [`00adad48`](#insn-00adad48) 範囲 `[['00adad48', '00adad4f']]`
  - `FALL_THROUGH` [`00adad4c`](#insn-00adad4c) → [`00adad50`](#insn-00adad50)
- ブロック [`00adad50`](#insn-00adad50) 範囲 `[['00adad50', '00adad57']]`
  - `CONDITIONAL_JUMP` [`00adad54`](#insn-00adad54) → [`00adad60`](#insn-00adad60)
  - `FALL_THROUGH` [`00adad54`](#insn-00adad54) → [`00adad58`](#insn-00adad58)
- ブロック [`00adad58`](#insn-00adad58) 範囲 `[['00adad58', '00adad5b']]`
  - `FALL_THROUGH` [`00adad58`](#insn-00adad58) → [`00adad5c`](#insn-00adad5c)
- ブロック [`00adad5c`](#insn-00adad5c) 範囲 `[['00adad5c', '00adad5f']]`
  - `FALL_THROUGH` [`00adad5c`](#insn-00adad5c) → [`00adad60`](#insn-00adad60)
- ブロック [`00adad60`](#insn-00adad60) 範囲 `[['00adad60', '00adad6f']]`
  - `CONDITIONAL_JUMP` [`00adad6c`](#insn-00adad6c) → [`00adadc8`](#insn-00adadc8)
  - `FALL_THROUGH` [`00adad6c`](#insn-00adad6c) → [`00adad70`](#insn-00adad70)
- ブロック [`00adad70`](#insn-00adad70) 範囲 `[['00adad70', '00adad83']]`
- ブロック [`00adadc8`](#insn-00adadc8) 範囲 `[['00adadc8', '00adadcb']]`

## 命令位置別の参照

- [`00adacc4`](#insn-00adacc4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adacc8`](#insn-00adacc8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adaccc`](#insn-00adaccc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adace8`](#insn-00adace8) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adacf0`](#insn-00adacf0) → [`00566a7c`](../00566/00566a7c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00566a7c` · 推定シンボル `None` · 推定型 `None`
- [`00adad00`](#insn-00adad00) → [`00566a7c`](../00566/00566a7c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00566a7c` · 推定シンボル `None` · 推定型 `None`
- [`00adad08`](#insn-00adad08) → `0109fe38`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adad10`](#insn-00adad10) → [`00adb914`](../00adb/00adb914.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00adb914` · 推定シンボル `None` · 推定型 `None`
- [`00adad20`](#insn-00adad20) → [`00adad40`](#insn-00adad40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adad28`](#insn-00adad28) → [`00adad40`](#insn-00adad40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adad40`](#insn-00adad40) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adad44`](#insn-00adad44) → [`00adad50`](#insn-00adad50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adad48`](#insn-00adad48) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adad4c`](#insn-00adad4c) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00adad50`](#insn-00adad50) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adad54`](#insn-00adad54) → [`00adad60`](#insn-00adad60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adad58`](#insn-00adad58) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adad5c`](#insn-00adad5c) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00adad64`](#insn-00adad64) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adad6c`](#insn-00adad6c) → [`00adadc8`](#insn-00adadc8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adad70`](#insn-00adad70) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adad74`](#insn-00adad74) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adad78`](#insn-00adad78) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adadc8`](#insn-00adadc8) → [`00bdaf90`](../00bda/00bdaf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf90` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00adacc4`](#insn-00adacc4)

~~~json
{
  "source": "00adacc4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adacc8`](#insn-00adacc8)

~~~json
{
  "source": "00adacc8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adaccc`](#insn-00adaccc)

~~~json
{
  "source": "00adaccc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adace8`](#insn-00adace8)

~~~json
{
  "source": "00adace8",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adacf0`](#insn-00adacf0)

~~~json
{
  "source": "00adacf0",
  "target": "00566a7c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adad00`](#insn-00adad00)

~~~json
{
  "source": "00adad00",
  "target": "00566a7c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adad08`](#insn-00adad08)

~~~json
{
  "source": "00adad08",
  "target": "0109fe38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fe38",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adad10`](#insn-00adad10)

~~~json
{
  "source": "00adad10",
  "target": "00adb914",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adad20`](#insn-00adad20)

~~~json
{
  "source": "00adad20",
  "target": "00adad40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adad28`](#insn-00adad28)

~~~json
{
  "source": "00adad28",
  "target": "00adad40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adad40`](#insn-00adad40)

~~~json
{
  "source": "00adad40",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adad44`](#insn-00adad44)

~~~json
{
  "source": "00adad44",
  "target": "00adad50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adad48`](#insn-00adad48)

~~~json
{
  "source": "00adad48",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adad4c`](#insn-00adad4c)

~~~json
{
  "source": "00adad4c",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adad50`](#insn-00adad50)

~~~json
{
  "source": "00adad50",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adad54`](#insn-00adad54)

~~~json
{
  "source": "00adad54",
  "target": "00adad60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adad58`](#insn-00adad58)

~~~json
{
  "source": "00adad58",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adad5c`](#insn-00adad5c)

~~~json
{
  "source": "00adad5c",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adad64`](#insn-00adad64)

~~~json
{
  "source": "00adad64",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adad6c`](#insn-00adad6c)

~~~json
{
  "source": "00adad6c",
  "target": "00adadc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adad70`](#insn-00adad70)

~~~json
{
  "source": "00adad70",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adad74`](#insn-00adad74)

~~~json
{
  "source": "00adad74",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adad78`](#insn-00adad78)

~~~json
{
  "source": "00adad78",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adadc8`](#insn-00adadc8)

~~~json
{
  "source": "00adadc8",
  "target": "00bdaf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
