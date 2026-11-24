# 00acbb5c

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00acb960`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acb960.md) · 移動量 `+0x1fc`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0035.md#compare-f1aee4037deb0eba8c61ed3ca4d2b8e5)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00acbbcc`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acb/00acbbcc.md) · 移動量 `+0x70`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0034.md#compare-3dfdf3c7107c7c49938b965602b5332d)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acbb5c",
  "name": "FUN_00acbb5c",
  "size": 212,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1f37964a810c53d0625e7ee4094efae45b131d052d0bd3b89436b2af901911e1",
  "source_text_sha256": "1f37964a810c53d0625e7ee4094efae45b131d052d0bd3b89436b2af901911e1",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00acbb5c",
        "00acbc2b"
      ],
      [
        "00acbc50",
        "00acbc53"
      ]
    ],
    "bytes_sha256": "1c5e9633c3d2a105cbcea405c3b10aa9aa94a75af8aaeaa2a57264035e01792f",
    "instruction_count": 53,
    "instruction_bytes": 212,
    "body_bytes": 212,
    "indirect": 2,
    "unresolved": 2
  }
}
~~~

## 呼び出し元

- [00935b10](../00935/00935b10.md)

## 呼び出し先

- [00c53cd0](../00c53/00c53cd0.md)
- [00c53d00](../00c53/00c53d00.md)
- [00c57e80](../00c57/00c57e80.md)
- [00c57ee0](../00c57/00c57ee0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1010 bytes

~~~c

void FUN_00acbb5c(long param_1,undefined8 param_2)

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
        FUN_00c53cd0(1,plVar4 + 1);
      }
      (**(code **)*puVar2)(puVar2,param_2);
      if ((plVar4 != (long *)0x0) &&
         (lVar6 = FUN_00c53d00(0xffffffffffffffff,plVar4 + 1), lVar6 == 0)) {
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
<a id="insn-00acbb5c"></a> `00acbb5c` | `ff 83 01 d1` | sub sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00acbb60"></a> `00acbb60` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00acbb64"></a> `00acbb64` | `f8 5f 03 a9` | stp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00acbb68"></a> `00acbb68` | `f6 57 04 a9` | stp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00acbb6c"></a> `00acbb6c` | `f4 4f 05 a9` | stp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00acbb70"></a> `00acbb70` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00acbb74"></a> `00acbb74` | `56 d0 3b d5` | mrs x22,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00acbb78"></a> `00acbb78` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00acbb7c"></a> `00acbb7c` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00acbb80"></a> `00acbb80` | `08 a0 40 39` | ldrb w8,[x0, #0x28] | `FALL_THROUGH`
<a id="insn-00acbb84"></a> `00acbb84` | `08 04 00 34` | cbz w8,0x00acbc04 | `CONDITIONAL_JUMP`
<a id="insn-00acbb88"></a> `00acbb88` | `17 60 44 a9` | ldp x23,x24,[x0, #0x40] | `FALL_THROUGH`
<a id="insn-00acbb8c"></a> `00acbb8c` | `ff 02 18 eb` | cmp x23,x24 | `FALL_THROUGH`
<a id="insn-00acbb90"></a> `00acbb90` | `a0 03 00 54` | b.eq 0x00acbc04 | `CONDITIONAL_JUMP`
<a id="insn-00acbb94"></a> `00acbb94` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00acbb98"></a> `00acbb98` | `04 00 00 14` | b 0x00acbba8 | `UNCONDITIONAL_JUMP`
<a id="insn-00acbb9c"></a> `00acbb9c` | `f7 42 00 91` | add x23,x23,#0x10 | `FALL_THROUGH`
<a id="insn-00acbba0"></a> `00acbba0` | `ff 02 18 eb` | cmp x23,x24 | `FALL_THROUGH`
<a id="insn-00acbba4"></a> `00acbba4` | `00 03 00 54` | b.eq 0x00acbc04 | `CONDITIONAL_JUMP`
<a id="insn-00acbba8"></a> `00acbba8` | `f5 52 40 a9` | ldp x21,x20,[x23] | `FALL_THROUGH`
<a id="insn-00acbbac"></a> `00acbbac` | `f5 d3 00 a9` | stp x21,x20,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00acbbb0"></a> `00acbbb0` | `94 00 00 b4` | cbz x20,0x00acbbc0 | `CONDITIONAL_JUMP`
<a id="insn-00acbbb4"></a> `00acbbb4` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00acbbb8"></a> `00acbbb8` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00acbbbc"></a> `00acbbbc` | `45 20 06 94` | bl 0x00c53cd0 | `UNCONDITIONAL_CALL`
<a id="insn-00acbbc0"></a> `00acbbc0` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00acbbc4"></a> `00acbbc4` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00acbbc8"></a> `00acbbc8` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00acbbcc"></a> `00acbbcc` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00acbbd0"></a> `00acbbd0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00acbbd4"></a> `00acbbd4` | `54 fe ff b4` | cbz x20,0x00acbb9c | `CONDITIONAL_JUMP`
<a id="insn-00acbbd8"></a> `00acbbd8` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00acbbdc"></a> `00acbbdc` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00acbbe0"></a> `00acbbe0` | `48 20 06 94` | bl 0x00c53d00 | `UNCONDITIONAL_CALL`
<a id="insn-00acbbe4"></a> `00acbbe4` | `c0 fd ff b5` | cbnz x0,0x00acbb9c | `CONDITIONAL_JUMP`
<a id="insn-00acbbe8"></a> `00acbbe8` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00acbbec"></a> `00acbbec` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00acbbf0"></a> `00acbbf0` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00acbbf4"></a> `00acbbf4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00acbbf8"></a> `00acbbf8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00acbbfc"></a> `00acbbfc` | `a1 30 06 94` | bl 0x00c57e80 | `UNCONDITIONAL_CALL`
<a id="insn-00acbc00"></a> `00acbc00` | `e7 ff ff 17` | b 0x00acbb9c | `UNCONDITIONAL_JUMP`
<a id="insn-00acbc04"></a> `00acbc04` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00acbc08"></a> `00acbc08` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00acbc0c"></a> `00acbc0c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00acbc10"></a> `00acbc10` | `01 02 00 54` | b.ne 0x00acbc50 | `CONDITIONAL_JUMP`
<a id="insn-00acbc14"></a> `00acbc14` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00acbc18"></a> `00acbc18` | `f6 57 44 a9` | ldp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00acbc1c"></a> `00acbc1c` | `f8 5f 43 a9` | ldp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00acbc20"></a> `00acbc20` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00acbc24"></a> `00acbc24` | `ff 83 01 91` | add sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00acbc28"></a> `00acbc28` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00acbc50"></a> `00acbc50` | `a4 30 06 94` | bl 0x00c57ee0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00acbb5c`](#insn-00acbb5c) 範囲 `[['00acbb5c', '00acbb87']]`
  - `CONDITIONAL_JUMP` [`00acbb84`](#insn-00acbb84) → [`00acbc04`](#insn-00acbc04)
  - `FALL_THROUGH` [`00acbb84`](#insn-00acbb84) → [`00acbb88`](#insn-00acbb88)
- ブロック [`00acbb88`](#insn-00acbb88) 範囲 `[['00acbb88', '00acbb93']]`
  - `CONDITIONAL_JUMP` [`00acbb90`](#insn-00acbb90) → [`00acbc04`](#insn-00acbc04)
  - `FALL_THROUGH` [`00acbb90`](#insn-00acbb90) → [`00acbb94`](#insn-00acbb94)
- ブロック [`00acbb94`](#insn-00acbb94) 範囲 `[['00acbb94', '00acbb9b']]`
  - `UNCONDITIONAL_JUMP` [`00acbb98`](#insn-00acbb98) → [`00acbba8`](#insn-00acbba8)
- ブロック [`00acbb9c`](#insn-00acbb9c) 範囲 `[['00acbb9c', '00acbba7']]`
  - `CONDITIONAL_JUMP` [`00acbba4`](#insn-00acbba4) → [`00acbc04`](#insn-00acbc04)
  - `FALL_THROUGH` [`00acbba4`](#insn-00acbba4) → [`00acbba8`](#insn-00acbba8)
- ブロック [`00acbba8`](#insn-00acbba8) 範囲 `[['00acbba8', '00acbbb3']]`
  - `CONDITIONAL_JUMP` [`00acbbb0`](#insn-00acbbb0) → [`00acbbc0`](#insn-00acbbc0)
  - `FALL_THROUGH` [`00acbbb0`](#insn-00acbbb0) → [`00acbbb4`](#insn-00acbbb4)
- ブロック [`00acbbb4`](#insn-00acbbb4) 範囲 `[['00acbbb4', '00acbbbf']]`
  - `FALL_THROUGH` [`00acbbbc`](#insn-00acbbbc) → [`00acbbc0`](#insn-00acbbc0)
- ブロック [`00acbbc0`](#insn-00acbbc0) 範囲 `[['00acbbc0', '00acbbd7']]`
  - `CONDITIONAL_JUMP` [`00acbbd4`](#insn-00acbbd4) → [`00acbb9c`](#insn-00acbb9c)
  - `FALL_THROUGH` [`00acbbd4`](#insn-00acbbd4) → [`00acbbd8`](#insn-00acbbd8)
- ブロック [`00acbbd8`](#insn-00acbbd8) 範囲 `[['00acbbd8', '00acbbe7']]`
  - `CONDITIONAL_JUMP` [`00acbbe4`](#insn-00acbbe4) → [`00acbb9c`](#insn-00acbb9c)
  - `FALL_THROUGH` [`00acbbe4`](#insn-00acbbe4) → [`00acbbe8`](#insn-00acbbe8)
- ブロック [`00acbbe8`](#insn-00acbbe8) 範囲 `[['00acbbe8', '00acbc03']]`
  - `UNCONDITIONAL_JUMP` [`00acbc00`](#insn-00acbc00) → [`00acbb9c`](#insn-00acbb9c)
- ブロック [`00acbc04`](#insn-00acbc04) 範囲 `[['00acbc04', '00acbc13']]`
  - `CONDITIONAL_JUMP` [`00acbc10`](#insn-00acbc10) → [`00acbc50`](#insn-00acbc50)
  - `FALL_THROUGH` [`00acbc10`](#insn-00acbc10) → [`00acbc14`](#insn-00acbc14)
- ブロック [`00acbc14`](#insn-00acbc14) 範囲 `[['00acbc14', '00acbc2b']]`
- ブロック [`00acbc50`](#insn-00acbc50) 範囲 `[['00acbc50', '00acbc53']]`

## 命令位置別の参照

- [`00acbb60`](#insn-00acbb60) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbb64`](#insn-00acbb64) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbb68`](#insn-00acbb68) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbb6c`](#insn-00acbb6c) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbb7c`](#insn-00acbb7c) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbb84`](#insn-00acbb84) → [`00acbc04`](#insn-00acbc04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbb90`](#insn-00acbb90) → [`00acbc04`](#insn-00acbc04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbb98`](#insn-00acbb98) → [`00acbba8`](#insn-00acbba8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbba4`](#insn-00acbba4) → [`00acbc04`](#insn-00acbc04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbbac`](#insn-00acbbac) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbbb0`](#insn-00acbbb0) → [`00acbbc0`](#insn-00acbbc0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbbbc`](#insn-00acbbbc) → [`00c53cd0`](../00c53/00c53cd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53cd0` · 推定シンボル `None` · 推定型 `None`
- [`00acbbd4`](#insn-00acbbd4) → [`00acbb9c`](#insn-00acbb9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbbe0`](#insn-00acbbe0) → [`00c53d00`](../00c53/00c53d00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53d00` · 推定シンボル `None` · 推定型 `None`
- [`00acbbe4`](#insn-00acbbe4) → [`00acbb9c`](#insn-00acbb9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbbfc`](#insn-00acbbfc) → [`00c57e80`](../00c57/00c57e80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e80` · 推定シンボル `None` · 推定型 `None`
- [`00acbc00`](#insn-00acbc00) → [`00acbb9c`](#insn-00acbb9c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbc08`](#insn-00acbc08) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbc10`](#insn-00acbc10) → [`00acbc50`](#insn-00acbc50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbc14`](#insn-00acbc14) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbc18`](#insn-00acbc18) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbc1c`](#insn-00acbc1c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbc20`](#insn-00acbc20) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbc50`](#insn-00acbc50) → [`00c57ee0`](../00c57/00c57ee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ee0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00acbb60`](#insn-00acbb60)

~~~json
{
  "source": "00acbb60",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbb64`](#insn-00acbb64)

~~~json
{
  "source": "00acbb64",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbb68`](#insn-00acbb68)

~~~json
{
  "source": "00acbb68",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbb6c`](#insn-00acbb6c)

~~~json
{
  "source": "00acbb6c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbb7c`](#insn-00acbb7c)

~~~json
{
  "source": "00acbb7c",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbb84`](#insn-00acbb84)

~~~json
{
  "source": "00acbb84",
  "target": "00acbc04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbb90`](#insn-00acbb90)

~~~json
{
  "source": "00acbb90",
  "target": "00acbc04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbb98`](#insn-00acbb98)

~~~json
{
  "source": "00acbb98",
  "target": "00acbba8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbba4`](#insn-00acbba4)

~~~json
{
  "source": "00acbba4",
  "target": "00acbc04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbbac`](#insn-00acbbac)

~~~json
{
  "source": "00acbbac",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbbb0`](#insn-00acbbb0)

~~~json
{
  "source": "00acbbb0",
  "target": "00acbbc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbbbc`](#insn-00acbbbc)

~~~json
{
  "source": "00acbbbc",
  "target": "00c53cd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbbd4`](#insn-00acbbd4)

~~~json
{
  "source": "00acbbd4",
  "target": "00acbb9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbbe0`](#insn-00acbbe0)

~~~json
{
  "source": "00acbbe0",
  "target": "00c53d00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbbe4`](#insn-00acbbe4)

~~~json
{
  "source": "00acbbe4",
  "target": "00acbb9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbbfc`](#insn-00acbbfc)

~~~json
{
  "source": "00acbbfc",
  "target": "00c57e80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbc00`](#insn-00acbc00)

~~~json
{
  "source": "00acbc00",
  "target": "00acbb9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbc08`](#insn-00acbc08)

~~~json
{
  "source": "00acbc08",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbc10`](#insn-00acbc10)

~~~json
{
  "source": "00acbc10",
  "target": "00acbc50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbc14`](#insn-00acbc14)

~~~json
{
  "source": "00acbc14",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbc18`](#insn-00acbc18)

~~~json
{
  "source": "00acbc18",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbc1c`](#insn-00acbc1c)

~~~json
{
  "source": "00acbc1c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbc20`](#insn-00acbc20)

~~~json
{
  "source": "00acbc20",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbc50`](#insn-00acbc50)

~~~json
{
  "source": "00acbc50",
  "target": "00c57ee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
