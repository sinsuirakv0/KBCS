# 00b3abcc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b3a7a4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3a/00b3a7a4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0069.md#compare-fbb302573bbdec938e37f1c92ed7f7e6)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00b3ac68`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3a/00b3ac68.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0069.md#compare-39c7d1e21ff23dc1a78d583e76449d77)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b3abcc",
  "name": "Java_jp_co_ponos_battlecats_TapjoyImplementation_onTapjoyPlacementRequestFailure",
  "size": 200,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "49780c986b547de2dd3e6bdeade6deedd6f1d3bc8b1400db1d23771aec54fbc0",
  "source_text_sha256": "49780c986b547de2dd3e6bdeade6deedd6f1d3bc8b1400db1d23771aec54fbc0",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b3abcc",
        "00b3ac8f"
      ],
      [
        "00b3acd4",
        "00b3acd7"
      ]
    ],
    "bytes_sha256": "42641555cf2c6b45c890ec6b9877beed4555e1fe20c508a634a05a984574d43a",
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

- [00589954](../00589/00589954.md)
- [00b3b820](../00b3b/00b3b820.md)
- [00c57eb0](../00c57/00c57eb0.md)
- [00c57ee0](../00c57/00c57ee0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1041 bytes

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
  FUN_00589954(local_50,param_1,param_3);
  FUN_00589954(local_68,param_1,param_3);
  puVar2 = (undefined8 *)FUN_00b3b820(&DAT_011251f8,local_50);
  if ((puVar2 != &DAT_01125200) && (plVar3 = (long *)puVar2[0x12], plVar3 != (long *)0x0)) {
    (**(code **)(*plVar3 + 0x30))(plVar3,local_50,local_68);
  }
  if ((local_68[0] & 1) != 0) {
    _ZdlPv(local_58);
  }
  if ((local_50[0] & 1) != 0) {
    _ZdlPv(local_40);
  }
  if (*(long *)(lVar1 + 0x28) == local_38) {
                    /* try { // try from 00b3ac84 to 00c3ac87 has its CatchHandler @ 00b3b080 */
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
<a id="insn-00b3abcc"></a> `00b3abcc` | `ff c3 01 d1` | sub sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00b3abd0"></a> `00b3abd0` | `fd 7b 04 a9` | stp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b3abd4"></a> `00b3abd4` | `f5 2b 00 f9` | str x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00b3abd8"></a> `00b3abd8` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00b3abdc"></a> `00b3abdc` | `fd 03 01 91` | add x29,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00b3abe0"></a> `00b3abe0` | `55 d0 3b d5` | mrs x21,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00b3abe4"></a> `00b3abe4` | `e1 03 02 aa` | mov x1,x2 | `FALL_THROUGH`
<a id="insn-00b3abe8"></a> `00b3abe8` | `f3 03 02 aa` | mov x19,x2 | `FALL_THROUGH`
<a id="insn-00b3abec"></a> `00b3abec` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00b3abf0"></a> `00b3abf0` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00b3abf4"></a> `00b3abf4` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00b3abf8"></a> `00b3abf8` | `e8 83 00 91` | add x8,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00b3abfc"></a> `00b3abfc` | `56 3b e9 97` | bl 0x00589954 | `UNCONDITIONAL_CALL`
<a id="insn-00b3ac00"></a> `00b3ac00` | `e8 23 00 91` | add x8,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00b3ac04"></a> `00b3ac04` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b3ac08"></a> `00b3ac08` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00b3ac0c"></a> `00b3ac0c` | `52 3b e9 97` | bl 0x00589954 | `UNCONDITIONAL_CALL`
<a id="insn-00b3ac10"></a> `00b3ac10` | `40 2f 00 f0` | adrp x0,0x1125000 | `FALL_THROUGH`
<a id="insn-00b3ac14"></a> `00b3ac14` | `00 e0 07 91` | add x0,x0,#0x1f8 | `FALL_THROUGH`
<a id="insn-00b3ac18"></a> `00b3ac18` | `e1 83 00 91` | add x1,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00b3ac1c"></a> `00b3ac1c` | `01 03 00 94` | bl 0x00b3b820 | `UNCONDITIONAL_CALL`
<a id="insn-00b3ac20"></a> `00b3ac20` | `48 2f 00 f0` | adrp x8,0x1125000 | `FALL_THROUGH`
<a id="insn-00b3ac24"></a> `00b3ac24` | `08 01 08 91` | add x8,x8,#0x200 | `FALL_THROUGH`
<a id="insn-00b3ac28"></a> `00b3ac28` | `1f 00 08 eb` | cmp x0,x8 | `FALL_THROUGH`
<a id="insn-00b3ac2c"></a> `00b3ac2c` | `00 01 00 54` | b.eq 0x00b3ac4c | `CONDITIONAL_JUMP`
<a id="insn-00b3ac30"></a> `00b3ac30` | `00 48 40 f9` | ldr x0,[x0, #0x90] | `FALL_THROUGH`
<a id="insn-00b3ac34"></a> `00b3ac34` | `c0 00 00 b4` | cbz x0,0x00b3ac4c | `CONDITIONAL_JUMP`
<a id="insn-00b3ac38"></a> `00b3ac38` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00b3ac3c"></a> `00b3ac3c` | `08 19 40 f9` | ldr x8,[x8, #0x30] | `FALL_THROUGH`
<a id="insn-00b3ac40"></a> `00b3ac40` | `e1 83 00 91` | add x1,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00b3ac44"></a> `00b3ac44` | `e2 23 00 91` | add x2,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00b3ac48"></a> `00b3ac48` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b3ac4c"></a> `00b3ac4c` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00b3ac50"></a> `00b3ac50` | `68 00 00 36` | tbz w8,#0x0,0x00b3ac5c | `CONDITIONAL_JUMP`
<a id="insn-00b3ac54"></a> `00b3ac54` | `e0 0f 40 f9` | ldr x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00b3ac58"></a> `00b3ac58` | `96 74 04 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00b3ac5c"></a> `00b3ac5c` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b3ac60"></a> `00b3ac60` | `68 00 00 36` | tbz w8,#0x0,0x00b3ac6c | `CONDITIONAL_JUMP`
<a id="insn-00b3ac64"></a> `00b3ac64` | `e0 1b 40 f9` | ldr x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b3ac68"></a> `00b3ac68` | `92 74 04 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00b3ac6c"></a> `00b3ac6c` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00b3ac70"></a> `00b3ac70` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00b3ac74"></a> `00b3ac74` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00b3ac78"></a> `00b3ac78` | `e1 02 00 54` | b.ne 0x00b3acd4 | `CONDITIONAL_JUMP`
<a id="insn-00b3ac7c"></a> `00b3ac7c` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00b3ac80"></a> `00b3ac80` | `f5 2b 40 f9` | ldr x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00b3ac84"></a> `00b3ac84` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b3ac88"></a> `00b3ac88` | `ff c3 01 91` | add sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00b3ac8c"></a> `00b3ac8c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00b3acd4"></a> `00b3acd4` | `83 74 04 94` | bl 0x00c57ee0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b3abcc`](#insn-00b3abcc) 範囲 `[['00b3abcc', '00b3ac2f']]`
  - `CONDITIONAL_JUMP` [`00b3ac2c`](#insn-00b3ac2c) → [`00b3ac4c`](#insn-00b3ac4c)
  - `FALL_THROUGH` [`00b3ac2c`](#insn-00b3ac2c) → [`00b3ac30`](#insn-00b3ac30)
- ブロック [`00b3ac30`](#insn-00b3ac30) 範囲 `[['00b3ac30', '00b3ac37']]`
  - `CONDITIONAL_JUMP` [`00b3ac34`](#insn-00b3ac34) → [`00b3ac4c`](#insn-00b3ac4c)
  - `FALL_THROUGH` [`00b3ac34`](#insn-00b3ac34) → [`00b3ac38`](#insn-00b3ac38)
- ブロック [`00b3ac38`](#insn-00b3ac38) 範囲 `[['00b3ac38', '00b3ac4b']]`
  - `FALL_THROUGH` [`00b3ac48`](#insn-00b3ac48) → [`00b3ac4c`](#insn-00b3ac4c)
- ブロック [`00b3ac4c`](#insn-00b3ac4c) 範囲 `[['00b3ac4c', '00b3ac53']]`
  - `CONDITIONAL_JUMP` [`00b3ac50`](#insn-00b3ac50) → [`00b3ac5c`](#insn-00b3ac5c)
  - `FALL_THROUGH` [`00b3ac50`](#insn-00b3ac50) → [`00b3ac54`](#insn-00b3ac54)
- ブロック [`00b3ac54`](#insn-00b3ac54) 範囲 `[['00b3ac54', '00b3ac5b']]`
  - `FALL_THROUGH` [`00b3ac58`](#insn-00b3ac58) → [`00b3ac5c`](#insn-00b3ac5c)
- ブロック [`00b3ac5c`](#insn-00b3ac5c) 範囲 `[['00b3ac5c', '00b3ac63']]`
  - `CONDITIONAL_JUMP` [`00b3ac60`](#insn-00b3ac60) → [`00b3ac6c`](#insn-00b3ac6c)
  - `FALL_THROUGH` [`00b3ac60`](#insn-00b3ac60) → [`00b3ac64`](#insn-00b3ac64)
- ブロック [`00b3ac64`](#insn-00b3ac64) 範囲 `[['00b3ac64', '00b3ac6b']]`
  - `FALL_THROUGH` [`00b3ac68`](#insn-00b3ac68) → [`00b3ac6c`](#insn-00b3ac6c)
- ブロック [`00b3ac6c`](#insn-00b3ac6c) 範囲 `[['00b3ac6c', '00b3ac7b']]`
  - `CONDITIONAL_JUMP` [`00b3ac78`](#insn-00b3ac78) → [`00b3acd4`](#insn-00b3acd4)
  - `FALL_THROUGH` [`00b3ac78`](#insn-00b3ac78) → [`00b3ac7c`](#insn-00b3ac7c)
- ブロック [`00b3ac7c`](#insn-00b3ac7c) 範囲 `[['00b3ac7c', '00b3ac83']]`
  - `FALL_THROUGH` [`00b3ac80`](#insn-00b3ac80) → [`00b3ac84`](#insn-00b3ac84)
- ブロック [`00b3ac84`](#insn-00b3ac84) 範囲 `[['00b3ac84', '00b3ac8f']]`
- ブロック [`00b3acd4`](#insn-00b3acd4) 範囲 `[['00b3acd4', '00b3acd7']]`

## 命令位置別の参照

- [`00b3abd0`](#insn-00b3abd0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3abd4`](#insn-00b3abd4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3abd8`](#insn-00b3abd8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3abf4`](#insn-00b3abf4) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3abfc`](#insn-00b3abfc) → [`00589954`](../00589/00589954.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00589954` · 推定シンボル `None` · 推定型 `None`
- [`00b3ac0c`](#insn-00b3ac0c) → [`00589954`](../00589/00589954.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00589954` · 推定シンボル `None` · 推定型 `None`
- [`00b3ac14`](#insn-00b3ac14) → `011251f8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b3ac1c`](#insn-00b3ac1c) → [`00b3b820`](../00b3b/00b3b820.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00b3b820` · 推定シンボル `None` · 推定型 `None`
- [`00b3ac2c`](#insn-00b3ac2c) → [`00b3ac4c`](#insn-00b3ac4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3ac34`](#insn-00b3ac34) → [`00b3ac4c`](#insn-00b3ac4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3ac4c`](#insn-00b3ac4c) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3ac50`](#insn-00b3ac50) → [`00b3ac5c`](#insn-00b3ac5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3ac54`](#insn-00b3ac54) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3ac58`](#insn-00b3ac58) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00b3ac5c`](#insn-00b3ac5c) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3ac60`](#insn-00b3ac60) → [`00b3ac6c`](#insn-00b3ac6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3ac64`](#insn-00b3ac64) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3ac68`](#insn-00b3ac68) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00b3ac70`](#insn-00b3ac70) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3ac78`](#insn-00b3ac78) → [`00b3acd4`](#insn-00b3acd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3ac7c`](#insn-00b3ac7c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3ac80`](#insn-00b3ac80) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3ac84`](#insn-00b3ac84) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3acd4`](#insn-00b3acd4) → [`00c57ee0`](../00c57/00c57ee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ee0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b3abd0`](#insn-00b3abd0)

~~~json
{
  "source": "00b3abd0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3abd4`](#insn-00b3abd4)

~~~json
{
  "source": "00b3abd4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3abd8`](#insn-00b3abd8)

~~~json
{
  "source": "00b3abd8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3abf4`](#insn-00b3abf4)

~~~json
{
  "source": "00b3abf4",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3abfc`](#insn-00b3abfc)

~~~json
{
  "source": "00b3abfc",
  "target": "00589954",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b3ac0c`](#insn-00b3ac0c)

~~~json
{
  "source": "00b3ac0c",
  "target": "00589954",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b3ac14`](#insn-00b3ac14)

~~~json
{
  "source": "00b3ac14",
  "target": "011251f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011251f8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b3ac1c`](#insn-00b3ac1c)

~~~json
{
  "source": "00b3ac1c",
  "target": "00b3b820",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b3ac2c`](#insn-00b3ac2c)

~~~json
{
  "source": "00b3ac2c",
  "target": "00b3ac4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3ac34`](#insn-00b3ac34)

~~~json
{
  "source": "00b3ac34",
  "target": "00b3ac4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3ac4c`](#insn-00b3ac4c)

~~~json
{
  "source": "00b3ac4c",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3ac50`](#insn-00b3ac50)

~~~json
{
  "source": "00b3ac50",
  "target": "00b3ac5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3ac54`](#insn-00b3ac54)

~~~json
{
  "source": "00b3ac54",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3ac58`](#insn-00b3ac58)

~~~json
{
  "source": "00b3ac58",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b3ac5c`](#insn-00b3ac5c)

~~~json
{
  "source": "00b3ac5c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3ac60`](#insn-00b3ac60)

~~~json
{
  "source": "00b3ac60",
  "target": "00b3ac6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3ac64`](#insn-00b3ac64)

~~~json
{
  "source": "00b3ac64",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3ac68`](#insn-00b3ac68)

~~~json
{
  "source": "00b3ac68",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b3ac70`](#insn-00b3ac70)

~~~json
{
  "source": "00b3ac70",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3ac78`](#insn-00b3ac78)

~~~json
{
  "source": "00b3ac78",
  "target": "00b3acd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3ac7c`](#insn-00b3ac7c)

~~~json
{
  "source": "00b3ac7c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3ac80`](#insn-00b3ac80)

~~~json
{
  "source": "00b3ac80",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3ac84`](#insn-00b3ac84)

~~~json
{
  "source": "00b3ac84",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3acd4`](#insn-00b3acd4)

~~~json
{
  "source": "00b3acd4",
  "target": "00c57ee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
