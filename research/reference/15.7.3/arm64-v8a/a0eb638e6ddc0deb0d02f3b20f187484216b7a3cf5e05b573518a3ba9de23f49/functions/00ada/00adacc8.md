# 00adacc8

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00adac00`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ada/00adac00.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/alignment_unresolved-0001.md#compare-a1bf2d2cef0dc35954fd39d6a152ba35)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00adad0c`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00adad0c.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0060.md#compare-4eaa7dae35d352a7411cf23e577d7f8d)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00adacc8",
  "name": "Java_jp_co_ponos_battlecats_TapjoyImplementation_onTapjoyPlacementRequestSuccess",
  "size": 148,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7374003f99f66fa28d2fea19bd9d5906a185c8dbcf3f7f37861d658c2a0d53f1",
  "source_text_sha256": "7374003f99f66fa28d2fea19bd9d5906a185c8dbcf3f7f37861d658c2a0d53f1",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00adacc8",
        "00adad57"
      ],
      [
        "00adad84",
        "00adad87"
      ]
    ],
    "bytes_sha256": "3e4ab0a338759da68cb24a001cabb8735863a1b7069800994bcb04293f89a419",
    "instruction_count": 37,
    "instruction_bytes": 148,
    "body_bytes": 148,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00566a7c](../00566/00566a7c.md)
- [00adb9dc](../00adb/00adb9dc.md)
- [00bdb010](../00bdb/00bdb010.md)
- [00bdb040](../00bdb/00bdb040.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1253 bytes

~~~c

void Java_jp_co_ponos_battlecats_TapjoyImplementation_onTapjoyPlacementRequestSuccess
               (undefined8 param_1,undefined8 param_2,undefined8 param_3)

{
  long lVar1;
  undefined8 *puVar2;
  long *plVar3;
  byte local_40 [16];
  void *local_30;
  long local_28;
  
                    /* try { // try from 00adaccc to 00bdad0b has its CatchHandler @ 00adaccc
                       catch() { ... } // from try @ 00adaccc with catch @ 00adaccc
                       catch() { ... } // from try @ 00adad1c with catch @ 00adaccc */
  lVar1 = tpidr_el0;
  local_28 = *(long *)(lVar1 + 0x28);
  FUN_00566a7c(local_40,param_1,param_3);
  puVar2 = (undefined8 *)FUN_00adb9dc(&DAT_0109fef8,local_40);
                    /* try { // try from 00adad0c to 00bdad1b has its CatchHandler @ 00adad5c */
  if ((puVar2 != &DAT_0109ff00) && (plVar3 = (long *)puVar2[0xc], plVar3 != (long *)0x0)) {
                    /* try { // try from 00adad1c to 00bdad9b has its CatchHandler @ 00adaccc */
    (**(code **)(*plVar3 + 0x30))(plVar3,local_40);
  }
  if ((local_40[0] & 1) != 0) {
    _ZdlPv(local_30);
  }
  if (*(long *)(lVar1 + 0x28) == local_28) {
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
<a id="insn-00adacc8"></a> `00adacc8` | `ff 03 01 d1` | sub sp,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00adaccc"></a> `00adaccc` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00adacd0"></a> `00adacd0` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00adacd4"></a> `00adacd4` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00adacd8"></a> `00adacd8` | `54 d0 3b d5` | mrs x20,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00adacdc"></a> `00adacdc` | `e1 03 02 aa` | mov x1,x2 | `FALL_THROUGH`
<a id="insn-00adace0"></a> `00adace0` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00adace4"></a> `00adace4` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00adace8"></a> `00adace8` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00adacec"></a> `00adacec` | `64 2f ea 97` | bl 0x00566a7c | `UNCONDITIONAL_CALL`
<a id="insn-00adacf0"></a> `00adacf0` | `20 2e 00 b0` | adrp x0,0x109f000 | `FALL_THROUGH`
<a id="insn-00adacf4"></a> `00adacf4` | `00 e0 3b 91` | add x0,x0,#0xef8 | `FALL_THROUGH`
<a id="insn-00adacf8"></a> `00adacf8` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00adacfc"></a> `00adacfc` | `38 03 00 94` | bl 0x00adb9dc | `UNCONDITIONAL_CALL`
<a id="insn-00adad00"></a> `00adad00` | `28 2e 00 b0` | adrp x8,0x109f000 | `FALL_THROUGH`
<a id="insn-00adad04"></a> `00adad04` | `08 01 3c 91` | add x8,x8,#0xf00 | `FALL_THROUGH`
<a id="insn-00adad08"></a> `00adad08` | `1f 00 08 eb` | cmp x0,x8 | `FALL_THROUGH`
<a id="insn-00adad0c"></a> `00adad0c` | `e0 00 00 54` | b.eq 0x00adad28 | `CONDITIONAL_JUMP`
<a id="insn-00adad10"></a> `00adad10` | `00 30 40 f9` | ldr x0,[x0, #0x60] | `FALL_THROUGH`
<a id="insn-00adad14"></a> `00adad14` | `a0 00 00 b4` | cbz x0,0x00adad28 | `CONDITIONAL_JUMP`
<a id="insn-00adad18"></a> `00adad18` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00adad1c"></a> `00adad1c` | `08 19 40 f9` | ldr x8,[x8, #0x30] | `FALL_THROUGH`
<a id="insn-00adad20"></a> `00adad20` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00adad24"></a> `00adad24` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00adad28"></a> `00adad28` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-00adad2c"></a> `00adad2c` | `68 00 00 36` | tbz w8,#0x0,0x00adad38 | `CONDITIONAL_JUMP`
<a id="insn-00adad30"></a> `00adad30` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00adad34"></a> `00adad34` | `b7 00 04 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00adad38"></a> `00adad38` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00adad3c"></a> `00adad3c` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00adad40"></a> `00adad40` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00adad44"></a> `00adad44` | `01 02 00 54` | b.ne 0x00adad84 | `CONDITIONAL_JUMP`
<a id="insn-00adad48"></a> `00adad48` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00adad4c"></a> `00adad4c` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00adad50"></a> `00adad50` | `ff 03 01 91` | add sp,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00adad54"></a> `00adad54` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00adad84"></a> `00adad84` | `af 00 04 94` | bl 0x00bdb040 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00adacc8`](#insn-00adacc8) 範囲 `[['00adacc8', '00adaccb']]`
  - `FALL_THROUGH` [`00adacc8`](#insn-00adacc8) → [`00adaccc`](#insn-00adaccc)
- ブロック [`00adaccc`](#insn-00adaccc) 範囲 `[['00adaccc', '00adad0b']]`
  - `FALL_THROUGH` [`00adad08`](#insn-00adad08) → [`00adad0c`](#insn-00adad0c)
- ブロック [`00adad0c`](#insn-00adad0c) 範囲 `[['00adad0c', '00adad0f']]`
  - `CONDITIONAL_JUMP` [`00adad0c`](#insn-00adad0c) → [`00adad28`](#insn-00adad28)
  - `FALL_THROUGH` [`00adad0c`](#insn-00adad0c) → [`00adad10`](#insn-00adad10)
- ブロック [`00adad10`](#insn-00adad10) 範囲 `[['00adad10', '00adad17']]`
  - `CONDITIONAL_JUMP` [`00adad14`](#insn-00adad14) → [`00adad28`](#insn-00adad28)
  - `FALL_THROUGH` [`00adad14`](#insn-00adad14) → [`00adad18`](#insn-00adad18)
- ブロック [`00adad18`](#insn-00adad18) 範囲 `[['00adad18', '00adad1b']]`
  - `FALL_THROUGH` [`00adad18`](#insn-00adad18) → [`00adad1c`](#insn-00adad1c)
- ブロック [`00adad1c`](#insn-00adad1c) 範囲 `[['00adad1c', '00adad27']]`
  - `FALL_THROUGH` [`00adad24`](#insn-00adad24) → [`00adad28`](#insn-00adad28)
- ブロック [`00adad28`](#insn-00adad28) 範囲 `[['00adad28', '00adad2f']]`
  - `CONDITIONAL_JUMP` [`00adad2c`](#insn-00adad2c) → [`00adad38`](#insn-00adad38)
  - `FALL_THROUGH` [`00adad2c`](#insn-00adad2c) → [`00adad30`](#insn-00adad30)
- ブロック [`00adad30`](#insn-00adad30) 範囲 `[['00adad30', '00adad37']]`
  - `FALL_THROUGH` [`00adad34`](#insn-00adad34) → [`00adad38`](#insn-00adad38)
- ブロック [`00adad38`](#insn-00adad38) 範囲 `[['00adad38', '00adad47']]`
  - `CONDITIONAL_JUMP` [`00adad44`](#insn-00adad44) → [`00adad84`](#insn-00adad84)
  - `FALL_THROUGH` [`00adad44`](#insn-00adad44) → [`00adad48`](#insn-00adad48)
- ブロック [`00adad48`](#insn-00adad48) 範囲 `[['00adad48', '00adad57']]`
- ブロック [`00adad84`](#insn-00adad84) 範囲 `[['00adad84', '00adad87']]`

## 命令位置別の参照

- [`00adaccc`](#insn-00adaccc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adacd0`](#insn-00adacd0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adace4`](#insn-00adace4) → `Stack[-0x28]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adacec`](#insn-00adacec) → [`00566a7c`](../00566/00566a7c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00566a7c` · 推定シンボル `None` · 推定型 `None`
- [`00adacf4`](#insn-00adacf4) → `0109fef8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adacfc`](#insn-00adacfc) → [`00adb9dc`](../00adb/00adb9dc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00adb9dc` · 推定シンボル `None` · 推定型 `None`
- [`00adad0c`](#insn-00adad0c) → [`00adad28`](#insn-00adad28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adad14`](#insn-00adad14) → [`00adad28`](#insn-00adad28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adad28`](#insn-00adad28) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adad2c`](#insn-00adad2c) → [`00adad38`](#insn-00adad38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adad30`](#insn-00adad30) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adad34`](#insn-00adad34) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00adad3c`](#insn-00adad3c) → `Stack[-0x28]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adad44`](#insn-00adad44) → [`00adad84`](#insn-00adad84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adad48`](#insn-00adad48) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adad4c`](#insn-00adad4c) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adad84`](#insn-00adad84) → [`00bdb040`](../00bdb/00bdb040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb040` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00adaccc`](#insn-00adaccc)

~~~json
{
  "source": "00adaccc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adacd0`](#insn-00adacd0)

~~~json
{
  "source": "00adacd0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adace4`](#insn-00adace4)

~~~json
{
  "source": "00adace4",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adacec`](#insn-00adacec)

~~~json
{
  "source": "00adacec",
  "target": "00566a7c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adacf4`](#insn-00adacf4)

~~~json
{
  "source": "00adacf4",
  "target": "0109fef8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fef8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adacfc`](#insn-00adacfc)

~~~json
{
  "source": "00adacfc",
  "target": "00adb9dc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adad0c`](#insn-00adad0c)

~~~json
{
  "source": "00adad0c",
  "target": "00adad28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adad14`](#insn-00adad14)

~~~json
{
  "source": "00adad14",
  "target": "00adad28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adad28`](#insn-00adad28)

~~~json
{
  "source": "00adad28",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adad2c`](#insn-00adad2c)

~~~json
{
  "source": "00adad2c",
  "target": "00adad38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adad30`](#insn-00adad30)

~~~json
{
  "source": "00adad30",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adad34`](#insn-00adad34)

~~~json
{
  "source": "00adad34",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adad3c`](#insn-00adad3c)

~~~json
{
  "source": "00adad3c",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adad44`](#insn-00adad44)

~~~json
{
  "source": "00adad44",
  "target": "00adad84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adad48`](#insn-00adad48)

~~~json
{
  "source": "00adad48",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adad4c`](#insn-00adad4c)

~~~json
{
  "source": "00adad4c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adad84`](#insn-00adad84)

~~~json
{
  "source": "00adad84",
  "target": "00bdb040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
