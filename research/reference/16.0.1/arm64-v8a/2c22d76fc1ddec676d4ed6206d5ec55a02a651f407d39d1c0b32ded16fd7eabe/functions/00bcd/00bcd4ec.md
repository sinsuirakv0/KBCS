# 00bcd4ec

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bcd0c4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcd0c4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0081.md#compare-a1ba4bd0e55e291e64dfb104f4b3484a)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bcd588`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcd/00bcd588.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0081.md#compare-4920aa021a411e079161a02653e7c2ad)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcd4ec",
  "name": "_ZN8firebase4auth13CheckEmulatorEPNS0_8AuthDataE",
  "size": 328,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "cbf095072252d4b5722aa06a8b97f1cd61eb116cf3a6ec2997a5bfb3c6ca40af",
  "source_text_sha256": "cbf095072252d4b5722aa06a8b97f1cd61eb116cf3a6ec2997a5bfb3c6ca40af",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcd4ec",
        "00bcd633"
      ]
    ],
    "bytes_sha256": "87df279062ab9e3d7985e21d849752ae5e731cb9402fb2b9b9c454d007ae24a1",
    "instruction_count": 82,
    "instruction_bytes": 328,
    "body_bytes": 328,
    "indirect": 2,
    "unresolved": 2
  }
}
~~~

## 呼び出し元

- [00c5dc20](../00c5d/00c5dc20.md)

## 呼び出し先

- [00574cec](../00574/00574cec.md)
- [00c57eb0](../00c57/00c57eb0.md)
- [00c57ee0](../00c57/00c57ee0.md)
- [00c58060](../00c58/00c58060.md)
- [00c598a0](../00c59/00c598a0.md)
- [00c5af60](../00c5a/00c5af60.md)
- [00c5afe0](../00c5a/00c5afe0.md)
- [00c5b080](../00c5b/00c5b080.md)
- [00c5b5c0](../00c5b/00c5b5c0.md)

## 関連文字列（未確認候補）

~~~text
"10.0.2.2"
"9099"
"AUTH_EMULATOR_PORT"
"USE_AUTH_EMULATOR"
"Using Auth Emulator for testing."
"Using Auth Prod for testing."
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1957 bytes

~~~c

void _ZN8firebase4auth13CheckEmulatorEPNS0_8AuthDataE(undefined8 *param_1)

{
  long lVar1;
  undefined4 uVar2;
  char *pcVar3;
  long *plVar4;
  undefined8 uVar5;
  byte local_50 [16];
  void *local_40;
  long local_38;
  
  lVar1 = tpidr_el0;
  local_38 = *(long *)(lVar1 + 0x28);
  pcVar3 = getenv("USE_AUTH_EMULATOR");
  if (pcVar3 == (char *)0x0) {
    _ZN8firebase7LogInfoEPKcz("Using Auth Prod for testing.");
  }
  else {
    _ZN8firebase7LogInfoEPKcz("Using Auth Emulator for testing.");
    _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2IDnEEPKc
              (local_50,&DAT_002bd456);
                    /* try { // try from 00bcd540 to 00ccd54b has its CatchHandler @ 00bce8e4 */
    uVar2 = _ZNSt6__ndk14stoiERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPmi
                      (local_50,0,10);
    if ((local_50[0] & 1) != 0) {
      _ZdlPv(local_40);
    }
                    /* try { // try from 00bcd560 to 00ccd563 has its CatchHandler @ 00bce888 */
                    /* try { // try from 00bcd564 to 00ccd88f has its CatchHandler @ 00bcc5d0 */
    pcVar3 = getenv("AUTH_EMULATOR_PORT");
    if (pcVar3 != (char *)0x0) {
      _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2IDnEEPKc(local_50,pcVar3);
      uVar2 = _ZNSt6__ndk14stoiERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPmi
                        (local_50,0,10);
      if ((local_50[0] & 1) != 0) {
        _ZdlPv(local_40);
      }
    }
    plVar4 = (long *)_ZNK8firebase3App9GetJNIEnvEv(*param_1);
    uVar5 = (**(code **)(*plVar4 + 0x538))(plVar4,"10.0.2.2");
    FUN_00574cec(plVar4,param_1[0x3f],DAT_01126788,uVar5,uVar2);
    (**(code **)(*plVar4 + 0xb8))(plVar4,uVar5);
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar4);
  }
  if (*(long *)(lVar1 + 0x28) == local_38) {
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
<a id="insn-00bcd4ec"></a> `00bcd4ec` | `ff 43 01 d1` | sub sp,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00bcd4f0"></a> `00bcd4f0` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcd4f4"></a> `00bcd4f4` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bcd4f8"></a> `00bcd4f8` | `fd 7b 04 a9` | stp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bcd4fc"></a> `00bcd4fc` | `fd 03 01 91` | add x29,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00bcd500"></a> `00bcd500` | `56 d0 3b d5` | mrs x22,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00bcd504"></a> `00bcd504` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00bcd508"></a> `00bcd508` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bcd50c"></a> `00bcd50c` | `60 b7 ff b0` | adrp x0,0x2ba000 | `FALL_THROUGH`
<a id="insn-00bcd510"></a> `00bcd510` | `00 4c 3c 91` | add x0,x0,#0xf13 | `FALL_THROUGH`
<a id="insn-00bcd514"></a> `00bcd514` | `e8 0f 00 f9` | str x8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bcd518"></a> `00bcd518` | `e2 30 02 94` | bl 0x00c598a0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcd51c"></a> `00bcd51c` | `20 07 00 b4` | cbz x0,0x00bcd600 | `CONDITIONAL_JUMP`
<a id="insn-00bcd520"></a> `00bcd520` | `a0 b7 ff 90` | adrp x0,0x2c1000 | `FALL_THROUGH`
<a id="insn-00bcd524"></a> `00bcd524` | `00 0c 36 91` | add x0,x0,#0xd83 | `FALL_THROUGH`
<a id="insn-00bcd528"></a> `00bcd528` | `ae 36 02 94` | bl 0x00c5afe0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcd52c"></a> `00bcd52c` | `81 b7 ff 90` | adrp x1,0x2bd000 | `FALL_THROUGH`
<a id="insn-00bcd530"></a> `00bcd530` | `21 58 11 91` | add x1,x1,#0x456 | `FALL_THROUGH`
<a id="insn-00bcd534"></a> `00bcd534` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00bcd538"></a> `00bcd538` | `22 38 02 94` | bl 0x00c5b5c0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcd53c"></a> `00bcd53c` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00bcd540"></a> `00bcd540` | `42 01 80 52` | mov w2,#0xa | `FALL_THROUGH`
<a id="insn-00bcd544"></a> `00bcd544` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-00bcd548"></a> `00bcd548` | `c6 2a 02 94` | bl 0x00c58060 | `UNCONDITIONAL_CALL`
<a id="insn-00bcd54c"></a> `00bcd54c` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-00bcd550"></a> `00bcd550` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00bcd554"></a> `00bcd554` | `68 00 00 36` | tbz w8,#0x0,0x00bcd560 | `CONDITIONAL_JUMP`
<a id="insn-00bcd558"></a> `00bcd558` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcd55c"></a> `00bcd55c` | `55 2a 02 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcd560"></a> `00bcd560` | `20 b7 ff 90` | adrp x0,0x2b1000 | `FALL_THROUGH`
<a id="insn-00bcd564"></a> `00bcd564` | `00 78 1c 91` | add x0,x0,#0x71e | `FALL_THROUGH`
<a id="insn-00bcd568"></a> `00bcd568` | `ce 30 02 94` | bl 0x00c598a0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcd56c"></a> `00bcd56c` | `a0 01 00 b4` | cbz x0,0x00bcd5a0 | `CONDITIONAL_JUMP`
<a id="insn-00bcd570"></a> `00bcd570` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00bcd574"></a> `00bcd574` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00bcd578"></a> `00bcd578` | `12 38 02 94` | bl 0x00c5b5c0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcd57c"></a> `00bcd57c` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00bcd580"></a> `00bcd580` | `42 01 80 52` | mov w2,#0xa | `FALL_THROUGH`
<a id="insn-00bcd584"></a> `00bcd584` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-00bcd588"></a> `00bcd588` | `b6 2a 02 94` | bl 0x00c58060 | `UNCONDITIONAL_CALL`
<a id="insn-00bcd58c"></a> `00bcd58c` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-00bcd590"></a> `00bcd590` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00bcd594"></a> `00bcd594` | `68 00 00 36` | tbz w8,#0x0,0x00bcd5a0 | `CONDITIONAL_JUMP`
<a id="insn-00bcd598"></a> `00bcd598` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcd59c"></a> `00bcd59c` | `45 2a 02 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcd5a0"></a> `00bcd5a0` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00bcd5a4"></a> `00bcd5a4` | `b7 36 02 94` | bl 0x00c5b080 | `UNCONDITIONAL_CALL`
<a id="insn-00bcd5a8"></a> `00bcd5a8` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bcd5ac"></a> `00bcd5ac` | `61 b7 ff f0` | adrp x1,0x2bc000 | `FALL_THROUGH`
<a id="insn-00bcd5b0"></a> `00bcd5b0` | `21 78 04 91` | add x1,x1,#0x11e | `FALL_THROUGH`
<a id="insn-00bcd5b4"></a> `00bcd5b4` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bcd5b8"></a> `00bcd5b8` | `08 9d 42 f9` | ldr x8,[x8, #0x538] | `FALL_THROUGH`
<a id="insn-00bcd5bc"></a> `00bcd5bc` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcd5c0"></a> `00bcd5c0` | `c8 2a 00 b0` | adrp x8,0x1126000 | `FALL_THROUGH`
<a id="insn-00bcd5c4"></a> `00bcd5c4` | `61 fe 40 f9` | ldr x1,[x19, #0x1f8] | `FALL_THROUGH`
<a id="insn-00bcd5c8"></a> `00bcd5c8` | `02 c5 43 f9` | ldr x2,[x8, #0x788] | `FALL_THROUGH`
<a id="insn-00bcd5cc"></a> `00bcd5cc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bcd5d0"></a> `00bcd5d0` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bcd5d4"></a> `00bcd5d4` | `e3 03 13 aa` | mov x3,x19 | `FALL_THROUGH`
<a id="insn-00bcd5d8"></a> `00bcd5d8` | `e4 03 14 2a` | mov w4,w20 | `FALL_THROUGH`
<a id="insn-00bcd5dc"></a> `00bcd5dc` | `c4 9d e6 97` | bl 0x00574cec | `UNCONDITIONAL_CALL`
<a id="insn-00bcd5e0"></a> `00bcd5e0` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bcd5e4"></a> `00bcd5e4` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bcd5e8"></a> `00bcd5e8` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bcd5ec"></a> `00bcd5ec` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bcd5f0"></a> `00bcd5f0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcd5f4"></a> `00bcd5f4` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bcd5f8"></a> `00bcd5f8` | `5a 36 02 94` | bl 0x00c5af60 | `UNCONDITIONAL_CALL`
<a id="insn-00bcd5fc"></a> `00bcd5fc` | `04 00 00 14` | b 0x00bcd60c | `UNCONDITIONAL_JUMP`
<a id="insn-00bcd600"></a> `00bcd600` | `00 b7 ff 90` | adrp x0,0x2ad000 | `FALL_THROUGH`
<a id="insn-00bcd604"></a> `00bcd604` | `00 a8 0d 91` | add x0,x0,#0x36a | `FALL_THROUGH`
<a id="insn-00bcd608"></a> `00bcd608` | `76 36 02 94` | bl 0x00c5afe0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcd60c"></a> `00bcd60c` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00bcd610"></a> `00bcd610` | `e9 0f 40 f9` | ldr x9,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bcd614"></a> `00bcd614` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bcd618"></a> `00bcd618` | `c1 00 00 54` | b.ne 0x00bcd630 | `CONDITIONAL_JUMP`
<a id="insn-00bcd61c"></a> `00bcd61c` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bcd620"></a> `00bcd620` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bcd624"></a> `00bcd624` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcd628"></a> `00bcd628` | `ff 43 01 91` | add sp,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00bcd62c"></a> `00bcd62c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bcd630"></a> `00bcd630` | `2c 2a 02 94` | bl 0x00c57ee0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcd4ec`](#insn-00bcd4ec) 範囲 `[['00bcd4ec', '00bcd51f']]`
  - `CONDITIONAL_JUMP` [`00bcd51c`](#insn-00bcd51c) → [`00bcd600`](#insn-00bcd600)
  - `FALL_THROUGH` [`00bcd51c`](#insn-00bcd51c) → [`00bcd520`](#insn-00bcd520)
- ブロック [`00bcd520`](#insn-00bcd520) 範囲 `[['00bcd520', '00bcd53f']]`
  - `FALL_THROUGH` [`00bcd53c`](#insn-00bcd53c) → [`00bcd540`](#insn-00bcd540)
- ブロック [`00bcd540`](#insn-00bcd540) 範囲 `[['00bcd540', '00bcd557']]`
  - `CONDITIONAL_JUMP` [`00bcd554`](#insn-00bcd554) → [`00bcd560`](#insn-00bcd560)
  - `FALL_THROUGH` [`00bcd554`](#insn-00bcd554) → [`00bcd558`](#insn-00bcd558)
- ブロック [`00bcd558`](#insn-00bcd558) 範囲 `[['00bcd558', '00bcd55f']]`
  - `FALL_THROUGH` [`00bcd55c`](#insn-00bcd55c) → [`00bcd560`](#insn-00bcd560)
- ブロック [`00bcd560`](#insn-00bcd560) 範囲 `[['00bcd560', '00bcd563']]`
  - `FALL_THROUGH` [`00bcd560`](#insn-00bcd560) → [`00bcd564`](#insn-00bcd564)
- ブロック [`00bcd564`](#insn-00bcd564) 範囲 `[['00bcd564', '00bcd56f']]`
  - `CONDITIONAL_JUMP` [`00bcd56c`](#insn-00bcd56c) → [`00bcd5a0`](#insn-00bcd5a0)
  - `FALL_THROUGH` [`00bcd56c`](#insn-00bcd56c) → [`00bcd570`](#insn-00bcd570)
- ブロック [`00bcd570`](#insn-00bcd570) 範囲 `[['00bcd570', '00bcd597']]`
  - `CONDITIONAL_JUMP` [`00bcd594`](#insn-00bcd594) → [`00bcd5a0`](#insn-00bcd5a0)
  - `FALL_THROUGH` [`00bcd594`](#insn-00bcd594) → [`00bcd598`](#insn-00bcd598)
- ブロック [`00bcd598`](#insn-00bcd598) 範囲 `[['00bcd598', '00bcd59f']]`
  - `FALL_THROUGH` [`00bcd59c`](#insn-00bcd59c) → [`00bcd5a0`](#insn-00bcd5a0)
- ブロック [`00bcd5a0`](#insn-00bcd5a0) 範囲 `[['00bcd5a0', '00bcd5ff']]`
  - `UNCONDITIONAL_JUMP` [`00bcd5fc`](#insn-00bcd5fc) → [`00bcd60c`](#insn-00bcd60c)
- ブロック [`00bcd600`](#insn-00bcd600) 範囲 `[['00bcd600', '00bcd60b']]`
  - `FALL_THROUGH` [`00bcd608`](#insn-00bcd608) → [`00bcd60c`](#insn-00bcd60c)
- ブロック [`00bcd60c`](#insn-00bcd60c) 範囲 `[['00bcd60c', '00bcd61b']]`
  - `CONDITIONAL_JUMP` [`00bcd618`](#insn-00bcd618) → [`00bcd630`](#insn-00bcd630)
  - `FALL_THROUGH` [`00bcd618`](#insn-00bcd618) → [`00bcd61c`](#insn-00bcd61c)
- ブロック [`00bcd61c`](#insn-00bcd61c) 範囲 `[['00bcd61c', '00bcd62f']]`
- ブロック [`00bcd630`](#insn-00bcd630) 範囲 `[['00bcd630', '00bcd633']]`

## 命令位置別の参照

- [`00bcd4f0`](#insn-00bcd4f0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd4f4`](#insn-00bcd4f4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd4f8`](#insn-00bcd4f8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd510`](#insn-00bcd510) → `002baf13`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bcd514`](#insn-00bcd514) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd518`](#insn-00bcd518) → [`00c598a0`](../00c59/00c598a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c598a0` · 推定シンボル `None` · 推定型 `None`
- [`00bcd51c`](#insn-00bcd51c) → [`00bcd600`](#insn-00bcd600) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd524`](#insn-00bcd524) → `002c1d83`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bcd528`](#insn-00bcd528) → [`00c5afe0`](../00c5a/00c5afe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5afe0` · 推定シンボル `None` · 推定型 `None`
- [`00bcd530`](#insn-00bcd530) → `002bd456`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd538`](#insn-00bcd538) → [`00c5b5c0`](../00c5b/00c5b5c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b5c0` · 推定シンボル `None` · 推定型 `None`
- [`00bcd548`](#insn-00bcd548) → [`00c58060`](../00c58/00c58060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58060` · 推定シンボル `None` · 推定型 `None`
- [`00bcd54c`](#insn-00bcd54c) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd554`](#insn-00bcd554) → [`00bcd560`](#insn-00bcd560) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd558`](#insn-00bcd558) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd55c`](#insn-00bcd55c) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00bcd564`](#insn-00bcd564) → `002b171e`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bcd568`](#insn-00bcd568) → [`00c598a0`](../00c59/00c598a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c598a0` · 推定シンボル `None` · 推定型 `None`
- [`00bcd56c`](#insn-00bcd56c) → [`00bcd5a0`](#insn-00bcd5a0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd578`](#insn-00bcd578) → [`00c5b5c0`](../00c5b/00c5b5c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b5c0` · 推定シンボル `None` · 推定型 `None`
- [`00bcd588`](#insn-00bcd588) → [`00c58060`](../00c58/00c58060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58060` · 推定シンボル `None` · 推定型 `None`
- [`00bcd58c`](#insn-00bcd58c) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd594`](#insn-00bcd594) → [`00bcd5a0`](#insn-00bcd5a0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd598`](#insn-00bcd598) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd59c`](#insn-00bcd59c) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00bcd5a4`](#insn-00bcd5a4) → [`00c5b080`](../00c5b/00c5b080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b080` · 推定シンボル `None` · 推定型 `None`
- [`00bcd5b0`](#insn-00bcd5b0) → `002bc11e`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bcd5c8`](#insn-00bcd5c8) → `01126788`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bcd5dc`](#insn-00bcd5dc) → [`00574cec`](../00574/00574cec.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00574cec` · 推定シンボル `None` · 推定型 `None`
- [`00bcd5f8`](#insn-00bcd5f8) → [`00c5af60`](../00c5a/00c5af60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af60` · 推定シンボル `None` · 推定型 `None`
- [`00bcd5fc`](#insn-00bcd5fc) → [`00bcd60c`](#insn-00bcd60c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd604`](#insn-00bcd604) → `002ad36a`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bcd608`](#insn-00bcd608) → [`00c5afe0`](../00c5a/00c5afe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5afe0` · 推定シンボル `None` · 推定型 `None`
- [`00bcd610`](#insn-00bcd610) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd618`](#insn-00bcd618) → [`00bcd630`](#insn-00bcd630) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd61c`](#insn-00bcd61c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd620`](#insn-00bcd620) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd624`](#insn-00bcd624) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd630`](#insn-00bcd630) → [`00c57ee0`](../00c57/00c57ee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ee0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcd4f0`](#insn-00bcd4f0)

~~~json
{
  "source": "00bcd4f0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd4f4`](#insn-00bcd4f4)

~~~json
{
  "source": "00bcd4f4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd4f8`](#insn-00bcd4f8)

~~~json
{
  "source": "00bcd4f8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd510`](#insn-00bcd510)

~~~json
{
  "source": "00bcd510",
  "target": "002baf13",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002baf13",
  "offset": 0,
  "size": 18,
  "datatype": "string",
  "bytes": "5553455f415554485f454d554c41544f5200",
  "capture_start": "002baf13",
  "capture_bytes": 18,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bcd514`](#insn-00bcd514)

~~~json
{
  "source": "00bcd514",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd518`](#insn-00bcd518)

~~~json
{
  "source": "00bcd518",
  "target": "00c598a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcd51c`](#insn-00bcd51c)

~~~json
{
  "source": "00bcd51c",
  "target": "00bcd600",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd524`](#insn-00bcd524)

~~~json
{
  "source": "00bcd524",
  "target": "002c1d83",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002c1d83",
  "offset": 0,
  "size": 33,
  "datatype": "string",
  "bytes": "5573696e67204175746820456d756c61746f7220666f722074657374696e672e",
  "capture_start": "002c1d83",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bcd528`](#insn-00bcd528)

~~~json
{
  "source": "00bcd528",
  "target": "00c5afe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcd530`](#insn-00bcd530)

~~~json
{
  "source": "00bcd530",
  "target": "002bd456",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd538`](#insn-00bcd538)

~~~json
{
  "source": "00bcd538",
  "target": "00c5b5c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcd548`](#insn-00bcd548)

~~~json
{
  "source": "00bcd548",
  "target": "00c58060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcd54c`](#insn-00bcd54c)

~~~json
{
  "source": "00bcd54c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd554`](#insn-00bcd554)

~~~json
{
  "source": "00bcd554",
  "target": "00bcd560",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd558`](#insn-00bcd558)

~~~json
{
  "source": "00bcd558",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd55c`](#insn-00bcd55c)

~~~json
{
  "source": "00bcd55c",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcd564`](#insn-00bcd564)

~~~json
{
  "source": "00bcd564",
  "target": "002b171e",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b171e",
  "offset": 0,
  "size": 19,
  "datatype": "string",
  "bytes": "415554485f454d554c41544f525f504f525400",
  "capture_start": "002b171e",
  "capture_bytes": 19,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bcd568`](#insn-00bcd568)

~~~json
{
  "source": "00bcd568",
  "target": "00c598a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcd56c`](#insn-00bcd56c)

~~~json
{
  "source": "00bcd56c",
  "target": "00bcd5a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd578`](#insn-00bcd578)

~~~json
{
  "source": "00bcd578",
  "target": "00c5b5c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcd588`](#insn-00bcd588)

~~~json
{
  "source": "00bcd588",
  "target": "00c58060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcd58c`](#insn-00bcd58c)

~~~json
{
  "source": "00bcd58c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd594`](#insn-00bcd594)

~~~json
{
  "source": "00bcd594",
  "target": "00bcd5a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd598`](#insn-00bcd598)

~~~json
{
  "source": "00bcd598",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd59c`](#insn-00bcd59c)

~~~json
{
  "source": "00bcd59c",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcd5a4`](#insn-00bcd5a4)

~~~json
{
  "source": "00bcd5a4",
  "target": "00c5b080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcd5b0`](#insn-00bcd5b0)

~~~json
{
  "source": "00bcd5b0",
  "target": "002bc11e",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002bc11e",
  "offset": 0,
  "size": 9,
  "datatype": "string",
  "bytes": "31302e302e322e3200",
  "capture_start": "002bc11e",
  "capture_bytes": 9,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bcd5c8`](#insn-00bcd5c8)

~~~json
{
  "source": "00bcd5c8",
  "target": "01126788",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126788",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcd5dc`](#insn-00bcd5dc)

~~~json
{
  "source": "00bcd5dc",
  "target": "00574cec",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcd5f8`](#insn-00bcd5f8)

~~~json
{
  "source": "00bcd5f8",
  "target": "00c5af60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcd5fc`](#insn-00bcd5fc)

~~~json
{
  "source": "00bcd5fc",
  "target": "00bcd60c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd604`](#insn-00bcd604)

~~~json
{
  "source": "00bcd604",
  "target": "002ad36a",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002ad36a",
  "offset": 0,
  "size": 29,
  "datatype": "string",
  "bytes": "5573696e6720417574682050726f6420666f722074657374696e672e00",
  "capture_start": "002ad36a",
  "capture_bytes": 29,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bcd608`](#insn-00bcd608)

~~~json
{
  "source": "00bcd608",
  "target": "00c5afe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcd610`](#insn-00bcd610)

~~~json
{
  "source": "00bcd610",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd618`](#insn-00bcd618)

~~~json
{
  "source": "00bcd618",
  "target": "00bcd630",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd61c`](#insn-00bcd61c)

~~~json
{
  "source": "00bcd61c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd620`](#insn-00bcd620)

~~~json
{
  "source": "00bcd620",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd624`](#insn-00bcd624)

~~~json
{
  "source": "00bcd624",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd630`](#insn-00bcd630)

~~~json
{
  "source": "00bcd630",
  "target": "00c57ee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
