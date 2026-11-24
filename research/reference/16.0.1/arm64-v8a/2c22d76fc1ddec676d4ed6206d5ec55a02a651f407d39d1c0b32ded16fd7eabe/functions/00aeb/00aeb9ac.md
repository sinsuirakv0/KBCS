# 00aeb9ac

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00aeb584`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aeb/00aeb584.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0064.md#compare-cedd26c88dbf717fe870e1bf1c704a9b)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 要確認
  - [v16.0.1 → v16.0.2 候補と検査根拠](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/review-0041.md#review-01e2e1130230dbcc8ea18f125c410f6c)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aeb9ac",
  "name": "FUN_00aeb9ac",
  "size": 420,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "70fdb1566cd55805bce5297bda9c319271851acb9ecc43b3635831e42b9bf0ef",
  "source_text_sha256": "70fdb1566cd55805bce5297bda9c319271851acb9ecc43b3635831e42b9bf0ef",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aeb9ac",
        "00aebb4b"
      ],
      [
        "00aebb90",
        "00aebb93"
      ]
    ],
    "bytes_sha256": "955744a91707a523345fbf96a22d0d174bbe367e585a4e68577bec3e24a7913f",
    "instruction_count": 105,
    "instruction_bytes": 420,
    "body_bytes": 420,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00b28f54](../00b28/00b28f54.md)

## 呼び出し先

- [0048791c](../00487/0048791c.md)
- [0048793c](../00487/0048793c.md)
- [00487e20](../00487/00487e20.md)
- [00488658](../00488/00488658.md)
- [00b110ec](../00b11/00b110ec.md)
- [00c57e90](../00c57/00c57e90.md)
- [00c57eb0](../00c57/00c57eb0.md)
- [00c57ee0](../00c57/00c57ee0.md)
- [00c57fa0](../00c57/00c57fa0.md)
- [00c57fb0](../00c57/00c57fb0.md)
- [00c57fc0](../00c57/00c57fc0.md)

## 関連文字列（未確認候補）

~~~text
"UnitSlot_UnlockData.csv"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 4083 bytes

~~~c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_00aeb9ac(long param_1)

{
  long lVar1;
  undefined8 uVar2;
  undefined8 uVar3;
  undefined *puVar4;
  undefined4 uVar5;
  ulong uVar6;
  undefined4 *puVar7;
  long lVar8;
  ulong local_1c0;
  undefined8 uStack_1b8;
  char *local_1b0;
  undefined **local_1a0;
  void *local_198;
  void *local_190;
  byte local_180;
  void *local_170;
  long local_158;
  undefined *local_150 [8];
  byte local_110;
  void *local_100;
  undefined1 auStack_e8 [160];
  long local_48;
  
                    /* try { // try from 00aeb9b4 to 00beb9c3 has its CatchHandler @ 00aebe90 */
                    /* try { // try from 00aeb9c4 to 00beb9d3 has its CatchHandler @ 00aebe88 */
  lVar1 = tpidr_el0;
  local_48 = *(long *)(lVar1 + 0x28);
                    /* try { // try from 00aeb9d4 to 00beb9eb has its CatchHandler @ 00aebe80 */
  FUN_00487e20(&local_1a0);
  local_1a0 = &PTR_FUN_00c64d38;
  local_1b0 = (char *)_Znwm(0x19);
  uStack_1b8 = _UNK_002c2458;
  local_1c0 = _DAT_002c2450;
  uVar3 = s_UnitSlot_UnlockData_csv_002a6f6c._0_8_;
  uVar2 = CONCAT71(s_UnitSlot_UnlockData_csv_002a6f6c._16_7_,s_UnitSlot_UnlockData_csv_002a6f6c[0xf]
                  );
                    /* try { // try from 00aeba04 to 00beba13 has its CatchHandler @ 00aebe38 */
  *(ulong *)(local_1b0 + 8) =
       CONCAT17(s_UnitSlot_UnlockData_csv_002a6f6c[0xf],s_UnitSlot_UnlockData_csv_002a6f6c._8_7_);
  *(undefined8 *)local_1b0 = uVar3;
  *(undefined8 *)(local_1b0 + 0xf) = uVar2;
                    /* try { // try from 00aeba14 to 00beba37 has its CatchHandler @ 00aebe78 */
  local_1b0[0x17] = '\0';
  uVar6 = FUN_00b110ec(&local_1a0,&local_1c0,0,0);
  if ((local_1c0 & 1) != 0) {
    _ZdlPv(local_1b0);
  }
  if ((uVar6 & 1) != 0) {
    FUN_0048791c(&local_1a0);
    lVar8 = 0x13;
    puVar7 = (undefined4 *)((long)&QWORD_0039b984 + param_1 + 4);
    do {
      FUN_0048791c(&local_1a0);
      uVar5 = FUN_0048793c(&local_1a0,0);
      puVar7[-1] = uVar5;
      uVar5 = FUN_0048793c(&local_1a0,1);
                    /* try { // try from 00aeba80 to 00beba8f has its CatchHandler @ 00aebe8c */
      lVar8 = lVar8 + -1;
      *puVar7 = uVar5;
      puVar7 = puVar7 + 2;
    } while (lVar8 != 0);
                    /* try { // try from 00aeba90 to 00beba9f has its CatchHandler @ 00aebe84 */
    FUN_00488658(&local_1a0);
  }
  puVar4 = PTR__ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c9abb8
  ;
                    /* try { // try from 00aebaa0 to 00bebab7 has its CatchHandler @ 00aebe7c */
  local_158 = *(long *)
               PTR__ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c9abb8
  ;
  local_1a0 = (undefined **)(PTR_DAT_00c9abb0 + 0x10);
  *(undefined8 *)((long)&local_158 + *(long *)(local_158 + -0x18)) =
       *(undefined8 *)
        (PTR__ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c9abb8 +
        0x18);
                    /* try { // try from 00aebad0 to 00bebadf has its CatchHandler @ 00aebe34 */
  local_150[0] = PTR__ZTVNSt6__ndk115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c9abc0
                 + 0x10;
  if ((local_110 & 1) != 0) {
                    /* try { // try from 00aebae0 to 00bebb03 has its CatchHandler @ 00aebe74 */
    _ZdlPv(local_100);
  }
  _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEED2Ev(local_150);
  _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEED2Ev(&local_158,puVar4 + 8);
  _ZNSt6__ndk19basic_iosIcNS_11char_traitsIcEEED1Ev(auStack_e8);
  if ((local_180 & 1) != 0) {
    _ZdlPv(local_170);
  }
  if (local_198 != (void *)0x0) {
    local_190 = local_198;
    _ZdlPv(local_198);
  }
                    /* try { // try from 00aebb30 to 00bebb3f has its CatchHandler @ 00aebe10 */
  if (*(long *)(lVar1 + 0x28) == local_48) {
                    /* try { // try from 00aebb48 to 00bebb57 has its CatchHandler @ 00aebe08 */
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
<a id="insn-00aeb9ac"></a> `00aeb9ac` | `ff 03 07 d1` | sub sp,sp,#0x1c0 | `FALL_THROUGH`
<a id="insn-00aeb9b0"></a> `00aeb9b0` | `fd 7b 18 a9` | stp x29,x30,[sp, #0x180] | `FALL_THROUGH`
<a id="insn-00aeb9b4"></a> `00aeb9b4` | `fc cb 00 f9` | str x28,[sp, #0x190] | `FALL_THROUGH`
<a id="insn-00aeb9b8"></a> `00aeb9b8` | `f6 57 1a a9` | stp x22,x21,[sp, #0x1a0] | `FALL_THROUGH`
<a id="insn-00aeb9bc"></a> `00aeb9bc` | `f4 4f 1b a9` | stp x20,x19,[sp, #0x1b0] | `FALL_THROUGH`
<a id="insn-00aeb9c0"></a> `00aeb9c0` | `fd 03 06 91` | add x29,sp,#0x180 | `FALL_THROUGH`
<a id="insn-00aeb9c4"></a> `00aeb9c4` | `55 d0 3b d5` | mrs x21,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00aeb9c8"></a> `00aeb9c8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aeb9cc"></a> `00aeb9cc` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00aeb9d0"></a> `00aeb9d0` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00aeb9d4"></a> `00aeb9d4` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aeb9d8"></a> `00aeb9d8` | `12 71 e6 97` | bl 0x00487e20 | `UNCONDITIONAL_CALL`
<a id="insn-00aeb9dc"></a> `00aeb9dc` | `c8 0b 00 b0` | adrp x8,0xc64000 | `FALL_THROUGH`
<a id="insn-00aeb9e0"></a> `00aeb9e0` | `08 e1 34 91` | add x8,x8,#0xd38 | `FALL_THROUGH`
<a id="insn-00aeb9e4"></a> `00aeb9e4` | `e8 13 00 f9` | str x8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aeb9e8"></a> `00aeb9e8` | `20 03 80 52` | mov w0,#0x19 | `FALL_THROUGH`
<a id="insn-00aeb9ec"></a> `00aeb9ec` | `29 b1 05 94` | bl 0x00c57e90 | `UNCONDITIONAL_CALL`
<a id="insn-00aeb9f0"></a> `00aeb9f0` | `c8 bd ff f0` | adrp x8,0x2a6000 | `FALL_THROUGH`
<a id="insn-00aeb9f4"></a> `00aeb9f4` | `08 b1 3d 91` | add x8,x8,#0xf6c | `FALL_THROUGH`
<a id="insn-00aeb9f8"></a> `00aeb9f8` | `a9 be ff f0` | adrp x9,0x2c2000 | `FALL_THROUGH`
<a id="insn-00aeb9fc"></a> `00aeb9fc` | `00 01 c0 3d` | ldr q0,[x8] | `FALL_THROUGH`
<a id="insn-00aeba00"></a> `00aeba00` | `08 f1 40 f8` | ldur x8,[x8, #0xf] | `FALL_THROUGH`
<a id="insn-00aeba04"></a> `00aeba04` | `21 15 c1 3d` | ldr q1,[x9, #0x450] | `FALL_THROUGH`
<a id="insn-00aeba08"></a> `00aeba08` | `e0 0b 00 f9` | str x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aeba0c"></a> `00aeba0c` | `00 00 80 3d` | str q0,[x0] | `FALL_THROUGH`
<a id="insn-00aeba10"></a> `00aeba10` | `08 f0 00 f8` | stur x8,[x0, #0xf] | `FALL_THROUGH`
<a id="insn-00aeba14"></a> `00aeba14` | `e1 03 80 3d` | str q1,[sp] | `FALL_THROUGH`
<a id="insn-00aeba18"></a> `00aeba18` | `1f 5c 00 39` | strb wzr,[x0, #0x17] | `FALL_THROUGH`
<a id="insn-00aeba1c"></a> `00aeba1c` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00aeba20"></a> `00aeba20` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00aeba24"></a> `00aeba24` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-00aeba28"></a> `00aeba28` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-00aeba2c"></a> `00aeba2c` | `b0 95 00 94` | bl 0x00b110ec | `UNCONDITIONAL_CALL`
<a id="insn-00aeba30"></a> `00aeba30` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-00aeba34"></a> `00aeba34` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00aeba38"></a> `00aeba38` | `68 00 00 36` | tbz w8,#0x0,0x00aeba44 | `CONDITIONAL_JUMP`
<a id="insn-00aeba3c"></a> `00aeba3c` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aeba40"></a> `00aeba40` | `1c b1 05 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00aeba44"></a> `00aeba44` | `94 02 00 36` | tbz w20,#0x0,0x00aeba94 | `CONDITIONAL_JUMP`
<a id="insn-00aeba48"></a> `00aeba48` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00aeba4c"></a> `00aeba4c` | `b4 6f e6 97` | bl 0x0048791c | `UNCONDITIONAL_CALL`
<a id="insn-00aeba50"></a> `00aeba50` | `68 6e 4e 91` | add x8,x19,#0x39b, LSL #12 | `FALL_THROUGH`
<a id="insn-00aeba54"></a> `00aeba54` | `74 02 80 52` | mov w20,#0x13 | `FALL_THROUGH`
<a id="insn-00aeba58"></a> `00aeba58` | `13 21 26 91` | add x19,x8,#0x988 | `FALL_THROUGH`
<a id="insn-00aeba5c"></a> `00aeba5c` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00aeba60"></a> `00aeba60` | `af 6f e6 97` | bl 0x0048791c | `UNCONDITIONAL_CALL`
<a id="insn-00aeba64"></a> `00aeba64` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00aeba68"></a> `00aeba68` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aeba6c"></a> `00aeba6c` | `b4 6f e6 97` | bl 0x0048793c | `UNCONDITIONAL_CALL`
<a id="insn-00aeba70"></a> `00aeba70` | `60 c2 1f b8` | stur w0,[x19, #-0x4] | `FALL_THROUGH`
<a id="insn-00aeba74"></a> `00aeba74` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00aeba78"></a> `00aeba78` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00aeba7c"></a> `00aeba7c` | `b0 6f e6 97` | bl 0x0048793c | `UNCONDITIONAL_CALL`
<a id="insn-00aeba80"></a> `00aeba80` | `94 06 00 f1` | subs x20,x20,#0x1 | `FALL_THROUGH`
<a id="insn-00aeba84"></a> `00aeba84` | `60 86 00 b8` | str w0,[x19], #0x8 | `FALL_THROUGH`
<a id="insn-00aeba88"></a> `00aeba88` | `a1 fe ff 54` | b.ne 0x00aeba5c | `CONDITIONAL_JUMP`
<a id="insn-00aeba8c"></a> `00aeba8c` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00aeba90"></a> `00aeba90` | `f2 72 e6 97` | bl 0x00488658 | `UNCONDITIONAL_CALL`
<a id="insn-00aeba94"></a> `00aeba94` | `68 0d 00 f0` | adrp x8,0xc9a000 | `FALL_THROUGH`
<a id="insn-00aeba98"></a> `00aeba98` | `76 0d 00 f0` | adrp x22,0xc9a000 | `FALL_THROUGH`
<a id="insn-00aeba9c"></a> `00aeba9c` | `f4 83 00 91` | add x20,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00aebaa0"></a> `00aebaa0` | `08 d9 45 f9` | ldr x8,[x8, #0xbb0] | `FALL_THROUGH`
<a id="insn-00aebaa4"></a> `00aebaa4` | `d6 de 45 f9` | ldr x22,[x22, #0xbb8] | `FALL_THROUGH`
<a id="insn-00aebaa8"></a> `00aebaa8` | `93 22 01 91` | add x19,x20,#0x48 | `FALL_THROUGH`
<a id="insn-00aebaac"></a> `00aebaac` | `c9 02 40 f9` | ldr x9,[x22] | `FALL_THROUGH`
<a id="insn-00aebab0"></a> `00aebab0` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00aebab4"></a> `00aebab4` | `e8 13 00 f9` | str x8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aebab8"></a> `00aebab8` | `e9 37 00 f9` | str x9,[sp, #0x68] | `FALL_THROUGH`
<a id="insn-00aebabc"></a> `00aebabc` | `28 81 5e f8` | ldur x8,[x9, #-0x18] | `FALL_THROUGH`
<a id="insn-00aebac0"></a> `00aebac0` | `c9 0e 40 f9` | ldr x9,[x22, #0x18] | `FALL_THROUGH`
<a id="insn-00aebac4"></a> `00aebac4` | `69 6a 28 f8` | str x9,[x19, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00aebac8"></a> `00aebac8` | `68 0d 00 f0` | adrp x8,0xc9a000 | `FALL_THROUGH`
<a id="insn-00aebacc"></a> `00aebacc` | `08 e1 45 f9` | ldr x8,[x8, #0xbc0] | `FALL_THROUGH`
<a id="insn-00aebad0"></a> `00aebad0` | `e9 c3 42 39` | ldrb w9,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00aebad4"></a> `00aebad4` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00aebad8"></a> `00aebad8` | `e8 3b 00 f9` | str x8,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00aebadc"></a> `00aebadc` | `69 00 00 36` | tbz w9,#0x0,0x00aebae8 | `CONDITIONAL_JUMP`
<a id="insn-00aebae0"></a> `00aebae0` | `e0 63 40 f9` | ldr x0,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00aebae4"></a> `00aebae4` | `f3 b0 05 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00aebae8"></a> `00aebae8` | `80 42 01 91` | add x0,x20,#0x50 | `FALL_THROUGH`
<a id="insn-00aebaec"></a> `00aebaec` | `2d b1 05 94` | bl 0x00c57fa0 | `UNCONDITIONAL_CALL`
<a id="insn-00aebaf0"></a> `00aebaf0` | `c1 22 00 91` | add x1,x22,#0x8 | `FALL_THROUGH`
<a id="insn-00aebaf4"></a> `00aebaf4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aebaf8"></a> `00aebaf8` | `2e b1 05 94` | bl 0x00c57fb0 | `UNCONDITIONAL_CALL`
<a id="insn-00aebafc"></a> `00aebafc` | `80 e2 02 91` | add x0,x20,#0xb8 | `FALL_THROUGH`
<a id="insn-00aebb00"></a> `00aebb00` | `30 b1 05 94` | bl 0x00c57fc0 | `UNCONDITIONAL_CALL`
<a id="insn-00aebb04"></a> `00aebb04` | `e8 03 41 39` | ldrb w8,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00aebb08"></a> `00aebb08` | `68 00 00 36` | tbz w8,#0x0,0x00aebb14 | `CONDITIONAL_JUMP`
<a id="insn-00aebb0c"></a> `00aebb0c` | `e0 2b 40 f9` | ldr x0,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00aebb10"></a> `00aebb10` | `e8 b0 05 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00aebb14"></a> `00aebb14` | `e0 17 40 f9` | ldr x0,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00aebb18"></a> `00aebb18` | `60 00 00 b4` | cbz x0,0x00aebb24 | `CONDITIONAL_JUMP`
<a id="insn-00aebb1c"></a> `00aebb1c` | `e0 1b 00 f9` | str x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aebb20"></a> `00aebb20` | `e4 b0 05 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00aebb24"></a> `00aebb24` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00aebb28"></a> `00aebb28` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aebb2c"></a> `00aebb2c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00aebb30"></a> `00aebb30` | `01 03 00 54` | b.ne 0x00aebb90 | `CONDITIONAL_JUMP`
<a id="insn-00aebb34"></a> `00aebb34` | `f4 4f 5b a9` | ldp x20,x19,[sp, #0x1b0] | `FALL_THROUGH`
<a id="insn-00aebb38"></a> `00aebb38` | `fc cb 40 f9` | ldr x28,[sp, #0x190] | `FALL_THROUGH`
<a id="insn-00aebb3c"></a> `00aebb3c` | `f6 57 5a a9` | ldp x22,x21,[sp, #0x1a0] | `FALL_THROUGH`
<a id="insn-00aebb40"></a> `00aebb40` | `fd 7b 58 a9` | ldp x29,x30,[sp, #0x180] | `FALL_THROUGH`
<a id="insn-00aebb44"></a> `00aebb44` | `ff 03 07 91` | add sp,sp,#0x1c0 | `FALL_THROUGH`
<a id="insn-00aebb48"></a> `00aebb48` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00aebb90"></a> `00aebb90` | `d4 b0 05 94` | bl 0x00c57ee0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aeb9ac`](#insn-00aeb9ac) 範囲 `[['00aeb9ac', '00aeb9b3']]`
  - `FALL_THROUGH` [`00aeb9b0`](#insn-00aeb9b0) → [`00aeb9b4`](#insn-00aeb9b4)
- ブロック [`00aeb9b4`](#insn-00aeb9b4) 範囲 `[['00aeb9b4', '00aeb9c3']]`
  - `FALL_THROUGH` [`00aeb9c0`](#insn-00aeb9c0) → [`00aeb9c4`](#insn-00aeb9c4)
- ブロック [`00aeb9c4`](#insn-00aeb9c4) 範囲 `[['00aeb9c4', '00aeb9d3']]`
  - `FALL_THROUGH` [`00aeb9d0`](#insn-00aeb9d0) → [`00aeb9d4`](#insn-00aeb9d4)
- ブロック [`00aeb9d4`](#insn-00aeb9d4) 範囲 `[['00aeb9d4', '00aeba03']]`
  - `FALL_THROUGH` [`00aeba00`](#insn-00aeba00) → [`00aeba04`](#insn-00aeba04)
- ブロック [`00aeba04`](#insn-00aeba04) 範囲 `[['00aeba04', '00aeba13']]`
  - `FALL_THROUGH` [`00aeba10`](#insn-00aeba10) → [`00aeba14`](#insn-00aeba14)
- ブロック [`00aeba14`](#insn-00aeba14) 範囲 `[['00aeba14', '00aeba3b']]`
  - `CONDITIONAL_JUMP` [`00aeba38`](#insn-00aeba38) → [`00aeba44`](#insn-00aeba44)
  - `FALL_THROUGH` [`00aeba38`](#insn-00aeba38) → [`00aeba3c`](#insn-00aeba3c)
- ブロック [`00aeba3c`](#insn-00aeba3c) 範囲 `[['00aeba3c', '00aeba43']]`
  - `FALL_THROUGH` [`00aeba40`](#insn-00aeba40) → [`00aeba44`](#insn-00aeba44)
- ブロック [`00aeba44`](#insn-00aeba44) 範囲 `[['00aeba44', '00aeba47']]`
  - `CONDITIONAL_JUMP` [`00aeba44`](#insn-00aeba44) → [`00aeba94`](#insn-00aeba94)
  - `FALL_THROUGH` [`00aeba44`](#insn-00aeba44) → [`00aeba48`](#insn-00aeba48)
- ブロック [`00aeba48`](#insn-00aeba48) 範囲 `[['00aeba48', '00aeba5b']]`
  - `FALL_THROUGH` [`00aeba58`](#insn-00aeba58) → [`00aeba5c`](#insn-00aeba5c)
- ブロック [`00aeba5c`](#insn-00aeba5c) 範囲 `[['00aeba5c', '00aeba7f']]`
  - `FALL_THROUGH` [`00aeba7c`](#insn-00aeba7c) → [`00aeba80`](#insn-00aeba80)
- ブロック [`00aeba80`](#insn-00aeba80) 範囲 `[['00aeba80', '00aeba8b']]`
  - `CONDITIONAL_JUMP` [`00aeba88`](#insn-00aeba88) → [`00aeba5c`](#insn-00aeba5c)
  - `FALL_THROUGH` [`00aeba88`](#insn-00aeba88) → [`00aeba8c`](#insn-00aeba8c)
- ブロック [`00aeba8c`](#insn-00aeba8c) 範囲 `[['00aeba8c', '00aeba8f']]`
  - `FALL_THROUGH` [`00aeba8c`](#insn-00aeba8c) → [`00aeba90`](#insn-00aeba90)
- ブロック [`00aeba90`](#insn-00aeba90) 範囲 `[['00aeba90', '00aeba93']]`
  - `FALL_THROUGH` [`00aeba90`](#insn-00aeba90) → [`00aeba94`](#insn-00aeba94)
- ブロック [`00aeba94`](#insn-00aeba94) 範囲 `[['00aeba94', '00aeba9f']]`
  - `FALL_THROUGH` [`00aeba9c`](#insn-00aeba9c) → [`00aebaa0`](#insn-00aebaa0)
- ブロック [`00aebaa0`](#insn-00aebaa0) 範囲 `[['00aebaa0', '00aebacf']]`
  - `FALL_THROUGH` [`00aebacc`](#insn-00aebacc) → [`00aebad0`](#insn-00aebad0)
- ブロック [`00aebad0`](#insn-00aebad0) 範囲 `[['00aebad0', '00aebadf']]`
  - `CONDITIONAL_JUMP` [`00aebadc`](#insn-00aebadc) → [`00aebae8`](#insn-00aebae8)
  - `FALL_THROUGH` [`00aebadc`](#insn-00aebadc) → [`00aebae0`](#insn-00aebae0)
- ブロック [`00aebae0`](#insn-00aebae0) 範囲 `[['00aebae0', '00aebae7']]`
  - `FALL_THROUGH` [`00aebae4`](#insn-00aebae4) → [`00aebae8`](#insn-00aebae8)
- ブロック [`00aebae8`](#insn-00aebae8) 範囲 `[['00aebae8', '00aebb0b']]`
  - `CONDITIONAL_JUMP` [`00aebb08`](#insn-00aebb08) → [`00aebb14`](#insn-00aebb14)
  - `FALL_THROUGH` [`00aebb08`](#insn-00aebb08) → [`00aebb0c`](#insn-00aebb0c)
- ブロック [`00aebb0c`](#insn-00aebb0c) 範囲 `[['00aebb0c', '00aebb13']]`
  - `FALL_THROUGH` [`00aebb10`](#insn-00aebb10) → [`00aebb14`](#insn-00aebb14)
- ブロック [`00aebb14`](#insn-00aebb14) 範囲 `[['00aebb14', '00aebb1b']]`
  - `CONDITIONAL_JUMP` [`00aebb18`](#insn-00aebb18) → [`00aebb24`](#insn-00aebb24)
  - `FALL_THROUGH` [`00aebb18`](#insn-00aebb18) → [`00aebb1c`](#insn-00aebb1c)
- ブロック [`00aebb1c`](#insn-00aebb1c) 範囲 `[['00aebb1c', '00aebb23']]`
  - `FALL_THROUGH` [`00aebb20`](#insn-00aebb20) → [`00aebb24`](#insn-00aebb24)
- ブロック [`00aebb24`](#insn-00aebb24) 範囲 `[['00aebb24', '00aebb2f']]`
  - `FALL_THROUGH` [`00aebb2c`](#insn-00aebb2c) → [`00aebb30`](#insn-00aebb30)
- ブロック [`00aebb30`](#insn-00aebb30) 範囲 `[['00aebb30', '00aebb33']]`
  - `CONDITIONAL_JUMP` [`00aebb30`](#insn-00aebb30) → [`00aebb90`](#insn-00aebb90)
  - `FALL_THROUGH` [`00aebb30`](#insn-00aebb30) → [`00aebb34`](#insn-00aebb34)
- ブロック [`00aebb34`](#insn-00aebb34) 範囲 `[['00aebb34', '00aebb47']]`
  - `FALL_THROUGH` [`00aebb44`](#insn-00aebb44) → [`00aebb48`](#insn-00aebb48)
- ブロック [`00aebb48`](#insn-00aebb48) 範囲 `[['00aebb48', '00aebb4b']]`
- ブロック [`00aebb90`](#insn-00aebb90) 範囲 `[['00aebb90', '00aebb93']]`

## 命令位置別の参照

- [`00aeb9b0`](#insn-00aeb9b0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeb9b4`](#insn-00aeb9b4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeb9b8`](#insn-00aeb9b8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeb9bc`](#insn-00aeb9bc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeb9d4`](#insn-00aeb9d4) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeb9d8`](#insn-00aeb9d8) → [`00487e20`](../00487/00487e20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00487e20` · 推定シンボル `None` · 推定型 `None`
- [`00aeb9e4`](#insn-00aeb9e4) → `00c64d38`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00aeb9e4`](#insn-00aeb9e4) → `Stack[-0x1a0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeb9ec`](#insn-00aeb9ec) → [`00c57e90`](../00c57/00c57e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e90` · 推定シンボル `None` · 推定型 `None`
- [`00aeb9fc`](#insn-00aeb9fc) → `002a6f6c`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aeba00`](#insn-00aeba00) → `002a6f7b`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aeba04`](#insn-00aeba04) → `002c2450`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeba08`](#insn-00aeba08) → `Stack[-0x1b0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeba14`](#insn-00aeba14) → `Stack[-0x1c0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeba2c`](#insn-00aeba2c) → [`00b110ec`](../00b11/00b110ec.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00b110ec` · 推定シンボル `None` · 推定型 `None`
- [`00aeba30`](#insn-00aeba30) → `Stack[-0x1c0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeba38`](#insn-00aeba38) → [`00aeba44`](#insn-00aeba44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeba3c`](#insn-00aeba3c) → `Stack[-0x1b0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeba40`](#insn-00aeba40) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00aeba44`](#insn-00aeba44) → [`00aeba94`](#insn-00aeba94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeba4c`](#insn-00aeba4c) → [`0048791c`](../00487/0048791c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0048791c` · 推定シンボル `None` · 推定型 `None`
- [`00aeba60`](#insn-00aeba60) → [`0048791c`](../00487/0048791c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0048791c` · 推定シンボル `None` · 推定型 `None`
- [`00aeba6c`](#insn-00aeba6c) → [`0048793c`](../00487/0048793c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0048793c` · 推定シンボル `None` · 推定型 `None`
- [`00aeba70`](#insn-00aeba70) → `0039b984`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `qword`
- [`00aeba7c`](#insn-00aeba7c) → [`0048793c`](../00487/0048793c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0048793c` · 推定シンボル `None` · 推定型 `None`
- [`00aeba84`](#insn-00aeba84) → `0039b988`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `qword`
- [`00aeba88`](#insn-00aeba88) → [`00aeba5c`](#insn-00aeba5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeba90`](#insn-00aeba90) → [`00488658`](../00488/00488658.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00488658` · 推定シンボル `None` · 推定型 `None`
- [`00aebaa0`](#insn-00aebaa0) → `00c9abb0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00aebaa4`](#insn-00aebaa4) → `00c9abb8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00aebaac`](#insn-00aebaac) → `00c93200`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE` · 推定型 `pointer __((offset(0x18)))`
- [`00aebab4`](#insn-00aebab4) → `00c65818`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00aebab4`](#insn-00aebab4) → `Stack[-0x1a0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebab8`](#insn-00aebab8) → `00c91010`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00aebab8`](#insn-00aebab8) → `Stack[-0x158]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebabc`](#insn-00aebabc) → `00c90ff8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTVNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE` · 推定型 `undefined8`
- [`00aebac0`](#insn-00aebac0) → `00c93218`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x40)))`
- [`00aebac4`](#insn-00aebac4) → `00c91038`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00aebacc`](#insn-00aebacc) → `00c9abc0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00aebad0`](#insn-00aebad0) → `Stack[-0x110]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebad8`](#insn-00aebad8) → `00c90c08`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[128]`
- [`00aebad8`](#insn-00aebad8) → `Stack[-0x150]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebadc`](#insn-00aebadc) → [`00aebae8`](#insn-00aebae8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebae0`](#insn-00aebae0) → `Stack[-0x100]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebae4`](#insn-00aebae4) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00aebaec`](#insn-00aebaec) → [`00c57fa0`](../00c57/00c57fa0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fa0` · 推定シンボル `None` · 推定型 `None`
- [`00aebaf0`](#insn-00aebaf0) → `00c93208`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x18)))`
- [`00aebaf8`](#insn-00aebaf8) → [`00c57fb0`](../00c57/00c57fb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fb0` · 推定シンボル `None` · 推定型 `None`
- [`00aebb00`](#insn-00aebb00) → [`00c57fc0`](../00c57/00c57fc0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fc0` · 推定シンボル `None` · 推定型 `None`
- [`00aebb04`](#insn-00aebb04) → `Stack[-0x180]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebb08`](#insn-00aebb08) → [`00aebb14`](#insn-00aebb14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebb0c`](#insn-00aebb0c) → `Stack[-0x170]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebb10`](#insn-00aebb10) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00aebb14`](#insn-00aebb14) → `Stack[-0x198]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebb18`](#insn-00aebb18) → [`00aebb24`](#insn-00aebb24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebb1c`](#insn-00aebb1c) → `Stack[-0x190]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebb20`](#insn-00aebb20) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00aebb28`](#insn-00aebb28) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebb30`](#insn-00aebb30) → [`00aebb90`](#insn-00aebb90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebb34`](#insn-00aebb34) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebb38`](#insn-00aebb38) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebb3c`](#insn-00aebb3c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebb40`](#insn-00aebb40) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebb90`](#insn-00aebb90) → [`00c57ee0`](../00c57/00c57ee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ee0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aeb9b0`](#insn-00aeb9b0)

~~~json
{
  "source": "00aeb9b0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeb9b4`](#insn-00aeb9b4)

~~~json
{
  "source": "00aeb9b4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeb9b8`](#insn-00aeb9b8)

~~~json
{
  "source": "00aeb9b8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeb9bc`](#insn-00aeb9bc)

~~~json
{
  "source": "00aeb9bc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeb9d4`](#insn-00aeb9d4)

~~~json
{
  "source": "00aeb9d4",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeb9d8`](#insn-00aeb9d8)

~~~json
{
  "source": "00aeb9d8",
  "target": "00487e20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeb9e4`](#insn-00aeb9e4)

~~~json
{
  "source": "00aeb9e4",
  "target": "00c64d38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c64d38",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aeb9e4`](#insn-00aeb9e4)

~~~json
{
  "source": "00aeb9e4",
  "target": "Stack[-0x1a0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeb9ec`](#insn-00aeb9ec)

~~~json
{
  "source": "00aeb9ec",
  "target": "00c57e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeb9fc`](#insn-00aeb9fc)

~~~json
{
  "source": "00aeb9fc",
  "target": "002a6f6c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a6f6c",
  "offset": 0,
  "size": 24,
  "datatype": "string",
  "bytes": "556e6974536c6f745f556e6c6f636b446174612e63737600",
  "capture_start": "002a6f6c",
  "capture_bytes": 24,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aeba00`](#insn-00aeba00)

~~~json
{
  "source": "00aeba00",
  "target": "002a6f7b",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a6f6c",
  "offset": 15,
  "size": 24,
  "datatype": "string",
  "bytes": "556e6974536c6f745f556e6c6f636b446174612e63737600",
  "capture_start": "002a6f6c",
  "capture_bytes": 24,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aeba04`](#insn-00aeba04)

~~~json
{
  "source": "00aeba04",
  "target": "002c2450",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeba08`](#insn-00aeba08)

~~~json
{
  "source": "00aeba08",
  "target": "Stack[-0x1b0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeba14`](#insn-00aeba14)

~~~json
{
  "source": "00aeba14",
  "target": "Stack[-0x1c0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeba2c`](#insn-00aeba2c)

~~~json
{
  "source": "00aeba2c",
  "target": "00b110ec",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeba30`](#insn-00aeba30)

~~~json
{
  "source": "00aeba30",
  "target": "Stack[-0x1c0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeba38`](#insn-00aeba38)

~~~json
{
  "source": "00aeba38",
  "target": "00aeba44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeba3c`](#insn-00aeba3c)

~~~json
{
  "source": "00aeba3c",
  "target": "Stack[-0x1b0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeba40`](#insn-00aeba40)

~~~json
{
  "source": "00aeba40",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeba44`](#insn-00aeba44)

~~~json
{
  "source": "00aeba44",
  "target": "00aeba94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeba4c`](#insn-00aeba4c)

~~~json
{
  "source": "00aeba4c",
  "target": "0048791c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeba60`](#insn-00aeba60)

~~~json
{
  "source": "00aeba60",
  "target": "0048791c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeba6c`](#insn-00aeba6c)

~~~json
{
  "source": "00aeba6c",
  "target": "0048793c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeba70`](#insn-00aeba70)

~~~json
{
  "source": "00aeba70",
  "target": "0039b984",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0039b984",
  "offset": 0,
  "size": 8,
  "datatype": "qword",
  "bytes": "0400000000000000",
  "capture_start": "0039b984",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aeba7c`](#insn-00aeba7c)

~~~json
{
  "source": "00aeba7c",
  "target": "0048793c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeba84`](#insn-00aeba84)

~~~json
{
  "source": "00aeba84",
  "target": "0039b988",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0039b984",
  "offset": 4,
  "size": 8,
  "datatype": "qword",
  "bytes": "0400000000000000",
  "capture_start": "0039b984",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aeba88`](#insn-00aeba88)

~~~json
{
  "source": "00aeba88",
  "target": "00aeba5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeba90`](#insn-00aeba90)

~~~json
{
  "source": "00aeba90",
  "target": "00488658",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aebaa0`](#insn-00aebaa0)

~~~json
{
  "source": "00aebaa0",
  "target": "00c9abb0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9abb0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aebaa4`](#insn-00aebaa4)

~~~json
{
  "source": "00aebaa4",
  "target": "00c9abb8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9abb8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aebaac`](#insn-00aebaac)

~~~json
{
  "source": "00aebaac",
  "target": "00c93200",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c93200",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x18)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aebab4`](#insn-00aebab4)

~~~json
{
  "source": "00aebab4",
  "target": "00c65818",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c65818",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aebab4`](#insn-00aebab4)

~~~json
{
  "source": "00aebab4",
  "target": "Stack[-0x1a0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebab8`](#insn-00aebab8)

~~~json
{
  "source": "00aebab8",
  "target": "00c91010",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c91010",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aebab8`](#insn-00aebab8)

~~~json
{
  "source": "00aebab8",
  "target": "Stack[-0x158]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebabc`](#insn-00aebabc)

~~~json
{
  "source": "00aebabc",
  "target": "00c90ff8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c90ff8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "bytes": "7000000000000000",
  "capture_start": "00c90ff8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aebac0`](#insn-00aebac0)

~~~json
{
  "source": "00aebac0",
  "target": "00c93218",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c93218",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x40)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aebac4`](#insn-00aebac4)

~~~json
{
  "source": "00aebac4",
  "target": "00c91038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c91038",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aebacc`](#insn-00aebacc)

~~~json
{
  "source": "00aebacc",
  "target": "00c9abc0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9abc0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aebad0`](#insn-00aebad0)

~~~json
{
  "source": "00aebad0",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebad8`](#insn-00aebad8)

~~~json
{
  "source": "00aebad8",
  "target": "00c90c08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c90bf8",
  "offset": 16,
  "size": 128,
  "datatype": "undefined1[128]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`00aebad8`](#insn-00aebad8)

~~~json
{
  "source": "00aebad8",
  "target": "Stack[-0x150]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebadc`](#insn-00aebadc)

~~~json
{
  "source": "00aebadc",
  "target": "00aebae8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebae0`](#insn-00aebae0)

~~~json
{
  "source": "00aebae0",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebae4`](#insn-00aebae4)

~~~json
{
  "source": "00aebae4",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aebaec`](#insn-00aebaec)

~~~json
{
  "source": "00aebaec",
  "target": "00c57fa0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aebaf0`](#insn-00aebaf0)

~~~json
{
  "source": "00aebaf0",
  "target": "00c93208",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c93208",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x18)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aebaf8`](#insn-00aebaf8)

~~~json
{
  "source": "00aebaf8",
  "target": "00c57fb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aebb00`](#insn-00aebb00)

~~~json
{
  "source": "00aebb00",
  "target": "00c57fc0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aebb04`](#insn-00aebb04)

~~~json
{
  "source": "00aebb04",
  "target": "Stack[-0x180]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebb08`](#insn-00aebb08)

~~~json
{
  "source": "00aebb08",
  "target": "00aebb14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebb0c`](#insn-00aebb0c)

~~~json
{
  "source": "00aebb0c",
  "target": "Stack[-0x170]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebb10`](#insn-00aebb10)

~~~json
{
  "source": "00aebb10",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aebb14`](#insn-00aebb14)

~~~json
{
  "source": "00aebb14",
  "target": "Stack[-0x198]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebb18`](#insn-00aebb18)

~~~json
{
  "source": "00aebb18",
  "target": "00aebb24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebb1c`](#insn-00aebb1c)

~~~json
{
  "source": "00aebb1c",
  "target": "Stack[-0x190]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebb20`](#insn-00aebb20)

~~~json
{
  "source": "00aebb20",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aebb28`](#insn-00aebb28)

~~~json
{
  "source": "00aebb28",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebb30`](#insn-00aebb30)

~~~json
{
  "source": "00aebb30",
  "target": "00aebb90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebb34`](#insn-00aebb34)

~~~json
{
  "source": "00aebb34",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebb38`](#insn-00aebb38)

~~~json
{
  "source": "00aebb38",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebb3c`](#insn-00aebb3c)

~~~json
{
  "source": "00aebb3c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebb40`](#insn-00aebb40)

~~~json
{
  "source": "00aebb40",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebb90`](#insn-00aebb90)

~~~json
{
  "source": "00aebb90",
  "target": "00c57ee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
