# 005cebdc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `005a9f10`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a9f10.md) · 移動量 `+0x24ccc`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/alignment_unresolved-0003.md#compare-a055ae505012bc9d51af7e336b86caf8)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `005cec1c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ce/005cec1c.md) · 移動量 `+0x40`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0016.md#compare-8f96e0c6ad2f1215db44a2679f47fa25)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "005cebdc",
  "name": "FUN_005cebdc",
  "size": 864,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7dd083a7170e688349530cb757efe52d5f2d7df68324f3c75467748f3b8a04d9",
  "source_text_sha256": "7dd083a7170e688349530cb757efe52d5f2d7df68324f3c75467748f3b8a04d9",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "005cebdc",
        "005cef3b"
      ]
    ],
    "bytes_sha256": "924b63ca0f9b9ed4937373be6405dc34bdbfcb99ca5404be086441d85926e08c",
    "instruction_count": 216,
    "instruction_bytes": 864,
    "body_bytes": 864,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [005ce48c](../005ce/005ce48c.md)
- [005ce52c](../005ce/005ce52c.md)
- [005d582c](../005d5/005d582c.md)

## 呼び出し先

- [005d4b08](../005d4/005d4b08.md)
- [005d4c48](../005d4/005d4c48.md)
- [005d4c94](../005d4/005d4c94.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 3928 bytes

~~~c

byte * FUN_005cebdc(long param_1,byte *param_2,byte *param_3,undefined8 param_4,undefined4 param_5,
                   undefined4 param_6)

{
  uint uVar1;
  byte bVar2;
  int iVar3;
  int iVar4;
  long lVar5;
  long lVar6;
  undefined8 uVar7;
  uint uVar8;
  byte *pbVar9;
  byte *pbVar10;
  byte *pbVar11;
  
  if (param_2 == param_3) {
    return param_2;
  }
  bVar2 = *param_2;
  uVar1 = *(uint *)(param_1 + 0x18) & 0x1f0;
  if (bVar2 < 0x3f) {
    if (bVar2 == 0x2a) {
      pbVar11 = param_2 + 1;
      if (((uVar1 == 0) && (pbVar11 != param_3)) && (*pbVar11 == 0x3f)) {
        pbVar11 = param_2 + 2;
        lVar5 = 0;
LAB_005ced60:
        lVar6 = -1;
LAB_005ced98:
        uVar7 = 0;
        goto LAB_005cef20;
      }
      lVar5 = 0;
    }
    else {
      if (bVar2 != 0x2b) {
        return param_2;
      }
      pbVar11 = param_2 + 1;
      if (((uVar1 == 0) && (pbVar11 != param_3)) && (*pbVar11 == 0x3f)) {
        pbVar11 = param_2 + 2;
        lVar5 = 1;
        goto LAB_005ced60;
      }
      lVar5 = 1;
    }
LAB_005cedbc:
    lVar6 = -1;
  }
  else if (bVar2 == 0x3f) {
    pbVar11 = param_2 + 1;
    if (((uVar1 == 0) && (pbVar11 != param_3)) && (*pbVar11 == 0x3f)) {
      pbVar11 = param_2 + 2;
      lVar5 = 0;
      lVar6 = 1;
      goto LAB_005ced98;
    }
    lVar5 = 0;
    lVar6 = 1;
  }
  else {
    if (bVar2 != 0x7b) {
      return param_2;
    }
    pbVar11 = param_2 + 1;
    if ((pbVar11 == param_3) ||
       ((bVar2 = *pbVar11, (bVar2 & 0xf8) != 0x30 && ((bVar2 & 0xfe) != 0x38)))) {
LAB_005cef34:
                    /* WARNING: Subroutine does not return */
      FUN_005d4c48();
    }
    uVar8 = (uint)bVar2;
    for (param_2 = param_2 + 2;
        (iVar3 = uVar8 - 0x30, pbVar9 = param_3, param_2 != param_3 &&
        ((bVar2 = *param_2, (bVar2 & 0xf8) == 0x30 || (pbVar9 = param_2, (bVar2 & 0xfe) == 0x38))));
        param_2 = param_2 + 1) {
      if (0xccccccb < iVar3) goto LAB_005cef34;
      uVar8 = (uint)bVar2 + iVar3 * 10;
    }
    if (pbVar9 == pbVar11) goto LAB_005cef34;
    if (pbVar9 == param_3) goto LAB_005cef38;
    if (*pbVar9 == 0x2c) {
      pbVar11 = pbVar9 + 1;
      if (pbVar11 == param_3) goto LAB_005cef34;
      bVar2 = *pbVar11;
      if (bVar2 == 0x7d) {
        pbVar11 = pbVar9 + 2;
        if (((uVar1 == 0) && (pbVar11 != param_3)) && (*pbVar11 == 0x3f)) {
          lVar5 = (long)iVar3;
          pbVar11 = pbVar9 + 3;
          goto LAB_005ced60;
        }
        lVar5 = (long)iVar3;
        goto LAB_005cedbc;
      }
      uVar8 = (uint)bVar2;
      if (((bVar2 & 0xf8) != 0x30) && ((uVar8 & 0xfe) != 0x38)) {
LAB_005cef38:
                    /* WARNING: Subroutine does not return */
        FUN_005d4c94();
      }
      for (pbVar9 = pbVar9 + 2;
          (iVar4 = uVar8 - 0x30, pbVar10 = param_3, pbVar9 != param_3 &&
          ((bVar2 = *pbVar9, (bVar2 & 0xf8) == 0x30 || (pbVar10 = pbVar9, (bVar2 & 0xfe) == 0x38))))
          ; pbVar9 = pbVar9 + 1) {
        if (0xccccccb < iVar4) goto LAB_005cef34;
        uVar8 = (uint)bVar2 + iVar4 * 10;
      }
      if (((pbVar10 == pbVar11) || (pbVar10 == param_3)) || (*pbVar10 != 0x7d)) goto LAB_005cef38;
      if (iVar4 < iVar3) goto LAB_005cef34;
      pbVar11 = pbVar10 + 1;
      if (((uVar1 == 0) && (pbVar11 != param_3)) && (*pbVar11 == 0x3f)) {
        lVar5 = (long)iVar3;
        lVar6 = (long)iVar4;
        pbVar11 = pbVar10 + 2;
        goto LAB_005ced98;
      }
      lVar5 = (long)iVar3;
      lVar6 = (long)iVar4;
    }
    else {
      if (*pbVar9 != 0x7d) goto LAB_005cef34;
      pbVar11 = pbVar9 + 1;
      if (((uVar1 == 0) && (pbVar11 != param_3)) && (*pbVar11 == 0x3f)) {
        lVar5 = (long)iVar3;
        pbVar11 = pbVar9 + 2;
        lVar6 = lVar5;
        goto LAB_005ced98;
      }
      lVar5 = (long)iVar3;
      lVar6 = lVar5;
    }
  }
  uVar7 = 1;
LAB_005cef20:
  FUN_005d4b08(param_1,lVar5,lVar6,param_4,param_5,param_6,uVar7);
  return pbVar11;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-005cebdc"></a> `005cebdc` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-005cebe0"></a> `005cebe0` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-005cebe4"></a> `005cebe4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-005cebe8"></a> `005cebe8` | `3f 00 02 eb` | cmp x1,x2 | `FALL_THROUGH`
<a id="insn-005cebec"></a> `005cebec` | `00 0a 00 54` | b.eq 0x005ced2c | `CONDITIONAL_JUMP`
<a id="insn-005cebf0"></a> `005cebf0` | `29 00 40 39` | ldrb w9,[x1] | `FALL_THROUGH`
<a id="insn-005cebf4"></a> `005cebf4` | `08 18 40 b9` | ldr w8,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-005cebf8"></a> `005cebf8` | `3f f9 00 71` | cmp w9,#0x3e | `FALL_THROUGH`
<a id="insn-005cebfc"></a> `005cebfc` | `08 11 1c 12` | and w8,w8,#0x1f0 | `FALL_THROUGH`
<a id="insn-005cec00"></a> `005cec00` | `2c 02 00 54` | b.gt 0x005cec44 | `CONDITIONAL_JUMP`
<a id="insn-005cec04"></a> `005cec04` | `3f a9 00 71` | cmp w9,#0x2a | `FALL_THROUGH`
<a id="insn-005cec08"></a> `005cec08` | `60 09 00 54` | b.eq 0x005ced34 | `CONDITIONAL_JUMP`
<a id="insn-005cec0c"></a> `005cec0c` | `3f ad 00 71` | cmp w9,#0x2b | `FALL_THROUGH`
<a id="insn-005cec10"></a> `005cec10` | `e1 08 00 54` | b.ne 0x005ced2c | `CONDITIONAL_JUMP`
<a id="insn-005cec14"></a> `005cec14` | `33 04 00 91` | add x19,x1,#0x1 | `FALL_THROUGH`
<a id="insn-005cec18"></a> `005cec18` | `48 0c 00 35` | cbnz w8,0x005ceda0 | `CONDITIONAL_JUMP`
<a id="insn-005cec1c"></a> `005cec1c` | `7f 02 02 eb` | cmp x19,x2 | `FALL_THROUGH`
<a id="insn-005cec20"></a> `005cec20` | `00 0c 00 54` | b.eq 0x005ceda0 | `CONDITIONAL_JUMP`
<a id="insn-005cec24"></a> `005cec24` | `68 02 40 39` | ldrb w8,[x19] | `FALL_THROUGH`
<a id="insn-005cec28"></a> `005cec28` | `1f fd 00 71` | cmp w8,#0x3f | `FALL_THROUGH`
<a id="insn-005cec2c"></a> `005cec2c` | `a1 0b 00 54` | b.ne 0x005ceda0 | `CONDITIONAL_JUMP`
<a id="insn-005cec30"></a> `005cec30` | `33 08 00 91` | add x19,x1,#0x2 | `FALL_THROUGH`
<a id="insn-005cec34"></a> `005cec34` | `e4 03 04 2a` | mov w4,w4 | `FALL_THROUGH`
<a id="insn-005cec38"></a> `005cec38` | `e5 03 05 2a` | mov w5,w5 | `FALL_THROUGH`
<a id="insn-005cec3c"></a> `005cec3c` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-005cec40"></a> `005cec40` | `48 00 00 14` | b 0x005ced60 | `UNCONDITIONAL_JUMP`
<a id="insn-005cec44"></a> `005cec44` | `3f fd 00 71` | cmp w9,#0x3f | `FALL_THROUGH`
<a id="insn-005cec48"></a> `005cec48` | `00 09 00 54` | b.eq 0x005ced68 | `CONDITIONAL_JUMP`
<a id="insn-005cec4c"></a> `005cec4c` | `3f ed 01 71` | cmp w9,#0x7b | `FALL_THROUGH`
<a id="insn-005cec50"></a> `005cec50` | `e1 06 00 54` | b.ne 0x005ced2c | `CONDITIONAL_JUMP`
<a id="insn-005cec54"></a> `005cec54` | `2b 04 00 91` | add x11,x1,#0x1 | `FALL_THROUGH`
<a id="insn-005cec58"></a> `005cec58` | `7f 01 02 eb` | cmp x11,x2 | `FALL_THROUGH`
<a id="insn-005cec5c"></a> `005cec5c` | `c0 16 00 54` | b.eq 0x005cef34 | `CONDITIONAL_JUMP`
<a id="insn-005cec60"></a> `005cec60` | `69 01 40 39` | ldrb w9,[x11] | `FALL_THROUGH`
<a id="insn-005cec64"></a> `005cec64` | `2a 11 1d 12` | and w10,w9,#0xf8 | `FALL_THROUGH`
<a id="insn-005cec68"></a> `005cec68` | `5f c1 00 71` | cmp w10,#0x30 | `FALL_THROUGH`
<a id="insn-005cec6c"></a> `005cec6c` | `80 00 00 54` | b.eq 0x005cec7c | `CONDITIONAL_JUMP`
<a id="insn-005cec70"></a> `005cec70` | `2a 19 1f 12` | and w10,w9,#0xfe | `FALL_THROUGH`
<a id="insn-005cec74"></a> `005cec74` | `5f e1 00 71` | cmp w10,#0x38 | `FALL_THROUGH`
<a id="insn-005cec78"></a> `005cec78` | `e1 15 00 54` | b.ne 0x005cef34 | `CONDITIONAL_JUMP`
<a id="insn-005cec7c"></a> `005cec7c` | `2a 08 00 91` | add x10,x1,#0x2 | `FALL_THROUGH`
<a id="insn-005cec80"></a> `005cec80` | `29 c1 00 51` | sub w9,w9,#0x30 | `FALL_THROUGH`
<a id="insn-005cec84"></a> `005cec84` | `5f 01 02 eb` | cmp x10,x2 | `FALL_THROUGH`
<a id="insn-005cec88"></a> `005cec88` | `40 02 00 54` | b.eq 0x005cecd0 | `CONDITIONAL_JUMP`
<a id="insn-005cec8c"></a> `005cec8c` | `8c 99 99 52` | mov w12,#0xcccc | `FALL_THROUGH`
<a id="insn-005cec90"></a> `005cec90` | `4d 01 80 52` | mov w13,#0xa | `FALL_THROUGH`
<a id="insn-005cec94"></a> `005cec94` | `8c 99 a1 72` | movk w12,#0xccc, LSL #16 | `FALL_THROUGH`
<a id="insn-005cec98"></a> `005cec98` | `4e 01 40 39` | ldrb w14,[x10] | `FALL_THROUGH`
<a id="insn-005cec9c"></a> `005cec9c` | `cf 11 1d 12` | and w15,w14,#0xf8 | `FALL_THROUGH`
<a id="insn-005ceca0"></a> `005ceca0` | `ff c1 00 71` | cmp w15,#0x30 | `FALL_THROUGH`
<a id="insn-005ceca4"></a> `005ceca4` | `80 00 00 54` | b.eq 0x005cecb4 | `CONDITIONAL_JUMP`
<a id="insn-005ceca8"></a> `005ceca8` | `cf 19 1f 12` | and w15,w14,#0xfe | `FALL_THROUGH`
<a id="insn-005cecac"></a> `005cecac` | `ff e1 00 71` | cmp w15,#0x38 | `FALL_THROUGH`
<a id="insn-005cecb0"></a> `005cecb0` | `21 01 00 54` | b.ne 0x005cecd4 | `CONDITIONAL_JUMP`
<a id="insn-005cecb4"></a> `005cecb4` | `3f 01 0c 6b` | cmp w9,w12 | `FALL_THROUGH`
<a id="insn-005cecb8"></a> `005cecb8` | `ea 13 00 54` | b.ge 0x005cef34 | `CONDITIONAL_JUMP`
<a id="insn-005cecbc"></a> `005cecbc` | `29 39 0d 1b` | madd w9,w9,w13,w14 | `FALL_THROUGH`
<a id="insn-005cecc0"></a> `005cecc0` | `4a 05 00 91` | add x10,x10,#0x1 | `FALL_THROUGH`
<a id="insn-005cecc4"></a> `005cecc4` | `5f 01 02 eb` | cmp x10,x2 | `FALL_THROUGH`
<a id="insn-005cecc8"></a> `005cecc8` | `29 c1 00 51` | sub w9,w9,#0x30 | `FALL_THROUGH`
<a id="insn-005ceccc"></a> `005ceccc` | `61 fe ff 54` | b.ne 0x005cec98 | `CONDITIONAL_JUMP`
<a id="insn-005cecd0"></a> `005cecd0` | `ea 03 02 aa` | mov x10,x2 | `FALL_THROUGH`
<a id="insn-005cecd4"></a> `005cecd4` | `5f 01 0b eb` | cmp x10,x11 | `FALL_THROUGH`
<a id="insn-005cecd8"></a> `005cecd8` | `e0 12 00 54` | b.eq 0x005cef34 | `CONDITIONAL_JUMP`
<a id="insn-005cecdc"></a> `005cecdc` | `5f 01 02 eb` | cmp x10,x2 | `FALL_THROUGH`
<a id="insn-005cece0"></a> `005cece0` | `c0 12 00 54` | b.eq 0x005cef38 | `CONDITIONAL_JUMP`
<a id="insn-005cece4"></a> `005cece4` | `4b 01 40 39` | ldrb w11,[x10] | `FALL_THROUGH`
<a id="insn-005cece8"></a> `005cece8` | `7f b1 00 71` | cmp w11,#0x2c | `FALL_THROUGH`
<a id="insn-005cecec"></a> `005cecec` | `60 07 00 54` | b.eq 0x005cedd8 | `CONDITIONAL_JUMP`
<a id="insn-005cecf0"></a> `005cecf0` | `7f f5 01 71` | cmp w11,#0x7d | `FALL_THROUGH`
<a id="insn-005cecf4"></a> `005cecf4` | `01 12 00 54` | b.ne 0x005cef34 | `CONDITIONAL_JUMP`
<a id="insn-005cecf8"></a> `005cecf8` | `53 05 00 91` | add x19,x10,#0x1 | `FALL_THROUGH`
<a id="insn-005cecfc"></a> `005cecfc` | `28 09 00 35` | cbnz w8,0x005cee20 | `CONDITIONAL_JUMP`
<a id="insn-005ced00"></a> `005ced00` | `7f 02 02 eb` | cmp x19,x2 | `FALL_THROUGH`
<a id="insn-005ced04"></a> `005ced04` | `e0 08 00 54` | b.eq 0x005cee20 | `CONDITIONAL_JUMP`
<a id="insn-005ced08"></a> `005ced08` | `68 02 40 39` | ldrb w8,[x19] | `FALL_THROUGH`
<a id="insn-005ced0c"></a> `005ced0c` | `1f fd 00 71` | cmp w8,#0x3f | `FALL_THROUGH`
<a id="insn-005ced10"></a> `005ced10` | `81 08 00 54` | b.ne 0x005cee20 | `CONDITIONAL_JUMP`
<a id="insn-005ced14"></a> `005ced14` | `21 7d 40 93` | sxtw x1,w9 | `FALL_THROUGH`
<a id="insn-005ced18"></a> `005ced18` | `53 09 00 91` | add x19,x10,#0x2 | `FALL_THROUGH`
<a id="insn-005ced1c"></a> `005ced1c` | `e4 03 04 2a` | mov w4,w4 | `FALL_THROUGH`
<a id="insn-005ced20"></a> `005ced20` | `e5 03 05 2a` | mov w5,w5 | `FALL_THROUGH`
<a id="insn-005ced24"></a> `005ced24` | `e2 03 01 aa` | mov x2,x1 | `FALL_THROUGH`
<a id="insn-005ced28"></a> `005ced28` | `1c 00 00 14` | b 0x005ced98 | `UNCONDITIONAL_JUMP`
<a id="insn-005ced2c"></a> `005ced2c` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-005ced30"></a> `005ced30` | `7d 00 00 14` | b 0x005cef24 | `UNCONDITIONAL_JUMP`
<a id="insn-005ced34"></a> `005ced34` | `33 04 00 91` | add x19,x1,#0x1 | `FALL_THROUGH`
<a id="insn-005ced38"></a> `005ced38` | `c8 03 00 35` | cbnz w8,0x005cedb0 | `CONDITIONAL_JUMP`
<a id="insn-005ced3c"></a> `005ced3c` | `7f 02 02 eb` | cmp x19,x2 | `FALL_THROUGH`
<a id="insn-005ced40"></a> `005ced40` | `80 03 00 54` | b.eq 0x005cedb0 | `CONDITIONAL_JUMP`
<a id="insn-005ced44"></a> `005ced44` | `68 02 40 39` | ldrb w8,[x19] | `FALL_THROUGH`
<a id="insn-005ced48"></a> `005ced48` | `1f fd 00 71` | cmp w8,#0x3f | `FALL_THROUGH`
<a id="insn-005ced4c"></a> `005ced4c` | `21 03 00 54` | b.ne 0x005cedb0 | `CONDITIONAL_JUMP`
<a id="insn-005ced50"></a> `005ced50` | `33 08 00 91` | add x19,x1,#0x2 | `FALL_THROUGH`
<a id="insn-005ced54"></a> `005ced54` | `e4 03 04 2a` | mov w4,w4 | `FALL_THROUGH`
<a id="insn-005ced58"></a> `005ced58` | `e5 03 05 2a` | mov w5,w5 | `FALL_THROUGH`
<a id="insn-005ced5c"></a> `005ced5c` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-005ced60"></a> `005ced60` | `02 00 80 92` | mov x2,#-0x1 | `FALL_THROUGH`
<a id="insn-005ced64"></a> `005ced64` | `0d 00 00 14` | b 0x005ced98 | `UNCONDITIONAL_JUMP`
<a id="insn-005ced68"></a> `005ced68` | `33 04 00 91` | add x19,x1,#0x1 | `FALL_THROUGH`
<a id="insn-005ced6c"></a> `005ced6c` | `c8 02 00 35` | cbnz w8,0x005cedc4 | `CONDITIONAL_JUMP`
<a id="insn-005ced70"></a> `005ced70` | `7f 02 02 eb` | cmp x19,x2 | `FALL_THROUGH`
<a id="insn-005ced74"></a> `005ced74` | `80 02 00 54` | b.eq 0x005cedc4 | `CONDITIONAL_JUMP`
<a id="insn-005ced78"></a> `005ced78` | `68 02 40 39` | ldrb w8,[x19] | `FALL_THROUGH`
<a id="insn-005ced7c"></a> `005ced7c` | `1f fd 00 71` | cmp w8,#0x3f | `FALL_THROUGH`
<a id="insn-005ced80"></a> `005ced80` | `21 02 00 54` | b.ne 0x005cedc4 | `CONDITIONAL_JUMP`
<a id="insn-005ced84"></a> `005ced84` | `33 08 00 91` | add x19,x1,#0x2 | `FALL_THROUGH`
<a id="insn-005ced88"></a> `005ced88` | `e4 03 04 2a` | mov w4,w4 | `FALL_THROUGH`
<a id="insn-005ced8c"></a> `005ced8c` | `e5 03 05 2a` | mov w5,w5 | `FALL_THROUGH`
<a id="insn-005ced90"></a> `005ced90` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-005ced94"></a> `005ced94` | `22 00 80 52` | mov w2,#0x1 | `FALL_THROUGH`
<a id="insn-005ced98"></a> `005ced98` | `e6 03 1f 2a` | mov w6,wzr | `FALL_THROUGH`
<a id="insn-005ced9c"></a> `005ced9c` | `61 00 00 14` | b 0x005cef20 | `UNCONDITIONAL_JUMP`
<a id="insn-005ceda0"></a> `005ceda0` | `e4 03 04 2a` | mov w4,w4 | `FALL_THROUGH`
<a id="insn-005ceda4"></a> `005ceda4` | `e5 03 05 2a` | mov w5,w5 | `FALL_THROUGH`
<a id="insn-005ceda8"></a> `005ceda8` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-005cedac"></a> `005cedac` | `04 00 00 14` | b 0x005cedbc | `UNCONDITIONAL_JUMP`
<a id="insn-005cedb0"></a> `005cedb0` | `e4 03 04 2a` | mov w4,w4 | `FALL_THROUGH`
<a id="insn-005cedb4"></a> `005cedb4` | `e5 03 05 2a` | mov w5,w5 | `FALL_THROUGH`
<a id="insn-005cedb8"></a> `005cedb8` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-005cedbc"></a> `005cedbc` | `02 00 80 92` | mov x2,#-0x1 | `FALL_THROUGH`
<a id="insn-005cedc0"></a> `005cedc0` | `57 00 00 14` | b 0x005cef1c | `UNCONDITIONAL_JUMP`
<a id="insn-005cedc4"></a> `005cedc4` | `e4 03 04 2a` | mov w4,w4 | `FALL_THROUGH`
<a id="insn-005cedc8"></a> `005cedc8` | `e5 03 05 2a` | mov w5,w5 | `FALL_THROUGH`
<a id="insn-005cedcc"></a> `005cedcc` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-005cedd0"></a> `005cedd0` | `22 00 80 52` | mov w2,#0x1 | `FALL_THROUGH`
<a id="insn-005cedd4"></a> `005cedd4` | `52 00 00 14` | b 0x005cef1c | `UNCONDITIONAL_JUMP`
<a id="insn-005cedd8"></a> `005cedd8` | `4c 05 00 91` | add x12,x10,#0x1 | `FALL_THROUGH`
<a id="insn-005ceddc"></a> `005ceddc` | `9f 01 02 eb` | cmp x12,x2 | `FALL_THROUGH`
<a id="insn-005cede0"></a> `005cede0` | `a0 0a 00 54` | b.eq 0x005cef34 | `CONDITIONAL_JUMP`
<a id="insn-005cede4"></a> `005cede4` | `8b 01 40 39` | ldrb w11,[x12] | `FALL_THROUGH`
<a id="insn-005cede8"></a> `005cede8` | `7f f5 01 71` | cmp w11,#0x7d | `FALL_THROUGH`
<a id="insn-005cedec"></a> `005cedec` | `41 02 00 54` | b.ne 0x005cee34 | `CONDITIONAL_JUMP`
<a id="insn-005cedf0"></a> `005cedf0` | `53 09 00 91` | add x19,x10,#0x2 | `FALL_THROUGH`
<a id="insn-005cedf4"></a> `005cedf4` | `48 08 00 35` | cbnz w8,0x005ceefc | `CONDITIONAL_JUMP`
<a id="insn-005cedf8"></a> `005cedf8` | `7f 02 02 eb` | cmp x19,x2 | `FALL_THROUGH`
<a id="insn-005cedfc"></a> `005cedfc` | `00 08 00 54` | b.eq 0x005ceefc | `CONDITIONAL_JUMP`
<a id="insn-005cee00"></a> `005cee00` | `68 02 40 39` | ldrb w8,[x19] | `FALL_THROUGH`
<a id="insn-005cee04"></a> `005cee04` | `1f fd 00 71` | cmp w8,#0x3f | `FALL_THROUGH`
<a id="insn-005cee08"></a> `005cee08` | `a1 07 00 54` | b.ne 0x005ceefc | `CONDITIONAL_JUMP`
<a id="insn-005cee0c"></a> `005cee0c` | `21 7d 40 93` | sxtw x1,w9 | `FALL_THROUGH`
<a id="insn-005cee10"></a> `005cee10` | `53 0d 00 91` | add x19,x10,#0x3 | `FALL_THROUGH`
<a id="insn-005cee14"></a> `005cee14` | `e4 03 04 2a` | mov w4,w4 | `FALL_THROUGH`
<a id="insn-005cee18"></a> `005cee18` | `e5 03 05 2a` | mov w5,w5 | `FALL_THROUGH`
<a id="insn-005cee1c"></a> `005cee1c` | `d1 ff ff 17` | b 0x005ced60 | `UNCONDITIONAL_JUMP`
<a id="insn-005cee20"></a> `005cee20` | `21 7d 40 93` | sxtw x1,w9 | `FALL_THROUGH`
<a id="insn-005cee24"></a> `005cee24` | `e4 03 04 2a` | mov w4,w4 | `FALL_THROUGH`
<a id="insn-005cee28"></a> `005cee28` | `e5 03 05 2a` | mov w5,w5 | `FALL_THROUGH`
<a id="insn-005cee2c"></a> `005cee2c` | `e2 03 01 aa` | mov x2,x1 | `FALL_THROUGH`
<a id="insn-005cee30"></a> `005cee30` | `3b 00 00 14` | b 0x005cef1c | `UNCONDITIONAL_JUMP`
<a id="insn-005cee34"></a> `005cee34` | `6d 11 1d 12` | and w13,w11,#0xf8 | `FALL_THROUGH`
<a id="insn-005cee38"></a> `005cee38` | `bf c1 00 71` | cmp w13,#0x30 | `FALL_THROUGH`
<a id="insn-005cee3c"></a> `005cee3c` | `80 00 00 54` | b.eq 0x005cee4c | `CONDITIONAL_JUMP`
<a id="insn-005cee40"></a> `005cee40` | `6d 19 1f 12` | and w13,w11,#0xfe | `FALL_THROUGH`
<a id="insn-005cee44"></a> `005cee44` | `bf e1 00 71` | cmp w13,#0x38 | `FALL_THROUGH`
<a id="insn-005cee48"></a> `005cee48` | `81 07 00 54` | b.ne 0x005cef38 | `CONDITIONAL_JUMP`
<a id="insn-005cee4c"></a> `005cee4c` | `4a 09 00 91` | add x10,x10,#0x2 | `FALL_THROUGH`
<a id="insn-005cee50"></a> `005cee50` | `6b c1 00 51` | sub w11,w11,#0x30 | `FALL_THROUGH`
<a id="insn-005cee54"></a> `005cee54` | `5f 01 02 eb` | cmp x10,x2 | `FALL_THROUGH`
<a id="insn-005cee58"></a> `005cee58` | `40 02 00 54` | b.eq 0x005ceea0 | `CONDITIONAL_JUMP`
<a id="insn-005cee5c"></a> `005cee5c` | `8d 99 99 52` | mov w13,#0xcccc | `FALL_THROUGH`
<a id="insn-005cee60"></a> `005cee60` | `4e 01 80 52` | mov w14,#0xa | `FALL_THROUGH`
<a id="insn-005cee64"></a> `005cee64` | `8d 99 a1 72` | movk w13,#0xccc, LSL #16 | `FALL_THROUGH`
<a id="insn-005cee68"></a> `005cee68` | `4f 01 40 39` | ldrb w15,[x10] | `FALL_THROUGH`
<a id="insn-005cee6c"></a> `005cee6c` | `f0 11 1d 12` | and w16,w15,#0xf8 | `FALL_THROUGH`
<a id="insn-005cee70"></a> `005cee70` | `1f c2 00 71` | cmp w16,#0x30 | `FALL_THROUGH`
<a id="insn-005cee74"></a> `005cee74` | `80 00 00 54` | b.eq 0x005cee84 | `CONDITIONAL_JUMP`
<a id="insn-005cee78"></a> `005cee78` | `f0 19 1f 12` | and w16,w15,#0xfe | `FALL_THROUGH`
<a id="insn-005cee7c"></a> `005cee7c` | `1f e2 00 71` | cmp w16,#0x38 | `FALL_THROUGH`
<a id="insn-005cee80"></a> `005cee80` | `21 01 00 54` | b.ne 0x005ceea4 | `CONDITIONAL_JUMP`
<a id="insn-005cee84"></a> `005cee84` | `7f 01 0d 6b` | cmp w11,w13 | `FALL_THROUGH`
<a id="insn-005cee88"></a> `005cee88` | `6a 05 00 54` | b.ge 0x005cef34 | `CONDITIONAL_JUMP`
<a id="insn-005cee8c"></a> `005cee8c` | `6b 3d 0e 1b` | madd w11,w11,w14,w15 | `FALL_THROUGH`
<a id="insn-005cee90"></a> `005cee90` | `4a 05 00 91` | add x10,x10,#0x1 | `FALL_THROUGH`
<a id="insn-005cee94"></a> `005cee94` | `5f 01 02 eb` | cmp x10,x2 | `FALL_THROUGH`
<a id="insn-005cee98"></a> `005cee98` | `6b c1 00 51` | sub w11,w11,#0x30 | `FALL_THROUGH`
<a id="insn-005cee9c"></a> `005cee9c` | `61 fe ff 54` | b.ne 0x005cee68 | `CONDITIONAL_JUMP`
<a id="insn-005ceea0"></a> `005ceea0` | `ea 03 02 aa` | mov x10,x2 | `FALL_THROUGH`
<a id="insn-005ceea4"></a> `005ceea4` | `5f 01 0c eb` | cmp x10,x12 | `FALL_THROUGH`
<a id="insn-005ceea8"></a> `005ceea8` | `80 04 00 54` | b.eq 0x005cef38 | `CONDITIONAL_JUMP`
<a id="insn-005ceeac"></a> `005ceeac` | `5f 01 02 eb` | cmp x10,x2 | `FALL_THROUGH`
<a id="insn-005ceeb0"></a> `005ceeb0` | `40 04 00 54` | b.eq 0x005cef38 | `CONDITIONAL_JUMP`
<a id="insn-005ceeb4"></a> `005ceeb4` | `4c 01 40 39` | ldrb w12,[x10] | `FALL_THROUGH`
<a id="insn-005ceeb8"></a> `005ceeb8` | `9f f5 01 71` | cmp w12,#0x7d | `FALL_THROUGH`
<a id="insn-005ceebc"></a> `005ceebc` | `e1 03 00 54` | b.ne 0x005cef38 | `CONDITIONAL_JUMP`
<a id="insn-005ceec0"></a> `005ceec0` | `7f 01 09 6b` | cmp w11,w9 | `FALL_THROUGH`
<a id="insn-005ceec4"></a> `005ceec4` | `8b 03 00 54` | b.lt 0x005cef34 | `CONDITIONAL_JUMP`
<a id="insn-005ceec8"></a> `005ceec8` | `53 05 00 91` | add x19,x10,#0x1 | `FALL_THROUGH`
<a id="insn-005ceecc"></a> `005ceecc` | `08 02 00 35` | cbnz w8,0x005cef0c | `CONDITIONAL_JUMP`
<a id="insn-005ceed0"></a> `005ceed0` | `7f 02 02 eb` | cmp x19,x2 | `FALL_THROUGH`
<a id="insn-005ceed4"></a> `005ceed4` | `c0 01 00 54` | b.eq 0x005cef0c | `CONDITIONAL_JUMP`
<a id="insn-005ceed8"></a> `005ceed8` | `68 02 40 39` | ldrb w8,[x19] | `FALL_THROUGH`
<a id="insn-005ceedc"></a> `005ceedc` | `1f fd 00 71` | cmp w8,#0x3f | `FALL_THROUGH`
<a id="insn-005ceee0"></a> `005ceee0` | `61 01 00 54` | b.ne 0x005cef0c | `CONDITIONAL_JUMP`
<a id="insn-005ceee4"></a> `005ceee4` | `21 7d 40 93` | sxtw x1,w9 | `FALL_THROUGH`
<a id="insn-005ceee8"></a> `005ceee8` | `62 7d 40 93` | sxtw x2,w11 | `FALL_THROUGH`
<a id="insn-005ceeec"></a> `005ceeec` | `53 09 00 91` | add x19,x10,#0x2 | `FALL_THROUGH`
<a id="insn-005ceef0"></a> `005ceef0` | `e4 03 04 2a` | mov w4,w4 | `FALL_THROUGH`
<a id="insn-005ceef4"></a> `005ceef4` | `e5 03 05 2a` | mov w5,w5 | `FALL_THROUGH`
<a id="insn-005ceef8"></a> `005ceef8` | `a8 ff ff 17` | b 0x005ced98 | `UNCONDITIONAL_JUMP`
<a id="insn-005ceefc"></a> `005ceefc` | `21 7d 40 93` | sxtw x1,w9 | `FALL_THROUGH`
<a id="insn-005cef00"></a> `005cef00` | `e4 03 04 2a` | mov w4,w4 | `FALL_THROUGH`
<a id="insn-005cef04"></a> `005cef04` | `e5 03 05 2a` | mov w5,w5 | `FALL_THROUGH`
<a id="insn-005cef08"></a> `005cef08` | `ad ff ff 17` | b 0x005cedbc | `UNCONDITIONAL_JUMP`
<a id="insn-005cef0c"></a> `005cef0c` | `21 7d 40 93` | sxtw x1,w9 | `FALL_THROUGH`
<a id="insn-005cef10"></a> `005cef10` | `62 7d 40 93` | sxtw x2,w11 | `FALL_THROUGH`
<a id="insn-005cef14"></a> `005cef14` | `e4 03 04 2a` | mov w4,w4 | `FALL_THROUGH`
<a id="insn-005cef18"></a> `005cef18` | `e5 03 05 2a` | mov w5,w5 | `FALL_THROUGH`
<a id="insn-005cef1c"></a> `005cef1c` | `26 00 80 52` | mov w6,#0x1 | `FALL_THROUGH`
<a id="insn-005cef20"></a> `005cef20` | `fa 16 00 94` | bl 0x005d4b08 | `UNCONDITIONAL_CALL`
<a id="insn-005cef24"></a> `005cef24` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-005cef28"></a> `005cef28` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-005cef2c"></a> `005cef2c` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-005cef30"></a> `005cef30` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-005cef34"></a> `005cef34` | `45 17 00 94` | bl 0x005d4c48 | `CALL_TERMINATOR`
<a id="insn-005cef38"></a> `005cef38` | `57 17 00 94` | bl 0x005d4c94 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`005cebdc`](#insn-005cebdc) 範囲 `[['005cebdc', '005cebef']]`
  - `CONDITIONAL_JUMP` [`005cebec`](#insn-005cebec) → [`005ced2c`](#insn-005ced2c)
  - `FALL_THROUGH` [`005cebec`](#insn-005cebec) → [`005cebf0`](#insn-005cebf0)
- ブロック [`005cebf0`](#insn-005cebf0) 範囲 `[['005cebf0', '005cec03']]`
  - `CONDITIONAL_JUMP` [`005cec00`](#insn-005cec00) → [`005cec44`](#insn-005cec44)
  - `FALL_THROUGH` [`005cec00`](#insn-005cec00) → [`005cec04`](#insn-005cec04)
- ブロック [`005cec04`](#insn-005cec04) 範囲 `[['005cec04', '005cec0b']]`
  - `CONDITIONAL_JUMP` [`005cec08`](#insn-005cec08) → [`005ced34`](#insn-005ced34)
  - `FALL_THROUGH` [`005cec08`](#insn-005cec08) → [`005cec0c`](#insn-005cec0c)
- ブロック [`005cec0c`](#insn-005cec0c) 範囲 `[['005cec0c', '005cec13']]`
  - `CONDITIONAL_JUMP` [`005cec10`](#insn-005cec10) → [`005ced2c`](#insn-005ced2c)
  - `FALL_THROUGH` [`005cec10`](#insn-005cec10) → [`005cec14`](#insn-005cec14)
- ブロック [`005cec14`](#insn-005cec14) 範囲 `[['005cec14', '005cec1b']]`
  - `CONDITIONAL_JUMP` [`005cec18`](#insn-005cec18) → [`005ceda0`](#insn-005ceda0)
  - `FALL_THROUGH` [`005cec18`](#insn-005cec18) → [`005cec1c`](#insn-005cec1c)
- ブロック [`005cec1c`](#insn-005cec1c) 範囲 `[['005cec1c', '005cec23']]`
  - `CONDITIONAL_JUMP` [`005cec20`](#insn-005cec20) → [`005ceda0`](#insn-005ceda0)
  - `FALL_THROUGH` [`005cec20`](#insn-005cec20) → [`005cec24`](#insn-005cec24)
- ブロック [`005cec24`](#insn-005cec24) 範囲 `[['005cec24', '005cec2f']]`
  - `CONDITIONAL_JUMP` [`005cec2c`](#insn-005cec2c) → [`005ceda0`](#insn-005ceda0)
  - `FALL_THROUGH` [`005cec2c`](#insn-005cec2c) → [`005cec30`](#insn-005cec30)
- ブロック [`005cec30`](#insn-005cec30) 範囲 `[['005cec30', '005cec43']]`
  - `UNCONDITIONAL_JUMP` [`005cec40`](#insn-005cec40) → [`005ced60`](#insn-005ced60)
- ブロック [`005cec44`](#insn-005cec44) 範囲 `[['005cec44', '005cec4b']]`
  - `CONDITIONAL_JUMP` [`005cec48`](#insn-005cec48) → [`005ced68`](#insn-005ced68)
  - `FALL_THROUGH` [`005cec48`](#insn-005cec48) → [`005cec4c`](#insn-005cec4c)
- ブロック [`005cec4c`](#insn-005cec4c) 範囲 `[['005cec4c', '005cec53']]`
  - `CONDITIONAL_JUMP` [`005cec50`](#insn-005cec50) → [`005ced2c`](#insn-005ced2c)
  - `FALL_THROUGH` [`005cec50`](#insn-005cec50) → [`005cec54`](#insn-005cec54)
- ブロック [`005cec54`](#insn-005cec54) 範囲 `[['005cec54', '005cec5f']]`
  - `CONDITIONAL_JUMP` [`005cec5c`](#insn-005cec5c) → [`005cef34`](#insn-005cef34)
  - `FALL_THROUGH` [`005cec5c`](#insn-005cec5c) → [`005cec60`](#insn-005cec60)
- ブロック [`005cec60`](#insn-005cec60) 範囲 `[['005cec60', '005cec6f']]`
  - `CONDITIONAL_JUMP` [`005cec6c`](#insn-005cec6c) → [`005cec7c`](#insn-005cec7c)
  - `FALL_THROUGH` [`005cec6c`](#insn-005cec6c) → [`005cec70`](#insn-005cec70)
- ブロック [`005cec70`](#insn-005cec70) 範囲 `[['005cec70', '005cec7b']]`
  - `CONDITIONAL_JUMP` [`005cec78`](#insn-005cec78) → [`005cef34`](#insn-005cef34)
  - `FALL_THROUGH` [`005cec78`](#insn-005cec78) → [`005cec7c`](#insn-005cec7c)
- ブロック [`005cec7c`](#insn-005cec7c) 範囲 `[['005cec7c', '005cec8b']]`
  - `CONDITIONAL_JUMP` [`005cec88`](#insn-005cec88) → [`005cecd0`](#insn-005cecd0)
  - `FALL_THROUGH` [`005cec88`](#insn-005cec88) → [`005cec8c`](#insn-005cec8c)
- ブロック [`005cec8c`](#insn-005cec8c) 範囲 `[['005cec8c', '005cec97']]`
  - `FALL_THROUGH` [`005cec94`](#insn-005cec94) → [`005cec98`](#insn-005cec98)
- ブロック [`005cec98`](#insn-005cec98) 範囲 `[['005cec98', '005ceca7']]`
  - `CONDITIONAL_JUMP` [`005ceca4`](#insn-005ceca4) → [`005cecb4`](#insn-005cecb4)
  - `FALL_THROUGH` [`005ceca4`](#insn-005ceca4) → [`005ceca8`](#insn-005ceca8)
- ブロック [`005ceca8`](#insn-005ceca8) 範囲 `[['005ceca8', '005cecb3']]`
  - `CONDITIONAL_JUMP` [`005cecb0`](#insn-005cecb0) → [`005cecd4`](#insn-005cecd4)
  - `FALL_THROUGH` [`005cecb0`](#insn-005cecb0) → [`005cecb4`](#insn-005cecb4)
- ブロック [`005cecb4`](#insn-005cecb4) 範囲 `[['005cecb4', '005cecbb']]`
  - `CONDITIONAL_JUMP` [`005cecb8`](#insn-005cecb8) → [`005cef34`](#insn-005cef34)
  - `FALL_THROUGH` [`005cecb8`](#insn-005cecb8) → [`005cecbc`](#insn-005cecbc)
- ブロック [`005cecbc`](#insn-005cecbc) 範囲 `[['005cecbc', '005ceccf']]`
  - `CONDITIONAL_JUMP` [`005ceccc`](#insn-005ceccc) → [`005cec98`](#insn-005cec98)
  - `FALL_THROUGH` [`005ceccc`](#insn-005ceccc) → [`005cecd0`](#insn-005cecd0)
- ブロック [`005cecd0`](#insn-005cecd0) 範囲 `[['005cecd0', '005cecd3']]`
  - `FALL_THROUGH` [`005cecd0`](#insn-005cecd0) → [`005cecd4`](#insn-005cecd4)
- ブロック [`005cecd4`](#insn-005cecd4) 範囲 `[['005cecd4', '005cecdb']]`
  - `CONDITIONAL_JUMP` [`005cecd8`](#insn-005cecd8) → [`005cef34`](#insn-005cef34)
  - `FALL_THROUGH` [`005cecd8`](#insn-005cecd8) → [`005cecdc`](#insn-005cecdc)
- ブロック [`005cecdc`](#insn-005cecdc) 範囲 `[['005cecdc', '005cece3']]`
  - `CONDITIONAL_JUMP` [`005cece0`](#insn-005cece0) → [`005cef38`](#insn-005cef38)
  - `FALL_THROUGH` [`005cece0`](#insn-005cece0) → [`005cece4`](#insn-005cece4)
- ブロック [`005cece4`](#insn-005cece4) 範囲 `[['005cece4', '005cecef']]`
  - `CONDITIONAL_JUMP` [`005cecec`](#insn-005cecec) → [`005cedd8`](#insn-005cedd8)
  - `FALL_THROUGH` [`005cecec`](#insn-005cecec) → [`005cecf0`](#insn-005cecf0)
- ブロック [`005cecf0`](#insn-005cecf0) 範囲 `[['005cecf0', '005cecf7']]`
  - `CONDITIONAL_JUMP` [`005cecf4`](#insn-005cecf4) → [`005cef34`](#insn-005cef34)
  - `FALL_THROUGH` [`005cecf4`](#insn-005cecf4) → [`005cecf8`](#insn-005cecf8)
- ブロック [`005cecf8`](#insn-005cecf8) 範囲 `[['005cecf8', '005cecff']]`
  - `CONDITIONAL_JUMP` [`005cecfc`](#insn-005cecfc) → [`005cee20`](#insn-005cee20)
  - `FALL_THROUGH` [`005cecfc`](#insn-005cecfc) → [`005ced00`](#insn-005ced00)
- ブロック [`005ced00`](#insn-005ced00) 範囲 `[['005ced00', '005ced07']]`
  - `CONDITIONAL_JUMP` [`005ced04`](#insn-005ced04) → [`005cee20`](#insn-005cee20)
  - `FALL_THROUGH` [`005ced04`](#insn-005ced04) → [`005ced08`](#insn-005ced08)
- ブロック [`005ced08`](#insn-005ced08) 範囲 `[['005ced08', '005ced13']]`
  - `CONDITIONAL_JUMP` [`005ced10`](#insn-005ced10) → [`005cee20`](#insn-005cee20)
  - `FALL_THROUGH` [`005ced10`](#insn-005ced10) → [`005ced14`](#insn-005ced14)
- ブロック [`005ced14`](#insn-005ced14) 範囲 `[['005ced14', '005ced2b']]`
  - `UNCONDITIONAL_JUMP` [`005ced28`](#insn-005ced28) → [`005ced98`](#insn-005ced98)
- ブロック [`005ced2c`](#insn-005ced2c) 範囲 `[['005ced2c', '005ced33']]`
  - `UNCONDITIONAL_JUMP` [`005ced30`](#insn-005ced30) → [`005cef24`](#insn-005cef24)
- ブロック [`005ced34`](#insn-005ced34) 範囲 `[['005ced34', '005ced3b']]`
  - `CONDITIONAL_JUMP` [`005ced38`](#insn-005ced38) → [`005cedb0`](#insn-005cedb0)
  - `FALL_THROUGH` [`005ced38`](#insn-005ced38) → [`005ced3c`](#insn-005ced3c)
- ブロック [`005ced3c`](#insn-005ced3c) 範囲 `[['005ced3c', '005ced43']]`
  - `CONDITIONAL_JUMP` [`005ced40`](#insn-005ced40) → [`005cedb0`](#insn-005cedb0)
  - `FALL_THROUGH` [`005ced40`](#insn-005ced40) → [`005ced44`](#insn-005ced44)
- ブロック [`005ced44`](#insn-005ced44) 範囲 `[['005ced44', '005ced4f']]`
  - `CONDITIONAL_JUMP` [`005ced4c`](#insn-005ced4c) → [`005cedb0`](#insn-005cedb0)
  - `FALL_THROUGH` [`005ced4c`](#insn-005ced4c) → [`005ced50`](#insn-005ced50)
- ブロック [`005ced50`](#insn-005ced50) 範囲 `[['005ced50', '005ced5f']]`
  - `FALL_THROUGH` [`005ced5c`](#insn-005ced5c) → [`005ced60`](#insn-005ced60)
- ブロック [`005ced60`](#insn-005ced60) 範囲 `[['005ced60', '005ced67']]`
  - `UNCONDITIONAL_JUMP` [`005ced64`](#insn-005ced64) → [`005ced98`](#insn-005ced98)
- ブロック [`005ced68`](#insn-005ced68) 範囲 `[['005ced68', '005ced6f']]`
  - `CONDITIONAL_JUMP` [`005ced6c`](#insn-005ced6c) → [`005cedc4`](#insn-005cedc4)
  - `FALL_THROUGH` [`005ced6c`](#insn-005ced6c) → [`005ced70`](#insn-005ced70)
- ブロック [`005ced70`](#insn-005ced70) 範囲 `[['005ced70', '005ced77']]`
  - `CONDITIONAL_JUMP` [`005ced74`](#insn-005ced74) → [`005cedc4`](#insn-005cedc4)
  - `FALL_THROUGH` [`005ced74`](#insn-005ced74) → [`005ced78`](#insn-005ced78)
- ブロック [`005ced78`](#insn-005ced78) 範囲 `[['005ced78', '005ced83']]`
  - `CONDITIONAL_JUMP` [`005ced80`](#insn-005ced80) → [`005cedc4`](#insn-005cedc4)
  - `FALL_THROUGH` [`005ced80`](#insn-005ced80) → [`005ced84`](#insn-005ced84)
- ブロック [`005ced84`](#insn-005ced84) 範囲 `[['005ced84', '005ced97']]`
  - `FALL_THROUGH` [`005ced94`](#insn-005ced94) → [`005ced98`](#insn-005ced98)
- ブロック [`005ced98`](#insn-005ced98) 範囲 `[['005ced98', '005ced9f']]`
  - `UNCONDITIONAL_JUMP` [`005ced9c`](#insn-005ced9c) → [`005cef20`](#insn-005cef20)
- ブロック [`005ceda0`](#insn-005ceda0) 範囲 `[['005ceda0', '005cedaf']]`
  - `UNCONDITIONAL_JUMP` [`005cedac`](#insn-005cedac) → [`005cedbc`](#insn-005cedbc)
- ブロック [`005cedb0`](#insn-005cedb0) 範囲 `[['005cedb0', '005cedbb']]`
  - `FALL_THROUGH` [`005cedb8`](#insn-005cedb8) → [`005cedbc`](#insn-005cedbc)
- ブロック [`005cedbc`](#insn-005cedbc) 範囲 `[['005cedbc', '005cedc3']]`
  - `UNCONDITIONAL_JUMP` [`005cedc0`](#insn-005cedc0) → [`005cef1c`](#insn-005cef1c)
- ブロック [`005cedc4`](#insn-005cedc4) 範囲 `[['005cedc4', '005cedd7']]`
  - `UNCONDITIONAL_JUMP` [`005cedd4`](#insn-005cedd4) → [`005cef1c`](#insn-005cef1c)
- ブロック [`005cedd8`](#insn-005cedd8) 範囲 `[['005cedd8', '005cede3']]`
  - `CONDITIONAL_JUMP` [`005cede0`](#insn-005cede0) → [`005cef34`](#insn-005cef34)
  - `FALL_THROUGH` [`005cede0`](#insn-005cede0) → [`005cede4`](#insn-005cede4)
- ブロック [`005cede4`](#insn-005cede4) 範囲 `[['005cede4', '005cedef']]`
  - `CONDITIONAL_JUMP` [`005cedec`](#insn-005cedec) → [`005cee34`](#insn-005cee34)
  - `FALL_THROUGH` [`005cedec`](#insn-005cedec) → [`005cedf0`](#insn-005cedf0)
- ブロック [`005cedf0`](#insn-005cedf0) 範囲 `[['005cedf0', '005cedf7']]`
  - `CONDITIONAL_JUMP` [`005cedf4`](#insn-005cedf4) → [`005ceefc`](#insn-005ceefc)
  - `FALL_THROUGH` [`005cedf4`](#insn-005cedf4) → [`005cedf8`](#insn-005cedf8)
- ブロック [`005cedf8`](#insn-005cedf8) 範囲 `[['005cedf8', '005cedff']]`
  - `CONDITIONAL_JUMP` [`005cedfc`](#insn-005cedfc) → [`005ceefc`](#insn-005ceefc)
  - `FALL_THROUGH` [`005cedfc`](#insn-005cedfc) → [`005cee00`](#insn-005cee00)
- ブロック [`005cee00`](#insn-005cee00) 範囲 `[['005cee00', '005cee0b']]`
  - `CONDITIONAL_JUMP` [`005cee08`](#insn-005cee08) → [`005ceefc`](#insn-005ceefc)
  - `FALL_THROUGH` [`005cee08`](#insn-005cee08) → [`005cee0c`](#insn-005cee0c)
- ブロック [`005cee0c`](#insn-005cee0c) 範囲 `[['005cee0c', '005cee1f']]`
  - `UNCONDITIONAL_JUMP` [`005cee1c`](#insn-005cee1c) → [`005ced60`](#insn-005ced60)
- ブロック [`005cee20`](#insn-005cee20) 範囲 `[['005cee20', '005cee33']]`
  - `UNCONDITIONAL_JUMP` [`005cee30`](#insn-005cee30) → [`005cef1c`](#insn-005cef1c)
- ブロック [`005cee34`](#insn-005cee34) 範囲 `[['005cee34', '005cee3f']]`
  - `CONDITIONAL_JUMP` [`005cee3c`](#insn-005cee3c) → [`005cee4c`](#insn-005cee4c)
  - `FALL_THROUGH` [`005cee3c`](#insn-005cee3c) → [`005cee40`](#insn-005cee40)
- ブロック [`005cee40`](#insn-005cee40) 範囲 `[['005cee40', '005cee4b']]`
  - `CONDITIONAL_JUMP` [`005cee48`](#insn-005cee48) → [`005cef38`](#insn-005cef38)
  - `FALL_THROUGH` [`005cee48`](#insn-005cee48) → [`005cee4c`](#insn-005cee4c)
- ブロック [`005cee4c`](#insn-005cee4c) 範囲 `[['005cee4c', '005cee5b']]`
  - `CONDITIONAL_JUMP` [`005cee58`](#insn-005cee58) → [`005ceea0`](#insn-005ceea0)
  - `FALL_THROUGH` [`005cee58`](#insn-005cee58) → [`005cee5c`](#insn-005cee5c)
- ブロック [`005cee5c`](#insn-005cee5c) 範囲 `[['005cee5c', '005cee67']]`
  - `FALL_THROUGH` [`005cee64`](#insn-005cee64) → [`005cee68`](#insn-005cee68)
- ブロック [`005cee68`](#insn-005cee68) 範囲 `[['005cee68', '005cee77']]`
  - `CONDITIONAL_JUMP` [`005cee74`](#insn-005cee74) → [`005cee84`](#insn-005cee84)
  - `FALL_THROUGH` [`005cee74`](#insn-005cee74) → [`005cee78`](#insn-005cee78)
- ブロック [`005cee78`](#insn-005cee78) 範囲 `[['005cee78', '005cee83']]`
  - `CONDITIONAL_JUMP` [`005cee80`](#insn-005cee80) → [`005ceea4`](#insn-005ceea4)
  - `FALL_THROUGH` [`005cee80`](#insn-005cee80) → [`005cee84`](#insn-005cee84)
- ブロック [`005cee84`](#insn-005cee84) 範囲 `[['005cee84', '005cee8b']]`
  - `CONDITIONAL_JUMP` [`005cee88`](#insn-005cee88) → [`005cef34`](#insn-005cef34)
  - `FALL_THROUGH` [`005cee88`](#insn-005cee88) → [`005cee8c`](#insn-005cee8c)
- ブロック [`005cee8c`](#insn-005cee8c) 範囲 `[['005cee8c', '005cee9f']]`
  - `CONDITIONAL_JUMP` [`005cee9c`](#insn-005cee9c) → [`005cee68`](#insn-005cee68)
  - `FALL_THROUGH` [`005cee9c`](#insn-005cee9c) → [`005ceea0`](#insn-005ceea0)
- ブロック [`005ceea0`](#insn-005ceea0) 範囲 `[['005ceea0', '005ceea3']]`
  - `FALL_THROUGH` [`005ceea0`](#insn-005ceea0) → [`005ceea4`](#insn-005ceea4)
- ブロック [`005ceea4`](#insn-005ceea4) 範囲 `[['005ceea4', '005ceeab']]`
  - `CONDITIONAL_JUMP` [`005ceea8`](#insn-005ceea8) → [`005cef38`](#insn-005cef38)
  - `FALL_THROUGH` [`005ceea8`](#insn-005ceea8) → [`005ceeac`](#insn-005ceeac)
- ブロック [`005ceeac`](#insn-005ceeac) 範囲 `[['005ceeac', '005ceeb3']]`
  - `CONDITIONAL_JUMP` [`005ceeb0`](#insn-005ceeb0) → [`005cef38`](#insn-005cef38)
  - `FALL_THROUGH` [`005ceeb0`](#insn-005ceeb0) → [`005ceeb4`](#insn-005ceeb4)
- ブロック [`005ceeb4`](#insn-005ceeb4) 範囲 `[['005ceeb4', '005ceebf']]`
  - `CONDITIONAL_JUMP` [`005ceebc`](#insn-005ceebc) → [`005cef38`](#insn-005cef38)
  - `FALL_THROUGH` [`005ceebc`](#insn-005ceebc) → [`005ceec0`](#insn-005ceec0)
- ブロック [`005ceec0`](#insn-005ceec0) 範囲 `[['005ceec0', '005ceec7']]`
  - `CONDITIONAL_JUMP` [`005ceec4`](#insn-005ceec4) → [`005cef34`](#insn-005cef34)
  - `FALL_THROUGH` [`005ceec4`](#insn-005ceec4) → [`005ceec8`](#insn-005ceec8)
- ブロック [`005ceec8`](#insn-005ceec8) 範囲 `[['005ceec8', '005ceecf']]`
  - `CONDITIONAL_JUMP` [`005ceecc`](#insn-005ceecc) → [`005cef0c`](#insn-005cef0c)
  - `FALL_THROUGH` [`005ceecc`](#insn-005ceecc) → [`005ceed0`](#insn-005ceed0)
- ブロック [`005ceed0`](#insn-005ceed0) 範囲 `[['005ceed0', '005ceed7']]`
  - `CONDITIONAL_JUMP` [`005ceed4`](#insn-005ceed4) → [`005cef0c`](#insn-005cef0c)
  - `FALL_THROUGH` [`005ceed4`](#insn-005ceed4) → [`005ceed8`](#insn-005ceed8)
- ブロック [`005ceed8`](#insn-005ceed8) 範囲 `[['005ceed8', '005ceee3']]`
  - `CONDITIONAL_JUMP` [`005ceee0`](#insn-005ceee0) → [`005cef0c`](#insn-005cef0c)
  - `FALL_THROUGH` [`005ceee0`](#insn-005ceee0) → [`005ceee4`](#insn-005ceee4)
- ブロック [`005ceee4`](#insn-005ceee4) 範囲 `[['005ceee4', '005ceefb']]`
  - `UNCONDITIONAL_JUMP` [`005ceef8`](#insn-005ceef8) → [`005ced98`](#insn-005ced98)
- ブロック [`005ceefc`](#insn-005ceefc) 範囲 `[['005ceefc', '005cef0b']]`
  - `UNCONDITIONAL_JUMP` [`005cef08`](#insn-005cef08) → [`005cedbc`](#insn-005cedbc)
- ブロック [`005cef0c`](#insn-005cef0c) 範囲 `[['005cef0c', '005cef1b']]`
  - `FALL_THROUGH` [`005cef18`](#insn-005cef18) → [`005cef1c`](#insn-005cef1c)
- ブロック [`005cef1c`](#insn-005cef1c) 範囲 `[['005cef1c', '005cef1f']]`
  - `FALL_THROUGH` [`005cef1c`](#insn-005cef1c) → [`005cef20`](#insn-005cef20)
- ブロック [`005cef20`](#insn-005cef20) 範囲 `[['005cef20', '005cef23']]`
  - `FALL_THROUGH` [`005cef20`](#insn-005cef20) → [`005cef24`](#insn-005cef24)
- ブロック [`005cef24`](#insn-005cef24) 範囲 `[['005cef24', '005cef33']]`
- ブロック [`005cef34`](#insn-005cef34) 範囲 `[['005cef34', '005cef37']]`
- ブロック [`005cef38`](#insn-005cef38) 範囲 `[['005cef38', '005cef3b']]`

## 命令位置別の参照

- [`005cebdc`](#insn-005cebdc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cebe0`](#insn-005cebe0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cebec`](#insn-005cebec) → [`005ced2c`](#insn-005ced2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cec00`](#insn-005cec00) → [`005cec44`](#insn-005cec44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cec08`](#insn-005cec08) → [`005ced34`](#insn-005ced34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cec10`](#insn-005cec10) → [`005ced2c`](#insn-005ced2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cec18`](#insn-005cec18) → [`005ceda0`](#insn-005ceda0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cec20`](#insn-005cec20) → [`005ceda0`](#insn-005ceda0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cec2c`](#insn-005cec2c) → [`005ceda0`](#insn-005ceda0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cec40`](#insn-005cec40) → [`005ced60`](#insn-005ced60) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cec48`](#insn-005cec48) → [`005ced68`](#insn-005ced68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cec50`](#insn-005cec50) → [`005ced2c`](#insn-005ced2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cec5c`](#insn-005cec5c) → [`005cef34`](#insn-005cef34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cec6c`](#insn-005cec6c) → [`005cec7c`](#insn-005cec7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cec78`](#insn-005cec78) → [`005cef34`](#insn-005cef34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cec88`](#insn-005cec88) → [`005cecd0`](#insn-005cecd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005ceca4`](#insn-005ceca4) → [`005cecb4`](#insn-005cecb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cecb0`](#insn-005cecb0) → [`005cecd4`](#insn-005cecd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cecb8`](#insn-005cecb8) → [`005cef34`](#insn-005cef34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005ceccc`](#insn-005ceccc) → [`005cec98`](#insn-005cec98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cecd8`](#insn-005cecd8) → [`005cef34`](#insn-005cef34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cece0`](#insn-005cece0) → [`005cef38`](#insn-005cef38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cecec`](#insn-005cecec) → [`005cedd8`](#insn-005cedd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cecf4`](#insn-005cecf4) → [`005cef34`](#insn-005cef34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cecfc`](#insn-005cecfc) → [`005cee20`](#insn-005cee20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005ced04`](#insn-005ced04) → [`005cee20`](#insn-005cee20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005ced10`](#insn-005ced10) → [`005cee20`](#insn-005cee20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005ced28`](#insn-005ced28) → [`005ced98`](#insn-005ced98) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005ced30`](#insn-005ced30) → [`005cef24`](#insn-005cef24) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005ced38`](#insn-005ced38) → [`005cedb0`](#insn-005cedb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005ced40`](#insn-005ced40) → [`005cedb0`](#insn-005cedb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005ced4c`](#insn-005ced4c) → [`005cedb0`](#insn-005cedb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005ced64`](#insn-005ced64) → [`005ced98`](#insn-005ced98) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005ced6c`](#insn-005ced6c) → [`005cedc4`](#insn-005cedc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005ced74`](#insn-005ced74) → [`005cedc4`](#insn-005cedc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005ced80`](#insn-005ced80) → [`005cedc4`](#insn-005cedc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005ced9c`](#insn-005ced9c) → [`005cef20`](#insn-005cef20) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cedac`](#insn-005cedac) → [`005cedbc`](#insn-005cedbc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cedc0`](#insn-005cedc0) → [`005cef1c`](#insn-005cef1c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cedd4`](#insn-005cedd4) → [`005cef1c`](#insn-005cef1c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cede0`](#insn-005cede0) → [`005cef34`](#insn-005cef34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cedec`](#insn-005cedec) → [`005cee34`](#insn-005cee34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cedf4`](#insn-005cedf4) → [`005ceefc`](#insn-005ceefc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cedfc`](#insn-005cedfc) → [`005ceefc`](#insn-005ceefc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cee08`](#insn-005cee08) → [`005ceefc`](#insn-005ceefc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cee1c`](#insn-005cee1c) → [`005ced60`](#insn-005ced60) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cee30`](#insn-005cee30) → [`005cef1c`](#insn-005cef1c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cee3c`](#insn-005cee3c) → [`005cee4c`](#insn-005cee4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cee48`](#insn-005cee48) → [`005cef38`](#insn-005cef38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cee58`](#insn-005cee58) → [`005ceea0`](#insn-005ceea0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cee74`](#insn-005cee74) → [`005cee84`](#insn-005cee84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cee80`](#insn-005cee80) → [`005ceea4`](#insn-005ceea4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cee88`](#insn-005cee88) → [`005cef34`](#insn-005cef34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cee9c`](#insn-005cee9c) → [`005cee68`](#insn-005cee68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005ceea8`](#insn-005ceea8) → [`005cef38`](#insn-005cef38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005ceeb0`](#insn-005ceeb0) → [`005cef38`](#insn-005cef38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005ceebc`](#insn-005ceebc) → [`005cef38`](#insn-005cef38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005ceec4`](#insn-005ceec4) → [`005cef34`](#insn-005cef34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005ceecc`](#insn-005ceecc) → [`005cef0c`](#insn-005cef0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005ceed4`](#insn-005ceed4) → [`005cef0c`](#insn-005cef0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005ceee0`](#insn-005ceee0) → [`005cef0c`](#insn-005cef0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005ceef8`](#insn-005ceef8) → [`005ced98`](#insn-005ced98) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cef08`](#insn-005cef08) → [`005cedbc`](#insn-005cedbc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cef20`](#insn-005cef20) → [`005d4b08`](../005d4/005d4b08.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005d4b08` · 推定シンボル `None` · 推定型 `None`
- [`005cef28`](#insn-005cef28) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cef2c`](#insn-005cef2c) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cef34`](#insn-005cef34) → [`005d4c48`](../005d4/005d4c48.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005d4c48` · 推定シンボル `None` · 推定型 `None`
- [`005cef38`](#insn-005cef38) → [`005d4c94`](../005d4/005d4c94.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005d4c94` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`005cebdc`](#insn-005cebdc)

~~~json
{
  "source": "005cebdc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cebe0`](#insn-005cebe0)

~~~json
{
  "source": "005cebe0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cebec`](#insn-005cebec)

~~~json
{
  "source": "005cebec",
  "target": "005ced2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cec00`](#insn-005cec00)

~~~json
{
  "source": "005cec00",
  "target": "005cec44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cec08`](#insn-005cec08)

~~~json
{
  "source": "005cec08",
  "target": "005ced34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cec10`](#insn-005cec10)

~~~json
{
  "source": "005cec10",
  "target": "005ced2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cec18`](#insn-005cec18)

~~~json
{
  "source": "005cec18",
  "target": "005ceda0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cec20`](#insn-005cec20)

~~~json
{
  "source": "005cec20",
  "target": "005ceda0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cec2c`](#insn-005cec2c)

~~~json
{
  "source": "005cec2c",
  "target": "005ceda0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cec40`](#insn-005cec40)

~~~json
{
  "source": "005cec40",
  "target": "005ced60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cec48`](#insn-005cec48)

~~~json
{
  "source": "005cec48",
  "target": "005ced68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cec50`](#insn-005cec50)

~~~json
{
  "source": "005cec50",
  "target": "005ced2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cec5c`](#insn-005cec5c)

~~~json
{
  "source": "005cec5c",
  "target": "005cef34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cec6c`](#insn-005cec6c)

~~~json
{
  "source": "005cec6c",
  "target": "005cec7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cec78`](#insn-005cec78)

~~~json
{
  "source": "005cec78",
  "target": "005cef34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cec88`](#insn-005cec88)

~~~json
{
  "source": "005cec88",
  "target": "005cecd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005ceca4`](#insn-005ceca4)

~~~json
{
  "source": "005ceca4",
  "target": "005cecb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cecb0`](#insn-005cecb0)

~~~json
{
  "source": "005cecb0",
  "target": "005cecd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cecb8`](#insn-005cecb8)

~~~json
{
  "source": "005cecb8",
  "target": "005cef34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005ceccc`](#insn-005ceccc)

~~~json
{
  "source": "005ceccc",
  "target": "005cec98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cecd8`](#insn-005cecd8)

~~~json
{
  "source": "005cecd8",
  "target": "005cef34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cece0`](#insn-005cece0)

~~~json
{
  "source": "005cece0",
  "target": "005cef38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cecec`](#insn-005cecec)

~~~json
{
  "source": "005cecec",
  "target": "005cedd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cecf4`](#insn-005cecf4)

~~~json
{
  "source": "005cecf4",
  "target": "005cef34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cecfc`](#insn-005cecfc)

~~~json
{
  "source": "005cecfc",
  "target": "005cee20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005ced04`](#insn-005ced04)

~~~json
{
  "source": "005ced04",
  "target": "005cee20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005ced10`](#insn-005ced10)

~~~json
{
  "source": "005ced10",
  "target": "005cee20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005ced28`](#insn-005ced28)

~~~json
{
  "source": "005ced28",
  "target": "005ced98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005ced30`](#insn-005ced30)

~~~json
{
  "source": "005ced30",
  "target": "005cef24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005ced38`](#insn-005ced38)

~~~json
{
  "source": "005ced38",
  "target": "005cedb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005ced40`](#insn-005ced40)

~~~json
{
  "source": "005ced40",
  "target": "005cedb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005ced4c`](#insn-005ced4c)

~~~json
{
  "source": "005ced4c",
  "target": "005cedb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005ced64`](#insn-005ced64)

~~~json
{
  "source": "005ced64",
  "target": "005ced98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005ced6c`](#insn-005ced6c)

~~~json
{
  "source": "005ced6c",
  "target": "005cedc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005ced74`](#insn-005ced74)

~~~json
{
  "source": "005ced74",
  "target": "005cedc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005ced80`](#insn-005ced80)

~~~json
{
  "source": "005ced80",
  "target": "005cedc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005ced9c`](#insn-005ced9c)

~~~json
{
  "source": "005ced9c",
  "target": "005cef20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cedac`](#insn-005cedac)

~~~json
{
  "source": "005cedac",
  "target": "005cedbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cedc0`](#insn-005cedc0)

~~~json
{
  "source": "005cedc0",
  "target": "005cef1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cedd4`](#insn-005cedd4)

~~~json
{
  "source": "005cedd4",
  "target": "005cef1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cede0`](#insn-005cede0)

~~~json
{
  "source": "005cede0",
  "target": "005cef34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cedec`](#insn-005cedec)

~~~json
{
  "source": "005cedec",
  "target": "005cee34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cedf4`](#insn-005cedf4)

~~~json
{
  "source": "005cedf4",
  "target": "005ceefc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cedfc`](#insn-005cedfc)

~~~json
{
  "source": "005cedfc",
  "target": "005ceefc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cee08`](#insn-005cee08)

~~~json
{
  "source": "005cee08",
  "target": "005ceefc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cee1c`](#insn-005cee1c)

~~~json
{
  "source": "005cee1c",
  "target": "005ced60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cee30`](#insn-005cee30)

~~~json
{
  "source": "005cee30",
  "target": "005cef1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cee3c`](#insn-005cee3c)

~~~json
{
  "source": "005cee3c",
  "target": "005cee4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cee48`](#insn-005cee48)

~~~json
{
  "source": "005cee48",
  "target": "005cef38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cee58`](#insn-005cee58)

~~~json
{
  "source": "005cee58",
  "target": "005ceea0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cee74`](#insn-005cee74)

~~~json
{
  "source": "005cee74",
  "target": "005cee84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cee80`](#insn-005cee80)

~~~json
{
  "source": "005cee80",
  "target": "005ceea4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cee88`](#insn-005cee88)

~~~json
{
  "source": "005cee88",
  "target": "005cef34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cee9c`](#insn-005cee9c)

~~~json
{
  "source": "005cee9c",
  "target": "005cee68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005ceea8`](#insn-005ceea8)

~~~json
{
  "source": "005ceea8",
  "target": "005cef38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005ceeb0`](#insn-005ceeb0)

~~~json
{
  "source": "005ceeb0",
  "target": "005cef38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005ceebc`](#insn-005ceebc)

~~~json
{
  "source": "005ceebc",
  "target": "005cef38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005ceec4`](#insn-005ceec4)

~~~json
{
  "source": "005ceec4",
  "target": "005cef34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005ceecc`](#insn-005ceecc)

~~~json
{
  "source": "005ceecc",
  "target": "005cef0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005ceed4`](#insn-005ceed4)

~~~json
{
  "source": "005ceed4",
  "target": "005cef0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005ceee0`](#insn-005ceee0)

~~~json
{
  "source": "005ceee0",
  "target": "005cef0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005ceef8`](#insn-005ceef8)

~~~json
{
  "source": "005ceef8",
  "target": "005ced98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cef08`](#insn-005cef08)

~~~json
{
  "source": "005cef08",
  "target": "005cedbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cef20`](#insn-005cef20)

~~~json
{
  "source": "005cef20",
  "target": "005d4b08",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005cef28`](#insn-005cef28)

~~~json
{
  "source": "005cef28",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cef2c`](#insn-005cef2c)

~~~json
{
  "source": "005cef2c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cef34`](#insn-005cef34)

~~~json
{
  "source": "005cef34",
  "target": "005d4c48",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005cef38`](#insn-005cef38)

~~~json
{
  "source": "005cef38",
  "target": "005d4c94",
  "target_space": "ram",
  "resolution": "function"
}
~~~
