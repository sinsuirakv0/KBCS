# 00afddf8

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00afddb4`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afddb4.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0008.md#compare-481345d1ee4aeec1907f4c3b8703ffed)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b5db7c`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5d/00b5db7c.md) · 移動量 `+0x5fd84`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/inspection-0018.md#compare-68966228caecc139903baa3de95d0173)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afddf8",
  "name": "_ZN8firebase4Path11GetRelativeERKS0_S2_",
  "size": 612,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "edc168672f43c5a0b06824bbe30d7e0b8bb0a164ed8439db4db17ff11d9130a3",
  "source_text_sha256": "edc168672f43c5a0b06824bbe30d7e0b8bb0a164ed8439db4db17ff11d9130a3",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afddf8",
        "00afe05b"
      ]
    ],
    "bytes_sha256": "a20e9b709462685531bc793f12793ebdc4bd5769f04d47ca107ad40850bb537c",
    "instruction_count": 153,
    "instruction_bytes": 612,
    "body_bytes": 612,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bded20](../00bde/00bded20.md)

## 呼び出し先

- [00afd2ac](../00afd/00afd2ac.md)
- [00bdb060](../00bdb/00bdb060.md)
- [00bdb090](../00bdb/00bdb090.md)
- [00bdb200](../00bdb/00bdb200.md)
- [00bde230](../00bde/00bde230.md)
- [00bded40](../00bde/00bded40.md)

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
      FUN_00afd2ac(local_b8,pbVar2,pbVar11);
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
joined_r0x00afdf80:
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
LAB_00afdefc:
      *(undefined1 *)(param_1 + 3) = 0;
      pbVar1 = local_88;
      goto joined_r0x00afdf80;
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
    if (__n != sVar3) goto LAB_00afdefc;
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
          if (pbVar1[uVar14 + 1] != __s2[uVar14]) goto LAB_00afdefc;
          uVar14 = uVar14 + 1;
        } while (bVar4 >> 1 != uVar14);
      }
    }
    else if ((__n != 0) && (iVar13 = memcmp(__s1,__s2,__n), iVar13 != 0)) goto LAB_00afdefc;
    pbVar1 = pbVar1 + 0x18;
    pbVar2 = pbVar2 + 0x18;
  } while( true );
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afddf8"></a> `00afddf8` | `ff 03 03 d1` | sub sp,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00afddfc"></a> `00afddfc` | `f9 3b 00 f9` | str x25,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00afde00"></a> `00afde00` | `f8 5f 08 a9` | stp x24,x23,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00afde04"></a> `00afde04` | `f6 57 09 a9` | stp x22,x21,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00afde08"></a> `00afde08` | `f4 4f 0a a9` | stp x20,x19,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00afde0c"></a> `00afde0c` | `fd 7b 0b a9` | stp x29,x30,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00afde10"></a> `00afde10` | `fd c3 02 91` | add x29,sp,#0xb0 | `FALL_THROUGH`
<a id="insn-00afde14"></a> `00afde14` | `56 d0 3b d5` | mrs x22,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00afde18"></a> `00afde18` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00afde1c"></a> `00afde1c` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00afde20"></a> `00afde20` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00afde24"></a> `00afde24` | `a8 83 1b f8` | stur x8,[x29, #-0x48] | `FALL_THROUGH`
<a id="insn-00afde28"></a> `00afde28` | `e8 43 01 91` | add x8,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00afde2c"></a> `00afde2c` | `c5 83 03 94` | bl 0x00bded40 | `UNCONDITIONAL_CALL`
<a id="insn-00afde30"></a> `00afde30` | `e8 e3 00 91` | add x8,sp,#0x38 | `FALL_THROUGH`
<a id="insn-00afde34"></a> `00afde34` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00afde38"></a> `00afde38` | `c2 83 03 94` | bl 0x00bded40 | `UNCONDITIONAL_CALL`
<a id="insn-00afde3c"></a> `00afde3c` | `f8 5f 45 a9` | ldp x24,x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00afde40"></a> `00afde40` | `f4 1f 40 f9` | ldr x20,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00afde44"></a> `00afde44` | `1f 03 17 eb` | cmp x24,x23 | `FALL_THROUGH`
<a id="insn-00afde48"></a> `00afde48` | `00 06 00 54` | b.eq 0x00afdf08 | `CONDITIONAL_JUMP`
<a id="insn-00afde4c"></a> `00afde4c` | `f5 23 40 f9` | ldr x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00afde50"></a> `00afde50` | `f9 03 14 aa` | mov x25,x20 | `FALL_THROUGH`
<a id="insn-00afde54"></a> `00afde54` | `bf 02 19 eb` | cmp x21,x25 | `FALL_THROUGH`
<a id="insn-00afde58"></a> `00afde58` | `01 01 00 54` | b.ne 0x00afde78 | `CONDITIONAL_JUMP`
<a id="insn-00afde5c"></a> `00afde5c` | `28 00 00 14` | b 0x00afdefc | `UNCONDITIONAL_JUMP`
<a id="insn-00afde60"></a> `00afde60` | `18 63 00 91` | add x24,x24,#0x18 | `FALL_THROUGH`
<a id="insn-00afde64"></a> `00afde64` | `1f 03 17 eb` | cmp x24,x23 | `FALL_THROUGH`
<a id="insn-00afde68"></a> `00afde68` | `39 63 00 91` | add x25,x25,#0x18 | `FALL_THROUGH`
<a id="insn-00afde6c"></a> `00afde6c` | `20 0f 00 54` | b.eq 0x00afe050 | `CONDITIONAL_JUMP`
<a id="insn-00afde70"></a> `00afde70` | `bf 02 19 eb` | cmp x21,x25 | `FALL_THROUGH`
<a id="insn-00afde74"></a> `00afde74` | `40 04 00 54` | b.eq 0x00afdefc | `CONDITIONAL_JUMP`
<a id="insn-00afde78"></a> `00afde78` | `09 03 40 39` | ldrb w9,[x24] | `FALL_THROUGH`
<a id="insn-00afde7c"></a> `00afde7c` | `0b 07 40 f9` | ldr x11,[x24, #0x8] | `FALL_THROUGH`
<a id="insn-00afde80"></a> `00afde80` | `2a 03 40 39` | ldrb w10,[x25] | `FALL_THROUGH`
<a id="insn-00afde84"></a> `00afde84` | `2c 07 40 f9` | ldr x12,[x25, #0x8] | `FALL_THROUGH`
<a id="insn-00afde88"></a> `00afde88` | `28 fd 41 d3` | lsr x8,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00afde8c"></a> `00afde8c` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00afde90"></a> `00afde90` | `4d fd 41 d3` | lsr x13,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00afde94"></a> `00afde94` | `02 01 8b 9a` | csel x2,x8,x11,eq | `FALL_THROUGH`
<a id="insn-00afde98"></a> `00afde98` | `5f 01 00 72` | tst w10,#0x1 | `FALL_THROUGH`
<a id="insn-00afde9c"></a> `00afde9c` | `ab 01 8c 9a` | csel x11,x13,x12,eq | `FALL_THROUGH`
<a id="insn-00afdea0"></a> `00afdea0` | `5f 00 0b eb` | cmp x2,x11 | `FALL_THROUGH`
<a id="insn-00afdea4"></a> `00afdea4` | `c1 02 00 54` | b.ne 0x00afdefc | `CONDITIONAL_JUMP`
<a id="insn-00afdea8"></a> `00afdea8` | `0b 0b 40 f9` | ldr x11,[x24, #0x10] | `FALL_THROUGH`
<a id="insn-00afdeac"></a> `00afdeac` | `2c 0b 40 f9` | ldr x12,[x25, #0x10] | `FALL_THROUGH`
<a id="insn-00afdeb0"></a> `00afdeb0` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00afdeb4"></a> `00afdeb4` | `60 15 98 9a` | csinc x0,x11,x24,ne | `FALL_THROUGH`
<a id="insn-00afdeb8"></a> `00afdeb8` | `5f 01 00 72` | tst w10,#0x1 | `FALL_THROUGH`
<a id="insn-00afdebc"></a> `00afdebc` | `81 15 99 9a` | csinc x1,x12,x25,ne | `FALL_THROUGH`
<a id="insn-00afdec0"></a> `00afdec0` | `89 01 00 37` | tbnz w9,#0x0,0x00afdef0 | `CONDITIONAL_JUMP`
<a id="insn-00afdec4"></a> `00afdec4` | `e2 fc ff b4` | cbz x2,0x00afde60 | `CONDITIONAL_JUMP`
<a id="insn-00afdec8"></a> `00afdec8` | `e9 03 1f aa` | mov x9,xzr | `FALL_THROUGH`
<a id="insn-00afdecc"></a> `00afdecc` | `0a 03 09 8b` | add x10,x24,x9 | `FALL_THROUGH`
<a id="insn-00afded0"></a> `00afded0` | `4a 05 40 39` | ldrb w10,[x10, #0x1] | `FALL_THROUGH`
<a id="insn-00afded4"></a> `00afded4` | `2b 68 69 38` | ldrb w11,[x1, x9, LSL ] | `FALL_THROUGH`
<a id="insn-00afded8"></a> `00afded8` | `5f 01 0b 6b` | cmp w10,w11 | `FALL_THROUGH`
<a id="insn-00afdedc"></a> `00afdedc` | `01 01 00 54` | b.ne 0x00afdefc | `CONDITIONAL_JUMP`
<a id="insn-00afdee0"></a> `00afdee0` | `29 05 00 91` | add x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00afdee4"></a> `00afdee4` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00afdee8"></a> `00afdee8` | `21 ff ff 54` | b.ne 0x00afdecc | `CONDITIONAL_JUMP`
<a id="insn-00afdeec"></a> `00afdeec` | `dd ff ff 17` | b 0x00afde60 | `UNCONDITIONAL_JUMP`
<a id="insn-00afdef0"></a> `00afdef0` | `82 fb ff b4` | cbz x2,0x00afde60 | `CONDITIONAL_JUMP`
<a id="insn-00afdef4"></a> `00afdef4` | `c3 74 03 94` | bl 0x00bdb200 | `UNCONDITIONAL_CALL`
<a id="insn-00afdef8"></a> `00afdef8` | `40 fb ff 34` | cbz w0,0x00afde60 | `CONDITIONAL_JUMP`
<a id="insn-00afdefc"></a> `00afdefc` | `7f 62 00 39` | strb wzr,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00afdf00"></a> `00afdf00` | `34 04 00 b5` | cbnz x20,0x00afdf84 | `CONDITIONAL_JUMP`
<a id="insn-00afdf04"></a> `00afdf04` | `33 00 00 14` | b 0x00afdfd0 | `UNCONDITIONAL_JUMP`
<a id="insn-00afdf08"></a> `00afdf08` | `f5 23 40 f9` | ldr x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00afdf0c"></a> `00afdf0c` | `e8 23 00 91` | add x8,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00afdf10"></a> `00afdf10` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00afdf14"></a> `00afdf14` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00afdf18"></a> `00afdf18` | `f7 23 00 91` | add x23,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00afdf1c"></a> `00afdf1c` | `e4 fc ff 97` | bl 0x00afd2ac | `UNCONDITIONAL_CALL`
<a id="insn-00afdf20"></a> `00afdf20` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00afdf24"></a> `00afdf24` | `ea 27 41 a9` | ldp x10,x9,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afdf28"></a> `00afdf28` | `eb 02 40 b2` | orr x11,x23,#0x1 | `FALL_THROUGH`
<a id="insn-00afdf2c"></a> `00afdf2c` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00afdf30"></a> `00afdf30` | `0c fd 41 d3` | lsr x12,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00afdf34"></a> `00afdf34` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00afdf38"></a> `00afdf38` | `61 01 89 9a` | csel x1,x11,x9,eq | `FALL_THROUGH`
<a id="insn-00afdf3c"></a> `00afdf3c` | `82 01 8a 9a` | csel x2,x12,x10,eq | `FALL_THROUGH`
<a id="insn-00afdf40"></a> `00afdf40` | `ff ff 02 a9` | stp xzr,xzr,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00afdf44"></a> `00afdf44` | `ff 13 00 f9` | str xzr,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afdf48"></a> `00afdf48` | `ba 80 03 94` | bl 0x00bde230 | `UNCONDITIONAL_CALL`
<a id="insn-00afdf4c"></a> `00afdf4c` | `e0 0b c0 3d` | ldr q0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afdf50"></a> `00afdf50` | `e9 1b 40 f9` | ldr x9,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00afdf54"></a> `00afdf54` | `ea 23 40 39` | ldrb w10,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00afdf58"></a> `00afdf58` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00afdf5c"></a> `00afdf5c` | `ff 7f 02 a9` | stp xzr,xzr,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afdf60"></a> `00afdf60` | `68 62 00 39` | strb w8,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00afdf64"></a> `00afdf64` | `69 0a 00 f9` | str x9,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00afdf68"></a> `00afdf68` | `60 02 80 3d` | str q0,[x19] | `FALL_THROUGH`
<a id="insn-00afdf6c"></a> `00afdf6c` | `ff 1b 00 f9` | str xzr,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00afdf70"></a> `00afdf70` | `6a 00 00 36` | tbz w10,#0x0,0x00afdf7c | `CONDITIONAL_JUMP`
<a id="insn-00afdf74"></a> `00afdf74` | `e0 0f 40 f9` | ldr x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00afdf78"></a> `00afdf78` | `3a 74 03 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00afdf7c"></a> `00afdf7c` | `f4 1f 40 f9` | ldr x20,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00afdf80"></a> `00afdf80` | `94 02 00 b4` | cbz x20,0x00afdfd0 | `CONDITIONAL_JUMP`
<a id="insn-00afdf84"></a> `00afdf84` | `e8 23 40 f9` | ldr x8,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00afdf88"></a> `00afdf88` | `1f 01 14 eb` | cmp x8,x20 | `FALL_THROUGH`
<a id="insn-00afdf8c"></a> `00afdf8c` | `c0 01 00 54` | b.eq 0x00afdfc4 | `CONDITIONAL_JUMP`
<a id="insn-00afdf90"></a> `00afdf90` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00afdf94"></a> `00afdf94` | `69 8e 5e 38` | ldrb w9,[x19, #-0x18]! | `FALL_THROUGH`
<a id="insn-00afdf98"></a> `00afdf98` | `c9 00 00 37` | tbnz w9,#0x0,0x00afdfb0 | `CONDITIONAL_JUMP`
<a id="insn-00afdf9c"></a> `00afdf9c` | `9f 02 13 eb` | cmp x20,x19 | `FALL_THROUGH`
<a id="insn-00afdfa0"></a> `00afdfa0` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-00afdfa4"></a> `00afdfa4` | `c0 00 00 54` | b.eq 0x00afdfbc | `CONDITIONAL_JUMP`
<a id="insn-00afdfa8"></a> `00afdfa8` | `69 8e 5e 38` | ldrb w9,[x19, #-0x18]! | `FALL_THROUGH`
<a id="insn-00afdfac"></a> `00afdfac` | `89 ff 07 36` | tbz w9,#0x0,0x00afdf9c | `CONDITIONAL_JUMP`
<a id="insn-00afdfb0"></a> `00afdfb0` | `00 81 5f f8` | ldur x0,[x8, #-0x8] | `FALL_THROUGH`
<a id="insn-00afdfb4"></a> `00afdfb4` | `2b 74 03 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00afdfb8"></a> `00afdfb8` | `f9 ff ff 17` | b 0x00afdf9c | `UNCONDITIONAL_JUMP`
<a id="insn-00afdfbc"></a> `00afdfbc` | `e0 1f 40 f9` | ldr x0,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00afdfc0"></a> `00afdfc0` | `02 00 00 14` | b 0x00afdfc8 | `UNCONDITIONAL_JUMP`
<a id="insn-00afdfc4"></a> `00afdfc4` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00afdfc8"></a> `00afdfc8` | `f4 23 00 f9` | str x20,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00afdfcc"></a> `00afdfcc` | `25 74 03 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00afdfd0"></a> `00afdfd0` | `f3 2b 40 f9` | ldr x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00afdfd4"></a> `00afdfd4` | `93 02 00 b4` | cbz x19,0x00afe024 | `CONDITIONAL_JUMP`
<a id="insn-00afdfd8"></a> `00afdfd8` | `e8 2f 40 f9` | ldr x8,[sp, #0x58] | `FALL_THROUGH`
<a id="insn-00afdfdc"></a> `00afdfdc` | `1f 01 13 eb` | cmp x8,x19 | `FALL_THROUGH`
<a id="insn-00afdfe0"></a> `00afdfe0` | `c0 01 00 54` | b.eq 0x00afe018 | `CONDITIONAL_JUMP`
<a id="insn-00afdfe4"></a> `00afdfe4` | `f4 03 08 aa` | mov x20,x8 | `FALL_THROUGH`
<a id="insn-00afdfe8"></a> `00afdfe8` | `89 8e 5e 38` | ldrb w9,[x20, #-0x18]! | `FALL_THROUGH`
<a id="insn-00afdfec"></a> `00afdfec` | `c9 00 00 37` | tbnz w9,#0x0,0x00afe004 | `CONDITIONAL_JUMP`
<a id="insn-00afdff0"></a> `00afdff0` | `7f 02 14 eb` | cmp x19,x20 | `FALL_THROUGH`
<a id="insn-00afdff4"></a> `00afdff4` | `e8 03 14 aa` | mov x8,x20 | `FALL_THROUGH`
<a id="insn-00afdff8"></a> `00afdff8` | `c0 00 00 54` | b.eq 0x00afe010 | `CONDITIONAL_JUMP`
<a id="insn-00afdffc"></a> `00afdffc` | `89 8e 5e 38` | ldrb w9,[x20, #-0x18]! | `FALL_THROUGH`
<a id="insn-00afe000"></a> `00afe000` | `89 ff 07 36` | tbz w9,#0x0,0x00afdff0 | `CONDITIONAL_JUMP`
<a id="insn-00afe004"></a> `00afe004` | `00 81 5f f8` | ldur x0,[x8, #-0x8] | `FALL_THROUGH`
<a id="insn-00afe008"></a> `00afe008` | `16 74 03 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00afe00c"></a> `00afe00c` | `f9 ff ff 17` | b 0x00afdff0 | `UNCONDITIONAL_JUMP`
<a id="insn-00afe010"></a> `00afe010` | `e0 2b 40 f9` | ldr x0,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00afe014"></a> `00afe014` | `02 00 00 14` | b 0x00afe01c | `UNCONDITIONAL_JUMP`
<a id="insn-00afe018"></a> `00afe018` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00afe01c"></a> `00afe01c` | `f3 2f 00 f9` | str x19,[sp, #0x58] | `FALL_THROUGH`
<a id="insn-00afe020"></a> `00afe020` | `10 74 03 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00afe024"></a> `00afe024` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00afe028"></a> `00afe028` | `a9 83 5b f8` | ldur x9,[x29, #-0x48] | `FALL_THROUGH`
<a id="insn-00afe02c"></a> `00afe02c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00afe030"></a> `00afe030` | `41 01 00 54` | b.ne 0x00afe058 | `CONDITIONAL_JUMP`
<a id="insn-00afe034"></a> `00afe034` | `fd 7b 4b a9` | ldp x29,x30,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00afe038"></a> `00afe038` | `f4 4f 4a a9` | ldp x20,x19,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00afe03c"></a> `00afe03c` | `f6 57 49 a9` | ldp x22,x21,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00afe040"></a> `00afe040` | `f8 5f 48 a9` | ldp x24,x23,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00afe044"></a> `00afe044` | `f9 3b 40 f9` | ldr x25,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00afe048"></a> `00afe048` | `ff 03 03 91` | add sp,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00afe04c"></a> `00afe04c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00afe050"></a> `00afe050` | `f4 03 19 aa` | mov x20,x25 | `FALL_THROUGH`
<a id="insn-00afe054"></a> `00afe054` | `ae ff ff 17` | b 0x00afdf0c | `UNCONDITIONAL_JUMP`
<a id="insn-00afe058"></a> `00afe058` | `0e 74 03 94` | bl 0x00bdb090 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afddf8`](#insn-00afddf8) 範囲 `[['00afddf8', '00afde4b']]`
  - `CONDITIONAL_JUMP` [`00afde48`](#insn-00afde48) → [`00afdf08`](#insn-00afdf08)
  - `FALL_THROUGH` [`00afde48`](#insn-00afde48) → [`00afde4c`](#insn-00afde4c)
- ブロック [`00afde4c`](#insn-00afde4c) 範囲 `[['00afde4c', '00afde5b']]`
  - `CONDITIONAL_JUMP` [`00afde58`](#insn-00afde58) → [`00afde78`](#insn-00afde78)
  - `FALL_THROUGH` [`00afde58`](#insn-00afde58) → [`00afde5c`](#insn-00afde5c)
- ブロック [`00afde5c`](#insn-00afde5c) 範囲 `[['00afde5c', '00afde5f']]`
  - `UNCONDITIONAL_JUMP` [`00afde5c`](#insn-00afde5c) → [`00afdefc`](#insn-00afdefc)
- ブロック [`00afde60`](#insn-00afde60) 範囲 `[['00afde60', '00afde6f']]`
  - `CONDITIONAL_JUMP` [`00afde6c`](#insn-00afde6c) → [`00afe050`](#insn-00afe050)
  - `FALL_THROUGH` [`00afde6c`](#insn-00afde6c) → [`00afde70`](#insn-00afde70)
- ブロック [`00afde70`](#insn-00afde70) 範囲 `[['00afde70', '00afde77']]`
  - `CONDITIONAL_JUMP` [`00afde74`](#insn-00afde74) → [`00afdefc`](#insn-00afdefc)
  - `FALL_THROUGH` [`00afde74`](#insn-00afde74) → [`00afde78`](#insn-00afde78)
- ブロック [`00afde78`](#insn-00afde78) 範囲 `[['00afde78', '00afdea7']]`
  - `CONDITIONAL_JUMP` [`00afdea4`](#insn-00afdea4) → [`00afdefc`](#insn-00afdefc)
  - `FALL_THROUGH` [`00afdea4`](#insn-00afdea4) → [`00afdea8`](#insn-00afdea8)
- ブロック [`00afdea8`](#insn-00afdea8) 範囲 `[['00afdea8', '00afdec3']]`
  - `CONDITIONAL_JUMP` [`00afdec0`](#insn-00afdec0) → [`00afdef0`](#insn-00afdef0)
  - `FALL_THROUGH` [`00afdec0`](#insn-00afdec0) → [`00afdec4`](#insn-00afdec4)
- ブロック [`00afdec4`](#insn-00afdec4) 範囲 `[['00afdec4', '00afdec7']]`
  - `CONDITIONAL_JUMP` [`00afdec4`](#insn-00afdec4) → [`00afde60`](#insn-00afde60)
  - `FALL_THROUGH` [`00afdec4`](#insn-00afdec4) → [`00afdec8`](#insn-00afdec8)
- ブロック [`00afdec8`](#insn-00afdec8) 範囲 `[['00afdec8', '00afdecb']]`
  - `FALL_THROUGH` [`00afdec8`](#insn-00afdec8) → [`00afdecc`](#insn-00afdecc)
- ブロック [`00afdecc`](#insn-00afdecc) 範囲 `[['00afdecc', '00afdedf']]`
  - `CONDITIONAL_JUMP` [`00afdedc`](#insn-00afdedc) → [`00afdefc`](#insn-00afdefc)
  - `FALL_THROUGH` [`00afdedc`](#insn-00afdedc) → [`00afdee0`](#insn-00afdee0)
- ブロック [`00afdee0`](#insn-00afdee0) 範囲 `[['00afdee0', '00afdeeb']]`
  - `CONDITIONAL_JUMP` [`00afdee8`](#insn-00afdee8) → [`00afdecc`](#insn-00afdecc)
  - `FALL_THROUGH` [`00afdee8`](#insn-00afdee8) → [`00afdeec`](#insn-00afdeec)
- ブロック [`00afdeec`](#insn-00afdeec) 範囲 `[['00afdeec', '00afdeef']]`
  - `UNCONDITIONAL_JUMP` [`00afdeec`](#insn-00afdeec) → [`00afde60`](#insn-00afde60)
- ブロック [`00afdef0`](#insn-00afdef0) 範囲 `[['00afdef0', '00afdef3']]`
  - `CONDITIONAL_JUMP` [`00afdef0`](#insn-00afdef0) → [`00afde60`](#insn-00afde60)
  - `FALL_THROUGH` [`00afdef0`](#insn-00afdef0) → [`00afdef4`](#insn-00afdef4)
- ブロック [`00afdef4`](#insn-00afdef4) 範囲 `[['00afdef4', '00afdefb']]`
  - `CONDITIONAL_JUMP` [`00afdef8`](#insn-00afdef8) → [`00afde60`](#insn-00afde60)
  - `FALL_THROUGH` [`00afdef8`](#insn-00afdef8) → [`00afdefc`](#insn-00afdefc)
- ブロック [`00afdefc`](#insn-00afdefc) 範囲 `[['00afdefc', '00afdf03']]`
  - `CONDITIONAL_JUMP` [`00afdf00`](#insn-00afdf00) → [`00afdf84`](#insn-00afdf84)
  - `FALL_THROUGH` [`00afdf00`](#insn-00afdf00) → [`00afdf04`](#insn-00afdf04)
- ブロック [`00afdf04`](#insn-00afdf04) 範囲 `[['00afdf04', '00afdf07']]`
  - `UNCONDITIONAL_JUMP` [`00afdf04`](#insn-00afdf04) → [`00afdfd0`](#insn-00afdfd0)
- ブロック [`00afdf08`](#insn-00afdf08) 範囲 `[['00afdf08', '00afdf0b']]`
  - `FALL_THROUGH` [`00afdf08`](#insn-00afdf08) → [`00afdf0c`](#insn-00afdf0c)
- ブロック [`00afdf0c`](#insn-00afdf0c) 範囲 `[['00afdf0c', '00afdf73']]`
  - `CONDITIONAL_JUMP` [`00afdf70`](#insn-00afdf70) → [`00afdf7c`](#insn-00afdf7c)
  - `FALL_THROUGH` [`00afdf70`](#insn-00afdf70) → [`00afdf74`](#insn-00afdf74)
- ブロック [`00afdf74`](#insn-00afdf74) 範囲 `[['00afdf74', '00afdf7b']]`
  - `FALL_THROUGH` [`00afdf78`](#insn-00afdf78) → [`00afdf7c`](#insn-00afdf7c)
- ブロック [`00afdf7c`](#insn-00afdf7c) 範囲 `[['00afdf7c', '00afdf83']]`
  - `CONDITIONAL_JUMP` [`00afdf80`](#insn-00afdf80) → [`00afdfd0`](#insn-00afdfd0)
  - `FALL_THROUGH` [`00afdf80`](#insn-00afdf80) → [`00afdf84`](#insn-00afdf84)
- ブロック [`00afdf84`](#insn-00afdf84) 範囲 `[['00afdf84', '00afdf8f']]`
  - `CONDITIONAL_JUMP` [`00afdf8c`](#insn-00afdf8c) → [`00afdfc4`](#insn-00afdfc4)
  - `FALL_THROUGH` [`00afdf8c`](#insn-00afdf8c) → [`00afdf90`](#insn-00afdf90)
- ブロック [`00afdf90`](#insn-00afdf90) 範囲 `[['00afdf90', '00afdf9b']]`
  - `CONDITIONAL_JUMP` [`00afdf98`](#insn-00afdf98) → [`00afdfb0`](#insn-00afdfb0)
  - `FALL_THROUGH` [`00afdf98`](#insn-00afdf98) → [`00afdf9c`](#insn-00afdf9c)
- ブロック [`00afdf9c`](#insn-00afdf9c) 範囲 `[['00afdf9c', '00afdfa7']]`
  - `CONDITIONAL_JUMP` [`00afdfa4`](#insn-00afdfa4) → [`00afdfbc`](#insn-00afdfbc)
  - `FALL_THROUGH` [`00afdfa4`](#insn-00afdfa4) → [`00afdfa8`](#insn-00afdfa8)
- ブロック [`00afdfa8`](#insn-00afdfa8) 範囲 `[['00afdfa8', '00afdfaf']]`
  - `CONDITIONAL_JUMP` [`00afdfac`](#insn-00afdfac) → [`00afdf9c`](#insn-00afdf9c)
  - `FALL_THROUGH` [`00afdfac`](#insn-00afdfac) → [`00afdfb0`](#insn-00afdfb0)
- ブロック [`00afdfb0`](#insn-00afdfb0) 範囲 `[['00afdfb0', '00afdfbb']]`
  - `UNCONDITIONAL_JUMP` [`00afdfb8`](#insn-00afdfb8) → [`00afdf9c`](#insn-00afdf9c)
- ブロック [`00afdfbc`](#insn-00afdfbc) 範囲 `[['00afdfbc', '00afdfc3']]`
  - `UNCONDITIONAL_JUMP` [`00afdfc0`](#insn-00afdfc0) → [`00afdfc8`](#insn-00afdfc8)
- ブロック [`00afdfc4`](#insn-00afdfc4) 範囲 `[['00afdfc4', '00afdfc7']]`
  - `FALL_THROUGH` [`00afdfc4`](#insn-00afdfc4) → [`00afdfc8`](#insn-00afdfc8)
- ブロック [`00afdfc8`](#insn-00afdfc8) 範囲 `[['00afdfc8', '00afdfcf']]`
  - `FALL_THROUGH` [`00afdfcc`](#insn-00afdfcc) → [`00afdfd0`](#insn-00afdfd0)
- ブロック [`00afdfd0`](#insn-00afdfd0) 範囲 `[['00afdfd0', '00afdfd7']]`
  - `CONDITIONAL_JUMP` [`00afdfd4`](#insn-00afdfd4) → [`00afe024`](#insn-00afe024)
  - `FALL_THROUGH` [`00afdfd4`](#insn-00afdfd4) → [`00afdfd8`](#insn-00afdfd8)
- ブロック [`00afdfd8`](#insn-00afdfd8) 範囲 `[['00afdfd8', '00afdfe3']]`
  - `CONDITIONAL_JUMP` [`00afdfe0`](#insn-00afdfe0) → [`00afe018`](#insn-00afe018)
  - `FALL_THROUGH` [`00afdfe0`](#insn-00afdfe0) → [`00afdfe4`](#insn-00afdfe4)
- ブロック [`00afdfe4`](#insn-00afdfe4) 範囲 `[['00afdfe4', '00afdfef']]`
  - `CONDITIONAL_JUMP` [`00afdfec`](#insn-00afdfec) → [`00afe004`](#insn-00afe004)
  - `FALL_THROUGH` [`00afdfec`](#insn-00afdfec) → [`00afdff0`](#insn-00afdff0)
- ブロック [`00afdff0`](#insn-00afdff0) 範囲 `[['00afdff0', '00afdffb']]`
  - `CONDITIONAL_JUMP` [`00afdff8`](#insn-00afdff8) → [`00afe010`](#insn-00afe010)
  - `FALL_THROUGH` [`00afdff8`](#insn-00afdff8) → [`00afdffc`](#insn-00afdffc)
- ブロック [`00afdffc`](#insn-00afdffc) 範囲 `[['00afdffc', '00afe003']]`
  - `CONDITIONAL_JUMP` [`00afe000`](#insn-00afe000) → [`00afdff0`](#insn-00afdff0)
  - `FALL_THROUGH` [`00afe000`](#insn-00afe000) → [`00afe004`](#insn-00afe004)
- ブロック [`00afe004`](#insn-00afe004) 範囲 `[['00afe004', '00afe00f']]`
  - `UNCONDITIONAL_JUMP` [`00afe00c`](#insn-00afe00c) → [`00afdff0`](#insn-00afdff0)
- ブロック [`00afe010`](#insn-00afe010) 範囲 `[['00afe010', '00afe017']]`
  - `UNCONDITIONAL_JUMP` [`00afe014`](#insn-00afe014) → [`00afe01c`](#insn-00afe01c)
- ブロック [`00afe018`](#insn-00afe018) 範囲 `[['00afe018', '00afe01b']]`
  - `FALL_THROUGH` [`00afe018`](#insn-00afe018) → [`00afe01c`](#insn-00afe01c)
- ブロック [`00afe01c`](#insn-00afe01c) 範囲 `[['00afe01c', '00afe023']]`
  - `FALL_THROUGH` [`00afe020`](#insn-00afe020) → [`00afe024`](#insn-00afe024)
- ブロック [`00afe024`](#insn-00afe024) 範囲 `[['00afe024', '00afe033']]`
  - `CONDITIONAL_JUMP` [`00afe030`](#insn-00afe030) → [`00afe058`](#insn-00afe058)
  - `FALL_THROUGH` [`00afe030`](#insn-00afe030) → [`00afe034`](#insn-00afe034)
- ブロック [`00afe034`](#insn-00afe034) 範囲 `[['00afe034', '00afe04f']]`
- ブロック [`00afe050`](#insn-00afe050) 範囲 `[['00afe050', '00afe057']]`
  - `UNCONDITIONAL_JUMP` [`00afe054`](#insn-00afe054) → [`00afdf0c`](#insn-00afdf0c)
- ブロック [`00afe058`](#insn-00afe058) 範囲 `[['00afe058', '00afe05b']]`

## 命令位置別の参照

- [`00afddfc`](#insn-00afddfc) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afde00`](#insn-00afde00) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afde04`](#insn-00afde04) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afde08`](#insn-00afde08) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afde0c`](#insn-00afde0c) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afde24`](#insn-00afde24) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afde2c`](#insn-00afde2c) → [`00bded40`](../00bde/00bded40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bded40` · 推定シンボル `None` · 推定型 `None`
- [`00afde38`](#insn-00afde38) → [`00bded40`](../00bde/00bded40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bded40` · 推定シンボル `None` · 推定型 `None`
- [`00afde3c`](#insn-00afde3c) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afde40`](#insn-00afde40) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afde48`](#insn-00afde48) → [`00afdf08`](#insn-00afdf08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afde4c`](#insn-00afde4c) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afde58`](#insn-00afde58) → [`00afde78`](#insn-00afde78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afde5c`](#insn-00afde5c) → [`00afdefc`](#insn-00afdefc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afde6c`](#insn-00afde6c) → [`00afe050`](#insn-00afe050) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afde74`](#insn-00afde74) → [`00afdefc`](#insn-00afdefc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdea4`](#insn-00afdea4) → [`00afdefc`](#insn-00afdefc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdec0`](#insn-00afdec0) → [`00afdef0`](#insn-00afdef0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdec4`](#insn-00afdec4) → [`00afde60`](#insn-00afde60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdedc`](#insn-00afdedc) → [`00afdefc`](#insn-00afdefc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdee8`](#insn-00afdee8) → [`00afdecc`](#insn-00afdecc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdeec`](#insn-00afdeec) → [`00afde60`](#insn-00afde60) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdef0`](#insn-00afdef0) → [`00afde60`](#insn-00afde60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdef4`](#insn-00afdef4) → [`00bdb200`](../00bdb/00bdb200.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb200` · 推定シンボル `None` · 推定型 `None`
- [`00afdef8`](#insn-00afdef8) → [`00afde60`](#insn-00afde60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdf00`](#insn-00afdf00) → [`00afdf84`](#insn-00afdf84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdf04`](#insn-00afdf04) → [`00afdfd0`](#insn-00afdfd0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdf08`](#insn-00afdf08) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdf1c`](#insn-00afdf1c) → [`00afd2ac`](00afd2ac.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00afd2ac` · 推定シンボル `None` · 推定型 `None`
- [`00afdf20`](#insn-00afdf20) → `Stack[-0xb8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdf24`](#insn-00afdf24) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdf40`](#insn-00afdf40) → `Stack[-0x98]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdf44`](#insn-00afdf44) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdf48`](#insn-00afdf48) → [`00bde230`](../00bde/00bde230.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde230` · 推定シンボル `None` · 推定型 `None`
- [`00afdf4c`](#insn-00afdf4c) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdf50`](#insn-00afdf50) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdf54`](#insn-00afdf54) → `Stack[-0xb8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdf5c`](#insn-00afdf5c) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdf6c`](#insn-00afdf6c) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdf70`](#insn-00afdf70) → [`00afdf7c`](#insn-00afdf7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdf74`](#insn-00afdf74) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdf78`](#insn-00afdf78) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00afdf7c`](#insn-00afdf7c) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdf80`](#insn-00afdf80) → [`00afdfd0`](#insn-00afdfd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdf84`](#insn-00afdf84) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdf8c`](#insn-00afdf8c) → [`00afdfc4`](#insn-00afdfc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdf98`](#insn-00afdf98) → [`00afdfb0`](#insn-00afdfb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdfa4`](#insn-00afdfa4) → [`00afdfbc`](#insn-00afdfbc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdfac`](#insn-00afdfac) → [`00afdf9c`](#insn-00afdf9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdfb4`](#insn-00afdfb4) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00afdfb8`](#insn-00afdfb8) → [`00afdf9c`](#insn-00afdf9c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdfbc`](#insn-00afdfbc) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdfc0`](#insn-00afdfc0) → [`00afdfc8`](#insn-00afdfc8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdfc8`](#insn-00afdfc8) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdfcc`](#insn-00afdfcc) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00afdfd0`](#insn-00afdfd0) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdfd4`](#insn-00afdfd4) → [`00afe024`](#insn-00afe024) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdfd8`](#insn-00afdfd8) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdfe0`](#insn-00afdfe0) → [`00afe018`](#insn-00afe018) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdfec`](#insn-00afdfec) → [`00afe004`](#insn-00afe004) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdff8`](#insn-00afdff8) → [`00afe010`](#insn-00afe010) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe000`](#insn-00afe000) → [`00afdff0`](#insn-00afdff0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe008`](#insn-00afe008) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00afe00c`](#insn-00afe00c) → [`00afdff0`](#insn-00afdff0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe010`](#insn-00afe010) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe014`](#insn-00afe014) → [`00afe01c`](#insn-00afe01c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe01c`](#insn-00afe01c) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe020`](#insn-00afe020) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00afe028`](#insn-00afe028) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe030`](#insn-00afe030) → [`00afe058`](#insn-00afe058) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe034`](#insn-00afe034) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe038`](#insn-00afe038) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe03c`](#insn-00afe03c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe040`](#insn-00afe040) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe044`](#insn-00afe044) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe054`](#insn-00afe054) → [`00afdf0c`](#insn-00afdf0c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe058`](#insn-00afe058) → [`00bdb090`](../00bdb/00bdb090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb090` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afddfc`](#insn-00afddfc)

~~~json
{
  "source": "00afddfc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afde00`](#insn-00afde00)

~~~json
{
  "source": "00afde00",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afde04`](#insn-00afde04)

~~~json
{
  "source": "00afde04",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afde08`](#insn-00afde08)

~~~json
{
  "source": "00afde08",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afde0c`](#insn-00afde0c)

~~~json
{
  "source": "00afde0c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afde24`](#insn-00afde24)

~~~json
{
  "source": "00afde24",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afde2c`](#insn-00afde2c)

~~~json
{
  "source": "00afde2c",
  "target": "00bded40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afde38`](#insn-00afde38)

~~~json
{
  "source": "00afde38",
  "target": "00bded40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afde3c`](#insn-00afde3c)

~~~json
{
  "source": "00afde3c",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afde40`](#insn-00afde40)

~~~json
{
  "source": "00afde40",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afde48`](#insn-00afde48)

~~~json
{
  "source": "00afde48",
  "target": "00afdf08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afde4c`](#insn-00afde4c)

~~~json
{
  "source": "00afde4c",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afde58`](#insn-00afde58)

~~~json
{
  "source": "00afde58",
  "target": "00afde78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afde5c`](#insn-00afde5c)

~~~json
{
  "source": "00afde5c",
  "target": "00afdefc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afde6c`](#insn-00afde6c)

~~~json
{
  "source": "00afde6c",
  "target": "00afe050",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afde74`](#insn-00afde74)

~~~json
{
  "source": "00afde74",
  "target": "00afdefc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdea4`](#insn-00afdea4)

~~~json
{
  "source": "00afdea4",
  "target": "00afdefc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdec0`](#insn-00afdec0)

~~~json
{
  "source": "00afdec0",
  "target": "00afdef0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdec4`](#insn-00afdec4)

~~~json
{
  "source": "00afdec4",
  "target": "00afde60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdedc`](#insn-00afdedc)

~~~json
{
  "source": "00afdedc",
  "target": "00afdefc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdee8`](#insn-00afdee8)

~~~json
{
  "source": "00afdee8",
  "target": "00afdecc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdeec`](#insn-00afdeec)

~~~json
{
  "source": "00afdeec",
  "target": "00afde60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdef0`](#insn-00afdef0)

~~~json
{
  "source": "00afdef0",
  "target": "00afde60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdef4`](#insn-00afdef4)

~~~json
{
  "source": "00afdef4",
  "target": "00bdb200",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afdef8`](#insn-00afdef8)

~~~json
{
  "source": "00afdef8",
  "target": "00afde60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdf00`](#insn-00afdf00)

~~~json
{
  "source": "00afdf00",
  "target": "00afdf84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdf04`](#insn-00afdf04)

~~~json
{
  "source": "00afdf04",
  "target": "00afdfd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdf08`](#insn-00afdf08)

~~~json
{
  "source": "00afdf08",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdf1c`](#insn-00afdf1c)

~~~json
{
  "source": "00afdf1c",
  "target": "00afd2ac",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afdf20`](#insn-00afdf20)

~~~json
{
  "source": "00afdf20",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdf24`](#insn-00afdf24)

~~~json
{
  "source": "00afdf24",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdf40`](#insn-00afdf40)

~~~json
{
  "source": "00afdf40",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdf44`](#insn-00afdf44)

~~~json
{
  "source": "00afdf44",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdf48`](#insn-00afdf48)

~~~json
{
  "source": "00afdf48",
  "target": "00bde230",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afdf4c`](#insn-00afdf4c)

~~~json
{
  "source": "00afdf4c",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdf50`](#insn-00afdf50)

~~~json
{
  "source": "00afdf50",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdf54`](#insn-00afdf54)

~~~json
{
  "source": "00afdf54",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdf5c`](#insn-00afdf5c)

~~~json
{
  "source": "00afdf5c",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdf6c`](#insn-00afdf6c)

~~~json
{
  "source": "00afdf6c",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdf70`](#insn-00afdf70)

~~~json
{
  "source": "00afdf70",
  "target": "00afdf7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdf74`](#insn-00afdf74)

~~~json
{
  "source": "00afdf74",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdf78`](#insn-00afdf78)

~~~json
{
  "source": "00afdf78",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afdf7c`](#insn-00afdf7c)

~~~json
{
  "source": "00afdf7c",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdf80`](#insn-00afdf80)

~~~json
{
  "source": "00afdf80",
  "target": "00afdfd0",
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
- 参照命令 [`00afdf8c`](#insn-00afdf8c)

~~~json
{
  "source": "00afdf8c",
  "target": "00afdfc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdf98`](#insn-00afdf98)

~~~json
{
  "source": "00afdf98",
  "target": "00afdfb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdfa4`](#insn-00afdfa4)

~~~json
{
  "source": "00afdfa4",
  "target": "00afdfbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdfac`](#insn-00afdfac)

~~~json
{
  "source": "00afdfac",
  "target": "00afdf9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdfb4`](#insn-00afdfb4)

~~~json
{
  "source": "00afdfb4",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afdfb8`](#insn-00afdfb8)

~~~json
{
  "source": "00afdfb8",
  "target": "00afdf9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdfbc`](#insn-00afdfbc)

~~~json
{
  "source": "00afdfbc",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdfc0`](#insn-00afdfc0)

~~~json
{
  "source": "00afdfc0",
  "target": "00afdfc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdfc8`](#insn-00afdfc8)

~~~json
{
  "source": "00afdfc8",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdfcc`](#insn-00afdfcc)

~~~json
{
  "source": "00afdfcc",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afdfd0`](#insn-00afdfd0)

~~~json
{
  "source": "00afdfd0",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdfd4`](#insn-00afdfd4)

~~~json
{
  "source": "00afdfd4",
  "target": "00afe024",
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
- 参照命令 [`00afdfe0`](#insn-00afdfe0)

~~~json
{
  "source": "00afdfe0",
  "target": "00afe018",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdfec`](#insn-00afdfec)

~~~json
{
  "source": "00afdfec",
  "target": "00afe004",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdff8`](#insn-00afdff8)

~~~json
{
  "source": "00afdff8",
  "target": "00afe010",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe000`](#insn-00afe000)

~~~json
{
  "source": "00afe000",
  "target": "00afdff0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe008`](#insn-00afe008)

~~~json
{
  "source": "00afe008",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afe00c`](#insn-00afe00c)

~~~json
{
  "source": "00afe00c",
  "target": "00afdff0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe010`](#insn-00afe010)

~~~json
{
  "source": "00afe010",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe014`](#insn-00afe014)

~~~json
{
  "source": "00afe014",
  "target": "00afe01c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe01c`](#insn-00afe01c)

~~~json
{
  "source": "00afe01c",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe020`](#insn-00afe020)

~~~json
{
  "source": "00afe020",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afe028`](#insn-00afe028)

~~~json
{
  "source": "00afe028",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe030`](#insn-00afe030)

~~~json
{
  "source": "00afe030",
  "target": "00afe058",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe034`](#insn-00afe034)

~~~json
{
  "source": "00afe034",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe038`](#insn-00afe038)

~~~json
{
  "source": "00afe038",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe03c`](#insn-00afe03c)

~~~json
{
  "source": "00afe03c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe040`](#insn-00afe040)

~~~json
{
  "source": "00afe040",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe044`](#insn-00afe044)

~~~json
{
  "source": "00afe044",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe054`](#insn-00afe054)

~~~json
{
  "source": "00afe054",
  "target": "00afdf0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe058`](#insn-00afe058)

~~~json
{
  "source": "00afe058",
  "target": "00bdb090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
