# 00afd2ac

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00afd268`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afd268.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0066.md#compare-6abf83cdd9e31cbb998be4fb910d4df8)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b5d030`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5d/00b5d030.md) · 移動量 `+0x5fd84`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0061.md#compare-14b9234d06aadf588e2f4e9d3a91f453)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afd2ac",
  "name": "FUN_00afd2ac",
  "size": 480,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e35b21d1eb9576f80ba0bb4126a497039eefeb8770c72d9b303f7a85c2b36504",
  "source_text_sha256": "e35b21d1eb9576f80ba0bb4126a497039eefeb8770c72d9b303f7a85c2b36504",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afd2ac",
        "00afd48b"
      ]
    ],
    "bytes_sha256": "1bbd7add79a23c4a7c1d4c38ae9961d7ca5aa80ce260c96943105289928a025c",
    "instruction_count": 120,
    "instruction_bytes": 480,
    "body_bytes": 480,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00afd108](../00afd/00afd108.md)
- [00afd23c](../00afd/00afd23c.md)
- [00afdc48](../00afd/00afdc48.md)
- [00afddf8](../00afd/00afddf8.md)

## 呼び出し先

- [00bdb130](../00bdb/00bdb130.md)
- [00bdb7a0](../00bdb/00bdb7a0.md)
- [00bded80](../00bde/00bded80.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 3503 bytes

~~~c

void FUN_00afd2ac(undefined8 *param_1,byte *param_2,byte *param_3)

{
  ulong uVar1;
  byte bVar2;
  byte bVar3;
  int iVar4;
  int iVar5;
  uint uVar6;
  undefined8 extraout_x1;
  undefined8 uVar7;
  uint uVar8;
  byte *pbVar9;
  int iVar10;
  int iVar11;
  ulong uVar12;
  byte *pbVar13;
  ulong uVar14;
  undefined8 extraout_x17;
  undefined8 uVar15;
  
                    /* try { // try from 00afd2c8 to 00bfd373 has its CatchHandler @ 00af5650 */
  *param_1 = 0;
  param_1[1] = 0;
  iVar4 = (int)((ulong)((long)param_3 - (long)param_2) >> 3) * -0x55555555;
  param_1[2] = 0;
  if (iVar4 != 0) {
    iVar4 = iVar4 + -1;
    iVar5 = __strlen_chk(&DAT_0029583d,2);
    if (param_2 == param_3) {
                    /* try { // try from 00afd374 to 00bfd3fb has its CatchHandler @ 00b00180 */
      _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE7reserveEm
                (param_1,(long)(iVar4 * iVar5));
      return;
    }
    uVar1 = (((long)param_3 - (long)param_2) - 0x18U) / 0x18 + 1;
    if (uVar1 < 2) {
      iVar10 = 0;
      bVar2 = *param_2;
      pbVar9 = param_2;
      if ((bVar2 & 1) != 0) goto LAB_00afd354;
      goto LAB_00afd338;
    }
    uVar12 = uVar1 & 0x1ffffffffffffffe;
    iVar11 = 0;
    iVar10 = 0;
    pbVar9 = param_2 + uVar12 * 0x18;
    pbVar13 = param_2 + 0x20;
    uVar7 = extraout_x1;
    uVar14 = uVar12;
    uVar15 = extraout_x17;
    do {
      bVar2 = pbVar13[-0x20];
      bVar3 = pbVar13[-8];
      if ((bVar2 & 1) != 0) {
        uVar15 = *(undefined8 *)(pbVar13 + -0x18);
      }
      if ((bVar3 & 1) != 0) {
        uVar7 = *(undefined8 *)pbVar13;
      }
      uVar8 = (uint)(bVar2 >> 1);
      if ((bVar2 & 1) != 0) {
        uVar8 = (uint)uVar15;
      }
      uVar6 = (uint)(bVar3 >> 1);
      if ((bVar3 & 1) != 0) {
        uVar6 = (uint)uVar7;
      }
      iVar11 = iVar11 + uVar8;
      uVar14 = uVar14 - 2;
      iVar10 = iVar10 + uVar6;
      pbVar13 = pbVar13 + 0x30;
    } while (uVar14 != 0);
    iVar10 = iVar10 + iVar11;
    if (uVar1 != uVar12) {
      do {
        bVar2 = *pbVar9;
        if ((bVar2 & 1) == 0) {
LAB_00afd338:
          uVar8 = (uint)(bVar2 >> 1);
        }
        else {
LAB_00afd354:
          uVar8 = (uint)*(undefined8 *)(pbVar9 + 8);
        }
        pbVar9 = pbVar9 + 0x18;
        iVar10 = iVar10 + uVar8;
      } while (param_3 != pbVar9);
    }
                    /* try { // try from 00afd3fc to 00bfdb2f has its CatchHandler @ 00af5650 */
    _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE7reserveEm
              (param_1,(long)(iVar10 + iVar4 * iVar5));
    if (param_2 != param_3) {
      uVar1 = *(ulong *)(param_2 + 8);
      pbVar9 = *(byte **)(param_2 + 0x10);
      if ((*param_2 & 1) == 0) {
        pbVar9 = param_2 + 1;
        uVar1 = (ulong)(*param_2 >> 1);
      }
      _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKcm
                (param_1,pbVar9,uVar1);
      while (param_2 = param_2 + 0x18, param_2 != param_3) {
        _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKcm
                  (param_1,&DAT_0029583d,1);
        uVar1 = *(ulong *)(param_2 + 8);
        pbVar9 = *(byte **)(param_2 + 0x10);
        if ((*param_2 & 1) == 0) {
          pbVar9 = param_2 + 1;
          uVar1 = (ulong)(*param_2 >> 1);
        }
        _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKcm
                  (param_1,pbVar9,uVar1);
      }
    }
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afd2ac"></a> `00afd2ac` | `f7 0f 1c f8` | str x23,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00afd2b0"></a> `00afd2b0` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afd2b4"></a> `00afd2b4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afd2b8"></a> `00afd2b8` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00afd2bc"></a> `00afd2bc` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00afd2c0"></a> `00afd2c0` | `37 00 00 cb` | sub x23,x1,x0 | `FALL_THROUGH`
<a id="insn-00afd2c4"></a> `00afd2c4` | `69 55 95 52` | mov w9,#0xaaab | `FALL_THROUGH`
<a id="insn-00afd2c8"></a> `00afd2c8` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00afd2cc"></a> `00afd2cc` | `1f 7d 00 a9` | stp xzr,xzr,[x8] | `FALL_THROUGH`
<a id="insn-00afd2d0"></a> `00afd2d0` | `e8 fe 43 d3` | lsr x8,x23,#0x3 | `FALL_THROUGH`
<a id="insn-00afd2d4"></a> `00afd2d4` | `49 55 b5 72` | movk w9,#0xaaaa, LSL #16 | `FALL_THROUGH`
<a id="insn-00afd2d8"></a> `00afd2d8` | `08 7d 09 1b` | mul w8,w8,w9 | `FALL_THROUGH`
<a id="insn-00afd2dc"></a> `00afd2dc` | `7f 0a 00 f9` | str xzr,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00afd2e0"></a> `00afd2e0` | `c8 0c 00 34` | cbz w8,0x00afd478 | `CONDITIONAL_JUMP`
<a id="insn-00afd2e4"></a> `00afd2e4` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00afd2e8"></a> `00afd2e8` | `c0 bc ff 90` | adrp x0,0x295000 | `FALL_THROUGH`
<a id="insn-00afd2ec"></a> `00afd2ec` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00afd2f0"></a> `00afd2f0` | `00 f4 20 91` | add x0,x0,#0x83d | `FALL_THROUGH`
<a id="insn-00afd2f4"></a> `00afd2f4` | `41 00 80 52` | mov w1,#0x2 | `FALL_THROUGH`
<a id="insn-00afd2f8"></a> `00afd2f8` | `16 05 00 51` | sub w22,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00afd2fc"></a> `00afd2fc` | `a1 86 03 94` | bl 0x00bded80 | `UNCONDITIONAL_CALL`
<a id="insn-00afd300"></a> `00afd300` | `bf 02 14 eb` | cmp x21,x20 | `FALL_THROUGH`
<a id="insn-00afd304"></a> `00afd304` | `c0 02 00 54` | b.eq 0x00afd35c | `CONDITIONAL_JUMP`
<a id="insn-00afd308"></a> `00afd308` | `e9 f3 01 b2` | orr x9,xzr,#-0x5555555555555556 | `FALL_THROUGH`
<a id="insn-00afd30c"></a> `00afd30c` | `e8 62 00 d1` | sub x8,x23,#0x18 | `FALL_THROUGH`
<a id="insn-00afd310"></a> `00afd310` | `69 55 95 f2` | movk x9,#0xaaab | `FALL_THROUGH`
<a id="insn-00afd314"></a> `00afd314` | `08 7d c9 9b` | umulh x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00afd318"></a> `00afd318` | `08 fd 44 d3` | lsr x8,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00afd31c"></a> `00afd31c` | `09 05 00 91` | add x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00afd320"></a> `00afd320` | `3f 05 00 f1` | cmp x9,#0x1 | `FALL_THROUGH`
<a id="insn-00afd324"></a> `00afd324` | `c8 02 00 54` | b.hi 0x00afd37c | `CONDITIONAL_JUMP`
<a id="insn-00afd328"></a> `00afd328` | `e9 03 1f 2a` | mov w9,wzr | `FALL_THROUGH`
<a id="insn-00afd32c"></a> `00afd32c` | `e8 03 15 aa` | mov x8,x21 | `FALL_THROUGH`
<a id="insn-00afd330"></a> `00afd330` | `0a 01 40 39` | ldrb w10,[x8] | `FALL_THROUGH`
<a id="insn-00afd334"></a> `00afd334` | `0a 01 00 37` | tbnz w10,#0x0,0x00afd354 | `CONDITIONAL_JUMP`
<a id="insn-00afd338"></a> `00afd338` | `4a fd 41 d3` | lsr x10,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00afd33c"></a> `00afd33c` | `08 61 00 91` | add x8,x8,#0x18 | `FALL_THROUGH`
<a id="insn-00afd340"></a> `00afd340` | `9f 02 08 eb` | cmp x20,x8 | `FALL_THROUGH`
<a id="insn-00afd344"></a> `00afd344` | `29 01 0a 0b` | add w9,w9,w10 | `FALL_THROUGH`
<a id="insn-00afd348"></a> `00afd348` | `40 05 00 54` | b.eq 0x00afd3f0 | `CONDITIONAL_JUMP`
<a id="insn-00afd34c"></a> `00afd34c` | `0a 01 40 39` | ldrb w10,[x8] | `FALL_THROUGH`
<a id="insn-00afd350"></a> `00afd350` | `4a ff 07 36` | tbz w10,#0x0,0x00afd338 | `CONDITIONAL_JUMP`
<a id="insn-00afd354"></a> `00afd354` | `0a 05 40 f9` | ldr x10,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00afd358"></a> `00afd358` | `f9 ff ff 17` | b 0x00afd33c | `UNCONDITIONAL_JUMP`
<a id="insn-00afd35c"></a> `00afd35c` | `c8 7e 00 1b` | mul w8,w22,w0 | `FALL_THROUGH`
<a id="insn-00afd360"></a> `00afd360` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00afd364"></a> `00afd364` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00afd368"></a> `00afd368` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afd36c"></a> `00afd36c` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afd370"></a> `00afd370` | `01 7d 40 93` | sxtw x1,w8 | `FALL_THROUGH`
<a id="insn-00afd374"></a> `00afd374` | `f7 07 44 f8` | ldr x23,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00afd378"></a> `00afd378` | `0a 79 03 14` | b 0x00bdb7a0 | `CALL_TERMINATOR`
<a id="insn-00afd37c"></a> `00afd37c` | `2c ed 7f 92` | and x12,x9,#0x1ffffffffffffffe | `FALL_THROUGH`
<a id="insn-00afd380"></a> `00afd380` | `08 03 80 52` | mov w8,#0x18 | `FALL_THROUGH`
<a id="insn-00afd384"></a> `00afd384` | `ea 03 1f 2a` | mov w10,wzr | `FALL_THROUGH`
<a id="insn-00afd388"></a> `00afd388` | `eb 03 1f 2a` | mov w11,wzr | `FALL_THROUGH`
<a id="insn-00afd38c"></a> `00afd38c` | `88 55 08 9b` | madd x8,x12,x8,x21 | `FALL_THROUGH`
<a id="insn-00afd390"></a> `00afd390` | `ad 82 00 91` | add x13,x21,#0x20 | `FALL_THROUGH`
<a id="insn-00afd394"></a> `00afd394` | `ee 03 0c aa` | mov x14,x12 | `FALL_THROUGH`
<a id="insn-00afd398"></a> `00afd398` | `0c 00 00 14` | b 0x00afd3c8 | `UNCONDITIONAL_JUMP`
<a id="insn-00afd39c"></a> `00afd39c` | `e2 fd 41 d3` | lsr x2,x15,#0x1 | `FALL_THROUGH`
<a id="insn-00afd3a0"></a> `00afd3a0` | `ff 01 00 72` | tst w15,#0x1 | `FALL_THROUGH`
<a id="insn-00afd3a4"></a> `00afd3a4` | `03 fe 41 d3` | lsr x3,x16,#0x1 | `FALL_THROUGH`
<a id="insn-00afd3a8"></a> `00afd3a8` | `4f 00 91 1a` | csel w15,w2,w17,eq | `FALL_THROUGH`
<a id="insn-00afd3ac"></a> `00afd3ac` | `1f 02 00 72` | tst w16,#0x1 | `FALL_THROUGH`
<a id="insn-00afd3b0"></a> `00afd3b0` | `70 00 81 1a` | csel w16,w3,w1,eq | `FALL_THROUGH`
<a id="insn-00afd3b4"></a> `00afd3b4` | `4a 01 0f 0b` | add w10,w10,w15 | `FALL_THROUGH`
<a id="insn-00afd3b8"></a> `00afd3b8` | `ce 09 00 f1` | subs x14,x14,#0x2 | `FALL_THROUGH`
<a id="insn-00afd3bc"></a> `00afd3bc` | `6b 01 10 0b` | add w11,w11,w16 | `FALL_THROUGH`
<a id="insn-00afd3c0"></a> `00afd3c0` | `ad c1 00 91` | add x13,x13,#0x30 | `FALL_THROUGH`
<a id="insn-00afd3c4"></a> `00afd3c4` | `00 01 00 54` | b.eq 0x00afd3e4 | `CONDITIONAL_JUMP`
<a id="insn-00afd3c8"></a> `00afd3c8` | `af 01 5e 38` | ldurb w15,[x13, #-0x20] | `FALL_THROUGH`
<a id="insn-00afd3cc"></a> `00afd3cc` | `b0 81 5f 38` | ldurb w16,[x13, #-0x8] | `FALL_THROUGH`
<a id="insn-00afd3d0"></a> `00afd3d0` | `4f 00 00 36` | tbz w15,#0x0,0x00afd3d8 | `CONDITIONAL_JUMP`
<a id="insn-00afd3d4"></a> `00afd3d4` | `b1 81 5e f8` | ldur x17,[x13, #-0x18] | `FALL_THROUGH`
<a id="insn-00afd3d8"></a> `00afd3d8` | `30 fe 07 36` | tbz w16,#0x0,0x00afd39c | `CONDITIONAL_JUMP`
<a id="insn-00afd3dc"></a> `00afd3dc` | `a1 01 40 f9` | ldr x1,[x13] | `FALL_THROUGH`
<a id="insn-00afd3e0"></a> `00afd3e0` | `ef ff ff 17` | b 0x00afd39c | `UNCONDITIONAL_JUMP`
<a id="insn-00afd3e4"></a> `00afd3e4` | `3f 01 0c eb` | cmp x9,x12 | `FALL_THROUGH`
<a id="insn-00afd3e8"></a> `00afd3e8` | `69 01 0a 0b` | add w9,w11,w10 | `FALL_THROUGH`
<a id="insn-00afd3ec"></a> `00afd3ec` | `01 fb ff 54` | b.ne 0x00afd34c | `CONDITIONAL_JUMP`
<a id="insn-00afd3f0"></a> `00afd3f0` | `c8 26 00 1b` | madd w8,w22,w0,w9 | `FALL_THROUGH`
<a id="insn-00afd3f4"></a> `00afd3f4` | `01 7d 40 93` | sxtw x1,w8 | `FALL_THROUGH`
<a id="insn-00afd3f8"></a> `00afd3f8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00afd3fc"></a> `00afd3fc` | `e9 78 03 94` | bl 0x00bdb7a0 | `UNCONDITIONAL_CALL`
<a id="insn-00afd400"></a> `00afd400` | `bf 02 14 eb` | cmp x21,x20 | `FALL_THROUGH`
<a id="insn-00afd404"></a> `00afd404` | `a0 03 00 54` | b.eq 0x00afd478 | `CONDITIONAL_JUMP`
<a id="insn-00afd408"></a> `00afd408` | `a8 02 40 39` | ldrb w8,[x21] | `FALL_THROUGH`
<a id="insn-00afd40c"></a> `00afd40c` | `aa a6 40 a9` | ldp x10,x9,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00afd410"></a> `00afd410` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00afd414"></a> `00afd414` | `0b fd 41 d3` | lsr x11,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00afd418"></a> `00afd418` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00afd41c"></a> `00afd41c` | `21 15 95 9a` | csinc x1,x9,x21,ne | `FALL_THROUGH`
<a id="insn-00afd420"></a> `00afd420` | `62 01 8a 9a` | csel x2,x11,x10,eq | `FALL_THROUGH`
<a id="insn-00afd424"></a> `00afd424` | `43 77 03 94` | bl 0x00bdb130 | `UNCONDITIONAL_CALL`
<a id="insn-00afd428"></a> `00afd428` | `b6 62 00 91` | add x22,x21,#0x18 | `FALL_THROUGH`
<a id="insn-00afd42c"></a> `00afd42c` | `df 02 14 eb` | cmp x22,x20 | `FALL_THROUGH`
<a id="insn-00afd430"></a> `00afd430` | `40 02 00 54` | b.eq 0x00afd478 | `CONDITIONAL_JUMP`
<a id="insn-00afd434"></a> `00afd434` | `d5 bc ff 90` | adrp x21,0x295000 | `FALL_THROUGH`
<a id="insn-00afd438"></a> `00afd438` | `b5 f6 20 91` | add x21,x21,#0x83d | `FALL_THROUGH`
<a id="insn-00afd43c"></a> `00afd43c` | `22 00 80 52` | mov w2,#0x1 | `FALL_THROUGH`
<a id="insn-00afd440"></a> `00afd440` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00afd444"></a> `00afd444` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00afd448"></a> `00afd448` | `3a 77 03 94` | bl 0x00bdb130 | `UNCONDITIONAL_CALL`
<a id="insn-00afd44c"></a> `00afd44c` | `c8 02 40 39` | ldrb w8,[x22] | `FALL_THROUGH`
<a id="insn-00afd450"></a> `00afd450` | `ca a6 40 a9` | ldp x10,x9,[x22, #0x8] | `FALL_THROUGH`
<a id="insn-00afd454"></a> `00afd454` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00afd458"></a> `00afd458` | `0b fd 41 d3` | lsr x11,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00afd45c"></a> `00afd45c` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00afd460"></a> `00afd460` | `21 15 96 9a` | csinc x1,x9,x22,ne | `FALL_THROUGH`
<a id="insn-00afd464"></a> `00afd464` | `62 01 8a 9a` | csel x2,x11,x10,eq | `FALL_THROUGH`
<a id="insn-00afd468"></a> `00afd468` | `32 77 03 94` | bl 0x00bdb130 | `UNCONDITIONAL_CALL`
<a id="insn-00afd46c"></a> `00afd46c` | `d6 62 00 91` | add x22,x22,#0x18 | `FALL_THROUGH`
<a id="insn-00afd470"></a> `00afd470` | `df 02 14 eb` | cmp x22,x20 | `FALL_THROUGH`
<a id="insn-00afd474"></a> `00afd474` | `41 fe ff 54` | b.ne 0x00afd43c | `CONDITIONAL_JUMP`
<a id="insn-00afd478"></a> `00afd478` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00afd47c"></a> `00afd47c` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afd480"></a> `00afd480` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afd484"></a> `00afd484` | `f7 07 44 f8` | ldr x23,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00afd488"></a> `00afd488` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afd2ac`](#insn-00afd2ac) 範囲 `[['00afd2ac', '00afd2c7']]`
  - `FALL_THROUGH` [`00afd2c4`](#insn-00afd2c4) → [`00afd2c8`](#insn-00afd2c8)
- ブロック [`00afd2c8`](#insn-00afd2c8) 範囲 `[['00afd2c8', '00afd2e3']]`
  - `CONDITIONAL_JUMP` [`00afd2e0`](#insn-00afd2e0) → [`00afd478`](#insn-00afd478)
  - `FALL_THROUGH` [`00afd2e0`](#insn-00afd2e0) → [`00afd2e4`](#insn-00afd2e4)
- ブロック [`00afd2e4`](#insn-00afd2e4) 範囲 `[['00afd2e4', '00afd307']]`
  - `CONDITIONAL_JUMP` [`00afd304`](#insn-00afd304) → [`00afd35c`](#insn-00afd35c)
  - `FALL_THROUGH` [`00afd304`](#insn-00afd304) → [`00afd308`](#insn-00afd308)
- ブロック [`00afd308`](#insn-00afd308) 範囲 `[['00afd308', '00afd327']]`
  - `CONDITIONAL_JUMP` [`00afd324`](#insn-00afd324) → [`00afd37c`](#insn-00afd37c)
  - `FALL_THROUGH` [`00afd324`](#insn-00afd324) → [`00afd328`](#insn-00afd328)
- ブロック [`00afd328`](#insn-00afd328) 範囲 `[['00afd328', '00afd337']]`
  - `CONDITIONAL_JUMP` [`00afd334`](#insn-00afd334) → [`00afd354`](#insn-00afd354)
  - `FALL_THROUGH` [`00afd334`](#insn-00afd334) → [`00afd338`](#insn-00afd338)
- ブロック [`00afd338`](#insn-00afd338) 範囲 `[['00afd338', '00afd33b']]`
  - `FALL_THROUGH` [`00afd338`](#insn-00afd338) → [`00afd33c`](#insn-00afd33c)
- ブロック [`00afd33c`](#insn-00afd33c) 範囲 `[['00afd33c', '00afd34b']]`
  - `CONDITIONAL_JUMP` [`00afd348`](#insn-00afd348) → [`00afd3f0`](#insn-00afd3f0)
  - `FALL_THROUGH` [`00afd348`](#insn-00afd348) → [`00afd34c`](#insn-00afd34c)
- ブロック [`00afd34c`](#insn-00afd34c) 範囲 `[['00afd34c', '00afd353']]`
  - `CONDITIONAL_JUMP` [`00afd350`](#insn-00afd350) → [`00afd338`](#insn-00afd338)
  - `FALL_THROUGH` [`00afd350`](#insn-00afd350) → [`00afd354`](#insn-00afd354)
- ブロック [`00afd354`](#insn-00afd354) 範囲 `[['00afd354', '00afd35b']]`
  - `UNCONDITIONAL_JUMP` [`00afd358`](#insn-00afd358) → [`00afd33c`](#insn-00afd33c)
- ブロック [`00afd35c`](#insn-00afd35c) 範囲 `[['00afd35c', '00afd373']]`
  - `FALL_THROUGH` [`00afd370`](#insn-00afd370) → [`00afd374`](#insn-00afd374)
- ブロック [`00afd374`](#insn-00afd374) 範囲 `[['00afd374', '00afd37b']]`
- ブロック [`00afd37c`](#insn-00afd37c) 範囲 `[['00afd37c', '00afd39b']]`
  - `UNCONDITIONAL_JUMP` [`00afd398`](#insn-00afd398) → [`00afd3c8`](#insn-00afd3c8)
- ブロック [`00afd39c`](#insn-00afd39c) 範囲 `[['00afd39c', '00afd3c7']]`
  - `CONDITIONAL_JUMP` [`00afd3c4`](#insn-00afd3c4) → [`00afd3e4`](#insn-00afd3e4)
  - `FALL_THROUGH` [`00afd3c4`](#insn-00afd3c4) → [`00afd3c8`](#insn-00afd3c8)
- ブロック [`00afd3c8`](#insn-00afd3c8) 範囲 `[['00afd3c8', '00afd3d3']]`
  - `CONDITIONAL_JUMP` [`00afd3d0`](#insn-00afd3d0) → [`00afd3d8`](#insn-00afd3d8)
  - `FALL_THROUGH` [`00afd3d0`](#insn-00afd3d0) → [`00afd3d4`](#insn-00afd3d4)
- ブロック [`00afd3d4`](#insn-00afd3d4) 範囲 `[['00afd3d4', '00afd3d7']]`
  - `FALL_THROUGH` [`00afd3d4`](#insn-00afd3d4) → [`00afd3d8`](#insn-00afd3d8)
- ブロック [`00afd3d8`](#insn-00afd3d8) 範囲 `[['00afd3d8', '00afd3db']]`
  - `CONDITIONAL_JUMP` [`00afd3d8`](#insn-00afd3d8) → [`00afd39c`](#insn-00afd39c)
  - `FALL_THROUGH` [`00afd3d8`](#insn-00afd3d8) → [`00afd3dc`](#insn-00afd3dc)
- ブロック [`00afd3dc`](#insn-00afd3dc) 範囲 `[['00afd3dc', '00afd3e3']]`
  - `UNCONDITIONAL_JUMP` [`00afd3e0`](#insn-00afd3e0) → [`00afd39c`](#insn-00afd39c)
- ブロック [`00afd3e4`](#insn-00afd3e4) 範囲 `[['00afd3e4', '00afd3ef']]`
  - `CONDITIONAL_JUMP` [`00afd3ec`](#insn-00afd3ec) → [`00afd34c`](#insn-00afd34c)
  - `FALL_THROUGH` [`00afd3ec`](#insn-00afd3ec) → [`00afd3f0`](#insn-00afd3f0)
- ブロック [`00afd3f0`](#insn-00afd3f0) 範囲 `[['00afd3f0', '00afd3fb']]`
  - `FALL_THROUGH` [`00afd3f8`](#insn-00afd3f8) → [`00afd3fc`](#insn-00afd3fc)
- ブロック [`00afd3fc`](#insn-00afd3fc) 範囲 `[['00afd3fc', '00afd407']]`
  - `CONDITIONAL_JUMP` [`00afd404`](#insn-00afd404) → [`00afd478`](#insn-00afd478)
  - `FALL_THROUGH` [`00afd404`](#insn-00afd404) → [`00afd408`](#insn-00afd408)
- ブロック [`00afd408`](#insn-00afd408) 範囲 `[['00afd408', '00afd433']]`
  - `CONDITIONAL_JUMP` [`00afd430`](#insn-00afd430) → [`00afd478`](#insn-00afd478)
  - `FALL_THROUGH` [`00afd430`](#insn-00afd430) → [`00afd434`](#insn-00afd434)
- ブロック [`00afd434`](#insn-00afd434) 範囲 `[['00afd434', '00afd43b']]`
  - `FALL_THROUGH` [`00afd438`](#insn-00afd438) → [`00afd43c`](#insn-00afd43c)
- ブロック [`00afd43c`](#insn-00afd43c) 範囲 `[['00afd43c', '00afd477']]`
  - `CONDITIONAL_JUMP` [`00afd474`](#insn-00afd474) → [`00afd43c`](#insn-00afd43c)
  - `FALL_THROUGH` [`00afd474`](#insn-00afd474) → [`00afd478`](#insn-00afd478)
- ブロック [`00afd478`](#insn-00afd478) 範囲 `[['00afd478', '00afd48b']]`

## 命令位置別の参照

- [`00afd2ac`](#insn-00afd2ac) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afd2b0`](#insn-00afd2b0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afd2b4`](#insn-00afd2b4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afd2b8`](#insn-00afd2b8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afd2e0`](#insn-00afd2e0) → [`00afd478`](#insn-00afd478) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afd2f0`](#insn-00afd2f0) → `0029583d`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afd2fc`](#insn-00afd2fc) → [`00bded80`](../00bde/00bded80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bded80` · 推定シンボル `None` · 推定型 `None`
- [`00afd304`](#insn-00afd304) → [`00afd35c`](#insn-00afd35c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afd324`](#insn-00afd324) → [`00afd37c`](#insn-00afd37c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afd334`](#insn-00afd334) → [`00afd354`](#insn-00afd354) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afd348`](#insn-00afd348) → [`00afd3f0`](#insn-00afd3f0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afd350`](#insn-00afd350) → [`00afd338`](#insn-00afd338) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afd358`](#insn-00afd358) → [`00afd33c`](#insn-00afd33c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afd364`](#insn-00afd364) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afd368`](#insn-00afd368) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afd36c`](#insn-00afd36c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afd378`](#insn-00afd378) → [`00bdb7a0`](../00bdb/00bdb7a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb7a0` · 推定シンボル `None` · 推定型 `None`
- [`00afd398`](#insn-00afd398) → [`00afd3c8`](#insn-00afd3c8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afd3c4`](#insn-00afd3c4) → [`00afd3e4`](#insn-00afd3e4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afd3d0`](#insn-00afd3d0) → [`00afd3d8`](#insn-00afd3d8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afd3d8`](#insn-00afd3d8) → [`00afd39c`](#insn-00afd39c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afd3e0`](#insn-00afd3e0) → [`00afd39c`](#insn-00afd39c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afd3ec`](#insn-00afd3ec) → [`00afd34c`](#insn-00afd34c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afd3fc`](#insn-00afd3fc) → [`00bdb7a0`](../00bdb/00bdb7a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb7a0` · 推定シンボル `None` · 推定型 `None`
- [`00afd404`](#insn-00afd404) → [`00afd478`](#insn-00afd478) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afd424`](#insn-00afd424) → [`00bdb130`](../00bdb/00bdb130.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb130` · 推定シンボル `None` · 推定型 `None`
- [`00afd430`](#insn-00afd430) → [`00afd478`](#insn-00afd478) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afd444`](#insn-00afd444) → `0029583d`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afd448`](#insn-00afd448) → [`00bdb130`](../00bdb/00bdb130.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb130` · 推定シンボル `None` · 推定型 `None`
- [`00afd468`](#insn-00afd468) → [`00bdb130`](../00bdb/00bdb130.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb130` · 推定シンボル `None` · 推定型 `None`
- [`00afd474`](#insn-00afd474) → [`00afd43c`](#insn-00afd43c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afd478`](#insn-00afd478) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afd47c`](#insn-00afd47c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afd480`](#insn-00afd480) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afd2ac`](#insn-00afd2ac)

~~~json
{
  "source": "00afd2ac",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afd2b0`](#insn-00afd2b0)

~~~json
{
  "source": "00afd2b0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afd2b4`](#insn-00afd2b4)

~~~json
{
  "source": "00afd2b4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afd2b8`](#insn-00afd2b8)

~~~json
{
  "source": "00afd2b8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afd2e0`](#insn-00afd2e0)

~~~json
{
  "source": "00afd2e0",
  "target": "00afd478",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afd2f0`](#insn-00afd2f0)

~~~json
{
  "source": "00afd2f0",
  "target": "0029583d",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afd2fc`](#insn-00afd2fc)

~~~json
{
  "source": "00afd2fc",
  "target": "00bded80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afd304`](#insn-00afd304)

~~~json
{
  "source": "00afd304",
  "target": "00afd35c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afd324`](#insn-00afd324)

~~~json
{
  "source": "00afd324",
  "target": "00afd37c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afd334`](#insn-00afd334)

~~~json
{
  "source": "00afd334",
  "target": "00afd354",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afd348`](#insn-00afd348)

~~~json
{
  "source": "00afd348",
  "target": "00afd3f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afd350`](#insn-00afd350)

~~~json
{
  "source": "00afd350",
  "target": "00afd338",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afd358`](#insn-00afd358)

~~~json
{
  "source": "00afd358",
  "target": "00afd33c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afd364`](#insn-00afd364)

~~~json
{
  "source": "00afd364",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afd368`](#insn-00afd368)

~~~json
{
  "source": "00afd368",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afd36c`](#insn-00afd36c)

~~~json
{
  "source": "00afd36c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afd378`](#insn-00afd378)

~~~json
{
  "source": "00afd378",
  "target": "00bdb7a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afd398`](#insn-00afd398)

~~~json
{
  "source": "00afd398",
  "target": "00afd3c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afd3c4`](#insn-00afd3c4)

~~~json
{
  "source": "00afd3c4",
  "target": "00afd3e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afd3d0`](#insn-00afd3d0)

~~~json
{
  "source": "00afd3d0",
  "target": "00afd3d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afd3d8`](#insn-00afd3d8)

~~~json
{
  "source": "00afd3d8",
  "target": "00afd39c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afd3e0`](#insn-00afd3e0)

~~~json
{
  "source": "00afd3e0",
  "target": "00afd39c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afd3ec`](#insn-00afd3ec)

~~~json
{
  "source": "00afd3ec",
  "target": "00afd34c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afd3fc`](#insn-00afd3fc)

~~~json
{
  "source": "00afd3fc",
  "target": "00bdb7a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afd404`](#insn-00afd404)

~~~json
{
  "source": "00afd404",
  "target": "00afd478",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afd424`](#insn-00afd424)

~~~json
{
  "source": "00afd424",
  "target": "00bdb130",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afd430`](#insn-00afd430)

~~~json
{
  "source": "00afd430",
  "target": "00afd478",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afd444`](#insn-00afd444)

~~~json
{
  "source": "00afd444",
  "target": "0029583d",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afd448`](#insn-00afd448)

~~~json
{
  "source": "00afd448",
  "target": "00bdb130",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afd468`](#insn-00afd468)

~~~json
{
  "source": "00afd468",
  "target": "00bdb130",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afd474`](#insn-00afd474)

~~~json
{
  "source": "00afd474",
  "target": "00afd43c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afd478`](#insn-00afd478)

~~~json
{
  "source": "00afd478",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afd47c`](#insn-00afd47c)

~~~json
{
  "source": "00afd47c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afd480`](#insn-00afd480)

~~~json
{
  "source": "00afd480",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
