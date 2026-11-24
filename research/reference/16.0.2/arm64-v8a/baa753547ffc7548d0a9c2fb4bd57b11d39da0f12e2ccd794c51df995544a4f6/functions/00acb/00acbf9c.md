# 00acbf9c

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00acbf2c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00acb/00acbf2c.md) · 移動量 `+0x70`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0034.md#compare-7d57a8ede36054e241b968350c8b1402)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00accf90`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acc/00accf90.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0028.md#compare-a2a52cd015f1e0588551a4c9e355fbff)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acbf9c",
  "name": "FUN_00acbf9c",
  "size": 200,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0f43dd37e86b4a452d43f3ff02fe8eced714140f4bc65b3a049f43b34c1242ed",
  "source_text_sha256": "0f43dd37e86b4a452d43f3ff02fe8eced714140f4bc65b3a049f43b34c1242ed",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00acbf9c",
        "00acc05f"
      ],
      [
        "00acc084",
        "00acc087"
      ]
    ],
    "bytes_sha256": "0e167dfc9713064d15691bd758e0937e8fe80f82458dd5a14372dfa3b8da0d3a",
    "instruction_count": 50,
    "instruction_bytes": 200,
    "body_bytes": 200,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

- [009b9738](../009b9/009b9738.md)
- [00acbf9c](../00acb/00acbf9c.md)

## 呼び出し先

- [00acbf9c](../00acb/00acbf9c.md)
- [00c53d70](../00c53/00c53d70.md)
- [00c53da0](../00c53/00c53da0.md)
- [00c57f50](../00c57/00c57f50.md)
- [00c57fb0](../00c57/00c57fb0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 951 bytes

~~~c

void FUN_00acbf9c(long param_1,byte param_2)

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
      FUN_00c53d70(1,plVar4 + 1);
    }
    FUN_00acbf9c(uVar2,param_2 & 1);
    if ((plVar4 != (long *)0x0) && (lVar6 = FUN_00c53da0(0xffffffffffffffff,plVar4 + 1), lVar6 == 0)
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
<a id="insn-00acbf9c"></a> `00acbf9c` | `ff 83 01 d1` | sub sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00acbfa0"></a> `00acbfa0` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00acbfa4"></a> `00acbfa4` | `f8 5f 03 a9` | stp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00acbfa8"></a> `00acbfa8` | `f6 57 04 a9` | stp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00acbfac"></a> `00acbfac` | `f4 4f 05 a9` | stp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00acbfb0"></a> `00acbfb0` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00acbfb4"></a> `00acbfb4` | `56 d0 3b d5` | mrs x22,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00acbfb8"></a> `00acbfb8` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00acbfbc"></a> `00acbfbc` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00acbfc0"></a> `00acbfc0` | `17 60 44 a9` | ldp x23,x24,[x0, #0x40] | `FALL_THROUGH`
<a id="insn-00acbfc4"></a> `00acbfc4` | `01 a0 00 39` | strb w1,[x0, #0x28] | `FALL_THROUGH`
<a id="insn-00acbfc8"></a> `00acbfc8` | `ff 02 18 eb` | cmp x23,x24 | `FALL_THROUGH`
<a id="insn-00acbfcc"></a> `00acbfcc` | `60 03 00 54` | b.eq 0x00acc038 | `CONDITIONAL_JUMP`
<a id="insn-00acbfd0"></a> `00acbfd0` | `f3 03 01 2a` | mov w19,w1 | `FALL_THROUGH`
<a id="insn-00acbfd4"></a> `00acbfd4` | `04 00 00 14` | b 0x00acbfe4 | `UNCONDITIONAL_JUMP`
<a id="insn-00acbfd8"></a> `00acbfd8` | `f7 42 00 91` | add x23,x23,#0x10 | `FALL_THROUGH`
<a id="insn-00acbfdc"></a> `00acbfdc` | `ff 02 18 eb` | cmp x23,x24 | `FALL_THROUGH`
<a id="insn-00acbfe0"></a> `00acbfe0` | `c0 02 00 54` | b.eq 0x00acc038 | `CONDITIONAL_JUMP`
<a id="insn-00acbfe4"></a> `00acbfe4` | `f5 52 40 a9` | ldp x21,x20,[x23] | `FALL_THROUGH`
<a id="insn-00acbfe8"></a> `00acbfe8` | `f5 d3 00 a9` | stp x21,x20,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00acbfec"></a> `00acbfec` | `94 00 00 b4` | cbz x20,0x00acbffc | `CONDITIONAL_JUMP`
<a id="insn-00acbff0"></a> `00acbff0` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00acbff4"></a> `00acbff4` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00acbff8"></a> `00acbff8` | `5e 1f 06 94` | bl 0x00c53d70 | `UNCONDITIONAL_CALL`
<a id="insn-00acbffc"></a> `00acbffc` | `61 02 00 12` | and w1,w19,#0x1 | `FALL_THROUGH`
<a id="insn-00acc000"></a> `00acc000` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00acc004"></a> `00acc004` | `e6 ff ff 97` | bl 0x00acbf9c | `UNCONDITIONAL_CALL`
<a id="insn-00acc008"></a> `00acc008` | `94 fe ff b4` | cbz x20,0x00acbfd8 | `CONDITIONAL_JUMP`
<a id="insn-00acc00c"></a> `00acc00c` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00acc010"></a> `00acc010` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00acc014"></a> `00acc014` | `63 1f 06 94` | bl 0x00c53da0 | `UNCONDITIONAL_CALL`
<a id="insn-00acc018"></a> `00acc018` | `00 fe ff b5` | cbnz x0,0x00acbfd8 | `CONDITIONAL_JUMP`
<a id="insn-00acc01c"></a> `00acc01c` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00acc020"></a> `00acc020` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00acc024"></a> `00acc024` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00acc028"></a> `00acc028` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00acc02c"></a> `00acc02c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00acc030"></a> `00acc030` | `c8 2f 06 94` | bl 0x00c57f50 | `UNCONDITIONAL_CALL`
<a id="insn-00acc034"></a> `00acc034` | `e9 ff ff 17` | b 0x00acbfd8 | `UNCONDITIONAL_JUMP`
<a id="insn-00acc038"></a> `00acc038` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00acc03c"></a> `00acc03c` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00acc040"></a> `00acc040` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00acc044"></a> `00acc044` | `01 02 00 54` | b.ne 0x00acc084 | `CONDITIONAL_JUMP`
<a id="insn-00acc048"></a> `00acc048` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00acc04c"></a> `00acc04c` | `f6 57 44 a9` | ldp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00acc050"></a> `00acc050` | `f8 5f 43 a9` | ldp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00acc054"></a> `00acc054` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00acc058"></a> `00acc058` | `ff 83 01 91` | add sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00acc05c"></a> `00acc05c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00acc084"></a> `00acc084` | `cb 2f 06 94` | bl 0x00c57fb0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00acbf9c`](#insn-00acbf9c) 範囲 `[['00acbf9c', '00acbfcf']]`
  - `CONDITIONAL_JUMP` [`00acbfcc`](#insn-00acbfcc) → [`00acc038`](#insn-00acc038)
  - `FALL_THROUGH` [`00acbfcc`](#insn-00acbfcc) → [`00acbfd0`](#insn-00acbfd0)
- ブロック [`00acbfd0`](#insn-00acbfd0) 範囲 `[['00acbfd0', '00acbfd7']]`
  - `UNCONDITIONAL_JUMP` [`00acbfd4`](#insn-00acbfd4) → [`00acbfe4`](#insn-00acbfe4)
- ブロック [`00acbfd8`](#insn-00acbfd8) 範囲 `[['00acbfd8', '00acbfe3']]`
  - `CONDITIONAL_JUMP` [`00acbfe0`](#insn-00acbfe0) → [`00acc038`](#insn-00acc038)
  - `FALL_THROUGH` [`00acbfe0`](#insn-00acbfe0) → [`00acbfe4`](#insn-00acbfe4)
- ブロック [`00acbfe4`](#insn-00acbfe4) 範囲 `[['00acbfe4', '00acbfef']]`
  - `CONDITIONAL_JUMP` [`00acbfec`](#insn-00acbfec) → [`00acbffc`](#insn-00acbffc)
  - `FALL_THROUGH` [`00acbfec`](#insn-00acbfec) → [`00acbff0`](#insn-00acbff0)
- ブロック [`00acbff0`](#insn-00acbff0) 範囲 `[['00acbff0', '00acbffb']]`
  - `FALL_THROUGH` [`00acbff8`](#insn-00acbff8) → [`00acbffc`](#insn-00acbffc)
- ブロック [`00acbffc`](#insn-00acbffc) 範囲 `[['00acbffc', '00acc00b']]`
  - `CONDITIONAL_JUMP` [`00acc008`](#insn-00acc008) → [`00acbfd8`](#insn-00acbfd8)
  - `FALL_THROUGH` [`00acc008`](#insn-00acc008) → [`00acc00c`](#insn-00acc00c)
- ブロック [`00acc00c`](#insn-00acc00c) 範囲 `[['00acc00c', '00acc01b']]`
  - `CONDITIONAL_JUMP` [`00acc018`](#insn-00acc018) → [`00acbfd8`](#insn-00acbfd8)
  - `FALL_THROUGH` [`00acc018`](#insn-00acc018) → [`00acc01c`](#insn-00acc01c)
- ブロック [`00acc01c`](#insn-00acc01c) 範囲 `[['00acc01c', '00acc037']]`
  - `UNCONDITIONAL_JUMP` [`00acc034`](#insn-00acc034) → [`00acbfd8`](#insn-00acbfd8)
- ブロック [`00acc038`](#insn-00acc038) 範囲 `[['00acc038', '00acc047']]`
  - `CONDITIONAL_JUMP` [`00acc044`](#insn-00acc044) → [`00acc084`](#insn-00acc084)
  - `FALL_THROUGH` [`00acc044`](#insn-00acc044) → [`00acc048`](#insn-00acc048)
- ブロック [`00acc048`](#insn-00acc048) 範囲 `[['00acc048', '00acc05f']]`
- ブロック [`00acc084`](#insn-00acc084) 範囲 `[['00acc084', '00acc087']]`

## 命令位置別の参照

- [`00acbfa0`](#insn-00acbfa0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbfa4`](#insn-00acbfa4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbfa8`](#insn-00acbfa8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbfac`](#insn-00acbfac) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbfbc`](#insn-00acbfbc) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbfcc`](#insn-00acbfcc) → [`00acc038`](#insn-00acc038) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbfd4`](#insn-00acbfd4) → [`00acbfe4`](#insn-00acbfe4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbfe0`](#insn-00acbfe0) → [`00acc038`](#insn-00acc038) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbfe8`](#insn-00acbfe8) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbfec`](#insn-00acbfec) → [`00acbffc`](#insn-00acbffc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbff8`](#insn-00acbff8) → [`00c53d70`](../00c53/00c53d70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53d70` · 推定シンボル `None` · 推定型 `None`
- [`00acc004`](#insn-00acc004) → [`00acbf9c`](#insn-00acbf9c) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00acbf9c` · 推定シンボル `None` · 推定型 `None`
- [`00acc008`](#insn-00acc008) → [`00acbfd8`](#insn-00acbfd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acc014`](#insn-00acc014) → [`00c53da0`](../00c53/00c53da0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53da0` · 推定シンボル `None` · 推定型 `None`
- [`00acc018`](#insn-00acc018) → [`00acbfd8`](#insn-00acbfd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acc030`](#insn-00acc030) → [`00c57f50`](../00c57/00c57f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f50` · 推定シンボル `None` · 推定型 `None`
- [`00acc034`](#insn-00acc034) → [`00acbfd8`](#insn-00acbfd8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acc03c`](#insn-00acc03c) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acc044`](#insn-00acc044) → [`00acc084`](#insn-00acc084) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acc048`](#insn-00acc048) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acc04c`](#insn-00acc04c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acc050`](#insn-00acc050) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acc054`](#insn-00acc054) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acc084`](#insn-00acc084) → [`00c57fb0`](../00c57/00c57fb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fb0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00acbfa0`](#insn-00acbfa0)

~~~json
{
  "source": "00acbfa0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbfa4`](#insn-00acbfa4)

~~~json
{
  "source": "00acbfa4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbfa8`](#insn-00acbfa8)

~~~json
{
  "source": "00acbfa8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbfac`](#insn-00acbfac)

~~~json
{
  "source": "00acbfac",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbfbc`](#insn-00acbfbc)

~~~json
{
  "source": "00acbfbc",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbfcc`](#insn-00acbfcc)

~~~json
{
  "source": "00acbfcc",
  "target": "00acc038",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbfd4`](#insn-00acbfd4)

~~~json
{
  "source": "00acbfd4",
  "target": "00acbfe4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbfe0`](#insn-00acbfe0)

~~~json
{
  "source": "00acbfe0",
  "target": "00acc038",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbfe8`](#insn-00acbfe8)

~~~json
{
  "source": "00acbfe8",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbfec`](#insn-00acbfec)

~~~json
{
  "source": "00acbfec",
  "target": "00acbffc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbff8`](#insn-00acbff8)

~~~json
{
  "source": "00acbff8",
  "target": "00c53d70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acc004`](#insn-00acc004)

~~~json
{
  "source": "00acc004",
  "target": "00acbf9c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acc008`](#insn-00acc008)

~~~json
{
  "source": "00acc008",
  "target": "00acbfd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acc014`](#insn-00acc014)

~~~json
{
  "source": "00acc014",
  "target": "00c53da0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acc018`](#insn-00acc018)

~~~json
{
  "source": "00acc018",
  "target": "00acbfd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acc030`](#insn-00acc030)

~~~json
{
  "source": "00acc030",
  "target": "00c57f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acc034`](#insn-00acc034)

~~~json
{
  "source": "00acc034",
  "target": "00acbfd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acc03c`](#insn-00acc03c)

~~~json
{
  "source": "00acc03c",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acc044`](#insn-00acc044)

~~~json
{
  "source": "00acc044",
  "target": "00acc084",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acc048`](#insn-00acc048)

~~~json
{
  "source": "00acc048",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acc04c`](#insn-00acc04c)

~~~json
{
  "source": "00acc04c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acc050`](#insn-00acc050)

~~~json
{
  "source": "00acc050",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acc054`](#insn-00acc054)

~~~json
{
  "source": "00acc054",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acc084`](#insn-00acc084)

~~~json
{
  "source": "00acc084",
  "target": "00c57fb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
