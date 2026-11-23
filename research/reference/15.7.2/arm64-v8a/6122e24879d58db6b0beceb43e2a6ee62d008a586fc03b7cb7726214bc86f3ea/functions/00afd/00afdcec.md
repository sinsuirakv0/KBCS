# 00afdcec

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00afddb4`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afddb4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/alignment_unresolved-0002.md#compare-35d66230e38eee5023913762801e9692)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afdcec",
  "name": "_ZN8firebase4Path11GetRelativeERKS0_S2_",
  "size": 612,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "78ead4e4e5d111b7e639814d87def2787b21230824c8c758f99f96b96ee69292",
  "source_text_sha256": "78ead4e4e5d111b7e639814d87def2787b21230824c8c758f99f96b96ee69292",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afdcec",
        "00afdf4f"
      ]
    ],
    "bytes_sha256": "a48c33833fe47a63076f1bbd5d86891f7967d28857911d8517f346deb39a3747",
    "instruction_count": 153,
    "instruction_bytes": 612,
    "body_bytes": 612,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bdec20](../00bde/00bdec20.md)

## 呼び出し先

- [00afd1a0](../00afd/00afd1a0.md)
- [00bdaf60](../00bda/00bdaf60.md)
- [00bdaf90](../00bda/00bdaf90.md)
- [00bdb100](../00bdb/00bdb100.md)
- [00bde130](../00bde/00bde130.md)
- [00bdec40](../00bde/00bdec40.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 4367 bytes

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
  
                    /* try { // try from 00afdcfc to 00bfdd07 has its CatchHandler @ 00afebe4 */
                    /* try { // try from 00afdd08 to 00bfdd1f has its CatchHandler @ 00afeb88 */
  lVar6 = tpidr_el0;
  local_58 = *(long *)(lVar6 + 0x28);
                    /* try { // try from 00afdd20 to 00c00b67 has its CatchHandler @ 00af560c */
  _ZNK8firebase4Path14GetDirectoriesEv(&local_70);
  _ZNK8firebase4Path14GetDirectoriesEv(&local_88,param_3);
  pbVar12 = local_68;
  pbVar11 = local_80;
  pbVar8 = local_88;
  pbVar2 = local_88;
  pbVar1 = local_70;
  do {
    if (pbVar1 == pbVar12) {
      FUN_00afd1a0(local_b8,pbVar2,pbVar11);
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
joined_r0x00afde74:
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
LAB_00afddf0:
      *(undefined1 *)(param_1 + 3) = 0;
      pbVar1 = local_88;
      goto joined_r0x00afde74;
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
    if (__n != sVar3) goto LAB_00afddf0;
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
          if (pbVar1[uVar14 + 1] != __s2[uVar14]) goto LAB_00afddf0;
          uVar14 = uVar14 + 1;
        } while (bVar4 >> 1 != uVar14);
      }
    }
    else if ((__n != 0) && (iVar13 = memcmp(__s1,__s2,__n), iVar13 != 0)) goto LAB_00afddf0;
    pbVar1 = pbVar1 + 0x18;
    pbVar2 = pbVar2 + 0x18;
  } while( true );
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afdcec"></a> `00afdcec` | `ff 03 03 d1` | sub sp,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00afdcf0"></a> `00afdcf0` | `f9 3b 00 f9` | str x25,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00afdcf4"></a> `00afdcf4` | `f8 5f 08 a9` | stp x24,x23,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00afdcf8"></a> `00afdcf8` | `f6 57 09 a9` | stp x22,x21,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00afdcfc"></a> `00afdcfc` | `f4 4f 0a a9` | stp x20,x19,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00afdd00"></a> `00afdd00` | `fd 7b 0b a9` | stp x29,x30,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00afdd04"></a> `00afdd04` | `fd c3 02 91` | add x29,sp,#0xb0 | `FALL_THROUGH`
<a id="insn-00afdd08"></a> `00afdd08` | `56 d0 3b d5` | mrs x22,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00afdd0c"></a> `00afdd0c` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00afdd10"></a> `00afdd10` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00afdd14"></a> `00afdd14` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00afdd18"></a> `00afdd18` | `a8 83 1b f8` | stur x8,[x29, #-0x48] | `FALL_THROUGH`
<a id="insn-00afdd1c"></a> `00afdd1c` | `e8 43 01 91` | add x8,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00afdd20"></a> `00afdd20` | `c8 83 03 94` | bl 0x00bdec40 | `UNCONDITIONAL_CALL`
<a id="insn-00afdd24"></a> `00afdd24` | `e8 e3 00 91` | add x8,sp,#0x38 | `FALL_THROUGH`
<a id="insn-00afdd28"></a> `00afdd28` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00afdd2c"></a> `00afdd2c` | `c5 83 03 94` | bl 0x00bdec40 | `UNCONDITIONAL_CALL`
<a id="insn-00afdd30"></a> `00afdd30` | `f8 5f 45 a9` | ldp x24,x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00afdd34"></a> `00afdd34` | `f4 1f 40 f9` | ldr x20,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00afdd38"></a> `00afdd38` | `1f 03 17 eb` | cmp x24,x23 | `FALL_THROUGH`
<a id="insn-00afdd3c"></a> `00afdd3c` | `00 06 00 54` | b.eq 0x00afddfc | `CONDITIONAL_JUMP`
<a id="insn-00afdd40"></a> `00afdd40` | `f5 23 40 f9` | ldr x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00afdd44"></a> `00afdd44` | `f9 03 14 aa` | mov x25,x20 | `FALL_THROUGH`
<a id="insn-00afdd48"></a> `00afdd48` | `bf 02 19 eb` | cmp x21,x25 | `FALL_THROUGH`
<a id="insn-00afdd4c"></a> `00afdd4c` | `01 01 00 54` | b.ne 0x00afdd6c | `CONDITIONAL_JUMP`
<a id="insn-00afdd50"></a> `00afdd50` | `28 00 00 14` | b 0x00afddf0 | `UNCONDITIONAL_JUMP`
<a id="insn-00afdd54"></a> `00afdd54` | `18 63 00 91` | add x24,x24,#0x18 | `FALL_THROUGH`
<a id="insn-00afdd58"></a> `00afdd58` | `1f 03 17 eb` | cmp x24,x23 | `FALL_THROUGH`
<a id="insn-00afdd5c"></a> `00afdd5c` | `39 63 00 91` | add x25,x25,#0x18 | `FALL_THROUGH`
<a id="insn-00afdd60"></a> `00afdd60` | `20 0f 00 54` | b.eq 0x00afdf44 | `CONDITIONAL_JUMP`
<a id="insn-00afdd64"></a> `00afdd64` | `bf 02 19 eb` | cmp x21,x25 | `FALL_THROUGH`
<a id="insn-00afdd68"></a> `00afdd68` | `40 04 00 54` | b.eq 0x00afddf0 | `CONDITIONAL_JUMP`
<a id="insn-00afdd6c"></a> `00afdd6c` | `09 03 40 39` | ldrb w9,[x24] | `FALL_THROUGH`
<a id="insn-00afdd70"></a> `00afdd70` | `0b 07 40 f9` | ldr x11,[x24, #0x8] | `FALL_THROUGH`
<a id="insn-00afdd74"></a> `00afdd74` | `2a 03 40 39` | ldrb w10,[x25] | `FALL_THROUGH`
<a id="insn-00afdd78"></a> `00afdd78` | `2c 07 40 f9` | ldr x12,[x25, #0x8] | `FALL_THROUGH`
<a id="insn-00afdd7c"></a> `00afdd7c` | `28 fd 41 d3` | lsr x8,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00afdd80"></a> `00afdd80` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00afdd84"></a> `00afdd84` | `4d fd 41 d3` | lsr x13,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00afdd88"></a> `00afdd88` | `02 01 8b 9a` | csel x2,x8,x11,eq | `FALL_THROUGH`
<a id="insn-00afdd8c"></a> `00afdd8c` | `5f 01 00 72` | tst w10,#0x1 | `FALL_THROUGH`
<a id="insn-00afdd90"></a> `00afdd90` | `ab 01 8c 9a` | csel x11,x13,x12,eq | `FALL_THROUGH`
<a id="insn-00afdd94"></a> `00afdd94` | `5f 00 0b eb` | cmp x2,x11 | `FALL_THROUGH`
<a id="insn-00afdd98"></a> `00afdd98` | `c1 02 00 54` | b.ne 0x00afddf0 | `CONDITIONAL_JUMP`
<a id="insn-00afdd9c"></a> `00afdd9c` | `0b 0b 40 f9` | ldr x11,[x24, #0x10] | `FALL_THROUGH`
<a id="insn-00afdda0"></a> `00afdda0` | `2c 0b 40 f9` | ldr x12,[x25, #0x10] | `FALL_THROUGH`
<a id="insn-00afdda4"></a> `00afdda4` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00afdda8"></a> `00afdda8` | `60 15 98 9a` | csinc x0,x11,x24,ne | `FALL_THROUGH`
<a id="insn-00afddac"></a> `00afddac` | `5f 01 00 72` | tst w10,#0x1 | `FALL_THROUGH`
<a id="insn-00afddb0"></a> `00afddb0` | `81 15 99 9a` | csinc x1,x12,x25,ne | `FALL_THROUGH`
<a id="insn-00afddb4"></a> `00afddb4` | `89 01 00 37` | tbnz w9,#0x0,0x00afdde4 | `CONDITIONAL_JUMP`
<a id="insn-00afddb8"></a> `00afddb8` | `e2 fc ff b4` | cbz x2,0x00afdd54 | `CONDITIONAL_JUMP`
<a id="insn-00afddbc"></a> `00afddbc` | `e9 03 1f aa` | mov x9,xzr | `FALL_THROUGH`
<a id="insn-00afddc0"></a> `00afddc0` | `0a 03 09 8b` | add x10,x24,x9 | `FALL_THROUGH`
<a id="insn-00afddc4"></a> `00afddc4` | `4a 05 40 39` | ldrb w10,[x10, #0x1] | `FALL_THROUGH`
<a id="insn-00afddc8"></a> `00afddc8` | `2b 68 69 38` | ldrb w11,[x1, x9, LSL ] | `FALL_THROUGH`
<a id="insn-00afddcc"></a> `00afddcc` | `5f 01 0b 6b` | cmp w10,w11 | `FALL_THROUGH`
<a id="insn-00afddd0"></a> `00afddd0` | `01 01 00 54` | b.ne 0x00afddf0 | `CONDITIONAL_JUMP`
<a id="insn-00afddd4"></a> `00afddd4` | `29 05 00 91` | add x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00afddd8"></a> `00afddd8` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00afdddc"></a> `00afdddc` | `21 ff ff 54` | b.ne 0x00afddc0 | `CONDITIONAL_JUMP`
<a id="insn-00afdde0"></a> `00afdde0` | `dd ff ff 17` | b 0x00afdd54 | `UNCONDITIONAL_JUMP`
<a id="insn-00afdde4"></a> `00afdde4` | `82 fb ff b4` | cbz x2,0x00afdd54 | `CONDITIONAL_JUMP`
<a id="insn-00afdde8"></a> `00afdde8` | `c6 74 03 94` | bl 0x00bdb100 | `UNCONDITIONAL_CALL`
<a id="insn-00afddec"></a> `00afddec` | `40 fb ff 34` | cbz w0,0x00afdd54 | `CONDITIONAL_JUMP`
<a id="insn-00afddf0"></a> `00afddf0` | `7f 62 00 39` | strb wzr,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00afddf4"></a> `00afddf4` | `34 04 00 b5` | cbnz x20,0x00afde78 | `CONDITIONAL_JUMP`
<a id="insn-00afddf8"></a> `00afddf8` | `33 00 00 14` | b 0x00afdec4 | `UNCONDITIONAL_JUMP`
<a id="insn-00afddfc"></a> `00afddfc` | `f5 23 40 f9` | ldr x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00afde00"></a> `00afde00` | `e8 23 00 91` | add x8,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00afde04"></a> `00afde04` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00afde08"></a> `00afde08` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00afde0c"></a> `00afde0c` | `f7 23 00 91` | add x23,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00afde10"></a> `00afde10` | `e4 fc ff 97` | bl 0x00afd1a0 | `UNCONDITIONAL_CALL`
<a id="insn-00afde14"></a> `00afde14` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00afde18"></a> `00afde18` | `ea 27 41 a9` | ldp x10,x9,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afde1c"></a> `00afde1c` | `eb 02 40 b2` | orr x11,x23,#0x1 | `FALL_THROUGH`
<a id="insn-00afde20"></a> `00afde20` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00afde24"></a> `00afde24` | `0c fd 41 d3` | lsr x12,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00afde28"></a> `00afde28` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00afde2c"></a> `00afde2c` | `61 01 89 9a` | csel x1,x11,x9,eq | `FALL_THROUGH`
<a id="insn-00afde30"></a> `00afde30` | `82 01 8a 9a` | csel x2,x12,x10,eq | `FALL_THROUGH`
<a id="insn-00afde34"></a> `00afde34` | `ff ff 02 a9` | stp xzr,xzr,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00afde38"></a> `00afde38` | `ff 13 00 f9` | str xzr,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afde3c"></a> `00afde3c` | `bd 80 03 94` | bl 0x00bde130 | `UNCONDITIONAL_CALL`
<a id="insn-00afde40"></a> `00afde40` | `e0 0b c0 3d` | ldr q0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afde44"></a> `00afde44` | `e9 1b 40 f9` | ldr x9,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00afde48"></a> `00afde48` | `ea 23 40 39` | ldrb w10,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00afde4c"></a> `00afde4c` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00afde50"></a> `00afde50` | `ff 7f 02 a9` | stp xzr,xzr,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afde54"></a> `00afde54` | `68 62 00 39` | strb w8,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00afde58"></a> `00afde58` | `69 0a 00 f9` | str x9,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00afde5c"></a> `00afde5c` | `60 02 80 3d` | str q0,[x19] | `FALL_THROUGH`
<a id="insn-00afde60"></a> `00afde60` | `ff 1b 00 f9` | str xzr,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00afde64"></a> `00afde64` | `6a 00 00 36` | tbz w10,#0x0,0x00afde70 | `CONDITIONAL_JUMP`
<a id="insn-00afde68"></a> `00afde68` | `e0 0f 40 f9` | ldr x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00afde6c"></a> `00afde6c` | `3d 74 03 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00afde70"></a> `00afde70` | `f4 1f 40 f9` | ldr x20,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00afde74"></a> `00afde74` | `94 02 00 b4` | cbz x20,0x00afdec4 | `CONDITIONAL_JUMP`
<a id="insn-00afde78"></a> `00afde78` | `e8 23 40 f9` | ldr x8,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00afde7c"></a> `00afde7c` | `1f 01 14 eb` | cmp x8,x20 | `FALL_THROUGH`
<a id="insn-00afde80"></a> `00afde80` | `c0 01 00 54` | b.eq 0x00afdeb8 | `CONDITIONAL_JUMP`
<a id="insn-00afde84"></a> `00afde84` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00afde88"></a> `00afde88` | `69 8e 5e 38` | ldrb w9,[x19, #-0x18]! | `FALL_THROUGH`
<a id="insn-00afde8c"></a> `00afde8c` | `c9 00 00 37` | tbnz w9,#0x0,0x00afdea4 | `CONDITIONAL_JUMP`
<a id="insn-00afde90"></a> `00afde90` | `9f 02 13 eb` | cmp x20,x19 | `FALL_THROUGH`
<a id="insn-00afde94"></a> `00afde94` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-00afde98"></a> `00afde98` | `c0 00 00 54` | b.eq 0x00afdeb0 | `CONDITIONAL_JUMP`
<a id="insn-00afde9c"></a> `00afde9c` | `69 8e 5e 38` | ldrb w9,[x19, #-0x18]! | `FALL_THROUGH`
<a id="insn-00afdea0"></a> `00afdea0` | `89 ff 07 36` | tbz w9,#0x0,0x00afde90 | `CONDITIONAL_JUMP`
<a id="insn-00afdea4"></a> `00afdea4` | `00 81 5f f8` | ldur x0,[x8, #-0x8] | `FALL_THROUGH`
<a id="insn-00afdea8"></a> `00afdea8` | `2e 74 03 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00afdeac"></a> `00afdeac` | `f9 ff ff 17` | b 0x00afde90 | `UNCONDITIONAL_JUMP`
<a id="insn-00afdeb0"></a> `00afdeb0` | `e0 1f 40 f9` | ldr x0,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00afdeb4"></a> `00afdeb4` | `02 00 00 14` | b 0x00afdebc | `UNCONDITIONAL_JUMP`
<a id="insn-00afdeb8"></a> `00afdeb8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00afdebc"></a> `00afdebc` | `f4 23 00 f9` | str x20,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00afdec0"></a> `00afdec0` | `28 74 03 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00afdec4"></a> `00afdec4` | `f3 2b 40 f9` | ldr x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00afdec8"></a> `00afdec8` | `93 02 00 b4` | cbz x19,0x00afdf18 | `CONDITIONAL_JUMP`
<a id="insn-00afdecc"></a> `00afdecc` | `e8 2f 40 f9` | ldr x8,[sp, #0x58] | `FALL_THROUGH`
<a id="insn-00afded0"></a> `00afded0` | `1f 01 13 eb` | cmp x8,x19 | `FALL_THROUGH`
<a id="insn-00afded4"></a> `00afded4` | `c0 01 00 54` | b.eq 0x00afdf0c | `CONDITIONAL_JUMP`
<a id="insn-00afded8"></a> `00afded8` | `f4 03 08 aa` | mov x20,x8 | `FALL_THROUGH`
<a id="insn-00afdedc"></a> `00afdedc` | `89 8e 5e 38` | ldrb w9,[x20, #-0x18]! | `FALL_THROUGH`
<a id="insn-00afdee0"></a> `00afdee0` | `c9 00 00 37` | tbnz w9,#0x0,0x00afdef8 | `CONDITIONAL_JUMP`
<a id="insn-00afdee4"></a> `00afdee4` | `7f 02 14 eb` | cmp x19,x20 | `FALL_THROUGH`
<a id="insn-00afdee8"></a> `00afdee8` | `e8 03 14 aa` | mov x8,x20 | `FALL_THROUGH`
<a id="insn-00afdeec"></a> `00afdeec` | `c0 00 00 54` | b.eq 0x00afdf04 | `CONDITIONAL_JUMP`
<a id="insn-00afdef0"></a> `00afdef0` | `89 8e 5e 38` | ldrb w9,[x20, #-0x18]! | `FALL_THROUGH`
<a id="insn-00afdef4"></a> `00afdef4` | `89 ff 07 36` | tbz w9,#0x0,0x00afdee4 | `CONDITIONAL_JUMP`
<a id="insn-00afdef8"></a> `00afdef8` | `00 81 5f f8` | ldur x0,[x8, #-0x8] | `FALL_THROUGH`
<a id="insn-00afdefc"></a> `00afdefc` | `19 74 03 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00afdf00"></a> `00afdf00` | `f9 ff ff 17` | b 0x00afdee4 | `UNCONDITIONAL_JUMP`
<a id="insn-00afdf04"></a> `00afdf04` | `e0 2b 40 f9` | ldr x0,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00afdf08"></a> `00afdf08` | `02 00 00 14` | b 0x00afdf10 | `UNCONDITIONAL_JUMP`
<a id="insn-00afdf0c"></a> `00afdf0c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00afdf10"></a> `00afdf10` | `f3 2f 00 f9` | str x19,[sp, #0x58] | `FALL_THROUGH`
<a id="insn-00afdf14"></a> `00afdf14` | `13 74 03 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00afdf18"></a> `00afdf18` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00afdf1c"></a> `00afdf1c` | `a9 83 5b f8` | ldur x9,[x29, #-0x48] | `FALL_THROUGH`
<a id="insn-00afdf20"></a> `00afdf20` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00afdf24"></a> `00afdf24` | `41 01 00 54` | b.ne 0x00afdf4c | `CONDITIONAL_JUMP`
<a id="insn-00afdf28"></a> `00afdf28` | `fd 7b 4b a9` | ldp x29,x30,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00afdf2c"></a> `00afdf2c` | `f4 4f 4a a9` | ldp x20,x19,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00afdf30"></a> `00afdf30` | `f6 57 49 a9` | ldp x22,x21,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00afdf34"></a> `00afdf34` | `f8 5f 48 a9` | ldp x24,x23,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00afdf38"></a> `00afdf38` | `f9 3b 40 f9` | ldr x25,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00afdf3c"></a> `00afdf3c` | `ff 03 03 91` | add sp,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00afdf40"></a> `00afdf40` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00afdf44"></a> `00afdf44` | `f4 03 19 aa` | mov x20,x25 | `FALL_THROUGH`
<a id="insn-00afdf48"></a> `00afdf48` | `ae ff ff 17` | b 0x00afde00 | `UNCONDITIONAL_JUMP`
<a id="insn-00afdf4c"></a> `00afdf4c` | `11 74 03 94` | bl 0x00bdaf90 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afdcec`](#insn-00afdcec) 範囲 `[['00afdcec', '00afdcfb']]`
  - `FALL_THROUGH` [`00afdcf8`](#insn-00afdcf8) → [`00afdcfc`](#insn-00afdcfc)
- ブロック [`00afdcfc`](#insn-00afdcfc) 範囲 `[['00afdcfc', '00afdd07']]`
  - `FALL_THROUGH` [`00afdd04`](#insn-00afdd04) → [`00afdd08`](#insn-00afdd08)
- ブロック [`00afdd08`](#insn-00afdd08) 範囲 `[['00afdd08', '00afdd1f']]`
  - `FALL_THROUGH` [`00afdd1c`](#insn-00afdd1c) → [`00afdd20`](#insn-00afdd20)
- ブロック [`00afdd20`](#insn-00afdd20) 範囲 `[['00afdd20', '00afdd3f']]`
  - `CONDITIONAL_JUMP` [`00afdd3c`](#insn-00afdd3c) → [`00afddfc`](#insn-00afddfc)
  - `FALL_THROUGH` [`00afdd3c`](#insn-00afdd3c) → [`00afdd40`](#insn-00afdd40)
- ブロック [`00afdd40`](#insn-00afdd40) 範囲 `[['00afdd40', '00afdd4f']]`
  - `CONDITIONAL_JUMP` [`00afdd4c`](#insn-00afdd4c) → [`00afdd6c`](#insn-00afdd6c)
  - `FALL_THROUGH` [`00afdd4c`](#insn-00afdd4c) → [`00afdd50`](#insn-00afdd50)
- ブロック [`00afdd50`](#insn-00afdd50) 範囲 `[['00afdd50', '00afdd53']]`
  - `UNCONDITIONAL_JUMP` [`00afdd50`](#insn-00afdd50) → [`00afddf0`](#insn-00afddf0)
- ブロック [`00afdd54`](#insn-00afdd54) 範囲 `[['00afdd54', '00afdd63']]`
  - `CONDITIONAL_JUMP` [`00afdd60`](#insn-00afdd60) → [`00afdf44`](#insn-00afdf44)
  - `FALL_THROUGH` [`00afdd60`](#insn-00afdd60) → [`00afdd64`](#insn-00afdd64)
- ブロック [`00afdd64`](#insn-00afdd64) 範囲 `[['00afdd64', '00afdd6b']]`
  - `CONDITIONAL_JUMP` [`00afdd68`](#insn-00afdd68) → [`00afddf0`](#insn-00afddf0)
  - `FALL_THROUGH` [`00afdd68`](#insn-00afdd68) → [`00afdd6c`](#insn-00afdd6c)
- ブロック [`00afdd6c`](#insn-00afdd6c) 範囲 `[['00afdd6c', '00afdd9b']]`
  - `CONDITIONAL_JUMP` [`00afdd98`](#insn-00afdd98) → [`00afddf0`](#insn-00afddf0)
  - `FALL_THROUGH` [`00afdd98`](#insn-00afdd98) → [`00afdd9c`](#insn-00afdd9c)
- ブロック [`00afdd9c`](#insn-00afdd9c) 範囲 `[['00afdd9c', '00afddb7']]`
  - `CONDITIONAL_JUMP` [`00afddb4`](#insn-00afddb4) → [`00afdde4`](#insn-00afdde4)
  - `FALL_THROUGH` [`00afddb4`](#insn-00afddb4) → [`00afddb8`](#insn-00afddb8)
- ブロック [`00afddb8`](#insn-00afddb8) 範囲 `[['00afddb8', '00afddbb']]`
  - `CONDITIONAL_JUMP` [`00afddb8`](#insn-00afddb8) → [`00afdd54`](#insn-00afdd54)
  - `FALL_THROUGH` [`00afddb8`](#insn-00afddb8) → [`00afddbc`](#insn-00afddbc)
- ブロック [`00afddbc`](#insn-00afddbc) 範囲 `[['00afddbc', '00afddbf']]`
  - `FALL_THROUGH` [`00afddbc`](#insn-00afddbc) → [`00afddc0`](#insn-00afddc0)
- ブロック [`00afddc0`](#insn-00afddc0) 範囲 `[['00afddc0', '00afddd3']]`
  - `CONDITIONAL_JUMP` [`00afddd0`](#insn-00afddd0) → [`00afddf0`](#insn-00afddf0)
  - `FALL_THROUGH` [`00afddd0`](#insn-00afddd0) → [`00afddd4`](#insn-00afddd4)
- ブロック [`00afddd4`](#insn-00afddd4) 範囲 `[['00afddd4', '00afdddf']]`
  - `CONDITIONAL_JUMP` [`00afdddc`](#insn-00afdddc) → [`00afddc0`](#insn-00afddc0)
  - `FALL_THROUGH` [`00afdddc`](#insn-00afdddc) → [`00afdde0`](#insn-00afdde0)
- ブロック [`00afdde0`](#insn-00afdde0) 範囲 `[['00afdde0', '00afdde3']]`
  - `UNCONDITIONAL_JUMP` [`00afdde0`](#insn-00afdde0) → [`00afdd54`](#insn-00afdd54)
- ブロック [`00afdde4`](#insn-00afdde4) 範囲 `[['00afdde4', '00afdde7']]`
  - `CONDITIONAL_JUMP` [`00afdde4`](#insn-00afdde4) → [`00afdd54`](#insn-00afdd54)
  - `FALL_THROUGH` [`00afdde4`](#insn-00afdde4) → [`00afdde8`](#insn-00afdde8)
- ブロック [`00afdde8`](#insn-00afdde8) 範囲 `[['00afdde8', '00afddef']]`
  - `CONDITIONAL_JUMP` [`00afddec`](#insn-00afddec) → [`00afdd54`](#insn-00afdd54)
  - `FALL_THROUGH` [`00afddec`](#insn-00afddec) → [`00afddf0`](#insn-00afddf0)
- ブロック [`00afddf0`](#insn-00afddf0) 範囲 `[['00afddf0', '00afddf7']]`
  - `CONDITIONAL_JUMP` [`00afddf4`](#insn-00afddf4) → [`00afde78`](#insn-00afde78)
  - `FALL_THROUGH` [`00afddf4`](#insn-00afddf4) → [`00afddf8`](#insn-00afddf8)
- ブロック [`00afddf8`](#insn-00afddf8) 範囲 `[['00afddf8', '00afddfb']]`
  - `UNCONDITIONAL_JUMP` [`00afddf8`](#insn-00afddf8) → [`00afdec4`](#insn-00afdec4)
- ブロック [`00afddfc`](#insn-00afddfc) 範囲 `[['00afddfc', '00afddff']]`
  - `FALL_THROUGH` [`00afddfc`](#insn-00afddfc) → [`00afde00`](#insn-00afde00)
- ブロック [`00afde00`](#insn-00afde00) 範囲 `[['00afde00', '00afde67']]`
  - `CONDITIONAL_JUMP` [`00afde64`](#insn-00afde64) → [`00afde70`](#insn-00afde70)
  - `FALL_THROUGH` [`00afde64`](#insn-00afde64) → [`00afde68`](#insn-00afde68)
- ブロック [`00afde68`](#insn-00afde68) 範囲 `[['00afde68', '00afde6f']]`
  - `FALL_THROUGH` [`00afde6c`](#insn-00afde6c) → [`00afde70`](#insn-00afde70)
- ブロック [`00afde70`](#insn-00afde70) 範囲 `[['00afde70', '00afde77']]`
  - `CONDITIONAL_JUMP` [`00afde74`](#insn-00afde74) → [`00afdec4`](#insn-00afdec4)
  - `FALL_THROUGH` [`00afde74`](#insn-00afde74) → [`00afde78`](#insn-00afde78)
- ブロック [`00afde78`](#insn-00afde78) 範囲 `[['00afde78', '00afde83']]`
  - `CONDITIONAL_JUMP` [`00afde80`](#insn-00afde80) → [`00afdeb8`](#insn-00afdeb8)
  - `FALL_THROUGH` [`00afde80`](#insn-00afde80) → [`00afde84`](#insn-00afde84)
- ブロック [`00afde84`](#insn-00afde84) 範囲 `[['00afde84', '00afde8f']]`
  - `CONDITIONAL_JUMP` [`00afde8c`](#insn-00afde8c) → [`00afdea4`](#insn-00afdea4)
  - `FALL_THROUGH` [`00afde8c`](#insn-00afde8c) → [`00afde90`](#insn-00afde90)
- ブロック [`00afde90`](#insn-00afde90) 範囲 `[['00afde90', '00afde9b']]`
  - `CONDITIONAL_JUMP` [`00afde98`](#insn-00afde98) → [`00afdeb0`](#insn-00afdeb0)
  - `FALL_THROUGH` [`00afde98`](#insn-00afde98) → [`00afde9c`](#insn-00afde9c)
- ブロック [`00afde9c`](#insn-00afde9c) 範囲 `[['00afde9c', '00afdea3']]`
  - `CONDITIONAL_JUMP` [`00afdea0`](#insn-00afdea0) → [`00afde90`](#insn-00afde90)
  - `FALL_THROUGH` [`00afdea0`](#insn-00afdea0) → [`00afdea4`](#insn-00afdea4)
- ブロック [`00afdea4`](#insn-00afdea4) 範囲 `[['00afdea4', '00afdeaf']]`
  - `UNCONDITIONAL_JUMP` [`00afdeac`](#insn-00afdeac) → [`00afde90`](#insn-00afde90)
- ブロック [`00afdeb0`](#insn-00afdeb0) 範囲 `[['00afdeb0', '00afdeb7']]`
  - `UNCONDITIONAL_JUMP` [`00afdeb4`](#insn-00afdeb4) → [`00afdebc`](#insn-00afdebc)
- ブロック [`00afdeb8`](#insn-00afdeb8) 範囲 `[['00afdeb8', '00afdebb']]`
  - `FALL_THROUGH` [`00afdeb8`](#insn-00afdeb8) → [`00afdebc`](#insn-00afdebc)
- ブロック [`00afdebc`](#insn-00afdebc) 範囲 `[['00afdebc', '00afdec3']]`
  - `FALL_THROUGH` [`00afdec0`](#insn-00afdec0) → [`00afdec4`](#insn-00afdec4)
- ブロック [`00afdec4`](#insn-00afdec4) 範囲 `[['00afdec4', '00afdecb']]`
  - `CONDITIONAL_JUMP` [`00afdec8`](#insn-00afdec8) → [`00afdf18`](#insn-00afdf18)
  - `FALL_THROUGH` [`00afdec8`](#insn-00afdec8) → [`00afdecc`](#insn-00afdecc)
- ブロック [`00afdecc`](#insn-00afdecc) 範囲 `[['00afdecc', '00afded7']]`
  - `CONDITIONAL_JUMP` [`00afded4`](#insn-00afded4) → [`00afdf0c`](#insn-00afdf0c)
  - `FALL_THROUGH` [`00afded4`](#insn-00afded4) → [`00afded8`](#insn-00afded8)
- ブロック [`00afded8`](#insn-00afded8) 範囲 `[['00afded8', '00afdee3']]`
  - `CONDITIONAL_JUMP` [`00afdee0`](#insn-00afdee0) → [`00afdef8`](#insn-00afdef8)
  - `FALL_THROUGH` [`00afdee0`](#insn-00afdee0) → [`00afdee4`](#insn-00afdee4)
- ブロック [`00afdee4`](#insn-00afdee4) 範囲 `[['00afdee4', '00afdeef']]`
  - `CONDITIONAL_JUMP` [`00afdeec`](#insn-00afdeec) → [`00afdf04`](#insn-00afdf04)
  - `FALL_THROUGH` [`00afdeec`](#insn-00afdeec) → [`00afdef0`](#insn-00afdef0)
- ブロック [`00afdef0`](#insn-00afdef0) 範囲 `[['00afdef0', '00afdef7']]`
  - `CONDITIONAL_JUMP` [`00afdef4`](#insn-00afdef4) → [`00afdee4`](#insn-00afdee4)
  - `FALL_THROUGH` [`00afdef4`](#insn-00afdef4) → [`00afdef8`](#insn-00afdef8)
- ブロック [`00afdef8`](#insn-00afdef8) 範囲 `[['00afdef8', '00afdf03']]`
  - `UNCONDITIONAL_JUMP` [`00afdf00`](#insn-00afdf00) → [`00afdee4`](#insn-00afdee4)
- ブロック [`00afdf04`](#insn-00afdf04) 範囲 `[['00afdf04', '00afdf0b']]`
  - `UNCONDITIONAL_JUMP` [`00afdf08`](#insn-00afdf08) → [`00afdf10`](#insn-00afdf10)
- ブロック [`00afdf0c`](#insn-00afdf0c) 範囲 `[['00afdf0c', '00afdf0f']]`
  - `FALL_THROUGH` [`00afdf0c`](#insn-00afdf0c) → [`00afdf10`](#insn-00afdf10)
- ブロック [`00afdf10`](#insn-00afdf10) 範囲 `[['00afdf10', '00afdf17']]`
  - `FALL_THROUGH` [`00afdf14`](#insn-00afdf14) → [`00afdf18`](#insn-00afdf18)
- ブロック [`00afdf18`](#insn-00afdf18) 範囲 `[['00afdf18', '00afdf27']]`
  - `CONDITIONAL_JUMP` [`00afdf24`](#insn-00afdf24) → [`00afdf4c`](#insn-00afdf4c)
  - `FALL_THROUGH` [`00afdf24`](#insn-00afdf24) → [`00afdf28`](#insn-00afdf28)
- ブロック [`00afdf28`](#insn-00afdf28) 範囲 `[['00afdf28', '00afdf43']]`
- ブロック [`00afdf44`](#insn-00afdf44) 範囲 `[['00afdf44', '00afdf4b']]`
  - `UNCONDITIONAL_JUMP` [`00afdf48`](#insn-00afdf48) → [`00afde00`](#insn-00afde00)
- ブロック [`00afdf4c`](#insn-00afdf4c) 範囲 `[['00afdf4c', '00afdf4f']]`

## 命令位置別の参照

- [`00afdcf0`](#insn-00afdcf0) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdcf4`](#insn-00afdcf4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdcf8`](#insn-00afdcf8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdcfc`](#insn-00afdcfc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdd00`](#insn-00afdd00) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdd18`](#insn-00afdd18) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdd20`](#insn-00afdd20) → [`00bdec40`](../00bde/00bdec40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdec40` · 推定シンボル `None` · 推定型 `None`
- [`00afdd2c`](#insn-00afdd2c) → [`00bdec40`](../00bde/00bdec40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdec40` · 推定シンボル `None` · 推定型 `None`
- [`00afdd30`](#insn-00afdd30) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdd34`](#insn-00afdd34) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdd3c`](#insn-00afdd3c) → [`00afddfc`](#insn-00afddfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdd40`](#insn-00afdd40) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdd4c`](#insn-00afdd4c) → [`00afdd6c`](#insn-00afdd6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdd50`](#insn-00afdd50) → [`00afddf0`](#insn-00afddf0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdd60`](#insn-00afdd60) → [`00afdf44`](#insn-00afdf44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdd68`](#insn-00afdd68) → [`00afddf0`](#insn-00afddf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdd98`](#insn-00afdd98) → [`00afddf0`](#insn-00afddf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afddb4`](#insn-00afddb4) → [`00afdde4`](#insn-00afdde4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afddb8`](#insn-00afddb8) → [`00afdd54`](#insn-00afdd54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afddd0`](#insn-00afddd0) → [`00afddf0`](#insn-00afddf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdddc`](#insn-00afdddc) → [`00afddc0`](#insn-00afddc0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdde0`](#insn-00afdde0) → [`00afdd54`](#insn-00afdd54) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdde4`](#insn-00afdde4) → [`00afdd54`](#insn-00afdd54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdde8`](#insn-00afdde8) → [`00bdb100`](../00bdb/00bdb100.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb100` · 推定シンボル `None` · 推定型 `None`
- [`00afddec`](#insn-00afddec) → [`00afdd54`](#insn-00afdd54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afddf4`](#insn-00afddf4) → [`00afde78`](#insn-00afde78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afddf8`](#insn-00afddf8) → [`00afdec4`](#insn-00afdec4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afddfc`](#insn-00afddfc) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afde10`](#insn-00afde10) → [`00afd1a0`](00afd1a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00afd1a0` · 推定シンボル `None` · 推定型 `None`
- [`00afde14`](#insn-00afde14) → `Stack[-0xb8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afde18`](#insn-00afde18) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afde34`](#insn-00afde34) → `Stack[-0x98]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afde38`](#insn-00afde38) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afde3c`](#insn-00afde3c) → [`00bde130`](../00bde/00bde130.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde130` · 推定シンボル `None` · 推定型 `None`
- [`00afde40`](#insn-00afde40) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afde44`](#insn-00afde44) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afde48`](#insn-00afde48) → `Stack[-0xb8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afde50`](#insn-00afde50) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afde60`](#insn-00afde60) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afde64`](#insn-00afde64) → [`00afde70`](#insn-00afde70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afde68`](#insn-00afde68) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afde6c`](#insn-00afde6c) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00afde70`](#insn-00afde70) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afde74`](#insn-00afde74) → [`00afdec4`](#insn-00afdec4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afde78`](#insn-00afde78) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afde80`](#insn-00afde80) → [`00afdeb8`](#insn-00afdeb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afde8c`](#insn-00afde8c) → [`00afdea4`](#insn-00afdea4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afde98`](#insn-00afde98) → [`00afdeb0`](#insn-00afdeb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdea0`](#insn-00afdea0) → [`00afde90`](#insn-00afde90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdea8`](#insn-00afdea8) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00afdeac`](#insn-00afdeac) → [`00afde90`](#insn-00afde90) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdeb0`](#insn-00afdeb0) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdeb4`](#insn-00afdeb4) → [`00afdebc`](#insn-00afdebc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdebc`](#insn-00afdebc) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdec0`](#insn-00afdec0) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00afdec4`](#insn-00afdec4) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdec8`](#insn-00afdec8) → [`00afdf18`](#insn-00afdf18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdecc`](#insn-00afdecc) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afded4`](#insn-00afded4) → [`00afdf0c`](#insn-00afdf0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdee0`](#insn-00afdee0) → [`00afdef8`](#insn-00afdef8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdeec`](#insn-00afdeec) → [`00afdf04`](#insn-00afdf04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdef4`](#insn-00afdef4) → [`00afdee4`](#insn-00afdee4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdefc`](#insn-00afdefc) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00afdf00`](#insn-00afdf00) → [`00afdee4`](#insn-00afdee4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdf04`](#insn-00afdf04) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdf08`](#insn-00afdf08) → [`00afdf10`](#insn-00afdf10) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdf10`](#insn-00afdf10) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdf14`](#insn-00afdf14) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00afdf1c`](#insn-00afdf1c) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdf24`](#insn-00afdf24) → [`00afdf4c`](#insn-00afdf4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdf28`](#insn-00afdf28) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdf2c`](#insn-00afdf2c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdf30`](#insn-00afdf30) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdf34`](#insn-00afdf34) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdf38`](#insn-00afdf38) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdf48`](#insn-00afdf48) → [`00afde00`](#insn-00afde00) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdf4c`](#insn-00afdf4c) → [`00bdaf90`](../00bda/00bdaf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf90` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afdcf0`](#insn-00afdcf0)

~~~json
{
  "source": "00afdcf0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdcf4`](#insn-00afdcf4)

~~~json
{
  "source": "00afdcf4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdcf8`](#insn-00afdcf8)

~~~json
{
  "source": "00afdcf8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdcfc`](#insn-00afdcfc)

~~~json
{
  "source": "00afdcfc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdd00`](#insn-00afdd00)

~~~json
{
  "source": "00afdd00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdd18`](#insn-00afdd18)

~~~json
{
  "source": "00afdd18",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdd20`](#insn-00afdd20)

~~~json
{
  "source": "00afdd20",
  "target": "00bdec40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afdd2c`](#insn-00afdd2c)

~~~json
{
  "source": "00afdd2c",
  "target": "00bdec40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afdd30`](#insn-00afdd30)

~~~json
{
  "source": "00afdd30",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdd34`](#insn-00afdd34)

~~~json
{
  "source": "00afdd34",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdd3c`](#insn-00afdd3c)

~~~json
{
  "source": "00afdd3c",
  "target": "00afddfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdd40`](#insn-00afdd40)

~~~json
{
  "source": "00afdd40",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdd4c`](#insn-00afdd4c)

~~~json
{
  "source": "00afdd4c",
  "target": "00afdd6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdd50`](#insn-00afdd50)

~~~json
{
  "source": "00afdd50",
  "target": "00afddf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdd60`](#insn-00afdd60)

~~~json
{
  "source": "00afdd60",
  "target": "00afdf44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdd68`](#insn-00afdd68)

~~~json
{
  "source": "00afdd68",
  "target": "00afddf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdd98`](#insn-00afdd98)

~~~json
{
  "source": "00afdd98",
  "target": "00afddf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afddb4`](#insn-00afddb4)

~~~json
{
  "source": "00afddb4",
  "target": "00afdde4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afddb8`](#insn-00afddb8)

~~~json
{
  "source": "00afddb8",
  "target": "00afdd54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afddd0`](#insn-00afddd0)

~~~json
{
  "source": "00afddd0",
  "target": "00afddf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdddc`](#insn-00afdddc)

~~~json
{
  "source": "00afdddc",
  "target": "00afddc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdde0`](#insn-00afdde0)

~~~json
{
  "source": "00afdde0",
  "target": "00afdd54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdde4`](#insn-00afdde4)

~~~json
{
  "source": "00afdde4",
  "target": "00afdd54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdde8`](#insn-00afdde8)

~~~json
{
  "source": "00afdde8",
  "target": "00bdb100",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afddec`](#insn-00afddec)

~~~json
{
  "source": "00afddec",
  "target": "00afdd54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afddf4`](#insn-00afddf4)

~~~json
{
  "source": "00afddf4",
  "target": "00afde78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afddf8`](#insn-00afddf8)

~~~json
{
  "source": "00afddf8",
  "target": "00afdec4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afddfc`](#insn-00afddfc)

~~~json
{
  "source": "00afddfc",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afde10`](#insn-00afde10)

~~~json
{
  "source": "00afde10",
  "target": "00afd1a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afde14`](#insn-00afde14)

~~~json
{
  "source": "00afde14",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afde18`](#insn-00afde18)

~~~json
{
  "source": "00afde18",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afde34`](#insn-00afde34)

~~~json
{
  "source": "00afde34",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afde38`](#insn-00afde38)

~~~json
{
  "source": "00afde38",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afde3c`](#insn-00afde3c)

~~~json
{
  "source": "00afde3c",
  "target": "00bde130",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afde40`](#insn-00afde40)

~~~json
{
  "source": "00afde40",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afde44`](#insn-00afde44)

~~~json
{
  "source": "00afde44",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afde48`](#insn-00afde48)

~~~json
{
  "source": "00afde48",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afde50`](#insn-00afde50)

~~~json
{
  "source": "00afde50",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afde60`](#insn-00afde60)

~~~json
{
  "source": "00afde60",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afde64`](#insn-00afde64)

~~~json
{
  "source": "00afde64",
  "target": "00afde70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afde68`](#insn-00afde68)

~~~json
{
  "source": "00afde68",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afde6c`](#insn-00afde6c)

~~~json
{
  "source": "00afde6c",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afde70`](#insn-00afde70)

~~~json
{
  "source": "00afde70",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afde74`](#insn-00afde74)

~~~json
{
  "source": "00afde74",
  "target": "00afdec4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afde78`](#insn-00afde78)

~~~json
{
  "source": "00afde78",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afde80`](#insn-00afde80)

~~~json
{
  "source": "00afde80",
  "target": "00afdeb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afde8c`](#insn-00afde8c)

~~~json
{
  "source": "00afde8c",
  "target": "00afdea4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afde98`](#insn-00afde98)

~~~json
{
  "source": "00afde98",
  "target": "00afdeb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdea0`](#insn-00afdea0)

~~~json
{
  "source": "00afdea0",
  "target": "00afde90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdea8`](#insn-00afdea8)

~~~json
{
  "source": "00afdea8",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afdeac`](#insn-00afdeac)

~~~json
{
  "source": "00afdeac",
  "target": "00afde90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdeb0`](#insn-00afdeb0)

~~~json
{
  "source": "00afdeb0",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdeb4`](#insn-00afdeb4)

~~~json
{
  "source": "00afdeb4",
  "target": "00afdebc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdebc`](#insn-00afdebc)

~~~json
{
  "source": "00afdebc",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdec0`](#insn-00afdec0)

~~~json
{
  "source": "00afdec0",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afdec4`](#insn-00afdec4)

~~~json
{
  "source": "00afdec4",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdec8`](#insn-00afdec8)

~~~json
{
  "source": "00afdec8",
  "target": "00afdf18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdecc`](#insn-00afdecc)

~~~json
{
  "source": "00afdecc",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afded4`](#insn-00afded4)

~~~json
{
  "source": "00afded4",
  "target": "00afdf0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdee0`](#insn-00afdee0)

~~~json
{
  "source": "00afdee0",
  "target": "00afdef8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdeec`](#insn-00afdeec)

~~~json
{
  "source": "00afdeec",
  "target": "00afdf04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdef4`](#insn-00afdef4)

~~~json
{
  "source": "00afdef4",
  "target": "00afdee4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdefc`](#insn-00afdefc)

~~~json
{
  "source": "00afdefc",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afdf00`](#insn-00afdf00)

~~~json
{
  "source": "00afdf00",
  "target": "00afdee4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdf04`](#insn-00afdf04)

~~~json
{
  "source": "00afdf04",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdf08`](#insn-00afdf08)

~~~json
{
  "source": "00afdf08",
  "target": "00afdf10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdf10`](#insn-00afdf10)

~~~json
{
  "source": "00afdf10",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdf14`](#insn-00afdf14)

~~~json
{
  "source": "00afdf14",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afdf1c`](#insn-00afdf1c)

~~~json
{
  "source": "00afdf1c",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdf24`](#insn-00afdf24)

~~~json
{
  "source": "00afdf24",
  "target": "00afdf4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdf28`](#insn-00afdf28)

~~~json
{
  "source": "00afdf28",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdf2c`](#insn-00afdf2c)

~~~json
{
  "source": "00afdf2c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdf30`](#insn-00afdf30)

~~~json
{
  "source": "00afdf30",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdf34`](#insn-00afdf34)

~~~json
{
  "source": "00afdf34",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdf38`](#insn-00afdf38)

~~~json
{
  "source": "00afdf38",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdf48`](#insn-00afdf48)

~~~json
{
  "source": "00afdf48",
  "target": "00afde00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdf4c`](#insn-00afdf4c)

~~~json
{
  "source": "00afdf4c",
  "target": "00bdaf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
