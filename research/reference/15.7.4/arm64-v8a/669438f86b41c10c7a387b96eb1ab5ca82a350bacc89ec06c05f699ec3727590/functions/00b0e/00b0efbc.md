# 00b0efbc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00b0ef78`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0e/00b0ef78.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0067.md#compare-e542386f2862fe750bb3d4b49018fa87)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b6ed88`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6ed88.md) · 移動量 `+0x5fdcc`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0062.md#compare-014fd8fcee2756a2dfdc005a5278506b)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b0efbc",
  "name": "_ZN11flatbuffers6Parser12RecurseErrorEv",
  "size": 308,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2c49598281e4c0d1cd3bbcf09819215abab35f636d3bfa1472655dd450159b91",
  "source_text_sha256": "2c49598281e4c0d1cd3bbcf09819215abab35f636d3bfa1472655dd450159b91",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b0efbc",
        "00b0f0ef"
      ]
    ],
    "bytes_sha256": "2eb2c04ca123f1a94bb02eef868c61888bcef0dffd7987f6e132171a2861b60d",
    "instruction_count": 77,
    "instruction_bytes": 308,
    "body_bytes": 308,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bdf7f0](../00bdf/00bdf7f0.md)

## 呼び出し先

- [00bdb060](../00bdb/00bdb060.md)
- [00bdb090](../00bdb/00bdb090.md)
- [00bdb130](../00bdb/00bdb130.md)
- [00bdb260](../00bdb/00bdb260.md)
- [00bdc180](../00bdc/00bdc180.md)
- [00bdf1a0](../00bdf/00bdf1a0.md)
- [00bdf9d0](../00bdf/00bdf9d0.md)

## 関連文字列（未確認候補）

~~~text
" reached"
"error: "
"maximum parsing recursion of "
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2169 bytes

~~~c

void _ZN11flatbuffers6Parser12RecurseErrorEv(undefined2 *param_1,undefined8 param_2)

{
  long lVar1;
  ulong *puVar2;
  byte local_a8 [16];
  void *local_98;
  ulong local_90;
  ulong uStack_88;
  void *local_80;
  ulong local_70;
  ulong uStack_68;
  void *local_60;
  byte local_50 [16];
  void *local_40;
  long local_38;
  
  lVar1 = tpidr_el0;
  local_38 = *(long *)(lVar1 + 0x28);
  _ZN11flatbuffers11NumToStringIiEENSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEET_
            (local_a8,0x40);
  puVar2 = (ulong *)_ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6insertEmPKcm
                              (local_a8,0,"maximum parsing recursion of ",0x1d);
  uStack_88 = puVar2[1];
  local_90 = *puVar2;
  local_80 = (void *)puVar2[2];
  *puVar2 = 0;
  puVar2[1] = 0;
  puVar2[2] = 0;
  puVar2 = (ulong *)_ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKcm
                              (&local_90," reached",8);
  uStack_68 = puVar2[1];
  local_70 = *puVar2;
  local_60 = (void *)puVar2[2];
  *puVar2 = 0;
  puVar2[1] = 0;
  puVar2[2] = 0;
                    /* try { // try from 00b0f054 to 00c0f06b has its CatchHandler @ 00b0fc00 */
  _ZNSt6__ndk1plIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EEPKS6_RKS9_
            (local_50,"error: ",&local_70);
  _ZN11flatbuffers6Parser7MessageERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
            (param_2,local_50);
                    /* try { // try from 00b0f06c to 00c0f0df has its CatchHandler @ 00b0ee6c */
  if ((local_50[0] & 1) != 0) {
    _ZdlPv(local_40);
  }
  *param_1 = 1;
  if ((local_70 & 1) != 0) {
    _ZdlPv(local_60);
  }
  if ((local_90 & 1) != 0) {
    _ZdlPv(local_80);
                    /* try { // try from 00b0f0e0 to 00c0f0eb has its CatchHandler @ 00b0fbf8 */
  }
  if ((local_a8[0] & 1) != 0) {
    _ZdlPv(local_98);
  }
  if (*(long *)(lVar1 + 0x28) == local_38) {
    return;
  }
                    /* WARNING: Subroutine does not return */
                    /* try { // try from 00b0f0ec to 00c0f1a7 has its CatchHandler @ 00b0ee6c */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b0efbc"></a> `00b0efbc` | `ff c3 02 d1` | sub sp,sp,#0xb0 | `FALL_THROUGH`
<a id="insn-00b0efc0"></a> `00b0efc0` | `f5 43 00 f9` | str x21,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00b0efc4"></a> `00b0efc4` | `f4 4f 09 a9` | stp x20,x19,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00b0efc8"></a> `00b0efc8` | `fd 7b 0a a9` | stp x29,x30,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00b0efcc"></a> `00b0efcc` | `fd 83 02 91` | add x29,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-00b0efd0"></a> `00b0efd0` | `55 d0 3b d5` | mrs x21,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00b0efd4"></a> `00b0efd4` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00b0efd8"></a> `00b0efd8` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00b0efdc"></a> `00b0efdc` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00b0efe0"></a> `00b0efe0` | `00 08 80 52` | mov w0,#0x40 | `FALL_THROUGH`
<a id="insn-00b0efe4"></a> `00b0efe4` | `a8 83 1d f8` | stur x8,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-00b0efe8"></a> `00b0efe8` | `e8 23 00 91` | add x8,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00b0efec"></a> `00b0efec` | `6d 40 03 94` | bl 0x00bdf1a0 | `UNCONDITIONAL_CALL`
<a id="insn-00b0eff0"></a> `00b0eff0` | `a2 bc ff b0` | adrp x2,0x2a3000 | `FALL_THROUGH`
<a id="insn-00b0eff4"></a> `00b0eff4` | `42 30 39 91` | add x2,x2,#0xe4c | `FALL_THROUGH`
<a id="insn-00b0eff8"></a> `00b0eff8` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00b0effc"></a> `00b0effc` | `a3 03 80 52` | mov w3,#0x1d | `FALL_THROUGH`
<a id="insn-00b0f000"></a> `00b0f000` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-00b0f004"></a> `00b0f004` | `5f 34 03 94` | bl 0x00bdc180 | `UNCONDITIONAL_CALL`
<a id="insn-00b0f008"></a> `00b0f008` | `00 00 c0 3d` | ldr q0,[x0] | `FALL_THROUGH`
<a id="insn-00b0f00c"></a> `00b0f00c` | `08 08 40 f9` | ldr x8,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00b0f010"></a> `00b0f010` | `41 bc ff b0` | adrp x1,0x298000 | `FALL_THROUGH`
<a id="insn-00b0f014"></a> `00b0f014` | `21 28 1d 91` | add x1,x1,#0x74a | `FALL_THROUGH`
<a id="insn-00b0f018"></a> `00b0f018` | `e0 0b 80 3d` | str q0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b0f01c"></a> `00b0f01c` | `e8 1b 00 f9` | str x8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b0f020"></a> `00b0f020` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00b0f024"></a> `00b0f024` | `1f 08 00 f9` | str xzr,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00b0f028"></a> `00b0f028` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00b0f02c"></a> `00b0f02c` | `02 01 80 52` | mov w2,#0x8 | `FALL_THROUGH`
<a id="insn-00b0f030"></a> `00b0f030` | `40 30 03 94` | bl 0x00bdb130 | `UNCONDITIONAL_CALL`
<a id="insn-00b0f034"></a> `00b0f034` | `00 00 c0 3d` | ldr q0,[x0] | `FALL_THROUGH`
<a id="insn-00b0f038"></a> `00b0f038` | `08 08 40 f9` | ldr x8,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00b0f03c"></a> `00b0f03c` | `e1 03 01 91` | add x1,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00b0f040"></a> `00b0f040` | `e0 13 80 3d` | str q0,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b0f044"></a> `00b0f044` | `e8 2b 00 f9` | str x8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00b0f048"></a> `00b0f048` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00b0f04c"></a> `00b0f04c` | `1f 08 00 f9` | str xzr,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00b0f050"></a> `00b0f050` | `00 bc ff d0` | adrp x0,0x291000 | `FALL_THROUGH`
<a id="insn-00b0f054"></a> `00b0f054` | `00 14 15 91` | add x0,x0,#0x545 | `FALL_THROUGH`
<a id="insn-00b0f058"></a> `00b0f058` | `a8 03 01 d1` | sub x8,x29,#0x40 | `FALL_THROUGH`
<a id="insn-00b0f05c"></a> `00b0f05c` | `81 30 03 94` | bl 0x00bdb260 | `UNCONDITIONAL_CALL`
<a id="insn-00b0f060"></a> `00b0f060` | `a1 03 01 d1` | sub x1,x29,#0x40 | `FALL_THROUGH`
<a id="insn-00b0f064"></a> `00b0f064` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b0f068"></a> `00b0f068` | `5a 42 03 94` | bl 0x00bdf9d0 | `UNCONDITIONAL_CALL`
<a id="insn-00b0f06c"></a> `00b0f06c` | `a8 03 5c 38` | ldurb w8,[x29, #-0x40] | `FALL_THROUGH`
<a id="insn-00b0f070"></a> `00b0f070` | `68 00 00 36` | tbz w8,#0x0,0x00b0f07c | `CONDITIONAL_JUMP`
<a id="insn-00b0f074"></a> `00b0f074` | `a0 03 5d f8` | ldur x0,[x29, #-0x30] | `FALL_THROUGH`
<a id="insn-00b0f078"></a> `00b0f078` | `fa 2f 03 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00b0f07c"></a> `00b0f07c` | `e8 03 41 39` | ldrb w8,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b0f080"></a> `00b0f080` | `29 00 80 52` | mov w9,#0x1 | `FALL_THROUGH`
<a id="insn-00b0f084"></a> `00b0f084` | `69 02 00 79` | strh w9,[x19] | `FALL_THROUGH`
<a id="insn-00b0f088"></a> `00b0f088` | `08 02 00 37` | tbnz w8,#0x0,0x00b0f0c8 | `CONDITIONAL_JUMP`
<a id="insn-00b0f08c"></a> `00b0f08c` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b0f090"></a> `00b0f090` | `48 02 00 37` | tbnz w8,#0x0,0x00b0f0d8 | `CONDITIONAL_JUMP`
<a id="insn-00b0f094"></a> `00b0f094` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00b0f098"></a> `00b0f098` | `68 00 00 36` | tbz w8,#0x0,0x00b0f0a4 | `CONDITIONAL_JUMP`
<a id="insn-00b0f09c"></a> `00b0f09c` | `e0 0f 40 f9` | ldr x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00b0f0a0"></a> `00b0f0a0` | `f0 2f 03 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00b0f0a4"></a> `00b0f0a4` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00b0f0a8"></a> `00b0f0a8` | `a9 83 5d f8` | ldur x9,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-00b0f0ac"></a> `00b0f0ac` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00b0f0b0"></a> `00b0f0b0` | `e1 01 00 54` | b.ne 0x00b0f0ec | `CONDITIONAL_JUMP`
<a id="insn-00b0f0b4"></a> `00b0f0b4` | `fd 7b 4a a9` | ldp x29,x30,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00b0f0b8"></a> `00b0f0b8` | `f4 4f 49 a9` | ldp x20,x19,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00b0f0bc"></a> `00b0f0bc` | `f5 43 40 f9` | ldr x21,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00b0f0c0"></a> `00b0f0c0` | `ff c3 02 91` | add sp,sp,#0xb0 | `FALL_THROUGH`
<a id="insn-00b0f0c4"></a> `00b0f0c4` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00b0f0c8"></a> `00b0f0c8` | `e0 2b 40 f9` | ldr x0,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00b0f0cc"></a> `00b0f0cc` | `e5 2f 03 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00b0f0d0"></a> `00b0f0d0` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b0f0d4"></a> `00b0f0d4` | `08 fe 07 36` | tbz w8,#0x0,0x00b0f094 | `CONDITIONAL_JUMP`
<a id="insn-00b0f0d8"></a> `00b0f0d8` | `e0 1b 40 f9` | ldr x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b0f0dc"></a> `00b0f0dc` | `e1 2f 03 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00b0f0e0"></a> `00b0f0e0` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00b0f0e4"></a> `00b0f0e4` | `c8 fd 07 37` | tbnz w8,#0x0,0x00b0f09c | `CONDITIONAL_JUMP`
<a id="insn-00b0f0e8"></a> `00b0f0e8` | `ef ff ff 17` | b 0x00b0f0a4 | `UNCONDITIONAL_JUMP`
<a id="insn-00b0f0ec"></a> `00b0f0ec` | `e9 2f 03 94` | bl 0x00bdb090 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b0efbc`](#insn-00b0efbc) 範囲 `[['00b0efbc', '00b0f053']]`
  - `FALL_THROUGH` [`00b0f050`](#insn-00b0f050) → [`00b0f054`](#insn-00b0f054)
- ブロック [`00b0f054`](#insn-00b0f054) 範囲 `[['00b0f054', '00b0f06b']]`
  - `FALL_THROUGH` [`00b0f068`](#insn-00b0f068) → [`00b0f06c`](#insn-00b0f06c)
- ブロック [`00b0f06c`](#insn-00b0f06c) 範囲 `[['00b0f06c', '00b0f073']]`
  - `CONDITIONAL_JUMP` [`00b0f070`](#insn-00b0f070) → [`00b0f07c`](#insn-00b0f07c)
  - `FALL_THROUGH` [`00b0f070`](#insn-00b0f070) → [`00b0f074`](#insn-00b0f074)
- ブロック [`00b0f074`](#insn-00b0f074) 範囲 `[['00b0f074', '00b0f07b']]`
  - `FALL_THROUGH` [`00b0f078`](#insn-00b0f078) → [`00b0f07c`](#insn-00b0f07c)
- ブロック [`00b0f07c`](#insn-00b0f07c) 範囲 `[['00b0f07c', '00b0f08b']]`
  - `CONDITIONAL_JUMP` [`00b0f088`](#insn-00b0f088) → [`00b0f0c8`](#insn-00b0f0c8)
  - `FALL_THROUGH` [`00b0f088`](#insn-00b0f088) → [`00b0f08c`](#insn-00b0f08c)
- ブロック [`00b0f08c`](#insn-00b0f08c) 範囲 `[['00b0f08c', '00b0f093']]`
  - `CONDITIONAL_JUMP` [`00b0f090`](#insn-00b0f090) → [`00b0f0d8`](#insn-00b0f0d8)
  - `FALL_THROUGH` [`00b0f090`](#insn-00b0f090) → [`00b0f094`](#insn-00b0f094)
- ブロック [`00b0f094`](#insn-00b0f094) 範囲 `[['00b0f094', '00b0f09b']]`
  - `CONDITIONAL_JUMP` [`00b0f098`](#insn-00b0f098) → [`00b0f0a4`](#insn-00b0f0a4)
  - `FALL_THROUGH` [`00b0f098`](#insn-00b0f098) → [`00b0f09c`](#insn-00b0f09c)
- ブロック [`00b0f09c`](#insn-00b0f09c) 範囲 `[['00b0f09c', '00b0f0a3']]`
  - `FALL_THROUGH` [`00b0f0a0`](#insn-00b0f0a0) → [`00b0f0a4`](#insn-00b0f0a4)
- ブロック [`00b0f0a4`](#insn-00b0f0a4) 範囲 `[['00b0f0a4', '00b0f0b3']]`
  - `CONDITIONAL_JUMP` [`00b0f0b0`](#insn-00b0f0b0) → [`00b0f0ec`](#insn-00b0f0ec)
  - `FALL_THROUGH` [`00b0f0b0`](#insn-00b0f0b0) → [`00b0f0b4`](#insn-00b0f0b4)
- ブロック [`00b0f0b4`](#insn-00b0f0b4) 範囲 `[['00b0f0b4', '00b0f0c7']]`
- ブロック [`00b0f0c8`](#insn-00b0f0c8) 範囲 `[['00b0f0c8', '00b0f0d7']]`
  - `CONDITIONAL_JUMP` [`00b0f0d4`](#insn-00b0f0d4) → [`00b0f094`](#insn-00b0f094)
  - `FALL_THROUGH` [`00b0f0d4`](#insn-00b0f0d4) → [`00b0f0d8`](#insn-00b0f0d8)
- ブロック [`00b0f0d8`](#insn-00b0f0d8) 範囲 `[['00b0f0d8', '00b0f0df']]`
  - `FALL_THROUGH` [`00b0f0dc`](#insn-00b0f0dc) → [`00b0f0e0`](#insn-00b0f0e0)
- ブロック [`00b0f0e0`](#insn-00b0f0e0) 範囲 `[['00b0f0e0', '00b0f0e7']]`
  - `CONDITIONAL_JUMP` [`00b0f0e4`](#insn-00b0f0e4) → [`00b0f09c`](#insn-00b0f09c)
  - `FALL_THROUGH` [`00b0f0e4`](#insn-00b0f0e4) → [`00b0f0e8`](#insn-00b0f0e8)
- ブロック [`00b0f0e8`](#insn-00b0f0e8) 範囲 `[['00b0f0e8', '00b0f0eb']]`
  - `UNCONDITIONAL_JUMP` [`00b0f0e8`](#insn-00b0f0e8) → [`00b0f0a4`](#insn-00b0f0a4)
- ブロック [`00b0f0ec`](#insn-00b0f0ec) 範囲 `[['00b0f0ec', '00b0f0ef']]`

## 命令位置別の参照

- [`00b0efc0`](#insn-00b0efc0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0efc4`](#insn-00b0efc4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0efc8`](#insn-00b0efc8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0efe4`](#insn-00b0efe4) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0efec`](#insn-00b0efec) → [`00bdf1a0`](../00bdf/00bdf1a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdf1a0` · 推定シンボル `None` · 推定型 `None`
- [`00b0eff4`](#insn-00b0eff4) → `002a3e4c`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b0f004`](#insn-00b0f004) → [`00bdc180`](../00bdc/00bdc180.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdc180` · 推定シンボル `None` · 推定型 `None`
- [`00b0f014`](#insn-00b0f014) → `0029874a`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b0f018`](#insn-00b0f018) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0f01c`](#insn-00b0f01c) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0f030`](#insn-00b0f030) → [`00bdb130`](../00bdb/00bdb130.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb130` · 推定シンボル `None` · 推定型 `None`
- [`00b0f040`](#insn-00b0f040) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0f044`](#insn-00b0f044) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0f054`](#insn-00b0f054) → `00291545`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b0f05c`](#insn-00b0f05c) → [`00bdb260`](../00bdb/00bdb260.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb260` · 推定シンボル `None` · 推定型 `None`
- [`00b0f068`](#insn-00b0f068) → [`00bdf9d0`](../00bdf/00bdf9d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdf9d0` · 推定シンボル `None` · 推定型 `None`
- [`00b0f06c`](#insn-00b0f06c) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0f070`](#insn-00b0f070) → [`00b0f07c`](#insn-00b0f07c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0f074`](#insn-00b0f074) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0f078`](#insn-00b0f078) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00b0f07c`](#insn-00b0f07c) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0f088`](#insn-00b0f088) → [`00b0f0c8`](#insn-00b0f0c8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0f08c`](#insn-00b0f08c) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0f090`](#insn-00b0f090) → [`00b0f0d8`](#insn-00b0f0d8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0f094`](#insn-00b0f094) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0f098`](#insn-00b0f098) → [`00b0f0a4`](#insn-00b0f0a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0f09c`](#insn-00b0f09c) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0f0a0`](#insn-00b0f0a0) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00b0f0a8`](#insn-00b0f0a8) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0f0b0`](#insn-00b0f0b0) → [`00b0f0ec`](#insn-00b0f0ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0f0b4`](#insn-00b0f0b4) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0f0b8`](#insn-00b0f0b8) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0f0bc`](#insn-00b0f0bc) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0f0c8`](#insn-00b0f0c8) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0f0cc`](#insn-00b0f0cc) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00b0f0d0`](#insn-00b0f0d0) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0f0d4`](#insn-00b0f0d4) → [`00b0f094`](#insn-00b0f094) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0f0d8`](#insn-00b0f0d8) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0f0dc`](#insn-00b0f0dc) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00b0f0e0`](#insn-00b0f0e0) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0f0e4`](#insn-00b0f0e4) → [`00b0f09c`](#insn-00b0f09c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0f0e8`](#insn-00b0f0e8) → [`00b0f0a4`](#insn-00b0f0a4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0f0ec`](#insn-00b0f0ec) → [`00bdb090`](../00bdb/00bdb090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb090` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b0efc0`](#insn-00b0efc0)

~~~json
{
  "source": "00b0efc0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0efc4`](#insn-00b0efc4)

~~~json
{
  "source": "00b0efc4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0efc8`](#insn-00b0efc8)

~~~json
{
  "source": "00b0efc8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0efe4`](#insn-00b0efe4)

~~~json
{
  "source": "00b0efe4",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0efec`](#insn-00b0efec)

~~~json
{
  "source": "00b0efec",
  "target": "00bdf1a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0eff4`](#insn-00b0eff4)

~~~json
{
  "source": "00b0eff4",
  "target": "002a3e4c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a3e4c",
  "offset": 0,
  "size": 30,
  "datatype": "string",
  "bytes": "6d6178696d756d2070617273696e6720726563757273696f6e206f662000",
  "capture_start": "002a3e4c",
  "capture_bytes": 30,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b0f004`](#insn-00b0f004)

~~~json
{
  "source": "00b0f004",
  "target": "00bdc180",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0f014`](#insn-00b0f014)

~~~json
{
  "source": "00b0f014",
  "target": "0029874a",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029874a",
  "offset": 0,
  "size": 9,
  "datatype": "string",
  "bytes": "207265616368656400",
  "capture_start": "0029874a",
  "capture_bytes": 9,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b0f018`](#insn-00b0f018)

~~~json
{
  "source": "00b0f018",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0f01c`](#insn-00b0f01c)

~~~json
{
  "source": "00b0f01c",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0f030`](#insn-00b0f030)

~~~json
{
  "source": "00b0f030",
  "target": "00bdb130",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0f040`](#insn-00b0f040)

~~~json
{
  "source": "00b0f040",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0f044`](#insn-00b0f044)

~~~json
{
  "source": "00b0f044",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0f054`](#insn-00b0f054)

~~~json
{
  "source": "00b0f054",
  "target": "00291545",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00291545",
  "offset": 0,
  "size": 8,
  "datatype": "string",
  "bytes": "6572726f723a2000",
  "capture_start": "00291545",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b0f05c`](#insn-00b0f05c)

~~~json
{
  "source": "00b0f05c",
  "target": "00bdb260",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0f068`](#insn-00b0f068)

~~~json
{
  "source": "00b0f068",
  "target": "00bdf9d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0f06c`](#insn-00b0f06c)

~~~json
{
  "source": "00b0f06c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0f070`](#insn-00b0f070)

~~~json
{
  "source": "00b0f070",
  "target": "00b0f07c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0f074`](#insn-00b0f074)

~~~json
{
  "source": "00b0f074",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0f078`](#insn-00b0f078)

~~~json
{
  "source": "00b0f078",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0f07c`](#insn-00b0f07c)

~~~json
{
  "source": "00b0f07c",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0f088`](#insn-00b0f088)

~~~json
{
  "source": "00b0f088",
  "target": "00b0f0c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0f08c`](#insn-00b0f08c)

~~~json
{
  "source": "00b0f08c",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0f090`](#insn-00b0f090)

~~~json
{
  "source": "00b0f090",
  "target": "00b0f0d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0f094`](#insn-00b0f094)

~~~json
{
  "source": "00b0f094",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0f098`](#insn-00b0f098)

~~~json
{
  "source": "00b0f098",
  "target": "00b0f0a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0f09c`](#insn-00b0f09c)

~~~json
{
  "source": "00b0f09c",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0f0a0`](#insn-00b0f0a0)

~~~json
{
  "source": "00b0f0a0",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0f0a8`](#insn-00b0f0a8)

~~~json
{
  "source": "00b0f0a8",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0f0b0`](#insn-00b0f0b0)

~~~json
{
  "source": "00b0f0b0",
  "target": "00b0f0ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0f0b4`](#insn-00b0f0b4)

~~~json
{
  "source": "00b0f0b4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0f0b8`](#insn-00b0f0b8)

~~~json
{
  "source": "00b0f0b8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0f0bc`](#insn-00b0f0bc)

~~~json
{
  "source": "00b0f0bc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0f0c8`](#insn-00b0f0c8)

~~~json
{
  "source": "00b0f0c8",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0f0cc`](#insn-00b0f0cc)

~~~json
{
  "source": "00b0f0cc",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0f0d0`](#insn-00b0f0d0)

~~~json
{
  "source": "00b0f0d0",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0f0d4`](#insn-00b0f0d4)

~~~json
{
  "source": "00b0f0d4",
  "target": "00b0f094",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0f0d8`](#insn-00b0f0d8)

~~~json
{
  "source": "00b0f0d8",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0f0dc`](#insn-00b0f0dc)

~~~json
{
  "source": "00b0f0dc",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0f0e0`](#insn-00b0f0e0)

~~~json
{
  "source": "00b0f0e0",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0f0e4`](#insn-00b0f0e4)

~~~json
{
  "source": "00b0f0e4",
  "target": "00b0f09c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0f0e8`](#insn-00b0f0e8)

~~~json
{
  "source": "00b0f0e8",
  "target": "00b0f0a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0f0ec`](#insn-00b0f0ec)

~~~json
{
  "source": "00b0f0ec",
  "target": "00bdb090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
