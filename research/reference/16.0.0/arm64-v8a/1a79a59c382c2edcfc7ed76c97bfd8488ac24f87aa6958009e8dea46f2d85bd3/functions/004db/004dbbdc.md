# 004dbbdc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `004b8d44`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b8/004b8d44.md) · 移動量 `+0x22e98`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0009.md#compare-3c121b51fe0f33b0771e4292ba3fdc1e)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `004dbc1c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004db/004dbc1c.md) · 移動量 `+0x40`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0009.md#compare-284ec9582ed41e5183061be5be372c30)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "004dbbdc",
  "name": "_ZN5Botan3lcmERKNS_6BigIntES2_",
  "size": 216,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "72dd29224750ccfbc8b32a005b1c9dc4d36b8f4857cea4a56f97d2a5e5c150e0",
  "source_text_sha256": "72dd29224750ccfbc8b32a005b1c9dc4d36b8f4857cea4a56f97d2a5e5c150e0",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "004dbbdc",
        "004dbcaf"
      ],
      [
        "004dbcec",
        "004dbcef"
      ]
    ],
    "bytes_sha256": "6ca48cee0fb715321c01071de184ff7b12548f55c9205eb474482d550b31360a",
    "instruction_count": 54,
    "instruction_bytes": 216,
    "body_bytes": 216,
    "indirect": 2,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c58f90](../00c58/00c58f90.md)

## 呼び出し先

- [00c57ae0](../00c57/00c57ae0.md)
- [00c58260](../00c58/00c58260.md)
- [00c58850](../00c58/00c58850.md)
- [00c58890](../00c58/00c58890.md)
- [00c58f60](../00c58/00c58f60.md)
- [0112a058](../0112a/0112a058.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 922 bytes

~~~c

void _ZN5Botan3lcmERKNS_6BigIntES2_(undefined8 param_1,undefined8 param_2,undefined8 param_3)

{
  long lVar1;
  void *local_78;
  void *local_70;
  long local_68;
  void *local_58;
  void *local_50;
  long local_48;
  long local_38;
  
  lVar1 = tpidr_el0;
  local_38 = *(long *)(lVar1 + 0x28);
  _ZN5BotanmlERKNS_6BigIntES2_(&local_58);
  _ZN5Botan3gcdERKNS_6BigIntES2_(&local_78,param_2,param_3);
  _ZN5BotandvERKNS_6BigIntES2_(param_1,&local_58,&local_78);
  if (local_78 != (void *)0x0) {
    local_70 = local_78;
    (*(code *)PTR_memset_00c67338)(local_78,0,local_68 - (long)local_78);
    free(local_78);
  }
  if (local_58 != (void *)0x0) {
    local_50 = local_58;
    (*(code *)PTR_memset_00c67338)(local_58,0,local_48 - (long)local_58);
    free(local_58);
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
<a id="insn-004dbbdc"></a> `004dbbdc` | `ff 03 02 d1` | sub sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-004dbbe0"></a> `004dbbe0` | `fd 7b 05 a9` | stp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-004dbbe4"></a> `004dbbe4` | `f6 57 06 a9` | stp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-004dbbe8"></a> `004dbbe8` | `f4 4f 07 a9` | stp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-004dbbec"></a> `004dbbec` | `fd 43 01 91` | add x29,sp,#0x50 | `FALL_THROUGH`
<a id="insn-004dbbf0"></a> `004dbbf0` | `56 d0 3b d5` | mrs x22,tpidr_el0 | `FALL_THROUGH`
<a id="insn-004dbbf4"></a> `004dbbf4` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-004dbbf8"></a> `004dbbf8` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-004dbbfc"></a> `004dbbfc` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-004dbc00"></a> `004dbc00` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-004dbc04"></a> `004dbc04` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-004dbc08"></a> `004dbc08` | `e8 a3 00 91` | add x8,sp,#0x28 | `FALL_THROUGH`
<a id="insn-004dbc0c"></a> `004dbc0c` | `11 f3 1d 94` | bl 0x00c58850 | `UNCONDITIONAL_CALL`
<a id="insn-004dbc10"></a> `004dbc10` | `e8 23 00 91` | add x8,sp,#0x8 | `FALL_THROUGH`
<a id="insn-004dbc14"></a> `004dbc14` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-004dbc18"></a> `004dbc18` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-004dbc1c"></a> `004dbc1c` | `d1 f4 1d 94` | bl 0x00c58f60 | `UNCONDITIONAL_CALL`
<a id="insn-004dbc20"></a> `004dbc20` | `e0 a3 00 91` | add x0,sp,#0x28 | `FALL_THROUGH`
<a id="insn-004dbc24"></a> `004dbc24` | `e1 23 00 91` | add x1,sp,#0x8 | `FALL_THROUGH`
<a id="insn-004dbc28"></a> `004dbc28` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-004dbc2c"></a> `004dbc2c` | `19 f3 1d 94` | bl 0x00c58890 | `UNCONDITIONAL_CALL`
<a id="insn-004dbc30"></a> `004dbc30` | `f3 07 40 f9` | ldr x19,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-004dbc34"></a> `004dbc34` | `74 3c 00 90` | adrp x20,0xc67000 | `FALL_THROUGH`
<a id="insn-004dbc38"></a> `004dbc38` | `53 01 00 b4` | cbz x19,0x004dbc60 | `CONDITIONAL_JUMP`
<a id="insn-004dbc3c"></a> `004dbc3c` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-004dbc40"></a> `004dbc40` | `e8 0f 40 f9` | ldr x8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-004dbc44"></a> `004dbc44` | `89 9e 41 f9` | ldr x9,[x20, #0x338] | `FALL_THROUGH`
<a id="insn-004dbc48"></a> `004dbc48` | `02 01 13 cb` | sub x2,x8,x19 | `FALL_THROUGH`
<a id="insn-004dbc4c"></a> `004dbc4c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-004dbc50"></a> `004dbc50` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-004dbc54"></a> `004dbc54` | `20 01 3f d6` | blr x9 | `COMPUTED_CALL`
<a id="insn-004dbc58"></a> `004dbc58` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-004dbc5c"></a> `004dbc5c` | `81 f1 1d 94` | bl 0x00c58260 | `UNCONDITIONAL_CALL`
<a id="insn-004dbc60"></a> `004dbc60` | `f3 17 40 f9` | ldr x19,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-004dbc64"></a> `004dbc64` | `53 01 00 b4` | cbz x19,0x004dbc8c | `CONDITIONAL_JUMP`
<a id="insn-004dbc68"></a> `004dbc68` | `f3 1b 00 f9` | str x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-004dbc6c"></a> `004dbc6c` | `e8 1f 40 f9` | ldr x8,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-004dbc70"></a> `004dbc70` | `89 9e 41 f9` | ldr x9,[x20, #0x338] | `FALL_THROUGH`
<a id="insn-004dbc74"></a> `004dbc74` | `02 01 13 cb` | sub x2,x8,x19 | `FALL_THROUGH`
<a id="insn-004dbc78"></a> `004dbc78` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-004dbc7c"></a> `004dbc7c` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-004dbc80"></a> `004dbc80` | `20 01 3f d6` | blr x9 | `COMPUTED_CALL`
<a id="insn-004dbc84"></a> `004dbc84` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-004dbc88"></a> `004dbc88` | `76 f1 1d 94` | bl 0x00c58260 | `UNCONDITIONAL_CALL`
<a id="insn-004dbc8c"></a> `004dbc8c` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-004dbc90"></a> `004dbc90` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-004dbc94"></a> `004dbc94` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-004dbc98"></a> `004dbc98` | `a1 02 00 54` | b.ne 0x004dbcec | `CONDITIONAL_JUMP`
<a id="insn-004dbc9c"></a> `004dbc9c` | `f4 4f 47 a9` | ldp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-004dbca0"></a> `004dbca0` | `f6 57 46 a9` | ldp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-004dbca4"></a> `004dbca4` | `fd 7b 45 a9` | ldp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-004dbca8"></a> `004dbca8` | `ff 03 02 91` | add sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-004dbcac"></a> `004dbcac` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-004dbcec"></a> `004dbcec` | `7d ef 1d 94` | bl 0x00c57ae0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`004dbbdc`](#insn-004dbbdc) 範囲 `[['004dbbdc', '004dbc3b']]`
  - `CONDITIONAL_JUMP` [`004dbc38`](#insn-004dbc38) → [`004dbc60`](#insn-004dbc60)
  - `FALL_THROUGH` [`004dbc38`](#insn-004dbc38) → [`004dbc3c`](#insn-004dbc3c)
- ブロック [`004dbc3c`](#insn-004dbc3c) 範囲 `[['004dbc3c', '004dbc5f']]`
  - `FALL_THROUGH` [`004dbc5c`](#insn-004dbc5c) → [`004dbc60`](#insn-004dbc60)
- ブロック [`004dbc60`](#insn-004dbc60) 範囲 `[['004dbc60', '004dbc67']]`
  - `CONDITIONAL_JUMP` [`004dbc64`](#insn-004dbc64) → [`004dbc8c`](#insn-004dbc8c)
  - `FALL_THROUGH` [`004dbc64`](#insn-004dbc64) → [`004dbc68`](#insn-004dbc68)
- ブロック [`004dbc68`](#insn-004dbc68) 範囲 `[['004dbc68', '004dbc8b']]`
  - `FALL_THROUGH` [`004dbc88`](#insn-004dbc88) → [`004dbc8c`](#insn-004dbc8c)
- ブロック [`004dbc8c`](#insn-004dbc8c) 範囲 `[['004dbc8c', '004dbc9b']]`
  - `CONDITIONAL_JUMP` [`004dbc98`](#insn-004dbc98) → [`004dbcec`](#insn-004dbcec)
  - `FALL_THROUGH` [`004dbc98`](#insn-004dbc98) → [`004dbc9c`](#insn-004dbc9c)
- ブロック [`004dbc9c`](#insn-004dbc9c) 範囲 `[['004dbc9c', '004dbcaf']]`
- ブロック [`004dbcec`](#insn-004dbcec) 範囲 `[['004dbcec', '004dbcef']]`

## 命令位置別の参照

- [`004dbbe0`](#insn-004dbbe0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dbbe4`](#insn-004dbbe4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dbbe8`](#insn-004dbbe8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dbc04`](#insn-004dbc04) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dbc0c`](#insn-004dbc0c) → [`00c58850`](../00c58/00c58850.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58850` · 推定シンボル `None` · 推定型 `None`
- [`004dbc1c`](#insn-004dbc1c) → [`00c58f60`](../00c58/00c58f60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f60` · 推定シンボル `None` · 推定型 `None`
- [`004dbc2c`](#insn-004dbc2c) → [`00c58890`](../00c58/00c58890.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58890` · 推定シンボル `None` · 推定型 `None`
- [`004dbc30`](#insn-004dbc30) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dbc38`](#insn-004dbc38) → [`004dbc60`](#insn-004dbc60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dbc3c`](#insn-004dbc3c) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dbc40`](#insn-004dbc40) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dbc44`](#insn-004dbc44) → `00c67338`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004dbc54`](#insn-004dbc54) → [`0112a058`](../0112a/0112a058.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `0112a058` · 推定シンボル `None` · 推定型 `None`
- [`004dbc5c`](#insn-004dbc5c) → [`00c58260`](../00c58/00c58260.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58260` · 推定シンボル `None` · 推定型 `None`
- [`004dbc60`](#insn-004dbc60) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dbc64`](#insn-004dbc64) → [`004dbc8c`](#insn-004dbc8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dbc68`](#insn-004dbc68) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dbc6c`](#insn-004dbc6c) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dbc70`](#insn-004dbc70) → `00c67338`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004dbc80`](#insn-004dbc80) → [`0112a058`](../0112a/0112a058.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `0112a058` · 推定シンボル `None` · 推定型 `None`
- [`004dbc88`](#insn-004dbc88) → [`00c58260`](../00c58/00c58260.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58260` · 推定シンボル `None` · 推定型 `None`
- [`004dbc90`](#insn-004dbc90) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dbc98`](#insn-004dbc98) → [`004dbcec`](#insn-004dbcec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dbc9c`](#insn-004dbc9c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dbca0`](#insn-004dbca0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dbca4`](#insn-004dbca4) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004dbcec`](#insn-004dbcec) → [`00c57ae0`](../00c57/00c57ae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ae0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`004dbbe0`](#insn-004dbbe0)

~~~json
{
  "source": "004dbbe0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dbbe4`](#insn-004dbbe4)

~~~json
{
  "source": "004dbbe4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dbbe8`](#insn-004dbbe8)

~~~json
{
  "source": "004dbbe8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dbc04`](#insn-004dbc04)

~~~json
{
  "source": "004dbc04",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dbc0c`](#insn-004dbc0c)

~~~json
{
  "source": "004dbc0c",
  "target": "00c58850",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004dbc1c`](#insn-004dbc1c)

~~~json
{
  "source": "004dbc1c",
  "target": "00c58f60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004dbc2c`](#insn-004dbc2c)

~~~json
{
  "source": "004dbc2c",
  "target": "00c58890",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004dbc30`](#insn-004dbc30)

~~~json
{
  "source": "004dbc30",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dbc38`](#insn-004dbc38)

~~~json
{
  "source": "004dbc38",
  "target": "004dbc60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dbc3c`](#insn-004dbc3c)

~~~json
{
  "source": "004dbc3c",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dbc40`](#insn-004dbc40)

~~~json
{
  "source": "004dbc40",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dbc44`](#insn-004dbc44)

~~~json
{
  "source": "004dbc44",
  "target": "00c67338",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c67338",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004dbc54`](#insn-004dbc54)

~~~json
{
  "source": "004dbc54",
  "target": "0112a058",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004dbc5c`](#insn-004dbc5c)

~~~json
{
  "source": "004dbc5c",
  "target": "00c58260",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004dbc60`](#insn-004dbc60)

~~~json
{
  "source": "004dbc60",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dbc64`](#insn-004dbc64)

~~~json
{
  "source": "004dbc64",
  "target": "004dbc8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dbc68`](#insn-004dbc68)

~~~json
{
  "source": "004dbc68",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dbc6c`](#insn-004dbc6c)

~~~json
{
  "source": "004dbc6c",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dbc70`](#insn-004dbc70)

~~~json
{
  "source": "004dbc70",
  "target": "00c67338",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c67338",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004dbc80`](#insn-004dbc80)

~~~json
{
  "source": "004dbc80",
  "target": "0112a058",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004dbc88`](#insn-004dbc88)

~~~json
{
  "source": "004dbc88",
  "target": "00c58260",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004dbc90`](#insn-004dbc90)

~~~json
{
  "source": "004dbc90",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dbc98`](#insn-004dbc98)

~~~json
{
  "source": "004dbc98",
  "target": "004dbcec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dbc9c`](#insn-004dbc9c)

~~~json
{
  "source": "004dbc9c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dbca0`](#insn-004dbca0)

~~~json
{
  "source": "004dbca0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dbca4`](#insn-004dbca4)

~~~json
{
  "source": "004dbca4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004dbcec`](#insn-004dbcec)

~~~json
{
  "source": "004dbcec",
  "target": "00c57ae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
