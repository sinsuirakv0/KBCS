# 00acbcc4

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00acbc54`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00acb/00acbc54.md) · 移動量 `+0x70`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0034.md#compare-ae83384600c30816f80310355082e171)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00acccb8`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acc/00acccb8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0028.md#compare-d7ae66b7c4c2dad31b6c990d24507445)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acbcc4",
  "name": "FUN_00acbcc4",
  "size": 212,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "dc57a27120658a4fbedc9776d2dca93fb9ec607664a9d3e0606df07a8e090f6f",
  "source_text_sha256": "dc57a27120658a4fbedc9776d2dca93fb9ec607664a9d3e0606df07a8e090f6f",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00acbcc4",
        "00acbd93"
      ],
      [
        "00acbdb8",
        "00acbdbb"
      ]
    ],
    "bytes_sha256": "a21d5c732555cab7647d1352b42b540b6186112330b0735686a0bfb754f7493d",
    "instruction_count": 53,
    "instruction_bytes": 212,
    "body_bytes": 212,
    "indirect": 2,
    "unresolved": 2
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c53d70](../00c53/00c53d70.md)
- [00c53da0](../00c53/00c53da0.md)
- [00c57f50](../00c57/00c57f50.md)
- [00c57fb0](../00c57/00c57fb0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1004 bytes

~~~c

void FUN_00acbcc4(long param_1,undefined8 param_2)

{
  undefined8 *puVar1;
  long *plVar2;
  undefined8 *puVar3;
  long *plVar4;
  long lVar5;
  long lVar6;
  long lVar7;
  
  lVar5 = tpidr_el0;
  lVar7 = *(long *)(lVar5 + 0x28);
  if (*(char *)(param_1 + 0x28) != '\0') {
    puVar3 = *(undefined8 **)(param_1 + 0x48);
    for (puVar1 = *(undefined8 **)(param_1 + 0x40); puVar1 != puVar3; puVar1 = puVar1 + 2) {
      plVar2 = (long *)*puVar1;
      plVar4 = (long *)puVar1[1];
      if (plVar4 != (long *)0x0) {
        FUN_00c53d70(1,plVar4 + 1);
      }
      (**(code **)(*plVar2 + 8))(plVar2,param_2);
      if ((plVar4 != (long *)0x0) &&
         (lVar6 = FUN_00c53da0(0xffffffffffffffff,plVar4 + 1), lVar6 == 0)) {
        (**(code **)(*plVar4 + 0x10))(plVar4);
        _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar4);
      }
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
<a id="insn-00acbcc4"></a> `00acbcc4` | `ff 83 01 d1` | sub sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00acbcc8"></a> `00acbcc8` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00acbccc"></a> `00acbccc` | `f8 5f 03 a9` | stp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00acbcd0"></a> `00acbcd0` | `f6 57 04 a9` | stp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00acbcd4"></a> `00acbcd4` | `f4 4f 05 a9` | stp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00acbcd8"></a> `00acbcd8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00acbcdc"></a> `00acbcdc` | `56 d0 3b d5` | mrs x22,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00acbce0"></a> `00acbce0` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00acbce4"></a> `00acbce4` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00acbce8"></a> `00acbce8` | `08 a0 40 39` | ldrb w8,[x0, #0x28] | `FALL_THROUGH`
<a id="insn-00acbcec"></a> `00acbcec` | `08 04 00 34` | cbz w8,0x00acbd6c | `CONDITIONAL_JUMP`
<a id="insn-00acbcf0"></a> `00acbcf0` | `17 60 44 a9` | ldp x23,x24,[x0, #0x40] | `FALL_THROUGH`
<a id="insn-00acbcf4"></a> `00acbcf4` | `ff 02 18 eb` | cmp x23,x24 | `FALL_THROUGH`
<a id="insn-00acbcf8"></a> `00acbcf8` | `a0 03 00 54` | b.eq 0x00acbd6c | `CONDITIONAL_JUMP`
<a id="insn-00acbcfc"></a> `00acbcfc` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00acbd00"></a> `00acbd00` | `04 00 00 14` | b 0x00acbd10 | `UNCONDITIONAL_JUMP`
<a id="insn-00acbd04"></a> `00acbd04` | `f7 42 00 91` | add x23,x23,#0x10 | `FALL_THROUGH`
<a id="insn-00acbd08"></a> `00acbd08` | `ff 02 18 eb` | cmp x23,x24 | `FALL_THROUGH`
<a id="insn-00acbd0c"></a> `00acbd0c` | `00 03 00 54` | b.eq 0x00acbd6c | `CONDITIONAL_JUMP`
<a id="insn-00acbd10"></a> `00acbd10` | `f5 52 40 a9` | ldp x21,x20,[x23] | `FALL_THROUGH`
<a id="insn-00acbd14"></a> `00acbd14` | `f5 d3 00 a9` | stp x21,x20,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00acbd18"></a> `00acbd18` | `94 00 00 b4` | cbz x20,0x00acbd28 | `CONDITIONAL_JUMP`
<a id="insn-00acbd1c"></a> `00acbd1c` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00acbd20"></a> `00acbd20` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00acbd24"></a> `00acbd24` | `13 20 06 94` | bl 0x00c53d70 | `UNCONDITIONAL_CALL`
<a id="insn-00acbd28"></a> `00acbd28` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00acbd2c"></a> `00acbd2c` | `08 05 40 f9` | ldr x8,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00acbd30"></a> `00acbd30` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00acbd34"></a> `00acbd34` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00acbd38"></a> `00acbd38` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00acbd3c"></a> `00acbd3c` | `54 fe ff b4` | cbz x20,0x00acbd04 | `CONDITIONAL_JUMP`
<a id="insn-00acbd40"></a> `00acbd40` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00acbd44"></a> `00acbd44` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00acbd48"></a> `00acbd48` | `16 20 06 94` | bl 0x00c53da0 | `UNCONDITIONAL_CALL`
<a id="insn-00acbd4c"></a> `00acbd4c` | `c0 fd ff b5` | cbnz x0,0x00acbd04 | `CONDITIONAL_JUMP`
<a id="insn-00acbd50"></a> `00acbd50` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00acbd54"></a> `00acbd54` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00acbd58"></a> `00acbd58` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00acbd5c"></a> `00acbd5c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00acbd60"></a> `00acbd60` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00acbd64"></a> `00acbd64` | `7b 30 06 94` | bl 0x00c57f50 | `UNCONDITIONAL_CALL`
<a id="insn-00acbd68"></a> `00acbd68` | `e7 ff ff 17` | b 0x00acbd04 | `UNCONDITIONAL_JUMP`
<a id="insn-00acbd6c"></a> `00acbd6c` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00acbd70"></a> `00acbd70` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00acbd74"></a> `00acbd74` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00acbd78"></a> `00acbd78` | `01 02 00 54` | b.ne 0x00acbdb8 | `CONDITIONAL_JUMP`
<a id="insn-00acbd7c"></a> `00acbd7c` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00acbd80"></a> `00acbd80` | `f6 57 44 a9` | ldp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00acbd84"></a> `00acbd84` | `f8 5f 43 a9` | ldp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00acbd88"></a> `00acbd88` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00acbd8c"></a> `00acbd8c` | `ff 83 01 91` | add sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00acbd90"></a> `00acbd90` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00acbdb8"></a> `00acbdb8` | `7e 30 06 94` | bl 0x00c57fb0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00acbcc4`](#insn-00acbcc4) 範囲 `[['00acbcc4', '00acbcef']]`
  - `CONDITIONAL_JUMP` [`00acbcec`](#insn-00acbcec) → [`00acbd6c`](#insn-00acbd6c)
  - `FALL_THROUGH` [`00acbcec`](#insn-00acbcec) → [`00acbcf0`](#insn-00acbcf0)
- ブロック [`00acbcf0`](#insn-00acbcf0) 範囲 `[['00acbcf0', '00acbcfb']]`
  - `CONDITIONAL_JUMP` [`00acbcf8`](#insn-00acbcf8) → [`00acbd6c`](#insn-00acbd6c)
  - `FALL_THROUGH` [`00acbcf8`](#insn-00acbcf8) → [`00acbcfc`](#insn-00acbcfc)
- ブロック [`00acbcfc`](#insn-00acbcfc) 範囲 `[['00acbcfc', '00acbd03']]`
  - `UNCONDITIONAL_JUMP` [`00acbd00`](#insn-00acbd00) → [`00acbd10`](#insn-00acbd10)
- ブロック [`00acbd04`](#insn-00acbd04) 範囲 `[['00acbd04', '00acbd0f']]`
  - `CONDITIONAL_JUMP` [`00acbd0c`](#insn-00acbd0c) → [`00acbd6c`](#insn-00acbd6c)
  - `FALL_THROUGH` [`00acbd0c`](#insn-00acbd0c) → [`00acbd10`](#insn-00acbd10)
- ブロック [`00acbd10`](#insn-00acbd10) 範囲 `[['00acbd10', '00acbd1b']]`
  - `CONDITIONAL_JUMP` [`00acbd18`](#insn-00acbd18) → [`00acbd28`](#insn-00acbd28)
  - `FALL_THROUGH` [`00acbd18`](#insn-00acbd18) → [`00acbd1c`](#insn-00acbd1c)
- ブロック [`00acbd1c`](#insn-00acbd1c) 範囲 `[['00acbd1c', '00acbd27']]`
  - `FALL_THROUGH` [`00acbd24`](#insn-00acbd24) → [`00acbd28`](#insn-00acbd28)
- ブロック [`00acbd28`](#insn-00acbd28) 範囲 `[['00acbd28', '00acbd3f']]`
  - `CONDITIONAL_JUMP` [`00acbd3c`](#insn-00acbd3c) → [`00acbd04`](#insn-00acbd04)
  - `FALL_THROUGH` [`00acbd3c`](#insn-00acbd3c) → [`00acbd40`](#insn-00acbd40)
- ブロック [`00acbd40`](#insn-00acbd40) 範囲 `[['00acbd40', '00acbd4f']]`
  - `CONDITIONAL_JUMP` [`00acbd4c`](#insn-00acbd4c) → [`00acbd04`](#insn-00acbd04)
  - `FALL_THROUGH` [`00acbd4c`](#insn-00acbd4c) → [`00acbd50`](#insn-00acbd50)
- ブロック [`00acbd50`](#insn-00acbd50) 範囲 `[['00acbd50', '00acbd6b']]`
  - `UNCONDITIONAL_JUMP` [`00acbd68`](#insn-00acbd68) → [`00acbd04`](#insn-00acbd04)
- ブロック [`00acbd6c`](#insn-00acbd6c) 範囲 `[['00acbd6c', '00acbd7b']]`
  - `CONDITIONAL_JUMP` [`00acbd78`](#insn-00acbd78) → [`00acbdb8`](#insn-00acbdb8)
  - `FALL_THROUGH` [`00acbd78`](#insn-00acbd78) → [`00acbd7c`](#insn-00acbd7c)
- ブロック [`00acbd7c`](#insn-00acbd7c) 範囲 `[['00acbd7c', '00acbd93']]`
- ブロック [`00acbdb8`](#insn-00acbdb8) 範囲 `[['00acbdb8', '00acbdbb']]`

## 命令位置別の参照

- [`00acbcc8`](#insn-00acbcc8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbccc`](#insn-00acbccc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbcd0`](#insn-00acbcd0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbcd4`](#insn-00acbcd4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbce4`](#insn-00acbce4) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbcec`](#insn-00acbcec) → [`00acbd6c`](#insn-00acbd6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbcf8`](#insn-00acbcf8) → [`00acbd6c`](#insn-00acbd6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbd00`](#insn-00acbd00) → [`00acbd10`](#insn-00acbd10) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbd0c`](#insn-00acbd0c) → [`00acbd6c`](#insn-00acbd6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbd14`](#insn-00acbd14) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbd18`](#insn-00acbd18) → [`00acbd28`](#insn-00acbd28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbd24`](#insn-00acbd24) → [`00c53d70`](../00c53/00c53d70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53d70` · 推定シンボル `None` · 推定型 `None`
- [`00acbd3c`](#insn-00acbd3c) → [`00acbd04`](#insn-00acbd04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbd48`](#insn-00acbd48) → [`00c53da0`](../00c53/00c53da0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53da0` · 推定シンボル `None` · 推定型 `None`
- [`00acbd4c`](#insn-00acbd4c) → [`00acbd04`](#insn-00acbd04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbd64`](#insn-00acbd64) → [`00c57f50`](../00c57/00c57f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f50` · 推定シンボル `None` · 推定型 `None`
- [`00acbd68`](#insn-00acbd68) → [`00acbd04`](#insn-00acbd04) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbd70`](#insn-00acbd70) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbd78`](#insn-00acbd78) → [`00acbdb8`](#insn-00acbdb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbd7c`](#insn-00acbd7c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbd80`](#insn-00acbd80) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbd84`](#insn-00acbd84) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbd88`](#insn-00acbd88) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbdb8`](#insn-00acbdb8) → [`00c57fb0`](../00c57/00c57fb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fb0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00acbcc8`](#insn-00acbcc8)

~~~json
{
  "source": "00acbcc8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbccc`](#insn-00acbccc)

~~~json
{
  "source": "00acbccc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbcd0`](#insn-00acbcd0)

~~~json
{
  "source": "00acbcd0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbcd4`](#insn-00acbcd4)

~~~json
{
  "source": "00acbcd4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbce4`](#insn-00acbce4)

~~~json
{
  "source": "00acbce4",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbcec`](#insn-00acbcec)

~~~json
{
  "source": "00acbcec",
  "target": "00acbd6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbcf8`](#insn-00acbcf8)

~~~json
{
  "source": "00acbcf8",
  "target": "00acbd6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbd00`](#insn-00acbd00)

~~~json
{
  "source": "00acbd00",
  "target": "00acbd10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbd0c`](#insn-00acbd0c)

~~~json
{
  "source": "00acbd0c",
  "target": "00acbd6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbd14`](#insn-00acbd14)

~~~json
{
  "source": "00acbd14",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbd18`](#insn-00acbd18)

~~~json
{
  "source": "00acbd18",
  "target": "00acbd28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbd24`](#insn-00acbd24)

~~~json
{
  "source": "00acbd24",
  "target": "00c53d70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbd3c`](#insn-00acbd3c)

~~~json
{
  "source": "00acbd3c",
  "target": "00acbd04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbd48`](#insn-00acbd48)

~~~json
{
  "source": "00acbd48",
  "target": "00c53da0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbd4c`](#insn-00acbd4c)

~~~json
{
  "source": "00acbd4c",
  "target": "00acbd04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbd64`](#insn-00acbd64)

~~~json
{
  "source": "00acbd64",
  "target": "00c57f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbd68`](#insn-00acbd68)

~~~json
{
  "source": "00acbd68",
  "target": "00acbd04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbd70`](#insn-00acbd70)

~~~json
{
  "source": "00acbd70",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbd78`](#insn-00acbd78)

~~~json
{
  "source": "00acbd78",
  "target": "00acbdb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbd7c`](#insn-00acbd7c)

~~~json
{
  "source": "00acbd7c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbd80`](#insn-00acbd80)

~~~json
{
  "source": "00acbd80",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbd84`](#insn-00acbd84)

~~~json
{
  "source": "00acbd84",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbd88`](#insn-00acbd88)

~~~json
{
  "source": "00acbd88",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbdb8`](#insn-00acbdb8)

~~~json
{
  "source": "00acbdb8",
  "target": "00c57fb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
