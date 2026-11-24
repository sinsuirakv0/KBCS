# 004ebfcc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `004ebcac`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004eb/004ebcac.md) · 移動量 `+0x320`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0010.md#compare-3f1b4b08dd2d6b7c3ba852ab3d1836fa)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "004ebfcc",
  "name": "_ZN5Botan5PKCS810BER_encodeERKNS_11Private_KeyERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS6_11char_traitsIcEENS6_9allocatorIcEEEENS6_6chrono8durationIxNS6_5ratioILl1ELl1000EEEEESE_",
  "size": 1292,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "77a32efd759780517b428b693bd3a5860d049219a74a859557dbca67ae5c9eb6",
  "source_text_sha256": "77a32efd759780517b428b693bd3a5860d049219a74a859557dbca67ae5c9eb6",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "004ebfcc",
        "004ec4d3"
      ],
      [
        "004ec5b4",
        "004ec5b7"
      ]
    ],
    "bytes_sha256": "1b72272197388e8233516acc30751cdf2877aca7753cd4298955b07d54d0493a",
    "instruction_count": 323,
    "instruction_bytes": 1292,
    "body_bytes": 1292,
    "indirect": 4,
    "unresolved": 2
  }
}
~~~

## 呼び出し元

- [00c5a6a0](../00c5a/00c5a6a0.md)

## 呼び出し先

- [0043be80](../0043b/0043be80.md)
- [004a7110](../004a7/004a7110.md)
- [004e27b4](../004e2/004e27b4.md)
- [00535ee0](../00535/00535ee0.md)
- [00536c3c](../00536/00536c3c.md)
- [00c58f50](../00c58/00c58f50.md)
- [00c58f80](../00c58/00c58f80.md)
- [00c58f90](../00c58/00c58f90.md)
- [00c58fb0](../00c58/00c58fb0.md)
- [00c59150](../00c59/00c59150.md)
- [00c59700](../00c59/00c59700.md)
- [00c59750](../00c59/00c59750.md)
- [00c59770](../00c59/00c59770.md)
- [00c59860](../00c59/00c59860.md)
- [00c598c0](../00c59/00c598c0.md)
- [00c59c30](../00c59/00c59c30.md)
- [00c59de0](../00c59/00c59de0.md)
- [00c5a680](../00c5a/00c5a680.md)
- [0112b058](../0112b/0112b058.md)

## 関連文字列（未確認候補）

~~~text
"AES-256/CBC"
"AES-256/GCM"
"SHA-256"
"SHA-512"
"Unsupported PBE "
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 6829 bytes

~~~c

void _ZN5Botan5PKCS810BER_encodeERKNS_11Private_KeyERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS6_11char_traitsIcEENS6_9allocatorIcEEEENS6_6chrono8durationIxNS6_5ratioILl1ELl1000EEEEESE_
               (undefined8 param_1,long *param_2,undefined8 param_3,undefined8 param_4,ulong param_5
               ,ulong *param_6)

{
  ulong uVar1;
  byte *pbVar2;
  long *plVar3;
  byte bVar4;
  long lVar5;
  byte *pbVar6;
  void *pvVar7;
  void *pvVar8;
  undefined8 uVar9;
  void *local_180;
  void *pvStack_178;
  void *local_170;
  void *pvStack_168;
  void *local_160;
  undefined8 auStack_158 [2];
  byte local_148;
  undefined1 auStack_147 [15];
  long *local_138;
  ulong local_130;
  undefined8 uStack_128;
  void *local_120;
  ulong local_118;
  undefined8 uStack_110;
  void *local_108;
  ulong local_f8;
  undefined8 uStack_f0;
  void *local_e8;
  ulong local_e0;
  undefined8 uStack_d8;
  void *local_d0;
  char *local_c8;
  char *pcStack_c0;
  void *local_b8;
  undefined8 local_b0;
  ulong local_a8;
  byte *local_a0;
  byte *local_98;
  byte *local_90;
  byte *local_88;
  byte *local_80;
  byte *local_78;
  long local_68;
  
  lVar5 = tpidr_el0;
  local_68 = *(long *)(lVar5 + 0x28);
  (**(code **)(*(long *)((long)param_2 + *(long *)(*param_2 + -0x80)) + 0x10))
            (&local_148,(long)param_2 + *(long *)(*param_2 + -0x80));
  bVar4 = (byte)*param_6;
  uVar1 = (ulong)(bVar4 >> 1);
  if ((bVar4 & 1) != 0) {
    uVar1 = param_6[1];
  }
  if (uVar1 == 0) {
    uVar1 = (ulong)(local_148 >> 1);
    if ((local_148 & 1) != 0) {
      uVar1 = auStack_147._7_8_;
    }
    if (uVar1 == 8) {
      plVar3 = local_138;
      if ((local_148 & 1) == 0) {
        plVar3 = (long *)auStack_147;
      }
      if (*plVar3 == 0x656365696c45634d) {
LAB_004ec298:
        local_c8 = "AES-256/GCM";
        pcStack_c0 = "SHA-512";
        FUN_00536c3c(&local_130,&local_c8);
        goto LAB_004ec2b8;
      }
    }
    else if (uVar1 == 10) {
      plVar3 = local_138;
      if ((local_148 & 1) == 0) {
        plVar3 = (long *)auStack_147;
      }
      if (*plVar3 == 0x3535326576727543 && (short)plVar3[1] == 0x3931) goto LAB_004ec298;
    }
    local_c8 = "AES-256/CBC";
    pcStack_c0 = "SHA-256";
    FUN_00536c3c(&local_130,&local_c8);
LAB_004ec2b8:
    if ((local_148 & 1) != 0) {
      _ZdlPv(local_138);
    }
    _ZNK5Botan11Private_Key16private_key_infoEv(&local_180,param_2);
    local_e0 = param_5;
    FUN_004e27b4(&local_c8,&local_180,param_4,&local_e0,0,&local_130,&local_118,param_3);
    pvVar7 = local_180;
    if (local_180 != (void *)0x0) {
      pvStack_178 = local_180;
      (*(code *)PTR_memset_00c687d8)(local_180,0,(long)local_170 - (long)local_180);
      free(pvVar7);
    }
    pvStack_168 = (void *)0x0;
    local_170 = (void *)0x0;
    auStack_158[0] = 0;
    local_160 = (void *)0x0;
    pvStack_178 = (void *)0x0;
    local_180 = (void *)0x0;
    _ZN5Botan11DER_Encoder10start_consENS_8ASN1_TagES1_(&local_180,0x10,0);
    (**(code **)local_c8)(&local_c8,&local_180);
    _ZN5Botan11DER_Encoder10add_objectENS_8ASN1_TagES1_PKhm
              (&local_180,4,0,local_88,(long)local_80 - (long)local_88);
    _ZN5Botan11DER_Encoder8end_consEv(&local_180);
    FUN_004a7110(param_1,&local_180);
    pvVar8 = pvStack_168;
    pvVar7 = local_160;
    if (pvStack_168 != (void *)0x0) {
      while (pvVar7 != pvVar8) {
        FUN_00535ee0(auStack_158,(void *)((long)pvVar7 + -0x38));
        pvVar7 = (void *)((long)pvVar7 + -0x38);
      }
      local_160 = pvVar8;
      _ZdlPv(pvStack_168);
    }
    pvVar7 = local_180;
    if (local_180 != (void *)0x0) {
      pvStack_178 = local_180;
      (*(code *)PTR_memset_00c687d8)(local_180,0,(long)local_170 - (long)local_180);
      free(pvVar7);
    }
    if (local_88 != (byte *)0x0) {
      local_80 = local_88;
      _ZdlPv(local_88);
    }
    if (local_a0 != (byte *)0x0) {
      local_98 = local_a0;
      _ZdlPv(local_a0);
    }
    if (local_b8 != (void *)0x0) {
      local_b0 = local_b8;
      _ZdlPv(local_b8);
    }
    if ((local_118 & 1) != 0) {
      _ZdlPv(local_108);
    }
    if ((local_130 & 1) != 0) {
      _ZdlPv(local_120);
    }
    if (*(long *)(lVar5 + 0x28) == local_68) {
      return;
    }
  }
  else {
    if ((bVar4 & 1) == 0) {
      pvStack_178 = (void *)param_6[1];
      local_180 = (void *)*param_6;
      local_170 = (void *)param_6[2];
    }
    else {
      FUN_0043be80(&local_180,param_6[2]);
    }
    _ZN5Botan9SCAN_NameC1ENSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
              (&local_c8,&local_180);
    if (((ulong)local_180 & 1) != 0) {
      _ZdlPv(local_170);
    }
    uVar1 = (ulong)local_b0 >> 1 & 0x7f;
    if (((ulong)local_b0 & 1) != 0) {
      uVar1 = local_a8;
    }
    if (uVar1 == 0xc) {
      pbVar2 = (byte *)((long)&local_b0 + 1);
      if (((ulong)local_b0 & 1) != 0) {
        pbVar2 = local_a0;
      }
      if ((*(long *)pbVar2 == 0x53434b502d454250 && *(int *)(pbVar2 + 8) == 0x30327635) &&
         ((long)local_90 - (long)local_98 == 0x30)) {
        _ZNK5Botan9SCAN_Name3argEm(&local_e0,&local_c8,1);
        _ZNK5Botan9SCAN_Name3argEm(&local_f8,&local_c8,0);
        pbVar2 = local_80;
        uStack_128 = uStack_d8;
        local_130 = local_e0;
        local_120 = local_d0;
        uStack_110 = uStack_f0;
        local_118 = local_f8;
        local_108 = local_e8;
        if (local_80 != (byte *)0x0) {
          while (pbVar6 = local_78, pbVar6 != pbVar2) {
            local_78 = pbVar6 + -0x18;
            if ((*local_78 & 1) != 0) {
              _ZdlPv(*(void **)(pbVar6 + -8));
            }
          }
          local_78 = pbVar2;
          _ZdlPv(local_80);
        }
        pbVar2 = local_98;
        if (local_98 != (byte *)0x0) {
          while (pbVar6 = local_90, pbVar6 != pbVar2) {
            local_90 = pbVar6 + -0x18;
            if ((*local_90 & 1) != 0) {
              _ZdlPv(*(void **)(pbVar6 + -8));
            }
          }
          local_90 = pbVar2;
          _ZdlPv(local_98);
        }
        if (((ulong)local_b0 & 1) != 0) {
          _ZdlPv(local_a0);
        }
        if (((ulong)local_c8 & 1) != 0) {
          _ZdlPv(local_b8);
        }
        goto LAB_004ec2b8;
      }
    }
    uVar9 = __cxa_allocate_exception(0x20);
    _ZNSt6__ndk1plIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EEPKS6_RKS9_
              (&local_e0,"Unsupported PBE ",param_6);
    _ZN5Botan9ExceptionC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
              (uVar9,&local_e0);
    if (*(long *)(lVar5 + 0x28) == local_68) {
                    /* WARNING: Subroutine does not return */
      __cxa_throw(uVar9,PTR__ZTIN5Botan9ExceptionE_00c9be28,FUN_00535bc8);
    }
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-004ebfcc"></a> `004ebfcc` | `ff 03 06 d1` | sub sp,sp,#0x180 | `FALL_THROUGH`
<a id="insn-004ebfd0"></a> `004ebfd0` | `fd 7b 12 a9` | stp x29,x30,[sp, #0x120] | `FALL_THROUGH`
<a id="insn-004ebfd4"></a> `004ebfd4` | `fc 9b 00 f9` | str x28,[sp, #0x130] | `FALL_THROUGH`
<a id="insn-004ebfd8"></a> `004ebfd8` | `fa 67 14 a9` | stp x26,x25,[sp, #0x140] | `FALL_THROUGH`
<a id="insn-004ebfdc"></a> `004ebfdc` | `f8 5f 15 a9` | stp x24,x23,[sp, #0x150] | `FALL_THROUGH`
<a id="insn-004ebfe0"></a> `004ebfe0` | `f6 57 16 a9` | stp x22,x21,[sp, #0x160] | `FALL_THROUGH`
<a id="insn-004ebfe4"></a> `004ebfe4` | `f4 4f 17 a9` | stp x20,x19,[sp, #0x170] | `FALL_THROUGH`
<a id="insn-004ebfe8"></a> `004ebfe8` | `fd 83 04 91` | add x29,sp,#0x120 | `FALL_THROUGH`
<a id="insn-004ebfec"></a> `004ebfec` | `59 d0 3b d5` | mrs x25,tpidr_el0 | `FALL_THROUGH`
<a id="insn-004ebff0"></a> `004ebff0` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-004ebff4"></a> `004ebff4` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-004ebff8"></a> `004ebff8` | `29 17 40 f9` | ldr x9,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-004ebffc"></a> `004ebffc` | `e8 e3 00 91` | add x8,sp,#0x38 | `FALL_THROUGH`
<a id="insn-004ec000"></a> `004ec000` | `f8 03 04 aa` | mov x24,x4 | `FALL_THROUGH`
<a id="insn-004ec004"></a> `004ec004` | `f6 03 03 aa` | mov x22,x3 | `FALL_THROUGH`
<a id="insn-004ec008"></a> `004ec008` | `f5 03 02 aa` | mov x21,x2 | `FALL_THROUGH`
<a id="insn-004ec00c"></a> `004ec00c` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-004ec010"></a> `004ec010` | `a9 83 1f f8` | stur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-004ec014"></a> `004ec014` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-004ec018"></a> `004ec018` | `29 01 58 f8` | ldur x9,[x9, #-0x80] | `FALL_THROUGH`
<a id="insn-004ec01c"></a> `004ec01c` | `0a 68 69 f8` | ldr x10,[x0, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-004ec020"></a> `004ec020` | `00 00 09 8b` | add x0,x0,x9 | `FALL_THROUGH`
<a id="insn-004ec024"></a> `004ec024` | `4a 09 40 f9` | ldr x10,[x10, #0x10] | `FALL_THROUGH`
<a id="insn-004ec028"></a> `004ec028` | `40 01 3f d6` | blr x10 | `COMPUTED_CALL`
<a id="insn-004ec02c"></a> `004ec02c` | `08 03 40 39` | ldrb w8,[x24] | `FALL_THROUGH`
<a id="insn-004ec030"></a> `004ec030` | `02 07 40 f9` | ldr x2,[x24, #0x8] | `FALL_THROUGH`
<a id="insn-004ec034"></a> `004ec034` | `09 fd 41 d3` | lsr x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-004ec038"></a> `004ec038` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-004ec03c"></a> `004ec03c` | `29 01 82 9a` | csel x9,x9,x2,eq | `FALL_THROUGH`
<a id="insn-004ec040"></a> `004ec040` | `e9 00 00 b4` | cbz x9,0x004ec05c | `CONDITIONAL_JUMP`
<a id="insn-004ec044"></a> `004ec044` | `c8 04 00 37` | tbnz w8,#0x0,0x004ec0dc | `CONDITIONAL_JUMP`
<a id="insn-004ec048"></a> `004ec048` | `00 03 c0 3d` | ldr q0,[x24] | `FALL_THROUGH`
<a id="insn-004ec04c"></a> `004ec04c` | `08 0b 40 f9` | ldr x8,[x24, #0x10] | `FALL_THROUGH`
<a id="insn-004ec050"></a> `004ec050` | `e0 03 80 3d` | str q0,[sp] | `FALL_THROUGH`
<a id="insn-004ec054"></a> `004ec054` | `e8 0b 00 f9` | str x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-004ec058"></a> `004ec058` | `24 00 00 14` | b 0x004ec0e8 | `UNCONDITIONAL_JUMP`
<a id="insn-004ec05c"></a> `004ec05c` | `e8 e3 40 39` | ldrb w8,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-004ec060"></a> `004ec060` | `e9 23 40 f9` | ldr x9,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-004ec064"></a> `004ec064` | `0a fd 41 d3` | lsr x10,x8,#0x1 | `FALL_THROUGH`
<a id="insn-004ec068"></a> `004ec068` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-004ec06c"></a> `004ec06c` | `49 01 89 9a` | csel x9,x10,x9,eq | `FALL_THROUGH`
<a id="insn-004ec070"></a> `004ec070` | `3f 21 00 f1` | cmp x9,#0x8 | `FALL_THROUGH`
<a id="insn-004ec074"></a> `004ec074` | `c0 0f 00 54` | b.eq 0x004ec26c | `CONDITIONAL_JUMP`
<a id="insn-004ec078"></a> `004ec078` | `3f 29 00 f1` | cmp x9,#0xa | `FALL_THROUGH`
<a id="insn-004ec07c"></a> `004ec07c` | `e1 01 00 54` | b.ne 0x004ec0b8 | `CONDITIONAL_JUMP`
<a id="insn-004ec080"></a> `004ec080` | `e9 27 40 f9` | ldr x9,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-004ec084"></a> `004ec084` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-004ec088"></a> `004ec088` | `e8 e3 00 91` | add x8,sp,#0x38 | `FALL_THROUGH`
<a id="insn-004ec08c"></a> `004ec08c` | `6a a8 8e d2` | mov x10,#0x7543 | `FALL_THROUGH`
<a id="insn-004ec090"></a> `004ec090` | `28 15 88 9a` | csinc x8,x9,x8,ne | `FALL_THROUGH`
<a id="insn-004ec094"></a> `004ec094` | `4a ce ae f2` | movk x10,#0x7672, LSL #16 | `FALL_THROUGH`
<a id="insn-004ec098"></a> `004ec098` | `09 01 40 f9` | ldr x9,[x8] | `FALL_THROUGH`
<a id="insn-004ec09c"></a> `004ec09c` | `aa 4c c6 f2` | movk x10,#0x3265, LSL #32 | `FALL_THROUGH`
<a id="insn-004ec0a0"></a> `004ec0a0` | `08 11 40 79` | ldrh w8,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-004ec0a4"></a> `004ec0a4` | `aa a6 e6 f2` | movk x10,#0x3535, LSL #48 | `FALL_THROUGH`
<a id="insn-004ec0a8"></a> `004ec0a8` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-004ec0ac"></a> `004ec0ac` | `29 26 87 52` | mov w9,#0x3931 | `FALL_THROUGH`
<a id="insn-004ec0b0"></a> `004ec0b0` | `00 01 49 7a` | ccmp w8,w9,#0x0,eq | `FALL_THROUGH`
<a id="insn-004ec0b4"></a> `004ec0b4` | `20 0f 00 54` | b.eq 0x004ec298 | `CONDITIONAL_JUMP`
<a id="insn-004ec0b8"></a> `004ec0b8` | `88 ee ff d0` | adrp x8,0x2be000 | `FALL_THROUGH`
<a id="insn-004ec0bc"></a> `004ec0bc` | `08 11 34 91` | add x8,x8,#0xd04 | `FALL_THROUGH`
<a id="insn-004ec0c0"></a> `004ec0c0` | `e9 ed ff b0` | adrp x9,0x2a9000 | `FALL_THROUGH`
<a id="insn-004ec0c4"></a> `004ec0c4` | `29 7d 30 91` | add x9,x9,#0xc1f | `FALL_THROUGH`
<a id="insn-004ec0c8"></a> `004ec0c8` | `a8 a7 39 a9` | stp x8,x9,[x29, #-0x68] | `FALL_THROUGH`
<a id="insn-004ec0cc"></a> `004ec0cc` | `e0 43 01 91` | add x0,sp,#0x50 | `FALL_THROUGH`
<a id="insn-004ec0d0"></a> `004ec0d0` | `a1 a3 01 d1` | sub x1,x29,#0x68 | `FALL_THROUGH`
<a id="insn-004ec0d4"></a> `004ec0d4` | `da 2a 01 94` | bl 0x00536c3c | `UNCONDITIONAL_CALL`
<a id="insn-004ec0d8"></a> `004ec0d8` | `78 00 00 14` | b 0x004ec2b8 | `UNCONDITIONAL_JUMP`
<a id="insn-004ec0dc"></a> `004ec0dc` | `01 0b 40 f9` | ldr x1,[x24, #0x10] | `FALL_THROUGH`
<a id="insn-004ec0e0"></a> `004ec0e0` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-004ec0e4"></a> `004ec0e4` | `67 3f fd 97` | bl 0x0043be80 | `UNCONDITIONAL_CALL`
<a id="insn-004ec0e8"></a> `004ec0e8` | `a0 a3 01 d1` | sub x0,x29,#0x68 | `FALL_THROUGH`
<a id="insn-004ec0ec"></a> `004ec0ec` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-004ec0f0"></a> `004ec0f0` | `3c b7 1d 94` | bl 0x00c59de0 | `UNCONDITIONAL_CALL`
<a id="insn-004ec0f4"></a> `004ec0f4` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-004ec0f8"></a> `004ec0f8` | `68 00 00 36` | tbz w8,#0x0,0x004ec104 | `CONDITIONAL_JUMP`
<a id="insn-004ec0fc"></a> `004ec0fc` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-004ec100"></a> `004ec100` | `94 b3 1d 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-004ec104"></a> `004ec104` | `a8 03 5b 38` | ldurb w8,[x29, #-0x50] | `FALL_THROUGH`
<a id="insn-004ec108"></a> `004ec108` | `a9 83 5b f8` | ldur x9,[x29, #-0x48] | `FALL_THROUGH`
<a id="insn-004ec10c"></a> `004ec10c` | `0a fd 41 d3` | lsr x10,x8,#0x1 | `FALL_THROUGH`
<a id="insn-004ec110"></a> `004ec110` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-004ec114"></a> `004ec114` | `49 01 89 9a` | csel x9,x10,x9,eq | `FALL_THROUGH`
<a id="insn-004ec118"></a> `004ec118` | `3f 31 00 f1` | cmp x9,#0xc | `FALL_THROUGH`
<a id="insn-004ec11c"></a> `004ec11c` | `e1 1a 00 54` | b.ne 0x004ec478 | `CONDITIONAL_JUMP`
<a id="insn-004ec120"></a> `004ec120` | `a9 03 5c f8` | ldur x9,[x29, #-0x40] | `FALL_THROUGH`
<a id="insn-004ec124"></a> `004ec124` | `aa a3 01 d1` | sub x10,x29,#0x68 | `FALL_THROUGH`
<a id="insn-004ec128"></a> `004ec128` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-004ec12c"></a> `004ec12c` | `4a 65 00 91` | add x10,x10,#0x19 | `FALL_THROUGH`
<a id="insn-004ec130"></a> `004ec130` | `48 01 89 9a` | csel x8,x10,x9,eq | `FALL_THROUGH`
<a id="insn-004ec134"></a> `004ec134` | `0a 4a 88 d2` | mov x10,#0x4250 | `FALL_THROUGH`
<a id="insn-004ec138"></a> `004ec138` | `aa a8 a5 f2` | movk x10,#0x2d45, LSL #16 | `FALL_THROUGH`
<a id="insn-004ec13c"></a> `004ec13c` | `09 01 40 f9` | ldr x9,[x8] | `FALL_THROUGH`
<a id="insn-004ec140"></a> `004ec140` | `08 09 40 b9` | ldr w8,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-004ec144"></a> `004ec144` | `0a 6a c9 f2` | movk x10,#0x4b50, LSL #32 | `FALL_THROUGH`
<a id="insn-004ec148"></a> `004ec148` | `6a 68 ea f2` | movk x10,#0x5343, LSL #48 | `FALL_THROUGH`
<a id="insn-004ec14c"></a> `004ec14c` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-004ec150"></a> `004ec150` | `a9 c6 8e 52` | mov w9,#0x7635 | `FALL_THROUGH`
<a id="insn-004ec154"></a> `004ec154` | `49 06 a6 72` | movk w9,#0x3032, LSL #16 | `FALL_THROUGH`
<a id="insn-004ec158"></a> `004ec158` | `00 01 49 7a` | ccmp w8,w9,#0x0,eq | `FALL_THROUGH`
<a id="insn-004ec15c"></a> `004ec15c` | `e1 18 00 54` | b.ne 0x004ec478 | `CONDITIONAL_JUMP`
<a id="insn-004ec160"></a> `004ec160` | `a9 a3 7c a9` | ldp x9,x8,[x29, #-0x38] | `FALL_THROUGH`
<a id="insn-004ec164"></a> `004ec164` | `08 01 09 cb` | sub x8,x8,x9 | `FALL_THROUGH`
<a id="insn-004ec168"></a> `004ec168` | `1f c1 00 f1` | cmp x8,#0x30 | `FALL_THROUGH`
<a id="insn-004ec16c"></a> `004ec16c` | `61 18 00 54` | b.ne 0x004ec478 | `CONDITIONAL_JUMP`
<a id="insn-004ec170"></a> `004ec170` | `a8 03 02 d1` | sub x8,x29,#0x80 | `FALL_THROUGH`
<a id="insn-004ec174"></a> `004ec174` | `a0 a3 01 d1` | sub x0,x29,#0x68 | `FALL_THROUGH`
<a id="insn-004ec178"></a> `004ec178` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-004ec17c"></a> `004ec17c` | `ad b6 1d 94` | bl 0x00c59c30 | `UNCONDITIONAL_CALL`
<a id="insn-004ec180"></a> `004ec180` | `e8 23 02 91` | add x8,sp,#0x88 | `FALL_THROUGH`
<a id="insn-004ec184"></a> `004ec184` | `a0 a3 01 d1` | sub x0,x29,#0x68 | `FALL_THROUGH`
<a id="insn-004ec188"></a> `004ec188` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-004ec18c"></a> `004ec18c` | `a9 b6 1d 94` | bl 0x00c59c30 | `UNCONDITIONAL_CALL`
<a id="insn-004ec190"></a> `004ec190` | `a0 03 d8 3c` | ldur q0,[x29, #-0x80] | `FALL_THROUGH`
<a id="insn-004ec194"></a> `004ec194` | `a8 03 59 f8` | ldur x8,[x29, #-0x70] | `FALL_THROUGH`
<a id="insn-004ec198"></a> `004ec198` | `e1 83 c8 3c` | ldur q1,[sp, #0x88] | `FALL_THROUGH`
<a id="insn-004ec19c"></a> `004ec19c` | `e9 4f 40 f9` | ldr x9,[sp, #0x98] | `FALL_THROUGH`
<a id="insn-004ec1a0"></a> `004ec1a0` | `b8 03 5e f8` | ldur x24,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-004ec1a4"></a> `004ec1a4` | `e0 17 80 3d` | str q0,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-004ec1a8"></a> `004ec1a8` | `e8 33 00 f9` | str x8,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-004ec1ac"></a> `004ec1ac` | `e1 83 86 3c` | stur q1,[sp, #0x68] | `FALL_THROUGH`
<a id="insn-004ec1b0"></a> `004ec1b0` | `e9 3f 00 f9` | str x9,[sp, #0x78] | `FALL_THROUGH`
<a id="insn-004ec1b4"></a> `004ec1b4` | `58 02 00 b4` | cbz x24,0x004ec1fc | `CONDITIONAL_JUMP`
<a id="insn-004ec1b8"></a> `004ec1b8` | `a8 83 5e f8` | ldur x8,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-004ec1bc"></a> `004ec1bc` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-004ec1c0"></a> `004ec1c0` | `1f 01 18 eb` | cmp x8,x24 | `FALL_THROUGH`
<a id="insn-004ec1c4"></a> `004ec1c4` | `80 01 00 54` | b.eq 0x004ec1f4 | `CONDITIONAL_JUMP`
<a id="insn-004ec1c8"></a> `004ec1c8` | `fa 03 08 aa` | mov x26,x8 | `FALL_THROUGH`
<a id="insn-004ec1cc"></a> `004ec1cc` | `04 00 00 14` | b 0x004ec1dc | `UNCONDITIONAL_JUMP`
<a id="insn-004ec1d0"></a> `004ec1d0` | `5f 03 18 eb` | cmp x26,x24 | `FALL_THROUGH`
<a id="insn-004ec1d4"></a> `004ec1d4` | `e8 03 1a aa` | mov x8,x26 | `FALL_THROUGH`
<a id="insn-004ec1d8"></a> `004ec1d8` | `c0 00 00 54` | b.eq 0x004ec1f0 | `CONDITIONAL_JUMP`
<a id="insn-004ec1dc"></a> `004ec1dc` | `49 8f 5e 38` | ldrb w9,[x26, #-0x18]! | `FALL_THROUGH`
<a id="insn-004ec1e0"></a> `004ec1e0` | `89 ff 07 36` | tbz w9,#0x0,0x004ec1d0 | `CONDITIONAL_JUMP`
<a id="insn-004ec1e4"></a> `004ec1e4` | `00 81 5f f8` | ldur x0,[x8, #-0x8] | `FALL_THROUGH`
<a id="insn-004ec1e8"></a> `004ec1e8` | `5a b3 1d 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-004ec1ec"></a> `004ec1ec` | `f9 ff ff 17` | b 0x004ec1d0 | `UNCONDITIONAL_JUMP`
<a id="insn-004ec1f0"></a> `004ec1f0` | `a0 03 5e f8` | ldur x0,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-004ec1f4"></a> `004ec1f4` | `b8 83 1e f8` | stur x24,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-004ec1f8"></a> `004ec1f8` | `56 b3 1d 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-004ec1fc"></a> `004ec1fc` | `b8 83 5c f8` | ldur x24,[x29, #-0x38] | `FALL_THROUGH`
<a id="insn-004ec200"></a> `004ec200` | `58 02 00 b4` | cbz x24,0x004ec248 | `CONDITIONAL_JUMP`
<a id="insn-004ec204"></a> `004ec204` | `a8 03 5d f8` | ldur x8,[x29, #-0x30] | `FALL_THROUGH`
<a id="insn-004ec208"></a> `004ec208` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-004ec20c"></a> `004ec20c` | `1f 01 18 eb` | cmp x8,x24 | `FALL_THROUGH`
<a id="insn-004ec210"></a> `004ec210` | `80 01 00 54` | b.eq 0x004ec240 | `CONDITIONAL_JUMP`
<a id="insn-004ec214"></a> `004ec214` | `fa 03 08 aa` | mov x26,x8 | `FALL_THROUGH`
<a id="insn-004ec218"></a> `004ec218` | `04 00 00 14` | b 0x004ec228 | `UNCONDITIONAL_JUMP`
<a id="insn-004ec21c"></a> `004ec21c` | `5f 03 18 eb` | cmp x26,x24 | `FALL_THROUGH`
<a id="insn-004ec220"></a> `004ec220` | `e8 03 1a aa` | mov x8,x26 | `FALL_THROUGH`
<a id="insn-004ec224"></a> `004ec224` | `c0 00 00 54` | b.eq 0x004ec23c | `CONDITIONAL_JUMP`
<a id="insn-004ec228"></a> `004ec228` | `49 8f 5e 38` | ldrb w9,[x26, #-0x18]! | `FALL_THROUGH`
<a id="insn-004ec22c"></a> `004ec22c` | `89 ff 07 36` | tbz w9,#0x0,0x004ec21c | `CONDITIONAL_JUMP`
<a id="insn-004ec230"></a> `004ec230` | `00 81 5f f8` | ldur x0,[x8, #-0x8] | `FALL_THROUGH`
<a id="insn-004ec234"></a> `004ec234` | `47 b3 1d 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-004ec238"></a> `004ec238` | `f9 ff ff 17` | b 0x004ec21c | `UNCONDITIONAL_JUMP`
<a id="insn-004ec23c"></a> `004ec23c` | `a0 83 5c f8` | ldur x0,[x29, #-0x38] | `FALL_THROUGH`
<a id="insn-004ec240"></a> `004ec240` | `b8 03 1d f8` | stur x24,[x29, #-0x30] | `FALL_THROUGH`
<a id="insn-004ec244"></a> `004ec244` | `43 b3 1d 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-004ec248"></a> `004ec248` | `a8 03 5b 38` | ldurb w8,[x29, #-0x50] | `FALL_THROUGH`
<a id="insn-004ec24c"></a> `004ec24c` | `68 00 00 36` | tbz w8,#0x0,0x004ec258 | `CONDITIONAL_JUMP`
<a id="insn-004ec250"></a> `004ec250` | `a0 03 5c f8` | ldur x0,[x29, #-0x40] | `FALL_THROUGH`
<a id="insn-004ec254"></a> `004ec254` | `3f b3 1d 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-004ec258"></a> `004ec258` | `a8 83 59 38` | ldurb w8,[x29, #-0x68] | `FALL_THROUGH`
<a id="insn-004ec25c"></a> `004ec25c` | `e8 02 00 36` | tbz w8,#0x0,0x004ec2b8 | `CONDITIONAL_JUMP`
<a id="insn-004ec260"></a> `004ec260` | `a0 83 5a f8` | ldur x0,[x29, #-0x58] | `FALL_THROUGH`
<a id="insn-004ec264"></a> `004ec264` | `3b b3 1d 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-004ec268"></a> `004ec268` | `14 00 00 14` | b 0x004ec2b8 | `UNCONDITIONAL_JUMP`
<a id="insn-004ec26c"></a> `004ec26c` | `e9 27 40 f9` | ldr x9,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-004ec270"></a> `004ec270` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-004ec274"></a> `004ec274` | `e8 e3 00 91` | add x8,sp,#0x38 | `FALL_THROUGH`
<a id="insn-004ec278"></a> `004ec278` | `28 15 88 9a` | csinc x8,x9,x8,ne | `FALL_THROUGH`
<a id="insn-004ec27c"></a> `004ec27c` | `a9 69 8c d2` | mov x9,#0x634d | `FALL_THROUGH`
<a id="insn-004ec280"></a> `004ec280` | `a9 88 ad f2` | movk x9,#0x6c45, LSL #16 | `FALL_THROUGH`
<a id="insn-004ec284"></a> `004ec284` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-004ec288"></a> `004ec288` | `29 ad cc f2` | movk x9,#0x6569, LSL #32 | `FALL_THROUGH`
<a id="insn-004ec28c"></a> `004ec28c` | `69 ac ec f2` | movk x9,#0x6563, LSL #48 | `FALL_THROUGH`
<a id="insn-004ec290"></a> `004ec290` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-004ec294"></a> `004ec294` | `21 f1 ff 54` | b.ne 0x004ec0b8 | `CONDITIONAL_JUMP`
<a id="insn-004ec298"></a> `004ec298` | `e8 ed ff f0` | adrp x8,0x2ab000 | `FALL_THROUGH`
<a id="insn-004ec29c"></a> `004ec29c` | `08 f9 10 91` | add x8,x8,#0x43e | `FALL_THROUGH`
<a id="insn-004ec2a0"></a> `004ec2a0` | `69 ee ff f0` | adrp x9,0x2bb000 | `FALL_THROUGH`
<a id="insn-004ec2a4"></a> `004ec2a4` | `29 cd 0d 91` | add x9,x9,#0x373 | `FALL_THROUGH`
<a id="insn-004ec2a8"></a> `004ec2a8` | `a8 a7 39 a9` | stp x8,x9,[x29, #-0x68] | `FALL_THROUGH`
<a id="insn-004ec2ac"></a> `004ec2ac` | `e0 43 01 91` | add x0,sp,#0x50 | `FALL_THROUGH`
<a id="insn-004ec2b0"></a> `004ec2b0` | `a1 a3 01 d1` | sub x1,x29,#0x68 | `FALL_THROUGH`
<a id="insn-004ec2b4"></a> `004ec2b4` | `62 2a 01 94` | bl 0x00536c3c | `UNCONDITIONAL_CALL`
<a id="insn-004ec2b8"></a> `004ec2b8` | `e8 e3 40 39` | ldrb w8,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-004ec2bc"></a> `004ec2bc` | `68 00 00 36` | tbz w8,#0x0,0x004ec2c8 | `CONDITIONAL_JUMP`
<a id="insn-004ec2c0"></a> `004ec2c0` | `e0 27 40 f9` | ldr x0,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-004ec2c4"></a> `004ec2c4` | `23 b3 1d 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-004ec2c8"></a> `004ec2c8` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-004ec2cc"></a> `004ec2cc` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-004ec2d0"></a> `004ec2d0` | `ec b8 1d 94` | bl 0x00c5a680 | `UNCONDITIONAL_CALL`
<a id="insn-004ec2d4"></a> `004ec2d4` | `e9 43 01 91` | add x9,sp,#0x50 | `FALL_THROUGH`
<a id="insn-004ec2d8"></a> `004ec2d8` | `b6 03 18 f8` | stur x22,[x29, #-0x80] | `FALL_THROUGH`
<a id="insn-004ec2dc"></a> `004ec2dc` | `a8 a3 01 d1` | sub x8,x29,#0x68 | `FALL_THROUGH`
<a id="insn-004ec2e0"></a> `004ec2e0` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-004ec2e4"></a> `004ec2e4` | `a2 03 02 d1` | sub x2,x29,#0x80 | `FALL_THROUGH`
<a id="insn-004ec2e8"></a> `004ec2e8` | `e4 43 01 91` | add x4,sp,#0x50 | `FALL_THROUGH`
<a id="insn-004ec2ec"></a> `004ec2ec` | `25 61 00 91` | add x5,x9,#0x18 | `FALL_THROUGH`
<a id="insn-004ec2f0"></a> `004ec2f0` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-004ec2f4"></a> `004ec2f4` | `e3 03 1f aa` | mov x3,xzr | `FALL_THROUGH`
<a id="insn-004ec2f8"></a> `004ec2f8` | `e6 03 14 aa` | mov x6,x20 | `FALL_THROUGH`
<a id="insn-004ec2fc"></a> `004ec2fc` | `2e d9 ff 97` | bl 0x004e27b4 | `UNCONDITIONAL_CALL`
<a id="insn-004ec300"></a> `004ec300` | `f4 03 40 f9` | ldr x20,[sp] | `FALL_THROUGH`
<a id="insn-004ec304"></a> `004ec304` | `f5 3b 00 90` | adrp x21,0xc68000 | `FALL_THROUGH`
<a id="insn-004ec308"></a> `004ec308` | `54 01 00 b4` | cbz x20,0x004ec330 | `CONDITIONAL_JUMP`
<a id="insn-004ec30c"></a> `004ec30c` | `f4 07 00 f9` | str x20,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-004ec310"></a> `004ec310` | `e8 0b 40 f9` | ldr x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-004ec314"></a> `004ec314` | `a9 ee 43 f9` | ldr x9,[x21, #0x7d8] | `FALL_THROUGH`
<a id="insn-004ec318"></a> `004ec318` | `02 01 14 cb` | sub x2,x8,x20 | `FALL_THROUGH`
<a id="insn-004ec31c"></a> `004ec31c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-004ec320"></a> `004ec320` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-004ec324"></a> `004ec324` | `20 01 3f d6` | blr x9 | `COMPUTED_CALL`
<a id="insn-004ec328"></a> `004ec328` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-004ec32c"></a> `004ec32c` | `f5 b4 1d 94` | bl 0x00c59700 | `UNCONDITIONAL_CALL`
<a id="insn-004ec330"></a> `004ec330` | `00 e4 00 6f` | movi v0.2D,#0x0 | `FALL_THROUGH`
<a id="insn-004ec334"></a> `004ec334` | `e0 83 00 ad` | stp q0,q0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-004ec338"></a> `004ec338` | `e0 03 80 3d` | str q0,[sp] | `FALL_THROUGH`
<a id="insn-004ec33c"></a> `004ec33c` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-004ec340"></a> `004ec340` | `01 02 80 52` | mov w1,#0x10 | `FALL_THROUGH`
<a id="insn-004ec344"></a> `004ec344` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-004ec348"></a> `004ec348` | `02 b5 1d 94` | bl 0x00c59750 | `UNCONDITIONAL_CALL`
<a id="insn-004ec34c"></a> `004ec34c` | `a8 83 59 f8` | ldur x8,[x29, #-0x68] | `FALL_THROUGH`
<a id="insn-004ec350"></a> `004ec350` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-004ec354"></a> `004ec354` | `a0 a3 01 d1` | sub x0,x29,#0x68 | `FALL_THROUGH`
<a id="insn-004ec358"></a> `004ec358` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-004ec35c"></a> `004ec35c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-004ec360"></a> `004ec360` | `a3 a3 7d a9` | ldp x3,x8,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-004ec364"></a> `004ec364` | `04 01 03 cb` | sub x4,x8,x3 | `FALL_THROUGH`
<a id="insn-004ec368"></a> `004ec368` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-004ec36c"></a> `004ec36c` | `81 00 80 52` | mov w1,#0x4 | `FALL_THROUGH`
<a id="insn-004ec370"></a> `004ec370` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-004ec374"></a> `004ec374` | `53 b5 1d 94` | bl 0x00c598c0 | `UNCONDITIONAL_CALL`
<a id="insn-004ec378"></a> `004ec378` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-004ec37c"></a> `004ec37c` | `fd b4 1d 94` | bl 0x00c59770 | `UNCONDITIONAL_CALL`
<a id="insn-004ec380"></a> `004ec380` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-004ec384"></a> `004ec384` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-004ec388"></a> `004ec388` | `62 eb fe 97` | bl 0x004a7110 | `UNCONDITIONAL_CALL`
<a id="insn-004ec38c"></a> `004ec38c` | `f4 0f 40 f9` | ldr x20,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-004ec390"></a> `004ec390` | `f4 01 00 b4` | cbz x20,0x004ec3cc | `CONDITIONAL_JUMP`
<a id="insn-004ec394"></a> `004ec394` | `f3 13 40 f9` | ldr x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-004ec398"></a> `004ec398` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-004ec39c"></a> `004ec39c` | `7f 02 14 eb` | cmp x19,x20 | `FALL_THROUGH`
<a id="insn-004ec3a0"></a> `004ec3a0` | `20 01 00 54` | b.eq 0x004ec3c4 | `CONDITIONAL_JUMP`
<a id="insn-004ec3a4"></a> `004ec3a4` | `f6 03 00 91` | mov x22,sp | `FALL_THROUGH`
<a id="insn-004ec3a8"></a> `004ec3a8` | `73 e2 00 d1` | sub x19,x19,#0x38 | `FALL_THROUGH`
<a id="insn-004ec3ac"></a> `004ec3ac` | `c0 a2 00 91` | add x0,x22,#0x28 | `FALL_THROUGH`
<a id="insn-004ec3b0"></a> `004ec3b0` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-004ec3b4"></a> `004ec3b4` | `cb 26 01 94` | bl 0x00535ee0 | `UNCONDITIONAL_CALL`
<a id="insn-004ec3b8"></a> `004ec3b8` | `7f 02 14 eb` | cmp x19,x20 | `FALL_THROUGH`
<a id="insn-004ec3bc"></a> `004ec3bc` | `61 ff ff 54` | b.ne 0x004ec3a8 | `CONDITIONAL_JUMP`
<a id="insn-004ec3c0"></a> `004ec3c0` | `e0 0f 40 f9` | ldr x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-004ec3c4"></a> `004ec3c4` | `f4 13 00 f9` | str x20,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-004ec3c8"></a> `004ec3c8` | `e2 b2 1d 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-004ec3cc"></a> `004ec3cc` | `f3 03 40 f9` | ldr x19,[sp] | `FALL_THROUGH`
<a id="insn-004ec3d0"></a> `004ec3d0` | `53 01 00 b4` | cbz x19,0x004ec3f8 | `CONDITIONAL_JUMP`
<a id="insn-004ec3d4"></a> `004ec3d4` | `f3 07 00 f9` | str x19,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-004ec3d8"></a> `004ec3d8` | `e8 0b 40 f9` | ldr x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-004ec3dc"></a> `004ec3dc` | `a9 ee 43 f9` | ldr x9,[x21, #0x7d8] | `FALL_THROUGH`
<a id="insn-004ec3e0"></a> `004ec3e0` | `02 01 13 cb` | sub x2,x8,x19 | `FALL_THROUGH`
<a id="insn-004ec3e4"></a> `004ec3e4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-004ec3e8"></a> `004ec3e8` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-004ec3ec"></a> `004ec3ec` | `20 01 3f d6` | blr x9 | `COMPUTED_CALL`
<a id="insn-004ec3f0"></a> `004ec3f0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-004ec3f4"></a> `004ec3f4` | `c3 b4 1d 94` | bl 0x00c59700 | `UNCONDITIONAL_CALL`
<a id="insn-004ec3f8"></a> `004ec3f8` | `a0 83 5d f8` | ldur x0,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-004ec3fc"></a> `004ec3fc` | `60 00 00 b4` | cbz x0,0x004ec408 | `CONDITIONAL_JUMP`
<a id="insn-004ec400"></a> `004ec400` | `a0 03 1e f8` | stur x0,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-004ec404"></a> `004ec404` | `d3 b2 1d 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-004ec408"></a> `004ec408` | `a0 03 5c f8` | ldur x0,[x29, #-0x40] | `FALL_THROUGH`
<a id="insn-004ec40c"></a> `004ec40c` | `60 00 00 b4` | cbz x0,0x004ec418 | `CONDITIONAL_JUMP`
<a id="insn-004ec410"></a> `004ec410` | `a0 83 1c f8` | stur x0,[x29, #-0x38] | `FALL_THROUGH`
<a id="insn-004ec414"></a> `004ec414` | `cf b2 1d 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-004ec418"></a> `004ec418` | `a0 83 5a f8` | ldur x0,[x29, #-0x58] | `FALL_THROUGH`
<a id="insn-004ec41c"></a> `004ec41c` | `60 00 00 b4` | cbz x0,0x004ec428 | `CONDITIONAL_JUMP`
<a id="insn-004ec420"></a> `004ec420` | `a0 03 1b f8` | stur x0,[x29, #-0x50] | `FALL_THROUGH`
<a id="insn-004ec424"></a> `004ec424` | `cb b2 1d 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-004ec428"></a> `004ec428` | `e8 a3 41 39` | ldrb w8,[sp, #0x68] | `FALL_THROUGH`
<a id="insn-004ec42c"></a> `004ec42c` | `68 00 00 36` | tbz w8,#0x0,0x004ec438 | `CONDITIONAL_JUMP`
<a id="insn-004ec430"></a> `004ec430` | `e0 3f 40 f9` | ldr x0,[sp, #0x78] | `FALL_THROUGH`
<a id="insn-004ec434"></a> `004ec434` | `c7 b2 1d 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-004ec438"></a> `004ec438` | `e8 43 41 39` | ldrb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-004ec43c"></a> `004ec43c` | `68 00 00 36` | tbz w8,#0x0,0x004ec448 | `CONDITIONAL_JUMP`
<a id="insn-004ec440"></a> `004ec440` | `e0 33 40 f9` | ldr x0,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-004ec444"></a> `004ec444` | `c3 b2 1d 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-004ec448"></a> `004ec448` | `28 17 40 f9` | ldr x8,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-004ec44c"></a> `004ec44c` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-004ec450"></a> `004ec450` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-004ec454"></a> `004ec454` | `01 0b 00 54` | b.ne 0x004ec5b4 | `CONDITIONAL_JUMP`
<a id="insn-004ec458"></a> `004ec458` | `f4 4f 57 a9` | ldp x20,x19,[sp, #0x170] | `FALL_THROUGH`
<a id="insn-004ec45c"></a> `004ec45c` | `fc 9b 40 f9` | ldr x28,[sp, #0x130] | `FALL_THROUGH`
<a id="insn-004ec460"></a> `004ec460` | `f6 57 56 a9` | ldp x22,x21,[sp, #0x160] | `FALL_THROUGH`
<a id="insn-004ec464"></a> `004ec464` | `f8 5f 55 a9` | ldp x24,x23,[sp, #0x150] | `FALL_THROUGH`
<a id="insn-004ec468"></a> `004ec468` | `fa 67 54 a9` | ldp x26,x25,[sp, #0x140] | `FALL_THROUGH`
<a id="insn-004ec46c"></a> `004ec46c` | `fd 7b 52 a9` | ldp x29,x30,[sp, #0x120] | `FALL_THROUGH`
<a id="insn-004ec470"></a> `004ec470` | `ff 03 06 91` | add sp,sp,#0x180 | `FALL_THROUGH`
<a id="insn-004ec474"></a> `004ec474` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-004ec478"></a> `004ec478` | `00 04 80 52` | mov w0,#0x20 | `FALL_THROUGH`
<a id="insn-004ec47c"></a> `004ec47c` | `c5 b2 1d 94` | bl 0x00c58f90 | `UNCONDITIONAL_CALL`
<a id="insn-004ec480"></a> `004ec480` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-004ec484"></a> `004ec484` | `80 ee ff 90` | adrp x0,0x2bc000 | `FALL_THROUGH`
<a id="insn-004ec488"></a> `004ec488` | `00 90 1d 91` | add x0,x0,#0x764 | `FALL_THROUGH`
<a id="insn-004ec48c"></a> `004ec48c` | `a8 03 02 d1` | sub x8,x29,#0x80 | `FALL_THROUGH`
<a id="insn-004ec490"></a> `004ec490` | `e1 03 18 aa` | mov x1,x24 | `FALL_THROUGH`
<a id="insn-004ec494"></a> `004ec494` | `2f b3 1d 94` | bl 0x00c59150 | `UNCONDITIONAL_CALL`
<a id="insn-004ec498"></a> `004ec498` | `35 00 80 52` | mov w21,#0x1 | `FALL_THROUGH`
<a id="insn-004ec49c"></a> `004ec49c` | `a1 03 02 d1` | sub x1,x29,#0x80 | `FALL_THROUGH`
<a id="insn-004ec4a0"></a> `004ec4a0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-004ec4a4"></a> `004ec4a4` | `ef b4 1d 94` | bl 0x00c59860 | `UNCONDITIONAL_CALL`
<a id="insn-004ec4a8"></a> `004ec4a8` | `28 17 40 f9` | ldr x8,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-004ec4ac"></a> `004ec4ac` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-004ec4b0"></a> `004ec4b0` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-004ec4b4"></a> `004ec4b4` | `01 08 00 54` | b.ne 0x004ec5b4 | `CONDITIONAL_JUMP`
<a id="insn-004ec4b8"></a> `004ec4b8` | `61 3d 00 f0` | adrp x1,0xc9b000 | `FALL_THROUGH`
<a id="insn-004ec4bc"></a> `004ec4bc` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-004ec4c0"></a> `004ec4c0` | `42 b8 24 10` | adr x2,0x535bc8 | `FALL_THROUGH`
<a id="insn-004ec4c4"></a> `004ec4c4` | `21 14 47 f9` | ldr x1,[x1, #0xe28] | `FALL_THROUGH`
<a id="insn-004ec4c8"></a> `004ec4c8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-004ec4cc"></a> `004ec4cc` | `f5 03 1f 2a` | mov w21,wzr | `FALL_THROUGH`
<a id="insn-004ec4d0"></a> `004ec4d0` | `b8 b2 1d 94` | bl 0x00c58fb0 | `CALL_TERMINATOR`
<a id="insn-004ec5b4"></a> `004ec5b4` | `73 b2 1d 94` | bl 0x00c58f80 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`004ebfcc`](#insn-004ebfcc) 範囲 `[['004ebfcc', '004ec043']]`
  - `CONDITIONAL_JUMP` [`004ec040`](#insn-004ec040) → [`004ec05c`](#insn-004ec05c)
  - `FALL_THROUGH` [`004ec040`](#insn-004ec040) → [`004ec044`](#insn-004ec044)
- ブロック [`004ec044`](#insn-004ec044) 範囲 `[['004ec044', '004ec047']]`
  - `CONDITIONAL_JUMP` [`004ec044`](#insn-004ec044) → [`004ec0dc`](#insn-004ec0dc)
  - `FALL_THROUGH` [`004ec044`](#insn-004ec044) → [`004ec048`](#insn-004ec048)
- ブロック [`004ec048`](#insn-004ec048) 範囲 `[['004ec048', '004ec05b']]`
  - `UNCONDITIONAL_JUMP` [`004ec058`](#insn-004ec058) → [`004ec0e8`](#insn-004ec0e8)
- ブロック [`004ec05c`](#insn-004ec05c) 範囲 `[['004ec05c', '004ec077']]`
  - `CONDITIONAL_JUMP` [`004ec074`](#insn-004ec074) → [`004ec26c`](#insn-004ec26c)
  - `FALL_THROUGH` [`004ec074`](#insn-004ec074) → [`004ec078`](#insn-004ec078)
- ブロック [`004ec078`](#insn-004ec078) 範囲 `[['004ec078', '004ec07f']]`
  - `CONDITIONAL_JUMP` [`004ec07c`](#insn-004ec07c) → [`004ec0b8`](#insn-004ec0b8)
  - `FALL_THROUGH` [`004ec07c`](#insn-004ec07c) → [`004ec080`](#insn-004ec080)
- ブロック [`004ec080`](#insn-004ec080) 範囲 `[['004ec080', '004ec0b7']]`
  - `CONDITIONAL_JUMP` [`004ec0b4`](#insn-004ec0b4) → [`004ec298`](#insn-004ec298)
  - `FALL_THROUGH` [`004ec0b4`](#insn-004ec0b4) → [`004ec0b8`](#insn-004ec0b8)
- ブロック [`004ec0b8`](#insn-004ec0b8) 範囲 `[['004ec0b8', '004ec0db']]`
  - `UNCONDITIONAL_JUMP` [`004ec0d8`](#insn-004ec0d8) → [`004ec2b8`](#insn-004ec2b8)
- ブロック [`004ec0dc`](#insn-004ec0dc) 範囲 `[['004ec0dc', '004ec0e7']]`
  - `FALL_THROUGH` [`004ec0e4`](#insn-004ec0e4) → [`004ec0e8`](#insn-004ec0e8)
- ブロック [`004ec0e8`](#insn-004ec0e8) 範囲 `[['004ec0e8', '004ec0fb']]`
  - `CONDITIONAL_JUMP` [`004ec0f8`](#insn-004ec0f8) → [`004ec104`](#insn-004ec104)
  - `FALL_THROUGH` [`004ec0f8`](#insn-004ec0f8) → [`004ec0fc`](#insn-004ec0fc)
- ブロック [`004ec0fc`](#insn-004ec0fc) 範囲 `[['004ec0fc', '004ec103']]`
  - `FALL_THROUGH` [`004ec100`](#insn-004ec100) → [`004ec104`](#insn-004ec104)
- ブロック [`004ec104`](#insn-004ec104) 範囲 `[['004ec104', '004ec11f']]`
  - `CONDITIONAL_JUMP` [`004ec11c`](#insn-004ec11c) → [`004ec478`](#insn-004ec478)
  - `FALL_THROUGH` [`004ec11c`](#insn-004ec11c) → [`004ec120`](#insn-004ec120)
- ブロック [`004ec120`](#insn-004ec120) 範囲 `[['004ec120', '004ec15f']]`
  - `CONDITIONAL_JUMP` [`004ec15c`](#insn-004ec15c) → [`004ec478`](#insn-004ec478)
  - `FALL_THROUGH` [`004ec15c`](#insn-004ec15c) → [`004ec160`](#insn-004ec160)
- ブロック [`004ec160`](#insn-004ec160) 範囲 `[['004ec160', '004ec16f']]`
  - `CONDITIONAL_JUMP` [`004ec16c`](#insn-004ec16c) → [`004ec478`](#insn-004ec478)
  - `FALL_THROUGH` [`004ec16c`](#insn-004ec16c) → [`004ec170`](#insn-004ec170)
- ブロック [`004ec170`](#insn-004ec170) 範囲 `[['004ec170', '004ec1b7']]`
  - `CONDITIONAL_JUMP` [`004ec1b4`](#insn-004ec1b4) → [`004ec1fc`](#insn-004ec1fc)
  - `FALL_THROUGH` [`004ec1b4`](#insn-004ec1b4) → [`004ec1b8`](#insn-004ec1b8)
- ブロック [`004ec1b8`](#insn-004ec1b8) 範囲 `[['004ec1b8', '004ec1c7']]`
  - `CONDITIONAL_JUMP` [`004ec1c4`](#insn-004ec1c4) → [`004ec1f4`](#insn-004ec1f4)
  - `FALL_THROUGH` [`004ec1c4`](#insn-004ec1c4) → [`004ec1c8`](#insn-004ec1c8)
- ブロック [`004ec1c8`](#insn-004ec1c8) 範囲 `[['004ec1c8', '004ec1cf']]`
  - `UNCONDITIONAL_JUMP` [`004ec1cc`](#insn-004ec1cc) → [`004ec1dc`](#insn-004ec1dc)
- ブロック [`004ec1d0`](#insn-004ec1d0) 範囲 `[['004ec1d0', '004ec1db']]`
  - `CONDITIONAL_JUMP` [`004ec1d8`](#insn-004ec1d8) → [`004ec1f0`](#insn-004ec1f0)
  - `FALL_THROUGH` [`004ec1d8`](#insn-004ec1d8) → [`004ec1dc`](#insn-004ec1dc)
- ブロック [`004ec1dc`](#insn-004ec1dc) 範囲 `[['004ec1dc', '004ec1e3']]`
  - `CONDITIONAL_JUMP` [`004ec1e0`](#insn-004ec1e0) → [`004ec1d0`](#insn-004ec1d0)
  - `FALL_THROUGH` [`004ec1e0`](#insn-004ec1e0) → [`004ec1e4`](#insn-004ec1e4)
- ブロック [`004ec1e4`](#insn-004ec1e4) 範囲 `[['004ec1e4', '004ec1ef']]`
  - `UNCONDITIONAL_JUMP` [`004ec1ec`](#insn-004ec1ec) → [`004ec1d0`](#insn-004ec1d0)
- ブロック [`004ec1f0`](#insn-004ec1f0) 範囲 `[['004ec1f0', '004ec1f3']]`
  - `FALL_THROUGH` [`004ec1f0`](#insn-004ec1f0) → [`004ec1f4`](#insn-004ec1f4)
- ブロック [`004ec1f4`](#insn-004ec1f4) 範囲 `[['004ec1f4', '004ec1fb']]`
  - `FALL_THROUGH` [`004ec1f8`](#insn-004ec1f8) → [`004ec1fc`](#insn-004ec1fc)
- ブロック [`004ec1fc`](#insn-004ec1fc) 範囲 `[['004ec1fc', '004ec203']]`
  - `CONDITIONAL_JUMP` [`004ec200`](#insn-004ec200) → [`004ec248`](#insn-004ec248)
  - `FALL_THROUGH` [`004ec200`](#insn-004ec200) → [`004ec204`](#insn-004ec204)
- ブロック [`004ec204`](#insn-004ec204) 範囲 `[['004ec204', '004ec213']]`
  - `CONDITIONAL_JUMP` [`004ec210`](#insn-004ec210) → [`004ec240`](#insn-004ec240)
  - `FALL_THROUGH` [`004ec210`](#insn-004ec210) → [`004ec214`](#insn-004ec214)
- ブロック [`004ec214`](#insn-004ec214) 範囲 `[['004ec214', '004ec21b']]`
  - `UNCONDITIONAL_JUMP` [`004ec218`](#insn-004ec218) → [`004ec228`](#insn-004ec228)
- ブロック [`004ec21c`](#insn-004ec21c) 範囲 `[['004ec21c', '004ec227']]`
  - `CONDITIONAL_JUMP` [`004ec224`](#insn-004ec224) → [`004ec23c`](#insn-004ec23c)
  - `FALL_THROUGH` [`004ec224`](#insn-004ec224) → [`004ec228`](#insn-004ec228)
- ブロック [`004ec228`](#insn-004ec228) 範囲 `[['004ec228', '004ec22f']]`
  - `CONDITIONAL_JUMP` [`004ec22c`](#insn-004ec22c) → [`004ec21c`](#insn-004ec21c)
  - `FALL_THROUGH` [`004ec22c`](#insn-004ec22c) → [`004ec230`](#insn-004ec230)
- ブロック [`004ec230`](#insn-004ec230) 範囲 `[['004ec230', '004ec23b']]`
  - `UNCONDITIONAL_JUMP` [`004ec238`](#insn-004ec238) → [`004ec21c`](#insn-004ec21c)
- ブロック [`004ec23c`](#insn-004ec23c) 範囲 `[['004ec23c', '004ec23f']]`
  - `FALL_THROUGH` [`004ec23c`](#insn-004ec23c) → [`004ec240`](#insn-004ec240)
- ブロック [`004ec240`](#insn-004ec240) 範囲 `[['004ec240', '004ec247']]`
  - `FALL_THROUGH` [`004ec244`](#insn-004ec244) → [`004ec248`](#insn-004ec248)
- ブロック [`004ec248`](#insn-004ec248) 範囲 `[['004ec248', '004ec24f']]`
  - `CONDITIONAL_JUMP` [`004ec24c`](#insn-004ec24c) → [`004ec258`](#insn-004ec258)
  - `FALL_THROUGH` [`004ec24c`](#insn-004ec24c) → [`004ec250`](#insn-004ec250)
- ブロック [`004ec250`](#insn-004ec250) 範囲 `[['004ec250', '004ec257']]`
  - `FALL_THROUGH` [`004ec254`](#insn-004ec254) → [`004ec258`](#insn-004ec258)
- ブロック [`004ec258`](#insn-004ec258) 範囲 `[['004ec258', '004ec25f']]`
  - `CONDITIONAL_JUMP` [`004ec25c`](#insn-004ec25c) → [`004ec2b8`](#insn-004ec2b8)
  - `FALL_THROUGH` [`004ec25c`](#insn-004ec25c) → [`004ec260`](#insn-004ec260)
- ブロック [`004ec260`](#insn-004ec260) 範囲 `[['004ec260', '004ec26b']]`
  - `UNCONDITIONAL_JUMP` [`004ec268`](#insn-004ec268) → [`004ec2b8`](#insn-004ec2b8)
- ブロック [`004ec26c`](#insn-004ec26c) 範囲 `[['004ec26c', '004ec297']]`
  - `CONDITIONAL_JUMP` [`004ec294`](#insn-004ec294) → [`004ec0b8`](#insn-004ec0b8)
  - `FALL_THROUGH` [`004ec294`](#insn-004ec294) → [`004ec298`](#insn-004ec298)
- ブロック [`004ec298`](#insn-004ec298) 範囲 `[['004ec298', '004ec2b7']]`
  - `FALL_THROUGH` [`004ec2b4`](#insn-004ec2b4) → [`004ec2b8`](#insn-004ec2b8)
- ブロック [`004ec2b8`](#insn-004ec2b8) 範囲 `[['004ec2b8', '004ec2bf']]`
  - `CONDITIONAL_JUMP` [`004ec2bc`](#insn-004ec2bc) → [`004ec2c8`](#insn-004ec2c8)
  - `FALL_THROUGH` [`004ec2bc`](#insn-004ec2bc) → [`004ec2c0`](#insn-004ec2c0)
- ブロック [`004ec2c0`](#insn-004ec2c0) 範囲 `[['004ec2c0', '004ec2c7']]`
  - `FALL_THROUGH` [`004ec2c4`](#insn-004ec2c4) → [`004ec2c8`](#insn-004ec2c8)
- ブロック [`004ec2c8`](#insn-004ec2c8) 範囲 `[['004ec2c8', '004ec30b']]`
  - `CONDITIONAL_JUMP` [`004ec308`](#insn-004ec308) → [`004ec330`](#insn-004ec330)
  - `FALL_THROUGH` [`004ec308`](#insn-004ec308) → [`004ec30c`](#insn-004ec30c)
- ブロック [`004ec30c`](#insn-004ec30c) 範囲 `[['004ec30c', '004ec32f']]`
  - `FALL_THROUGH` [`004ec32c`](#insn-004ec32c) → [`004ec330`](#insn-004ec330)
- ブロック [`004ec330`](#insn-004ec330) 範囲 `[['004ec330', '004ec393']]`
  - `CONDITIONAL_JUMP` [`004ec390`](#insn-004ec390) → [`004ec3cc`](#insn-004ec3cc)
  - `FALL_THROUGH` [`004ec390`](#insn-004ec390) → [`004ec394`](#insn-004ec394)
- ブロック [`004ec394`](#insn-004ec394) 範囲 `[['004ec394', '004ec3a3']]`
  - `CONDITIONAL_JUMP` [`004ec3a0`](#insn-004ec3a0) → [`004ec3c4`](#insn-004ec3c4)
  - `FALL_THROUGH` [`004ec3a0`](#insn-004ec3a0) → [`004ec3a4`](#insn-004ec3a4)
- ブロック [`004ec3a4`](#insn-004ec3a4) 範囲 `[['004ec3a4', '004ec3a7']]`
  - `FALL_THROUGH` [`004ec3a4`](#insn-004ec3a4) → [`004ec3a8`](#insn-004ec3a8)
- ブロック [`004ec3a8`](#insn-004ec3a8) 範囲 `[['004ec3a8', '004ec3bf']]`
  - `CONDITIONAL_JUMP` [`004ec3bc`](#insn-004ec3bc) → [`004ec3a8`](#insn-004ec3a8)
  - `FALL_THROUGH` [`004ec3bc`](#insn-004ec3bc) → [`004ec3c0`](#insn-004ec3c0)
- ブロック [`004ec3c0`](#insn-004ec3c0) 範囲 `[['004ec3c0', '004ec3c3']]`
  - `FALL_THROUGH` [`004ec3c0`](#insn-004ec3c0) → [`004ec3c4`](#insn-004ec3c4)
- ブロック [`004ec3c4`](#insn-004ec3c4) 範囲 `[['004ec3c4', '004ec3cb']]`
  - `FALL_THROUGH` [`004ec3c8`](#insn-004ec3c8) → [`004ec3cc`](#insn-004ec3cc)
- ブロック [`004ec3cc`](#insn-004ec3cc) 範囲 `[['004ec3cc', '004ec3d3']]`
  - `CONDITIONAL_JUMP` [`004ec3d0`](#insn-004ec3d0) → [`004ec3f8`](#insn-004ec3f8)
  - `FALL_THROUGH` [`004ec3d0`](#insn-004ec3d0) → [`004ec3d4`](#insn-004ec3d4)
- ブロック [`004ec3d4`](#insn-004ec3d4) 範囲 `[['004ec3d4', '004ec3f7']]`
  - `FALL_THROUGH` [`004ec3f4`](#insn-004ec3f4) → [`004ec3f8`](#insn-004ec3f8)
- ブロック [`004ec3f8`](#insn-004ec3f8) 範囲 `[['004ec3f8', '004ec3ff']]`
  - `CONDITIONAL_JUMP` [`004ec3fc`](#insn-004ec3fc) → [`004ec408`](#insn-004ec408)
  - `FALL_THROUGH` [`004ec3fc`](#insn-004ec3fc) → [`004ec400`](#insn-004ec400)
- ブロック [`004ec400`](#insn-004ec400) 範囲 `[['004ec400', '004ec407']]`
  - `FALL_THROUGH` [`004ec404`](#insn-004ec404) → [`004ec408`](#insn-004ec408)
- ブロック [`004ec408`](#insn-004ec408) 範囲 `[['004ec408', '004ec40f']]`
  - `CONDITIONAL_JUMP` [`004ec40c`](#insn-004ec40c) → [`004ec418`](#insn-004ec418)
  - `FALL_THROUGH` [`004ec40c`](#insn-004ec40c) → [`004ec410`](#insn-004ec410)
- ブロック [`004ec410`](#insn-004ec410) 範囲 `[['004ec410', '004ec417']]`
  - `FALL_THROUGH` [`004ec414`](#insn-004ec414) → [`004ec418`](#insn-004ec418)
- ブロック [`004ec418`](#insn-004ec418) 範囲 `[['004ec418', '004ec41f']]`
  - `CONDITIONAL_JUMP` [`004ec41c`](#insn-004ec41c) → [`004ec428`](#insn-004ec428)
  - `FALL_THROUGH` [`004ec41c`](#insn-004ec41c) → [`004ec420`](#insn-004ec420)
- ブロック [`004ec420`](#insn-004ec420) 範囲 `[['004ec420', '004ec427']]`
  - `FALL_THROUGH` [`004ec424`](#insn-004ec424) → [`004ec428`](#insn-004ec428)
- ブロック [`004ec428`](#insn-004ec428) 範囲 `[['004ec428', '004ec42f']]`
  - `CONDITIONAL_JUMP` [`004ec42c`](#insn-004ec42c) → [`004ec438`](#insn-004ec438)
  - `FALL_THROUGH` [`004ec42c`](#insn-004ec42c) → [`004ec430`](#insn-004ec430)
- ブロック [`004ec430`](#insn-004ec430) 範囲 `[['004ec430', '004ec437']]`
  - `FALL_THROUGH` [`004ec434`](#insn-004ec434) → [`004ec438`](#insn-004ec438)
- ブロック [`004ec438`](#insn-004ec438) 範囲 `[['004ec438', '004ec43f']]`
  - `CONDITIONAL_JUMP` [`004ec43c`](#insn-004ec43c) → [`004ec448`](#insn-004ec448)
  - `FALL_THROUGH` [`004ec43c`](#insn-004ec43c) → [`004ec440`](#insn-004ec440)
- ブロック [`004ec440`](#insn-004ec440) 範囲 `[['004ec440', '004ec447']]`
  - `FALL_THROUGH` [`004ec444`](#insn-004ec444) → [`004ec448`](#insn-004ec448)
- ブロック [`004ec448`](#insn-004ec448) 範囲 `[['004ec448', '004ec457']]`
  - `CONDITIONAL_JUMP` [`004ec454`](#insn-004ec454) → [`004ec5b4`](#insn-004ec5b4)
  - `FALL_THROUGH` [`004ec454`](#insn-004ec454) → [`004ec458`](#insn-004ec458)
- ブロック [`004ec458`](#insn-004ec458) 範囲 `[['004ec458', '004ec477']]`
- ブロック [`004ec478`](#insn-004ec478) 範囲 `[['004ec478', '004ec4b7']]`
  - `CONDITIONAL_JUMP` [`004ec4b4`](#insn-004ec4b4) → [`004ec5b4`](#insn-004ec5b4)
  - `FALL_THROUGH` [`004ec4b4`](#insn-004ec4b4) → [`004ec4b8`](#insn-004ec4b8)
- ブロック [`004ec4b8`](#insn-004ec4b8) 範囲 `[['004ec4b8', '004ec4d3']]`
- ブロック [`004ec5b4`](#insn-004ec5b4) 範囲 `[['004ec5b4', '004ec5b7']]`

## 命令位置別の参照

- [`004ebfd0`](#insn-004ebfd0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ebfd4`](#insn-004ebfd4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ebfd8`](#insn-004ebfd8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ebfdc`](#insn-004ebfdc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ebfe0`](#insn-004ebfe0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ebfe4`](#insn-004ebfe4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec010`](#insn-004ec010) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec040`](#insn-004ec040) → [`004ec05c`](#insn-004ec05c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec044`](#insn-004ec044) → [`004ec0dc`](#insn-004ec0dc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec050`](#insn-004ec050) → `Stack[-0x180]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec054`](#insn-004ec054) → `Stack[-0x170]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec058`](#insn-004ec058) → [`004ec0e8`](#insn-004ec0e8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec05c`](#insn-004ec05c) → `Stack[-0x148]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec060`](#insn-004ec060) → `Stack[-0x140]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec074`](#insn-004ec074) → [`004ec26c`](#insn-004ec26c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec07c`](#insn-004ec07c) → [`004ec0b8`](#insn-004ec0b8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec080`](#insn-004ec080) → `Stack[-0x138]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec098`](#insn-004ec098) → `Stack[-0x147]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec0a0`](#insn-004ec0a0) → `Stack[-0x13f]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec0b4`](#insn-004ec0b4) → [`004ec298`](#insn-004ec298) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec0c8`](#insn-004ec0c8) → `002bed04`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`004ec0c8`](#insn-004ec0c8) → `002a9c1f`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`004ec0c8`](#insn-004ec0c8) → `Stack[-0xc8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec0d4`](#insn-004ec0d4) → [`00536c3c`](../00536/00536c3c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00536c3c` · 推定シンボル `None` · 推定型 `None`
- [`004ec0d8`](#insn-004ec0d8) → [`004ec2b8`](#insn-004ec2b8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec0e4`](#insn-004ec0e4) → [`0043be80`](../0043b/0043be80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043be80` · 推定シンボル `None` · 推定型 `None`
- [`004ec0f0`](#insn-004ec0f0) → [`00c59de0`](../00c59/00c59de0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59de0` · 推定シンボル `None` · 推定型 `None`
- [`004ec0f4`](#insn-004ec0f4) → `Stack[-0x180]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec0f8`](#insn-004ec0f8) → [`004ec104`](#insn-004ec104) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec0fc`](#insn-004ec0fc) → `Stack[-0x170]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec100`](#insn-004ec100) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`004ec104`](#insn-004ec104) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec108`](#insn-004ec108) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec11c`](#insn-004ec11c) → [`004ec478`](#insn-004ec478) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec120`](#insn-004ec120) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec13c`](#insn-004ec13c) → `Stack[-0xaf]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec140`](#insn-004ec140) → `Stack[-0xa7]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec15c`](#insn-004ec15c) → [`004ec478`](#insn-004ec478) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec160`](#insn-004ec160) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec16c`](#insn-004ec16c) → [`004ec478`](#insn-004ec478) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec17c`](#insn-004ec17c) → [`00c59c30`](../00c59/00c59c30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59c30` · 推定シンボル `None` · 推定型 `None`
- [`004ec18c`](#insn-004ec18c) → [`00c59c30`](../00c59/00c59c30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59c30` · 推定シンボル `None` · 推定型 `None`
- [`004ec190`](#insn-004ec190) → `Stack[-0xe0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec194`](#insn-004ec194) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec198`](#insn-004ec198) → `Stack[-0xf8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec19c`](#insn-004ec19c) → `Stack[-0xe8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec1a0`](#insn-004ec1a0) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec1a4`](#insn-004ec1a4) → `Stack[-0x130]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec1a8`](#insn-004ec1a8) → `Stack[-0x120]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec1ac`](#insn-004ec1ac) → `Stack[-0x118]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec1b0`](#insn-004ec1b0) → `Stack[-0x108]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec1b4`](#insn-004ec1b4) → [`004ec1fc`](#insn-004ec1fc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec1b8`](#insn-004ec1b8) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec1c4`](#insn-004ec1c4) → [`004ec1f4`](#insn-004ec1f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec1cc`](#insn-004ec1cc) → [`004ec1dc`](#insn-004ec1dc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec1d8`](#insn-004ec1d8) → [`004ec1f0`](#insn-004ec1f0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec1e0`](#insn-004ec1e0) → [`004ec1d0`](#insn-004ec1d0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec1e8`](#insn-004ec1e8) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`004ec1ec`](#insn-004ec1ec) → [`004ec1d0`](#insn-004ec1d0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec1f0`](#insn-004ec1f0) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec1f4`](#insn-004ec1f4) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec1f8`](#insn-004ec1f8) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`004ec1fc`](#insn-004ec1fc) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec200`](#insn-004ec200) → [`004ec248`](#insn-004ec248) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec204`](#insn-004ec204) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec210`](#insn-004ec210) → [`004ec240`](#insn-004ec240) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec218`](#insn-004ec218) → [`004ec228`](#insn-004ec228) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec224`](#insn-004ec224) → [`004ec23c`](#insn-004ec23c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec22c`](#insn-004ec22c) → [`004ec21c`](#insn-004ec21c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec234`](#insn-004ec234) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`004ec238`](#insn-004ec238) → [`004ec21c`](#insn-004ec21c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec23c`](#insn-004ec23c) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec240`](#insn-004ec240) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec244`](#insn-004ec244) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`004ec248`](#insn-004ec248) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec24c`](#insn-004ec24c) → [`004ec258`](#insn-004ec258) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec250`](#insn-004ec250) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec254`](#insn-004ec254) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`004ec258`](#insn-004ec258) → `Stack[-0xc8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec25c`](#insn-004ec25c) → [`004ec2b8`](#insn-004ec2b8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec260`](#insn-004ec260) → `Stack[-0xb8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec264`](#insn-004ec264) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`004ec268`](#insn-004ec268) → [`004ec2b8`](#insn-004ec2b8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec26c`](#insn-004ec26c) → `Stack[-0x138]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec284`](#insn-004ec284) → `Stack[-0x147]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec294`](#insn-004ec294) → [`004ec0b8`](#insn-004ec0b8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec2a8`](#insn-004ec2a8) → `002ab43e`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`004ec2a8`](#insn-004ec2a8) → `002bb373`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`004ec2a8`](#insn-004ec2a8) → `Stack[-0xc8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec2b4`](#insn-004ec2b4) → [`00536c3c`](../00536/00536c3c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00536c3c` · 推定シンボル `None` · 推定型 `None`
- [`004ec2b8`](#insn-004ec2b8) → `Stack[-0x148]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec2bc`](#insn-004ec2bc) → [`004ec2c8`](#insn-004ec2c8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec2c0`](#insn-004ec2c0) → `Stack[-0x138]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec2c4`](#insn-004ec2c4) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`004ec2d0`](#insn-004ec2d0) → [`00c5a680`](../00c5a/00c5a680.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a680` · 推定シンボル `None` · 推定型 `None`
- [`004ec2d8`](#insn-004ec2d8) → `Stack[-0xe0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec2fc`](#insn-004ec2fc) → [`004e27b4`](../004e2/004e27b4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004e27b4` · 推定シンボル `None` · 推定型 `None`
- [`004ec300`](#insn-004ec300) → `Stack[-0x180]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec308`](#insn-004ec308) → [`004ec330`](#insn-004ec330) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec30c`](#insn-004ec30c) → `Stack[-0x178]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec310`](#insn-004ec310) → `Stack[-0x170]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec314`](#insn-004ec314) → `00c687d8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004ec324`](#insn-004ec324) → [`0112b058`](../0112b/0112b058.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `0112b058` · 推定シンボル `None` · 推定型 `None`
- [`004ec32c`](#insn-004ec32c) → [`00c59700`](../00c59/00c59700.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59700` · 推定シンボル `None` · 推定型 `None`
- [`004ec334`](#insn-004ec334) → `Stack[-0x170]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec338`](#insn-004ec338) → `Stack[-0x180]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec348`](#insn-004ec348) → [`00c59750`](../00c59/00c59750.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59750` · 推定シンボル `None` · 推定型 `None`
- [`004ec34c`](#insn-004ec34c) → `Stack[-0xc8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec360`](#insn-004ec360) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec374`](#insn-004ec374) → [`00c598c0`](../00c59/00c598c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c598c0` · 推定シンボル `None` · 推定型 `None`
- [`004ec37c`](#insn-004ec37c) → [`00c59770`](../00c59/00c59770.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59770` · 推定シンボル `None` · 推定型 `None`
- [`004ec388`](#insn-004ec388) → [`004a7110`](../004a7/004a7110.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004a7110` · 推定シンボル `None` · 推定型 `None`
- [`004ec38c`](#insn-004ec38c) → `Stack[-0x168]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec390`](#insn-004ec390) → [`004ec3cc`](#insn-004ec3cc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec394`](#insn-004ec394) → `Stack[-0x160]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec3a0`](#insn-004ec3a0) → [`004ec3c4`](#insn-004ec3c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec3b4`](#insn-004ec3b4) → [`00535ee0`](../00535/00535ee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00535ee0` · 推定シンボル `None` · 推定型 `None`
- [`004ec3bc`](#insn-004ec3bc) → [`004ec3a8`](#insn-004ec3a8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec3c0`](#insn-004ec3c0) → `Stack[-0x168]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec3c4`](#insn-004ec3c4) → `Stack[-0x160]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec3c8`](#insn-004ec3c8) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`004ec3cc`](#insn-004ec3cc) → `Stack[-0x180]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec3d0`](#insn-004ec3d0) → [`004ec3f8`](#insn-004ec3f8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec3d4`](#insn-004ec3d4) → `Stack[-0x178]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec3d8`](#insn-004ec3d8) → `Stack[-0x170]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec3dc`](#insn-004ec3dc) → `00c687d8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004ec3ec`](#insn-004ec3ec) → [`0112b058`](../0112b/0112b058.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `0112b058` · 推定シンボル `None` · 推定型 `None`
- [`004ec3f4`](#insn-004ec3f4) → [`00c59700`](../00c59/00c59700.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59700` · 推定シンボル `None` · 推定型 `None`
- [`004ec3f8`](#insn-004ec3f8) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec3fc`](#insn-004ec3fc) → [`004ec408`](#insn-004ec408) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec400`](#insn-004ec400) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec404`](#insn-004ec404) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`004ec408`](#insn-004ec408) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec40c`](#insn-004ec40c) → [`004ec418`](#insn-004ec418) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec410`](#insn-004ec410) → `Stack[-0x98]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec414`](#insn-004ec414) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`004ec418`](#insn-004ec418) → `Stack[-0xb8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec41c`](#insn-004ec41c) → [`004ec428`](#insn-004ec428) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec420`](#insn-004ec420) → `Stack[-0xb0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec424`](#insn-004ec424) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`004ec428`](#insn-004ec428) → `Stack[-0x118]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec42c`](#insn-004ec42c) → [`004ec438`](#insn-004ec438) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec430`](#insn-004ec430) → `Stack[-0x108]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec434`](#insn-004ec434) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`004ec438`](#insn-004ec438) → `Stack[-0x130]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec43c`](#insn-004ec43c) → [`004ec448`](#insn-004ec448) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec440`](#insn-004ec440) → `Stack[-0x120]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec444`](#insn-004ec444) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`004ec44c`](#insn-004ec44c) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec454`](#insn-004ec454) → [`004ec5b4`](#insn-004ec5b4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec458`](#insn-004ec458) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec45c`](#insn-004ec45c) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec460`](#insn-004ec460) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec464`](#insn-004ec464) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec468`](#insn-004ec468) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec46c`](#insn-004ec46c) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec47c`](#insn-004ec47c) → [`00c58f90`](../00c58/00c58f90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f90` · 推定シンボル `None` · 推定型 `None`
- [`004ec488`](#insn-004ec488) → `002bc764`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`004ec494`](#insn-004ec494) → [`00c59150`](../00c59/00c59150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59150` · 推定シンボル `None` · 推定型 `None`
- [`004ec4a4`](#insn-004ec4a4) → [`00c59860`](../00c59/00c59860.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59860` · 推定シンボル `None` · 推定型 `None`
- [`004ec4ac`](#insn-004ec4ac) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec4b4`](#insn-004ec4b4) → [`004ec5b4`](#insn-004ec5b4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec4c0`](#insn-004ec4c0) → [`00535bc8`](../00535/00535bc8.md) · `PARAM` · `ANALYSIS` · 関数 `00535bc8` · 推定シンボル `None` · 推定型 `None`
- [`004ec4c4`](#insn-004ec4c4) → `00c9be28`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004ec4c4`](#insn-004ec4c4) → `00c672e8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTIN5Botan9ExceptionE` · 推定型 `pointer __((offset(0x10)))`
- [`004ec4d0`](#insn-004ec4d0) → [`00c58fb0`](../00c58/00c58fb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58fb0` · 推定シンボル `None` · 推定型 `None`
- [`004ec5b4`](#insn-004ec5b4) → [`00c58f80`](../00c58/00c58f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f80` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`004ebfd0`](#insn-004ebfd0)

~~~json
{
  "source": "004ebfd0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ebfd4`](#insn-004ebfd4)

~~~json
{
  "source": "004ebfd4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ebfd8`](#insn-004ebfd8)

~~~json
{
  "source": "004ebfd8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ebfdc`](#insn-004ebfdc)

~~~json
{
  "source": "004ebfdc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ebfe0`](#insn-004ebfe0)

~~~json
{
  "source": "004ebfe0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ebfe4`](#insn-004ebfe4)

~~~json
{
  "source": "004ebfe4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec010`](#insn-004ec010)

~~~json
{
  "source": "004ec010",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec040`](#insn-004ec040)

~~~json
{
  "source": "004ec040",
  "target": "004ec05c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec044`](#insn-004ec044)

~~~json
{
  "source": "004ec044",
  "target": "004ec0dc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec050`](#insn-004ec050)

~~~json
{
  "source": "004ec050",
  "target": "Stack[-0x180]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec054`](#insn-004ec054)

~~~json
{
  "source": "004ec054",
  "target": "Stack[-0x170]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec058`](#insn-004ec058)

~~~json
{
  "source": "004ec058",
  "target": "004ec0e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec05c`](#insn-004ec05c)

~~~json
{
  "source": "004ec05c",
  "target": "Stack[-0x148]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec060`](#insn-004ec060)

~~~json
{
  "source": "004ec060",
  "target": "Stack[-0x140]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec074`](#insn-004ec074)

~~~json
{
  "source": "004ec074",
  "target": "004ec26c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec07c`](#insn-004ec07c)

~~~json
{
  "source": "004ec07c",
  "target": "004ec0b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec080`](#insn-004ec080)

~~~json
{
  "source": "004ec080",
  "target": "Stack[-0x138]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec098`](#insn-004ec098)

~~~json
{
  "source": "004ec098",
  "target": "Stack[-0x147]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec0a0`](#insn-004ec0a0)

~~~json
{
  "source": "004ec0a0",
  "target": "Stack[-0x13f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec0b4`](#insn-004ec0b4)

~~~json
{
  "source": "004ec0b4",
  "target": "004ec298",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec0c8`](#insn-004ec0c8)

~~~json
{
  "source": "004ec0c8",
  "target": "002bed04",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002bed04",
  "offset": 0,
  "size": 12,
  "datatype": "string",
  "bytes": "4145532d3235362f43424300",
  "capture_start": "002bed04",
  "capture_bytes": 12,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`004ec0c8`](#insn-004ec0c8)

~~~json
{
  "source": "004ec0c8",
  "target": "002a9c1f",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a9c1f",
  "offset": 0,
  "size": 8,
  "datatype": "string",
  "bytes": "5348412d32353600",
  "capture_start": "002a9c1f",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`004ec0c8`](#insn-004ec0c8)

~~~json
{
  "source": "004ec0c8",
  "target": "Stack[-0xc8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec0d4`](#insn-004ec0d4)

~~~json
{
  "source": "004ec0d4",
  "target": "00536c3c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ec0d8`](#insn-004ec0d8)

~~~json
{
  "source": "004ec0d8",
  "target": "004ec2b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec0e4`](#insn-004ec0e4)

~~~json
{
  "source": "004ec0e4",
  "target": "0043be80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ec0f0`](#insn-004ec0f0)

~~~json
{
  "source": "004ec0f0",
  "target": "00c59de0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ec0f4`](#insn-004ec0f4)

~~~json
{
  "source": "004ec0f4",
  "target": "Stack[-0x180]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec0f8`](#insn-004ec0f8)

~~~json
{
  "source": "004ec0f8",
  "target": "004ec104",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec0fc`](#insn-004ec0fc)

~~~json
{
  "source": "004ec0fc",
  "target": "Stack[-0x170]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec100`](#insn-004ec100)

~~~json
{
  "source": "004ec100",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ec104`](#insn-004ec104)

~~~json
{
  "source": "004ec104",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec108`](#insn-004ec108)

~~~json
{
  "source": "004ec108",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec11c`](#insn-004ec11c)

~~~json
{
  "source": "004ec11c",
  "target": "004ec478",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec120`](#insn-004ec120)

~~~json
{
  "source": "004ec120",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec13c`](#insn-004ec13c)

~~~json
{
  "source": "004ec13c",
  "target": "Stack[-0xaf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec140`](#insn-004ec140)

~~~json
{
  "source": "004ec140",
  "target": "Stack[-0xa7]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec15c`](#insn-004ec15c)

~~~json
{
  "source": "004ec15c",
  "target": "004ec478",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec160`](#insn-004ec160)

~~~json
{
  "source": "004ec160",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec16c`](#insn-004ec16c)

~~~json
{
  "source": "004ec16c",
  "target": "004ec478",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec17c`](#insn-004ec17c)

~~~json
{
  "source": "004ec17c",
  "target": "00c59c30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ec18c`](#insn-004ec18c)

~~~json
{
  "source": "004ec18c",
  "target": "00c59c30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ec190`](#insn-004ec190)

~~~json
{
  "source": "004ec190",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec194`](#insn-004ec194)

~~~json
{
  "source": "004ec194",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec198`](#insn-004ec198)

~~~json
{
  "source": "004ec198",
  "target": "Stack[-0xf8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec19c`](#insn-004ec19c)

~~~json
{
  "source": "004ec19c",
  "target": "Stack[-0xe8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec1a0`](#insn-004ec1a0)

~~~json
{
  "source": "004ec1a0",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec1a4`](#insn-004ec1a4)

~~~json
{
  "source": "004ec1a4",
  "target": "Stack[-0x130]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec1a8`](#insn-004ec1a8)

~~~json
{
  "source": "004ec1a8",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec1ac`](#insn-004ec1ac)

~~~json
{
  "source": "004ec1ac",
  "target": "Stack[-0x118]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec1b0`](#insn-004ec1b0)

~~~json
{
  "source": "004ec1b0",
  "target": "Stack[-0x108]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec1b4`](#insn-004ec1b4)

~~~json
{
  "source": "004ec1b4",
  "target": "004ec1fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec1b8`](#insn-004ec1b8)

~~~json
{
  "source": "004ec1b8",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec1c4`](#insn-004ec1c4)

~~~json
{
  "source": "004ec1c4",
  "target": "004ec1f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec1cc`](#insn-004ec1cc)

~~~json
{
  "source": "004ec1cc",
  "target": "004ec1dc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec1d8`](#insn-004ec1d8)

~~~json
{
  "source": "004ec1d8",
  "target": "004ec1f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec1e0`](#insn-004ec1e0)

~~~json
{
  "source": "004ec1e0",
  "target": "004ec1d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec1e8`](#insn-004ec1e8)

~~~json
{
  "source": "004ec1e8",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ec1ec`](#insn-004ec1ec)

~~~json
{
  "source": "004ec1ec",
  "target": "004ec1d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec1f0`](#insn-004ec1f0)

~~~json
{
  "source": "004ec1f0",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec1f4`](#insn-004ec1f4)

~~~json
{
  "source": "004ec1f4",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec1f8`](#insn-004ec1f8)

~~~json
{
  "source": "004ec1f8",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ec1fc`](#insn-004ec1fc)

~~~json
{
  "source": "004ec1fc",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec200`](#insn-004ec200)

~~~json
{
  "source": "004ec200",
  "target": "004ec248",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec204`](#insn-004ec204)

~~~json
{
  "source": "004ec204",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec210`](#insn-004ec210)

~~~json
{
  "source": "004ec210",
  "target": "004ec240",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec218`](#insn-004ec218)

~~~json
{
  "source": "004ec218",
  "target": "004ec228",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec224`](#insn-004ec224)

~~~json
{
  "source": "004ec224",
  "target": "004ec23c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec22c`](#insn-004ec22c)

~~~json
{
  "source": "004ec22c",
  "target": "004ec21c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec234`](#insn-004ec234)

~~~json
{
  "source": "004ec234",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ec238`](#insn-004ec238)

~~~json
{
  "source": "004ec238",
  "target": "004ec21c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec23c`](#insn-004ec23c)

~~~json
{
  "source": "004ec23c",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec240`](#insn-004ec240)

~~~json
{
  "source": "004ec240",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec244`](#insn-004ec244)

~~~json
{
  "source": "004ec244",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ec248`](#insn-004ec248)

~~~json
{
  "source": "004ec248",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec24c`](#insn-004ec24c)

~~~json
{
  "source": "004ec24c",
  "target": "004ec258",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec250`](#insn-004ec250)

~~~json
{
  "source": "004ec250",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec254`](#insn-004ec254)

~~~json
{
  "source": "004ec254",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ec258`](#insn-004ec258)

~~~json
{
  "source": "004ec258",
  "target": "Stack[-0xc8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec25c`](#insn-004ec25c)

~~~json
{
  "source": "004ec25c",
  "target": "004ec2b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec260`](#insn-004ec260)

~~~json
{
  "source": "004ec260",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec264`](#insn-004ec264)

~~~json
{
  "source": "004ec264",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ec268`](#insn-004ec268)

~~~json
{
  "source": "004ec268",
  "target": "004ec2b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec26c`](#insn-004ec26c)

~~~json
{
  "source": "004ec26c",
  "target": "Stack[-0x138]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec284`](#insn-004ec284)

~~~json
{
  "source": "004ec284",
  "target": "Stack[-0x147]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec294`](#insn-004ec294)

~~~json
{
  "source": "004ec294",
  "target": "004ec0b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec2a8`](#insn-004ec2a8)

~~~json
{
  "source": "004ec2a8",
  "target": "002ab43e",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002ab43e",
  "offset": 0,
  "size": 12,
  "datatype": "string",
  "bytes": "4145532d3235362f47434d00",
  "capture_start": "002ab43e",
  "capture_bytes": 12,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`004ec2a8`](#insn-004ec2a8)

~~~json
{
  "source": "004ec2a8",
  "target": "002bb373",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002bb373",
  "offset": 0,
  "size": 8,
  "datatype": "string",
  "bytes": "5348412d35313200",
  "capture_start": "002bb373",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`004ec2a8`](#insn-004ec2a8)

~~~json
{
  "source": "004ec2a8",
  "target": "Stack[-0xc8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec2b4`](#insn-004ec2b4)

~~~json
{
  "source": "004ec2b4",
  "target": "00536c3c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ec2b8`](#insn-004ec2b8)

~~~json
{
  "source": "004ec2b8",
  "target": "Stack[-0x148]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec2bc`](#insn-004ec2bc)

~~~json
{
  "source": "004ec2bc",
  "target": "004ec2c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec2c0`](#insn-004ec2c0)

~~~json
{
  "source": "004ec2c0",
  "target": "Stack[-0x138]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec2c4`](#insn-004ec2c4)

~~~json
{
  "source": "004ec2c4",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ec2d0`](#insn-004ec2d0)

~~~json
{
  "source": "004ec2d0",
  "target": "00c5a680",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ec2d8`](#insn-004ec2d8)

~~~json
{
  "source": "004ec2d8",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec2fc`](#insn-004ec2fc)

~~~json
{
  "source": "004ec2fc",
  "target": "004e27b4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ec300`](#insn-004ec300)

~~~json
{
  "source": "004ec300",
  "target": "Stack[-0x180]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec308`](#insn-004ec308)

~~~json
{
  "source": "004ec308",
  "target": "004ec330",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec30c`](#insn-004ec30c)

~~~json
{
  "source": "004ec30c",
  "target": "Stack[-0x178]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec310`](#insn-004ec310)

~~~json
{
  "source": "004ec310",
  "target": "Stack[-0x170]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec314`](#insn-004ec314)

~~~json
{
  "source": "004ec314",
  "target": "00c687d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c687d8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004ec324`](#insn-004ec324)

~~~json
{
  "source": "004ec324",
  "target": "0112b058",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ec32c`](#insn-004ec32c)

~~~json
{
  "source": "004ec32c",
  "target": "00c59700",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ec334`](#insn-004ec334)

~~~json
{
  "source": "004ec334",
  "target": "Stack[-0x170]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec338`](#insn-004ec338)

~~~json
{
  "source": "004ec338",
  "target": "Stack[-0x180]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec348`](#insn-004ec348)

~~~json
{
  "source": "004ec348",
  "target": "00c59750",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ec34c`](#insn-004ec34c)

~~~json
{
  "source": "004ec34c",
  "target": "Stack[-0xc8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec360`](#insn-004ec360)

~~~json
{
  "source": "004ec360",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec374`](#insn-004ec374)

~~~json
{
  "source": "004ec374",
  "target": "00c598c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ec37c`](#insn-004ec37c)

~~~json
{
  "source": "004ec37c",
  "target": "00c59770",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ec388`](#insn-004ec388)

~~~json
{
  "source": "004ec388",
  "target": "004a7110",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ec38c`](#insn-004ec38c)

~~~json
{
  "source": "004ec38c",
  "target": "Stack[-0x168]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec390`](#insn-004ec390)

~~~json
{
  "source": "004ec390",
  "target": "004ec3cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec394`](#insn-004ec394)

~~~json
{
  "source": "004ec394",
  "target": "Stack[-0x160]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec3a0`](#insn-004ec3a0)

~~~json
{
  "source": "004ec3a0",
  "target": "004ec3c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec3b4`](#insn-004ec3b4)

~~~json
{
  "source": "004ec3b4",
  "target": "00535ee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ec3bc`](#insn-004ec3bc)

~~~json
{
  "source": "004ec3bc",
  "target": "004ec3a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec3c0`](#insn-004ec3c0)

~~~json
{
  "source": "004ec3c0",
  "target": "Stack[-0x168]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec3c4`](#insn-004ec3c4)

~~~json
{
  "source": "004ec3c4",
  "target": "Stack[-0x160]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec3c8`](#insn-004ec3c8)

~~~json
{
  "source": "004ec3c8",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ec3cc`](#insn-004ec3cc)

~~~json
{
  "source": "004ec3cc",
  "target": "Stack[-0x180]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec3d0`](#insn-004ec3d0)

~~~json
{
  "source": "004ec3d0",
  "target": "004ec3f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec3d4`](#insn-004ec3d4)

~~~json
{
  "source": "004ec3d4",
  "target": "Stack[-0x178]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec3d8`](#insn-004ec3d8)

~~~json
{
  "source": "004ec3d8",
  "target": "Stack[-0x170]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec3dc`](#insn-004ec3dc)

~~~json
{
  "source": "004ec3dc",
  "target": "00c687d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c687d8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004ec3ec`](#insn-004ec3ec)

~~~json
{
  "source": "004ec3ec",
  "target": "0112b058",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ec3f4`](#insn-004ec3f4)

~~~json
{
  "source": "004ec3f4",
  "target": "00c59700",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ec3f8`](#insn-004ec3f8)

~~~json
{
  "source": "004ec3f8",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec3fc`](#insn-004ec3fc)

~~~json
{
  "source": "004ec3fc",
  "target": "004ec408",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec400`](#insn-004ec400)

~~~json
{
  "source": "004ec400",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec404`](#insn-004ec404)

~~~json
{
  "source": "004ec404",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ec408`](#insn-004ec408)

~~~json
{
  "source": "004ec408",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec40c`](#insn-004ec40c)

~~~json
{
  "source": "004ec40c",
  "target": "004ec418",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec410`](#insn-004ec410)

~~~json
{
  "source": "004ec410",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec414`](#insn-004ec414)

~~~json
{
  "source": "004ec414",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ec418`](#insn-004ec418)

~~~json
{
  "source": "004ec418",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec41c`](#insn-004ec41c)

~~~json
{
  "source": "004ec41c",
  "target": "004ec428",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec420`](#insn-004ec420)

~~~json
{
  "source": "004ec420",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec424`](#insn-004ec424)

~~~json
{
  "source": "004ec424",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ec428`](#insn-004ec428)

~~~json
{
  "source": "004ec428",
  "target": "Stack[-0x118]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec42c`](#insn-004ec42c)

~~~json
{
  "source": "004ec42c",
  "target": "004ec438",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec430`](#insn-004ec430)

~~~json
{
  "source": "004ec430",
  "target": "Stack[-0x108]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec434`](#insn-004ec434)

~~~json
{
  "source": "004ec434",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ec438`](#insn-004ec438)

~~~json
{
  "source": "004ec438",
  "target": "Stack[-0x130]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec43c`](#insn-004ec43c)

~~~json
{
  "source": "004ec43c",
  "target": "004ec448",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec440`](#insn-004ec440)

~~~json
{
  "source": "004ec440",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec444`](#insn-004ec444)

~~~json
{
  "source": "004ec444",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ec44c`](#insn-004ec44c)

~~~json
{
  "source": "004ec44c",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec454`](#insn-004ec454)

~~~json
{
  "source": "004ec454",
  "target": "004ec5b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec458`](#insn-004ec458)

~~~json
{
  "source": "004ec458",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec45c`](#insn-004ec45c)

~~~json
{
  "source": "004ec45c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec460`](#insn-004ec460)

~~~json
{
  "source": "004ec460",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec464`](#insn-004ec464)

~~~json
{
  "source": "004ec464",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec468`](#insn-004ec468)

~~~json
{
  "source": "004ec468",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec46c`](#insn-004ec46c)

~~~json
{
  "source": "004ec46c",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec47c`](#insn-004ec47c)

~~~json
{
  "source": "004ec47c",
  "target": "00c58f90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ec488`](#insn-004ec488)

~~~json
{
  "source": "004ec488",
  "target": "002bc764",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002bc764",
  "offset": 0,
  "size": 17,
  "datatype": "string",
  "bytes": "556e737570706f72746564205042452000",
  "capture_start": "002bc764",
  "capture_bytes": 17,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`004ec494`](#insn-004ec494)

~~~json
{
  "source": "004ec494",
  "target": "00c59150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ec4a4`](#insn-004ec4a4)

~~~json
{
  "source": "004ec4a4",
  "target": "00c59860",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ec4ac`](#insn-004ec4ac)

~~~json
{
  "source": "004ec4ac",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec4b4`](#insn-004ec4b4)

~~~json
{
  "source": "004ec4b4",
  "target": "004ec5b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec4c0`](#insn-004ec4c0)

~~~json
{
  "source": "004ec4c0",
  "target": "00535bc8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ec4c4`](#insn-004ec4c4)

~~~json
{
  "source": "004ec4c4",
  "target": "00c9be28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9be28",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004ec4c4`](#insn-004ec4c4)

~~~json
{
  "source": "004ec4c4",
  "target": "00c672e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c672e8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004ec4d0`](#insn-004ec4d0)

~~~json
{
  "source": "004ec4d0",
  "target": "00c58fb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ec5b4`](#insn-004ec5b4)

~~~json
{
  "source": "004ec5b4",
  "target": "00c58f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
