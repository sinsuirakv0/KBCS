# 008acdac

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `008acd54`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ac/008acd54.md) · 移動量 `+0x58`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0050.md#compare-facac817ce3ef636546c6bfce232b78e)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `008add58`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ad/008add58.md) · 移動量 `+0xfac`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0051.md#compare-63c872a62e1bfde2d659b91d3f0ae53c)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "008acdac",
  "name": "FUN_008acdac",
  "size": 400,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7e954d3ba74afb568254f507934a55f63d0d9662ae2fcce1eca5ec12082efdb1",
  "source_text_sha256": "7e954d3ba74afb568254f507934a55f63d0d9662ae2fcce1eca5ec12082efdb1",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "008acdac",
        "008acf37"
      ],
      [
        "008acf88",
        "008acf8b"
      ]
    ],
    "bytes_sha256": "fa788556ef583098a98d9a52511f43ac65c2e80e10d6c903a8dd4d6bcaa9f15a",
    "instruction_count": 100,
    "instruction_bytes": 400,
    "body_bytes": 400,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0048ce94](../0048c/0048ce94.md)
- [00851550](../00851/00851550.md)
- [00851a64](../00851/00851a64.md)
- [008629d8](../00862/008629d8.md)
- [008ad02c](../008ad/008ad02c.md)
- [008ad030](../008ad/008ad030.md)
- [008bad20](../008ba/008bad20.md)
- [008bb568](../008bb/008bb568.md)
- [008bbab8](../008bb/008bbab8.md)
- [009ccb84](../009cc/009ccb84.md)
- [00a1a6f8](../00a1a/00a1a6f8.md)
- [00c57f80](../00c57/00c57f80.md)
- [00c57fb0](../00c57/00c57fb0.md)

## 関連文字列（未確認候補）

~~~text
"AccountDelete_error02"
"AccountDelete_error03"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2881 bytes

~~~c

void FUN_008acdac(undefined8 param_1,int *param_2)

{
  char *pcVar1;
  int iVar2;
  long lVar3;
  long lVar4;
  undefined8 uVar5;
  undefined ***pppuVar6;
  byte local_a0;
  undefined8 local_9f;
  undefined5 uStack_97;
  undefined2 uStack_92;
  undefined1 uStack_90;
  undefined5 uStack_8f;
  undefined1 uStack_8a;
  undefined1 uStack_89;
  byte local_88 [16];
  void *local_78;
  undefined **local_70 [4];
  undefined ***local_50;
  long local_38;
  
                    /* try { // try from 008acdb8 to 009acdc7 has its CatchHandler @ 008ad074 */
  lVar3 = tpidr_el0;
  local_38 = *(long *)(lVar3 + 0x28);
  iVar2 = *param_2;
  lVar4 = FUN_00851550();
  lVar4 = FUN_008bb568(lVar4 + 0x2f08);
  if (lVar4 != 0) {
    lVar4 = FUN_00851550();
    FUN_008bbab8(lVar4 + 0x2f08);
  }
  lVar4 = FUN_00851550();
  if (iVar2 == 1) {
    FUN_009ccb84();
    FUN_00851550();
    FUN_008629d8();
    lVar4 = FUN_00851550();
    *(undefined1 *)(lVar4 + 0x11c1) = 1;
    FUN_00851550();
    FUN_00a1a6f8();
                    /* try { // try from 008ace24 to 009ace2f has its CatchHandler @ 008ad064 */
    uVar5 = FUN_00851550();
    if (*(long *)(lVar3 + 0x28) == local_38) {
                    /* try { // try from 008ace48 to 009ace4f has its CatchHandler @ 008ad050 */
      FUN_00851a64(uVar5,0x68);
      return;
    }
    goto LAB_008acf88;
  }
  pcVar1 = "AccountDelete_error03";
  if (iVar2 != 0x71) {
    pcVar1 = "AccountDelete_error02";
  }
  uStack_8a = 0;
  local_9f = *(undefined8 *)pcVar1;
                    /* try { // try from 008ace78 to 009ace83 has its CatchHandler @ 008ad040 */
  uVar5 = *(undefined8 *)(pcVar1 + 0xd);
  local_a0 = 0x2a;
  uStack_97 = (undefined5)*(undefined8 *)(pcVar1 + 8);
  uStack_92 = (undefined2)uVar5;
  uStack_90 = (undefined1)((ulong)uVar5 >> 0x10);
  uStack_8f = (undefined5)((ulong)uVar5 >> 0x18);
  FUN_0048ce94(local_88,&local_a0);
  local_70[0] = &PTR_FUN_00c83970;
                    /* try { // try from 008acea8 to 009aceb3 has its CatchHandler @ 008ad028 */
                    /* try { // try from 008aceb4 to 009acec3 has its CatchHandler @ 008ad010 */
  local_50 = local_70;
                    /* try { // try from 008acec4 to 009ad15b has its CatchHandler @ 008acb24 */
  FUN_008bad20(lVar4 + 0x2f08,local_88,0,0,4,local_70);
  if (local_50 == local_70) {
    lVar4 = 0x20;
    pppuVar6 = local_70;
LAB_008acee8:
    (**(code **)((long)*pppuVar6 + lVar4))();
  }
  else if (local_50 != (undefined ***)0x0) {
    lVar4 = 0x28;
    pppuVar6 = local_50;
    goto LAB_008acee8;
  }
  if ((local_88[0] & 1) != 0) {
    _ZdlPv(local_78);
  }
  if ((local_a0 & 1) != 0) {
    _ZdlPv((void *)CONCAT17(uStack_89,CONCAT16(uStack_8a,CONCAT51(uStack_8f,uStack_90))));
  }
  if (*(long *)(lVar3 + 0x28) == local_38) {
    return;
  }
LAB_008acf88:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-008acdac"></a> `008acdac` | `ff 83 02 d1` | sub sp,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-008acdb0"></a> `008acdb0` | `fd 7b 07 a9` | stp x29,x30,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-008acdb4"></a> `008acdb4` | `f5 43 00 f9` | str x21,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-008acdb8"></a> `008acdb8` | `f4 4f 09 a9` | stp x20,x19,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-008acdbc"></a> `008acdbc` | `fd c3 01 91` | add x29,sp,#0x70 | `FALL_THROUGH`
<a id="insn-008acdc0"></a> `008acdc0` | `54 d0 3b d5` | mrs x20,tpidr_el0 | `FALL_THROUGH`
<a id="insn-008acdc4"></a> `008acdc4` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-008acdc8"></a> `008acdc8` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-008acdcc"></a> `008acdcc` | `35 00 40 b9` | ldr w21,[x1] | `FALL_THROUGH`
<a id="insn-008acdd0"></a> `008acdd0` | `e0 91 fe 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-008acdd4"></a> `008acdd4` | `08 e1 85 52` | mov w8,#0x2f08 | `FALL_THROUGH`
<a id="insn-008acdd8"></a> `008acdd8` | `00 00 08 8b` | add x0,x0,x8 | `FALL_THROUGH`
<a id="insn-008acddc"></a> `008acddc` | `e3 39 00 94` | bl 0x008bb568 | `UNCONDITIONAL_CALL`
<a id="insn-008acde0"></a> `008acde0` | `a0 00 00 b4` | cbz x0,0x008acdf4 | `CONDITIONAL_JUMP`
<a id="insn-008acde4"></a> `008acde4` | `db 91 fe 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-008acde8"></a> `008acde8` | `08 e1 85 52` | mov w8,#0x2f08 | `FALL_THROUGH`
<a id="insn-008acdec"></a> `008acdec` | `00 00 08 8b` | add x0,x0,x8 | `FALL_THROUGH`
<a id="insn-008acdf0"></a> `008acdf0` | `32 3b 00 94` | bl 0x008bbab8 | `UNCONDITIONAL_CALL`
<a id="insn-008acdf4"></a> `008acdf4` | `d7 91 fe 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-008acdf8"></a> `008acdf8` | `bf 06 00 71` | cmp w21,#0x1 | `FALL_THROUGH`
<a id="insn-008acdfc"></a> `008acdfc` | `a1 02 00 54` | b.ne 0x008ace50 | `CONDITIONAL_JUMP`
<a id="insn-008ace00"></a> `008ace00` | `61 7f 04 94` | bl 0x009ccb84 | `UNCONDITIONAL_CALL`
<a id="insn-008ace04"></a> `008ace04` | `d3 91 fe 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-008ace08"></a> `008ace08` | `f4 d6 fe 97` | bl 0x008629d8 | `UNCONDITIONAL_CALL`
<a id="insn-008ace0c"></a> `008ace0c` | `d1 91 fe 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-008ace10"></a> `008ace10` | `28 38 82 52` | mov w8,#0x11c1 | `FALL_THROUGH`
<a id="insn-008ace14"></a> `008ace14` | `29 00 80 52` | mov w9,#0x1 | `FALL_THROUGH`
<a id="insn-008ace18"></a> `008ace18` | `09 68 28 38` | strb w9,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-008ace1c"></a> `008ace1c` | `cd 91 fe 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-008ace20"></a> `008ace20` | `36 b6 05 94` | bl 0x00a1a6f8 | `UNCONDITIONAL_CALL`
<a id="insn-008ace24"></a> `008ace24` | `cb 91 fe 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-008ace28"></a> `008ace28` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-008ace2c"></a> `008ace2c` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-008ace30"></a> `008ace30` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-008ace34"></a> `008ace34` | `a1 0a 00 54` | b.ne 0x008acf88 | `CONDITIONAL_JUMP`
<a id="insn-008ace38"></a> `008ace38` | `01 0d 80 52` | mov w1,#0x68 | `FALL_THROUGH`
<a id="insn-008ace3c"></a> `008ace3c` | `f4 4f 49 a9` | ldp x20,x19,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-008ace40"></a> `008ace40` | `f5 43 40 f9` | ldr x21,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-008ace44"></a> `008ace44` | `fd 7b 47 a9` | ldp x29,x30,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-008ace48"></a> `008ace48` | `ff 83 02 91` | add sp,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-008ace4c"></a> `008ace4c` | `06 93 fe 17` | b 0x00851a64 | `CALL_TERMINATOR`
<a id="insn-008ace50"></a> `008ace50` | `68 d0 ff b0` | adrp x8,0x2b9000 | `FALL_THROUGH`
<a id="insn-008ace54"></a> `008ace54` | `08 6d 16 91` | add x8,x8,#0x59b | `FALL_THROUGH`
<a id="insn-008ace58"></a> `008ace58` | `bf c6 01 71` | cmp w21,#0x71 | `FALL_THROUGH`
<a id="insn-008ace5c"></a> `008ace5c` | `69 d0 ff 90` | adrp x9,0x2b8000 | `FALL_THROUGH`
<a id="insn-008ace60"></a> `008ace60` | `29 35 1d 91` | add x9,x9,#0x74d | `FALL_THROUGH`
<a id="insn-008ace64"></a> `008ace64` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-008ace68"></a> `008ace68` | `28 01 88 9a` | csel x8,x9,x8,eq | `FALL_THROUGH`
<a id="insn-008ace6c"></a> `008ace6c` | `49 05 80 52` | mov w9,#0x2a | `FALL_THROUGH`
<a id="insn-008ace70"></a> `008ace70` | `ff 5b 00 39` | strb wzr,[sp, #0x16] | `FALL_THROUGH`
<a id="insn-008ace74"></a> `008ace74` | `00 01 c0 3d` | ldr q0,[x8] | `FALL_THROUGH`
<a id="insn-008ace78"></a> `008ace78` | `08 d1 40 f8` | ldur x8,[x8, #0xd] | `FALL_THROUGH`
<a id="insn-008ace7c"></a> `008ace7c` | `e9 03 00 39` | strb w9,[sp] | `FALL_THROUGH`
<a id="insn-008ace80"></a> `008ace80` | `e0 13 80 3c` | stur q0,[sp, #0x1] | `FALL_THROUGH`
<a id="insn-008ace84"></a> `008ace84` | `e8 e3 00 f8` | stur x8,[sp, #0xe] | `FALL_THROUGH`
<a id="insn-008ace88"></a> `008ace88` | `e8 63 00 91` | add x8,sp,#0x18 | `FALL_THROUGH`
<a id="insn-008ace8c"></a> `008ace8c` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-008ace90"></a> `008ace90` | `01 80 ef 97` | bl 0x0048ce94 | `UNCONDITIONAL_CALL`
<a id="insn-008ace94"></a> `008ace94` | `a8 1e 00 f0` | adrp x8,0xc83000 | `FALL_THROUGH`
<a id="insn-008ace98"></a> `008ace98` | `08 c1 25 91` | add x8,x8,#0x970 | `FALL_THROUGH`
<a id="insn-008ace9c"></a> `008ace9c` | `f5 c3 00 91` | add x21,sp,#0x30 | `FALL_THROUGH`
<a id="insn-008acea0"></a> `008acea0` | `e8 1b 00 f9` | str x8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-008acea4"></a> `008acea4` | `08 e1 85 52` | mov w8,#0x2f08 | `FALL_THROUGH`
<a id="insn-008acea8"></a> `008acea8` | `f5 2b 00 f9` | str x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-008aceac"></a> `008aceac` | `60 02 08 8b` | add x0,x19,x8 | `FALL_THROUGH`
<a id="insn-008aceb0"></a> `008aceb0` | `e1 63 00 91` | add x1,sp,#0x18 | `FALL_THROUGH`
<a id="insn-008aceb4"></a> `008aceb4` | `e5 c3 00 91` | add x5,sp,#0x30 | `FALL_THROUGH`
<a id="insn-008aceb8"></a> `008aceb8` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-008acebc"></a> `008acebc` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-008acec0"></a> `008acec0` | `84 00 80 52` | mov w4,#0x4 | `FALL_THROUGH`
<a id="insn-008acec4"></a> `008acec4` | `97 37 00 94` | bl 0x008bad20 | `UNCONDITIONAL_CALL`
<a id="insn-008acec8"></a> `008acec8` | `e0 2b 40 f9` | ldr x0,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-008acecc"></a> `008acecc` | `1f 00 15 eb` | cmp x0,x21 | `FALL_THROUGH`
<a id="insn-008aced0"></a> `008aced0` | `80 00 00 54` | b.eq 0x008acee0 | `CONDITIONAL_JUMP`
<a id="insn-008aced4"></a> `008aced4` | `00 01 00 b4` | cbz x0,0x008acef4 | `CONDITIONAL_JUMP`
<a id="insn-008aced8"></a> `008aced8` | `08 05 80 52` | mov w8,#0x28 | `FALL_THROUGH`
<a id="insn-008acedc"></a> `008acedc` | `03 00 00 14` | b 0x008acee8 | `UNCONDITIONAL_JUMP`
<a id="insn-008acee0"></a> `008acee0` | `08 04 80 52` | mov w8,#0x20 | `FALL_THROUGH`
<a id="insn-008acee4"></a> `008acee4` | `e0 c3 00 91` | add x0,sp,#0x30 | `FALL_THROUGH`
<a id="insn-008acee8"></a> `008acee8` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-008aceec"></a> `008aceec` | `28 69 68 f8` | ldr x8,[x9, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-008acef0"></a> `008acef0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-008acef4"></a> `008acef4` | `e8 63 40 39` | ldrb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-008acef8"></a> `008acef8` | `68 00 00 36` | tbz w8,#0x0,0x008acf04 | `CONDITIONAL_JUMP`
<a id="insn-008acefc"></a> `008acefc` | `e0 17 40 f9` | ldr x0,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-008acf00"></a> `008acf00` | `20 ac 0e 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-008acf04"></a> `008acf04` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-008acf08"></a> `008acf08` | `68 00 00 36` | tbz w8,#0x0,0x008acf14 | `CONDITIONAL_JUMP`
<a id="insn-008acf0c"></a> `008acf0c` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-008acf10"></a> `008acf10` | `1c ac 0e 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-008acf14"></a> `008acf14` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-008acf18"></a> `008acf18` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-008acf1c"></a> `008acf1c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-008acf20"></a> `008acf20` | `41 03 00 54` | b.ne 0x008acf88 | `CONDITIONAL_JUMP`
<a id="insn-008acf24"></a> `008acf24` | `f4 4f 49 a9` | ldp x20,x19,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-008acf28"></a> `008acf28` | `f5 43 40 f9` | ldr x21,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-008acf2c"></a> `008acf2c` | `fd 7b 47 a9` | ldp x29,x30,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-008acf30"></a> `008acf30` | `ff 83 02 91` | add sp,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-008acf34"></a> `008acf34` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-008acf88"></a> `008acf88` | `0a ac 0e 94` | bl 0x00c57fb0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`008acdac`](#insn-008acdac) 範囲 `[['008acdac', '008acdb7']]`
  - `FALL_THROUGH` [`008acdb4`](#insn-008acdb4) → [`008acdb8`](#insn-008acdb8)
- ブロック [`008acdb8`](#insn-008acdb8) 範囲 `[['008acdb8', '008acde3']]`
  - `CONDITIONAL_JUMP` [`008acde0`](#insn-008acde0) → [`008acdf4`](#insn-008acdf4)
  - `FALL_THROUGH` [`008acde0`](#insn-008acde0) → [`008acde4`](#insn-008acde4)
- ブロック [`008acde4`](#insn-008acde4) 範囲 `[['008acde4', '008acdf3']]`
  - `FALL_THROUGH` [`008acdf0`](#insn-008acdf0) → [`008acdf4`](#insn-008acdf4)
- ブロック [`008acdf4`](#insn-008acdf4) 範囲 `[['008acdf4', '008acdff']]`
  - `CONDITIONAL_JUMP` [`008acdfc`](#insn-008acdfc) → [`008ace50`](#insn-008ace50)
  - `FALL_THROUGH` [`008acdfc`](#insn-008acdfc) → [`008ace00`](#insn-008ace00)
- ブロック [`008ace00`](#insn-008ace00) 範囲 `[['008ace00', '008ace23']]`
  - `FALL_THROUGH` [`008ace20`](#insn-008ace20) → [`008ace24`](#insn-008ace24)
- ブロック [`008ace24`](#insn-008ace24) 範囲 `[['008ace24', '008ace37']]`
  - `CONDITIONAL_JUMP` [`008ace34`](#insn-008ace34) → [`008acf88`](#insn-008acf88)
  - `FALL_THROUGH` [`008ace34`](#insn-008ace34) → [`008ace38`](#insn-008ace38)
- ブロック [`008ace38`](#insn-008ace38) 範囲 `[['008ace38', '008ace47']]`
  - `FALL_THROUGH` [`008ace44`](#insn-008ace44) → [`008ace48`](#insn-008ace48)
- ブロック [`008ace48`](#insn-008ace48) 範囲 `[['008ace48', '008ace4f']]`
- ブロック [`008ace50`](#insn-008ace50) 範囲 `[['008ace50', '008ace77']]`
  - `FALL_THROUGH` [`008ace74`](#insn-008ace74) → [`008ace78`](#insn-008ace78)
- ブロック [`008ace78`](#insn-008ace78) 範囲 `[['008ace78', '008acea7']]`
  - `FALL_THROUGH` [`008acea4`](#insn-008acea4) → [`008acea8`](#insn-008acea8)
- ブロック [`008acea8`](#insn-008acea8) 範囲 `[['008acea8', '008aceb3']]`
  - `FALL_THROUGH` [`008aceb0`](#insn-008aceb0) → [`008aceb4`](#insn-008aceb4)
- ブロック [`008aceb4`](#insn-008aceb4) 範囲 `[['008aceb4', '008acec3']]`
  - `FALL_THROUGH` [`008acec0`](#insn-008acec0) → [`008acec4`](#insn-008acec4)
- ブロック [`008acec4`](#insn-008acec4) 範囲 `[['008acec4', '008aced3']]`
  - `CONDITIONAL_JUMP` [`008aced0`](#insn-008aced0) → [`008acee0`](#insn-008acee0)
  - `FALL_THROUGH` [`008aced0`](#insn-008aced0) → [`008aced4`](#insn-008aced4)
- ブロック [`008aced4`](#insn-008aced4) 範囲 `[['008aced4', '008aced7']]`
  - `CONDITIONAL_JUMP` [`008aced4`](#insn-008aced4) → [`008acef4`](#insn-008acef4)
  - `FALL_THROUGH` [`008aced4`](#insn-008aced4) → [`008aced8`](#insn-008aced8)
- ブロック [`008aced8`](#insn-008aced8) 範囲 `[['008aced8', '008acedf']]`
  - `UNCONDITIONAL_JUMP` [`008acedc`](#insn-008acedc) → [`008acee8`](#insn-008acee8)
- ブロック [`008acee0`](#insn-008acee0) 範囲 `[['008acee0', '008acee7']]`
  - `FALL_THROUGH` [`008acee4`](#insn-008acee4) → [`008acee8`](#insn-008acee8)
- ブロック [`008acee8`](#insn-008acee8) 範囲 `[['008acee8', '008acef3']]`
  - `FALL_THROUGH` [`008acef0`](#insn-008acef0) → [`008acef4`](#insn-008acef4)
- ブロック [`008acef4`](#insn-008acef4) 範囲 `[['008acef4', '008acefb']]`
  - `CONDITIONAL_JUMP` [`008acef8`](#insn-008acef8) → [`008acf04`](#insn-008acf04)
  - `FALL_THROUGH` [`008acef8`](#insn-008acef8) → [`008acefc`](#insn-008acefc)
- ブロック [`008acefc`](#insn-008acefc) 範囲 `[['008acefc', '008acf03']]`
  - `FALL_THROUGH` [`008acf00`](#insn-008acf00) → [`008acf04`](#insn-008acf04)
- ブロック [`008acf04`](#insn-008acf04) 範囲 `[['008acf04', '008acf0b']]`
  - `CONDITIONAL_JUMP` [`008acf08`](#insn-008acf08) → [`008acf14`](#insn-008acf14)
  - `FALL_THROUGH` [`008acf08`](#insn-008acf08) → [`008acf0c`](#insn-008acf0c)
- ブロック [`008acf0c`](#insn-008acf0c) 範囲 `[['008acf0c', '008acf13']]`
  - `FALL_THROUGH` [`008acf10`](#insn-008acf10) → [`008acf14`](#insn-008acf14)
- ブロック [`008acf14`](#insn-008acf14) 範囲 `[['008acf14', '008acf23']]`
  - `CONDITIONAL_JUMP` [`008acf20`](#insn-008acf20) → [`008acf88`](#insn-008acf88)
  - `FALL_THROUGH` [`008acf20`](#insn-008acf20) → [`008acf24`](#insn-008acf24)
- ブロック [`008acf24`](#insn-008acf24) 範囲 `[['008acf24', '008acf37']]`
- ブロック [`008acf88`](#insn-008acf88) 範囲 `[['008acf88', '008acf8b']]`

## 命令位置別の参照

- [`008acdb0`](#insn-008acdb0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008acdb4`](#insn-008acdb4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008acdb8`](#insn-008acdb8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008acdc8`](#insn-008acdc8) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008acdd0`](#insn-008acdd0) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`008acddc`](#insn-008acddc) → [`008bb568`](../008bb/008bb568.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008bb568` · 推定シンボル `None` · 推定型 `None`
- [`008acde0`](#insn-008acde0) → [`008acdf4`](#insn-008acdf4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008acde4`](#insn-008acde4) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`008acdf0`](#insn-008acdf0) → [`008bbab8`](../008bb/008bbab8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008bbab8` · 推定シンボル `None` · 推定型 `None`
- [`008acdf4`](#insn-008acdf4) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`008acdfc`](#insn-008acdfc) → [`008ace50`](#insn-008ace50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ace00`](#insn-008ace00) → [`009ccb84`](../009cc/009ccb84.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009ccb84` · 推定シンボル `None` · 推定型 `None`
- [`008ace04`](#insn-008ace04) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`008ace08`](#insn-008ace08) → [`008629d8`](../00862/008629d8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008629d8` · 推定シンボル `None` · 推定型 `None`
- [`008ace0c`](#insn-008ace0c) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`008ace1c`](#insn-008ace1c) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`008ace20`](#insn-008ace20) → [`00a1a6f8`](../00a1a/00a1a6f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a1a6f8` · 推定シンボル `None` · 推定型 `None`
- [`008ace24`](#insn-008ace24) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`008ace2c`](#insn-008ace2c) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ace34`](#insn-008ace34) → [`008acf88`](#insn-008acf88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ace3c`](#insn-008ace3c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ace40`](#insn-008ace40) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ace44`](#insn-008ace44) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ace4c`](#insn-008ace4c) → [`00851a64`](../00851/00851a64.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851a64` · 推定シンボル `None` · 推定型 `None`
- [`008ace70`](#insn-008ace70) → `Stack[-0x8a]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ace74`](#insn-008ace74) → `002b959b`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`008ace74`](#insn-008ace74) → `002b874d`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`008ace78`](#insn-008ace78) → `002b95a8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`008ace78`](#insn-008ace78) → `002b875a`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`008ace7c`](#insn-008ace7c) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ace80`](#insn-008ace80) → `Stack[-0x9f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ace84`](#insn-008ace84) → `Stack[-0x92]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ace90`](#insn-008ace90) → [`0048ce94`](../0048c/0048ce94.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0048ce94` · 推定シンボル `None` · 推定型 `None`
- [`008acea0`](#insn-008acea0) → `00c83970`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`008acea0`](#insn-008acea0) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008acea8`](#insn-008acea8) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008acec4`](#insn-008acec4) → [`008bad20`](../008ba/008bad20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008bad20` · 推定シンボル `None` · 推定型 `None`
- [`008acec8`](#insn-008acec8) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008aced0`](#insn-008aced0) → [`008acee0`](#insn-008acee0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008aced4`](#insn-008aced4) → [`008acef4`](#insn-008acef4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008acedc`](#insn-008acedc) → [`008acee8`](#insn-008acee8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008acee8`](#insn-008acee8) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008aceec`](#insn-008aceec) → `00c83990`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`008aceec`](#insn-008aceec) → `00c83998`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`008acef0`](#insn-008acef0) → [`008ad02c`](../008ad/008ad02c.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `008ad02c` · 推定シンボル `None` · 推定型 `None`
- [`008acef0`](#insn-008acef0) → [`008ad030`](../008ad/008ad030.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `008ad030` · 推定シンボル `None` · 推定型 `None`
- [`008acef4`](#insn-008acef4) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008acef8`](#insn-008acef8) → [`008acf04`](#insn-008acf04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008acefc`](#insn-008acefc) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008acf00`](#insn-008acf00) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`008acf04`](#insn-008acf04) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008acf08`](#insn-008acf08) → [`008acf14`](#insn-008acf14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008acf0c`](#insn-008acf0c) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008acf10`](#insn-008acf10) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`008acf18`](#insn-008acf18) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008acf20`](#insn-008acf20) → [`008acf88`](#insn-008acf88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008acf24`](#insn-008acf24) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008acf28`](#insn-008acf28) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008acf2c`](#insn-008acf2c) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008acf88`](#insn-008acf88) → [`00c57fb0`](../00c57/00c57fb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fb0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`008acdb0`](#insn-008acdb0)

~~~json
{
  "source": "008acdb0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008acdb4`](#insn-008acdb4)

~~~json
{
  "source": "008acdb4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008acdb8`](#insn-008acdb8)

~~~json
{
  "source": "008acdb8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008acdc8`](#insn-008acdc8)

~~~json
{
  "source": "008acdc8",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008acdd0`](#insn-008acdd0)

~~~json
{
  "source": "008acdd0",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008acddc`](#insn-008acddc)

~~~json
{
  "source": "008acddc",
  "target": "008bb568",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008acde0`](#insn-008acde0)

~~~json
{
  "source": "008acde0",
  "target": "008acdf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008acde4`](#insn-008acde4)

~~~json
{
  "source": "008acde4",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008acdf0`](#insn-008acdf0)

~~~json
{
  "source": "008acdf0",
  "target": "008bbab8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008acdf4`](#insn-008acdf4)

~~~json
{
  "source": "008acdf4",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008acdfc`](#insn-008acdfc)

~~~json
{
  "source": "008acdfc",
  "target": "008ace50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ace00`](#insn-008ace00)

~~~json
{
  "source": "008ace00",
  "target": "009ccb84",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008ace04`](#insn-008ace04)

~~~json
{
  "source": "008ace04",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008ace08`](#insn-008ace08)

~~~json
{
  "source": "008ace08",
  "target": "008629d8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008ace0c`](#insn-008ace0c)

~~~json
{
  "source": "008ace0c",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008ace1c`](#insn-008ace1c)

~~~json
{
  "source": "008ace1c",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008ace20`](#insn-008ace20)

~~~json
{
  "source": "008ace20",
  "target": "00a1a6f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008ace24`](#insn-008ace24)

~~~json
{
  "source": "008ace24",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008ace2c`](#insn-008ace2c)

~~~json
{
  "source": "008ace2c",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ace34`](#insn-008ace34)

~~~json
{
  "source": "008ace34",
  "target": "008acf88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ace3c`](#insn-008ace3c)

~~~json
{
  "source": "008ace3c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ace40`](#insn-008ace40)

~~~json
{
  "source": "008ace40",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ace44`](#insn-008ace44)

~~~json
{
  "source": "008ace44",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ace4c`](#insn-008ace4c)

~~~json
{
  "source": "008ace4c",
  "target": "00851a64",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008ace70`](#insn-008ace70)

~~~json
{
  "source": "008ace70",
  "target": "Stack[-0x8a]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ace74`](#insn-008ace74)

~~~json
{
  "source": "008ace74",
  "target": "002b959b",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b959b",
  "offset": 0,
  "size": 22,
  "datatype": "string",
  "bytes": "4163636f756e7444656c6574655f6572726f72303200",
  "capture_start": "002b959b",
  "capture_bytes": 22,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008ace74`](#insn-008ace74)

~~~json
{
  "source": "008ace74",
  "target": "002b874d",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b874d",
  "offset": 0,
  "size": 22,
  "datatype": "string",
  "bytes": "4163636f756e7444656c6574655f6572726f72303300",
  "capture_start": "002b874d",
  "capture_bytes": 22,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008ace78`](#insn-008ace78)

~~~json
{
  "source": "008ace78",
  "target": "002b95a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b959b",
  "offset": 13,
  "size": 22,
  "datatype": "string",
  "bytes": "4163636f756e7444656c6574655f6572726f72303200",
  "capture_start": "002b959b",
  "capture_bytes": 22,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008ace78`](#insn-008ace78)

~~~json
{
  "source": "008ace78",
  "target": "002b875a",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b874d",
  "offset": 13,
  "size": 22,
  "datatype": "string",
  "bytes": "4163636f756e7444656c6574655f6572726f72303300",
  "capture_start": "002b874d",
  "capture_bytes": 22,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008ace7c`](#insn-008ace7c)

~~~json
{
  "source": "008ace7c",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ace80`](#insn-008ace80)

~~~json
{
  "source": "008ace80",
  "target": "Stack[-0x9f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ace84`](#insn-008ace84)

~~~json
{
  "source": "008ace84",
  "target": "Stack[-0x92]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ace90`](#insn-008ace90)

~~~json
{
  "source": "008ace90",
  "target": "0048ce94",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008acea0`](#insn-008acea0)

~~~json
{
  "source": "008acea0",
  "target": "00c83970",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c83970",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`008acea0`](#insn-008acea0)

~~~json
{
  "source": "008acea0",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008acea8`](#insn-008acea8)

~~~json
{
  "source": "008acea8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008acec4`](#insn-008acec4)

~~~json
{
  "source": "008acec4",
  "target": "008bad20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008acec8`](#insn-008acec8)

~~~json
{
  "source": "008acec8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008aced0`](#insn-008aced0)

~~~json
{
  "source": "008aced0",
  "target": "008acee0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008aced4`](#insn-008aced4)

~~~json
{
  "source": "008aced4",
  "target": "008acef4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008acedc`](#insn-008acedc)

~~~json
{
  "source": "008acedc",
  "target": "008acee8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008acee8`](#insn-008acee8)

~~~json
{
  "source": "008acee8",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008aceec`](#insn-008aceec)

~~~json
{
  "source": "008aceec",
  "target": "00c83990",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c83990",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`008aceec`](#insn-008aceec)

~~~json
{
  "source": "008aceec",
  "target": "00c83998",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c83998",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`008acef0`](#insn-008acef0)

~~~json
{
  "source": "008acef0",
  "target": "008ad02c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008acef0`](#insn-008acef0)

~~~json
{
  "source": "008acef0",
  "target": "008ad030",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008acef4`](#insn-008acef4)

~~~json
{
  "source": "008acef4",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008acef8`](#insn-008acef8)

~~~json
{
  "source": "008acef8",
  "target": "008acf04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008acefc`](#insn-008acefc)

~~~json
{
  "source": "008acefc",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008acf00`](#insn-008acf00)

~~~json
{
  "source": "008acf00",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008acf04`](#insn-008acf04)

~~~json
{
  "source": "008acf04",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008acf08`](#insn-008acf08)

~~~json
{
  "source": "008acf08",
  "target": "008acf14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008acf0c`](#insn-008acf0c)

~~~json
{
  "source": "008acf0c",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008acf10`](#insn-008acf10)

~~~json
{
  "source": "008acf10",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008acf18`](#insn-008acf18)

~~~json
{
  "source": "008acf18",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008acf20`](#insn-008acf20)

~~~json
{
  "source": "008acf20",
  "target": "008acf88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008acf24`](#insn-008acf24)

~~~json
{
  "source": "008acf24",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008acf28`](#insn-008acf28)

~~~json
{
  "source": "008acf28",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008acf2c`](#insn-008acf2c)

~~~json
{
  "source": "008acf2c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008acf88`](#insn-008acf88)

~~~json
{
  "source": "008acf88",
  "target": "00c57fb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
