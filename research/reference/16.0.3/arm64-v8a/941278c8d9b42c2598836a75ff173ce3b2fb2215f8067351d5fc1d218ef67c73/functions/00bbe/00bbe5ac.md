# 00bbe5ac

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bbd5b8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbd5b8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0035.md#compare-16e79b18999fe0527547bbe14488ee2b)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbe5ac",
  "name": "_ZNSt6__ndk16vectorINS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN8firebase16SafeFutureHandleIvEEEENS5_ISB_EEE21__push_back_slow_pathISB_EEvOT_",
  "size": 420,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "631b46ec5b8ac9767b84ac6aba33b1f78ae0399f9f53c49801f463f3cf8fd0b6",
  "source_text_sha256": "631b46ec5b8ac9767b84ac6aba33b1f78ae0399f9f53c49801f463f3cf8fd0b6",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbe5ac",
        "00bbe74f"
      ]
    ],
    "bytes_sha256": "d7aaa1791fdb242e739dcf9d91fa2fe8013cdd31d50d834c09cb21e12a7e49c5",
    "instruction_count": 105,
    "instruction_bytes": 420,
    "body_bytes": 420,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5e670](../00c5e/00c5e670.md)

## 呼び出し先

- [00c58f30](../00c58/00c58f30.md)
- [00c58f50](../00c58/00c58f50.md)
- [00c5bb30](../00c5b/00c5bb30.md)
- [00c5bdb0](../00c5b/00c5bdb0.md)
- [00c5cd00](../00c5c/00c5cd00.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 4094 bytes

~~~c

void _ZNSt6__ndk16vectorINS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN8firebase16SafeFutureHandleIvEEEENS5_ISB_EEE21__push_back_slow_pathISB_EEvOT_
               (long *param_1,undefined8 *param_2)

{
  ulong uVar1;
  undefined8 *puVar2;
  byte *pbVar3;
  long lVar4;
  long lVar5;
  ulong uVar6;
  byte *pbVar7;
  byte *__ptr;
  undefined8 *puVar8;
  ulong uVar9;
  undefined8 uVar10;
  undefined8 uVar11;
  
  lVar4 = param_1[1] - *param_1 >> 3;
  uVar9 = 0x666666666666666;
  uVar1 = lVar4 * -0x3333333333333333 + 1;
  if (0x666666666666666 < uVar1) {
                    /* WARNING: Subroutine does not return */
    _ZNKSt6__ndk120__vector_base_commonILb1EE20__throw_length_errorEv(param_1);
  }
  lVar5 = param_1[2] - *param_1 >> 3;
  if ((ulong)(lVar5 * -0x3333333333333333) < 0x333333333333333) {
    uVar6 = lVar5 * -0x6666666666666666;
    uVar9 = uVar1;
    if (uVar1 <= uVar6) {
      uVar9 = uVar6;
    }
    if (uVar9 == 0) {
      lVar5 = 0;
      goto LAB_00bbe638;
    }
  }
  lVar5 = _Znwm(uVar9 * 0x28);
LAB_00bbe638:
  uVar11 = param_2[1];
  uVar10 = *param_2;
  puVar8 = (undefined8 *)(lVar5 + lVar4 * 8);
  puVar8[2] = param_2[2];
  puVar8[1] = uVar11;
  *puVar8 = uVar10;
  param_2[1] = 0;
  param_2[2] = 0;
  *param_2 = 0;
  _ZN8firebase12FutureHandleC1EOS0_(puVar8 + 3,param_2 + 3);
  __ptr = (byte *)*param_1;
  pbVar3 = (byte *)param_1[1];
  puVar2 = puVar8 + 5;
  pbVar7 = __ptr;
  if (pbVar3 != __ptr) {
    lVar4 = 0;
    do {
      uVar11 = *(undefined8 *)(pbVar3 + lVar4 + -0x20);
      uVar10 = *(undefined8 *)(pbVar3 + lVar4 + -0x28);
                    /* try { // try from 00bbe690 to 00cbe697 has its CatchHandler @ 00bbe72c */
      *(undefined8 *)((long)puVar8 + lVar4 + -0x18) = *(undefined8 *)(pbVar3 + lVar4 + -0x18);
      *(undefined8 *)((long)puVar8 + lVar4 + -0x20) = uVar11;
      *(undefined8 *)((long)puVar8 + lVar4 + -0x28) = uVar10;
      pbVar7 = pbVar3 + lVar4 + -0x20;
      pbVar7[0] = 0;
      pbVar7[1] = 0;
      pbVar7[2] = 0;
      pbVar7[3] = 0;
      pbVar7[4] = 0;
      pbVar7[5] = 0;
      pbVar7[6] = 0;
      pbVar7[7] = 0;
      pbVar7 = pbVar3 + lVar4 + -0x18;
      pbVar7[0] = 0;
      pbVar7[1] = 0;
      pbVar7[2] = 0;
      pbVar7[3] = 0;
      pbVar7[4] = 0;
      pbVar7[5] = 0;
      pbVar7[6] = 0;
      pbVar7[7] = 0;
      pbVar7 = pbVar3 + lVar4 + -0x28;
      pbVar7[0] = 0;
      pbVar7[1] = 0;
      pbVar7[2] = 0;
      pbVar7[3] = 0;
      pbVar7[4] = 0;
      pbVar7[5] = 0;
      pbVar7[6] = 0;
      pbVar7[7] = 0;
      _ZN8firebase12FutureHandleC1EOS0_((long)puVar8 + lVar4 + -0x10,pbVar3 + lVar4 + -0x10);
                    /* try { // try from 00bbe6ac to 00cbe6b3 has its CatchHandler @ 00bbe724 */
      lVar4 = lVar4 + -0x28;
    } while ((long)__ptr - (long)pbVar3 != lVar4);
    __ptr = (byte *)*param_1;
    puVar8 = (undefined8 *)((long)puVar8 + lVar4);
    pbVar7 = (byte *)param_1[1];
  }
  *param_1 = (long)puVar8;
  param_1[1] = (long)puVar2;
  param_1[2] = lVar5 + uVar9 * 0x28;
                    /* try { // try from 00bbe6c8 to 00cbe6cf has its CatchHandler @ 00bbe720 */
  while (pbVar3 = pbVar7, pbVar3 != __ptr) {
    _ZN8firebase12FutureHandleD2Ev(pbVar3 + -0x10);
    pbVar7 = pbVar3 + -0x28;
    if ((*pbVar7 & 1) != 0) {
      _ZdlPv(*(void **)(pbVar3 + -0x18));
                    /* catch() { ... } // from try @ 00bbe414 with catch @ 00bbe704
                       try { // try from 00bbe704 to 00cbe75b has its CatchHandler @ 00bbe340 */
    }
  }
  if (__ptr == (byte *)0x0) {
                    /* catch() { ... } // from try @ 00bbe45c with catch @ 00bbe728 */
                    /* catch() { ... } // from try @ 00bbe690 with catch @ 00bbe72c
                       catch() { ... } // from try @ 00bbe6e4 with catch @ 00bbe72c */
                    /* catch() { ... } // from try @ 00bbe548 with catch @ 00bbe730 */
    return;
  }
                    /* catch() { ... } // from try @ 00bbe6c8 with catch @ 00bbe720 */
                    /* catch() { ... } // from try @ 00bbe6ac with catch @ 00bbe724 */
  _ZdlPv(__ptr);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbe5ac"></a> `00bbe5ac` | `f9 0f 1b f8` | str x25,[sp, #-0x50]! | `FALL_THROUGH`
<a id="insn-00bbe5b0"></a> `00bbe5b0` | `f8 5f 01 a9` | stp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbe5b4"></a> `00bbe5b4` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbe5b8"></a> `00bbe5b8` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bbe5bc"></a> `00bbe5bc` | `fd 7b 04 a9` | stp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bbe5c0"></a> `00bbe5c0` | `fd 03 01 91` | add x29,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00bbe5c4"></a> `00bbe5c4` | `09 20 40 a9` | ldp x9,x8,[x0] | `FALL_THROUGH`
<a id="insn-00bbe5c8"></a> `00bbe5c8` | `ea e7 02 b2` | orr x10,xzr,#-0x3333333333333334 | `FALL_THROUGH`
<a id="insn-00bbe5cc"></a> `00bbe5cc` | `aa 99 99 f2` | movk x10,#0xcccd | `FALL_THROUGH`
<a id="insn-00bbe5d0"></a> `00bbe5d0` | `f7 e7 03 b2` | orr x23,xzr,#0x6666666666666666 | `FALL_THROUGH`
<a id="insn-00bbe5d4"></a> `00bbe5d4` | `08 01 09 cb` | sub x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbe5d8"></a> `00bbe5d8` | `08 fd 43 93` | asr x8,x8,#0x3 | `FALL_THROUGH`
<a id="insn-00bbe5dc"></a> `00bbe5dc` | `15 7d 0a 9b` | mul x21,x8,x10 | `FALL_THROUGH`
<a id="insn-00bbe5e0"></a> `00bbe5e0` | `d7 cc e0 f2` | movk x23,#0x666, LSL #48 | `FALL_THROUGH`
<a id="insn-00bbe5e4"></a> `00bbe5e4` | `a8 06 00 91` | add x8,x21,#0x1 | `FALL_THROUGH`
<a id="insn-00bbe5e8"></a> `00bbe5e8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bbe5ec"></a> `00bbe5ec` | `1f 01 17 eb` | cmp x8,x23 | `FALL_THROUGH`
<a id="insn-00bbe5f0"></a> `00bbe5f0` | `c8 0a 00 54` | b.hi 0x00bbe748 | `CONDITIONAL_JUMP`
<a id="insn-00bbe5f4"></a> `00bbe5f4` | `6b 0a 40 f9` | ldr x11,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bbe5f8"></a> `00bbe5f8` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00bbe5fc"></a> `00bbe5fc` | `69 01 09 cb` | sub x9,x11,x9 | `FALL_THROUGH`
<a id="insn-00bbe600"></a> `00bbe600` | `29 fd 43 93` | asr x9,x9,#0x3 | `FALL_THROUGH`
<a id="insn-00bbe604"></a> `00bbe604` | `29 7d 0a 9b` | mul x9,x9,x10 | `FALL_THROUGH`
<a id="insn-00bbe608"></a> `00bbe608` | `ea e7 00 b2` | orr x10,xzr,#0x3333333333333333 | `FALL_THROUGH`
<a id="insn-00bbe60c"></a> `00bbe60c` | `4a 66 86 f2` | movk x10,#0x3332 | `FALL_THROUGH`
<a id="insn-00bbe610"></a> `00bbe610` | `6a 66 e0 f2` | movk x10,#0x333, LSL #48 | `FALL_THROUGH`
<a id="insn-00bbe614"></a> `00bbe614` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00bbe618"></a> `00bbe618` | `a8 00 00 54` | b.hi 0x00bbe62c | `CONDITIONAL_JUMP`
<a id="insn-00bbe61c"></a> `00bbe61c` | `29 f9 7f d3` | lsl x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bbe620"></a> `00bbe620` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bbe624"></a> `00bbe624` | `17 31 89 9a` | csel x23,x8,x9,cc | `FALL_THROUGH`
<a id="insn-00bbe628"></a> `00bbe628` | `d7 08 00 b4` | cbz x23,0x00bbe740 | `CONDITIONAL_JUMP`
<a id="insn-00bbe62c"></a> `00bbe62c` | `e8 0a 17 8b` | add x8,x23,x23, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00bbe630"></a> `00bbe630` | `00 f1 7d d3` | lsl x0,x8,#0x3 | `FALL_THROUGH`
<a id="insn-00bbe634"></a> `00bbe634` | `3f 6a 02 94` | bl 0x00c58f30 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe638"></a> `00bbe638` | `80 02 c0 3d` | ldr q0,[x20] | `FALL_THROUGH`
<a id="insn-00bbe63c"></a> `00bbe63c` | `89 0a 40 f9` | ldr x9,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00bbe640"></a> `00bbe640` | `08 05 80 52` | mov w8,#0x28 | `FALL_THROUGH`
<a id="insn-00bbe644"></a> `00bbe644` | `b6 02 08 9b` | madd x22,x21,x8,x0 | `FALL_THROUGH`
<a id="insn-00bbe648"></a> `00bbe648` | `f5 02 08 9b` | madd x21,x23,x8,x0 | `FALL_THROUGH`
<a id="insn-00bbe64c"></a> `00bbe64c` | `c0 62 00 91` | add x0,x22,#0x18 | `FALL_THROUGH`
<a id="insn-00bbe650"></a> `00bbe650` | `81 62 00 91` | add x1,x20,#0x18 | `FALL_THROUGH`
<a id="insn-00bbe654"></a> `00bbe654` | `c9 0a 00 f9` | str x9,[x22, #0x10] | `FALL_THROUGH`
<a id="insn-00bbe658"></a> `00bbe658` | `c0 02 80 3d` | str q0,[x22] | `FALL_THROUGH`
<a id="insn-00bbe65c"></a> `00bbe65c` | `9f fe 00 a9` | stp xzr,xzr,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00bbe660"></a> `00bbe660` | `9f 02 00 f9` | str xzr,[x20] | `FALL_THROUGH`
<a id="insn-00bbe664"></a> `00bbe664` | `a7 79 02 94` | bl 0x00c5cd00 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe668"></a> `00bbe668` | `78 52 40 a9` | ldp x24,x20,[x19] | `FALL_THROUGH`
<a id="insn-00bbe66c"></a> `00bbe66c` | `d7 a2 00 91` | add x23,x22,#0x28 | `FALL_THROUGH`
<a id="insn-00bbe670"></a> `00bbe670` | `9f 02 18 eb` | cmp x20,x24 | `FALL_THROUGH`
<a id="insn-00bbe674"></a> `00bbe674` | `80 02 00 54` | b.eq 0x00bbe6c4 | `CONDITIONAL_JUMP`
<a id="insn-00bbe678"></a> `00bbe678` | `f9 03 1f aa` | mov x25,xzr | `FALL_THROUGH`
<a id="insn-00bbe67c"></a> `00bbe67c` | `18 03 14 cb` | sub x24,x24,x20 | `FALL_THROUGH`
<a id="insn-00bbe680"></a> `00bbe680` | `88 02 19 8b` | add x8,x20,x25 | `FALL_THROUGH`
<a id="insn-00bbe684"></a> `00bbe684` | `09 81 5e f8` | ldur x9,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bbe688"></a> `00bbe688` | `00 81 dd 3c` | ldur q0,[x8, #-0x28] | `FALL_THROUGH`
<a id="insn-00bbe68c"></a> `00bbe68c` | `ca 02 19 8b` | add x10,x22,x25 | `FALL_THROUGH`
<a id="insn-00bbe690"></a> `00bbe690` | `40 41 00 d1` | sub x0,x10,#0x10 | `FALL_THROUGH`
<a id="insn-00bbe694"></a> `00bbe694` | `01 41 00 d1` | sub x1,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00bbe698"></a> `00bbe698` | `49 81 1e f8` | stur x9,[x10, #-0x18] | `FALL_THROUGH`
<a id="insn-00bbe69c"></a> `00bbe69c` | `40 81 9d 3c` | stur q0,[x10, #-0x28] | `FALL_THROUGH`
<a id="insn-00bbe6a0"></a> `00bbe6a0` | `1f 7d 3e a9` | stp xzr,xzr,[x8, #-0x20] | `FALL_THROUGH`
<a id="insn-00bbe6a4"></a> `00bbe6a4` | `1f 81 1d f8` | stur xzr,[x8, #-0x28] | `FALL_THROUGH`
<a id="insn-00bbe6a8"></a> `00bbe6a8` | `96 79 02 94` | bl 0x00c5cd00 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe6ac"></a> `00bbe6ac` | `39 a3 00 d1` | sub x25,x25,#0x28 | `FALL_THROUGH`
<a id="insn-00bbe6b0"></a> `00bbe6b0` | `1f 03 19 eb` | cmp x24,x25 | `FALL_THROUGH`
<a id="insn-00bbe6b4"></a> `00bbe6b4` | `61 fe ff 54` | b.ne 0x00bbe680 | `CONDITIONAL_JUMP`
<a id="insn-00bbe6b8"></a> `00bbe6b8` | `74 62 40 a9` | ldp x20,x24,[x19] | `FALL_THROUGH`
<a id="insn-00bbe6bc"></a> `00bbe6bc` | `d6 02 19 8b` | add x22,x22,x25 | `FALL_THROUGH`
<a id="insn-00bbe6c0"></a> `00bbe6c0` | `02 00 00 14` | b 0x00bbe6c8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbe6c4"></a> `00bbe6c4` | `f4 03 18 aa` | mov x20,x24 | `FALL_THROUGH`
<a id="insn-00bbe6c8"></a> `00bbe6c8` | `1f 03 14 eb` | cmp x24,x20 | `FALL_THROUGH`
<a id="insn-00bbe6cc"></a> `00bbe6cc` | `76 5e 00 a9` | stp x22,x23,[x19] | `FALL_THROUGH`
<a id="insn-00bbe6d0"></a> `00bbe6d0` | `75 0a 00 f9` | str x21,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bbe6d4"></a> `00bbe6d4` | `a0 01 00 54` | b.eq 0x00bbe708 | `CONDITIONAL_JUMP`
<a id="insn-00bbe6d8"></a> `00bbe6d8` | `f3 03 18 aa` | mov x19,x24 | `FALL_THROUGH`
<a id="insn-00bbe6dc"></a> `00bbe6dc` | `04 00 00 14` | b 0x00bbe6ec | `UNCONDITIONAL_JUMP`
<a id="insn-00bbe6e0"></a> `00bbe6e0` | `9f 02 13 eb` | cmp x20,x19 | `FALL_THROUGH`
<a id="insn-00bbe6e4"></a> `00bbe6e4` | `f8 03 13 aa` | mov x24,x19 | `FALL_THROUGH`
<a id="insn-00bbe6e8"></a> `00bbe6e8` | `00 01 00 54` | b.eq 0x00bbe708 | `CONDITIONAL_JUMP`
<a id="insn-00bbe6ec"></a> `00bbe6ec` | `00 43 00 d1` | sub x0,x24,#0x10 | `FALL_THROUGH`
<a id="insn-00bbe6f0"></a> `00bbe6f0` | `10 75 02 94` | bl 0x00c5bb30 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe6f4"></a> `00bbe6f4` | `68 8e 5d 38` | ldrb w8,[x19, #-0x28]! | `FALL_THROUGH`
<a id="insn-00bbe6f8"></a> `00bbe6f8` | `48 ff 07 36` | tbz w8,#0x0,0x00bbe6e0 | `CONDITIONAL_JUMP`
<a id="insn-00bbe6fc"></a> `00bbe6fc` | `00 83 5e f8` | ldur x0,[x24, #-0x18] | `FALL_THROUGH`
<a id="insn-00bbe700"></a> `00bbe700` | `14 6a 02 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe704"></a> `00bbe704` | `f7 ff ff 17` | b 0x00bbe6e0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbe708"></a> `00bbe708` | `14 01 00 b4` | cbz x20,0x00bbe728 | `CONDITIONAL_JUMP`
<a id="insn-00bbe70c"></a> `00bbe70c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbe710"></a> `00bbe710` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bbe714"></a> `00bbe714` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bbe718"></a> `00bbe718` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbe71c"></a> `00bbe71c` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbe720"></a> `00bbe720` | `f9 07 45 f8` | ldr x25,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00bbe724"></a> `00bbe724` | `0b 6a 02 14` | b 0x00c58f50 | `CALL_TERMINATOR`
<a id="insn-00bbe728"></a> `00bbe728` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bbe72c"></a> `00bbe72c` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bbe730"></a> `00bbe730` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbe734"></a> `00bbe734` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbe738"></a> `00bbe738` | `f9 07 45 f8` | ldr x25,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00bbe73c"></a> `00bbe73c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bbe740"></a> `00bbe740` | `e0 03 1f aa` | mov x0,xzr | `FALL_THROUGH`
<a id="insn-00bbe744"></a> `00bbe744` | `bd ff ff 17` | b 0x00bbe638 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbe748"></a> `00bbe748` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbe74c"></a> `00bbe74c` | `99 75 02 94` | bl 0x00c5bdb0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbe5ac`](#insn-00bbe5ac) 範囲 `[['00bbe5ac', '00bbe5f3']]`
  - `CONDITIONAL_JUMP` [`00bbe5f0`](#insn-00bbe5f0) → [`00bbe748`](#insn-00bbe748)
  - `FALL_THROUGH` [`00bbe5f0`](#insn-00bbe5f0) → [`00bbe5f4`](#insn-00bbe5f4)
- ブロック [`00bbe5f4`](#insn-00bbe5f4) 範囲 `[['00bbe5f4', '00bbe61b']]`
  - `CONDITIONAL_JUMP` [`00bbe618`](#insn-00bbe618) → [`00bbe62c`](#insn-00bbe62c)
  - `FALL_THROUGH` [`00bbe618`](#insn-00bbe618) → [`00bbe61c`](#insn-00bbe61c)
- ブロック [`00bbe61c`](#insn-00bbe61c) 範囲 `[['00bbe61c', '00bbe62b']]`
  - `CONDITIONAL_JUMP` [`00bbe628`](#insn-00bbe628) → [`00bbe740`](#insn-00bbe740)
  - `FALL_THROUGH` [`00bbe628`](#insn-00bbe628) → [`00bbe62c`](#insn-00bbe62c)
- ブロック [`00bbe62c`](#insn-00bbe62c) 範囲 `[['00bbe62c', '00bbe637']]`
  - `FALL_THROUGH` [`00bbe634`](#insn-00bbe634) → [`00bbe638`](#insn-00bbe638)
- ブロック [`00bbe638`](#insn-00bbe638) 範囲 `[['00bbe638', '00bbe677']]`
  - `CONDITIONAL_JUMP` [`00bbe674`](#insn-00bbe674) → [`00bbe6c4`](#insn-00bbe6c4)
  - `FALL_THROUGH` [`00bbe674`](#insn-00bbe674) → [`00bbe678`](#insn-00bbe678)
- ブロック [`00bbe678`](#insn-00bbe678) 範囲 `[['00bbe678', '00bbe67f']]`
  - `FALL_THROUGH` [`00bbe67c`](#insn-00bbe67c) → [`00bbe680`](#insn-00bbe680)
- ブロック [`00bbe680`](#insn-00bbe680) 範囲 `[['00bbe680', '00bbe68f']]`
  - `FALL_THROUGH` [`00bbe68c`](#insn-00bbe68c) → [`00bbe690`](#insn-00bbe690)
- ブロック [`00bbe690`](#insn-00bbe690) 範囲 `[['00bbe690', '00bbe6ab']]`
  - `FALL_THROUGH` [`00bbe6a8`](#insn-00bbe6a8) → [`00bbe6ac`](#insn-00bbe6ac)
- ブロック [`00bbe6ac`](#insn-00bbe6ac) 範囲 `[['00bbe6ac', '00bbe6b7']]`
  - `CONDITIONAL_JUMP` [`00bbe6b4`](#insn-00bbe6b4) → [`00bbe680`](#insn-00bbe680)
  - `FALL_THROUGH` [`00bbe6b4`](#insn-00bbe6b4) → [`00bbe6b8`](#insn-00bbe6b8)
- ブロック [`00bbe6b8`](#insn-00bbe6b8) 範囲 `[['00bbe6b8', '00bbe6c3']]`
  - `UNCONDITIONAL_JUMP` [`00bbe6c0`](#insn-00bbe6c0) → [`00bbe6c8`](#insn-00bbe6c8)
- ブロック [`00bbe6c4`](#insn-00bbe6c4) 範囲 `[['00bbe6c4', '00bbe6c7']]`
  - `FALL_THROUGH` [`00bbe6c4`](#insn-00bbe6c4) → [`00bbe6c8`](#insn-00bbe6c8)
- ブロック [`00bbe6c8`](#insn-00bbe6c8) 範囲 `[['00bbe6c8', '00bbe6d7']]`
  - `CONDITIONAL_JUMP` [`00bbe6d4`](#insn-00bbe6d4) → [`00bbe708`](#insn-00bbe708)
  - `FALL_THROUGH` [`00bbe6d4`](#insn-00bbe6d4) → [`00bbe6d8`](#insn-00bbe6d8)
- ブロック [`00bbe6d8`](#insn-00bbe6d8) 範囲 `[['00bbe6d8', '00bbe6df']]`
  - `UNCONDITIONAL_JUMP` [`00bbe6dc`](#insn-00bbe6dc) → [`00bbe6ec`](#insn-00bbe6ec)
- ブロック [`00bbe6e0`](#insn-00bbe6e0) 範囲 `[['00bbe6e0', '00bbe6e3']]`
  - `FALL_THROUGH` [`00bbe6e0`](#insn-00bbe6e0) → [`00bbe6e4`](#insn-00bbe6e4)
- ブロック [`00bbe6e4`](#insn-00bbe6e4) 範囲 `[['00bbe6e4', '00bbe6eb']]`
  - `CONDITIONAL_JUMP` [`00bbe6e8`](#insn-00bbe6e8) → [`00bbe708`](#insn-00bbe708)
  - `FALL_THROUGH` [`00bbe6e8`](#insn-00bbe6e8) → [`00bbe6ec`](#insn-00bbe6ec)
- ブロック [`00bbe6ec`](#insn-00bbe6ec) 範囲 `[['00bbe6ec', '00bbe6fb']]`
  - `CONDITIONAL_JUMP` [`00bbe6f8`](#insn-00bbe6f8) → [`00bbe6e0`](#insn-00bbe6e0)
  - `FALL_THROUGH` [`00bbe6f8`](#insn-00bbe6f8) → [`00bbe6fc`](#insn-00bbe6fc)
- ブロック [`00bbe6fc`](#insn-00bbe6fc) 範囲 `[['00bbe6fc', '00bbe703']]`
  - `FALL_THROUGH` [`00bbe700`](#insn-00bbe700) → [`00bbe704`](#insn-00bbe704)
- ブロック [`00bbe704`](#insn-00bbe704) 範囲 `[['00bbe704', '00bbe707']]`
  - `UNCONDITIONAL_JUMP` [`00bbe704`](#insn-00bbe704) → [`00bbe6e0`](#insn-00bbe6e0)
- ブロック [`00bbe708`](#insn-00bbe708) 範囲 `[['00bbe708', '00bbe70b']]`
  - `CONDITIONAL_JUMP` [`00bbe708`](#insn-00bbe708) → [`00bbe728`](#insn-00bbe728)
  - `FALL_THROUGH` [`00bbe708`](#insn-00bbe708) → [`00bbe70c`](#insn-00bbe70c)
- ブロック [`00bbe70c`](#insn-00bbe70c) 範囲 `[['00bbe70c', '00bbe71f']]`
  - `FALL_THROUGH` [`00bbe71c`](#insn-00bbe71c) → [`00bbe720`](#insn-00bbe720)
- ブロック [`00bbe720`](#insn-00bbe720) 範囲 `[['00bbe720', '00bbe723']]`
  - `FALL_THROUGH` [`00bbe720`](#insn-00bbe720) → [`00bbe724`](#insn-00bbe724)
- ブロック [`00bbe724`](#insn-00bbe724) 範囲 `[['00bbe724', '00bbe727']]`
- ブロック [`00bbe728`](#insn-00bbe728) 範囲 `[['00bbe728', '00bbe72b']]`
  - `FALL_THROUGH` [`00bbe728`](#insn-00bbe728) → [`00bbe72c`](#insn-00bbe72c)
- ブロック [`00bbe72c`](#insn-00bbe72c) 範囲 `[['00bbe72c', '00bbe72f']]`
  - `FALL_THROUGH` [`00bbe72c`](#insn-00bbe72c) → [`00bbe730`](#insn-00bbe730)
- ブロック [`00bbe730`](#insn-00bbe730) 範囲 `[['00bbe730', '00bbe73f']]`
- ブロック [`00bbe740`](#insn-00bbe740) 範囲 `[['00bbe740', '00bbe747']]`
  - `UNCONDITIONAL_JUMP` [`00bbe744`](#insn-00bbe744) → [`00bbe638`](#insn-00bbe638)
- ブロック [`00bbe748`](#insn-00bbe748) 範囲 `[['00bbe748', '00bbe74f']]`

## 命令位置別の参照

- [`00bbe5ac`](#insn-00bbe5ac) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe5b0`](#insn-00bbe5b0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe5b4`](#insn-00bbe5b4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe5b8`](#insn-00bbe5b8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe5bc`](#insn-00bbe5bc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe5f0`](#insn-00bbe5f0) → [`00bbe748`](#insn-00bbe748) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe618`](#insn-00bbe618) → [`00bbe62c`](#insn-00bbe62c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe628`](#insn-00bbe628) → [`00bbe740`](#insn-00bbe740) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe634`](#insn-00bbe634) → [`00c58f30`](../00c58/00c58f30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f30` · 推定シンボル `None` · 推定型 `None`
- [`00bbe664`](#insn-00bbe664) → [`00c5cd00`](../00c5c/00c5cd00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5cd00` · 推定シンボル `None` · 推定型 `None`
- [`00bbe674`](#insn-00bbe674) → [`00bbe6c4`](#insn-00bbe6c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe6a8`](#insn-00bbe6a8) → [`00c5cd00`](../00c5c/00c5cd00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5cd00` · 推定シンボル `None` · 推定型 `None`
- [`00bbe6b4`](#insn-00bbe6b4) → [`00bbe680`](#insn-00bbe680) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe6c0`](#insn-00bbe6c0) → [`00bbe6c8`](#insn-00bbe6c8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe6d4`](#insn-00bbe6d4) → [`00bbe708`](#insn-00bbe708) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe6dc`](#insn-00bbe6dc) → [`00bbe6ec`](#insn-00bbe6ec) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe6e8`](#insn-00bbe6e8) → [`00bbe708`](#insn-00bbe708) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe6f0`](#insn-00bbe6f0) → [`00c5bb30`](../00c5b/00c5bb30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bb30` · 推定シンボル `None` · 推定型 `None`
- [`00bbe6f8`](#insn-00bbe6f8) → [`00bbe6e0`](#insn-00bbe6e0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe700`](#insn-00bbe700) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00bbe704`](#insn-00bbe704) → [`00bbe6e0`](#insn-00bbe6e0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe708`](#insn-00bbe708) → [`00bbe728`](#insn-00bbe728) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe710`](#insn-00bbe710) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe714`](#insn-00bbe714) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe718`](#insn-00bbe718) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe71c`](#insn-00bbe71c) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe724`](#insn-00bbe724) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00bbe728`](#insn-00bbe728) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe72c`](#insn-00bbe72c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe730`](#insn-00bbe730) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe734`](#insn-00bbe734) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe744`](#insn-00bbe744) → [`00bbe638`](#insn-00bbe638) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe74c`](#insn-00bbe74c) → [`00c5bdb0`](../00c5b/00c5bdb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bdb0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbe5ac`](#insn-00bbe5ac)

~~~json
{
  "source": "00bbe5ac",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe5b0`](#insn-00bbe5b0)

~~~json
{
  "source": "00bbe5b0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe5b4`](#insn-00bbe5b4)

~~~json
{
  "source": "00bbe5b4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe5b8`](#insn-00bbe5b8)

~~~json
{
  "source": "00bbe5b8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe5bc`](#insn-00bbe5bc)

~~~json
{
  "source": "00bbe5bc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe5f0`](#insn-00bbe5f0)

~~~json
{
  "source": "00bbe5f0",
  "target": "00bbe748",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe618`](#insn-00bbe618)

~~~json
{
  "source": "00bbe618",
  "target": "00bbe62c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe628`](#insn-00bbe628)

~~~json
{
  "source": "00bbe628",
  "target": "00bbe740",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe634`](#insn-00bbe634)

~~~json
{
  "source": "00bbe634",
  "target": "00c58f30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe664`](#insn-00bbe664)

~~~json
{
  "source": "00bbe664",
  "target": "00c5cd00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe674`](#insn-00bbe674)

~~~json
{
  "source": "00bbe674",
  "target": "00bbe6c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe6a8`](#insn-00bbe6a8)

~~~json
{
  "source": "00bbe6a8",
  "target": "00c5cd00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe6b4`](#insn-00bbe6b4)

~~~json
{
  "source": "00bbe6b4",
  "target": "00bbe680",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe6c0`](#insn-00bbe6c0)

~~~json
{
  "source": "00bbe6c0",
  "target": "00bbe6c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe6d4`](#insn-00bbe6d4)

~~~json
{
  "source": "00bbe6d4",
  "target": "00bbe708",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe6dc`](#insn-00bbe6dc)

~~~json
{
  "source": "00bbe6dc",
  "target": "00bbe6ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe6e8`](#insn-00bbe6e8)

~~~json
{
  "source": "00bbe6e8",
  "target": "00bbe708",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe6f0`](#insn-00bbe6f0)

~~~json
{
  "source": "00bbe6f0",
  "target": "00c5bb30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe6f8`](#insn-00bbe6f8)

~~~json
{
  "source": "00bbe6f8",
  "target": "00bbe6e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe700`](#insn-00bbe700)

~~~json
{
  "source": "00bbe700",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe704`](#insn-00bbe704)

~~~json
{
  "source": "00bbe704",
  "target": "00bbe6e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe708`](#insn-00bbe708)

~~~json
{
  "source": "00bbe708",
  "target": "00bbe728",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe710`](#insn-00bbe710)

~~~json
{
  "source": "00bbe710",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe714`](#insn-00bbe714)

~~~json
{
  "source": "00bbe714",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe718`](#insn-00bbe718)

~~~json
{
  "source": "00bbe718",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe71c`](#insn-00bbe71c)

~~~json
{
  "source": "00bbe71c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe724`](#insn-00bbe724)

~~~json
{
  "source": "00bbe724",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe728`](#insn-00bbe728)

~~~json
{
  "source": "00bbe728",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe72c`](#insn-00bbe72c)

~~~json
{
  "source": "00bbe72c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe730`](#insn-00bbe730)

~~~json
{
  "source": "00bbe730",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe734`](#insn-00bbe734)

~~~json
{
  "source": "00bbe734",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe744`](#insn-00bbe744)

~~~json
{
  "source": "00bbe744",
  "target": "00bbe638",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe74c`](#insn-00bbe74c)

~~~json
{
  "source": "00bbe74c",
  "target": "00c5bdb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
