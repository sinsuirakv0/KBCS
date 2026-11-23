# 00afddb4

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00afdcec`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afd/00afdcec.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/alignment_unresolved-0002.md#compare-35d66230e38eee5023913762801e9692)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00afddf8`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afd/00afddf8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0008.md#compare-481345d1ee4aeec1907f4c3b8703ffed)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afddb4",
  "name": "_ZN8firebase4Path11GetRelativeERKS0_S2_",
  "size": 612,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ad4d556eaadc703b0f7834c87028cc47306fc90a71618d833cbb184ca8b8dbe4",
  "source_text_sha256": "ad4d556eaadc703b0f7834c87028cc47306fc90a71618d833cbb184ca8b8dbe4",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afddb4",
        "00afe017"
      ]
    ],
    "bytes_sha256": "e44d62d8430cf8cfcf278f4abdf55a34ea07b91ece0000d0e186d8fd200a57f5",
    "instruction_count": 153,
    "instruction_bytes": 612,
    "body_bytes": 612,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bdecd0](../00bde/00bdecd0.md)

## 呼び出し先

- [00afd268](../00afd/00afd268.md)
- [00bdb010](../00bdb/00bdb010.md)
- [00bdb040](../00bdb/00bdb040.md)
- [00bdb1b0](../00bdb/00bdb1b0.md)
- [00bde1e0](../00bde/00bde1e0.md)
- [00bdecf0](../00bde/00bdecf0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 4076 bytes

~~~c

void _ZN8firebase4Path11GetRelativeERKS0_S2_
               (undefined8 *param_1,undefined8 param_2,undefined8 param_3)

{
  byte *pbVar1;
  byte *pbVar2;
  size_t __n;
  size_t sVar3;
  byte bVar4;
  byte bVar5;
  long lVar6;
  void *pvVar7;
  byte *pbVar8;
  undefined8 uVar9;
  undefined8 uVar10;
  byte *pbVar11;
  byte *pbVar12;
  int iVar13;
  ulong uVar14;
  byte *__s1;
  byte *__s2;
  byte local_b8 [8];
  ulong local_b0;
  void *local_a8;
  undefined8 local_a0;
  undefined8 uStack_98;
  undefined8 local_90;
  byte *local_88;
  byte *local_80;
  byte *local_70;
  byte *local_68;
  long local_58;
  
  lVar6 = tpidr_el0;
  local_58 = *(long *)(lVar6 + 0x28);
  _ZNK8firebase4Path14GetDirectoriesEv(&local_70);
  _ZNK8firebase4Path14GetDirectoriesEv(&local_88,param_3);
  pbVar12 = local_68;
  pbVar11 = local_80;
  pbVar8 = local_88;
  pbVar2 = local_88;
  pbVar1 = local_70;
  do {
    if (pbVar1 == pbVar12) {
      FUN_00afd268(local_b8,pbVar2,pbVar11);
      uVar14 = (ulong)(local_b8[0] >> 1);
      pvVar7 = (void *)((ulong)local_b8 | 1);
      if ((local_b8[0] & 1) != 0) {
        uVar14 = local_b0;
        pvVar7 = local_a8;
      }
      uStack_98 = 0;
      local_90 = 0;
      local_a0 = 0;
      _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
                (&local_a0,pvVar7,uVar14);
      uVar10 = uStack_98;
      uVar9 = local_a0;
      local_a0 = 0;
      uStack_98 = 0;
      *(undefined1 *)(param_1 + 3) = 1;
      param_1[2] = local_90;
      param_1[1] = uVar10;
      *param_1 = uVar9;
      local_90 = 0;
      pbVar8 = local_88;
      pbVar1 = local_88;
      if ((local_b8[0] & 1) != 0) {
        _ZdlPv(local_a8);
        pbVar8 = local_88;
        pbVar1 = local_88;
      }
joined_r0x00afdf3c:
      if (pbVar8 != (byte *)0x0) {
        local_88 = pbVar8;
        if (local_80 != pbVar8) {
          bVar4 = local_80[-0x18];
          pbVar2 = local_80 + -0x18;
          local_88 = pbVar1;
          while( true ) {
            pbVar1 = pbVar2;
            if ((bVar4 & 1) != 0) {
              _ZdlPv(*(void **)(local_80 + -8));
            }
            if (pbVar8 == pbVar1) break;
            bVar4 = pbVar1[-0x18];
            pbVar2 = pbVar1 + -0x18;
            local_80 = pbVar1;
          }
        }
        _ZdlPv(local_88);
      }
      pbVar1 = local_70;
      if (local_70 != (byte *)0x0) {
        if (local_68 != local_70) {
          bVar4 = local_68[-0x18];
          pbVar2 = local_68 + -0x18;
          while( true ) {
            pbVar8 = pbVar2;
            if ((bVar4 & 1) != 0) {
              _ZdlPv(*(void **)(local_68 + -8));
            }
            if (pbVar1 == pbVar8) break;
            bVar4 = pbVar8[-0x18];
            pbVar2 = pbVar8 + -0x18;
            local_68 = pbVar8;
          }
        }
        local_68 = pbVar1;
        _ZdlPv(local_70);
      }
      if (*(long *)(lVar6 + 0x28) == local_58) {
        return;
      }
                    /* WARNING: Subroutine does not return */
      __stack_chk_fail();
    }
    if (pbVar11 == pbVar2) {
LAB_00afdeb8:
      *(undefined1 *)(param_1 + 3) = 0;
      pbVar1 = local_88;
      goto joined_r0x00afdf3c;
    }
    bVar4 = *pbVar1;
    bVar5 = *pbVar2;
    __n = (ulong)(bVar4 >> 1);
    if ((bVar4 & 1) != 0) {
      __n = *(size_t *)(pbVar1 + 8);
    }
    sVar3 = (ulong)(bVar5 >> 1);
    if ((bVar5 & 1) != 0) {
      sVar3 = *(size_t *)(pbVar2 + 8);
    }
    if (__n != sVar3) goto LAB_00afdeb8;
    __s1 = *(byte **)(pbVar1 + 0x10);
    __s2 = *(byte **)(pbVar2 + 0x10);
    if ((bVar4 & 1) == 0) {
      __s1 = pbVar1 + 1;
    }
    if ((bVar5 & 1) == 0) {
      __s2 = pbVar2 + 1;
    }
    if ((bVar4 & 1) == 0) {
      if (__n != 0) {
        uVar14 = 0;
        do {
          if (pbVar1[uVar14 + 1] != __s2[uVar14]) goto LAB_00afdeb8;
          uVar14 = uVar14 + 1;
        } while (bVar4 >> 1 != uVar14);
      }
    }
    else if ((__n != 0) && (iVar13 = memcmp(__s1,__s2,__n), iVar13 != 0)) goto LAB_00afdeb8;
    pbVar1 = pbVar1 + 0x18;
    pbVar2 = pbVar2 + 0x18;
  } while( true );
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afddb4"></a> `00afddb4` | `ff 03 03 d1` | sub sp,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00afddb8"></a> `00afddb8` | `f9 3b 00 f9` | str x25,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00afddbc"></a> `00afddbc` | `f8 5f 08 a9` | stp x24,x23,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00afddc0"></a> `00afddc0` | `f6 57 09 a9` | stp x22,x21,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00afddc4"></a> `00afddc4` | `f4 4f 0a a9` | stp x20,x19,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00afddc8"></a> `00afddc8` | `fd 7b 0b a9` | stp x29,x30,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00afddcc"></a> `00afddcc` | `fd c3 02 91` | add x29,sp,#0xb0 | `FALL_THROUGH`
<a id="insn-00afddd0"></a> `00afddd0` | `56 d0 3b d5` | mrs x22,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00afddd4"></a> `00afddd4` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00afddd8"></a> `00afddd8` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00afdddc"></a> `00afdddc` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00afdde0"></a> `00afdde0` | `a8 83 1b f8` | stur x8,[x29, #-0x48] | `FALL_THROUGH`
<a id="insn-00afdde4"></a> `00afdde4` | `e8 43 01 91` | add x8,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00afdde8"></a> `00afdde8` | `c2 83 03 94` | bl 0x00bdecf0 | `UNCONDITIONAL_CALL`
<a id="insn-00afddec"></a> `00afddec` | `e8 e3 00 91` | add x8,sp,#0x38 | `FALL_THROUGH`
<a id="insn-00afddf0"></a> `00afddf0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00afddf4"></a> `00afddf4` | `bf 83 03 94` | bl 0x00bdecf0 | `UNCONDITIONAL_CALL`
<a id="insn-00afddf8"></a> `00afddf8` | `f8 5f 45 a9` | ldp x24,x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00afddfc"></a> `00afddfc` | `f4 1f 40 f9` | ldr x20,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00afde00"></a> `00afde00` | `1f 03 17 eb` | cmp x24,x23 | `FALL_THROUGH`
<a id="insn-00afde04"></a> `00afde04` | `00 06 00 54` | b.eq 0x00afdec4 | `CONDITIONAL_JUMP`
<a id="insn-00afde08"></a> `00afde08` | `f5 23 40 f9` | ldr x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00afde0c"></a> `00afde0c` | `f9 03 14 aa` | mov x25,x20 | `FALL_THROUGH`
<a id="insn-00afde10"></a> `00afde10` | `bf 02 19 eb` | cmp x21,x25 | `FALL_THROUGH`
<a id="insn-00afde14"></a> `00afde14` | `01 01 00 54` | b.ne 0x00afde34 | `CONDITIONAL_JUMP`
<a id="insn-00afde18"></a> `00afde18` | `28 00 00 14` | b 0x00afdeb8 | `UNCONDITIONAL_JUMP`
<a id="insn-00afde1c"></a> `00afde1c` | `18 63 00 91` | add x24,x24,#0x18 | `FALL_THROUGH`
<a id="insn-00afde20"></a> `00afde20` | `1f 03 17 eb` | cmp x24,x23 | `FALL_THROUGH`
<a id="insn-00afde24"></a> `00afde24` | `39 63 00 91` | add x25,x25,#0x18 | `FALL_THROUGH`
<a id="insn-00afde28"></a> `00afde28` | `20 0f 00 54` | b.eq 0x00afe00c | `CONDITIONAL_JUMP`
<a id="insn-00afde2c"></a> `00afde2c` | `bf 02 19 eb` | cmp x21,x25 | `FALL_THROUGH`
<a id="insn-00afde30"></a> `00afde30` | `40 04 00 54` | b.eq 0x00afdeb8 | `CONDITIONAL_JUMP`
<a id="insn-00afde34"></a> `00afde34` | `09 03 40 39` | ldrb w9,[x24] | `FALL_THROUGH`
<a id="insn-00afde38"></a> `00afde38` | `0b 07 40 f9` | ldr x11,[x24, #0x8] | `FALL_THROUGH`
<a id="insn-00afde3c"></a> `00afde3c` | `2a 03 40 39` | ldrb w10,[x25] | `FALL_THROUGH`
<a id="insn-00afde40"></a> `00afde40` | `2c 07 40 f9` | ldr x12,[x25, #0x8] | `FALL_THROUGH`
<a id="insn-00afde44"></a> `00afde44` | `28 fd 41 d3` | lsr x8,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00afde48"></a> `00afde48` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00afde4c"></a> `00afde4c` | `4d fd 41 d3` | lsr x13,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00afde50"></a> `00afde50` | `02 01 8b 9a` | csel x2,x8,x11,eq | `FALL_THROUGH`
<a id="insn-00afde54"></a> `00afde54` | `5f 01 00 72` | tst w10,#0x1 | `FALL_THROUGH`
<a id="insn-00afde58"></a> `00afde58` | `ab 01 8c 9a` | csel x11,x13,x12,eq | `FALL_THROUGH`
<a id="insn-00afde5c"></a> `00afde5c` | `5f 00 0b eb` | cmp x2,x11 | `FALL_THROUGH`
<a id="insn-00afde60"></a> `00afde60` | `c1 02 00 54` | b.ne 0x00afdeb8 | `CONDITIONAL_JUMP`
<a id="insn-00afde64"></a> `00afde64` | `0b 0b 40 f9` | ldr x11,[x24, #0x10] | `FALL_THROUGH`
<a id="insn-00afde68"></a> `00afde68` | `2c 0b 40 f9` | ldr x12,[x25, #0x10] | `FALL_THROUGH`
<a id="insn-00afde6c"></a> `00afde6c` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00afde70"></a> `00afde70` | `60 15 98 9a` | csinc x0,x11,x24,ne | `FALL_THROUGH`
<a id="insn-00afde74"></a> `00afde74` | `5f 01 00 72` | tst w10,#0x1 | `FALL_THROUGH`
<a id="insn-00afde78"></a> `00afde78` | `81 15 99 9a` | csinc x1,x12,x25,ne | `FALL_THROUGH`
<a id="insn-00afde7c"></a> `00afde7c` | `89 01 00 37` | tbnz w9,#0x0,0x00afdeac | `CONDITIONAL_JUMP`
<a id="insn-00afde80"></a> `00afde80` | `e2 fc ff b4` | cbz x2,0x00afde1c | `CONDITIONAL_JUMP`
<a id="insn-00afde84"></a> `00afde84` | `e9 03 1f aa` | mov x9,xzr | `FALL_THROUGH`
<a id="insn-00afde88"></a> `00afde88` | `0a 03 09 8b` | add x10,x24,x9 | `FALL_THROUGH`
<a id="insn-00afde8c"></a> `00afde8c` | `4a 05 40 39` | ldrb w10,[x10, #0x1] | `FALL_THROUGH`
<a id="insn-00afde90"></a> `00afde90` | `2b 68 69 38` | ldrb w11,[x1, x9, LSL ] | `FALL_THROUGH`
<a id="insn-00afde94"></a> `00afde94` | `5f 01 0b 6b` | cmp w10,w11 | `FALL_THROUGH`
<a id="insn-00afde98"></a> `00afde98` | `01 01 00 54` | b.ne 0x00afdeb8 | `CONDITIONAL_JUMP`
<a id="insn-00afde9c"></a> `00afde9c` | `29 05 00 91` | add x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00afdea0"></a> `00afdea0` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00afdea4"></a> `00afdea4` | `21 ff ff 54` | b.ne 0x00afde88 | `CONDITIONAL_JUMP`
<a id="insn-00afdea8"></a> `00afdea8` | `dd ff ff 17` | b 0x00afde1c | `UNCONDITIONAL_JUMP`
<a id="insn-00afdeac"></a> `00afdeac` | `82 fb ff b4` | cbz x2,0x00afde1c | `CONDITIONAL_JUMP`
<a id="insn-00afdeb0"></a> `00afdeb0` | `c0 74 03 94` | bl 0x00bdb1b0 | `UNCONDITIONAL_CALL`
<a id="insn-00afdeb4"></a> `00afdeb4` | `40 fb ff 34` | cbz w0,0x00afde1c | `CONDITIONAL_JUMP`
<a id="insn-00afdeb8"></a> `00afdeb8` | `7f 62 00 39` | strb wzr,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00afdebc"></a> `00afdebc` | `34 04 00 b5` | cbnz x20,0x00afdf40 | `CONDITIONAL_JUMP`
<a id="insn-00afdec0"></a> `00afdec0` | `33 00 00 14` | b 0x00afdf8c | `UNCONDITIONAL_JUMP`
<a id="insn-00afdec4"></a> `00afdec4` | `f5 23 40 f9` | ldr x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00afdec8"></a> `00afdec8` | `e8 23 00 91` | add x8,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00afdecc"></a> `00afdecc` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00afded0"></a> `00afded0` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00afded4"></a> `00afded4` | `f7 23 00 91` | add x23,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00afded8"></a> `00afded8` | `e4 fc ff 97` | bl 0x00afd268 | `UNCONDITIONAL_CALL`
<a id="insn-00afdedc"></a> `00afdedc` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00afdee0"></a> `00afdee0` | `ea 27 41 a9` | ldp x10,x9,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afdee4"></a> `00afdee4` | `eb 02 40 b2` | orr x11,x23,#0x1 | `FALL_THROUGH`
<a id="insn-00afdee8"></a> `00afdee8` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00afdeec"></a> `00afdeec` | `0c fd 41 d3` | lsr x12,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00afdef0"></a> `00afdef0` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00afdef4"></a> `00afdef4` | `61 01 89 9a` | csel x1,x11,x9,eq | `FALL_THROUGH`
<a id="insn-00afdef8"></a> `00afdef8` | `82 01 8a 9a` | csel x2,x12,x10,eq | `FALL_THROUGH`
<a id="insn-00afdefc"></a> `00afdefc` | `ff ff 02 a9` | stp xzr,xzr,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00afdf00"></a> `00afdf00` | `ff 13 00 f9` | str xzr,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afdf04"></a> `00afdf04` | `b7 80 03 94` | bl 0x00bde1e0 | `UNCONDITIONAL_CALL`
<a id="insn-00afdf08"></a> `00afdf08` | `e0 0b c0 3d` | ldr q0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afdf0c"></a> `00afdf0c` | `e9 1b 40 f9` | ldr x9,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00afdf10"></a> `00afdf10` | `ea 23 40 39` | ldrb w10,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00afdf14"></a> `00afdf14` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00afdf18"></a> `00afdf18` | `ff 7f 02 a9` | stp xzr,xzr,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afdf1c"></a> `00afdf1c` | `68 62 00 39` | strb w8,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00afdf20"></a> `00afdf20` | `69 0a 00 f9` | str x9,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00afdf24"></a> `00afdf24` | `60 02 80 3d` | str q0,[x19] | `FALL_THROUGH`
<a id="insn-00afdf28"></a> `00afdf28` | `ff 1b 00 f9` | str xzr,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00afdf2c"></a> `00afdf2c` | `6a 00 00 36` | tbz w10,#0x0,0x00afdf38 | `CONDITIONAL_JUMP`
<a id="insn-00afdf30"></a> `00afdf30` | `e0 0f 40 f9` | ldr x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00afdf34"></a> `00afdf34` | `37 74 03 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00afdf38"></a> `00afdf38` | `f4 1f 40 f9` | ldr x20,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00afdf3c"></a> `00afdf3c` | `94 02 00 b4` | cbz x20,0x00afdf8c | `CONDITIONAL_JUMP`
<a id="insn-00afdf40"></a> `00afdf40` | `e8 23 40 f9` | ldr x8,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00afdf44"></a> `00afdf44` | `1f 01 14 eb` | cmp x8,x20 | `FALL_THROUGH`
<a id="insn-00afdf48"></a> `00afdf48` | `c0 01 00 54` | b.eq 0x00afdf80 | `CONDITIONAL_JUMP`
<a id="insn-00afdf4c"></a> `00afdf4c` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00afdf50"></a> `00afdf50` | `69 8e 5e 38` | ldrb w9,[x19, #-0x18]! | `FALL_THROUGH`
<a id="insn-00afdf54"></a> `00afdf54` | `c9 00 00 37` | tbnz w9,#0x0,0x00afdf6c | `CONDITIONAL_JUMP`
<a id="insn-00afdf58"></a> `00afdf58` | `9f 02 13 eb` | cmp x20,x19 | `FALL_THROUGH`
<a id="insn-00afdf5c"></a> `00afdf5c` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-00afdf60"></a> `00afdf60` | `c0 00 00 54` | b.eq 0x00afdf78 | `CONDITIONAL_JUMP`
<a id="insn-00afdf64"></a> `00afdf64` | `69 8e 5e 38` | ldrb w9,[x19, #-0x18]! | `FALL_THROUGH`
<a id="insn-00afdf68"></a> `00afdf68` | `89 ff 07 36` | tbz w9,#0x0,0x00afdf58 | `CONDITIONAL_JUMP`
<a id="insn-00afdf6c"></a> `00afdf6c` | `00 81 5f f8` | ldur x0,[x8, #-0x8] | `FALL_THROUGH`
<a id="insn-00afdf70"></a> `00afdf70` | `28 74 03 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00afdf74"></a> `00afdf74` | `f9 ff ff 17` | b 0x00afdf58 | `UNCONDITIONAL_JUMP`
<a id="insn-00afdf78"></a> `00afdf78` | `e0 1f 40 f9` | ldr x0,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00afdf7c"></a> `00afdf7c` | `02 00 00 14` | b 0x00afdf84 | `UNCONDITIONAL_JUMP`
<a id="insn-00afdf80"></a> `00afdf80` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00afdf84"></a> `00afdf84` | `f4 23 00 f9` | str x20,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00afdf88"></a> `00afdf88` | `22 74 03 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00afdf8c"></a> `00afdf8c` | `f3 2b 40 f9` | ldr x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00afdf90"></a> `00afdf90` | `93 02 00 b4` | cbz x19,0x00afdfe0 | `CONDITIONAL_JUMP`
<a id="insn-00afdf94"></a> `00afdf94` | `e8 2f 40 f9` | ldr x8,[sp, #0x58] | `FALL_THROUGH`
<a id="insn-00afdf98"></a> `00afdf98` | `1f 01 13 eb` | cmp x8,x19 | `FALL_THROUGH`
<a id="insn-00afdf9c"></a> `00afdf9c` | `c0 01 00 54` | b.eq 0x00afdfd4 | `CONDITIONAL_JUMP`
<a id="insn-00afdfa0"></a> `00afdfa0` | `f4 03 08 aa` | mov x20,x8 | `FALL_THROUGH`
<a id="insn-00afdfa4"></a> `00afdfa4` | `89 8e 5e 38` | ldrb w9,[x20, #-0x18]! | `FALL_THROUGH`
<a id="insn-00afdfa8"></a> `00afdfa8` | `c9 00 00 37` | tbnz w9,#0x0,0x00afdfc0 | `CONDITIONAL_JUMP`
<a id="insn-00afdfac"></a> `00afdfac` | `7f 02 14 eb` | cmp x19,x20 | `FALL_THROUGH`
<a id="insn-00afdfb0"></a> `00afdfb0` | `e8 03 14 aa` | mov x8,x20 | `FALL_THROUGH`
<a id="insn-00afdfb4"></a> `00afdfb4` | `c0 00 00 54` | b.eq 0x00afdfcc | `CONDITIONAL_JUMP`
<a id="insn-00afdfb8"></a> `00afdfb8` | `89 8e 5e 38` | ldrb w9,[x20, #-0x18]! | `FALL_THROUGH`
<a id="insn-00afdfbc"></a> `00afdfbc` | `89 ff 07 36` | tbz w9,#0x0,0x00afdfac | `CONDITIONAL_JUMP`
<a id="insn-00afdfc0"></a> `00afdfc0` | `00 81 5f f8` | ldur x0,[x8, #-0x8] | `FALL_THROUGH`
<a id="insn-00afdfc4"></a> `00afdfc4` | `13 74 03 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00afdfc8"></a> `00afdfc8` | `f9 ff ff 17` | b 0x00afdfac | `UNCONDITIONAL_JUMP`
<a id="insn-00afdfcc"></a> `00afdfcc` | `e0 2b 40 f9` | ldr x0,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00afdfd0"></a> `00afdfd0` | `02 00 00 14` | b 0x00afdfd8 | `UNCONDITIONAL_JUMP`
<a id="insn-00afdfd4"></a> `00afdfd4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00afdfd8"></a> `00afdfd8` | `f3 2f 00 f9` | str x19,[sp, #0x58] | `FALL_THROUGH`
<a id="insn-00afdfdc"></a> `00afdfdc` | `0d 74 03 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00afdfe0"></a> `00afdfe0` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00afdfe4"></a> `00afdfe4` | `a9 83 5b f8` | ldur x9,[x29, #-0x48] | `FALL_THROUGH`
<a id="insn-00afdfe8"></a> `00afdfe8` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00afdfec"></a> `00afdfec` | `41 01 00 54` | b.ne 0x00afe014 | `CONDITIONAL_JUMP`
<a id="insn-00afdff0"></a> `00afdff0` | `fd 7b 4b a9` | ldp x29,x30,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00afdff4"></a> `00afdff4` | `f4 4f 4a a9` | ldp x20,x19,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00afdff8"></a> `00afdff8` | `f6 57 49 a9` | ldp x22,x21,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00afdffc"></a> `00afdffc` | `f8 5f 48 a9` | ldp x24,x23,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00afe000"></a> `00afe000` | `f9 3b 40 f9` | ldr x25,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00afe004"></a> `00afe004` | `ff 03 03 91` | add sp,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00afe008"></a> `00afe008` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00afe00c"></a> `00afe00c` | `f4 03 19 aa` | mov x20,x25 | `FALL_THROUGH`
<a id="insn-00afe010"></a> `00afe010` | `ae ff ff 17` | b 0x00afdec8 | `UNCONDITIONAL_JUMP`
<a id="insn-00afe014"></a> `00afe014` | `0b 74 03 94` | bl 0x00bdb040 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afddb4`](#insn-00afddb4) 範囲 `[['00afddb4', '00afde07']]`
  - `CONDITIONAL_JUMP` [`00afde04`](#insn-00afde04) → [`00afdec4`](#insn-00afdec4)
  - `FALL_THROUGH` [`00afde04`](#insn-00afde04) → [`00afde08`](#insn-00afde08)
- ブロック [`00afde08`](#insn-00afde08) 範囲 `[['00afde08', '00afde17']]`
  - `CONDITIONAL_JUMP` [`00afde14`](#insn-00afde14) → [`00afde34`](#insn-00afde34)
  - `FALL_THROUGH` [`00afde14`](#insn-00afde14) → [`00afde18`](#insn-00afde18)
- ブロック [`00afde18`](#insn-00afde18) 範囲 `[['00afde18', '00afde1b']]`
  - `UNCONDITIONAL_JUMP` [`00afde18`](#insn-00afde18) → [`00afdeb8`](#insn-00afdeb8)
- ブロック [`00afde1c`](#insn-00afde1c) 範囲 `[['00afde1c', '00afde2b']]`
  - `CONDITIONAL_JUMP` [`00afde28`](#insn-00afde28) → [`00afe00c`](#insn-00afe00c)
  - `FALL_THROUGH` [`00afde28`](#insn-00afde28) → [`00afde2c`](#insn-00afde2c)
- ブロック [`00afde2c`](#insn-00afde2c) 範囲 `[['00afde2c', '00afde33']]`
  - `CONDITIONAL_JUMP` [`00afde30`](#insn-00afde30) → [`00afdeb8`](#insn-00afdeb8)
  - `FALL_THROUGH` [`00afde30`](#insn-00afde30) → [`00afde34`](#insn-00afde34)
- ブロック [`00afde34`](#insn-00afde34) 範囲 `[['00afde34', '00afde63']]`
  - `CONDITIONAL_JUMP` [`00afde60`](#insn-00afde60) → [`00afdeb8`](#insn-00afdeb8)
  - `FALL_THROUGH` [`00afde60`](#insn-00afde60) → [`00afde64`](#insn-00afde64)
- ブロック [`00afde64`](#insn-00afde64) 範囲 `[['00afde64', '00afde7f']]`
  - `CONDITIONAL_JUMP` [`00afde7c`](#insn-00afde7c) → [`00afdeac`](#insn-00afdeac)
  - `FALL_THROUGH` [`00afde7c`](#insn-00afde7c) → [`00afde80`](#insn-00afde80)
- ブロック [`00afde80`](#insn-00afde80) 範囲 `[['00afde80', '00afde83']]`
  - `CONDITIONAL_JUMP` [`00afde80`](#insn-00afde80) → [`00afde1c`](#insn-00afde1c)
  - `FALL_THROUGH` [`00afde80`](#insn-00afde80) → [`00afde84`](#insn-00afde84)
- ブロック [`00afde84`](#insn-00afde84) 範囲 `[['00afde84', '00afde87']]`
  - `FALL_THROUGH` [`00afde84`](#insn-00afde84) → [`00afde88`](#insn-00afde88)
- ブロック [`00afde88`](#insn-00afde88) 範囲 `[['00afde88', '00afde9b']]`
  - `CONDITIONAL_JUMP` [`00afde98`](#insn-00afde98) → [`00afdeb8`](#insn-00afdeb8)
  - `FALL_THROUGH` [`00afde98`](#insn-00afde98) → [`00afde9c`](#insn-00afde9c)
- ブロック [`00afde9c`](#insn-00afde9c) 範囲 `[['00afde9c', '00afdea7']]`
  - `CONDITIONAL_JUMP` [`00afdea4`](#insn-00afdea4) → [`00afde88`](#insn-00afde88)
  - `FALL_THROUGH` [`00afdea4`](#insn-00afdea4) → [`00afdea8`](#insn-00afdea8)
- ブロック [`00afdea8`](#insn-00afdea8) 範囲 `[['00afdea8', '00afdeab']]`
  - `UNCONDITIONAL_JUMP` [`00afdea8`](#insn-00afdea8) → [`00afde1c`](#insn-00afde1c)
- ブロック [`00afdeac`](#insn-00afdeac) 範囲 `[['00afdeac', '00afdeaf']]`
  - `CONDITIONAL_JUMP` [`00afdeac`](#insn-00afdeac) → [`00afde1c`](#insn-00afde1c)
  - `FALL_THROUGH` [`00afdeac`](#insn-00afdeac) → [`00afdeb0`](#insn-00afdeb0)
- ブロック [`00afdeb0`](#insn-00afdeb0) 範囲 `[['00afdeb0', '00afdeb7']]`
  - `CONDITIONAL_JUMP` [`00afdeb4`](#insn-00afdeb4) → [`00afde1c`](#insn-00afde1c)
  - `FALL_THROUGH` [`00afdeb4`](#insn-00afdeb4) → [`00afdeb8`](#insn-00afdeb8)
- ブロック [`00afdeb8`](#insn-00afdeb8) 範囲 `[['00afdeb8', '00afdebf']]`
  - `CONDITIONAL_JUMP` [`00afdebc`](#insn-00afdebc) → [`00afdf40`](#insn-00afdf40)
  - `FALL_THROUGH` [`00afdebc`](#insn-00afdebc) → [`00afdec0`](#insn-00afdec0)
- ブロック [`00afdec0`](#insn-00afdec0) 範囲 `[['00afdec0', '00afdec3']]`
  - `UNCONDITIONAL_JUMP` [`00afdec0`](#insn-00afdec0) → [`00afdf8c`](#insn-00afdf8c)
- ブロック [`00afdec4`](#insn-00afdec4) 範囲 `[['00afdec4', '00afdec7']]`
  - `FALL_THROUGH` [`00afdec4`](#insn-00afdec4) → [`00afdec8`](#insn-00afdec8)
- ブロック [`00afdec8`](#insn-00afdec8) 範囲 `[['00afdec8', '00afdf2f']]`
  - `CONDITIONAL_JUMP` [`00afdf2c`](#insn-00afdf2c) → [`00afdf38`](#insn-00afdf38)
  - `FALL_THROUGH` [`00afdf2c`](#insn-00afdf2c) → [`00afdf30`](#insn-00afdf30)
- ブロック [`00afdf30`](#insn-00afdf30) 範囲 `[['00afdf30', '00afdf37']]`
  - `FALL_THROUGH` [`00afdf34`](#insn-00afdf34) → [`00afdf38`](#insn-00afdf38)
- ブロック [`00afdf38`](#insn-00afdf38) 範囲 `[['00afdf38', '00afdf3f']]`
  - `CONDITIONAL_JUMP` [`00afdf3c`](#insn-00afdf3c) → [`00afdf8c`](#insn-00afdf8c)
  - `FALL_THROUGH` [`00afdf3c`](#insn-00afdf3c) → [`00afdf40`](#insn-00afdf40)
- ブロック [`00afdf40`](#insn-00afdf40) 範囲 `[['00afdf40', '00afdf4b']]`
  - `CONDITIONAL_JUMP` [`00afdf48`](#insn-00afdf48) → [`00afdf80`](#insn-00afdf80)
  - `FALL_THROUGH` [`00afdf48`](#insn-00afdf48) → [`00afdf4c`](#insn-00afdf4c)
- ブロック [`00afdf4c`](#insn-00afdf4c) 範囲 `[['00afdf4c', '00afdf57']]`
  - `CONDITIONAL_JUMP` [`00afdf54`](#insn-00afdf54) → [`00afdf6c`](#insn-00afdf6c)
  - `FALL_THROUGH` [`00afdf54`](#insn-00afdf54) → [`00afdf58`](#insn-00afdf58)
- ブロック [`00afdf58`](#insn-00afdf58) 範囲 `[['00afdf58', '00afdf63']]`
  - `CONDITIONAL_JUMP` [`00afdf60`](#insn-00afdf60) → [`00afdf78`](#insn-00afdf78)
  - `FALL_THROUGH` [`00afdf60`](#insn-00afdf60) → [`00afdf64`](#insn-00afdf64)
- ブロック [`00afdf64`](#insn-00afdf64) 範囲 `[['00afdf64', '00afdf6b']]`
  - `CONDITIONAL_JUMP` [`00afdf68`](#insn-00afdf68) → [`00afdf58`](#insn-00afdf58)
  - `FALL_THROUGH` [`00afdf68`](#insn-00afdf68) → [`00afdf6c`](#insn-00afdf6c)
- ブロック [`00afdf6c`](#insn-00afdf6c) 範囲 `[['00afdf6c', '00afdf77']]`
  - `UNCONDITIONAL_JUMP` [`00afdf74`](#insn-00afdf74) → [`00afdf58`](#insn-00afdf58)
- ブロック [`00afdf78`](#insn-00afdf78) 範囲 `[['00afdf78', '00afdf7f']]`
  - `UNCONDITIONAL_JUMP` [`00afdf7c`](#insn-00afdf7c) → [`00afdf84`](#insn-00afdf84)
- ブロック [`00afdf80`](#insn-00afdf80) 範囲 `[['00afdf80', '00afdf83']]`
  - `FALL_THROUGH` [`00afdf80`](#insn-00afdf80) → [`00afdf84`](#insn-00afdf84)
- ブロック [`00afdf84`](#insn-00afdf84) 範囲 `[['00afdf84', '00afdf8b']]`
  - `FALL_THROUGH` [`00afdf88`](#insn-00afdf88) → [`00afdf8c`](#insn-00afdf8c)
- ブロック [`00afdf8c`](#insn-00afdf8c) 範囲 `[['00afdf8c', '00afdf93']]`
  - `CONDITIONAL_JUMP` [`00afdf90`](#insn-00afdf90) → [`00afdfe0`](#insn-00afdfe0)
  - `FALL_THROUGH` [`00afdf90`](#insn-00afdf90) → [`00afdf94`](#insn-00afdf94)
- ブロック [`00afdf94`](#insn-00afdf94) 範囲 `[['00afdf94', '00afdf9f']]`
  - `CONDITIONAL_JUMP` [`00afdf9c`](#insn-00afdf9c) → [`00afdfd4`](#insn-00afdfd4)
  - `FALL_THROUGH` [`00afdf9c`](#insn-00afdf9c) → [`00afdfa0`](#insn-00afdfa0)
- ブロック [`00afdfa0`](#insn-00afdfa0) 範囲 `[['00afdfa0', '00afdfab']]`
  - `CONDITIONAL_JUMP` [`00afdfa8`](#insn-00afdfa8) → [`00afdfc0`](#insn-00afdfc0)
  - `FALL_THROUGH` [`00afdfa8`](#insn-00afdfa8) → [`00afdfac`](#insn-00afdfac)
- ブロック [`00afdfac`](#insn-00afdfac) 範囲 `[['00afdfac', '00afdfb7']]`
  - `CONDITIONAL_JUMP` [`00afdfb4`](#insn-00afdfb4) → [`00afdfcc`](#insn-00afdfcc)
  - `FALL_THROUGH` [`00afdfb4`](#insn-00afdfb4) → [`00afdfb8`](#insn-00afdfb8)
- ブロック [`00afdfb8`](#insn-00afdfb8) 範囲 `[['00afdfb8', '00afdfbf']]`
  - `CONDITIONAL_JUMP` [`00afdfbc`](#insn-00afdfbc) → [`00afdfac`](#insn-00afdfac)
  - `FALL_THROUGH` [`00afdfbc`](#insn-00afdfbc) → [`00afdfc0`](#insn-00afdfc0)
- ブロック [`00afdfc0`](#insn-00afdfc0) 範囲 `[['00afdfc0', '00afdfcb']]`
  - `UNCONDITIONAL_JUMP` [`00afdfc8`](#insn-00afdfc8) → [`00afdfac`](#insn-00afdfac)
- ブロック [`00afdfcc`](#insn-00afdfcc) 範囲 `[['00afdfcc', '00afdfd3']]`
  - `UNCONDITIONAL_JUMP` [`00afdfd0`](#insn-00afdfd0) → [`00afdfd8`](#insn-00afdfd8)
- ブロック [`00afdfd4`](#insn-00afdfd4) 範囲 `[['00afdfd4', '00afdfd7']]`
  - `FALL_THROUGH` [`00afdfd4`](#insn-00afdfd4) → [`00afdfd8`](#insn-00afdfd8)
- ブロック [`00afdfd8`](#insn-00afdfd8) 範囲 `[['00afdfd8', '00afdfdf']]`
  - `FALL_THROUGH` [`00afdfdc`](#insn-00afdfdc) → [`00afdfe0`](#insn-00afdfe0)
- ブロック [`00afdfe0`](#insn-00afdfe0) 範囲 `[['00afdfe0', '00afdfef']]`
  - `CONDITIONAL_JUMP` [`00afdfec`](#insn-00afdfec) → [`00afe014`](#insn-00afe014)
  - `FALL_THROUGH` [`00afdfec`](#insn-00afdfec) → [`00afdff0`](#insn-00afdff0)
- ブロック [`00afdff0`](#insn-00afdff0) 範囲 `[['00afdff0', '00afe00b']]`
- ブロック [`00afe00c`](#insn-00afe00c) 範囲 `[['00afe00c', '00afe013']]`
  - `UNCONDITIONAL_JUMP` [`00afe010`](#insn-00afe010) → [`00afdec8`](#insn-00afdec8)
- ブロック [`00afe014`](#insn-00afe014) 範囲 `[['00afe014', '00afe017']]`

## 命令位置別の参照

- [`00afddb8`](#insn-00afddb8) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afddbc`](#insn-00afddbc) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afddc0`](#insn-00afddc0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afddc4`](#insn-00afddc4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afddc8`](#insn-00afddc8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdde0`](#insn-00afdde0) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdde8`](#insn-00afdde8) → [`00bdecf0`](../00bde/00bdecf0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdecf0` · 推定シンボル `None` · 推定型 `None`
- [`00afddf4`](#insn-00afddf4) → [`00bdecf0`](../00bde/00bdecf0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdecf0` · 推定シンボル `None` · 推定型 `None`
- [`00afddf8`](#insn-00afddf8) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afddfc`](#insn-00afddfc) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afde04`](#insn-00afde04) → [`00afdec4`](#insn-00afdec4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afde08`](#insn-00afde08) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afde14`](#insn-00afde14) → [`00afde34`](#insn-00afde34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afde18`](#insn-00afde18) → [`00afdeb8`](#insn-00afdeb8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afde28`](#insn-00afde28) → [`00afe00c`](#insn-00afe00c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afde30`](#insn-00afde30) → [`00afdeb8`](#insn-00afdeb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afde60`](#insn-00afde60) → [`00afdeb8`](#insn-00afdeb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afde7c`](#insn-00afde7c) → [`00afdeac`](#insn-00afdeac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afde80`](#insn-00afde80) → [`00afde1c`](#insn-00afde1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afde98`](#insn-00afde98) → [`00afdeb8`](#insn-00afdeb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdea4`](#insn-00afdea4) → [`00afde88`](#insn-00afde88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdea8`](#insn-00afdea8) → [`00afde1c`](#insn-00afde1c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdeac`](#insn-00afdeac) → [`00afde1c`](#insn-00afde1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdeb0`](#insn-00afdeb0) → [`00bdb1b0`](../00bdb/00bdb1b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb1b0` · 推定シンボル `None` · 推定型 `None`
- [`00afdeb4`](#insn-00afdeb4) → [`00afde1c`](#insn-00afde1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdebc`](#insn-00afdebc) → [`00afdf40`](#insn-00afdf40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdec0`](#insn-00afdec0) → [`00afdf8c`](#insn-00afdf8c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdec4`](#insn-00afdec4) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afded8`](#insn-00afded8) → [`00afd268`](00afd268.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00afd268` · 推定シンボル `None` · 推定型 `None`
- [`00afdedc`](#insn-00afdedc) → `Stack[-0xb8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdee0`](#insn-00afdee0) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdefc`](#insn-00afdefc) → `Stack[-0x98]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdf00`](#insn-00afdf00) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdf04`](#insn-00afdf04) → [`00bde1e0`](../00bde/00bde1e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde1e0` · 推定シンボル `None` · 推定型 `None`
- [`00afdf08`](#insn-00afdf08) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdf0c`](#insn-00afdf0c) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdf10`](#insn-00afdf10) → `Stack[-0xb8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdf18`](#insn-00afdf18) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdf28`](#insn-00afdf28) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdf2c`](#insn-00afdf2c) → [`00afdf38`](#insn-00afdf38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdf30`](#insn-00afdf30) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdf34`](#insn-00afdf34) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00afdf38`](#insn-00afdf38) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdf3c`](#insn-00afdf3c) → [`00afdf8c`](#insn-00afdf8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdf40`](#insn-00afdf40) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdf48`](#insn-00afdf48) → [`00afdf80`](#insn-00afdf80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdf54`](#insn-00afdf54) → [`00afdf6c`](#insn-00afdf6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdf60`](#insn-00afdf60) → [`00afdf78`](#insn-00afdf78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdf68`](#insn-00afdf68) → [`00afdf58`](#insn-00afdf58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdf70`](#insn-00afdf70) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00afdf74`](#insn-00afdf74) → [`00afdf58`](#insn-00afdf58) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdf78`](#insn-00afdf78) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdf7c`](#insn-00afdf7c) → [`00afdf84`](#insn-00afdf84) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdf84`](#insn-00afdf84) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdf88`](#insn-00afdf88) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00afdf8c`](#insn-00afdf8c) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdf90`](#insn-00afdf90) → [`00afdfe0`](#insn-00afdfe0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdf94`](#insn-00afdf94) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdf9c`](#insn-00afdf9c) → [`00afdfd4`](#insn-00afdfd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdfa8`](#insn-00afdfa8) → [`00afdfc0`](#insn-00afdfc0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdfb4`](#insn-00afdfb4) → [`00afdfcc`](#insn-00afdfcc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdfbc`](#insn-00afdfbc) → [`00afdfac`](#insn-00afdfac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdfc4`](#insn-00afdfc4) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00afdfc8`](#insn-00afdfc8) → [`00afdfac`](#insn-00afdfac) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdfcc`](#insn-00afdfcc) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdfd0`](#insn-00afdfd0) → [`00afdfd8`](#insn-00afdfd8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdfd8`](#insn-00afdfd8) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdfdc`](#insn-00afdfdc) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00afdfe4`](#insn-00afdfe4) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdfec`](#insn-00afdfec) → [`00afe014`](#insn-00afe014) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdff0`](#insn-00afdff0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdff4`](#insn-00afdff4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdff8`](#insn-00afdff8) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdffc`](#insn-00afdffc) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe000`](#insn-00afe000) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe010`](#insn-00afe010) → [`00afdec8`](#insn-00afdec8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe014`](#insn-00afe014) → [`00bdb040`](../00bdb/00bdb040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb040` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afddb8`](#insn-00afddb8)

~~~json
{
  "source": "00afddb8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afddbc`](#insn-00afddbc)

~~~json
{
  "source": "00afddbc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afddc0`](#insn-00afddc0)

~~~json
{
  "source": "00afddc0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afddc4`](#insn-00afddc4)

~~~json
{
  "source": "00afddc4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afddc8`](#insn-00afddc8)

~~~json
{
  "source": "00afddc8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdde0`](#insn-00afdde0)

~~~json
{
  "source": "00afdde0",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdde8`](#insn-00afdde8)

~~~json
{
  "source": "00afdde8",
  "target": "00bdecf0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afddf4`](#insn-00afddf4)

~~~json
{
  "source": "00afddf4",
  "target": "00bdecf0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afddf8`](#insn-00afddf8)

~~~json
{
  "source": "00afddf8",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afddfc`](#insn-00afddfc)

~~~json
{
  "source": "00afddfc",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afde04`](#insn-00afde04)

~~~json
{
  "source": "00afde04",
  "target": "00afdec4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afde08`](#insn-00afde08)

~~~json
{
  "source": "00afde08",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afde14`](#insn-00afde14)

~~~json
{
  "source": "00afde14",
  "target": "00afde34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afde18`](#insn-00afde18)

~~~json
{
  "source": "00afde18",
  "target": "00afdeb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afde28`](#insn-00afde28)

~~~json
{
  "source": "00afde28",
  "target": "00afe00c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afde30`](#insn-00afde30)

~~~json
{
  "source": "00afde30",
  "target": "00afdeb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afde60`](#insn-00afde60)

~~~json
{
  "source": "00afde60",
  "target": "00afdeb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afde7c`](#insn-00afde7c)

~~~json
{
  "source": "00afde7c",
  "target": "00afdeac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afde80`](#insn-00afde80)

~~~json
{
  "source": "00afde80",
  "target": "00afde1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afde98`](#insn-00afde98)

~~~json
{
  "source": "00afde98",
  "target": "00afdeb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdea4`](#insn-00afdea4)

~~~json
{
  "source": "00afdea4",
  "target": "00afde88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdea8`](#insn-00afdea8)

~~~json
{
  "source": "00afdea8",
  "target": "00afde1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdeac`](#insn-00afdeac)

~~~json
{
  "source": "00afdeac",
  "target": "00afde1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdeb0`](#insn-00afdeb0)

~~~json
{
  "source": "00afdeb0",
  "target": "00bdb1b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afdeb4`](#insn-00afdeb4)

~~~json
{
  "source": "00afdeb4",
  "target": "00afde1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdebc`](#insn-00afdebc)

~~~json
{
  "source": "00afdebc",
  "target": "00afdf40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdec0`](#insn-00afdec0)

~~~json
{
  "source": "00afdec0",
  "target": "00afdf8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdec4`](#insn-00afdec4)

~~~json
{
  "source": "00afdec4",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afded8`](#insn-00afded8)

~~~json
{
  "source": "00afded8",
  "target": "00afd268",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afdedc`](#insn-00afdedc)

~~~json
{
  "source": "00afdedc",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdee0`](#insn-00afdee0)

~~~json
{
  "source": "00afdee0",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdefc`](#insn-00afdefc)

~~~json
{
  "source": "00afdefc",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdf00`](#insn-00afdf00)

~~~json
{
  "source": "00afdf00",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdf04`](#insn-00afdf04)

~~~json
{
  "source": "00afdf04",
  "target": "00bde1e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afdf08`](#insn-00afdf08)

~~~json
{
  "source": "00afdf08",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdf0c`](#insn-00afdf0c)

~~~json
{
  "source": "00afdf0c",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdf10`](#insn-00afdf10)

~~~json
{
  "source": "00afdf10",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdf18`](#insn-00afdf18)

~~~json
{
  "source": "00afdf18",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdf28`](#insn-00afdf28)

~~~json
{
  "source": "00afdf28",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdf2c`](#insn-00afdf2c)

~~~json
{
  "source": "00afdf2c",
  "target": "00afdf38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdf30`](#insn-00afdf30)

~~~json
{
  "source": "00afdf30",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdf34`](#insn-00afdf34)

~~~json
{
  "source": "00afdf34",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afdf38`](#insn-00afdf38)

~~~json
{
  "source": "00afdf38",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdf3c`](#insn-00afdf3c)

~~~json
{
  "source": "00afdf3c",
  "target": "00afdf8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdf40`](#insn-00afdf40)

~~~json
{
  "source": "00afdf40",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdf48`](#insn-00afdf48)

~~~json
{
  "source": "00afdf48",
  "target": "00afdf80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdf54`](#insn-00afdf54)

~~~json
{
  "source": "00afdf54",
  "target": "00afdf6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdf60`](#insn-00afdf60)

~~~json
{
  "source": "00afdf60",
  "target": "00afdf78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdf68`](#insn-00afdf68)

~~~json
{
  "source": "00afdf68",
  "target": "00afdf58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdf70`](#insn-00afdf70)

~~~json
{
  "source": "00afdf70",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afdf74`](#insn-00afdf74)

~~~json
{
  "source": "00afdf74",
  "target": "00afdf58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdf78`](#insn-00afdf78)

~~~json
{
  "source": "00afdf78",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdf7c`](#insn-00afdf7c)

~~~json
{
  "source": "00afdf7c",
  "target": "00afdf84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdf84`](#insn-00afdf84)

~~~json
{
  "source": "00afdf84",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdf88`](#insn-00afdf88)

~~~json
{
  "source": "00afdf88",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afdf8c`](#insn-00afdf8c)

~~~json
{
  "source": "00afdf8c",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdf90`](#insn-00afdf90)

~~~json
{
  "source": "00afdf90",
  "target": "00afdfe0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdf94`](#insn-00afdf94)

~~~json
{
  "source": "00afdf94",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdf9c`](#insn-00afdf9c)

~~~json
{
  "source": "00afdf9c",
  "target": "00afdfd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdfa8`](#insn-00afdfa8)

~~~json
{
  "source": "00afdfa8",
  "target": "00afdfc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdfb4`](#insn-00afdfb4)

~~~json
{
  "source": "00afdfb4",
  "target": "00afdfcc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdfbc`](#insn-00afdfbc)

~~~json
{
  "source": "00afdfbc",
  "target": "00afdfac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdfc4`](#insn-00afdfc4)

~~~json
{
  "source": "00afdfc4",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afdfc8`](#insn-00afdfc8)

~~~json
{
  "source": "00afdfc8",
  "target": "00afdfac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdfcc`](#insn-00afdfcc)

~~~json
{
  "source": "00afdfcc",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdfd0`](#insn-00afdfd0)

~~~json
{
  "source": "00afdfd0",
  "target": "00afdfd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdfd8`](#insn-00afdfd8)

~~~json
{
  "source": "00afdfd8",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdfdc`](#insn-00afdfdc)

~~~json
{
  "source": "00afdfdc",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afdfe4`](#insn-00afdfe4)

~~~json
{
  "source": "00afdfe4",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdfec`](#insn-00afdfec)

~~~json
{
  "source": "00afdfec",
  "target": "00afe014",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdff0`](#insn-00afdff0)

~~~json
{
  "source": "00afdff0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdff4`](#insn-00afdff4)

~~~json
{
  "source": "00afdff4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdff8`](#insn-00afdff8)

~~~json
{
  "source": "00afdff8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdffc`](#insn-00afdffc)

~~~json
{
  "source": "00afdffc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe000`](#insn-00afe000)

~~~json
{
  "source": "00afe000",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe010`](#insn-00afe010)

~~~json
{
  "source": "00afe010",
  "target": "00afdec8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe014`](#insn-00afe014)

~~~json
{
  "source": "00afe014",
  "target": "00bdb040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
