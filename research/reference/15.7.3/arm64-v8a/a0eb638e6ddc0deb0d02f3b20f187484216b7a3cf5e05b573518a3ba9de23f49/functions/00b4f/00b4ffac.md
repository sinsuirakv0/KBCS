# 00b4ffac

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00b4fee4`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4f/00b4fee4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/alignment_unresolved-0004.md#compare-8b0accc5b91c547f503b5e6587b3a5dc)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b4fff0`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4f/00b4fff0.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0012.md#compare-1c16f0cb2cf4d9a3747f53aedaef048e)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b4ffac",
  "name": "_ZNSt6__ndk16vectorIhNS_9allocatorIhEEE6assignIN11flatbuffers14VectorIteratorIhhEEEENS_9enable_ifIXaasr21__is_forward_iteratorIT_EE5valuesr16is_constructibleIhNS_15iterator_traitsIS9_E9referenceEEE5valueEvE4typeES9_S9_",
  "size": 608,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7e2242dfa2ee451206b1ac9383e664e2df418387d071223adb288888e7ec90c2",
  "source_text_sha256": "7e2242dfa2ee451206b1ac9383e664e2df418387d071223adb288888e7ec90c2",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b4ffac",
        "00b5020b"
      ]
    ],
    "bytes_sha256": "0c2962e28955512b33950e93199ed45df8dacad04e55474df9d395ab8fcbdc2a",
    "instruction_count": 152,
    "instruction_bytes": 608,
    "body_bytes": 608,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00be0530](../00be0/00be0530.md)

## 呼び出し先

- [00bdaff0](../00bda/00bdaff0.md)
- [00bdb010](../00bdb/00bdb010.md)
- [00bdde60](../00bdd/00bdde60.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 5257 bytes

~~~c

void _ZNSt6__ndk16vectorIhNS_9allocatorIhEEE6assignIN11flatbuffers14VectorIteratorIhhEEEENS_9enable_ifIXaasr21__is_forward_iteratorIT_EE5valuesr16is_constructibleIhNS_15iterator_traitsIS9_E9referenceEEE5valueEvE4typeES9_S9_
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
                    /* try { // try from 00b4fffc to 00c50003 has its CatchHandler @ 00b50070 */
      param_1[2] = 0;
    }
    if ((long)uVar13 < 0) {
                    /* WARNING: Subroutine does not return */
      _ZNKSt6__ndk120__vector_base_commonILb1EE20__throw_length_errorEv(param_1);
    }
                    /* try { // try from 00b50004 to 00c50097 has its CatchHandler @ 00b4ff68 */
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
                    /* catch() { ... } // from try @ 00b4fffc with catch @ 00b50070 */
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
        if (uVar13 == uVar8) goto LAB_00b500e8;
      }
      do {
        puVar5 = puVar2 + 1;
        puVar7 = puVar6 + 1;
        *puVar6 = *puVar2;
        puVar2 = puVar5;
        puVar6 = puVar7;
      } while (puVar4 != puVar5);
    }
LAB_00b500e8:
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
      if (uVar11 == uVar8) goto LAB_00b50158;
    }
    do {
      puVar5 = puVar7 + 1;
      puVar2 = puVar6 + 1;
      *puVar6 = *puVar7;
      puVar6 = puVar2;
      puVar7 = puVar5;
    } while (puVar4 != puVar5);
  }
LAB_00b50158:
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
      if (uVar8 == uVar13) goto LAB_00b501f0;
    }
    do {
      puVar5 = puVar4 + 1;
      puVar2 = puVar7 + 1;
      *puVar7 = *puVar4;
      puVar4 = puVar5;
      puVar7 = puVar2;
    } while (puVar6 != puVar5);
  }
LAB_00b501f0:
  param_1[1] = puVar2;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b4ffac"></a> `00b4ffac` | `f6 57 bd a9` | stp x22,x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00b4ffb0"></a> `00b4ffb0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b4ffb4"></a> `00b4ffb4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b4ffb8"></a> `00b4ffb8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00b4ffbc"></a> `00b4ffbc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00b4ffc0"></a> `00b4ffc0` | `2c 00 40 f9` | ldr x12,[x1] | `FALL_THROUGH`
<a id="insn-00b4ffc4"></a> `00b4ffc4` | `4a 00 40 f9` | ldr x10,[x2] | `FALL_THROUGH`
<a id="insn-00b4ffc8"></a> `00b4ffc8` | `08 08 40 f9` | ldr x8,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00b4ffcc"></a> `00b4ffcc` | `00 00 40 f9` | ldr x0,[x0] | `FALL_THROUGH`
<a id="insn-00b4ffd0"></a> `00b4ffd0` | `f4 03 02 aa` | mov x20,x2 | `FALL_THROUGH`
<a id="insn-00b4ffd4"></a> `00b4ffd4` | `56 01 0c cb` | sub x22,x10,x12 | `FALL_THROUGH`
<a id="insn-00b4ffd8"></a> `00b4ffd8` | `09 01 00 cb` | sub x9,x8,x0 | `FALL_THROUGH`
<a id="insn-00b4ffdc"></a> `00b4ffdc` | `df 02 09 eb` | cmp x22,x9 | `FALL_THROUGH`
<a id="insn-00b4ffe0"></a> `00b4ffe0` | `09 02 00 54` | b.ls 0x00b50020 | `CONDITIONAL_JUMP`
<a id="insn-00b4ffe4"></a> `00b4ffe4` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-00b4ffe8"></a> `00b4ffe8` | `c0 00 00 b4` | cbz x0,0x00b50000 | `CONDITIONAL_JUMP`
<a id="insn-00b4ffec"></a> `00b4ffec` | `60 06 00 f9` | str x0,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00b4fff0"></a> `00b4fff0` | `08 2c 02 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00b4fff4"></a> `00b4fff4` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00b4fff8"></a> `00b4fff8` | `7f 7e 00 a9` | stp xzr,xzr,[x19] | `FALL_THROUGH`
<a id="insn-00b4fffc"></a> `00b4fffc` | `7f 0a 00 f9` | str xzr,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00b50000"></a> `00b50000` | `36 10 f8 b7` | tbnz x22,#0x3f,0x00b50204 | `CONDITIONAL_JUMP`
<a id="insn-00b50004"></a> `00b50004` | `e9 f3 7f b2` | orr x9,xzr,#0x3ffffffffffffffe | `FALL_THROUGH`
<a id="insn-00b50008"></a> `00b50008` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00b5000c"></a> `00b5000c` | `08 02 00 54` | b.hi 0x00b5004c | `CONDITIONAL_JUMP`
<a id="insn-00b50010"></a> `00b50010` | `08 f9 7f d3` | lsl x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00b50014"></a> `00b50014` | `1f 01 16 eb` | cmp x8,x22 | `FALL_THROUGH`
<a id="insn-00b50018"></a> `00b50018` | `d6 32 88 9a` | csel x22,x22,x8,cc | `FALL_THROUGH`
<a id="insn-00b5001c"></a> `00b5001c` | `0d 00 00 14` | b 0x00b50050 | `UNCONDITIONAL_JUMP`
<a id="insn-00b50020"></a> `00b50020` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00b50024"></a> `00b50024` | `09 01 00 cb` | sub x9,x8,x0 | `FALL_THROUGH`
<a id="insn-00b50028"></a> `00b50028` | `88 41 29 8b` | add x8,x12,w9, UXTW  | `FALL_THROUGH`
<a id="insn-00b5002c"></a> `00b5002c` | `df 02 09 eb` | cmp x22,x9 | `FALL_THROUGH`
<a id="insn-00b50030"></a> `00b50030` | `08 81 8a 9a` | csel x8,x8,x10,hi | `FALL_THROUGH`
<a id="insn-00b50034"></a> `00b50034` | `0b 01 0c eb` | subs x11,x8,x12 | `FALL_THROUGH`
<a id="insn-00b50038"></a> `00b50038` | `00 09 00 54` | b.eq 0x00b50158 | `CONDITIONAL_JUMP`
<a id="insn-00b5003c"></a> `00b5003c` | `7f 81 00 f1` | cmp x11,#0x20 | `FALL_THROUGH`
<a id="insn-00b50040"></a> `00b50040` | `82 05 00 54` | b.cs 0x00b500f0 | `CONDITIONAL_JUMP`
<a id="insn-00b50044"></a> `00b50044` | `ea 03 0c aa` | mov x10,x12 | `FALL_THROUGH`
<a id="insn-00b50048"></a> `00b50048` | `40 00 00 14` | b 0x00b50148 | `UNCONDITIONAL_JUMP`
<a id="insn-00b5004c"></a> `00b5004c` | `16 00 f0 92` | mov x22,#0x7fffffffffffffff | `FALL_THROUGH`
<a id="insn-00b50050"></a> `00b50050` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00b50054"></a> `00b50054` | `e7 2b 02 94` | bl 0x00bdaff0 | `UNCONDITIONAL_CALL`
<a id="insn-00b50058"></a> `00b50058` | `08 00 16 8b` | add x8,x0,x22 | `FALL_THROUGH`
<a id="insn-00b5005c"></a> `00b5005c` | `60 02 00 a9` | stp x0,x0,[x19] | `FALL_THROUGH`
<a id="insn-00b50060"></a> `00b50060` | `68 0a 00 f9` | str x8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00b50064"></a> `00b50064` | `a9 02 40 f9` | ldr x9,[x21] | `FALL_THROUGH`
<a id="insn-00b50068"></a> `00b50068` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00b5006c"></a> `00b5006c` | `0b 01 09 eb` | subs x11,x8,x9 | `FALL_THROUGH`
<a id="insn-00b50070"></a> `00b50070` | `a0 03 00 54` | b.eq 0x00b500e4 | `CONDITIONAL_JUMP`
<a id="insn-00b50074"></a> `00b50074` | `7f 81 00 f1` | cmp x11,#0x20 | `FALL_THROUGH`
<a id="insn-00b50078"></a> `00b50078` | `a3 02 00 54` | b.cc 0x00b500cc | `CONDITIONAL_JUMP`
<a id="insn-00b5007c"></a> `00b5007c` | `1f 00 08 eb` | cmp x0,x8 | `FALL_THROUGH`
<a id="insn-00b50080"></a> `00b50080` | `82 00 00 54` | b.cs 0x00b50090 | `CONDITIONAL_JUMP`
<a id="insn-00b50084"></a> `00b50084` | `0a 00 0b 8b` | add x10,x0,x11 | `FALL_THROUGH`
<a id="insn-00b50088"></a> `00b50088` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00b5008c"></a> `00b5008c` | `03 02 00 54` | b.cc 0x00b500cc | `CONDITIONAL_JUMP`
<a id="insn-00b50090"></a> `00b50090` | `6c e9 7b 92` | and x12,x11,#-0x20 | `FALL_THROUGH`
<a id="insn-00b50094"></a> `00b50094` | `2d 41 00 91` | add x13,x9,#0x10 | `FALL_THROUGH`
<a id="insn-00b50098"></a> `00b50098` | `0a 00 0c 8b` | add x10,x0,x12 | `FALL_THROUGH`
<a id="insn-00b5009c"></a> `00b5009c` | `29 01 0c 8b` | add x9,x9,x12 | `FALL_THROUGH`
<a id="insn-00b500a0"></a> `00b500a0` | `0e 40 00 91` | add x14,x0,#0x10 | `FALL_THROUGH`
<a id="insn-00b500a4"></a> `00b500a4` | `ef 03 0c aa` | mov x15,x12 | `FALL_THROUGH`
<a id="insn-00b500a8"></a> `00b500a8` | `a0 85 7f ad` | ldp q0,q1,[x13, #-0x10] | `FALL_THROUGH`
<a id="insn-00b500ac"></a> `00b500ac` | `ad 81 00 91` | add x13,x13,#0x20 | `FALL_THROUGH`
<a id="insn-00b500b0"></a> `00b500b0` | `ef 81 00 f1` | subs x15,x15,#0x20 | `FALL_THROUGH`
<a id="insn-00b500b4"></a> `00b500b4` | `c0 85 3f ad` | stp q0,q1,[x14, #-0x10] | `FALL_THROUGH`
<a id="insn-00b500b8"></a> `00b500b8` | `ce 81 00 91` | add x14,x14,#0x20 | `FALL_THROUGH`
<a id="insn-00b500bc"></a> `00b500bc` | `61 ff ff 54` | b.ne 0x00b500a8 | `CONDITIONAL_JUMP`
<a id="insn-00b500c0"></a> `00b500c0` | `7f 01 0c eb` | cmp x11,x12 | `FALL_THROUGH`
<a id="insn-00b500c4"></a> `00b500c4` | `e0 03 0a aa` | mov x0,x10 | `FALL_THROUGH`
<a id="insn-00b500c8"></a> `00b500c8` | `00 01 00 54` | b.eq 0x00b500e8 | `CONDITIONAL_JUMP`
<a id="insn-00b500cc"></a> `00b500cc` | `ea 03 00 aa` | mov x10,x0 | `FALL_THROUGH`
<a id="insn-00b500d0"></a> `00b500d0` | `2b 15 40 38` | ldrb w11,[x9], #0x1 | `FALL_THROUGH`
<a id="insn-00b500d4"></a> `00b500d4` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00b500d8"></a> `00b500d8` | `4b 15 00 38` | strb w11,[x10], #0x1 | `FALL_THROUGH`
<a id="insn-00b500dc"></a> `00b500dc` | `a1 ff ff 54` | b.ne 0x00b500d0 | `CONDITIONAL_JUMP`
<a id="insn-00b500e0"></a> `00b500e0` | `02 00 00 14` | b 0x00b500e8 | `UNCONDITIONAL_JUMP`
<a id="insn-00b500e4"></a> `00b500e4` | `ea 03 00 aa` | mov x10,x0 | `FALL_THROUGH`
<a id="insn-00b500e8"></a> `00b500e8` | `6a 06 00 f9` | str x10,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00b500ec"></a> `00b500ec` | `42 00 00 14` | b 0x00b501f4 | `UNCONDITIONAL_JUMP`
<a id="insn-00b500f0"></a> `00b500f0` | `1f 00 08 eb` | cmp x0,x8 | `FALL_THROUGH`
<a id="insn-00b500f4"></a> `00b500f4` | `e2 00 00 54` | b.cs 0x00b50110 | `CONDITIONAL_JUMP`
<a id="insn-00b500f8"></a> `00b500f8` | `0a 00 0c cb` | sub x10,x0,x12 | `FALL_THROUGH`
<a id="insn-00b500fc"></a> `00b500fc` | `0a 01 0a 8b` | add x10,x8,x10 | `FALL_THROUGH`
<a id="insn-00b50100"></a> `00b50100` | `5f 01 0c eb` | cmp x10,x12 | `FALL_THROUGH`
<a id="insn-00b50104"></a> `00b50104` | `69 00 00 54` | b.ls 0x00b50110 | `CONDITIONAL_JUMP`
<a id="insn-00b50108"></a> `00b50108` | `ea 03 0c aa` | mov x10,x12 | `FALL_THROUGH`
<a id="insn-00b5010c"></a> `00b5010c` | `0f 00 00 14` | b 0x00b50148 | `UNCONDITIONAL_JUMP`
<a id="insn-00b50110"></a> `00b50110` | `6d e9 7b 92` | and x13,x11,#-0x20 | `FALL_THROUGH`
<a id="insn-00b50114"></a> `00b50114` | `0e 40 00 91` | add x14,x0,#0x10 | `FALL_THROUGH`
<a id="insn-00b50118"></a> `00b50118` | `8a 01 0d 8b` | add x10,x12,x13 | `FALL_THROUGH`
<a id="insn-00b5011c"></a> `00b5011c` | `00 00 0d 8b` | add x0,x0,x13 | `FALL_THROUGH`
<a id="insn-00b50120"></a> `00b50120` | `8c 41 00 91` | add x12,x12,#0x10 | `FALL_THROUGH`
<a id="insn-00b50124"></a> `00b50124` | `ef 03 0d aa` | mov x15,x13 | `FALL_THROUGH`
<a id="insn-00b50128"></a> `00b50128` | `80 85 7f ad` | ldp q0,q1,[x12, #-0x10] | `FALL_THROUGH`
<a id="insn-00b5012c"></a> `00b5012c` | `ef 81 00 f1` | subs x15,x15,#0x20 | `FALL_THROUGH`
<a id="insn-00b50130"></a> `00b50130` | `8c 81 00 91` | add x12,x12,#0x20 | `FALL_THROUGH`
<a id="insn-00b50134"></a> `00b50134` | `c0 85 3f ad` | stp q0,q1,[x14, #-0x10] | `FALL_THROUGH`
<a id="insn-00b50138"></a> `00b50138` | `ce 81 00 91` | add x14,x14,#0x20 | `FALL_THROUGH`
<a id="insn-00b5013c"></a> `00b5013c` | `61 ff ff 54` | b.ne 0x00b50128 | `CONDITIONAL_JUMP`
<a id="insn-00b50140"></a> `00b50140` | `bf 01 0b eb` | cmp x13,x11 | `FALL_THROUGH`
<a id="insn-00b50144"></a> `00b50144` | `a0 00 00 54` | b.eq 0x00b50158 | `CONDITIONAL_JUMP`
<a id="insn-00b50148"></a> `00b50148` | `4b 15 40 38` | ldrb w11,[x10], #0x1 | `FALL_THROUGH`
<a id="insn-00b5014c"></a> `00b5014c` | `1f 01 0a eb` | cmp x8,x10 | `FALL_THROUGH`
<a id="insn-00b50150"></a> `00b50150` | `0b 14 00 38` | strb w11,[x0], #0x1 | `FALL_THROUGH`
<a id="insn-00b50154"></a> `00b50154` | `a1 ff ff 54` | b.ne 0x00b50148 | `CONDITIONAL_JUMP`
<a id="insn-00b50158"></a> `00b50158` | `df 02 09 eb` | cmp x22,x9 | `FALL_THROUGH`
<a id="insn-00b5015c"></a> `00b5015c` | `29 01 00 54` | b.ls 0x00b50180 | `CONDITIONAL_JUMP`
<a id="insn-00b50160"></a> `00b50160` | `89 02 40 f9` | ldr x9,[x20] | `FALL_THROUGH`
<a id="insn-00b50164"></a> `00b50164` | `6c 06 40 f9` | ldr x12,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00b50168"></a> `00b50168` | `2b 01 08 eb` | subs x11,x9,x8 | `FALL_THROUGH`
<a id="insn-00b5016c"></a> `00b5016c` | `20 04 00 54` | b.eq 0x00b501f0 | `CONDITIONAL_JUMP`
<a id="insn-00b50170"></a> `00b50170` | `7f 81 00 f1` | cmp x11,#0x20 | `FALL_THROUGH`
<a id="insn-00b50174"></a> `00b50174` | `a2 00 00 54` | b.cs 0x00b50188 | `CONDITIONAL_JUMP`
<a id="insn-00b50178"></a> `00b50178` | `ea 03 0c aa` | mov x10,x12 | `FALL_THROUGH`
<a id="insn-00b5017c"></a> `00b5017c` | `18 00 00 14` | b 0x00b501dc | `UNCONDITIONAL_JUMP`
<a id="insn-00b50180"></a> `00b50180` | `60 06 00 f9` | str x0,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00b50184"></a> `00b50184` | `1c 00 00 14` | b 0x00b501f4 | `UNCONDITIONAL_JUMP`
<a id="insn-00b50188"></a> `00b50188` | `3f 01 0c eb` | cmp x9,x12 | `FALL_THROUGH`
<a id="insn-00b5018c"></a> `00b5018c` | `c9 00 00 54` | b.ls 0x00b501a4 | `CONDITIONAL_JUMP`
<a id="insn-00b50190"></a> `00b50190` | `8a 01 0b 8b` | add x10,x12,x11 | `FALL_THROUGH`
<a id="insn-00b50194"></a> `00b50194` | `5f 01 08 eb` | cmp x10,x8 | `FALL_THROUGH`
<a id="insn-00b50198"></a> `00b50198` | `69 00 00 54` | b.ls 0x00b501a4 | `CONDITIONAL_JUMP`
<a id="insn-00b5019c"></a> `00b5019c` | `ea 03 0c aa` | mov x10,x12 | `FALL_THROUGH`
<a id="insn-00b501a0"></a> `00b501a0` | `0f 00 00 14` | b 0x00b501dc | `UNCONDITIONAL_JUMP`
<a id="insn-00b501a4"></a> `00b501a4` | `6d e9 7b 92` | and x13,x11,#-0x20 | `FALL_THROUGH`
<a id="insn-00b501a8"></a> `00b501a8` | `0e 41 00 91` | add x14,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00b501ac"></a> `00b501ac` | `8a 01 0d 8b` | add x10,x12,x13 | `FALL_THROUGH`
<a id="insn-00b501b0"></a> `00b501b0` | `08 01 0d 8b` | add x8,x8,x13 | `FALL_THROUGH`
<a id="insn-00b501b4"></a> `00b501b4` | `8c 41 00 91` | add x12,x12,#0x10 | `FALL_THROUGH`
<a id="insn-00b501b8"></a> `00b501b8` | `ef 03 0d aa` | mov x15,x13 | `FALL_THROUGH`
<a id="insn-00b501bc"></a> `00b501bc` | `c0 85 7f ad` | ldp q0,q1,[x14, #-0x10] | `FALL_THROUGH`
<a id="insn-00b501c0"></a> `00b501c0` | `ce 81 00 91` | add x14,x14,#0x20 | `FALL_THROUGH`
<a id="insn-00b501c4"></a> `00b501c4` | `ef 81 00 f1` | subs x15,x15,#0x20 | `FALL_THROUGH`
<a id="insn-00b501c8"></a> `00b501c8` | `80 85 3f ad` | stp q0,q1,[x12, #-0x10] | `FALL_THROUGH`
<a id="insn-00b501cc"></a> `00b501cc` | `8c 81 00 91` | add x12,x12,#0x20 | `FALL_THROUGH`
<a id="insn-00b501d0"></a> `00b501d0` | `61 ff ff 54` | b.ne 0x00b501bc | `CONDITIONAL_JUMP`
<a id="insn-00b501d4"></a> `00b501d4` | `bf 01 0b eb` | cmp x13,x11 | `FALL_THROUGH`
<a id="insn-00b501d8"></a> `00b501d8` | `a0 00 00 54` | b.eq 0x00b501ec | `CONDITIONAL_JUMP`
<a id="insn-00b501dc"></a> `00b501dc` | `0b 15 40 38` | ldrb w11,[x8], #0x1 | `FALL_THROUGH`
<a id="insn-00b501e0"></a> `00b501e0` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00b501e4"></a> `00b501e4` | `4b 15 00 38` | strb w11,[x10], #0x1 | `FALL_THROUGH`
<a id="insn-00b501e8"></a> `00b501e8` | `a1 ff ff 54` | b.ne 0x00b501dc | `CONDITIONAL_JUMP`
<a id="insn-00b501ec"></a> `00b501ec` | `ec 03 0a aa` | mov x12,x10 | `FALL_THROUGH`
<a id="insn-00b501f0"></a> `00b501f0` | `6c 06 00 f9` | str x12,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00b501f4"></a> `00b501f4` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b501f8"></a> `00b501f8` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b501fc"></a> `00b501fc` | `f6 57 c3 a8` | ldp x22,x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00b50200"></a> `00b50200` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00b50204"></a> `00b50204` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b50208"></a> `00b50208` | `16 37 02 94` | bl 0x00bdde60 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b4ffac`](#insn-00b4ffac) 範囲 `[['00b4ffac', '00b4ffe3']]`
  - `CONDITIONAL_JUMP` [`00b4ffe0`](#insn-00b4ffe0) → [`00b50020`](#insn-00b50020)
  - `FALL_THROUGH` [`00b4ffe0`](#insn-00b4ffe0) → [`00b4ffe4`](#insn-00b4ffe4)
- ブロック [`00b4ffe4`](#insn-00b4ffe4) 範囲 `[['00b4ffe4', '00b4ffeb']]`
  - `CONDITIONAL_JUMP` [`00b4ffe8`](#insn-00b4ffe8) → [`00b50000`](#insn-00b50000)
  - `FALL_THROUGH` [`00b4ffe8`](#insn-00b4ffe8) → [`00b4ffec`](#insn-00b4ffec)
- ブロック [`00b4ffec`](#insn-00b4ffec) 範囲 `[['00b4ffec', '00b4fffb']]`
  - `FALL_THROUGH` [`00b4fff8`](#insn-00b4fff8) → [`00b4fffc`](#insn-00b4fffc)
- ブロック [`00b4fffc`](#insn-00b4fffc) 範囲 `[['00b4fffc', '00b4ffff']]`
  - `FALL_THROUGH` [`00b4fffc`](#insn-00b4fffc) → [`00b50000`](#insn-00b50000)
- ブロック [`00b50000`](#insn-00b50000) 範囲 `[['00b50000', '00b50003']]`
  - `CONDITIONAL_JUMP` [`00b50000`](#insn-00b50000) → [`00b50204`](#insn-00b50204)
  - `FALL_THROUGH` [`00b50000`](#insn-00b50000) → [`00b50004`](#insn-00b50004)
- ブロック [`00b50004`](#insn-00b50004) 範囲 `[['00b50004', '00b5000f']]`
  - `CONDITIONAL_JUMP` [`00b5000c`](#insn-00b5000c) → [`00b5004c`](#insn-00b5004c)
  - `FALL_THROUGH` [`00b5000c`](#insn-00b5000c) → [`00b50010`](#insn-00b50010)
- ブロック [`00b50010`](#insn-00b50010) 範囲 `[['00b50010', '00b5001f']]`
  - `UNCONDITIONAL_JUMP` [`00b5001c`](#insn-00b5001c) → [`00b50050`](#insn-00b50050)
- ブロック [`00b50020`](#insn-00b50020) 範囲 `[['00b50020', '00b5003b']]`
  - `CONDITIONAL_JUMP` [`00b50038`](#insn-00b50038) → [`00b50158`](#insn-00b50158)
  - `FALL_THROUGH` [`00b50038`](#insn-00b50038) → [`00b5003c`](#insn-00b5003c)
- ブロック [`00b5003c`](#insn-00b5003c) 範囲 `[['00b5003c', '00b50043']]`
  - `CONDITIONAL_JUMP` [`00b50040`](#insn-00b50040) → [`00b500f0`](#insn-00b500f0)
  - `FALL_THROUGH` [`00b50040`](#insn-00b50040) → [`00b50044`](#insn-00b50044)
- ブロック [`00b50044`](#insn-00b50044) 範囲 `[['00b50044', '00b5004b']]`
  - `UNCONDITIONAL_JUMP` [`00b50048`](#insn-00b50048) → [`00b50148`](#insn-00b50148)
- ブロック [`00b5004c`](#insn-00b5004c) 範囲 `[['00b5004c', '00b5004f']]`
  - `FALL_THROUGH` [`00b5004c`](#insn-00b5004c) → [`00b50050`](#insn-00b50050)
- ブロック [`00b50050`](#insn-00b50050) 範囲 `[['00b50050', '00b5006f']]`
  - `FALL_THROUGH` [`00b5006c`](#insn-00b5006c) → [`00b50070`](#insn-00b50070)
- ブロック [`00b50070`](#insn-00b50070) 範囲 `[['00b50070', '00b50073']]`
  - `CONDITIONAL_JUMP` [`00b50070`](#insn-00b50070) → [`00b500e4`](#insn-00b500e4)
  - `FALL_THROUGH` [`00b50070`](#insn-00b50070) → [`00b50074`](#insn-00b50074)
- ブロック [`00b50074`](#insn-00b50074) 範囲 `[['00b50074', '00b5007b']]`
  - `CONDITIONAL_JUMP` [`00b50078`](#insn-00b50078) → [`00b500cc`](#insn-00b500cc)
  - `FALL_THROUGH` [`00b50078`](#insn-00b50078) → [`00b5007c`](#insn-00b5007c)
- ブロック [`00b5007c`](#insn-00b5007c) 範囲 `[['00b5007c', '00b50083']]`
  - `CONDITIONAL_JUMP` [`00b50080`](#insn-00b50080) → [`00b50090`](#insn-00b50090)
  - `FALL_THROUGH` [`00b50080`](#insn-00b50080) → [`00b50084`](#insn-00b50084)
- ブロック [`00b50084`](#insn-00b50084) 範囲 `[['00b50084', '00b5008f']]`
  - `CONDITIONAL_JUMP` [`00b5008c`](#insn-00b5008c) → [`00b500cc`](#insn-00b500cc)
  - `FALL_THROUGH` [`00b5008c`](#insn-00b5008c) → [`00b50090`](#insn-00b50090)
- ブロック [`00b50090`](#insn-00b50090) 範囲 `[['00b50090', '00b500a7']]`
  - `FALL_THROUGH` [`00b500a4`](#insn-00b500a4) → [`00b500a8`](#insn-00b500a8)
- ブロック [`00b500a8`](#insn-00b500a8) 範囲 `[['00b500a8', '00b500bf']]`
  - `CONDITIONAL_JUMP` [`00b500bc`](#insn-00b500bc) → [`00b500a8`](#insn-00b500a8)
  - `FALL_THROUGH` [`00b500bc`](#insn-00b500bc) → [`00b500c0`](#insn-00b500c0)
- ブロック [`00b500c0`](#insn-00b500c0) 範囲 `[['00b500c0', '00b500cb']]`
  - `CONDITIONAL_JUMP` [`00b500c8`](#insn-00b500c8) → [`00b500e8`](#insn-00b500e8)
  - `FALL_THROUGH` [`00b500c8`](#insn-00b500c8) → [`00b500cc`](#insn-00b500cc)
- ブロック [`00b500cc`](#insn-00b500cc) 範囲 `[['00b500cc', '00b500cf']]`
  - `FALL_THROUGH` [`00b500cc`](#insn-00b500cc) → [`00b500d0`](#insn-00b500d0)
- ブロック [`00b500d0`](#insn-00b500d0) 範囲 `[['00b500d0', '00b500df']]`
  - `CONDITIONAL_JUMP` [`00b500dc`](#insn-00b500dc) → [`00b500d0`](#insn-00b500d0)
  - `FALL_THROUGH` [`00b500dc`](#insn-00b500dc) → [`00b500e0`](#insn-00b500e0)
- ブロック [`00b500e0`](#insn-00b500e0) 範囲 `[['00b500e0', '00b500e3']]`
  - `UNCONDITIONAL_JUMP` [`00b500e0`](#insn-00b500e0) → [`00b500e8`](#insn-00b500e8)
- ブロック [`00b500e4`](#insn-00b500e4) 範囲 `[['00b500e4', '00b500e7']]`
  - `FALL_THROUGH` [`00b500e4`](#insn-00b500e4) → [`00b500e8`](#insn-00b500e8)
- ブロック [`00b500e8`](#insn-00b500e8) 範囲 `[['00b500e8', '00b500ef']]`
  - `UNCONDITIONAL_JUMP` [`00b500ec`](#insn-00b500ec) → [`00b501f4`](#insn-00b501f4)
- ブロック [`00b500f0`](#insn-00b500f0) 範囲 `[['00b500f0', '00b500f7']]`
  - `CONDITIONAL_JUMP` [`00b500f4`](#insn-00b500f4) → [`00b50110`](#insn-00b50110)
  - `FALL_THROUGH` [`00b500f4`](#insn-00b500f4) → [`00b500f8`](#insn-00b500f8)
- ブロック [`00b500f8`](#insn-00b500f8) 範囲 `[['00b500f8', '00b50107']]`
  - `CONDITIONAL_JUMP` [`00b50104`](#insn-00b50104) → [`00b50110`](#insn-00b50110)
  - `FALL_THROUGH` [`00b50104`](#insn-00b50104) → [`00b50108`](#insn-00b50108)
- ブロック [`00b50108`](#insn-00b50108) 範囲 `[['00b50108', '00b5010f']]`
  - `UNCONDITIONAL_JUMP` [`00b5010c`](#insn-00b5010c) → [`00b50148`](#insn-00b50148)
- ブロック [`00b50110`](#insn-00b50110) 範囲 `[['00b50110', '00b50127']]`
  - `FALL_THROUGH` [`00b50124`](#insn-00b50124) → [`00b50128`](#insn-00b50128)
- ブロック [`00b50128`](#insn-00b50128) 範囲 `[['00b50128', '00b5013f']]`
  - `CONDITIONAL_JUMP` [`00b5013c`](#insn-00b5013c) → [`00b50128`](#insn-00b50128)
  - `FALL_THROUGH` [`00b5013c`](#insn-00b5013c) → [`00b50140`](#insn-00b50140)
- ブロック [`00b50140`](#insn-00b50140) 範囲 `[['00b50140', '00b50147']]`
  - `CONDITIONAL_JUMP` [`00b50144`](#insn-00b50144) → [`00b50158`](#insn-00b50158)
  - `FALL_THROUGH` [`00b50144`](#insn-00b50144) → [`00b50148`](#insn-00b50148)
- ブロック [`00b50148`](#insn-00b50148) 範囲 `[['00b50148', '00b50157']]`
  - `CONDITIONAL_JUMP` [`00b50154`](#insn-00b50154) → [`00b50148`](#insn-00b50148)
  - `FALL_THROUGH` [`00b50154`](#insn-00b50154) → [`00b50158`](#insn-00b50158)
- ブロック [`00b50158`](#insn-00b50158) 範囲 `[['00b50158', '00b5015f']]`
  - `CONDITIONAL_JUMP` [`00b5015c`](#insn-00b5015c) → [`00b50180`](#insn-00b50180)
  - `FALL_THROUGH` [`00b5015c`](#insn-00b5015c) → [`00b50160`](#insn-00b50160)
- ブロック [`00b50160`](#insn-00b50160) 範囲 `[['00b50160', '00b5016f']]`
  - `CONDITIONAL_JUMP` [`00b5016c`](#insn-00b5016c) → [`00b501f0`](#insn-00b501f0)
  - `FALL_THROUGH` [`00b5016c`](#insn-00b5016c) → [`00b50170`](#insn-00b50170)
- ブロック [`00b50170`](#insn-00b50170) 範囲 `[['00b50170', '00b50177']]`
  - `CONDITIONAL_JUMP` [`00b50174`](#insn-00b50174) → [`00b50188`](#insn-00b50188)
  - `FALL_THROUGH` [`00b50174`](#insn-00b50174) → [`00b50178`](#insn-00b50178)
- ブロック [`00b50178`](#insn-00b50178) 範囲 `[['00b50178', '00b5017f']]`
  - `UNCONDITIONAL_JUMP` [`00b5017c`](#insn-00b5017c) → [`00b501dc`](#insn-00b501dc)
- ブロック [`00b50180`](#insn-00b50180) 範囲 `[['00b50180', '00b50187']]`
  - `UNCONDITIONAL_JUMP` [`00b50184`](#insn-00b50184) → [`00b501f4`](#insn-00b501f4)
- ブロック [`00b50188`](#insn-00b50188) 範囲 `[['00b50188', '00b5018f']]`
  - `CONDITIONAL_JUMP` [`00b5018c`](#insn-00b5018c) → [`00b501a4`](#insn-00b501a4)
  - `FALL_THROUGH` [`00b5018c`](#insn-00b5018c) → [`00b50190`](#insn-00b50190)
- ブロック [`00b50190`](#insn-00b50190) 範囲 `[['00b50190', '00b5019b']]`
  - `CONDITIONAL_JUMP` [`00b50198`](#insn-00b50198) → [`00b501a4`](#insn-00b501a4)
  - `FALL_THROUGH` [`00b50198`](#insn-00b50198) → [`00b5019c`](#insn-00b5019c)
- ブロック [`00b5019c`](#insn-00b5019c) 範囲 `[['00b5019c', '00b501a3']]`
  - `UNCONDITIONAL_JUMP` [`00b501a0`](#insn-00b501a0) → [`00b501dc`](#insn-00b501dc)
- ブロック [`00b501a4`](#insn-00b501a4) 範囲 `[['00b501a4', '00b501bb']]`
  - `FALL_THROUGH` [`00b501b8`](#insn-00b501b8) → [`00b501bc`](#insn-00b501bc)
- ブロック [`00b501bc`](#insn-00b501bc) 範囲 `[['00b501bc', '00b501d3']]`
  - `CONDITIONAL_JUMP` [`00b501d0`](#insn-00b501d0) → [`00b501bc`](#insn-00b501bc)
  - `FALL_THROUGH` [`00b501d0`](#insn-00b501d0) → [`00b501d4`](#insn-00b501d4)
- ブロック [`00b501d4`](#insn-00b501d4) 範囲 `[['00b501d4', '00b501db']]`
  - `CONDITIONAL_JUMP` [`00b501d8`](#insn-00b501d8) → [`00b501ec`](#insn-00b501ec)
  - `FALL_THROUGH` [`00b501d8`](#insn-00b501d8) → [`00b501dc`](#insn-00b501dc)
- ブロック [`00b501dc`](#insn-00b501dc) 範囲 `[['00b501dc', '00b501eb']]`
  - `CONDITIONAL_JUMP` [`00b501e8`](#insn-00b501e8) → [`00b501dc`](#insn-00b501dc)
  - `FALL_THROUGH` [`00b501e8`](#insn-00b501e8) → [`00b501ec`](#insn-00b501ec)
- ブロック [`00b501ec`](#insn-00b501ec) 範囲 `[['00b501ec', '00b501ef']]`
  - `FALL_THROUGH` [`00b501ec`](#insn-00b501ec) → [`00b501f0`](#insn-00b501f0)
- ブロック [`00b501f0`](#insn-00b501f0) 範囲 `[['00b501f0', '00b501f3']]`
  - `FALL_THROUGH` [`00b501f0`](#insn-00b501f0) → [`00b501f4`](#insn-00b501f4)
- ブロック [`00b501f4`](#insn-00b501f4) 範囲 `[['00b501f4', '00b50203']]`
- ブロック [`00b50204`](#insn-00b50204) 範囲 `[['00b50204', '00b5020b']]`

## 命令位置別の参照

- [`00b4ffac`](#insn-00b4ffac) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4ffb0`](#insn-00b4ffb0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4ffb4`](#insn-00b4ffb4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4ffe0`](#insn-00b4ffe0) → [`00b50020`](#insn-00b50020) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4ffe8`](#insn-00b4ffe8) → [`00b50000`](#insn-00b50000) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4fff0`](#insn-00b4fff0) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00b50000`](#insn-00b50000) → [`00b50204`](#insn-00b50204) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5000c`](#insn-00b5000c) → [`00b5004c`](#insn-00b5004c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5001c`](#insn-00b5001c) → [`00b50050`](#insn-00b50050) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b50038`](#insn-00b50038) → [`00b50158`](#insn-00b50158) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b50040`](#insn-00b50040) → [`00b500f0`](#insn-00b500f0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b50048`](#insn-00b50048) → [`00b50148`](#insn-00b50148) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b50054`](#insn-00b50054) → [`00bdaff0`](../00bda/00bdaff0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaff0` · 推定シンボル `None` · 推定型 `None`
- [`00b50070`](#insn-00b50070) → [`00b500e4`](#insn-00b500e4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b50078`](#insn-00b50078) → [`00b500cc`](#insn-00b500cc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b50080`](#insn-00b50080) → [`00b50090`](#insn-00b50090) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5008c`](#insn-00b5008c) → [`00b500cc`](#insn-00b500cc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b500bc`](#insn-00b500bc) → [`00b500a8`](#insn-00b500a8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b500c8`](#insn-00b500c8) → [`00b500e8`](#insn-00b500e8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b500dc`](#insn-00b500dc) → [`00b500d0`](#insn-00b500d0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b500e0`](#insn-00b500e0) → [`00b500e8`](#insn-00b500e8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b500ec`](#insn-00b500ec) → [`00b501f4`](#insn-00b501f4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b500f4`](#insn-00b500f4) → [`00b50110`](#insn-00b50110) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b50104`](#insn-00b50104) → [`00b50110`](#insn-00b50110) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5010c`](#insn-00b5010c) → [`00b50148`](#insn-00b50148) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5013c`](#insn-00b5013c) → [`00b50128`](#insn-00b50128) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b50144`](#insn-00b50144) → [`00b50158`](#insn-00b50158) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b50154`](#insn-00b50154) → [`00b50148`](#insn-00b50148) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5015c`](#insn-00b5015c) → [`00b50180`](#insn-00b50180) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5016c`](#insn-00b5016c) → [`00b501f0`](#insn-00b501f0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b50174`](#insn-00b50174) → [`00b50188`](#insn-00b50188) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5017c`](#insn-00b5017c) → [`00b501dc`](#insn-00b501dc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b50184`](#insn-00b50184) → [`00b501f4`](#insn-00b501f4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5018c`](#insn-00b5018c) → [`00b501a4`](#insn-00b501a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b50198`](#insn-00b50198) → [`00b501a4`](#insn-00b501a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b501a0`](#insn-00b501a0) → [`00b501dc`](#insn-00b501dc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b501d0`](#insn-00b501d0) → [`00b501bc`](#insn-00b501bc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b501d8`](#insn-00b501d8) → [`00b501ec`](#insn-00b501ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b501e8`](#insn-00b501e8) → [`00b501dc`](#insn-00b501dc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b501f4`](#insn-00b501f4) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b501f8`](#insn-00b501f8) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b50208`](#insn-00b50208) → [`00bdde60`](../00bdd/00bdde60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdde60` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b4ffac`](#insn-00b4ffac)

~~~json
{
  "source": "00b4ffac",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4ffb0`](#insn-00b4ffb0)

~~~json
{
  "source": "00b4ffb0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4ffb4`](#insn-00b4ffb4)

~~~json
{
  "source": "00b4ffb4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4ffe0`](#insn-00b4ffe0)

~~~json
{
  "source": "00b4ffe0",
  "target": "00b50020",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4ffe8`](#insn-00b4ffe8)

~~~json
{
  "source": "00b4ffe8",
  "target": "00b50000",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4fff0`](#insn-00b4fff0)

~~~json
{
  "source": "00b4fff0",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b50000`](#insn-00b50000)

~~~json
{
  "source": "00b50000",
  "target": "00b50204",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5000c`](#insn-00b5000c)

~~~json
{
  "source": "00b5000c",
  "target": "00b5004c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5001c`](#insn-00b5001c)

~~~json
{
  "source": "00b5001c",
  "target": "00b50050",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b50038`](#insn-00b50038)

~~~json
{
  "source": "00b50038",
  "target": "00b50158",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b50040`](#insn-00b50040)

~~~json
{
  "source": "00b50040",
  "target": "00b500f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b50048`](#insn-00b50048)

~~~json
{
  "source": "00b50048",
  "target": "00b50148",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b50054`](#insn-00b50054)

~~~json
{
  "source": "00b50054",
  "target": "00bdaff0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b50070`](#insn-00b50070)

~~~json
{
  "source": "00b50070",
  "target": "00b500e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b50078`](#insn-00b50078)

~~~json
{
  "source": "00b50078",
  "target": "00b500cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b50080`](#insn-00b50080)

~~~json
{
  "source": "00b50080",
  "target": "00b50090",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5008c`](#insn-00b5008c)

~~~json
{
  "source": "00b5008c",
  "target": "00b500cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b500bc`](#insn-00b500bc)

~~~json
{
  "source": "00b500bc",
  "target": "00b500a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b500c8`](#insn-00b500c8)

~~~json
{
  "source": "00b500c8",
  "target": "00b500e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b500dc`](#insn-00b500dc)

~~~json
{
  "source": "00b500dc",
  "target": "00b500d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b500e0`](#insn-00b500e0)

~~~json
{
  "source": "00b500e0",
  "target": "00b500e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b500ec`](#insn-00b500ec)

~~~json
{
  "source": "00b500ec",
  "target": "00b501f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b500f4`](#insn-00b500f4)

~~~json
{
  "source": "00b500f4",
  "target": "00b50110",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b50104`](#insn-00b50104)

~~~json
{
  "source": "00b50104",
  "target": "00b50110",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5010c`](#insn-00b5010c)

~~~json
{
  "source": "00b5010c",
  "target": "00b50148",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5013c`](#insn-00b5013c)

~~~json
{
  "source": "00b5013c",
  "target": "00b50128",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b50144`](#insn-00b50144)

~~~json
{
  "source": "00b50144",
  "target": "00b50158",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b50154`](#insn-00b50154)

~~~json
{
  "source": "00b50154",
  "target": "00b50148",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5015c`](#insn-00b5015c)

~~~json
{
  "source": "00b5015c",
  "target": "00b50180",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5016c`](#insn-00b5016c)

~~~json
{
  "source": "00b5016c",
  "target": "00b501f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b50174`](#insn-00b50174)

~~~json
{
  "source": "00b50174",
  "target": "00b50188",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5017c`](#insn-00b5017c)

~~~json
{
  "source": "00b5017c",
  "target": "00b501dc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b50184`](#insn-00b50184)

~~~json
{
  "source": "00b50184",
  "target": "00b501f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5018c`](#insn-00b5018c)

~~~json
{
  "source": "00b5018c",
  "target": "00b501a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b50198`](#insn-00b50198)

~~~json
{
  "source": "00b50198",
  "target": "00b501a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b501a0`](#insn-00b501a0)

~~~json
{
  "source": "00b501a0",
  "target": "00b501dc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b501d0`](#insn-00b501d0)

~~~json
{
  "source": "00b501d0",
  "target": "00b501bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b501d8`](#insn-00b501d8)

~~~json
{
  "source": "00b501d8",
  "target": "00b501ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b501e8`](#insn-00b501e8)

~~~json
{
  "source": "00b501e8",
  "target": "00b501dc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b501f4`](#insn-00b501f4)

~~~json
{
  "source": "00b501f4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b501f8`](#insn-00b501f8)

~~~json
{
  "source": "00b501f8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b50208`](#insn-00b50208)

~~~json
{
  "source": "00b50208",
  "target": "00bdde60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
