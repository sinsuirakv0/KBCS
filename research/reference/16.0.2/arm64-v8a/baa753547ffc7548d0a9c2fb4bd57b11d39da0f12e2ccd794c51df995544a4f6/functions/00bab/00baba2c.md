# 00baba2c

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bab990`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bab/00bab990.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0078.md#compare-298de6d9fc5d947d7b306f17ea94b39a)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00baca20`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bac/00baca20.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0035.md#compare-d6f83a3c45a23a37b56e41c16499eff9)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00baba2c",
  "name": "_ZNSt6__ndk16vectorIN11flatbuffers5ValueENS_9allocatorIS2_EEE24__emplace_back_slow_pathIJS2_EEEvDpOT_",
  "size": 356,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "74c3d64390d5455b679c0584ebf86e8f588ca4a27e41da279ddff858aba98401",
  "source_text_sha256": "74c3d64390d5455b679c0584ebf86e8f588ca4a27e41da279ddff858aba98401",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00baba2c",
        "00babb8f"
      ]
    ],
    "bytes_sha256": "31a46204419d7800b7009e630eabe42ede9125528f8ce2938a7792a00c1ad792",
    "instruction_count": 89,
    "instruction_bytes": 356,
    "body_bytes": 356,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5d0d0](../00c5d/00c5d0d0.md)

## 呼び出し先

- [00c57f60](../00c57/00c57f60.md)
- [00c57f80](../00c57/00c57f80.md)
- [00c5b210](../00c5b/00c5b210.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 5818 bytes

~~~c

void _ZNSt6__ndk16vectorIN11flatbuffers5ValueENS_9allocatorIS2_EEE24__emplace_back_slow_pathIJS2_EEEvDpOT_
               (long *param_1,undefined8 *param_2)

{
  undefined8 *puVar1;
  void *pvVar2;
  undefined8 *puVar3;
  long lVar4;
  ulong uVar5;
  void *pvVar6;
  long lVar7;
  void *__ptr;
  long lVar8;
  ulong uVar9;
  undefined8 uVar10;
  undefined8 uVar11;
  undefined8 uVar12;
  
                    /* catch() { ... } // from try @ 00bab4e0 with catch @ 00baba30 */
                    /* catch() { ... } // from try @ 00bab4b4 with catch @ 00baba40 */
                    /* catch() { ... } // from try @ 00bab490 with catch @ 00baba44 */
  lVar8 = param_1[1] - *param_1 >> 6;
  uVar9 = lVar8 + 1;
  if (uVar9 >> 0x3a != 0) {
LAB_00baba88:
                    /* WARNING: Subroutine does not return */
    abort();
  }
                    /* catch() { ... } // from try @ 00bab7fc with catch @ 00baba54 */
                    /* catch() { ... } // from try @ 00bab7d8 with catch @ 00baba58 */
  lVar4 = param_1[2] - *param_1;
                    /* catch() { ... } // from try @ 00bab7ac with catch @ 00baba68 */
                    /* catch() { ... } // from try @ 00bab464 with catch @ 00baba6c */
  if ((ulong)(lVar4 >> 6) < 0x1ffffffffffffff) {
                    /* catch() { ... } // from try @ 00bab440 with catch @ 00baba70 */
    uVar5 = lVar4 >> 5;
    if (uVar9 <= uVar5) {
      uVar9 = uVar5;
    }
    if (uVar9 == 0) {
      lVar4 = 0;
      goto LAB_00baba98;
    }
                    /* catch() { ... } // from try @ 00bab414 with catch @ 00baba80 */
                    /* catch() { ... } // from try @ 00bab78c with catch @ 00baba84 */
    if (uVar9 >> 0x3a != 0) goto LAB_00baba88;
  }
  else {
    uVar9 = 0x3ffffffffffffff;
  }
                    /* catch() { ... } // from try @ 00bab760 with catch @ 00baba94 */
  lVar4 = _Znwm(uVar9 << 6);
LAB_00baba98:
                    /* catch() { ... } // from try @ 00bab73c with catch @ 00baba98 */
  uVar10 = *param_2;
  uVar12 = param_2[3];
  uVar11 = param_2[2];
  puVar3 = (undefined8 *)(lVar4 + lVar8 * 0x40);
  puVar1 = puVar3 + 8;
  puVar3[1] = param_2[1];
  *puVar3 = uVar10;
  puVar3[3] = uVar12;
  puVar3[2] = uVar11;
                    /* catch() { ... } // from try @ 00bab3f4 with catch @ 00babaa8 */
  uVar11 = param_2[5];
  uVar10 = param_2[4];
  puVar3[6] = param_2[6];
  puVar3[5] = uVar11;
  puVar3[4] = uVar10;
                    /* catch() { ... } // from try @ 00bab3c8 with catch @ 00babab8 */
                    /* catch() { ... } // from try @ 00bab3a4 with catch @ 00bababc */
  param_2[5] = 0;
  param_2[6] = 0;
  param_2[4] = 0;
  *(undefined2 *)(puVar3 + 7) = *(undefined2 *)(param_2 + 7);
  pvVar6 = (void *)*param_1;
  pvVar2 = (void *)param_1[1];
                    /* catch() { ... } // from try @ 00bab710 with catch @ 00babacc */
                    /* catch() { ... } // from try @ 00bab6f0 with catch @ 00babad0 */
  __ptr = pvVar6;
  if (pvVar2 != pvVar6) {
    lVar8 = 0;
    do {
                    /* catch() { ... } // from try @ 00bab378 with catch @ 00babae0 */
                    /* catch() { ... } // from try @ 00bab358 with catch @ 00babae4 */
      uVar10 = *(undefined8 *)((long)pvVar2 + lVar8 + -0x40);
      uVar12 = *(undefined8 *)((long)pvVar2 + lVar8 + -0x28);
      uVar11 = *(undefined8 *)((long)pvVar2 + lVar8 + -0x30);
      lVar7 = lVar8 + -0x40;
                    /* catch() { ... } // from try @ 00bab6d0 with catch @ 00babaf4 */
      *(undefined8 *)((long)puVar3 + lVar8 + -0x38) = *(undefined8 *)((long)pvVar2 + lVar8 + -0x38);
      *(undefined8 *)((long)puVar3 + lVar8 + -0x40) = uVar10;
      *(undefined8 *)((long)puVar3 + lVar8 + -0x28) = uVar12;
      *(undefined8 *)((long)puVar3 + lVar8 + -0x30) = uVar11;
      uVar11 = *(undefined8 *)((long)pvVar2 + lVar8 + -0x18);
      uVar10 = *(undefined8 *)((long)pvVar2 + lVar8 + -0x20);
      *(undefined8 *)((long)puVar3 + lVar8 + -0x10) = *(undefined8 *)((long)pvVar2 + lVar8 + -0x10);
      *(undefined8 *)((long)puVar3 + lVar8 + -0x18) = uVar11;
      *(undefined8 *)((long)puVar3 + lVar8 + -0x20) = uVar10;
      *(undefined8 *)((long)pvVar2 + lVar8 + -0x18) = 0;
      *(undefined8 *)((long)pvVar2 + lVar8 + -0x10) = 0;
      *(undefined8 *)((long)pvVar2 + lVar8 + -0x20) = 0;
                    /* catch() { ... } // from try @ 00bab6bc with catch @ 00babb14 */
      *(undefined2 *)((long)puVar3 + lVar8 + -8) = *(undefined2 *)((long)pvVar2 + lVar8 + -8);
      lVar8 = lVar7;
                    /* catch() { ... } // from try @ 00bab698 with catch @ 00babb18 */
    } while ((long)pvVar6 - (long)pvVar2 != lVar7);
                    /* catch() { ... } // from try @ 00bab338 with catch @ 00babb1c */
    pvVar6 = (void *)param_1[1];
    puVar3 = (undefined8 *)((long)puVar3 + lVar7);
    __ptr = (void *)*param_1;
  }
  *param_1 = (long)puVar3;
  param_1[1] = (long)puVar1;
  param_1[2] = lVar4 + uVar9 * 0x40;
  while (pvVar2 = pvVar6, pvVar2 != __ptr) {
    pvVar6 = (void *)((long)pvVar2 + -0x40);
    if ((*(byte *)((long)pvVar2 + -0x20) & 1) != 0) {
                    /* catch() { ... } // from try @ 00bab1b4 with catch @ 00babb6c */
                    /* catch() { ... } // from try @ 00bab194 with catch @ 00babb70 */
      _ZdlPv(*(void **)((long)pvVar2 + -0x10));
    }
  }
                    /* catch() { ... } // from try @ 00bab324 with catch @ 00babb3c */
  if (__ptr != (void *)0x0) {
                    /* catch() { ... } // from try @ 00bab300 with catch @ 00babb40 */
                    /* catch() { ... } // from try @ 00baabf8 with catch @ 00babb50 */
    _ZdlPv(__ptr);
    return;
  }
                    /* catch() { ... } // from try @ 00baaea8 with catch @ 00babb80 */
                    /* catch() { ... } // from try @ 00baae8c with catch @ 00babb84 */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00baba2c"></a> `00baba2c` | `f6 57 bd a9` | stp x22,x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00baba30"></a> `00baba30` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00baba34"></a> `00baba34` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00baba38"></a> `00baba38` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00baba3c"></a> `00baba3c` | `09 20 40 a9` | ldp x9,x8,[x0] | `FALL_THROUGH`
<a id="insn-00baba40"></a> `00baba40` | `08 01 09 cb` | sub x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00baba44"></a> `00baba44` | `15 fd 46 93` | asr x21,x8,#0x6 | `FALL_THROUGH`
<a id="insn-00baba48"></a> `00baba48` | `a8 06 00 91` | add x8,x21,#0x1 | `FALL_THROUGH`
<a id="insn-00baba4c"></a> `00baba4c` | `0a fd 7a d3` | lsr x10,x8,#0x3a | `FALL_THROUGH`
<a id="insn-00baba50"></a> `00baba50` | `ca 01 00 b5` | cbnz x10,0x00baba88 | `CONDITIONAL_JUMP`
<a id="insn-00baba54"></a> `00baba54` | `0a 08 40 f9` | ldr x10,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00baba58"></a> `00baba58` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00baba5c"></a> `00baba5c` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00baba60"></a> `00baba60` | `49 01 09 cb` | sub x9,x10,x9 | `FALL_THROUGH`
<a id="insn-00baba64"></a> `00baba64` | `ea df 7f b2` | orr x10,xzr,#0x1fffffffffffffe | `FALL_THROUGH`
<a id="insn-00baba68"></a> `00baba68` | `5f 19 89 eb` | cmp x10,x9, ASR #0x6 | `FALL_THROUGH`
<a id="insn-00baba6c"></a> `00baba6c` | `03 01 00 54` | b.cc 0x00baba8c | `CONDITIONAL_JUMP`
<a id="insn-00baba70"></a> `00baba70` | `29 fd 45 93` | asr x9,x9,#0x5 | `FALL_THROUGH`
<a id="insn-00baba74"></a> `00baba74` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00baba78"></a> `00baba78` | `16 31 89 9a` | csel x22,x8,x9,cc | `FALL_THROUGH`
<a id="insn-00baba7c"></a> `00baba7c` | `76 08 00 b4` | cbz x22,0x00babb88 | `CONDITIONAL_JUMP`
<a id="insn-00baba80"></a> `00baba80` | `c8 fe 7a d3` | lsr x8,x22,#0x3a | `FALL_THROUGH`
<a id="insn-00baba84"></a> `00baba84` | `68 00 00 b4` | cbz x8,0x00baba90 | `CONDITIONAL_JUMP`
<a id="insn-00baba88"></a> `00baba88` | `e2 bd 02 94` | bl 0x00c5b210 | `CALL_TERMINATOR`
<a id="insn-00baba8c"></a> `00baba8c` | `16 80 ff 92` | mov x22,#0x3ffffffffffffff | `FALL_THROUGH`
<a id="insn-00baba90"></a> `00baba90` | `c0 e6 7a d3` | lsl x0,x22,#0x6 | `FALL_THROUGH`
<a id="insn-00baba94"></a> `00baba94` | `33 b1 02 94` | bl 0x00c57f60 | `UNCONDITIONAL_CALL`
<a id="insn-00baba98"></a> `00baba98` | `80 06 40 ad` | ldp q0,q1,[x20] | `FALL_THROUGH`
<a id="insn-00baba9c"></a> `00baba9c` | `08 18 15 8b` | add x8,x0,x21, LSL #0x6 | `FALL_THROUGH`
<a id="insn-00babaa0"></a> `00babaa0` | `0a 01 01 91` | add x10,x8,#0x40 | `FALL_THROUGH`
<a id="insn-00babaa4"></a> `00babaa4` | `00 05 00 ad` | stp q0,q1,[x8] | `FALL_THROUGH`
<a id="insn-00babaa8"></a> `00babaa8` | `89 1a 40 f9` | ldr x9,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-00babaac"></a> `00babaac` | `80 0a c0 3d` | ldr q0,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-00babab0"></a> `00babab0` | `09 19 00 f9` | str x9,[x8, #0x30] | `FALL_THROUGH`
<a id="insn-00babab4"></a> `00babab4` | `00 09 80 3d` | str q0,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00babab8"></a> `00babab8` | `89 72 40 79` | ldrh w9,[x20, #0x38] | `FALL_THROUGH`
<a id="insn-00bababc"></a> `00bababc` | `9f fe 02 a9` | stp xzr,xzr,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00babac0"></a> `00babac0` | `9f 12 00 f9` | str xzr,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-00babac4"></a> `00babac4` | `09 71 00 79` | strh w9,[x8, #0x38] | `FALL_THROUGH`
<a id="insn-00babac8"></a> `00babac8` | `6b 36 40 a9` | ldp x11,x13,[x19] | `FALL_THROUGH`
<a id="insn-00babacc"></a> `00babacc` | `09 18 16 8b` | add x9,x0,x22, LSL #0x6 | `FALL_THROUGH`
<a id="insn-00babad0"></a> `00babad0` | `bf 01 0b eb` | cmp x13,x11 | `FALL_THROUGH`
<a id="insn-00babad4"></a> `00babad4` | `a0 02 00 54` | b.eq 0x00babb28 | `CONDITIONAL_JUMP`
<a id="insn-00babad8"></a> `00babad8` | `ec 03 1f aa` | mov x12,xzr | `FALL_THROUGH`
<a id="insn-00babadc"></a> `00babadc` | `6b 01 0d cb` | sub x11,x11,x13 | `FALL_THROUGH`
<a id="insn-00babae0"></a> `00babae0` | `ae 01 0c 8b` | add x14,x13,x12 | `FALL_THROUGH`
<a id="insn-00babae4"></a> `00babae4` | `c0 05 7e ad` | ldp q0,q1,[x14, #-0x40] | `FALL_THROUGH`
<a id="insn-00babae8"></a> `00babae8` | `0f 01 0c 8b` | add x15,x8,x12 | `FALL_THROUGH`
<a id="insn-00babaec"></a> `00babaec` | `8c 01 01 d1` | sub x12,x12,#0x40 | `FALL_THROUGH`
<a id="insn-00babaf0"></a> `00babaf0` | `7f 01 0c eb` | cmp x11,x12 | `FALL_THROUGH`
<a id="insn-00babaf4"></a> `00babaf4` | `e0 05 3e ad` | stp q0,q1,[x15, #-0x40] | `FALL_THROUGH`
<a id="insn-00babaf8"></a> `00babaf8` | `d0 01 5f f8` | ldur x16,[x14, #-0x10] | `FALL_THROUGH`
<a id="insn-00babafc"></a> `00babafc` | `c0 01 de 3c` | ldur q0,[x14, #-0x20] | `FALL_THROUGH`
<a id="insn-00babb00"></a> `00babb00` | `f0 01 1f f8` | stur x16,[x15, #-0x10] | `FALL_THROUGH`
<a id="insn-00babb04"></a> `00babb04` | `e0 01 9e 3c` | stur q0,[x15, #-0x20] | `FALL_THROUGH`
<a id="insn-00babb08"></a> `00babb08` | `d0 81 5f 78` | ldurh w16,[x14, #-0x8] | `FALL_THROUGH`
<a id="insn-00babb0c"></a> `00babb0c` | `df fd 3e a9` | stp xzr,xzr,[x14, #-0x18] | `FALL_THROUGH`
<a id="insn-00babb10"></a> `00babb10` | `df 01 1e f8` | stur xzr,[x14, #-0x20] | `FALL_THROUGH`
<a id="insn-00babb14"></a> `00babb14` | `f0 81 1f 78` | sturh w16,[x15, #-0x8] | `FALL_THROUGH`
<a id="insn-00babb18"></a> `00babb18` | `41 fe ff 54` | b.ne 0x00babae0 | `CONDITIONAL_JUMP`
<a id="insn-00babb1c"></a> `00babb1c` | `74 2e 40 a9` | ldp x20,x11,[x19] | `FALL_THROUGH`
<a id="insn-00babb20"></a> `00babb20` | `08 01 0c 8b` | add x8,x8,x12 | `FALL_THROUGH`
<a id="insn-00babb24"></a> `00babb24` | `02 00 00 14` | b 0x00babb2c | `UNCONDITIONAL_JUMP`
<a id="insn-00babb28"></a> `00babb28` | `f4 03 0b aa` | mov x20,x11 | `FALL_THROUGH`
<a id="insn-00babb2c"></a> `00babb2c` | `7f 01 14 eb` | cmp x11,x20 | `FALL_THROUGH`
<a id="insn-00babb30"></a> `00babb30` | `68 2a 00 a9` | stp x8,x10,[x19] | `FALL_THROUGH`
<a id="insn-00babb34"></a> `00babb34` | `69 0a 00 f9` | str x9,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00babb38"></a> `00babb38` | `41 01 00 54` | b.ne 0x00babb60 | `CONDITIONAL_JUMP`
<a id="insn-00babb3c"></a> `00babb3c` | `f4 01 00 b4` | cbz x20,0x00babb78 | `CONDITIONAL_JUMP`
<a id="insn-00babb40"></a> `00babb40` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00babb44"></a> `00babb44` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00babb48"></a> `00babb48` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00babb4c"></a> `00babb4c` | `f6 57 c3 a8` | ldp x22,x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00babb50"></a> `00babb50` | `0c b1 02 14` | b 0x00c57f80 | `CALL_TERMINATOR`
<a id="insn-00babb54"></a> `00babb54` | `9f 02 13 eb` | cmp x20,x19 | `FALL_THROUGH`
<a id="insn-00babb58"></a> `00babb58` | `eb 03 13 aa` | mov x11,x19 | `FALL_THROUGH`
<a id="insn-00babb5c"></a> `00babb5c` | `00 ff ff 54` | b.eq 0x00babb3c | `CONDITIONAL_JUMP`
<a id="insn-00babb60"></a> `00babb60` | `68 01 5e 38` | ldurb w8,[x11, #-0x20] | `FALL_THROUGH`
<a id="insn-00babb64"></a> `00babb64` | `73 01 01 d1` | sub x19,x11,#0x40 | `FALL_THROUGH`
<a id="insn-00babb68"></a> `00babb68` | `68 ff 07 36` | tbz w8,#0x0,0x00babb54 | `CONDITIONAL_JUMP`
<a id="insn-00babb6c"></a> `00babb6c` | `60 01 5f f8` | ldur x0,[x11, #-0x10] | `FALL_THROUGH`
<a id="insn-00babb70"></a> `00babb70` | `04 b1 02 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00babb74"></a> `00babb74` | `f8 ff ff 17` | b 0x00babb54 | `UNCONDITIONAL_JUMP`
<a id="insn-00babb78"></a> `00babb78` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00babb7c"></a> `00babb7c` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00babb80"></a> `00babb80` | `f6 57 c3 a8` | ldp x22,x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00babb84"></a> `00babb84` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00babb88"></a> `00babb88` | `e0 03 1f aa` | mov x0,xzr | `FALL_THROUGH`
<a id="insn-00babb8c"></a> `00babb8c` | `c3 ff ff 17` | b 0x00baba98 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00baba2c`](#insn-00baba2c) 範囲 `[['00baba2c', '00baba2f']]`
  - `FALL_THROUGH` [`00baba2c`](#insn-00baba2c) → [`00baba30`](#insn-00baba30)
- ブロック [`00baba30`](#insn-00baba30) 範囲 `[['00baba30', '00baba3f']]`
  - `FALL_THROUGH` [`00baba3c`](#insn-00baba3c) → [`00baba40`](#insn-00baba40)
- ブロック [`00baba40`](#insn-00baba40) 範囲 `[['00baba40', '00baba43']]`
  - `FALL_THROUGH` [`00baba40`](#insn-00baba40) → [`00baba44`](#insn-00baba44)
- ブロック [`00baba44`](#insn-00baba44) 範囲 `[['00baba44', '00baba53']]`
  - `CONDITIONAL_JUMP` [`00baba50`](#insn-00baba50) → [`00baba88`](#insn-00baba88)
  - `FALL_THROUGH` [`00baba50`](#insn-00baba50) → [`00baba54`](#insn-00baba54)
- ブロック [`00baba54`](#insn-00baba54) 範囲 `[['00baba54', '00baba57']]`
  - `FALL_THROUGH` [`00baba54`](#insn-00baba54) → [`00baba58`](#insn-00baba58)
- ブロック [`00baba58`](#insn-00baba58) 範囲 `[['00baba58', '00baba67']]`
  - `FALL_THROUGH` [`00baba64`](#insn-00baba64) → [`00baba68`](#insn-00baba68)
- ブロック [`00baba68`](#insn-00baba68) 範囲 `[['00baba68', '00baba6b']]`
  - `FALL_THROUGH` [`00baba68`](#insn-00baba68) → [`00baba6c`](#insn-00baba6c)
- ブロック [`00baba6c`](#insn-00baba6c) 範囲 `[['00baba6c', '00baba6f']]`
  - `CONDITIONAL_JUMP` [`00baba6c`](#insn-00baba6c) → [`00baba8c`](#insn-00baba8c)
  - `FALL_THROUGH` [`00baba6c`](#insn-00baba6c) → [`00baba70`](#insn-00baba70)
- ブロック [`00baba70`](#insn-00baba70) 範囲 `[['00baba70', '00baba7f']]`
  - `CONDITIONAL_JUMP` [`00baba7c`](#insn-00baba7c) → [`00babb88`](#insn-00babb88)
  - `FALL_THROUGH` [`00baba7c`](#insn-00baba7c) → [`00baba80`](#insn-00baba80)
- ブロック [`00baba80`](#insn-00baba80) 範囲 `[['00baba80', '00baba83']]`
  - `FALL_THROUGH` [`00baba80`](#insn-00baba80) → [`00baba84`](#insn-00baba84)
- ブロック [`00baba84`](#insn-00baba84) 範囲 `[['00baba84', '00baba87']]`
  - `CONDITIONAL_JUMP` [`00baba84`](#insn-00baba84) → [`00baba90`](#insn-00baba90)
  - `FALL_THROUGH` [`00baba84`](#insn-00baba84) → [`00baba88`](#insn-00baba88)
- ブロック [`00baba88`](#insn-00baba88) 範囲 `[['00baba88', '00baba8b']]`
- ブロック [`00baba8c`](#insn-00baba8c) 範囲 `[['00baba8c', '00baba8f']]`
  - `FALL_THROUGH` [`00baba8c`](#insn-00baba8c) → [`00baba90`](#insn-00baba90)
- ブロック [`00baba90`](#insn-00baba90) 範囲 `[['00baba90', '00baba93']]`
  - `FALL_THROUGH` [`00baba90`](#insn-00baba90) → [`00baba94`](#insn-00baba94)
- ブロック [`00baba94`](#insn-00baba94) 範囲 `[['00baba94', '00baba97']]`
  - `FALL_THROUGH` [`00baba94`](#insn-00baba94) → [`00baba98`](#insn-00baba98)
- ブロック [`00baba98`](#insn-00baba98) 範囲 `[['00baba98', '00babaa7']]`
  - `FALL_THROUGH` [`00babaa4`](#insn-00babaa4) → [`00babaa8`](#insn-00babaa8)
- ブロック [`00babaa8`](#insn-00babaa8) 範囲 `[['00babaa8', '00babab7']]`
  - `FALL_THROUGH` [`00babab4`](#insn-00babab4) → [`00babab8`](#insn-00babab8)
- ブロック [`00babab8`](#insn-00babab8) 範囲 `[['00babab8', '00bababb']]`
  - `FALL_THROUGH` [`00babab8`](#insn-00babab8) → [`00bababc`](#insn-00bababc)
- ブロック [`00bababc`](#insn-00bababc) 範囲 `[['00bababc', '00babacb']]`
  - `FALL_THROUGH` [`00babac8`](#insn-00babac8) → [`00babacc`](#insn-00babacc)
- ブロック [`00babacc`](#insn-00babacc) 範囲 `[['00babacc', '00babacf']]`
  - `FALL_THROUGH` [`00babacc`](#insn-00babacc) → [`00babad0`](#insn-00babad0)
- ブロック [`00babad0`](#insn-00babad0) 範囲 `[['00babad0', '00babad7']]`
  - `CONDITIONAL_JUMP` [`00babad4`](#insn-00babad4) → [`00babb28`](#insn-00babb28)
  - `FALL_THROUGH` [`00babad4`](#insn-00babad4) → [`00babad8`](#insn-00babad8)
- ブロック [`00babad8`](#insn-00babad8) 範囲 `[['00babad8', '00babadf']]`
  - `FALL_THROUGH` [`00babadc`](#insn-00babadc) → [`00babae0`](#insn-00babae0)
- ブロック [`00babae0`](#insn-00babae0) 範囲 `[['00babae0', '00babae3']]`
  - `FALL_THROUGH` [`00babae0`](#insn-00babae0) → [`00babae4`](#insn-00babae4)
- ブロック [`00babae4`](#insn-00babae4) 範囲 `[['00babae4', '00babaf3']]`
  - `FALL_THROUGH` [`00babaf0`](#insn-00babaf0) → [`00babaf4`](#insn-00babaf4)
- ブロック [`00babaf4`](#insn-00babaf4) 範囲 `[['00babaf4', '00babb13']]`
  - `FALL_THROUGH` [`00babb10`](#insn-00babb10) → [`00babb14`](#insn-00babb14)
- ブロック [`00babb14`](#insn-00babb14) 範囲 `[['00babb14', '00babb17']]`
  - `FALL_THROUGH` [`00babb14`](#insn-00babb14) → [`00babb18`](#insn-00babb18)
- ブロック [`00babb18`](#insn-00babb18) 範囲 `[['00babb18', '00babb1b']]`
  - `CONDITIONAL_JUMP` [`00babb18`](#insn-00babb18) → [`00babae0`](#insn-00babae0)
  - `FALL_THROUGH` [`00babb18`](#insn-00babb18) → [`00babb1c`](#insn-00babb1c)
- ブロック [`00babb1c`](#insn-00babb1c) 範囲 `[['00babb1c', '00babb27']]`
  - `UNCONDITIONAL_JUMP` [`00babb24`](#insn-00babb24) → [`00babb2c`](#insn-00babb2c)
- ブロック [`00babb28`](#insn-00babb28) 範囲 `[['00babb28', '00babb2b']]`
  - `FALL_THROUGH` [`00babb28`](#insn-00babb28) → [`00babb2c`](#insn-00babb2c)
- ブロック [`00babb2c`](#insn-00babb2c) 範囲 `[['00babb2c', '00babb3b']]`
  - `CONDITIONAL_JUMP` [`00babb38`](#insn-00babb38) → [`00babb60`](#insn-00babb60)
  - `FALL_THROUGH` [`00babb38`](#insn-00babb38) → [`00babb3c`](#insn-00babb3c)
- ブロック [`00babb3c`](#insn-00babb3c) 範囲 `[['00babb3c', '00babb3f']]`
  - `CONDITIONAL_JUMP` [`00babb3c`](#insn-00babb3c) → [`00babb78`](#insn-00babb78)
  - `FALL_THROUGH` [`00babb3c`](#insn-00babb3c) → [`00babb40`](#insn-00babb40)
- ブロック [`00babb40`](#insn-00babb40) 範囲 `[['00babb40', '00babb4f']]`
  - `FALL_THROUGH` [`00babb4c`](#insn-00babb4c) → [`00babb50`](#insn-00babb50)
- ブロック [`00babb50`](#insn-00babb50) 範囲 `[['00babb50', '00babb53']]`
- ブロック [`00babb54`](#insn-00babb54) 範囲 `[['00babb54', '00babb5f']]`
  - `CONDITIONAL_JUMP` [`00babb5c`](#insn-00babb5c) → [`00babb3c`](#insn-00babb3c)
  - `FALL_THROUGH` [`00babb5c`](#insn-00babb5c) → [`00babb60`](#insn-00babb60)
- ブロック [`00babb60`](#insn-00babb60) 範囲 `[['00babb60', '00babb6b']]`
  - `CONDITIONAL_JUMP` [`00babb68`](#insn-00babb68) → [`00babb54`](#insn-00babb54)
  - `FALL_THROUGH` [`00babb68`](#insn-00babb68) → [`00babb6c`](#insn-00babb6c)
- ブロック [`00babb6c`](#insn-00babb6c) 範囲 `[['00babb6c', '00babb6f']]`
  - `FALL_THROUGH` [`00babb6c`](#insn-00babb6c) → [`00babb70`](#insn-00babb70)
- ブロック [`00babb70`](#insn-00babb70) 範囲 `[['00babb70', '00babb77']]`
  - `UNCONDITIONAL_JUMP` [`00babb74`](#insn-00babb74) → [`00babb54`](#insn-00babb54)
- ブロック [`00babb78`](#insn-00babb78) 範囲 `[['00babb78', '00babb7f']]`
  - `FALL_THROUGH` [`00babb7c`](#insn-00babb7c) → [`00babb80`](#insn-00babb80)
- ブロック [`00babb80`](#insn-00babb80) 範囲 `[['00babb80', '00babb83']]`
  - `FALL_THROUGH` [`00babb80`](#insn-00babb80) → [`00babb84`](#insn-00babb84)
- ブロック [`00babb84`](#insn-00babb84) 範囲 `[['00babb84', '00babb87']]`
- ブロック [`00babb88`](#insn-00babb88) 範囲 `[['00babb88', '00babb8f']]`
  - `UNCONDITIONAL_JUMP` [`00babb8c`](#insn-00babb8c) → [`00baba98`](#insn-00baba98)

## 命令位置別の参照

- [`00baba2c`](#insn-00baba2c) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baba30`](#insn-00baba30) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baba34`](#insn-00baba34) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baba50`](#insn-00baba50) → [`00baba88`](#insn-00baba88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baba6c`](#insn-00baba6c) → [`00baba8c`](#insn-00baba8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baba7c`](#insn-00baba7c) → [`00babb88`](#insn-00babb88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baba84`](#insn-00baba84) → [`00baba90`](#insn-00baba90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baba88`](#insn-00baba88) → [`00c5b210`](../00c5b/00c5b210.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b210` · 推定シンボル `None` · 推定型 `None`
- [`00baba94`](#insn-00baba94) → [`00c57f60`](../00c57/00c57f60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f60` · 推定シンボル `None` · 推定型 `None`
- [`00babad4`](#insn-00babad4) → [`00babb28`](#insn-00babb28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babb18`](#insn-00babb18) → [`00babae0`](#insn-00babae0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babb24`](#insn-00babb24) → [`00babb2c`](#insn-00babb2c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babb38`](#insn-00babb38) → [`00babb60`](#insn-00babb60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babb3c`](#insn-00babb3c) → [`00babb78`](#insn-00babb78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babb44`](#insn-00babb44) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babb48`](#insn-00babb48) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babb50`](#insn-00babb50) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00babb5c`](#insn-00babb5c) → [`00babb3c`](#insn-00babb3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babb68`](#insn-00babb68) → [`00babb54`](#insn-00babb54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babb70`](#insn-00babb70) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00babb74`](#insn-00babb74) → [`00babb54`](#insn-00babb54) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babb78`](#insn-00babb78) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babb7c`](#insn-00babb7c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babb8c`](#insn-00babb8c) → [`00baba98`](#insn-00baba98) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00baba2c`](#insn-00baba2c)

~~~json
{
  "source": "00baba2c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baba30`](#insn-00baba30)

~~~json
{
  "source": "00baba30",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baba34`](#insn-00baba34)

~~~json
{
  "source": "00baba34",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baba50`](#insn-00baba50)

~~~json
{
  "source": "00baba50",
  "target": "00baba88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baba6c`](#insn-00baba6c)

~~~json
{
  "source": "00baba6c",
  "target": "00baba8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baba7c`](#insn-00baba7c)

~~~json
{
  "source": "00baba7c",
  "target": "00babb88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baba84`](#insn-00baba84)

~~~json
{
  "source": "00baba84",
  "target": "00baba90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baba88`](#insn-00baba88)

~~~json
{
  "source": "00baba88",
  "target": "00c5b210",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baba94`](#insn-00baba94)

~~~json
{
  "source": "00baba94",
  "target": "00c57f60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00babad4`](#insn-00babad4)

~~~json
{
  "source": "00babad4",
  "target": "00babb28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babb18`](#insn-00babb18)

~~~json
{
  "source": "00babb18",
  "target": "00babae0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babb24`](#insn-00babb24)

~~~json
{
  "source": "00babb24",
  "target": "00babb2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babb38`](#insn-00babb38)

~~~json
{
  "source": "00babb38",
  "target": "00babb60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babb3c`](#insn-00babb3c)

~~~json
{
  "source": "00babb3c",
  "target": "00babb78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babb44`](#insn-00babb44)

~~~json
{
  "source": "00babb44",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babb48`](#insn-00babb48)

~~~json
{
  "source": "00babb48",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babb50`](#insn-00babb50)

~~~json
{
  "source": "00babb50",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00babb5c`](#insn-00babb5c)

~~~json
{
  "source": "00babb5c",
  "target": "00babb3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babb68`](#insn-00babb68)

~~~json
{
  "source": "00babb68",
  "target": "00babb54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babb70`](#insn-00babb70)

~~~json
{
  "source": "00babb70",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00babb74`](#insn-00babb74)

~~~json
{
  "source": "00babb74",
  "target": "00babb54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babb78`](#insn-00babb78)

~~~json
{
  "source": "00babb78",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babb7c`](#insn-00babb7c)

~~~json
{
  "source": "00babb7c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babb8c`](#insn-00babb8c)

~~~json
{
  "source": "00babb8c",
  "target": "00baba98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
