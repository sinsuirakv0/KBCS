# 00aed9ec

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00aed950`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aed/00aed950.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0065.md#compare-a05d00e6ac3fd063525c7708cbf5b05e)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00aee9e0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aee/00aee9e0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0067.md#compare-0c3db88a67dd5e4d5bdf149cfacc8434)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aed9ec",
  "name": "FUN_00aed9ec",
  "size": 804,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1fb529ae8bd58bd7578171f288bdcc580b5732c83eb290e6e0721fb59bb1d58a",
  "source_text_sha256": "1fb529ae8bd58bd7578171f288bdcc580b5732c83eb290e6e0721fb59bb1d58a",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aed9ec",
        "00aedd0b"
      ],
      [
        "00aeddac",
        "00aeddaf"
      ]
    ],
    "bytes_sha256": "3666a08ecc10fa309a3c2ffd6b0b82dc52fa1f2c2bf37c53f2c773159936f7d1",
    "instruction_count": 201,
    "instruction_bytes": 804,
    "body_bytes": 804,
    "indirect": 2,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00447f34](../00447/00447f34.md)
- [0047ad34](../0047a/0047ad34.md)
- [0047ce14](../0047c/0047ce14.md)
- [00489f8c](../00489/00489f8c.md)
- [0048ce94](../0048c/0048ce94.md)
- [00851550](../00851/00851550.md)
- [008b96fc](../008b9/008b96fc.md)
- [008b97d4](../008b9/008b97d4.md)
- [008b97f8](../008b9/008b97f8.md)
- [008b98b0](../008b9/008b98b0.md)
- [008bb144](../008bb/008bb144.md)
- [008bb568](../008bb/008bb568.md)
- [00aede74](../00aed/00aede74.md)
- [00aede78](../00aed/00aede78.md)
- [00aeec84](../00aee/00aeec84.md)
- [00aeec88](../00aee/00aeec88.md)
- [00c57f80](../00c57/00c57f80.md)
- [00c57fb0](../00c57/00c57fb0.md)
- [00c586e0](../00c58/00c586e0.md)

## 関連文字列（未確認候補）

~~~text
"slot_copy_select"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 6639 bytes

~~~c

void FUN_00aed9ec(long param_1,undefined8 param_2,int *param_3)

{
  int iVar1;
  long lVar2;
  undefined8 uVar3;
  long lVar4;
  long lVar5;
  undefined ***pppuVar6;
  undefined8 uVar7;
  long lVar8;
  byte local_d0;
  char local_cf [8];
  undefined7 uStack_c7;
  char cStack_c0;
  undefined1 uStack_bf;
  undefined6 uStack_be;
  byte local_b8 [16];
  void *local_a8;
  undefined **local_a0;
  long lStack_98;
  void *local_90;
  undefined ***local_80;
  undefined **local_70;
  long lStack_68;
  undefined ***local_50;
  long local_38;
  
  lVar2 = tpidr_el0;
  local_38 = *(long *)(lVar2 + 0x28);
  iVar1 = *param_3;
  if (iVar1 == 4) {
    lVar8 = *(long *)(param_1 + 8);
    uStack_bf = 0;
    local_d0 = 0x20;
    uStack_c7 = (undefined7)s_slot_copy_select_0029f825._8_8_;
    cStack_c0 = SUB81(s_slot_copy_select_0029f825._8_8_,7);
    local_cf = (char  [8])s_slot_copy_select_0029f825._0_8_;
                    /* try { // try from 00aeda94 to 00beda97 has its CatchHandler @ 00aedb1c */
    FUN_0048ce94(local_b8,&local_d0);
    lVar4 = FUN_00851550();
                    /* try { // try from 00aedaa8 to 00bedaab has its CatchHandler @ 00aedad0 */
                    /* try { // try from 00aedabc to 00bedabf has its CatchHandler @ 00aedac8 */
    FUN_00447f34(&local_a0,local_b8,0,*(int *)(BYTE_ARRAY_0039b979 + lVar4 + 3) + 1);
                    /* catch() { ... } // from try @ 00aed928 with catch @ 00aedac0
                       try { // try from 00aedac0 to 00bedb8f has its CatchHandler @ 00aed60c */
                    /* catch() { ... } // from try @ 00aed8bc with catch @ 00aedac4 */
                    /* catch() { ... } // from try @ 00aed974 with catch @ 00aedac8
                       catch() { ... } // from try @ 00aedabc with catch @ 00aedac8 */
    local_50 = &local_70;
                    /* catch() { ... } // from try @ 00aed74c with catch @ 00aedacc */
                    /* catch() { ... } // from try @ 00aed908 with catch @ 00aedad0
                       catch() { ... } // from try @ 00aedaa8 with catch @ 00aedad0 */
    local_70 = &PTR_FUN_00c8dd38;
    lStack_68 = lVar8;
                    /* catch() { ... } // from try @ 00aed714 with catch @ 00aedae8 */
                    /* catch() { ... } // from try @ 00aed6c8 with catch @ 00aedaec */
    uVar3 = FUN_008bb144(lVar8 + 0x2f08,&local_a0,0,0,0x5c,&local_70);
    FUN_008b98b0(uVar3,0xfffffffe);
                    /* catch() { ... } // from try @ 00aed6bc with catch @ 00aedafc */
    if (local_50 == &local_70) {
      lVar4 = 0x20;
                    /* catch() { ... } // from try @ 00aed898 with catch @ 00aedb1c
                       catch() { ... } // from try @ 00aeda94 with catch @ 00aedb1c */
      pppuVar6 = &local_70;
LAB_00aedb20:
                    /* catch() { ... } // from try @ 00aed684 with catch @ 00aedb20 */
      (**(code **)((long)*pppuVar6 + lVar4))();
    }
    else {
                    /* catch() { ... } // from try @ 00aed84c with catch @ 00aedb0c */
      if (local_50 != (undefined ***)0x0) {
        lVar4 = 0x28;
        pppuVar6 = local_50;
                    /* catch() { ... } // from try @ 00aed6b0 with catch @ 00aedb14 */
        goto LAB_00aedb20;
      }
    }
    if (((byte)local_a0 & 1) != 0) {
      _ZdlPv(local_90);
    }
    if ((local_b8[0] & 1) != 0) {
      _ZdlPv(local_a8);
    }
                    /* catch() { ... } // from try @ 00aed808 with catch @ 00aedb40 */
    if ((local_d0 & 1) != 0) {
                    /* catch() { ... } // from try @ 00aed7e4 with catch @ 00aedb44 */
      _ZdlPv((void *)CONCAT62(uStack_be,CONCAT11(uStack_bf,cStack_c0)));
    }
    lVar4 = FUN_00851550();
                    /* catch() { ... } // from try @ 00aed7b4 with catch @ 00aedb60 */
    if ((*(int *)((long)&fde_table_entry_00333b98.data_loc + lVar4) < 2) &&
       (lVar4 = FUN_00851550(), (*(byte *)(lVar4 + 0x33a5) & 1) == 0)) {
      uVar3 = FUN_008bb568(lVar8 + 0x2f08);
      FUN_008b97f8(uVar3,1,0);
    }
    FUN_00851550();
    lVar4 = FUN_00851550();
                    /* catch() { ... } // from try @ 00aedcdc with catch @ 00aedb90
                       catch() { ... } // from try @ 00aede38 with catch @ 00aedb90
                       catch() { ... } // from try @ 00aedee4 with catch @ 00aedb90 */
    lVar5 = FUN_00851550();
    lVar4 = lVar4 + (long)*(int *)(BYTE_ARRAY_0039b979 + lVar5 + 3) * 0x2c;
                    /* try { // try from 00aedbf0 to 00bedbf7 has its CatchHandler @ 00aedefc */
    if ((int)((uint)(*(byte *)(lVar4 + 0xc5e2) ^ *(byte *)(lVar4 + 0xc5ba)) << 0x10 |
              (uint)(*(byte *)(lVar4 + 0xc5e3) ^ *(byte *)(lVar4 + 0xc5bb)) << 0x18 |
              (uint)(*(byte *)(lVar4 + 0xc5e1) ^ *(byte *)(lVar4 + 0xc5b9)) << 8 |
             (uint)(*(byte *)(lVar4 + 0xc5e0) ^ *(byte *)(lVar4 + 0xc5b8))) < 2) {
      uVar3 = FUN_008bb568(lVar8 + 0x2f08);
      FUN_008b97f8(uVar3,0,0);
    }
    if (DAT_00ca4a78 == 0) {
      lVar4 = 0;
    }
    else {
                    /* try { // try from 00aedc34 to 00bedc83 has its CatchHandler @ 00aedf08 */
      lVar4 = __dynamic_cast(DAT_00ca4a78,&PTR__ZTVN10__cxxabiv117__class_type_infoE_16__00c65f28,
                             &PTR__ZTVN10__cxxabiv120__si_class_type_infoE_16__00c8da20,0);
    }
    uVar3 = FUN_008bb568(lVar8 + 0x2f08);
    lVar4 = FUN_00489f8c(*(undefined8 *)(lVar4 + 0x118),0x2b);
    FUN_008b97d4(uVar3,1,*(int *)(lVar4 + 8) + 0x1e);
    uVar3 = FUN_008bb568(lVar8 + 0x2f08);
    local_a0 = &PTR_FUN_00c8df38;
    lStack_98 = lVar8;
    local_80 = &local_a0;
    FUN_008b96fc(uVar3,&local_a0);
    if (local_80 == &local_a0) {
      lVar4 = 0x20;
      pppuVar6 = &local_a0;
    }
    else {
      if (local_80 == (undefined ***)0x0) goto LAB_00aedce8;
      lVar4 = 0x28;
      pppuVar6 = local_80;
                    /* try { // try from 00aedcd0 to 00bedcdb has its CatchHandler @ 00aedee4 */
    }
                    /* try { // try from 00aedcdc to 00bede0b has its CatchHandler @ 00aedb90 */
    (**(code **)((long)*pppuVar6 + lVar4))();
  }
  else {
    if (iVar1 == 3) {
      uVar3 = FUN_0047ad34();
      if (*(long *)(lVar2 + 0x28) == local_38) {
        uVar7 = 0xb;
LAB_00aeda58:
        FUN_0047ce14(uVar3,uVar7,0);
        return;
      }
      goto LAB_00aeddac;
    }
    if (iVar1 == 0) {
      uVar3 = FUN_0047ad34();
      if (*(long *)(lVar2 + 0x28) == local_38) {
        uVar7 = 10;
        goto LAB_00aeda58;
      }
      goto LAB_00aeddac;
    }
  }
LAB_00aedce8:
  if (*(long *)(lVar2 + 0x28) == local_38) {
    return;
  }
LAB_00aeddac:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aed9ec"></a> `00aed9ec` | `ff 43 03 d1` | sub sp,sp,#0xd0 | `FALL_THROUGH`
<a id="insn-00aed9f0"></a> `00aed9f0` | `fd 7b 0a a9` | stp x29,x30,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00aed9f4"></a> `00aed9f4` | `f6 57 0b a9` | stp x22,x21,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00aed9f8"></a> `00aed9f8` | `f4 4f 0c a9` | stp x20,x19,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00aed9fc"></a> `00aed9fc` | `fd 83 02 91` | add x29,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-00aeda00"></a> `00aeda00` | `54 d0 3b d5` | mrs x20,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00aeda04"></a> `00aeda04` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00aeda08"></a> `00aeda08` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aeda0c"></a> `00aeda0c` | `48 00 40 b9` | ldr w8,[x2] | `FALL_THROUGH`
<a id="insn-00aeda10"></a> `00aeda10` | `1f 11 00 71` | cmp w8,#0x4 | `FALL_THROUGH`
<a id="insn-00aeda14"></a> `00aeda14` | `e0 02 00 54` | b.eq 0x00aeda70 | `CONDITIONAL_JUMP`
<a id="insn-00aeda18"></a> `00aeda18` | `1f 0d 00 71` | cmp w8,#0x3 | `FALL_THROUGH`
<a id="insn-00aeda1c"></a> `00aeda1c` | `20 01 00 54` | b.eq 0x00aeda40 | `CONDITIONAL_JUMP`
<a id="insn-00aeda20"></a> `00aeda20` | `48 16 00 35` | cbnz w8,0x00aedce8 | `CONDITIONAL_JUMP`
<a id="insn-00aeda24"></a> `00aeda24` | `c4 34 e6 97` | bl 0x0047ad34 | `UNCONDITIONAL_CALL`
<a id="insn-00aeda28"></a> `00aeda28` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00aeda2c"></a> `00aeda2c` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aeda30"></a> `00aeda30` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00aeda34"></a> `00aeda34` | `c1 1b 00 54` | b.ne 0x00aeddac | `CONDITIONAL_JUMP`
<a id="insn-00aeda38"></a> `00aeda38` | `41 01 80 52` | mov w1,#0xa | `FALL_THROUGH`
<a id="insn-00aeda3c"></a> `00aeda3c` | `07 00 00 14` | b 0x00aeda58 | `UNCONDITIONAL_JUMP`
<a id="insn-00aeda40"></a> `00aeda40` | `bd 34 e6 97` | bl 0x0047ad34 | `UNCONDITIONAL_CALL`
<a id="insn-00aeda44"></a> `00aeda44` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00aeda48"></a> `00aeda48` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aeda4c"></a> `00aeda4c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00aeda50"></a> `00aeda50` | `e1 1a 00 54` | b.ne 0x00aeddac | `CONDITIONAL_JUMP`
<a id="insn-00aeda54"></a> `00aeda54` | `61 01 80 52` | mov w1,#0xb | `FALL_THROUGH`
<a id="insn-00aeda58"></a> `00aeda58` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00aeda5c"></a> `00aeda5c` | `f4 4f 4c a9` | ldp x20,x19,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00aeda60"></a> `00aeda60` | `f6 57 4b a9` | ldp x22,x21,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00aeda64"></a> `00aeda64` | `fd 7b 4a a9` | ldp x29,x30,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00aeda68"></a> `00aeda68` | `ff 43 03 91` | add sp,sp,#0xd0 | `FALL_THROUGH`
<a id="insn-00aeda6c"></a> `00aeda6c` | `ea 3c e6 17` | b 0x0047ce14 | `CALL_TERMINATOR`
<a id="insn-00aeda70"></a> `00aeda70` | `89 bd ff d0` | adrp x9,0x29f000 | `FALL_THROUGH`
<a id="insn-00aeda74"></a> `00aeda74` | `29 95 20 91` | add x9,x9,#0x825 | `FALL_THROUGH`
<a id="insn-00aeda78"></a> `00aeda78` | `15 04 40 f9` | ldr x21,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00aeda7c"></a> `00aeda7c` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00aeda80"></a> `00aeda80` | `08 04 80 52` | mov w8,#0x20 | `FALL_THROUGH`
<a id="insn-00aeda84"></a> `00aeda84` | `ff 47 00 39` | strb wzr,[sp, #0x11] | `FALL_THROUGH`
<a id="insn-00aeda88"></a> `00aeda88` | `e8 03 00 39` | strb w8,[sp] | `FALL_THROUGH`
<a id="insn-00aeda8c"></a> `00aeda8c` | `e0 13 80 3c` | stur q0,[sp, #0x1] | `FALL_THROUGH`
<a id="insn-00aeda90"></a> `00aeda90` | `e8 63 00 91` | add x8,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00aeda94"></a> `00aeda94` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00aeda98"></a> `00aeda98` | `ff 7c e6 97` | bl 0x0048ce94 | `UNCONDITIONAL_CALL`
<a id="insn-00aeda9c"></a> `00aeda9c` | `ad 8e f5 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-00aedaa0"></a> `00aedaa0` | `88 2f 97 52` | mov w8,#0xb97c | `FALL_THROUGH`
<a id="insn-00aedaa4"></a> `00aedaa4` | `28 07 a0 72` | movk w8,#0x39, LSL #16 | `FALL_THROUGH`
<a id="insn-00aedaa8"></a> `00aedaa8` | `09 68 68 b8` | ldr w9,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00aedaac"></a> `00aedaac` | `e8 c3 00 91` | add x8,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00aedab0"></a> `00aedab0` | `e0 63 00 91` | add x0,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00aedab4"></a> `00aedab4` | `22 05 00 11` | add w2,w9,#0x1 | `FALL_THROUGH`
<a id="insn-00aedab8"></a> `00aedab8` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-00aedabc"></a> `00aedabc` | `1e 69 e5 97` | bl 0x00447f34 | `UNCONDITIONAL_CALL`
<a id="insn-00aedac0"></a> `00aedac0` | `08 0d 00 90` | adrp x8,0xc8d000 | `FALL_THROUGH`
<a id="insn-00aedac4"></a> `00aedac4` | `08 e1 34 91` | add x8,x8,#0xd38 | `FALL_THROUGH`
<a id="insn-00aedac8"></a> `00aedac8` | `b3 03 01 d1` | sub x19,x29,#0x40 | `FALL_THROUGH`
<a id="insn-00aedacc"></a> `00aedacc` | `16 e1 85 52` | mov w22,#0x2f08 | `FALL_THROUGH`
<a id="insn-00aedad0"></a> `00aedad0` | `a8 57 3c a9` | stp x8,x21,[x29, #-0x40] | `FALL_THROUGH`
<a id="insn-00aedad4"></a> `00aedad4` | `b3 03 1e f8` | stur x19,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00aedad8"></a> `00aedad8` | `a0 02 16 8b` | add x0,x21,x22 | `FALL_THROUGH`
<a id="insn-00aedadc"></a> `00aedadc` | `e1 c3 00 91` | add x1,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00aedae0"></a> `00aedae0` | `a5 03 01 d1` | sub x5,x29,#0x40 | `FALL_THROUGH`
<a id="insn-00aedae4"></a> `00aedae4` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-00aedae8"></a> `00aedae8` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-00aedaec"></a> `00aedaec` | `84 0b 80 52` | mov w4,#0x5c | `FALL_THROUGH`
<a id="insn-00aedaf0"></a> `00aedaf0` | `95 35 f7 97` | bl 0x008bb144 | `UNCONDITIONAL_CALL`
<a id="insn-00aedaf4"></a> `00aedaf4` | `21 00 80 12` | mov w1,#0xfffffffe | `FALL_THROUGH`
<a id="insn-00aedaf8"></a> `00aedaf8` | `6e 2f f7 97` | bl 0x008b98b0 | `UNCONDITIONAL_CALL`
<a id="insn-00aedafc"></a> `00aedafc` | `a0 03 5e f8` | ldur x0,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00aedb00"></a> `00aedb00` | `a8 03 01 d1` | sub x8,x29,#0x40 | `FALL_THROUGH`
<a id="insn-00aedb04"></a> `00aedb04` | `1f 00 08 eb` | cmp x0,x8 | `FALL_THROUGH`
<a id="insn-00aedb08"></a> `00aedb08` | `80 00 00 54` | b.eq 0x00aedb18 | `CONDITIONAL_JUMP`
<a id="insn-00aedb0c"></a> `00aedb0c` | `00 01 00 b4` | cbz x0,0x00aedb2c | `CONDITIONAL_JUMP`
<a id="insn-00aedb10"></a> `00aedb10` | `08 05 80 52` | mov w8,#0x28 | `FALL_THROUGH`
<a id="insn-00aedb14"></a> `00aedb14` | `03 00 00 14` | b 0x00aedb20 | `UNCONDITIONAL_JUMP`
<a id="insn-00aedb18"></a> `00aedb18` | `08 04 80 52` | mov w8,#0x20 | `FALL_THROUGH`
<a id="insn-00aedb1c"></a> `00aedb1c` | `a0 03 01 d1` | sub x0,x29,#0x40 | `FALL_THROUGH`
<a id="insn-00aedb20"></a> `00aedb20` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-00aedb24"></a> `00aedb24` | `28 69 68 f8` | ldr x8,[x9, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00aedb28"></a> `00aedb28` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aedb2c"></a> `00aedb2c` | `e8 c3 40 39` | ldrb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aedb30"></a> `00aedb30` | `88 08 00 37` | tbnz w8,#0x0,0x00aedc40 | `CONDITIONAL_JUMP`
<a id="insn-00aedb34"></a> `00aedb34` | `e8 63 40 39` | ldrb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00aedb38"></a> `00aedb38` | `c8 08 00 37` | tbnz w8,#0x0,0x00aedc50 | `CONDITIONAL_JUMP`
<a id="insn-00aedb3c"></a> `00aedb3c` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-00aedb40"></a> `00aedb40` | `68 00 00 36` | tbz w8,#0x0,0x00aedb4c | `CONDITIONAL_JUMP`
<a id="insn-00aedb44"></a> `00aedb44` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aedb48"></a> `00aedb48` | `0e a9 05 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00aedb4c"></a> `00aedb4c` | `81 8e f5 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-00aedb50"></a> `00aedb50` | `88 73 87 52` | mov w8,#0x3b9c | `FALL_THROUGH`
<a id="insn-00aedb54"></a> `00aedb54` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00aedb58"></a> `00aedb58` | `08 68 68 b8` | ldr w8,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00aedb5c"></a> `00aedb5c` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00aedb60"></a> `00aedb60` | `4c 01 00 54` | b.gt 0x00aedb88 | `CONDITIONAL_JUMP`
<a id="insn-00aedb64"></a> `00aedb64` | `7b 8e f5 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-00aedb68"></a> `00aedb68` | `a8 74 86 52` | mov w8,#0x33a5 | `FALL_THROUGH`
<a id="insn-00aedb6c"></a> `00aedb6c` | `08 68 68 38` | ldrb w8,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00aedb70"></a> `00aedb70` | `c8 00 00 37` | tbnz w8,#0x0,0x00aedb88 | `CONDITIONAL_JUMP`
<a id="insn-00aedb74"></a> `00aedb74` | `a0 02 16 8b` | add x0,x21,x22 | `FALL_THROUGH`
<a id="insn-00aedb78"></a> `00aedb78` | `7c 36 f7 97` | bl 0x008bb568 | `UNCONDITIONAL_CALL`
<a id="insn-00aedb7c"></a> `00aedb7c` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00aedb80"></a> `00aedb80` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-00aedb84"></a> `00aedb84` | `1d 2f f7 97` | bl 0x008b97f8 | `UNCONDITIONAL_CALL`
<a id="insn-00aedb88"></a> `00aedb88` | `72 8e f5 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-00aedb8c"></a> `00aedb8c` | `71 8e f5 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-00aedb90"></a> `00aedb90` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aedb94"></a> `00aedb94` | `6f 8e f5 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-00aedb98"></a> `00aedb98` | `88 2f 97 52` | mov w8,#0xb97c | `FALL_THROUGH`
<a id="insn-00aedb9c"></a> `00aedb9c` | `89 05 80 52` | mov w9,#0x2c | `FALL_THROUGH`
<a id="insn-00aedba0"></a> `00aedba0` | `28 07 a0 72` | movk w8,#0x39, LSL #16 | `FALL_THROUGH`
<a id="insn-00aedba4"></a> `00aedba4` | `08 68 a8 b8` | ldrsw x8,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00aedba8"></a> `00aedba8` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00aedbac"></a> `00aedbac` | `08 4d 29 9b` | smaddl x8,w8,w9,x19 | `FALL_THROUGH`
<a id="insn-00aedbb0"></a> `00aedbb0` | `09 b7 98 52` | mov w9,#0xc5b8 | `FALL_THROUGH`
<a id="insn-00aedbb4"></a> `00aedbb4` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00aedbb8"></a> `00aedbb8` | `09 09 40 39` | ldrb w9,[x8, #0x2] | `FALL_THROUGH`
<a id="insn-00aedbbc"></a> `00aedbbc` | `0a a9 40 39` | ldrb w10,[x8, #0x2a] | `FALL_THROUGH`
<a id="insn-00aedbc0"></a> `00aedbc0` | `0b ad 40 39` | ldrb w11,[x8, #0x2b] | `FALL_THROUGH`
<a id="insn-00aedbc4"></a> `00aedbc4` | `0c 05 40 39` | ldrb w12,[x8, #0x1] | `FALL_THROUGH`
<a id="insn-00aedbc8"></a> `00aedbc8` | `49 01 09 4a` | eor w9,w10,w9 | `FALL_THROUGH`
<a id="insn-00aedbcc"></a> `00aedbcc` | `0a 0d 40 39` | ldrb w10,[x8, #0x3] | `FALL_THROUGH`
<a id="insn-00aedbd0"></a> `00aedbd0` | `29 3d 10 53` | lsl w9,w9,#0x10 | `FALL_THROUGH`
<a id="insn-00aedbd4"></a> `00aedbd4` | `6a 01 0a 4a` | eor w10,w11,w10 | `FALL_THROUGH`
<a id="insn-00aedbd8"></a> `00aedbd8` | `0b a5 40 39` | ldrb w11,[x8, #0x29] | `FALL_THROUGH`
<a id="insn-00aedbdc"></a> `00aedbdc` | `29 61 0a 2a` | orr w9,w9,w10, LSL #0x18 | `FALL_THROUGH`
<a id="insn-00aedbe0"></a> `00aedbe0` | `0a 01 40 39` | ldrb w10,[x8] | `FALL_THROUGH`
<a id="insn-00aedbe4"></a> `00aedbe4` | `08 a1 40 39` | ldrb w8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00aedbe8"></a> `00aedbe8` | `6b 01 0c 4a` | eor w11,w11,w12 | `FALL_THROUGH`
<a id="insn-00aedbec"></a> `00aedbec` | `29 21 0b 2a` | orr w9,w9,w11, LSL #0x8 | `FALL_THROUGH`
<a id="insn-00aedbf0"></a> `00aedbf0` | `08 01 0a 4a` | eor w8,w8,w10 | `FALL_THROUGH`
<a id="insn-00aedbf4"></a> `00aedbf4` | `28 01 08 2a` | orr w8,w9,w8 | `FALL_THROUGH`
<a id="insn-00aedbf8"></a> `00aedbf8` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00aedbfc"></a> `00aedbfc` | `cc 00 00 54` | b.gt 0x00aedc14 | `CONDITIONAL_JUMP`
<a id="insn-00aedc00"></a> `00aedc00` | `a0 02 16 8b` | add x0,x21,x22 | `FALL_THROUGH`
<a id="insn-00aedc04"></a> `00aedc04` | `59 36 f7 97` | bl 0x008bb568 | `UNCONDITIONAL_CALL`
<a id="insn-00aedc08"></a> `00aedc08` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aedc0c"></a> `00aedc0c` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-00aedc10"></a> `00aedc10` | `fa 2e f7 97` | bl 0x008b97f8 | `UNCONDITIONAL_CALL`
<a id="insn-00aedc14"></a> `00aedc14` | `a8 0d 00 f0` | adrp x8,0xca4000 | `FALL_THROUGH`
<a id="insn-00aedc18"></a> `00aedc18` | `00 3d 45 f9` | ldr x0,[x8, #0xa78] | `FALL_THROUGH`
<a id="insn-00aedc1c"></a> `00aedc1c` | `40 02 00 b4` | cbz x0,0x00aedc64 | `CONDITIONAL_JUMP`
<a id="insn-00aedc20"></a> `00aedc20` | `c1 0b 00 90` | adrp x1,0xc65000 | `FALL_THROUGH`
<a id="insn-00aedc24"></a> `00aedc24` | `21 a0 3c 91` | add x1,x1,#0xf28 | `FALL_THROUGH`
<a id="insn-00aedc28"></a> `00aedc28` | `02 0d 00 90` | adrp x2,0xc8d000 | `FALL_THROUGH`
<a id="insn-00aedc2c"></a> `00aedc2c` | `42 80 28 91` | add x2,x2,#0xa20 | `FALL_THROUGH`
<a id="insn-00aedc30"></a> `00aedc30` | `e3 03 1f aa` | mov x3,xzr | `FALL_THROUGH`
<a id="insn-00aedc34"></a> `00aedc34` | `ab aa 05 94` | bl 0x00c586e0 | `UNCONDITIONAL_CALL`
<a id="insn-00aedc38"></a> `00aedc38` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aedc3c"></a> `00aedc3c` | `0b 00 00 14` | b 0x00aedc68 | `UNCONDITIONAL_JUMP`
<a id="insn-00aedc40"></a> `00aedc40` | `e0 23 40 f9` | ldr x0,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00aedc44"></a> `00aedc44` | `cf a8 05 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00aedc48"></a> `00aedc48` | `e8 63 40 39` | ldrb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00aedc4c"></a> `00aedc4c` | `88 f7 07 36` | tbz w8,#0x0,0x00aedb3c | `CONDITIONAL_JUMP`
<a id="insn-00aedc50"></a> `00aedc50` | `e0 17 40 f9` | ldr x0,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00aedc54"></a> `00aedc54` | `cb a8 05 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00aedc58"></a> `00aedc58` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-00aedc5c"></a> `00aedc5c` | `48 f7 07 37` | tbnz w8,#0x0,0x00aedb44 | `CONDITIONAL_JUMP`
<a id="insn-00aedc60"></a> `00aedc60` | `bb ff ff 17` | b 0x00aedb4c | `UNCONDITIONAL_JUMP`
<a id="insn-00aedc64"></a> `00aedc64` | `f3 03 1f aa` | mov x19,xzr | `FALL_THROUGH`
<a id="insn-00aedc68"></a> `00aedc68` | `a0 02 16 8b` | add x0,x21,x22 | `FALL_THROUGH`
<a id="insn-00aedc6c"></a> `00aedc6c` | `3f 36 f7 97` | bl 0x008bb568 | `UNCONDITIONAL_CALL`
<a id="insn-00aedc70"></a> `00aedc70` | `68 8e 40 f9` | ldr x8,[x19, #0x118] | `FALL_THROUGH`
<a id="insn-00aedc74"></a> `00aedc74` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aedc78"></a> `00aedc78` | `61 05 80 52` | mov w1,#0x2b | `FALL_THROUGH`
<a id="insn-00aedc7c"></a> `00aedc7c` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00aedc80"></a> `00aedc80` | `c3 70 e6 97` | bl 0x00489f8c | `UNCONDITIONAL_CALL`
<a id="insn-00aedc84"></a> `00aedc84` | `08 08 40 b9` | ldr w8,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00aedc88"></a> `00aedc88` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aedc8c"></a> `00aedc8c` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00aedc90"></a> `00aedc90` | `02 79 00 11` | add w2,w8,#0x1e | `FALL_THROUGH`
<a id="insn-00aedc94"></a> `00aedc94` | `d0 2e f7 97` | bl 0x008b97d4 | `UNCONDITIONAL_CALL`
<a id="insn-00aedc98"></a> `00aedc98` | `a0 02 16 8b` | add x0,x21,x22 | `FALL_THROUGH`
<a id="insn-00aedc9c"></a> `00aedc9c` | `33 36 f7 97` | bl 0x008bb568 | `UNCONDITIONAL_CALL`
<a id="insn-00aedca0"></a> `00aedca0` | `08 0d 00 90` | adrp x8,0xc8d000 | `FALL_THROUGH`
<a id="insn-00aedca4"></a> `00aedca4` | `08 e1 3c 91` | add x8,x8,#0xf38 | `FALL_THROUGH`
<a id="insn-00aedca8"></a> `00aedca8` | `f3 c3 00 91` | add x19,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00aedcac"></a> `00aedcac` | `e8 57 03 a9` | stp x8,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aedcb0"></a> `00aedcb0` | `f3 2b 00 f9` | str x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00aedcb4"></a> `00aedcb4` | `e1 c3 00 91` | add x1,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00aedcb8"></a> `00aedcb8` | `91 2e f7 97` | bl 0x008b96fc | `UNCONDITIONAL_CALL`
<a id="insn-00aedcbc"></a> `00aedcbc` | `e0 2b 40 f9` | ldr x0,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00aedcc0"></a> `00aedcc0` | `1f 00 13 eb` | cmp x0,x19 | `FALL_THROUGH`
<a id="insn-00aedcc4"></a> `00aedcc4` | `80 00 00 54` | b.eq 0x00aedcd4 | `CONDITIONAL_JUMP`
<a id="insn-00aedcc8"></a> `00aedcc8` | `00 01 00 b4` | cbz x0,0x00aedce8 | `CONDITIONAL_JUMP`
<a id="insn-00aedccc"></a> `00aedccc` | `08 05 80 52` | mov w8,#0x28 | `FALL_THROUGH`
<a id="insn-00aedcd0"></a> `00aedcd0` | `03 00 00 14` | b 0x00aedcdc | `UNCONDITIONAL_JUMP`
<a id="insn-00aedcd4"></a> `00aedcd4` | `08 04 80 52` | mov w8,#0x20 | `FALL_THROUGH`
<a id="insn-00aedcd8"></a> `00aedcd8` | `e0 c3 00 91` | add x0,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00aedcdc"></a> `00aedcdc` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-00aedce0"></a> `00aedce0` | `28 69 68 f8` | ldr x8,[x9, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00aedce4"></a> `00aedce4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aedce8"></a> `00aedce8` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00aedcec"></a> `00aedcec` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aedcf0"></a> `00aedcf0` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00aedcf4"></a> `00aedcf4` | `c1 05 00 54` | b.ne 0x00aeddac | `CONDITIONAL_JUMP`
<a id="insn-00aedcf8"></a> `00aedcf8` | `f4 4f 4c a9` | ldp x20,x19,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00aedcfc"></a> `00aedcfc` | `f6 57 4b a9` | ldp x22,x21,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00aedd00"></a> `00aedd00` | `fd 7b 4a a9` | ldp x29,x30,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00aedd04"></a> `00aedd04` | `ff 43 03 91` | add sp,sp,#0xd0 | `FALL_THROUGH`
<a id="insn-00aedd08"></a> `00aedd08` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00aeddac"></a> `00aeddac` | `81 a8 05 94` | bl 0x00c57fb0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aed9ec`](#insn-00aed9ec) 範囲 `[['00aed9ec', '00aeda17']]`
  - `CONDITIONAL_JUMP` [`00aeda14`](#insn-00aeda14) → [`00aeda70`](#insn-00aeda70)
  - `FALL_THROUGH` [`00aeda14`](#insn-00aeda14) → [`00aeda18`](#insn-00aeda18)
- ブロック [`00aeda18`](#insn-00aeda18) 範囲 `[['00aeda18', '00aeda1f']]`
  - `CONDITIONAL_JUMP` [`00aeda1c`](#insn-00aeda1c) → [`00aeda40`](#insn-00aeda40)
  - `FALL_THROUGH` [`00aeda1c`](#insn-00aeda1c) → [`00aeda20`](#insn-00aeda20)
- ブロック [`00aeda20`](#insn-00aeda20) 範囲 `[['00aeda20', '00aeda23']]`
  - `CONDITIONAL_JUMP` [`00aeda20`](#insn-00aeda20) → [`00aedce8`](#insn-00aedce8)
  - `FALL_THROUGH` [`00aeda20`](#insn-00aeda20) → [`00aeda24`](#insn-00aeda24)
- ブロック [`00aeda24`](#insn-00aeda24) 範囲 `[['00aeda24', '00aeda37']]`
  - `CONDITIONAL_JUMP` [`00aeda34`](#insn-00aeda34) → [`00aeddac`](#insn-00aeddac)
  - `FALL_THROUGH` [`00aeda34`](#insn-00aeda34) → [`00aeda38`](#insn-00aeda38)
- ブロック [`00aeda38`](#insn-00aeda38) 範囲 `[['00aeda38', '00aeda3f']]`
  - `UNCONDITIONAL_JUMP` [`00aeda3c`](#insn-00aeda3c) → [`00aeda58`](#insn-00aeda58)
- ブロック [`00aeda40`](#insn-00aeda40) 範囲 `[['00aeda40', '00aeda53']]`
  - `CONDITIONAL_JUMP` [`00aeda50`](#insn-00aeda50) → [`00aeddac`](#insn-00aeddac)
  - `FALL_THROUGH` [`00aeda50`](#insn-00aeda50) → [`00aeda54`](#insn-00aeda54)
- ブロック [`00aeda54`](#insn-00aeda54) 範囲 `[['00aeda54', '00aeda57']]`
  - `FALL_THROUGH` [`00aeda54`](#insn-00aeda54) → [`00aeda58`](#insn-00aeda58)
- ブロック [`00aeda58`](#insn-00aeda58) 範囲 `[['00aeda58', '00aeda6f']]`
- ブロック [`00aeda70`](#insn-00aeda70) 範囲 `[['00aeda70', '00aeda93']]`
  - `FALL_THROUGH` [`00aeda90`](#insn-00aeda90) → [`00aeda94`](#insn-00aeda94)
- ブロック [`00aeda94`](#insn-00aeda94) 範囲 `[['00aeda94', '00aedaa7']]`
  - `FALL_THROUGH` [`00aedaa4`](#insn-00aedaa4) → [`00aedaa8`](#insn-00aedaa8)
- ブロック [`00aedaa8`](#insn-00aedaa8) 範囲 `[['00aedaa8', '00aedabb']]`
  - `FALL_THROUGH` [`00aedab8`](#insn-00aedab8) → [`00aedabc`](#insn-00aedabc)
- ブロック [`00aedabc`](#insn-00aedabc) 範囲 `[['00aedabc', '00aedabf']]`
  - `FALL_THROUGH` [`00aedabc`](#insn-00aedabc) → [`00aedac0`](#insn-00aedac0)
- ブロック [`00aedac0`](#insn-00aedac0) 範囲 `[['00aedac0', '00aedac3']]`
  - `FALL_THROUGH` [`00aedac0`](#insn-00aedac0) → [`00aedac4`](#insn-00aedac4)
- ブロック [`00aedac4`](#insn-00aedac4) 範囲 `[['00aedac4', '00aedac7']]`
  - `FALL_THROUGH` [`00aedac4`](#insn-00aedac4) → [`00aedac8`](#insn-00aedac8)
- ブロック [`00aedac8`](#insn-00aedac8) 範囲 `[['00aedac8', '00aedacb']]`
  - `FALL_THROUGH` [`00aedac8`](#insn-00aedac8) → [`00aedacc`](#insn-00aedacc)
- ブロック [`00aedacc`](#insn-00aedacc) 範囲 `[['00aedacc', '00aedacf']]`
  - `FALL_THROUGH` [`00aedacc`](#insn-00aedacc) → [`00aedad0`](#insn-00aedad0)
- ブロック [`00aedad0`](#insn-00aedad0) 範囲 `[['00aedad0', '00aedae7']]`
  - `FALL_THROUGH` [`00aedae4`](#insn-00aedae4) → [`00aedae8`](#insn-00aedae8)
- ブロック [`00aedae8`](#insn-00aedae8) 範囲 `[['00aedae8', '00aedaeb']]`
  - `FALL_THROUGH` [`00aedae8`](#insn-00aedae8) → [`00aedaec`](#insn-00aedaec)
- ブロック [`00aedaec`](#insn-00aedaec) 範囲 `[['00aedaec', '00aedafb']]`
  - `FALL_THROUGH` [`00aedaf8`](#insn-00aedaf8) → [`00aedafc`](#insn-00aedafc)
- ブロック [`00aedafc`](#insn-00aedafc) 範囲 `[['00aedafc', '00aedb0b']]`
  - `CONDITIONAL_JUMP` [`00aedb08`](#insn-00aedb08) → [`00aedb18`](#insn-00aedb18)
  - `FALL_THROUGH` [`00aedb08`](#insn-00aedb08) → [`00aedb0c`](#insn-00aedb0c)
- ブロック [`00aedb0c`](#insn-00aedb0c) 範囲 `[['00aedb0c', '00aedb0f']]`
  - `CONDITIONAL_JUMP` [`00aedb0c`](#insn-00aedb0c) → [`00aedb2c`](#insn-00aedb2c)
  - `FALL_THROUGH` [`00aedb0c`](#insn-00aedb0c) → [`00aedb10`](#insn-00aedb10)
- ブロック [`00aedb10`](#insn-00aedb10) 範囲 `[['00aedb10', '00aedb13']]`
  - `FALL_THROUGH` [`00aedb10`](#insn-00aedb10) → [`00aedb14`](#insn-00aedb14)
- ブロック [`00aedb14`](#insn-00aedb14) 範囲 `[['00aedb14', '00aedb17']]`
  - `UNCONDITIONAL_JUMP` [`00aedb14`](#insn-00aedb14) → [`00aedb20`](#insn-00aedb20)
- ブロック [`00aedb18`](#insn-00aedb18) 範囲 `[['00aedb18', '00aedb1b']]`
  - `FALL_THROUGH` [`00aedb18`](#insn-00aedb18) → [`00aedb1c`](#insn-00aedb1c)
- ブロック [`00aedb1c`](#insn-00aedb1c) 範囲 `[['00aedb1c', '00aedb1f']]`
  - `FALL_THROUGH` [`00aedb1c`](#insn-00aedb1c) → [`00aedb20`](#insn-00aedb20)
- ブロック [`00aedb20`](#insn-00aedb20) 範囲 `[['00aedb20', '00aedb2b']]`
  - `FALL_THROUGH` [`00aedb28`](#insn-00aedb28) → [`00aedb2c`](#insn-00aedb2c)
- ブロック [`00aedb2c`](#insn-00aedb2c) 範囲 `[['00aedb2c', '00aedb33']]`
  - `CONDITIONAL_JUMP` [`00aedb30`](#insn-00aedb30) → [`00aedc40`](#insn-00aedc40)
  - `FALL_THROUGH` [`00aedb30`](#insn-00aedb30) → [`00aedb34`](#insn-00aedb34)
- ブロック [`00aedb34`](#insn-00aedb34) 範囲 `[['00aedb34', '00aedb37']]`
  - `FALL_THROUGH` [`00aedb34`](#insn-00aedb34) → [`00aedb38`](#insn-00aedb38)
- ブロック [`00aedb38`](#insn-00aedb38) 範囲 `[['00aedb38', '00aedb3b']]`
  - `CONDITIONAL_JUMP` [`00aedb38`](#insn-00aedb38) → [`00aedc50`](#insn-00aedc50)
  - `FALL_THROUGH` [`00aedb38`](#insn-00aedb38) → [`00aedb3c`](#insn-00aedb3c)
- ブロック [`00aedb3c`](#insn-00aedb3c) 範囲 `[['00aedb3c', '00aedb3f']]`
  - `FALL_THROUGH` [`00aedb3c`](#insn-00aedb3c) → [`00aedb40`](#insn-00aedb40)
- ブロック [`00aedb40`](#insn-00aedb40) 範囲 `[['00aedb40', '00aedb43']]`
  - `CONDITIONAL_JUMP` [`00aedb40`](#insn-00aedb40) → [`00aedb4c`](#insn-00aedb4c)
  - `FALL_THROUGH` [`00aedb40`](#insn-00aedb40) → [`00aedb44`](#insn-00aedb44)
- ブロック [`00aedb44`](#insn-00aedb44) 範囲 `[['00aedb44', '00aedb4b']]`
  - `FALL_THROUGH` [`00aedb48`](#insn-00aedb48) → [`00aedb4c`](#insn-00aedb4c)
- ブロック [`00aedb4c`](#insn-00aedb4c) 範囲 `[['00aedb4c', '00aedb5f']]`
  - `FALL_THROUGH` [`00aedb5c`](#insn-00aedb5c) → [`00aedb60`](#insn-00aedb60)
- ブロック [`00aedb60`](#insn-00aedb60) 範囲 `[['00aedb60', '00aedb63']]`
  - `CONDITIONAL_JUMP` [`00aedb60`](#insn-00aedb60) → [`00aedb88`](#insn-00aedb88)
  - `FALL_THROUGH` [`00aedb60`](#insn-00aedb60) → [`00aedb64`](#insn-00aedb64)
- ブロック [`00aedb64`](#insn-00aedb64) 範囲 `[['00aedb64', '00aedb73']]`
  - `CONDITIONAL_JUMP` [`00aedb70`](#insn-00aedb70) → [`00aedb88`](#insn-00aedb88)
  - `FALL_THROUGH` [`00aedb70`](#insn-00aedb70) → [`00aedb74`](#insn-00aedb74)
- ブロック [`00aedb74`](#insn-00aedb74) 範囲 `[['00aedb74', '00aedb87']]`
  - `FALL_THROUGH` [`00aedb84`](#insn-00aedb84) → [`00aedb88`](#insn-00aedb88)
- ブロック [`00aedb88`](#insn-00aedb88) 範囲 `[['00aedb88', '00aedb8f']]`
  - `FALL_THROUGH` [`00aedb8c`](#insn-00aedb8c) → [`00aedb90`](#insn-00aedb90)
- ブロック [`00aedb90`](#insn-00aedb90) 範囲 `[['00aedb90', '00aedbef']]`
  - `FALL_THROUGH` [`00aedbec`](#insn-00aedbec) → [`00aedbf0`](#insn-00aedbf0)
- ブロック [`00aedbf0`](#insn-00aedbf0) 範囲 `[['00aedbf0', '00aedbff']]`
  - `CONDITIONAL_JUMP` [`00aedbfc`](#insn-00aedbfc) → [`00aedc14`](#insn-00aedc14)
  - `FALL_THROUGH` [`00aedbfc`](#insn-00aedbfc) → [`00aedc00`](#insn-00aedc00)
- ブロック [`00aedc00`](#insn-00aedc00) 範囲 `[['00aedc00', '00aedc13']]`
  - `FALL_THROUGH` [`00aedc10`](#insn-00aedc10) → [`00aedc14`](#insn-00aedc14)
- ブロック [`00aedc14`](#insn-00aedc14) 範囲 `[['00aedc14', '00aedc1f']]`
  - `CONDITIONAL_JUMP` [`00aedc1c`](#insn-00aedc1c) → [`00aedc64`](#insn-00aedc64)
  - `FALL_THROUGH` [`00aedc1c`](#insn-00aedc1c) → [`00aedc20`](#insn-00aedc20)
- ブロック [`00aedc20`](#insn-00aedc20) 範囲 `[['00aedc20', '00aedc33']]`
  - `FALL_THROUGH` [`00aedc30`](#insn-00aedc30) → [`00aedc34`](#insn-00aedc34)
- ブロック [`00aedc34`](#insn-00aedc34) 範囲 `[['00aedc34', '00aedc3f']]`
  - `UNCONDITIONAL_JUMP` [`00aedc3c`](#insn-00aedc3c) → [`00aedc68`](#insn-00aedc68)
- ブロック [`00aedc40`](#insn-00aedc40) 範囲 `[['00aedc40', '00aedc4f']]`
  - `CONDITIONAL_JUMP` [`00aedc4c`](#insn-00aedc4c) → [`00aedb3c`](#insn-00aedb3c)
  - `FALL_THROUGH` [`00aedc4c`](#insn-00aedc4c) → [`00aedc50`](#insn-00aedc50)
- ブロック [`00aedc50`](#insn-00aedc50) 範囲 `[['00aedc50', '00aedc5f']]`
  - `CONDITIONAL_JUMP` [`00aedc5c`](#insn-00aedc5c) → [`00aedb44`](#insn-00aedb44)
  - `FALL_THROUGH` [`00aedc5c`](#insn-00aedc5c) → [`00aedc60`](#insn-00aedc60)
- ブロック [`00aedc60`](#insn-00aedc60) 範囲 `[['00aedc60', '00aedc63']]`
  - `UNCONDITIONAL_JUMP` [`00aedc60`](#insn-00aedc60) → [`00aedb4c`](#insn-00aedb4c)
- ブロック [`00aedc64`](#insn-00aedc64) 範囲 `[['00aedc64', '00aedc67']]`
  - `FALL_THROUGH` [`00aedc64`](#insn-00aedc64) → [`00aedc68`](#insn-00aedc68)
- ブロック [`00aedc68`](#insn-00aedc68) 範囲 `[['00aedc68', '00aedcc7']]`
  - `CONDITIONAL_JUMP` [`00aedcc4`](#insn-00aedcc4) → [`00aedcd4`](#insn-00aedcd4)
  - `FALL_THROUGH` [`00aedcc4`](#insn-00aedcc4) → [`00aedcc8`](#insn-00aedcc8)
- ブロック [`00aedcc8`](#insn-00aedcc8) 範囲 `[['00aedcc8', '00aedccb']]`
  - `CONDITIONAL_JUMP` [`00aedcc8`](#insn-00aedcc8) → [`00aedce8`](#insn-00aedce8)
  - `FALL_THROUGH` [`00aedcc8`](#insn-00aedcc8) → [`00aedccc`](#insn-00aedccc)
- ブロック [`00aedccc`](#insn-00aedccc) 範囲 `[['00aedccc', '00aedccf']]`
  - `FALL_THROUGH` [`00aedccc`](#insn-00aedccc) → [`00aedcd0`](#insn-00aedcd0)
- ブロック [`00aedcd0`](#insn-00aedcd0) 範囲 `[['00aedcd0', '00aedcd3']]`
  - `UNCONDITIONAL_JUMP` [`00aedcd0`](#insn-00aedcd0) → [`00aedcdc`](#insn-00aedcdc)
- ブロック [`00aedcd4`](#insn-00aedcd4) 範囲 `[['00aedcd4', '00aedcdb']]`
  - `FALL_THROUGH` [`00aedcd8`](#insn-00aedcd8) → [`00aedcdc`](#insn-00aedcdc)
- ブロック [`00aedcdc`](#insn-00aedcdc) 範囲 `[['00aedcdc', '00aedce7']]`
  - `FALL_THROUGH` [`00aedce4`](#insn-00aedce4) → [`00aedce8`](#insn-00aedce8)
- ブロック [`00aedce8`](#insn-00aedce8) 範囲 `[['00aedce8', '00aedcf7']]`
  - `CONDITIONAL_JUMP` [`00aedcf4`](#insn-00aedcf4) → [`00aeddac`](#insn-00aeddac)
  - `FALL_THROUGH` [`00aedcf4`](#insn-00aedcf4) → [`00aedcf8`](#insn-00aedcf8)
- ブロック [`00aedcf8`](#insn-00aedcf8) 範囲 `[['00aedcf8', '00aedd0b']]`
- ブロック [`00aeddac`](#insn-00aeddac) 範囲 `[['00aeddac', '00aeddaf']]`

## 命令位置別の参照

- [`00aed9f0`](#insn-00aed9f0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aed9f4`](#insn-00aed9f4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aed9f8`](#insn-00aed9f8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeda08`](#insn-00aeda08) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeda14`](#insn-00aeda14) → [`00aeda70`](#insn-00aeda70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeda1c`](#insn-00aeda1c) → [`00aeda40`](#insn-00aeda40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeda20`](#insn-00aeda20) → [`00aedce8`](#insn-00aedce8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeda24`](#insn-00aeda24) → [`0047ad34`](../0047a/0047ad34.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047ad34` · 推定シンボル `None` · 推定型 `None`
- [`00aeda2c`](#insn-00aeda2c) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeda34`](#insn-00aeda34) → [`00aeddac`](#insn-00aeddac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeda3c`](#insn-00aeda3c) → [`00aeda58`](#insn-00aeda58) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeda40`](#insn-00aeda40) → [`0047ad34`](../0047a/0047ad34.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047ad34` · 推定シンボル `None` · 推定型 `None`
- [`00aeda48`](#insn-00aeda48) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeda50`](#insn-00aeda50) → [`00aeddac`](#insn-00aeddac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeda5c`](#insn-00aeda5c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeda60`](#insn-00aeda60) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeda64`](#insn-00aeda64) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeda6c`](#insn-00aeda6c) → [`0047ce14`](../0047c/0047ce14.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047ce14` · 推定シンボル `None` · 推定型 `None`
- [`00aeda7c`](#insn-00aeda7c) → `0029f825`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aeda84`](#insn-00aeda84) → `Stack[-0xbf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeda88`](#insn-00aeda88) → `Stack[-0xd0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeda8c`](#insn-00aeda8c) → `Stack[-0xcf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeda98`](#insn-00aeda98) → [`0048ce94`](../0048c/0048ce94.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0048ce94` · 推定シンボル `None` · 推定型 `None`
- [`00aeda9c`](#insn-00aeda9c) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`00aedaa8`](#insn-00aedaa8) → `0039b97c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[23]`
- [`00aedabc`](#insn-00aedabc) → [`00447f34`](../00447/00447f34.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00447f34` · 推定シンボル `None` · 推定型 `None`
- [`00aedad0`](#insn-00aedad0) → `00c8dd38`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00aedad0`](#insn-00aedad0) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedad4`](#insn-00aedad4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedaf0`](#insn-00aedaf0) → [`008bb144`](../008bb/008bb144.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008bb144` · 推定シンボル `None` · 推定型 `None`
- [`00aedaf8`](#insn-00aedaf8) → [`008b98b0`](../008b9/008b98b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b98b0` · 推定シンボル `None` · 推定型 `None`
- [`00aedafc`](#insn-00aedafc) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedb08`](#insn-00aedb08) → [`00aedb18`](#insn-00aedb18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedb0c`](#insn-00aedb0c) → [`00aedb2c`](#insn-00aedb2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedb14`](#insn-00aedb14) → [`00aedb20`](#insn-00aedb20) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedb20`](#insn-00aedb20) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedb24`](#insn-00aedb24) → `00c8dd58`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00aedb24`](#insn-00aedb24) → `00c8dd60`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00aedb28`](#insn-00aedb28) → [`00aede74`](00aede74.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00aede74` · 推定シンボル `None` · 推定型 `None`
- [`00aedb28`](#insn-00aedb28) → [`00aede78`](00aede78.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00aede78` · 推定シンボル `None` · 推定型 `None`
- [`00aedb2c`](#insn-00aedb2c) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedb30`](#insn-00aedb30) → [`00aedc40`](#insn-00aedc40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedb34`](#insn-00aedb34) → `Stack[-0xb8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedb38`](#insn-00aedb38) → [`00aedc50`](#insn-00aedc50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedb3c`](#insn-00aedb3c) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedb40`](#insn-00aedb40) → [`00aedb4c`](#insn-00aedb4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedb44`](#insn-00aedb44) → `Stack[-0xc0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedb48`](#insn-00aedb48) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00aedb4c`](#insn-00aedb4c) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`00aedb58`](#insn-00aedb58) → `00333b9c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00aedb60`](#insn-00aedb60) → [`00aedb88`](#insn-00aedb88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedb64`](#insn-00aedb64) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`00aedb70`](#insn-00aedb70) → [`00aedb88`](#insn-00aedb88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedb78`](#insn-00aedb78) → [`008bb568`](../008bb/008bb568.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008bb568` · 推定シンボル `None` · 推定型 `None`
- [`00aedb84`](#insn-00aedb84) → [`008b97f8`](../008b9/008b97f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b97f8` · 推定シンボル `None` · 推定型 `None`
- [`00aedb88`](#insn-00aedb88) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`00aedb8c`](#insn-00aedb8c) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`00aedb94`](#insn-00aedb94) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`00aedba4`](#insn-00aedba4) → `0039b97c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[23]`
- [`00aedbfc`](#insn-00aedbfc) → [`00aedc14`](#insn-00aedc14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedc04`](#insn-00aedc04) → [`008bb568`](../008bb/008bb568.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008bb568` · 推定シンボル `None` · 推定型 `None`
- [`00aedc10`](#insn-00aedc10) → [`008b97f8`](../008b9/008b97f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b97f8` · 推定シンボル `None` · 推定型 `None`
- [`00aedc18`](#insn-00aedc18) → `00ca4a78`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aedc1c`](#insn-00aedc1c) → [`00aedc64`](#insn-00aedc64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedc24`](#insn-00aedc24) → `00c65f28`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x10)))`
- [`00aedc2c`](#insn-00aedc2c) → `00c8da20`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x10)))`
- [`00aedc34`](#insn-00aedc34) → [`00c586e0`](../00c58/00c586e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c586e0` · 推定シンボル `None` · 推定型 `None`
- [`00aedc3c`](#insn-00aedc3c) → [`00aedc68`](#insn-00aedc68) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedc40`](#insn-00aedc40) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedc44`](#insn-00aedc44) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00aedc48`](#insn-00aedc48) → `Stack[-0xb8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedc4c`](#insn-00aedc4c) → [`00aedb3c`](#insn-00aedb3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedc50`](#insn-00aedc50) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedc54`](#insn-00aedc54) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00aedc58`](#insn-00aedc58) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedc5c`](#insn-00aedc5c) → [`00aedb44`](#insn-00aedb44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedc60`](#insn-00aedc60) → [`00aedb4c`](#insn-00aedb4c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedc6c`](#insn-00aedc6c) → [`008bb568`](../008bb/008bb568.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008bb568` · 推定シンボル `None` · 推定型 `None`
- [`00aedc80`](#insn-00aedc80) → [`00489f8c`](../00489/00489f8c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00489f8c` · 推定シンボル `None` · 推定型 `None`
- [`00aedc94`](#insn-00aedc94) → [`008b97d4`](../008b9/008b97d4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b97d4` · 推定シンボル `None` · 推定型 `None`
- [`00aedc9c`](#insn-00aedc9c) → [`008bb568`](../008bb/008bb568.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008bb568` · 推定シンボル `None` · 推定型 `None`
- [`00aedcac`](#insn-00aedcac) → `00c8df38`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00aedcac`](#insn-00aedcac) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedcb0`](#insn-00aedcb0) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedcb8`](#insn-00aedcb8) → [`008b96fc`](../008b9/008b96fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b96fc` · 推定シンボル `None` · 推定型 `None`
- [`00aedcbc`](#insn-00aedcbc) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedcc4`](#insn-00aedcc4) → [`00aedcd4`](#insn-00aedcd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedcc8`](#insn-00aedcc8) → [`00aedce8`](#insn-00aedce8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedcd0`](#insn-00aedcd0) → [`00aedcdc`](#insn-00aedcdc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedcdc`](#insn-00aedcdc) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedce0`](#insn-00aedce0) → `00c8df58`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00aedce0`](#insn-00aedce0) → `00c8df60`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00aedce4`](#insn-00aedce4) → [`00aeec84`](../00aee/00aeec84.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00aeec84` · 推定シンボル `None` · 推定型 `None`
- [`00aedce4`](#insn-00aedce4) → [`00aeec88`](../00aee/00aeec88.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00aeec88` · 推定シンボル `None` · 推定型 `None`
- [`00aedcec`](#insn-00aedcec) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedcf4`](#insn-00aedcf4) → [`00aeddac`](#insn-00aeddac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedcf8`](#insn-00aedcf8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedcfc`](#insn-00aedcfc) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedd00`](#insn-00aedd00) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeddac`](#insn-00aeddac) → [`00c57fb0`](../00c57/00c57fb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fb0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aed9f0`](#insn-00aed9f0)

~~~json
{
  "source": "00aed9f0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aed9f4`](#insn-00aed9f4)

~~~json
{
  "source": "00aed9f4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aed9f8`](#insn-00aed9f8)

~~~json
{
  "source": "00aed9f8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeda08`](#insn-00aeda08)

~~~json
{
  "source": "00aeda08",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeda14`](#insn-00aeda14)

~~~json
{
  "source": "00aeda14",
  "target": "00aeda70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeda1c`](#insn-00aeda1c)

~~~json
{
  "source": "00aeda1c",
  "target": "00aeda40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeda20`](#insn-00aeda20)

~~~json
{
  "source": "00aeda20",
  "target": "00aedce8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeda24`](#insn-00aeda24)

~~~json
{
  "source": "00aeda24",
  "target": "0047ad34",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeda2c`](#insn-00aeda2c)

~~~json
{
  "source": "00aeda2c",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeda34`](#insn-00aeda34)

~~~json
{
  "source": "00aeda34",
  "target": "00aeddac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeda3c`](#insn-00aeda3c)

~~~json
{
  "source": "00aeda3c",
  "target": "00aeda58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeda40`](#insn-00aeda40)

~~~json
{
  "source": "00aeda40",
  "target": "0047ad34",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeda48`](#insn-00aeda48)

~~~json
{
  "source": "00aeda48",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeda50`](#insn-00aeda50)

~~~json
{
  "source": "00aeda50",
  "target": "00aeddac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeda5c`](#insn-00aeda5c)

~~~json
{
  "source": "00aeda5c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeda60`](#insn-00aeda60)

~~~json
{
  "source": "00aeda60",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeda64`](#insn-00aeda64)

~~~json
{
  "source": "00aeda64",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeda6c`](#insn-00aeda6c)

~~~json
{
  "source": "00aeda6c",
  "target": "0047ce14",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeda7c`](#insn-00aeda7c)

~~~json
{
  "source": "00aeda7c",
  "target": "0029f825",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029f825",
  "offset": 0,
  "size": 17,
  "datatype": "string",
  "bytes": "736c6f745f636f70795f73656c65637400",
  "capture_start": "0029f825",
  "capture_bytes": 17,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aeda84`](#insn-00aeda84)

~~~json
{
  "source": "00aeda84",
  "target": "Stack[-0xbf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeda88`](#insn-00aeda88)

~~~json
{
  "source": "00aeda88",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeda8c`](#insn-00aeda8c)

~~~json
{
  "source": "00aeda8c",
  "target": "Stack[-0xcf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeda98`](#insn-00aeda98)

~~~json
{
  "source": "00aeda98",
  "target": "0048ce94",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeda9c`](#insn-00aeda9c)

~~~json
{
  "source": "00aeda9c",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aedaa8`](#insn-00aedaa8)

~~~json
{
  "source": "00aedaa8",
  "target": "0039b97c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0039b979",
  "offset": 3,
  "size": 23,
  "datatype": "byte[23]",
  "bytes": "440e10440c1d109e029d04540c1f10440e00dedd000000",
  "capture_start": "0039b979",
  "capture_bytes": 23,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aedabc`](#insn-00aedabc)

~~~json
{
  "source": "00aedabc",
  "target": "00447f34",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aedad0`](#insn-00aedad0)

~~~json
{
  "source": "00aedad0",
  "target": "00c8dd38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8dd38",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aedad0`](#insn-00aedad0)

~~~json
{
  "source": "00aedad0",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedad4`](#insn-00aedad4)

~~~json
{
  "source": "00aedad4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedaf0`](#insn-00aedaf0)

~~~json
{
  "source": "00aedaf0",
  "target": "008bb144",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aedaf8`](#insn-00aedaf8)

~~~json
{
  "source": "00aedaf8",
  "target": "008b98b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aedafc`](#insn-00aedafc)

~~~json
{
  "source": "00aedafc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedb08`](#insn-00aedb08)

~~~json
{
  "source": "00aedb08",
  "target": "00aedb18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedb0c`](#insn-00aedb0c)

~~~json
{
  "source": "00aedb0c",
  "target": "00aedb2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedb14`](#insn-00aedb14)

~~~json
{
  "source": "00aedb14",
  "target": "00aedb20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedb20`](#insn-00aedb20)

~~~json
{
  "source": "00aedb20",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedb24`](#insn-00aedb24)

~~~json
{
  "source": "00aedb24",
  "target": "00c8dd58",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8dd58",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aedb24`](#insn-00aedb24)

~~~json
{
  "source": "00aedb24",
  "target": "00c8dd60",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8dd60",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aedb28`](#insn-00aedb28)

~~~json
{
  "source": "00aedb28",
  "target": "00aede74",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aedb28`](#insn-00aedb28)

~~~json
{
  "source": "00aedb28",
  "target": "00aede78",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aedb2c`](#insn-00aedb2c)

~~~json
{
  "source": "00aedb2c",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedb30`](#insn-00aedb30)

~~~json
{
  "source": "00aedb30",
  "target": "00aedc40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedb34`](#insn-00aedb34)

~~~json
{
  "source": "00aedb34",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedb38`](#insn-00aedb38)

~~~json
{
  "source": "00aedb38",
  "target": "00aedc50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedb3c`](#insn-00aedb3c)

~~~json
{
  "source": "00aedb3c",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedb40`](#insn-00aedb40)

~~~json
{
  "source": "00aedb40",
  "target": "00aedb4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedb44`](#insn-00aedb44)

~~~json
{
  "source": "00aedb44",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedb48`](#insn-00aedb48)

~~~json
{
  "source": "00aedb48",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aedb4c`](#insn-00aedb4c)

~~~json
{
  "source": "00aedb4c",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aedb58`](#insn-00aedb58)

~~~json
{
  "source": "00aedb58",
  "target": "00333b9c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333b98",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "44cf6a001c7d0900",
  "capture_start": "00333b98",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aedb60`](#insn-00aedb60)

~~~json
{
  "source": "00aedb60",
  "target": "00aedb88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedb64`](#insn-00aedb64)

~~~json
{
  "source": "00aedb64",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aedb70`](#insn-00aedb70)

~~~json
{
  "source": "00aedb70",
  "target": "00aedb88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedb78`](#insn-00aedb78)

~~~json
{
  "source": "00aedb78",
  "target": "008bb568",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aedb84`](#insn-00aedb84)

~~~json
{
  "source": "00aedb84",
  "target": "008b97f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aedb88`](#insn-00aedb88)

~~~json
{
  "source": "00aedb88",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aedb8c`](#insn-00aedb8c)

~~~json
{
  "source": "00aedb8c",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aedb94`](#insn-00aedb94)

~~~json
{
  "source": "00aedb94",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aedba4`](#insn-00aedba4)

~~~json
{
  "source": "00aedba4",
  "target": "0039b97c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0039b979",
  "offset": 3,
  "size": 23,
  "datatype": "byte[23]",
  "bytes": "440e10440c1d109e029d04540c1f10440e00dedd000000",
  "capture_start": "0039b979",
  "capture_bytes": 23,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aedbfc`](#insn-00aedbfc)

~~~json
{
  "source": "00aedbfc",
  "target": "00aedc14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedc04`](#insn-00aedc04)

~~~json
{
  "source": "00aedc04",
  "target": "008bb568",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aedc10`](#insn-00aedc10)

~~~json
{
  "source": "00aedc10",
  "target": "008b97f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aedc18`](#insn-00aedc18)

~~~json
{
  "source": "00aedc18",
  "target": "00ca4a78",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4a78",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aedc1c`](#insn-00aedc1c)

~~~json
{
  "source": "00aedc1c",
  "target": "00aedc64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedc24`](#insn-00aedc24)

~~~json
{
  "source": "00aedc24",
  "target": "00c65f28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c65f28",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aedc2c`](#insn-00aedc2c)

~~~json
{
  "source": "00aedc2c",
  "target": "00c8da20",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8da20",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aedc34`](#insn-00aedc34)

~~~json
{
  "source": "00aedc34",
  "target": "00c586e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aedc3c`](#insn-00aedc3c)

~~~json
{
  "source": "00aedc3c",
  "target": "00aedc68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedc40`](#insn-00aedc40)

~~~json
{
  "source": "00aedc40",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedc44`](#insn-00aedc44)

~~~json
{
  "source": "00aedc44",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aedc48`](#insn-00aedc48)

~~~json
{
  "source": "00aedc48",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedc4c`](#insn-00aedc4c)

~~~json
{
  "source": "00aedc4c",
  "target": "00aedb3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedc50`](#insn-00aedc50)

~~~json
{
  "source": "00aedc50",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedc54`](#insn-00aedc54)

~~~json
{
  "source": "00aedc54",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aedc58`](#insn-00aedc58)

~~~json
{
  "source": "00aedc58",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedc5c`](#insn-00aedc5c)

~~~json
{
  "source": "00aedc5c",
  "target": "00aedb44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedc60`](#insn-00aedc60)

~~~json
{
  "source": "00aedc60",
  "target": "00aedb4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedc6c`](#insn-00aedc6c)

~~~json
{
  "source": "00aedc6c",
  "target": "008bb568",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aedc80`](#insn-00aedc80)

~~~json
{
  "source": "00aedc80",
  "target": "00489f8c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aedc94`](#insn-00aedc94)

~~~json
{
  "source": "00aedc94",
  "target": "008b97d4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aedc9c`](#insn-00aedc9c)

~~~json
{
  "source": "00aedc9c",
  "target": "008bb568",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aedcac`](#insn-00aedcac)

~~~json
{
  "source": "00aedcac",
  "target": "00c8df38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8df38",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aedcac`](#insn-00aedcac)

~~~json
{
  "source": "00aedcac",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedcb0`](#insn-00aedcb0)

~~~json
{
  "source": "00aedcb0",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedcb8`](#insn-00aedcb8)

~~~json
{
  "source": "00aedcb8",
  "target": "008b96fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aedcbc`](#insn-00aedcbc)

~~~json
{
  "source": "00aedcbc",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedcc4`](#insn-00aedcc4)

~~~json
{
  "source": "00aedcc4",
  "target": "00aedcd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedcc8`](#insn-00aedcc8)

~~~json
{
  "source": "00aedcc8",
  "target": "00aedce8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedcd0`](#insn-00aedcd0)

~~~json
{
  "source": "00aedcd0",
  "target": "00aedcdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedcdc`](#insn-00aedcdc)

~~~json
{
  "source": "00aedcdc",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedce0`](#insn-00aedce0)

~~~json
{
  "source": "00aedce0",
  "target": "00c8df58",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8df58",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aedce0`](#insn-00aedce0)

~~~json
{
  "source": "00aedce0",
  "target": "00c8df60",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8df60",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aedce4`](#insn-00aedce4)

~~~json
{
  "source": "00aedce4",
  "target": "00aeec84",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aedce4`](#insn-00aedce4)

~~~json
{
  "source": "00aedce4",
  "target": "00aeec88",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aedcec`](#insn-00aedcec)

~~~json
{
  "source": "00aedcec",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedcf4`](#insn-00aedcf4)

~~~json
{
  "source": "00aedcf4",
  "target": "00aeddac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedcf8`](#insn-00aedcf8)

~~~json
{
  "source": "00aedcf8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedcfc`](#insn-00aedcfc)

~~~json
{
  "source": "00aedcfc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedd00`](#insn-00aedd00)

~~~json
{
  "source": "00aedd00",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeddac`](#insn-00aeddac)

~~~json
{
  "source": "00aeddac",
  "target": "00c57fb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
