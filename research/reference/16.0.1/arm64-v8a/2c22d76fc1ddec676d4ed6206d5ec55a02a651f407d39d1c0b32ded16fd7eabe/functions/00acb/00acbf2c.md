# 00acbf2c

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00acbd30`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acbd30.md) · 移動量 `+0x1fc`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0035.md#compare-e046a5cf660bb26f513d9a8e88783459)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00acbf9c`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acb/00acbf9c.md) · 移動量 `+0x70`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0034.md#compare-7d57a8ede36054e241b968350c8b1402)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acbf2c",
  "name": "FUN_00acbf2c",
  "size": 200,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "584d98049768cd3e608ed0ef0eb70492bc41d2b7b1fcb4a95c53468c533cabf4",
  "source_text_sha256": "584d98049768cd3e608ed0ef0eb70492bc41d2b7b1fcb4a95c53468c533cabf4",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00acbf2c",
        "00acbfef"
      ],
      [
        "00acc014",
        "00acc017"
      ]
    ],
    "bytes_sha256": "7a11687b181acdbd94f28ebe014e53162815f33bd26d5d4fd544fcf14f9b8421",
    "instruction_count": 50,
    "instruction_bytes": 200,
    "body_bytes": 200,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

- [009b96e4](../009b9/009b96e4.md)
- [00acbf2c](../00acb/00acbf2c.md)

## 呼び出し先

- [00acbf2c](../00acb/00acbf2c.md)
- [00c53cd0](../00c53/00c53cd0.md)
- [00c53d00](../00c53/00c53d00.md)
- [00c57e80](../00c57/00c57e80.md)
- [00c57ee0](../00c57/00c57ee0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 951 bytes

~~~c

void FUN_00acbf2c(long param_1,byte param_2)

{
  undefined8 *puVar1;
  undefined8 uVar2;
  undefined8 *puVar3;
  long *plVar4;
  long lVar5;
  long lVar6;
  long lVar7;
  
  lVar5 = tpidr_el0;
  lVar7 = *(long *)(lVar5 + 0x28);
  puVar1 = *(undefined8 **)(param_1 + 0x40);
  puVar3 = *(undefined8 **)(param_1 + 0x48);
  *(byte *)(param_1 + 0x28) = param_2;
  for (; puVar1 != puVar3; puVar1 = puVar1 + 2) {
    uVar2 = *puVar1;
    plVar4 = (long *)puVar1[1];
    if (plVar4 != (long *)0x0) {
      FUN_00c53cd0(1,plVar4 + 1);
    }
    FUN_00acbf2c(uVar2,param_2 & 1);
    if ((plVar4 != (long *)0x0) && (lVar6 = FUN_00c53d00(0xffffffffffffffff,plVar4 + 1), lVar6 == 0)
       ) {
      (**(code **)(*plVar4 + 0x10))(plVar4);
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar4);
    }
  }
  if (*(long *)(lVar5 + 0x28) == lVar7) {
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
<a id="insn-00acbf2c"></a> `00acbf2c` | `ff 83 01 d1` | sub sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00acbf30"></a> `00acbf30` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00acbf34"></a> `00acbf34` | `f8 5f 03 a9` | stp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00acbf38"></a> `00acbf38` | `f6 57 04 a9` | stp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00acbf3c"></a> `00acbf3c` | `f4 4f 05 a9` | stp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00acbf40"></a> `00acbf40` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00acbf44"></a> `00acbf44` | `56 d0 3b d5` | mrs x22,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00acbf48"></a> `00acbf48` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00acbf4c"></a> `00acbf4c` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00acbf50"></a> `00acbf50` | `17 60 44 a9` | ldp x23,x24,[x0, #0x40] | `FALL_THROUGH`
<a id="insn-00acbf54"></a> `00acbf54` | `01 a0 00 39` | strb w1,[x0, #0x28] | `FALL_THROUGH`
<a id="insn-00acbf58"></a> `00acbf58` | `ff 02 18 eb` | cmp x23,x24 | `FALL_THROUGH`
<a id="insn-00acbf5c"></a> `00acbf5c` | `60 03 00 54` | b.eq 0x00acbfc8 | `CONDITIONAL_JUMP`
<a id="insn-00acbf60"></a> `00acbf60` | `f3 03 01 2a` | mov w19,w1 | `FALL_THROUGH`
<a id="insn-00acbf64"></a> `00acbf64` | `04 00 00 14` | b 0x00acbf74 | `UNCONDITIONAL_JUMP`
<a id="insn-00acbf68"></a> `00acbf68` | `f7 42 00 91` | add x23,x23,#0x10 | `FALL_THROUGH`
<a id="insn-00acbf6c"></a> `00acbf6c` | `ff 02 18 eb` | cmp x23,x24 | `FALL_THROUGH`
<a id="insn-00acbf70"></a> `00acbf70` | `c0 02 00 54` | b.eq 0x00acbfc8 | `CONDITIONAL_JUMP`
<a id="insn-00acbf74"></a> `00acbf74` | `f5 52 40 a9` | ldp x21,x20,[x23] | `FALL_THROUGH`
<a id="insn-00acbf78"></a> `00acbf78` | `f5 d3 00 a9` | stp x21,x20,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00acbf7c"></a> `00acbf7c` | `94 00 00 b4` | cbz x20,0x00acbf8c | `CONDITIONAL_JUMP`
<a id="insn-00acbf80"></a> `00acbf80` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00acbf84"></a> `00acbf84` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00acbf88"></a> `00acbf88` | `52 1f 06 94` | bl 0x00c53cd0 | `UNCONDITIONAL_CALL`
<a id="insn-00acbf8c"></a> `00acbf8c` | `61 02 00 12` | and w1,w19,#0x1 | `FALL_THROUGH`
<a id="insn-00acbf90"></a> `00acbf90` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00acbf94"></a> `00acbf94` | `e6 ff ff 97` | bl 0x00acbf2c | `UNCONDITIONAL_CALL`
<a id="insn-00acbf98"></a> `00acbf98` | `94 fe ff b4` | cbz x20,0x00acbf68 | `CONDITIONAL_JUMP`
<a id="insn-00acbf9c"></a> `00acbf9c` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00acbfa0"></a> `00acbfa0` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00acbfa4"></a> `00acbfa4` | `57 1f 06 94` | bl 0x00c53d00 | `UNCONDITIONAL_CALL`
<a id="insn-00acbfa8"></a> `00acbfa8` | `00 fe ff b5` | cbnz x0,0x00acbf68 | `CONDITIONAL_JUMP`
<a id="insn-00acbfac"></a> `00acbfac` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00acbfb0"></a> `00acbfb0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00acbfb4"></a> `00acbfb4` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00acbfb8"></a> `00acbfb8` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00acbfbc"></a> `00acbfbc` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00acbfc0"></a> `00acbfc0` | `b0 2f 06 94` | bl 0x00c57e80 | `UNCONDITIONAL_CALL`
<a id="insn-00acbfc4"></a> `00acbfc4` | `e9 ff ff 17` | b 0x00acbf68 | `UNCONDITIONAL_JUMP`
<a id="insn-00acbfc8"></a> `00acbfc8` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00acbfcc"></a> `00acbfcc` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00acbfd0"></a> `00acbfd0` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00acbfd4"></a> `00acbfd4` | `01 02 00 54` | b.ne 0x00acc014 | `CONDITIONAL_JUMP`
<a id="insn-00acbfd8"></a> `00acbfd8` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00acbfdc"></a> `00acbfdc` | `f6 57 44 a9` | ldp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00acbfe0"></a> `00acbfe0` | `f8 5f 43 a9` | ldp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00acbfe4"></a> `00acbfe4` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00acbfe8"></a> `00acbfe8` | `ff 83 01 91` | add sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00acbfec"></a> `00acbfec` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00acc014"></a> `00acc014` | `b3 2f 06 94` | bl 0x00c57ee0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00acbf2c`](#insn-00acbf2c) 範囲 `[['00acbf2c', '00acbf5f']]`
  - `CONDITIONAL_JUMP` [`00acbf5c`](#insn-00acbf5c) → [`00acbfc8`](#insn-00acbfc8)
  - `FALL_THROUGH` [`00acbf5c`](#insn-00acbf5c) → [`00acbf60`](#insn-00acbf60)
- ブロック [`00acbf60`](#insn-00acbf60) 範囲 `[['00acbf60', '00acbf67']]`
  - `UNCONDITIONAL_JUMP` [`00acbf64`](#insn-00acbf64) → [`00acbf74`](#insn-00acbf74)
- ブロック [`00acbf68`](#insn-00acbf68) 範囲 `[['00acbf68', '00acbf73']]`
  - `CONDITIONAL_JUMP` [`00acbf70`](#insn-00acbf70) → [`00acbfc8`](#insn-00acbfc8)
  - `FALL_THROUGH` [`00acbf70`](#insn-00acbf70) → [`00acbf74`](#insn-00acbf74)
- ブロック [`00acbf74`](#insn-00acbf74) 範囲 `[['00acbf74', '00acbf7f']]`
  - `CONDITIONAL_JUMP` [`00acbf7c`](#insn-00acbf7c) → [`00acbf8c`](#insn-00acbf8c)
  - `FALL_THROUGH` [`00acbf7c`](#insn-00acbf7c) → [`00acbf80`](#insn-00acbf80)
- ブロック [`00acbf80`](#insn-00acbf80) 範囲 `[['00acbf80', '00acbf8b']]`
  - `FALL_THROUGH` [`00acbf88`](#insn-00acbf88) → [`00acbf8c`](#insn-00acbf8c)
- ブロック [`00acbf8c`](#insn-00acbf8c) 範囲 `[['00acbf8c', '00acbf9b']]`
  - `CONDITIONAL_JUMP` [`00acbf98`](#insn-00acbf98) → [`00acbf68`](#insn-00acbf68)
  - `FALL_THROUGH` [`00acbf98`](#insn-00acbf98) → [`00acbf9c`](#insn-00acbf9c)
- ブロック [`00acbf9c`](#insn-00acbf9c) 範囲 `[['00acbf9c', '00acbfab']]`
  - `CONDITIONAL_JUMP` [`00acbfa8`](#insn-00acbfa8) → [`00acbf68`](#insn-00acbf68)
  - `FALL_THROUGH` [`00acbfa8`](#insn-00acbfa8) → [`00acbfac`](#insn-00acbfac)
- ブロック [`00acbfac`](#insn-00acbfac) 範囲 `[['00acbfac', '00acbfc7']]`
  - `UNCONDITIONAL_JUMP` [`00acbfc4`](#insn-00acbfc4) → [`00acbf68`](#insn-00acbf68)
- ブロック [`00acbfc8`](#insn-00acbfc8) 範囲 `[['00acbfc8', '00acbfd7']]`
  - `CONDITIONAL_JUMP` [`00acbfd4`](#insn-00acbfd4) → [`00acc014`](#insn-00acc014)
  - `FALL_THROUGH` [`00acbfd4`](#insn-00acbfd4) → [`00acbfd8`](#insn-00acbfd8)
- ブロック [`00acbfd8`](#insn-00acbfd8) 範囲 `[['00acbfd8', '00acbfef']]`
- ブロック [`00acc014`](#insn-00acc014) 範囲 `[['00acc014', '00acc017']]`

## 命令位置別の参照

- [`00acbf30`](#insn-00acbf30) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbf34`](#insn-00acbf34) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbf38`](#insn-00acbf38) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbf3c`](#insn-00acbf3c) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbf4c`](#insn-00acbf4c) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbf5c`](#insn-00acbf5c) → [`00acbfc8`](#insn-00acbfc8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbf64`](#insn-00acbf64) → [`00acbf74`](#insn-00acbf74) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbf70`](#insn-00acbf70) → [`00acbfc8`](#insn-00acbfc8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbf78`](#insn-00acbf78) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbf7c`](#insn-00acbf7c) → [`00acbf8c`](#insn-00acbf8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbf88`](#insn-00acbf88) → [`00c53cd0`](../00c53/00c53cd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53cd0` · 推定シンボル `None` · 推定型 `None`
- [`00acbf94`](#insn-00acbf94) → [`00acbf2c`](#insn-00acbf2c) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00acbf2c` · 推定シンボル `None` · 推定型 `None`
- [`00acbf98`](#insn-00acbf98) → [`00acbf68`](#insn-00acbf68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbfa4`](#insn-00acbfa4) → [`00c53d00`](../00c53/00c53d00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53d00` · 推定シンボル `None` · 推定型 `None`
- [`00acbfa8`](#insn-00acbfa8) → [`00acbf68`](#insn-00acbf68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbfc0`](#insn-00acbfc0) → [`00c57e80`](../00c57/00c57e80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e80` · 推定シンボル `None` · 推定型 `None`
- [`00acbfc4`](#insn-00acbfc4) → [`00acbf68`](#insn-00acbf68) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbfcc`](#insn-00acbfcc) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbfd4`](#insn-00acbfd4) → [`00acc014`](#insn-00acc014) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbfd8`](#insn-00acbfd8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbfdc`](#insn-00acbfdc) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbfe0`](#insn-00acbfe0) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbfe4`](#insn-00acbfe4) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acc014`](#insn-00acc014) → [`00c57ee0`](../00c57/00c57ee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ee0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00acbf30`](#insn-00acbf30)

~~~json
{
  "source": "00acbf30",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbf34`](#insn-00acbf34)

~~~json
{
  "source": "00acbf34",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbf38`](#insn-00acbf38)

~~~json
{
  "source": "00acbf38",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbf3c`](#insn-00acbf3c)

~~~json
{
  "source": "00acbf3c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbf4c`](#insn-00acbf4c)

~~~json
{
  "source": "00acbf4c",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbf5c`](#insn-00acbf5c)

~~~json
{
  "source": "00acbf5c",
  "target": "00acbfc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbf64`](#insn-00acbf64)

~~~json
{
  "source": "00acbf64",
  "target": "00acbf74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbf70`](#insn-00acbf70)

~~~json
{
  "source": "00acbf70",
  "target": "00acbfc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbf78`](#insn-00acbf78)

~~~json
{
  "source": "00acbf78",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbf7c`](#insn-00acbf7c)

~~~json
{
  "source": "00acbf7c",
  "target": "00acbf8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbf88`](#insn-00acbf88)

~~~json
{
  "source": "00acbf88",
  "target": "00c53cd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbf94`](#insn-00acbf94)

~~~json
{
  "source": "00acbf94",
  "target": "00acbf2c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbf98`](#insn-00acbf98)

~~~json
{
  "source": "00acbf98",
  "target": "00acbf68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbfa4`](#insn-00acbfa4)

~~~json
{
  "source": "00acbfa4",
  "target": "00c53d00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbfa8`](#insn-00acbfa8)

~~~json
{
  "source": "00acbfa8",
  "target": "00acbf68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbfc0`](#insn-00acbfc0)

~~~json
{
  "source": "00acbfc0",
  "target": "00c57e80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbfc4`](#insn-00acbfc4)

~~~json
{
  "source": "00acbfc4",
  "target": "00acbf68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbfcc`](#insn-00acbfcc)

~~~json
{
  "source": "00acbfcc",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbfd4`](#insn-00acbfd4)

~~~json
{
  "source": "00acbfd4",
  "target": "00acc014",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbfd8`](#insn-00acbfd8)

~~~json
{
  "source": "00acbfd8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbfdc`](#insn-00acbfdc)

~~~json
{
  "source": "00acbfdc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbfe0`](#insn-00acbfe0)

~~~json
{
  "source": "00acbfe0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbfe4`](#insn-00acbfe4)

~~~json
{
  "source": "00acbfe4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acc014`](#insn-00acc014)

~~~json
{
  "source": "00acc014",
  "target": "00c57ee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
