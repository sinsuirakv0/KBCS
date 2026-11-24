# 006dadcc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `006dad74`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006da/006dad74.md) · 移動量 `+0x58`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0032.md#compare-ad2353d9d66ebaac8c54870ab9c2198b)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `006db17c`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006db/006db17c.md) · 移動量 `+0x3b0`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0034.md#compare-95aa2fc9f868f2583fd88c0921573f33)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "006dadcc",
  "name": "FUN_006dadcc",
  "size": 400,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9188979e18b5a60d774cce7363860d5932b3b295313e576c6853858b3861bfbd",
  "source_text_sha256": "9188979e18b5a60d774cce7363860d5932b3b295313e576c6853858b3861bfbd",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "006dadcc",
        "006daf57"
      ],
      [
        "006daf98",
        "006daf9b"
      ]
    ],
    "bytes_sha256": "c7e9c02277157678b5977435f99c3785c6f6cf8d25edd2c27aef3466d1ddaadf",
    "instruction_count": 100,
    "instruction_bytes": 400,
    "body_bytes": 400,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00b11e20](../00b11/00b11e20.md)

## 呼び出し先

- [00487e60](../00487/00487e60.md)
- [00488698](../00488/00488698.md)
- [006dac04](../006da/006dac04.md)
- [00b11188](../00b11/00b11188.md)
- [00c57f80](../00c57/00c57f80.md)
- [00c57fb0](../00c57/00c57fb0.md)
- [00c58070](../00c58/00c58070.md)
- [00c58080](../00c58/00c58080.md)
- [00c58090](../00c58/00c58090.md)

## 関連文字列（未確認候補）

~~~text
"Gamatoto_Bonus.csv"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 5341 bytes

~~~c

void FUN_006dadcc(long param_1)

{
  long lVar1;
  undefined *puVar2;
  ulong uVar3;
  void *__ptr;
  byte local_1c0;
  undefined7 uStack_1bf;
  char cStack_1b8;
  undefined7 uStack_1b7;
  char cStack_1b0;
  undefined2 uStack_1af;
  undefined1 uStack_1ad;
  undefined4 uStack_1ac;
  undefined8 local_1a8;
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
  
                    /* try { // try from 006dadcc to 007daddb has its CatchHandler @ 006daf04 */
  lVar1 = tpidr_el0;
  local_48 = *(long *)(lVar1 + 0x28);
  FUN_00487e60(&local_1a0);
  local_1a0 = &PTR_FUN_00c64e08;
                    /* try { // try from 006dae0c to 007dae1f has its CatchHandler @ 006daf30 */
  local_1c0 = 0x24;
  uStack_1af = 0x7673;
                    /* try { // try from 006dae24 to 007dae5b has its CatchHandler @ 006daf48 */
  uStack_1ad = 0;
  uStack_1b7 = (undefined7)s_Gamatoto_Bonus_csv_002b76bb._8_8_;
  cStack_1b0 = SUB81(s_Gamatoto_Bonus_csv_002b76bb._8_8_,7);
  uStack_1bf = (undefined7)s_Gamatoto_Bonus_csv_002b76bb._0_8_;
  cStack_1b8 = SUB81(s_Gamatoto_Bonus_csv_002b76bb._0_8_,7);
  uVar3 = FUN_00b11188(&local_1a0,&local_1c0,0,0);
  if ((local_1c0 & 1) != 0) {
    _ZdlPv((void *)CONCAT44(uStack_1ac,CONCAT13(uStack_1ad,CONCAT21(uStack_1af,cStack_1b0))));
  }
  if ((uVar3 & 1) != 0) {
                    /* try { // try from 006dae5c to 007daecb has its CatchHandler @ 006da6ec */
    FUN_006dac04(&local_1c0,&local_1a0);
    __ptr = *(void **)(param_1 + 0x20);
    *(ulong *)(param_1 + 0x18) = CONCAT71(uStack_1bf,local_1c0);
    if (__ptr != (void *)0x0) {
      *(void **)(param_1 + 0x28) = __ptr;
      _ZdlPv(__ptr);
      *(undefined8 *)(param_1 + 0x20) = 0;
      *(undefined8 *)(param_1 + 0x28) = 0;
      *(undefined8 *)(param_1 + 0x30) = 0;
    }
    *(ulong *)(param_1 + 0x28) =
         CONCAT44(uStack_1ac,CONCAT13(uStack_1ad,CONCAT21(uStack_1af,cStack_1b0)));
    *(ulong *)(param_1 + 0x20) = CONCAT71(uStack_1b7,cStack_1b8);
    *(undefined8 *)(param_1 + 0x30) = local_1a8;
    FUN_00488698(&local_1a0);
  }
  puVar2 = PTR__ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c9ac88
  ;
  local_158 = *(long *)
               PTR__ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c9ac88
  ;
  local_1a0 = (undefined **)(PTR_DAT_00c9ac80 + 0x10);
                    /* try { // try from 006daecc to 007daed3 has its CatchHandler @ 006daf70 */
  *(undefined8 *)((long)&local_158 + *(long *)(local_158 + -0x18)) =
       *(undefined8 *)
        (PTR__ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c9ac88 +
        0x18);
  local_150[0] = PTR__ZTVNSt6__ndk115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c9ac90
                 + 0x10;
                    /* try { // try from 006daee4 to 007daeeb has its CatchHandler @ 006daf68 */
  if ((local_110 & 1) != 0) {
                    /* catch() { ... } // from try @ 006dad34 with catch @ 006daeec
                       try { // try from 006daeec to 007dafcb has its CatchHandler @ 006da6ec */
    _ZdlPv(local_100);
  }
                    /* catch() { ... } // from try @ 006dacf8 with catch @ 006daef4 */
                    /* catch() { ... } // from try @ 006dace8 with catch @ 006daef8 */
  _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEED2Ev(local_150);
                    /* catch() { ... } // from try @ 006dacd0 with catch @ 006daf00 */
                    /* catch() { ... } // from try @ 006dadcc with catch @ 006daf04 */
  _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEED2Ev(&local_158,puVar2 + 8);
                    /* catch() { ... } // from try @ 006daa80 with catch @ 006daf08
                       catch() { ... } // from try @ 006dadbc with catch @ 006daf08 */
  _ZNSt6__ndk19basic_iosIcNS_11char_traitsIcEEED1Ev(auStack_e8);
                    /* catch() { ... } // from try @ 006dad68 with catch @ 006daf10 */
  if ((local_180 & 1) != 0) {
                    /* catch() { ... } // from try @ 006daa3c with catch @ 006daf18 */
                    /* catch() { ... } // from try @ 006daa2c with catch @ 006daf1c */
    _ZdlPv(local_170);
  }
                    /* catch() { ... } // from try @ 006dacc0 with catch @ 006daf24 */
  if (local_198 != (void *)0x0) {
                    /* catch() { ... } // from try @ 006daa9c with catch @ 006daf28 */
    local_190 = local_198;
                    /* catch() { ... } // from try @ 006dad80 with catch @ 006daf2c */
    _ZdlPv(local_198);
  }
                    /* catch() { ... } // from try @ 006dae0c with catch @ 006daf30 */
                    /* catch() { ... } // from try @ 006dac80 with catch @ 006daf38 */
  if (*(long *)(lVar1 + 0x28) == local_48) {
                    /* catch() { ... } // from try @ 006daaac with catch @ 006daf40 */
                    /* catch() { ... } // from try @ 006da9d0 with catch @ 006daf44 */
                    /* catch() { ... } // from try @ 006dae24 with catch @ 006daf48 */
                    /* catch() { ... } // from try @ 006dac38 with catch @ 006daf4c */
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
<a id="insn-006dadcc"></a> `006dadcc` | `ff 03 07 d1` | sub sp,sp,#0x1c0 | `FALL_THROUGH`
<a id="insn-006dadd0"></a> `006dadd0` | `fd 7b 18 a9` | stp x29,x30,[sp, #0x180] | `FALL_THROUGH`
<a id="insn-006dadd4"></a> `006dadd4` | `fc cb 00 f9` | str x28,[sp, #0x190] | `FALL_THROUGH`
<a id="insn-006dadd8"></a> `006dadd8` | `f6 57 1a a9` | stp x22,x21,[sp, #0x1a0] | `FALL_THROUGH`
<a id="insn-006daddc"></a> `006daddc` | `f4 4f 1b a9` | stp x20,x19,[sp, #0x1b0] | `FALL_THROUGH`
<a id="insn-006dade0"></a> `006dade0` | `fd 03 06 91` | add x29,sp,#0x180 | `FALL_THROUGH`
<a id="insn-006dade4"></a> `006dade4` | `55 d0 3b d5` | mrs x21,tpidr_el0 | `FALL_THROUGH`
<a id="insn-006dade8"></a> `006dade8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-006dadec"></a> `006dadec` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-006dadf0"></a> `006dadf0` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-006dadf4"></a> `006dadf4` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-006dadf8"></a> `006dadf8` | `1a b4 f6 97` | bl 0x00487e60 | `UNCONDITIONAL_CALL`
<a id="insn-006dadfc"></a> `006dadfc` | `48 2c 00 d0` | adrp x8,0xc64000 | `FALL_THROUGH`
<a id="insn-006dae00"></a> `006dae00` | `08 21 38 91` | add x8,x8,#0xe08 | `FALL_THROUGH`
<a id="insn-006dae04"></a> `006dae04` | `69 ce 8e 52` | mov w9,#0x7673 | `FALL_THROUGH`
<a id="insn-006dae08"></a> `006dae08` | `e8 13 00 f9` | str x8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-006dae0c"></a> `006dae0c` | `88 04 80 52` | mov w8,#0x24 | `FALL_THROUGH`
<a id="insn-006dae10"></a> `006dae10` | `e8 03 00 39` | strb w8,[sp] | `FALL_THROUGH`
<a id="insn-006dae14"></a> `006dae14` | `e8 de ff b0` | adrp x8,0x2b7000 | `FALL_THROUGH`
<a id="insn-006dae18"></a> `006dae18` | `08 ed 1a 91` | add x8,x8,#0x6bb | `FALL_THROUGH`
<a id="insn-006dae1c"></a> `006dae1c` | `00 01 c0 3d` | ldr q0,[x8] | `FALL_THROUGH`
<a id="insn-006dae20"></a> `006dae20` | `e9 13 01 78` | sturh w9,[sp, #0x11] | `FALL_THROUGH`
<a id="insn-006dae24"></a> `006dae24` | `ff 4f 00 39` | strb wzr,[sp, #0x13] | `FALL_THROUGH`
<a id="insn-006dae28"></a> `006dae28` | `e0 13 80 3c` | stur q0,[sp, #0x1] | `FALL_THROUGH`
<a id="insn-006dae2c"></a> `006dae2c` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-006dae30"></a> `006dae30` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-006dae34"></a> `006dae34` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-006dae38"></a> `006dae38` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-006dae3c"></a> `006dae3c` | `d3 d8 10 94` | bl 0x00b11188 | `UNCONDITIONAL_CALL`
<a id="insn-006dae40"></a> `006dae40` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-006dae44"></a> `006dae44` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-006dae48"></a> `006dae48` | `68 00 00 36` | tbz w8,#0x0,0x006dae54 | `CONDITIONAL_JUMP`
<a id="insn-006dae4c"></a> `006dae4c` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-006dae50"></a> `006dae50` | `4c f4 15 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-006dae54"></a> `006dae54` | `74 02 00 36` | tbz w20,#0x0,0x006daea0 | `CONDITIONAL_JUMP`
<a id="insn-006dae58"></a> `006dae58` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-006dae5c"></a> `006dae5c` | `e1 83 00 91` | add x1,sp,#0x20 | `FALL_THROUGH`
<a id="insn-006dae60"></a> `006dae60` | `69 ff ff 97` | bl 0x006dac04 | `UNCONDITIONAL_CALL`
<a id="insn-006dae64"></a> `006dae64` | `f4 03 13 aa` | mov x20,x19 | `FALL_THROUGH`
<a id="insn-006dae68"></a> `006dae68` | `e8 03 40 f9` | ldr x8,[sp] | `FALL_THROUGH`
<a id="insn-006dae6c"></a> `006dae6c` | `80 0e 42 f8` | ldr x0,[x20, #0x20]! | `FALL_THROUGH`
<a id="insn-006dae70"></a> `006dae70` | `88 82 1f f8` | stur x8,[x20, #-0x8] | `FALL_THROUGH`
<a id="insn-006dae74"></a> `006dae74` | `a0 00 00 b4` | cbz x0,0x006dae88 | `CONDITIONAL_JUMP`
<a id="insn-006dae78"></a> `006dae78` | `60 16 00 f9` | str x0,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-006dae7c"></a> `006dae7c` | `41 f4 15 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-006dae80"></a> `006dae80` | `9f 7e 00 a9` | stp xzr,xzr,[x20] | `FALL_THROUGH`
<a id="insn-006dae84"></a> `006dae84` | `9f 0a 00 f9` | str xzr,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-006dae88"></a> `006dae88` | `e0 83 c0 3c` | ldur q0,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-006dae8c"></a> `006dae8c` | `e8 0f 40 f9` | ldr x8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-006dae90"></a> `006dae90` | `60 0a 80 3d` | str q0,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-006dae94"></a> `006dae94` | `68 1a 00 f9` | str x8,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-006dae98"></a> `006dae98` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-006dae9c"></a> `006dae9c` | `ff b5 f6 97` | bl 0x00488698 | `UNCONDITIONAL_CALL`
<a id="insn-006daea0"></a> `006daea0` | `08 2e 00 90` | adrp x8,0xc9a000 | `FALL_THROUGH`
<a id="insn-006daea4"></a> `006daea4` | `16 2e 00 90` | adrp x22,0xc9a000 | `FALL_THROUGH`
<a id="insn-006daea8"></a> `006daea8` | `f4 83 00 91` | add x20,sp,#0x20 | `FALL_THROUGH`
<a id="insn-006daeac"></a> `006daeac` | `08 41 46 f9` | ldr x8,[x8, #0xc80] | `FALL_THROUGH`
<a id="insn-006daeb0"></a> `006daeb0` | `d6 46 46 f9` | ldr x22,[x22, #0xc88] | `FALL_THROUGH`
<a id="insn-006daeb4"></a> `006daeb4` | `93 22 01 91` | add x19,x20,#0x48 | `FALL_THROUGH`
<a id="insn-006daeb8"></a> `006daeb8` | `c9 02 40 f9` | ldr x9,[x22] | `FALL_THROUGH`
<a id="insn-006daebc"></a> `006daebc` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-006daec0"></a> `006daec0` | `e8 13 00 f9` | str x8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-006daec4"></a> `006daec4` | `e9 37 00 f9` | str x9,[sp, #0x68] | `FALL_THROUGH`
<a id="insn-006daec8"></a> `006daec8` | `28 81 5e f8` | ldur x8,[x9, #-0x18] | `FALL_THROUGH`
<a id="insn-006daecc"></a> `006daecc` | `c9 0e 40 f9` | ldr x9,[x22, #0x18] | `FALL_THROUGH`
<a id="insn-006daed0"></a> `006daed0` | `69 6a 28 f8` | str x9,[x19, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-006daed4"></a> `006daed4` | `08 2e 00 90` | adrp x8,0xc9a000 | `FALL_THROUGH`
<a id="insn-006daed8"></a> `006daed8` | `08 49 46 f9` | ldr x8,[x8, #0xc90] | `FALL_THROUGH`
<a id="insn-006daedc"></a> `006daedc` | `e9 c3 42 39` | ldrb w9,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-006daee0"></a> `006daee0` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-006daee4"></a> `006daee4` | `e8 3b 00 f9` | str x8,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-006daee8"></a> `006daee8` | `69 00 00 36` | tbz w9,#0x0,0x006daef4 | `CONDITIONAL_JUMP`
<a id="insn-006daeec"></a> `006daeec` | `e0 63 40 f9` | ldr x0,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-006daef0"></a> `006daef0` | `24 f4 15 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-006daef4"></a> `006daef4` | `80 42 01 91` | add x0,x20,#0x50 | `FALL_THROUGH`
<a id="insn-006daef8"></a> `006daef8` | `5e f4 15 94` | bl 0x00c58070 | `UNCONDITIONAL_CALL`
<a id="insn-006daefc"></a> `006daefc` | `c1 22 00 91` | add x1,x22,#0x8 | `FALL_THROUGH`
<a id="insn-006daf00"></a> `006daf00` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-006daf04"></a> `006daf04` | `5f f4 15 94` | bl 0x00c58080 | `UNCONDITIONAL_CALL`
<a id="insn-006daf08"></a> `006daf08` | `80 e2 02 91` | add x0,x20,#0xb8 | `FALL_THROUGH`
<a id="insn-006daf0c"></a> `006daf0c` | `61 f4 15 94` | bl 0x00c58090 | `UNCONDITIONAL_CALL`
<a id="insn-006daf10"></a> `006daf10` | `e8 03 41 39` | ldrb w8,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-006daf14"></a> `006daf14` | `68 00 00 36` | tbz w8,#0x0,0x006daf20 | `CONDITIONAL_JUMP`
<a id="insn-006daf18"></a> `006daf18` | `e0 2b 40 f9` | ldr x0,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-006daf1c"></a> `006daf1c` | `19 f4 15 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-006daf20"></a> `006daf20` | `e0 17 40 f9` | ldr x0,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-006daf24"></a> `006daf24` | `60 00 00 b4` | cbz x0,0x006daf30 | `CONDITIONAL_JUMP`
<a id="insn-006daf28"></a> `006daf28` | `e0 1b 00 f9` | str x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-006daf2c"></a> `006daf2c` | `15 f4 15 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-006daf30"></a> `006daf30` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-006daf34"></a> `006daf34` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-006daf38"></a> `006daf38` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-006daf3c"></a> `006daf3c` | `e1 02 00 54` | b.ne 0x006daf98 | `CONDITIONAL_JUMP`
<a id="insn-006daf40"></a> `006daf40` | `f4 4f 5b a9` | ldp x20,x19,[sp, #0x1b0] | `FALL_THROUGH`
<a id="insn-006daf44"></a> `006daf44` | `fc cb 40 f9` | ldr x28,[sp, #0x190] | `FALL_THROUGH`
<a id="insn-006daf48"></a> `006daf48` | `f6 57 5a a9` | ldp x22,x21,[sp, #0x1a0] | `FALL_THROUGH`
<a id="insn-006daf4c"></a> `006daf4c` | `fd 7b 58 a9` | ldp x29,x30,[sp, #0x180] | `FALL_THROUGH`
<a id="insn-006daf50"></a> `006daf50` | `ff 03 07 91` | add sp,sp,#0x1c0 | `FALL_THROUGH`
<a id="insn-006daf54"></a> `006daf54` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-006daf98"></a> `006daf98` | `06 f4 15 94` | bl 0x00c57fb0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`006dadcc`](#insn-006dadcc) 範囲 `[['006dadcc', '006dae0b']]`
  - `FALL_THROUGH` [`006dae08`](#insn-006dae08) → [`006dae0c`](#insn-006dae0c)
- ブロック [`006dae0c`](#insn-006dae0c) 範囲 `[['006dae0c', '006dae23']]`
  - `FALL_THROUGH` [`006dae20`](#insn-006dae20) → [`006dae24`](#insn-006dae24)
- ブロック [`006dae24`](#insn-006dae24) 範囲 `[['006dae24', '006dae4b']]`
  - `CONDITIONAL_JUMP` [`006dae48`](#insn-006dae48) → [`006dae54`](#insn-006dae54)
  - `FALL_THROUGH` [`006dae48`](#insn-006dae48) → [`006dae4c`](#insn-006dae4c)
- ブロック [`006dae4c`](#insn-006dae4c) 範囲 `[['006dae4c', '006dae53']]`
  - `FALL_THROUGH` [`006dae50`](#insn-006dae50) → [`006dae54`](#insn-006dae54)
- ブロック [`006dae54`](#insn-006dae54) 範囲 `[['006dae54', '006dae57']]`
  - `CONDITIONAL_JUMP` [`006dae54`](#insn-006dae54) → [`006daea0`](#insn-006daea0)
  - `FALL_THROUGH` [`006dae54`](#insn-006dae54) → [`006dae58`](#insn-006dae58)
- ブロック [`006dae58`](#insn-006dae58) 範囲 `[['006dae58', '006dae5b']]`
  - `FALL_THROUGH` [`006dae58`](#insn-006dae58) → [`006dae5c`](#insn-006dae5c)
- ブロック [`006dae5c`](#insn-006dae5c) 範囲 `[['006dae5c', '006dae77']]`
  - `CONDITIONAL_JUMP` [`006dae74`](#insn-006dae74) → [`006dae88`](#insn-006dae88)
  - `FALL_THROUGH` [`006dae74`](#insn-006dae74) → [`006dae78`](#insn-006dae78)
- ブロック [`006dae78`](#insn-006dae78) 範囲 `[['006dae78', '006dae87']]`
  - `FALL_THROUGH` [`006dae84`](#insn-006dae84) → [`006dae88`](#insn-006dae88)
- ブロック [`006dae88`](#insn-006dae88) 範囲 `[['006dae88', '006dae9f']]`
  - `FALL_THROUGH` [`006dae9c`](#insn-006dae9c) → [`006daea0`](#insn-006daea0)
- ブロック [`006daea0`](#insn-006daea0) 範囲 `[['006daea0', '006daecb']]`
  - `FALL_THROUGH` [`006daec8`](#insn-006daec8) → [`006daecc`](#insn-006daecc)
- ブロック [`006daecc`](#insn-006daecc) 範囲 `[['006daecc', '006daee3']]`
  - `FALL_THROUGH` [`006daee0`](#insn-006daee0) → [`006daee4`](#insn-006daee4)
- ブロック [`006daee4`](#insn-006daee4) 範囲 `[['006daee4', '006daeeb']]`
  - `CONDITIONAL_JUMP` [`006daee8`](#insn-006daee8) → [`006daef4`](#insn-006daef4)
  - `FALL_THROUGH` [`006daee8`](#insn-006daee8) → [`006daeec`](#insn-006daeec)
- ブロック [`006daeec`](#insn-006daeec) 範囲 `[['006daeec', '006daef3']]`
  - `FALL_THROUGH` [`006daef0`](#insn-006daef0) → [`006daef4`](#insn-006daef4)
- ブロック [`006daef4`](#insn-006daef4) 範囲 `[['006daef4', '006daef7']]`
  - `FALL_THROUGH` [`006daef4`](#insn-006daef4) → [`006daef8`](#insn-006daef8)
- ブロック [`006daef8`](#insn-006daef8) 範囲 `[['006daef8', '006daeff']]`
  - `FALL_THROUGH` [`006daefc`](#insn-006daefc) → [`006daf00`](#insn-006daf00)
- ブロック [`006daf00`](#insn-006daf00) 範囲 `[['006daf00', '006daf03']]`
  - `FALL_THROUGH` [`006daf00`](#insn-006daf00) → [`006daf04`](#insn-006daf04)
- ブロック [`006daf04`](#insn-006daf04) 範囲 `[['006daf04', '006daf07']]`
  - `FALL_THROUGH` [`006daf04`](#insn-006daf04) → [`006daf08`](#insn-006daf08)
- ブロック [`006daf08`](#insn-006daf08) 範囲 `[['006daf08', '006daf0f']]`
  - `FALL_THROUGH` [`006daf0c`](#insn-006daf0c) → [`006daf10`](#insn-006daf10)
- ブロック [`006daf10`](#insn-006daf10) 範囲 `[['006daf10', '006daf17']]`
  - `CONDITIONAL_JUMP` [`006daf14`](#insn-006daf14) → [`006daf20`](#insn-006daf20)
  - `FALL_THROUGH` [`006daf14`](#insn-006daf14) → [`006daf18`](#insn-006daf18)
- ブロック [`006daf18`](#insn-006daf18) 範囲 `[['006daf18', '006daf1b']]`
  - `FALL_THROUGH` [`006daf18`](#insn-006daf18) → [`006daf1c`](#insn-006daf1c)
- ブロック [`006daf1c`](#insn-006daf1c) 範囲 `[['006daf1c', '006daf1f']]`
  - `FALL_THROUGH` [`006daf1c`](#insn-006daf1c) → [`006daf20`](#insn-006daf20)
- ブロック [`006daf20`](#insn-006daf20) 範囲 `[['006daf20', '006daf23']]`
  - `FALL_THROUGH` [`006daf20`](#insn-006daf20) → [`006daf24`](#insn-006daf24)
- ブロック [`006daf24`](#insn-006daf24) 範囲 `[['006daf24', '006daf27']]`
  - `CONDITIONAL_JUMP` [`006daf24`](#insn-006daf24) → [`006daf30`](#insn-006daf30)
  - `FALL_THROUGH` [`006daf24`](#insn-006daf24) → [`006daf28`](#insn-006daf28)
- ブロック [`006daf28`](#insn-006daf28) 範囲 `[['006daf28', '006daf2b']]`
  - `FALL_THROUGH` [`006daf28`](#insn-006daf28) → [`006daf2c`](#insn-006daf2c)
- ブロック [`006daf2c`](#insn-006daf2c) 範囲 `[['006daf2c', '006daf2f']]`
  - `FALL_THROUGH` [`006daf2c`](#insn-006daf2c) → [`006daf30`](#insn-006daf30)
- ブロック [`006daf30`](#insn-006daf30) 範囲 `[['006daf30', '006daf37']]`
  - `FALL_THROUGH` [`006daf34`](#insn-006daf34) → [`006daf38`](#insn-006daf38)
- ブロック [`006daf38`](#insn-006daf38) 範囲 `[['006daf38', '006daf3f']]`
  - `CONDITIONAL_JUMP` [`006daf3c`](#insn-006daf3c) → [`006daf98`](#insn-006daf98)
  - `FALL_THROUGH` [`006daf3c`](#insn-006daf3c) → [`006daf40`](#insn-006daf40)
- ブロック [`006daf40`](#insn-006daf40) 範囲 `[['006daf40', '006daf43']]`
  - `FALL_THROUGH` [`006daf40`](#insn-006daf40) → [`006daf44`](#insn-006daf44)
- ブロック [`006daf44`](#insn-006daf44) 範囲 `[['006daf44', '006daf47']]`
  - `FALL_THROUGH` [`006daf44`](#insn-006daf44) → [`006daf48`](#insn-006daf48)
- ブロック [`006daf48`](#insn-006daf48) 範囲 `[['006daf48', '006daf4b']]`
  - `FALL_THROUGH` [`006daf48`](#insn-006daf48) → [`006daf4c`](#insn-006daf4c)
- ブロック [`006daf4c`](#insn-006daf4c) 範囲 `[['006daf4c', '006daf57']]`
- ブロック [`006daf98`](#insn-006daf98) 範囲 `[['006daf98', '006daf9b']]`

## 命令位置別の参照

- [`006dadd0`](#insn-006dadd0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006dadd4`](#insn-006dadd4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006dadd8`](#insn-006dadd8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006daddc`](#insn-006daddc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006dadf4`](#insn-006dadf4) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006dadf8`](#insn-006dadf8) → [`00487e60`](../00487/00487e60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00487e60` · 推定シンボル `None` · 推定型 `None`
- [`006dae08`](#insn-006dae08) → `00c64e08`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`006dae08`](#insn-006dae08) → `Stack[-0x1a0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006dae10`](#insn-006dae10) → `Stack[-0x1c0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006dae1c`](#insn-006dae1c) → `002b76bb`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`006dae20`](#insn-006dae20) → `Stack[-0x1af]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006dae24`](#insn-006dae24) → `Stack[-0x1ad]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006dae28`](#insn-006dae28) → `Stack[-0x1bf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006dae3c`](#insn-006dae3c) → [`00b11188`](../00b11/00b11188.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00b11188` · 推定シンボル `None` · 推定型 `None`
- [`006dae40`](#insn-006dae40) → `Stack[-0x1c0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006dae48`](#insn-006dae48) → [`006dae54`](#insn-006dae54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006dae4c`](#insn-006dae4c) → `Stack[-0x1b0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006dae50`](#insn-006dae50) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`006dae54`](#insn-006dae54) → [`006daea0`](#insn-006daea0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006dae60`](#insn-006dae60) → [`006dac04`](006dac04.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `006dac04` · 推定シンボル `None` · 推定型 `None`
- [`006dae68`](#insn-006dae68) → `Stack[-0x1c0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006dae74`](#insn-006dae74) → [`006dae88`](#insn-006dae88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006dae7c`](#insn-006dae7c) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`006dae88`](#insn-006dae88) → `Stack[-0x1b8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006dae8c`](#insn-006dae8c) → `Stack[-0x1a8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006dae9c`](#insn-006dae9c) → [`00488698`](../00488/00488698.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00488698` · 推定シンボル `None` · 推定型 `None`
- [`006daeac`](#insn-006daeac) → `00c9ac80`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`006daeb0`](#insn-006daeb0) → `00c9ac88`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`006daeb8`](#insn-006daeb8) → `00c932d0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE` · 推定型 `pointer __((offset(0x18)))`
- [`006daec0`](#insn-006daec0) → `00c658e8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`006daec0`](#insn-006daec0) → `Stack[-0x1a0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006daec4`](#insn-006daec4) → `00c910e0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`006daec4`](#insn-006daec4) → `Stack[-0x158]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006daec8`](#insn-006daec8) → `00c910c8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTVNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE` · 推定型 `undefined8`
- [`006daecc`](#insn-006daecc) → `00c932e8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x40)))`
- [`006daed0`](#insn-006daed0) → `00c91108`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`006daed8`](#insn-006daed8) → `00c9ac90`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`006daedc`](#insn-006daedc) → `Stack[-0x110]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006daee4`](#insn-006daee4) → `00c90cd8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[128]`
- [`006daee4`](#insn-006daee4) → `Stack[-0x150]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006daee8`](#insn-006daee8) → [`006daef4`](#insn-006daef4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006daeec`](#insn-006daeec) → `Stack[-0x100]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006daef0`](#insn-006daef0) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`006daef8`](#insn-006daef8) → [`00c58070`](../00c58/00c58070.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58070` · 推定シンボル `None` · 推定型 `None`
- [`006daefc`](#insn-006daefc) → `00c932d8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x18)))`
- [`006daf04`](#insn-006daf04) → [`00c58080`](../00c58/00c58080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58080` · 推定シンボル `None` · 推定型 `None`
- [`006daf0c`](#insn-006daf0c) → [`00c58090`](../00c58/00c58090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58090` · 推定シンボル `None` · 推定型 `None`
- [`006daf10`](#insn-006daf10) → `Stack[-0x180]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006daf14`](#insn-006daf14) → [`006daf20`](#insn-006daf20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006daf18`](#insn-006daf18) → `Stack[-0x170]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006daf1c`](#insn-006daf1c) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`006daf20`](#insn-006daf20) → `Stack[-0x198]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006daf24`](#insn-006daf24) → [`006daf30`](#insn-006daf30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006daf28`](#insn-006daf28) → `Stack[-0x190]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006daf2c`](#insn-006daf2c) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`006daf34`](#insn-006daf34) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006daf3c`](#insn-006daf3c) → [`006daf98`](#insn-006daf98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006daf40`](#insn-006daf40) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006daf44`](#insn-006daf44) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006daf48`](#insn-006daf48) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006daf4c`](#insn-006daf4c) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006daf98`](#insn-006daf98) → [`00c57fb0`](../00c57/00c57fb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fb0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`006dadd0`](#insn-006dadd0)

~~~json
{
  "source": "006dadd0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006dadd4`](#insn-006dadd4)

~~~json
{
  "source": "006dadd4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006dadd8`](#insn-006dadd8)

~~~json
{
  "source": "006dadd8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006daddc`](#insn-006daddc)

~~~json
{
  "source": "006daddc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006dadf4`](#insn-006dadf4)

~~~json
{
  "source": "006dadf4",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006dadf8`](#insn-006dadf8)

~~~json
{
  "source": "006dadf8",
  "target": "00487e60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006dae08`](#insn-006dae08)

~~~json
{
  "source": "006dae08",
  "target": "00c64e08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c64e08",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`006dae08`](#insn-006dae08)

~~~json
{
  "source": "006dae08",
  "target": "Stack[-0x1a0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006dae10`](#insn-006dae10)

~~~json
{
  "source": "006dae10",
  "target": "Stack[-0x1c0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006dae1c`](#insn-006dae1c)

~~~json
{
  "source": "006dae1c",
  "target": "002b76bb",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b76bb",
  "offset": 0,
  "size": 19,
  "datatype": "string",
  "bytes": "47616d61746f746f5f426f6e75732e63737600",
  "capture_start": "002b76bb",
  "capture_bytes": 19,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`006dae20`](#insn-006dae20)

~~~json
{
  "source": "006dae20",
  "target": "Stack[-0x1af]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006dae24`](#insn-006dae24)

~~~json
{
  "source": "006dae24",
  "target": "Stack[-0x1ad]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006dae28`](#insn-006dae28)

~~~json
{
  "source": "006dae28",
  "target": "Stack[-0x1bf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006dae3c`](#insn-006dae3c)

~~~json
{
  "source": "006dae3c",
  "target": "00b11188",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006dae40`](#insn-006dae40)

~~~json
{
  "source": "006dae40",
  "target": "Stack[-0x1c0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006dae48`](#insn-006dae48)

~~~json
{
  "source": "006dae48",
  "target": "006dae54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006dae4c`](#insn-006dae4c)

~~~json
{
  "source": "006dae4c",
  "target": "Stack[-0x1b0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006dae50`](#insn-006dae50)

~~~json
{
  "source": "006dae50",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006dae54`](#insn-006dae54)

~~~json
{
  "source": "006dae54",
  "target": "006daea0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006dae60`](#insn-006dae60)

~~~json
{
  "source": "006dae60",
  "target": "006dac04",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006dae68`](#insn-006dae68)

~~~json
{
  "source": "006dae68",
  "target": "Stack[-0x1c0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006dae74`](#insn-006dae74)

~~~json
{
  "source": "006dae74",
  "target": "006dae88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006dae7c`](#insn-006dae7c)

~~~json
{
  "source": "006dae7c",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006dae88`](#insn-006dae88)

~~~json
{
  "source": "006dae88",
  "target": "Stack[-0x1b8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006dae8c`](#insn-006dae8c)

~~~json
{
  "source": "006dae8c",
  "target": "Stack[-0x1a8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006dae9c`](#insn-006dae9c)

~~~json
{
  "source": "006dae9c",
  "target": "00488698",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006daeac`](#insn-006daeac)

~~~json
{
  "source": "006daeac",
  "target": "00c9ac80",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9ac80",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`006daeb0`](#insn-006daeb0)

~~~json
{
  "source": "006daeb0",
  "target": "00c9ac88",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9ac88",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`006daeb8`](#insn-006daeb8)

~~~json
{
  "source": "006daeb8",
  "target": "00c932d0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c932d0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x18)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`006daec0`](#insn-006daec0)

~~~json
{
  "source": "006daec0",
  "target": "00c658e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c658e8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`006daec0`](#insn-006daec0)

~~~json
{
  "source": "006daec0",
  "target": "Stack[-0x1a0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006daec4`](#insn-006daec4)

~~~json
{
  "source": "006daec4",
  "target": "00c910e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c910e0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`006daec4`](#insn-006daec4)

~~~json
{
  "source": "006daec4",
  "target": "Stack[-0x158]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006daec8`](#insn-006daec8)

~~~json
{
  "source": "006daec8",
  "target": "00c910c8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c910c8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "bytes": "7000000000000000",
  "capture_start": "00c910c8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`006daecc`](#insn-006daecc)

~~~json
{
  "source": "006daecc",
  "target": "00c932e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c932e8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x40)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`006daed0`](#insn-006daed0)

~~~json
{
  "source": "006daed0",
  "target": "00c91108",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c91108",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`006daed8`](#insn-006daed8)

~~~json
{
  "source": "006daed8",
  "target": "00c9ac90",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9ac90",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`006daedc`](#insn-006daedc)

~~~json
{
  "source": "006daedc",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006daee4`](#insn-006daee4)

~~~json
{
  "source": "006daee4",
  "target": "00c90cd8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c90cc8",
  "offset": 16,
  "size": 128,
  "datatype": "undefined1[128]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`006daee4`](#insn-006daee4)

~~~json
{
  "source": "006daee4",
  "target": "Stack[-0x150]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006daee8`](#insn-006daee8)

~~~json
{
  "source": "006daee8",
  "target": "006daef4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006daeec`](#insn-006daeec)

~~~json
{
  "source": "006daeec",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006daef0`](#insn-006daef0)

~~~json
{
  "source": "006daef0",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006daef8`](#insn-006daef8)

~~~json
{
  "source": "006daef8",
  "target": "00c58070",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006daefc`](#insn-006daefc)

~~~json
{
  "source": "006daefc",
  "target": "00c932d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c932d8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x18)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`006daf04`](#insn-006daf04)

~~~json
{
  "source": "006daf04",
  "target": "00c58080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006daf0c`](#insn-006daf0c)

~~~json
{
  "source": "006daf0c",
  "target": "00c58090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006daf10`](#insn-006daf10)

~~~json
{
  "source": "006daf10",
  "target": "Stack[-0x180]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006daf14`](#insn-006daf14)

~~~json
{
  "source": "006daf14",
  "target": "006daf20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006daf18`](#insn-006daf18)

~~~json
{
  "source": "006daf18",
  "target": "Stack[-0x170]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006daf1c`](#insn-006daf1c)

~~~json
{
  "source": "006daf1c",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006daf20`](#insn-006daf20)

~~~json
{
  "source": "006daf20",
  "target": "Stack[-0x198]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006daf24`](#insn-006daf24)

~~~json
{
  "source": "006daf24",
  "target": "006daf30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006daf28`](#insn-006daf28)

~~~json
{
  "source": "006daf28",
  "target": "Stack[-0x190]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006daf2c`](#insn-006daf2c)

~~~json
{
  "source": "006daf2c",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006daf34`](#insn-006daf34)

~~~json
{
  "source": "006daf34",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006daf3c`](#insn-006daf3c)

~~~json
{
  "source": "006daf3c",
  "target": "006daf98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006daf40`](#insn-006daf40)

~~~json
{
  "source": "006daf40",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006daf44`](#insn-006daf44)

~~~json
{
  "source": "006daf44",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006daf48`](#insn-006daf48)

~~~json
{
  "source": "006daf48",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006daf4c`](#insn-006daf4c)

~~~json
{
  "source": "006daf4c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006daf98`](#insn-006daf98)

~~~json
{
  "source": "006daf98",
  "target": "00c57fb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
