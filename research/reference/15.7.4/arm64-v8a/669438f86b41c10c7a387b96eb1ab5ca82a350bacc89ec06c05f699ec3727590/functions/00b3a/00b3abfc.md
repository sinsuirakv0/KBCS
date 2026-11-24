# 00b3abfc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00b3abb8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3a/00b3abb8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0010.md#compare-071dc8853389ceddc262c7ade37b6d52)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0091.md#review-767015ee39cec2a69adff9629d30c523)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b3abfc",
  "name": "_ZNSt6__ndk118__insertion_sort_3IRN11flatbuffers17FlatBufferBuilder18TableKeyComparatorIN10reflection5FieldEEEPNS1_6OffsetIS5_EEEEvT0_SB_T_",
  "size": 412,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8d0b5ba62b02d7258667cfd3b10f9570bd677861b13b3977169277ef915730ce",
  "source_text_sha256": "8d0b5ba62b02d7258667cfd3b10f9570bd677861b13b3977169277ef915730ce",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b3abfc",
        "00b3ad97"
      ]
    ],
    "bytes_sha256": "f479b67ceb9f27651e00cce890d420fa53655945146fe64269afc14cf801d1cd",
    "instruction_count": 103,
    "instruction_bytes": 412,
    "body_bytes": 412,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bdfd40](../00bdf/00bdfd40.md)

## 呼び出し先

- [00bdb200](../00bdb/00bdb200.md)
- [00be0100](../00be0/00be0100.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2890 bytes

~~~c

void _ZNSt6__ndk118__insertion_sort_3IRN11flatbuffers17FlatBufferBuilder18TableKeyComparatorIN10reflection5FieldEEEPNS1_6OffsetIS5_EEEEvT0_SB_T_
               (uint *param_1,uint *param_2,long *param_3)

{
  long lVar1;
  uint uVar2;
  uint uVar3;
  uint uVar4;
  uint uVar5;
  long lVar6;
  bool bVar7;
  int iVar8;
  uint *puVar9;
  uint *puVar10;
  int *piVar11;
  long lVar12;
  uint *puVar13;
  long lVar14;
  int *piVar15;
  ulong uVar16;
  
  _ZNSt6__ndk17__sort3IRN11flatbuffers17FlatBufferBuilder18TableKeyComparatorIN10reflection5FieldEEEPNS1_6OffsetIS5_EEEEjT0_SB_SB_T_
            (param_1,param_1 + 1,param_1 + 2,param_3);
  if (param_1 + 3 != param_2) {
    lVar14 = 0xc;
    lVar1 = *(long *)(*param_3 + 0x28) + *(long *)(*param_3 + 0x20);
    puVar9 = param_1 + 3;
    puVar13 = param_1 + 2;
    do {
      puVar10 = puVar9;
      uVar3 = *puVar10;
      uVar16 = (ulong)*puVar13;
      piVar15 = (int *)(lVar1 - (ulong)uVar3);
      piVar11 = (int *)(lVar1 - uVar16);
      puVar9 = (uint *)((long)piVar15 + (ulong)*(ushort *)((long)piVar15 + (4 - (long)*piVar15)));
      puVar13 = (uint *)((long)piVar11 + (ulong)*(ushort *)((long)piVar11 + (4 - (long)*piVar11)));
      puVar9 = (uint *)((long)puVar9 + (ulong)*puVar9);
      puVar13 = (uint *)((long)puVar13 + (ulong)*puVar13);
      uVar4 = *puVar9;
      uVar5 = *puVar13;
      uVar2 = uVar5;
      if (uVar4 <= uVar5) {
        uVar2 = uVar4;
      }
      iVar8 = memcmp(puVar9 + 1,puVar13 + 1,(ulong)uVar2);
      bVar7 = uVar4 < uVar5;
      if (iVar8 != 0) {
        bVar7 = iVar8 < 0;
      }
      lVar12 = lVar14;
      if (bVar7) {
        do {
          lVar6 = lVar12 + -4;
          *(int *)((long)param_1 + lVar12) = (int)uVar16;
          puVar9 = param_1;
          if (lVar6 == 0) goto LAB_00b3ac64;
          uVar16 = (ulong)*(uint *)((long)param_1 + lVar12 + -8);
          piVar11 = (int *)(lVar1 - uVar16);
          puVar9 = (uint *)((long)piVar15 + (ulong)*(ushort *)((long)piVar15 + (4 - (long)*piVar15))
                           );
          puVar13 = (uint *)((long)piVar11 +
                            (ulong)*(ushort *)((long)piVar11 + (4 - (long)*piVar11)));
          puVar9 = (uint *)((long)puVar9 + (ulong)*puVar9);
          uVar4 = *puVar9;
          puVar13 = (uint *)((long)puVar13 + (ulong)*puVar13);
          uVar5 = *puVar13;
          uVar2 = uVar5;
          if (uVar4 <= uVar5) {
            uVar2 = uVar4;
          }
          iVar8 = memcmp(puVar9 + 1,puVar13 + 1,(ulong)uVar2);
          bVar7 = uVar4 < uVar5;
          if (iVar8 != 0) {
            bVar7 = iVar8 < 0;
          }
          lVar12 = lVar6;
        } while (bVar7);
        puVar9 = (uint *)((long)param_1 + lVar6);
LAB_00b3ac64:
        *puVar9 = uVar3;
      }
      lVar14 = lVar14 + 4;
      puVar9 = puVar10 + 1;
      puVar13 = puVar10;
    } while (puVar10 + 1 != param_2);
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b3abfc"></a> `00b3abfc` | `ff c3 01 d1` | sub sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00b3ac00"></a> `00b3ac00` | `fc 6f 01 a9` | stp x28,x27,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b3ac04"></a> `00b3ac04` | `fa 67 02 a9` | stp x26,x25,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b3ac08"></a> `00b3ac08` | `f8 5f 03 a9` | stp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b3ac0c"></a> `00b3ac0c` | `f6 57 04 a9` | stp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b3ac10"></a> `00b3ac10` | `f4 4f 05 a9` | stp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00b3ac14"></a> `00b3ac14` | `fd 7b 06 a9` | stp x29,x30,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00b3ac18"></a> `00b3ac18` | `fd 83 01 91` | add x29,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00b3ac1c"></a> `00b3ac1c` | `f6 03 02 aa` | mov x22,x2 | `FALL_THROUGH`
<a id="insn-00b3ac20"></a> `00b3ac20` | `15 20 00 91` | add x21,x0,#0x8 | `FALL_THROUGH`
<a id="insn-00b3ac24"></a> `00b3ac24` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00b3ac28"></a> `00b3ac28` | `01 10 00 91` | add x1,x0,#0x4 | `FALL_THROUGH`
<a id="insn-00b3ac2c"></a> `00b3ac2c` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-00b3ac30"></a> `00b3ac30` | `e3 03 16 aa` | mov x3,x22 | `FALL_THROUGH`
<a id="insn-00b3ac34"></a> `00b3ac34` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00b3ac38"></a> `00b3ac38` | `32 95 02 94` | bl 0x00be0100 | `UNCONDITIONAL_CALL`
<a id="insn-00b3ac3c"></a> `00b3ac3c` | `88 32 00 91` | add x8,x20,#0xc | `FALL_THROUGH`
<a id="insn-00b3ac40"></a> `00b3ac40` | `1f 01 13 eb` | cmp x8,x19 | `FALL_THROUGH`
<a id="insn-00b3ac44"></a> `00b3ac44` | `a0 09 00 54` | b.eq 0x00b3ad78 | `CONDITIONAL_JUMP`
<a id="insn-00b3ac48"></a> `00b3ac48` | `c9 02 40 f9` | ldr x9,[x22] | `FALL_THROUGH`
<a id="insn-00b3ac4c"></a> `00b3ac4c` | `97 01 80 52` | mov w23,#0xc | `FALL_THROUGH`
<a id="insn-00b3ac50"></a> `00b3ac50` | `2a 25 42 a9` | ldp x10,x9,[x9, #0x20] | `FALL_THROUGH`
<a id="insn-00b3ac54"></a> `00b3ac54` | `f3 07 00 f9` | str x19,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00b3ac58"></a> `00b3ac58` | `36 01 0a 8b` | add x22,x9,x10 | `FALL_THROUGH`
<a id="insn-00b3ac5c"></a> `00b3ac5c` | `08 00 00 14` | b 0x00b3ac7c | `UNCONDITIONAL_JUMP`
<a id="insn-00b3ac60"></a> `00b3ac60` | `e8 03 14 aa` | mov x8,x20 | `FALL_THROUGH`
<a id="insn-00b3ac64"></a> `00b3ac64` | `f3 07 40 f9` | ldr x19,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00b3ac68"></a> `00b3ac68` | `18 01 00 b9` | str w24,[x8] | `FALL_THROUGH`
<a id="insn-00b3ac6c"></a> `00b3ac6c` | `a8 12 00 91` | add x8,x21,#0x4 | `FALL_THROUGH`
<a id="insn-00b3ac70"></a> `00b3ac70` | `1f 01 13 eb` | cmp x8,x19 | `FALL_THROUGH`
<a id="insn-00b3ac74"></a> `00b3ac74` | `f7 12 00 91` | add x23,x23,#0x4 | `FALL_THROUGH`
<a id="insn-00b3ac78"></a> `00b3ac78` | `00 08 00 54` | b.eq 0x00b3ad78 | `CONDITIONAL_JUMP`
<a id="insn-00b3ac7c"></a> `00b3ac7c` | `e9 03 15 aa` | mov x9,x21 | `FALL_THROUGH`
<a id="insn-00b3ac80"></a> `00b3ac80` | `18 01 40 b9` | ldr w24,[x8] | `FALL_THROUGH`
<a id="insn-00b3ac84"></a> `00b3ac84` | `3a 01 40 b9` | ldr w26,[x9] | `FALL_THROUGH`
<a id="insn-00b3ac88"></a> `00b3ac88` | `f5 03 08 aa` | mov x21,x8 | `FALL_THROUGH`
<a id="insn-00b3ac8c"></a> `00b3ac8c` | `d9 02 18 cb` | sub x25,x22,x24 | `FALL_THROUGH`
<a id="insn-00b3ac90"></a> `00b3ac90` | `c8 02 1a cb` | sub x8,x22,x26 | `FALL_THROUGH`
<a id="insn-00b3ac94"></a> `00b3ac94` | `29 03 80 b9` | ldrsw x9,[x25] | `FALL_THROUGH`
<a id="insn-00b3ac98"></a> `00b3ac98` | `0a 01 80 b9` | ldrsw x10,[x8] | `FALL_THROUGH`
<a id="insn-00b3ac9c"></a> `00b3ac9c` | `29 03 09 cb` | sub x9,x25,x9 | `FALL_THROUGH`
<a id="insn-00b3aca0"></a> `00b3aca0` | `0a 01 0a cb` | sub x10,x8,x10 | `FALL_THROUGH`
<a id="insn-00b3aca4"></a> `00b3aca4` | `29 09 40 79` | ldrh w9,[x9, #0x4] | `FALL_THROUGH`
<a id="insn-00b3aca8"></a> `00b3aca8` | `4a 09 40 79` | ldrh w10,[x10, #0x4] | `FALL_THROUGH`
<a id="insn-00b3acac"></a> `00b3acac` | `29 03 09 8b` | add x9,x25,x9 | `FALL_THROUGH`
<a id="insn-00b3acb0"></a> `00b3acb0` | `08 01 0a 8b` | add x8,x8,x10 | `FALL_THROUGH`
<a id="insn-00b3acb4"></a> `00b3acb4` | `2a 01 40 b9` | ldr w10,[x9] | `FALL_THROUGH`
<a id="insn-00b3acb8"></a> `00b3acb8` | `0b 01 40 b9` | ldr w11,[x8] | `FALL_THROUGH`
<a id="insn-00b3acbc"></a> `00b3acbc` | `20 01 0a 8b` | add x0,x9,x10 | `FALL_THROUGH`
<a id="insn-00b3acc0"></a> `00b3acc0` | `01 01 0b 8b` | add x1,x8,x11 | `FALL_THROUGH`
<a id="insn-00b3acc4"></a> `00b3acc4` | `1b 44 40 b8` | ldr w27,[x0], #0x4 | `FALL_THROUGH`
<a id="insn-00b3acc8"></a> `00b3acc8` | `3c 44 40 b8` | ldr w28,[x1], #0x4 | `FALL_THROUGH`
<a id="insn-00b3accc"></a> `00b3accc` | `9f 03 1b 6b` | cmp w28,w27 | `FALL_THROUGH`
<a id="insn-00b3acd0"></a> `00b3acd0` | `82 33 9b 1a` | csel w2,w28,w27,cc | `FALL_THROUGH`
<a id="insn-00b3acd4"></a> `00b3acd4` | `4b 81 02 94` | bl 0x00bdb200 | `UNCONDITIONAL_CALL`
<a id="insn-00b3acd8"></a> `00b3acd8` | `7f 03 1c 6b` | cmp w27,w28 | `FALL_THROUGH`
<a id="insn-00b3acdc"></a> `00b3acdc` | `e8 27 9f 1a` | cset w8,cc | `FALL_THROUGH`
<a id="insn-00b3ace0"></a> `00b3ace0` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00b3ace4"></a> `00b3ace4` | `e9 a7 9f 1a` | cset w9,lt | `FALL_THROUGH`
<a id="insn-00b3ace8"></a> `00b3ace8` | `08 01 89 1a` | csel w8,w8,w9,eq | `FALL_THROUGH`
<a id="insn-00b3acec"></a> `00b3acec` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00b3acf0"></a> `00b3acf0` | `e1 fb ff 54` | b.ne 0x00b3ac6c | `CONDITIONAL_JUMP`
<a id="insn-00b3acf4"></a> `00b3acf4` | `e8 03 17 aa` | mov x8,x23 | `FALL_THROUGH`
<a id="insn-00b3acf8"></a> `00b3acf8` | `1b 11 00 f1` | subs x27,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00b3acfc"></a> `00b3acfc` | `9a 6a 28 b8` | str w26,[x20, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00b3ad00"></a> `00b3ad00` | `00 fb ff 54` | b.eq 0x00b3ac60 | `CONDITIONAL_JUMP`
<a id="insn-00b3ad04"></a> `00b3ad04` | `88 02 08 8b` | add x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00b3ad08"></a> `00b3ad08` | `1a 81 5f b8` | ldur w26,[x8, #-0x8] | `FALL_THROUGH`
<a id="insn-00b3ad0c"></a> `00b3ad0c` | `28 03 80 b9` | ldrsw x8,[x25] | `FALL_THROUGH`
<a id="insn-00b3ad10"></a> `00b3ad10` | `c9 02 1a cb` | sub x9,x22,x26 | `FALL_THROUGH`
<a id="insn-00b3ad14"></a> `00b3ad14` | `2a 01 80 b9` | ldrsw x10,[x9] | `FALL_THROUGH`
<a id="insn-00b3ad18"></a> `00b3ad18` | `28 03 08 cb` | sub x8,x25,x8 | `FALL_THROUGH`
<a id="insn-00b3ad1c"></a> `00b3ad1c` | `08 09 40 79` | ldrh w8,[x8, #0x4] | `FALL_THROUGH`
<a id="insn-00b3ad20"></a> `00b3ad20` | `2a 01 0a cb` | sub x10,x9,x10 | `FALL_THROUGH`
<a id="insn-00b3ad24"></a> `00b3ad24` | `4a 09 40 79` | ldrh w10,[x10, #0x4] | `FALL_THROUGH`
<a id="insn-00b3ad28"></a> `00b3ad28` | `28 03 08 8b` | add x8,x25,x8 | `FALL_THROUGH`
<a id="insn-00b3ad2c"></a> `00b3ad2c` | `0b 01 40 b9` | ldr w11,[x8] | `FALL_THROUGH`
<a id="insn-00b3ad30"></a> `00b3ad30` | `29 01 0a 8b` | add x9,x9,x10 | `FALL_THROUGH`
<a id="insn-00b3ad34"></a> `00b3ad34` | `2a 01 40 b9` | ldr w10,[x9] | `FALL_THROUGH`
<a id="insn-00b3ad38"></a> `00b3ad38` | `00 01 0b 8b` | add x0,x8,x11 | `FALL_THROUGH`
<a id="insn-00b3ad3c"></a> `00b3ad3c` | `1c 44 40 b8` | ldr w28,[x0], #0x4 | `FALL_THROUGH`
<a id="insn-00b3ad40"></a> `00b3ad40` | `21 01 0a 8b` | add x1,x9,x10 | `FALL_THROUGH`
<a id="insn-00b3ad44"></a> `00b3ad44` | `33 44 40 b8` | ldr w19,[x1], #0x4 | `FALL_THROUGH`
<a id="insn-00b3ad48"></a> `00b3ad48` | `7f 02 1c 6b` | cmp w19,w28 | `FALL_THROUGH`
<a id="insn-00b3ad4c"></a> `00b3ad4c` | `62 32 9c 1a` | csel w2,w19,w28,cc | `FALL_THROUGH`
<a id="insn-00b3ad50"></a> `00b3ad50` | `2c 81 02 94` | bl 0x00bdb200 | `UNCONDITIONAL_CALL`
<a id="insn-00b3ad54"></a> `00b3ad54` | `9f 03 13 6b` | cmp w28,w19 | `FALL_THROUGH`
<a id="insn-00b3ad58"></a> `00b3ad58` | `e8 27 9f 1a` | cset w8,cc | `FALL_THROUGH`
<a id="insn-00b3ad5c"></a> `00b3ad5c` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00b3ad60"></a> `00b3ad60` | `e9 a7 9f 1a` | cset w9,lt | `FALL_THROUGH`
<a id="insn-00b3ad64"></a> `00b3ad64` | `09 01 89 1a` | csel w9,w8,w9,eq | `FALL_THROUGH`
<a id="insn-00b3ad68"></a> `00b3ad68` | `e8 03 1b aa` | mov x8,x27 | `FALL_THROUGH`
<a id="insn-00b3ad6c"></a> `00b3ad6c` | `69 fc 07 37` | tbnz w9,#0x0,0x00b3acf8 | `CONDITIONAL_JUMP`
<a id="insn-00b3ad70"></a> `00b3ad70` | `88 02 1b 8b` | add x8,x20,x27 | `FALL_THROUGH`
<a id="insn-00b3ad74"></a> `00b3ad74` | `bc ff ff 17` | b 0x00b3ac64 | `UNCONDITIONAL_JUMP`
<a id="insn-00b3ad78"></a> `00b3ad78` | `fd 7b 46 a9` | ldp x29,x30,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00b3ad7c"></a> `00b3ad7c` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00b3ad80"></a> `00b3ad80` | `f6 57 44 a9` | ldp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b3ad84"></a> `00b3ad84` | `f8 5f 43 a9` | ldp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b3ad88"></a> `00b3ad88` | `fa 67 42 a9` | ldp x26,x25,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b3ad8c"></a> `00b3ad8c` | `fc 6f 41 a9` | ldp x28,x27,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b3ad90"></a> `00b3ad90` | `ff c3 01 91` | add sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00b3ad94"></a> `00b3ad94` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b3abfc`](#insn-00b3abfc) 範囲 `[['00b3abfc', '00b3ac47']]`
  - `CONDITIONAL_JUMP` [`00b3ac44`](#insn-00b3ac44) → [`00b3ad78`](#insn-00b3ad78)
  - `FALL_THROUGH` [`00b3ac44`](#insn-00b3ac44) → [`00b3ac48`](#insn-00b3ac48)
- ブロック [`00b3ac48`](#insn-00b3ac48) 範囲 `[['00b3ac48', '00b3ac5f']]`
  - `UNCONDITIONAL_JUMP` [`00b3ac5c`](#insn-00b3ac5c) → [`00b3ac7c`](#insn-00b3ac7c)
- ブロック [`00b3ac60`](#insn-00b3ac60) 範囲 `[['00b3ac60', '00b3ac63']]`
  - `FALL_THROUGH` [`00b3ac60`](#insn-00b3ac60) → [`00b3ac64`](#insn-00b3ac64)
- ブロック [`00b3ac64`](#insn-00b3ac64) 範囲 `[['00b3ac64', '00b3ac6b']]`
  - `FALL_THROUGH` [`00b3ac68`](#insn-00b3ac68) → [`00b3ac6c`](#insn-00b3ac6c)
- ブロック [`00b3ac6c`](#insn-00b3ac6c) 範囲 `[['00b3ac6c', '00b3ac7b']]`
  - `CONDITIONAL_JUMP` [`00b3ac78`](#insn-00b3ac78) → [`00b3ad78`](#insn-00b3ad78)
  - `FALL_THROUGH` [`00b3ac78`](#insn-00b3ac78) → [`00b3ac7c`](#insn-00b3ac7c)
- ブロック [`00b3ac7c`](#insn-00b3ac7c) 範囲 `[['00b3ac7c', '00b3acf3']]`
  - `CONDITIONAL_JUMP` [`00b3acf0`](#insn-00b3acf0) → [`00b3ac6c`](#insn-00b3ac6c)
  - `FALL_THROUGH` [`00b3acf0`](#insn-00b3acf0) → [`00b3acf4`](#insn-00b3acf4)
- ブロック [`00b3acf4`](#insn-00b3acf4) 範囲 `[['00b3acf4', '00b3acf7']]`
  - `FALL_THROUGH` [`00b3acf4`](#insn-00b3acf4) → [`00b3acf8`](#insn-00b3acf8)
- ブロック [`00b3acf8`](#insn-00b3acf8) 範囲 `[['00b3acf8', '00b3ad03']]`
  - `CONDITIONAL_JUMP` [`00b3ad00`](#insn-00b3ad00) → [`00b3ac60`](#insn-00b3ac60)
  - `FALL_THROUGH` [`00b3ad00`](#insn-00b3ad00) → [`00b3ad04`](#insn-00b3ad04)
- ブロック [`00b3ad04`](#insn-00b3ad04) 範囲 `[['00b3ad04', '00b3ad6f']]`
  - `CONDITIONAL_JUMP` [`00b3ad6c`](#insn-00b3ad6c) → [`00b3acf8`](#insn-00b3acf8)
  - `FALL_THROUGH` [`00b3ad6c`](#insn-00b3ad6c) → [`00b3ad70`](#insn-00b3ad70)
- ブロック [`00b3ad70`](#insn-00b3ad70) 範囲 `[['00b3ad70', '00b3ad77']]`
  - `UNCONDITIONAL_JUMP` [`00b3ad74`](#insn-00b3ad74) → [`00b3ac64`](#insn-00b3ac64)
- ブロック [`00b3ad78`](#insn-00b3ad78) 範囲 `[['00b3ad78', '00b3ad97']]`

## 命令位置別の参照

- [`00b3ac00`](#insn-00b3ac00) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3ac04`](#insn-00b3ac04) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3ac08`](#insn-00b3ac08) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3ac0c`](#insn-00b3ac0c) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3ac10`](#insn-00b3ac10) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3ac14`](#insn-00b3ac14) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3ac38`](#insn-00b3ac38) → [`00be0100`](../00be0/00be0100.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be0100` · 推定シンボル `None` · 推定型 `None`
- [`00b3ac44`](#insn-00b3ac44) → [`00b3ad78`](#insn-00b3ad78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3ac54`](#insn-00b3ac54) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3ac5c`](#insn-00b3ac5c) → [`00b3ac7c`](#insn-00b3ac7c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3ac64`](#insn-00b3ac64) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3ac78`](#insn-00b3ac78) → [`00b3ad78`](#insn-00b3ad78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3acd4`](#insn-00b3acd4) → [`00bdb200`](../00bdb/00bdb200.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb200` · 推定シンボル `None` · 推定型 `None`
- [`00b3acf0`](#insn-00b3acf0) → [`00b3ac6c`](#insn-00b3ac6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3ad00`](#insn-00b3ad00) → [`00b3ac60`](#insn-00b3ac60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3ad50`](#insn-00b3ad50) → [`00bdb200`](../00bdb/00bdb200.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb200` · 推定シンボル `None` · 推定型 `None`
- [`00b3ad6c`](#insn-00b3ad6c) → [`00b3acf8`](#insn-00b3acf8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3ad74`](#insn-00b3ad74) → [`00b3ac64`](#insn-00b3ac64) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3ad78`](#insn-00b3ad78) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3ad7c`](#insn-00b3ad7c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3ad80`](#insn-00b3ad80) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3ad84`](#insn-00b3ad84) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3ad88`](#insn-00b3ad88) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3ad8c`](#insn-00b3ad8c) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b3ac00`](#insn-00b3ac00)

~~~json
{
  "source": "00b3ac00",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3ac04`](#insn-00b3ac04)

~~~json
{
  "source": "00b3ac04",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3ac08`](#insn-00b3ac08)

~~~json
{
  "source": "00b3ac08",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3ac0c`](#insn-00b3ac0c)

~~~json
{
  "source": "00b3ac0c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3ac10`](#insn-00b3ac10)

~~~json
{
  "source": "00b3ac10",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3ac14`](#insn-00b3ac14)

~~~json
{
  "source": "00b3ac14",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3ac38`](#insn-00b3ac38)

~~~json
{
  "source": "00b3ac38",
  "target": "00be0100",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b3ac44`](#insn-00b3ac44)

~~~json
{
  "source": "00b3ac44",
  "target": "00b3ad78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3ac54`](#insn-00b3ac54)

~~~json
{
  "source": "00b3ac54",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3ac5c`](#insn-00b3ac5c)

~~~json
{
  "source": "00b3ac5c",
  "target": "00b3ac7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3ac64`](#insn-00b3ac64)

~~~json
{
  "source": "00b3ac64",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3ac78`](#insn-00b3ac78)

~~~json
{
  "source": "00b3ac78",
  "target": "00b3ad78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3acd4`](#insn-00b3acd4)

~~~json
{
  "source": "00b3acd4",
  "target": "00bdb200",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b3acf0`](#insn-00b3acf0)

~~~json
{
  "source": "00b3acf0",
  "target": "00b3ac6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3ad00`](#insn-00b3ad00)

~~~json
{
  "source": "00b3ad00",
  "target": "00b3ac60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3ad50`](#insn-00b3ad50)

~~~json
{
  "source": "00b3ad50",
  "target": "00bdb200",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b3ad6c`](#insn-00b3ad6c)

~~~json
{
  "source": "00b3ad6c",
  "target": "00b3acf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3ad74`](#insn-00b3ad74)

~~~json
{
  "source": "00b3ad74",
  "target": "00b3ac64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3ad78`](#insn-00b3ad78)

~~~json
{
  "source": "00b3ad78",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3ad7c`](#insn-00b3ad7c)

~~~json
{
  "source": "00b3ad7c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3ad80`](#insn-00b3ad80)

~~~json
{
  "source": "00b3ad80",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3ad84`](#insn-00b3ad84)

~~~json
{
  "source": "00b3ad84",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3ad88`](#insn-00b3ad88)

~~~json
{
  "source": "00b3ad88",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3ad8c`](#insn-00b3ad8c)

~~~json
{
  "source": "00b3ad8c",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
