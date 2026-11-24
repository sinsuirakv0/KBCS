# 00bbfa4c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bbea58`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbe/00bbea58.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0035.md#compare-eeebfd69bbc129b03864e4ad23ca4166)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbfa4c",
  "name": "_ZNSt6__ndk16vectorIhNS_9allocatorIhEEE6assignIN11flatbuffers14VectorIteratorIhhPKhjEEEENS_9enable_ifIXaasr21__is_forward_iteratorIT_EE5valuesr16is_constructibleIhNS_15iterator_traitsISB_E9referenceEEE5valueEvE4typeESB_SB_",
  "size": 608,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d618f06c984cd2e09238cc886ee87fafaa4123421b572ddb2fe2374320fc43b6",
  "source_text_sha256": "d618f06c984cd2e09238cc886ee87fafaa4123421b572ddb2fe2374320fc43b6",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbfa4c",
        "00bbfcab"
      ]
    ],
    "bytes_sha256": "8103981dbb10a766e258b5e70634c655e41aa0fc5f9da427579038f9f4752b82",
    "instruction_count": 152,
    "instruction_bytes": 608,
    "body_bytes": 608,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5e610](../00c5e/00c5e610.md)

## 呼び出し先

- [00c58f30](../00c58/00c58f30.md)
- [00c58f50](../00c58/00c58f50.md)
- [00c5bdb0](../00c5b/00c5bdb0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 5465 bytes

~~~c

void _ZNSt6__ndk16vectorIhNS_9allocatorIhEEE6assignIN11flatbuffers14VectorIteratorIhhPKhjEEEENS_9enable_ifIXaasr21__is_forward_iteratorIT_EE5valuesr16is_constructibleIhNS_15iterator_traitsISB_E9referenceEEE5valueEvE4typeESB_SB_
               (undefined8 *param_1,undefined8 *param_2,ulong *param_3)

{
  undefined8 *puVar1;
  undefined1 *puVar2;
  ulong uVar3;
  undefined1 *puVar4;
  undefined1 *puVar5;
  undefined1 *puVar6;
  undefined1 *puVar7;
  ulong uVar8;
  undefined8 *puVar9;
  undefined8 *puVar10;
  ulong uVar11;
  ulong uVar12;
  ulong uVar13;
  undefined8 uVar14;
  undefined8 uVar15;
  undefined8 uVar16;
  
  puVar7 = (undefined1 *)*param_2;
  uVar3 = param_1[2];
  puVar2 = (undefined1 *)*param_1;
  uVar13 = (long)*param_3 - (long)puVar7;
  if (uVar3 - (long)puVar2 < uVar13) {
    if (puVar2 != (undefined1 *)0x0) {
      param_1[1] = puVar2;
      _ZdlPv(puVar2);
      uVar3 = 0;
      *param_1 = 0;
      param_1[1] = 0;
      param_1[2] = 0;
    }
    if ((long)uVar13 < 0) {
                    /* WARNING: Subroutine does not return */
      _ZNKSt6__ndk120__vector_base_commonILb1EE20__throw_length_errorEv(param_1);
    }
    if (uVar3 < 0x3fffffffffffffff) {
      if (uVar13 <= uVar3 << 1) {
        uVar13 = uVar3 << 1;
      }
    }
    else {
      uVar13 = 0x7fffffffffffffff;
    }
    puVar7 = (undefined1 *)_Znwm(uVar13);
    *param_1 = puVar7;
    param_1[1] = puVar7;
    param_1[2] = puVar7 + uVar13;
    puVar2 = (undefined1 *)*param_2;
    puVar4 = (undefined1 *)*param_3;
    uVar13 = (long)puVar4 - (long)puVar2;
    if (uVar13 != 0) {
      puVar6 = puVar7;
      if ((0x1f < uVar13) && ((puVar4 <= puVar7 || (puVar7 + uVar13 <= puVar2)))) {
        uVar8 = uVar13 & 0xffffffffffffffe0;
        puVar10 = (undefined8 *)(puVar2 + 0x10);
        puVar6 = puVar7 + uVar8;
        puVar2 = puVar2 + uVar8;
        puVar9 = (undefined8 *)(puVar7 + 0x10);
        uVar3 = uVar8;
        do {
          puVar1 = puVar10 + -1;
          uVar14 = puVar10[-2];
          uVar16 = puVar10[1];
          uVar15 = *puVar10;
          puVar10 = puVar10 + 4;
          uVar3 = uVar3 - 0x20;
          puVar9[-1] = *puVar1;
          puVar9[-2] = uVar14;
          puVar9[1] = uVar16;
          *puVar9 = uVar15;
          puVar9 = puVar9 + 4;
        } while (uVar3 != 0);
        puVar7 = puVar6;
        if (uVar13 == uVar8) goto LAB_00bbfb88;
      }
      do {
        puVar5 = puVar2 + 1;
        puVar7 = puVar6 + 1;
        *puVar6 = *puVar2;
        puVar2 = puVar5;
        puVar6 = puVar7;
                    /* try { // try from 00bbfb7c to 00cbfb8f has its CatchHandler @ 00bc048c */
      } while (puVar4 != puVar5);
    }
LAB_00bbfb88:
    param_1[1] = puVar7;
    return;
  }
  uVar3 = param_1[1] - (long)puVar2;
  puVar4 = puVar7 + (uVar3 & 0xffffffff);
  if (uVar13 <= uVar3) {
    puVar4 = (undefined1 *)*param_3;
  }
  uVar8 = (long)puVar4 - (long)puVar7;
  if (uVar8 != 0) {
    puVar6 = puVar2;
    if ((0x1f < uVar8) && ((puVar4 <= puVar2 || (puVar4 + ((long)puVar2 - (long)puVar7) <= puVar7)))
       ) {
                    /* try { // try from 00bbfbb0 to 00cbfbcb has its CatchHandler @ 00bc0448 */
      uVar11 = uVar8 & 0xffffffffffffffe0;
      puVar10 = (undefined8 *)(puVar2 + 0x10);
      puVar2 = puVar2 + uVar11;
      puVar9 = (undefined8 *)(puVar7 + 0x10);
      uVar12 = uVar11;
      do {
        puVar1 = puVar9 + -1;
        uVar14 = puVar9[-2];
        uVar16 = puVar9[1];
        uVar15 = *puVar9;
                    /* try { // try from 00bbfbcc to 00cbfc8f has its CatchHandler @ 00bbf85c */
        uVar12 = uVar12 - 0x20;
        puVar9 = puVar9 + 4;
        puVar10[-1] = *puVar1;
        puVar10[-2] = uVar14;
        puVar10[1] = uVar16;
        *puVar10 = uVar15;
        puVar10 = puVar10 + 4;
      } while (uVar12 != 0);
      puVar6 = puVar2;
      puVar7 = puVar7 + uVar11;
      if (uVar11 == uVar8) goto LAB_00bbfbf8;
    }
    do {
      puVar5 = puVar7 + 1;
      puVar2 = puVar6 + 1;
      *puVar6 = *puVar7;
      puVar6 = puVar2;
      puVar7 = puVar5;
    } while (puVar4 != puVar5);
  }
LAB_00bbfbf8:
  if (uVar13 <= uVar3) {
    param_1[1] = puVar2;
    return;
  }
  puVar6 = (undefined1 *)*param_3;
  puVar7 = (undefined1 *)param_1[1];
  uVar13 = (long)puVar6 - (long)puVar4;
  puVar2 = puVar7;
  if (uVar13 != 0) {
    if ((0x1f < uVar13) && ((puVar6 <= puVar7 || (puVar7 + uVar13 <= puVar4)))) {
      uVar8 = uVar13 & 0xffffffffffffffe0;
      puVar10 = (undefined8 *)(puVar4 + 0x10);
      puVar2 = puVar7 + uVar8;
      puVar4 = puVar4 + uVar8;
      puVar9 = (undefined8 *)(puVar7 + 0x10);
      uVar3 = uVar8;
      do {
        puVar1 = puVar10 + -1;
        uVar14 = puVar10[-2];
        uVar16 = puVar10[1];
        uVar15 = *puVar10;
        puVar10 = puVar10 + 4;
        uVar3 = uVar3 - 0x20;
        puVar9[-1] = *puVar1;
        puVar9[-2] = uVar14;
        puVar9[1] = uVar16;
        *puVar9 = uVar15;
        puVar9 = puVar9 + 4;
      } while (uVar3 != 0);
      puVar7 = puVar2;
      if (uVar8 == uVar13) goto LAB_00bbfc90;
    }
    do {
      puVar5 = puVar4 + 1;
      puVar2 = puVar7 + 1;
      *puVar7 = *puVar4;
      puVar4 = puVar5;
      puVar7 = puVar2;
    } while (puVar6 != puVar5);
  }
LAB_00bbfc90:
                    /* try { // try from 00bbfc90 to 00cbfc9f has its CatchHandler @ 00bc0444 */
  param_1[1] = puVar2;
                    /* try { // try from 00bbfca0 to 00cbfca7 has its CatchHandler @ 00bc0404 */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbfa4c"></a> `00bbfa4c` | `f6 57 bd a9` | stp x22,x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bbfa50"></a> `00bbfa50` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbfa54"></a> `00bbfa54` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbfa58"></a> `00bbfa58` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bbfa5c"></a> `00bbfa5c` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bbfa60"></a> `00bbfa60` | `2c 00 40 f9` | ldr x12,[x1] | `FALL_THROUGH`
<a id="insn-00bbfa64"></a> `00bbfa64` | `4a 00 40 f9` | ldr x10,[x2] | `FALL_THROUGH`
<a id="insn-00bbfa68"></a> `00bbfa68` | `08 08 40 f9` | ldr x8,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bbfa6c"></a> `00bbfa6c` | `00 00 40 f9` | ldr x0,[x0] | `FALL_THROUGH`
<a id="insn-00bbfa70"></a> `00bbfa70` | `f4 03 02 aa` | mov x20,x2 | `FALL_THROUGH`
<a id="insn-00bbfa74"></a> `00bbfa74` | `56 01 0c cb` | sub x22,x10,x12 | `FALL_THROUGH`
<a id="insn-00bbfa78"></a> `00bbfa78` | `09 01 00 cb` | sub x9,x8,x0 | `FALL_THROUGH`
<a id="insn-00bbfa7c"></a> `00bbfa7c` | `df 02 09 eb` | cmp x22,x9 | `FALL_THROUGH`
<a id="insn-00bbfa80"></a> `00bbfa80` | `09 02 00 54` | b.ls 0x00bbfac0 | `CONDITIONAL_JUMP`
<a id="insn-00bbfa84"></a> `00bbfa84` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-00bbfa88"></a> `00bbfa88` | `c0 00 00 b4` | cbz x0,0x00bbfaa0 | `CONDITIONAL_JUMP`
<a id="insn-00bbfa8c"></a> `00bbfa8c` | `60 06 00 f9` | str x0,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bbfa90"></a> `00bbfa90` | `30 65 02 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00bbfa94"></a> `00bbfa94` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbfa98"></a> `00bbfa98` | `7f 7e 00 a9` | stp xzr,xzr,[x19] | `FALL_THROUGH`
<a id="insn-00bbfa9c"></a> `00bbfa9c` | `7f 0a 00 f9` | str xzr,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bbfaa0"></a> `00bbfaa0` | `36 10 f8 b7` | tbnz x22,#0x3f,0x00bbfca4 | `CONDITIONAL_JUMP`
<a id="insn-00bbfaa4"></a> `00bbfaa4` | `e9 f3 7f b2` | orr x9,xzr,#0x3ffffffffffffffe | `FALL_THROUGH`
<a id="insn-00bbfaa8"></a> `00bbfaa8` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bbfaac"></a> `00bbfaac` | `08 02 00 54` | b.hi 0x00bbfaec | `CONDITIONAL_JUMP`
<a id="insn-00bbfab0"></a> `00bbfab0` | `08 f9 7f d3` | lsl x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbfab4"></a> `00bbfab4` | `1f 01 16 eb` | cmp x8,x22 | `FALL_THROUGH`
<a id="insn-00bbfab8"></a> `00bbfab8` | `d6 32 88 9a` | csel x22,x22,x8,cc | `FALL_THROUGH`
<a id="insn-00bbfabc"></a> `00bbfabc` | `0d 00 00 14` | b 0x00bbfaf0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbfac0"></a> `00bbfac0` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bbfac4"></a> `00bbfac4` | `09 01 00 cb` | sub x9,x8,x0 | `FALL_THROUGH`
<a id="insn-00bbfac8"></a> `00bbfac8` | `88 41 29 8b` | add x8,x12,w9, UXTW  | `FALL_THROUGH`
<a id="insn-00bbfacc"></a> `00bbfacc` | `df 02 09 eb` | cmp x22,x9 | `FALL_THROUGH`
<a id="insn-00bbfad0"></a> `00bbfad0` | `08 81 8a 9a` | csel x8,x8,x10,hi | `FALL_THROUGH`
<a id="insn-00bbfad4"></a> `00bbfad4` | `0b 01 0c eb` | subs x11,x8,x12 | `FALL_THROUGH`
<a id="insn-00bbfad8"></a> `00bbfad8` | `00 09 00 54` | b.eq 0x00bbfbf8 | `CONDITIONAL_JUMP`
<a id="insn-00bbfadc"></a> `00bbfadc` | `7f 81 00 f1` | cmp x11,#0x20 | `FALL_THROUGH`
<a id="insn-00bbfae0"></a> `00bbfae0` | `82 05 00 54` | b.cs 0x00bbfb90 | `CONDITIONAL_JUMP`
<a id="insn-00bbfae4"></a> `00bbfae4` | `ea 03 0c aa` | mov x10,x12 | `FALL_THROUGH`
<a id="insn-00bbfae8"></a> `00bbfae8` | `40 00 00 14` | b 0x00bbfbe8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbfaec"></a> `00bbfaec` | `16 00 f0 92` | mov x22,#0x7fffffffffffffff | `FALL_THROUGH`
<a id="insn-00bbfaf0"></a> `00bbfaf0` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bbfaf4"></a> `00bbfaf4` | `0f 65 02 94` | bl 0x00c58f30 | `UNCONDITIONAL_CALL`
<a id="insn-00bbfaf8"></a> `00bbfaf8` | `08 00 16 8b` | add x8,x0,x22 | `FALL_THROUGH`
<a id="insn-00bbfafc"></a> `00bbfafc` | `60 02 00 a9` | stp x0,x0,[x19] | `FALL_THROUGH`
<a id="insn-00bbfb00"></a> `00bbfb00` | `68 0a 00 f9` | str x8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bbfb04"></a> `00bbfb04` | `a9 02 40 f9` | ldr x9,[x21] | `FALL_THROUGH`
<a id="insn-00bbfb08"></a> `00bbfb08` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bbfb0c"></a> `00bbfb0c` | `0b 01 09 eb` | subs x11,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbfb10"></a> `00bbfb10` | `a0 03 00 54` | b.eq 0x00bbfb84 | `CONDITIONAL_JUMP`
<a id="insn-00bbfb14"></a> `00bbfb14` | `7f 81 00 f1` | cmp x11,#0x20 | `FALL_THROUGH`
<a id="insn-00bbfb18"></a> `00bbfb18` | `a3 02 00 54` | b.cc 0x00bbfb6c | `CONDITIONAL_JUMP`
<a id="insn-00bbfb1c"></a> `00bbfb1c` | `1f 00 08 eb` | cmp x0,x8 | `FALL_THROUGH`
<a id="insn-00bbfb20"></a> `00bbfb20` | `82 00 00 54` | b.cs 0x00bbfb30 | `CONDITIONAL_JUMP`
<a id="insn-00bbfb24"></a> `00bbfb24` | `0a 00 0b 8b` | add x10,x0,x11 | `FALL_THROUGH`
<a id="insn-00bbfb28"></a> `00bbfb28` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00bbfb2c"></a> `00bbfb2c` | `03 02 00 54` | b.cc 0x00bbfb6c | `CONDITIONAL_JUMP`
<a id="insn-00bbfb30"></a> `00bbfb30` | `6c e9 7b 92` | and x12,x11,#-0x20 | `FALL_THROUGH`
<a id="insn-00bbfb34"></a> `00bbfb34` | `2d 41 00 91` | add x13,x9,#0x10 | `FALL_THROUGH`
<a id="insn-00bbfb38"></a> `00bbfb38` | `0a 00 0c 8b` | add x10,x0,x12 | `FALL_THROUGH`
<a id="insn-00bbfb3c"></a> `00bbfb3c` | `29 01 0c 8b` | add x9,x9,x12 | `FALL_THROUGH`
<a id="insn-00bbfb40"></a> `00bbfb40` | `0e 40 00 91` | add x14,x0,#0x10 | `FALL_THROUGH`
<a id="insn-00bbfb44"></a> `00bbfb44` | `ef 03 0c aa` | mov x15,x12 | `FALL_THROUGH`
<a id="insn-00bbfb48"></a> `00bbfb48` | `a0 85 7f ad` | ldp q0,q1,[x13, #-0x10] | `FALL_THROUGH`
<a id="insn-00bbfb4c"></a> `00bbfb4c` | `ad 81 00 91` | add x13,x13,#0x20 | `FALL_THROUGH`
<a id="insn-00bbfb50"></a> `00bbfb50` | `ef 81 00 f1` | subs x15,x15,#0x20 | `FALL_THROUGH`
<a id="insn-00bbfb54"></a> `00bbfb54` | `c0 85 3f ad` | stp q0,q1,[x14, #-0x10] | `FALL_THROUGH`
<a id="insn-00bbfb58"></a> `00bbfb58` | `ce 81 00 91` | add x14,x14,#0x20 | `FALL_THROUGH`
<a id="insn-00bbfb5c"></a> `00bbfb5c` | `61 ff ff 54` | b.ne 0x00bbfb48 | `CONDITIONAL_JUMP`
<a id="insn-00bbfb60"></a> `00bbfb60` | `7f 01 0c eb` | cmp x11,x12 | `FALL_THROUGH`
<a id="insn-00bbfb64"></a> `00bbfb64` | `e0 03 0a aa` | mov x0,x10 | `FALL_THROUGH`
<a id="insn-00bbfb68"></a> `00bbfb68` | `00 01 00 54` | b.eq 0x00bbfb88 | `CONDITIONAL_JUMP`
<a id="insn-00bbfb6c"></a> `00bbfb6c` | `ea 03 00 aa` | mov x10,x0 | `FALL_THROUGH`
<a id="insn-00bbfb70"></a> `00bbfb70` | `2b 15 40 38` | ldrb w11,[x9], #0x1 | `FALL_THROUGH`
<a id="insn-00bbfb74"></a> `00bbfb74` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bbfb78"></a> `00bbfb78` | `4b 15 00 38` | strb w11,[x10], #0x1 | `FALL_THROUGH`
<a id="insn-00bbfb7c"></a> `00bbfb7c` | `a1 ff ff 54` | b.ne 0x00bbfb70 | `CONDITIONAL_JUMP`
<a id="insn-00bbfb80"></a> `00bbfb80` | `02 00 00 14` | b 0x00bbfb88 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbfb84"></a> `00bbfb84` | `ea 03 00 aa` | mov x10,x0 | `FALL_THROUGH`
<a id="insn-00bbfb88"></a> `00bbfb88` | `6a 06 00 f9` | str x10,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bbfb8c"></a> `00bbfb8c` | `42 00 00 14` | b 0x00bbfc94 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbfb90"></a> `00bbfb90` | `1f 00 08 eb` | cmp x0,x8 | `FALL_THROUGH`
<a id="insn-00bbfb94"></a> `00bbfb94` | `e2 00 00 54` | b.cs 0x00bbfbb0 | `CONDITIONAL_JUMP`
<a id="insn-00bbfb98"></a> `00bbfb98` | `0a 00 0c cb` | sub x10,x0,x12 | `FALL_THROUGH`
<a id="insn-00bbfb9c"></a> `00bbfb9c` | `0a 01 0a 8b` | add x10,x8,x10 | `FALL_THROUGH`
<a id="insn-00bbfba0"></a> `00bbfba0` | `5f 01 0c eb` | cmp x10,x12 | `FALL_THROUGH`
<a id="insn-00bbfba4"></a> `00bbfba4` | `69 00 00 54` | b.ls 0x00bbfbb0 | `CONDITIONAL_JUMP`
<a id="insn-00bbfba8"></a> `00bbfba8` | `ea 03 0c aa` | mov x10,x12 | `FALL_THROUGH`
<a id="insn-00bbfbac"></a> `00bbfbac` | `0f 00 00 14` | b 0x00bbfbe8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbfbb0"></a> `00bbfbb0` | `6d e9 7b 92` | and x13,x11,#-0x20 | `FALL_THROUGH`
<a id="insn-00bbfbb4"></a> `00bbfbb4` | `0e 40 00 91` | add x14,x0,#0x10 | `FALL_THROUGH`
<a id="insn-00bbfbb8"></a> `00bbfbb8` | `8a 01 0d 8b` | add x10,x12,x13 | `FALL_THROUGH`
<a id="insn-00bbfbbc"></a> `00bbfbbc` | `00 00 0d 8b` | add x0,x0,x13 | `FALL_THROUGH`
<a id="insn-00bbfbc0"></a> `00bbfbc0` | `8c 41 00 91` | add x12,x12,#0x10 | `FALL_THROUGH`
<a id="insn-00bbfbc4"></a> `00bbfbc4` | `ef 03 0d aa` | mov x15,x13 | `FALL_THROUGH`
<a id="insn-00bbfbc8"></a> `00bbfbc8` | `80 85 7f ad` | ldp q0,q1,[x12, #-0x10] | `FALL_THROUGH`
<a id="insn-00bbfbcc"></a> `00bbfbcc` | `ef 81 00 f1` | subs x15,x15,#0x20 | `FALL_THROUGH`
<a id="insn-00bbfbd0"></a> `00bbfbd0` | `8c 81 00 91` | add x12,x12,#0x20 | `FALL_THROUGH`
<a id="insn-00bbfbd4"></a> `00bbfbd4` | `c0 85 3f ad` | stp q0,q1,[x14, #-0x10] | `FALL_THROUGH`
<a id="insn-00bbfbd8"></a> `00bbfbd8` | `ce 81 00 91` | add x14,x14,#0x20 | `FALL_THROUGH`
<a id="insn-00bbfbdc"></a> `00bbfbdc` | `61 ff ff 54` | b.ne 0x00bbfbc8 | `CONDITIONAL_JUMP`
<a id="insn-00bbfbe0"></a> `00bbfbe0` | `bf 01 0b eb` | cmp x13,x11 | `FALL_THROUGH`
<a id="insn-00bbfbe4"></a> `00bbfbe4` | `a0 00 00 54` | b.eq 0x00bbfbf8 | `CONDITIONAL_JUMP`
<a id="insn-00bbfbe8"></a> `00bbfbe8` | `4b 15 40 38` | ldrb w11,[x10], #0x1 | `FALL_THROUGH`
<a id="insn-00bbfbec"></a> `00bbfbec` | `1f 01 0a eb` | cmp x8,x10 | `FALL_THROUGH`
<a id="insn-00bbfbf0"></a> `00bbfbf0` | `0b 14 00 38` | strb w11,[x0], #0x1 | `FALL_THROUGH`
<a id="insn-00bbfbf4"></a> `00bbfbf4` | `a1 ff ff 54` | b.ne 0x00bbfbe8 | `CONDITIONAL_JUMP`
<a id="insn-00bbfbf8"></a> `00bbfbf8` | `df 02 09 eb` | cmp x22,x9 | `FALL_THROUGH`
<a id="insn-00bbfbfc"></a> `00bbfbfc` | `29 01 00 54` | b.ls 0x00bbfc20 | `CONDITIONAL_JUMP`
<a id="insn-00bbfc00"></a> `00bbfc00` | `89 02 40 f9` | ldr x9,[x20] | `FALL_THROUGH`
<a id="insn-00bbfc04"></a> `00bbfc04` | `6c 06 40 f9` | ldr x12,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bbfc08"></a> `00bbfc08` | `2b 01 08 eb` | subs x11,x9,x8 | `FALL_THROUGH`
<a id="insn-00bbfc0c"></a> `00bbfc0c` | `20 04 00 54` | b.eq 0x00bbfc90 | `CONDITIONAL_JUMP`
<a id="insn-00bbfc10"></a> `00bbfc10` | `7f 81 00 f1` | cmp x11,#0x20 | `FALL_THROUGH`
<a id="insn-00bbfc14"></a> `00bbfc14` | `a2 00 00 54` | b.cs 0x00bbfc28 | `CONDITIONAL_JUMP`
<a id="insn-00bbfc18"></a> `00bbfc18` | `ea 03 0c aa` | mov x10,x12 | `FALL_THROUGH`
<a id="insn-00bbfc1c"></a> `00bbfc1c` | `18 00 00 14` | b 0x00bbfc7c | `UNCONDITIONAL_JUMP`
<a id="insn-00bbfc20"></a> `00bbfc20` | `60 06 00 f9` | str x0,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bbfc24"></a> `00bbfc24` | `1c 00 00 14` | b 0x00bbfc94 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbfc28"></a> `00bbfc28` | `3f 01 0c eb` | cmp x9,x12 | `FALL_THROUGH`
<a id="insn-00bbfc2c"></a> `00bbfc2c` | `c9 00 00 54` | b.ls 0x00bbfc44 | `CONDITIONAL_JUMP`
<a id="insn-00bbfc30"></a> `00bbfc30` | `8a 01 0b 8b` | add x10,x12,x11 | `FALL_THROUGH`
<a id="insn-00bbfc34"></a> `00bbfc34` | `5f 01 08 eb` | cmp x10,x8 | `FALL_THROUGH`
<a id="insn-00bbfc38"></a> `00bbfc38` | `69 00 00 54` | b.ls 0x00bbfc44 | `CONDITIONAL_JUMP`
<a id="insn-00bbfc3c"></a> `00bbfc3c` | `ea 03 0c aa` | mov x10,x12 | `FALL_THROUGH`
<a id="insn-00bbfc40"></a> `00bbfc40` | `0f 00 00 14` | b 0x00bbfc7c | `UNCONDITIONAL_JUMP`
<a id="insn-00bbfc44"></a> `00bbfc44` | `6d e9 7b 92` | and x13,x11,#-0x20 | `FALL_THROUGH`
<a id="insn-00bbfc48"></a> `00bbfc48` | `0e 41 00 91` | add x14,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00bbfc4c"></a> `00bbfc4c` | `8a 01 0d 8b` | add x10,x12,x13 | `FALL_THROUGH`
<a id="insn-00bbfc50"></a> `00bbfc50` | `08 01 0d 8b` | add x8,x8,x13 | `FALL_THROUGH`
<a id="insn-00bbfc54"></a> `00bbfc54` | `8c 41 00 91` | add x12,x12,#0x10 | `FALL_THROUGH`
<a id="insn-00bbfc58"></a> `00bbfc58` | `ef 03 0d aa` | mov x15,x13 | `FALL_THROUGH`
<a id="insn-00bbfc5c"></a> `00bbfc5c` | `c0 85 7f ad` | ldp q0,q1,[x14, #-0x10] | `FALL_THROUGH`
<a id="insn-00bbfc60"></a> `00bbfc60` | `ce 81 00 91` | add x14,x14,#0x20 | `FALL_THROUGH`
<a id="insn-00bbfc64"></a> `00bbfc64` | `ef 81 00 f1` | subs x15,x15,#0x20 | `FALL_THROUGH`
<a id="insn-00bbfc68"></a> `00bbfc68` | `80 85 3f ad` | stp q0,q1,[x12, #-0x10] | `FALL_THROUGH`
<a id="insn-00bbfc6c"></a> `00bbfc6c` | `8c 81 00 91` | add x12,x12,#0x20 | `FALL_THROUGH`
<a id="insn-00bbfc70"></a> `00bbfc70` | `61 ff ff 54` | b.ne 0x00bbfc5c | `CONDITIONAL_JUMP`
<a id="insn-00bbfc74"></a> `00bbfc74` | `bf 01 0b eb` | cmp x13,x11 | `FALL_THROUGH`
<a id="insn-00bbfc78"></a> `00bbfc78` | `a0 00 00 54` | b.eq 0x00bbfc8c | `CONDITIONAL_JUMP`
<a id="insn-00bbfc7c"></a> `00bbfc7c` | `0b 15 40 38` | ldrb w11,[x8], #0x1 | `FALL_THROUGH`
<a id="insn-00bbfc80"></a> `00bbfc80` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bbfc84"></a> `00bbfc84` | `4b 15 00 38` | strb w11,[x10], #0x1 | `FALL_THROUGH`
<a id="insn-00bbfc88"></a> `00bbfc88` | `a1 ff ff 54` | b.ne 0x00bbfc7c | `CONDITIONAL_JUMP`
<a id="insn-00bbfc8c"></a> `00bbfc8c` | `ec 03 0a aa` | mov x12,x10 | `FALL_THROUGH`
<a id="insn-00bbfc90"></a> `00bbfc90` | `6c 06 00 f9` | str x12,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bbfc94"></a> `00bbfc94` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbfc98"></a> `00bbfc98` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbfc9c"></a> `00bbfc9c` | `f6 57 c3 a8` | ldp x22,x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bbfca0"></a> `00bbfca0` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bbfca4"></a> `00bbfca4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbfca8"></a> `00bbfca8` | `42 70 02 94` | bl 0x00c5bdb0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbfa4c`](#insn-00bbfa4c) 範囲 `[['00bbfa4c', '00bbfa83']]`
  - `CONDITIONAL_JUMP` [`00bbfa80`](#insn-00bbfa80) → [`00bbfac0`](#insn-00bbfac0)
  - `FALL_THROUGH` [`00bbfa80`](#insn-00bbfa80) → [`00bbfa84`](#insn-00bbfa84)
- ブロック [`00bbfa84`](#insn-00bbfa84) 範囲 `[['00bbfa84', '00bbfa8b']]`
  - `CONDITIONAL_JUMP` [`00bbfa88`](#insn-00bbfa88) → [`00bbfaa0`](#insn-00bbfaa0)
  - `FALL_THROUGH` [`00bbfa88`](#insn-00bbfa88) → [`00bbfa8c`](#insn-00bbfa8c)
- ブロック [`00bbfa8c`](#insn-00bbfa8c) 範囲 `[['00bbfa8c', '00bbfa9f']]`
  - `FALL_THROUGH` [`00bbfa9c`](#insn-00bbfa9c) → [`00bbfaa0`](#insn-00bbfaa0)
- ブロック [`00bbfaa0`](#insn-00bbfaa0) 範囲 `[['00bbfaa0', '00bbfaa3']]`
  - `CONDITIONAL_JUMP` [`00bbfaa0`](#insn-00bbfaa0) → [`00bbfca4`](#insn-00bbfca4)
  - `FALL_THROUGH` [`00bbfaa0`](#insn-00bbfaa0) → [`00bbfaa4`](#insn-00bbfaa4)
- ブロック [`00bbfaa4`](#insn-00bbfaa4) 範囲 `[['00bbfaa4', '00bbfaaf']]`
  - `CONDITIONAL_JUMP` [`00bbfaac`](#insn-00bbfaac) → [`00bbfaec`](#insn-00bbfaec)
  - `FALL_THROUGH` [`00bbfaac`](#insn-00bbfaac) → [`00bbfab0`](#insn-00bbfab0)
- ブロック [`00bbfab0`](#insn-00bbfab0) 範囲 `[['00bbfab0', '00bbfabf']]`
  - `UNCONDITIONAL_JUMP` [`00bbfabc`](#insn-00bbfabc) → [`00bbfaf0`](#insn-00bbfaf0)
- ブロック [`00bbfac0`](#insn-00bbfac0) 範囲 `[['00bbfac0', '00bbfadb']]`
  - `CONDITIONAL_JUMP` [`00bbfad8`](#insn-00bbfad8) → [`00bbfbf8`](#insn-00bbfbf8)
  - `FALL_THROUGH` [`00bbfad8`](#insn-00bbfad8) → [`00bbfadc`](#insn-00bbfadc)
- ブロック [`00bbfadc`](#insn-00bbfadc) 範囲 `[['00bbfadc', '00bbfae3']]`
  - `CONDITIONAL_JUMP` [`00bbfae0`](#insn-00bbfae0) → [`00bbfb90`](#insn-00bbfb90)
  - `FALL_THROUGH` [`00bbfae0`](#insn-00bbfae0) → [`00bbfae4`](#insn-00bbfae4)
- ブロック [`00bbfae4`](#insn-00bbfae4) 範囲 `[['00bbfae4', '00bbfaeb']]`
  - `UNCONDITIONAL_JUMP` [`00bbfae8`](#insn-00bbfae8) → [`00bbfbe8`](#insn-00bbfbe8)
- ブロック [`00bbfaec`](#insn-00bbfaec) 範囲 `[['00bbfaec', '00bbfaef']]`
  - `FALL_THROUGH` [`00bbfaec`](#insn-00bbfaec) → [`00bbfaf0`](#insn-00bbfaf0)
- ブロック [`00bbfaf0`](#insn-00bbfaf0) 範囲 `[['00bbfaf0', '00bbfb13']]`
  - `CONDITIONAL_JUMP` [`00bbfb10`](#insn-00bbfb10) → [`00bbfb84`](#insn-00bbfb84)
  - `FALL_THROUGH` [`00bbfb10`](#insn-00bbfb10) → [`00bbfb14`](#insn-00bbfb14)
- ブロック [`00bbfb14`](#insn-00bbfb14) 範囲 `[['00bbfb14', '00bbfb1b']]`
  - `CONDITIONAL_JUMP` [`00bbfb18`](#insn-00bbfb18) → [`00bbfb6c`](#insn-00bbfb6c)
  - `FALL_THROUGH` [`00bbfb18`](#insn-00bbfb18) → [`00bbfb1c`](#insn-00bbfb1c)
- ブロック [`00bbfb1c`](#insn-00bbfb1c) 範囲 `[['00bbfb1c', '00bbfb23']]`
  - `CONDITIONAL_JUMP` [`00bbfb20`](#insn-00bbfb20) → [`00bbfb30`](#insn-00bbfb30)
  - `FALL_THROUGH` [`00bbfb20`](#insn-00bbfb20) → [`00bbfb24`](#insn-00bbfb24)
- ブロック [`00bbfb24`](#insn-00bbfb24) 範囲 `[['00bbfb24', '00bbfb2f']]`
  - `CONDITIONAL_JUMP` [`00bbfb2c`](#insn-00bbfb2c) → [`00bbfb6c`](#insn-00bbfb6c)
  - `FALL_THROUGH` [`00bbfb2c`](#insn-00bbfb2c) → [`00bbfb30`](#insn-00bbfb30)
- ブロック [`00bbfb30`](#insn-00bbfb30) 範囲 `[['00bbfb30', '00bbfb47']]`
  - `FALL_THROUGH` [`00bbfb44`](#insn-00bbfb44) → [`00bbfb48`](#insn-00bbfb48)
- ブロック [`00bbfb48`](#insn-00bbfb48) 範囲 `[['00bbfb48', '00bbfb5f']]`
  - `CONDITIONAL_JUMP` [`00bbfb5c`](#insn-00bbfb5c) → [`00bbfb48`](#insn-00bbfb48)
  - `FALL_THROUGH` [`00bbfb5c`](#insn-00bbfb5c) → [`00bbfb60`](#insn-00bbfb60)
- ブロック [`00bbfb60`](#insn-00bbfb60) 範囲 `[['00bbfb60', '00bbfb6b']]`
  - `CONDITIONAL_JUMP` [`00bbfb68`](#insn-00bbfb68) → [`00bbfb88`](#insn-00bbfb88)
  - `FALL_THROUGH` [`00bbfb68`](#insn-00bbfb68) → [`00bbfb6c`](#insn-00bbfb6c)
- ブロック [`00bbfb6c`](#insn-00bbfb6c) 範囲 `[['00bbfb6c', '00bbfb6f']]`
  - `FALL_THROUGH` [`00bbfb6c`](#insn-00bbfb6c) → [`00bbfb70`](#insn-00bbfb70)
- ブロック [`00bbfb70`](#insn-00bbfb70) 範囲 `[['00bbfb70', '00bbfb7b']]`
  - `FALL_THROUGH` [`00bbfb78`](#insn-00bbfb78) → [`00bbfb7c`](#insn-00bbfb7c)
- ブロック [`00bbfb7c`](#insn-00bbfb7c) 範囲 `[['00bbfb7c', '00bbfb7f']]`
  - `CONDITIONAL_JUMP` [`00bbfb7c`](#insn-00bbfb7c) → [`00bbfb70`](#insn-00bbfb70)
  - `FALL_THROUGH` [`00bbfb7c`](#insn-00bbfb7c) → [`00bbfb80`](#insn-00bbfb80)
- ブロック [`00bbfb80`](#insn-00bbfb80) 範囲 `[['00bbfb80', '00bbfb83']]`
  - `UNCONDITIONAL_JUMP` [`00bbfb80`](#insn-00bbfb80) → [`00bbfb88`](#insn-00bbfb88)
- ブロック [`00bbfb84`](#insn-00bbfb84) 範囲 `[['00bbfb84', '00bbfb87']]`
  - `FALL_THROUGH` [`00bbfb84`](#insn-00bbfb84) → [`00bbfb88`](#insn-00bbfb88)
- ブロック [`00bbfb88`](#insn-00bbfb88) 範囲 `[['00bbfb88', '00bbfb8f']]`
  - `UNCONDITIONAL_JUMP` [`00bbfb8c`](#insn-00bbfb8c) → [`00bbfc94`](#insn-00bbfc94)
- ブロック [`00bbfb90`](#insn-00bbfb90) 範囲 `[['00bbfb90', '00bbfb97']]`
  - `CONDITIONAL_JUMP` [`00bbfb94`](#insn-00bbfb94) → [`00bbfbb0`](#insn-00bbfbb0)
  - `FALL_THROUGH` [`00bbfb94`](#insn-00bbfb94) → [`00bbfb98`](#insn-00bbfb98)
- ブロック [`00bbfb98`](#insn-00bbfb98) 範囲 `[['00bbfb98', '00bbfba7']]`
  - `CONDITIONAL_JUMP` [`00bbfba4`](#insn-00bbfba4) → [`00bbfbb0`](#insn-00bbfbb0)
  - `FALL_THROUGH` [`00bbfba4`](#insn-00bbfba4) → [`00bbfba8`](#insn-00bbfba8)
- ブロック [`00bbfba8`](#insn-00bbfba8) 範囲 `[['00bbfba8', '00bbfbaf']]`
  - `UNCONDITIONAL_JUMP` [`00bbfbac`](#insn-00bbfbac) → [`00bbfbe8`](#insn-00bbfbe8)
- ブロック [`00bbfbb0`](#insn-00bbfbb0) 範囲 `[['00bbfbb0', '00bbfbc7']]`
  - `FALL_THROUGH` [`00bbfbc4`](#insn-00bbfbc4) → [`00bbfbc8`](#insn-00bbfbc8)
- ブロック [`00bbfbc8`](#insn-00bbfbc8) 範囲 `[['00bbfbc8', '00bbfbcb']]`
  - `FALL_THROUGH` [`00bbfbc8`](#insn-00bbfbc8) → [`00bbfbcc`](#insn-00bbfbcc)
- ブロック [`00bbfbcc`](#insn-00bbfbcc) 範囲 `[['00bbfbcc', '00bbfbdf']]`
  - `CONDITIONAL_JUMP` [`00bbfbdc`](#insn-00bbfbdc) → [`00bbfbc8`](#insn-00bbfbc8)
  - `FALL_THROUGH` [`00bbfbdc`](#insn-00bbfbdc) → [`00bbfbe0`](#insn-00bbfbe0)
- ブロック [`00bbfbe0`](#insn-00bbfbe0) 範囲 `[['00bbfbe0', '00bbfbe7']]`
  - `CONDITIONAL_JUMP` [`00bbfbe4`](#insn-00bbfbe4) → [`00bbfbf8`](#insn-00bbfbf8)
  - `FALL_THROUGH` [`00bbfbe4`](#insn-00bbfbe4) → [`00bbfbe8`](#insn-00bbfbe8)
- ブロック [`00bbfbe8`](#insn-00bbfbe8) 範囲 `[['00bbfbe8', '00bbfbf7']]`
  - `CONDITIONAL_JUMP` [`00bbfbf4`](#insn-00bbfbf4) → [`00bbfbe8`](#insn-00bbfbe8)
  - `FALL_THROUGH` [`00bbfbf4`](#insn-00bbfbf4) → [`00bbfbf8`](#insn-00bbfbf8)
- ブロック [`00bbfbf8`](#insn-00bbfbf8) 範囲 `[['00bbfbf8', '00bbfbff']]`
  - `CONDITIONAL_JUMP` [`00bbfbfc`](#insn-00bbfbfc) → [`00bbfc20`](#insn-00bbfc20)
  - `FALL_THROUGH` [`00bbfbfc`](#insn-00bbfbfc) → [`00bbfc00`](#insn-00bbfc00)
- ブロック [`00bbfc00`](#insn-00bbfc00) 範囲 `[['00bbfc00', '00bbfc0f']]`
  - `CONDITIONAL_JUMP` [`00bbfc0c`](#insn-00bbfc0c) → [`00bbfc90`](#insn-00bbfc90)
  - `FALL_THROUGH` [`00bbfc0c`](#insn-00bbfc0c) → [`00bbfc10`](#insn-00bbfc10)
- ブロック [`00bbfc10`](#insn-00bbfc10) 範囲 `[['00bbfc10', '00bbfc17']]`
  - `CONDITIONAL_JUMP` [`00bbfc14`](#insn-00bbfc14) → [`00bbfc28`](#insn-00bbfc28)
  - `FALL_THROUGH` [`00bbfc14`](#insn-00bbfc14) → [`00bbfc18`](#insn-00bbfc18)
- ブロック [`00bbfc18`](#insn-00bbfc18) 範囲 `[['00bbfc18', '00bbfc1f']]`
  - `UNCONDITIONAL_JUMP` [`00bbfc1c`](#insn-00bbfc1c) → [`00bbfc7c`](#insn-00bbfc7c)
- ブロック [`00bbfc20`](#insn-00bbfc20) 範囲 `[['00bbfc20', '00bbfc27']]`
  - `UNCONDITIONAL_JUMP` [`00bbfc24`](#insn-00bbfc24) → [`00bbfc94`](#insn-00bbfc94)
- ブロック [`00bbfc28`](#insn-00bbfc28) 範囲 `[['00bbfc28', '00bbfc2f']]`
  - `CONDITIONAL_JUMP` [`00bbfc2c`](#insn-00bbfc2c) → [`00bbfc44`](#insn-00bbfc44)
  - `FALL_THROUGH` [`00bbfc2c`](#insn-00bbfc2c) → [`00bbfc30`](#insn-00bbfc30)
- ブロック [`00bbfc30`](#insn-00bbfc30) 範囲 `[['00bbfc30', '00bbfc3b']]`
  - `CONDITIONAL_JUMP` [`00bbfc38`](#insn-00bbfc38) → [`00bbfc44`](#insn-00bbfc44)
  - `FALL_THROUGH` [`00bbfc38`](#insn-00bbfc38) → [`00bbfc3c`](#insn-00bbfc3c)
- ブロック [`00bbfc3c`](#insn-00bbfc3c) 範囲 `[['00bbfc3c', '00bbfc43']]`
  - `UNCONDITIONAL_JUMP` [`00bbfc40`](#insn-00bbfc40) → [`00bbfc7c`](#insn-00bbfc7c)
- ブロック [`00bbfc44`](#insn-00bbfc44) 範囲 `[['00bbfc44', '00bbfc5b']]`
  - `FALL_THROUGH` [`00bbfc58`](#insn-00bbfc58) → [`00bbfc5c`](#insn-00bbfc5c)
- ブロック [`00bbfc5c`](#insn-00bbfc5c) 範囲 `[['00bbfc5c', '00bbfc73']]`
  - `CONDITIONAL_JUMP` [`00bbfc70`](#insn-00bbfc70) → [`00bbfc5c`](#insn-00bbfc5c)
  - `FALL_THROUGH` [`00bbfc70`](#insn-00bbfc70) → [`00bbfc74`](#insn-00bbfc74)
- ブロック [`00bbfc74`](#insn-00bbfc74) 範囲 `[['00bbfc74', '00bbfc7b']]`
  - `CONDITIONAL_JUMP` [`00bbfc78`](#insn-00bbfc78) → [`00bbfc8c`](#insn-00bbfc8c)
  - `FALL_THROUGH` [`00bbfc78`](#insn-00bbfc78) → [`00bbfc7c`](#insn-00bbfc7c)
- ブロック [`00bbfc7c`](#insn-00bbfc7c) 範囲 `[['00bbfc7c', '00bbfc8b']]`
  - `CONDITIONAL_JUMP` [`00bbfc88`](#insn-00bbfc88) → [`00bbfc7c`](#insn-00bbfc7c)
  - `FALL_THROUGH` [`00bbfc88`](#insn-00bbfc88) → [`00bbfc8c`](#insn-00bbfc8c)
- ブロック [`00bbfc8c`](#insn-00bbfc8c) 範囲 `[['00bbfc8c', '00bbfc8f']]`
  - `FALL_THROUGH` [`00bbfc8c`](#insn-00bbfc8c) → [`00bbfc90`](#insn-00bbfc90)
- ブロック [`00bbfc90`](#insn-00bbfc90) 範囲 `[['00bbfc90', '00bbfc93']]`
  - `FALL_THROUGH` [`00bbfc90`](#insn-00bbfc90) → [`00bbfc94`](#insn-00bbfc94)
- ブロック [`00bbfc94`](#insn-00bbfc94) 範囲 `[['00bbfc94', '00bbfc9f']]`
  - `FALL_THROUGH` [`00bbfc9c`](#insn-00bbfc9c) → [`00bbfca0`](#insn-00bbfca0)
- ブロック [`00bbfca0`](#insn-00bbfca0) 範囲 `[['00bbfca0', '00bbfca3']]`
- ブロック [`00bbfca4`](#insn-00bbfca4) 範囲 `[['00bbfca4', '00bbfcab']]`

## 命令位置別の参照

- [`00bbfa4c`](#insn-00bbfa4c) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfa50`](#insn-00bbfa50) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfa54`](#insn-00bbfa54) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfa80`](#insn-00bbfa80) → [`00bbfac0`](#insn-00bbfac0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfa88`](#insn-00bbfa88) → [`00bbfaa0`](#insn-00bbfaa0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfa90`](#insn-00bbfa90) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00bbfaa0`](#insn-00bbfaa0) → [`00bbfca4`](#insn-00bbfca4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfaac`](#insn-00bbfaac) → [`00bbfaec`](#insn-00bbfaec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfabc`](#insn-00bbfabc) → [`00bbfaf0`](#insn-00bbfaf0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfad8`](#insn-00bbfad8) → [`00bbfbf8`](#insn-00bbfbf8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfae0`](#insn-00bbfae0) → [`00bbfb90`](#insn-00bbfb90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfae8`](#insn-00bbfae8) → [`00bbfbe8`](#insn-00bbfbe8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfaf4`](#insn-00bbfaf4) → [`00c58f30`](../00c58/00c58f30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f30` · 推定シンボル `None` · 推定型 `None`
- [`00bbfb10`](#insn-00bbfb10) → [`00bbfb84`](#insn-00bbfb84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfb18`](#insn-00bbfb18) → [`00bbfb6c`](#insn-00bbfb6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfb20`](#insn-00bbfb20) → [`00bbfb30`](#insn-00bbfb30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfb2c`](#insn-00bbfb2c) → [`00bbfb6c`](#insn-00bbfb6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfb5c`](#insn-00bbfb5c) → [`00bbfb48`](#insn-00bbfb48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfb68`](#insn-00bbfb68) → [`00bbfb88`](#insn-00bbfb88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfb7c`](#insn-00bbfb7c) → [`00bbfb70`](#insn-00bbfb70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfb80`](#insn-00bbfb80) → [`00bbfb88`](#insn-00bbfb88) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfb8c`](#insn-00bbfb8c) → [`00bbfc94`](#insn-00bbfc94) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfb94`](#insn-00bbfb94) → [`00bbfbb0`](#insn-00bbfbb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfba4`](#insn-00bbfba4) → [`00bbfbb0`](#insn-00bbfbb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfbac`](#insn-00bbfbac) → [`00bbfbe8`](#insn-00bbfbe8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfbdc`](#insn-00bbfbdc) → [`00bbfbc8`](#insn-00bbfbc8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfbe4`](#insn-00bbfbe4) → [`00bbfbf8`](#insn-00bbfbf8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfbf4`](#insn-00bbfbf4) → [`00bbfbe8`](#insn-00bbfbe8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfbfc`](#insn-00bbfbfc) → [`00bbfc20`](#insn-00bbfc20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfc0c`](#insn-00bbfc0c) → [`00bbfc90`](#insn-00bbfc90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfc14`](#insn-00bbfc14) → [`00bbfc28`](#insn-00bbfc28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfc1c`](#insn-00bbfc1c) → [`00bbfc7c`](#insn-00bbfc7c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfc24`](#insn-00bbfc24) → [`00bbfc94`](#insn-00bbfc94) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfc2c`](#insn-00bbfc2c) → [`00bbfc44`](#insn-00bbfc44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfc38`](#insn-00bbfc38) → [`00bbfc44`](#insn-00bbfc44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfc40`](#insn-00bbfc40) → [`00bbfc7c`](#insn-00bbfc7c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfc70`](#insn-00bbfc70) → [`00bbfc5c`](#insn-00bbfc5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfc78`](#insn-00bbfc78) → [`00bbfc8c`](#insn-00bbfc8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfc88`](#insn-00bbfc88) → [`00bbfc7c`](#insn-00bbfc7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfc94`](#insn-00bbfc94) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfc98`](#insn-00bbfc98) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfca8`](#insn-00bbfca8) → [`00c5bdb0`](../00c5b/00c5bdb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bdb0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbfa4c`](#insn-00bbfa4c)

~~~json
{
  "source": "00bbfa4c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfa50`](#insn-00bbfa50)

~~~json
{
  "source": "00bbfa50",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfa54`](#insn-00bbfa54)

~~~json
{
  "source": "00bbfa54",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfa80`](#insn-00bbfa80)

~~~json
{
  "source": "00bbfa80",
  "target": "00bbfac0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfa88`](#insn-00bbfa88)

~~~json
{
  "source": "00bbfa88",
  "target": "00bbfaa0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfa90`](#insn-00bbfa90)

~~~json
{
  "source": "00bbfa90",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbfaa0`](#insn-00bbfaa0)

~~~json
{
  "source": "00bbfaa0",
  "target": "00bbfca4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfaac`](#insn-00bbfaac)

~~~json
{
  "source": "00bbfaac",
  "target": "00bbfaec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfabc`](#insn-00bbfabc)

~~~json
{
  "source": "00bbfabc",
  "target": "00bbfaf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfad8`](#insn-00bbfad8)

~~~json
{
  "source": "00bbfad8",
  "target": "00bbfbf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfae0`](#insn-00bbfae0)

~~~json
{
  "source": "00bbfae0",
  "target": "00bbfb90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfae8`](#insn-00bbfae8)

~~~json
{
  "source": "00bbfae8",
  "target": "00bbfbe8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfaf4`](#insn-00bbfaf4)

~~~json
{
  "source": "00bbfaf4",
  "target": "00c58f30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbfb10`](#insn-00bbfb10)

~~~json
{
  "source": "00bbfb10",
  "target": "00bbfb84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfb18`](#insn-00bbfb18)

~~~json
{
  "source": "00bbfb18",
  "target": "00bbfb6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfb20`](#insn-00bbfb20)

~~~json
{
  "source": "00bbfb20",
  "target": "00bbfb30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfb2c`](#insn-00bbfb2c)

~~~json
{
  "source": "00bbfb2c",
  "target": "00bbfb6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfb5c`](#insn-00bbfb5c)

~~~json
{
  "source": "00bbfb5c",
  "target": "00bbfb48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfb68`](#insn-00bbfb68)

~~~json
{
  "source": "00bbfb68",
  "target": "00bbfb88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfb7c`](#insn-00bbfb7c)

~~~json
{
  "source": "00bbfb7c",
  "target": "00bbfb70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfb80`](#insn-00bbfb80)

~~~json
{
  "source": "00bbfb80",
  "target": "00bbfb88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfb8c`](#insn-00bbfb8c)

~~~json
{
  "source": "00bbfb8c",
  "target": "00bbfc94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfb94`](#insn-00bbfb94)

~~~json
{
  "source": "00bbfb94",
  "target": "00bbfbb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfba4`](#insn-00bbfba4)

~~~json
{
  "source": "00bbfba4",
  "target": "00bbfbb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfbac`](#insn-00bbfbac)

~~~json
{
  "source": "00bbfbac",
  "target": "00bbfbe8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfbdc`](#insn-00bbfbdc)

~~~json
{
  "source": "00bbfbdc",
  "target": "00bbfbc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfbe4`](#insn-00bbfbe4)

~~~json
{
  "source": "00bbfbe4",
  "target": "00bbfbf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfbf4`](#insn-00bbfbf4)

~~~json
{
  "source": "00bbfbf4",
  "target": "00bbfbe8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfbfc`](#insn-00bbfbfc)

~~~json
{
  "source": "00bbfbfc",
  "target": "00bbfc20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfc0c`](#insn-00bbfc0c)

~~~json
{
  "source": "00bbfc0c",
  "target": "00bbfc90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfc14`](#insn-00bbfc14)

~~~json
{
  "source": "00bbfc14",
  "target": "00bbfc28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfc1c`](#insn-00bbfc1c)

~~~json
{
  "source": "00bbfc1c",
  "target": "00bbfc7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfc24`](#insn-00bbfc24)

~~~json
{
  "source": "00bbfc24",
  "target": "00bbfc94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfc2c`](#insn-00bbfc2c)

~~~json
{
  "source": "00bbfc2c",
  "target": "00bbfc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfc38`](#insn-00bbfc38)

~~~json
{
  "source": "00bbfc38",
  "target": "00bbfc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfc40`](#insn-00bbfc40)

~~~json
{
  "source": "00bbfc40",
  "target": "00bbfc7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfc70`](#insn-00bbfc70)

~~~json
{
  "source": "00bbfc70",
  "target": "00bbfc5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfc78`](#insn-00bbfc78)

~~~json
{
  "source": "00bbfc78",
  "target": "00bbfc8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfc88`](#insn-00bbfc88)

~~~json
{
  "source": "00bbfc88",
  "target": "00bbfc7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfc94`](#insn-00bbfc94)

~~~json
{
  "source": "00bbfc94",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfc98`](#insn-00bbfc98)

~~~json
{
  "source": "00bbfc98",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfca8`](#insn-00bbfca8)

~~~json
{
  "source": "00bbfca8",
  "target": "00c5bdb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
