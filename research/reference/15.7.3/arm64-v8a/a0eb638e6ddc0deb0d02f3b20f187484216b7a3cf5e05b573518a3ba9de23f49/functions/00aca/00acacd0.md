# 00acacd0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00acac08`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aca/00acac08.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0056.md#compare-7c3606e38fb63b5e29c816d58624e138)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00acad14`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aca/00acad14.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0007.md#compare-c7db17a6f61d274ac4c18a01cd3195a5)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acacd0",
  "name": "FUN_00acacd0",
  "size": 492,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "96823905f8308be8a322b4b9e0d876de5223618e64c6751795efc63d94fb63ce",
  "source_text_sha256": "96823905f8308be8a322b4b9e0d876de5223618e64c6751795efc63d94fb63ce",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00acacd0",
        "00acaeb7"
      ],
      [
        "00acaedc",
        "00acaedf"
      ]
    ],
    "bytes_sha256": "06b2df0018b64ac8e43a23404cce612eff8acd5304aa7d437f0b58c0cb022686",
    "instruction_count": 123,
    "instruction_bytes": 492,
    "body_bytes": 492,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00abf52c](../00abf/00abf52c.md)

## 呼び出し先

- [0041e380](../0041e/0041e380.md)
- [0051d884](../0051d/0051d884.md)
- [0076a658](../0076a/0076a658.md)
- [007d95c0](../007d9/007d95c0.md)
- [00bdaff0](../00bda/00bdaff0.md)
- [00bdb010](../00bdb/00bdb010.md)
- [00bdb040](../00bdb/00bdb040.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2596 bytes

~~~c

long FUN_00acacd0(long *param_1,long *param_2)

{
  ulong uVar1;
  long lVar2;
  long lVar3;
  undefined8 *puVar4;
  undefined8 *puVar5;
  long lVar6;
  byte *pbVar7;
  long lVar8;
  ulong uVar9;
  undefined8 *puVar10;
  byte *pbVar11;
  byte *pbVar12;
  void *local_80;
  undefined8 *local_78;
  undefined8 *local_70;
  void *pvStack_68;
  long *local_60;
  long local_58;
  
  lVar3 = tpidr_el0;
  local_58 = *(long *)(lVar3 + 0x28);
  lVar6 = param_1[1] - *param_1 >> 3;
  uVar1 = lVar6 * -0x5555555555555555 + 1;
  if (uVar1 < 0xaaaaaaaaaaaaaab) {
    local_60 = param_1 + 2;
    lVar8 = *local_60 - *param_1 >> 3;
    uVar9 = lVar8 * 0x5555555555555556;
    if (uVar9 < uVar1 || uVar9 - uVar1 == 0) {
      uVar9 = uVar1;
    }
    if (0x555555555555554 < (ulong)(lVar8 * -0x5555555555555555)) {
      uVar9 = 0xaaaaaaaaaaaaaaa;
    }
    if (uVar9 == 0) {
      local_80 = (void *)0x0;
    }
    else {
      if (0xaaaaaaaaaaaaaaa < uVar9) goto LAB_00acaea4;
      local_80 = (void *)_Znwm(uVar9 * 0x18);
    }
    lVar8 = *param_2;
    lVar2 = param_2[1];
    local_78 = (undefined8 *)((long)local_80 + lVar6 * 8);
    pvStack_68 = (void *)((long)local_80 + uVar9 * 0x18);
    local_78[1] = 0;
    local_78[2] = 0;
    *local_78 = 0;
    local_70 = local_78;
    FUN_0051d884(local_78,lVar8,lVar2,(lVar2 - lVar8 >> 3) * -0x5555555555555555);
    local_70 = local_70 + 3;
    FUN_007d95c0(param_1,&local_80);
    puVar5 = local_78;
    lVar6 = param_1[1];
    while (puVar4 = local_70, puVar4 != puVar5) {
      puVar10 = puVar4 + -3;
      pbVar11 = (byte *)*puVar10;
      local_70 = puVar10;
      if (pbVar11 != (byte *)0x0) {
        pbVar7 = (byte *)puVar4[-2];
        pbVar12 = pbVar11;
        if (pbVar7 != pbVar11) {
          do {
            pbVar12 = pbVar7 + -0x18;
            if ((*pbVar12 & 1) != 0) {
              _ZdlPv(*(void **)(pbVar7 + -8));
            }
            pbVar7 = pbVar12;
          } while (pbVar12 != pbVar11);
          pbVar12 = (byte *)*puVar10;
        }
        puVar4[-2] = pbVar11;
        _ZdlPv(pbVar12);
      }
    }
    local_70 = puVar4;
    if (local_80 != (void *)0x0) {
      _ZdlPv(local_80);
    }
    if (*(long *)(lVar3 + 0x28) == local_58) {
      return lVar6;
    }
  }
  else {
    if (*(long *)(lVar3 + 0x28) != local_58) goto LAB_00acaedc;
    FUN_0076a658(param_1);
LAB_00acaea4:
    if (*(long *)(lVar3 + 0x28) == local_58) {
                    /* WARNING: Subroutine does not return */
      FUN_0041e380();
    }
  }
LAB_00acaedc:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00acacd0"></a> `00acacd0` | `ff 03 02 d1` | sub sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00acacd4"></a> `00acacd4` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00acacd8"></a> `00acacd8` | `f9 23 00 f9` | str x25,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00acacdc"></a> `00acacdc` | `f8 5f 05 a9` | stp x24,x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00acace0"></a> `00acace0` | `f6 57 06 a9` | stp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00acace4"></a> `00acace4` | `f4 4f 07 a9` | stp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00acace8"></a> `00acace8` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00acacec"></a> `00acacec` | `55 d0 3b d5` | mrs x21,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00acacf0"></a> `00acacf0` | `eb f3 01 b2` | orr x11,xzr,#-0x5555555555555556 | `FALL_THROUGH`
<a id="insn-00acacf4"></a> `00acacf4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00acacf8"></a> `00acacf8` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00acacfc"></a> `00acacfc` | `6b 55 95 f2` | movk x11,#0xaaab | `FALL_THROUGH`
<a id="insn-00acad00"></a> `00acad00` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00acad04"></a> `00acad04` | `0a 20 40 a9` | ldp x10,x8,[x0] | `FALL_THROUGH`
<a id="insn-00acad08"></a> `00acad08` | `08 01 0a cb` | sub x8,x8,x10 | `FALL_THROUGH`
<a id="insn-00acad0c"></a> `00acad0c` | `08 fd 43 93` | asr x8,x8,#0x3 | `FALL_THROUGH`
<a id="insn-00acad10"></a> `00acad10` | `16 7d 0b 9b` | mul x22,x8,x11 | `FALL_THROUGH`
<a id="insn-00acad14"></a> `00acad14` | `e8 f3 01 b2` | orr x8,xzr,#-0x5555555555555556 | `FALL_THROUGH`
<a id="insn-00acad18"></a> `00acad18` | `48 55 e1 f2` | movk x8,#0xaaa, LSL #48 | `FALL_THROUGH`
<a id="insn-00acad1c"></a> `00acad1c` | `c9 06 00 91` | add x9,x22,#0x1 | `FALL_THROUGH`
<a id="insn-00acad20"></a> `00acad20` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00acad24"></a> `00acad24` | `48 0b 00 54` | b.hi 0x00acae8c | `CONDITIONAL_JUMP`
<a id="insn-00acad28"></a> `00acad28` | `ec 03 13 aa` | mov x12,x19 | `FALL_THROUGH`
<a id="insn-00acad2c"></a> `00acad2c` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00acad30"></a> `00acad30` | `8d 0d 41 f8` | ldr x13,[x12, #0x10]! | `FALL_THROUGH`
<a id="insn-00acad34"></a> `00acad34` | `ec 13 00 f9` | str x12,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00acad38"></a> `00acad38` | `aa 01 0a cb` | sub x10,x13,x10 | `FALL_THROUGH`
<a id="insn-00acad3c"></a> `00acad3c` | `ed f3 00 b2` | orr x13,xzr,#0x5555555555555555 | `FALL_THROUGH`
<a id="insn-00acad40"></a> `00acad40` | `4a fd 43 93` | asr x10,x10,#0x3 | `FALL_THROUGH`
<a id="insn-00acad44"></a> `00acad44` | `ad aa e0 f2` | movk x13,#0x555, LSL #48 | `FALL_THROUGH`
<a id="insn-00acad48"></a> `00acad48` | `4a 7d 0b 9b` | mul x10,x10,x11 | `FALL_THROUGH`
<a id="insn-00acad4c"></a> `00acad4c` | `4b f9 7f d3` | lsl x11,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00acad50"></a> `00acad50` | `7f 01 09 eb` | cmp x11,x9 | `FALL_THROUGH`
<a id="insn-00acad54"></a> `00acad54` | `69 81 89 9a` | csel x9,x11,x9,hi | `FALL_THROUGH`
<a id="insn-00acad58"></a> `00acad58` | `5f 01 0d eb` | cmp x10,x13 | `FALL_THROUGH`
<a id="insn-00acad5c"></a> `00acad5c` | `37 31 88 9a` | csel x23,x9,x8,cc | `FALL_THROUGH`
<a id="insn-00acad60"></a> `00acad60` | `f7 00 00 b4` | cbz x23,0x00acad7c | `CONDITIONAL_JUMP`
<a id="insn-00acad64"></a> `00acad64` | `ff 02 08 eb` | cmp x23,x8 | `FALL_THROUGH`
<a id="insn-00acad68"></a> `00acad68` | `e8 09 00 54` | b.hi 0x00acaea4 | `CONDITIONAL_JUMP`
<a id="insn-00acad6c"></a> `00acad6c` | `e8 06 17 8b` | add x8,x23,x23, LSL #0x1 | `FALL_THROUGH`
<a id="insn-00acad70"></a> `00acad70` | `00 f1 7d d3` | lsl x0,x8,#0x3 | `FALL_THROUGH`
<a id="insn-00acad74"></a> `00acad74` | `9f 40 04 94` | bl 0x00bdaff0 | `UNCONDITIONAL_CALL`
<a id="insn-00acad78"></a> `00acad78` | `02 00 00 14` | b 0x00acad80 | `UNCONDITIONAL_JUMP`
<a id="insn-00acad7c"></a> `00acad7c` | `e0 03 1f aa` | mov x0,xzr | `FALL_THROUGH`
<a id="insn-00acad80"></a> `00acad80` | `09 03 80 52` | mov w9,#0x18 | `FALL_THROUGH`
<a id="insn-00acad84"></a> `00acad84` | `81 0a 40 a9` | ldp x1,x2,[x20] | `FALL_THROUGH`
<a id="insn-00acad88"></a> `00acad88` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00acad8c"></a> `00acad8c` | `c8 02 09 9b` | madd x8,x22,x9,x0 | `FALL_THROUGH`
<a id="insn-00acad90"></a> `00acad90` | `eb f3 01 b2` | orr x11,xzr,#-0x5555555555555556 | `FALL_THROUGH`
<a id="insn-00acad94"></a> `00acad94` | `6b 55 95 f2` | movk x11,#0xaaab | `FALL_THROUGH`
<a id="insn-00acad98"></a> `00acad98` | `e9 02 09 9b` | madd x9,x23,x9,x0 | `FALL_THROUGH`
<a id="insn-00acad9c"></a> `00acad9c` | `4a 00 01 cb` | sub x10,x2,x1 | `FALL_THROUGH`
<a id="insn-00acada0"></a> `00acada0` | `4a fd 43 93` | asr x10,x10,#0x3 | `FALL_THROUGH`
<a id="insn-00acada4"></a> `00acada4` | `e0 23 00 a9` | stp x0,x8,[sp] | `FALL_THROUGH`
<a id="insn-00acada8"></a> `00acada8` | `43 7d 0b 9b` | mul x3,x10,x11 | `FALL_THROUGH`
<a id="insn-00acadac"></a> `00acadac` | `1f fd 00 a9` | stp xzr,xzr,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00acadb0"></a> `00acadb0` | `e8 27 01 a9` | stp x8,x9,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acadb4"></a> `00acadb4` | `1f 01 00 f9` | str xzr,[x8] | `FALL_THROUGH`
<a id="insn-00acadb8"></a> `00acadb8` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00acadbc"></a> `00acadbc` | `b2 4a e9 97` | bl 0x0051d884 | `UNCONDITIONAL_CALL`
<a id="insn-00acadc0"></a> `00acadc0` | `e8 0b 40 f9` | ldr x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acadc4"></a> `00acadc4` | `08 61 00 91` | add x8,x8,#0x18 | `FALL_THROUGH`
<a id="insn-00acadc8"></a> `00acadc8` | `e8 0b 00 f9` | str x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acadcc"></a> `00acadcc` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00acadd0"></a> `00acadd0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00acadd4"></a> `00acadd4` | `fb 39 f4 97` | bl 0x007d95c0 | `UNCONDITIONAL_CALL`
<a id="insn-00acadd8"></a> `00acadd8` | `f4 db 40 a9` | ldp x20,x22,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00acaddc"></a> `00acaddc` | `73 06 40 f9` | ldr x19,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00acade0"></a> `00acade0` | `df 02 14 eb` | cmp x22,x20 | `FALL_THROUGH`
<a id="insn-00acade4"></a> `00acade4` | `60 03 00 54` | b.eq 0x00acae50 | `CONDITIONAL_JUMP`
<a id="insn-00acade8"></a> `00acade8` | `f7 03 16 aa` | mov x23,x22 | `FALL_THROUGH`
<a id="insn-00acadec"></a> `00acadec` | `08 00 00 14` | b 0x00acae0c | `UNCONDITIONAL_JUMP`
<a id="insn-00acadf0"></a> `00acadf0` | `e0 02 40 f9` | ldr x0,[x23] | `FALL_THROUGH`
<a id="insn-00acadf4"></a> `00acadf4` | `d8 02 1f f8` | stur x24,[x22, #-0x10] | `FALL_THROUGH`
<a id="insn-00acadf8"></a> `00acadf8` | `86 40 04 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00acadfc"></a> `00acadfc` | `f7 0b 40 f9` | ldr x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acae00"></a> `00acae00` | `ff 02 14 eb` | cmp x23,x20 | `FALL_THROUGH`
<a id="insn-00acae04"></a> `00acae04` | `f6 03 17 aa` | mov x22,x23 | `FALL_THROUGH`
<a id="insn-00acae08"></a> `00acae08` | `40 02 00 54` | b.eq 0x00acae50 | `CONDITIONAL_JUMP`
<a id="insn-00acae0c"></a> `00acae0c` | `f8 8e 5e f8` | ldr x24,[x23, #-0x18]! | `FALL_THROUGH`
<a id="insn-00acae10"></a> `00acae10` | `f7 0b 00 f9` | str x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acae14"></a> `00acae14` | `78 ff ff b4` | cbz x24,0x00acae00 | `CONDITIONAL_JUMP`
<a id="insn-00acae18"></a> `00acae18` | `c8 02 5f f8` | ldur x8,[x22, #-0x10] | `FALL_THROUGH`
<a id="insn-00acae1c"></a> `00acae1c` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00acae20"></a> `00acae20` | `1f 01 18 eb` | cmp x8,x24 | `FALL_THROUGH`
<a id="insn-00acae24"></a> `00acae24` | `80 fe ff 54` | b.eq 0x00acadf4 | `CONDITIONAL_JUMP`
<a id="insn-00acae28"></a> `00acae28` | `f9 03 08 aa` | mov x25,x8 | `FALL_THROUGH`
<a id="insn-00acae2c"></a> `00acae2c` | `04 00 00 14` | b 0x00acae3c | `UNCONDITIONAL_JUMP`
<a id="insn-00acae30"></a> `00acae30` | `3f 03 18 eb` | cmp x25,x24 | `FALL_THROUGH`
<a id="insn-00acae34"></a> `00acae34` | `e8 03 19 aa` | mov x8,x25 | `FALL_THROUGH`
<a id="insn-00acae38"></a> `00acae38` | `c0 fd ff 54` | b.eq 0x00acadf0 | `CONDITIONAL_JUMP`
<a id="insn-00acae3c"></a> `00acae3c` | `29 8f 5e 38` | ldrb w9,[x25, #-0x18]! | `FALL_THROUGH`
<a id="insn-00acae40"></a> `00acae40` | `89 ff 07 36` | tbz w9,#0x0,0x00acae30 | `CONDITIONAL_JUMP`
<a id="insn-00acae44"></a> `00acae44` | `00 81 5f f8` | ldur x0,[x8, #-0x8] | `FALL_THROUGH`
<a id="insn-00acae48"></a> `00acae48` | `72 40 04 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00acae4c"></a> `00acae4c` | `f9 ff ff 17` | b 0x00acae30 | `UNCONDITIONAL_JUMP`
<a id="insn-00acae50"></a> `00acae50` | `e0 03 40 f9` | ldr x0,[sp] | `FALL_THROUGH`
<a id="insn-00acae54"></a> `00acae54` | `40 00 00 b4` | cbz x0,0x00acae5c | `CONDITIONAL_JUMP`
<a id="insn-00acae58"></a> `00acae58` | `6e 40 04 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00acae5c"></a> `00acae5c` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00acae60"></a> `00acae60` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00acae64"></a> `00acae64` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00acae68"></a> `00acae68` | `a1 03 00 54` | b.ne 0x00acaedc | `CONDITIONAL_JUMP`
<a id="insn-00acae6c"></a> `00acae6c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00acae70"></a> `00acae70` | `f4 4f 47 a9` | ldp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00acae74"></a> `00acae74` | `f9 23 40 f9` | ldr x25,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00acae78"></a> `00acae78` | `f6 57 46 a9` | ldp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00acae7c"></a> `00acae7c` | `f8 5f 45 a9` | ldp x24,x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00acae80"></a> `00acae80` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00acae84"></a> `00acae84` | `ff 03 02 91` | add sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00acae88"></a> `00acae88` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00acae8c"></a> `00acae8c` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00acae90"></a> `00acae90` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00acae94"></a> `00acae94` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00acae98"></a> `00acae98` | `21 02 00 54` | b.ne 0x00acaedc | `CONDITIONAL_JUMP`
<a id="insn-00acae9c"></a> `00acae9c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00acaea0"></a> `00acaea0` | `ee 7d f2 97` | bl 0x0076a658 | `UNCONDITIONAL_CALL`
<a id="insn-00acaea4"></a> `00acaea4` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00acaea8"></a> `00acaea8` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00acaeac"></a> `00acaeac` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00acaeb0"></a> `00acaeb0` | `61 01 00 54` | b.ne 0x00acaedc | `CONDITIONAL_JUMP`
<a id="insn-00acaeb4"></a> `00acaeb4` | `33 4d e5 97` | bl 0x0041e380 | `CALL_TERMINATOR`
<a id="insn-00acaedc"></a> `00acaedc` | `59 40 04 94` | bl 0x00bdb040 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00acacd0`](#insn-00acacd0) 範囲 `[['00acacd0', '00acad27']]`
  - `CONDITIONAL_JUMP` [`00acad24`](#insn-00acad24) → [`00acae8c`](#insn-00acae8c)
  - `FALL_THROUGH` [`00acad24`](#insn-00acad24) → [`00acad28`](#insn-00acad28)
- ブロック [`00acad28`](#insn-00acad28) 範囲 `[['00acad28', '00acad63']]`
  - `CONDITIONAL_JUMP` [`00acad60`](#insn-00acad60) → [`00acad7c`](#insn-00acad7c)
  - `FALL_THROUGH` [`00acad60`](#insn-00acad60) → [`00acad64`](#insn-00acad64)
- ブロック [`00acad64`](#insn-00acad64) 範囲 `[['00acad64', '00acad6b']]`
  - `CONDITIONAL_JUMP` [`00acad68`](#insn-00acad68) → [`00acaea4`](#insn-00acaea4)
  - `FALL_THROUGH` [`00acad68`](#insn-00acad68) → [`00acad6c`](#insn-00acad6c)
- ブロック [`00acad6c`](#insn-00acad6c) 範囲 `[['00acad6c', '00acad7b']]`
  - `UNCONDITIONAL_JUMP` [`00acad78`](#insn-00acad78) → [`00acad80`](#insn-00acad80)
- ブロック [`00acad7c`](#insn-00acad7c) 範囲 `[['00acad7c', '00acad7f']]`
  - `FALL_THROUGH` [`00acad7c`](#insn-00acad7c) → [`00acad80`](#insn-00acad80)
- ブロック [`00acad80`](#insn-00acad80) 範囲 `[['00acad80', '00acade7']]`
  - `CONDITIONAL_JUMP` [`00acade4`](#insn-00acade4) → [`00acae50`](#insn-00acae50)
  - `FALL_THROUGH` [`00acade4`](#insn-00acade4) → [`00acade8`](#insn-00acade8)
- ブロック [`00acade8`](#insn-00acade8) 範囲 `[['00acade8', '00acadef']]`
  - `UNCONDITIONAL_JUMP` [`00acadec`](#insn-00acadec) → [`00acae0c`](#insn-00acae0c)
- ブロック [`00acadf0`](#insn-00acadf0) 範囲 `[['00acadf0', '00acadf3']]`
  - `FALL_THROUGH` [`00acadf0`](#insn-00acadf0) → [`00acadf4`](#insn-00acadf4)
- ブロック [`00acadf4`](#insn-00acadf4) 範囲 `[['00acadf4', '00acadff']]`
  - `FALL_THROUGH` [`00acadfc`](#insn-00acadfc) → [`00acae00`](#insn-00acae00)
- ブロック [`00acae00`](#insn-00acae00) 範囲 `[['00acae00', '00acae0b']]`
  - `CONDITIONAL_JUMP` [`00acae08`](#insn-00acae08) → [`00acae50`](#insn-00acae50)
  - `FALL_THROUGH` [`00acae08`](#insn-00acae08) → [`00acae0c`](#insn-00acae0c)
- ブロック [`00acae0c`](#insn-00acae0c) 範囲 `[['00acae0c', '00acae17']]`
  - `CONDITIONAL_JUMP` [`00acae14`](#insn-00acae14) → [`00acae00`](#insn-00acae00)
  - `FALL_THROUGH` [`00acae14`](#insn-00acae14) → [`00acae18`](#insn-00acae18)
- ブロック [`00acae18`](#insn-00acae18) 範囲 `[['00acae18', '00acae27']]`
  - `CONDITIONAL_JUMP` [`00acae24`](#insn-00acae24) → [`00acadf4`](#insn-00acadf4)
  - `FALL_THROUGH` [`00acae24`](#insn-00acae24) → [`00acae28`](#insn-00acae28)
- ブロック [`00acae28`](#insn-00acae28) 範囲 `[['00acae28', '00acae2f']]`
  - `UNCONDITIONAL_JUMP` [`00acae2c`](#insn-00acae2c) → [`00acae3c`](#insn-00acae3c)
- ブロック [`00acae30`](#insn-00acae30) 範囲 `[['00acae30', '00acae3b']]`
  - `CONDITIONAL_JUMP` [`00acae38`](#insn-00acae38) → [`00acadf0`](#insn-00acadf0)
  - `FALL_THROUGH` [`00acae38`](#insn-00acae38) → [`00acae3c`](#insn-00acae3c)
- ブロック [`00acae3c`](#insn-00acae3c) 範囲 `[['00acae3c', '00acae43']]`
  - `CONDITIONAL_JUMP` [`00acae40`](#insn-00acae40) → [`00acae30`](#insn-00acae30)
  - `FALL_THROUGH` [`00acae40`](#insn-00acae40) → [`00acae44`](#insn-00acae44)
- ブロック [`00acae44`](#insn-00acae44) 範囲 `[['00acae44', '00acae4f']]`
  - `UNCONDITIONAL_JUMP` [`00acae4c`](#insn-00acae4c) → [`00acae30`](#insn-00acae30)
- ブロック [`00acae50`](#insn-00acae50) 範囲 `[['00acae50', '00acae57']]`
  - `CONDITIONAL_JUMP` [`00acae54`](#insn-00acae54) → [`00acae5c`](#insn-00acae5c)
  - `FALL_THROUGH` [`00acae54`](#insn-00acae54) → [`00acae58`](#insn-00acae58)
- ブロック [`00acae58`](#insn-00acae58) 範囲 `[['00acae58', '00acae5b']]`
  - `FALL_THROUGH` [`00acae58`](#insn-00acae58) → [`00acae5c`](#insn-00acae5c)
- ブロック [`00acae5c`](#insn-00acae5c) 範囲 `[['00acae5c', '00acae6b']]`
  - `CONDITIONAL_JUMP` [`00acae68`](#insn-00acae68) → [`00acaedc`](#insn-00acaedc)
  - `FALL_THROUGH` [`00acae68`](#insn-00acae68) → [`00acae6c`](#insn-00acae6c)
- ブロック [`00acae6c`](#insn-00acae6c) 範囲 `[['00acae6c', '00acae8b']]`
- ブロック [`00acae8c`](#insn-00acae8c) 範囲 `[['00acae8c', '00acae9b']]`
  - `CONDITIONAL_JUMP` [`00acae98`](#insn-00acae98) → [`00acaedc`](#insn-00acaedc)
  - `FALL_THROUGH` [`00acae98`](#insn-00acae98) → [`00acae9c`](#insn-00acae9c)
- ブロック [`00acae9c`](#insn-00acae9c) 範囲 `[['00acae9c', '00acaea3']]`
  - `FALL_THROUGH` [`00acaea0`](#insn-00acaea0) → [`00acaea4`](#insn-00acaea4)
- ブロック [`00acaea4`](#insn-00acaea4) 範囲 `[['00acaea4', '00acaeb3']]`
  - `CONDITIONAL_JUMP` [`00acaeb0`](#insn-00acaeb0) → [`00acaedc`](#insn-00acaedc)
  - `FALL_THROUGH` [`00acaeb0`](#insn-00acaeb0) → [`00acaeb4`](#insn-00acaeb4)
- ブロック [`00acaeb4`](#insn-00acaeb4) 範囲 `[['00acaeb4', '00acaeb7']]`
- ブロック [`00acaedc`](#insn-00acaedc) 範囲 `[['00acaedc', '00acaedf']]`

## 命令位置別の参照

- [`00acacd4`](#insn-00acacd4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acacd8`](#insn-00acacd8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acacdc`](#insn-00acacdc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acace0`](#insn-00acace0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acace4`](#insn-00acace4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acad00`](#insn-00acad00) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acad24`](#insn-00acad24) → [`00acae8c`](#insn-00acae8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acad34`](#insn-00acad34) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acad60`](#insn-00acad60) → [`00acad7c`](#insn-00acad7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acad68`](#insn-00acad68) → [`00acaea4`](#insn-00acaea4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acad74`](#insn-00acad74) → [`00bdaff0`](../00bda/00bdaff0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaff0` · 推定シンボル `None` · 推定型 `None`
- [`00acad78`](#insn-00acad78) → [`00acad80`](#insn-00acad80) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acada4`](#insn-00acada4) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acadb0`](#insn-00acadb0) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acadbc`](#insn-00acadbc) → [`0051d884`](../0051d/0051d884.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0051d884` · 推定シンボル `None` · 推定型 `None`
- [`00acadc0`](#insn-00acadc0) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acadc8`](#insn-00acadc8) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acadd4`](#insn-00acadd4) → [`007d95c0`](../007d9/007d95c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `007d95c0` · 推定シンボル `None` · 推定型 `None`
- [`00acadd8`](#insn-00acadd8) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acade4`](#insn-00acade4) → [`00acae50`](#insn-00acae50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acadec`](#insn-00acadec) → [`00acae0c`](#insn-00acae0c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acadf8`](#insn-00acadf8) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00acadfc`](#insn-00acadfc) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acae08`](#insn-00acae08) → [`00acae50`](#insn-00acae50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acae10`](#insn-00acae10) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acae14`](#insn-00acae14) → [`00acae00`](#insn-00acae00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acae24`](#insn-00acae24) → [`00acadf4`](#insn-00acadf4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acae2c`](#insn-00acae2c) → [`00acae3c`](#insn-00acae3c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acae38`](#insn-00acae38) → [`00acadf0`](#insn-00acadf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acae40`](#insn-00acae40) → [`00acae30`](#insn-00acae30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acae48`](#insn-00acae48) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00acae4c`](#insn-00acae4c) → [`00acae30`](#insn-00acae30) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acae50`](#insn-00acae50) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acae54`](#insn-00acae54) → [`00acae5c`](#insn-00acae5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acae58`](#insn-00acae58) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00acae60`](#insn-00acae60) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acae68`](#insn-00acae68) → [`00acaedc`](#insn-00acaedc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acae70`](#insn-00acae70) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acae74`](#insn-00acae74) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acae78`](#insn-00acae78) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acae7c`](#insn-00acae7c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acae80`](#insn-00acae80) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acae90`](#insn-00acae90) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acae98`](#insn-00acae98) → [`00acaedc`](#insn-00acaedc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acaea0`](#insn-00acaea0) → [`0076a658`](../0076a/0076a658.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0076a658` · 推定シンボル `None` · 推定型 `None`
- [`00acaea8`](#insn-00acaea8) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acaeb0`](#insn-00acaeb0) → [`00acaedc`](#insn-00acaedc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acaeb4`](#insn-00acaeb4) → [`0041e380`](../0041e/0041e380.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0041e380` · 推定シンボル `None` · 推定型 `None`
- [`00acaedc`](#insn-00acaedc) → [`00bdb040`](../00bdb/00bdb040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb040` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00acacd4`](#insn-00acacd4)

~~~json
{
  "source": "00acacd4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acacd8`](#insn-00acacd8)

~~~json
{
  "source": "00acacd8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acacdc`](#insn-00acacdc)

~~~json
{
  "source": "00acacdc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acace0`](#insn-00acace0)

~~~json
{
  "source": "00acace0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acace4`](#insn-00acace4)

~~~json
{
  "source": "00acace4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acad00`](#insn-00acad00)

~~~json
{
  "source": "00acad00",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acad24`](#insn-00acad24)

~~~json
{
  "source": "00acad24",
  "target": "00acae8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acad34`](#insn-00acad34)

~~~json
{
  "source": "00acad34",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acad60`](#insn-00acad60)

~~~json
{
  "source": "00acad60",
  "target": "00acad7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acad68`](#insn-00acad68)

~~~json
{
  "source": "00acad68",
  "target": "00acaea4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acad74`](#insn-00acad74)

~~~json
{
  "source": "00acad74",
  "target": "00bdaff0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acad78`](#insn-00acad78)

~~~json
{
  "source": "00acad78",
  "target": "00acad80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acada4`](#insn-00acada4)

~~~json
{
  "source": "00acada4",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acadb0`](#insn-00acadb0)

~~~json
{
  "source": "00acadb0",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acadbc`](#insn-00acadbc)

~~~json
{
  "source": "00acadbc",
  "target": "0051d884",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acadc0`](#insn-00acadc0)

~~~json
{
  "source": "00acadc0",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acadc8`](#insn-00acadc8)

~~~json
{
  "source": "00acadc8",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acadd4`](#insn-00acadd4)

~~~json
{
  "source": "00acadd4",
  "target": "007d95c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acadd8`](#insn-00acadd8)

~~~json
{
  "source": "00acadd8",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acade4`](#insn-00acade4)

~~~json
{
  "source": "00acade4",
  "target": "00acae50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acadec`](#insn-00acadec)

~~~json
{
  "source": "00acadec",
  "target": "00acae0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acadf8`](#insn-00acadf8)

~~~json
{
  "source": "00acadf8",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acadfc`](#insn-00acadfc)

~~~json
{
  "source": "00acadfc",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acae08`](#insn-00acae08)

~~~json
{
  "source": "00acae08",
  "target": "00acae50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acae10`](#insn-00acae10)

~~~json
{
  "source": "00acae10",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acae14`](#insn-00acae14)

~~~json
{
  "source": "00acae14",
  "target": "00acae00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acae24`](#insn-00acae24)

~~~json
{
  "source": "00acae24",
  "target": "00acadf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acae2c`](#insn-00acae2c)

~~~json
{
  "source": "00acae2c",
  "target": "00acae3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acae38`](#insn-00acae38)

~~~json
{
  "source": "00acae38",
  "target": "00acadf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acae40`](#insn-00acae40)

~~~json
{
  "source": "00acae40",
  "target": "00acae30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acae48`](#insn-00acae48)

~~~json
{
  "source": "00acae48",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acae4c`](#insn-00acae4c)

~~~json
{
  "source": "00acae4c",
  "target": "00acae30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acae50`](#insn-00acae50)

~~~json
{
  "source": "00acae50",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acae54`](#insn-00acae54)

~~~json
{
  "source": "00acae54",
  "target": "00acae5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acae58`](#insn-00acae58)

~~~json
{
  "source": "00acae58",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acae60`](#insn-00acae60)

~~~json
{
  "source": "00acae60",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acae68`](#insn-00acae68)

~~~json
{
  "source": "00acae68",
  "target": "00acaedc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acae70`](#insn-00acae70)

~~~json
{
  "source": "00acae70",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acae74`](#insn-00acae74)

~~~json
{
  "source": "00acae74",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acae78`](#insn-00acae78)

~~~json
{
  "source": "00acae78",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acae7c`](#insn-00acae7c)

~~~json
{
  "source": "00acae7c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acae80`](#insn-00acae80)

~~~json
{
  "source": "00acae80",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acae90`](#insn-00acae90)

~~~json
{
  "source": "00acae90",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acae98`](#insn-00acae98)

~~~json
{
  "source": "00acae98",
  "target": "00acaedc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acaea0`](#insn-00acaea0)

~~~json
{
  "source": "00acaea0",
  "target": "0076a658",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acaea8`](#insn-00acaea8)

~~~json
{
  "source": "00acaea8",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acaeb0`](#insn-00acaeb0)

~~~json
{
  "source": "00acaeb0",
  "target": "00acaedc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acaeb4`](#insn-00acaeb4)

~~~json
{
  "source": "00acaeb4",
  "target": "0041e380",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acaedc`](#insn-00acaedc)

~~~json
{
  "source": "00acaedc",
  "target": "00bdb040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
