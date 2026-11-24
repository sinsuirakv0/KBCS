# 00acd5fc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00acd5b8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acd5b8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0007.md#compare-2ac3ee9faf736e3f5be8057e6a570c50)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b2d0b4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2d/00b2d0b4.md) · 移動量 `+0x5fab8`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0054.md#compare-709637eff1df7ab91d5c11b985b27946)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acd5fc",
  "name": "FUN_00acd5fc",
  "size": 508,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2f8813b9b84fba773d9703e789bfdbb270512179b49dd1bdcbcb7d792b34b132",
  "source_text_sha256": "2f8813b9b84fba773d9703e789bfdbb270512179b49dd1bdcbcb7d792b34b132",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00acd5fc",
        "00acd7f7"
      ]
    ],
    "bytes_sha256": "6a541b21a780e4bd50446eb81f3dece82b617b9b9f679b2a5e5cf41135422ef4",
    "instruction_count": 127,
    "instruction_bytes": 508,
    "body_bytes": 508,
    "indirect": 3,
    "unresolved": 3
  }
}
~~~

## 呼び出し元

- [00acc598](../00acc/00acc598.md)

## 呼び出し先

- [0041e380](../0041e/0041e380.md)
- [00acd800](../00acd/00acd800.md)
- [00bdb040](../00bdb/00bdb040.md)
- [00bdb060](../00bdb/00bdb060.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 3402 bytes

~~~c

long FUN_00acd5fc(long *param_1,long *param_2)

{
  ulong uVar1;
  long *plVar2;
  void *__ptr;
  long lVar3;
  long *plVar4;
  long *plVar5;
  long *plVar6;
  long *plVar7;
  long lVar8;
  ulong uVar9;
  long lVar10;
  long *plVar11;
  long lVar12;
  long *plVar13;
  
  plVar13 = (long *)*param_1;
  plVar11 = (long *)param_1[1];
  lVar12 = (long)plVar11 - (long)plVar13;
  lVar3 = lVar12 >> 4;
  uVar1 = lVar3 * -0x5555555555555555 + 1;
  if (0x555555555555555 < uVar1) {
    FUN_00acd800(param_1);
LAB_00acd7f4:
                    /* WARNING: Subroutine does not return */
    FUN_0041e380();
  }
  lVar8 = param_1[2] - (long)plVar13 >> 4;
  uVar9 = lVar8 * 0x5555555555555556;
  if (uVar9 < uVar1 || uVar9 - uVar1 == 0) {
    uVar9 = uVar1;
  }
  if (0x2aaaaaaaaaaaaa9 < (ulong)(lVar8 * -0x5555555555555555)) {
    uVar9 = 0x555555555555555;
  }
  if (uVar9 == 0) {
    lVar8 = 0;
  }
  else {
    if (0x555555555555555 < uVar9) goto LAB_00acd7f4;
    lVar8 = _Znwm(uVar9 * 0x30);
  }
  lVar10 = lVar8 + lVar3 * 0x10;
  plVar2 = param_2 + 4;
  plVar5 = (long *)*plVar2;
  if (plVar5 == (long *)0x0) {
                    /* catch() { ... } // from try @ 00accb6c with catch @ 00acd6c0 */
    plVar2 = (long *)(lVar10 + 0x20);
LAB_00acd6c4:
                    /* catch() { ... } // from try @ 00accaec with catch @ 00acd6c4 */
    *plVar2 = 0;
                    /* catch() { ... } // from try @ 00acca7c with catch @ 00acd6c8 */
                    /* catch() { ... } // from try @ 00acca74 with catch @ 00acd6cc */
    if (plVar13 == plVar11) goto LAB_00acd7ac;
  }
  else {
    if (plVar5 != param_2) {
      *(long **)(lVar10 + 0x20) = plVar5;
      goto LAB_00acd6c4;
    }
    lVar12 = *param_2;
    *(long *)(lVar10 + 0x20) = lVar10;
                    /* catch() { ... } // from try @ 00acc0ac with catch @ 00acd6e0 */
                    /* catch() { ... } // from try @ 00acc0bc with catch @ 00acd6e8 */
    (**(code **)(lVar12 + 0x18))(param_2,lVar10);
    plVar13 = (long *)*param_1;
    plVar11 = (long *)param_1[1];
    lVar12 = (long)plVar11 - (long)plVar13;
    if (plVar13 == plVar11) goto LAB_00acd7ac;
  }
                    /* catch() { ... } // from try @ 00acacb0 with catch @ 00acd710 */
  plVar2 = (long *)(lVar3 * 0x10 + (lVar12 >> 4) * -0x10 + lVar8 + 0x20);
  plVar5 = plVar13;
  do {
    plVar4 = plVar5 + 4;
    plVar6 = (long *)*plVar4;
    plVar7 = plVar2;
    if (plVar6 == (long *)0x0) {
LAB_00acd72c:
      *plVar7 = 0;
    }
    else {
      if (plVar5 != plVar6) {
                    /* catch() { ... } // from try @ 00aca7d4 with catch @ 00acd728 */
        *plVar2 = (long)plVar6;
        plVar7 = plVar4;
        goto LAB_00acd72c;
      }
      *plVar2 = (long)(plVar2 + -4);
      (**(code **)(*(long *)*plVar4 + 0x18))();
    }
    plVar5 = plVar5 + 6;
    plVar2 = plVar2 + 6;
  } while (plVar5 != plVar11);
  do {
    plVar2 = (long *)plVar13[4];
    if (plVar13 == plVar2) {
      lVar3 = 0x20;
      plVar2 = plVar13;
LAB_00acd77c:
      (**(code **)(*plVar2 + lVar3))();
    }
    else if (plVar2 != (long *)0x0) {
      lVar3 = 0x28;
      goto LAB_00acd77c;
    }
    plVar13 = plVar13 + 6;
  } while (plVar13 != plVar11);
LAB_00acd7ac:
  __ptr = (void *)*param_1;
  *param_1 = lVar10 - lVar12;
  param_1[1] = lVar10 + 0x30;
  param_1[2] = lVar8 + uVar9 * 0x30;
  if (__ptr != (void *)0x0) {
    _ZdlPv(__ptr);
  }
  return lVar10 + 0x30;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00acd5fc"></a> `00acd5fc` | `fd 7b ba a9` | stp x29,x30,[sp, #-0x60]! | `FALL_THROUGH`
<a id="insn-00acd600"></a> `00acd600` | `fc 6f 01 a9` | stp x28,x27,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acd604"></a> `00acd604` | `fa 67 02 a9` | stp x26,x25,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00acd608"></a> `00acd608` | `f8 5f 03 a9` | stp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00acd60c"></a> `00acd60c` | `f6 57 04 a9` | stp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00acd610"></a> `00acd610` | `f4 4f 05 a9` | stp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00acd614"></a> `00acd614` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00acd618"></a> `00acd618` | `19 5c 40 a9` | ldp x25,x23,[x0] | `FALL_THROUGH`
<a id="insn-00acd61c"></a> `00acd61c` | `ea f3 01 b2` | orr x10,xzr,#-0x5555555555555556 | `FALL_THROUGH`
<a id="insn-00acd620"></a> `00acd620` | `6a 55 95 f2` | movk x10,#0xaaab | `FALL_THROUGH`
<a id="insn-00acd624"></a> `00acd624` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00acd628"></a> `00acd628` | `f8 02 19 cb` | sub x24,x23,x25 | `FALL_THROUGH`
<a id="insn-00acd62c"></a> `00acd62c` | `08 ff 44 93` | asr x8,x24,#0x4 | `FALL_THROUGH`
<a id="insn-00acd630"></a> `00acd630` | `1c 7d 0a 9b` | mul x28,x8,x10 | `FALL_THROUGH`
<a id="insn-00acd634"></a> `00acd634` | `e8 f3 00 b2` | orr x8,xzr,#0x5555555555555555 | `FALL_THROUGH`
<a id="insn-00acd638"></a> `00acd638` | `a8 aa e0 f2` | movk x8,#0x555, LSL #48 | `FALL_THROUGH`
<a id="insn-00acd63c"></a> `00acd63c` | `89 07 00 91` | add x9,x28,#0x1 | `FALL_THROUGH`
<a id="insn-00acd640"></a> `00acd640` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00acd644"></a> `00acd644` | `48 0d 00 54` | b.hi 0x00acd7ec | `CONDITIONAL_JUMP`
<a id="insn-00acd648"></a> `00acd648` | `6b 0a 40 f9` | ldr x11,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00acd64c"></a> `00acd64c` | `ec f3 01 b2` | orr x12,xzr,#-0x5555555555555556 | `FALL_THROUGH`
<a id="insn-00acd650"></a> `00acd650` | `f6 03 01 aa` | mov x22,x1 | `FALL_THROUGH`
<a id="insn-00acd654"></a> `00acd654` | `4c 55 e0 f2` | movk x12,#0x2aa, LSL #48 | `FALL_THROUGH`
<a id="insn-00acd658"></a> `00acd658` | `6b 01 19 cb` | sub x11,x11,x25 | `FALL_THROUGH`
<a id="insn-00acd65c"></a> `00acd65c` | `6b fd 44 93` | asr x11,x11,#0x4 | `FALL_THROUGH`
<a id="insn-00acd660"></a> `00acd660` | `6a 7d 0a 9b` | mul x10,x11,x10 | `FALL_THROUGH`
<a id="insn-00acd664"></a> `00acd664` | `4b f9 7f d3` | lsl x11,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00acd668"></a> `00acd668` | `7f 01 09 eb` | cmp x11,x9 | `FALL_THROUGH`
<a id="insn-00acd66c"></a> `00acd66c` | `69 81 89 9a` | csel x9,x11,x9,hi | `FALL_THROUGH`
<a id="insn-00acd670"></a> `00acd670` | `5f 01 0c eb` | cmp x10,x12 | `FALL_THROUGH`
<a id="insn-00acd674"></a> `00acd674` | `3a 31 88 9a` | csel x26,x9,x8,cc | `FALL_THROUGH`
<a id="insn-00acd678"></a> `00acd678` | `1a 01 00 b4` | cbz x26,0x00acd698 | `CONDITIONAL_JUMP`
<a id="insn-00acd67c"></a> `00acd67c` | `5f 03 08 eb` | cmp x26,x8 | `FALL_THROUGH`
<a id="insn-00acd680"></a> `00acd680` | `a8 0b 00 54` | b.hi 0x00acd7f4 | `CONDITIONAL_JUMP`
<a id="insn-00acd684"></a> `00acd684` | `48 07 1a 8b` | add x8,x26,x26, LSL #0x1 | `FALL_THROUGH`
<a id="insn-00acd688"></a> `00acd688` | `00 ed 7c d3` | lsl x0,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00acd68c"></a> `00acd68c` | `6d 36 04 94` | bl 0x00bdb040 | `UNCONDITIONAL_CALL`
<a id="insn-00acd690"></a> `00acd690` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00acd694"></a> `00acd694` | `02 00 00 14` | b 0x00acd69c | `UNCONDITIONAL_JUMP`
<a id="insn-00acd698"></a> `00acd698` | `f4 03 1f aa` | mov x20,xzr | `FALL_THROUGH`
<a id="insn-00acd69c"></a> `00acd69c` | `1b 06 80 52` | mov w27,#0x30 | `FALL_THROUGH`
<a id="insn-00acd6a0"></a> `00acd6a0` | `e8 03 16 aa` | mov x8,x22 | `FALL_THROUGH`
<a id="insn-00acd6a4"></a> `00acd6a4` | `95 53 1b 9b` | madd x21,x28,x27,x20 | `FALL_THROUGH`
<a id="insn-00acd6a8"></a> `00acd6a8` | `09 0d 42 f8` | ldr x9,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-00acd6ac"></a> `00acd6ac` | `a9 00 00 b4` | cbz x9,0x00acd6c0 | `CONDITIONAL_JUMP`
<a id="insn-00acd6b0"></a> `00acd6b0` | `3f 01 16 eb` | cmp x9,x22 | `FALL_THROUGH`
<a id="insn-00acd6b4"></a> `00acd6b4` | `00 01 00 54` | b.eq 0x00acd6d4 | `CONDITIONAL_JUMP`
<a id="insn-00acd6b8"></a> `00acd6b8` | `a9 12 00 f9` | str x9,[x21, #0x20] | `FALL_THROUGH`
<a id="insn-00acd6bc"></a> `00acd6bc` | `02 00 00 14` | b 0x00acd6c4 | `UNCONDITIONAL_JUMP`
<a id="insn-00acd6c0"></a> `00acd6c0` | `a8 82 00 91` | add x8,x21,#0x20 | `FALL_THROUGH`
<a id="insn-00acd6c4"></a> `00acd6c4` | `1f 01 00 f9` | str xzr,[x8] | `FALL_THROUGH`
<a id="insn-00acd6c8"></a> `00acd6c8` | `3f 03 17 eb` | cmp x25,x23 | `FALL_THROUGH`
<a id="insn-00acd6cc"></a> `00acd6cc` | `81 01 00 54` | b.ne 0x00acd6fc | `CONDITIONAL_JUMP`
<a id="insn-00acd6d0"></a> `00acd6d0` | `37 00 00 14` | b 0x00acd7ac | `UNCONDITIONAL_JUMP`
<a id="insn-00acd6d4"></a> `00acd6d4` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00acd6d8"></a> `00acd6d8` | `b5 12 00 f9` | str x21,[x21, #0x20] | `FALL_THROUGH`
<a id="insn-00acd6dc"></a> `00acd6dc` | `08 0d 40 f9` | ldr x8,[x8, #0x18] | `FALL_THROUGH`
<a id="insn-00acd6e0"></a> `00acd6e0` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00acd6e4"></a> `00acd6e4` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00acd6e8"></a> `00acd6e8` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00acd6ec"></a> `00acd6ec` | `79 5e 40 a9` | ldp x25,x23,[x19] | `FALL_THROUGH`
<a id="insn-00acd6f0"></a> `00acd6f0` | `f8 02 19 cb` | sub x24,x23,x25 | `FALL_THROUGH`
<a id="insn-00acd6f4"></a> `00acd6f4` | `3f 03 17 eb` | cmp x25,x23 | `FALL_THROUGH`
<a id="insn-00acd6f8"></a> `00acd6f8` | `a0 05 00 54` | b.eq 0x00acd7ac | `CONDITIONAL_JUMP`
<a id="insn-00acd6fc"></a> `00acd6fc` | `08 ff 44 93` | asr x8,x24,#0x4 | `FALL_THROUGH`
<a id="insn-00acd700"></a> `00acd700` | `e9 f3 00 b2` | orr x9,xzr,#0x5555555555555555 | `FALL_THROUGH`
<a id="insn-00acd704"></a> `00acd704` | `08 7d 09 9b` | mul x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00acd708"></a> `00acd708` | `09 06 80 52` | mov w9,#0x30 | `FALL_THROUGH`
<a id="insn-00acd70c"></a> `00acd70c` | `8a 7f 09 9b` | mul x10,x28,x9 | `FALL_THROUGH`
<a id="insn-00acd710"></a> `00acd710` | `fc 03 19 aa` | mov x28,x25 | `FALL_THROUGH`
<a id="insn-00acd714"></a> `00acd714` | `08 29 09 9b` | madd x8,x8,x9,x10 | `FALL_THROUGH`
<a id="insn-00acd718"></a> `00acd718` | `08 01 14 8b` | add x8,x8,x20 | `FALL_THROUGH`
<a id="insn-00acd71c"></a> `00acd71c` | `16 81 00 91` | add x22,x8,#0x20 | `FALL_THROUGH`
<a id="insn-00acd720"></a> `00acd720` | `08 00 00 14` | b 0x00acd740 | `UNCONDITIONAL_JUMP`
<a id="insn-00acd724"></a> `00acd724` | `ea 03 08 aa` | mov x10,x8 | `FALL_THROUGH`
<a id="insn-00acd728"></a> `00acd728` | `c9 02 00 f9` | str x9,[x22] | `FALL_THROUGH`
<a id="insn-00acd72c"></a> `00acd72c` | `5f 01 00 f9` | str xzr,[x10] | `FALL_THROUGH`
<a id="insn-00acd730"></a> `00acd730` | `9c c3 00 91` | add x28,x28,#0x30 | `FALL_THROUGH`
<a id="insn-00acd734"></a> `00acd734` | `d6 c2 00 91` | add x22,x22,#0x30 | `FALL_THROUGH`
<a id="insn-00acd738"></a> `00acd738` | `9f 03 17 eb` | cmp x28,x23 | `FALL_THROUGH`
<a id="insn-00acd73c"></a> `00acd73c` | `c0 02 00 54` | b.eq 0x00acd794 | `CONDITIONAL_JUMP`
<a id="insn-00acd740"></a> `00acd740` | `e8 03 1c aa` | mov x8,x28 | `FALL_THROUGH`
<a id="insn-00acd744"></a> `00acd744` | `ea 03 16 aa` | mov x10,x22 | `FALL_THROUGH`
<a id="insn-00acd748"></a> `00acd748` | `09 0d 42 f8` | ldr x9,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-00acd74c"></a> `00acd74c` | `09 ff ff b4` | cbz x9,0x00acd72c | `CONDITIONAL_JUMP`
<a id="insn-00acd750"></a> `00acd750` | `9f 03 09 eb` | cmp x28,x9 | `FALL_THROUGH`
<a id="insn-00acd754"></a> `00acd754` | `81 fe ff 54` | b.ne 0x00acd724 | `CONDITIONAL_JUMP`
<a id="insn-00acd758"></a> `00acd758` | `c1 82 00 d1` | sub x1,x22,#0x20 | `FALL_THROUGH`
<a id="insn-00acd75c"></a> `00acd75c` | `c1 02 00 f9` | str x1,[x22] | `FALL_THROUGH`
<a id="insn-00acd760"></a> `00acd760` | `00 01 40 f9` | ldr x0,[x8] | `FALL_THROUGH`
<a id="insn-00acd764"></a> `00acd764` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00acd768"></a> `00acd768` | `08 0d 40 f9` | ldr x8,[x8, #0x18] | `FALL_THROUGH`
<a id="insn-00acd76c"></a> `00acd76c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00acd770"></a> `00acd770` | `f0 ff ff 17` | b 0x00acd730 | `UNCONDITIONAL_JUMP`
<a id="insn-00acd774"></a> `00acd774` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-00acd778"></a> `00acd778` | `08 04 80 52` | mov w8,#0x20 | `FALL_THROUGH`
<a id="insn-00acd77c"></a> `00acd77c` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-00acd780"></a> `00acd780` | `28 69 68 f8` | ldr x8,[x9, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00acd784"></a> `00acd784` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00acd788"></a> `00acd788` | `39 c3 00 91` | add x25,x25,#0x30 | `FALL_THROUGH`
<a id="insn-00acd78c"></a> `00acd78c` | `3f 03 17 eb` | cmp x25,x23 | `FALL_THROUGH`
<a id="insn-00acd790"></a> `00acd790` | `e0 00 00 54` | b.eq 0x00acd7ac | `CONDITIONAL_JUMP`
<a id="insn-00acd794"></a> `00acd794` | `20 13 40 f9` | ldr x0,[x25, #0x20] | `FALL_THROUGH`
<a id="insn-00acd798"></a> `00acd798` | `3f 03 00 eb` | cmp x25,x0 | `FALL_THROUGH`
<a id="insn-00acd79c"></a> `00acd79c` | `c0 fe ff 54` | b.eq 0x00acd774 | `CONDITIONAL_JUMP`
<a id="insn-00acd7a0"></a> `00acd7a0` | `40 ff ff b4` | cbz x0,0x00acd788 | `CONDITIONAL_JUMP`
<a id="insn-00acd7a4"></a> `00acd7a4` | `08 05 80 52` | mov w8,#0x28 | `FALL_THROUGH`
<a id="insn-00acd7a8"></a> `00acd7a8` | `f5 ff ff 17` | b 0x00acd77c | `UNCONDITIONAL_JUMP`
<a id="insn-00acd7ac"></a> `00acd7ac` | `48 53 1b 9b` | madd x8,x26,x27,x20 | `FALL_THROUGH`
<a id="insn-00acd7b0"></a> `00acd7b0` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00acd7b4"></a> `00acd7b4` | `a9 02 18 cb` | sub x9,x21,x24 | `FALL_THROUGH`
<a id="insn-00acd7b8"></a> `00acd7b8` | `b4 c2 00 91` | add x20,x21,#0x30 | `FALL_THROUGH`
<a id="insn-00acd7bc"></a> `00acd7bc` | `69 52 00 a9` | stp x9,x20,[x19] | `FALL_THROUGH`
<a id="insn-00acd7c0"></a> `00acd7c0` | `68 0a 00 f9` | str x8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00acd7c4"></a> `00acd7c4` | `40 00 00 b4` | cbz x0,0x00acd7cc | `CONDITIONAL_JUMP`
<a id="insn-00acd7c8"></a> `00acd7c8` | `26 36 04 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00acd7cc"></a> `00acd7cc` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00acd7d0"></a> `00acd7d0` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00acd7d4"></a> `00acd7d4` | `f6 57 44 a9` | ldp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00acd7d8"></a> `00acd7d8` | `f8 5f 43 a9` | ldp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00acd7dc"></a> `00acd7dc` | `fa 67 42 a9` | ldp x26,x25,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00acd7e0"></a> `00acd7e0` | `fc 6f 41 a9` | ldp x28,x27,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acd7e4"></a> `00acd7e4` | `fd 7b c6 a8` | ldp x29,x30,[sp], #0x60 | `FALL_THROUGH`
<a id="insn-00acd7e8"></a> `00acd7e8` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00acd7ec"></a> `00acd7ec` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00acd7f0"></a> `00acd7f0` | `04 00 00 94` | bl 0x00acd800 | `UNCONDITIONAL_CALL`
<a id="insn-00acd7f4"></a> `00acd7f4` | `e3 42 e5 97` | bl 0x0041e380 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00acd5fc`](#insn-00acd5fc) 範囲 `[['00acd5fc', '00acd647']]`
  - `CONDITIONAL_JUMP` [`00acd644`](#insn-00acd644) → [`00acd7ec`](#insn-00acd7ec)
  - `FALL_THROUGH` [`00acd644`](#insn-00acd644) → [`00acd648`](#insn-00acd648)
- ブロック [`00acd648`](#insn-00acd648) 範囲 `[['00acd648', '00acd67b']]`
  - `CONDITIONAL_JUMP` [`00acd678`](#insn-00acd678) → [`00acd698`](#insn-00acd698)
  - `FALL_THROUGH` [`00acd678`](#insn-00acd678) → [`00acd67c`](#insn-00acd67c)
- ブロック [`00acd67c`](#insn-00acd67c) 範囲 `[['00acd67c', '00acd683']]`
  - `CONDITIONAL_JUMP` [`00acd680`](#insn-00acd680) → [`00acd7f4`](#insn-00acd7f4)
  - `FALL_THROUGH` [`00acd680`](#insn-00acd680) → [`00acd684`](#insn-00acd684)
- ブロック [`00acd684`](#insn-00acd684) 範囲 `[['00acd684', '00acd697']]`
  - `UNCONDITIONAL_JUMP` [`00acd694`](#insn-00acd694) → [`00acd69c`](#insn-00acd69c)
- ブロック [`00acd698`](#insn-00acd698) 範囲 `[['00acd698', '00acd69b']]`
  - `FALL_THROUGH` [`00acd698`](#insn-00acd698) → [`00acd69c`](#insn-00acd69c)
- ブロック [`00acd69c`](#insn-00acd69c) 範囲 `[['00acd69c', '00acd6af']]`
  - `CONDITIONAL_JUMP` [`00acd6ac`](#insn-00acd6ac) → [`00acd6c0`](#insn-00acd6c0)
  - `FALL_THROUGH` [`00acd6ac`](#insn-00acd6ac) → [`00acd6b0`](#insn-00acd6b0)
- ブロック [`00acd6b0`](#insn-00acd6b0) 範囲 `[['00acd6b0', '00acd6b7']]`
  - `CONDITIONAL_JUMP` [`00acd6b4`](#insn-00acd6b4) → [`00acd6d4`](#insn-00acd6d4)
  - `FALL_THROUGH` [`00acd6b4`](#insn-00acd6b4) → [`00acd6b8`](#insn-00acd6b8)
- ブロック [`00acd6b8`](#insn-00acd6b8) 範囲 `[['00acd6b8', '00acd6bf']]`
  - `UNCONDITIONAL_JUMP` [`00acd6bc`](#insn-00acd6bc) → [`00acd6c4`](#insn-00acd6c4)
- ブロック [`00acd6c0`](#insn-00acd6c0) 範囲 `[['00acd6c0', '00acd6c3']]`
  - `FALL_THROUGH` [`00acd6c0`](#insn-00acd6c0) → [`00acd6c4`](#insn-00acd6c4)
- ブロック [`00acd6c4`](#insn-00acd6c4) 範囲 `[['00acd6c4', '00acd6c7']]`
  - `FALL_THROUGH` [`00acd6c4`](#insn-00acd6c4) → [`00acd6c8`](#insn-00acd6c8)
- ブロック [`00acd6c8`](#insn-00acd6c8) 範囲 `[['00acd6c8', '00acd6cb']]`
  - `FALL_THROUGH` [`00acd6c8`](#insn-00acd6c8) → [`00acd6cc`](#insn-00acd6cc)
- ブロック [`00acd6cc`](#insn-00acd6cc) 範囲 `[['00acd6cc', '00acd6cf']]`
  - `CONDITIONAL_JUMP` [`00acd6cc`](#insn-00acd6cc) → [`00acd6fc`](#insn-00acd6fc)
  - `FALL_THROUGH` [`00acd6cc`](#insn-00acd6cc) → [`00acd6d0`](#insn-00acd6d0)
- ブロック [`00acd6d0`](#insn-00acd6d0) 範囲 `[['00acd6d0', '00acd6d3']]`
  - `UNCONDITIONAL_JUMP` [`00acd6d0`](#insn-00acd6d0) → [`00acd7ac`](#insn-00acd7ac)
- ブロック [`00acd6d4`](#insn-00acd6d4) 範囲 `[['00acd6d4', '00acd6df']]`
  - `FALL_THROUGH` [`00acd6dc`](#insn-00acd6dc) → [`00acd6e0`](#insn-00acd6e0)
- ブロック [`00acd6e0`](#insn-00acd6e0) 範囲 `[['00acd6e0', '00acd6e7']]`
  - `FALL_THROUGH` [`00acd6e4`](#insn-00acd6e4) → [`00acd6e8`](#insn-00acd6e8)
- ブロック [`00acd6e8`](#insn-00acd6e8) 範囲 `[['00acd6e8', '00acd6fb']]`
  - `CONDITIONAL_JUMP` [`00acd6f8`](#insn-00acd6f8) → [`00acd7ac`](#insn-00acd7ac)
  - `FALL_THROUGH` [`00acd6f8`](#insn-00acd6f8) → [`00acd6fc`](#insn-00acd6fc)
- ブロック [`00acd6fc`](#insn-00acd6fc) 範囲 `[['00acd6fc', '00acd70f']]`
  - `FALL_THROUGH` [`00acd70c`](#insn-00acd70c) → [`00acd710`](#insn-00acd710)
- ブロック [`00acd710`](#insn-00acd710) 範囲 `[['00acd710', '00acd723']]`
  - `UNCONDITIONAL_JUMP` [`00acd720`](#insn-00acd720) → [`00acd740`](#insn-00acd740)
- ブロック [`00acd724`](#insn-00acd724) 範囲 `[['00acd724', '00acd727']]`
  - `FALL_THROUGH` [`00acd724`](#insn-00acd724) → [`00acd728`](#insn-00acd728)
- ブロック [`00acd728`](#insn-00acd728) 範囲 `[['00acd728', '00acd72b']]`
  - `FALL_THROUGH` [`00acd728`](#insn-00acd728) → [`00acd72c`](#insn-00acd72c)
- ブロック [`00acd72c`](#insn-00acd72c) 範囲 `[['00acd72c', '00acd72f']]`
  - `FALL_THROUGH` [`00acd72c`](#insn-00acd72c) → [`00acd730`](#insn-00acd730)
- ブロック [`00acd730`](#insn-00acd730) 範囲 `[['00acd730', '00acd73f']]`
  - `CONDITIONAL_JUMP` [`00acd73c`](#insn-00acd73c) → [`00acd794`](#insn-00acd794)
  - `FALL_THROUGH` [`00acd73c`](#insn-00acd73c) → [`00acd740`](#insn-00acd740)
- ブロック [`00acd740`](#insn-00acd740) 範囲 `[['00acd740', '00acd74f']]`
  - `CONDITIONAL_JUMP` [`00acd74c`](#insn-00acd74c) → [`00acd72c`](#insn-00acd72c)
  - `FALL_THROUGH` [`00acd74c`](#insn-00acd74c) → [`00acd750`](#insn-00acd750)
- ブロック [`00acd750`](#insn-00acd750) 範囲 `[['00acd750', '00acd757']]`
  - `CONDITIONAL_JUMP` [`00acd754`](#insn-00acd754) → [`00acd724`](#insn-00acd724)
  - `FALL_THROUGH` [`00acd754`](#insn-00acd754) → [`00acd758`](#insn-00acd758)
- ブロック [`00acd758`](#insn-00acd758) 範囲 `[['00acd758', '00acd773']]`
  - `UNCONDITIONAL_JUMP` [`00acd770`](#insn-00acd770) → [`00acd730`](#insn-00acd730)
- ブロック [`00acd774`](#insn-00acd774) 範囲 `[['00acd774', '00acd77b']]`
  - `FALL_THROUGH` [`00acd778`](#insn-00acd778) → [`00acd77c`](#insn-00acd77c)
- ブロック [`00acd77c`](#insn-00acd77c) 範囲 `[['00acd77c', '00acd787']]`
  - `FALL_THROUGH` [`00acd784`](#insn-00acd784) → [`00acd788`](#insn-00acd788)
- ブロック [`00acd788`](#insn-00acd788) 範囲 `[['00acd788', '00acd793']]`
  - `CONDITIONAL_JUMP` [`00acd790`](#insn-00acd790) → [`00acd7ac`](#insn-00acd7ac)
  - `FALL_THROUGH` [`00acd790`](#insn-00acd790) → [`00acd794`](#insn-00acd794)
- ブロック [`00acd794`](#insn-00acd794) 範囲 `[['00acd794', '00acd79f']]`
  - `CONDITIONAL_JUMP` [`00acd79c`](#insn-00acd79c) → [`00acd774`](#insn-00acd774)
  - `FALL_THROUGH` [`00acd79c`](#insn-00acd79c) → [`00acd7a0`](#insn-00acd7a0)
- ブロック [`00acd7a0`](#insn-00acd7a0) 範囲 `[['00acd7a0', '00acd7a3']]`
  - `CONDITIONAL_JUMP` [`00acd7a0`](#insn-00acd7a0) → [`00acd788`](#insn-00acd788)
  - `FALL_THROUGH` [`00acd7a0`](#insn-00acd7a0) → [`00acd7a4`](#insn-00acd7a4)
- ブロック [`00acd7a4`](#insn-00acd7a4) 範囲 `[['00acd7a4', '00acd7ab']]`
  - `UNCONDITIONAL_JUMP` [`00acd7a8`](#insn-00acd7a8) → [`00acd77c`](#insn-00acd77c)
- ブロック [`00acd7ac`](#insn-00acd7ac) 範囲 `[['00acd7ac', '00acd7c7']]`
  - `CONDITIONAL_JUMP` [`00acd7c4`](#insn-00acd7c4) → [`00acd7cc`](#insn-00acd7cc)
  - `FALL_THROUGH` [`00acd7c4`](#insn-00acd7c4) → [`00acd7c8`](#insn-00acd7c8)
- ブロック [`00acd7c8`](#insn-00acd7c8) 範囲 `[['00acd7c8', '00acd7cb']]`
  - `FALL_THROUGH` [`00acd7c8`](#insn-00acd7c8) → [`00acd7cc`](#insn-00acd7cc)
- ブロック [`00acd7cc`](#insn-00acd7cc) 範囲 `[['00acd7cc', '00acd7eb']]`
- ブロック [`00acd7ec`](#insn-00acd7ec) 範囲 `[['00acd7ec', '00acd7f3']]`
  - `FALL_THROUGH` [`00acd7f0`](#insn-00acd7f0) → [`00acd7f4`](#insn-00acd7f4)
- ブロック [`00acd7f4`](#insn-00acd7f4) 範囲 `[['00acd7f4', '00acd7f7']]`

## 命令位置別の参照

- [`00acd5fc`](#insn-00acd5fc) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acd600`](#insn-00acd600) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acd604`](#insn-00acd604) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acd608`](#insn-00acd608) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acd60c`](#insn-00acd60c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acd610`](#insn-00acd610) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acd644`](#insn-00acd644) → [`00acd7ec`](#insn-00acd7ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acd678`](#insn-00acd678) → [`00acd698`](#insn-00acd698) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acd680`](#insn-00acd680) → [`00acd7f4`](#insn-00acd7f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acd68c`](#insn-00acd68c) → [`00bdb040`](../00bdb/00bdb040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb040` · 推定シンボル `None` · 推定型 `None`
- [`00acd694`](#insn-00acd694) → [`00acd69c`](#insn-00acd69c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acd6ac`](#insn-00acd6ac) → [`00acd6c0`](#insn-00acd6c0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acd6b4`](#insn-00acd6b4) → [`00acd6d4`](#insn-00acd6d4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acd6bc`](#insn-00acd6bc) → [`00acd6c4`](#insn-00acd6c4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acd6cc`](#insn-00acd6cc) → [`00acd6fc`](#insn-00acd6fc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acd6d0`](#insn-00acd6d0) → [`00acd7ac`](#insn-00acd7ac) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acd6f8`](#insn-00acd6f8) → [`00acd7ac`](#insn-00acd7ac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acd720`](#insn-00acd720) → [`00acd740`](#insn-00acd740) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acd73c`](#insn-00acd73c) → [`00acd794`](#insn-00acd794) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acd74c`](#insn-00acd74c) → [`00acd72c`](#insn-00acd72c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acd754`](#insn-00acd754) → [`00acd724`](#insn-00acd724) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acd770`](#insn-00acd770) → [`00acd730`](#insn-00acd730) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acd790`](#insn-00acd790) → [`00acd7ac`](#insn-00acd7ac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acd79c`](#insn-00acd79c) → [`00acd774`](#insn-00acd774) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acd7a0`](#insn-00acd7a0) → [`00acd788`](#insn-00acd788) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acd7a8`](#insn-00acd7a8) → [`00acd77c`](#insn-00acd77c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acd7c4`](#insn-00acd7c4) → [`00acd7cc`](#insn-00acd7cc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acd7c8`](#insn-00acd7c8) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00acd7d0`](#insn-00acd7d0) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acd7d4`](#insn-00acd7d4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acd7d8`](#insn-00acd7d8) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acd7dc`](#insn-00acd7dc) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acd7e0`](#insn-00acd7e0) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acd7e4`](#insn-00acd7e4) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acd7f0`](#insn-00acd7f0) → [`00acd800`](00acd800.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00acd800` · 推定シンボル `None` · 推定型 `None`
- [`00acd7f4`](#insn-00acd7f4) → [`0041e380`](../0041e/0041e380.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0041e380` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00acd5fc`](#insn-00acd5fc)

~~~json
{
  "source": "00acd5fc",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acd600`](#insn-00acd600)

~~~json
{
  "source": "00acd600",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acd604`](#insn-00acd604)

~~~json
{
  "source": "00acd604",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acd608`](#insn-00acd608)

~~~json
{
  "source": "00acd608",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acd60c`](#insn-00acd60c)

~~~json
{
  "source": "00acd60c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acd610`](#insn-00acd610)

~~~json
{
  "source": "00acd610",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acd644`](#insn-00acd644)

~~~json
{
  "source": "00acd644",
  "target": "00acd7ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acd678`](#insn-00acd678)

~~~json
{
  "source": "00acd678",
  "target": "00acd698",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acd680`](#insn-00acd680)

~~~json
{
  "source": "00acd680",
  "target": "00acd7f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acd68c`](#insn-00acd68c)

~~~json
{
  "source": "00acd68c",
  "target": "00bdb040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acd694`](#insn-00acd694)

~~~json
{
  "source": "00acd694",
  "target": "00acd69c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acd6ac`](#insn-00acd6ac)

~~~json
{
  "source": "00acd6ac",
  "target": "00acd6c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acd6b4`](#insn-00acd6b4)

~~~json
{
  "source": "00acd6b4",
  "target": "00acd6d4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acd6bc`](#insn-00acd6bc)

~~~json
{
  "source": "00acd6bc",
  "target": "00acd6c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acd6cc`](#insn-00acd6cc)

~~~json
{
  "source": "00acd6cc",
  "target": "00acd6fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acd6d0`](#insn-00acd6d0)

~~~json
{
  "source": "00acd6d0",
  "target": "00acd7ac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acd6f8`](#insn-00acd6f8)

~~~json
{
  "source": "00acd6f8",
  "target": "00acd7ac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acd720`](#insn-00acd720)

~~~json
{
  "source": "00acd720",
  "target": "00acd740",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acd73c`](#insn-00acd73c)

~~~json
{
  "source": "00acd73c",
  "target": "00acd794",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acd74c`](#insn-00acd74c)

~~~json
{
  "source": "00acd74c",
  "target": "00acd72c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acd754`](#insn-00acd754)

~~~json
{
  "source": "00acd754",
  "target": "00acd724",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acd770`](#insn-00acd770)

~~~json
{
  "source": "00acd770",
  "target": "00acd730",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acd790`](#insn-00acd790)

~~~json
{
  "source": "00acd790",
  "target": "00acd7ac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acd79c`](#insn-00acd79c)

~~~json
{
  "source": "00acd79c",
  "target": "00acd774",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acd7a0`](#insn-00acd7a0)

~~~json
{
  "source": "00acd7a0",
  "target": "00acd788",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acd7a8`](#insn-00acd7a8)

~~~json
{
  "source": "00acd7a8",
  "target": "00acd77c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acd7c4`](#insn-00acd7c4)

~~~json
{
  "source": "00acd7c4",
  "target": "00acd7cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acd7c8`](#insn-00acd7c8)

~~~json
{
  "source": "00acd7c8",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acd7d0`](#insn-00acd7d0)

~~~json
{
  "source": "00acd7d0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acd7d4`](#insn-00acd7d4)

~~~json
{
  "source": "00acd7d4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acd7d8`](#insn-00acd7d8)

~~~json
{
  "source": "00acd7d8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acd7dc`](#insn-00acd7dc)

~~~json
{
  "source": "00acd7dc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acd7e0`](#insn-00acd7e0)

~~~json
{
  "source": "00acd7e0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acd7e4`](#insn-00acd7e4)

~~~json
{
  "source": "00acd7e4",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acd7f0`](#insn-00acd7f0)

~~~json
{
  "source": "00acd7f0",
  "target": "00acd800",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acd7f4`](#insn-00acd7f4)

~~~json
{
  "source": "00acd7f4",
  "target": "0041e380",
  "target_space": "ram",
  "resolution": "function"
}
~~~
