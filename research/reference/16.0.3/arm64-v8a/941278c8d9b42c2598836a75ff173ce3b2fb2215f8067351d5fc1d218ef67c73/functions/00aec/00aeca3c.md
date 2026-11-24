# 00aeca3c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 要確認
  - [v16.0.2 → v16.0.3 候補と検査根拠](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/review-0081.md#review-efd8d86f9f2d2297040d5ef95410a2bd)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aeca3c",
  "name": "FUN_00aeca3c",
  "size": 420,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7aee08561ca9960b29b52f7fab8ca70984c55d98c80871e92ae699f694a3f337",
  "source_text_sha256": "7aee08561ca9960b29b52f7fab8ca70984c55d98c80871e92ae699f694a3f337",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aeca3c",
        "00aecbdb"
      ],
      [
        "00aecc20",
        "00aecc23"
      ]
    ],
    "bytes_sha256": "98377812deed90077a075cfc8e729acfd9bdec73cd87f7b2942c3297877c0018",
    "instruction_count": 105,
    "instruction_bytes": 420,
    "body_bytes": 420,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00b29fe4](../00b29/00b29fe4.md)

## 呼び出し先

- [00487c7c](../00487/00487c7c.md)
- [00487c9c](../00487/00487c9c.md)
- [00488180](../00488/00488180.md)
- [004889b8](../00488/004889b8.md)
- [00b1217c](../00b12/00b1217c.md)
- [00c58f30](../00c58/00c58f30.md)
- [00c58f50](../00c58/00c58f50.md)
- [00c58f80](../00c58/00c58f80.md)
- [00c59040](../00c59/00c59040.md)
- [00c59050](../00c59/00c59050.md)
- [00c59060](../00c59/00c59060.md)

## 関連文字列（未確認候補）

~~~text
"UnitSlot_UnlockData.csv"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 3788 bytes

~~~c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_00aeca3c(long param_1)

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
  
  lVar1 = tpidr_el0;
  local_48 = *(long *)(lVar1 + 0x28);
  FUN_00488180(&local_1a0);
  local_1a0 = &PTR_FUN_00c65dd8;
  local_1b0 = (char *)_Znwm(0x19);
  uStack_1b8 = _UNK_002c24e8;
  local_1c0 = _DAT_002c24e0;
  uVar3 = s_UnitSlot_UnlockData_csv_002a7068._0_8_;
                    /* try { // try from 00aeca80 to 00beca8f has its CatchHandler @ 00aece8c */
                    /* try { // try from 00aeca90 to 00beca9f has its CatchHandler @ 00aece84 */
  uVar2 = CONCAT71(s_UnitSlot_UnlockData_csv_002a7068._16_7_,s_UnitSlot_UnlockData_csv_002a7068[0xf]
                  );
  *(ulong *)(local_1b0 + 8) =
       CONCAT17(s_UnitSlot_UnlockData_csv_002a7068[0xf],s_UnitSlot_UnlockData_csv_002a7068._8_7_);
  *(undefined8 *)local_1b0 = uVar3;
                    /* try { // try from 00aecaa0 to 00becab7 has its CatchHandler @ 00aece7c */
  *(undefined8 *)(local_1b0 + 0xf) = uVar2;
  local_1b0[0x17] = '\0';
  uVar6 = FUN_00b1217c(&local_1a0,&local_1c0,0,0);
  if ((local_1c0 & 1) != 0) {
                    /* try { // try from 00aecad0 to 00becadf has its CatchHandler @ 00aece34 */
    _ZdlPv(local_1b0);
  }
  if ((uVar6 & 1) != 0) {
    FUN_00487c7c(&local_1a0);
                    /* try { // try from 00aecae0 to 00becb03 has its CatchHandler @ 00aece74 */
    lVar8 = 0x13;
    puVar7 = (undefined4 *)((long)&DWORD_0039b988 + param_1);
    do {
      FUN_00487c7c(&local_1a0);
      uVar5 = FUN_00487c9c(&local_1a0,0);
      puVar7[-1] = uVar5;
      uVar5 = FUN_00487c9c(&local_1a0,1);
      lVar8 = lVar8 + -1;
      *puVar7 = uVar5;
      puVar7 = puVar7 + 2;
    } while (lVar8 != 0);
    FUN_004889b8(&local_1a0);
  }
  puVar4 = PTR__ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c9bc58
  ;
                    /* try { // try from 00aecb30 to 00becb3f has its CatchHandler @ 00aece10 */
  local_158 = *(long *)
               PTR__ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c9bc58
  ;
  local_1a0 = (undefined **)(PTR_DAT_00c9bc50 + 0x10);
                    /* try { // try from 00aecb48 to 00becb57 has its CatchHandler @ 00aece08 */
  *(undefined8 *)((long)&local_158 + *(long *)(local_158 + -0x18)) =
       *(undefined8 *)
        (PTR__ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c9bc58 +
        0x18);
  local_150[0] = PTR__ZTVNSt6__ndk115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c9bc60
                 + 0x10;
                    /* try { // try from 00aecb68 to 00becb6f has its CatchHandler @ 00aece4c */
  if ((local_110 & 1) != 0) {
                    /* try { // try from 00aecb70 to 00becbff has its CatchHandler @ 00aebf84 */
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
  if (*(long *)(lVar1 + 0x28) == local_48) {
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
<a id="insn-00aeca3c"></a> `00aeca3c` | `ff 03 07 d1` | sub sp,sp,#0x1c0 | `FALL_THROUGH`
<a id="insn-00aeca40"></a> `00aeca40` | `fd 7b 18 a9` | stp x29,x30,[sp, #0x180] | `FALL_THROUGH`
<a id="insn-00aeca44"></a> `00aeca44` | `fc cb 00 f9` | str x28,[sp, #0x190] | `FALL_THROUGH`
<a id="insn-00aeca48"></a> `00aeca48` | `f6 57 1a a9` | stp x22,x21,[sp, #0x1a0] | `FALL_THROUGH`
<a id="insn-00aeca4c"></a> `00aeca4c` | `f4 4f 1b a9` | stp x20,x19,[sp, #0x1b0] | `FALL_THROUGH`
<a id="insn-00aeca50"></a> `00aeca50` | `fd 03 06 91` | add x29,sp,#0x180 | `FALL_THROUGH`
<a id="insn-00aeca54"></a> `00aeca54` | `55 d0 3b d5` | mrs x21,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00aeca58"></a> `00aeca58` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aeca5c"></a> `00aeca5c` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00aeca60"></a> `00aeca60` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00aeca64"></a> `00aeca64` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aeca68"></a> `00aeca68` | `c6 6d e6 97` | bl 0x00488180 | `UNCONDITIONAL_CALL`
<a id="insn-00aeca6c"></a> `00aeca6c` | `c8 0b 00 b0` | adrp x8,0xc65000 | `FALL_THROUGH`
<a id="insn-00aeca70"></a> `00aeca70` | `08 61 37 91` | add x8,x8,#0xdd8 | `FALL_THROUGH`
<a id="insn-00aeca74"></a> `00aeca74` | `e8 13 00 f9` | str x8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aeca78"></a> `00aeca78` | `20 03 80 52` | mov w0,#0x19 | `FALL_THROUGH`
<a id="insn-00aeca7c"></a> `00aeca7c` | `2d b1 05 94` | bl 0x00c58f30 | `UNCONDITIONAL_CALL`
<a id="insn-00aeca80"></a> `00aeca80` | `c8 bd ff f0` | adrp x8,0x2a7000 | `FALL_THROUGH`
<a id="insn-00aeca84"></a> `00aeca84` | `08 a1 01 91` | add x8,x8,#0x68 | `FALL_THROUGH`
<a id="insn-00aeca88"></a> `00aeca88` | `a9 be ff d0` | adrp x9,0x2c2000 | `FALL_THROUGH`
<a id="insn-00aeca8c"></a> `00aeca8c` | `00 01 c0 3d` | ldr q0,[x8] | `FALL_THROUGH`
<a id="insn-00aeca90"></a> `00aeca90` | `08 f1 40 f8` | ldur x8,[x8, #0xf] | `FALL_THROUGH`
<a id="insn-00aeca94"></a> `00aeca94` | `21 39 c1 3d` | ldr q1,[x9, #0x4e0] | `FALL_THROUGH`
<a id="insn-00aeca98"></a> `00aeca98` | `e0 0b 00 f9` | str x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aeca9c"></a> `00aeca9c` | `00 00 80 3d` | str q0,[x0] | `FALL_THROUGH`
<a id="insn-00aecaa0"></a> `00aecaa0` | `08 f0 00 f8` | stur x8,[x0, #0xf] | `FALL_THROUGH`
<a id="insn-00aecaa4"></a> `00aecaa4` | `e1 03 80 3d` | str q1,[sp] | `FALL_THROUGH`
<a id="insn-00aecaa8"></a> `00aecaa8` | `1f 5c 00 39` | strb wzr,[x0, #0x17] | `FALL_THROUGH`
<a id="insn-00aecaac"></a> `00aecaac` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00aecab0"></a> `00aecab0` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00aecab4"></a> `00aecab4` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-00aecab8"></a> `00aecab8` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-00aecabc"></a> `00aecabc` | `b0 95 00 94` | bl 0x00b1217c | `UNCONDITIONAL_CALL`
<a id="insn-00aecac0"></a> `00aecac0` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-00aecac4"></a> `00aecac4` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00aecac8"></a> `00aecac8` | `68 00 00 36` | tbz w8,#0x0,0x00aecad4 | `CONDITIONAL_JUMP`
<a id="insn-00aecacc"></a> `00aecacc` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aecad0"></a> `00aecad0` | `20 b1 05 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00aecad4"></a> `00aecad4` | `94 02 00 36` | tbz w20,#0x0,0x00aecb24 | `CONDITIONAL_JUMP`
<a id="insn-00aecad8"></a> `00aecad8` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00aecadc"></a> `00aecadc` | `68 6c e6 97` | bl 0x00487c7c | `UNCONDITIONAL_CALL`
<a id="insn-00aecae0"></a> `00aecae0` | `68 6e 4e 91` | add x8,x19,#0x39b, LSL #12 | `FALL_THROUGH`
<a id="insn-00aecae4"></a> `00aecae4` | `74 02 80 52` | mov w20,#0x13 | `FALL_THROUGH`
<a id="insn-00aecae8"></a> `00aecae8` | `13 21 26 91` | add x19,x8,#0x988 | `FALL_THROUGH`
<a id="insn-00aecaec"></a> `00aecaec` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00aecaf0"></a> `00aecaf0` | `63 6c e6 97` | bl 0x00487c7c | `UNCONDITIONAL_CALL`
<a id="insn-00aecaf4"></a> `00aecaf4` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00aecaf8"></a> `00aecaf8` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aecafc"></a> `00aecafc` | `68 6c e6 97` | bl 0x00487c9c | `UNCONDITIONAL_CALL`
<a id="insn-00aecb00"></a> `00aecb00` | `60 c2 1f b8` | stur w0,[x19, #-0x4] | `FALL_THROUGH`
<a id="insn-00aecb04"></a> `00aecb04` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00aecb08"></a> `00aecb08` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00aecb0c"></a> `00aecb0c` | `64 6c e6 97` | bl 0x00487c9c | `UNCONDITIONAL_CALL`
<a id="insn-00aecb10"></a> `00aecb10` | `94 06 00 f1` | subs x20,x20,#0x1 | `FALL_THROUGH`
<a id="insn-00aecb14"></a> `00aecb14` | `60 86 00 b8` | str w0,[x19], #0x8 | `FALL_THROUGH`
<a id="insn-00aecb18"></a> `00aecb18` | `a1 fe ff 54` | b.ne 0x00aecaec | `CONDITIONAL_JUMP`
<a id="insn-00aecb1c"></a> `00aecb1c` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00aecb20"></a> `00aecb20` | `a6 6f e6 97` | bl 0x004889b8 | `UNCONDITIONAL_CALL`
<a id="insn-00aecb24"></a> `00aecb24` | `68 0d 00 f0` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-00aecb28"></a> `00aecb28` | `76 0d 00 f0` | adrp x22,0xc9b000 | `FALL_THROUGH`
<a id="insn-00aecb2c"></a> `00aecb2c` | `f4 83 00 91` | add x20,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00aecb30"></a> `00aecb30` | `08 29 46 f9` | ldr x8,[x8, #0xc50] | `FALL_THROUGH`
<a id="insn-00aecb34"></a> `00aecb34` | `d6 2e 46 f9` | ldr x22,[x22, #0xc58] | `FALL_THROUGH`
<a id="insn-00aecb38"></a> `00aecb38` | `93 22 01 91` | add x19,x20,#0x48 | `FALL_THROUGH`
<a id="insn-00aecb3c"></a> `00aecb3c` | `c9 02 40 f9` | ldr x9,[x22] | `FALL_THROUGH`
<a id="insn-00aecb40"></a> `00aecb40` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00aecb44"></a> `00aecb44` | `e8 13 00 f9` | str x8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aecb48"></a> `00aecb48` | `e9 37 00 f9` | str x9,[sp, #0x68] | `FALL_THROUGH`
<a id="insn-00aecb4c"></a> `00aecb4c` | `28 81 5e f8` | ldur x8,[x9, #-0x18] | `FALL_THROUGH`
<a id="insn-00aecb50"></a> `00aecb50` | `c9 0e 40 f9` | ldr x9,[x22, #0x18] | `FALL_THROUGH`
<a id="insn-00aecb54"></a> `00aecb54` | `69 6a 28 f8` | str x9,[x19, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00aecb58"></a> `00aecb58` | `68 0d 00 f0` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-00aecb5c"></a> `00aecb5c` | `08 31 46 f9` | ldr x8,[x8, #0xc60] | `FALL_THROUGH`
<a id="insn-00aecb60"></a> `00aecb60` | `e9 c3 42 39` | ldrb w9,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00aecb64"></a> `00aecb64` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00aecb68"></a> `00aecb68` | `e8 3b 00 f9` | str x8,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00aecb6c"></a> `00aecb6c` | `69 00 00 36` | tbz w9,#0x0,0x00aecb78 | `CONDITIONAL_JUMP`
<a id="insn-00aecb70"></a> `00aecb70` | `e0 63 40 f9` | ldr x0,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00aecb74"></a> `00aecb74` | `f7 b0 05 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00aecb78"></a> `00aecb78` | `80 42 01 91` | add x0,x20,#0x50 | `FALL_THROUGH`
<a id="insn-00aecb7c"></a> `00aecb7c` | `31 b1 05 94` | bl 0x00c59040 | `UNCONDITIONAL_CALL`
<a id="insn-00aecb80"></a> `00aecb80` | `c1 22 00 91` | add x1,x22,#0x8 | `FALL_THROUGH`
<a id="insn-00aecb84"></a> `00aecb84` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aecb88"></a> `00aecb88` | `32 b1 05 94` | bl 0x00c59050 | `UNCONDITIONAL_CALL`
<a id="insn-00aecb8c"></a> `00aecb8c` | `80 e2 02 91` | add x0,x20,#0xb8 | `FALL_THROUGH`
<a id="insn-00aecb90"></a> `00aecb90` | `34 b1 05 94` | bl 0x00c59060 | `UNCONDITIONAL_CALL`
<a id="insn-00aecb94"></a> `00aecb94` | `e8 03 41 39` | ldrb w8,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00aecb98"></a> `00aecb98` | `68 00 00 36` | tbz w8,#0x0,0x00aecba4 | `CONDITIONAL_JUMP`
<a id="insn-00aecb9c"></a> `00aecb9c` | `e0 2b 40 f9` | ldr x0,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00aecba0"></a> `00aecba0` | `ec b0 05 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00aecba4"></a> `00aecba4` | `e0 17 40 f9` | ldr x0,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00aecba8"></a> `00aecba8` | `60 00 00 b4` | cbz x0,0x00aecbb4 | `CONDITIONAL_JUMP`
<a id="insn-00aecbac"></a> `00aecbac` | `e0 1b 00 f9` | str x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aecbb0"></a> `00aecbb0` | `e8 b0 05 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00aecbb4"></a> `00aecbb4` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00aecbb8"></a> `00aecbb8` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aecbbc"></a> `00aecbbc` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00aecbc0"></a> `00aecbc0` | `01 03 00 54` | b.ne 0x00aecc20 | `CONDITIONAL_JUMP`
<a id="insn-00aecbc4"></a> `00aecbc4` | `f4 4f 5b a9` | ldp x20,x19,[sp, #0x1b0] | `FALL_THROUGH`
<a id="insn-00aecbc8"></a> `00aecbc8` | `fc cb 40 f9` | ldr x28,[sp, #0x190] | `FALL_THROUGH`
<a id="insn-00aecbcc"></a> `00aecbcc` | `f6 57 5a a9` | ldp x22,x21,[sp, #0x1a0] | `FALL_THROUGH`
<a id="insn-00aecbd0"></a> `00aecbd0` | `fd 7b 58 a9` | ldp x29,x30,[sp, #0x180] | `FALL_THROUGH`
<a id="insn-00aecbd4"></a> `00aecbd4` | `ff 03 07 91` | add sp,sp,#0x1c0 | `FALL_THROUGH`
<a id="insn-00aecbd8"></a> `00aecbd8` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00aecc20"></a> `00aecc20` | `d8 b0 05 94` | bl 0x00c58f80 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aeca3c`](#insn-00aeca3c) 範囲 `[['00aeca3c', '00aeca7f']]`
  - `FALL_THROUGH` [`00aeca7c`](#insn-00aeca7c) → [`00aeca80`](#insn-00aeca80)
- ブロック [`00aeca80`](#insn-00aeca80) 範囲 `[['00aeca80', '00aeca8f']]`
  - `FALL_THROUGH` [`00aeca8c`](#insn-00aeca8c) → [`00aeca90`](#insn-00aeca90)
- ブロック [`00aeca90`](#insn-00aeca90) 範囲 `[['00aeca90', '00aeca9f']]`
  - `FALL_THROUGH` [`00aeca9c`](#insn-00aeca9c) → [`00aecaa0`](#insn-00aecaa0)
- ブロック [`00aecaa0`](#insn-00aecaa0) 範囲 `[['00aecaa0', '00aecacb']]`
  - `CONDITIONAL_JUMP` [`00aecac8`](#insn-00aecac8) → [`00aecad4`](#insn-00aecad4)
  - `FALL_THROUGH` [`00aecac8`](#insn-00aecac8) → [`00aecacc`](#insn-00aecacc)
- ブロック [`00aecacc`](#insn-00aecacc) 範囲 `[['00aecacc', '00aecacf']]`
  - `FALL_THROUGH` [`00aecacc`](#insn-00aecacc) → [`00aecad0`](#insn-00aecad0)
- ブロック [`00aecad0`](#insn-00aecad0) 範囲 `[['00aecad0', '00aecad3']]`
  - `FALL_THROUGH` [`00aecad0`](#insn-00aecad0) → [`00aecad4`](#insn-00aecad4)
- ブロック [`00aecad4`](#insn-00aecad4) 範囲 `[['00aecad4', '00aecad7']]`
  - `CONDITIONAL_JUMP` [`00aecad4`](#insn-00aecad4) → [`00aecb24`](#insn-00aecb24)
  - `FALL_THROUGH` [`00aecad4`](#insn-00aecad4) → [`00aecad8`](#insn-00aecad8)
- ブロック [`00aecad8`](#insn-00aecad8) 範囲 `[['00aecad8', '00aecadf']]`
  - `FALL_THROUGH` [`00aecadc`](#insn-00aecadc) → [`00aecae0`](#insn-00aecae0)
- ブロック [`00aecae0`](#insn-00aecae0) 範囲 `[['00aecae0', '00aecaeb']]`
  - `FALL_THROUGH` [`00aecae8`](#insn-00aecae8) → [`00aecaec`](#insn-00aecaec)
- ブロック [`00aecaec`](#insn-00aecaec) 範囲 `[['00aecaec', '00aecb1b']]`
  - `CONDITIONAL_JUMP` [`00aecb18`](#insn-00aecb18) → [`00aecaec`](#insn-00aecaec)
  - `FALL_THROUGH` [`00aecb18`](#insn-00aecb18) → [`00aecb1c`](#insn-00aecb1c)
- ブロック [`00aecb1c`](#insn-00aecb1c) 範囲 `[['00aecb1c', '00aecb23']]`
  - `FALL_THROUGH` [`00aecb20`](#insn-00aecb20) → [`00aecb24`](#insn-00aecb24)
- ブロック [`00aecb24`](#insn-00aecb24) 範囲 `[['00aecb24', '00aecb2f']]`
  - `FALL_THROUGH` [`00aecb2c`](#insn-00aecb2c) → [`00aecb30`](#insn-00aecb30)
- ブロック [`00aecb30`](#insn-00aecb30) 範囲 `[['00aecb30', '00aecb47']]`
  - `FALL_THROUGH` [`00aecb44`](#insn-00aecb44) → [`00aecb48`](#insn-00aecb48)
- ブロック [`00aecb48`](#insn-00aecb48) 範囲 `[['00aecb48', '00aecb67']]`
  - `FALL_THROUGH` [`00aecb64`](#insn-00aecb64) → [`00aecb68`](#insn-00aecb68)
- ブロック [`00aecb68`](#insn-00aecb68) 範囲 `[['00aecb68', '00aecb6f']]`
  - `CONDITIONAL_JUMP` [`00aecb6c`](#insn-00aecb6c) → [`00aecb78`](#insn-00aecb78)
  - `FALL_THROUGH` [`00aecb6c`](#insn-00aecb6c) → [`00aecb70`](#insn-00aecb70)
- ブロック [`00aecb70`](#insn-00aecb70) 範囲 `[['00aecb70', '00aecb77']]`
  - `FALL_THROUGH` [`00aecb74`](#insn-00aecb74) → [`00aecb78`](#insn-00aecb78)
- ブロック [`00aecb78`](#insn-00aecb78) 範囲 `[['00aecb78', '00aecb9b']]`
  - `CONDITIONAL_JUMP` [`00aecb98`](#insn-00aecb98) → [`00aecba4`](#insn-00aecba4)
  - `FALL_THROUGH` [`00aecb98`](#insn-00aecb98) → [`00aecb9c`](#insn-00aecb9c)
- ブロック [`00aecb9c`](#insn-00aecb9c) 範囲 `[['00aecb9c', '00aecba3']]`
  - `FALL_THROUGH` [`00aecba0`](#insn-00aecba0) → [`00aecba4`](#insn-00aecba4)
- ブロック [`00aecba4`](#insn-00aecba4) 範囲 `[['00aecba4', '00aecbab']]`
  - `CONDITIONAL_JUMP` [`00aecba8`](#insn-00aecba8) → [`00aecbb4`](#insn-00aecbb4)
  - `FALL_THROUGH` [`00aecba8`](#insn-00aecba8) → [`00aecbac`](#insn-00aecbac)
- ブロック [`00aecbac`](#insn-00aecbac) 範囲 `[['00aecbac', '00aecbb3']]`
  - `FALL_THROUGH` [`00aecbb0`](#insn-00aecbb0) → [`00aecbb4`](#insn-00aecbb4)
- ブロック [`00aecbb4`](#insn-00aecbb4) 範囲 `[['00aecbb4', '00aecbc3']]`
  - `CONDITIONAL_JUMP` [`00aecbc0`](#insn-00aecbc0) → [`00aecc20`](#insn-00aecc20)
  - `FALL_THROUGH` [`00aecbc0`](#insn-00aecbc0) → [`00aecbc4`](#insn-00aecbc4)
- ブロック [`00aecbc4`](#insn-00aecbc4) 範囲 `[['00aecbc4', '00aecbdb']]`
- ブロック [`00aecc20`](#insn-00aecc20) 範囲 `[['00aecc20', '00aecc23']]`

## 命令位置別の参照

- [`00aeca40`](#insn-00aeca40) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeca44`](#insn-00aeca44) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeca48`](#insn-00aeca48) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeca4c`](#insn-00aeca4c) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeca64`](#insn-00aeca64) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeca68`](#insn-00aeca68) → [`00488180`](../00488/00488180.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00488180` · 推定シンボル `None` · 推定型 `None`
- [`00aeca74`](#insn-00aeca74) → `00c65dd8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00aeca74`](#insn-00aeca74) → `Stack[-0x1a0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeca7c`](#insn-00aeca7c) → [`00c58f30`](../00c58/00c58f30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f30` · 推定シンボル `None` · 推定型 `None`
- [`00aeca8c`](#insn-00aeca8c) → `002a7068`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aeca90`](#insn-00aeca90) → `002a7077`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aeca94`](#insn-00aeca94) → `002c24e0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeca98`](#insn-00aeca98) → `Stack[-0x1b0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecaa4`](#insn-00aecaa4) → `Stack[-0x1c0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecabc`](#insn-00aecabc) → [`00b1217c`](../00b12/00b1217c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00b1217c` · 推定シンボル `None` · 推定型 `None`
- [`00aecac0`](#insn-00aecac0) → `Stack[-0x1c0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecac8`](#insn-00aecac8) → [`00aecad4`](#insn-00aecad4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecacc`](#insn-00aecacc) → `Stack[-0x1b0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecad0`](#insn-00aecad0) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00aecad4`](#insn-00aecad4) → [`00aecb24`](#insn-00aecb24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecadc`](#insn-00aecadc) → [`00487c7c`](../00487/00487c7c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00487c7c` · 推定シンボル `None` · 推定型 `None`
- [`00aecaf0`](#insn-00aecaf0) → [`00487c7c`](../00487/00487c7c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00487c7c` · 推定シンボル `None` · 推定型 `None`
- [`00aecafc`](#insn-00aecafc) → [`00487c9c`](../00487/00487c9c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00487c9c` · 推定シンボル `None` · 推定型 `None`
- [`00aecb00`](#insn-00aecb00) → `0039b984`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00aecb0c`](#insn-00aecb0c) → [`00487c9c`](../00487/00487c9c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00487c9c` · 推定シンボル `None` · 推定型 `None`
- [`00aecb14`](#insn-00aecb14) → `0039b988`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00aecb18`](#insn-00aecb18) → [`00aecaec`](#insn-00aecaec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecb20`](#insn-00aecb20) → [`004889b8`](../00488/004889b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004889b8` · 推定シンボル `None` · 推定型 `None`
- [`00aecb30`](#insn-00aecb30) → `00c9bc50`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00aecb34`](#insn-00aecb34) → `00c9bc58`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00aecb3c`](#insn-00aecb3c) → `00c942a0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE` · 推定型 `pointer __((offset(0x18)))`
- [`00aecb44`](#insn-00aecb44) → `00c668b8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00aecb44`](#insn-00aecb44) → `Stack[-0x1a0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecb48`](#insn-00aecb48) → `00c920b0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00aecb48`](#insn-00aecb48) → `Stack[-0x158]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecb4c`](#insn-00aecb4c) → `00c92098`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTVNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE` · 推定型 `undefined8`
- [`00aecb50`](#insn-00aecb50) → `00c942b8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x40)))`
- [`00aecb54`](#insn-00aecb54) → `00c920d8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00aecb5c`](#insn-00aecb5c) → `00c9bc60`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00aecb60`](#insn-00aecb60) → `Stack[-0x110]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecb68`](#insn-00aecb68) → `00c91ca8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[128]`
- [`00aecb68`](#insn-00aecb68) → `Stack[-0x150]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecb6c`](#insn-00aecb6c) → [`00aecb78`](#insn-00aecb78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecb70`](#insn-00aecb70) → `Stack[-0x100]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecb74`](#insn-00aecb74) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00aecb7c`](#insn-00aecb7c) → [`00c59040`](../00c59/00c59040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59040` · 推定シンボル `None` · 推定型 `None`
- [`00aecb80`](#insn-00aecb80) → `00c942a8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x18)))`
- [`00aecb88`](#insn-00aecb88) → [`00c59050`](../00c59/00c59050.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59050` · 推定シンボル `None` · 推定型 `None`
- [`00aecb90`](#insn-00aecb90) → [`00c59060`](../00c59/00c59060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59060` · 推定シンボル `None` · 推定型 `None`
- [`00aecb94`](#insn-00aecb94) → `Stack[-0x180]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecb98`](#insn-00aecb98) → [`00aecba4`](#insn-00aecba4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecb9c`](#insn-00aecb9c) → `Stack[-0x170]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecba0`](#insn-00aecba0) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00aecba4`](#insn-00aecba4) → `Stack[-0x198]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecba8`](#insn-00aecba8) → [`00aecbb4`](#insn-00aecbb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecbac`](#insn-00aecbac) → `Stack[-0x190]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecbb0`](#insn-00aecbb0) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00aecbb8`](#insn-00aecbb8) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecbc0`](#insn-00aecbc0) → [`00aecc20`](#insn-00aecc20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecbc4`](#insn-00aecbc4) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecbc8`](#insn-00aecbc8) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecbcc`](#insn-00aecbcc) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecbd0`](#insn-00aecbd0) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecc20`](#insn-00aecc20) → [`00c58f80`](../00c58/00c58f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f80` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aeca40`](#insn-00aeca40)

~~~json
{
  "source": "00aeca40",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeca44`](#insn-00aeca44)

~~~json
{
  "source": "00aeca44",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeca48`](#insn-00aeca48)

~~~json
{
  "source": "00aeca48",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeca4c`](#insn-00aeca4c)

~~~json
{
  "source": "00aeca4c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeca64`](#insn-00aeca64)

~~~json
{
  "source": "00aeca64",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeca68`](#insn-00aeca68)

~~~json
{
  "source": "00aeca68",
  "target": "00488180",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeca74`](#insn-00aeca74)

~~~json
{
  "source": "00aeca74",
  "target": "00c65dd8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c65dd8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aeca74`](#insn-00aeca74)

~~~json
{
  "source": "00aeca74",
  "target": "Stack[-0x1a0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeca7c`](#insn-00aeca7c)

~~~json
{
  "source": "00aeca7c",
  "target": "00c58f30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeca8c`](#insn-00aeca8c)

~~~json
{
  "source": "00aeca8c",
  "target": "002a7068",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a7068",
  "offset": 0,
  "size": 24,
  "datatype": "string",
  "bytes": "556e6974536c6f745f556e6c6f636b446174612e63737600",
  "capture_start": "002a7068",
  "capture_bytes": 24,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aeca90`](#insn-00aeca90)

~~~json
{
  "source": "00aeca90",
  "target": "002a7077",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a7068",
  "offset": 15,
  "size": 24,
  "datatype": "string",
  "bytes": "556e6974536c6f745f556e6c6f636b446174612e63737600",
  "capture_start": "002a7068",
  "capture_bytes": 24,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aeca94`](#insn-00aeca94)

~~~json
{
  "source": "00aeca94",
  "target": "002c24e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeca98`](#insn-00aeca98)

~~~json
{
  "source": "00aeca98",
  "target": "Stack[-0x1b0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecaa4`](#insn-00aecaa4)

~~~json
{
  "source": "00aecaa4",
  "target": "Stack[-0x1c0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecabc`](#insn-00aecabc)

~~~json
{
  "source": "00aecabc",
  "target": "00b1217c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aecac0`](#insn-00aecac0)

~~~json
{
  "source": "00aecac0",
  "target": "Stack[-0x1c0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecac8`](#insn-00aecac8)

~~~json
{
  "source": "00aecac8",
  "target": "00aecad4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecacc`](#insn-00aecacc)

~~~json
{
  "source": "00aecacc",
  "target": "Stack[-0x1b0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecad0`](#insn-00aecad0)

~~~json
{
  "source": "00aecad0",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aecad4`](#insn-00aecad4)

~~~json
{
  "source": "00aecad4",
  "target": "00aecb24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecadc`](#insn-00aecadc)

~~~json
{
  "source": "00aecadc",
  "target": "00487c7c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aecaf0`](#insn-00aecaf0)

~~~json
{
  "source": "00aecaf0",
  "target": "00487c7c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aecafc`](#insn-00aecafc)

~~~json
{
  "source": "00aecafc",
  "target": "00487c9c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aecb00`](#insn-00aecb00)

~~~json
{
  "source": "00aecb00",
  "target": "0039b984",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0039b984",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "ec810500",
  "capture_start": "0039b984",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aecb0c`](#insn-00aecb0c)

~~~json
{
  "source": "00aecb0c",
  "target": "00487c9c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aecb14`](#insn-00aecb14)

~~~json
{
  "source": "00aecb14",
  "target": "0039b988",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0039b988",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "3c8c4f00",
  "capture_start": "0039b988",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aecb18`](#insn-00aecb18)

~~~json
{
  "source": "00aecb18",
  "target": "00aecaec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecb20`](#insn-00aecb20)

~~~json
{
  "source": "00aecb20",
  "target": "004889b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aecb30`](#insn-00aecb30)

~~~json
{
  "source": "00aecb30",
  "target": "00c9bc50",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9bc50",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aecb34`](#insn-00aecb34)

~~~json
{
  "source": "00aecb34",
  "target": "00c9bc58",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9bc58",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aecb3c`](#insn-00aecb3c)

~~~json
{
  "source": "00aecb3c",
  "target": "00c942a0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c942a0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x18)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aecb44`](#insn-00aecb44)

~~~json
{
  "source": "00aecb44",
  "target": "00c668b8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c668b8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aecb44`](#insn-00aecb44)

~~~json
{
  "source": "00aecb44",
  "target": "Stack[-0x1a0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecb48`](#insn-00aecb48)

~~~json
{
  "source": "00aecb48",
  "target": "00c920b0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c920b0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aecb48`](#insn-00aecb48)

~~~json
{
  "source": "00aecb48",
  "target": "Stack[-0x158]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecb4c`](#insn-00aecb4c)

~~~json
{
  "source": "00aecb4c",
  "target": "00c92098",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c92098",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "bytes": "7000000000000000",
  "capture_start": "00c92098",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aecb50`](#insn-00aecb50)

~~~json
{
  "source": "00aecb50",
  "target": "00c942b8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c942b8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x40)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aecb54`](#insn-00aecb54)

~~~json
{
  "source": "00aecb54",
  "target": "00c920d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c920d8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aecb5c`](#insn-00aecb5c)

~~~json
{
  "source": "00aecb5c",
  "target": "00c9bc60",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9bc60",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aecb60`](#insn-00aecb60)

~~~json
{
  "source": "00aecb60",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecb68`](#insn-00aecb68)

~~~json
{
  "source": "00aecb68",
  "target": "00c91ca8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c91c98",
  "offset": 16,
  "size": 128,
  "datatype": "undefined1[128]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`00aecb68`](#insn-00aecb68)

~~~json
{
  "source": "00aecb68",
  "target": "Stack[-0x150]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecb6c`](#insn-00aecb6c)

~~~json
{
  "source": "00aecb6c",
  "target": "00aecb78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecb70`](#insn-00aecb70)

~~~json
{
  "source": "00aecb70",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecb74`](#insn-00aecb74)

~~~json
{
  "source": "00aecb74",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aecb7c`](#insn-00aecb7c)

~~~json
{
  "source": "00aecb7c",
  "target": "00c59040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aecb80`](#insn-00aecb80)

~~~json
{
  "source": "00aecb80",
  "target": "00c942a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c942a8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x18)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aecb88`](#insn-00aecb88)

~~~json
{
  "source": "00aecb88",
  "target": "00c59050",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aecb90`](#insn-00aecb90)

~~~json
{
  "source": "00aecb90",
  "target": "00c59060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aecb94`](#insn-00aecb94)

~~~json
{
  "source": "00aecb94",
  "target": "Stack[-0x180]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecb98`](#insn-00aecb98)

~~~json
{
  "source": "00aecb98",
  "target": "00aecba4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecb9c`](#insn-00aecb9c)

~~~json
{
  "source": "00aecb9c",
  "target": "Stack[-0x170]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecba0`](#insn-00aecba0)

~~~json
{
  "source": "00aecba0",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aecba4`](#insn-00aecba4)

~~~json
{
  "source": "00aecba4",
  "target": "Stack[-0x198]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecba8`](#insn-00aecba8)

~~~json
{
  "source": "00aecba8",
  "target": "00aecbb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecbac`](#insn-00aecbac)

~~~json
{
  "source": "00aecbac",
  "target": "Stack[-0x190]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecbb0`](#insn-00aecbb0)

~~~json
{
  "source": "00aecbb0",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aecbb8`](#insn-00aecbb8)

~~~json
{
  "source": "00aecbb8",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecbc0`](#insn-00aecbc0)

~~~json
{
  "source": "00aecbc0",
  "target": "00aecc20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecbc4`](#insn-00aecbc4)

~~~json
{
  "source": "00aecbc4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecbc8`](#insn-00aecbc8)

~~~json
{
  "source": "00aecbc8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecbcc`](#insn-00aecbcc)

~~~json
{
  "source": "00aecbcc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecbd0`](#insn-00aecbd0)

~~~json
{
  "source": "00aecbd0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecc20`](#insn-00aecc20)

~~~json
{
  "source": "00aecc20",
  "target": "00c58f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
