# 00adad0c

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00adacc8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ada/00adacc8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0060.md#compare-4eaa7dae35d352a7411cf23e577d7f8d)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b3a6e4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3a/00b3a6e4.md) · 移動量 `+0x5f9d8`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/alignment_unresolved-0014.md#compare-bc19c51d1470d9a62b5eca2eb2bab7b6)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00adad0c",
  "name": "Java_jp_co_ponos_battlecats_TapjoyImplementation_onTapjoyPlacementRequestSuccess",
  "size": 148,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "405da835612ac695f21eb4936043978e35e2c0ce9ca62ee010310e27ff766a62",
  "source_text_sha256": "405da835612ac695f21eb4936043978e35e2c0ce9ca62ee010310e27ff766a62",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00adad0c",
        "00adad9b"
      ],
      [
        "00adadc8",
        "00adadcb"
      ]
    ],
    "bytes_sha256": "8a96112709c5ecafdd69200d6fd3aa8222f8b5cc9e73f58c6a41dc46013ad1df",
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
- [00adba20](../00adb/00adba20.md)
- [00bdb060](../00bdb/00bdb060.md)
- [00bdb090](../00bdb/00bdb090.md)

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
  
                    /* try { // try from 00adad10 to 00bdad4f has its CatchHandler @ 00adad10
                       catch() { ... } // from try @ 00adad10 with catch @ 00adad10
                       catch() { ... } // from try @ 00adad60 with catch @ 00adad10 */
  lVar1 = tpidr_el0;
  local_28 = *(long *)(lVar1 + 0x28);
  FUN_00566a7c(local_40,param_1,param_3);
  puVar2 = (undefined8 *)FUN_00adba20(&DAT_0109ff38,local_40);
                    /* try { // try from 00adad50 to 00bdad5f has its CatchHandler @ 00adada0 */
  if ((puVar2 != &DAT_0109ff40) && (plVar3 = (long *)puVar2[0xc], plVar3 != (long *)0x0)) {
                    /* try { // try from 00adad60 to 00bdaddf has its CatchHandler @ 00adad10 */
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
<a id="insn-00adad0c"></a> `00adad0c` | `ff 03 01 d1` | sub sp,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00adad10"></a> `00adad10` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00adad14"></a> `00adad14` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00adad18"></a> `00adad18` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00adad1c"></a> `00adad1c` | `54 d0 3b d5` | mrs x20,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00adad20"></a> `00adad20` | `e1 03 02 aa` | mov x1,x2 | `FALL_THROUGH`
<a id="insn-00adad24"></a> `00adad24` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00adad28"></a> `00adad28` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00adad2c"></a> `00adad2c` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00adad30"></a> `00adad30` | `53 2f ea 97` | bl 0x00566a7c | `UNCONDITIONAL_CALL`
<a id="insn-00adad34"></a> `00adad34` | `20 2e 00 b0` | adrp x0,0x109f000 | `FALL_THROUGH`
<a id="insn-00adad38"></a> `00adad38` | `00 e0 3c 91` | add x0,x0,#0xf38 | `FALL_THROUGH`
<a id="insn-00adad3c"></a> `00adad3c` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00adad40"></a> `00adad40` | `38 03 00 94` | bl 0x00adba20 | `UNCONDITIONAL_CALL`
<a id="insn-00adad44"></a> `00adad44` | `28 2e 00 b0` | adrp x8,0x109f000 | `FALL_THROUGH`
<a id="insn-00adad48"></a> `00adad48` | `08 01 3d 91` | add x8,x8,#0xf40 | `FALL_THROUGH`
<a id="insn-00adad4c"></a> `00adad4c` | `1f 00 08 eb` | cmp x0,x8 | `FALL_THROUGH`
<a id="insn-00adad50"></a> `00adad50` | `e0 00 00 54` | b.eq 0x00adad6c | `CONDITIONAL_JUMP`
<a id="insn-00adad54"></a> `00adad54` | `00 30 40 f9` | ldr x0,[x0, #0x60] | `FALL_THROUGH`
<a id="insn-00adad58"></a> `00adad58` | `a0 00 00 b4` | cbz x0,0x00adad6c | `CONDITIONAL_JUMP`
<a id="insn-00adad5c"></a> `00adad5c` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00adad60"></a> `00adad60` | `08 19 40 f9` | ldr x8,[x8, #0x30] | `FALL_THROUGH`
<a id="insn-00adad64"></a> `00adad64` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00adad68"></a> `00adad68` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00adad6c"></a> `00adad6c` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-00adad70"></a> `00adad70` | `68 00 00 36` | tbz w8,#0x0,0x00adad7c | `CONDITIONAL_JUMP`
<a id="insn-00adad74"></a> `00adad74` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00adad78"></a> `00adad78` | `ba 00 04 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00adad7c"></a> `00adad7c` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00adad80"></a> `00adad80` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00adad84"></a> `00adad84` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00adad88"></a> `00adad88` | `01 02 00 54` | b.ne 0x00adadc8 | `CONDITIONAL_JUMP`
<a id="insn-00adad8c"></a> `00adad8c` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00adad90"></a> `00adad90` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00adad94"></a> `00adad94` | `ff 03 01 91` | add sp,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00adad98"></a> `00adad98` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00adadc8"></a> `00adadc8` | `b2 00 04 94` | bl 0x00bdb090 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00adad0c`](#insn-00adad0c) 範囲 `[['00adad0c', '00adad0f']]`
  - `FALL_THROUGH` [`00adad0c`](#insn-00adad0c) → [`00adad10`](#insn-00adad10)
- ブロック [`00adad10`](#insn-00adad10) 範囲 `[['00adad10', '00adad4f']]`
  - `FALL_THROUGH` [`00adad4c`](#insn-00adad4c) → [`00adad50`](#insn-00adad50)
- ブロック [`00adad50`](#insn-00adad50) 範囲 `[['00adad50', '00adad53']]`
  - `CONDITIONAL_JUMP` [`00adad50`](#insn-00adad50) → [`00adad6c`](#insn-00adad6c)
  - `FALL_THROUGH` [`00adad50`](#insn-00adad50) → [`00adad54`](#insn-00adad54)
- ブロック [`00adad54`](#insn-00adad54) 範囲 `[['00adad54', '00adad5b']]`
  - `CONDITIONAL_JUMP` [`00adad58`](#insn-00adad58) → [`00adad6c`](#insn-00adad6c)
  - `FALL_THROUGH` [`00adad58`](#insn-00adad58) → [`00adad5c`](#insn-00adad5c)
- ブロック [`00adad5c`](#insn-00adad5c) 範囲 `[['00adad5c', '00adad5f']]`
  - `FALL_THROUGH` [`00adad5c`](#insn-00adad5c) → [`00adad60`](#insn-00adad60)
- ブロック [`00adad60`](#insn-00adad60) 範囲 `[['00adad60', '00adad6b']]`
  - `FALL_THROUGH` [`00adad68`](#insn-00adad68) → [`00adad6c`](#insn-00adad6c)
- ブロック [`00adad6c`](#insn-00adad6c) 範囲 `[['00adad6c', '00adad73']]`
  - `CONDITIONAL_JUMP` [`00adad70`](#insn-00adad70) → [`00adad7c`](#insn-00adad7c)
  - `FALL_THROUGH` [`00adad70`](#insn-00adad70) → [`00adad74`](#insn-00adad74)
- ブロック [`00adad74`](#insn-00adad74) 範囲 `[['00adad74', '00adad7b']]`
  - `FALL_THROUGH` [`00adad78`](#insn-00adad78) → [`00adad7c`](#insn-00adad7c)
- ブロック [`00adad7c`](#insn-00adad7c) 範囲 `[['00adad7c', '00adad8b']]`
  - `CONDITIONAL_JUMP` [`00adad88`](#insn-00adad88) → [`00adadc8`](#insn-00adadc8)
  - `FALL_THROUGH` [`00adad88`](#insn-00adad88) → [`00adad8c`](#insn-00adad8c)
- ブロック [`00adad8c`](#insn-00adad8c) 範囲 `[['00adad8c', '00adad9b']]`
- ブロック [`00adadc8`](#insn-00adadc8) 範囲 `[['00adadc8', '00adadcb']]`

## 命令位置別の参照

- [`00adad10`](#insn-00adad10) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adad14`](#insn-00adad14) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adad28`](#insn-00adad28) → `Stack[-0x28]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adad30`](#insn-00adad30) → [`00566a7c`](../00566/00566a7c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00566a7c` · 推定シンボル `None` · 推定型 `None`
- [`00adad38`](#insn-00adad38) → `0109ff38`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adad40`](#insn-00adad40) → [`00adba20`](../00adb/00adba20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00adba20` · 推定シンボル `None` · 推定型 `None`
- [`00adad50`](#insn-00adad50) → [`00adad6c`](#insn-00adad6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adad58`](#insn-00adad58) → [`00adad6c`](#insn-00adad6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adad6c`](#insn-00adad6c) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adad70`](#insn-00adad70) → [`00adad7c`](#insn-00adad7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adad74`](#insn-00adad74) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adad78`](#insn-00adad78) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00adad80`](#insn-00adad80) → `Stack[-0x28]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adad88`](#insn-00adad88) → [`00adadc8`](#insn-00adadc8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adad8c`](#insn-00adad8c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adad90`](#insn-00adad90) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adadc8`](#insn-00adadc8) → [`00bdb090`](../00bdb/00bdb090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb090` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00adad10`](#insn-00adad10)

~~~json
{
  "source": "00adad10",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adad14`](#insn-00adad14)

~~~json
{
  "source": "00adad14",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adad28`](#insn-00adad28)

~~~json
{
  "source": "00adad28",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adad30`](#insn-00adad30)

~~~json
{
  "source": "00adad30",
  "target": "00566a7c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adad38`](#insn-00adad38)

~~~json
{
  "source": "00adad38",
  "target": "0109ff38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109ff38",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adad40`](#insn-00adad40)

~~~json
{
  "source": "00adad40",
  "target": "00adba20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adad50`](#insn-00adad50)

~~~json
{
  "source": "00adad50",
  "target": "00adad6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adad58`](#insn-00adad58)

~~~json
{
  "source": "00adad58",
  "target": "00adad6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adad6c`](#insn-00adad6c)

~~~json
{
  "source": "00adad6c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adad70`](#insn-00adad70)

~~~json
{
  "source": "00adad70",
  "target": "00adad7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adad74`](#insn-00adad74)

~~~json
{
  "source": "00adad74",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adad78`](#insn-00adad78)

~~~json
{
  "source": "00adad78",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adad80`](#insn-00adad80)

~~~json
{
  "source": "00adad80",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adad88`](#insn-00adad88)

~~~json
{
  "source": "00adad88",
  "target": "00adadc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adad8c`](#insn-00adad8c)

~~~json
{
  "source": "00adad8c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adad90`](#insn-00adad90)

~~~json
{
  "source": "00adad90",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adadc8`](#insn-00adadc8)

~~~json
{
  "source": "00adadc8",
  "target": "00bdb090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
