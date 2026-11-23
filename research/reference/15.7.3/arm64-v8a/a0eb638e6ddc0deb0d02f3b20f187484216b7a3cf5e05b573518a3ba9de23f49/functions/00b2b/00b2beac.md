# 00b2beac

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00b2bde4`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b2b/00b2bde4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0065.md#compare-f9e0a888eec40746c1adb9a7d8ec8f49)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b2bef0`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2b/00b2bef0.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0010.md#compare-c3b67aa37fa73d524951b81355aa98fc)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b2beac",
  "name": "_ZN11flatbuffers7EnumDef11DeserializeERNS_6ParserEPKN10reflection4EnumE",
  "size": 856,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f85e2623cfb1fb00ff5f384fb5301e27bff597763a2bd0f674f6024775d3792e",
  "source_text_sha256": "f85e2623cfb1fb00ff5f384fb5301e27bff597763a2bd0f674f6024775d3792e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b2beac",
        "00b2c203"
      ]
    ],
    "bytes_sha256": "4cc7f5e5c8ccf178aef818e0377dcbcd681b5f5944fceb2a7c4f8ef88630ea8d",
    "instruction_count": 214,
    "instruction_bytes": 856,
    "body_bytes": 856,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bdfa10](../00bdf/00bdfa10.md)

## 呼び出し先

- [00bdaff0](../00bda/00bdaff0.md)
- [00bdb010](../00bdb/00bdb010.md)
- [00bdb040](../00bdb/00bdb040.md)
- [00bdb160](../00bdb/00bdb160.md)
- [00bdf100](../00bdf/00bdf100.md)
- [00bdf1f0](../00bdf/00bdf1f0.md)
- [00bdf260](../00bdf/00bdf260.md)
- [00bdf630](../00bdf/00bdf630.md)
- [00bdf860](../00bdf/00bdf860.md)
- [00bdfa30](../00bdf/00bdfa30.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 9255 bytes

~~~c

void _ZN11flatbuffers7EnumDef11DeserializeERNS_6ParserEPKN10reflection4EnumE
               (byte *param_1,undefined8 param_2,int *param_3)

{
  uint *puVar1;
  ushort *puVar2;
  uint uVar3;
  byte bVar4;
  ushort uVar5;
  long lVar6;
  bool bVar7;
  byte *__ptr;
  byte *pbVar8;
  undefined8 uVar9;
  long lVar10;
  byte *pbVar11;
  byte *pbVar12;
  ulong uVar13;
  void *__dest;
  ulong uVar14;
  int *piVar15;
  ulong uVar16;
  ulong local_98;
  ulong local_90;
  void *local_88;
  undefined8 local_80;
  undefined8 uStack_78;
  undefined8 local_70;
  long local_68;
  
                    /* try { // try from 00b2beb0 to 00c2bebb has its CatchHandler @ 00b2c2a0 */
                    /* try { // try from 00b2bebc to 00c2bf53 has its CatchHandler @ 00b2bab0 */
  lVar6 = tpidr_el0;
  local_68 = *(long *)(lVar6 + 0x28);
  puVar1 = (uint *)((long)param_3 + (ulong)*(ushort *)((long)param_3 + (4 - (long)*param_3)));
  puVar1 = (uint *)((long)puVar1 + (ulong)*puVar1);
  uVar3 = *puVar1;
  uVar13 = (ulong)uVar3;
  local_90 = 0;
  local_88 = (void *)0x0;
  local_98 = 0;
  if (uVar3 < 0x17) {
    __dest = (void *)((ulong)&local_98 | 1);
    local_98 = (ulong)(byte)(uVar3 << 1);
    if (uVar3 != 0) goto LAB_00b2bf48;
  }
  else {
    uVar16 = uVar13 + 0x10 & 0x1fffffff0;
    __dest = (void *)_Znwm(uVar16);
    local_98 = uVar16 | 1;
    local_90 = uVar13;
    local_88 = __dest;
LAB_00b2bf48:
                    /* try { // try from 00b2bf54 to 00c2bf67 has its CatchHandler @ 00b2c298 */
    memcpy(__dest,puVar1 + 1,uVar13);
  }
  *(undefined1 *)((long)__dest + uVar13) = 0;
  _ZN11flatbuffers6Parser15UnqualifiedNameERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
            (&local_80,param_2,&local_98);
                    /* try { // try from 00b2bf70 to 00c2bf7b has its CatchHandler @ 00b2c294 */
  if ((*param_1 & 1) == 0) {
    param_1[0] = 0;
    param_1[1] = 0;
  }
  else {
    **(undefined1 **)(param_1 + 0x10) = 0;
    param_1[8] = 0;
    param_1[9] = 0;
    param_1[10] = 0;
    param_1[0xb] = 0;
    param_1[0xc] = 0;
    param_1[0xd] = 0;
    param_1[0xe] = 0;
    param_1[0xf] = 0;
    if ((*param_1 & 1) != 0) {
      _ZdlPv(*(void **)(param_1 + 0x10));
                    /* try { // try from 00b2bf98 to 00c2bfab has its CatchHandler @ 00b2c284 */
      param_1[0] = 0;
      param_1[1] = 0;
      param_1[2] = 0;
      param_1[3] = 0;
      param_1[4] = 0;
      param_1[5] = 0;
      param_1[6] = 0;
      param_1[7] = 0;
    }
  }
  *(undefined8 *)(param_1 + 0x10) = local_70;
  *(undefined8 *)(param_1 + 8) = uStack_78;
  *(undefined8 *)param_1 = local_80;
  uStack_78 = 0;
  local_70 = 0;
                    /* try { // try from 00b2bfb4 to 00c2bfbf has its CatchHandler @ 00b2c27c */
  local_80 = 0;
  if ((local_98 & 1) != 0) {
                    /* try { // try from 00b2bfc0 to 00c2c07b has its CatchHandler @ 00b2bab0 */
    _ZdlPv(local_88);
  }
  lVar10 = (long)*param_3;
  uVar13 = (ulong)*(ushort *)((long)param_3 + (6 - lVar10));
  uVar16 = (ulong)*(uint *)((long)param_3 + uVar13);
  if (*(int *)((long)((long)param_3 + uVar13) + uVar16) != 0) {
    uVar14 = 0;
    piVar15 = param_3;
    do {
      piVar15 = piVar15 + 1;
      __ptr = (byte *)_Znwm(0x58);
      __ptr[0x50] = 0;
      __ptr[0x51] = 0;
      __ptr[0x52] = 0;
      __ptr[0x53] = 0;
      __ptr[0x54] = 0;
      __ptr[0x55] = 0;
      __ptr[0x56] = 0;
      __ptr[0x57] = 0;
      __ptr[8] = 0;
      __ptr[9] = 0;
      __ptr[10] = 0;
      __ptr[0xb] = 0;
      __ptr[0xc] = 0;
      __ptr[0xd] = 0;
      __ptr[0xe] = 0;
      __ptr[0xf] = 0;
      __ptr[0] = 0;
      __ptr[1] = 0;
      __ptr[2] = 0;
      __ptr[3] = 0;
      __ptr[4] = 0;
      __ptr[5] = 0;
      __ptr[6] = 0;
      __ptr[7] = 0;
      __ptr[0x18] = 0;
      __ptr[0x19] = 0;
      __ptr[0x1a] = 0;
      __ptr[0x1b] = 0;
      __ptr[0x1c] = 0;
      __ptr[0x1d] = 0;
      __ptr[0x1e] = 0;
      __ptr[0x1f] = 0;
      __ptr[0x10] = 0;
      __ptr[0x11] = 0;
      __ptr[0x12] = 0;
      __ptr[0x13] = 0;
      __ptr[0x14] = 0;
      __ptr[0x15] = 0;
      __ptr[0x16] = 0;
      __ptr[0x17] = 0;
      __ptr[0x28] = 0;
      __ptr[0x29] = 0;
      __ptr[0x2a] = 0;
      __ptr[0x2b] = 0;
      __ptr[0x2c] = 0;
      __ptr[0x2d] = 0;
      __ptr[0x2e] = 0;
      __ptr[0x2f] = 0;
      __ptr[0x20] = 0;
      __ptr[0x21] = 0;
      __ptr[0x22] = 0;
      __ptr[0x23] = 0;
      __ptr[0x24] = 0;
      __ptr[0x25] = 0;
      __ptr[0x26] = 0;
      __ptr[0x27] = 0;
      __ptr[0x38] = 0;
      __ptr[0x39] = 0;
      __ptr[0x3a] = 0;
      __ptr[0x3b] = 0;
      __ptr[0x3c] = 0;
      __ptr[0x3d] = 0;
      __ptr[0x3e] = 0;
      __ptr[0x3f] = 0;
      __ptr[0x30] = 0;
      __ptr[0x31] = 0;
      __ptr[0x32] = 0;
      __ptr[0x33] = 0;
      __ptr[0x34] = 0;
      __ptr[0x35] = 0;
      __ptr[0x36] = 0;
      __ptr[0x37] = 0;
      __ptr[0x42] = 0;
      __ptr[0x43] = 0;
      __ptr[0x44] = 0;
      __ptr[0x45] = 0;
      __ptr[0x46] = 0;
      __ptr[0x47] = 0;
      __ptr[0x48] = 0;
      __ptr[0x49] = 0;
      __ptr[0x3a] = 0;
      __ptr[0x3b] = 0;
      __ptr[0x3c] = 0;
      __ptr[0x3d] = 0;
      __ptr[0x3e] = 0;
      __ptr[0x3f] = 0;
      __ptr[0x40] = 0;
      __ptr[0x41] = 0;
      uVar13 = _ZN11flatbuffers7EnumVal11DeserializeERKNS_6ParserEPKN10reflection7EnumValE
                         (__ptr,param_2,
                          (long)piVar15 +
                          (ulong)*(uint *)((long)piVar15 + uVar13 + uVar16) + uVar13 + uVar16);
      if (((uVar13 & 1) == 0) ||
         (uVar13 = _ZN11flatbuffers11SymbolTableINS_7EnumValEE3AddERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEPS1_
                             (param_1 + 0xb8,__ptr,__ptr), (uVar13 & 1) != 0)) {
        pbVar12 = *(byte **)(__ptr + 0x18);
        if (pbVar12 != (byte *)0x0) {
          pbVar11 = *(byte **)(__ptr + 0x20);
          pbVar8 = pbVar12;
          if (pbVar11 != pbVar12) {
            bVar4 = pbVar11[-0x18];
            pbVar8 = pbVar11 + -0x18;
            while( true ) {
              if ((bVar4 & 1) != 0) {
                _ZdlPv(*(void **)(pbVar11 + -8));
              }
              if (pbVar12 == pbVar8) break;
              bVar4 = pbVar8[-0x18];
              pbVar11 = pbVar8;
              pbVar8 = pbVar8 + -0x18;
            }
            pbVar8 = *(byte **)(__ptr + 0x18);
          }
          *(byte **)(__ptr + 0x20) = pbVar12;
          _ZdlPv(pbVar8);
        }
        if ((*__ptr & 1) != 0) {
          _ZdlPv(*(void **)(__ptr + 0x10));
        }
        _ZdlPv(__ptr);
        uVar9 = 0;
        goto LAB_00b2c1d0;
      }
      lVar10 = (long)*param_3;
      uVar14 = uVar14 + 1;
      uVar13 = (ulong)*(ushort *)((long)param_3 + (6 - lVar10));
      uVar16 = (ulong)*(uint *)((long)param_3 + uVar13);
    } while (uVar14 < *(uint *)((long)((long)param_3 + uVar13) + uVar16));
  }
  puVar2 = (ushort *)((long)param_3 - lVar10);
  uVar5 = *puVar2;
  if (uVar5 < 9) {
    lVar10 = 0;
    param_1[0x94] = 0;
  }
  else {
                    /* try { // try from 00b2c07c to 00c2c08f has its CatchHandler @ 00b2c274 */
    bVar7 = false;
    if ((ulong)puVar2[4] != 0) {
      bVar7 = *(char *)((long)param_3 + (ulong)puVar2[4]) != '\0';
    }
                    /* try { // try from 00b2c098 to 00c2c0a3 has its CatchHandler @ 00b2c270 */
    param_1[0x94] = bVar7;
                    /* try { // try from 00b2c0a4 to 00c2c14f has its CatchHandler @ 00b2bab0 */
    if ((uVar5 < 0xb) || ((ulong)puVar2[5] == 0)) {
      lVar10 = 0;
    }
    else {
      puVar1 = (uint *)((long)param_3 + (ulong)puVar2[5]);
      lVar10 = (long)puVar1 + (ulong)*puVar1;
    }
  }
  uVar13 = _ZN11flatbuffers4Type11DeserializeERKNS_6ParserEPKN10reflection4TypeE
                     (param_1 + 0x98,param_2,lVar10);
  if ((uVar13 & 1) != 0) {
    if ((*(ushort *)((long)param_3 - (long)*param_3) < 0xd) ||
       (uVar13 = (ulong)((ushort *)((long)param_3 - (long)*param_3))[6], uVar13 == 0)) {
      lVar10 = 0;
    }
    else {
      puVar1 = (uint *)((long)param_3 + uVar13);
      lVar10 = (long)puVar1 + (ulong)*puVar1;
    }
                    /* try { // try from 00b2c150 to 00c2c187 has its CatchHandler @ 00b2c304 */
    uVar13 = _ZN11flatbuffers10Definition21DeserializeAttributesERNS_6ParserEPKNS_6VectorINS_6OffsetIN10reflection8KeyValueEEEEE
                       (param_1,param_2,lVar10);
    if ((uVar13 & 1) != 0) {
      if ((*(ushort *)((long)param_3 - (long)*param_3) < 0xf) ||
         (uVar13 = (ulong)((ushort *)((long)param_3 - (long)*param_3))[7], uVar13 == 0)) {
        lVar10 = 0;
      }
      else {
        puVar1 = (uint *)((long)param_3 + uVar13);
        lVar10 = (long)puVar1 + (ulong)*puVar1;
      }
      _ZN11flatbuffers14DeserializeDocERNSt6__ndk16vectorINS0_12basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEENS5_IS7_EEEEPKNS_6VectorINS_6OffsetINS_6StringEEEEE
                (param_1 + 0x30,lVar10);
      uVar9 = 1;
      goto LAB_00b2c1d0;
    }
  }
                    /* try { // try from 00b2c188 to 00c2c36b has its CatchHandler @ 00b2bab0 */
  uVar9 = 0;
LAB_00b2c1d0:
  if (*(long *)(lVar6 + 0x28) == local_68) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail(uVar9);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b2beac"></a> `00b2beac` | `ff 83 02 d1` | sub sp,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-00b2beb0"></a> `00b2beb0` | `fc 6f 04 a9` | stp x28,x27,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b2beb4"></a> `00b2beb4` | `fa 67 05 a9` | stp x26,x25,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00b2beb8"></a> `00b2beb8` | `f8 5f 06 a9` | stp x24,x23,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00b2bebc"></a> `00b2bebc` | `f6 57 07 a9` | stp x22,x21,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00b2bec0"></a> `00b2bec0` | `f4 4f 08 a9` | stp x20,x19,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00b2bec4"></a> `00b2bec4` | `fd 7b 09 a9` | stp x29,x30,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00b2bec8"></a> `00b2bec8` | `fd 43 02 91` | add x29,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00b2becc"></a> `00b2becc` | `5a d0 3b d5` | mrs x26,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00b2bed0"></a> `00b2bed0` | `48 17 40 f9` | ldr x8,[x26, #0x28] | `FALL_THROUGH`
<a id="insn-00b2bed4"></a> `00b2bed4` | `f3 03 02 aa` | mov x19,x2 | `FALL_THROUGH`
<a id="insn-00b2bed8"></a> `00b2bed8` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-00b2bedc"></a> `00b2bedc` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00b2bee0"></a> `00b2bee0` | `e8 1f 00 f9` | str x8,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00b2bee4"></a> `00b2bee4` | `48 00 80 b9` | ldrsw x8,[x2] | `FALL_THROUGH`
<a id="insn-00b2bee8"></a> `00b2bee8` | `48 00 08 cb` | sub x8,x2,x8 | `FALL_THROUGH`
<a id="insn-00b2beec"></a> `00b2beec` | `08 09 40 79` | ldrh w8,[x8, #0x4] | `FALL_THROUGH`
<a id="insn-00b2bef0"></a> `00b2bef0` | `48 00 08 8b` | add x8,x2,x8 | `FALL_THROUGH`
<a id="insn-00b2bef4"></a> `00b2bef4` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00b2bef8"></a> `00b2bef8` | `17 01 09 8b` | add x23,x8,x9 | `FALL_THROUGH`
<a id="insn-00b2befc"></a> `00b2befc` | `f6 46 40 b8` | ldr w22,[x23], #0x4 | `FALL_THROUGH`
<a id="insn-00b2bf00"></a> `00b2bf00` | `ff 7f 01 a9` | stp xzr,xzr,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b2bf04"></a> `00b2bf04` | `ff 07 00 f9` | str xzr,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00b2bf08"></a> `00b2bf08` | `df 5e 00 71` | cmp w22,#0x17 | `FALL_THROUGH`
<a id="insn-00b2bf0c"></a> `00b2bf0c` | `e2 00 00 54` | b.cs 0x00b2bf28 | `CONDITIONAL_JUMP`
<a id="insn-00b2bf10"></a> `00b2bf10` | `e9 23 00 91` | add x9,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00b2bf14"></a> `00b2bf14` | `c8 7a 1f 53` | lsl w8,w22,#0x1 | `FALL_THROUGH`
<a id="insn-00b2bf18"></a> `00b2bf18` | `38 01 40 b2` | orr x24,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00b2bf1c"></a> `00b2bf1c` | `e8 23 00 39` | strb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00b2bf20"></a> `00b2bf20` | `56 01 00 35` | cbnz w22,0x00b2bf48 | `CONDITIONAL_JUMP`
<a id="insn-00b2bf24"></a> `00b2bf24` | `0d 00 00 14` | b 0x00b2bf58 | `UNCONDITIONAL_JUMP`
<a id="insn-00b2bf28"></a> `00b2bf28` | `c8 42 00 91` | add x8,x22,#0x10 | `FALL_THROUGH`
<a id="insn-00b2bf2c"></a> `00b2bf2c` | `19 71 7c 92` | and x25,x8,#0x1fffffff0 | `FALL_THROUGH`
<a id="insn-00b2bf30"></a> `00b2bf30` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-00b2bf34"></a> `00b2bf34` | `2f bc 02 94` | bl 0x00bdaff0 | `UNCONDITIONAL_CALL`
<a id="insn-00b2bf38"></a> `00b2bf38` | `28 03 40 b2` | orr x8,x25,#0x1 | `FALL_THROUGH`
<a id="insn-00b2bf3c"></a> `00b2bf3c` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-00b2bf40"></a> `00b2bf40` | `e8 db 00 a9` | stp x8,x22,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00b2bf44"></a> `00b2bf44` | `e0 0f 00 f9` | str x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00b2bf48"></a> `00b2bf48` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00b2bf4c"></a> `00b2bf4c` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-00b2bf50"></a> `00b2bf50` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00b2bf54"></a> `00b2bf54` | `83 bc 02 94` | bl 0x00bdb160 | `UNCONDITIONAL_CALL`
<a id="insn-00b2bf58"></a> `00b2bf58` | `e8 83 00 91` | add x8,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00b2bf5c"></a> `00b2bf5c` | `e1 23 00 91` | add x1,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00b2bf60"></a> `00b2bf60` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00b2bf64"></a> `00b2bf64` | `1f 6b 36 38` | strb wzr,[x24, x22, LSL ] | `FALL_THROUGH`
<a id="insn-00b2bf68"></a> `00b2bf68` | `3e ce 02 94` | bl 0x00bdf860 | `UNCONDITIONAL_CALL`
<a id="insn-00b2bf6c"></a> `00b2bf6c` | `88 02 40 39` | ldrb w8,[x20] | `FALL_THROUGH`
<a id="insn-00b2bf70"></a> `00b2bf70` | `68 00 00 37` | tbnz w8,#0x0,0x00b2bf7c | `CONDITIONAL_JUMP`
<a id="insn-00b2bf74"></a> `00b2bf74` | `9f 02 00 79` | strh wzr,[x20] | `FALL_THROUGH`
<a id="insn-00b2bf78"></a> `00b2bf78` | `09 00 00 14` | b 0x00b2bf9c | `UNCONDITIONAL_JUMP`
<a id="insn-00b2bf7c"></a> `00b2bf7c` | `88 0a 40 f9` | ldr x8,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00b2bf80"></a> `00b2bf80` | `1f 01 00 39` | strb wzr,[x8] | `FALL_THROUGH`
<a id="insn-00b2bf84"></a> `00b2bf84` | `88 02 40 39` | ldrb w8,[x20] | `FALL_THROUGH`
<a id="insn-00b2bf88"></a> `00b2bf88` | `9f 06 00 f9` | str xzr,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00b2bf8c"></a> `00b2bf8c` | `88 00 00 36` | tbz w8,#0x0,0x00b2bf9c | `CONDITIONAL_JUMP`
<a id="insn-00b2bf90"></a> `00b2bf90` | `80 0a 40 f9` | ldr x0,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00b2bf94"></a> `00b2bf94` | `1f bc 02 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00b2bf98"></a> `00b2bf98` | `9f 02 00 f9` | str xzr,[x20] | `FALL_THROUGH`
<a id="insn-00b2bf9c"></a> `00b2bf9c` | `e8 1b 40 f9` | ldr x8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b2bfa0"></a> `00b2bfa0` | `e0 0b c0 3d` | ldr q0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b2bfa4"></a> `00b2bfa4` | `88 0a 00 f9` | str x8,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00b2bfa8"></a> `00b2bfa8` | `80 02 80 3d` | str q0,[x20] | `FALL_THROUGH`
<a id="insn-00b2bfac"></a> `00b2bfac` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00b2bfb0"></a> `00b2bfb0` | `ff ff 02 a9` | stp xzr,xzr,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00b2bfb4"></a> `00b2bfb4` | `ff 13 00 f9` | str xzr,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b2bfb8"></a> `00b2bfb8` | `68 00 00 36` | tbz w8,#0x0,0x00b2bfc4 | `CONDITIONAL_JUMP`
<a id="insn-00b2bfbc"></a> `00b2bfbc` | `e0 0f 40 f9` | ldr x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00b2bfc0"></a> `00b2bfc0` | `14 bc 02 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00b2bfc4"></a> `00b2bfc4` | `68 02 80 b9` | ldrsw x8,[x19] | `FALL_THROUGH`
<a id="insn-00b2bfc8"></a> `00b2bfc8` | `69 02 08 cb` | sub x9,x19,x8 | `FALL_THROUGH`
<a id="insn-00b2bfcc"></a> `00b2bfcc` | `3b 0d 40 79` | ldrh w27,[x9, #0x6] | `FALL_THROUGH`
<a id="insn-00b2bfd0"></a> `00b2bfd0` | `69 02 1b 8b` | add x9,x19,x27 | `FALL_THROUGH`
<a id="insn-00b2bfd4"></a> `00b2bfd4` | `3c 01 40 b9` | ldr w28,[x9] | `FALL_THROUGH`
<a id="insn-00b2bfd8"></a> `00b2bfd8` | `29 69 7c b8` | ldr w9,[x9, x28, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00b2bfdc"></a> `00b2bfdc` | `69 04 00 34` | cbz w9,0x00b2c068 | `CONDITIONAL_JUMP`
<a id="insn-00b2bfe0"></a> `00b2bfe0` | `f8 03 1f aa` | mov x24,xzr | `FALL_THROUGH`
<a id="insn-00b2bfe4"></a> `00b2bfe4` | `97 e2 02 91` | add x23,x20,#0xb8 | `FALL_THROUGH`
<a id="insn-00b2bfe8"></a> `00b2bfe8` | `79 12 00 91` | add x25,x19,#0x4 | `FALL_THROUGH`
<a id="insn-00b2bfec"></a> `00b2bfec` | `00 0b 80 52` | mov w0,#0x58 | `FALL_THROUGH`
<a id="insn-00b2bff0"></a> `00b2bff0` | `00 bc 02 94` | bl 0x00bdaff0 | `UNCONDITIONAL_CALL`
<a id="insn-00b2bff4"></a> `00b2bff4` | `00 e4 00 6f` | movi v0.2D,#0x0 | `FALL_THROUGH`
<a id="insn-00b2bff8"></a> `00b2bff8` | `68 3f 40 92` | and x8,x27,#0xffff | `FALL_THROUGH`
<a id="insn-00b2bffc"></a> `00b2bffc` | `1f 28 00 f9` | str xzr,[x0, #0x50] | `FALL_THROUGH`
<a id="insn-00b2c000"></a> `00b2c000` | `00 00 00 ad` | stp q0,q0,[x0] | `FALL_THROUGH`
<a id="insn-00b2c004"></a> `00b2c004` | `00 00 01 ad` | stp q0,q0,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00b2c008"></a> `00b2c008` | `00 a0 83 3c` | stur q0,[x0, #0x3a] | `FALL_THROUGH`
<a id="insn-00b2c00c"></a> `00b2c00c` | `08 41 3c 8b` | add x8,x8,w28, UXTW  | `FALL_THROUGH`
<a id="insn-00b2c010"></a> `00b2c010` | `29 6b 68 b8` | ldr w9,[x25, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00b2c014"></a> `00b2c014` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00b2c018"></a> `00b2c018` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00b2c01c"></a> `00b2c01c` | `28 01 08 8b` | add x8,x9,x8 | `FALL_THROUGH`
<a id="insn-00b2c020"></a> `00b2c020` | `22 03 08 8b` | add x2,x25,x8 | `FALL_THROUGH`
<a id="insn-00b2c024"></a> `00b2c024` | `83 ce 02 94` | bl 0x00bdfa30 | `UNCONDITIONAL_CALL`
<a id="insn-00b2c028"></a> `00b2c028` | `80 04 00 36` | tbz w0,#0x0,0x00b2c0b8 | `CONDITIONAL_JUMP`
<a id="insn-00b2c02c"></a> `00b2c02c` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00b2c030"></a> `00b2c030` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00b2c034"></a> `00b2c034` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00b2c038"></a> `00b2c038` | `6e cc 02 94` | bl 0x00bdf1f0 | `UNCONDITIONAL_CALL`
<a id="insn-00b2c03c"></a> `00b2c03c` | `e0 03 00 37` | tbnz w0,#0x0,0x00b2c0b8 | `CONDITIONAL_JUMP`
<a id="insn-00b2c040"></a> `00b2c040` | `68 02 80 b9` | ldrsw x8,[x19] | `FALL_THROUGH`
<a id="insn-00b2c044"></a> `00b2c044` | `18 07 00 91` | add x24,x24,#0x1 | `FALL_THROUGH`
<a id="insn-00b2c048"></a> `00b2c048` | `39 13 00 91` | add x25,x25,#0x4 | `FALL_THROUGH`
<a id="insn-00b2c04c"></a> `00b2c04c` | `69 02 08 cb` | sub x9,x19,x8 | `FALL_THROUGH`
<a id="insn-00b2c050"></a> `00b2c050` | `3b 0d 40 79` | ldrh w27,[x9, #0x6] | `FALL_THROUGH`
<a id="insn-00b2c054"></a> `00b2c054` | `69 02 1b 8b` | add x9,x19,x27 | `FALL_THROUGH`
<a id="insn-00b2c058"></a> `00b2c058` | `3c 01 40 b9` | ldr w28,[x9] | `FALL_THROUGH`
<a id="insn-00b2c05c"></a> `00b2c05c` | `29 69 7c b8` | ldr w9,[x9, x28, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00b2c060"></a> `00b2c060` | `1f 03 09 eb` | cmp x24,x9 | `FALL_THROUGH`
<a id="insn-00b2c064"></a> `00b2c064` | `43 fc ff 54` | b.cc 0x00b2bfec | `CONDITIONAL_JUMP`
<a id="insn-00b2c068"></a> `00b2c068` | `e8 03 08 cb` | neg x8,x8 | `FALL_THROUGH`
<a id="insn-00b2c06c"></a> `00b2c06c` | `68 02 08 8b` | add x8,x19,x8 | `FALL_THROUGH`
<a id="insn-00b2c070"></a> `00b2c070` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00b2c074"></a> `00b2c074` | `3f 21 00 71` | cmp w9,#0x8 | `FALL_THROUGH`
<a id="insn-00b2c078"></a> `00b2c078` | `09 04 00 54` | b.ls 0x00b2c0f8 | `CONDITIONAL_JUMP`
<a id="insn-00b2c07c"></a> `00b2c07c` | `0a 11 40 79` | ldrh w10,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00b2c080"></a> `00b2c080` | `8a 00 00 b4` | cbz x10,0x00b2c090 | `CONDITIONAL_JUMP`
<a id="insn-00b2c084"></a> `00b2c084` | `6a 6a 6a 38` | ldrb w10,[x19, x10, LSL ] | `FALL_THROUGH`
<a id="insn-00b2c088"></a> `00b2c088` | `5f 01 00 71` | cmp w10,#0x0 | `FALL_THROUGH`
<a id="insn-00b2c08c"></a> `00b2c08c` | `ea 07 9f 1a` | cset w10,ne | `FALL_THROUGH`
<a id="insn-00b2c090"></a> `00b2c090` | `3f 2d 00 71` | cmp w9,#0xb | `FALL_THROUGH`
<a id="insn-00b2c094"></a> `00b2c094` | `80 62 02 91` | add x0,x20,#0x98 | `FALL_THROUGH`
<a id="insn-00b2c098"></a> `00b2c098` | `8a 52 02 39` | strb w10,[x20, #0x94] | `FALL_THROUGH`
<a id="insn-00b2c09c"></a> `00b2c09c` | `63 03 00 54` | b.cc 0x00b2c108 | `CONDITIONAL_JUMP`
<a id="insn-00b2c0a0"></a> `00b2c0a0` | `08 15 40 79` | ldrh w8,[x8, #0xa] | `FALL_THROUGH`
<a id="insn-00b2c0a4"></a> `00b2c0a4` | `28 03 00 b4` | cbz x8,0x00b2c108 | `CONDITIONAL_JUMP`
<a id="insn-00b2c0a8"></a> `00b2c0a8` | `68 02 08 8b` | add x8,x19,x8 | `FALL_THROUGH`
<a id="insn-00b2c0ac"></a> `00b2c0ac` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00b2c0b0"></a> `00b2c0b0` | `02 01 09 8b` | add x2,x8,x9 | `FALL_THROUGH`
<a id="insn-00b2c0b4"></a> `00b2c0b4` | `16 00 00 14` | b 0x00b2c10c | `UNCONDITIONAL_JUMP`
<a id="insn-00b2c0b8"></a> `00b2c0b8` | `d3 0e 40 f9` | ldr x19,[x22, #0x18] | `FALL_THROUGH`
<a id="insn-00b2c0bc"></a> `00b2c0bc` | `53 07 00 b4` | cbz x19,0x00b2c1a4 | `CONDITIONAL_JUMP`
<a id="insn-00b2c0c0"></a> `00b2c0c0` | `c8 12 40 f9` | ldr x8,[x22, #0x20] | `FALL_THROUGH`
<a id="insn-00b2c0c4"></a> `00b2c0c4` | `1f 01 13 eb` | cmp x8,x19 | `FALL_THROUGH`
<a id="insn-00b2c0c8"></a> `00b2c0c8` | `80 06 00 54` | b.eq 0x00b2c198 | `CONDITIONAL_JUMP`
<a id="insn-00b2c0cc"></a> `00b2c0cc` | `f4 03 08 aa` | mov x20,x8 | `FALL_THROUGH`
<a id="insn-00b2c0d0"></a> `00b2c0d0` | `89 8e 5e 38` | ldrb w9,[x20, #-0x18]! | `FALL_THROUGH`
<a id="insn-00b2c0d4"></a> `00b2c0d4` | `c9 00 00 37` | tbnz w9,#0x0,0x00b2c0ec | `CONDITIONAL_JUMP`
<a id="insn-00b2c0d8"></a> `00b2c0d8` | `7f 02 14 eb` | cmp x19,x20 | `FALL_THROUGH`
<a id="insn-00b2c0dc"></a> `00b2c0dc` | `e8 03 14 aa` | mov x8,x20 | `FALL_THROUGH`
<a id="insn-00b2c0e0"></a> `00b2c0e0` | `80 05 00 54` | b.eq 0x00b2c190 | `CONDITIONAL_JUMP`
<a id="insn-00b2c0e4"></a> `00b2c0e4` | `89 8e 5e 38` | ldrb w9,[x20, #-0x18]! | `FALL_THROUGH`
<a id="insn-00b2c0e8"></a> `00b2c0e8` | `89 ff 07 36` | tbz w9,#0x0,0x00b2c0d8 | `CONDITIONAL_JUMP`
<a id="insn-00b2c0ec"></a> `00b2c0ec` | `00 81 5f f8` | ldur x0,[x8, #-0x8] | `FALL_THROUGH`
<a id="insn-00b2c0f0"></a> `00b2c0f0` | `c8 bb 02 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00b2c0f4"></a> `00b2c0f4` | `f9 ff ff 17` | b 0x00b2c0d8 | `UNCONDITIONAL_JUMP`
<a id="insn-00b2c0f8"></a> `00b2c0f8` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00b2c0fc"></a> `00b2c0fc` | `9f 52 02 39` | strb wzr,[x20, #0x94] | `FALL_THROUGH`
<a id="insn-00b2c100"></a> `00b2c100` | `80 62 02 91` | add x0,x20,#0x98 | `FALL_THROUGH`
<a id="insn-00b2c104"></a> `00b2c104` | `02 00 00 14` | b 0x00b2c10c | `UNCONDITIONAL_JUMP`
<a id="insn-00b2c108"></a> `00b2c108` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00b2c10c"></a> `00b2c10c` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00b2c110"></a> `00b2c110` | `48 cd 02 94` | bl 0x00bdf630 | `UNCONDITIONAL_CALL`
<a id="insn-00b2c114"></a> `00b2c114` | `a0 03 00 36` | tbz w0,#0x0,0x00b2c188 | `CONDITIONAL_JUMP`
<a id="insn-00b2c118"></a> `00b2c118` | `68 02 80 b9` | ldrsw x8,[x19] | `FALL_THROUGH`
<a id="insn-00b2c11c"></a> `00b2c11c` | `68 02 08 cb` | sub x8,x19,x8 | `FALL_THROUGH`
<a id="insn-00b2c120"></a> `00b2c120` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00b2c124"></a> `00b2c124` | `3f 35 00 71` | cmp w9,#0xd | `FALL_THROUGH`
<a id="insn-00b2c128"></a> `00b2c128` | `e3 00 00 54` | b.cc 0x00b2c144 | `CONDITIONAL_JUMP`
<a id="insn-00b2c12c"></a> `00b2c12c` | `08 19 40 79` | ldrh w8,[x8, #0xc] | `FALL_THROUGH`
<a id="insn-00b2c130"></a> `00b2c130` | `a8 00 00 b4` | cbz x8,0x00b2c144 | `CONDITIONAL_JUMP`
<a id="insn-00b2c134"></a> `00b2c134` | `68 02 08 8b` | add x8,x19,x8 | `FALL_THROUGH`
<a id="insn-00b2c138"></a> `00b2c138` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00b2c13c"></a> `00b2c13c` | `02 01 09 8b` | add x2,x8,x9 | `FALL_THROUGH`
<a id="insn-00b2c140"></a> `00b2c140` | `02 00 00 14` | b 0x00b2c148 | `UNCONDITIONAL_JUMP`
<a id="insn-00b2c144"></a> `00b2c144` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00b2c148"></a> `00b2c148` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b2c14c"></a> `00b2c14c` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00b2c150"></a> `00b2c150` | `ec cb 02 94` | bl 0x00bdf100 | `UNCONDITIONAL_CALL`
<a id="insn-00b2c154"></a> `00b2c154` | `a0 01 00 36` | tbz w0,#0x0,0x00b2c188 | `CONDITIONAL_JUMP`
<a id="insn-00b2c158"></a> `00b2c158` | `68 02 80 b9` | ldrsw x8,[x19] | `FALL_THROUGH`
<a id="insn-00b2c15c"></a> `00b2c15c` | `80 c2 00 91` | add x0,x20,#0x30 | `FALL_THROUGH`
<a id="insn-00b2c160"></a> `00b2c160` | `68 02 08 cb` | sub x8,x19,x8 | `FALL_THROUGH`
<a id="insn-00b2c164"></a> `00b2c164` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00b2c168"></a> `00b2c168` | `3f 3d 00 71` | cmp w9,#0xf | `FALL_THROUGH`
<a id="insn-00b2c16c"></a> `00b2c16c` | `c3 02 00 54` | b.cc 0x00b2c1c4 | `CONDITIONAL_JUMP`
<a id="insn-00b2c170"></a> `00b2c170` | `08 1d 40 79` | ldrh w8,[x8, #0xe] | `FALL_THROUGH`
<a id="insn-00b2c174"></a> `00b2c174` | `88 02 00 b4` | cbz x8,0x00b2c1c4 | `CONDITIONAL_JUMP`
<a id="insn-00b2c178"></a> `00b2c178` | `68 02 08 8b` | add x8,x19,x8 | `FALL_THROUGH`
<a id="insn-00b2c17c"></a> `00b2c17c` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00b2c180"></a> `00b2c180` | `01 01 09 8b` | add x1,x8,x9 | `FALL_THROUGH`
<a id="insn-00b2c184"></a> `00b2c184` | `11 00 00 14` | b 0x00b2c1c8 | `UNCONDITIONAL_JUMP`
<a id="insn-00b2c188"></a> `00b2c188` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00b2c18c"></a> `00b2c18c` | `11 00 00 14` | b 0x00b2c1d0 | `UNCONDITIONAL_JUMP`
<a id="insn-00b2c190"></a> `00b2c190` | `c0 0e 40 f9` | ldr x0,[x22, #0x18] | `FALL_THROUGH`
<a id="insn-00b2c194"></a> `00b2c194` | `02 00 00 14` | b 0x00b2c19c | `UNCONDITIONAL_JUMP`
<a id="insn-00b2c198"></a> `00b2c198` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b2c19c"></a> `00b2c19c` | `d3 12 00 f9` | str x19,[x22, #0x20] | `FALL_THROUGH`
<a id="insn-00b2c1a0"></a> `00b2c1a0` | `9c bb 02 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00b2c1a4"></a> `00b2c1a4` | `c8 02 40 39` | ldrb w8,[x22] | `FALL_THROUGH`
<a id="insn-00b2c1a8"></a> `00b2c1a8` | `68 00 00 36` | tbz w8,#0x0,0x00b2c1b4 | `CONDITIONAL_JUMP`
<a id="insn-00b2c1ac"></a> `00b2c1ac` | `c0 0a 40 f9` | ldr x0,[x22, #0x10] | `FALL_THROUGH`
<a id="insn-00b2c1b0"></a> `00b2c1b0` | `98 bb 02 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00b2c1b4"></a> `00b2c1b4` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00b2c1b8"></a> `00b2c1b8` | `96 bb 02 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00b2c1bc"></a> `00b2c1bc` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00b2c1c0"></a> `00b2c1c0` | `04 00 00 14` | b 0x00b2c1d0 | `UNCONDITIONAL_JUMP`
<a id="insn-00b2c1c4"></a> `00b2c1c4` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-00b2c1c8"></a> `00b2c1c8` | `26 cc 02 94` | bl 0x00bdf260 | `UNCONDITIONAL_CALL`
<a id="insn-00b2c1cc"></a> `00b2c1cc` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00b2c1d0"></a> `00b2c1d0` | `48 17 40 f9` | ldr x8,[x26, #0x28] | `FALL_THROUGH`
<a id="insn-00b2c1d4"></a> `00b2c1d4` | `e9 1f 40 f9` | ldr x9,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00b2c1d8"></a> `00b2c1d8` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00b2c1dc"></a> `00b2c1dc` | `21 01 00 54` | b.ne 0x00b2c200 | `CONDITIONAL_JUMP`
<a id="insn-00b2c1e0"></a> `00b2c1e0` | `fd 7b 49 a9` | ldp x29,x30,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00b2c1e4"></a> `00b2c1e4` | `f4 4f 48 a9` | ldp x20,x19,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00b2c1e8"></a> `00b2c1e8` | `f6 57 47 a9` | ldp x22,x21,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00b2c1ec"></a> `00b2c1ec` | `f8 5f 46 a9` | ldp x24,x23,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00b2c1f0"></a> `00b2c1f0` | `fa 67 45 a9` | ldp x26,x25,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00b2c1f4"></a> `00b2c1f4` | `fc 6f 44 a9` | ldp x28,x27,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b2c1f8"></a> `00b2c1f8` | `ff 83 02 91` | add sp,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-00b2c1fc"></a> `00b2c1fc` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00b2c200"></a> `00b2c200` | `90 bb 02 94` | bl 0x00bdb040 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b2beac`](#insn-00b2beac) 範囲 `[['00b2beac', '00b2beaf']]`
  - `FALL_THROUGH` [`00b2beac`](#insn-00b2beac) → [`00b2beb0`](#insn-00b2beb0)
- ブロック [`00b2beb0`](#insn-00b2beb0) 範囲 `[['00b2beb0', '00b2bebb']]`
  - `FALL_THROUGH` [`00b2beb8`](#insn-00b2beb8) → [`00b2bebc`](#insn-00b2bebc)
- ブロック [`00b2bebc`](#insn-00b2bebc) 範囲 `[['00b2bebc', '00b2bf0f']]`
  - `CONDITIONAL_JUMP` [`00b2bf0c`](#insn-00b2bf0c) → [`00b2bf28`](#insn-00b2bf28)
  - `FALL_THROUGH` [`00b2bf0c`](#insn-00b2bf0c) → [`00b2bf10`](#insn-00b2bf10)
- ブロック [`00b2bf10`](#insn-00b2bf10) 範囲 `[['00b2bf10', '00b2bf23']]`
  - `CONDITIONAL_JUMP` [`00b2bf20`](#insn-00b2bf20) → [`00b2bf48`](#insn-00b2bf48)
  - `FALL_THROUGH` [`00b2bf20`](#insn-00b2bf20) → [`00b2bf24`](#insn-00b2bf24)
- ブロック [`00b2bf24`](#insn-00b2bf24) 範囲 `[['00b2bf24', '00b2bf27']]`
  - `UNCONDITIONAL_JUMP` [`00b2bf24`](#insn-00b2bf24) → [`00b2bf58`](#insn-00b2bf58)
- ブロック [`00b2bf28`](#insn-00b2bf28) 範囲 `[['00b2bf28', '00b2bf47']]`
  - `FALL_THROUGH` [`00b2bf44`](#insn-00b2bf44) → [`00b2bf48`](#insn-00b2bf48)
- ブロック [`00b2bf48`](#insn-00b2bf48) 範囲 `[['00b2bf48', '00b2bf53']]`
  - `FALL_THROUGH` [`00b2bf50`](#insn-00b2bf50) → [`00b2bf54`](#insn-00b2bf54)
- ブロック [`00b2bf54`](#insn-00b2bf54) 範囲 `[['00b2bf54', '00b2bf57']]`
  - `FALL_THROUGH` [`00b2bf54`](#insn-00b2bf54) → [`00b2bf58`](#insn-00b2bf58)
- ブロック [`00b2bf58`](#insn-00b2bf58) 範囲 `[['00b2bf58', '00b2bf6f']]`
  - `FALL_THROUGH` [`00b2bf6c`](#insn-00b2bf6c) → [`00b2bf70`](#insn-00b2bf70)
- ブロック [`00b2bf70`](#insn-00b2bf70) 範囲 `[['00b2bf70', '00b2bf73']]`
  - `CONDITIONAL_JUMP` [`00b2bf70`](#insn-00b2bf70) → [`00b2bf7c`](#insn-00b2bf7c)
  - `FALL_THROUGH` [`00b2bf70`](#insn-00b2bf70) → [`00b2bf74`](#insn-00b2bf74)
- ブロック [`00b2bf74`](#insn-00b2bf74) 範囲 `[['00b2bf74', '00b2bf7b']]`
  - `UNCONDITIONAL_JUMP` [`00b2bf78`](#insn-00b2bf78) → [`00b2bf9c`](#insn-00b2bf9c)
- ブロック [`00b2bf7c`](#insn-00b2bf7c) 範囲 `[['00b2bf7c', '00b2bf8f']]`
  - `CONDITIONAL_JUMP` [`00b2bf8c`](#insn-00b2bf8c) → [`00b2bf9c`](#insn-00b2bf9c)
  - `FALL_THROUGH` [`00b2bf8c`](#insn-00b2bf8c) → [`00b2bf90`](#insn-00b2bf90)
- ブロック [`00b2bf90`](#insn-00b2bf90) 範囲 `[['00b2bf90', '00b2bf97']]`
  - `FALL_THROUGH` [`00b2bf94`](#insn-00b2bf94) → [`00b2bf98`](#insn-00b2bf98)
- ブロック [`00b2bf98`](#insn-00b2bf98) 範囲 `[['00b2bf98', '00b2bf9b']]`
  - `FALL_THROUGH` [`00b2bf98`](#insn-00b2bf98) → [`00b2bf9c`](#insn-00b2bf9c)
- ブロック [`00b2bf9c`](#insn-00b2bf9c) 範囲 `[['00b2bf9c', '00b2bfb3']]`
  - `FALL_THROUGH` [`00b2bfb0`](#insn-00b2bfb0) → [`00b2bfb4`](#insn-00b2bfb4)
- ブロック [`00b2bfb4`](#insn-00b2bfb4) 範囲 `[['00b2bfb4', '00b2bfbb']]`
  - `CONDITIONAL_JUMP` [`00b2bfb8`](#insn-00b2bfb8) → [`00b2bfc4`](#insn-00b2bfc4)
  - `FALL_THROUGH` [`00b2bfb8`](#insn-00b2bfb8) → [`00b2bfbc`](#insn-00b2bfbc)
- ブロック [`00b2bfbc`](#insn-00b2bfbc) 範囲 `[['00b2bfbc', '00b2bfbf']]`
  - `FALL_THROUGH` [`00b2bfbc`](#insn-00b2bfbc) → [`00b2bfc0`](#insn-00b2bfc0)
- ブロック [`00b2bfc0`](#insn-00b2bfc0) 範囲 `[['00b2bfc0', '00b2bfc3']]`
  - `FALL_THROUGH` [`00b2bfc0`](#insn-00b2bfc0) → [`00b2bfc4`](#insn-00b2bfc4)
- ブロック [`00b2bfc4`](#insn-00b2bfc4) 範囲 `[['00b2bfc4', '00b2bfdf']]`
  - `CONDITIONAL_JUMP` [`00b2bfdc`](#insn-00b2bfdc) → [`00b2c068`](#insn-00b2c068)
  - `FALL_THROUGH` [`00b2bfdc`](#insn-00b2bfdc) → [`00b2bfe0`](#insn-00b2bfe0)
- ブロック [`00b2bfe0`](#insn-00b2bfe0) 範囲 `[['00b2bfe0', '00b2bfeb']]`
  - `FALL_THROUGH` [`00b2bfe8`](#insn-00b2bfe8) → [`00b2bfec`](#insn-00b2bfec)
- ブロック [`00b2bfec`](#insn-00b2bfec) 範囲 `[['00b2bfec', '00b2c02b']]`
  - `CONDITIONAL_JUMP` [`00b2c028`](#insn-00b2c028) → [`00b2c0b8`](#insn-00b2c0b8)
  - `FALL_THROUGH` [`00b2c028`](#insn-00b2c028) → [`00b2c02c`](#insn-00b2c02c)
- ブロック [`00b2c02c`](#insn-00b2c02c) 範囲 `[['00b2c02c', '00b2c03f']]`
  - `CONDITIONAL_JUMP` [`00b2c03c`](#insn-00b2c03c) → [`00b2c0b8`](#insn-00b2c0b8)
  - `FALL_THROUGH` [`00b2c03c`](#insn-00b2c03c) → [`00b2c040`](#insn-00b2c040)
- ブロック [`00b2c040`](#insn-00b2c040) 範囲 `[['00b2c040', '00b2c067']]`
  - `CONDITIONAL_JUMP` [`00b2c064`](#insn-00b2c064) → [`00b2bfec`](#insn-00b2bfec)
  - `FALL_THROUGH` [`00b2c064`](#insn-00b2c064) → [`00b2c068`](#insn-00b2c068)
- ブロック [`00b2c068`](#insn-00b2c068) 範囲 `[['00b2c068', '00b2c07b']]`
  - `CONDITIONAL_JUMP` [`00b2c078`](#insn-00b2c078) → [`00b2c0f8`](#insn-00b2c0f8)
  - `FALL_THROUGH` [`00b2c078`](#insn-00b2c078) → [`00b2c07c`](#insn-00b2c07c)
- ブロック [`00b2c07c`](#insn-00b2c07c) 範囲 `[['00b2c07c', '00b2c083']]`
  - `CONDITIONAL_JUMP` [`00b2c080`](#insn-00b2c080) → [`00b2c090`](#insn-00b2c090)
  - `FALL_THROUGH` [`00b2c080`](#insn-00b2c080) → [`00b2c084`](#insn-00b2c084)
- ブロック [`00b2c084`](#insn-00b2c084) 範囲 `[['00b2c084', '00b2c08f']]`
  - `FALL_THROUGH` [`00b2c08c`](#insn-00b2c08c) → [`00b2c090`](#insn-00b2c090)
- ブロック [`00b2c090`](#insn-00b2c090) 範囲 `[['00b2c090', '00b2c097']]`
  - `FALL_THROUGH` [`00b2c094`](#insn-00b2c094) → [`00b2c098`](#insn-00b2c098)
- ブロック [`00b2c098`](#insn-00b2c098) 範囲 `[['00b2c098', '00b2c09f']]`
  - `CONDITIONAL_JUMP` [`00b2c09c`](#insn-00b2c09c) → [`00b2c108`](#insn-00b2c108)
  - `FALL_THROUGH` [`00b2c09c`](#insn-00b2c09c) → [`00b2c0a0`](#insn-00b2c0a0)
- ブロック [`00b2c0a0`](#insn-00b2c0a0) 範囲 `[['00b2c0a0', '00b2c0a3']]`
  - `FALL_THROUGH` [`00b2c0a0`](#insn-00b2c0a0) → [`00b2c0a4`](#insn-00b2c0a4)
- ブロック [`00b2c0a4`](#insn-00b2c0a4) 範囲 `[['00b2c0a4', '00b2c0a7']]`
  - `CONDITIONAL_JUMP` [`00b2c0a4`](#insn-00b2c0a4) → [`00b2c108`](#insn-00b2c108)
  - `FALL_THROUGH` [`00b2c0a4`](#insn-00b2c0a4) → [`00b2c0a8`](#insn-00b2c0a8)
- ブロック [`00b2c0a8`](#insn-00b2c0a8) 範囲 `[['00b2c0a8', '00b2c0b7']]`
  - `UNCONDITIONAL_JUMP` [`00b2c0b4`](#insn-00b2c0b4) → [`00b2c10c`](#insn-00b2c10c)
- ブロック [`00b2c0b8`](#insn-00b2c0b8) 範囲 `[['00b2c0b8', '00b2c0bf']]`
  - `CONDITIONAL_JUMP` [`00b2c0bc`](#insn-00b2c0bc) → [`00b2c1a4`](#insn-00b2c1a4)
  - `FALL_THROUGH` [`00b2c0bc`](#insn-00b2c0bc) → [`00b2c0c0`](#insn-00b2c0c0)
- ブロック [`00b2c0c0`](#insn-00b2c0c0) 範囲 `[['00b2c0c0', '00b2c0cb']]`
  - `CONDITIONAL_JUMP` [`00b2c0c8`](#insn-00b2c0c8) → [`00b2c198`](#insn-00b2c198)
  - `FALL_THROUGH` [`00b2c0c8`](#insn-00b2c0c8) → [`00b2c0cc`](#insn-00b2c0cc)
- ブロック [`00b2c0cc`](#insn-00b2c0cc) 範囲 `[['00b2c0cc', '00b2c0d7']]`
  - `CONDITIONAL_JUMP` [`00b2c0d4`](#insn-00b2c0d4) → [`00b2c0ec`](#insn-00b2c0ec)
  - `FALL_THROUGH` [`00b2c0d4`](#insn-00b2c0d4) → [`00b2c0d8`](#insn-00b2c0d8)
- ブロック [`00b2c0d8`](#insn-00b2c0d8) 範囲 `[['00b2c0d8', '00b2c0e3']]`
  - `CONDITIONAL_JUMP` [`00b2c0e0`](#insn-00b2c0e0) → [`00b2c190`](#insn-00b2c190)
  - `FALL_THROUGH` [`00b2c0e0`](#insn-00b2c0e0) → [`00b2c0e4`](#insn-00b2c0e4)
- ブロック [`00b2c0e4`](#insn-00b2c0e4) 範囲 `[['00b2c0e4', '00b2c0eb']]`
  - `CONDITIONAL_JUMP` [`00b2c0e8`](#insn-00b2c0e8) → [`00b2c0d8`](#insn-00b2c0d8)
  - `FALL_THROUGH` [`00b2c0e8`](#insn-00b2c0e8) → [`00b2c0ec`](#insn-00b2c0ec)
- ブロック [`00b2c0ec`](#insn-00b2c0ec) 範囲 `[['00b2c0ec', '00b2c0f7']]`
  - `UNCONDITIONAL_JUMP` [`00b2c0f4`](#insn-00b2c0f4) → [`00b2c0d8`](#insn-00b2c0d8)
- ブロック [`00b2c0f8`](#insn-00b2c0f8) 範囲 `[['00b2c0f8', '00b2c107']]`
  - `UNCONDITIONAL_JUMP` [`00b2c104`](#insn-00b2c104) → [`00b2c10c`](#insn-00b2c10c)
- ブロック [`00b2c108`](#insn-00b2c108) 範囲 `[['00b2c108', '00b2c10b']]`
  - `FALL_THROUGH` [`00b2c108`](#insn-00b2c108) → [`00b2c10c`](#insn-00b2c10c)
- ブロック [`00b2c10c`](#insn-00b2c10c) 範囲 `[['00b2c10c', '00b2c117']]`
  - `CONDITIONAL_JUMP` [`00b2c114`](#insn-00b2c114) → [`00b2c188`](#insn-00b2c188)
  - `FALL_THROUGH` [`00b2c114`](#insn-00b2c114) → [`00b2c118`](#insn-00b2c118)
- ブロック [`00b2c118`](#insn-00b2c118) 範囲 `[['00b2c118', '00b2c12b']]`
  - `CONDITIONAL_JUMP` [`00b2c128`](#insn-00b2c128) → [`00b2c144`](#insn-00b2c144)
  - `FALL_THROUGH` [`00b2c128`](#insn-00b2c128) → [`00b2c12c`](#insn-00b2c12c)
- ブロック [`00b2c12c`](#insn-00b2c12c) 範囲 `[['00b2c12c', '00b2c133']]`
  - `CONDITIONAL_JUMP` [`00b2c130`](#insn-00b2c130) → [`00b2c144`](#insn-00b2c144)
  - `FALL_THROUGH` [`00b2c130`](#insn-00b2c130) → [`00b2c134`](#insn-00b2c134)
- ブロック [`00b2c134`](#insn-00b2c134) 範囲 `[['00b2c134', '00b2c143']]`
  - `UNCONDITIONAL_JUMP` [`00b2c140`](#insn-00b2c140) → [`00b2c148`](#insn-00b2c148)
- ブロック [`00b2c144`](#insn-00b2c144) 範囲 `[['00b2c144', '00b2c147']]`
  - `FALL_THROUGH` [`00b2c144`](#insn-00b2c144) → [`00b2c148`](#insn-00b2c148)
- ブロック [`00b2c148`](#insn-00b2c148) 範囲 `[['00b2c148', '00b2c14f']]`
  - `FALL_THROUGH` [`00b2c14c`](#insn-00b2c14c) → [`00b2c150`](#insn-00b2c150)
- ブロック [`00b2c150`](#insn-00b2c150) 範囲 `[['00b2c150', '00b2c157']]`
  - `CONDITIONAL_JUMP` [`00b2c154`](#insn-00b2c154) → [`00b2c188`](#insn-00b2c188)
  - `FALL_THROUGH` [`00b2c154`](#insn-00b2c154) → [`00b2c158`](#insn-00b2c158)
- ブロック [`00b2c158`](#insn-00b2c158) 範囲 `[['00b2c158', '00b2c16f']]`
  - `CONDITIONAL_JUMP` [`00b2c16c`](#insn-00b2c16c) → [`00b2c1c4`](#insn-00b2c1c4)
  - `FALL_THROUGH` [`00b2c16c`](#insn-00b2c16c) → [`00b2c170`](#insn-00b2c170)
- ブロック [`00b2c170`](#insn-00b2c170) 範囲 `[['00b2c170', '00b2c177']]`
  - `CONDITIONAL_JUMP` [`00b2c174`](#insn-00b2c174) → [`00b2c1c4`](#insn-00b2c1c4)
  - `FALL_THROUGH` [`00b2c174`](#insn-00b2c174) → [`00b2c178`](#insn-00b2c178)
- ブロック [`00b2c178`](#insn-00b2c178) 範囲 `[['00b2c178', '00b2c187']]`
  - `UNCONDITIONAL_JUMP` [`00b2c184`](#insn-00b2c184) → [`00b2c1c8`](#insn-00b2c1c8)
- ブロック [`00b2c188`](#insn-00b2c188) 範囲 `[['00b2c188', '00b2c18f']]`
  - `UNCONDITIONAL_JUMP` [`00b2c18c`](#insn-00b2c18c) → [`00b2c1d0`](#insn-00b2c1d0)
- ブロック [`00b2c190`](#insn-00b2c190) 範囲 `[['00b2c190', '00b2c197']]`
  - `UNCONDITIONAL_JUMP` [`00b2c194`](#insn-00b2c194) → [`00b2c19c`](#insn-00b2c19c)
- ブロック [`00b2c198`](#insn-00b2c198) 範囲 `[['00b2c198', '00b2c19b']]`
  - `FALL_THROUGH` [`00b2c198`](#insn-00b2c198) → [`00b2c19c`](#insn-00b2c19c)
- ブロック [`00b2c19c`](#insn-00b2c19c) 範囲 `[['00b2c19c', '00b2c1a3']]`
  - `FALL_THROUGH` [`00b2c1a0`](#insn-00b2c1a0) → [`00b2c1a4`](#insn-00b2c1a4)
- ブロック [`00b2c1a4`](#insn-00b2c1a4) 範囲 `[['00b2c1a4', '00b2c1ab']]`
  - `CONDITIONAL_JUMP` [`00b2c1a8`](#insn-00b2c1a8) → [`00b2c1b4`](#insn-00b2c1b4)
  - `FALL_THROUGH` [`00b2c1a8`](#insn-00b2c1a8) → [`00b2c1ac`](#insn-00b2c1ac)
- ブロック [`00b2c1ac`](#insn-00b2c1ac) 範囲 `[['00b2c1ac', '00b2c1b3']]`
  - `FALL_THROUGH` [`00b2c1b0`](#insn-00b2c1b0) → [`00b2c1b4`](#insn-00b2c1b4)
- ブロック [`00b2c1b4`](#insn-00b2c1b4) 範囲 `[['00b2c1b4', '00b2c1c3']]`
  - `UNCONDITIONAL_JUMP` [`00b2c1c0`](#insn-00b2c1c0) → [`00b2c1d0`](#insn-00b2c1d0)
- ブロック [`00b2c1c4`](#insn-00b2c1c4) 範囲 `[['00b2c1c4', '00b2c1c7']]`
  - `FALL_THROUGH` [`00b2c1c4`](#insn-00b2c1c4) → [`00b2c1c8`](#insn-00b2c1c8)
- ブロック [`00b2c1c8`](#insn-00b2c1c8) 範囲 `[['00b2c1c8', '00b2c1cf']]`
  - `FALL_THROUGH` [`00b2c1cc`](#insn-00b2c1cc) → [`00b2c1d0`](#insn-00b2c1d0)
- ブロック [`00b2c1d0`](#insn-00b2c1d0) 範囲 `[['00b2c1d0', '00b2c1df']]`
  - `CONDITIONAL_JUMP` [`00b2c1dc`](#insn-00b2c1dc) → [`00b2c200`](#insn-00b2c200)
  - `FALL_THROUGH` [`00b2c1dc`](#insn-00b2c1dc) → [`00b2c1e0`](#insn-00b2c1e0)
- ブロック [`00b2c1e0`](#insn-00b2c1e0) 範囲 `[['00b2c1e0', '00b2c1ff']]`
- ブロック [`00b2c200`](#insn-00b2c200) 範囲 `[['00b2c200', '00b2c203']]`

## 命令位置別の参照

- [`00b2beb0`](#insn-00b2beb0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2beb4`](#insn-00b2beb4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2beb8`](#insn-00b2beb8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2bebc`](#insn-00b2bebc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2bec0`](#insn-00b2bec0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2bec4`](#insn-00b2bec4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2bee0`](#insn-00b2bee0) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2bf00`](#insn-00b2bf00) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2bf04`](#insn-00b2bf04) → `Stack[-0x98]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2bf0c`](#insn-00b2bf0c) → [`00b2bf28`](#insn-00b2bf28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2bf1c`](#insn-00b2bf1c) → `Stack[-0x98]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2bf20`](#insn-00b2bf20) → [`00b2bf48`](#insn-00b2bf48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2bf24`](#insn-00b2bf24) → [`00b2bf58`](#insn-00b2bf58) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2bf34`](#insn-00b2bf34) → [`00bdaff0`](../00bda/00bdaff0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaff0` · 推定シンボル `None` · 推定型 `None`
- [`00b2bf40`](#insn-00b2bf40) → `Stack[-0x98]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2bf44`](#insn-00b2bf44) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2bf54`](#insn-00b2bf54) → [`00bdb160`](../00bdb/00bdb160.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb160` · 推定シンボル `None` · 推定型 `None`
- [`00b2bf68`](#insn-00b2bf68) → [`00bdf860`](../00bdf/00bdf860.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdf860` · 推定シンボル `None` · 推定型 `None`
- [`00b2bf70`](#insn-00b2bf70) → [`00b2bf7c`](#insn-00b2bf7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2bf78`](#insn-00b2bf78) → [`00b2bf9c`](#insn-00b2bf9c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2bf8c`](#insn-00b2bf8c) → [`00b2bf9c`](#insn-00b2bf9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2bf94`](#insn-00b2bf94) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00b2bf9c`](#insn-00b2bf9c) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2bfa0`](#insn-00b2bfa0) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2bfac`](#insn-00b2bfac) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2bfb0`](#insn-00b2bfb0) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2bfb4`](#insn-00b2bfb4) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2bfb8`](#insn-00b2bfb8) → [`00b2bfc4`](#insn-00b2bfc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2bfbc`](#insn-00b2bfbc) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2bfc0`](#insn-00b2bfc0) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00b2bfdc`](#insn-00b2bfdc) → [`00b2c068`](#insn-00b2c068) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2bff0`](#insn-00b2bff0) → [`00bdaff0`](../00bda/00bdaff0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaff0` · 推定シンボル `None` · 推定型 `None`
- [`00b2c024`](#insn-00b2c024) → [`00bdfa30`](../00bdf/00bdfa30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdfa30` · 推定シンボル `None` · 推定型 `None`
- [`00b2c028`](#insn-00b2c028) → [`00b2c0b8`](#insn-00b2c0b8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2c038`](#insn-00b2c038) → [`00bdf1f0`](../00bdf/00bdf1f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdf1f0` · 推定シンボル `None` · 推定型 `None`
- [`00b2c03c`](#insn-00b2c03c) → [`00b2c0b8`](#insn-00b2c0b8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2c064`](#insn-00b2c064) → [`00b2bfec`](#insn-00b2bfec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2c078`](#insn-00b2c078) → [`00b2c0f8`](#insn-00b2c0f8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2c080`](#insn-00b2c080) → [`00b2c090`](#insn-00b2c090) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2c09c`](#insn-00b2c09c) → [`00b2c108`](#insn-00b2c108) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2c0a4`](#insn-00b2c0a4) → [`00b2c108`](#insn-00b2c108) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2c0b4`](#insn-00b2c0b4) → [`00b2c10c`](#insn-00b2c10c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2c0bc`](#insn-00b2c0bc) → [`00b2c1a4`](#insn-00b2c1a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2c0c8`](#insn-00b2c0c8) → [`00b2c198`](#insn-00b2c198) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2c0d4`](#insn-00b2c0d4) → [`00b2c0ec`](#insn-00b2c0ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2c0e0`](#insn-00b2c0e0) → [`00b2c190`](#insn-00b2c190) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2c0e8`](#insn-00b2c0e8) → [`00b2c0d8`](#insn-00b2c0d8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2c0f0`](#insn-00b2c0f0) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00b2c0f4`](#insn-00b2c0f4) → [`00b2c0d8`](#insn-00b2c0d8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2c104`](#insn-00b2c104) → [`00b2c10c`](#insn-00b2c10c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2c110`](#insn-00b2c110) → [`00bdf630`](../00bdf/00bdf630.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdf630` · 推定シンボル `None` · 推定型 `None`
- [`00b2c114`](#insn-00b2c114) → [`00b2c188`](#insn-00b2c188) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2c128`](#insn-00b2c128) → [`00b2c144`](#insn-00b2c144) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2c130`](#insn-00b2c130) → [`00b2c144`](#insn-00b2c144) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2c140`](#insn-00b2c140) → [`00b2c148`](#insn-00b2c148) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2c150`](#insn-00b2c150) → [`00bdf100`](../00bdf/00bdf100.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdf100` · 推定シンボル `None` · 推定型 `None`
- [`00b2c154`](#insn-00b2c154) → [`00b2c188`](#insn-00b2c188) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2c16c`](#insn-00b2c16c) → [`00b2c1c4`](#insn-00b2c1c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2c174`](#insn-00b2c174) → [`00b2c1c4`](#insn-00b2c1c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2c184`](#insn-00b2c184) → [`00b2c1c8`](#insn-00b2c1c8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2c18c`](#insn-00b2c18c) → [`00b2c1d0`](#insn-00b2c1d0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2c194`](#insn-00b2c194) → [`00b2c19c`](#insn-00b2c19c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2c1a0`](#insn-00b2c1a0) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00b2c1a8`](#insn-00b2c1a8) → [`00b2c1b4`](#insn-00b2c1b4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2c1b0`](#insn-00b2c1b0) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00b2c1b8`](#insn-00b2c1b8) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00b2c1c0`](#insn-00b2c1c0) → [`00b2c1d0`](#insn-00b2c1d0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2c1c8`](#insn-00b2c1c8) → [`00bdf260`](../00bdf/00bdf260.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdf260` · 推定シンボル `None` · 推定型 `None`
- [`00b2c1d4`](#insn-00b2c1d4) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2c1dc`](#insn-00b2c1dc) → [`00b2c200`](#insn-00b2c200) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2c1e0`](#insn-00b2c1e0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2c1e4`](#insn-00b2c1e4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2c1e8`](#insn-00b2c1e8) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2c1ec`](#insn-00b2c1ec) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2c1f0`](#insn-00b2c1f0) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2c1f4`](#insn-00b2c1f4) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2c200`](#insn-00b2c200) → [`00bdb040`](../00bdb/00bdb040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb040` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b2beb0`](#insn-00b2beb0)

~~~json
{
  "source": "00b2beb0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2beb4`](#insn-00b2beb4)

~~~json
{
  "source": "00b2beb4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2beb8`](#insn-00b2beb8)

~~~json
{
  "source": "00b2beb8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2bebc`](#insn-00b2bebc)

~~~json
{
  "source": "00b2bebc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2bec0`](#insn-00b2bec0)

~~~json
{
  "source": "00b2bec0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2bec4`](#insn-00b2bec4)

~~~json
{
  "source": "00b2bec4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2bee0`](#insn-00b2bee0)

~~~json
{
  "source": "00b2bee0",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2bf00`](#insn-00b2bf00)

~~~json
{
  "source": "00b2bf00",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2bf04`](#insn-00b2bf04)

~~~json
{
  "source": "00b2bf04",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2bf0c`](#insn-00b2bf0c)

~~~json
{
  "source": "00b2bf0c",
  "target": "00b2bf28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2bf1c`](#insn-00b2bf1c)

~~~json
{
  "source": "00b2bf1c",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2bf20`](#insn-00b2bf20)

~~~json
{
  "source": "00b2bf20",
  "target": "00b2bf48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2bf24`](#insn-00b2bf24)

~~~json
{
  "source": "00b2bf24",
  "target": "00b2bf58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2bf34`](#insn-00b2bf34)

~~~json
{
  "source": "00b2bf34",
  "target": "00bdaff0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b2bf40`](#insn-00b2bf40)

~~~json
{
  "source": "00b2bf40",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2bf44`](#insn-00b2bf44)

~~~json
{
  "source": "00b2bf44",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2bf54`](#insn-00b2bf54)

~~~json
{
  "source": "00b2bf54",
  "target": "00bdb160",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b2bf68`](#insn-00b2bf68)

~~~json
{
  "source": "00b2bf68",
  "target": "00bdf860",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b2bf70`](#insn-00b2bf70)

~~~json
{
  "source": "00b2bf70",
  "target": "00b2bf7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2bf78`](#insn-00b2bf78)

~~~json
{
  "source": "00b2bf78",
  "target": "00b2bf9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2bf8c`](#insn-00b2bf8c)

~~~json
{
  "source": "00b2bf8c",
  "target": "00b2bf9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2bf94`](#insn-00b2bf94)

~~~json
{
  "source": "00b2bf94",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b2bf9c`](#insn-00b2bf9c)

~~~json
{
  "source": "00b2bf9c",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2bfa0`](#insn-00b2bfa0)

~~~json
{
  "source": "00b2bfa0",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2bfac`](#insn-00b2bfac)

~~~json
{
  "source": "00b2bfac",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2bfb0`](#insn-00b2bfb0)

~~~json
{
  "source": "00b2bfb0",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2bfb4`](#insn-00b2bfb4)

~~~json
{
  "source": "00b2bfb4",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2bfb8`](#insn-00b2bfb8)

~~~json
{
  "source": "00b2bfb8",
  "target": "00b2bfc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2bfbc`](#insn-00b2bfbc)

~~~json
{
  "source": "00b2bfbc",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2bfc0`](#insn-00b2bfc0)

~~~json
{
  "source": "00b2bfc0",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b2bfdc`](#insn-00b2bfdc)

~~~json
{
  "source": "00b2bfdc",
  "target": "00b2c068",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2bff0`](#insn-00b2bff0)

~~~json
{
  "source": "00b2bff0",
  "target": "00bdaff0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b2c024`](#insn-00b2c024)

~~~json
{
  "source": "00b2c024",
  "target": "00bdfa30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b2c028`](#insn-00b2c028)

~~~json
{
  "source": "00b2c028",
  "target": "00b2c0b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2c038`](#insn-00b2c038)

~~~json
{
  "source": "00b2c038",
  "target": "00bdf1f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b2c03c`](#insn-00b2c03c)

~~~json
{
  "source": "00b2c03c",
  "target": "00b2c0b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2c064`](#insn-00b2c064)

~~~json
{
  "source": "00b2c064",
  "target": "00b2bfec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2c078`](#insn-00b2c078)

~~~json
{
  "source": "00b2c078",
  "target": "00b2c0f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2c080`](#insn-00b2c080)

~~~json
{
  "source": "00b2c080",
  "target": "00b2c090",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2c09c`](#insn-00b2c09c)

~~~json
{
  "source": "00b2c09c",
  "target": "00b2c108",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2c0a4`](#insn-00b2c0a4)

~~~json
{
  "source": "00b2c0a4",
  "target": "00b2c108",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2c0b4`](#insn-00b2c0b4)

~~~json
{
  "source": "00b2c0b4",
  "target": "00b2c10c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2c0bc`](#insn-00b2c0bc)

~~~json
{
  "source": "00b2c0bc",
  "target": "00b2c1a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2c0c8`](#insn-00b2c0c8)

~~~json
{
  "source": "00b2c0c8",
  "target": "00b2c198",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2c0d4`](#insn-00b2c0d4)

~~~json
{
  "source": "00b2c0d4",
  "target": "00b2c0ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2c0e0`](#insn-00b2c0e0)

~~~json
{
  "source": "00b2c0e0",
  "target": "00b2c190",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2c0e8`](#insn-00b2c0e8)

~~~json
{
  "source": "00b2c0e8",
  "target": "00b2c0d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2c0f0`](#insn-00b2c0f0)

~~~json
{
  "source": "00b2c0f0",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b2c0f4`](#insn-00b2c0f4)

~~~json
{
  "source": "00b2c0f4",
  "target": "00b2c0d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2c104`](#insn-00b2c104)

~~~json
{
  "source": "00b2c104",
  "target": "00b2c10c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2c110`](#insn-00b2c110)

~~~json
{
  "source": "00b2c110",
  "target": "00bdf630",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b2c114`](#insn-00b2c114)

~~~json
{
  "source": "00b2c114",
  "target": "00b2c188",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2c128`](#insn-00b2c128)

~~~json
{
  "source": "00b2c128",
  "target": "00b2c144",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2c130`](#insn-00b2c130)

~~~json
{
  "source": "00b2c130",
  "target": "00b2c144",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2c140`](#insn-00b2c140)

~~~json
{
  "source": "00b2c140",
  "target": "00b2c148",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2c150`](#insn-00b2c150)

~~~json
{
  "source": "00b2c150",
  "target": "00bdf100",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b2c154`](#insn-00b2c154)

~~~json
{
  "source": "00b2c154",
  "target": "00b2c188",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2c16c`](#insn-00b2c16c)

~~~json
{
  "source": "00b2c16c",
  "target": "00b2c1c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2c174`](#insn-00b2c174)

~~~json
{
  "source": "00b2c174",
  "target": "00b2c1c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2c184`](#insn-00b2c184)

~~~json
{
  "source": "00b2c184",
  "target": "00b2c1c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2c18c`](#insn-00b2c18c)

~~~json
{
  "source": "00b2c18c",
  "target": "00b2c1d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2c194`](#insn-00b2c194)

~~~json
{
  "source": "00b2c194",
  "target": "00b2c19c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2c1a0`](#insn-00b2c1a0)

~~~json
{
  "source": "00b2c1a0",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b2c1a8`](#insn-00b2c1a8)

~~~json
{
  "source": "00b2c1a8",
  "target": "00b2c1b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2c1b0`](#insn-00b2c1b0)

~~~json
{
  "source": "00b2c1b0",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b2c1b8`](#insn-00b2c1b8)

~~~json
{
  "source": "00b2c1b8",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b2c1c0`](#insn-00b2c1c0)

~~~json
{
  "source": "00b2c1c0",
  "target": "00b2c1d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2c1c8`](#insn-00b2c1c8)

~~~json
{
  "source": "00b2c1c8",
  "target": "00bdf260",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b2c1d4`](#insn-00b2c1d4)

~~~json
{
  "source": "00b2c1d4",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2c1dc`](#insn-00b2c1dc)

~~~json
{
  "source": "00b2c1dc",
  "target": "00b2c200",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2c1e0`](#insn-00b2c1e0)

~~~json
{
  "source": "00b2c1e0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2c1e4`](#insn-00b2c1e4)

~~~json
{
  "source": "00b2c1e4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2c1e8`](#insn-00b2c1e8)

~~~json
{
  "source": "00b2c1e8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2c1ec`](#insn-00b2c1ec)

~~~json
{
  "source": "00b2c1ec",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2c1f0`](#insn-00b2c1f0)

~~~json
{
  "source": "00b2c1f0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2c1f4`](#insn-00b2c1f4)

~~~json
{
  "source": "00b2c1f4",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2c200`](#insn-00b2c200)

~~~json
{
  "source": "00b2c200",
  "target": "00bdb040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
