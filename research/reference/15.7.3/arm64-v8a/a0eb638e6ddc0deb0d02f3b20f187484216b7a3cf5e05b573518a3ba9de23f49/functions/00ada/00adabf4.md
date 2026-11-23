# 00adabf4

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00adab2c`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ada/00adab2c.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/alignment_unresolved-0001.md#compare-e62b86351db585331f253732675edd9a)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00adac38`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00adac38.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0060.md#compare-2c417d0928e0b51defe2881e0fbbfc58)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00adabf4",
  "name": "Java_jp_co_ponos_battlecats_TapjoyImplementation_onTapjoySpendCurrency",
  "size": 168,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a860d264e9b0092b14ba4e71380fe46dde89aa6ac8d7e755a0f4ce89ddbf063b",
  "source_text_sha256": "a860d264e9b0092b14ba4e71380fe46dde89aa6ac8d7e755a0f4ce89ddbf063b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00adabf4",
        "00adac97"
      ],
      [
        "00adacc4",
        "00adacc7"
      ]
    ],
    "bytes_sha256": "ceaeec311014d91757e70febd56c21f598e9be123e735c16cd61ca18d55af6fb",
    "instruction_count": 42,
    "instruction_bytes": 168,
    "body_bytes": 168,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00436e9c](../00436/00436e9c.md)
- [00566a7c](../00566/00566a7c.md)
- [00bdb010](../00bdb/00bdb010.md)
- [00bdb040](../00bdb/00bdb040.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1145 bytes

~~~c

void Java_jp_co_ponos_battlecats_TapjoyImplementation_onTapjoySpendCurrency
               (undefined8 param_1,undefined8 param_2,undefined8 param_3,undefined4 param_4)

{
  long lVar1;
  byte local_58 [16];
  void *local_48;
  undefined4 local_3c;
  long local_38;
  
  lVar1 = tpidr_el0;
  local_38 = *(long *)(lVar1 + 0x28);
  if (DAT_0109ffb0 != (long *)0x0) {
    FUN_00566a7c(local_58,param_1,param_3);
    local_3c = param_4;
    if (DAT_0109ffb0 == (long *)0x0) {
                    /* try { // try from 00adac8c to 00bdac97 has its CatchHandler @ 00adac98 */
      if (*(long *)(lVar1 + 0x28) == local_38) {
                    /* WARNING: Subroutine does not return */
        FUN_00436e9c();
      }
      goto LAB_00adacc4;
    }
    (**(code **)(*DAT_0109ffb0 + 0x30))(DAT_0109ffb0,local_58,&local_3c);
    if ((local_58[0] & 1) != 0) {
      _ZdlPv(local_48);
    }
  }
  if (*(long *)(lVar1 + 0x28) == local_38) {
                    /* try { // try from 00adac70 to 00bdac7b has its CatchHandler @ 00adac9c */
    return;
  }
LAB_00adacc4:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00adabf4"></a> `00adabf4` | `ff 83 01 d1` | sub sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00adabf8"></a> `00adabf8` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00adabfc"></a> `00adabfc` | `f5 23 00 f9` | str x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00adac00"></a> `00adac00` | `f4 4f 05 a9` | stp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00adac04"></a> `00adac04` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00adac08"></a> `00adac08` | `54 d0 3b d5` | mrs x20,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00adac0c"></a> `00adac0c` | `35 2e 00 b0` | adrp x21,0x109f000 | `FALL_THROUGH`
<a id="insn-00adac10"></a> `00adac10` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00adac14"></a> `00adac14` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00adac18"></a> `00adac18` | `a8 da 47 f9` | ldr x8,[x21, #0xfb0] | `FALL_THROUGH`
<a id="insn-00adac1c"></a> `00adac1c` | `28 02 00 b4` | cbz x8,0x00adac60 | `CONDITIONAL_JUMP`
<a id="insn-00adac20"></a> `00adac20` | `e8 23 00 91` | add x8,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00adac24"></a> `00adac24` | `e1 03 02 aa` | mov x1,x2 | `FALL_THROUGH`
<a id="insn-00adac28"></a> `00adac28` | `f3 03 03 2a` | mov w19,w3 | `FALL_THROUGH`
<a id="insn-00adac2c"></a> `00adac2c` | `94 2f ea 97` | bl 0x00566a7c | `UNCONDITIONAL_CALL`
<a id="insn-00adac30"></a> `00adac30` | `a0 da 47 f9` | ldr x0,[x21, #0xfb0] | `FALL_THROUGH`
<a id="insn-00adac34"></a> `00adac34` | `b3 43 1f b8` | stur w19,[x29, #-0xc] | `FALL_THROUGH`
<a id="insn-00adac38"></a> `00adac38` | `60 02 00 b4` | cbz x0,0x00adac84 | `CONDITIONAL_JUMP`
<a id="insn-00adac3c"></a> `00adac3c` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00adac40"></a> `00adac40` | `08 19 40 f9` | ldr x8,[x8, #0x30] | `FALL_THROUGH`
<a id="insn-00adac44"></a> `00adac44` | `e1 23 00 91` | add x1,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00adac48"></a> `00adac48` | `a2 33 00 d1` | sub x2,x29,#0xc | `FALL_THROUGH`
<a id="insn-00adac4c"></a> `00adac4c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00adac50"></a> `00adac50` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00adac54"></a> `00adac54` | `68 00 00 36` | tbz w8,#0x0,0x00adac60 | `CONDITIONAL_JUMP`
<a id="insn-00adac58"></a> `00adac58` | `e0 0f 40 f9` | ldr x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00adac5c"></a> `00adac5c` | `ed 00 04 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00adac60"></a> `00adac60` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00adac64"></a> `00adac64` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00adac68"></a> `00adac68` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00adac6c"></a> `00adac6c` | `c1 02 00 54` | b.ne 0x00adacc4 | `CONDITIONAL_JUMP`
<a id="insn-00adac70"></a> `00adac70` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00adac74"></a> `00adac74` | `f5 23 40 f9` | ldr x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00adac78"></a> `00adac78` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00adac7c"></a> `00adac7c` | `ff 83 01 91` | add sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00adac80"></a> `00adac80` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00adac84"></a> `00adac84` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00adac88"></a> `00adac88` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00adac8c"></a> `00adac8c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00adac90"></a> `00adac90` | `a1 01 00 54` | b.ne 0x00adacc4 | `CONDITIONAL_JUMP`
<a id="insn-00adac94"></a> `00adac94` | `82 70 e5 97` | bl 0x00436e9c | `CALL_TERMINATOR`
<a id="insn-00adacc4"></a> `00adacc4` | `df 00 04 94` | bl 0x00bdb040 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00adabf4`](#insn-00adabf4) 範囲 `[['00adabf4', '00adac1f']]`
  - `CONDITIONAL_JUMP` [`00adac1c`](#insn-00adac1c) → [`00adac60`](#insn-00adac60)
  - `FALL_THROUGH` [`00adac1c`](#insn-00adac1c) → [`00adac20`](#insn-00adac20)
- ブロック [`00adac20`](#insn-00adac20) 範囲 `[['00adac20', '00adac3b']]`
  - `CONDITIONAL_JUMP` [`00adac38`](#insn-00adac38) → [`00adac84`](#insn-00adac84)
  - `FALL_THROUGH` [`00adac38`](#insn-00adac38) → [`00adac3c`](#insn-00adac3c)
- ブロック [`00adac3c`](#insn-00adac3c) 範囲 `[['00adac3c', '00adac57']]`
  - `CONDITIONAL_JUMP` [`00adac54`](#insn-00adac54) → [`00adac60`](#insn-00adac60)
  - `FALL_THROUGH` [`00adac54`](#insn-00adac54) → [`00adac58`](#insn-00adac58)
- ブロック [`00adac58`](#insn-00adac58) 範囲 `[['00adac58', '00adac5f']]`
  - `FALL_THROUGH` [`00adac5c`](#insn-00adac5c) → [`00adac60`](#insn-00adac60)
- ブロック [`00adac60`](#insn-00adac60) 範囲 `[['00adac60', '00adac6f']]`
  - `CONDITIONAL_JUMP` [`00adac6c`](#insn-00adac6c) → [`00adacc4`](#insn-00adacc4)
  - `FALL_THROUGH` [`00adac6c`](#insn-00adac6c) → [`00adac70`](#insn-00adac70)
- ブロック [`00adac70`](#insn-00adac70) 範囲 `[['00adac70', '00adac83']]`
- ブロック [`00adac84`](#insn-00adac84) 範囲 `[['00adac84', '00adac8b']]`
  - `FALL_THROUGH` [`00adac88`](#insn-00adac88) → [`00adac8c`](#insn-00adac8c)
- ブロック [`00adac8c`](#insn-00adac8c) 範囲 `[['00adac8c', '00adac93']]`
  - `CONDITIONAL_JUMP` [`00adac90`](#insn-00adac90) → [`00adacc4`](#insn-00adacc4)
  - `FALL_THROUGH` [`00adac90`](#insn-00adac90) → [`00adac94`](#insn-00adac94)
- ブロック [`00adac94`](#insn-00adac94) 範囲 `[['00adac94', '00adac97']]`
- ブロック [`00adacc4`](#insn-00adacc4) 範囲 `[['00adacc4', '00adacc7']]`

## 命令位置別の参照

- [`00adabf8`](#insn-00adabf8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adabfc`](#insn-00adabfc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adac00`](#insn-00adac00) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adac14`](#insn-00adac14) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adac18`](#insn-00adac18) → `0109ffb0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adac1c`](#insn-00adac1c) → [`00adac60`](#insn-00adac60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adac2c`](#insn-00adac2c) → [`00566a7c`](../00566/00566a7c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00566a7c` · 推定シンボル `None` · 推定型 `None`
- [`00adac30`](#insn-00adac30) → `0109ffb0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adac34`](#insn-00adac34) → `Stack[-0x3c]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adac38`](#insn-00adac38) → [`00adac84`](#insn-00adac84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adac50`](#insn-00adac50) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adac54`](#insn-00adac54) → [`00adac60`](#insn-00adac60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adac58`](#insn-00adac58) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adac5c`](#insn-00adac5c) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00adac64`](#insn-00adac64) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adac6c`](#insn-00adac6c) → [`00adacc4`](#insn-00adacc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adac70`](#insn-00adac70) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adac74`](#insn-00adac74) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adac78`](#insn-00adac78) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adac88`](#insn-00adac88) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adac90`](#insn-00adac90) → [`00adacc4`](#insn-00adacc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adac94`](#insn-00adac94) → [`00436e9c`](../00436/00436e9c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00436e9c` · 推定シンボル `None` · 推定型 `None`
- [`00adacc4`](#insn-00adacc4) → [`00bdb040`](../00bdb/00bdb040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb040` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00adabf8`](#insn-00adabf8)

~~~json
{
  "source": "00adabf8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adabfc`](#insn-00adabfc)

~~~json
{
  "source": "00adabfc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adac00`](#insn-00adac00)

~~~json
{
  "source": "00adac00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adac14`](#insn-00adac14)

~~~json
{
  "source": "00adac14",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adac18`](#insn-00adac18)

~~~json
{
  "source": "00adac18",
  "target": "0109ffb0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109ffb0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adac1c`](#insn-00adac1c)

~~~json
{
  "source": "00adac1c",
  "target": "00adac60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adac2c`](#insn-00adac2c)

~~~json
{
  "source": "00adac2c",
  "target": "00566a7c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adac30`](#insn-00adac30)

~~~json
{
  "source": "00adac30",
  "target": "0109ffb0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109ffb0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adac34`](#insn-00adac34)

~~~json
{
  "source": "00adac34",
  "target": "Stack[-0x3c]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adac38`](#insn-00adac38)

~~~json
{
  "source": "00adac38",
  "target": "00adac84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adac50`](#insn-00adac50)

~~~json
{
  "source": "00adac50",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adac54`](#insn-00adac54)

~~~json
{
  "source": "00adac54",
  "target": "00adac60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adac58`](#insn-00adac58)

~~~json
{
  "source": "00adac58",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adac5c`](#insn-00adac5c)

~~~json
{
  "source": "00adac5c",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adac64`](#insn-00adac64)

~~~json
{
  "source": "00adac64",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adac6c`](#insn-00adac6c)

~~~json
{
  "source": "00adac6c",
  "target": "00adacc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adac70`](#insn-00adac70)

~~~json
{
  "source": "00adac70",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adac74`](#insn-00adac74)

~~~json
{
  "source": "00adac74",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adac78`](#insn-00adac78)

~~~json
{
  "source": "00adac78",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adac88`](#insn-00adac88)

~~~json
{
  "source": "00adac88",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adac90`](#insn-00adac90)

~~~json
{
  "source": "00adac90",
  "target": "00adacc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adac94`](#insn-00adac94)

~~~json
{
  "source": "00adac94",
  "target": "00436e9c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adacc4`](#insn-00adacc4)

~~~json
{
  "source": "00adacc4",
  "target": "00bdb040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
