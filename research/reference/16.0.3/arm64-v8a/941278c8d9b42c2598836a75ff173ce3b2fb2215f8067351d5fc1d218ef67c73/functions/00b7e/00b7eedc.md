# 00b7eedc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00b7dee8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7d/00b7dee8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0078.md#compare-c9dfc39fc39787ebc66b9c73c50966d8)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b7eedc",
  "name": "FUN_00b7eedc",
  "size": 1140,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "636e944a18f25919806d1c68c60201da43a1c5aa6411b169b5b7777c8a3c664c",
  "source_text_sha256": "636e944a18f25919806d1c68c60201da43a1c5aa6411b169b5b7777c8a3c664c",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b7eedc",
        "00b7f34f"
      ]
    ],
    "bytes_sha256": "e7f3aee44d93718a8956aef93edf364c3bc787e3cd2a2a871016a7e96bd976b9",
    "instruction_count": 285,
    "instruction_bytes": 1140,
    "body_bytes": 1140,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00b764d0](../00b76/00b764d0.md)
- [00b79e94](../00b79/00b79e94.md)
- [00b7c308](../00b7c/00b7c308.md)
- [00b7d08c](../00b7d/00b7d08c.md)

## 呼び出し先

- [00b99610](../00b99/00b99610.md)
- [00c58f30](../00c58/00c58f30.md)
- [00c58f50](../00c58/00c58f50.md)
- [00c58f80](../00c58/00c58f80.md)
- [00c59020](../00c59/00c59020.md)
- [00c59080](../00c59/00c59080.md)
- [00c590a0](../00c59/00c590a0.md)
- [00c59150](../00c59/00c59150.md)
- [00c5a070](../00c5a/00c5a070.md)
- [00c5c1e0](../00c5c/00c5c1e0.md)
- [00c5d810](../00c5d/00c5d810.md)
- [00c5e1f0](../00c5e/00c5e1f0.md)

## 関連文字列（未確認候補）

~~~text
", constant does not fit "
"error: "
"invalid number: \""
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 7614 bytes

~~~c

/* WARNING: Type propagation algorithm not settling */

void FUN_00b7eedc(undefined2 *param_1,byte *param_2,undefined8 param_3,undefined4 *param_4)

{
  long lVar1;
  longlong lVar2;
  size_t sVar3;
  ulong *puVar4;
  int __base;
  __locale_t __loc;
  undefined4 uVar5;
  long lVar6;
  uint uVar7;
  void *pvVar8;
  ulong uVar9;
  byte local_120 [8];
  ulong local_118;
  void *local_110;
  ulong local_108;
  size_t local_100;
  void *local_f8;
  ulong local_f0;
  ulong uStack_e8;
  void *local_e0;
  ulong local_d0;
  size_t sStack_c8;
  void *local_c0;
  ulong local_b0;
  ulong uStack_a8;
  void *local_a0;
  ulong local_90;
  ulong uStack_88;
  void *local_80;
  byte *local_70 [2];
  void *local_60;
  long local_58;
  
  lVar1 = tpidr_el0;
  local_58 = *(long *)(lVar1 + 0x28);
  uVar7 = (uint)*param_2;
  if (*param_2 != 0) {
    lVar6 = 1;
    do {
                    /* try { // try from 00b7ef28 to 00c7f037 has its CatchHandler @ 00b7ef28
                       catch() { ... } // from try @ 00b7ef28 with catch @ 00b7ef28
                       catch() { ... } // from try @ 00b7f078 with catch @ 00b7ef28 */
      if (uVar7 - 0x30 < 10) {
        if ((uVar7 == 0x30) && ((param_2[lVar6] & 0xdf) == 0x58)) {
          __loc = *(__locale_t *)PTR__ZN11flatbuffers13ClassicLocale9instance_E_00c9c8d0;
          __base = 0x10;
          goto LAB_00b7ef84;
        }
        break;
      }
      uVar7 = (uint)param_2[lVar6];
      lVar6 = lVar6 + 1;
    } while (uVar7 != 0);
  }
  __loc = *(__locale_t *)PTR__ZN11flatbuffers13ClassicLocale9instance_E_00c9c8d0;
  __base = 10;
LAB_00b7ef84:
  local_70[0] = param_2;
  lVar2 = strtoll_l((char *)param_2,(char **)local_70,__base,__loc);
  if ((local_70[0] == param_2) || (*local_70[0] != 0)) {
    *param_4 = 0;
    sStack_c8 = 0;
    local_c0 = (void *)0x0;
    local_d0 = 0;
    sVar3 = strlen((char *)param_2);
    if (0xffffffffffffffef < sVar3) goto LAB_00b7f34c;
    if (sVar3 < 0x17) {
      pvVar8 = (void *)((ulong)&local_d0 | 1);
      local_d0 = CONCAT71(local_d0._1_7_,(char)((int)sVar3 << 1));
      if (sVar3 != 0) goto LAB_00b7f05c;
    }
    else {
      uVar9 = sVar3 + 0x10 & 0xfffffffffffffff0;
      pvVar8 = (void *)_Znwm(uVar9);
      local_d0 = uVar9 | 1;
      sStack_c8 = sVar3;
      local_c0 = pvVar8;
LAB_00b7f05c:
                    /* try { // try from 00b7f05c to 00c7f077 has its CatchHandler @ 00b7f0e8 */
      memcpy(pvVar8,param_2,sVar3);
    }
                    /* try { // try from 00b7f078 to 00c7f17b has its CatchHandler @ 00b7ef28 */
    *(undefined1 *)((long)pvVar8 + sVar3) = 0;
    puVar4 = (ulong *)_ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6insertEmPKcm
                                (&local_d0,0,"invalid number: \"",0x11);
    uStack_a8 = puVar4[1];
    local_b0 = *puVar4;
    local_a0 = (void *)puVar4[2];
    *puVar4 = 0;
    puVar4[1] = 0;
    puVar4[2] = 0;
    puVar4 = (ulong *)_ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKcm
                                (&local_b0,&DAT_002b5f9c,1);
    uStack_88 = puVar4[1];
    local_90 = *puVar4;
    local_80 = (void *)puVar4[2];
    *puVar4 = 0;
    puVar4[1] = 0;
    puVar4[2] = 0;
    _ZNSt6__ndk1plIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EEPKS6_RKS9_
              (local_70,"error: ",&local_90);
                    /* catch() { ... } // from try @ 00b7f05c with catch @ 00b7f0e8 */
    _ZN11flatbuffers6Parser7MessageERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
              (param_3,local_70);
    if (((ulong)local_70[0] & 1) != 0) {
      _ZdlPv(local_60);
    }
    *param_1 = 1;
    if ((local_90 & 1) != 0) {
      _ZdlPv(local_80);
    }
    pvVar8 = local_c0;
    uVar9 = local_d0;
    if ((local_b0 & 1) != 0) {
      _ZdlPv(local_a0);
      pvVar8 = local_c0;
      uVar9 = local_d0;
    }
  }
  else {
    uVar5 = 0x7fffffff;
    if (lVar2 < 0x80000000) {
      if (-0x80000001 < lVar2) {
        *param_4 = (int)lVar2;
        *param_1 = 0;
        goto LAB_00b7f31c;
      }
      uVar5 = 0x80000000;
    }
    *param_4 = uVar5;
    local_100 = 0;
    local_f8 = (void *)0x0;
    local_108 = 0;
    sVar3 = strlen((char *)param_2);
    if (0xffffffffffffffef < sVar3) {
LAB_00b7f34c:
                    /* WARNING: Subroutine does not return */
      abort();
    }
    if (sVar3 < 0x17) {
      pvVar8 = (void *)((ulong)&local_108 | 1);
      local_108 = CONCAT71(local_108._1_7_,(char)((int)sVar3 << 1));
      if (sVar3 != 0) goto LAB_00b7f168;
    }
    else {
      uVar9 = sVar3 + 0x10 & 0xfffffffffffffff0;
      pvVar8 = (void *)_Znwm(uVar9);
      local_108 = uVar9 | 1;
      local_100 = sVar3;
      local_f8 = pvVar8;
LAB_00b7f168:
                    /* catch() { ... } // from try @ 00b7f038 with catch @ 00b7f16c */
      memcpy(pvVar8,param_2,sVar3);
    }
    *(undefined1 *)((long)pvVar8 + sVar3) = 0;
    puVar4 = (ulong *)_ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6insertEmPKcm
                                (&local_108,0,"invalid number: \"",0x11);
    uStack_e8 = puVar4[1];
    local_f0 = *puVar4;
    local_e0 = (void *)puVar4[2];
    *puVar4 = 0;
    puVar4[1] = 0;
    puVar4[2] = 0;
    puVar4 = (ulong *)_ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKcm
                                (&local_f0,&DAT_002b5f9c,1);
    sStack_c8 = puVar4[1];
    local_d0 = *puVar4;
    local_c0 = (void *)puVar4[2];
    *puVar4 = 0;
    puVar4[1] = 0;
    puVar4[2] = 0;
    puVar4 = (ulong *)_ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKcm
                                (&local_d0,", constant does not fit ",0x18);
    local_a0 = (void *)puVar4[2];
    uStack_a8 = puVar4[1];
    local_b0 = *puVar4;
    *puVar4 = 0;
    puVar4[1] = 0;
    puVar4[2] = 0;
    FUN_00b99610(local_120);
    uVar9 = (ulong)(local_120[0] >> 1);
    pvVar8 = (void *)((ulong)local_120 | 1);
    if ((local_120[0] & 1) != 0) {
      uVar9 = local_118;
      pvVar8 = local_110;
    }
    puVar4 = (ulong *)_ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKcm
                                (&local_b0,pvVar8,uVar9);
    uStack_88 = puVar4[1];
    local_90 = *puVar4;
    local_80 = (void *)puVar4[2];
    *puVar4 = 0;
    puVar4[1] = 0;
    puVar4[2] = 0;
    _ZNSt6__ndk1plIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EEPKS6_RKS9_
              (local_70,"error: ",&local_90);
    _ZN11flatbuffers6Parser7MessageERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
              (param_3,local_70);
    if (((ulong)local_70[0] & 1) != 0) {
                    /* try { // try from 00b7f278 to 00c7f387 has its CatchHandler @ 00b7f278
                       catch() { ... } // from try @ 00b7f278 with catch @ 00b7f278
                       catch() { ... } // from try @ 00b7f3c8 with catch @ 00b7f278 */
      _ZdlPv(local_60);
    }
    *param_1 = 1;
    if ((local_90 & 1) != 0) {
      _ZdlPv(local_80);
    }
    if ((local_120[0] & 1) != 0) {
      _ZdlPv(local_110);
    }
    if ((local_b0 & 1) != 0) {
      _ZdlPv(local_a0);
    }
    if ((local_d0 & 1) != 0) {
      _ZdlPv(local_c0);
    }
    pvVar8 = local_f8;
    uVar9 = local_108;
    if ((local_f0 & 1) != 0) {
      _ZdlPv(local_e0);
      pvVar8 = local_f8;
      uVar9 = local_108;
    }
  }
  if ((uVar9 & 1) != 0) {
    _ZdlPv(pvVar8);
  }
LAB_00b7f31c:
  if (*(long *)(lVar1 + 0x28) != local_58) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b7eedc"></a> `00b7eedc` | `ff 83 04 d1` | sub sp,sp,#0x120 | `FALL_THROUGH`
<a id="insn-00b7eee0"></a> `00b7eee0` | `fc 67 0d a9` | stp x28,x25,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-00b7eee4"></a> `00b7eee4` | `f8 5f 0e a9` | stp x24,x23,[sp, #0xe0] | `FALL_THROUGH`
<a id="insn-00b7eee8"></a> `00b7eee8` | `f6 57 0f a9` | stp x22,x21,[sp, #0xf0] | `FALL_THROUGH`
<a id="insn-00b7eeec"></a> `00b7eeec` | `f4 4f 10 a9` | stp x20,x19,[sp, #0x100] | `FALL_THROUGH`
<a id="insn-00b7eef0"></a> `00b7eef0` | `fd 7b 11 a9` | stp x29,x30,[sp, #0x110] | `FALL_THROUGH`
<a id="insn-00b7eef4"></a> `00b7eef4` | `fd 43 04 91` | add x29,sp,#0x110 | `FALL_THROUGH`
<a id="insn-00b7eef8"></a> `00b7eef8` | `59 d0 3b d5` | mrs x25,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00b7eefc"></a> `00b7eefc` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00b7ef00"></a> `00b7ef00` | `28 17 40 f9` | ldr x8,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-00b7ef04"></a> `00b7ef04` | `f6 03 02 aa` | mov x22,x2 | `FALL_THROUGH`
<a id="insn-00b7ef08"></a> `00b7ef08` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00b7ef0c"></a> `00b7ef0c` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00b7ef10"></a> `00b7ef10` | `a8 83 1b f8` | stur x8,[x29, #-0x48] | `FALL_THROUGH`
<a id="insn-00b7ef14"></a> `00b7ef14` | `e8 08 00 d0` | adrp x8,0xc9c000 | `FALL_THROUGH`
<a id="insn-00b7ef18"></a> `00b7ef18` | `0a 00 40 39` | ldrb w10,[x0] | `FALL_THROUGH`
<a id="insn-00b7ef1c"></a> `00b7ef1c` | `08 69 44 f9` | ldr x8,[x8, #0x8d0] | `FALL_THROUGH`
<a id="insn-00b7ef20"></a> `00b7ef20` | `aa 02 00 34` | cbz w10,0x00b7ef74 | `CONDITIONAL_JUMP`
<a id="insn-00b7ef24"></a> `00b7ef24` | `29 00 80 52` | mov w9,#0x1 | `FALL_THROUGH`
<a id="insn-00b7ef28"></a> `00b7ef28` | `4a 1d 00 12` | and w10,w10,#0xff | `FALL_THROUGH`
<a id="insn-00b7ef2c"></a> `00b7ef2c` | `4b c1 00 51` | sub w11,w10,#0x30 | `FALL_THROUGH`
<a id="insn-00b7ef30"></a> `00b7ef30` | `7f 29 00 71` | cmp w11,#0xa | `FALL_THROUGH`
<a id="insn-00b7ef34"></a> `00b7ef34` | `a3 00 00 54` | b.cc 0x00b7ef48 | `CONDITIONAL_JUMP`
<a id="insn-00b7ef38"></a> `00b7ef38` | `aa 6a 69 38` | ldrb w10,[x21, x9, LSL ] | `FALL_THROUGH`
<a id="insn-00b7ef3c"></a> `00b7ef3c` | `29 05 00 91` | add x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00b7ef40"></a> `00b7ef40` | `4a ff ff 35` | cbnz w10,0x00b7ef28 | `CONDITIONAL_JUMP`
<a id="insn-00b7ef44"></a> `00b7ef44` | `0c 00 00 14` | b 0x00b7ef74 | `UNCONDITIONAL_JUMP`
<a id="insn-00b7ef48"></a> `00b7ef48` | `5f c1 00 71` | cmp w10,#0x30 | `FALL_THROUGH`
<a id="insn-00b7ef4c"></a> `00b7ef4c` | `41 01 00 54` | b.ne 0x00b7ef74 | `CONDITIONAL_JUMP`
<a id="insn-00b7ef50"></a> `00b7ef50` | `a9 6a 69 38` | ldrb w9,[x21, x9, LSL ] | `FALL_THROUGH`
<a id="insn-00b7ef54"></a> `00b7ef54` | `29 79 1a 12` | and w9,w9,#0xffffffdf | `FALL_THROUGH`
<a id="insn-00b7ef58"></a> `00b7ef58` | `3f 61 01 71` | cmp w9,#0x58 | `FALL_THROUGH`
<a id="insn-00b7ef5c"></a> `00b7ef5c` | `c1 00 00 54` | b.ne 0x00b7ef74 | `CONDITIONAL_JUMP`
<a id="insn-00b7ef60"></a> `00b7ef60` | `03 01 40 f9` | ldr x3,[x8] | `FALL_THROUGH`
<a id="insn-00b7ef64"></a> `00b7ef64` | `b5 03 1a f8` | stur x21,[x29, #-0x60] | `FALL_THROUGH`
<a id="insn-00b7ef68"></a> `00b7ef68` | `a1 83 01 d1` | sub x1,x29,#0x60 | `FALL_THROUGH`
<a id="insn-00b7ef6c"></a> `00b7ef6c` | `02 02 80 52` | mov w2,#0x10 | `FALL_THROUGH`
<a id="insn-00b7ef70"></a> `00b7ef70` | `05 00 00 14` | b 0x00b7ef84 | `UNCONDITIONAL_JUMP`
<a id="insn-00b7ef74"></a> `00b7ef74` | `03 01 40 f9` | ldr x3,[x8] | `FALL_THROUGH`
<a id="insn-00b7ef78"></a> `00b7ef78` | `a1 83 01 d1` | sub x1,x29,#0x60 | `FALL_THROUGH`
<a id="insn-00b7ef7c"></a> `00b7ef7c` | `42 01 80 52` | mov w2,#0xa | `FALL_THROUGH`
<a id="insn-00b7ef80"></a> `00b7ef80` | `b5 03 1a f8` | stur x21,[x29, #-0x60] | `FALL_THROUGH`
<a id="insn-00b7ef84"></a> `00b7ef84` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00b7ef88"></a> `00b7ef88` | `9a 7c 03 94` | bl 0x00c5e1f0 | `UNCONDITIONAL_CALL`
<a id="insn-00b7ef8c"></a> `00b7ef8c` | `a8 03 5a f8` | ldur x8,[x29, #-0x60] | `FALL_THROUGH`
<a id="insn-00b7ef90"></a> `00b7ef90` | `1f 01 15 eb` | cmp x8,x21 | `FALL_THROUGH`
<a id="insn-00b7ef94"></a> `00b7ef94` | `40 03 00 54` | b.eq 0x00b7effc | `CONDITIONAL_JUMP`
<a id="insn-00b7ef98"></a> `00b7ef98` | `08 01 40 39` | ldrb w8,[x8] | `FALL_THROUGH`
<a id="insn-00b7ef9c"></a> `00b7ef9c` | `08 03 00 35` | cbnz w8,0x00b7effc | `CONDITIONAL_JUMP`
<a id="insn-00b7efa0"></a> `00b7efa0` | `08 00 b0 12` | mov w8,#0x7fffffff | `FALL_THROUGH`
<a id="insn-00b7efa4"></a> `00b7efa4` | `1f 00 08 eb` | cmp x0,x8 | `FALL_THROUGH`
<a id="insn-00b7efa8"></a> `00b7efa8` | `ac 00 00 54` | b.gt 0x00b7efbc | `CONDITIONAL_JUMP`
<a id="insn-00b7efac"></a> `00b7efac` | `e8 83 61 b2` | orr x8,xzr,#-0x80000000 | `FALL_THROUGH`
<a id="insn-00b7efb0"></a> `00b7efb0` | `1f 00 08 eb` | cmp x0,x8 | `FALL_THROUGH`
<a id="insn-00b7efb4"></a> `00b7efb4` | `0a 1b 00 54` | b.ge 0x00b7f314 | `CONDITIONAL_JUMP`
<a id="insn-00b7efb8"></a> `00b7efb8` | `08 00 b0 52` | mov w8,#0x80000000 | `FALL_THROUGH`
<a id="insn-00b7efbc"></a> `00b7efbc` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00b7efc0"></a> `00b7efc0` | `c8 02 00 b9` | str w8,[x22] | `FALL_THROUGH`
<a id="insn-00b7efc4"></a> `00b7efc4` | `ff 7f 02 a9` | stp xzr,xzr,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b7efc8"></a> `00b7efc8` | `ff 0f 00 f9` | str xzr,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00b7efcc"></a> `00b7efcc` | `2d 68 03 94` | bl 0x00c59080 | `UNCONDITIONAL_CALL`
<a id="insn-00b7efd0"></a> `00b7efd0` | `1f 40 00 b1` | cmn x0,#0x10 | `FALL_THROUGH`
<a id="insn-00b7efd4"></a> `00b7efd4` | `c2 1b 00 54` | b.cs 0x00b7f34c | `CONDITIONAL_JUMP`
<a id="insn-00b7efd8"></a> `00b7efd8` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00b7efdc"></a> `00b7efdc` | `1f 5c 00 f1` | cmp x0,#0x17 | `FALL_THROUGH`
<a id="insn-00b7efe0"></a> `00b7efe0` | `42 0b 00 54` | b.cs 0x00b7f148 | `CONDITIONAL_JUMP`
<a id="insn-00b7efe4"></a> `00b7efe4` | `e9 63 00 91` | add x9,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00b7efe8"></a> `00b7efe8` | `c8 7a 1f 53` | lsl w8,w22,#0x1 | `FALL_THROUGH`
<a id="insn-00b7efec"></a> `00b7efec` | `37 01 40 b2` | orr x23,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00b7eff0"></a> `00b7eff0` | `e8 63 00 39` | strb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00b7eff4"></a> `00b7eff4` | `b6 0b 00 b5` | cbnz x22,0x00b7f168 | `CONDITIONAL_JUMP`
<a id="insn-00b7eff8"></a> `00b7eff8` | `60 00 00 14` | b 0x00b7f178 | `UNCONDITIONAL_JUMP`
<a id="insn-00b7effc"></a> `00b7effc` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00b7f000"></a> `00b7f000` | `df 02 00 b9` | str wzr,[x22] | `FALL_THROUGH`
<a id="insn-00b7f004"></a> `00b7f004` | `ff ff 05 a9` | stp xzr,xzr,[sp, #0x58] | `FALL_THROUGH`
<a id="insn-00b7f008"></a> `00b7f008` | `ff 2b 00 f9` | str xzr,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00b7f00c"></a> `00b7f00c` | `1d 68 03 94` | bl 0x00c59080 | `UNCONDITIONAL_CALL`
<a id="insn-00b7f010"></a> `00b7f010` | `1f 40 00 b1` | cmn x0,#0x10 | `FALL_THROUGH`
<a id="insn-00b7f014"></a> `00b7f014` | `c2 19 00 54` | b.cs 0x00b7f34c | `CONDITIONAL_JUMP`
<a id="insn-00b7f018"></a> `00b7f018` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00b7f01c"></a> `00b7f01c` | `1f 5c 00 f1` | cmp x0,#0x17 | `FALL_THROUGH`
<a id="insn-00b7f020"></a> `00b7f020` | `e2 00 00 54` | b.cs 0x00b7f03c | `CONDITIONAL_JUMP`
<a id="insn-00b7f024"></a> `00b7f024` | `e9 43 01 91` | add x9,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00b7f028"></a> `00b7f028` | `c8 7a 1f 53` | lsl w8,w22,#0x1 | `FALL_THROUGH`
<a id="insn-00b7f02c"></a> `00b7f02c` | `37 01 40 b2` | orr x23,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00b7f030"></a> `00b7f030` | `e8 43 01 39` | strb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00b7f034"></a> `00b7f034` | `56 01 00 b5` | cbnz x22,0x00b7f05c | `CONDITIONAL_JUMP`
<a id="insn-00b7f038"></a> `00b7f038` | `0d 00 00 14` | b 0x00b7f06c | `UNCONDITIONAL_JUMP`
<a id="insn-00b7f03c"></a> `00b7f03c` | `c8 42 00 91` | add x8,x22,#0x10 | `FALL_THROUGH`
<a id="insn-00b7f040"></a> `00b7f040` | `18 ed 7c 92` | and x24,x8,#-0x10 | `FALL_THROUGH`
<a id="insn-00b7f044"></a> `00b7f044` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00b7f048"></a> `00b7f048` | `ba 67 03 94` | bl 0x00c58f30 | `UNCONDITIONAL_CALL`
<a id="insn-00b7f04c"></a> `00b7f04c` | `08 03 40 b2` | orr x8,x24,#0x1 | `FALL_THROUGH`
<a id="insn-00b7f050"></a> `00b7f050` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00b7f054"></a> `00b7f054` | `e8 5b 05 a9` | stp x8,x22,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00b7f058"></a> `00b7f058` | `e0 33 00 f9` | str x0,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00b7f05c"></a> `00b7f05c` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00b7f060"></a> `00b7f060` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00b7f064"></a> `00b7f064` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00b7f068"></a> `00b7f068` | `0e 68 03 94` | bl 0x00c590a0 | `UNCONDITIONAL_CALL`
<a id="insn-00b7f06c"></a> `00b7f06c` | `a2 b9 ff f0` | adrp x2,0x2b6000 | `FALL_THROUGH`
<a id="insn-00b7f070"></a> `00b7f070` | `42 2c 3b 91` | add x2,x2,#0xecb | `FALL_THROUGH`
<a id="insn-00b7f074"></a> `00b7f074` | `e0 43 01 91` | add x0,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00b7f078"></a> `00b7f078` | `23 02 80 52` | mov w3,#0x11 | `FALL_THROUGH`
<a id="insn-00b7f07c"></a> `00b7f07c` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-00b7f080"></a> `00b7f080` | `ff 6a 36 38` | strb wzr,[x23, x22, LSL ] | `FALL_THROUGH`
<a id="insn-00b7f084"></a> `00b7f084` | `fb 6b 03 94` | bl 0x00c5a070 | `UNCONDITIONAL_CALL`
<a id="insn-00b7f088"></a> `00b7f088` | `00 00 c0 3d` | ldr q0,[x0] | `FALL_THROUGH`
<a id="insn-00b7f08c"></a> `00b7f08c` | `08 08 40 f9` | ldr x8,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00b7f090"></a> `00b7f090` | `a1 b9 ff d0` | adrp x1,0x2b5000 | `FALL_THROUGH`
<a id="insn-00b7f094"></a> `00b7f094` | `21 70 3e 91` | add x1,x1,#0xf9c | `FALL_THROUGH`
<a id="insn-00b7f098"></a> `00b7f098` | `e0 1f 80 3d` | str q0,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00b7f09c"></a> `00b7f09c` | `e8 43 00 f9` | str x8,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00b7f0a0"></a> `00b7f0a0` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00b7f0a4"></a> `00b7f0a4` | `1f 08 00 f9` | str xzr,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00b7f0a8"></a> `00b7f0a8` | `e0 c3 01 91` | add x0,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00b7f0ac"></a> `00b7f0ac` | `22 00 80 52` | mov w2,#0x1 | `FALL_THROUGH`
<a id="insn-00b7f0b0"></a> `00b7f0b0` | `35 00 80 52` | mov w21,#0x1 | `FALL_THROUGH`
<a id="insn-00b7f0b4"></a> `00b7f0b4` | `db 67 03 94` | bl 0x00c59020 | `UNCONDITIONAL_CALL`
<a id="insn-00b7f0b8"></a> `00b7f0b8` | `00 00 c0 3d` | ldr q0,[x0] | `FALL_THROUGH`
<a id="insn-00b7f0bc"></a> `00b7f0bc` | `08 08 40 f9` | ldr x8,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00b7f0c0"></a> `00b7f0c0` | `a1 03 02 d1` | sub x1,x29,#0x80 | `FALL_THROUGH`
<a id="insn-00b7f0c4"></a> `00b7f0c4` | `a0 03 98 3c` | stur q0,[x29, #-0x80] | `FALL_THROUGH`
<a id="insn-00b7f0c8"></a> `00b7f0c8` | `a8 03 19 f8` | stur x8,[x29, #-0x70] | `FALL_THROUGH`
<a id="insn-00b7f0cc"></a> `00b7f0cc` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00b7f0d0"></a> `00b7f0d0` | `1f 08 00 f9` | str xzr,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00b7f0d4"></a> `00b7f0d4` | `00 b9 ff b0` | adrp x0,0x2a0000 | `FALL_THROUGH`
<a id="insn-00b7f0d8"></a> `00b7f0d8` | `00 a4 2e 91` | add x0,x0,#0xba9 | `FALL_THROUGH`
<a id="insn-00b7f0dc"></a> `00b7f0dc` | `a8 83 01 d1` | sub x8,x29,#0x60 | `FALL_THROUGH`
<a id="insn-00b7f0e0"></a> `00b7f0e0` | `1c 68 03 94` | bl 0x00c59150 | `UNCONDITIONAL_CALL`
<a id="insn-00b7f0e4"></a> `00b7f0e4` | `a1 83 01 d1` | sub x1,x29,#0x60 | `FALL_THROUGH`
<a id="insn-00b7f0e8"></a> `00b7f0e8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b7f0ec"></a> `00b7f0ec` | `c9 79 03 94` | bl 0x00c5d810 | `UNCONDITIONAL_CALL`
<a id="insn-00b7f0f0"></a> `00b7f0f0` | `a8 03 5a 38` | ldurb w8,[x29, #-0x60] | `FALL_THROUGH`
<a id="insn-00b7f0f4"></a> `00b7f0f4` | `68 00 00 36` | tbz w8,#0x0,0x00b7f100 | `CONDITIONAL_JUMP`
<a id="insn-00b7f0f8"></a> `00b7f0f8` | `a0 03 5b f8` | ldur x0,[x29, #-0x50] | `FALL_THROUGH`
<a id="insn-00b7f0fc"></a> `00b7f0fc` | `95 67 03 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00b7f100"></a> `00b7f100` | `a8 03 58 38` | ldurb w8,[x29, #-0x80] | `FALL_THROUGH`
<a id="insn-00b7f104"></a> `00b7f104` | `75 02 00 79` | strh w21,[x19] | `FALL_THROUGH`
<a id="insn-00b7f108"></a> `00b7f108` | `c8 00 00 37` | tbnz w8,#0x0,0x00b7f120 | `CONDITIONAL_JUMP`
<a id="insn-00b7f10c"></a> `00b7f10c` | `e8 c3 41 39` | ldrb w8,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00b7f110"></a> `00b7f110` | `08 01 00 37` | tbnz w8,#0x0,0x00b7f130 | `CONDITIONAL_JUMP`
<a id="insn-00b7f114"></a> `00b7f114` | `e8 43 41 39` | ldrb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00b7f118"></a> `00b7f118` | `48 01 00 37` | tbnz w8,#0x0,0x00b7f140 | `CONDITIONAL_JUMP`
<a id="insn-00b7f11c"></a> `00b7f11c` | `80 00 00 14` | b 0x00b7f31c | `UNCONDITIONAL_JUMP`
<a id="insn-00b7f120"></a> `00b7f120` | `a0 03 59 f8` | ldur x0,[x29, #-0x70] | `FALL_THROUGH`
<a id="insn-00b7f124"></a> `00b7f124` | `8b 67 03 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00b7f128"></a> `00b7f128` | `e8 c3 41 39` | ldrb w8,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00b7f12c"></a> `00b7f12c` | `48 ff 07 36` | tbz w8,#0x0,0x00b7f114 | `CONDITIONAL_JUMP`
<a id="insn-00b7f130"></a> `00b7f130` | `e0 43 40 f9` | ldr x0,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00b7f134"></a> `00b7f134` | `87 67 03 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00b7f138"></a> `00b7f138` | `e8 43 41 39` | ldrb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00b7f13c"></a> `00b7f13c` | `08 0f 00 36` | tbz w8,#0x0,0x00b7f31c | `CONDITIONAL_JUMP`
<a id="insn-00b7f140"></a> `00b7f140` | `e0 33 40 f9` | ldr x0,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00b7f144"></a> `00b7f144` | `72 00 00 14` | b 0x00b7f30c | `UNCONDITIONAL_JUMP`
<a id="insn-00b7f148"></a> `00b7f148` | `c8 42 00 91` | add x8,x22,#0x10 | `FALL_THROUGH`
<a id="insn-00b7f14c"></a> `00b7f14c` | `18 ed 7c 92` | and x24,x8,#-0x10 | `FALL_THROUGH`
<a id="insn-00b7f150"></a> `00b7f150` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00b7f154"></a> `00b7f154` | `77 67 03 94` | bl 0x00c58f30 | `UNCONDITIONAL_CALL`
<a id="insn-00b7f158"></a> `00b7f158` | `08 03 40 b2` | orr x8,x24,#0x1 | `FALL_THROUGH`
<a id="insn-00b7f15c"></a> `00b7f15c` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00b7f160"></a> `00b7f160` | `e8 db 01 a9` | stp x8,x22,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00b7f164"></a> `00b7f164` | `e0 17 00 f9` | str x0,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00b7f168"></a> `00b7f168` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00b7f16c"></a> `00b7f16c` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00b7f170"></a> `00b7f170` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00b7f174"></a> `00b7f174` | `cb 67 03 94` | bl 0x00c590a0 | `UNCONDITIONAL_CALL`
<a id="insn-00b7f178"></a> `00b7f178` | `a2 b9 ff f0` | adrp x2,0x2b6000 | `FALL_THROUGH`
<a id="insn-00b7f17c"></a> `00b7f17c` | `42 2c 3b 91` | add x2,x2,#0xecb | `FALL_THROUGH`
<a id="insn-00b7f180"></a> `00b7f180` | `e0 63 00 91` | add x0,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00b7f184"></a> `00b7f184` | `23 02 80 52` | mov w3,#0x11 | `FALL_THROUGH`
<a id="insn-00b7f188"></a> `00b7f188` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-00b7f18c"></a> `00b7f18c` | `ff 6a 36 38` | strb wzr,[x23, x22, LSL ] | `FALL_THROUGH`
<a id="insn-00b7f190"></a> `00b7f190` | `b8 6b 03 94` | bl 0x00c5a070 | `UNCONDITIONAL_CALL`
<a id="insn-00b7f194"></a> `00b7f194` | `00 00 c0 3d` | ldr q0,[x0] | `FALL_THROUGH`
<a id="insn-00b7f198"></a> `00b7f198` | `08 08 40 f9` | ldr x8,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00b7f19c"></a> `00b7f19c` | `a1 b9 ff d0` | adrp x1,0x2b5000 | `FALL_THROUGH`
<a id="insn-00b7f1a0"></a> `00b7f1a0` | `21 70 3e 91` | add x1,x1,#0xf9c | `FALL_THROUGH`
<a id="insn-00b7f1a4"></a> `00b7f1a4` | `e0 0f 80 3d` | str q0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b7f1a8"></a> `00b7f1a8` | `e8 23 00 f9` | str x8,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b7f1ac"></a> `00b7f1ac` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00b7f1b0"></a> `00b7f1b0` | `1f 08 00 f9` | str xzr,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00b7f1b4"></a> `00b7f1b4` | `e0 c3 00 91` | add x0,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00b7f1b8"></a> `00b7f1b8` | `22 00 80 52` | mov w2,#0x1 | `FALL_THROUGH`
<a id="insn-00b7f1bc"></a> `00b7f1bc` | `35 00 80 52` | mov w21,#0x1 | `FALL_THROUGH`
<a id="insn-00b7f1c0"></a> `00b7f1c0` | `98 67 03 94` | bl 0x00c59020 | `UNCONDITIONAL_CALL`
<a id="insn-00b7f1c4"></a> `00b7f1c4` | `00 00 c0 3d` | ldr q0,[x0] | `FALL_THROUGH`
<a id="insn-00b7f1c8"></a> `00b7f1c8` | `08 08 40 f9` | ldr x8,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00b7f1cc"></a> `00b7f1cc` | `01 b9 ff d0` | adrp x1,0x2a1000 | `FALL_THROUGH`
<a id="insn-00b7f1d0"></a> `00b7f1d0` | `21 b8 2e 91` | add x1,x1,#0xbae | `FALL_THROUGH`
<a id="insn-00b7f1d4"></a> `00b7f1d4` | `e0 17 80 3d` | str q0,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00b7f1d8"></a> `00b7f1d8` | `e8 33 00 f9` | str x8,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00b7f1dc"></a> `00b7f1dc` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00b7f1e0"></a> `00b7f1e0` | `1f 08 00 f9` | str xzr,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00b7f1e4"></a> `00b7f1e4` | `e0 43 01 91` | add x0,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00b7f1e8"></a> `00b7f1e8` | `02 03 80 52` | mov w2,#0x18 | `FALL_THROUGH`
<a id="insn-00b7f1ec"></a> `00b7f1ec` | `8d 67 03 94` | bl 0x00c59020 | `UNCONDITIONAL_CALL`
<a id="insn-00b7f1f0"></a> `00b7f1f0` | `08 08 40 f9` | ldr x8,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00b7f1f4"></a> `00b7f1f4` | `00 00 c0 3d` | ldr q0,[x0] | `FALL_THROUGH`
<a id="insn-00b7f1f8"></a> `00b7f1f8` | `f6 03 00 91` | mov x22,sp | `FALL_THROUGH`
<a id="insn-00b7f1fc"></a> `00b7f1fc` | `e8 43 00 f9` | str x8,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00b7f200"></a> `00b7f200` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00b7f204"></a> `00b7f204` | `e0 1f 80 3d` | str q0,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00b7f208"></a> `00b7f208` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00b7f20c"></a> `00b7f20c` | `1f 08 00 f9` | str xzr,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00b7f210"></a> `00b7f210` | `00 69 00 94` | bl 0x00b99610 | `UNCONDITIONAL_CALL`
<a id="insn-00b7f214"></a> `00b7f214` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-00b7f218"></a> `00b7f218` | `ea a7 40 a9` | ldp x10,x9,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00b7f21c"></a> `00b7f21c` | `cb 02 40 b2` | orr x11,x22,#0x1 | `FALL_THROUGH`
<a id="insn-00b7f220"></a> `00b7f220` | `e0 c3 01 91` | add x0,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00b7f224"></a> `00b7f224` | `0c fd 41 d3` | lsr x12,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00b7f228"></a> `00b7f228` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00b7f22c"></a> `00b7f22c` | `61 01 89 9a` | csel x1,x11,x9,eq | `FALL_THROUGH`
<a id="insn-00b7f230"></a> `00b7f230` | `82 01 8a 9a` | csel x2,x12,x10,eq | `FALL_THROUGH`
<a id="insn-00b7f234"></a> `00b7f234` | `7b 67 03 94` | bl 0x00c59020 | `UNCONDITIONAL_CALL`
<a id="insn-00b7f238"></a> `00b7f238` | `00 00 c0 3d` | ldr q0,[x0] | `FALL_THROUGH`
<a id="insn-00b7f23c"></a> `00b7f23c` | `08 08 40 f9` | ldr x8,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00b7f240"></a> `00b7f240` | `a1 03 02 d1` | sub x1,x29,#0x80 | `FALL_THROUGH`
<a id="insn-00b7f244"></a> `00b7f244` | `a0 03 98 3c` | stur q0,[x29, #-0x80] | `FALL_THROUGH`
<a id="insn-00b7f248"></a> `00b7f248` | `a8 03 19 f8` | stur x8,[x29, #-0x70] | `FALL_THROUGH`
<a id="insn-00b7f24c"></a> `00b7f24c` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00b7f250"></a> `00b7f250` | `1f 08 00 f9` | str xzr,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00b7f254"></a> `00b7f254` | `00 b9 ff b0` | adrp x0,0x2a0000 | `FALL_THROUGH`
<a id="insn-00b7f258"></a> `00b7f258` | `00 a4 2e 91` | add x0,x0,#0xba9 | `FALL_THROUGH`
<a id="insn-00b7f25c"></a> `00b7f25c` | `a8 83 01 d1` | sub x8,x29,#0x60 | `FALL_THROUGH`
<a id="insn-00b7f260"></a> `00b7f260` | `bc 67 03 94` | bl 0x00c59150 | `UNCONDITIONAL_CALL`
<a id="insn-00b7f264"></a> `00b7f264` | `a1 83 01 d1` | sub x1,x29,#0x60 | `FALL_THROUGH`
<a id="insn-00b7f268"></a> `00b7f268` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b7f26c"></a> `00b7f26c` | `69 79 03 94` | bl 0x00c5d810 | `UNCONDITIONAL_CALL`
<a id="insn-00b7f270"></a> `00b7f270` | `a8 03 5a 38` | ldurb w8,[x29, #-0x60] | `FALL_THROUGH`
<a id="insn-00b7f274"></a> `00b7f274` | `68 00 00 36` | tbz w8,#0x0,0x00b7f280 | `CONDITIONAL_JUMP`
<a id="insn-00b7f278"></a> `00b7f278` | `a0 03 5b f8` | ldur x0,[x29, #-0x50] | `FALL_THROUGH`
<a id="insn-00b7f27c"></a> `00b7f27c` | `35 67 03 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00b7f280"></a> `00b7f280` | `a8 03 58 38` | ldurb w8,[x29, #-0x80] | `FALL_THROUGH`
<a id="insn-00b7f284"></a> `00b7f284` | `75 02 00 79` | strh w21,[x19] | `FALL_THROUGH`
<a id="insn-00b7f288"></a> `00b7f288` | `88 01 00 37` | tbnz w8,#0x0,0x00b7f2b8 | `CONDITIONAL_JUMP`
<a id="insn-00b7f28c"></a> `00b7f28c` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-00b7f290"></a> `00b7f290` | `c8 01 00 37` | tbnz w8,#0x0,0x00b7f2c8 | `CONDITIONAL_JUMP`
<a id="insn-00b7f294"></a> `00b7f294` | `e8 c3 41 39` | ldrb w8,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00b7f298"></a> `00b7f298` | `08 02 00 37` | tbnz w8,#0x0,0x00b7f2d8 | `CONDITIONAL_JUMP`
<a id="insn-00b7f29c"></a> `00b7f29c` | `e8 43 41 39` | ldrb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00b7f2a0"></a> `00b7f2a0` | `48 02 00 37` | tbnz w8,#0x0,0x00b7f2e8 | `CONDITIONAL_JUMP`
<a id="insn-00b7f2a4"></a> `00b7f2a4` | `e8 c3 40 39` | ldrb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b7f2a8"></a> `00b7f2a8` | `88 02 00 37` | tbnz w8,#0x0,0x00b7f2f8 | `CONDITIONAL_JUMP`
<a id="insn-00b7f2ac"></a> `00b7f2ac` | `e8 63 40 39` | ldrb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00b7f2b0"></a> `00b7f2b0` | `c8 02 00 37` | tbnz w8,#0x0,0x00b7f308 | `CONDITIONAL_JUMP`
<a id="insn-00b7f2b4"></a> `00b7f2b4` | `1a 00 00 14` | b 0x00b7f31c | `UNCONDITIONAL_JUMP`
<a id="insn-00b7f2b8"></a> `00b7f2b8` | `a0 03 59 f8` | ldur x0,[x29, #-0x70] | `FALL_THROUGH`
<a id="insn-00b7f2bc"></a> `00b7f2bc` | `25 67 03 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00b7f2c0"></a> `00b7f2c0` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-00b7f2c4"></a> `00b7f2c4` | `88 fe 07 36` | tbz w8,#0x0,0x00b7f294 | `CONDITIONAL_JUMP`
<a id="insn-00b7f2c8"></a> `00b7f2c8` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b7f2cc"></a> `00b7f2cc` | `21 67 03 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00b7f2d0"></a> `00b7f2d0` | `e8 c3 41 39` | ldrb w8,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00b7f2d4"></a> `00b7f2d4` | `48 fe 07 36` | tbz w8,#0x0,0x00b7f29c | `CONDITIONAL_JUMP`
<a id="insn-00b7f2d8"></a> `00b7f2d8` | `e0 43 40 f9` | ldr x0,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00b7f2dc"></a> `00b7f2dc` | `1d 67 03 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00b7f2e0"></a> `00b7f2e0` | `e8 43 41 39` | ldrb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00b7f2e4"></a> `00b7f2e4` | `08 fe 07 36` | tbz w8,#0x0,0x00b7f2a4 | `CONDITIONAL_JUMP`
<a id="insn-00b7f2e8"></a> `00b7f2e8` | `e0 33 40 f9` | ldr x0,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00b7f2ec"></a> `00b7f2ec` | `19 67 03 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00b7f2f0"></a> `00b7f2f0` | `e8 c3 40 39` | ldrb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b7f2f4"></a> `00b7f2f4` | `c8 fd 07 36` | tbz w8,#0x0,0x00b7f2ac | `CONDITIONAL_JUMP`
<a id="insn-00b7f2f8"></a> `00b7f2f8` | `e0 23 40 f9` | ldr x0,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b7f2fc"></a> `00b7f2fc` | `15 67 03 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00b7f300"></a> `00b7f300` | `e8 63 40 39` | ldrb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00b7f304"></a> `00b7f304` | `c8 00 00 36` | tbz w8,#0x0,0x00b7f31c | `CONDITIONAL_JUMP`
<a id="insn-00b7f308"></a> `00b7f308` | `e0 17 40 f9` | ldr x0,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00b7f30c"></a> `00b7f30c` | `11 67 03 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00b7f310"></a> `00b7f310` | `03 00 00 14` | b 0x00b7f31c | `UNCONDITIONAL_JUMP`
<a id="insn-00b7f314"></a> `00b7f314` | `c0 02 00 b9` | str w0,[x22] | `FALL_THROUGH`
<a id="insn-00b7f318"></a> `00b7f318` | `7f 02 00 79` | strh wzr,[x19] | `FALL_THROUGH`
<a id="insn-00b7f31c"></a> `00b7f31c` | `28 17 40 f9` | ldr x8,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-00b7f320"></a> `00b7f320` | `a9 83 5b f8` | ldur x9,[x29, #-0x48] | `FALL_THROUGH`
<a id="insn-00b7f324"></a> `00b7f324` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00b7f328"></a> `00b7f328` | `01 01 00 54` | b.ne 0x00b7f348 | `CONDITIONAL_JUMP`
<a id="insn-00b7f32c"></a> `00b7f32c` | `fd 7b 51 a9` | ldp x29,x30,[sp, #0x110] | `FALL_THROUGH`
<a id="insn-00b7f330"></a> `00b7f330` | `f4 4f 50 a9` | ldp x20,x19,[sp, #0x100] | `FALL_THROUGH`
<a id="insn-00b7f334"></a> `00b7f334` | `f6 57 4f a9` | ldp x22,x21,[sp, #0xf0] | `FALL_THROUGH`
<a id="insn-00b7f338"></a> `00b7f338` | `f8 5f 4e a9` | ldp x24,x23,[sp, #0xe0] | `FALL_THROUGH`
<a id="insn-00b7f33c"></a> `00b7f33c` | `fc 67 4d a9` | ldp x28,x25,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-00b7f340"></a> `00b7f340` | `ff 83 04 91` | add sp,sp,#0x120 | `FALL_THROUGH`
<a id="insn-00b7f344"></a> `00b7f344` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00b7f348"></a> `00b7f348` | `0e 67 03 94` | bl 0x00c58f80 | `CALL_TERMINATOR`
<a id="insn-00b7f34c"></a> `00b7f34c` | `a5 73 03 94` | bl 0x00c5c1e0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b7eedc`](#insn-00b7eedc) 範囲 `[['00b7eedc', '00b7ef23']]`
  - `CONDITIONAL_JUMP` [`00b7ef20`](#insn-00b7ef20) → [`00b7ef74`](#insn-00b7ef74)
  - `FALL_THROUGH` [`00b7ef20`](#insn-00b7ef20) → [`00b7ef24`](#insn-00b7ef24)
- ブロック [`00b7ef24`](#insn-00b7ef24) 範囲 `[['00b7ef24', '00b7ef27']]`
  - `FALL_THROUGH` [`00b7ef24`](#insn-00b7ef24) → [`00b7ef28`](#insn-00b7ef28)
- ブロック [`00b7ef28`](#insn-00b7ef28) 範囲 `[['00b7ef28', '00b7ef37']]`
  - `CONDITIONAL_JUMP` [`00b7ef34`](#insn-00b7ef34) → [`00b7ef48`](#insn-00b7ef48)
  - `FALL_THROUGH` [`00b7ef34`](#insn-00b7ef34) → [`00b7ef38`](#insn-00b7ef38)
- ブロック [`00b7ef38`](#insn-00b7ef38) 範囲 `[['00b7ef38', '00b7ef43']]`
  - `CONDITIONAL_JUMP` [`00b7ef40`](#insn-00b7ef40) → [`00b7ef28`](#insn-00b7ef28)
  - `FALL_THROUGH` [`00b7ef40`](#insn-00b7ef40) → [`00b7ef44`](#insn-00b7ef44)
- ブロック [`00b7ef44`](#insn-00b7ef44) 範囲 `[['00b7ef44', '00b7ef47']]`
  - `UNCONDITIONAL_JUMP` [`00b7ef44`](#insn-00b7ef44) → [`00b7ef74`](#insn-00b7ef74)
- ブロック [`00b7ef48`](#insn-00b7ef48) 範囲 `[['00b7ef48', '00b7ef4f']]`
  - `CONDITIONAL_JUMP` [`00b7ef4c`](#insn-00b7ef4c) → [`00b7ef74`](#insn-00b7ef74)
  - `FALL_THROUGH` [`00b7ef4c`](#insn-00b7ef4c) → [`00b7ef50`](#insn-00b7ef50)
- ブロック [`00b7ef50`](#insn-00b7ef50) 範囲 `[['00b7ef50', '00b7ef5f']]`
  - `CONDITIONAL_JUMP` [`00b7ef5c`](#insn-00b7ef5c) → [`00b7ef74`](#insn-00b7ef74)
  - `FALL_THROUGH` [`00b7ef5c`](#insn-00b7ef5c) → [`00b7ef60`](#insn-00b7ef60)
- ブロック [`00b7ef60`](#insn-00b7ef60) 範囲 `[['00b7ef60', '00b7ef73']]`
  - `UNCONDITIONAL_JUMP` [`00b7ef70`](#insn-00b7ef70) → [`00b7ef84`](#insn-00b7ef84)
- ブロック [`00b7ef74`](#insn-00b7ef74) 範囲 `[['00b7ef74', '00b7ef83']]`
  - `FALL_THROUGH` [`00b7ef80`](#insn-00b7ef80) → [`00b7ef84`](#insn-00b7ef84)
- ブロック [`00b7ef84`](#insn-00b7ef84) 範囲 `[['00b7ef84', '00b7ef97']]`
  - `CONDITIONAL_JUMP` [`00b7ef94`](#insn-00b7ef94) → [`00b7effc`](#insn-00b7effc)
  - `FALL_THROUGH` [`00b7ef94`](#insn-00b7ef94) → [`00b7ef98`](#insn-00b7ef98)
- ブロック [`00b7ef98`](#insn-00b7ef98) 範囲 `[['00b7ef98', '00b7ef9f']]`
  - `CONDITIONAL_JUMP` [`00b7ef9c`](#insn-00b7ef9c) → [`00b7effc`](#insn-00b7effc)
  - `FALL_THROUGH` [`00b7ef9c`](#insn-00b7ef9c) → [`00b7efa0`](#insn-00b7efa0)
- ブロック [`00b7efa0`](#insn-00b7efa0) 範囲 `[['00b7efa0', '00b7efab']]`
  - `CONDITIONAL_JUMP` [`00b7efa8`](#insn-00b7efa8) → [`00b7efbc`](#insn-00b7efbc)
  - `FALL_THROUGH` [`00b7efa8`](#insn-00b7efa8) → [`00b7efac`](#insn-00b7efac)
- ブロック [`00b7efac`](#insn-00b7efac) 範囲 `[['00b7efac', '00b7efb7']]`
  - `CONDITIONAL_JUMP` [`00b7efb4`](#insn-00b7efb4) → [`00b7f314`](#insn-00b7f314)
  - `FALL_THROUGH` [`00b7efb4`](#insn-00b7efb4) → [`00b7efb8`](#insn-00b7efb8)
- ブロック [`00b7efb8`](#insn-00b7efb8) 範囲 `[['00b7efb8', '00b7efbb']]`
  - `FALL_THROUGH` [`00b7efb8`](#insn-00b7efb8) → [`00b7efbc`](#insn-00b7efbc)
- ブロック [`00b7efbc`](#insn-00b7efbc) 範囲 `[['00b7efbc', '00b7efd7']]`
  - `CONDITIONAL_JUMP` [`00b7efd4`](#insn-00b7efd4) → [`00b7f34c`](#insn-00b7f34c)
  - `FALL_THROUGH` [`00b7efd4`](#insn-00b7efd4) → [`00b7efd8`](#insn-00b7efd8)
- ブロック [`00b7efd8`](#insn-00b7efd8) 範囲 `[['00b7efd8', '00b7efe3']]`
  - `CONDITIONAL_JUMP` [`00b7efe0`](#insn-00b7efe0) → [`00b7f148`](#insn-00b7f148)
  - `FALL_THROUGH` [`00b7efe0`](#insn-00b7efe0) → [`00b7efe4`](#insn-00b7efe4)
- ブロック [`00b7efe4`](#insn-00b7efe4) 範囲 `[['00b7efe4', '00b7eff7']]`
  - `CONDITIONAL_JUMP` [`00b7eff4`](#insn-00b7eff4) → [`00b7f168`](#insn-00b7f168)
  - `FALL_THROUGH` [`00b7eff4`](#insn-00b7eff4) → [`00b7eff8`](#insn-00b7eff8)
- ブロック [`00b7eff8`](#insn-00b7eff8) 範囲 `[['00b7eff8', '00b7effb']]`
  - `UNCONDITIONAL_JUMP` [`00b7eff8`](#insn-00b7eff8) → [`00b7f178`](#insn-00b7f178)
- ブロック [`00b7effc`](#insn-00b7effc) 範囲 `[['00b7effc', '00b7f017']]`
  - `CONDITIONAL_JUMP` [`00b7f014`](#insn-00b7f014) → [`00b7f34c`](#insn-00b7f34c)
  - `FALL_THROUGH` [`00b7f014`](#insn-00b7f014) → [`00b7f018`](#insn-00b7f018)
- ブロック [`00b7f018`](#insn-00b7f018) 範囲 `[['00b7f018', '00b7f023']]`
  - `CONDITIONAL_JUMP` [`00b7f020`](#insn-00b7f020) → [`00b7f03c`](#insn-00b7f03c)
  - `FALL_THROUGH` [`00b7f020`](#insn-00b7f020) → [`00b7f024`](#insn-00b7f024)
- ブロック [`00b7f024`](#insn-00b7f024) 範囲 `[['00b7f024', '00b7f037']]`
  - `CONDITIONAL_JUMP` [`00b7f034`](#insn-00b7f034) → [`00b7f05c`](#insn-00b7f05c)
  - `FALL_THROUGH` [`00b7f034`](#insn-00b7f034) → [`00b7f038`](#insn-00b7f038)
- ブロック [`00b7f038`](#insn-00b7f038) 範囲 `[['00b7f038', '00b7f03b']]`
  - `UNCONDITIONAL_JUMP` [`00b7f038`](#insn-00b7f038) → [`00b7f06c`](#insn-00b7f06c)
- ブロック [`00b7f03c`](#insn-00b7f03c) 範囲 `[['00b7f03c', '00b7f05b']]`
  - `FALL_THROUGH` [`00b7f058`](#insn-00b7f058) → [`00b7f05c`](#insn-00b7f05c)
- ブロック [`00b7f05c`](#insn-00b7f05c) 範囲 `[['00b7f05c', '00b7f06b']]`
  - `FALL_THROUGH` [`00b7f068`](#insn-00b7f068) → [`00b7f06c`](#insn-00b7f06c)
- ブロック [`00b7f06c`](#insn-00b7f06c) 範囲 `[['00b7f06c', '00b7f077']]`
  - `FALL_THROUGH` [`00b7f074`](#insn-00b7f074) → [`00b7f078`](#insn-00b7f078)
- ブロック [`00b7f078`](#insn-00b7f078) 範囲 `[['00b7f078', '00b7f0e7']]`
  - `FALL_THROUGH` [`00b7f0e4`](#insn-00b7f0e4) → [`00b7f0e8`](#insn-00b7f0e8)
- ブロック [`00b7f0e8`](#insn-00b7f0e8) 範囲 `[['00b7f0e8', '00b7f0f7']]`
  - `CONDITIONAL_JUMP` [`00b7f0f4`](#insn-00b7f0f4) → [`00b7f100`](#insn-00b7f100)
  - `FALL_THROUGH` [`00b7f0f4`](#insn-00b7f0f4) → [`00b7f0f8`](#insn-00b7f0f8)
- ブロック [`00b7f0f8`](#insn-00b7f0f8) 範囲 `[['00b7f0f8', '00b7f0ff']]`
  - `FALL_THROUGH` [`00b7f0fc`](#insn-00b7f0fc) → [`00b7f100`](#insn-00b7f100)
- ブロック [`00b7f100`](#insn-00b7f100) 範囲 `[['00b7f100', '00b7f10b']]`
  - `CONDITIONAL_JUMP` [`00b7f108`](#insn-00b7f108) → [`00b7f120`](#insn-00b7f120)
  - `FALL_THROUGH` [`00b7f108`](#insn-00b7f108) → [`00b7f10c`](#insn-00b7f10c)
- ブロック [`00b7f10c`](#insn-00b7f10c) 範囲 `[['00b7f10c', '00b7f113']]`
  - `CONDITIONAL_JUMP` [`00b7f110`](#insn-00b7f110) → [`00b7f130`](#insn-00b7f130)
  - `FALL_THROUGH` [`00b7f110`](#insn-00b7f110) → [`00b7f114`](#insn-00b7f114)
- ブロック [`00b7f114`](#insn-00b7f114) 範囲 `[['00b7f114', '00b7f11b']]`
  - `CONDITIONAL_JUMP` [`00b7f118`](#insn-00b7f118) → [`00b7f140`](#insn-00b7f140)
  - `FALL_THROUGH` [`00b7f118`](#insn-00b7f118) → [`00b7f11c`](#insn-00b7f11c)
- ブロック [`00b7f11c`](#insn-00b7f11c) 範囲 `[['00b7f11c', '00b7f11f']]`
  - `UNCONDITIONAL_JUMP` [`00b7f11c`](#insn-00b7f11c) → [`00b7f31c`](#insn-00b7f31c)
- ブロック [`00b7f120`](#insn-00b7f120) 範囲 `[['00b7f120', '00b7f12f']]`
  - `CONDITIONAL_JUMP` [`00b7f12c`](#insn-00b7f12c) → [`00b7f114`](#insn-00b7f114)
  - `FALL_THROUGH` [`00b7f12c`](#insn-00b7f12c) → [`00b7f130`](#insn-00b7f130)
- ブロック [`00b7f130`](#insn-00b7f130) 範囲 `[['00b7f130', '00b7f13f']]`
  - `CONDITIONAL_JUMP` [`00b7f13c`](#insn-00b7f13c) → [`00b7f31c`](#insn-00b7f31c)
  - `FALL_THROUGH` [`00b7f13c`](#insn-00b7f13c) → [`00b7f140`](#insn-00b7f140)
- ブロック [`00b7f140`](#insn-00b7f140) 範囲 `[['00b7f140', '00b7f147']]`
  - `UNCONDITIONAL_JUMP` [`00b7f144`](#insn-00b7f144) → [`00b7f30c`](#insn-00b7f30c)
- ブロック [`00b7f148`](#insn-00b7f148) 範囲 `[['00b7f148', '00b7f167']]`
  - `FALL_THROUGH` [`00b7f164`](#insn-00b7f164) → [`00b7f168`](#insn-00b7f168)
- ブロック [`00b7f168`](#insn-00b7f168) 範囲 `[['00b7f168', '00b7f16b']]`
  - `FALL_THROUGH` [`00b7f168`](#insn-00b7f168) → [`00b7f16c`](#insn-00b7f16c)
- ブロック [`00b7f16c`](#insn-00b7f16c) 範囲 `[['00b7f16c', '00b7f177']]`
  - `FALL_THROUGH` [`00b7f174`](#insn-00b7f174) → [`00b7f178`](#insn-00b7f178)
- ブロック [`00b7f178`](#insn-00b7f178) 範囲 `[['00b7f178', '00b7f277']]`
  - `CONDITIONAL_JUMP` [`00b7f274`](#insn-00b7f274) → [`00b7f280`](#insn-00b7f280)
  - `FALL_THROUGH` [`00b7f274`](#insn-00b7f274) → [`00b7f278`](#insn-00b7f278)
- ブロック [`00b7f278`](#insn-00b7f278) 範囲 `[['00b7f278', '00b7f27f']]`
  - `FALL_THROUGH` [`00b7f27c`](#insn-00b7f27c) → [`00b7f280`](#insn-00b7f280)
- ブロック [`00b7f280`](#insn-00b7f280) 範囲 `[['00b7f280', '00b7f28b']]`
  - `CONDITIONAL_JUMP` [`00b7f288`](#insn-00b7f288) → [`00b7f2b8`](#insn-00b7f2b8)
  - `FALL_THROUGH` [`00b7f288`](#insn-00b7f288) → [`00b7f28c`](#insn-00b7f28c)
- ブロック [`00b7f28c`](#insn-00b7f28c) 範囲 `[['00b7f28c', '00b7f293']]`
  - `CONDITIONAL_JUMP` [`00b7f290`](#insn-00b7f290) → [`00b7f2c8`](#insn-00b7f2c8)
  - `FALL_THROUGH` [`00b7f290`](#insn-00b7f290) → [`00b7f294`](#insn-00b7f294)
- ブロック [`00b7f294`](#insn-00b7f294) 範囲 `[['00b7f294', '00b7f29b']]`
  - `CONDITIONAL_JUMP` [`00b7f298`](#insn-00b7f298) → [`00b7f2d8`](#insn-00b7f2d8)
  - `FALL_THROUGH` [`00b7f298`](#insn-00b7f298) → [`00b7f29c`](#insn-00b7f29c)
- ブロック [`00b7f29c`](#insn-00b7f29c) 範囲 `[['00b7f29c', '00b7f2a3']]`
  - `CONDITIONAL_JUMP` [`00b7f2a0`](#insn-00b7f2a0) → [`00b7f2e8`](#insn-00b7f2e8)
  - `FALL_THROUGH` [`00b7f2a0`](#insn-00b7f2a0) → [`00b7f2a4`](#insn-00b7f2a4)
- ブロック [`00b7f2a4`](#insn-00b7f2a4) 範囲 `[['00b7f2a4', '00b7f2ab']]`
  - `CONDITIONAL_JUMP` [`00b7f2a8`](#insn-00b7f2a8) → [`00b7f2f8`](#insn-00b7f2f8)
  - `FALL_THROUGH` [`00b7f2a8`](#insn-00b7f2a8) → [`00b7f2ac`](#insn-00b7f2ac)
- ブロック [`00b7f2ac`](#insn-00b7f2ac) 範囲 `[['00b7f2ac', '00b7f2b3']]`
  - `CONDITIONAL_JUMP` [`00b7f2b0`](#insn-00b7f2b0) → [`00b7f308`](#insn-00b7f308)
  - `FALL_THROUGH` [`00b7f2b0`](#insn-00b7f2b0) → [`00b7f2b4`](#insn-00b7f2b4)
- ブロック [`00b7f2b4`](#insn-00b7f2b4) 範囲 `[['00b7f2b4', '00b7f2b7']]`
  - `UNCONDITIONAL_JUMP` [`00b7f2b4`](#insn-00b7f2b4) → [`00b7f31c`](#insn-00b7f31c)
- ブロック [`00b7f2b8`](#insn-00b7f2b8) 範囲 `[['00b7f2b8', '00b7f2c7']]`
  - `CONDITIONAL_JUMP` [`00b7f2c4`](#insn-00b7f2c4) → [`00b7f294`](#insn-00b7f294)
  - `FALL_THROUGH` [`00b7f2c4`](#insn-00b7f2c4) → [`00b7f2c8`](#insn-00b7f2c8)
- ブロック [`00b7f2c8`](#insn-00b7f2c8) 範囲 `[['00b7f2c8', '00b7f2d7']]`
  - `CONDITIONAL_JUMP` [`00b7f2d4`](#insn-00b7f2d4) → [`00b7f29c`](#insn-00b7f29c)
  - `FALL_THROUGH` [`00b7f2d4`](#insn-00b7f2d4) → [`00b7f2d8`](#insn-00b7f2d8)
- ブロック [`00b7f2d8`](#insn-00b7f2d8) 範囲 `[['00b7f2d8', '00b7f2e7']]`
  - `CONDITIONAL_JUMP` [`00b7f2e4`](#insn-00b7f2e4) → [`00b7f2a4`](#insn-00b7f2a4)
  - `FALL_THROUGH` [`00b7f2e4`](#insn-00b7f2e4) → [`00b7f2e8`](#insn-00b7f2e8)
- ブロック [`00b7f2e8`](#insn-00b7f2e8) 範囲 `[['00b7f2e8', '00b7f2f7']]`
  - `CONDITIONAL_JUMP` [`00b7f2f4`](#insn-00b7f2f4) → [`00b7f2ac`](#insn-00b7f2ac)
  - `FALL_THROUGH` [`00b7f2f4`](#insn-00b7f2f4) → [`00b7f2f8`](#insn-00b7f2f8)
- ブロック [`00b7f2f8`](#insn-00b7f2f8) 範囲 `[['00b7f2f8', '00b7f307']]`
  - `CONDITIONAL_JUMP` [`00b7f304`](#insn-00b7f304) → [`00b7f31c`](#insn-00b7f31c)
  - `FALL_THROUGH` [`00b7f304`](#insn-00b7f304) → [`00b7f308`](#insn-00b7f308)
- ブロック [`00b7f308`](#insn-00b7f308) 範囲 `[['00b7f308', '00b7f30b']]`
  - `FALL_THROUGH` [`00b7f308`](#insn-00b7f308) → [`00b7f30c`](#insn-00b7f30c)
- ブロック [`00b7f30c`](#insn-00b7f30c) 範囲 `[['00b7f30c', '00b7f313']]`
  - `UNCONDITIONAL_JUMP` [`00b7f310`](#insn-00b7f310) → [`00b7f31c`](#insn-00b7f31c)
- ブロック [`00b7f314`](#insn-00b7f314) 範囲 `[['00b7f314', '00b7f31b']]`
  - `FALL_THROUGH` [`00b7f318`](#insn-00b7f318) → [`00b7f31c`](#insn-00b7f31c)
- ブロック [`00b7f31c`](#insn-00b7f31c) 範囲 `[['00b7f31c', '00b7f32b']]`
  - `CONDITIONAL_JUMP` [`00b7f328`](#insn-00b7f328) → [`00b7f348`](#insn-00b7f348)
  - `FALL_THROUGH` [`00b7f328`](#insn-00b7f328) → [`00b7f32c`](#insn-00b7f32c)
- ブロック [`00b7f32c`](#insn-00b7f32c) 範囲 `[['00b7f32c', '00b7f347']]`
- ブロック [`00b7f348`](#insn-00b7f348) 範囲 `[['00b7f348', '00b7f34b']]`
- ブロック [`00b7f34c`](#insn-00b7f34c) 範囲 `[['00b7f34c', '00b7f34f']]`

## 命令位置別の参照

- [`00b7eee0`](#insn-00b7eee0) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7eee4`](#insn-00b7eee4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7eee8`](#insn-00b7eee8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7eeec`](#insn-00b7eeec) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7eef0`](#insn-00b7eef0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7ef10`](#insn-00b7ef10) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7ef1c`](#insn-00b7ef1c) → `00c9c8d0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00b7ef20`](#insn-00b7ef20) → [`00b7ef74`](#insn-00b7ef74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7ef34`](#insn-00b7ef34) → [`00b7ef48`](#insn-00b7ef48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7ef40`](#insn-00b7ef40) → [`00b7ef28`](#insn-00b7ef28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7ef44`](#insn-00b7ef44) → [`00b7ef74`](#insn-00b7ef74) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7ef4c`](#insn-00b7ef4c) → [`00b7ef74`](#insn-00b7ef74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7ef5c`](#insn-00b7ef5c) → [`00b7ef74`](#insn-00b7ef74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7ef60`](#insn-00b7ef60) → `011272a0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZN11flatbuffers13ClassicLocale9instance_E` · 推定型 `undefined8`
- [`00b7ef64`](#insn-00b7ef64) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7ef70`](#insn-00b7ef70) → [`00b7ef84`](#insn-00b7ef84) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7ef74`](#insn-00b7ef74) → `011272a0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZN11flatbuffers13ClassicLocale9instance_E` · 推定型 `undefined8`
- [`00b7ef80`](#insn-00b7ef80) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7ef88`](#insn-00b7ef88) → [`00c5e1f0`](../00c5e/00c5e1f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e1f0` · 推定シンボル `None` · 推定型 `None`
- [`00b7ef8c`](#insn-00b7ef8c) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7ef94`](#insn-00b7ef94) → [`00b7effc`](#insn-00b7effc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7ef9c`](#insn-00b7ef9c) → [`00b7effc`](#insn-00b7effc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7efa8`](#insn-00b7efa8) → [`00b7efbc`](#insn-00b7efbc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7efb4`](#insn-00b7efb4) → [`00b7f314`](#insn-00b7f314) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7efc4`](#insn-00b7efc4) → `Stack[-0x100]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7efc8`](#insn-00b7efc8) → `Stack[-0x108]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7efcc`](#insn-00b7efcc) → [`00c59080`](../00c59/00c59080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59080` · 推定シンボル `None` · 推定型 `None`
- [`00b7efd4`](#insn-00b7efd4) → [`00b7f34c`](#insn-00b7f34c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7efe0`](#insn-00b7efe0) → [`00b7f148`](#insn-00b7f148) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7eff0`](#insn-00b7eff0) → `Stack[-0x108]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7eff4`](#insn-00b7eff4) → [`00b7f168`](#insn-00b7f168) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7eff8`](#insn-00b7eff8) → [`00b7f178`](#insn-00b7f178) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7f004`](#insn-00b7f004) → `Stack[-0xc8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7f008`](#insn-00b7f008) → `Stack[-0xd0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7f00c`](#insn-00b7f00c) → [`00c59080`](../00c59/00c59080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59080` · 推定シンボル `None` · 推定型 `None`
- [`00b7f014`](#insn-00b7f014) → [`00b7f34c`](#insn-00b7f34c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7f020`](#insn-00b7f020) → [`00b7f03c`](#insn-00b7f03c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7f030`](#insn-00b7f030) → `Stack[-0xd0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7f034`](#insn-00b7f034) → [`00b7f05c`](#insn-00b7f05c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7f038`](#insn-00b7f038) → [`00b7f06c`](#insn-00b7f06c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7f048`](#insn-00b7f048) → [`00c58f30`](../00c58/00c58f30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f30` · 推定シンボル `None` · 推定型 `None`
- [`00b7f054`](#insn-00b7f054) → `Stack[-0xd0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7f058`](#insn-00b7f058) → `Stack[-0xc0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7f068`](#insn-00b7f068) → [`00c590a0`](../00c59/00c590a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c590a0` · 推定シンボル `None` · 推定型 `None`
- [`00b7f070`](#insn-00b7f070) → `002b6ecb`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b7f084`](#insn-00b7f084) → [`00c5a070`](../00c5a/00c5a070.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a070` · 推定シンボル `None` · 推定型 `None`
- [`00b7f094`](#insn-00b7f094) → `002b5f9c`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7f098`](#insn-00b7f098) → `Stack[-0xb0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7f09c`](#insn-00b7f09c) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7f0b4`](#insn-00b7f0b4) → [`00c59020`](../00c59/00c59020.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59020` · 推定シンボル `None` · 推定型 `None`
- [`00b7f0c4`](#insn-00b7f0c4) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7f0c8`](#insn-00b7f0c8) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7f0d8`](#insn-00b7f0d8) → `002a0ba9`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b7f0e0`](#insn-00b7f0e0) → [`00c59150`](../00c59/00c59150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59150` · 推定シンボル `None` · 推定型 `None`
- [`00b7f0ec`](#insn-00b7f0ec) → [`00c5d810`](../00c5d/00c5d810.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d810` · 推定シンボル `None` · 推定型 `None`
- [`00b7f0f0`](#insn-00b7f0f0) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7f0f4`](#insn-00b7f0f4) → [`00b7f100`](#insn-00b7f100) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7f0f8`](#insn-00b7f0f8) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7f0fc`](#insn-00b7f0fc) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00b7f100`](#insn-00b7f100) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7f108`](#insn-00b7f108) → [`00b7f120`](#insn-00b7f120) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7f10c`](#insn-00b7f10c) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7f110`](#insn-00b7f110) → [`00b7f130`](#insn-00b7f130) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7f114`](#insn-00b7f114) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7f118`](#insn-00b7f118) → [`00b7f140`](#insn-00b7f140) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7f11c`](#insn-00b7f11c) → [`00b7f31c`](#insn-00b7f31c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7f120`](#insn-00b7f120) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7f124`](#insn-00b7f124) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00b7f128`](#insn-00b7f128) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7f12c`](#insn-00b7f12c) → [`00b7f114`](#insn-00b7f114) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7f130`](#insn-00b7f130) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7f134`](#insn-00b7f134) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00b7f138`](#insn-00b7f138) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7f13c`](#insn-00b7f13c) → [`00b7f31c`](#insn-00b7f31c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7f140`](#insn-00b7f140) → `Stack[-0xc0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7f144`](#insn-00b7f144) → [`00b7f30c`](#insn-00b7f30c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7f154`](#insn-00b7f154) → [`00c58f30`](../00c58/00c58f30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f30` · 推定シンボル `None` · 推定型 `None`
- [`00b7f160`](#insn-00b7f160) → `Stack[-0x108]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7f164`](#insn-00b7f164) → `Stack[-0xf8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7f174`](#insn-00b7f174) → [`00c590a0`](../00c59/00c590a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c590a0` · 推定シンボル `None` · 推定型 `None`
- [`00b7f17c`](#insn-00b7f17c) → `002b6ecb`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b7f190`](#insn-00b7f190) → [`00c5a070`](../00c5a/00c5a070.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a070` · 推定シンボル `None` · 推定型 `None`
- [`00b7f1a0`](#insn-00b7f1a0) → `002b5f9c`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7f1a4`](#insn-00b7f1a4) → `Stack[-0xf0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7f1a8`](#insn-00b7f1a8) → `Stack[-0xe0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7f1c0`](#insn-00b7f1c0) → [`00c59020`](../00c59/00c59020.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59020` · 推定シンボル `None` · 推定型 `None`
- [`00b7f1d0`](#insn-00b7f1d0) → `002a1bae`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b7f1d4`](#insn-00b7f1d4) → `Stack[-0xd0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7f1d8`](#insn-00b7f1d8) → `Stack[-0xc0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7f1ec`](#insn-00b7f1ec) → [`00c59020`](../00c59/00c59020.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59020` · 推定シンボル `None` · 推定型 `None`
- [`00b7f1fc`](#insn-00b7f1fc) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7f204`](#insn-00b7f204) → `Stack[-0xb0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7f210`](#insn-00b7f210) → [`00b99610`](../00b99/00b99610.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00b99610` · 推定シンボル `None` · 推定型 `None`
- [`00b7f214`](#insn-00b7f214) → `Stack[-0x120]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7f218`](#insn-00b7f218) → `Stack[-0x118]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7f234`](#insn-00b7f234) → [`00c59020`](../00c59/00c59020.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59020` · 推定シンボル `None` · 推定型 `None`
- [`00b7f244`](#insn-00b7f244) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7f248`](#insn-00b7f248) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7f258`](#insn-00b7f258) → `002a0ba9`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b7f260`](#insn-00b7f260) → [`00c59150`](../00c59/00c59150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59150` · 推定シンボル `None` · 推定型 `None`
- [`00b7f26c`](#insn-00b7f26c) → [`00c5d810`](../00c5d/00c5d810.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d810` · 推定シンボル `None` · 推定型 `None`
- [`00b7f270`](#insn-00b7f270) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7f274`](#insn-00b7f274) → [`00b7f280`](#insn-00b7f280) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7f278`](#insn-00b7f278) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7f27c`](#insn-00b7f27c) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00b7f280`](#insn-00b7f280) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7f288`](#insn-00b7f288) → [`00b7f2b8`](#insn-00b7f2b8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7f28c`](#insn-00b7f28c) → `Stack[-0x120]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7f290`](#insn-00b7f290) → [`00b7f2c8`](#insn-00b7f2c8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7f294`](#insn-00b7f294) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7f298`](#insn-00b7f298) → [`00b7f2d8`](#insn-00b7f2d8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7f29c`](#insn-00b7f29c) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7f2a0`](#insn-00b7f2a0) → [`00b7f2e8`](#insn-00b7f2e8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7f2a4`](#insn-00b7f2a4) → `Stack[-0xf0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7f2a8`](#insn-00b7f2a8) → [`00b7f2f8`](#insn-00b7f2f8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7f2ac`](#insn-00b7f2ac) → `Stack[-0x108]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7f2b0`](#insn-00b7f2b0) → [`00b7f308`](#insn-00b7f308) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7f2b4`](#insn-00b7f2b4) → [`00b7f31c`](#insn-00b7f31c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7f2b8`](#insn-00b7f2b8) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7f2bc`](#insn-00b7f2bc) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00b7f2c0`](#insn-00b7f2c0) → `Stack[-0x120]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7f2c4`](#insn-00b7f2c4) → [`00b7f294`](#insn-00b7f294) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7f2c8`](#insn-00b7f2c8) → `Stack[-0x110]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7f2cc`](#insn-00b7f2cc) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00b7f2d0`](#insn-00b7f2d0) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7f2d4`](#insn-00b7f2d4) → [`00b7f29c`](#insn-00b7f29c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7f2d8`](#insn-00b7f2d8) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7f2dc`](#insn-00b7f2dc) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00b7f2e0`](#insn-00b7f2e0) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7f2e4`](#insn-00b7f2e4) → [`00b7f2a4`](#insn-00b7f2a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7f2e8`](#insn-00b7f2e8) → `Stack[-0xc0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7f2ec`](#insn-00b7f2ec) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00b7f2f0`](#insn-00b7f2f0) → `Stack[-0xf0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7f2f4`](#insn-00b7f2f4) → [`00b7f2ac`](#insn-00b7f2ac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7f2f8`](#insn-00b7f2f8) → `Stack[-0xe0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7f2fc`](#insn-00b7f2fc) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00b7f300`](#insn-00b7f300) → `Stack[-0x108]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7f304`](#insn-00b7f304) → [`00b7f31c`](#insn-00b7f31c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7f308`](#insn-00b7f308) → `Stack[-0xf8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7f30c`](#insn-00b7f30c) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00b7f310`](#insn-00b7f310) → [`00b7f31c`](#insn-00b7f31c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7f320`](#insn-00b7f320) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7f328`](#insn-00b7f328) → [`00b7f348`](#insn-00b7f348) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7f32c`](#insn-00b7f32c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7f330`](#insn-00b7f330) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7f334`](#insn-00b7f334) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7f338`](#insn-00b7f338) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7f33c`](#insn-00b7f33c) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7f348`](#insn-00b7f348) → [`00c58f80`](../00c58/00c58f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f80` · 推定シンボル `None` · 推定型 `None`
- [`00b7f34c`](#insn-00b7f34c) → [`00c5c1e0`](../00c5c/00c5c1e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c1e0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b7eee0`](#insn-00b7eee0)

~~~json
{
  "source": "00b7eee0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7eee4`](#insn-00b7eee4)

~~~json
{
  "source": "00b7eee4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7eee8`](#insn-00b7eee8)

~~~json
{
  "source": "00b7eee8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7eeec`](#insn-00b7eeec)

~~~json
{
  "source": "00b7eeec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7eef0`](#insn-00b7eef0)

~~~json
{
  "source": "00b7eef0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7ef10`](#insn-00b7ef10)

~~~json
{
  "source": "00b7ef10",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7ef1c`](#insn-00b7ef1c)

~~~json
{
  "source": "00b7ef1c",
  "target": "00c9c8d0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9c8d0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00b7ef20`](#insn-00b7ef20)

~~~json
{
  "source": "00b7ef20",
  "target": "00b7ef74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7ef34`](#insn-00b7ef34)

~~~json
{
  "source": "00b7ef34",
  "target": "00b7ef48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7ef40`](#insn-00b7ef40)

~~~json
{
  "source": "00b7ef40",
  "target": "00b7ef28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7ef44`](#insn-00b7ef44)

~~~json
{
  "source": "00b7ef44",
  "target": "00b7ef74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7ef4c`](#insn-00b7ef4c)

~~~json
{
  "source": "00b7ef4c",
  "target": "00b7ef74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7ef5c`](#insn-00b7ef5c)

~~~json
{
  "source": "00b7ef5c",
  "target": "00b7ef74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7ef60`](#insn-00b7ef60)

~~~json
{
  "source": "00b7ef60",
  "target": "011272a0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011272a0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b7ef64`](#insn-00b7ef64)

~~~json
{
  "source": "00b7ef64",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7ef70`](#insn-00b7ef70)

~~~json
{
  "source": "00b7ef70",
  "target": "00b7ef84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7ef74`](#insn-00b7ef74)

~~~json
{
  "source": "00b7ef74",
  "target": "011272a0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011272a0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b7ef80`](#insn-00b7ef80)

~~~json
{
  "source": "00b7ef80",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7ef88`](#insn-00b7ef88)

~~~json
{
  "source": "00b7ef88",
  "target": "00c5e1f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b7ef8c`](#insn-00b7ef8c)

~~~json
{
  "source": "00b7ef8c",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7ef94`](#insn-00b7ef94)

~~~json
{
  "source": "00b7ef94",
  "target": "00b7effc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7ef9c`](#insn-00b7ef9c)

~~~json
{
  "source": "00b7ef9c",
  "target": "00b7effc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7efa8`](#insn-00b7efa8)

~~~json
{
  "source": "00b7efa8",
  "target": "00b7efbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7efb4`](#insn-00b7efb4)

~~~json
{
  "source": "00b7efb4",
  "target": "00b7f314",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7efc4`](#insn-00b7efc4)

~~~json
{
  "source": "00b7efc4",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7efc8`](#insn-00b7efc8)

~~~json
{
  "source": "00b7efc8",
  "target": "Stack[-0x108]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7efcc`](#insn-00b7efcc)

~~~json
{
  "source": "00b7efcc",
  "target": "00c59080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b7efd4`](#insn-00b7efd4)

~~~json
{
  "source": "00b7efd4",
  "target": "00b7f34c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7efe0`](#insn-00b7efe0)

~~~json
{
  "source": "00b7efe0",
  "target": "00b7f148",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7eff0`](#insn-00b7eff0)

~~~json
{
  "source": "00b7eff0",
  "target": "Stack[-0x108]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7eff4`](#insn-00b7eff4)

~~~json
{
  "source": "00b7eff4",
  "target": "00b7f168",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7eff8`](#insn-00b7eff8)

~~~json
{
  "source": "00b7eff8",
  "target": "00b7f178",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7f004`](#insn-00b7f004)

~~~json
{
  "source": "00b7f004",
  "target": "Stack[-0xc8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7f008`](#insn-00b7f008)

~~~json
{
  "source": "00b7f008",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7f00c`](#insn-00b7f00c)

~~~json
{
  "source": "00b7f00c",
  "target": "00c59080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b7f014`](#insn-00b7f014)

~~~json
{
  "source": "00b7f014",
  "target": "00b7f34c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7f020`](#insn-00b7f020)

~~~json
{
  "source": "00b7f020",
  "target": "00b7f03c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7f030`](#insn-00b7f030)

~~~json
{
  "source": "00b7f030",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7f034`](#insn-00b7f034)

~~~json
{
  "source": "00b7f034",
  "target": "00b7f05c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7f038`](#insn-00b7f038)

~~~json
{
  "source": "00b7f038",
  "target": "00b7f06c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7f048`](#insn-00b7f048)

~~~json
{
  "source": "00b7f048",
  "target": "00c58f30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b7f054`](#insn-00b7f054)

~~~json
{
  "source": "00b7f054",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7f058`](#insn-00b7f058)

~~~json
{
  "source": "00b7f058",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7f068`](#insn-00b7f068)

~~~json
{
  "source": "00b7f068",
  "target": "00c590a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b7f070`](#insn-00b7f070)

~~~json
{
  "source": "00b7f070",
  "target": "002b6ecb",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b6ecb",
  "offset": 0,
  "size": 18,
  "datatype": "string",
  "bytes": "696e76616c6964206e756d6265723a202200",
  "capture_start": "002b6ecb",
  "capture_bytes": 18,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b7f084`](#insn-00b7f084)

~~~json
{
  "source": "00b7f084",
  "target": "00c5a070",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b7f094`](#insn-00b7f094)

~~~json
{
  "source": "00b7f094",
  "target": "002b5f9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7f098`](#insn-00b7f098)

~~~json
{
  "source": "00b7f098",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7f09c`](#insn-00b7f09c)

~~~json
{
  "source": "00b7f09c",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7f0b4`](#insn-00b7f0b4)

~~~json
{
  "source": "00b7f0b4",
  "target": "00c59020",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b7f0c4`](#insn-00b7f0c4)

~~~json
{
  "source": "00b7f0c4",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7f0c8`](#insn-00b7f0c8)

~~~json
{
  "source": "00b7f0c8",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7f0d8`](#insn-00b7f0d8)

~~~json
{
  "source": "00b7f0d8",
  "target": "002a0ba9",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a0ba9",
  "offset": 0,
  "size": 8,
  "datatype": "string",
  "bytes": "6572726f723a2000",
  "capture_start": "002a0ba9",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b7f0e0`](#insn-00b7f0e0)

~~~json
{
  "source": "00b7f0e0",
  "target": "00c59150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b7f0ec`](#insn-00b7f0ec)

~~~json
{
  "source": "00b7f0ec",
  "target": "00c5d810",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b7f0f0`](#insn-00b7f0f0)

~~~json
{
  "source": "00b7f0f0",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7f0f4`](#insn-00b7f0f4)

~~~json
{
  "source": "00b7f0f4",
  "target": "00b7f100",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7f0f8`](#insn-00b7f0f8)

~~~json
{
  "source": "00b7f0f8",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7f0fc`](#insn-00b7f0fc)

~~~json
{
  "source": "00b7f0fc",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b7f100`](#insn-00b7f100)

~~~json
{
  "source": "00b7f100",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7f108`](#insn-00b7f108)

~~~json
{
  "source": "00b7f108",
  "target": "00b7f120",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7f10c`](#insn-00b7f10c)

~~~json
{
  "source": "00b7f10c",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7f110`](#insn-00b7f110)

~~~json
{
  "source": "00b7f110",
  "target": "00b7f130",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7f114`](#insn-00b7f114)

~~~json
{
  "source": "00b7f114",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7f118`](#insn-00b7f118)

~~~json
{
  "source": "00b7f118",
  "target": "00b7f140",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7f11c`](#insn-00b7f11c)

~~~json
{
  "source": "00b7f11c",
  "target": "00b7f31c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7f120`](#insn-00b7f120)

~~~json
{
  "source": "00b7f120",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7f124`](#insn-00b7f124)

~~~json
{
  "source": "00b7f124",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b7f128`](#insn-00b7f128)

~~~json
{
  "source": "00b7f128",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7f12c`](#insn-00b7f12c)

~~~json
{
  "source": "00b7f12c",
  "target": "00b7f114",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7f130`](#insn-00b7f130)

~~~json
{
  "source": "00b7f130",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7f134`](#insn-00b7f134)

~~~json
{
  "source": "00b7f134",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b7f138`](#insn-00b7f138)

~~~json
{
  "source": "00b7f138",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7f13c`](#insn-00b7f13c)

~~~json
{
  "source": "00b7f13c",
  "target": "00b7f31c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7f140`](#insn-00b7f140)

~~~json
{
  "source": "00b7f140",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7f144`](#insn-00b7f144)

~~~json
{
  "source": "00b7f144",
  "target": "00b7f30c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7f154`](#insn-00b7f154)

~~~json
{
  "source": "00b7f154",
  "target": "00c58f30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b7f160`](#insn-00b7f160)

~~~json
{
  "source": "00b7f160",
  "target": "Stack[-0x108]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7f164`](#insn-00b7f164)

~~~json
{
  "source": "00b7f164",
  "target": "Stack[-0xf8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7f174`](#insn-00b7f174)

~~~json
{
  "source": "00b7f174",
  "target": "00c590a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b7f17c`](#insn-00b7f17c)

~~~json
{
  "source": "00b7f17c",
  "target": "002b6ecb",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b6ecb",
  "offset": 0,
  "size": 18,
  "datatype": "string",
  "bytes": "696e76616c6964206e756d6265723a202200",
  "capture_start": "002b6ecb",
  "capture_bytes": 18,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b7f190`](#insn-00b7f190)

~~~json
{
  "source": "00b7f190",
  "target": "00c5a070",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b7f1a0`](#insn-00b7f1a0)

~~~json
{
  "source": "00b7f1a0",
  "target": "002b5f9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7f1a4`](#insn-00b7f1a4)

~~~json
{
  "source": "00b7f1a4",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7f1a8`](#insn-00b7f1a8)

~~~json
{
  "source": "00b7f1a8",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7f1c0`](#insn-00b7f1c0)

~~~json
{
  "source": "00b7f1c0",
  "target": "00c59020",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b7f1d0`](#insn-00b7f1d0)

~~~json
{
  "source": "00b7f1d0",
  "target": "002a1bae",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a1bae",
  "offset": 0,
  "size": 25,
  "datatype": "string",
  "bytes": "2c20636f6e7374616e7420646f6573206e6f74206669742000",
  "capture_start": "002a1bae",
  "capture_bytes": 25,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b7f1d4`](#insn-00b7f1d4)

~~~json
{
  "source": "00b7f1d4",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7f1d8`](#insn-00b7f1d8)

~~~json
{
  "source": "00b7f1d8",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7f1ec`](#insn-00b7f1ec)

~~~json
{
  "source": "00b7f1ec",
  "target": "00c59020",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b7f1fc`](#insn-00b7f1fc)

~~~json
{
  "source": "00b7f1fc",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7f204`](#insn-00b7f204)

~~~json
{
  "source": "00b7f204",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7f210`](#insn-00b7f210)

~~~json
{
  "source": "00b7f210",
  "target": "00b99610",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b7f214`](#insn-00b7f214)

~~~json
{
  "source": "00b7f214",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7f218`](#insn-00b7f218)

~~~json
{
  "source": "00b7f218",
  "target": "Stack[-0x118]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7f234`](#insn-00b7f234)

~~~json
{
  "source": "00b7f234",
  "target": "00c59020",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b7f244`](#insn-00b7f244)

~~~json
{
  "source": "00b7f244",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7f248`](#insn-00b7f248)

~~~json
{
  "source": "00b7f248",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7f258`](#insn-00b7f258)

~~~json
{
  "source": "00b7f258",
  "target": "002a0ba9",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a0ba9",
  "offset": 0,
  "size": 8,
  "datatype": "string",
  "bytes": "6572726f723a2000",
  "capture_start": "002a0ba9",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b7f260`](#insn-00b7f260)

~~~json
{
  "source": "00b7f260",
  "target": "00c59150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b7f26c`](#insn-00b7f26c)

~~~json
{
  "source": "00b7f26c",
  "target": "00c5d810",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b7f270`](#insn-00b7f270)

~~~json
{
  "source": "00b7f270",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7f274`](#insn-00b7f274)

~~~json
{
  "source": "00b7f274",
  "target": "00b7f280",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7f278`](#insn-00b7f278)

~~~json
{
  "source": "00b7f278",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7f27c`](#insn-00b7f27c)

~~~json
{
  "source": "00b7f27c",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b7f280`](#insn-00b7f280)

~~~json
{
  "source": "00b7f280",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7f288`](#insn-00b7f288)

~~~json
{
  "source": "00b7f288",
  "target": "00b7f2b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7f28c`](#insn-00b7f28c)

~~~json
{
  "source": "00b7f28c",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7f290`](#insn-00b7f290)

~~~json
{
  "source": "00b7f290",
  "target": "00b7f2c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7f294`](#insn-00b7f294)

~~~json
{
  "source": "00b7f294",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7f298`](#insn-00b7f298)

~~~json
{
  "source": "00b7f298",
  "target": "00b7f2d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7f29c`](#insn-00b7f29c)

~~~json
{
  "source": "00b7f29c",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7f2a0`](#insn-00b7f2a0)

~~~json
{
  "source": "00b7f2a0",
  "target": "00b7f2e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7f2a4`](#insn-00b7f2a4)

~~~json
{
  "source": "00b7f2a4",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7f2a8`](#insn-00b7f2a8)

~~~json
{
  "source": "00b7f2a8",
  "target": "00b7f2f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7f2ac`](#insn-00b7f2ac)

~~~json
{
  "source": "00b7f2ac",
  "target": "Stack[-0x108]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7f2b0`](#insn-00b7f2b0)

~~~json
{
  "source": "00b7f2b0",
  "target": "00b7f308",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7f2b4`](#insn-00b7f2b4)

~~~json
{
  "source": "00b7f2b4",
  "target": "00b7f31c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7f2b8`](#insn-00b7f2b8)

~~~json
{
  "source": "00b7f2b8",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7f2bc`](#insn-00b7f2bc)

~~~json
{
  "source": "00b7f2bc",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b7f2c0`](#insn-00b7f2c0)

~~~json
{
  "source": "00b7f2c0",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7f2c4`](#insn-00b7f2c4)

~~~json
{
  "source": "00b7f2c4",
  "target": "00b7f294",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7f2c8`](#insn-00b7f2c8)

~~~json
{
  "source": "00b7f2c8",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7f2cc`](#insn-00b7f2cc)

~~~json
{
  "source": "00b7f2cc",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b7f2d0`](#insn-00b7f2d0)

~~~json
{
  "source": "00b7f2d0",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7f2d4`](#insn-00b7f2d4)

~~~json
{
  "source": "00b7f2d4",
  "target": "00b7f29c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7f2d8`](#insn-00b7f2d8)

~~~json
{
  "source": "00b7f2d8",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7f2dc`](#insn-00b7f2dc)

~~~json
{
  "source": "00b7f2dc",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b7f2e0`](#insn-00b7f2e0)

~~~json
{
  "source": "00b7f2e0",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7f2e4`](#insn-00b7f2e4)

~~~json
{
  "source": "00b7f2e4",
  "target": "00b7f2a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7f2e8`](#insn-00b7f2e8)

~~~json
{
  "source": "00b7f2e8",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7f2ec`](#insn-00b7f2ec)

~~~json
{
  "source": "00b7f2ec",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b7f2f0`](#insn-00b7f2f0)

~~~json
{
  "source": "00b7f2f0",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7f2f4`](#insn-00b7f2f4)

~~~json
{
  "source": "00b7f2f4",
  "target": "00b7f2ac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7f2f8`](#insn-00b7f2f8)

~~~json
{
  "source": "00b7f2f8",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7f2fc`](#insn-00b7f2fc)

~~~json
{
  "source": "00b7f2fc",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b7f300`](#insn-00b7f300)

~~~json
{
  "source": "00b7f300",
  "target": "Stack[-0x108]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7f304`](#insn-00b7f304)

~~~json
{
  "source": "00b7f304",
  "target": "00b7f31c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7f308`](#insn-00b7f308)

~~~json
{
  "source": "00b7f308",
  "target": "Stack[-0xf8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7f30c`](#insn-00b7f30c)

~~~json
{
  "source": "00b7f30c",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b7f310`](#insn-00b7f310)

~~~json
{
  "source": "00b7f310",
  "target": "00b7f31c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7f320`](#insn-00b7f320)

~~~json
{
  "source": "00b7f320",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7f328`](#insn-00b7f328)

~~~json
{
  "source": "00b7f328",
  "target": "00b7f348",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7f32c`](#insn-00b7f32c)

~~~json
{
  "source": "00b7f32c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7f330`](#insn-00b7f330)

~~~json
{
  "source": "00b7f330",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7f334`](#insn-00b7f334)

~~~json
{
  "source": "00b7f334",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7f338`](#insn-00b7f338)

~~~json
{
  "source": "00b7f338",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7f33c`](#insn-00b7f33c)

~~~json
{
  "source": "00b7f33c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7f348`](#insn-00b7f348)

~~~json
{
  "source": "00b7f348",
  "target": "00c58f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b7f34c`](#insn-00b7f34c)

~~~json
{
  "source": "00b7f34c",
  "target": "00c5c1e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
