# 00acccb8

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00acbcc4`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acb/00acbcc4.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0028.md#compare-d7ae66b7c4c2dad31b6c990d24507445)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acccb8",
  "name": "FUN_00acccb8",
  "size": 212,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1b76fd1b49085e1a594e25b77b123108156dea8e0c0403904b224cfbe2ea234c",
  "source_text_sha256": "1b76fd1b49085e1a594e25b77b123108156dea8e0c0403904b224cfbe2ea234c",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00acccb8",
        "00accd87"
      ],
      [
        "00accdac",
        "00accdaf"
      ]
    ],
    "bytes_sha256": "a2d1e2c0cf6c453f922ba90854ed0fd914ca5484587df70e3a54d7e5b0619a0f",
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

- [00c54d60](../00c54/00c54d60.md)
- [00c54d90](../00c54/00c54d90.md)
- [00c58f20](../00c58/00c58f20.md)
- [00c58f80](../00c58/00c58f80.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1004 bytes

~~~c

void FUN_00acccb8(long param_1,undefined8 param_2)

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
        FUN_00c54d60(1,plVar4 + 1);
      }
      (**(code **)(*plVar2 + 8))(plVar2,param_2);
      if ((plVar4 != (long *)0x0) &&
         (lVar6 = FUN_00c54d90(0xffffffffffffffff,plVar4 + 1), lVar6 == 0)) {
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
<a id="insn-00acccb8"></a> `00acccb8` | `ff 83 01 d1` | sub sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00acccbc"></a> `00acccbc` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00acccc0"></a> `00acccc0` | `f8 5f 03 a9` | stp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00acccc4"></a> `00acccc4` | `f6 57 04 a9` | stp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00acccc8"></a> `00acccc8` | `f4 4f 05 a9` | stp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00accccc"></a> `00accccc` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00acccd0"></a> `00acccd0` | `56 d0 3b d5` | mrs x22,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00acccd4"></a> `00acccd4` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00acccd8"></a> `00acccd8` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00acccdc"></a> `00acccdc` | `08 a0 40 39` | ldrb w8,[x0, #0x28] | `FALL_THROUGH`
<a id="insn-00accce0"></a> `00accce0` | `08 04 00 34` | cbz w8,0x00accd60 | `CONDITIONAL_JUMP`
<a id="insn-00accce4"></a> `00accce4` | `17 60 44 a9` | ldp x23,x24,[x0, #0x40] | `FALL_THROUGH`
<a id="insn-00accce8"></a> `00accce8` | `ff 02 18 eb` | cmp x23,x24 | `FALL_THROUGH`
<a id="insn-00acccec"></a> `00acccec` | `a0 03 00 54` | b.eq 0x00accd60 | `CONDITIONAL_JUMP`
<a id="insn-00acccf0"></a> `00acccf0` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00acccf4"></a> `00acccf4` | `04 00 00 14` | b 0x00accd04 | `UNCONDITIONAL_JUMP`
<a id="insn-00acccf8"></a> `00acccf8` | `f7 42 00 91` | add x23,x23,#0x10 | `FALL_THROUGH`
<a id="insn-00acccfc"></a> `00acccfc` | `ff 02 18 eb` | cmp x23,x24 | `FALL_THROUGH`
<a id="insn-00accd00"></a> `00accd00` | `00 03 00 54` | b.eq 0x00accd60 | `CONDITIONAL_JUMP`
<a id="insn-00accd04"></a> `00accd04` | `f5 52 40 a9` | ldp x21,x20,[x23] | `FALL_THROUGH`
<a id="insn-00accd08"></a> `00accd08` | `f5 d3 00 a9` | stp x21,x20,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00accd0c"></a> `00accd0c` | `94 00 00 b4` | cbz x20,0x00accd1c | `CONDITIONAL_JUMP`
<a id="insn-00accd10"></a> `00accd10` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00accd14"></a> `00accd14` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00accd18"></a> `00accd18` | `12 20 06 94` | bl 0x00c54d60 | `UNCONDITIONAL_CALL`
<a id="insn-00accd1c"></a> `00accd1c` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00accd20"></a> `00accd20` | `08 05 40 f9` | ldr x8,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00accd24"></a> `00accd24` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00accd28"></a> `00accd28` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00accd2c"></a> `00accd2c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00accd30"></a> `00accd30` | `54 fe ff b4` | cbz x20,0x00acccf8 | `CONDITIONAL_JUMP`
<a id="insn-00accd34"></a> `00accd34` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00accd38"></a> `00accd38` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00accd3c"></a> `00accd3c` | `15 20 06 94` | bl 0x00c54d90 | `UNCONDITIONAL_CALL`
<a id="insn-00accd40"></a> `00accd40` | `c0 fd ff b5` | cbnz x0,0x00acccf8 | `CONDITIONAL_JUMP`
<a id="insn-00accd44"></a> `00accd44` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00accd48"></a> `00accd48` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00accd4c"></a> `00accd4c` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00accd50"></a> `00accd50` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00accd54"></a> `00accd54` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00accd58"></a> `00accd58` | `72 30 06 94` | bl 0x00c58f20 | `UNCONDITIONAL_CALL`
<a id="insn-00accd5c"></a> `00accd5c` | `e7 ff ff 17` | b 0x00acccf8 | `UNCONDITIONAL_JUMP`
<a id="insn-00accd60"></a> `00accd60` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00accd64"></a> `00accd64` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00accd68"></a> `00accd68` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00accd6c"></a> `00accd6c` | `01 02 00 54` | b.ne 0x00accdac | `CONDITIONAL_JUMP`
<a id="insn-00accd70"></a> `00accd70` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00accd74"></a> `00accd74` | `f6 57 44 a9` | ldp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00accd78"></a> `00accd78` | `f8 5f 43 a9` | ldp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00accd7c"></a> `00accd7c` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00accd80"></a> `00accd80` | `ff 83 01 91` | add sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00accd84"></a> `00accd84` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00accdac"></a> `00accdac` | `75 30 06 94` | bl 0x00c58f80 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00acccb8`](#insn-00acccb8) 範囲 `[['00acccb8', '00accce3']]`
  - `CONDITIONAL_JUMP` [`00accce0`](#insn-00accce0) → [`00accd60`](#insn-00accd60)
  - `FALL_THROUGH` [`00accce0`](#insn-00accce0) → [`00accce4`](#insn-00accce4)
- ブロック [`00accce4`](#insn-00accce4) 範囲 `[['00accce4', '00acccef']]`
  - `CONDITIONAL_JUMP` [`00acccec`](#insn-00acccec) → [`00accd60`](#insn-00accd60)
  - `FALL_THROUGH` [`00acccec`](#insn-00acccec) → [`00acccf0`](#insn-00acccf0)
- ブロック [`00acccf0`](#insn-00acccf0) 範囲 `[['00acccf0', '00acccf7']]`
  - `UNCONDITIONAL_JUMP` [`00acccf4`](#insn-00acccf4) → [`00accd04`](#insn-00accd04)
- ブロック [`00acccf8`](#insn-00acccf8) 範囲 `[['00acccf8', '00accd03']]`
  - `CONDITIONAL_JUMP` [`00accd00`](#insn-00accd00) → [`00accd60`](#insn-00accd60)
  - `FALL_THROUGH` [`00accd00`](#insn-00accd00) → [`00accd04`](#insn-00accd04)
- ブロック [`00accd04`](#insn-00accd04) 範囲 `[['00accd04', '00accd0f']]`
  - `CONDITIONAL_JUMP` [`00accd0c`](#insn-00accd0c) → [`00accd1c`](#insn-00accd1c)
  - `FALL_THROUGH` [`00accd0c`](#insn-00accd0c) → [`00accd10`](#insn-00accd10)
- ブロック [`00accd10`](#insn-00accd10) 範囲 `[['00accd10', '00accd1b']]`
  - `FALL_THROUGH` [`00accd18`](#insn-00accd18) → [`00accd1c`](#insn-00accd1c)
- ブロック [`00accd1c`](#insn-00accd1c) 範囲 `[['00accd1c', '00accd33']]`
  - `CONDITIONAL_JUMP` [`00accd30`](#insn-00accd30) → [`00acccf8`](#insn-00acccf8)
  - `FALL_THROUGH` [`00accd30`](#insn-00accd30) → [`00accd34`](#insn-00accd34)
- ブロック [`00accd34`](#insn-00accd34) 範囲 `[['00accd34', '00accd43']]`
  - `CONDITIONAL_JUMP` [`00accd40`](#insn-00accd40) → [`00acccf8`](#insn-00acccf8)
  - `FALL_THROUGH` [`00accd40`](#insn-00accd40) → [`00accd44`](#insn-00accd44)
- ブロック [`00accd44`](#insn-00accd44) 範囲 `[['00accd44', '00accd5f']]`
  - `UNCONDITIONAL_JUMP` [`00accd5c`](#insn-00accd5c) → [`00acccf8`](#insn-00acccf8)
- ブロック [`00accd60`](#insn-00accd60) 範囲 `[['00accd60', '00accd6f']]`
  - `CONDITIONAL_JUMP` [`00accd6c`](#insn-00accd6c) → [`00accdac`](#insn-00accdac)
  - `FALL_THROUGH` [`00accd6c`](#insn-00accd6c) → [`00accd70`](#insn-00accd70)
- ブロック [`00accd70`](#insn-00accd70) 範囲 `[['00accd70', '00accd87']]`
- ブロック [`00accdac`](#insn-00accdac) 範囲 `[['00accdac', '00accdaf']]`

## 命令位置別の参照

- [`00acccbc`](#insn-00acccbc) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acccc0`](#insn-00acccc0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acccc4`](#insn-00acccc4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acccc8`](#insn-00acccc8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acccd8`](#insn-00acccd8) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00accce0`](#insn-00accce0) → [`00accd60`](#insn-00accd60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acccec`](#insn-00acccec) → [`00accd60`](#insn-00accd60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acccf4`](#insn-00acccf4) → [`00accd04`](#insn-00accd04) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00accd00`](#insn-00accd00) → [`00accd60`](#insn-00accd60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00accd08`](#insn-00accd08) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00accd0c`](#insn-00accd0c) → [`00accd1c`](#insn-00accd1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00accd18`](#insn-00accd18) → [`00c54d60`](../00c54/00c54d60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c54d60` · 推定シンボル `None` · 推定型 `None`
- [`00accd30`](#insn-00accd30) → [`00acccf8`](#insn-00acccf8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00accd3c`](#insn-00accd3c) → [`00c54d90`](../00c54/00c54d90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c54d90` · 推定シンボル `None` · 推定型 `None`
- [`00accd40`](#insn-00accd40) → [`00acccf8`](#insn-00acccf8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00accd58`](#insn-00accd58) → [`00c58f20`](../00c58/00c58f20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f20` · 推定シンボル `None` · 推定型 `None`
- [`00accd5c`](#insn-00accd5c) → [`00acccf8`](#insn-00acccf8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00accd64`](#insn-00accd64) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00accd6c`](#insn-00accd6c) → [`00accdac`](#insn-00accdac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00accd70`](#insn-00accd70) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00accd74`](#insn-00accd74) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00accd78`](#insn-00accd78) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00accd7c`](#insn-00accd7c) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00accdac`](#insn-00accdac) → [`00c58f80`](../00c58/00c58f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f80` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00acccbc`](#insn-00acccbc)

~~~json
{
  "source": "00acccbc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acccc0`](#insn-00acccc0)

~~~json
{
  "source": "00acccc0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acccc4`](#insn-00acccc4)

~~~json
{
  "source": "00acccc4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acccc8`](#insn-00acccc8)

~~~json
{
  "source": "00acccc8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acccd8`](#insn-00acccd8)

~~~json
{
  "source": "00acccd8",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00accce0`](#insn-00accce0)

~~~json
{
  "source": "00accce0",
  "target": "00accd60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acccec`](#insn-00acccec)

~~~json
{
  "source": "00acccec",
  "target": "00accd60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acccf4`](#insn-00acccf4)

~~~json
{
  "source": "00acccf4",
  "target": "00accd04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00accd00`](#insn-00accd00)

~~~json
{
  "source": "00accd00",
  "target": "00accd60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00accd08`](#insn-00accd08)

~~~json
{
  "source": "00accd08",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00accd0c`](#insn-00accd0c)

~~~json
{
  "source": "00accd0c",
  "target": "00accd1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00accd18`](#insn-00accd18)

~~~json
{
  "source": "00accd18",
  "target": "00c54d60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00accd30`](#insn-00accd30)

~~~json
{
  "source": "00accd30",
  "target": "00acccf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00accd3c`](#insn-00accd3c)

~~~json
{
  "source": "00accd3c",
  "target": "00c54d90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00accd40`](#insn-00accd40)

~~~json
{
  "source": "00accd40",
  "target": "00acccf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00accd58`](#insn-00accd58)

~~~json
{
  "source": "00accd58",
  "target": "00c58f20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00accd5c`](#insn-00accd5c)

~~~json
{
  "source": "00accd5c",
  "target": "00acccf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00accd64`](#insn-00accd64)

~~~json
{
  "source": "00accd64",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00accd6c`](#insn-00accd6c)

~~~json
{
  "source": "00accd6c",
  "target": "00accdac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00accd70`](#insn-00accd70)

~~~json
{
  "source": "00accd70",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00accd74`](#insn-00accd74)

~~~json
{
  "source": "00accd74",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00accd78`](#insn-00accd78)

~~~json
{
  "source": "00accd78",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00accd7c`](#insn-00accd7c)

~~~json
{
  "source": "00accd7c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00accdac`](#insn-00accdac)

~~~json
{
  "source": "00accdac",
  "target": "00c58f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
