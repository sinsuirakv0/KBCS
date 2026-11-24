# 00accbc0

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00acbbcc`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acb/00acbbcc.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0028.md#compare-1a0ac0719df8a4e42d7fc8ed4771dda6)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00accbc0",
  "name": "FUN_00accbc0",
  "size": 212,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "63a8f838853dc1f6c67889319d67b91977f9607c2c10f3d6c5f5f5185f415bf6",
  "source_text_sha256": "63a8f838853dc1f6c67889319d67b91977f9607c2c10f3d6c5f5f5185f415bf6",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00accbc0",
        "00accc8f"
      ],
      [
        "00acccb4",
        "00acccb7"
      ]
    ],
    "bytes_sha256": "a569a3b4d2d61a9e7f965c9a77d540f6c7c7ceef09d380ed17d47a272a2d4b5f",
    "instruction_count": 53,
    "instruction_bytes": 212,
    "body_bytes": 212,
    "indirect": 2,
    "unresolved": 2
  }
}
~~~

## 呼び出し元

- [00936b10](../00936/00936b10.md)

## 呼び出し先

- [00c54d60](../00c54/00c54d60.md)
- [00c54d90](../00c54/00c54d90.md)
- [00c58f20](../00c58/00c58f20.md)
- [00c58f80](../00c58/00c58f80.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1010 bytes

~~~c

void FUN_00accbc0(long param_1,undefined8 param_2)

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
        FUN_00c54d60(1,plVar4 + 1);
      }
      (**(code **)*puVar2)(puVar2,param_2);
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
<a id="insn-00accbc0"></a> `00accbc0` | `ff 83 01 d1` | sub sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00accbc4"></a> `00accbc4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00accbc8"></a> `00accbc8` | `f8 5f 03 a9` | stp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00accbcc"></a> `00accbcc` | `f6 57 04 a9` | stp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00accbd0"></a> `00accbd0` | `f4 4f 05 a9` | stp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00accbd4"></a> `00accbd4` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00accbd8"></a> `00accbd8` | `56 d0 3b d5` | mrs x22,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00accbdc"></a> `00accbdc` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00accbe0"></a> `00accbe0` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00accbe4"></a> `00accbe4` | `08 a0 40 39` | ldrb w8,[x0, #0x28] | `FALL_THROUGH`
<a id="insn-00accbe8"></a> `00accbe8` | `08 04 00 34` | cbz w8,0x00accc68 | `CONDITIONAL_JUMP`
<a id="insn-00accbec"></a> `00accbec` | `17 60 44 a9` | ldp x23,x24,[x0, #0x40] | `FALL_THROUGH`
<a id="insn-00accbf0"></a> `00accbf0` | `ff 02 18 eb` | cmp x23,x24 | `FALL_THROUGH`
<a id="insn-00accbf4"></a> `00accbf4` | `a0 03 00 54` | b.eq 0x00accc68 | `CONDITIONAL_JUMP`
<a id="insn-00accbf8"></a> `00accbf8` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00accbfc"></a> `00accbfc` | `04 00 00 14` | b 0x00accc0c | `UNCONDITIONAL_JUMP`
<a id="insn-00accc00"></a> `00accc00` | `f7 42 00 91` | add x23,x23,#0x10 | `FALL_THROUGH`
<a id="insn-00accc04"></a> `00accc04` | `ff 02 18 eb` | cmp x23,x24 | `FALL_THROUGH`
<a id="insn-00accc08"></a> `00accc08` | `00 03 00 54` | b.eq 0x00accc68 | `CONDITIONAL_JUMP`
<a id="insn-00accc0c"></a> `00accc0c` | `f5 52 40 a9` | ldp x21,x20,[x23] | `FALL_THROUGH`
<a id="insn-00accc10"></a> `00accc10` | `f5 d3 00 a9` | stp x21,x20,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00accc14"></a> `00accc14` | `94 00 00 b4` | cbz x20,0x00accc24 | `CONDITIONAL_JUMP`
<a id="insn-00accc18"></a> `00accc18` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00accc1c"></a> `00accc1c` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00accc20"></a> `00accc20` | `50 20 06 94` | bl 0x00c54d60 | `UNCONDITIONAL_CALL`
<a id="insn-00accc24"></a> `00accc24` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00accc28"></a> `00accc28` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00accc2c"></a> `00accc2c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00accc30"></a> `00accc30` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00accc34"></a> `00accc34` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00accc38"></a> `00accc38` | `54 fe ff b4` | cbz x20,0x00accc00 | `CONDITIONAL_JUMP`
<a id="insn-00accc3c"></a> `00accc3c` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00accc40"></a> `00accc40` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00accc44"></a> `00accc44` | `53 20 06 94` | bl 0x00c54d90 | `UNCONDITIONAL_CALL`
<a id="insn-00accc48"></a> `00accc48` | `c0 fd ff b5` | cbnz x0,0x00accc00 | `CONDITIONAL_JUMP`
<a id="insn-00accc4c"></a> `00accc4c` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00accc50"></a> `00accc50` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00accc54"></a> `00accc54` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00accc58"></a> `00accc58` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00accc5c"></a> `00accc5c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00accc60"></a> `00accc60` | `b0 30 06 94` | bl 0x00c58f20 | `UNCONDITIONAL_CALL`
<a id="insn-00accc64"></a> `00accc64` | `e7 ff ff 17` | b 0x00accc00 | `UNCONDITIONAL_JUMP`
<a id="insn-00accc68"></a> `00accc68` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00accc6c"></a> `00accc6c` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00accc70"></a> `00accc70` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00accc74"></a> `00accc74` | `01 02 00 54` | b.ne 0x00acccb4 | `CONDITIONAL_JUMP`
<a id="insn-00accc78"></a> `00accc78` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00accc7c"></a> `00accc7c` | `f6 57 44 a9` | ldp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00accc80"></a> `00accc80` | `f8 5f 43 a9` | ldp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00accc84"></a> `00accc84` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00accc88"></a> `00accc88` | `ff 83 01 91` | add sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00accc8c"></a> `00accc8c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00acccb4"></a> `00acccb4` | `b3 30 06 94` | bl 0x00c58f80 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00accbc0`](#insn-00accbc0) 範囲 `[['00accbc0', '00accbeb']]`
  - `CONDITIONAL_JUMP` [`00accbe8`](#insn-00accbe8) → [`00accc68`](#insn-00accc68)
  - `FALL_THROUGH` [`00accbe8`](#insn-00accbe8) → [`00accbec`](#insn-00accbec)
- ブロック [`00accbec`](#insn-00accbec) 範囲 `[['00accbec', '00accbf7']]`
  - `CONDITIONAL_JUMP` [`00accbf4`](#insn-00accbf4) → [`00accc68`](#insn-00accc68)
  - `FALL_THROUGH` [`00accbf4`](#insn-00accbf4) → [`00accbf8`](#insn-00accbf8)
- ブロック [`00accbf8`](#insn-00accbf8) 範囲 `[['00accbf8', '00accbff']]`
  - `UNCONDITIONAL_JUMP` [`00accbfc`](#insn-00accbfc) → [`00accc0c`](#insn-00accc0c)
- ブロック [`00accc00`](#insn-00accc00) 範囲 `[['00accc00', '00accc0b']]`
  - `CONDITIONAL_JUMP` [`00accc08`](#insn-00accc08) → [`00accc68`](#insn-00accc68)
  - `FALL_THROUGH` [`00accc08`](#insn-00accc08) → [`00accc0c`](#insn-00accc0c)
- ブロック [`00accc0c`](#insn-00accc0c) 範囲 `[['00accc0c', '00accc17']]`
  - `CONDITIONAL_JUMP` [`00accc14`](#insn-00accc14) → [`00accc24`](#insn-00accc24)
  - `FALL_THROUGH` [`00accc14`](#insn-00accc14) → [`00accc18`](#insn-00accc18)
- ブロック [`00accc18`](#insn-00accc18) 範囲 `[['00accc18', '00accc23']]`
  - `FALL_THROUGH` [`00accc20`](#insn-00accc20) → [`00accc24`](#insn-00accc24)
- ブロック [`00accc24`](#insn-00accc24) 範囲 `[['00accc24', '00accc3b']]`
  - `CONDITIONAL_JUMP` [`00accc38`](#insn-00accc38) → [`00accc00`](#insn-00accc00)
  - `FALL_THROUGH` [`00accc38`](#insn-00accc38) → [`00accc3c`](#insn-00accc3c)
- ブロック [`00accc3c`](#insn-00accc3c) 範囲 `[['00accc3c', '00accc4b']]`
  - `CONDITIONAL_JUMP` [`00accc48`](#insn-00accc48) → [`00accc00`](#insn-00accc00)
  - `FALL_THROUGH` [`00accc48`](#insn-00accc48) → [`00accc4c`](#insn-00accc4c)
- ブロック [`00accc4c`](#insn-00accc4c) 範囲 `[['00accc4c', '00accc67']]`
  - `UNCONDITIONAL_JUMP` [`00accc64`](#insn-00accc64) → [`00accc00`](#insn-00accc00)
- ブロック [`00accc68`](#insn-00accc68) 範囲 `[['00accc68', '00accc77']]`
  - `CONDITIONAL_JUMP` [`00accc74`](#insn-00accc74) → [`00acccb4`](#insn-00acccb4)
  - `FALL_THROUGH` [`00accc74`](#insn-00accc74) → [`00accc78`](#insn-00accc78)
- ブロック [`00accc78`](#insn-00accc78) 範囲 `[['00accc78', '00accc8f']]`
- ブロック [`00acccb4`](#insn-00acccb4) 範囲 `[['00acccb4', '00acccb7']]`

## 命令位置別の参照

- [`00accbc4`](#insn-00accbc4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00accbc8`](#insn-00accbc8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00accbcc`](#insn-00accbcc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00accbd0`](#insn-00accbd0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00accbe0`](#insn-00accbe0) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00accbe8`](#insn-00accbe8) → [`00accc68`](#insn-00accc68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00accbf4`](#insn-00accbf4) → [`00accc68`](#insn-00accc68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00accbfc`](#insn-00accbfc) → [`00accc0c`](#insn-00accc0c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00accc08`](#insn-00accc08) → [`00accc68`](#insn-00accc68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00accc10`](#insn-00accc10) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00accc14`](#insn-00accc14) → [`00accc24`](#insn-00accc24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00accc20`](#insn-00accc20) → [`00c54d60`](../00c54/00c54d60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c54d60` · 推定シンボル `None` · 推定型 `None`
- [`00accc38`](#insn-00accc38) → [`00accc00`](#insn-00accc00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00accc44`](#insn-00accc44) → [`00c54d90`](../00c54/00c54d90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c54d90` · 推定シンボル `None` · 推定型 `None`
- [`00accc48`](#insn-00accc48) → [`00accc00`](#insn-00accc00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00accc60`](#insn-00accc60) → [`00c58f20`](../00c58/00c58f20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f20` · 推定シンボル `None` · 推定型 `None`
- [`00accc64`](#insn-00accc64) → [`00accc00`](#insn-00accc00) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00accc6c`](#insn-00accc6c) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00accc74`](#insn-00accc74) → [`00acccb4`](#insn-00acccb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00accc78`](#insn-00accc78) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00accc7c`](#insn-00accc7c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00accc80`](#insn-00accc80) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00accc84`](#insn-00accc84) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acccb4`](#insn-00acccb4) → [`00c58f80`](../00c58/00c58f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f80` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00accbc4`](#insn-00accbc4)

~~~json
{
  "source": "00accbc4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00accbc8`](#insn-00accbc8)

~~~json
{
  "source": "00accbc8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00accbcc`](#insn-00accbcc)

~~~json
{
  "source": "00accbcc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00accbd0`](#insn-00accbd0)

~~~json
{
  "source": "00accbd0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00accbe0`](#insn-00accbe0)

~~~json
{
  "source": "00accbe0",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00accbe8`](#insn-00accbe8)

~~~json
{
  "source": "00accbe8",
  "target": "00accc68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00accbf4`](#insn-00accbf4)

~~~json
{
  "source": "00accbf4",
  "target": "00accc68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00accbfc`](#insn-00accbfc)

~~~json
{
  "source": "00accbfc",
  "target": "00accc0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00accc08`](#insn-00accc08)

~~~json
{
  "source": "00accc08",
  "target": "00accc68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00accc10`](#insn-00accc10)

~~~json
{
  "source": "00accc10",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00accc14`](#insn-00accc14)

~~~json
{
  "source": "00accc14",
  "target": "00accc24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00accc20`](#insn-00accc20)

~~~json
{
  "source": "00accc20",
  "target": "00c54d60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00accc38`](#insn-00accc38)

~~~json
{
  "source": "00accc38",
  "target": "00accc00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00accc44`](#insn-00accc44)

~~~json
{
  "source": "00accc44",
  "target": "00c54d90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00accc48`](#insn-00accc48)

~~~json
{
  "source": "00accc48",
  "target": "00accc00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00accc60`](#insn-00accc60)

~~~json
{
  "source": "00accc60",
  "target": "00c58f20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00accc64`](#insn-00accc64)

~~~json
{
  "source": "00accc64",
  "target": "00accc00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00accc6c`](#insn-00accc6c)

~~~json
{
  "source": "00accc6c",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00accc74`](#insn-00accc74)

~~~json
{
  "source": "00accc74",
  "target": "00acccb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00accc78`](#insn-00accc78)

~~~json
{
  "source": "00accc78",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00accc7c`](#insn-00accc7c)

~~~json
{
  "source": "00accc7c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00accc80`](#insn-00accc80)

~~~json
{
  "source": "00accc80",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00accc84`](#insn-00accc84)

~~~json
{
  "source": "00accc84",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acccb4`](#insn-00acccb4)

~~~json
{
  "source": "00acccb4",
  "target": "00c58f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
