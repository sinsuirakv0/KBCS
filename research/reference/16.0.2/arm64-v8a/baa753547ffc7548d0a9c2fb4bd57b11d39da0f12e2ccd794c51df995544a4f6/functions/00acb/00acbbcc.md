# 00acbbcc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00acbb5c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00acb/00acbb5c.md) · 移動量 `+0x70`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0034.md#compare-3dfdf3c7107c7c49938b965602b5332d)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00accbc0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acc/00accbc0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0028.md#compare-1a0ac0719df8a4e42d7fc8ed4771dda6)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acbbcc",
  "name": "FUN_00acbbcc",
  "size": 212,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "466825c0d53e60600d54d8d6a2ea4dc1a77c1d11e1d5eef49511cfe831d3c90d",
  "source_text_sha256": "466825c0d53e60600d54d8d6a2ea4dc1a77c1d11e1d5eef49511cfe831d3c90d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00acbbcc",
        "00acbc9b"
      ],
      [
        "00acbcc0",
        "00acbcc3"
      ]
    ],
    "bytes_sha256": "62eca5ea3007e86a573c51669a2c95ea9f9013603466ba0e1b188d7149c9d089",
    "instruction_count": 53,
    "instruction_bytes": 212,
    "body_bytes": 212,
    "indirect": 2,
    "unresolved": 2
  }
}
~~~

## 呼び出し元

- [00935b64](../00935/00935b64.md)

## 呼び出し先

- [00c53d70](../00c53/00c53d70.md)
- [00c53da0](../00c53/00c53da0.md)
- [00c57f50](../00c57/00c57f50.md)
- [00c57fb0](../00c57/00c57fb0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1010 bytes

~~~c

void FUN_00acbbcc(long param_1,undefined8 param_2)

{
  undefined8 *puVar1;
  undefined8 *puVar2;
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
      puVar2 = (undefined8 *)*puVar1;
      plVar4 = (long *)puVar1[1];
      if (plVar4 != (long *)0x0) {
        FUN_00c53d70(1,plVar4 + 1);
      }
      (**(code **)*puVar2)(puVar2,param_2);
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
<a id="insn-00acbbcc"></a> `00acbbcc` | `ff 83 01 d1` | sub sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00acbbd0"></a> `00acbbd0` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00acbbd4"></a> `00acbbd4` | `f8 5f 03 a9` | stp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00acbbd8"></a> `00acbbd8` | `f6 57 04 a9` | stp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00acbbdc"></a> `00acbbdc` | `f4 4f 05 a9` | stp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00acbbe0"></a> `00acbbe0` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00acbbe4"></a> `00acbbe4` | `56 d0 3b d5` | mrs x22,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00acbbe8"></a> `00acbbe8` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00acbbec"></a> `00acbbec` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00acbbf0"></a> `00acbbf0` | `08 a0 40 39` | ldrb w8,[x0, #0x28] | `FALL_THROUGH`
<a id="insn-00acbbf4"></a> `00acbbf4` | `08 04 00 34` | cbz w8,0x00acbc74 | `CONDITIONAL_JUMP`
<a id="insn-00acbbf8"></a> `00acbbf8` | `17 60 44 a9` | ldp x23,x24,[x0, #0x40] | `FALL_THROUGH`
<a id="insn-00acbbfc"></a> `00acbbfc` | `ff 02 18 eb` | cmp x23,x24 | `FALL_THROUGH`
<a id="insn-00acbc00"></a> `00acbc00` | `a0 03 00 54` | b.eq 0x00acbc74 | `CONDITIONAL_JUMP`
<a id="insn-00acbc04"></a> `00acbc04` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00acbc08"></a> `00acbc08` | `04 00 00 14` | b 0x00acbc18 | `UNCONDITIONAL_JUMP`
<a id="insn-00acbc0c"></a> `00acbc0c` | `f7 42 00 91` | add x23,x23,#0x10 | `FALL_THROUGH`
<a id="insn-00acbc10"></a> `00acbc10` | `ff 02 18 eb` | cmp x23,x24 | `FALL_THROUGH`
<a id="insn-00acbc14"></a> `00acbc14` | `00 03 00 54` | b.eq 0x00acbc74 | `CONDITIONAL_JUMP`
<a id="insn-00acbc18"></a> `00acbc18` | `f5 52 40 a9` | ldp x21,x20,[x23] | `FALL_THROUGH`
<a id="insn-00acbc1c"></a> `00acbc1c` | `f5 d3 00 a9` | stp x21,x20,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00acbc20"></a> `00acbc20` | `94 00 00 b4` | cbz x20,0x00acbc30 | `CONDITIONAL_JUMP`
<a id="insn-00acbc24"></a> `00acbc24` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00acbc28"></a> `00acbc28` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00acbc2c"></a> `00acbc2c` | `51 20 06 94` | bl 0x00c53d70 | `UNCONDITIONAL_CALL`
<a id="insn-00acbc30"></a> `00acbc30` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00acbc34"></a> `00acbc34` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00acbc38"></a> `00acbc38` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00acbc3c"></a> `00acbc3c` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00acbc40"></a> `00acbc40` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00acbc44"></a> `00acbc44` | `54 fe ff b4` | cbz x20,0x00acbc0c | `CONDITIONAL_JUMP`
<a id="insn-00acbc48"></a> `00acbc48` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00acbc4c"></a> `00acbc4c` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00acbc50"></a> `00acbc50` | `54 20 06 94` | bl 0x00c53da0 | `UNCONDITIONAL_CALL`
<a id="insn-00acbc54"></a> `00acbc54` | `c0 fd ff b5` | cbnz x0,0x00acbc0c | `CONDITIONAL_JUMP`
<a id="insn-00acbc58"></a> `00acbc58` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00acbc5c"></a> `00acbc5c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00acbc60"></a> `00acbc60` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00acbc64"></a> `00acbc64` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00acbc68"></a> `00acbc68` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00acbc6c"></a> `00acbc6c` | `b9 30 06 94` | bl 0x00c57f50 | `UNCONDITIONAL_CALL`
<a id="insn-00acbc70"></a> `00acbc70` | `e7 ff ff 17` | b 0x00acbc0c | `UNCONDITIONAL_JUMP`
<a id="insn-00acbc74"></a> `00acbc74` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00acbc78"></a> `00acbc78` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00acbc7c"></a> `00acbc7c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00acbc80"></a> `00acbc80` | `01 02 00 54` | b.ne 0x00acbcc0 | `CONDITIONAL_JUMP`
<a id="insn-00acbc84"></a> `00acbc84` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00acbc88"></a> `00acbc88` | `f6 57 44 a9` | ldp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00acbc8c"></a> `00acbc8c` | `f8 5f 43 a9` | ldp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00acbc90"></a> `00acbc90` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00acbc94"></a> `00acbc94` | `ff 83 01 91` | add sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00acbc98"></a> `00acbc98` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00acbcc0"></a> `00acbcc0` | `bc 30 06 94` | bl 0x00c57fb0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00acbbcc`](#insn-00acbbcc) 範囲 `[['00acbbcc', '00acbbf7']]`
  - `CONDITIONAL_JUMP` [`00acbbf4`](#insn-00acbbf4) → [`00acbc74`](#insn-00acbc74)
  - `FALL_THROUGH` [`00acbbf4`](#insn-00acbbf4) → [`00acbbf8`](#insn-00acbbf8)
- ブロック [`00acbbf8`](#insn-00acbbf8) 範囲 `[['00acbbf8', '00acbc03']]`
  - `CONDITIONAL_JUMP` [`00acbc00`](#insn-00acbc00) → [`00acbc74`](#insn-00acbc74)
  - `FALL_THROUGH` [`00acbc00`](#insn-00acbc00) → [`00acbc04`](#insn-00acbc04)
- ブロック [`00acbc04`](#insn-00acbc04) 範囲 `[['00acbc04', '00acbc0b']]`
  - `UNCONDITIONAL_JUMP` [`00acbc08`](#insn-00acbc08) → [`00acbc18`](#insn-00acbc18)
- ブロック [`00acbc0c`](#insn-00acbc0c) 範囲 `[['00acbc0c', '00acbc17']]`
  - `CONDITIONAL_JUMP` [`00acbc14`](#insn-00acbc14) → [`00acbc74`](#insn-00acbc74)
  - `FALL_THROUGH` [`00acbc14`](#insn-00acbc14) → [`00acbc18`](#insn-00acbc18)
- ブロック [`00acbc18`](#insn-00acbc18) 範囲 `[['00acbc18', '00acbc23']]`
  - `CONDITIONAL_JUMP` [`00acbc20`](#insn-00acbc20) → [`00acbc30`](#insn-00acbc30)
  - `FALL_THROUGH` [`00acbc20`](#insn-00acbc20) → [`00acbc24`](#insn-00acbc24)
- ブロック [`00acbc24`](#insn-00acbc24) 範囲 `[['00acbc24', '00acbc2f']]`
  - `FALL_THROUGH` [`00acbc2c`](#insn-00acbc2c) → [`00acbc30`](#insn-00acbc30)
- ブロック [`00acbc30`](#insn-00acbc30) 範囲 `[['00acbc30', '00acbc47']]`
  - `CONDITIONAL_JUMP` [`00acbc44`](#insn-00acbc44) → [`00acbc0c`](#insn-00acbc0c)
  - `FALL_THROUGH` [`00acbc44`](#insn-00acbc44) → [`00acbc48`](#insn-00acbc48)
- ブロック [`00acbc48`](#insn-00acbc48) 範囲 `[['00acbc48', '00acbc57']]`
  - `CONDITIONAL_JUMP` [`00acbc54`](#insn-00acbc54) → [`00acbc0c`](#insn-00acbc0c)
  - `FALL_THROUGH` [`00acbc54`](#insn-00acbc54) → [`00acbc58`](#insn-00acbc58)
- ブロック [`00acbc58`](#insn-00acbc58) 範囲 `[['00acbc58', '00acbc73']]`
  - `UNCONDITIONAL_JUMP` [`00acbc70`](#insn-00acbc70) → [`00acbc0c`](#insn-00acbc0c)
- ブロック [`00acbc74`](#insn-00acbc74) 範囲 `[['00acbc74', '00acbc83']]`
  - `CONDITIONAL_JUMP` [`00acbc80`](#insn-00acbc80) → [`00acbcc0`](#insn-00acbcc0)
  - `FALL_THROUGH` [`00acbc80`](#insn-00acbc80) → [`00acbc84`](#insn-00acbc84)
- ブロック [`00acbc84`](#insn-00acbc84) 範囲 `[['00acbc84', '00acbc9b']]`
- ブロック [`00acbcc0`](#insn-00acbcc0) 範囲 `[['00acbcc0', '00acbcc3']]`

## 命令位置別の参照

- [`00acbbd0`](#insn-00acbbd0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbbd4`](#insn-00acbbd4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbbd8`](#insn-00acbbd8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbbdc`](#insn-00acbbdc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbbec`](#insn-00acbbec) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbbf4`](#insn-00acbbf4) → [`00acbc74`](#insn-00acbc74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbc00`](#insn-00acbc00) → [`00acbc74`](#insn-00acbc74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbc08`](#insn-00acbc08) → [`00acbc18`](#insn-00acbc18) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbc14`](#insn-00acbc14) → [`00acbc74`](#insn-00acbc74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbc1c`](#insn-00acbc1c) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbc20`](#insn-00acbc20) → [`00acbc30`](#insn-00acbc30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbc2c`](#insn-00acbc2c) → [`00c53d70`](../00c53/00c53d70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53d70` · 推定シンボル `None` · 推定型 `None`
- [`00acbc44`](#insn-00acbc44) → [`00acbc0c`](#insn-00acbc0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbc50`](#insn-00acbc50) → [`00c53da0`](../00c53/00c53da0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53da0` · 推定シンボル `None` · 推定型 `None`
- [`00acbc54`](#insn-00acbc54) → [`00acbc0c`](#insn-00acbc0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbc6c`](#insn-00acbc6c) → [`00c57f50`](../00c57/00c57f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f50` · 推定シンボル `None` · 推定型 `None`
- [`00acbc70`](#insn-00acbc70) → [`00acbc0c`](#insn-00acbc0c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbc78`](#insn-00acbc78) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbc80`](#insn-00acbc80) → [`00acbcc0`](#insn-00acbcc0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbc84`](#insn-00acbc84) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbc88`](#insn-00acbc88) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbc8c`](#insn-00acbc8c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbc90`](#insn-00acbc90) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbcc0`](#insn-00acbcc0) → [`00c57fb0`](../00c57/00c57fb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fb0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00acbbd0`](#insn-00acbbd0)

~~~json
{
  "source": "00acbbd0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbbd4`](#insn-00acbbd4)

~~~json
{
  "source": "00acbbd4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbbd8`](#insn-00acbbd8)

~~~json
{
  "source": "00acbbd8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbbdc`](#insn-00acbbdc)

~~~json
{
  "source": "00acbbdc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbbec`](#insn-00acbbec)

~~~json
{
  "source": "00acbbec",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbbf4`](#insn-00acbbf4)

~~~json
{
  "source": "00acbbf4",
  "target": "00acbc74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbc00`](#insn-00acbc00)

~~~json
{
  "source": "00acbc00",
  "target": "00acbc74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbc08`](#insn-00acbc08)

~~~json
{
  "source": "00acbc08",
  "target": "00acbc18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbc14`](#insn-00acbc14)

~~~json
{
  "source": "00acbc14",
  "target": "00acbc74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbc1c`](#insn-00acbc1c)

~~~json
{
  "source": "00acbc1c",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbc20`](#insn-00acbc20)

~~~json
{
  "source": "00acbc20",
  "target": "00acbc30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbc2c`](#insn-00acbc2c)

~~~json
{
  "source": "00acbc2c",
  "target": "00c53d70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbc44`](#insn-00acbc44)

~~~json
{
  "source": "00acbc44",
  "target": "00acbc0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbc50`](#insn-00acbc50)

~~~json
{
  "source": "00acbc50",
  "target": "00c53da0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbc54`](#insn-00acbc54)

~~~json
{
  "source": "00acbc54",
  "target": "00acbc0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbc6c`](#insn-00acbc6c)

~~~json
{
  "source": "00acbc6c",
  "target": "00c57f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbc70`](#insn-00acbc70)

~~~json
{
  "source": "00acbc70",
  "target": "00acbc0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbc78`](#insn-00acbc78)

~~~json
{
  "source": "00acbc78",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbc80`](#insn-00acbc80)

~~~json
{
  "source": "00acbc80",
  "target": "00acbcc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbc84`](#insn-00acbc84)

~~~json
{
  "source": "00acbc84",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbc88`](#insn-00acbc88)

~~~json
{
  "source": "00acbc88",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbc8c`](#insn-00acbc8c)

~~~json
{
  "source": "00acbc8c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbc90`](#insn-00acbc90)

~~~json
{
  "source": "00acbc90",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbcc0`](#insn-00acbcc0)

~~~json
{
  "source": "00acbcc0",
  "target": "00c57fb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
