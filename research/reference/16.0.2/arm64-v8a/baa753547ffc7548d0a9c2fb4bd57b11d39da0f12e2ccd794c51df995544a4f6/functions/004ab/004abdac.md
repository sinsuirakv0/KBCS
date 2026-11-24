# 004abdac

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `004abd6c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ab/004abd6c.md) · 移動量 `+0x40`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0007.md#compare-fecc1390038861cee3e455c8c439aaac)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `004ac0cc`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ac/004ac0cc.md) · 移動量 `+0x320`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0007.md#compare-82a3d4a66fbdf8433615e60fbdcd870c)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "004abdac",
  "name": "_ZN5Botan11BER_Decoder6decodeERNS_6BigIntENS_8ASN1_TagES3_",
  "size": 644,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "42ca49d4938130bfc35f60a504b42dbaa1eacb79c5331477c17cd9dea0b10047",
  "source_text_sha256": "42ca49d4938130bfc35f60a504b42dbaa1eacb79c5331477c17cd9dea0b10047",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "004abdac",
        "004ac02b"
      ],
      [
        "004ac064",
        "004ac067"
      ]
    ],
    "bytes_sha256": "a9bc1e728f008a089ff2f76920e4f197503b284bcc1c044aa4108ed8d22f5e15",
    "instruction_count": 161,
    "instruction_bytes": 644,
    "body_bytes": 644,
    "indirect": 3,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c58990](../00c58/00c58990.md)

## 呼び出し先

- [00c57fb0](../00c57/00c57fb0.md)
- [00c58730](../00c58/00c58730.md)
- [00c587f0](../00c58/00c587f0.md)
- [00c58800](../00c58/00c58800.md)
- [00c589f0](../00c58/00c589f0.md)
- [00c58a00](../00c58/00c58a00.md)
- [0112a058](../0112a/0112a058.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 3541 bytes

~~~c

undefined8
_ZN5Botan11BER_Decoder6decodeERNS_6BigIntENS_8ASN1_TagES3_
          (undefined8 param_1,void **param_2,undefined4 param_3,undefined4 param_4)

{
  int *piVar1;
  undefined4 uVar2;
  char cVar3;
  char cVar4;
  long lVar5;
  uint uVar6;
  char *pcVar7;
  void *pvVar8;
  long lVar9;
  void *pvVar10;
  undefined1 auStack_98 [8];
  char *local_90;
  char *local_88;
  long local_80;
  void *local_78;
  void *local_70;
  void *pvStack_68;
  undefined4 local_60;
  long local_58;
  
  lVar5 = tpidr_el0;
  local_58 = *(long *)(lVar5 + 0x28);
  _ZN5Botan11BER_Decoder15get_next_objectEv(auStack_98);
  _ZNK5Botan10BER_Object11assert_is_aENS_8ASN1_TagES1_(auStack_98,param_3,param_4);
  if (local_90 == local_88) {
    _ZN5Botan6BigIntC1Em(&local_78,0);
    if (&local_78 != param_2) {
      pvVar10 = param_2[2];
      pvVar8 = *param_2;
      *param_2 = local_78;
      uVar2 = *(undefined4 *)(param_2 + 3);
      param_2[2] = pvStack_68;
      param_2[1] = local_70;
      *(undefined4 *)(param_2 + 3) = local_60;
      local_78 = pvVar8;
      pvStack_68 = pvVar10;
      local_60 = uVar2;
    }
    pvVar8 = local_78;
    pcVar7 = local_90;
    if (local_78 != (void *)0x0) {
      local_70 = local_78;
      (*(code *)PTR_memset_00c67808)(local_78,0,(long)pvStack_68 - (long)local_78);
      free(pvVar8);
      pcVar7 = local_90;
    }
  }
  else {
    cVar4 = *local_90;
    pcVar7 = local_88;
    if (cVar4 < '\0') {
      pcVar7 = local_88 + ~(ulong)local_90;
      do {
        if (pcVar7 == (char *)0xffffffffffffffff) break;
        cVar3 = local_90[(long)pcVar7];
        local_90[(long)pcVar7] = cVar3 + -1;
        pcVar7 = pcVar7 + -1;
      } while (cVar3 == '\0');
      pcVar7 = local_90;
      if (local_88 != local_90) {
        lVar9 = 0;
        do {
          local_90[lVar9] = ~local_90[lVar9];
          lVar9 = lVar9 + 1;
          pcVar7 = local_88;
        } while (lVar9 != (long)local_88 - (long)local_90);
      }
    }
    _ZN5Botan6BigIntC1EPKhmNS0_4BaseE(&local_78,local_90,(long)pcVar7 - (long)local_90,0x100);
    if (&local_78 != param_2) {
      pvVar10 = param_2[2];
      pvVar8 = *param_2;
      *param_2 = local_78;
      uVar2 = *(undefined4 *)(param_2 + 3);
      param_2[2] = pvStack_68;
      param_2[1] = local_70;
      *(undefined4 *)(param_2 + 3) = local_60;
      local_78 = pvVar8;
      pvStack_68 = pvVar10;
      local_60 = uVar2;
    }
    pvVar8 = local_78;
    if (local_78 != (void *)0x0) {
      local_70 = local_78;
      (*(code *)PTR_memset_00c67808)(local_78,0,(long)pvStack_68 - (long)local_78);
      free(pvVar8);
    }
    pcVar7 = local_90;
    if (cVar4 < '\0') {
      piVar1 = *param_2;
      uVar6 = (uint)(*(int *)(param_2 + 3) != 1);
      lVar9 = (long)param_2[1] - (long)piVar1 >> 2;
      if ((long)param_2[1] - (long)piVar1 == 0) {
joined_r0x004ac004:
        do {
          if (lVar9 == 0) goto LAB_004ac018;
          if (*piVar1 != 0) goto LAB_004ac01c;
          lVar9 = lVar9 + -1;
          piVar1 = piVar1 + 1;
        } while( true );
      }
      do {
        if (piVar1[lVar9 + -1] != 0) goto joined_r0x004ac004;
        lVar9 = lVar9 + -1;
      } while (lVar9 != 0);
LAB_004ac018:
      uVar6 = 1;
LAB_004ac01c:
      *(uint *)(param_2 + 3) = uVar6;
    }
  }
  if (pcVar7 != (char *)0x0) {
    (*(code *)PTR_memset_00c67808)(pcVar7,0,local_80 - (long)pcVar7);
    free(pcVar7);
  }
  if (*(long *)(lVar5 + 0x28) != local_58) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return param_1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-004abdac"></a> `004abdac` | `ff 83 02 d1` | sub sp,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-004abdb0"></a> `004abdb0` | `fd 7b 05 a9` | stp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-004abdb4"></a> `004abdb4` | `f9 33 00 f9` | str x25,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-004abdb8"></a> `004abdb8` | `f8 5f 07 a9` | stp x24,x23,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-004abdbc"></a> `004abdbc` | `f6 57 08 a9` | stp x22,x21,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-004abdc0"></a> `004abdc0` | `f4 4f 09 a9` | stp x20,x19,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-004abdc4"></a> `004abdc4` | `fd 43 01 91` | add x29,sp,#0x50 | `FALL_THROUGH`
<a id="insn-004abdc8"></a> `004abdc8` | `57 d0 3b d5` | mrs x23,tpidr_el0 | `FALL_THROUGH`
<a id="insn-004abdcc"></a> `004abdcc` | `f5 03 03 2a` | mov w21,w3 | `FALL_THROUGH`
<a id="insn-004abdd0"></a> `004abdd0` | `f6 03 02 2a` | mov w22,w2 | `FALL_THROUGH`
<a id="insn-004abdd4"></a> `004abdd4` | `e8 16 40 f9` | ldr x8,[x23, #0x28] | `FALL_THROUGH`
<a id="insn-004abdd8"></a> `004abdd8` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-004abddc"></a> `004abddc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-004abde0"></a> `004abde0` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-004abde4"></a> `004abde4` | `e8 23 00 91` | add x8,sp,#0x8 | `FALL_THROUGH`
<a id="insn-004abde8"></a> `004abde8` | `82 b2 1e 94` | bl 0x00c587f0 | `UNCONDITIONAL_CALL`
<a id="insn-004abdec"></a> `004abdec` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-004abdf0"></a> `004abdf0` | `e1 03 16 2a` | mov w1,w22 | `FALL_THROUGH`
<a id="insn-004abdf4"></a> `004abdf4` | `e2 03 15 2a` | mov w2,w21 | `FALL_THROUGH`
<a id="insn-004abdf8"></a> `004abdf8` | `82 b2 1e 94` | bl 0x00c58800 | `UNCONDITIONAL_CALL`
<a id="insn-004abdfc"></a> `004abdfc` | `e1 23 41 a9` | ldp x1,x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-004abe00"></a> `004abe00` | `f6 3d 00 90` | adrp x22,0xc67000 | `FALL_THROUGH`
<a id="insn-004abe04"></a> `004abe04` | `3f 00 08 eb` | cmp x1,x8 | `FALL_THROUGH`
<a id="insn-004abe08"></a> `004abe08` | `60 03 00 54` | b.eq 0x004abe74 | `CONDITIONAL_JUMP`
<a id="insn-004abe0c"></a> `004abe0c` | `38 00 c0 39` | ldrsb w24,[x1] | `FALL_THROUGH`
<a id="insn-004abe10"></a> `004abe10` | `58 07 f8 36` | tbz w24,#0x1f,0x004abef8 | `CONDITIONAL_JUMP`
<a id="insn-004abe14"></a> `004abe14` | `e9 03 21 aa` | mvn x9,x1 | `FALL_THROUGH`
<a id="insn-004abe18"></a> `004abe18` | `28 01 08 8b` | add x8,x9,x8 | `FALL_THROUGH`
<a id="insn-004abe1c"></a> `004abe1c` | `e1 0b 40 f9` | ldr x1,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-004abe20"></a> `004abe20` | `1f 05 00 b1` | cmn x8,#0x1 | `FALL_THROUGH`
<a id="insn-004abe24"></a> `004abe24` | `e0 00 00 54` | b.eq 0x004abe40 | `CONDITIONAL_JUMP`
<a id="insn-004abe28"></a> `004abe28` | `29 68 68 38` | ldrb w9,[x1, x8, LSL ] | `FALL_THROUGH`
<a id="insn-004abe2c"></a> `004abe2c` | `2a 05 00 51` | sub w10,w9,#0x1 | `FALL_THROUGH`
<a id="insn-004abe30"></a> `004abe30` | `2a 68 28 38` | strb w10,[x1, x8, LSL ] | `FALL_THROUGH`
<a id="insn-004abe34"></a> `004abe34` | `08 05 00 d1` | sub x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-004abe38"></a> `004abe38` | `29 ff ff 34` | cbz w9,0x004abe1c | `CONDITIONAL_JUMP`
<a id="insn-004abe3c"></a> `004abe3c` | `e1 0b 40 f9` | ldr x1,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-004abe40"></a> `004abe40` | `e8 0f 40 f9` | ldr x8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-004abe44"></a> `004abe44` | `1f 01 01 eb` | cmp x8,x1 | `FALL_THROUGH`
<a id="insn-004abe48"></a> `004abe48` | `60 05 00 54` | b.eq 0x004abef4 | `CONDITIONAL_JUMP`
<a id="insn-004abe4c"></a> `004abe4c` | `e9 03 1f aa` | mov x9,xzr | `FALL_THROUGH`
<a id="insn-004abe50"></a> `004abe50` | `28 68 69 38` | ldrb w8,[x1, x9, LSL ] | `FALL_THROUGH`
<a id="insn-004abe54"></a> `004abe54` | `e8 03 28 2a` | mvn w8,w8 | `FALL_THROUGH`
<a id="insn-004abe58"></a> `004abe58` | `28 68 29 38` | strb w8,[x1, x9, LSL ] | `FALL_THROUGH`
<a id="insn-004abe5c"></a> `004abe5c` | `29 05 00 91` | add x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-004abe60"></a> `004abe60` | `e1 23 41 a9` | ldp x1,x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-004abe64"></a> `004abe64` | `0a 01 01 cb` | sub x10,x8,x1 | `FALL_THROUGH`
<a id="insn-004abe68"></a> `004abe68` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-004abe6c"></a> `004abe6c` | `21 ff ff 54` | b.ne 0x004abe50 | `CONDITIONAL_JUMP`
<a id="insn-004abe70"></a> `004abe70` | `22 00 00 14` | b 0x004abef8 | `UNCONDITIONAL_JUMP`
<a id="insn-004abe74"></a> `004abe74` | `e0 a3 00 91` | add x0,sp,#0x28 | `FALL_THROUGH`
<a id="insn-004abe78"></a> `004abe78` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-004abe7c"></a> `004abe7c` | `f8 a3 00 91` | add x24,sp,#0x28 | `FALL_THROUGH`
<a id="insn-004abe80"></a> `004abe80` | `dc b2 1e 94` | bl 0x00c589f0 | `UNCONDITIONAL_CALL`
<a id="insn-004abe84"></a> `004abe84` | `f5 17 40 f9` | ldr x21,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-004abe88"></a> `004abe88` | `1f 03 14 eb` | cmp x24,x20 | `FALL_THROUGH`
<a id="insn-004abe8c"></a> `004abe8c` | `a0 01 00 54` | b.eq 0x004abec0 | `CONDITIONAL_JUMP`
<a id="insn-004abe90"></a> `004abe90` | `89 0a 40 f9` | ldr x9,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-004abe94"></a> `004abe94` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-004abe98"></a> `004abe98` | `e0 03 c3 3c` | ldur q0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-004abe9c"></a> `004abe9c` | `ea 43 40 b9` | ldr w10,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-004abea0"></a> `004abea0` | `95 02 00 f9` | str x21,[x20] | `FALL_THROUGH`
<a id="insn-004abea4"></a> `004abea4` | `e9 1f 00 f9` | str x9,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-004abea8"></a> `004abea8` | `f5 03 08 aa` | mov x21,x8 | `FALL_THROUGH`
<a id="insn-004abeac"></a> `004abeac` | `89 1a 40 b9` | ldr w9,[x20, #0x18] | `FALL_THROUGH`
<a id="insn-004abeb0"></a> `004abeb0` | `80 82 80 3c` | stur q0,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-004abeb4"></a> `004abeb4` | `e8 17 00 f9` | str x8,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-004abeb8"></a> `004abeb8` | `8a 1a 00 b9` | str w10,[x20, #0x18] | `FALL_THROUGH`
<a id="insn-004abebc"></a> `004abebc` | `e9 43 00 b9` | str w9,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-004abec0"></a> `004abec0` | `b5 05 00 b4` | cbz x21,0x004abf74 | `CONDITIONAL_JUMP`
<a id="insn-004abec4"></a> `004abec4` | `f5 1b 00 f9` | str x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-004abec8"></a> `004abec8` | `e8 1f 40 f9` | ldr x8,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-004abecc"></a> `004abecc` | `c9 06 44 f9` | ldr x9,[x22, #0x808] | `FALL_THROUGH`
<a id="insn-004abed0"></a> `004abed0` | `02 01 15 cb` | sub x2,x8,x21 | `FALL_THROUGH`
<a id="insn-004abed4"></a> `004abed4` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-004abed8"></a> `004abed8` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-004abedc"></a> `004abedc` | `20 01 3f d6` | blr x9 | `COMPUTED_CALL`
<a id="insn-004abee0"></a> `004abee0` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-004abee4"></a> `004abee4` | `13 b2 1e 94` | bl 0x00c58730 | `UNCONDITIONAL_CALL`
<a id="insn-004abee8"></a> `004abee8` | `f4 0b 40 f9` | ldr x20,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-004abeec"></a> `004abeec` | `94 04 00 b5` | cbnz x20,0x004abf7c | `CONDITIONAL_JUMP`
<a id="insn-004abef0"></a> `004abef0` | `2c 00 00 14` | b 0x004abfa0 | `UNCONDITIONAL_JUMP`
<a id="insn-004abef4"></a> `004abef4` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-004abef8"></a> `004abef8` | `02 01 01 cb` | sub x2,x8,x1 | `FALL_THROUGH`
<a id="insn-004abefc"></a> `004abefc` | `e0 a3 00 91` | add x0,sp,#0x28 | `FALL_THROUGH`
<a id="insn-004abf00"></a> `004abf00` | `03 20 80 52` | mov w3,#0x100 | `FALL_THROUGH`
<a id="insn-004abf04"></a> `004abf04` | `f9 a3 00 91` | add x25,sp,#0x28 | `FALL_THROUGH`
<a id="insn-004abf08"></a> `004abf08` | `be b2 1e 94` | bl 0x00c58a00 | `UNCONDITIONAL_CALL`
<a id="insn-004abf0c"></a> `004abf0c` | `f5 17 40 f9` | ldr x21,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-004abf10"></a> `004abf10` | `3f 03 14 eb` | cmp x25,x20 | `FALL_THROUGH`
<a id="insn-004abf14"></a> `004abf14` | `a0 01 00 54` | b.eq 0x004abf48 | `CONDITIONAL_JUMP`
<a id="insn-004abf18"></a> `004abf18` | `89 0a 40 f9` | ldr x9,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-004abf1c"></a> `004abf1c` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-004abf20"></a> `004abf20` | `e0 03 c3 3c` | ldur q0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-004abf24"></a> `004abf24` | `ea 43 40 b9` | ldr w10,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-004abf28"></a> `004abf28` | `95 02 00 f9` | str x21,[x20] | `FALL_THROUGH`
<a id="insn-004abf2c"></a> `004abf2c` | `e9 1f 00 f9` | str x9,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-004abf30"></a> `004abf30` | `f5 03 08 aa` | mov x21,x8 | `FALL_THROUGH`
<a id="insn-004abf34"></a> `004abf34` | `89 1a 40 b9` | ldr w9,[x20, #0x18] | `FALL_THROUGH`
<a id="insn-004abf38"></a> `004abf38` | `80 82 80 3c` | stur q0,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-004abf3c"></a> `004abf3c` | `e8 17 00 f9` | str x8,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-004abf40"></a> `004abf40` | `8a 1a 00 b9` | str w10,[x20, #0x18] | `FALL_THROUGH`
<a id="insn-004abf44"></a> `004abf44` | `e9 43 00 b9` | str w9,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-004abf48"></a> `004abf48` | `55 01 00 b4` | cbz x21,0x004abf70 | `CONDITIONAL_JUMP`
<a id="insn-004abf4c"></a> `004abf4c` | `f5 1b 00 f9` | str x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-004abf50"></a> `004abf50` | `e8 1f 40 f9` | ldr x8,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-004abf54"></a> `004abf54` | `c9 06 44 f9` | ldr x9,[x22, #0x808] | `FALL_THROUGH`
<a id="insn-004abf58"></a> `004abf58` | `02 01 15 cb` | sub x2,x8,x21 | `FALL_THROUGH`
<a id="insn-004abf5c"></a> `004abf5c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-004abf60"></a> `004abf60` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-004abf64"></a> `004abf64` | `20 01 3f d6` | blr x9 | `COMPUTED_CALL`
<a id="insn-004abf68"></a> `004abf68` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-004abf6c"></a> `004abf6c` | `f1 b1 1e 94` | bl 0x00c58730 | `UNCONDITIONAL_CALL`
<a id="insn-004abf70"></a> `004abf70` | `18 03 f8 37` | tbnz w24,#0x1f,0x004abfd0 | `CONDITIONAL_JUMP`
<a id="insn-004abf74"></a> `004abf74` | `f4 0b 40 f9` | ldr x20,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-004abf78"></a> `004abf78` | `54 01 00 b4` | cbz x20,0x004abfa0 | `CONDITIONAL_JUMP`
<a id="insn-004abf7c"></a> `004abf7c` | `f4 0f 00 f9` | str x20,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-004abf80"></a> `004abf80` | `e8 13 40 f9` | ldr x8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-004abf84"></a> `004abf84` | `c9 06 44 f9` | ldr x9,[x22, #0x808] | `FALL_THROUGH`
<a id="insn-004abf88"></a> `004abf88` | `02 01 14 cb` | sub x2,x8,x20 | `FALL_THROUGH`
<a id="insn-004abf8c"></a> `004abf8c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-004abf90"></a> `004abf90` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-004abf94"></a> `004abf94` | `20 01 3f d6` | blr x9 | `COMPUTED_CALL`
<a id="insn-004abf98"></a> `004abf98` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-004abf9c"></a> `004abf9c` | `e5 b1 1e 94` | bl 0x00c58730 | `UNCONDITIONAL_CALL`
<a id="insn-004abfa0"></a> `004abfa0` | `e8 16 40 f9` | ldr x8,[x23, #0x28] | `FALL_THROUGH`
<a id="insn-004abfa4"></a> `004abfa4` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-004abfa8"></a> `004abfa8` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-004abfac"></a> `004abfac` | `c1 05 00 54` | b.ne 0x004ac064 | `CONDITIONAL_JUMP`
<a id="insn-004abfb0"></a> `004abfb0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-004abfb4"></a> `004abfb4` | `f4 4f 49 a9` | ldp x20,x19,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-004abfb8"></a> `004abfb8` | `f9 33 40 f9` | ldr x25,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-004abfbc"></a> `004abfbc` | `f6 57 48 a9` | ldp x22,x21,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-004abfc0"></a> `004abfc0` | `f8 5f 47 a9` | ldp x24,x23,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-004abfc4"></a> `004abfc4` | `fd 7b 45 a9` | ldp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-004abfc8"></a> `004abfc8` | `ff 83 02 91` | add sp,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-004abfcc"></a> `004abfcc` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-004abfd0"></a> `004abfd0` | `88 1a 40 b9` | ldr w8,[x20, #0x18] | `FALL_THROUGH`
<a id="insn-004abfd4"></a> `004abfd4` | `89 2a 40 a9` | ldp x9,x10,[x20] | `FALL_THROUGH`
<a id="insn-004abfd8"></a> `004abfd8` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-004abfdc"></a> `004abfdc` | `e8 07 9f 1a` | cset w8,ne | `FALL_THROUGH`
<a id="insn-004abfe0"></a> `004abfe0` | `4a 01 09 eb` | subs x10,x10,x9 | `FALL_THROUGH`
<a id="insn-004abfe4"></a> `004abfe4` | `4a fd 42 93` | asr x10,x10,#0x2 | `FALL_THROUGH`
<a id="insn-004abfe8"></a> `004abfe8` | `e0 00 00 54` | b.eq 0x004ac004 | `CONDITIONAL_JUMP`
<a id="insn-004abfec"></a> `004abfec` | `2b 11 00 d1` | sub x11,x9,#0x4 | `FALL_THROUGH`
<a id="insn-004abff0"></a> `004abff0` | `6c 79 6a b8` | ldr w12,[x11, x10, LSL #0x2] | `FALL_THROUGH`
<a id="insn-004abff4"></a> `004abff4` | `8c 00 00 35` | cbnz w12,0x004ac004 | `CONDITIONAL_JUMP`
<a id="insn-004abff8"></a> `004abff8` | `4a 05 00 f1` | subs x10,x10,#0x1 | `FALL_THROUGH`
<a id="insn-004abffc"></a> `004abffc` | `a1 ff ff 54` | b.ne 0x004abff0 | `CONDITIONAL_JUMP`
<a id="insn-004ac000"></a> `004ac000` | `06 00 00 14` | b 0x004ac018 | `UNCONDITIONAL_JUMP`
<a id="insn-004ac004"></a> `004ac004` | `aa 00 00 b4` | cbz x10,0x004ac018 | `CONDITIONAL_JUMP`
<a id="insn-004ac008"></a> `004ac008` | `2b 45 40 b8` | ldr w11,[x9], #0x4 | `FALL_THROUGH`
<a id="insn-004ac00c"></a> `004ac00c` | `8b 00 00 35` | cbnz w11,0x004ac01c | `CONDITIONAL_JUMP`
<a id="insn-004ac010"></a> `004ac010` | `4a 05 00 f1` | subs x10,x10,#0x1 | `FALL_THROUGH`
<a id="insn-004ac014"></a> `004ac014` | `a1 ff ff 54` | b.ne 0x004ac008 | `CONDITIONAL_JUMP`
<a id="insn-004ac018"></a> `004ac018` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-004ac01c"></a> `004ac01c` | `88 1a 00 b9` | str w8,[x20, #0x18] | `FALL_THROUGH`
<a id="insn-004ac020"></a> `004ac020` | `f4 0b 40 f9` | ldr x20,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-004ac024"></a> `004ac024` | `d4 fa ff b5` | cbnz x20,0x004abf7c | `CONDITIONAL_JUMP`
<a id="insn-004ac028"></a> `004ac028` | `de ff ff 17` | b 0x004abfa0 | `UNCONDITIONAL_JUMP`
<a id="insn-004ac064"></a> `004ac064` | `d3 af 1e 94` | bl 0x00c57fb0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`004abdac`](#insn-004abdac) 範囲 `[['004abdac', '004abe0b']]`
  - `CONDITIONAL_JUMP` [`004abe08`](#insn-004abe08) → [`004abe74`](#insn-004abe74)
  - `FALL_THROUGH` [`004abe08`](#insn-004abe08) → [`004abe0c`](#insn-004abe0c)
- ブロック [`004abe0c`](#insn-004abe0c) 範囲 `[['004abe0c', '004abe13']]`
  - `CONDITIONAL_JUMP` [`004abe10`](#insn-004abe10) → [`004abef8`](#insn-004abef8)
  - `FALL_THROUGH` [`004abe10`](#insn-004abe10) → [`004abe14`](#insn-004abe14)
- ブロック [`004abe14`](#insn-004abe14) 範囲 `[['004abe14', '004abe1b']]`
  - `FALL_THROUGH` [`004abe18`](#insn-004abe18) → [`004abe1c`](#insn-004abe1c)
- ブロック [`004abe1c`](#insn-004abe1c) 範囲 `[['004abe1c', '004abe27']]`
  - `CONDITIONAL_JUMP` [`004abe24`](#insn-004abe24) → [`004abe40`](#insn-004abe40)
  - `FALL_THROUGH` [`004abe24`](#insn-004abe24) → [`004abe28`](#insn-004abe28)
- ブロック [`004abe28`](#insn-004abe28) 範囲 `[['004abe28', '004abe3b']]`
  - `CONDITIONAL_JUMP` [`004abe38`](#insn-004abe38) → [`004abe1c`](#insn-004abe1c)
  - `FALL_THROUGH` [`004abe38`](#insn-004abe38) → [`004abe3c`](#insn-004abe3c)
- ブロック [`004abe3c`](#insn-004abe3c) 範囲 `[['004abe3c', '004abe3f']]`
  - `FALL_THROUGH` [`004abe3c`](#insn-004abe3c) → [`004abe40`](#insn-004abe40)
- ブロック [`004abe40`](#insn-004abe40) 範囲 `[['004abe40', '004abe4b']]`
  - `CONDITIONAL_JUMP` [`004abe48`](#insn-004abe48) → [`004abef4`](#insn-004abef4)
  - `FALL_THROUGH` [`004abe48`](#insn-004abe48) → [`004abe4c`](#insn-004abe4c)
- ブロック [`004abe4c`](#insn-004abe4c) 範囲 `[['004abe4c', '004abe4f']]`
  - `FALL_THROUGH` [`004abe4c`](#insn-004abe4c) → [`004abe50`](#insn-004abe50)
- ブロック [`004abe50`](#insn-004abe50) 範囲 `[['004abe50', '004abe6f']]`
  - `CONDITIONAL_JUMP` [`004abe6c`](#insn-004abe6c) → [`004abe50`](#insn-004abe50)
  - `FALL_THROUGH` [`004abe6c`](#insn-004abe6c) → [`004abe70`](#insn-004abe70)
- ブロック [`004abe70`](#insn-004abe70) 範囲 `[['004abe70', '004abe73']]`
  - `UNCONDITIONAL_JUMP` [`004abe70`](#insn-004abe70) → [`004abef8`](#insn-004abef8)
- ブロック [`004abe74`](#insn-004abe74) 範囲 `[['004abe74', '004abe8f']]`
  - `CONDITIONAL_JUMP` [`004abe8c`](#insn-004abe8c) → [`004abec0`](#insn-004abec0)
  - `FALL_THROUGH` [`004abe8c`](#insn-004abe8c) → [`004abe90`](#insn-004abe90)
- ブロック [`004abe90`](#insn-004abe90) 範囲 `[['004abe90', '004abebf']]`
  - `FALL_THROUGH` [`004abebc`](#insn-004abebc) → [`004abec0`](#insn-004abec0)
- ブロック [`004abec0`](#insn-004abec0) 範囲 `[['004abec0', '004abec3']]`
  - `CONDITIONAL_JUMP` [`004abec0`](#insn-004abec0) → [`004abf74`](#insn-004abf74)
  - `FALL_THROUGH` [`004abec0`](#insn-004abec0) → [`004abec4`](#insn-004abec4)
- ブロック [`004abec4`](#insn-004abec4) 範囲 `[['004abec4', '004abeef']]`
  - `CONDITIONAL_JUMP` [`004abeec`](#insn-004abeec) → [`004abf7c`](#insn-004abf7c)
  - `FALL_THROUGH` [`004abeec`](#insn-004abeec) → [`004abef0`](#insn-004abef0)
- ブロック [`004abef0`](#insn-004abef0) 範囲 `[['004abef0', '004abef3']]`
  - `UNCONDITIONAL_JUMP` [`004abef0`](#insn-004abef0) → [`004abfa0`](#insn-004abfa0)
- ブロック [`004abef4`](#insn-004abef4) 範囲 `[['004abef4', '004abef7']]`
  - `FALL_THROUGH` [`004abef4`](#insn-004abef4) → [`004abef8`](#insn-004abef8)
- ブロック [`004abef8`](#insn-004abef8) 範囲 `[['004abef8', '004abf17']]`
  - `CONDITIONAL_JUMP` [`004abf14`](#insn-004abf14) → [`004abf48`](#insn-004abf48)
  - `FALL_THROUGH` [`004abf14`](#insn-004abf14) → [`004abf18`](#insn-004abf18)
- ブロック [`004abf18`](#insn-004abf18) 範囲 `[['004abf18', '004abf47']]`
  - `FALL_THROUGH` [`004abf44`](#insn-004abf44) → [`004abf48`](#insn-004abf48)
- ブロック [`004abf48`](#insn-004abf48) 範囲 `[['004abf48', '004abf4b']]`
  - `CONDITIONAL_JUMP` [`004abf48`](#insn-004abf48) → [`004abf70`](#insn-004abf70)
  - `FALL_THROUGH` [`004abf48`](#insn-004abf48) → [`004abf4c`](#insn-004abf4c)
- ブロック [`004abf4c`](#insn-004abf4c) 範囲 `[['004abf4c', '004abf6f']]`
  - `FALL_THROUGH` [`004abf6c`](#insn-004abf6c) → [`004abf70`](#insn-004abf70)
- ブロック [`004abf70`](#insn-004abf70) 範囲 `[['004abf70', '004abf73']]`
  - `CONDITIONAL_JUMP` [`004abf70`](#insn-004abf70) → [`004abfd0`](#insn-004abfd0)
  - `FALL_THROUGH` [`004abf70`](#insn-004abf70) → [`004abf74`](#insn-004abf74)
- ブロック [`004abf74`](#insn-004abf74) 範囲 `[['004abf74', '004abf7b']]`
  - `CONDITIONAL_JUMP` [`004abf78`](#insn-004abf78) → [`004abfa0`](#insn-004abfa0)
  - `FALL_THROUGH` [`004abf78`](#insn-004abf78) → [`004abf7c`](#insn-004abf7c)
- ブロック [`004abf7c`](#insn-004abf7c) 範囲 `[['004abf7c', '004abf9f']]`
  - `FALL_THROUGH` [`004abf9c`](#insn-004abf9c) → [`004abfa0`](#insn-004abfa0)
- ブロック [`004abfa0`](#insn-004abfa0) 範囲 `[['004abfa0', '004abfaf']]`
  - `CONDITIONAL_JUMP` [`004abfac`](#insn-004abfac) → [`004ac064`](#insn-004ac064)
  - `FALL_THROUGH` [`004abfac`](#insn-004abfac) → [`004abfb0`](#insn-004abfb0)
- ブロック [`004abfb0`](#insn-004abfb0) 範囲 `[['004abfb0', '004abfcf']]`
- ブロック [`004abfd0`](#insn-004abfd0) 範囲 `[['004abfd0', '004abfeb']]`
  - `CONDITIONAL_JUMP` [`004abfe8`](#insn-004abfe8) → [`004ac004`](#insn-004ac004)
  - `FALL_THROUGH` [`004abfe8`](#insn-004abfe8) → [`004abfec`](#insn-004abfec)
- ブロック [`004abfec`](#insn-004abfec) 範囲 `[['004abfec', '004abfef']]`
  - `FALL_THROUGH` [`004abfec`](#insn-004abfec) → [`004abff0`](#insn-004abff0)
- ブロック [`004abff0`](#insn-004abff0) 範囲 `[['004abff0', '004abff7']]`
  - `CONDITIONAL_JUMP` [`004abff4`](#insn-004abff4) → [`004ac004`](#insn-004ac004)
  - `FALL_THROUGH` [`004abff4`](#insn-004abff4) → [`004abff8`](#insn-004abff8)
- ブロック [`004abff8`](#insn-004abff8) 範囲 `[['004abff8', '004abfff']]`
  - `CONDITIONAL_JUMP` [`004abffc`](#insn-004abffc) → [`004abff0`](#insn-004abff0)
  - `FALL_THROUGH` [`004abffc`](#insn-004abffc) → [`004ac000`](#insn-004ac000)
- ブロック [`004ac000`](#insn-004ac000) 範囲 `[['004ac000', '004ac003']]`
  - `UNCONDITIONAL_JUMP` [`004ac000`](#insn-004ac000) → [`004ac018`](#insn-004ac018)
- ブロック [`004ac004`](#insn-004ac004) 範囲 `[['004ac004', '004ac007']]`
  - `CONDITIONAL_JUMP` [`004ac004`](#insn-004ac004) → [`004ac018`](#insn-004ac018)
  - `FALL_THROUGH` [`004ac004`](#insn-004ac004) → [`004ac008`](#insn-004ac008)
- ブロック [`004ac008`](#insn-004ac008) 範囲 `[['004ac008', '004ac00f']]`
  - `CONDITIONAL_JUMP` [`004ac00c`](#insn-004ac00c) → [`004ac01c`](#insn-004ac01c)
  - `FALL_THROUGH` [`004ac00c`](#insn-004ac00c) → [`004ac010`](#insn-004ac010)
- ブロック [`004ac010`](#insn-004ac010) 範囲 `[['004ac010', '004ac017']]`
  - `CONDITIONAL_JUMP` [`004ac014`](#insn-004ac014) → [`004ac008`](#insn-004ac008)
  - `FALL_THROUGH` [`004ac014`](#insn-004ac014) → [`004ac018`](#insn-004ac018)
- ブロック [`004ac018`](#insn-004ac018) 範囲 `[['004ac018', '004ac01b']]`
  - `FALL_THROUGH` [`004ac018`](#insn-004ac018) → [`004ac01c`](#insn-004ac01c)
- ブロック [`004ac01c`](#insn-004ac01c) 範囲 `[['004ac01c', '004ac027']]`
  - `CONDITIONAL_JUMP` [`004ac024`](#insn-004ac024) → [`004abf7c`](#insn-004abf7c)
  - `FALL_THROUGH` [`004ac024`](#insn-004ac024) → [`004ac028`](#insn-004ac028)
- ブロック [`004ac028`](#insn-004ac028) 範囲 `[['004ac028', '004ac02b']]`
  - `UNCONDITIONAL_JUMP` [`004ac028`](#insn-004ac028) → [`004abfa0`](#insn-004abfa0)
- ブロック [`004ac064`](#insn-004ac064) 範囲 `[['004ac064', '004ac067']]`

## 命令位置別の参照

- [`004abdb0`](#insn-004abdb0) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004abdb4`](#insn-004abdb4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004abdb8`](#insn-004abdb8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004abdbc`](#insn-004abdbc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004abdc0`](#insn-004abdc0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004abde0`](#insn-004abde0) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004abde8`](#insn-004abde8) → [`00c587f0`](../00c58/00c587f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c587f0` · 推定シンボル `None` · 推定型 `None`
- [`004abdf8`](#insn-004abdf8) → [`00c58800`](../00c58/00c58800.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58800` · 推定シンボル `None` · 推定型 `None`
- [`004abdfc`](#insn-004abdfc) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004abe08`](#insn-004abe08) → [`004abe74`](#insn-004abe74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004abe10`](#insn-004abe10) → [`004abef8`](#insn-004abef8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004abe1c`](#insn-004abe1c) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004abe24`](#insn-004abe24) → [`004abe40`](#insn-004abe40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004abe38`](#insn-004abe38) → [`004abe1c`](#insn-004abe1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004abe3c`](#insn-004abe3c) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004abe40`](#insn-004abe40) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004abe48`](#insn-004abe48) → [`004abef4`](#insn-004abef4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004abe60`](#insn-004abe60) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004abe6c`](#insn-004abe6c) → [`004abe50`](#insn-004abe50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004abe70`](#insn-004abe70) → [`004abef8`](#insn-004abef8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004abe80`](#insn-004abe80) → [`00c589f0`](../00c58/00c589f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c589f0` · 推定シンボル `None` · 推定型 `None`
- [`004abe84`](#insn-004abe84) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004abe8c`](#insn-004abe8c) → [`004abec0`](#insn-004abec0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004abe98`](#insn-004abe98) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004abe9c`](#insn-004abe9c) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004abea4`](#insn-004abea4) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004abeb4`](#insn-004abeb4) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004abebc`](#insn-004abebc) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004abec0`](#insn-004abec0) → [`004abf74`](#insn-004abf74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004abec4`](#insn-004abec4) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004abec8`](#insn-004abec8) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004abecc`](#insn-004abecc) → `00c67808`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004abedc`](#insn-004abedc) → [`0112a058`](../0112a/0112a058.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `0112a058` · 推定シンボル `None` · 推定型 `None`
- [`004abee4`](#insn-004abee4) → [`00c58730`](../00c58/00c58730.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58730` · 推定シンボル `None` · 推定型 `None`
- [`004abee8`](#insn-004abee8) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004abeec`](#insn-004abeec) → [`004abf7c`](#insn-004abf7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004abef0`](#insn-004abef0) → [`004abfa0`](#insn-004abfa0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004abf08`](#insn-004abf08) → [`00c58a00`](../00c58/00c58a00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58a00` · 推定シンボル `None` · 推定型 `None`
- [`004abf0c`](#insn-004abf0c) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004abf14`](#insn-004abf14) → [`004abf48`](#insn-004abf48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004abf20`](#insn-004abf20) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004abf24`](#insn-004abf24) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004abf2c`](#insn-004abf2c) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004abf3c`](#insn-004abf3c) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004abf44`](#insn-004abf44) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004abf48`](#insn-004abf48) → [`004abf70`](#insn-004abf70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004abf4c`](#insn-004abf4c) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004abf50`](#insn-004abf50) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004abf54`](#insn-004abf54) → `00c67808`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004abf64`](#insn-004abf64) → [`0112a058`](../0112a/0112a058.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `0112a058` · 推定シンボル `None` · 推定型 `None`
- [`004abf6c`](#insn-004abf6c) → [`00c58730`](../00c58/00c58730.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58730` · 推定シンボル `None` · 推定型 `None`
- [`004abf70`](#insn-004abf70) → [`004abfd0`](#insn-004abfd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004abf74`](#insn-004abf74) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004abf78`](#insn-004abf78) → [`004abfa0`](#insn-004abfa0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004abf7c`](#insn-004abf7c) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004abf80`](#insn-004abf80) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004abf84`](#insn-004abf84) → `00c67808`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004abf94`](#insn-004abf94) → [`0112a058`](../0112a/0112a058.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `0112a058` · 推定シンボル `None` · 推定型 `None`
- [`004abf9c`](#insn-004abf9c) → [`00c58730`](../00c58/00c58730.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58730` · 推定シンボル `None` · 推定型 `None`
- [`004abfa4`](#insn-004abfa4) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004abfac`](#insn-004abfac) → [`004ac064`](#insn-004ac064) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004abfb4`](#insn-004abfb4) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004abfb8`](#insn-004abfb8) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004abfbc`](#insn-004abfbc) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004abfc0`](#insn-004abfc0) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004abfc4`](#insn-004abfc4) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004abfe8`](#insn-004abfe8) → [`004ac004`](#insn-004ac004) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004abff4`](#insn-004abff4) → [`004ac004`](#insn-004ac004) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004abffc`](#insn-004abffc) → [`004abff0`](#insn-004abff0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ac000`](#insn-004ac000) → [`004ac018`](#insn-004ac018) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ac004`](#insn-004ac004) → [`004ac018`](#insn-004ac018) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ac00c`](#insn-004ac00c) → [`004ac01c`](#insn-004ac01c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ac014`](#insn-004ac014) → [`004ac008`](#insn-004ac008) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ac020`](#insn-004ac020) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ac024`](#insn-004ac024) → [`004abf7c`](#insn-004abf7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ac028`](#insn-004ac028) → [`004abfa0`](#insn-004abfa0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ac064`](#insn-004ac064) → [`00c57fb0`](../00c57/00c57fb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fb0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`004abdb0`](#insn-004abdb0)

~~~json
{
  "source": "004abdb0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004abdb4`](#insn-004abdb4)

~~~json
{
  "source": "004abdb4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004abdb8`](#insn-004abdb8)

~~~json
{
  "source": "004abdb8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004abdbc`](#insn-004abdbc)

~~~json
{
  "source": "004abdbc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004abdc0`](#insn-004abdc0)

~~~json
{
  "source": "004abdc0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004abde0`](#insn-004abde0)

~~~json
{
  "source": "004abde0",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004abde8`](#insn-004abde8)

~~~json
{
  "source": "004abde8",
  "target": "00c587f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004abdf8`](#insn-004abdf8)

~~~json
{
  "source": "004abdf8",
  "target": "00c58800",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004abdfc`](#insn-004abdfc)

~~~json
{
  "source": "004abdfc",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004abe08`](#insn-004abe08)

~~~json
{
  "source": "004abe08",
  "target": "004abe74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004abe10`](#insn-004abe10)

~~~json
{
  "source": "004abe10",
  "target": "004abef8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004abe1c`](#insn-004abe1c)

~~~json
{
  "source": "004abe1c",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004abe24`](#insn-004abe24)

~~~json
{
  "source": "004abe24",
  "target": "004abe40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004abe38`](#insn-004abe38)

~~~json
{
  "source": "004abe38",
  "target": "004abe1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004abe3c`](#insn-004abe3c)

~~~json
{
  "source": "004abe3c",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004abe40`](#insn-004abe40)

~~~json
{
  "source": "004abe40",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004abe48`](#insn-004abe48)

~~~json
{
  "source": "004abe48",
  "target": "004abef4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004abe60`](#insn-004abe60)

~~~json
{
  "source": "004abe60",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004abe6c`](#insn-004abe6c)

~~~json
{
  "source": "004abe6c",
  "target": "004abe50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004abe70`](#insn-004abe70)

~~~json
{
  "source": "004abe70",
  "target": "004abef8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004abe80`](#insn-004abe80)

~~~json
{
  "source": "004abe80",
  "target": "00c589f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004abe84`](#insn-004abe84)

~~~json
{
  "source": "004abe84",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004abe8c`](#insn-004abe8c)

~~~json
{
  "source": "004abe8c",
  "target": "004abec0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004abe98`](#insn-004abe98)

~~~json
{
  "source": "004abe98",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004abe9c`](#insn-004abe9c)

~~~json
{
  "source": "004abe9c",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004abea4`](#insn-004abea4)

~~~json
{
  "source": "004abea4",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004abeb4`](#insn-004abeb4)

~~~json
{
  "source": "004abeb4",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004abebc`](#insn-004abebc)

~~~json
{
  "source": "004abebc",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004abec0`](#insn-004abec0)

~~~json
{
  "source": "004abec0",
  "target": "004abf74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004abec4`](#insn-004abec4)

~~~json
{
  "source": "004abec4",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004abec8`](#insn-004abec8)

~~~json
{
  "source": "004abec8",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004abecc`](#insn-004abecc)

~~~json
{
  "source": "004abecc",
  "target": "00c67808",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c67808",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004abedc`](#insn-004abedc)

~~~json
{
  "source": "004abedc",
  "target": "0112a058",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004abee4`](#insn-004abee4)

~~~json
{
  "source": "004abee4",
  "target": "00c58730",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004abee8`](#insn-004abee8)

~~~json
{
  "source": "004abee8",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004abeec`](#insn-004abeec)

~~~json
{
  "source": "004abeec",
  "target": "004abf7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004abef0`](#insn-004abef0)

~~~json
{
  "source": "004abef0",
  "target": "004abfa0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004abf08`](#insn-004abf08)

~~~json
{
  "source": "004abf08",
  "target": "00c58a00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004abf0c`](#insn-004abf0c)

~~~json
{
  "source": "004abf0c",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004abf14`](#insn-004abf14)

~~~json
{
  "source": "004abf14",
  "target": "004abf48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004abf20`](#insn-004abf20)

~~~json
{
  "source": "004abf20",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004abf24`](#insn-004abf24)

~~~json
{
  "source": "004abf24",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004abf2c`](#insn-004abf2c)

~~~json
{
  "source": "004abf2c",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004abf3c`](#insn-004abf3c)

~~~json
{
  "source": "004abf3c",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004abf44`](#insn-004abf44)

~~~json
{
  "source": "004abf44",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004abf48`](#insn-004abf48)

~~~json
{
  "source": "004abf48",
  "target": "004abf70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004abf4c`](#insn-004abf4c)

~~~json
{
  "source": "004abf4c",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004abf50`](#insn-004abf50)

~~~json
{
  "source": "004abf50",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004abf54`](#insn-004abf54)

~~~json
{
  "source": "004abf54",
  "target": "00c67808",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c67808",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004abf64`](#insn-004abf64)

~~~json
{
  "source": "004abf64",
  "target": "0112a058",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004abf6c`](#insn-004abf6c)

~~~json
{
  "source": "004abf6c",
  "target": "00c58730",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004abf70`](#insn-004abf70)

~~~json
{
  "source": "004abf70",
  "target": "004abfd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004abf74`](#insn-004abf74)

~~~json
{
  "source": "004abf74",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004abf78`](#insn-004abf78)

~~~json
{
  "source": "004abf78",
  "target": "004abfa0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004abf7c`](#insn-004abf7c)

~~~json
{
  "source": "004abf7c",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004abf80`](#insn-004abf80)

~~~json
{
  "source": "004abf80",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004abf84`](#insn-004abf84)

~~~json
{
  "source": "004abf84",
  "target": "00c67808",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c67808",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004abf94`](#insn-004abf94)

~~~json
{
  "source": "004abf94",
  "target": "0112a058",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004abf9c`](#insn-004abf9c)

~~~json
{
  "source": "004abf9c",
  "target": "00c58730",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004abfa4`](#insn-004abfa4)

~~~json
{
  "source": "004abfa4",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004abfac`](#insn-004abfac)

~~~json
{
  "source": "004abfac",
  "target": "004ac064",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004abfb4`](#insn-004abfb4)

~~~json
{
  "source": "004abfb4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004abfb8`](#insn-004abfb8)

~~~json
{
  "source": "004abfb8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004abfbc`](#insn-004abfbc)

~~~json
{
  "source": "004abfbc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004abfc0`](#insn-004abfc0)

~~~json
{
  "source": "004abfc0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004abfc4`](#insn-004abfc4)

~~~json
{
  "source": "004abfc4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004abfe8`](#insn-004abfe8)

~~~json
{
  "source": "004abfe8",
  "target": "004ac004",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004abff4`](#insn-004abff4)

~~~json
{
  "source": "004abff4",
  "target": "004ac004",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004abffc`](#insn-004abffc)

~~~json
{
  "source": "004abffc",
  "target": "004abff0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ac000`](#insn-004ac000)

~~~json
{
  "source": "004ac000",
  "target": "004ac018",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ac004`](#insn-004ac004)

~~~json
{
  "source": "004ac004",
  "target": "004ac018",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ac00c`](#insn-004ac00c)

~~~json
{
  "source": "004ac00c",
  "target": "004ac01c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ac014`](#insn-004ac014)

~~~json
{
  "source": "004ac014",
  "target": "004ac008",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ac020`](#insn-004ac020)

~~~json
{
  "source": "004ac020",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ac024`](#insn-004ac024)

~~~json
{
  "source": "004ac024",
  "target": "004abf7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ac028`](#insn-004ac028)

~~~json
{
  "source": "004ac028",
  "target": "004abfa0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ac064`](#insn-004ac064)

~~~json
{
  "source": "004ac064",
  "target": "00c57fb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
