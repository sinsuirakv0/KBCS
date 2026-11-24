# 00adadcc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00adad88`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ada/00adad88.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0060.md#compare-97daa083f38d3b120a68a0e68a38f60a)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b3a7a4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3a/00b3a7a4.md) · 移動量 `+0x5f9d8`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0055.md#compare-f6cdcc80727bef735314652308a97888)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00adadcc",
  "name": "Java_jp_co_ponos_battlecats_TapjoyImplementation_onTapjoyPlacementRequestFailure",
  "size": 200,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d8420b36aab70911f79586e3351ded4690dee6ba398feb690ebfb737747fd4c1",
  "source_text_sha256": "d8420b36aab70911f79586e3351ded4690dee6ba398feb690ebfb737747fd4c1",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00adadcc",
        "00adae8f"
      ],
      [
        "00adaed4",
        "00adaed7"
      ]
    ],
    "bytes_sha256": "b848df9fc88426ab84aabff0a5a829245b8f38c01efcc0235e287f28e2d6a33b",
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
- [00adba20](../00adb/00adba20.md)
- [00bdb060](../00bdb/00bdb060.md)
- [00bdb090](../00bdb/00bdb090.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 944 bytes

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
  
  lVar1 = tpidr_el0;
  local_38 = *(long *)(lVar1 + 0x28);
  FUN_00566a7c(local_50,param_1,param_3);
  FUN_00566a7c(local_68,param_1,param_3);
  puVar2 = (undefined8 *)FUN_00adba20(&DAT_0109ff38,local_50);
  if ((puVar2 != &DAT_0109ff40) && (plVar3 = (long *)puVar2[0x12], plVar3 != (long *)0x0)) {
    (**(code **)(*plVar3 + 0x30))(plVar3,local_50,local_68);
  }
  if ((local_68[0] & 1) != 0) {
    _ZdlPv(local_58);
  }
  if ((local_50[0] & 1) != 0) {
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
<a id="insn-00adadcc"></a> `00adadcc` | `ff c3 01 d1` | sub sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00adadd0"></a> `00adadd0` | `fd 7b 04 a9` | stp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00adadd4"></a> `00adadd4` | `f5 2b 00 f9` | str x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00adadd8"></a> `00adadd8` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00adaddc"></a> `00adaddc` | `fd 03 01 91` | add x29,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00adade0"></a> `00adade0` | `55 d0 3b d5` | mrs x21,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00adade4"></a> `00adade4` | `e1 03 02 aa` | mov x1,x2 | `FALL_THROUGH`
<a id="insn-00adade8"></a> `00adade8` | `f3 03 02 aa` | mov x19,x2 | `FALL_THROUGH`
<a id="insn-00adadec"></a> `00adadec` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00adadf0"></a> `00adadf0` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00adadf4"></a> `00adadf4` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00adadf8"></a> `00adadf8` | `e8 83 00 91` | add x8,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00adadfc"></a> `00adadfc` | `20 2f ea 97` | bl 0x00566a7c | `UNCONDITIONAL_CALL`
<a id="insn-00adae00"></a> `00adae00` | `e8 23 00 91` | add x8,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00adae04"></a> `00adae04` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00adae08"></a> `00adae08` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00adae0c"></a> `00adae0c` | `1c 2f ea 97` | bl 0x00566a7c | `UNCONDITIONAL_CALL`
<a id="insn-00adae10"></a> `00adae10` | `20 2e 00 b0` | adrp x0,0x109f000 | `FALL_THROUGH`
<a id="insn-00adae14"></a> `00adae14` | `00 e0 3c 91` | add x0,x0,#0xf38 | `FALL_THROUGH`
<a id="insn-00adae18"></a> `00adae18` | `e1 83 00 91` | add x1,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00adae1c"></a> `00adae1c` | `01 03 00 94` | bl 0x00adba20 | `UNCONDITIONAL_CALL`
<a id="insn-00adae20"></a> `00adae20` | `28 2e 00 b0` | adrp x8,0x109f000 | `FALL_THROUGH`
<a id="insn-00adae24"></a> `00adae24` | `08 01 3d 91` | add x8,x8,#0xf40 | `FALL_THROUGH`
<a id="insn-00adae28"></a> `00adae28` | `1f 00 08 eb` | cmp x0,x8 | `FALL_THROUGH`
<a id="insn-00adae2c"></a> `00adae2c` | `00 01 00 54` | b.eq 0x00adae4c | `CONDITIONAL_JUMP`
<a id="insn-00adae30"></a> `00adae30` | `00 48 40 f9` | ldr x0,[x0, #0x90] | `FALL_THROUGH`
<a id="insn-00adae34"></a> `00adae34` | `c0 00 00 b4` | cbz x0,0x00adae4c | `CONDITIONAL_JUMP`
<a id="insn-00adae38"></a> `00adae38` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00adae3c"></a> `00adae3c` | `08 19 40 f9` | ldr x8,[x8, #0x30] | `FALL_THROUGH`
<a id="insn-00adae40"></a> `00adae40` | `e1 83 00 91` | add x1,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00adae44"></a> `00adae44` | `e2 23 00 91` | add x2,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00adae48"></a> `00adae48` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00adae4c"></a> `00adae4c` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00adae50"></a> `00adae50` | `68 00 00 36` | tbz w8,#0x0,0x00adae5c | `CONDITIONAL_JUMP`
<a id="insn-00adae54"></a> `00adae54` | `e0 0f 40 f9` | ldr x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00adae58"></a> `00adae58` | `82 00 04 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00adae5c"></a> `00adae5c` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00adae60"></a> `00adae60` | `68 00 00 36` | tbz w8,#0x0,0x00adae6c | `CONDITIONAL_JUMP`
<a id="insn-00adae64"></a> `00adae64` | `e0 1b 40 f9` | ldr x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00adae68"></a> `00adae68` | `7e 00 04 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00adae6c"></a> `00adae6c` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00adae70"></a> `00adae70` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00adae74"></a> `00adae74` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00adae78"></a> `00adae78` | `e1 02 00 54` | b.ne 0x00adaed4 | `CONDITIONAL_JUMP`
<a id="insn-00adae7c"></a> `00adae7c` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00adae80"></a> `00adae80` | `f5 2b 40 f9` | ldr x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00adae84"></a> `00adae84` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00adae88"></a> `00adae88` | `ff c3 01 91` | add sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00adae8c"></a> `00adae8c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00adaed4"></a> `00adaed4` | `6f 00 04 94` | bl 0x00bdb090 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00adadcc`](#insn-00adadcc) 範囲 `[['00adadcc', '00adae2f']]`
  - `CONDITIONAL_JUMP` [`00adae2c`](#insn-00adae2c) → [`00adae4c`](#insn-00adae4c)
  - `FALL_THROUGH` [`00adae2c`](#insn-00adae2c) → [`00adae30`](#insn-00adae30)
- ブロック [`00adae30`](#insn-00adae30) 範囲 `[['00adae30', '00adae37']]`
  - `CONDITIONAL_JUMP` [`00adae34`](#insn-00adae34) → [`00adae4c`](#insn-00adae4c)
  - `FALL_THROUGH` [`00adae34`](#insn-00adae34) → [`00adae38`](#insn-00adae38)
- ブロック [`00adae38`](#insn-00adae38) 範囲 `[['00adae38', '00adae4b']]`
  - `FALL_THROUGH` [`00adae48`](#insn-00adae48) → [`00adae4c`](#insn-00adae4c)
- ブロック [`00adae4c`](#insn-00adae4c) 範囲 `[['00adae4c', '00adae53']]`
  - `CONDITIONAL_JUMP` [`00adae50`](#insn-00adae50) → [`00adae5c`](#insn-00adae5c)
  - `FALL_THROUGH` [`00adae50`](#insn-00adae50) → [`00adae54`](#insn-00adae54)
- ブロック [`00adae54`](#insn-00adae54) 範囲 `[['00adae54', '00adae5b']]`
  - `FALL_THROUGH` [`00adae58`](#insn-00adae58) → [`00adae5c`](#insn-00adae5c)
- ブロック [`00adae5c`](#insn-00adae5c) 範囲 `[['00adae5c', '00adae63']]`
  - `CONDITIONAL_JUMP` [`00adae60`](#insn-00adae60) → [`00adae6c`](#insn-00adae6c)
  - `FALL_THROUGH` [`00adae60`](#insn-00adae60) → [`00adae64`](#insn-00adae64)
- ブロック [`00adae64`](#insn-00adae64) 範囲 `[['00adae64', '00adae6b']]`
  - `FALL_THROUGH` [`00adae68`](#insn-00adae68) → [`00adae6c`](#insn-00adae6c)
- ブロック [`00adae6c`](#insn-00adae6c) 範囲 `[['00adae6c', '00adae7b']]`
  - `CONDITIONAL_JUMP` [`00adae78`](#insn-00adae78) → [`00adaed4`](#insn-00adaed4)
  - `FALL_THROUGH` [`00adae78`](#insn-00adae78) → [`00adae7c`](#insn-00adae7c)
- ブロック [`00adae7c`](#insn-00adae7c) 範囲 `[['00adae7c', '00adae8f']]`
- ブロック [`00adaed4`](#insn-00adaed4) 範囲 `[['00adaed4', '00adaed7']]`

## 命令位置別の参照

- [`00adadd0`](#insn-00adadd0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adadd4`](#insn-00adadd4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adadd8`](#insn-00adadd8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adadf4`](#insn-00adadf4) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adadfc`](#insn-00adadfc) → [`00566a7c`](../00566/00566a7c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00566a7c` · 推定シンボル `None` · 推定型 `None`
- [`00adae0c`](#insn-00adae0c) → [`00566a7c`](../00566/00566a7c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00566a7c` · 推定シンボル `None` · 推定型 `None`
- [`00adae14`](#insn-00adae14) → `0109ff38`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adae1c`](#insn-00adae1c) → [`00adba20`](../00adb/00adba20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00adba20` · 推定シンボル `None` · 推定型 `None`
- [`00adae2c`](#insn-00adae2c) → [`00adae4c`](#insn-00adae4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adae34`](#insn-00adae34) → [`00adae4c`](#insn-00adae4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adae4c`](#insn-00adae4c) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adae50`](#insn-00adae50) → [`00adae5c`](#insn-00adae5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adae54`](#insn-00adae54) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adae58`](#insn-00adae58) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00adae5c`](#insn-00adae5c) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adae60`](#insn-00adae60) → [`00adae6c`](#insn-00adae6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adae64`](#insn-00adae64) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adae68`](#insn-00adae68) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00adae70`](#insn-00adae70) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adae78`](#insn-00adae78) → [`00adaed4`](#insn-00adaed4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adae7c`](#insn-00adae7c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adae80`](#insn-00adae80) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adae84`](#insn-00adae84) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adaed4`](#insn-00adaed4) → [`00bdb090`](../00bdb/00bdb090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb090` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00adadd0`](#insn-00adadd0)

~~~json
{
  "source": "00adadd0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adadd4`](#insn-00adadd4)

~~~json
{
  "source": "00adadd4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adadd8`](#insn-00adadd8)

~~~json
{
  "source": "00adadd8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adadf4`](#insn-00adadf4)

~~~json
{
  "source": "00adadf4",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adadfc`](#insn-00adadfc)

~~~json
{
  "source": "00adadfc",
  "target": "00566a7c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adae0c`](#insn-00adae0c)

~~~json
{
  "source": "00adae0c",
  "target": "00566a7c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adae14`](#insn-00adae14)

~~~json
{
  "source": "00adae14",
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
- 参照命令 [`00adae1c`](#insn-00adae1c)

~~~json
{
  "source": "00adae1c",
  "target": "00adba20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adae2c`](#insn-00adae2c)

~~~json
{
  "source": "00adae2c",
  "target": "00adae4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adae34`](#insn-00adae34)

~~~json
{
  "source": "00adae34",
  "target": "00adae4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adae4c`](#insn-00adae4c)

~~~json
{
  "source": "00adae4c",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adae50`](#insn-00adae50)

~~~json
{
  "source": "00adae50",
  "target": "00adae5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adae54`](#insn-00adae54)

~~~json
{
  "source": "00adae54",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adae58`](#insn-00adae58)

~~~json
{
  "source": "00adae58",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adae5c`](#insn-00adae5c)

~~~json
{
  "source": "00adae5c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adae60`](#insn-00adae60)

~~~json
{
  "source": "00adae60",
  "target": "00adae6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adae64`](#insn-00adae64)

~~~json
{
  "source": "00adae64",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adae68`](#insn-00adae68)

~~~json
{
  "source": "00adae68",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adae70`](#insn-00adae70)

~~~json
{
  "source": "00adae70",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adae78`](#insn-00adae78)

~~~json
{
  "source": "00adae78",
  "target": "00adaed4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adae7c`](#insn-00adae7c)

~~~json
{
  "source": "00adae7c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adae80`](#insn-00adae80)

~~~json
{
  "source": "00adae80",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adae84`](#insn-00adae84)

~~~json
{
  "source": "00adae84",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adaed4`](#insn-00adaed4)

~~~json
{
  "source": "00adaed4",
  "target": "00bdb090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
