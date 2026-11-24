# 00b3decc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00b3de88`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3d/00b3de88.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0011.md#compare-86d5c3a13817ea1435dc26f527c0177e)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0091.md#review-edd23383a23b9588f8ea3c11039edc83)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b3decc",
  "name": "_ZNSt6__ndk17__sort3IRN11flatbuffers17FlatBufferBuilder18TableKeyComparatorIN10reflection7ServiceEEEPNS1_6OffsetIS5_EEEEjT0_SB_SB_T_",
  "size": 588,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0c25c3deb94e941193334e0700b0bbe8a0ca1d8cd8b99a8224bae226b7c0287e",
  "source_text_sha256": "0c25c3deb94e941193334e0700b0bbe8a0ca1d8cd8b99a8224bae226b7c0287e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b3decc",
        "00b3e117"
      ]
    ],
    "bytes_sha256": "ebf6291af4f7144e1d631ead203ff5840eecd05300ede05933247d6692638bd7",
    "instruction_count": 147,
    "instruction_bytes": 588,
    "body_bytes": 588,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00be0120](../00be0/00be0120.md)

## 呼び出し先

- [00bdb200](../00bdb/00bdb200.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 4260 bytes

~~~c

undefined8
_ZNSt6__ndk17__sort3IRN11flatbuffers17FlatBufferBuilder18TableKeyComparatorIN10reflection7ServiceEEEPNS1_6OffsetIS5_EEEEjT0_SB_SB_T_
          (uint *param_1,uint *param_2,uint *param_3,long *param_4)

{
  long lVar1;
  uint *puVar2;
  uint *puVar3;
  uint uVar4;
  uint uVar5;
  uint uVar6;
  uint uVar7;
  uint uVar8;
  uint uVar9;
  bool bVar10;
  bool bVar11;
  int iVar12;
  int *piVar13;
  uint *__s1;
  int *piVar14;
  
  uVar4 = *param_2;
  uVar5 = *param_1;
  lVar1 = *(long *)(*param_4 + 0x28) + *(long *)(*param_4 + 0x20);
  piVar13 = (int *)(lVar1 - (ulong)uVar4);
  piVar14 = (int *)(lVar1 - (ulong)uVar5);
  puVar2 = (uint *)((long)piVar13 + (ulong)*(ushort *)((long)piVar13 + (4 - (long)*piVar13)));
  puVar3 = (uint *)((long)piVar14 + (ulong)*(ushort *)((long)piVar14 + (4 - (long)*piVar14)));
  puVar2 = (uint *)((long)puVar2 + (ulong)*puVar2);
  puVar3 = (uint *)((long)puVar3 + (ulong)*puVar3);
  __s1 = puVar2 + 1;
  uVar7 = *puVar2;
  uVar8 = *puVar3;
  uVar6 = uVar8;
  if (uVar7 <= uVar8) {
    uVar6 = uVar7;
  }
  iVar12 = memcmp(__s1,puVar3 + 1,(ulong)uVar6);
  uVar6 = *param_3;
  piVar13 = (int *)(lVar1 - (ulong)uVar6);
                    /* try { // try from 00b3df6c to 00c3e00b has its CatchHandler @ 00b3df6c
                       catch() { ... } // from try @ 00b3df6c with catch @ 00b3df6c
                       catch() { ... } // from try @ 00b3e2f8 with catch @ 00b3df6c
                       catch() { ... } // from try @ 00b3e3a4 with catch @ 00b3df6c
                       catch() { ... } // from try @ 00b3e51c with catch @ 00b3df6c */
  puVar2 = (uint *)((long)piVar13 + (ulong)*(ushort *)((long)piVar13 + (4 - (long)*piVar13)));
  puVar2 = (uint *)((long)puVar2 + (ulong)*puVar2);
  uVar9 = *puVar2;
  bVar10 = uVar7 < uVar8;
  if (iVar12 != 0) {
    bVar10 = iVar12 < 0;
  }
  uVar8 = uVar7;
  if (uVar9 <= uVar7) {
    uVar8 = uVar9;
  }
  iVar12 = memcmp(puVar2 + 1,__s1,(ulong)uVar8);
  bVar11 = uVar9 < uVar7;
  if (iVar12 != 0) {
    bVar11 = iVar12 < 0;
  }
  if (bVar10) {
    if (bVar11) {
      *param_1 = uVar6;
      *param_3 = uVar5;
      return 1;
    }
    *param_1 = uVar4;
                    /* try { // try from 00b3e06c to 00c3e07b has its CatchHandler @ 00b3e554 */
    *param_2 = uVar5;
    uVar4 = *param_3;
    piVar13 = (int *)(lVar1 - (ulong)uVar4);
    puVar2 = (uint *)((long)piVar14 + (ulong)*(ushort *)((long)piVar14 + (4 - (long)*piVar14)));
    puVar3 = (uint *)((long)piVar13 + (ulong)*(ushort *)((long)piVar13 + (4 - (long)*piVar13)));
    puVar2 = (uint *)((long)puVar2 + (ulong)*puVar2);
    puVar3 = (uint *)((long)puVar3 + (ulong)*puVar3);
    uVar7 = *puVar3;
    uVar8 = *puVar2;
    uVar6 = uVar8;
    if (uVar7 <= uVar8) {
      uVar6 = uVar7;
    }
    iVar12 = memcmp(puVar3 + 1,puVar2 + 1,(ulong)uVar6);
                    /* try { // try from 00b3e0c8 to 00c3e0d3 has its CatchHandler @ 00b3e540 */
    bVar10 = uVar7 < uVar8;
    if (iVar12 != 0) {
      bVar10 = iVar12 < 0;
    }
    if (!bVar10) {
      return 1;
    }
    *param_2 = uVar4;
    *param_3 = uVar5;
  }
  else {
    if (!bVar11) {
      return 0;
    }
    *param_2 = uVar6;
    *param_3 = uVar4;
    uVar4 = *param_2;
    uVar5 = *param_1;
    piVar13 = (int *)(lVar1 - (ulong)uVar4);
    piVar14 = (int *)(lVar1 - (ulong)uVar5);
                    /* try { // try from 00b3e00c to 00c3e01f has its CatchHandler @ 00b3e524 */
    puVar2 = (uint *)((long)piVar13 + (ulong)*(ushort *)((long)piVar13 + (4 - (long)*piVar13)));
    puVar3 = (uint *)((long)piVar14 + (ulong)*(ushort *)((long)piVar14 + (4 - (long)*piVar14)));
    puVar2 = (uint *)((long)puVar2 + (ulong)*puVar2);
    puVar3 = (uint *)((long)puVar3 + (ulong)*puVar3);
    uVar7 = *puVar2;
    uVar8 = *puVar3;
    uVar6 = uVar8;
    if (uVar7 <= uVar8) {
      uVar6 = uVar7;
    }
    iVar12 = memcmp(puVar2 + 1,puVar3 + 1,(ulong)uVar6);
                    /* try { // try from 00b3e03c to 00c3e047 has its CatchHandler @ 00b3e570 */
    bVar10 = uVar7 < uVar8;
                    /* try { // try from 00b3e04c to 00c3e06b has its CatchHandler @ 00b3e578 */
    if (iVar12 != 0) {
      bVar10 = iVar12 < 0;
    }
    if (!bVar10) {
      return 1;
    }
    *param_1 = uVar4;
    *param_2 = uVar5;
  }
  return 2;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b3decc"></a> `00b3decc` | `ff c3 01 d1` | sub sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00b3ded0"></a> `00b3ded0` | `fc 6f 01 a9` | stp x28,x27,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b3ded4"></a> `00b3ded4` | `fa 67 02 a9` | stp x26,x25,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b3ded8"></a> `00b3ded8` | `f8 5f 03 a9` | stp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b3dedc"></a> `00b3dedc` | `f6 57 04 a9` | stp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b3dee0"></a> `00b3dee0` | `f4 4f 05 a9` | stp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00b3dee4"></a> `00b3dee4` | `fd 7b 06 a9` | stp x29,x30,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00b3dee8"></a> `00b3dee8` | `fd 83 01 91` | add x29,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00b3deec"></a> `00b3deec` | `68 00 40 f9` | ldr x8,[x3] | `FALL_THROUGH`
<a id="insn-00b3def0"></a> `00b3def0` | `f4 03 02 aa` | mov x20,x2 | `FALL_THROUGH`
<a id="insn-00b3def4"></a> `00b3def4` | `09 21 42 a9` | ldp x9,x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00b3def8"></a> `00b3def8` | `e1 03 00 a9` | stp x1,x0,[sp] | `FALL_THROUGH`
<a id="insn-00b3defc"></a> `00b3defc` | `3a 00 40 b9` | ldr w26,[x1] | `FALL_THROUGH`
<a id="insn-00b3df00"></a> `00b3df00` | `15 00 40 b9` | ldr w21,[x0] | `FALL_THROUGH`
<a id="insn-00b3df04"></a> `00b3df04` | `18 01 09 8b` | add x24,x8,x9 | `FALL_THROUGH`
<a id="insn-00b3df08"></a> `00b3df08` | `08 03 1a cb` | sub x8,x24,x26 | `FALL_THROUGH`
<a id="insn-00b3df0c"></a> `00b3df0c` | `19 03 15 cb` | sub x25,x24,x21 | `FALL_THROUGH`
<a id="insn-00b3df10"></a> `00b3df10` | `09 01 80 b9` | ldrsw x9,[x8] | `FALL_THROUGH`
<a id="insn-00b3df14"></a> `00b3df14` | `2a 03 80 b9` | ldrsw x10,[x25] | `FALL_THROUGH`
<a id="insn-00b3df18"></a> `00b3df18` | `09 01 09 cb` | sub x9,x8,x9 | `FALL_THROUGH`
<a id="insn-00b3df1c"></a> `00b3df1c` | `2a 03 0a cb` | sub x10,x25,x10 | `FALL_THROUGH`
<a id="insn-00b3df20"></a> `00b3df20` | `29 09 40 79` | ldrh w9,[x9, #0x4] | `FALL_THROUGH`
<a id="insn-00b3df24"></a> `00b3df24` | `4a 09 40 79` | ldrh w10,[x10, #0x4] | `FALL_THROUGH`
<a id="insn-00b3df28"></a> `00b3df28` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00b3df2c"></a> `00b3df2c` | `29 03 0a 8b` | add x9,x25,x10 | `FALL_THROUGH`
<a id="insn-00b3df30"></a> `00b3df30` | `0a 01 40 b9` | ldr w10,[x8] | `FALL_THROUGH`
<a id="insn-00b3df34"></a> `00b3df34` | `2b 01 40 b9` | ldr w11,[x9] | `FALL_THROUGH`
<a id="insn-00b3df38"></a> `00b3df38` | `16 01 0a 8b` | add x22,x8,x10 | `FALL_THROUGH`
<a id="insn-00b3df3c"></a> `00b3df3c` | `21 01 0b 8b` | add x1,x9,x11 | `FALL_THROUGH`
<a id="insn-00b3df40"></a> `00b3df40` | `dc 46 40 b8` | ldr w28,[x22], #0x4 | `FALL_THROUGH`
<a id="insn-00b3df44"></a> `00b3df44` | `33 44 40 b8` | ldr w19,[x1], #0x4 | `FALL_THROUGH`
<a id="insn-00b3df48"></a> `00b3df48` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00b3df4c"></a> `00b3df4c` | `7f 02 1c 6b` | cmp w19,w28 | `FALL_THROUGH`
<a id="insn-00b3df50"></a> `00b3df50` | `62 32 9c 1a` | csel w2,w19,w28,cc | `FALL_THROUGH`
<a id="insn-00b3df54"></a> `00b3df54` | `ab 74 02 94` | bl 0x00bdb200 | `UNCONDITIONAL_CALL`
<a id="insn-00b3df58"></a> `00b3df58` | `9b 02 40 b9` | ldr w27,[x20] | `FALL_THROUGH`
<a id="insn-00b3df5c"></a> `00b3df5c` | `9f 03 13 6b` | cmp w28,w19 | `FALL_THROUGH`
<a id="insn-00b3df60"></a> `00b3df60` | `ea 27 9f 1a` | cset w10,cc | `FALL_THROUGH`
<a id="insn-00b3df64"></a> `00b3df64` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00b3df68"></a> `00b3df68` | `08 03 1b cb` | sub x8,x24,x27 | `FALL_THROUGH`
<a id="insn-00b3df6c"></a> `00b3df6c` | `09 01 80 b9` | ldrsw x9,[x8] | `FALL_THROUGH`
<a id="insn-00b3df70"></a> `00b3df70` | `f7 03 14 aa` | mov x23,x20 | `FALL_THROUGH`
<a id="insn-00b3df74"></a> `00b3df74` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00b3df78"></a> `00b3df78` | `09 01 09 cb` | sub x9,x8,x9 | `FALL_THROUGH`
<a id="insn-00b3df7c"></a> `00b3df7c` | `29 09 40 79` | ldrh w9,[x9, #0x4] | `FALL_THROUGH`
<a id="insn-00b3df80"></a> `00b3df80` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00b3df84"></a> `00b3df84` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00b3df88"></a> `00b3df88` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00b3df8c"></a> `00b3df8c` | `13 45 40 b8` | ldr w19,[x8], #0x4 | `FALL_THROUGH`
<a id="insn-00b3df90"></a> `00b3df90` | `e9 a7 9f 1a` | cset w9,lt | `FALL_THROUGH`
<a id="insn-00b3df94"></a> `00b3df94` | `54 01 89 1a` | csel w20,w10,w9,eq | `FALL_THROUGH`
<a id="insn-00b3df98"></a> `00b3df98` | `9f 03 13 6b` | cmp w28,w19 | `FALL_THROUGH`
<a id="insn-00b3df9c"></a> `00b3df9c` | `82 33 93 1a` | csel w2,w28,w19,cc | `FALL_THROUGH`
<a id="insn-00b3dfa0"></a> `00b3dfa0` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00b3dfa4"></a> `00b3dfa4` | `97 74 02 94` | bl 0x00bdb200 | `UNCONDITIONAL_CALL`
<a id="insn-00b3dfa8"></a> `00b3dfa8` | `7f 02 1c 6b` | cmp w19,w28 | `FALL_THROUGH`
<a id="insn-00b3dfac"></a> `00b3dfac` | `e8 27 9f 1a` | cset w8,cc | `FALL_THROUGH`
<a id="insn-00b3dfb0"></a> `00b3dfb0` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00b3dfb4"></a> `00b3dfb4` | `e9 a7 9f 1a` | cset w9,lt | `FALL_THROUGH`
<a id="insn-00b3dfb8"></a> `00b3dfb8` | `08 01 89 1a` | csel w8,w8,w9,eq | `FALL_THROUGH`
<a id="insn-00b3dfbc"></a> `00b3dfbc` | `f4 00 00 36` | tbz w20,#0x0,0x00b3dfd8 | `CONDITIONAL_JUMP`
<a id="insn-00b3dfc0"></a> `00b3dfc0` | `28 05 00 34` | cbz w8,0x00b3e064 | `CONDITIONAL_JUMP`
<a id="insn-00b3dfc4"></a> `00b3dfc4` | `e8 07 40 f9` | ldr x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00b3dfc8"></a> `00b3dfc8` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00b3dfcc"></a> `00b3dfcc` | `1b 01 00 b9` | str w27,[x8] | `FALL_THROUGH`
<a id="insn-00b3dfd0"></a> `00b3dfd0` | `f5 02 00 b9` | str w21,[x23] | `FALL_THROUGH`
<a id="insn-00b3dfd4"></a> `00b3dfd4` | `49 00 00 14` | b 0x00b3e0f8 | `UNCONDITIONAL_JUMP`
<a id="insn-00b3dfd8"></a> `00b3dfd8` | `e8 08 00 34` | cbz w8,0x00b3e0f4 | `CONDITIONAL_JUMP`
<a id="insn-00b3dfdc"></a> `00b3dfdc` | `f9 57 40 a9` | ldp x25,x21,[sp] | `FALL_THROUGH`
<a id="insn-00b3dfe0"></a> `00b3dfe0` | `3b 03 00 b9` | str w27,[x25] | `FALL_THROUGH`
<a id="insn-00b3dfe4"></a> `00b3dfe4` | `fa 02 00 b9` | str w26,[x23] | `FALL_THROUGH`
<a id="insn-00b3dfe8"></a> `00b3dfe8` | `34 03 40 b9` | ldr w20,[x25] | `FALL_THROUGH`
<a id="insn-00b3dfec"></a> `00b3dfec` | `b6 02 40 b9` | ldr w22,[x21] | `FALL_THROUGH`
<a id="insn-00b3dff0"></a> `00b3dff0` | `08 03 14 cb` | sub x8,x24,x20 | `FALL_THROUGH`
<a id="insn-00b3dff4"></a> `00b3dff4` | `09 03 16 cb` | sub x9,x24,x22 | `FALL_THROUGH`
<a id="insn-00b3dff8"></a> `00b3dff8` | `0a 01 80 b9` | ldrsw x10,[x8] | `FALL_THROUGH`
<a id="insn-00b3dffc"></a> `00b3dffc` | `2b 01 80 b9` | ldrsw x11,[x9] | `FALL_THROUGH`
<a id="insn-00b3e000"></a> `00b3e000` | `0a 01 0a cb` | sub x10,x8,x10 | `FALL_THROUGH`
<a id="insn-00b3e004"></a> `00b3e004` | `2b 01 0b cb` | sub x11,x9,x11 | `FALL_THROUGH`
<a id="insn-00b3e008"></a> `00b3e008` | `4a 09 40 79` | ldrh w10,[x10, #0x4] | `FALL_THROUGH`
<a id="insn-00b3e00c"></a> `00b3e00c` | `6b 09 40 79` | ldrh w11,[x11, #0x4] | `FALL_THROUGH`
<a id="insn-00b3e010"></a> `00b3e010` | `08 01 0a 8b` | add x8,x8,x10 | `FALL_THROUGH`
<a id="insn-00b3e014"></a> `00b3e014` | `29 01 0b 8b` | add x9,x9,x11 | `FALL_THROUGH`
<a id="insn-00b3e018"></a> `00b3e018` | `0a 01 40 b9` | ldr w10,[x8] | `FALL_THROUGH`
<a id="insn-00b3e01c"></a> `00b3e01c` | `2b 01 40 b9` | ldr w11,[x9] | `FALL_THROUGH`
<a id="insn-00b3e020"></a> `00b3e020` | `00 01 0a 8b` | add x0,x8,x10 | `FALL_THROUGH`
<a id="insn-00b3e024"></a> `00b3e024` | `21 01 0b 8b` | add x1,x9,x11 | `FALL_THROUGH`
<a id="insn-00b3e028"></a> `00b3e028` | `13 44 40 b8` | ldr w19,[x0], #0x4 | `FALL_THROUGH`
<a id="insn-00b3e02c"></a> `00b3e02c` | `37 44 40 b8` | ldr w23,[x1], #0x4 | `FALL_THROUGH`
<a id="insn-00b3e030"></a> `00b3e030` | `ff 02 13 6b` | cmp w23,w19 | `FALL_THROUGH`
<a id="insn-00b3e034"></a> `00b3e034` | `e2 32 93 1a` | csel w2,w23,w19,cc | `FALL_THROUGH`
<a id="insn-00b3e038"></a> `00b3e038` | `72 74 02 94` | bl 0x00bdb200 | `UNCONDITIONAL_CALL`
<a id="insn-00b3e03c"></a> `00b3e03c` | `7f 02 17 6b` | cmp w19,w23 | `FALL_THROUGH`
<a id="insn-00b3e040"></a> `00b3e040` | `e8 27 9f 1a` | cset w8,cc | `FALL_THROUGH`
<a id="insn-00b3e044"></a> `00b3e044` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00b3e048"></a> `00b3e048` | `e9 a7 9f 1a` | cset w9,lt | `FALL_THROUGH`
<a id="insn-00b3e04c"></a> `00b3e04c` | `08 01 89 1a` | csel w8,w8,w9,eq | `FALL_THROUGH`
<a id="insn-00b3e050"></a> `00b3e050` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00b3e054"></a> `00b3e054` | `c1 04 00 54` | b.ne 0x00b3e0ec | `CONDITIONAL_JUMP`
<a id="insn-00b3e058"></a> `00b3e058` | `b4 02 00 b9` | str w20,[x21] | `FALL_THROUGH`
<a id="insn-00b3e05c"></a> `00b3e05c` | `36 03 00 b9` | str w22,[x25] | `FALL_THROUGH`
<a id="insn-00b3e060"></a> `00b3e060` | `21 00 00 14` | b 0x00b3e0e4 | `UNCONDITIONAL_JUMP`
<a id="insn-00b3e064"></a> `00b3e064` | `f6 23 40 a9` | ldp x22,x8,[sp] | `FALL_THROUGH`
<a id="insn-00b3e068"></a> `00b3e068` | `1a 01 00 b9` | str w26,[x8] | `FALL_THROUGH`
<a id="insn-00b3e06c"></a> `00b3e06c` | `fa 03 15 aa` | mov x26,x21 | `FALL_THROUGH`
<a id="insn-00b3e070"></a> `00b3e070` | `da 02 00 b9` | str w26,[x22] | `FALL_THROUGH`
<a id="insn-00b3e074"></a> `00b3e074` | `f5 02 40 b9` | ldr w21,[x23] | `FALL_THROUGH`
<a id="insn-00b3e078"></a> `00b3e078` | `28 03 80 b9` | ldrsw x8,[x25] | `FALL_THROUGH`
<a id="insn-00b3e07c"></a> `00b3e07c` | `09 03 15 cb` | sub x9,x24,x21 | `FALL_THROUGH`
<a id="insn-00b3e080"></a> `00b3e080` | `2a 01 80 b9` | ldrsw x10,[x9] | `FALL_THROUGH`
<a id="insn-00b3e084"></a> `00b3e084` | `28 03 08 cb` | sub x8,x25,x8 | `FALL_THROUGH`
<a id="insn-00b3e088"></a> `00b3e088` | `08 09 40 79` | ldrh w8,[x8, #0x4] | `FALL_THROUGH`
<a id="insn-00b3e08c"></a> `00b3e08c` | `2a 01 0a cb` | sub x10,x9,x10 | `FALL_THROUGH`
<a id="insn-00b3e090"></a> `00b3e090` | `4a 09 40 79` | ldrh w10,[x10, #0x4] | `FALL_THROUGH`
<a id="insn-00b3e094"></a> `00b3e094` | `28 03 08 8b` | add x8,x25,x8 | `FALL_THROUGH`
<a id="insn-00b3e098"></a> `00b3e098` | `0b 01 40 b9` | ldr w11,[x8] | `FALL_THROUGH`
<a id="insn-00b3e09c"></a> `00b3e09c` | `29 01 0a 8b` | add x9,x9,x10 | `FALL_THROUGH`
<a id="insn-00b3e0a0"></a> `00b3e0a0` | `2a 01 40 b9` | ldr w10,[x9] | `FALL_THROUGH`
<a id="insn-00b3e0a4"></a> `00b3e0a4` | `01 01 0b 8b` | add x1,x8,x11 | `FALL_THROUGH`
<a id="insn-00b3e0a8"></a> `00b3e0a8` | `20 01 0a 8b` | add x0,x9,x10 | `FALL_THROUGH`
<a id="insn-00b3e0ac"></a> `00b3e0ac` | `13 44 40 b8` | ldr w19,[x0], #0x4 | `FALL_THROUGH`
<a id="insn-00b3e0b0"></a> `00b3e0b0` | `34 44 40 b8` | ldr w20,[x1], #0x4 | `FALL_THROUGH`
<a id="insn-00b3e0b4"></a> `00b3e0b4` | `9f 02 13 6b` | cmp w20,w19 | `FALL_THROUGH`
<a id="insn-00b3e0b8"></a> `00b3e0b8` | `82 32 93 1a` | csel w2,w20,w19,cc | `FALL_THROUGH`
<a id="insn-00b3e0bc"></a> `00b3e0bc` | `51 74 02 94` | bl 0x00bdb200 | `UNCONDITIONAL_CALL`
<a id="insn-00b3e0c0"></a> `00b3e0c0` | `7f 02 14 6b` | cmp w19,w20 | `FALL_THROUGH`
<a id="insn-00b3e0c4"></a> `00b3e0c4` | `e8 27 9f 1a` | cset w8,cc | `FALL_THROUGH`
<a id="insn-00b3e0c8"></a> `00b3e0c8` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00b3e0cc"></a> `00b3e0cc` | `e9 a7 9f 1a` | cset w9,lt | `FALL_THROUGH`
<a id="insn-00b3e0d0"></a> `00b3e0d0` | `08 01 89 1a` | csel w8,w8,w9,eq | `FALL_THROUGH`
<a id="insn-00b3e0d4"></a> `00b3e0d4` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00b3e0d8"></a> `00b3e0d8` | `a1 00 00 54` | b.ne 0x00b3e0ec | `CONDITIONAL_JUMP`
<a id="insn-00b3e0dc"></a> `00b3e0dc` | `d5 02 00 b9` | str w21,[x22] | `FALL_THROUGH`
<a id="insn-00b3e0e0"></a> `00b3e0e0` | `fa 02 00 b9` | str w26,[x23] | `FALL_THROUGH`
<a id="insn-00b3e0e4"></a> `00b3e0e4` | `40 00 80 52` | mov w0,#0x2 | `FALL_THROUGH`
<a id="insn-00b3e0e8"></a> `00b3e0e8` | `04 00 00 14` | b 0x00b3e0f8 | `UNCONDITIONAL_JUMP`
<a id="insn-00b3e0ec"></a> `00b3e0ec` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00b3e0f0"></a> `00b3e0f0` | `02 00 00 14` | b 0x00b3e0f8 | `UNCONDITIONAL_JUMP`
<a id="insn-00b3e0f4"></a> `00b3e0f4` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00b3e0f8"></a> `00b3e0f8` | `fd 7b 46 a9` | ldp x29,x30,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00b3e0fc"></a> `00b3e0fc` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00b3e100"></a> `00b3e100` | `f6 57 44 a9` | ldp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b3e104"></a> `00b3e104` | `f8 5f 43 a9` | ldp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b3e108"></a> `00b3e108` | `fa 67 42 a9` | ldp x26,x25,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b3e10c"></a> `00b3e10c` | `fc 6f 41 a9` | ldp x28,x27,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b3e110"></a> `00b3e110` | `ff c3 01 91` | add sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00b3e114"></a> `00b3e114` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b3decc`](#insn-00b3decc) 範囲 `[['00b3decc', '00b3df6b']]`
  - `FALL_THROUGH` [`00b3df68`](#insn-00b3df68) → [`00b3df6c`](#insn-00b3df6c)
- ブロック [`00b3df6c`](#insn-00b3df6c) 範囲 `[['00b3df6c', '00b3dfbf']]`
  - `CONDITIONAL_JUMP` [`00b3dfbc`](#insn-00b3dfbc) → [`00b3dfd8`](#insn-00b3dfd8)
  - `FALL_THROUGH` [`00b3dfbc`](#insn-00b3dfbc) → [`00b3dfc0`](#insn-00b3dfc0)
- ブロック [`00b3dfc0`](#insn-00b3dfc0) 範囲 `[['00b3dfc0', '00b3dfc3']]`
  - `CONDITIONAL_JUMP` [`00b3dfc0`](#insn-00b3dfc0) → [`00b3e064`](#insn-00b3e064)
  - `FALL_THROUGH` [`00b3dfc0`](#insn-00b3dfc0) → [`00b3dfc4`](#insn-00b3dfc4)
- ブロック [`00b3dfc4`](#insn-00b3dfc4) 範囲 `[['00b3dfc4', '00b3dfd7']]`
  - `UNCONDITIONAL_JUMP` [`00b3dfd4`](#insn-00b3dfd4) → [`00b3e0f8`](#insn-00b3e0f8)
- ブロック [`00b3dfd8`](#insn-00b3dfd8) 範囲 `[['00b3dfd8', '00b3dfdb']]`
  - `CONDITIONAL_JUMP` [`00b3dfd8`](#insn-00b3dfd8) → [`00b3e0f4`](#insn-00b3e0f4)
  - `FALL_THROUGH` [`00b3dfd8`](#insn-00b3dfd8) → [`00b3dfdc`](#insn-00b3dfdc)
- ブロック [`00b3dfdc`](#insn-00b3dfdc) 範囲 `[['00b3dfdc', '00b3e00b']]`
  - `FALL_THROUGH` [`00b3e008`](#insn-00b3e008) → [`00b3e00c`](#insn-00b3e00c)
- ブロック [`00b3e00c`](#insn-00b3e00c) 範囲 `[['00b3e00c', '00b3e03b']]`
  - `FALL_THROUGH` [`00b3e038`](#insn-00b3e038) → [`00b3e03c`](#insn-00b3e03c)
- ブロック [`00b3e03c`](#insn-00b3e03c) 範囲 `[['00b3e03c', '00b3e04b']]`
  - `FALL_THROUGH` [`00b3e048`](#insn-00b3e048) → [`00b3e04c`](#insn-00b3e04c)
- ブロック [`00b3e04c`](#insn-00b3e04c) 範囲 `[['00b3e04c', '00b3e057']]`
  - `CONDITIONAL_JUMP` [`00b3e054`](#insn-00b3e054) → [`00b3e0ec`](#insn-00b3e0ec)
  - `FALL_THROUGH` [`00b3e054`](#insn-00b3e054) → [`00b3e058`](#insn-00b3e058)
- ブロック [`00b3e058`](#insn-00b3e058) 範囲 `[['00b3e058', '00b3e063']]`
  - `UNCONDITIONAL_JUMP` [`00b3e060`](#insn-00b3e060) → [`00b3e0e4`](#insn-00b3e0e4)
- ブロック [`00b3e064`](#insn-00b3e064) 範囲 `[['00b3e064', '00b3e06b']]`
  - `FALL_THROUGH` [`00b3e068`](#insn-00b3e068) → [`00b3e06c`](#insn-00b3e06c)
- ブロック [`00b3e06c`](#insn-00b3e06c) 範囲 `[['00b3e06c', '00b3e0c7']]`
  - `FALL_THROUGH` [`00b3e0c4`](#insn-00b3e0c4) → [`00b3e0c8`](#insn-00b3e0c8)
- ブロック [`00b3e0c8`](#insn-00b3e0c8) 範囲 `[['00b3e0c8', '00b3e0db']]`
  - `CONDITIONAL_JUMP` [`00b3e0d8`](#insn-00b3e0d8) → [`00b3e0ec`](#insn-00b3e0ec)
  - `FALL_THROUGH` [`00b3e0d8`](#insn-00b3e0d8) → [`00b3e0dc`](#insn-00b3e0dc)
- ブロック [`00b3e0dc`](#insn-00b3e0dc) 範囲 `[['00b3e0dc', '00b3e0e3']]`
  - `FALL_THROUGH` [`00b3e0e0`](#insn-00b3e0e0) → [`00b3e0e4`](#insn-00b3e0e4)
- ブロック [`00b3e0e4`](#insn-00b3e0e4) 範囲 `[['00b3e0e4', '00b3e0eb']]`
  - `UNCONDITIONAL_JUMP` [`00b3e0e8`](#insn-00b3e0e8) → [`00b3e0f8`](#insn-00b3e0f8)
- ブロック [`00b3e0ec`](#insn-00b3e0ec) 範囲 `[['00b3e0ec', '00b3e0f3']]`
  - `UNCONDITIONAL_JUMP` [`00b3e0f0`](#insn-00b3e0f0) → [`00b3e0f8`](#insn-00b3e0f8)
- ブロック [`00b3e0f4`](#insn-00b3e0f4) 範囲 `[['00b3e0f4', '00b3e0f7']]`
  - `FALL_THROUGH` [`00b3e0f4`](#insn-00b3e0f4) → [`00b3e0f8`](#insn-00b3e0f8)
- ブロック [`00b3e0f8`](#insn-00b3e0f8) 範囲 `[['00b3e0f8', '00b3e117']]`

## 命令位置別の参照

- [`00b3ded0`](#insn-00b3ded0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3ded4`](#insn-00b3ded4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3ded8`](#insn-00b3ded8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3dedc`](#insn-00b3dedc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3dee0`](#insn-00b3dee0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3dee4`](#insn-00b3dee4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3def8`](#insn-00b3def8) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3df54`](#insn-00b3df54) → [`00bdb200`](../00bdb/00bdb200.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb200` · 推定シンボル `None` · 推定型 `None`
- [`00b3dfa4`](#insn-00b3dfa4) → [`00bdb200`](../00bdb/00bdb200.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb200` · 推定シンボル `None` · 推定型 `None`
- [`00b3dfbc`](#insn-00b3dfbc) → [`00b3dfd8`](#insn-00b3dfd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3dfc0`](#insn-00b3dfc0) → [`00b3e064`](#insn-00b3e064) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3dfc4`](#insn-00b3dfc4) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3dfd4`](#insn-00b3dfd4) → [`00b3e0f8`](#insn-00b3e0f8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3dfd8`](#insn-00b3dfd8) → [`00b3e0f4`](#insn-00b3e0f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3dfdc`](#insn-00b3dfdc) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3e038`](#insn-00b3e038) → [`00bdb200`](../00bdb/00bdb200.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb200` · 推定シンボル `None` · 推定型 `None`
- [`00b3e054`](#insn-00b3e054) → [`00b3e0ec`](#insn-00b3e0ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3e060`](#insn-00b3e060) → [`00b3e0e4`](#insn-00b3e0e4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3e064`](#insn-00b3e064) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3e0bc`](#insn-00b3e0bc) → [`00bdb200`](../00bdb/00bdb200.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb200` · 推定シンボル `None` · 推定型 `None`
- [`00b3e0d8`](#insn-00b3e0d8) → [`00b3e0ec`](#insn-00b3e0ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3e0e8`](#insn-00b3e0e8) → [`00b3e0f8`](#insn-00b3e0f8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3e0f0`](#insn-00b3e0f0) → [`00b3e0f8`](#insn-00b3e0f8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3e0f8`](#insn-00b3e0f8) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3e0fc`](#insn-00b3e0fc) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3e100`](#insn-00b3e100) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3e104`](#insn-00b3e104) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3e108`](#insn-00b3e108) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3e10c`](#insn-00b3e10c) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b3ded0`](#insn-00b3ded0)

~~~json
{
  "source": "00b3ded0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3ded4`](#insn-00b3ded4)

~~~json
{
  "source": "00b3ded4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3ded8`](#insn-00b3ded8)

~~~json
{
  "source": "00b3ded8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3dedc`](#insn-00b3dedc)

~~~json
{
  "source": "00b3dedc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3dee0`](#insn-00b3dee0)

~~~json
{
  "source": "00b3dee0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3dee4`](#insn-00b3dee4)

~~~json
{
  "source": "00b3dee4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3def8`](#insn-00b3def8)

~~~json
{
  "source": "00b3def8",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3df54`](#insn-00b3df54)

~~~json
{
  "source": "00b3df54",
  "target": "00bdb200",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b3dfa4`](#insn-00b3dfa4)

~~~json
{
  "source": "00b3dfa4",
  "target": "00bdb200",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b3dfbc`](#insn-00b3dfbc)

~~~json
{
  "source": "00b3dfbc",
  "target": "00b3dfd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3dfc0`](#insn-00b3dfc0)

~~~json
{
  "source": "00b3dfc0",
  "target": "00b3e064",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3dfc4`](#insn-00b3dfc4)

~~~json
{
  "source": "00b3dfc4",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3dfd4`](#insn-00b3dfd4)

~~~json
{
  "source": "00b3dfd4",
  "target": "00b3e0f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3dfd8`](#insn-00b3dfd8)

~~~json
{
  "source": "00b3dfd8",
  "target": "00b3e0f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3dfdc`](#insn-00b3dfdc)

~~~json
{
  "source": "00b3dfdc",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3e038`](#insn-00b3e038)

~~~json
{
  "source": "00b3e038",
  "target": "00bdb200",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b3e054`](#insn-00b3e054)

~~~json
{
  "source": "00b3e054",
  "target": "00b3e0ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3e060`](#insn-00b3e060)

~~~json
{
  "source": "00b3e060",
  "target": "00b3e0e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3e064`](#insn-00b3e064)

~~~json
{
  "source": "00b3e064",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3e0bc`](#insn-00b3e0bc)

~~~json
{
  "source": "00b3e0bc",
  "target": "00bdb200",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b3e0d8`](#insn-00b3e0d8)

~~~json
{
  "source": "00b3e0d8",
  "target": "00b3e0ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3e0e8`](#insn-00b3e0e8)

~~~json
{
  "source": "00b3e0e8",
  "target": "00b3e0f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3e0f0`](#insn-00b3e0f0)

~~~json
{
  "source": "00b3e0f0",
  "target": "00b3e0f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3e0f8`](#insn-00b3e0f8)

~~~json
{
  "source": "00b3e0f8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3e0fc`](#insn-00b3e0fc)

~~~json
{
  "source": "00b3e0fc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3e100`](#insn-00b3e100)

~~~json
{
  "source": "00b3e100",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3e104`](#insn-00b3e104)

~~~json
{
  "source": "00b3e104",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3e108`](#insn-00b3e108)

~~~json
{
  "source": "00b3e108",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3e10c`](#insn-00b3e10c)

~~~json
{
  "source": "00b3e10c",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
