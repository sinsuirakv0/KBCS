# 00bbbcdc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bbbc40`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbb/00bbbc40.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0079.md#compare-ef774e060e8858a61c26dfccf7368d38)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bbccd0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbc/00bbccd0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0079.md#compare-7722853f9e08a7f55e89940466ca005c)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbbcdc",
  "name": "FUN_00bbbcdc",
  "size": 444,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d1bc3d638d885641760719ada7586978f20d0a7c5ac5b9c6137a6f8b9bfcceff",
  "source_text_sha256": "d1bc3d638d885641760719ada7586978f20d0a7c5ac5b9c6137a6f8b9bfcceff",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbbcdc",
        "00bbbe97"
      ]
    ],
    "bytes_sha256": "4d17f8a4c349d726f3f90e84e9057f528a2bb7973ba490cdb3849607f14f0fd2",
    "instruction_count": 111,
    "instruction_bytes": 444,
    "body_bytes": 444,
    "indirect": 6,
    "unresolved": 6
  }
}
~~~

## 呼び出し元

- [00bbba0c](../00bbb/00bbba0c.md)
- [00bbd25c](../00bbd/00bbd25c.md)

## 呼び出し先

- [00497874](../00497/00497874.md)
- [00c57f60](../00c57/00c57f60.md)
- [00c57f80](../00c57/00c57f80.md)
- [00c57fb0](../00c57/00c57fb0.md)
- [00c5ab60](../00c5a/00c5ab60.md)
- [00c5ae70](../00c5a/00c5ae70.md)
- [00c5aed0](../00c5a/00c5aed0.md)
- [00c5b010](../00c5b/00c5b010.md)
- [00c5b020](../00c5b/00c5b020.md)
- [00c5b030](../00c5b/00c5b030.md)
- [00c5b150](../00c5b/00c5b150.md)
- [00c5b200](../00c5b/00c5b200.md)
- [00c5d340](../00c5d/00c5d340.md)

## 関連文字列（未確認候補）

~~~text
"Messaging"
"Unsubscribe from topic %s"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2399 bytes

~~~c

void FUN_00bbbcdc(undefined8 param_1,undefined8 param_2)

{
  void *pvVar1;
  long lVar2;
  char cVar3;
  long *plVar4;
  undefined8 uVar5;
  long lVar6;
  undefined8 uVar7;
  undefined1 auStack_78 [16];
  byte local_68 [16];
  void *local_58;
  undefined1 auStack_50 [8];
  long local_48;
  
  lVar2 = tpidr_el0;
  local_48 = *(long *)(lVar2 + 0x28);
  _ZN8firebase8LogDebugEPKcz("Unsubscribe from topic %s",param_1);
  plVar4 = (long *)_ZNK8firebase3App9GetJNIEnvEv(DAT_01126460);
  uVar5 = (**(code **)(*plVar4 + 0x538))(plVar4,param_1);
                    /* try { // try from 00bbbd48 to 00cbbd53 has its CatchHandler @ 00bbc81c */
  lVar6 = FUN_00497874(plVar4,DAT_01126498,DAT_011263d0,uVar5);
  cVar3 = (**(code **)(*plVar4 + 0x720))(plVar4);
  if (cVar3 == '\0') {
    if (lVar6 != 0) {
      uVar7 = _Znwm(0x10);
      _ZN8firebase12FutureHandleC1ERKS0_(uVar7,param_2);
      _ZN8firebase4util22RegisterCallbackOnTaskEP7_JNIEnvP8_jobjectPFvS2_S4_NS0_12FutureResultEPKcPvES8_S7_
                (plVar4,lVar6,FUN_00bbd4fc,uVar7,"Messaging");
                    /* try { // try from 00bbbe3c to 00cbbedb has its CatchHandler @ 00bbc838 */
      _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar4);
      (**(code **)(*plVar4 + 0xb8))(plVar4,lVar6);
    }
  }
  else {
    uVar7 = (**(code **)(*plVar4 + 0x78))(plVar4);
                    /* try { // try from 00bbbd90 to 00cbbd9b has its CatchHandler @ 00bbc820 */
    (**(code **)(*plVar4 + 0x88))(plVar4);
    _ZN8firebase4util23GetMessageFromExceptionEP7_JNIEnvP8_jobject(local_68,plVar4,uVar7);
    uVar7 = _ZN8firebase9messaging10FutureData3GetEv();
    _ZN8firebase12FutureHandleC1ERKS0_(auStack_78,param_2);
    pvVar1 = (void *)((ulong)local_68 | 1);
    if ((local_68[0] & 1) != 0) {
      pvVar1 = local_58;
    }
    _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalIvEEvRKNS_12FutureHandleEiPKcEUlPvE_EEvS5_iS7_RKT0_
              (uVar7,auStack_78,2,pvVar1,auStack_50);
    _ZN8firebase12FutureHandleD2Ev(auStack_78);
                    /* try { // try from 00bbbdf4 to 00cbbdff has its CatchHandler @ 00bbc818 */
    if ((local_68[0] & 1) != 0) {
      _ZdlPv(local_58);
    }
  }
  (**(code **)(*plVar4 + 0xb8))(plVar4,uVar5);
  if (*(long *)(lVar2 + 0x28) == local_48) {
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
<a id="insn-00bbbcdc"></a> `00bbbcdc` | `ff 03 02 d1` | sub sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00bbbce0"></a> `00bbbce0` | `f8 5f 04 a9` | stp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bbbce4"></a> `00bbbce4` | `f6 57 05 a9` | stp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bbbce8"></a> `00bbbce8` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bbbcec"></a> `00bbbcec` | `fd 7b 07 a9` | stp x29,x30,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bbbcf0"></a> `00bbbcf0` | `fd c3 01 91` | add x29,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00bbbcf4"></a> `00bbbcf4` | `58 d0 3b d5` | mrs x24,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00bbbcf8"></a> `00bbbcf8` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00bbbcfc"></a> `00bbbcfc` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bbbd00"></a> `00bbbd00` | `20 b8 ff b0` | adrp x0,0x2c0000 | `FALL_THROUGH`
<a id="insn-00bbbd04"></a> `00bbbd04` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-00bbbd08"></a> `00bbbd08` | `00 4c 2f 91` | add x0,x0,#0xbd3 | `FALL_THROUGH`
<a id="insn-00bbbd0c"></a> `00bbbd0c` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bbbd10"></a> `00bbbd10` | `e8 1f 00 f9` | str x8,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00bbbd14"></a> `00bbbd14` | `3b 7d 02 94` | bl 0x00c5b200 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbd18"></a> `00bbbd18` | `48 2b 00 f0` | adrp x8,0x1126000 | `FALL_THROUGH`
<a id="insn-00bbbd1c"></a> `00bbbd1c` | `00 31 42 f9` | ldr x0,[x8, #0x460] | `FALL_THROUGH`
<a id="insn-00bbbd20"></a> `00bbbd20` | `0c 7d 02 94` | bl 0x00c5b150 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbd24"></a> `00bbbd24` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bbbd28"></a> `00bbbd28` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bbbd2c"></a> `00bbbd2c` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bbbd30"></a> `00bbbd30` | `08 9d 42 f9` | ldr x8,[x8, #0x538] | `FALL_THROUGH`
<a id="insn-00bbbd34"></a> `00bbbd34` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bbbd38"></a> `00bbbd38` | `48 2b 00 f0` | adrp x8,0x1126000 | `FALL_THROUGH`
<a id="insn-00bbbd3c"></a> `00bbbd3c` | `49 2b 00 f0` | adrp x9,0x1126000 | `FALL_THROUGH`
<a id="insn-00bbbd40"></a> `00bbbd40` | `01 4d 42 f9` | ldr x1,[x8, #0x498] | `FALL_THROUGH`
<a id="insn-00bbbd44"></a> `00bbbd44` | `22 e9 41 f9` | ldr x2,[x9, #0x3d0] | `FALL_THROUGH`
<a id="insn-00bbbd48"></a> `00bbbd48` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bbbd4c"></a> `00bbbd4c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbbd50"></a> `00bbbd50` | `e3 03 14 aa` | mov x3,x20 | `FALL_THROUGH`
<a id="insn-00bbbd54"></a> `00bbbd54` | `c8 6e e3 97` | bl 0x00497874 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbd58"></a> `00bbbd58` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbbd5c"></a> `00bbbd5c` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bbbd60"></a> `00bbbd60` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbbd64"></a> `00bbbd64` | `08 91 43 f9` | ldr x8,[x8, #0x720] | `FALL_THROUGH`
<a id="insn-00bbbd68"></a> `00bbbd68` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bbbd6c"></a> `00bbbd6c` | `1f 1c 00 72` | tst w0,#0xff | `FALL_THROUGH`
<a id="insn-00bbbd70"></a> `00bbbd70` | `a0 04 00 54` | b.eq 0x00bbbe04 | `CONDITIONAL_JUMP`
<a id="insn-00bbbd74"></a> `00bbbd74` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbbd78"></a> `00bbbd78` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbbd7c"></a> `00bbbd7c` | `08 3d 40 f9` | ldr x8,[x8, #0x78] | `FALL_THROUGH`
<a id="insn-00bbbd80"></a> `00bbbd80` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bbbd84"></a> `00bbbd84` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbbd88"></a> `00bbbd88` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bbbd8c"></a> `00bbbd8c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbbd90"></a> `00bbbd90` | `08 45 40 f9` | ldr x8,[x8, #0x88] | `FALL_THROUGH`
<a id="insn-00bbbd94"></a> `00bbbd94` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bbbd98"></a> `00bbbd98` | `e8 63 00 91` | add x8,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bbbd9c"></a> `00bbbd9c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbbda0"></a> `00bbbda0` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bbbda4"></a> `00bbbda4` | `9f 7c 02 94` | bl 0x00c5b020 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbda8"></a> `00bbbda8` | `66 85 02 94` | bl 0x00c5d340 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbdac"></a> `00bbbdac` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bbbdb0"></a> `00bbbdb0` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bbbdb4"></a> `00bbbdb4` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bbbdb8"></a> `00bbbdb8` | `46 7c 02 94` | bl 0x00c5aed0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbdbc"></a> `00bbbdbc` | `e8 63 40 39` | ldrb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bbbdc0"></a> `00bbbdc0` | `e9 17 40 f9` | ldr x9,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00bbbdc4"></a> `00bbbdc4` | `ea 63 00 91` | add x10,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bbbdc8"></a> `00bbbdc8` | `4a 01 40 b2` | orr x10,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bbbdcc"></a> `00bbbdcc` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbbdd0"></a> `00bbbdd0` | `43 01 89 9a` | csel x3,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00bbbdd4"></a> `00bbbdd4` | `e1 23 00 91` | add x1,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bbbdd8"></a> `00bbbdd8` | `e4 c3 00 91` | add x4,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bbbddc"></a> `00bbbddc` | `42 00 80 52` | mov w2,#0x2 | `FALL_THROUGH`
<a id="insn-00bbbde0"></a> `00bbbde0` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bbbde4"></a> `00bbbde4` | `23 7c 02 94` | bl 0x00c5ae70 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbde8"></a> `00bbbde8` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bbbdec"></a> `00bbbdec` | `5d 7b 02 94` | bl 0x00c5ab60 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbdf0"></a> `00bbbdf0` | `e8 63 40 39` | ldrb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bbbdf4"></a> `00bbbdf4` | `28 03 00 36` | tbz w8,#0x0,0x00bbbe58 | `CONDITIONAL_JUMP`
<a id="insn-00bbbdf8"></a> `00bbbdf8` | `e0 17 40 f9` | ldr x0,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00bbbdfc"></a> `00bbbdfc` | `61 70 02 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbe00"></a> `00bbbe00` | `16 00 00 14` | b 0x00bbbe58 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbbe04"></a> `00bbbe04` | `b6 02 00 b4` | cbz x22,0x00bbbe58 | `CONDITIONAL_JUMP`
<a id="insn-00bbbe08"></a> `00bbbe08` | `00 02 80 52` | mov w0,#0x10 | `FALL_THROUGH`
<a id="insn-00bbbe0c"></a> `00bbbe0c` | `55 70 02 94` | bl 0x00c57f60 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbe10"></a> `00bbbe10` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00bbbe14"></a> `00bbbe14` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bbbe18"></a> `00bbbe18` | `2e 7c 02 94` | bl 0x00c5aed0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbe1c"></a> `00bbbe1c` | `02 00 00 d0` | adrp x2,0xbbd000 | `FALL_THROUGH`
<a id="insn-00bbbe20"></a> `00bbbe20` | `84 ba ff f0` | adrp x4,0x30e000 | `FALL_THROUGH`
<a id="insn-00bbbe24"></a> `00bbbe24` | `42 f0 13 91` | add x2,x2,#0x4fc | `FALL_THROUGH`
<a id="insn-00bbbe28"></a> `00bbbe28` | `84 04 20 91` | add x4,x4,#0x801 | `FALL_THROUGH`
<a id="insn-00bbbe2c"></a> `00bbbe2c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbbe30"></a> `00bbbe30` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bbbe34"></a> `00bbbe34` | `e3 03 17 aa` | mov x3,x23 | `FALL_THROUGH`
<a id="insn-00bbbe38"></a> `00bbbe38` | `76 7c 02 94` | bl 0x00c5b010 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbe3c"></a> `00bbbe3c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbbe40"></a> `00bbbe40` | `7c 7c 02 94` | bl 0x00c5b030 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbe44"></a> `00bbbe44` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbbe48"></a> `00bbbe48` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbbe4c"></a> `00bbbe4c` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bbbe50"></a> `00bbbe50` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bbbe54"></a> `00bbbe54` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bbbe58"></a> `00bbbe58` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbbe5c"></a> `00bbbe5c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbbe60"></a> `00bbbe60` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bbbe64"></a> `00bbbe64` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bbbe68"></a> `00bbbe68` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bbbe6c"></a> `00bbbe6c` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00bbbe70"></a> `00bbbe70` | `e9 1f 40 f9` | ldr x9,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00bbbe74"></a> `00bbbe74` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bbbe78"></a> `00bbbe78` | `e1 00 00 54` | b.ne 0x00bbbe94 | `CONDITIONAL_JUMP`
<a id="insn-00bbbe7c"></a> `00bbbe7c` | `fd 7b 47 a9` | ldp x29,x30,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bbbe80"></a> `00bbbe80` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bbbe84"></a> `00bbbe84` | `f6 57 45 a9` | ldp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bbbe88"></a> `00bbbe88` | `f8 5f 44 a9` | ldp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bbbe8c"></a> `00bbbe8c` | `ff 03 02 91` | add sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00bbbe90"></a> `00bbbe90` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bbbe94"></a> `00bbbe94` | `47 70 02 94` | bl 0x00c57fb0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbbcdc`](#insn-00bbbcdc) 範囲 `[['00bbbcdc', '00bbbd47']]`
  - `FALL_THROUGH` [`00bbbd44`](#insn-00bbbd44) → [`00bbbd48`](#insn-00bbbd48)
- ブロック [`00bbbd48`](#insn-00bbbd48) 範囲 `[['00bbbd48', '00bbbd73']]`
  - `CONDITIONAL_JUMP` [`00bbbd70`](#insn-00bbbd70) → [`00bbbe04`](#insn-00bbbe04)
  - `FALL_THROUGH` [`00bbbd70`](#insn-00bbbd70) → [`00bbbd74`](#insn-00bbbd74)
- ブロック [`00bbbd74`](#insn-00bbbd74) 範囲 `[['00bbbd74', '00bbbd8f']]`
  - `FALL_THROUGH` [`00bbbd8c`](#insn-00bbbd8c) → [`00bbbd90`](#insn-00bbbd90)
- ブロック [`00bbbd90`](#insn-00bbbd90) 範囲 `[['00bbbd90', '00bbbdf3']]`
  - `FALL_THROUGH` [`00bbbdf0`](#insn-00bbbdf0) → [`00bbbdf4`](#insn-00bbbdf4)
- ブロック [`00bbbdf4`](#insn-00bbbdf4) 範囲 `[['00bbbdf4', '00bbbdf7']]`
  - `CONDITIONAL_JUMP` [`00bbbdf4`](#insn-00bbbdf4) → [`00bbbe58`](#insn-00bbbe58)
  - `FALL_THROUGH` [`00bbbdf4`](#insn-00bbbdf4) → [`00bbbdf8`](#insn-00bbbdf8)
- ブロック [`00bbbdf8`](#insn-00bbbdf8) 範囲 `[['00bbbdf8', '00bbbe03']]`
  - `UNCONDITIONAL_JUMP` [`00bbbe00`](#insn-00bbbe00) → [`00bbbe58`](#insn-00bbbe58)
- ブロック [`00bbbe04`](#insn-00bbbe04) 範囲 `[['00bbbe04', '00bbbe07']]`
  - `CONDITIONAL_JUMP` [`00bbbe04`](#insn-00bbbe04) → [`00bbbe58`](#insn-00bbbe58)
  - `FALL_THROUGH` [`00bbbe04`](#insn-00bbbe04) → [`00bbbe08`](#insn-00bbbe08)
- ブロック [`00bbbe08`](#insn-00bbbe08) 範囲 `[['00bbbe08', '00bbbe3b']]`
  - `FALL_THROUGH` [`00bbbe38`](#insn-00bbbe38) → [`00bbbe3c`](#insn-00bbbe3c)
- ブロック [`00bbbe3c`](#insn-00bbbe3c) 範囲 `[['00bbbe3c', '00bbbe57']]`
  - `FALL_THROUGH` [`00bbbe54`](#insn-00bbbe54) → [`00bbbe58`](#insn-00bbbe58)
- ブロック [`00bbbe58`](#insn-00bbbe58) 範囲 `[['00bbbe58', '00bbbe7b']]`
  - `CONDITIONAL_JUMP` [`00bbbe78`](#insn-00bbbe78) → [`00bbbe94`](#insn-00bbbe94)
  - `FALL_THROUGH` [`00bbbe78`](#insn-00bbbe78) → [`00bbbe7c`](#insn-00bbbe7c)
- ブロック [`00bbbe7c`](#insn-00bbbe7c) 範囲 `[['00bbbe7c', '00bbbe93']]`
- ブロック [`00bbbe94`](#insn-00bbbe94) 範囲 `[['00bbbe94', '00bbbe97']]`

## 命令位置別の参照

- [`00bbbce0`](#insn-00bbbce0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbce4`](#insn-00bbbce4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbce8`](#insn-00bbbce8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbcec`](#insn-00bbbcec) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbd08`](#insn-00bbbd08) → `002c0bd3`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbbd10`](#insn-00bbbd10) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbd14`](#insn-00bbbd14) → [`00c5b200`](../00c5b/00c5b200.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b200` · 推定シンボル `None` · 推定型 `None`
- [`00bbbd1c`](#insn-00bbbd1c) → `01126460`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbbd20`](#insn-00bbbd20) → [`00c5b150`](../00c5b/00c5b150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b150` · 推定シンボル `None` · 推定型 `None`
- [`00bbbd40`](#insn-00bbbd40) → `01126498`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbbd44`](#insn-00bbbd44) → `011263d0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbbd54`](#insn-00bbbd54) → [`00497874`](../00497/00497874.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00497874` · 推定シンボル `None` · 推定型 `None`
- [`00bbbd70`](#insn-00bbbd70) → [`00bbbe04`](#insn-00bbbe04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbda4`](#insn-00bbbda4) → [`00c5b020`](../00c5b/00c5b020.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b020` · 推定シンボル `None` · 推定型 `None`
- [`00bbbda8`](#insn-00bbbda8) → [`00c5d340`](../00c5d/00c5d340.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d340` · 推定シンボル `None` · 推定型 `None`
- [`00bbbdb8`](#insn-00bbbdb8) → [`00c5aed0`](../00c5a/00c5aed0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aed0` · 推定シンボル `None` · 推定型 `None`
- [`00bbbdbc`](#insn-00bbbdbc) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbdc0`](#insn-00bbbdc0) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbde4`](#insn-00bbbde4) → [`00c5ae70`](../00c5a/00c5ae70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ae70` · 推定シンボル `None` · 推定型 `None`
- [`00bbbdec`](#insn-00bbbdec) → [`00c5ab60`](../00c5a/00c5ab60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab60` · 推定シンボル `None` · 推定型 `None`
- [`00bbbdf0`](#insn-00bbbdf0) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbdf4`](#insn-00bbbdf4) → [`00bbbe58`](#insn-00bbbe58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbdf8`](#insn-00bbbdf8) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbdfc`](#insn-00bbbdfc) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00bbbe00`](#insn-00bbbe00) → [`00bbbe58`](#insn-00bbbe58) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbe04`](#insn-00bbbe04) → [`00bbbe58`](#insn-00bbbe58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbe0c`](#insn-00bbbe0c) → [`00c57f60`](../00c57/00c57f60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f60` · 推定シンボル `None` · 推定型 `None`
- [`00bbbe18`](#insn-00bbbe18) → [`00c5aed0`](../00c5a/00c5aed0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aed0` · 推定シンボル `None` · 推定型 `None`
- [`00bbbe24`](#insn-00bbbe24) → [`00bbd4fc`](../00bbd/00bbd4fc.md) · `PARAM` · `ANALYSIS` · 関数 `00bbd4fc` · 推定シンボル `None` · 推定型 `None`
- [`00bbbe28`](#insn-00bbbe28) → `0030e801`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbbe38`](#insn-00bbbe38) → [`00c5b010`](../00c5b/00c5b010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b010` · 推定シンボル `None` · 推定型 `None`
- [`00bbbe40`](#insn-00bbbe40) → [`00c5b030`](../00c5b/00c5b030.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b030` · 推定シンボル `None` · 推定型 `None`
- [`00bbbe70`](#insn-00bbbe70) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbe78`](#insn-00bbbe78) → [`00bbbe94`](#insn-00bbbe94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbe7c`](#insn-00bbbe7c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbe80`](#insn-00bbbe80) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbe84`](#insn-00bbbe84) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbe88`](#insn-00bbbe88) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbe94`](#insn-00bbbe94) → [`00c57fb0`](../00c57/00c57fb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fb0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbbce0`](#insn-00bbbce0)

~~~json
{
  "source": "00bbbce0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbce4`](#insn-00bbbce4)

~~~json
{
  "source": "00bbbce4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbce8`](#insn-00bbbce8)

~~~json
{
  "source": "00bbbce8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbcec`](#insn-00bbbcec)

~~~json
{
  "source": "00bbbcec",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbd08`](#insn-00bbbd08)

~~~json
{
  "source": "00bbbd08",
  "target": "002c0bd3",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002c0bd3",
  "offset": 0,
  "size": 26,
  "datatype": "string",
  "bytes": "556e7375627363726962652066726f6d20746f70696320257300",
  "capture_start": "002c0bd3",
  "capture_bytes": 26,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbbd10`](#insn-00bbbd10)

~~~json
{
  "source": "00bbbd10",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbd14`](#insn-00bbbd14)

~~~json
{
  "source": "00bbbd14",
  "target": "00c5b200",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbd1c`](#insn-00bbbd1c)

~~~json
{
  "source": "00bbbd1c",
  "target": "01126460",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126460",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbbd20`](#insn-00bbbd20)

~~~json
{
  "source": "00bbbd20",
  "target": "00c5b150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbd40`](#insn-00bbbd40)

~~~json
{
  "source": "00bbbd40",
  "target": "01126498",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126498",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbbd44`](#insn-00bbbd44)

~~~json
{
  "source": "00bbbd44",
  "target": "011263d0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011263d0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbbd54`](#insn-00bbbd54)

~~~json
{
  "source": "00bbbd54",
  "target": "00497874",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbd70`](#insn-00bbbd70)

~~~json
{
  "source": "00bbbd70",
  "target": "00bbbe04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbda4`](#insn-00bbbda4)

~~~json
{
  "source": "00bbbda4",
  "target": "00c5b020",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbda8`](#insn-00bbbda8)

~~~json
{
  "source": "00bbbda8",
  "target": "00c5d340",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbdb8`](#insn-00bbbdb8)

~~~json
{
  "source": "00bbbdb8",
  "target": "00c5aed0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbdbc`](#insn-00bbbdbc)

~~~json
{
  "source": "00bbbdbc",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbdc0`](#insn-00bbbdc0)

~~~json
{
  "source": "00bbbdc0",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbde4`](#insn-00bbbde4)

~~~json
{
  "source": "00bbbde4",
  "target": "00c5ae70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbdec`](#insn-00bbbdec)

~~~json
{
  "source": "00bbbdec",
  "target": "00c5ab60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbdf0`](#insn-00bbbdf0)

~~~json
{
  "source": "00bbbdf0",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbdf4`](#insn-00bbbdf4)

~~~json
{
  "source": "00bbbdf4",
  "target": "00bbbe58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbdf8`](#insn-00bbbdf8)

~~~json
{
  "source": "00bbbdf8",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbdfc`](#insn-00bbbdfc)

~~~json
{
  "source": "00bbbdfc",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbe00`](#insn-00bbbe00)

~~~json
{
  "source": "00bbbe00",
  "target": "00bbbe58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbe04`](#insn-00bbbe04)

~~~json
{
  "source": "00bbbe04",
  "target": "00bbbe58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbe0c`](#insn-00bbbe0c)

~~~json
{
  "source": "00bbbe0c",
  "target": "00c57f60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbe18`](#insn-00bbbe18)

~~~json
{
  "source": "00bbbe18",
  "target": "00c5aed0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbe24`](#insn-00bbbe24)

~~~json
{
  "source": "00bbbe24",
  "target": "00bbd4fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbe28`](#insn-00bbbe28)

~~~json
{
  "source": "00bbbe28",
  "target": "0030e801",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0030e801",
  "offset": 0,
  "size": 10,
  "datatype": "string",
  "bytes": "4d6573736167696e6700",
  "capture_start": "0030e801",
  "capture_bytes": 10,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbbe38`](#insn-00bbbe38)

~~~json
{
  "source": "00bbbe38",
  "target": "00c5b010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbe40`](#insn-00bbbe40)

~~~json
{
  "source": "00bbbe40",
  "target": "00c5b030",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbe70`](#insn-00bbbe70)

~~~json
{
  "source": "00bbbe70",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbe78`](#insn-00bbbe78)

~~~json
{
  "source": "00bbbe78",
  "target": "00bbbe94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbe7c`](#insn-00bbbe7c)

~~~json
{
  "source": "00bbbe7c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbe80`](#insn-00bbbe80)

~~~json
{
  "source": "00bbbe80",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbe84`](#insn-00bbbe84)

~~~json
{
  "source": "00bbbe84",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbe88`](#insn-00bbbe88)

~~~json
{
  "source": "00bbbe88",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbe94`](#insn-00bbbe94)

~~~json
{
  "source": "00bbbe94",
  "target": "00c57fb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
