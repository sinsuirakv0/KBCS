# 00ad6cbc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00ad6c78`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad6/00ad6c78.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0060.md#compare-3e466af34811ab1f44532edee0fec0a5)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b36694`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b36/00b36694.md) · 移動量 `+0x5f9d8`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0054.md#compare-b2b12195f753ce01c67aebbb43be07dd)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ad6cbc",
  "name": "FUN_00ad6cbc",
  "size": 200,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "77d516ce3fa9a5f3bb0b7e53db8c3df7136093a5fb7d2df579acd6cfc776d686",
  "source_text_sha256": "77d516ce3fa9a5f3bb0b7e53db8c3df7136093a5fb7d2df579acd6cfc776d686",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ad6cbc",
        "00ad6d83"
      ]
    ],
    "bytes_sha256": "3294bcebb6d1942d76d3b142cf0227b03cf9d6f3d3654a3615f0d0e5dde058d4",
    "instruction_count": 50,
    "instruction_bytes": 200,
    "body_bytes": 200,
    "indirect": 3,
    "unresolved": 3
  }
}
~~~

## 呼び出し元

- [0058cea4](../0058c/0058cea4.md)

## 呼び出し先

- [00ad4a94](../00ad4/00ad4a94.md)
- [00bdb090](../00bdb/00bdb090.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 914 bytes

~~~c

void FUN_00ad6cbc(long *param_1)

{
  long lVar1;
  long *plVar2;
  long *plVar3;
  long lVar4;
  long local_60 [4];
  long *local_40;
  long local_28;
  
  local_40 = local_60;
  plVar2 = local_60;
  lVar1 = tpidr_el0;
  local_28 = *(long *)(lVar1 + 0x28);
  plVar3 = (long *)param_1[4];
  if (plVar3 == (long *)0x0) {
    local_40 = (long *)0x0;
  }
  else if (plVar3 == param_1) {
    (**(code **)(*param_1 + 0x18))(param_1,local_60);
  }
  else {
    local_40 = (long *)(**(code **)(*plVar3 + 0x10))(plVar3);
  }
  FUN_00ad4a94(local_60,&DAT_0109fda0);
  if (local_40 == local_60) {
    lVar4 = 0x20;
  }
  else {
    if (local_40 == (long *)0x0) goto LAB_00ad6d60;
    lVar4 = 0x28;
    plVar2 = local_40;
  }
  (**(code **)(*plVar2 + lVar4))();
LAB_00ad6d60:
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
<a id="insn-00ad6cbc"></a> `00ad6cbc` | `ff 83 01 d1` | sub sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00ad6cc0"></a> `00ad6cc0` | `fd 7b 04 a9` | stp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00ad6cc4"></a> `00ad6cc4` | `f4 4f 05 a9` | stp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00ad6cc8"></a> `00ad6cc8` | `fd 03 01 91` | add x29,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00ad6ccc"></a> `00ad6ccc` | `53 d0 3b d5` | mrs x19,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00ad6cd0"></a> `00ad6cd0` | `68 16 40 f9` | ldr x8,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00ad6cd4"></a> `00ad6cd4` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00ad6cd8"></a> `00ad6cd8` | `08 10 40 f9` | ldr x8,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00ad6cdc"></a> `00ad6cdc` | `28 01 00 b4` | cbz x8,0x00ad6d00 | `CONDITIONAL_JUMP`
<a id="insn-00ad6ce0"></a> `00ad6ce0` | `1f 01 00 eb` | cmp x8,x0 | `FALL_THROUGH`
<a id="insn-00ad6ce4"></a> `00ad6ce4` | `20 01 00 54` | b.eq 0x00ad6d08 | `CONDITIONAL_JUMP`
<a id="insn-00ad6ce8"></a> `00ad6ce8` | `09 01 40 f9` | ldr x9,[x8] | `FALL_THROUGH`
<a id="insn-00ad6cec"></a> `00ad6cec` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00ad6cf0"></a> `00ad6cf0` | `29 09 40 f9` | ldr x9,[x9, #0x10] | `FALL_THROUGH`
<a id="insn-00ad6cf4"></a> `00ad6cf4` | `20 01 3f d6` | blr x9 | `COMPUTED_CALL`
<a id="insn-00ad6cf8"></a> `00ad6cf8` | `e0 13 00 f9` | str x0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ad6cfc"></a> `00ad6cfc` | `09 00 00 14` | b 0x00ad6d20 | `UNCONDITIONAL_JUMP`
<a id="insn-00ad6d00"></a> `00ad6d00` | `ff 13 00 f9` | str xzr,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ad6d04"></a> `00ad6d04` | `07 00 00 14` | b 0x00ad6d20 | `UNCONDITIONAL_JUMP`
<a id="insn-00ad6d08"></a> `00ad6d08` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00ad6d0c"></a> `00ad6d0c` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-00ad6d10"></a> `00ad6d10` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00ad6d14"></a> `00ad6d14` | `e8 13 00 f9` | str x8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ad6d18"></a> `00ad6d18` | `28 0d 40 f9` | ldr x8,[x9, #0x18] | `FALL_THROUGH`
<a id="insn-00ad6d1c"></a> `00ad6d1c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ad6d20"></a> `00ad6d20` | `41 2e 00 b0` | adrp x1,0x109f000 | `FALL_THROUGH`
<a id="insn-00ad6d24"></a> `00ad6d24` | `21 80 36 91` | add x1,x1,#0xda0 | `FALL_THROUGH`
<a id="insn-00ad6d28"></a> `00ad6d28` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00ad6d2c"></a> `00ad6d2c` | `f4 03 00 91` | mov x20,sp | `FALL_THROUGH`
<a id="insn-00ad6d30"></a> `00ad6d30` | `59 f7 ff 97` | bl 0x00ad4a94 | `UNCONDITIONAL_CALL`
<a id="insn-00ad6d34"></a> `00ad6d34` | `e0 13 40 f9` | ldr x0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ad6d38"></a> `00ad6d38` | `1f 00 14 eb` | cmp x0,x20 | `FALL_THROUGH`
<a id="insn-00ad6d3c"></a> `00ad6d3c` | `80 00 00 54` | b.eq 0x00ad6d4c | `CONDITIONAL_JUMP`
<a id="insn-00ad6d40"></a> `00ad6d40` | `00 01 00 b4` | cbz x0,0x00ad6d60 | `CONDITIONAL_JUMP`
<a id="insn-00ad6d44"></a> `00ad6d44` | `08 05 80 52` | mov w8,#0x28 | `FALL_THROUGH`
<a id="insn-00ad6d48"></a> `00ad6d48` | `03 00 00 14` | b 0x00ad6d54 | `UNCONDITIONAL_JUMP`
<a id="insn-00ad6d4c"></a> `00ad6d4c` | `08 04 80 52` | mov w8,#0x20 | `FALL_THROUGH`
<a id="insn-00ad6d50"></a> `00ad6d50` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00ad6d54"></a> `00ad6d54` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-00ad6d58"></a> `00ad6d58` | `28 69 68 f8` | ldr x8,[x9, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ad6d5c"></a> `00ad6d5c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ad6d60"></a> `00ad6d60` | `68 16 40 f9` | ldr x8,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00ad6d64"></a> `00ad6d64` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00ad6d68"></a> `00ad6d68` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00ad6d6c"></a> `00ad6d6c` | `a1 00 00 54` | b.ne 0x00ad6d80 | `CONDITIONAL_JUMP`
<a id="insn-00ad6d70"></a> `00ad6d70` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00ad6d74"></a> `00ad6d74` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00ad6d78"></a> `00ad6d78` | `ff 83 01 91` | add sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00ad6d7c"></a> `00ad6d7c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00ad6d80"></a> `00ad6d80` | `c4 10 04 94` | bl 0x00bdb090 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00ad6cbc`](#insn-00ad6cbc) 範囲 `[['00ad6cbc', '00ad6cdf']]`
  - `CONDITIONAL_JUMP` [`00ad6cdc`](#insn-00ad6cdc) → [`00ad6d00`](#insn-00ad6d00)
  - `FALL_THROUGH` [`00ad6cdc`](#insn-00ad6cdc) → [`00ad6ce0`](#insn-00ad6ce0)
- ブロック [`00ad6ce0`](#insn-00ad6ce0) 範囲 `[['00ad6ce0', '00ad6ce7']]`
  - `CONDITIONAL_JUMP` [`00ad6ce4`](#insn-00ad6ce4) → [`00ad6d08`](#insn-00ad6d08)
  - `FALL_THROUGH` [`00ad6ce4`](#insn-00ad6ce4) → [`00ad6ce8`](#insn-00ad6ce8)
- ブロック [`00ad6ce8`](#insn-00ad6ce8) 範囲 `[['00ad6ce8', '00ad6cff']]`
  - `UNCONDITIONAL_JUMP` [`00ad6cfc`](#insn-00ad6cfc) → [`00ad6d20`](#insn-00ad6d20)
- ブロック [`00ad6d00`](#insn-00ad6d00) 範囲 `[['00ad6d00', '00ad6d07']]`
  - `UNCONDITIONAL_JUMP` [`00ad6d04`](#insn-00ad6d04) → [`00ad6d20`](#insn-00ad6d20)
- ブロック [`00ad6d08`](#insn-00ad6d08) 範囲 `[['00ad6d08', '00ad6d1f']]`
  - `FALL_THROUGH` [`00ad6d1c`](#insn-00ad6d1c) → [`00ad6d20`](#insn-00ad6d20)
- ブロック [`00ad6d20`](#insn-00ad6d20) 範囲 `[['00ad6d20', '00ad6d3f']]`
  - `CONDITIONAL_JUMP` [`00ad6d3c`](#insn-00ad6d3c) → [`00ad6d4c`](#insn-00ad6d4c)
  - `FALL_THROUGH` [`00ad6d3c`](#insn-00ad6d3c) → [`00ad6d40`](#insn-00ad6d40)
- ブロック [`00ad6d40`](#insn-00ad6d40) 範囲 `[['00ad6d40', '00ad6d43']]`
  - `CONDITIONAL_JUMP` [`00ad6d40`](#insn-00ad6d40) → [`00ad6d60`](#insn-00ad6d60)
  - `FALL_THROUGH` [`00ad6d40`](#insn-00ad6d40) → [`00ad6d44`](#insn-00ad6d44)
- ブロック [`00ad6d44`](#insn-00ad6d44) 範囲 `[['00ad6d44', '00ad6d4b']]`
  - `UNCONDITIONAL_JUMP` [`00ad6d48`](#insn-00ad6d48) → [`00ad6d54`](#insn-00ad6d54)
- ブロック [`00ad6d4c`](#insn-00ad6d4c) 範囲 `[['00ad6d4c', '00ad6d53']]`
  - `FALL_THROUGH` [`00ad6d50`](#insn-00ad6d50) → [`00ad6d54`](#insn-00ad6d54)
- ブロック [`00ad6d54`](#insn-00ad6d54) 範囲 `[['00ad6d54', '00ad6d5f']]`
  - `FALL_THROUGH` [`00ad6d5c`](#insn-00ad6d5c) → [`00ad6d60`](#insn-00ad6d60)
- ブロック [`00ad6d60`](#insn-00ad6d60) 範囲 `[['00ad6d60', '00ad6d6f']]`
  - `CONDITIONAL_JUMP` [`00ad6d6c`](#insn-00ad6d6c) → [`00ad6d80`](#insn-00ad6d80)
  - `FALL_THROUGH` [`00ad6d6c`](#insn-00ad6d6c) → [`00ad6d70`](#insn-00ad6d70)
- ブロック [`00ad6d70`](#insn-00ad6d70) 範囲 `[['00ad6d70', '00ad6d7f']]`
- ブロック [`00ad6d80`](#insn-00ad6d80) 範囲 `[['00ad6d80', '00ad6d83']]`

## 命令位置別の参照

- [`00ad6cc0`](#insn-00ad6cc0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad6cc4`](#insn-00ad6cc4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad6cd4`](#insn-00ad6cd4) → `Stack[-0x28]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad6cdc`](#insn-00ad6cdc) → [`00ad6d00`](#insn-00ad6d00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad6ce4`](#insn-00ad6ce4) → [`00ad6d08`](#insn-00ad6d08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad6cf8`](#insn-00ad6cf8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad6cfc`](#insn-00ad6cfc) → [`00ad6d20`](#insn-00ad6d20) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad6d00`](#insn-00ad6d00) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad6d04`](#insn-00ad6d04) → [`00ad6d20`](#insn-00ad6d20) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad6d14`](#insn-00ad6d14) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad6d24`](#insn-00ad6d24) → `0109fda0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad6d30`](#insn-00ad6d30) → [`00ad4a94`](../00ad4/00ad4a94.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ad4a94` · 推定シンボル `None` · 推定型 `None`
- [`00ad6d34`](#insn-00ad6d34) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad6d3c`](#insn-00ad6d3c) → [`00ad6d4c`](#insn-00ad6d4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad6d40`](#insn-00ad6d40) → [`00ad6d60`](#insn-00ad6d60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad6d48`](#insn-00ad6d48) → [`00ad6d54`](#insn-00ad6d54) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad6d54`](#insn-00ad6d54) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad6d64`](#insn-00ad6d64) → `Stack[-0x28]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad6d6c`](#insn-00ad6d6c) → [`00ad6d80`](#insn-00ad6d80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad6d70`](#insn-00ad6d70) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad6d74`](#insn-00ad6d74) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad6d80`](#insn-00ad6d80) → [`00bdb090`](../00bdb/00bdb090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb090` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00ad6cc0`](#insn-00ad6cc0)

~~~json
{
  "source": "00ad6cc0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad6cc4`](#insn-00ad6cc4)

~~~json
{
  "source": "00ad6cc4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad6cd4`](#insn-00ad6cd4)

~~~json
{
  "source": "00ad6cd4",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad6cdc`](#insn-00ad6cdc)

~~~json
{
  "source": "00ad6cdc",
  "target": "00ad6d00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad6ce4`](#insn-00ad6ce4)

~~~json
{
  "source": "00ad6ce4",
  "target": "00ad6d08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad6cf8`](#insn-00ad6cf8)

~~~json
{
  "source": "00ad6cf8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad6cfc`](#insn-00ad6cfc)

~~~json
{
  "source": "00ad6cfc",
  "target": "00ad6d20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad6d00`](#insn-00ad6d00)

~~~json
{
  "source": "00ad6d00",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad6d04`](#insn-00ad6d04)

~~~json
{
  "source": "00ad6d04",
  "target": "00ad6d20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad6d14`](#insn-00ad6d14)

~~~json
{
  "source": "00ad6d14",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad6d24`](#insn-00ad6d24)

~~~json
{
  "source": "00ad6d24",
  "target": "0109fda0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad6d30`](#insn-00ad6d30)

~~~json
{
  "source": "00ad6d30",
  "target": "00ad4a94",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad6d34`](#insn-00ad6d34)

~~~json
{
  "source": "00ad6d34",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad6d3c`](#insn-00ad6d3c)

~~~json
{
  "source": "00ad6d3c",
  "target": "00ad6d4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad6d40`](#insn-00ad6d40)

~~~json
{
  "source": "00ad6d40",
  "target": "00ad6d60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad6d48`](#insn-00ad6d48)

~~~json
{
  "source": "00ad6d48",
  "target": "00ad6d54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad6d54`](#insn-00ad6d54)

~~~json
{
  "source": "00ad6d54",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad6d64`](#insn-00ad6d64)

~~~json
{
  "source": "00ad6d64",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad6d6c`](#insn-00ad6d6c)

~~~json
{
  "source": "00ad6d6c",
  "target": "00ad6d80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad6d70`](#insn-00ad6d70)

~~~json
{
  "source": "00ad6d70",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad6d74`](#insn-00ad6d74)

~~~json
{
  "source": "00ad6d74",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad6d80`](#insn-00ad6d80)

~~~json
{
  "source": "00ad6d80",
  "target": "00bdb090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
