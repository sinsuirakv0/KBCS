# 00bbccd0

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bbbcdc`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbb/00bbbcdc.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0079.md#compare-7722853f9e08a7f55e89940466ca005c)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbccd0",
  "name": "FUN_00bbccd0",
  "size": 444,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "02a50d351a11fa033bba2f60dca602fecd10ee815a78aaa70e491de35020412a",
  "source_text_sha256": "02a50d351a11fa033bba2f60dca602fecd10ee815a78aaa70e491de35020412a",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbccd0",
        "00bbce8b"
      ]
    ],
    "bytes_sha256": "b91d4aca64f7dcd73db800dc19e48dbb28044500285bb6083c0e19183e5c9df9",
    "instruction_count": 111,
    "instruction_bytes": 444,
    "body_bytes": 444,
    "indirect": 6,
    "unresolved": 6
  }
}
~~~

## 呼び出し元

- [00bbca00](../00bbc/00bbca00.md)
- [00bbe250](../00bbe/00bbe250.md)

## 呼び出し先

- [00497b94](../00497/00497b94.md)
- [00c58f30](../00c58/00c58f30.md)
- [00c58f50](../00c58/00c58f50.md)
- [00c58f80](../00c58/00c58f80.md)
- [00c5bb30](../00c5b/00c5bb30.md)
- [00c5be40](../00c5b/00c5be40.md)
- [00c5bea0](../00c5b/00c5bea0.md)
- [00c5bfe0](../00c5b/00c5bfe0.md)
- [00c5bff0](../00c5b/00c5bff0.md)
- [00c5c000](../00c5c/00c5c000.md)
- [00c5c120](../00c5c/00c5c120.md)
- [00c5c1d0](../00c5c/00c5c1d0.md)
- [00c5e310](../00c5e/00c5e310.md)

## 関連文字列（未確認候補）

~~~text
"Messaging"
"Unsubscribe from topic %s"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2399 bytes

~~~c

void FUN_00bbccd0(undefined8 param_1,undefined8 param_2)

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
  plVar4 = (long *)_ZNK8firebase3App9GetJNIEnvEv(DAT_01127420);
  uVar5 = (**(code **)(*plVar4 + 0x538))(plVar4,param_1);
                    /* try { // try from 00bbcd3c to 00cbcd47 has its CatchHandler @ 00bbd810 */
  lVar6 = FUN_00497b94(plVar4,DAT_01127458,DAT_01127390,uVar5);
  cVar3 = (**(code **)(*plVar4 + 0x720))(plVar4);
  if (cVar3 == '\0') {
    if (lVar6 != 0) {
      uVar7 = _Znwm(0x10);
      _ZN8firebase12FutureHandleC1ERKS0_(uVar7,param_2);
      _ZN8firebase4util22RegisterCallbackOnTaskEP7_JNIEnvP8_jobjectPFvS2_S4_NS0_12FutureResultEPKcPvES8_S7_
                (plVar4,lVar6,FUN_00bbe4f0,uVar7,"Messaging");
                    /* try { // try from 00bbce30 to 00cbcecf has its CatchHandler @ 00bbd82c */
      _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar4);
      (**(code **)(*plVar4 + 0xb8))(plVar4,lVar6);
    }
  }
  else {
    uVar7 = (**(code **)(*plVar4 + 0x78))(plVar4);
                    /* try { // try from 00bbcd84 to 00cbcd8f has its CatchHandler @ 00bbd814 */
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
                    /* try { // try from 00bbcde8 to 00cbcdf3 has its CatchHandler @ 00bbd80c */
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
<a id="insn-00bbccd0"></a> `00bbccd0` | `ff 03 02 d1` | sub sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00bbccd4"></a> `00bbccd4` | `f8 5f 04 a9` | stp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bbccd8"></a> `00bbccd8` | `f6 57 05 a9` | stp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bbccdc"></a> `00bbccdc` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bbcce0"></a> `00bbcce0` | `fd 7b 07 a9` | stp x29,x30,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bbcce4"></a> `00bbcce4` | `fd c3 01 91` | add x29,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00bbcce8"></a> `00bbcce8` | `58 d0 3b d5` | mrs x24,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00bbccec"></a> `00bbccec` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00bbccf0"></a> `00bbccf0` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bbccf4"></a> `00bbccf4` | `20 b8 ff 90` | adrp x0,0x2c0000 | `FALL_THROUGH`
<a id="insn-00bbccf8"></a> `00bbccf8` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-00bbccfc"></a> `00bbccfc` | `00 74 30 91` | add x0,x0,#0xc1d | `FALL_THROUGH`
<a id="insn-00bbcd00"></a> `00bbcd00` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bbcd04"></a> `00bbcd04` | `e8 1f 00 f9` | str x8,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00bbcd08"></a> `00bbcd08` | `32 7d 02 94` | bl 0x00c5c1d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbcd0c"></a> `00bbcd0c` | `48 2b 00 f0` | adrp x8,0x1127000 | `FALL_THROUGH`
<a id="insn-00bbcd10"></a> `00bbcd10` | `00 11 42 f9` | ldr x0,[x8, #0x420] | `FALL_THROUGH`
<a id="insn-00bbcd14"></a> `00bbcd14` | `03 7d 02 94` | bl 0x00c5c120 | `UNCONDITIONAL_CALL`
<a id="insn-00bbcd18"></a> `00bbcd18` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bbcd1c"></a> `00bbcd1c` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bbcd20"></a> `00bbcd20` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bbcd24"></a> `00bbcd24` | `08 9d 42 f9` | ldr x8,[x8, #0x538] | `FALL_THROUGH`
<a id="insn-00bbcd28"></a> `00bbcd28` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bbcd2c"></a> `00bbcd2c` | `48 2b 00 f0` | adrp x8,0x1127000 | `FALL_THROUGH`
<a id="insn-00bbcd30"></a> `00bbcd30` | `49 2b 00 f0` | adrp x9,0x1127000 | `FALL_THROUGH`
<a id="insn-00bbcd34"></a> `00bbcd34` | `01 2d 42 f9` | ldr x1,[x8, #0x458] | `FALL_THROUGH`
<a id="insn-00bbcd38"></a> `00bbcd38` | `22 c9 41 f9` | ldr x2,[x9, #0x390] | `FALL_THROUGH`
<a id="insn-00bbcd3c"></a> `00bbcd3c` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bbcd40"></a> `00bbcd40` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbcd44"></a> `00bbcd44` | `e3 03 14 aa` | mov x3,x20 | `FALL_THROUGH`
<a id="insn-00bbcd48"></a> `00bbcd48` | `93 6b e3 97` | bl 0x00497b94 | `UNCONDITIONAL_CALL`
<a id="insn-00bbcd4c"></a> `00bbcd4c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbcd50"></a> `00bbcd50` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bbcd54"></a> `00bbcd54` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbcd58"></a> `00bbcd58` | `08 91 43 f9` | ldr x8,[x8, #0x720] | `FALL_THROUGH`
<a id="insn-00bbcd5c"></a> `00bbcd5c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bbcd60"></a> `00bbcd60` | `1f 1c 00 72` | tst w0,#0xff | `FALL_THROUGH`
<a id="insn-00bbcd64"></a> `00bbcd64` | `a0 04 00 54` | b.eq 0x00bbcdf8 | `CONDITIONAL_JUMP`
<a id="insn-00bbcd68"></a> `00bbcd68` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbcd6c"></a> `00bbcd6c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbcd70"></a> `00bbcd70` | `08 3d 40 f9` | ldr x8,[x8, #0x78] | `FALL_THROUGH`
<a id="insn-00bbcd74"></a> `00bbcd74` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bbcd78"></a> `00bbcd78` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbcd7c"></a> `00bbcd7c` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bbcd80"></a> `00bbcd80` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbcd84"></a> `00bbcd84` | `08 45 40 f9` | ldr x8,[x8, #0x88] | `FALL_THROUGH`
<a id="insn-00bbcd88"></a> `00bbcd88` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bbcd8c"></a> `00bbcd8c` | `e8 63 00 91` | add x8,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bbcd90"></a> `00bbcd90` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbcd94"></a> `00bbcd94` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bbcd98"></a> `00bbcd98` | `96 7c 02 94` | bl 0x00c5bff0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbcd9c"></a> `00bbcd9c` | `5d 85 02 94` | bl 0x00c5e310 | `UNCONDITIONAL_CALL`
<a id="insn-00bbcda0"></a> `00bbcda0` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bbcda4"></a> `00bbcda4` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bbcda8"></a> `00bbcda8` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bbcdac"></a> `00bbcdac` | `3d 7c 02 94` | bl 0x00c5bea0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbcdb0"></a> `00bbcdb0` | `e8 63 40 39` | ldrb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bbcdb4"></a> `00bbcdb4` | `e9 17 40 f9` | ldr x9,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00bbcdb8"></a> `00bbcdb8` | `ea 63 00 91` | add x10,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bbcdbc"></a> `00bbcdbc` | `4a 01 40 b2` | orr x10,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bbcdc0"></a> `00bbcdc0` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbcdc4"></a> `00bbcdc4` | `43 01 89 9a` | csel x3,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00bbcdc8"></a> `00bbcdc8` | `e1 23 00 91` | add x1,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bbcdcc"></a> `00bbcdcc` | `e4 c3 00 91` | add x4,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bbcdd0"></a> `00bbcdd0` | `42 00 80 52` | mov w2,#0x2 | `FALL_THROUGH`
<a id="insn-00bbcdd4"></a> `00bbcdd4` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bbcdd8"></a> `00bbcdd8` | `1a 7c 02 94` | bl 0x00c5be40 | `UNCONDITIONAL_CALL`
<a id="insn-00bbcddc"></a> `00bbcddc` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bbcde0"></a> `00bbcde0` | `54 7b 02 94` | bl 0x00c5bb30 | `UNCONDITIONAL_CALL`
<a id="insn-00bbcde4"></a> `00bbcde4` | `e8 63 40 39` | ldrb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bbcde8"></a> `00bbcde8` | `28 03 00 36` | tbz w8,#0x0,0x00bbce4c | `CONDITIONAL_JUMP`
<a id="insn-00bbcdec"></a> `00bbcdec` | `e0 17 40 f9` | ldr x0,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00bbcdf0"></a> `00bbcdf0` | `58 70 02 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00bbcdf4"></a> `00bbcdf4` | `16 00 00 14` | b 0x00bbce4c | `UNCONDITIONAL_JUMP`
<a id="insn-00bbcdf8"></a> `00bbcdf8` | `b6 02 00 b4` | cbz x22,0x00bbce4c | `CONDITIONAL_JUMP`
<a id="insn-00bbcdfc"></a> `00bbcdfc` | `00 02 80 52` | mov w0,#0x10 | `FALL_THROUGH`
<a id="insn-00bbce00"></a> `00bbce00` | `4c 70 02 94` | bl 0x00c58f30 | `UNCONDITIONAL_CALL`
<a id="insn-00bbce04"></a> `00bbce04` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00bbce08"></a> `00bbce08` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bbce0c"></a> `00bbce0c` | `25 7c 02 94` | bl 0x00c5bea0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbce10"></a> `00bbce10` | `02 00 00 d0` | adrp x2,0xbbe000 | `FALL_THROUGH`
<a id="insn-00bbce14"></a> `00bbce14` | `84 ba ff d0` | adrp x4,0x30e000 | `FALL_THROUGH`
<a id="insn-00bbce18"></a> `00bbce18` | `42 c0 13 91` | add x2,x2,#0x4f0 | `FALL_THROUGH`
<a id="insn-00bbce1c"></a> `00bbce1c` | `84 04 21 91` | add x4,x4,#0x841 | `FALL_THROUGH`
<a id="insn-00bbce20"></a> `00bbce20` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbce24"></a> `00bbce24` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bbce28"></a> `00bbce28` | `e3 03 17 aa` | mov x3,x23 | `FALL_THROUGH`
<a id="insn-00bbce2c"></a> `00bbce2c` | `6d 7c 02 94` | bl 0x00c5bfe0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbce30"></a> `00bbce30` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbce34"></a> `00bbce34` | `73 7c 02 94` | bl 0x00c5c000 | `UNCONDITIONAL_CALL`
<a id="insn-00bbce38"></a> `00bbce38` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbce3c"></a> `00bbce3c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbce40"></a> `00bbce40` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bbce44"></a> `00bbce44` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bbce48"></a> `00bbce48` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bbce4c"></a> `00bbce4c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbce50"></a> `00bbce50` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbce54"></a> `00bbce54` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bbce58"></a> `00bbce58` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bbce5c"></a> `00bbce5c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bbce60"></a> `00bbce60` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00bbce64"></a> `00bbce64` | `e9 1f 40 f9` | ldr x9,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00bbce68"></a> `00bbce68` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bbce6c"></a> `00bbce6c` | `e1 00 00 54` | b.ne 0x00bbce88 | `CONDITIONAL_JUMP`
<a id="insn-00bbce70"></a> `00bbce70` | `fd 7b 47 a9` | ldp x29,x30,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bbce74"></a> `00bbce74` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bbce78"></a> `00bbce78` | `f6 57 45 a9` | ldp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bbce7c"></a> `00bbce7c` | `f8 5f 44 a9` | ldp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bbce80"></a> `00bbce80` | `ff 03 02 91` | add sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00bbce84"></a> `00bbce84` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bbce88"></a> `00bbce88` | `3e 70 02 94` | bl 0x00c58f80 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbccd0`](#insn-00bbccd0) 範囲 `[['00bbccd0', '00bbcd3b']]`
  - `FALL_THROUGH` [`00bbcd38`](#insn-00bbcd38) → [`00bbcd3c`](#insn-00bbcd3c)
- ブロック [`00bbcd3c`](#insn-00bbcd3c) 範囲 `[['00bbcd3c', '00bbcd67']]`
  - `CONDITIONAL_JUMP` [`00bbcd64`](#insn-00bbcd64) → [`00bbcdf8`](#insn-00bbcdf8)
  - `FALL_THROUGH` [`00bbcd64`](#insn-00bbcd64) → [`00bbcd68`](#insn-00bbcd68)
- ブロック [`00bbcd68`](#insn-00bbcd68) 範囲 `[['00bbcd68', '00bbcd83']]`
  - `FALL_THROUGH` [`00bbcd80`](#insn-00bbcd80) → [`00bbcd84`](#insn-00bbcd84)
- ブロック [`00bbcd84`](#insn-00bbcd84) 範囲 `[['00bbcd84', '00bbcde7']]`
  - `FALL_THROUGH` [`00bbcde4`](#insn-00bbcde4) → [`00bbcde8`](#insn-00bbcde8)
- ブロック [`00bbcde8`](#insn-00bbcde8) 範囲 `[['00bbcde8', '00bbcdeb']]`
  - `CONDITIONAL_JUMP` [`00bbcde8`](#insn-00bbcde8) → [`00bbce4c`](#insn-00bbce4c)
  - `FALL_THROUGH` [`00bbcde8`](#insn-00bbcde8) → [`00bbcdec`](#insn-00bbcdec)
- ブロック [`00bbcdec`](#insn-00bbcdec) 範囲 `[['00bbcdec', '00bbcdf7']]`
  - `UNCONDITIONAL_JUMP` [`00bbcdf4`](#insn-00bbcdf4) → [`00bbce4c`](#insn-00bbce4c)
- ブロック [`00bbcdf8`](#insn-00bbcdf8) 範囲 `[['00bbcdf8', '00bbcdfb']]`
  - `CONDITIONAL_JUMP` [`00bbcdf8`](#insn-00bbcdf8) → [`00bbce4c`](#insn-00bbce4c)
  - `FALL_THROUGH` [`00bbcdf8`](#insn-00bbcdf8) → [`00bbcdfc`](#insn-00bbcdfc)
- ブロック [`00bbcdfc`](#insn-00bbcdfc) 範囲 `[['00bbcdfc', '00bbce2f']]`
  - `FALL_THROUGH` [`00bbce2c`](#insn-00bbce2c) → [`00bbce30`](#insn-00bbce30)
- ブロック [`00bbce30`](#insn-00bbce30) 範囲 `[['00bbce30', '00bbce4b']]`
  - `FALL_THROUGH` [`00bbce48`](#insn-00bbce48) → [`00bbce4c`](#insn-00bbce4c)
- ブロック [`00bbce4c`](#insn-00bbce4c) 範囲 `[['00bbce4c', '00bbce6f']]`
  - `CONDITIONAL_JUMP` [`00bbce6c`](#insn-00bbce6c) → [`00bbce88`](#insn-00bbce88)
  - `FALL_THROUGH` [`00bbce6c`](#insn-00bbce6c) → [`00bbce70`](#insn-00bbce70)
- ブロック [`00bbce70`](#insn-00bbce70) 範囲 `[['00bbce70', '00bbce87']]`
- ブロック [`00bbce88`](#insn-00bbce88) 範囲 `[['00bbce88', '00bbce8b']]`

## 命令位置別の参照

- [`00bbccd4`](#insn-00bbccd4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbccd8`](#insn-00bbccd8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbccdc`](#insn-00bbccdc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcce0`](#insn-00bbcce0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbccfc`](#insn-00bbccfc) → `002c0c1d`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbcd04`](#insn-00bbcd04) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcd08`](#insn-00bbcd08) → [`00c5c1d0`](../00c5c/00c5c1d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c1d0` · 推定シンボル `None` · 推定型 `None`
- [`00bbcd10`](#insn-00bbcd10) → `01127420`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbcd14`](#insn-00bbcd14) → [`00c5c120`](../00c5c/00c5c120.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c120` · 推定シンボル `None` · 推定型 `None`
- [`00bbcd34`](#insn-00bbcd34) → `01127458`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbcd38`](#insn-00bbcd38) → `01127390`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbcd48`](#insn-00bbcd48) → [`00497b94`](../00497/00497b94.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00497b94` · 推定シンボル `None` · 推定型 `None`
- [`00bbcd64`](#insn-00bbcd64) → [`00bbcdf8`](#insn-00bbcdf8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcd98`](#insn-00bbcd98) → [`00c5bff0`](../00c5b/00c5bff0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bff0` · 推定シンボル `None` · 推定型 `None`
- [`00bbcd9c`](#insn-00bbcd9c) → [`00c5e310`](../00c5e/00c5e310.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e310` · 推定シンボル `None` · 推定型 `None`
- [`00bbcdac`](#insn-00bbcdac) → [`00c5bea0`](../00c5b/00c5bea0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bea0` · 推定シンボル `None` · 推定型 `None`
- [`00bbcdb0`](#insn-00bbcdb0) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcdb4`](#insn-00bbcdb4) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcdd8`](#insn-00bbcdd8) → [`00c5be40`](../00c5b/00c5be40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5be40` · 推定シンボル `None` · 推定型 `None`
- [`00bbcde0`](#insn-00bbcde0) → [`00c5bb30`](../00c5b/00c5bb30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bb30` · 推定シンボル `None` · 推定型 `None`
- [`00bbcde4`](#insn-00bbcde4) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcde8`](#insn-00bbcde8) → [`00bbce4c`](#insn-00bbce4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcdec`](#insn-00bbcdec) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcdf0`](#insn-00bbcdf0) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00bbcdf4`](#insn-00bbcdf4) → [`00bbce4c`](#insn-00bbce4c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcdf8`](#insn-00bbcdf8) → [`00bbce4c`](#insn-00bbce4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbce00`](#insn-00bbce00) → [`00c58f30`](../00c58/00c58f30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f30` · 推定シンボル `None` · 推定型 `None`
- [`00bbce0c`](#insn-00bbce0c) → [`00c5bea0`](../00c5b/00c5bea0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bea0` · 推定シンボル `None` · 推定型 `None`
- [`00bbce18`](#insn-00bbce18) → [`00bbe4f0`](../00bbe/00bbe4f0.md) · `PARAM` · `ANALYSIS` · 関数 `00bbe4f0` · 推定シンボル `None` · 推定型 `None`
- [`00bbce1c`](#insn-00bbce1c) → `0030e841`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbce2c`](#insn-00bbce2c) → [`00c5bfe0`](../00c5b/00c5bfe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bfe0` · 推定シンボル `None` · 推定型 `None`
- [`00bbce34`](#insn-00bbce34) → [`00c5c000`](../00c5c/00c5c000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c000` · 推定シンボル `None` · 推定型 `None`
- [`00bbce64`](#insn-00bbce64) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbce6c`](#insn-00bbce6c) → [`00bbce88`](#insn-00bbce88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbce70`](#insn-00bbce70) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbce74`](#insn-00bbce74) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbce78`](#insn-00bbce78) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbce7c`](#insn-00bbce7c) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbce88`](#insn-00bbce88) → [`00c58f80`](../00c58/00c58f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f80` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbccd4`](#insn-00bbccd4)

~~~json
{
  "source": "00bbccd4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbccd8`](#insn-00bbccd8)

~~~json
{
  "source": "00bbccd8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbccdc`](#insn-00bbccdc)

~~~json
{
  "source": "00bbccdc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcce0`](#insn-00bbcce0)

~~~json
{
  "source": "00bbcce0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbccfc`](#insn-00bbccfc)

~~~json
{
  "source": "00bbccfc",
  "target": "002c0c1d",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002c0c1d",
  "offset": 0,
  "size": 26,
  "datatype": "string",
  "bytes": "556e7375627363726962652066726f6d20746f70696320257300",
  "capture_start": "002c0c1d",
  "capture_bytes": 26,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbcd04`](#insn-00bbcd04)

~~~json
{
  "source": "00bbcd04",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcd08`](#insn-00bbcd08)

~~~json
{
  "source": "00bbcd08",
  "target": "00c5c1d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbcd10`](#insn-00bbcd10)

~~~json
{
  "source": "00bbcd10",
  "target": "01127420",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127420",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbcd14`](#insn-00bbcd14)

~~~json
{
  "source": "00bbcd14",
  "target": "00c5c120",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbcd34`](#insn-00bbcd34)

~~~json
{
  "source": "00bbcd34",
  "target": "01127458",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127458",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbcd38`](#insn-00bbcd38)

~~~json
{
  "source": "00bbcd38",
  "target": "01127390",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127390",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbcd48`](#insn-00bbcd48)

~~~json
{
  "source": "00bbcd48",
  "target": "00497b94",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbcd64`](#insn-00bbcd64)

~~~json
{
  "source": "00bbcd64",
  "target": "00bbcdf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcd98`](#insn-00bbcd98)

~~~json
{
  "source": "00bbcd98",
  "target": "00c5bff0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbcd9c`](#insn-00bbcd9c)

~~~json
{
  "source": "00bbcd9c",
  "target": "00c5e310",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbcdac`](#insn-00bbcdac)

~~~json
{
  "source": "00bbcdac",
  "target": "00c5bea0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbcdb0`](#insn-00bbcdb0)

~~~json
{
  "source": "00bbcdb0",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcdb4`](#insn-00bbcdb4)

~~~json
{
  "source": "00bbcdb4",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcdd8`](#insn-00bbcdd8)

~~~json
{
  "source": "00bbcdd8",
  "target": "00c5be40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbcde0`](#insn-00bbcde0)

~~~json
{
  "source": "00bbcde0",
  "target": "00c5bb30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbcde4`](#insn-00bbcde4)

~~~json
{
  "source": "00bbcde4",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcde8`](#insn-00bbcde8)

~~~json
{
  "source": "00bbcde8",
  "target": "00bbce4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcdec`](#insn-00bbcdec)

~~~json
{
  "source": "00bbcdec",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcdf0`](#insn-00bbcdf0)

~~~json
{
  "source": "00bbcdf0",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbcdf4`](#insn-00bbcdf4)

~~~json
{
  "source": "00bbcdf4",
  "target": "00bbce4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcdf8`](#insn-00bbcdf8)

~~~json
{
  "source": "00bbcdf8",
  "target": "00bbce4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbce00`](#insn-00bbce00)

~~~json
{
  "source": "00bbce00",
  "target": "00c58f30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbce0c`](#insn-00bbce0c)

~~~json
{
  "source": "00bbce0c",
  "target": "00c5bea0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbce18`](#insn-00bbce18)

~~~json
{
  "source": "00bbce18",
  "target": "00bbe4f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbce1c`](#insn-00bbce1c)

~~~json
{
  "source": "00bbce1c",
  "target": "0030e841",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0030e841",
  "offset": 0,
  "size": 10,
  "datatype": "string",
  "bytes": "4d6573736167696e6700",
  "capture_start": "0030e841",
  "capture_bytes": 10,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbce2c`](#insn-00bbce2c)

~~~json
{
  "source": "00bbce2c",
  "target": "00c5bfe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbce34`](#insn-00bbce34)

~~~json
{
  "source": "00bbce34",
  "target": "00c5c000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbce64`](#insn-00bbce64)

~~~json
{
  "source": "00bbce64",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbce6c`](#insn-00bbce6c)

~~~json
{
  "source": "00bbce6c",
  "target": "00bbce88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbce70`](#insn-00bbce70)

~~~json
{
  "source": "00bbce70",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbce74`](#insn-00bbce74)

~~~json
{
  "source": "00bbce74",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbce78`](#insn-00bbce78)

~~~json
{
  "source": "00bbce78",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbce7c`](#insn-00bbce7c)

~~~json
{
  "source": "00bbce7c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbce88`](#insn-00bbce88)

~~~json
{
  "source": "00bbce88",
  "target": "00c58f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
