# 00aeead0

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00a8f6a4`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8f/00a8f6a4.md) · 移動量 `+0x5f42c`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0053.md#compare-8e4c25ad1ec430e2acb5d7810815acb3)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00aeeef8`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aee/00aeeef8.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0065.md#compare-f1143d6370ce8db1ba79bd202a27bdcb)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aeead0",
  "name": "FUN_00aeead0",
  "size": 248,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3c490b71a15511ef97d2d2b4a6e870d85fb02aca96afa0aa1c210309822a972a",
  "source_text_sha256": "3c490b71a15511ef97d2d2b4a6e870d85fb02aca96afa0aa1c210309822a972a",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aeead0",
        "00aeebc3"
      ],
      [
        "00aeec10",
        "00aeec13"
      ]
    ],
    "bytes_sha256": "5885450b524820e98184f6d25b12f9a90d6579aa0e0157fa813d2497e18d95b3",
    "instruction_count": 62,
    "instruction_bytes": 248,
    "body_bytes": 248,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0047acb4](../0047a/0047acb4.md)
- [0047cd94](../0047c/0047cd94.md)
- [00658d6c](../00658/00658d6c.md)
- [00aeec90](../00aee/00aeec90.md)
- [00aeec94](../00aee/00aeec94.md)
- [00c57ae0](../00c57/00c57ae0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1623 bytes

~~~c

void FUN_00aeead0(long param_1,undefined8 param_2,int *param_3)

{
  int iVar1;
  long lVar2;
  undefined8 uVar3;
  undefined ***pppuVar4;
  undefined8 uVar5;
  long lVar6;
  undefined **local_60;
  long lStack_58;
  undefined8 local_50;
  long *local_40;
  long local_28;
  
  pppuVar4 = &local_60;
                    /* catch() { ... } // from try @ 00aee878 with catch @ 00aeead4
                       catch() { ... } // from try @ 00aeeab8 with catch @ 00aeead4 */
  lVar2 = tpidr_el0;
  local_28 = *(long *)(lVar2 + 0x28);
  iVar1 = *param_3;
  if (iVar1 == 4) {
    lStack_58 = *(long *)(param_1 + 8);
    local_50 = *(undefined8 *)(param_1 + 0x10);
    local_60 = &PTR_FUN_00c8db68;
    local_40 = (long *)&local_60;
    FUN_00658d6c(lStack_58 + 0x1fd8,local_50,&local_60);
    if ((undefined ***)local_40 == &local_60) {
      lVar6 = 0x20;
    }
    else {
      if (local_40 == (long *)0x0) goto LAB_00aeeba4;
      lVar6 = 0x28;
      pppuVar4 = (undefined ***)local_40;
    }
    (**(code **)((long)*pppuVar4 + lVar6))();
  }
  else {
    if (iVar1 == 3) {
      uVar3 = FUN_0047acb4();
      if (*(long *)(lVar2 + 0x28) == local_28) {
        uVar5 = 0xb;
        goto LAB_00aeeb38;
      }
      goto LAB_00aeec10;
    }
    if (iVar1 == 0) {
      uVar3 = FUN_0047acb4();
      if (*(long *)(lVar2 + 0x28) != local_28) goto LAB_00aeec10;
      uVar5 = 10;
LAB_00aeeb38:
      FUN_0047cd94(uVar3,uVar5,0);
      return;
    }
  }
LAB_00aeeba4:
  if (*(long *)(lVar2 + 0x28) == local_28) {
    return;
  }
LAB_00aeec10:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aeead0"></a> `00aeead0` | `ff 83 01 d1` | sub sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00aeead4"></a> `00aeead4` | `fd 7b 04 a9` | stp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00aeead8"></a> `00aeead8` | `f4 4f 05 a9` | stp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00aeeadc"></a> `00aeeadc` | `fd 03 01 91` | add x29,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00aeeae0"></a> `00aeeae0` | `54 d0 3b d5` | mrs x20,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00aeeae4"></a> `00aeeae4` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00aeeae8"></a> `00aeeae8` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aeeaec"></a> `00aeeaec` | `48 00 40 b9` | ldr w8,[x2] | `FALL_THROUGH`
<a id="insn-00aeeaf0"></a> `00aeeaf0` | `1f 11 00 71` | cmp w8,#0x4 | `FALL_THROUGH`
<a id="insn-00aeeaf4"></a> `00aeeaf4` | `c0 02 00 54` | b.eq 0x00aeeb4c | `CONDITIONAL_JUMP`
<a id="insn-00aeeaf8"></a> `00aeeaf8` | `1f 0d 00 71` | cmp w8,#0x3 | `FALL_THROUGH`
<a id="insn-00aeeafc"></a> `00aeeafc` | `20 01 00 54` | b.eq 0x00aeeb20 | `CONDITIONAL_JUMP`
<a id="insn-00aeeb00"></a> `00aeeb00` | `28 05 00 35` | cbnz w8,0x00aeeba4 | `CONDITIONAL_JUMP`
<a id="insn-00aeeb04"></a> `00aeeb04` | `6c 30 e6 97` | bl 0x0047acb4 | `UNCONDITIONAL_CALL`
<a id="insn-00aeeb08"></a> `00aeeb08` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00aeeb0c"></a> `00aeeb0c` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aeeb10"></a> `00aeeb10` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00aeeb14"></a> `00aeeb14` | `e1 07 00 54` | b.ne 0x00aeec10 | `CONDITIONAL_JUMP`
<a id="insn-00aeeb18"></a> `00aeeb18` | `41 01 80 52` | mov w1,#0xa | `FALL_THROUGH`
<a id="insn-00aeeb1c"></a> `00aeeb1c` | `07 00 00 14` | b 0x00aeeb38 | `UNCONDITIONAL_JUMP`
<a id="insn-00aeeb20"></a> `00aeeb20` | `65 30 e6 97` | bl 0x0047acb4 | `UNCONDITIONAL_CALL`
<a id="insn-00aeeb24"></a> `00aeeb24` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00aeeb28"></a> `00aeeb28` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aeeb2c"></a> `00aeeb2c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00aeeb30"></a> `00aeeb30` | `01 07 00 54` | b.ne 0x00aeec10 | `CONDITIONAL_JUMP`
<a id="insn-00aeeb34"></a> `00aeeb34` | `61 01 80 52` | mov w1,#0xb | `FALL_THROUGH`
<a id="insn-00aeeb38"></a> `00aeeb38` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00aeeb3c"></a> `00aeeb3c` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00aeeb40"></a> `00aeeb40` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00aeeb44"></a> `00aeeb44` | `ff 83 01 91` | add sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00aeeb48"></a> `00aeeb48` | `93 38 e6 17` | b 0x0047cd94 | `CALL_TERMINATOR`
<a id="insn-00aeeb4c"></a> `00aeeb4c` | `08 84 40 a9` | ldp x8,x1,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00aeeb50"></a> `00aeeb50` | `e9 0c 00 f0` | adrp x9,0xc8d000 | `FALL_THROUGH`
<a id="insn-00aeeb54"></a> `00aeeb54` | `29 a1 2d 91` | add x9,x9,#0xb68 | `FALL_THROUGH`
<a id="insn-00aeeb58"></a> `00aeeb58` | `f3 03 00 91` | mov x19,sp | `FALL_THROUGH`
<a id="insn-00aeeb5c"></a> `00aeeb5c` | `f3 13 00 f9` | str x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aeeb60"></a> `00aeeb60` | `e9 23 00 a9` | stp x9,x8,[sp] | `FALL_THROUGH`
<a id="insn-00aeeb64"></a> `00aeeb64` | `09 fb 83 52` | mov w9,#0x1fd8 | `FALL_THROUGH`
<a id="insn-00aeeb68"></a> `00aeeb68` | `e1 0b 00 f9` | str x1,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aeeb6c"></a> `00aeeb6c` | `00 01 09 8b` | add x0,x8,x9 | `FALL_THROUGH`
<a id="insn-00aeeb70"></a> `00aeeb70` | `e2 03 00 91` | mov x2,sp | `FALL_THROUGH`
<a id="insn-00aeeb74"></a> `00aeeb74` | `7e a8 ed 97` | bl 0x00658d6c | `UNCONDITIONAL_CALL`
<a id="insn-00aeeb78"></a> `00aeeb78` | `e0 13 40 f9` | ldr x0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aeeb7c"></a> `00aeeb7c` | `1f 00 13 eb` | cmp x0,x19 | `FALL_THROUGH`
<a id="insn-00aeeb80"></a> `00aeeb80` | `80 00 00 54` | b.eq 0x00aeeb90 | `CONDITIONAL_JUMP`
<a id="insn-00aeeb84"></a> `00aeeb84` | `00 01 00 b4` | cbz x0,0x00aeeba4 | `CONDITIONAL_JUMP`
<a id="insn-00aeeb88"></a> `00aeeb88` | `08 05 80 52` | mov w8,#0x28 | `FALL_THROUGH`
<a id="insn-00aeeb8c"></a> `00aeeb8c` | `03 00 00 14` | b 0x00aeeb98 | `UNCONDITIONAL_JUMP`
<a id="insn-00aeeb90"></a> `00aeeb90` | `08 04 80 52` | mov w8,#0x20 | `FALL_THROUGH`
<a id="insn-00aeeb94"></a> `00aeeb94` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00aeeb98"></a> `00aeeb98` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-00aeeb9c"></a> `00aeeb9c` | `28 69 68 f8` | ldr x8,[x9, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00aeeba0"></a> `00aeeba0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aeeba4"></a> `00aeeba4` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00aeeba8"></a> `00aeeba8` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aeebac"></a> `00aeebac` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00aeebb0"></a> `00aeebb0` | `01 03 00 54` | b.ne 0x00aeec10 | `CONDITIONAL_JUMP`
<a id="insn-00aeebb4"></a> `00aeebb4` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00aeebb8"></a> `00aeebb8` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00aeebbc"></a> `00aeebbc` | `ff 83 01 91` | add sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00aeebc0"></a> `00aeebc0` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00aeec10"></a> `00aeec10` | `b4 a3 05 94` | bl 0x00c57ae0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aeead0`](#insn-00aeead0) 範囲 `[['00aeead0', '00aeead3']]`
  - `FALL_THROUGH` [`00aeead0`](#insn-00aeead0) → [`00aeead4`](#insn-00aeead4)
- ブロック [`00aeead4`](#insn-00aeead4) 範囲 `[['00aeead4', '00aeeaf7']]`
  - `CONDITIONAL_JUMP` [`00aeeaf4`](#insn-00aeeaf4) → [`00aeeb4c`](#insn-00aeeb4c)
  - `FALL_THROUGH` [`00aeeaf4`](#insn-00aeeaf4) → [`00aeeaf8`](#insn-00aeeaf8)
- ブロック [`00aeeaf8`](#insn-00aeeaf8) 範囲 `[['00aeeaf8', '00aeeaff']]`
  - `CONDITIONAL_JUMP` [`00aeeafc`](#insn-00aeeafc) → [`00aeeb20`](#insn-00aeeb20)
  - `FALL_THROUGH` [`00aeeafc`](#insn-00aeeafc) → [`00aeeb00`](#insn-00aeeb00)
- ブロック [`00aeeb00`](#insn-00aeeb00) 範囲 `[['00aeeb00', '00aeeb03']]`
  - `CONDITIONAL_JUMP` [`00aeeb00`](#insn-00aeeb00) → [`00aeeba4`](#insn-00aeeba4)
  - `FALL_THROUGH` [`00aeeb00`](#insn-00aeeb00) → [`00aeeb04`](#insn-00aeeb04)
- ブロック [`00aeeb04`](#insn-00aeeb04) 範囲 `[['00aeeb04', '00aeeb17']]`
  - `CONDITIONAL_JUMP` [`00aeeb14`](#insn-00aeeb14) → [`00aeec10`](#insn-00aeec10)
  - `FALL_THROUGH` [`00aeeb14`](#insn-00aeeb14) → [`00aeeb18`](#insn-00aeeb18)
- ブロック [`00aeeb18`](#insn-00aeeb18) 範囲 `[['00aeeb18', '00aeeb1f']]`
  - `UNCONDITIONAL_JUMP` [`00aeeb1c`](#insn-00aeeb1c) → [`00aeeb38`](#insn-00aeeb38)
- ブロック [`00aeeb20`](#insn-00aeeb20) 範囲 `[['00aeeb20', '00aeeb33']]`
  - `CONDITIONAL_JUMP` [`00aeeb30`](#insn-00aeeb30) → [`00aeec10`](#insn-00aeec10)
  - `FALL_THROUGH` [`00aeeb30`](#insn-00aeeb30) → [`00aeeb34`](#insn-00aeeb34)
- ブロック [`00aeeb34`](#insn-00aeeb34) 範囲 `[['00aeeb34', '00aeeb37']]`
  - `FALL_THROUGH` [`00aeeb34`](#insn-00aeeb34) → [`00aeeb38`](#insn-00aeeb38)
- ブロック [`00aeeb38`](#insn-00aeeb38) 範囲 `[['00aeeb38', '00aeeb4b']]`
- ブロック [`00aeeb4c`](#insn-00aeeb4c) 範囲 `[['00aeeb4c', '00aeeb83']]`
  - `CONDITIONAL_JUMP` [`00aeeb80`](#insn-00aeeb80) → [`00aeeb90`](#insn-00aeeb90)
  - `FALL_THROUGH` [`00aeeb80`](#insn-00aeeb80) → [`00aeeb84`](#insn-00aeeb84)
- ブロック [`00aeeb84`](#insn-00aeeb84) 範囲 `[['00aeeb84', '00aeeb87']]`
  - `CONDITIONAL_JUMP` [`00aeeb84`](#insn-00aeeb84) → [`00aeeba4`](#insn-00aeeba4)
  - `FALL_THROUGH` [`00aeeb84`](#insn-00aeeb84) → [`00aeeb88`](#insn-00aeeb88)
- ブロック [`00aeeb88`](#insn-00aeeb88) 範囲 `[['00aeeb88', '00aeeb8f']]`
  - `UNCONDITIONAL_JUMP` [`00aeeb8c`](#insn-00aeeb8c) → [`00aeeb98`](#insn-00aeeb98)
- ブロック [`00aeeb90`](#insn-00aeeb90) 範囲 `[['00aeeb90', '00aeeb97']]`
  - `FALL_THROUGH` [`00aeeb94`](#insn-00aeeb94) → [`00aeeb98`](#insn-00aeeb98)
- ブロック [`00aeeb98`](#insn-00aeeb98) 範囲 `[['00aeeb98', '00aeeba3']]`
  - `FALL_THROUGH` [`00aeeba0`](#insn-00aeeba0) → [`00aeeba4`](#insn-00aeeba4)
- ブロック [`00aeeba4`](#insn-00aeeba4) 範囲 `[['00aeeba4', '00aeebb3']]`
  - `CONDITIONAL_JUMP` [`00aeebb0`](#insn-00aeebb0) → [`00aeec10`](#insn-00aeec10)
  - `FALL_THROUGH` [`00aeebb0`](#insn-00aeebb0) → [`00aeebb4`](#insn-00aeebb4)
- ブロック [`00aeebb4`](#insn-00aeebb4) 範囲 `[['00aeebb4', '00aeebc3']]`
- ブロック [`00aeec10`](#insn-00aeec10) 範囲 `[['00aeec10', '00aeec13']]`

## 命令位置別の参照

- [`00aeead4`](#insn-00aeead4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeead8`](#insn-00aeead8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeeae8`](#insn-00aeeae8) → `Stack[-0x28]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeeaf4`](#insn-00aeeaf4) → [`00aeeb4c`](#insn-00aeeb4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeeafc`](#insn-00aeeafc) → [`00aeeb20`](#insn-00aeeb20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeeb00`](#insn-00aeeb00) → [`00aeeba4`](#insn-00aeeba4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeeb04`](#insn-00aeeb04) → [`0047acb4`](../0047a/0047acb4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047acb4` · 推定シンボル `None` · 推定型 `None`
- [`00aeeb0c`](#insn-00aeeb0c) → `Stack[-0x28]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeeb14`](#insn-00aeeb14) → [`00aeec10`](#insn-00aeec10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeeb1c`](#insn-00aeeb1c) → [`00aeeb38`](#insn-00aeeb38) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeeb20`](#insn-00aeeb20) → [`0047acb4`](../0047a/0047acb4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047acb4` · 推定シンボル `None` · 推定型 `None`
- [`00aeeb28`](#insn-00aeeb28) → `Stack[-0x28]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeeb30`](#insn-00aeeb30) → [`00aeec10`](#insn-00aeec10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeeb3c`](#insn-00aeeb3c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeeb40`](#insn-00aeeb40) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeeb48`](#insn-00aeeb48) → [`0047cd94`](../0047c/0047cd94.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047cd94` · 推定シンボル `None` · 推定型 `None`
- [`00aeeb5c`](#insn-00aeeb5c) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeeb60`](#insn-00aeeb60) → `00c8db68`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00aeeb60`](#insn-00aeeb60) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeeb68`](#insn-00aeeb68) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeeb74`](#insn-00aeeb74) → [`00658d6c`](../00658/00658d6c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00658d6c` · 推定シンボル `None` · 推定型 `None`
- [`00aeeb78`](#insn-00aeeb78) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeeb80`](#insn-00aeeb80) → [`00aeeb90`](#insn-00aeeb90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeeb84`](#insn-00aeeb84) → [`00aeeba4`](#insn-00aeeba4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeeb8c`](#insn-00aeeb8c) → [`00aeeb98`](#insn-00aeeb98) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeeb98`](#insn-00aeeb98) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeeb9c`](#insn-00aeeb9c) → `00c8db88`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00aeeb9c`](#insn-00aeeb9c) → `00c8db90`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00aeeba0`](#insn-00aeeba0) → [`00aeec90`](00aeec90.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00aeec90` · 推定シンボル `None` · 推定型 `None`
- [`00aeeba0`](#insn-00aeeba0) → [`00aeec94`](00aeec94.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00aeec94` · 推定シンボル `None` · 推定型 `None`
- [`00aeeba8`](#insn-00aeeba8) → `Stack[-0x28]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeebb0`](#insn-00aeebb0) → [`00aeec10`](#insn-00aeec10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeebb4`](#insn-00aeebb4) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeebb8`](#insn-00aeebb8) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeec10`](#insn-00aeec10) → [`00c57ae0`](../00c57/00c57ae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ae0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aeead4`](#insn-00aeead4)

~~~json
{
  "source": "00aeead4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeead8`](#insn-00aeead8)

~~~json
{
  "source": "00aeead8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeeae8`](#insn-00aeeae8)

~~~json
{
  "source": "00aeeae8",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeeaf4`](#insn-00aeeaf4)

~~~json
{
  "source": "00aeeaf4",
  "target": "00aeeb4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeeafc`](#insn-00aeeafc)

~~~json
{
  "source": "00aeeafc",
  "target": "00aeeb20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeeb00`](#insn-00aeeb00)

~~~json
{
  "source": "00aeeb00",
  "target": "00aeeba4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeeb04`](#insn-00aeeb04)

~~~json
{
  "source": "00aeeb04",
  "target": "0047acb4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeeb0c`](#insn-00aeeb0c)

~~~json
{
  "source": "00aeeb0c",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeeb14`](#insn-00aeeb14)

~~~json
{
  "source": "00aeeb14",
  "target": "00aeec10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeeb1c`](#insn-00aeeb1c)

~~~json
{
  "source": "00aeeb1c",
  "target": "00aeeb38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeeb20`](#insn-00aeeb20)

~~~json
{
  "source": "00aeeb20",
  "target": "0047acb4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeeb28`](#insn-00aeeb28)

~~~json
{
  "source": "00aeeb28",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeeb30`](#insn-00aeeb30)

~~~json
{
  "source": "00aeeb30",
  "target": "00aeec10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeeb3c`](#insn-00aeeb3c)

~~~json
{
  "source": "00aeeb3c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeeb40`](#insn-00aeeb40)

~~~json
{
  "source": "00aeeb40",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeeb48`](#insn-00aeeb48)

~~~json
{
  "source": "00aeeb48",
  "target": "0047cd94",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeeb5c`](#insn-00aeeb5c)

~~~json
{
  "source": "00aeeb5c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeeb60`](#insn-00aeeb60)

~~~json
{
  "source": "00aeeb60",
  "target": "00c8db68",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8db68",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aeeb60`](#insn-00aeeb60)

~~~json
{
  "source": "00aeeb60",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeeb68`](#insn-00aeeb68)

~~~json
{
  "source": "00aeeb68",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeeb74`](#insn-00aeeb74)

~~~json
{
  "source": "00aeeb74",
  "target": "00658d6c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeeb78`](#insn-00aeeb78)

~~~json
{
  "source": "00aeeb78",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeeb80`](#insn-00aeeb80)

~~~json
{
  "source": "00aeeb80",
  "target": "00aeeb90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeeb84`](#insn-00aeeb84)

~~~json
{
  "source": "00aeeb84",
  "target": "00aeeba4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeeb8c`](#insn-00aeeb8c)

~~~json
{
  "source": "00aeeb8c",
  "target": "00aeeb98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeeb98`](#insn-00aeeb98)

~~~json
{
  "source": "00aeeb98",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeeb9c`](#insn-00aeeb9c)

~~~json
{
  "source": "00aeeb9c",
  "target": "00c8db88",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8db88",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aeeb9c`](#insn-00aeeb9c)

~~~json
{
  "source": "00aeeb9c",
  "target": "00c8db90",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8db90",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aeeba0`](#insn-00aeeba0)

~~~json
{
  "source": "00aeeba0",
  "target": "00aeec90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeeba0`](#insn-00aeeba0)

~~~json
{
  "source": "00aeeba0",
  "target": "00aeec94",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeeba8`](#insn-00aeeba8)

~~~json
{
  "source": "00aeeba8",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeebb0`](#insn-00aeebb0)

~~~json
{
  "source": "00aeebb0",
  "target": "00aeec10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeebb4`](#insn-00aeebb4)

~~~json
{
  "source": "00aeebb4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeebb8`](#insn-00aeebb8)

~~~json
{
  "source": "00aeebb8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeec10`](#insn-00aeec10)

~~~json
{
  "source": "00aeec10",
  "target": "00c57ae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
