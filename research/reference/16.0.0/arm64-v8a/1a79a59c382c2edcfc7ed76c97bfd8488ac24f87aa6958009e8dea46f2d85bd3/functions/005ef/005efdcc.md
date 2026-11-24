# 005efdcc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0111.md#review-558a74d939d111b12f3421af213875b6)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `005efe0c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ef/005efe0c.md) · 移動量 `+0x40`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0025.md#compare-7797494350ecf1a048c09ff02b2b6057)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "005efdcc",
  "name": "FUN_005efdcc",
  "size": 284,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2d2a27ed9070afd5d2e9fb6fe7a40d2a24e20bd22d5f02995e439a0953438ef7",
  "source_text_sha256": "2d2a27ed9070afd5d2e9fb6fe7a40d2a24e20bd22d5f02995e439a0953438ef7",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "005efdcc",
        "005efee3"
      ],
      [
        "005eff10",
        "005eff13"
      ]
    ],
    "bytes_sha256": "715d1b9d70f3fb2705242c431536edde84075a818ca7c16e97eb25a5fa8c856c",
    "instruction_count": 71,
    "instruction_bytes": 284,
    "body_bytes": 284,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00700ab8](../00700/00700ab8.md)
- [00720050](../00720/00720050.md)
- [00a47d08](../00a47/00a47d08.md)
- [00a51580](../00a51/00a51580.md)

## 呼び出し先

- [005ed758](../005ed/005ed758.md)
- [00936428](../00936/00936428.md)
- [00c57ab0](../00c57/00c57ab0.md)
- [00c57ae0](../00c57/00c57ae0.md)

## 関連文字列（未確認候補）

~~~text
"battle_zoom_castle_y"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2523 bytes

~~~c

void FUN_005efdcc(long param_1)

{
  undefined4 uVar1;
  int iVar2;
  int iVar3;
  int iVar4;
  long lVar5;
  undefined8 uVar6;
  int iVar7;
  int iVar8;
  byte local_70;
  char local_6f [8];
  undefined7 uStack_67;
  char cStack_60;
  undefined4 uStack_5f;
  undefined1 uStack_5b;
  undefined2 uStack_5a;
  long local_58;
  
  uVar6 = s_battle_zoom_castle_y_002b3d1f._8_8_;
  local_6f = (char  [8])s_battle_zoom_castle_y_002b3d1f._0_8_;
                    /* try { // try from 005efde4 to 006efe3f has its CatchHandler @ 005efde4
                       catch() { ... } // from try @ 005efde4 with catch @ 005efde4
                       catch() { ... } // from try @ 005efe48 with catch @ 005efde4
                       catch() { ... } // from try @ 005efee4 with catch @ 005efde4
                       catch() { ... } // from try @ 005f00f0 with catch @ 005efde4
                       catch() { ... } // from try @ 005f01b4 with catch @ 005efde4
                       catch() { ... } // from try @ 005f023c with catch @ 005efde4 */
  lVar5 = tpidr_el0;
  local_58 = *(long *)(lVar5 + 0x28);
  uVar1 = *(undefined4 *)(param_1 + 0x3534);
  iVar2 = *(int *)(param_1 + 0x359c);
  local_70 = 0x28;
  uStack_5f = 0x795f656c;
  *(undefined4 *)(param_1 + 0x3534) = 10000;
  uStack_67 = (undefined7)uVar6;
  cStack_60 = SUB81(uVar6,7);
  uStack_5b = 0;
                    /* try { // try from 005efe40 to 006efe47 has its CatchHandler @ 005f02ac */
  iVar7 = FUN_00936428(param_1 + 0x1588,&local_70,0);
                    /* try { // try from 005efe48 to 006efea3 has its CatchHandler @ 005efde4 */
  if (*(char *)(param_1 + 0x14ed) == '\0') {
    iVar8 = 0;
  }
  else {
    iVar8 = FUN_005ed758(param_1);
  }
  iVar3 = *(int *)(param_1 + 0x359c);
  iVar4 = *(int *)((long)&fde_table_entry_003339e8.initial_loc + param_1);
  if ((local_70 & 1) != 0) {
    _ZdlPv((void *)CONCAT26(uStack_5a,CONCAT15(uStack_5b,CONCAT41(uStack_5f,cStack_60))));
  }
  *(undefined4 *)(param_1 + 0x3534) = uVar1;
                    /* try { // try from 005efea4 to 006efeaf has its CatchHandler @ 005f0298 */
  iVar8 = (iVar8 - iVar3) + iVar4 + 0x8a;
  iVar3 = 0;
  if (iVar8 != 0) {
    iVar3 = ((iVar7 - iVar2) * 10000 + 0x11da50) / iVar8;
  }
  if (9999 < iVar3) {
    iVar3 = 10000;
  }
  if (*(long *)(lVar5 + 0x28) == local_58) {
                    /* try { // try from 005efedc to 006efee3 has its CatchHandler @ 005f027c */
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail(iVar3);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-005efdcc"></a> `005efdcc` | `ff c3 01 d1` | sub sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-005efdd0"></a> `005efdd0` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-005efdd4"></a> `005efdd4` | `fa 67 03 a9` | stp x26,x25,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-005efdd8"></a> `005efdd8` | `f8 5f 04 a9` | stp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-005efddc"></a> `005efddc` | `f6 57 05 a9` | stp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-005efde0"></a> `005efde0` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-005efde4"></a> `005efde4` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-005efde8"></a> `005efde8` | `56 d0 3b d5` | mrs x22,tpidr_el0 | `FALL_THROUGH`
<a id="insn-005efdec"></a> `005efdec` | `09 05 80 52` | mov w9,#0x28 | `FALL_THROUGH`
<a id="insn-005efdf0"></a> `005efdf0` | `8a ad 8c 52` | mov w10,#0x656c | `FALL_THROUGH`
<a id="insn-005efdf4"></a> `005efdf4` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-005efdf8"></a> `005efdf8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-005efdfc"></a> `005efdfc` | `ea 2b af 72` | movk w10,#0x795f, LSL #16 | `FALL_THROUGH`
<a id="insn-005efe00"></a> `005efe00` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-005efe04"></a> `005efe04` | `28 e6 ff 90` | adrp x8,0x2b3000 | `FALL_THROUGH`
<a id="insn-005efe08"></a> `005efe08` | `08 7d 34 91` | add x8,x8,#0xd1f | `FALL_THROUGH`
<a id="insn-005efe0c"></a> `005efe0c` | `00 01 c0 3d` | ldr q0,[x8] | `FALL_THROUGH`
<a id="insn-005efe10"></a> `005efe10` | `17 34 75 b9` | ldr w23,[x0, #0x3534] | `FALL_THROUGH`
<a id="insn-005efe14"></a> `005efe14` | `18 9c 75 b9` | ldr w24,[x0, #0x359c] | `FALL_THROUGH`
<a id="insn-005efe18"></a> `005efe18` | `e9 03 00 39` | strb w9,[sp] | `FALL_THROUGH`
<a id="insn-005efe1c"></a> `005efe1c` | `09 e2 84 52` | mov w9,#0x2710 | `FALL_THROUGH`
<a id="insn-005efe20"></a> `005efe20` | `08 b1 82 52` | mov w8,#0x1588 | `FALL_THROUGH`
<a id="insn-005efe24"></a> `005efe24` | `ea 13 01 b8` | stur w10,[sp, #0x11] | `FALL_THROUGH`
<a id="insn-005efe28"></a> `005efe28` | `09 34 35 b9` | str w9,[x0, #0x3534] | `FALL_THROUGH`
<a id="insn-005efe2c"></a> `005efe2c` | `e0 13 80 3c` | stur q0,[sp, #0x1] | `FALL_THROUGH`
<a id="insn-005efe30"></a> `005efe30` | `ff 57 00 39` | strb wzr,[sp, #0x15] | `FALL_THROUGH`
<a id="insn-005efe34"></a> `005efe34` | `00 00 08 8b` | add x0,x0,x8 | `FALL_THROUGH`
<a id="insn-005efe38"></a> `005efe38` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-005efe3c"></a> `005efe3c` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-005efe40"></a> `005efe40` | `7a 19 0d 94` | bl 0x00936428 | `UNCONDITIONAL_CALL`
<a id="insn-005efe44"></a> `005efe44` | `a8 9d 82 52` | mov w8,#0x14ed | `FALL_THROUGH`
<a id="insn-005efe48"></a> `005efe48` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-005efe4c"></a> `005efe4c` | `68 6a 68 38` | ldrb w8,[x19, x8, LSL ] | `FALL_THROUGH`
<a id="insn-005efe50"></a> `005efe50` | `a8 00 00 34` | cbz w8,0x005efe64 | `CONDITIONAL_JUMP`
<a id="insn-005efe54"></a> `005efe54` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-005efe58"></a> `005efe58` | `40 f6 ff 97` | bl 0x005ed758 | `UNCONDITIONAL_CALL`
<a id="insn-005efe5c"></a> `005efe5c` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-005efe60"></a> `005efe60` | `02 00 00 14` | b 0x005efe68 | `UNCONDITIONAL_JUMP`
<a id="insn-005efe64"></a> `005efe64` | `f5 03 1f 2a` | mov w21,wzr | `FALL_THROUGH`
<a id="insn-005efe68"></a> `005efe68` | `08 3d 87 52` | mov w8,#0x39e8 | `FALL_THROUGH`
<a id="insn-005efe6c"></a> `005efe6c` | `e9 03 40 39` | ldrb w9,[sp] | `FALL_THROUGH`
<a id="insn-005efe70"></a> `005efe70` | `79 9e 75 b9` | ldr w25,[x19, #0x359c] | `FALL_THROUGH`
<a id="insn-005efe74"></a> `005efe74` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-005efe78"></a> `005efe78` | `7a 6a 68 b8` | ldr w26,[x19, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-005efe7c"></a> `005efe7c` | `69 00 00 36` | tbz w9,#0x0,0x005efe88 | `CONDITIONAL_JUMP`
<a id="insn-005efe80"></a> `005efe80` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-005efe84"></a> `005efe84` | `0b 9f 19 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-005efe88"></a> `005efe88` | `0a 4a 9b 52` | mov w10,#0xda50 | `FALL_THROUGH`
<a id="insn-005efe8c"></a> `005efe8c` | `88 02 18 4b` | sub w8,w20,w24 | `FALL_THROUGH`
<a id="insn-005efe90"></a> `005efe90` | `09 e2 84 52` | mov w9,#0x2710 | `FALL_THROUGH`
<a id="insn-005efe94"></a> `005efe94` | `2a 02 a0 72` | movk w10,#0x11, LSL #16 | `FALL_THROUGH`
<a id="insn-005efe98"></a> `005efe98` | `08 29 09 1b` | madd w8,w8,w9,w10 | `FALL_THROUGH`
<a id="insn-005efe9c"></a> `005efe9c` | `77 36 35 b9` | str w23,[x19, #0x3534] | `FALL_THROUGH`
<a id="insn-005efea0"></a> `005efea0` | `aa 02 19 4b` | sub w10,w21,w25 | `FALL_THROUGH`
<a id="insn-005efea4"></a> `005efea4` | `4a 01 1a 0b` | add w10,w10,w26 | `FALL_THROUGH`
<a id="insn-005efea8"></a> `005efea8` | `4a 29 02 11` | add w10,w10,#0x8a | `FALL_THROUGH`
<a id="insn-005efeac"></a> `005efeac` | `08 0d ca 1a` | sdiv w8,w8,w10 | `FALL_THROUGH`
<a id="insn-005efeb0"></a> `005efeb0` | `ca 16 40 f9` | ldr x10,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-005efeb4"></a> `005efeb4` | `ab 83 5f f8` | ldur x11,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-005efeb8"></a> `005efeb8` | `1f 01 09 6b` | cmp w8,w9 | `FALL_THROUGH`
<a id="insn-005efebc"></a> `005efebc` | `00 b1 89 1a` | csel w0,w8,w9,lt | `FALL_THROUGH`
<a id="insn-005efec0"></a> `005efec0` | `5f 01 0b eb` | cmp x10,x11 | `FALL_THROUGH`
<a id="insn-005efec4"></a> `005efec4` | `61 02 00 54` | b.ne 0x005eff10 | `CONDITIONAL_JUMP`
<a id="insn-005efec8"></a> `005efec8` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-005efecc"></a> `005efecc` | `f6 57 45 a9` | ldp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-005efed0"></a> `005efed0` | `f8 5f 44 a9` | ldp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-005efed4"></a> `005efed4` | `fa 67 43 a9` | ldp x26,x25,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-005efed8"></a> `005efed8` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-005efedc"></a> `005efedc` | `ff c3 01 91` | add sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-005efee0"></a> `005efee0` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-005eff10"></a> `005eff10` | `f4 9e 19 94` | bl 0x00c57ae0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`005efdcc`](#insn-005efdcc) 範囲 `[['005efdcc', '005efde3']]`
  - `FALL_THROUGH` [`005efde0`](#insn-005efde0) → [`005efde4`](#insn-005efde4)
- ブロック [`005efde4`](#insn-005efde4) 範囲 `[['005efde4', '005efe3f']]`
  - `FALL_THROUGH` [`005efe3c`](#insn-005efe3c) → [`005efe40`](#insn-005efe40)
- ブロック [`005efe40`](#insn-005efe40) 範囲 `[['005efe40', '005efe47']]`
  - `FALL_THROUGH` [`005efe44`](#insn-005efe44) → [`005efe48`](#insn-005efe48)
- ブロック [`005efe48`](#insn-005efe48) 範囲 `[['005efe48', '005efe53']]`
  - `CONDITIONAL_JUMP` [`005efe50`](#insn-005efe50) → [`005efe64`](#insn-005efe64)
  - `FALL_THROUGH` [`005efe50`](#insn-005efe50) → [`005efe54`](#insn-005efe54)
- ブロック [`005efe54`](#insn-005efe54) 範囲 `[['005efe54', '005efe63']]`
  - `UNCONDITIONAL_JUMP` [`005efe60`](#insn-005efe60) → [`005efe68`](#insn-005efe68)
- ブロック [`005efe64`](#insn-005efe64) 範囲 `[['005efe64', '005efe67']]`
  - `FALL_THROUGH` [`005efe64`](#insn-005efe64) → [`005efe68`](#insn-005efe68)
- ブロック [`005efe68`](#insn-005efe68) 範囲 `[['005efe68', '005efe7f']]`
  - `CONDITIONAL_JUMP` [`005efe7c`](#insn-005efe7c) → [`005efe88`](#insn-005efe88)
  - `FALL_THROUGH` [`005efe7c`](#insn-005efe7c) → [`005efe80`](#insn-005efe80)
- ブロック [`005efe80`](#insn-005efe80) 範囲 `[['005efe80', '005efe87']]`
  - `FALL_THROUGH` [`005efe84`](#insn-005efe84) → [`005efe88`](#insn-005efe88)
- ブロック [`005efe88`](#insn-005efe88) 範囲 `[['005efe88', '005efea3']]`
  - `FALL_THROUGH` [`005efea0`](#insn-005efea0) → [`005efea4`](#insn-005efea4)
- ブロック [`005efea4`](#insn-005efea4) 範囲 `[['005efea4', '005efec7']]`
  - `CONDITIONAL_JUMP` [`005efec4`](#insn-005efec4) → [`005eff10`](#insn-005eff10)
  - `FALL_THROUGH` [`005efec4`](#insn-005efec4) → [`005efec8`](#insn-005efec8)
- ブロック [`005efec8`](#insn-005efec8) 範囲 `[['005efec8', '005efedb']]`
  - `FALL_THROUGH` [`005efed8`](#insn-005efed8) → [`005efedc`](#insn-005efedc)
- ブロック [`005efedc`](#insn-005efedc) 範囲 `[['005efedc', '005efee3']]`
- ブロック [`005eff10`](#insn-005eff10) 範囲 `[['005eff10', '005eff13']]`

## 命令位置別の参照

- [`005efdd0`](#insn-005efdd0) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005efdd4`](#insn-005efdd4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005efdd8`](#insn-005efdd8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005efddc`](#insn-005efddc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005efde0`](#insn-005efde0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005efe00`](#insn-005efe00) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005efe0c`](#insn-005efe0c) → `002b3d1f`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`005efe18`](#insn-005efe18) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005efe24`](#insn-005efe24) → `Stack[-0x5f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005efe2c`](#insn-005efe2c) → `Stack[-0x6f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005efe30`](#insn-005efe30) → `Stack[-0x5b]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005efe40`](#insn-005efe40) → [`00936428`](../00936/00936428.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00936428` · 推定シンボル `None` · 推定型 `None`
- [`005efe50`](#insn-005efe50) → [`005efe64`](#insn-005efe64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005efe58`](#insn-005efe58) → [`005ed758`](../005ed/005ed758.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005ed758` · 推定シンボル `None` · 推定型 `None`
- [`005efe60`](#insn-005efe60) → [`005efe68`](#insn-005efe68) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005efe6c`](#insn-005efe6c) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005efe78`](#insn-005efe78) → `003339e8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`005efe7c`](#insn-005efe7c) → [`005efe88`](#insn-005efe88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005efe80`](#insn-005efe80) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005efe84`](#insn-005efe84) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`005efeb4`](#insn-005efeb4) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005efec4`](#insn-005efec4) → [`005eff10`](#insn-005eff10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005efec8`](#insn-005efec8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005efecc`](#insn-005efecc) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005efed0`](#insn-005efed0) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005efed4`](#insn-005efed4) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005efed8`](#insn-005efed8) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005eff10`](#insn-005eff10) → [`00c57ae0`](../00c57/00c57ae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ae0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`005efdd0`](#insn-005efdd0)

~~~json
{
  "source": "005efdd0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005efdd4`](#insn-005efdd4)

~~~json
{
  "source": "005efdd4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005efdd8`](#insn-005efdd8)

~~~json
{
  "source": "005efdd8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005efddc`](#insn-005efddc)

~~~json
{
  "source": "005efddc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005efde0`](#insn-005efde0)

~~~json
{
  "source": "005efde0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005efe00`](#insn-005efe00)

~~~json
{
  "source": "005efe00",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005efe0c`](#insn-005efe0c)

~~~json
{
  "source": "005efe0c",
  "target": "002b3d1f",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b3d1f",
  "offset": 0,
  "size": 21,
  "datatype": "string",
  "bytes": "626174746c655f7a6f6f6d5f636173746c655f7900",
  "capture_start": "002b3d1f",
  "capture_bytes": 21,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`005efe18`](#insn-005efe18)

~~~json
{
  "source": "005efe18",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005efe24`](#insn-005efe24)

~~~json
{
  "source": "005efe24",
  "target": "Stack[-0x5f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005efe2c`](#insn-005efe2c)

~~~json
{
  "source": "005efe2c",
  "target": "Stack[-0x6f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005efe30`](#insn-005efe30)

~~~json
{
  "source": "005efe30",
  "target": "Stack[-0x5b]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005efe40`](#insn-005efe40)

~~~json
{
  "source": "005efe40",
  "target": "00936428",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005efe50`](#insn-005efe50)

~~~json
{
  "source": "005efe50",
  "target": "005efe64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005efe58`](#insn-005efe58)

~~~json
{
  "source": "005efe58",
  "target": "005ed758",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005efe60`](#insn-005efe60)

~~~json
{
  "source": "005efe60",
  "target": "005efe68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005efe6c`](#insn-005efe6c)

~~~json
{
  "source": "005efe6c",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005efe78`](#insn-005efe78)

~~~json
{
  "source": "005efe78",
  "target": "003339e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003339e8",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "44c26a00bc790900",
  "capture_start": "003339e8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`005efe7c`](#insn-005efe7c)

~~~json
{
  "source": "005efe7c",
  "target": "005efe88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005efe80`](#insn-005efe80)

~~~json
{
  "source": "005efe80",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005efe84`](#insn-005efe84)

~~~json
{
  "source": "005efe84",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005efeb4`](#insn-005efeb4)

~~~json
{
  "source": "005efeb4",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005efec4`](#insn-005efec4)

~~~json
{
  "source": "005efec4",
  "target": "005eff10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005efec8`](#insn-005efec8)

~~~json
{
  "source": "005efec8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005efecc`](#insn-005efecc)

~~~json
{
  "source": "005efecc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005efed0`](#insn-005efed0)

~~~json
{
  "source": "005efed0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005efed4`](#insn-005efed4)

~~~json
{
  "source": "005efed4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005efed8`](#insn-005efed8)

~~~json
{
  "source": "005efed8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005eff10`](#insn-005eff10)

~~~json
{
  "source": "005eff10",
  "target": "00c57ae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
