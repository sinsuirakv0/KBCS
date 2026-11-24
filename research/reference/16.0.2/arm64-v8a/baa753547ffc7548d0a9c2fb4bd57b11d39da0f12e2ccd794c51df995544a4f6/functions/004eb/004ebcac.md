# 004ebcac

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `004ebc6c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004eb/004ebc6c.md) · 移動量 `+0x40`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0010.md#compare-7aed7cdb06110704d0dce508f1c78e78)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `004ebfcc`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004eb/004ebfcc.md) · 移動量 `+0x320`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0010.md#compare-3f1b4b08dd2d6b7c3ba852ab3d1836fa)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "004ebcac",
  "name": "_ZN5Botan5PKCS810BER_encodeERKNS_11Private_KeyERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS6_11char_traitsIcEENS6_9allocatorIcEEEENS6_6chrono8durationIxNS6_5ratioILl1ELl1000EEEEESE_",
  "size": 1292,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d81e8010e1dc46bc9c213e1a3cabbfe8aa4fa5bf88495ea791d245eaf4bdccdc",
  "source_text_sha256": "d81e8010e1dc46bc9c213e1a3cabbfe8aa4fa5bf88495ea791d245eaf4bdccdc",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "004ebcac",
        "004ec1b3"
      ],
      [
        "004ec294",
        "004ec297"
      ]
    ],
    "bytes_sha256": "98b40bf57a587f695792c7ea59854ba3139407ed046ff823a8403f403f2c4e65",
    "instruction_count": 323,
    "instruction_bytes": 1292,
    "body_bytes": 1292,
    "indirect": 4,
    "unresolved": 2
  }
}
~~~

## 呼び出し元

- [00c596d0](../00c59/00c596d0.md)

## 呼び出し先

- [0043bb60](../0043b/0043bb60.md)
- [004a6df0](../004a6/004a6df0.md)
- [004e2494](../004e2/004e2494.md)
- [00535bc0](../00535/00535bc0.md)
- [0053691c](../00536/0053691c.md)
- [00c57f80](../00c57/00c57f80.md)
- [00c57fb0](../00c57/00c57fb0.md)
- [00c57fc0](../00c57/00c57fc0.md)
- [00c57fe0](../00c57/00c57fe0.md)
- [00c58180](../00c58/00c58180.md)
- [00c58730](../00c58/00c58730.md)
- [00c58780](../00c58/00c58780.md)
- [00c587a0](../00c58/00c587a0.md)
- [00c58890](../00c58/00c58890.md)
- [00c588f0](../00c58/00c588f0.md)
- [00c58c60](../00c58/00c58c60.md)
- [00c58e10](../00c58/00c58e10.md)
- [00c596b0](../00c59/00c596b0.md)
- [0112a058](../0112a/0112a058.md)

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
LAB_004ebf78:
        local_c8 = "AES-256/GCM";
        pcStack_c0 = "SHA-512";
        FUN_0053691c(&local_130,&local_c8);
        goto LAB_004ebf98;
      }
    }
    else if (uVar1 == 10) {
      plVar3 = local_138;
      if ((local_148 & 1) == 0) {
        plVar3 = (long *)auStack_147;
      }
      if (*plVar3 == 0x3535326576727543 && (short)plVar3[1] == 0x3931) goto LAB_004ebf78;
    }
    local_c8 = "AES-256/CBC";
    pcStack_c0 = "SHA-256";
    FUN_0053691c(&local_130,&local_c8);
LAB_004ebf98:
    if ((local_148 & 1) != 0) {
      _ZdlPv(local_138);
    }
    _ZNK5Botan11Private_Key16private_key_infoEv(&local_180,param_2);
    local_e0 = param_5;
    FUN_004e2494(&local_c8,&local_180,param_4,&local_e0,0,&local_130,&local_118,param_3);
    pvVar7 = local_180;
    if (local_180 != (void *)0x0) {
      pvStack_178 = local_180;
      (*(code *)PTR_memset_00c67808)(local_180,0,(long)local_170 - (long)local_180);
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
    FUN_004a6df0(param_1,&local_180);
    pvVar8 = pvStack_168;
    pvVar7 = local_160;
    if (pvStack_168 != (void *)0x0) {
      while (pvVar7 != pvVar8) {
        FUN_00535bc0(auStack_158,(void *)((long)pvVar7 + -0x38));
        pvVar7 = (void *)((long)pvVar7 + -0x38);
      }
      local_160 = pvVar8;
      _ZdlPv(pvStack_168);
    }
    pvVar7 = local_180;
    if (local_180 != (void *)0x0) {
      pvStack_178 = local_180;
      (*(code *)PTR_memset_00c67808)(local_180,0,(long)local_170 - (long)local_180);
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
      FUN_0043bb60(&local_180,param_6[2]);
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
        goto LAB_004ebf98;
      }
    }
    uVar9 = __cxa_allocate_exception(0x20);
    _ZNSt6__ndk1plIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EEPKS6_RKS9_
              (&local_e0,"Unsupported PBE ",param_6);
    _ZN5Botan9ExceptionC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
              (uVar9,&local_e0);
    if (*(long *)(lVar5 + 0x28) == local_68) {
                    /* WARNING: Subroutine does not return */
      __cxa_throw(uVar9,PTR__ZTIN5Botan9ExceptionE_00c9ae58,FUN_005358a8);
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
<a id="insn-004ebcac"></a> `004ebcac` | `ff 03 06 d1` | sub sp,sp,#0x180 | `FALL_THROUGH`
<a id="insn-004ebcb0"></a> `004ebcb0` | `fd 7b 12 a9` | stp x29,x30,[sp, #0x120] | `FALL_THROUGH`
<a id="insn-004ebcb4"></a> `004ebcb4` | `fc 9b 00 f9` | str x28,[sp, #0x130] | `FALL_THROUGH`
<a id="insn-004ebcb8"></a> `004ebcb8` | `fa 67 14 a9` | stp x26,x25,[sp, #0x140] | `FALL_THROUGH`
<a id="insn-004ebcbc"></a> `004ebcbc` | `f8 5f 15 a9` | stp x24,x23,[sp, #0x150] | `FALL_THROUGH`
<a id="insn-004ebcc0"></a> `004ebcc0` | `f6 57 16 a9` | stp x22,x21,[sp, #0x160] | `FALL_THROUGH`
<a id="insn-004ebcc4"></a> `004ebcc4` | `f4 4f 17 a9` | stp x20,x19,[sp, #0x170] | `FALL_THROUGH`
<a id="insn-004ebcc8"></a> `004ebcc8` | `fd 83 04 91` | add x29,sp,#0x120 | `FALL_THROUGH`
<a id="insn-004ebccc"></a> `004ebccc` | `59 d0 3b d5` | mrs x25,tpidr_el0 | `FALL_THROUGH`
<a id="insn-004ebcd0"></a> `004ebcd0` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-004ebcd4"></a> `004ebcd4` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-004ebcd8"></a> `004ebcd8` | `29 17 40 f9` | ldr x9,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-004ebcdc"></a> `004ebcdc` | `e8 e3 00 91` | add x8,sp,#0x38 | `FALL_THROUGH`
<a id="insn-004ebce0"></a> `004ebce0` | `f8 03 04 aa` | mov x24,x4 | `FALL_THROUGH`
<a id="insn-004ebce4"></a> `004ebce4` | `f6 03 03 aa` | mov x22,x3 | `FALL_THROUGH`
<a id="insn-004ebce8"></a> `004ebce8` | `f5 03 02 aa` | mov x21,x2 | `FALL_THROUGH`
<a id="insn-004ebcec"></a> `004ebcec` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-004ebcf0"></a> `004ebcf0` | `a9 83 1f f8` | stur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-004ebcf4"></a> `004ebcf4` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-004ebcf8"></a> `004ebcf8` | `29 01 58 f8` | ldur x9,[x9, #-0x80] | `FALL_THROUGH`
<a id="insn-004ebcfc"></a> `004ebcfc` | `0a 68 69 f8` | ldr x10,[x0, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-004ebd00"></a> `004ebd00` | `00 00 09 8b` | add x0,x0,x9 | `FALL_THROUGH`
<a id="insn-004ebd04"></a> `004ebd04` | `4a 09 40 f9` | ldr x10,[x10, #0x10] | `FALL_THROUGH`
<a id="insn-004ebd08"></a> `004ebd08` | `40 01 3f d6` | blr x10 | `COMPUTED_CALL`
<a id="insn-004ebd0c"></a> `004ebd0c` | `08 03 40 39` | ldrb w8,[x24] | `FALL_THROUGH`
<a id="insn-004ebd10"></a> `004ebd10` | `02 07 40 f9` | ldr x2,[x24, #0x8] | `FALL_THROUGH`
<a id="insn-004ebd14"></a> `004ebd14` | `09 fd 41 d3` | lsr x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-004ebd18"></a> `004ebd18` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-004ebd1c"></a> `004ebd1c` | `29 01 82 9a` | csel x9,x9,x2,eq | `FALL_THROUGH`
<a id="insn-004ebd20"></a> `004ebd20` | `e9 00 00 b4` | cbz x9,0x004ebd3c | `CONDITIONAL_JUMP`
<a id="insn-004ebd24"></a> `004ebd24` | `c8 04 00 37` | tbnz w8,#0x0,0x004ebdbc | `CONDITIONAL_JUMP`
<a id="insn-004ebd28"></a> `004ebd28` | `00 03 c0 3d` | ldr q0,[x24] | `FALL_THROUGH`
<a id="insn-004ebd2c"></a> `004ebd2c` | `08 0b 40 f9` | ldr x8,[x24, #0x10] | `FALL_THROUGH`
<a id="insn-004ebd30"></a> `004ebd30` | `e0 03 80 3d` | str q0,[sp] | `FALL_THROUGH`
<a id="insn-004ebd34"></a> `004ebd34` | `e8 0b 00 f9` | str x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-004ebd38"></a> `004ebd38` | `24 00 00 14` | b 0x004ebdc8 | `UNCONDITIONAL_JUMP`
<a id="insn-004ebd3c"></a> `004ebd3c` | `e8 e3 40 39` | ldrb w8,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-004ebd40"></a> `004ebd40` | `e9 23 40 f9` | ldr x9,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-004ebd44"></a> `004ebd44` | `0a fd 41 d3` | lsr x10,x8,#0x1 | `FALL_THROUGH`
<a id="insn-004ebd48"></a> `004ebd48` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-004ebd4c"></a> `004ebd4c` | `49 01 89 9a` | csel x9,x10,x9,eq | `FALL_THROUGH`
<a id="insn-004ebd50"></a> `004ebd50` | `3f 21 00 f1` | cmp x9,#0x8 | `FALL_THROUGH`
<a id="insn-004ebd54"></a> `004ebd54` | `c0 0f 00 54` | b.eq 0x004ebf4c | `CONDITIONAL_JUMP`
<a id="insn-004ebd58"></a> `004ebd58` | `3f 29 00 f1` | cmp x9,#0xa | `FALL_THROUGH`
<a id="insn-004ebd5c"></a> `004ebd5c` | `e1 01 00 54` | b.ne 0x004ebd98 | `CONDITIONAL_JUMP`
<a id="insn-004ebd60"></a> `004ebd60` | `e9 27 40 f9` | ldr x9,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-004ebd64"></a> `004ebd64` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-004ebd68"></a> `004ebd68` | `e8 e3 00 91` | add x8,sp,#0x38 | `FALL_THROUGH`
<a id="insn-004ebd6c"></a> `004ebd6c` | `6a a8 8e d2` | mov x10,#0x7543 | `FALL_THROUGH`
<a id="insn-004ebd70"></a> `004ebd70` | `28 15 88 9a` | csinc x8,x9,x8,ne | `FALL_THROUGH`
<a id="insn-004ebd74"></a> `004ebd74` | `4a ce ae f2` | movk x10,#0x7672, LSL #16 | `FALL_THROUGH`
<a id="insn-004ebd78"></a> `004ebd78` | `09 01 40 f9` | ldr x9,[x8] | `FALL_THROUGH`
<a id="insn-004ebd7c"></a> `004ebd7c` | `aa 4c c6 f2` | movk x10,#0x3265, LSL #32 | `FALL_THROUGH`
<a id="insn-004ebd80"></a> `004ebd80` | `08 11 40 79` | ldrh w8,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-004ebd84"></a> `004ebd84` | `aa a6 e6 f2` | movk x10,#0x3535, LSL #48 | `FALL_THROUGH`
<a id="insn-004ebd88"></a> `004ebd88` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-004ebd8c"></a> `004ebd8c` | `29 26 87 52` | mov w9,#0x3931 | `FALL_THROUGH`
<a id="insn-004ebd90"></a> `004ebd90` | `00 01 49 7a` | ccmp w8,w9,#0x0,eq | `FALL_THROUGH`
<a id="insn-004ebd94"></a> `004ebd94` | `20 0f 00 54` | b.eq 0x004ebf78 | `CONDITIONAL_JUMP`
<a id="insn-004ebd98"></a> `004ebd98` | `88 ee ff f0` | adrp x8,0x2be000 | `FALL_THROUGH`
<a id="insn-004ebd9c"></a> `004ebd9c` | `08 99 30 91` | add x8,x8,#0xc26 | `FALL_THROUGH`
<a id="insn-004ebda0"></a> `004ebda0` | `e9 ed ff d0` | adrp x9,0x2a9000 | `FALL_THROUGH`
<a id="insn-004ebda4"></a> `004ebda4` | `29 49 2d 91` | add x9,x9,#0xb52 | `FALL_THROUGH`
<a id="insn-004ebda8"></a> `004ebda8` | `a8 a7 39 a9` | stp x8,x9,[x29, #-0x68] | `FALL_THROUGH`
<a id="insn-004ebdac"></a> `004ebdac` | `e0 43 01 91` | add x0,sp,#0x50 | `FALL_THROUGH`
<a id="insn-004ebdb0"></a> `004ebdb0` | `a1 a3 01 d1` | sub x1,x29,#0x68 | `FALL_THROUGH`
<a id="insn-004ebdb4"></a> `004ebdb4` | `da 2a 01 94` | bl 0x0053691c | `UNCONDITIONAL_CALL`
<a id="insn-004ebdb8"></a> `004ebdb8` | `78 00 00 14` | b 0x004ebf98 | `UNCONDITIONAL_JUMP`
<a id="insn-004ebdbc"></a> `004ebdbc` | `01 0b 40 f9` | ldr x1,[x24, #0x10] | `FALL_THROUGH`
<a id="insn-004ebdc0"></a> `004ebdc0` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-004ebdc4"></a> `004ebdc4` | `67 3f fd 97` | bl 0x0043bb60 | `UNCONDITIONAL_CALL`
<a id="insn-004ebdc8"></a> `004ebdc8` | `a0 a3 01 d1` | sub x0,x29,#0x68 | `FALL_THROUGH`
<a id="insn-004ebdcc"></a> `004ebdcc` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-004ebdd0"></a> `004ebdd0` | `10 b4 1d 94` | bl 0x00c58e10 | `UNCONDITIONAL_CALL`
<a id="insn-004ebdd4"></a> `004ebdd4` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-004ebdd8"></a> `004ebdd8` | `68 00 00 36` | tbz w8,#0x0,0x004ebde4 | `CONDITIONAL_JUMP`
<a id="insn-004ebddc"></a> `004ebddc` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-004ebde0"></a> `004ebde0` | `68 b0 1d 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-004ebde4"></a> `004ebde4` | `a8 03 5b 38` | ldurb w8,[x29, #-0x50] | `FALL_THROUGH`
<a id="insn-004ebde8"></a> `004ebde8` | `a9 83 5b f8` | ldur x9,[x29, #-0x48] | `FALL_THROUGH`
<a id="insn-004ebdec"></a> `004ebdec` | `0a fd 41 d3` | lsr x10,x8,#0x1 | `FALL_THROUGH`
<a id="insn-004ebdf0"></a> `004ebdf0` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-004ebdf4"></a> `004ebdf4` | `49 01 89 9a` | csel x9,x10,x9,eq | `FALL_THROUGH`
<a id="insn-004ebdf8"></a> `004ebdf8` | `3f 31 00 f1` | cmp x9,#0xc | `FALL_THROUGH`
<a id="insn-004ebdfc"></a> `004ebdfc` | `e1 1a 00 54` | b.ne 0x004ec158 | `CONDITIONAL_JUMP`
<a id="insn-004ebe00"></a> `004ebe00` | `a9 03 5c f8` | ldur x9,[x29, #-0x40] | `FALL_THROUGH`
<a id="insn-004ebe04"></a> `004ebe04` | `aa a3 01 d1` | sub x10,x29,#0x68 | `FALL_THROUGH`
<a id="insn-004ebe08"></a> `004ebe08` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-004ebe0c"></a> `004ebe0c` | `4a 65 00 91` | add x10,x10,#0x19 | `FALL_THROUGH`
<a id="insn-004ebe10"></a> `004ebe10` | `48 01 89 9a` | csel x8,x10,x9,eq | `FALL_THROUGH`
<a id="insn-004ebe14"></a> `004ebe14` | `0a 4a 88 d2` | mov x10,#0x4250 | `FALL_THROUGH`
<a id="insn-004ebe18"></a> `004ebe18` | `aa a8 a5 f2` | movk x10,#0x2d45, LSL #16 | `FALL_THROUGH`
<a id="insn-004ebe1c"></a> `004ebe1c` | `09 01 40 f9` | ldr x9,[x8] | `FALL_THROUGH`
<a id="insn-004ebe20"></a> `004ebe20` | `08 09 40 b9` | ldr w8,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-004ebe24"></a> `004ebe24` | `0a 6a c9 f2` | movk x10,#0x4b50, LSL #32 | `FALL_THROUGH`
<a id="insn-004ebe28"></a> `004ebe28` | `6a 68 ea f2` | movk x10,#0x5343, LSL #48 | `FALL_THROUGH`
<a id="insn-004ebe2c"></a> `004ebe2c` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-004ebe30"></a> `004ebe30` | `a9 c6 8e 52` | mov w9,#0x7635 | `FALL_THROUGH`
<a id="insn-004ebe34"></a> `004ebe34` | `49 06 a6 72` | movk w9,#0x3032, LSL #16 | `FALL_THROUGH`
<a id="insn-004ebe38"></a> `004ebe38` | `00 01 49 7a` | ccmp w8,w9,#0x0,eq | `FALL_THROUGH`
<a id="insn-004ebe3c"></a> `004ebe3c` | `e1 18 00 54` | b.ne 0x004ec158 | `CONDITIONAL_JUMP`
<a id="insn-004ebe40"></a> `004ebe40` | `a9 a3 7c a9` | ldp x9,x8,[x29, #-0x38] | `FALL_THROUGH`
<a id="insn-004ebe44"></a> `004ebe44` | `08 01 09 cb` | sub x8,x8,x9 | `FALL_THROUGH`
<a id="insn-004ebe48"></a> `004ebe48` | `1f c1 00 f1` | cmp x8,#0x30 | `FALL_THROUGH`
<a id="insn-004ebe4c"></a> `004ebe4c` | `61 18 00 54` | b.ne 0x004ec158 | `CONDITIONAL_JUMP`
<a id="insn-004ebe50"></a> `004ebe50` | `a8 03 02 d1` | sub x8,x29,#0x80 | `FALL_THROUGH`
<a id="insn-004ebe54"></a> `004ebe54` | `a0 a3 01 d1` | sub x0,x29,#0x68 | `FALL_THROUGH`
<a id="insn-004ebe58"></a> `004ebe58` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-004ebe5c"></a> `004ebe5c` | `81 b3 1d 94` | bl 0x00c58c60 | `UNCONDITIONAL_CALL`
<a id="insn-004ebe60"></a> `004ebe60` | `e8 23 02 91` | add x8,sp,#0x88 | `FALL_THROUGH`
<a id="insn-004ebe64"></a> `004ebe64` | `a0 a3 01 d1` | sub x0,x29,#0x68 | `FALL_THROUGH`
<a id="insn-004ebe68"></a> `004ebe68` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-004ebe6c"></a> `004ebe6c` | `7d b3 1d 94` | bl 0x00c58c60 | `UNCONDITIONAL_CALL`
<a id="insn-004ebe70"></a> `004ebe70` | `a0 03 d8 3c` | ldur q0,[x29, #-0x80] | `FALL_THROUGH`
<a id="insn-004ebe74"></a> `004ebe74` | `a8 03 59 f8` | ldur x8,[x29, #-0x70] | `FALL_THROUGH`
<a id="insn-004ebe78"></a> `004ebe78` | `e1 83 c8 3c` | ldur q1,[sp, #0x88] | `FALL_THROUGH`
<a id="insn-004ebe7c"></a> `004ebe7c` | `e9 4f 40 f9` | ldr x9,[sp, #0x98] | `FALL_THROUGH`
<a id="insn-004ebe80"></a> `004ebe80` | `b8 03 5e f8` | ldur x24,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-004ebe84"></a> `004ebe84` | `e0 17 80 3d` | str q0,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-004ebe88"></a> `004ebe88` | `e8 33 00 f9` | str x8,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-004ebe8c"></a> `004ebe8c` | `e1 83 86 3c` | stur q1,[sp, #0x68] | `FALL_THROUGH`
<a id="insn-004ebe90"></a> `004ebe90` | `e9 3f 00 f9` | str x9,[sp, #0x78] | `FALL_THROUGH`
<a id="insn-004ebe94"></a> `004ebe94` | `58 02 00 b4` | cbz x24,0x004ebedc | `CONDITIONAL_JUMP`
<a id="insn-004ebe98"></a> `004ebe98` | `a8 83 5e f8` | ldur x8,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-004ebe9c"></a> `004ebe9c` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-004ebea0"></a> `004ebea0` | `1f 01 18 eb` | cmp x8,x24 | `FALL_THROUGH`
<a id="insn-004ebea4"></a> `004ebea4` | `80 01 00 54` | b.eq 0x004ebed4 | `CONDITIONAL_JUMP`
<a id="insn-004ebea8"></a> `004ebea8` | `fa 03 08 aa` | mov x26,x8 | `FALL_THROUGH`
<a id="insn-004ebeac"></a> `004ebeac` | `04 00 00 14` | b 0x004ebebc | `UNCONDITIONAL_JUMP`
<a id="insn-004ebeb0"></a> `004ebeb0` | `5f 03 18 eb` | cmp x26,x24 | `FALL_THROUGH`
<a id="insn-004ebeb4"></a> `004ebeb4` | `e8 03 1a aa` | mov x8,x26 | `FALL_THROUGH`
<a id="insn-004ebeb8"></a> `004ebeb8` | `c0 00 00 54` | b.eq 0x004ebed0 | `CONDITIONAL_JUMP`
<a id="insn-004ebebc"></a> `004ebebc` | `49 8f 5e 38` | ldrb w9,[x26, #-0x18]! | `FALL_THROUGH`
<a id="insn-004ebec0"></a> `004ebec0` | `89 ff 07 36` | tbz w9,#0x0,0x004ebeb0 | `CONDITIONAL_JUMP`
<a id="insn-004ebec4"></a> `004ebec4` | `00 81 5f f8` | ldur x0,[x8, #-0x8] | `FALL_THROUGH`
<a id="insn-004ebec8"></a> `004ebec8` | `2e b0 1d 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-004ebecc"></a> `004ebecc` | `f9 ff ff 17` | b 0x004ebeb0 | `UNCONDITIONAL_JUMP`
<a id="insn-004ebed0"></a> `004ebed0` | `a0 03 5e f8` | ldur x0,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-004ebed4"></a> `004ebed4` | `b8 83 1e f8` | stur x24,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-004ebed8"></a> `004ebed8` | `2a b0 1d 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-004ebedc"></a> `004ebedc` | `b8 83 5c f8` | ldur x24,[x29, #-0x38] | `FALL_THROUGH`
<a id="insn-004ebee0"></a> `004ebee0` | `58 02 00 b4` | cbz x24,0x004ebf28 | `CONDITIONAL_JUMP`
<a id="insn-004ebee4"></a> `004ebee4` | `a8 03 5d f8` | ldur x8,[x29, #-0x30] | `FALL_THROUGH`
<a id="insn-004ebee8"></a> `004ebee8` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-004ebeec"></a> `004ebeec` | `1f 01 18 eb` | cmp x8,x24 | `FALL_THROUGH`
<a id="insn-004ebef0"></a> `004ebef0` | `80 01 00 54` | b.eq 0x004ebf20 | `CONDITIONAL_JUMP`
<a id="insn-004ebef4"></a> `004ebef4` | `fa 03 08 aa` | mov x26,x8 | `FALL_THROUGH`
<a id="insn-004ebef8"></a> `004ebef8` | `04 00 00 14` | b 0x004ebf08 | `UNCONDITIONAL_JUMP`
<a id="insn-004ebefc"></a> `004ebefc` | `5f 03 18 eb` | cmp x26,x24 | `FALL_THROUGH`
<a id="insn-004ebf00"></a> `004ebf00` | `e8 03 1a aa` | mov x8,x26 | `FALL_THROUGH`
<a id="insn-004ebf04"></a> `004ebf04` | `c0 00 00 54` | b.eq 0x004ebf1c | `CONDITIONAL_JUMP`
<a id="insn-004ebf08"></a> `004ebf08` | `49 8f 5e 38` | ldrb w9,[x26, #-0x18]! | `FALL_THROUGH`
<a id="insn-004ebf0c"></a> `004ebf0c` | `89 ff 07 36` | tbz w9,#0x0,0x004ebefc | `CONDITIONAL_JUMP`
<a id="insn-004ebf10"></a> `004ebf10` | `00 81 5f f8` | ldur x0,[x8, #-0x8] | `FALL_THROUGH`
<a id="insn-004ebf14"></a> `004ebf14` | `1b b0 1d 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-004ebf18"></a> `004ebf18` | `f9 ff ff 17` | b 0x004ebefc | `UNCONDITIONAL_JUMP`
<a id="insn-004ebf1c"></a> `004ebf1c` | `a0 83 5c f8` | ldur x0,[x29, #-0x38] | `FALL_THROUGH`
<a id="insn-004ebf20"></a> `004ebf20` | `b8 03 1d f8` | stur x24,[x29, #-0x30] | `FALL_THROUGH`
<a id="insn-004ebf24"></a> `004ebf24` | `17 b0 1d 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-004ebf28"></a> `004ebf28` | `a8 03 5b 38` | ldurb w8,[x29, #-0x50] | `FALL_THROUGH`
<a id="insn-004ebf2c"></a> `004ebf2c` | `68 00 00 36` | tbz w8,#0x0,0x004ebf38 | `CONDITIONAL_JUMP`
<a id="insn-004ebf30"></a> `004ebf30` | `a0 03 5c f8` | ldur x0,[x29, #-0x40] | `FALL_THROUGH`
<a id="insn-004ebf34"></a> `004ebf34` | `13 b0 1d 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-004ebf38"></a> `004ebf38` | `a8 83 59 38` | ldurb w8,[x29, #-0x68] | `FALL_THROUGH`
<a id="insn-004ebf3c"></a> `004ebf3c` | `e8 02 00 36` | tbz w8,#0x0,0x004ebf98 | `CONDITIONAL_JUMP`
<a id="insn-004ebf40"></a> `004ebf40` | `a0 83 5a f8` | ldur x0,[x29, #-0x58] | `FALL_THROUGH`
<a id="insn-004ebf44"></a> `004ebf44` | `0f b0 1d 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-004ebf48"></a> `004ebf48` | `14 00 00 14` | b 0x004ebf98 | `UNCONDITIONAL_JUMP`
<a id="insn-004ebf4c"></a> `004ebf4c` | `e9 27 40 f9` | ldr x9,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-004ebf50"></a> `004ebf50` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-004ebf54"></a> `004ebf54` | `e8 e3 00 91` | add x8,sp,#0x38 | `FALL_THROUGH`
<a id="insn-004ebf58"></a> `004ebf58` | `28 15 88 9a` | csinc x8,x9,x8,ne | `FALL_THROUGH`
<a id="insn-004ebf5c"></a> `004ebf5c` | `a9 69 8c d2` | mov x9,#0x634d | `FALL_THROUGH`
<a id="insn-004ebf60"></a> `004ebf60` | `a9 88 ad f2` | movk x9,#0x6c45, LSL #16 | `FALL_THROUGH`
<a id="insn-004ebf64"></a> `004ebf64` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-004ebf68"></a> `004ebf68` | `29 ad cc f2` | movk x9,#0x6569, LSL #32 | `FALL_THROUGH`
<a id="insn-004ebf6c"></a> `004ebf6c` | `69 ac ec f2` | movk x9,#0x6563, LSL #48 | `FALL_THROUGH`
<a id="insn-004ebf70"></a> `004ebf70` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-004ebf74"></a> `004ebf74` | `21 f1 ff 54` | b.ne 0x004ebd98 | `CONDITIONAL_JUMP`
<a id="insn-004ebf78"></a> `004ebf78` | `08 ee ff 90` | adrp x8,0x2ab000 | `FALL_THROUGH`
<a id="insn-004ebf7c"></a> `004ebf7c` | `08 c5 0d 91` | add x8,x8,#0x371 | `FALL_THROUGH`
<a id="insn-004ebf80"></a> `004ebf80` | `89 ee ff 90` | adrp x9,0x2bb000 | `FALL_THROUGH`
<a id="insn-004ebf84"></a> `004ebf84` | `29 55 0a 91` | add x9,x9,#0x295 | `FALL_THROUGH`
<a id="insn-004ebf88"></a> `004ebf88` | `a8 a7 39 a9` | stp x8,x9,[x29, #-0x68] | `FALL_THROUGH`
<a id="insn-004ebf8c"></a> `004ebf8c` | `e0 43 01 91` | add x0,sp,#0x50 | `FALL_THROUGH`
<a id="insn-004ebf90"></a> `004ebf90` | `a1 a3 01 d1` | sub x1,x29,#0x68 | `FALL_THROUGH`
<a id="insn-004ebf94"></a> `004ebf94` | `62 2a 01 94` | bl 0x0053691c | `UNCONDITIONAL_CALL`
<a id="insn-004ebf98"></a> `004ebf98` | `e8 e3 40 39` | ldrb w8,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-004ebf9c"></a> `004ebf9c` | `68 00 00 36` | tbz w8,#0x0,0x004ebfa8 | `CONDITIONAL_JUMP`
<a id="insn-004ebfa0"></a> `004ebfa0` | `e0 27 40 f9` | ldr x0,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-004ebfa4"></a> `004ebfa4` | `f7 af 1d 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-004ebfa8"></a> `004ebfa8` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-004ebfac"></a> `004ebfac` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-004ebfb0"></a> `004ebfb0` | `c0 b5 1d 94` | bl 0x00c596b0 | `UNCONDITIONAL_CALL`
<a id="insn-004ebfb4"></a> `004ebfb4` | `e9 43 01 91` | add x9,sp,#0x50 | `FALL_THROUGH`
<a id="insn-004ebfb8"></a> `004ebfb8` | `b6 03 18 f8` | stur x22,[x29, #-0x80] | `FALL_THROUGH`
<a id="insn-004ebfbc"></a> `004ebfbc` | `a8 a3 01 d1` | sub x8,x29,#0x68 | `FALL_THROUGH`
<a id="insn-004ebfc0"></a> `004ebfc0` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-004ebfc4"></a> `004ebfc4` | `a2 03 02 d1` | sub x2,x29,#0x80 | `FALL_THROUGH`
<a id="insn-004ebfc8"></a> `004ebfc8` | `e4 43 01 91` | add x4,sp,#0x50 | `FALL_THROUGH`
<a id="insn-004ebfcc"></a> `004ebfcc` | `25 61 00 91` | add x5,x9,#0x18 | `FALL_THROUGH`
<a id="insn-004ebfd0"></a> `004ebfd0` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-004ebfd4"></a> `004ebfd4` | `e3 03 1f aa` | mov x3,xzr | `FALL_THROUGH`
<a id="insn-004ebfd8"></a> `004ebfd8` | `e6 03 14 aa` | mov x6,x20 | `FALL_THROUGH`
<a id="insn-004ebfdc"></a> `004ebfdc` | `2e d9 ff 97` | bl 0x004e2494 | `UNCONDITIONAL_CALL`
<a id="insn-004ebfe0"></a> `004ebfe0` | `f4 03 40 f9` | ldr x20,[sp] | `FALL_THROUGH`
<a id="insn-004ebfe4"></a> `004ebfe4` | `f5 3b 00 90` | adrp x21,0xc67000 | `FALL_THROUGH`
<a id="insn-004ebfe8"></a> `004ebfe8` | `54 01 00 b4` | cbz x20,0x004ec010 | `CONDITIONAL_JUMP`
<a id="insn-004ebfec"></a> `004ebfec` | `f4 07 00 f9` | str x20,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-004ebff0"></a> `004ebff0` | `e8 0b 40 f9` | ldr x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-004ebff4"></a> `004ebff4` | `a9 06 44 f9` | ldr x9,[x21, #0x808] | `FALL_THROUGH`
<a id="insn-004ebff8"></a> `004ebff8` | `02 01 14 cb` | sub x2,x8,x20 | `FALL_THROUGH`
<a id="insn-004ebffc"></a> `004ebffc` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-004ec000"></a> `004ec000` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-004ec004"></a> `004ec004` | `20 01 3f d6` | blr x9 | `COMPUTED_CALL`
<a id="insn-004ec008"></a> `004ec008` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-004ec00c"></a> `004ec00c` | `c9 b1 1d 94` | bl 0x00c58730 | `UNCONDITIONAL_CALL`
<a id="insn-004ec010"></a> `004ec010` | `00 e4 00 6f` | movi v0.2D,#0x0 | `FALL_THROUGH`
<a id="insn-004ec014"></a> `004ec014` | `e0 83 00 ad` | stp q0,q0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-004ec018"></a> `004ec018` | `e0 03 80 3d` | str q0,[sp] | `FALL_THROUGH`
<a id="insn-004ec01c"></a> `004ec01c` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-004ec020"></a> `004ec020` | `01 02 80 52` | mov w1,#0x10 | `FALL_THROUGH`
<a id="insn-004ec024"></a> `004ec024` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-004ec028"></a> `004ec028` | `d6 b1 1d 94` | bl 0x00c58780 | `UNCONDITIONAL_CALL`
<a id="insn-004ec02c"></a> `004ec02c` | `a8 83 59 f8` | ldur x8,[x29, #-0x68] | `FALL_THROUGH`
<a id="insn-004ec030"></a> `004ec030` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-004ec034"></a> `004ec034` | `a0 a3 01 d1` | sub x0,x29,#0x68 | `FALL_THROUGH`
<a id="insn-004ec038"></a> `004ec038` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-004ec03c"></a> `004ec03c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-004ec040"></a> `004ec040` | `a3 a3 7d a9` | ldp x3,x8,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-004ec044"></a> `004ec044` | `04 01 03 cb` | sub x4,x8,x3 | `FALL_THROUGH`
<a id="insn-004ec048"></a> `004ec048` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-004ec04c"></a> `004ec04c` | `81 00 80 52` | mov w1,#0x4 | `FALL_THROUGH`
<a id="insn-004ec050"></a> `004ec050` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-004ec054"></a> `004ec054` | `27 b2 1d 94` | bl 0x00c588f0 | `UNCONDITIONAL_CALL`
<a id="insn-004ec058"></a> `004ec058` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-004ec05c"></a> `004ec05c` | `d1 b1 1d 94` | bl 0x00c587a0 | `UNCONDITIONAL_CALL`
<a id="insn-004ec060"></a> `004ec060` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-004ec064"></a> `004ec064` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-004ec068"></a> `004ec068` | `62 eb fe 97` | bl 0x004a6df0 | `UNCONDITIONAL_CALL`
<a id="insn-004ec06c"></a> `004ec06c` | `f4 0f 40 f9` | ldr x20,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-004ec070"></a> `004ec070` | `f4 01 00 b4` | cbz x20,0x004ec0ac | `CONDITIONAL_JUMP`
<a id="insn-004ec074"></a> `004ec074` | `f3 13 40 f9` | ldr x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-004ec078"></a> `004ec078` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-004ec07c"></a> `004ec07c` | `7f 02 14 eb` | cmp x19,x20 | `FALL_THROUGH`
<a id="insn-004ec080"></a> `004ec080` | `20 01 00 54` | b.eq 0x004ec0a4 | `CONDITIONAL_JUMP`
<a id="insn-004ec084"></a> `004ec084` | `f6 03 00 91` | mov x22,sp | `FALL_THROUGH`
<a id="insn-004ec088"></a> `004ec088` | `73 e2 00 d1` | sub x19,x19,#0x38 | `FALL_THROUGH`
<a id="insn-004ec08c"></a> `004ec08c` | `c0 a2 00 91` | add x0,x22,#0x28 | `FALL_THROUGH`
<a id="insn-004ec090"></a> `004ec090` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-004ec094"></a> `004ec094` | `cb 26 01 94` | bl 0x00535bc0 | `UNCONDITIONAL_CALL`
<a id="insn-004ec098"></a> `004ec098` | `7f 02 14 eb` | cmp x19,x20 | `FALL_THROUGH`
<a id="insn-004ec09c"></a> `004ec09c` | `61 ff ff 54` | b.ne 0x004ec088 | `CONDITIONAL_JUMP`
<a id="insn-004ec0a0"></a> `004ec0a0` | `e0 0f 40 f9` | ldr x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-004ec0a4"></a> `004ec0a4` | `f4 13 00 f9` | str x20,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-004ec0a8"></a> `004ec0a8` | `b6 af 1d 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-004ec0ac"></a> `004ec0ac` | `f3 03 40 f9` | ldr x19,[sp] | `FALL_THROUGH`
<a id="insn-004ec0b0"></a> `004ec0b0` | `53 01 00 b4` | cbz x19,0x004ec0d8 | `CONDITIONAL_JUMP`
<a id="insn-004ec0b4"></a> `004ec0b4` | `f3 07 00 f9` | str x19,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-004ec0b8"></a> `004ec0b8` | `e8 0b 40 f9` | ldr x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-004ec0bc"></a> `004ec0bc` | `a9 06 44 f9` | ldr x9,[x21, #0x808] | `FALL_THROUGH`
<a id="insn-004ec0c0"></a> `004ec0c0` | `02 01 13 cb` | sub x2,x8,x19 | `FALL_THROUGH`
<a id="insn-004ec0c4"></a> `004ec0c4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-004ec0c8"></a> `004ec0c8` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-004ec0cc"></a> `004ec0cc` | `20 01 3f d6` | blr x9 | `COMPUTED_CALL`
<a id="insn-004ec0d0"></a> `004ec0d0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-004ec0d4"></a> `004ec0d4` | `97 b1 1d 94` | bl 0x00c58730 | `UNCONDITIONAL_CALL`
<a id="insn-004ec0d8"></a> `004ec0d8` | `a0 83 5d f8` | ldur x0,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-004ec0dc"></a> `004ec0dc` | `60 00 00 b4` | cbz x0,0x004ec0e8 | `CONDITIONAL_JUMP`
<a id="insn-004ec0e0"></a> `004ec0e0` | `a0 03 1e f8` | stur x0,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-004ec0e4"></a> `004ec0e4` | `a7 af 1d 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-004ec0e8"></a> `004ec0e8` | `a0 03 5c f8` | ldur x0,[x29, #-0x40] | `FALL_THROUGH`
<a id="insn-004ec0ec"></a> `004ec0ec` | `60 00 00 b4` | cbz x0,0x004ec0f8 | `CONDITIONAL_JUMP`
<a id="insn-004ec0f0"></a> `004ec0f0` | `a0 83 1c f8` | stur x0,[x29, #-0x38] | `FALL_THROUGH`
<a id="insn-004ec0f4"></a> `004ec0f4` | `a3 af 1d 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-004ec0f8"></a> `004ec0f8` | `a0 83 5a f8` | ldur x0,[x29, #-0x58] | `FALL_THROUGH`
<a id="insn-004ec0fc"></a> `004ec0fc` | `60 00 00 b4` | cbz x0,0x004ec108 | `CONDITIONAL_JUMP`
<a id="insn-004ec100"></a> `004ec100` | `a0 03 1b f8` | stur x0,[x29, #-0x50] | `FALL_THROUGH`
<a id="insn-004ec104"></a> `004ec104` | `9f af 1d 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-004ec108"></a> `004ec108` | `e8 a3 41 39` | ldrb w8,[sp, #0x68] | `FALL_THROUGH`
<a id="insn-004ec10c"></a> `004ec10c` | `68 00 00 36` | tbz w8,#0x0,0x004ec118 | `CONDITIONAL_JUMP`
<a id="insn-004ec110"></a> `004ec110` | `e0 3f 40 f9` | ldr x0,[sp, #0x78] | `FALL_THROUGH`
<a id="insn-004ec114"></a> `004ec114` | `9b af 1d 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-004ec118"></a> `004ec118` | `e8 43 41 39` | ldrb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-004ec11c"></a> `004ec11c` | `68 00 00 36` | tbz w8,#0x0,0x004ec128 | `CONDITIONAL_JUMP`
<a id="insn-004ec120"></a> `004ec120` | `e0 33 40 f9` | ldr x0,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-004ec124"></a> `004ec124` | `97 af 1d 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-004ec128"></a> `004ec128` | `28 17 40 f9` | ldr x8,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-004ec12c"></a> `004ec12c` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-004ec130"></a> `004ec130` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-004ec134"></a> `004ec134` | `01 0b 00 54` | b.ne 0x004ec294 | `CONDITIONAL_JUMP`
<a id="insn-004ec138"></a> `004ec138` | `f4 4f 57 a9` | ldp x20,x19,[sp, #0x170] | `FALL_THROUGH`
<a id="insn-004ec13c"></a> `004ec13c` | `fc 9b 40 f9` | ldr x28,[sp, #0x130] | `FALL_THROUGH`
<a id="insn-004ec140"></a> `004ec140` | `f6 57 56 a9` | ldp x22,x21,[sp, #0x160] | `FALL_THROUGH`
<a id="insn-004ec144"></a> `004ec144` | `f8 5f 55 a9` | ldp x24,x23,[sp, #0x150] | `FALL_THROUGH`
<a id="insn-004ec148"></a> `004ec148` | `fa 67 54 a9` | ldp x26,x25,[sp, #0x140] | `FALL_THROUGH`
<a id="insn-004ec14c"></a> `004ec14c` | `fd 7b 52 a9` | ldp x29,x30,[sp, #0x120] | `FALL_THROUGH`
<a id="insn-004ec150"></a> `004ec150` | `ff 03 06 91` | add sp,sp,#0x180 | `FALL_THROUGH`
<a id="insn-004ec154"></a> `004ec154` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-004ec158"></a> `004ec158` | `00 04 80 52` | mov w0,#0x20 | `FALL_THROUGH`
<a id="insn-004ec15c"></a> `004ec15c` | `99 af 1d 94` | bl 0x00c57fc0 | `UNCONDITIONAL_CALL`
<a id="insn-004ec160"></a> `004ec160` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-004ec164"></a> `004ec164` | `80 ee ff 90` | adrp x0,0x2bc000 | `FALL_THROUGH`
<a id="insn-004ec168"></a> `004ec168` | `00 18 1a 91` | add x0,x0,#0x686 | `FALL_THROUGH`
<a id="insn-004ec16c"></a> `004ec16c` | `a8 03 02 d1` | sub x8,x29,#0x80 | `FALL_THROUGH`
<a id="insn-004ec170"></a> `004ec170` | `e1 03 18 aa` | mov x1,x24 | `FALL_THROUGH`
<a id="insn-004ec174"></a> `004ec174` | `03 b0 1d 94` | bl 0x00c58180 | `UNCONDITIONAL_CALL`
<a id="insn-004ec178"></a> `004ec178` | `35 00 80 52` | mov w21,#0x1 | `FALL_THROUGH`
<a id="insn-004ec17c"></a> `004ec17c` | `a1 03 02 d1` | sub x1,x29,#0x80 | `FALL_THROUGH`
<a id="insn-004ec180"></a> `004ec180` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-004ec184"></a> `004ec184` | `c3 b1 1d 94` | bl 0x00c58890 | `UNCONDITIONAL_CALL`
<a id="insn-004ec188"></a> `004ec188` | `28 17 40 f9` | ldr x8,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-004ec18c"></a> `004ec18c` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-004ec190"></a> `004ec190` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-004ec194"></a> `004ec194` | `01 08 00 54` | b.ne 0x004ec294 | `CONDITIONAL_JUMP`
<a id="insn-004ec198"></a> `004ec198` | `61 3d 00 d0` | adrp x1,0xc9a000 | `FALL_THROUGH`
<a id="insn-004ec19c"></a> `004ec19c` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-004ec1a0"></a> `004ec1a0` | `42 b8 24 10` | adr x2,0x5358a8 | `FALL_THROUGH`
<a id="insn-004ec1a4"></a> `004ec1a4` | `21 2c 47 f9` | ldr x1,[x1, #0xe58] | `FALL_THROUGH`
<a id="insn-004ec1a8"></a> `004ec1a8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-004ec1ac"></a> `004ec1ac` | `f5 03 1f 2a` | mov w21,wzr | `FALL_THROUGH`
<a id="insn-004ec1b0"></a> `004ec1b0` | `8c af 1d 94` | bl 0x00c57fe0 | `CALL_TERMINATOR`
<a id="insn-004ec294"></a> `004ec294` | `47 af 1d 94` | bl 0x00c57fb0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`004ebcac`](#insn-004ebcac) 範囲 `[['004ebcac', '004ebd23']]`
  - `CONDITIONAL_JUMP` [`004ebd20`](#insn-004ebd20) → [`004ebd3c`](#insn-004ebd3c)
  - `FALL_THROUGH` [`004ebd20`](#insn-004ebd20) → [`004ebd24`](#insn-004ebd24)
- ブロック [`004ebd24`](#insn-004ebd24) 範囲 `[['004ebd24', '004ebd27']]`
  - `CONDITIONAL_JUMP` [`004ebd24`](#insn-004ebd24) → [`004ebdbc`](#insn-004ebdbc)
  - `FALL_THROUGH` [`004ebd24`](#insn-004ebd24) → [`004ebd28`](#insn-004ebd28)
- ブロック [`004ebd28`](#insn-004ebd28) 範囲 `[['004ebd28', '004ebd3b']]`
  - `UNCONDITIONAL_JUMP` [`004ebd38`](#insn-004ebd38) → [`004ebdc8`](#insn-004ebdc8)
- ブロック [`004ebd3c`](#insn-004ebd3c) 範囲 `[['004ebd3c', '004ebd57']]`
  - `CONDITIONAL_JUMP` [`004ebd54`](#insn-004ebd54) → [`004ebf4c`](#insn-004ebf4c)
  - `FALL_THROUGH` [`004ebd54`](#insn-004ebd54) → [`004ebd58`](#insn-004ebd58)
- ブロック [`004ebd58`](#insn-004ebd58) 範囲 `[['004ebd58', '004ebd5f']]`
  - `CONDITIONAL_JUMP` [`004ebd5c`](#insn-004ebd5c) → [`004ebd98`](#insn-004ebd98)
  - `FALL_THROUGH` [`004ebd5c`](#insn-004ebd5c) → [`004ebd60`](#insn-004ebd60)
- ブロック [`004ebd60`](#insn-004ebd60) 範囲 `[['004ebd60', '004ebd97']]`
  - `CONDITIONAL_JUMP` [`004ebd94`](#insn-004ebd94) → [`004ebf78`](#insn-004ebf78)
  - `FALL_THROUGH` [`004ebd94`](#insn-004ebd94) → [`004ebd98`](#insn-004ebd98)
- ブロック [`004ebd98`](#insn-004ebd98) 範囲 `[['004ebd98', '004ebdbb']]`
  - `UNCONDITIONAL_JUMP` [`004ebdb8`](#insn-004ebdb8) → [`004ebf98`](#insn-004ebf98)
- ブロック [`004ebdbc`](#insn-004ebdbc) 範囲 `[['004ebdbc', '004ebdc7']]`
  - `FALL_THROUGH` [`004ebdc4`](#insn-004ebdc4) → [`004ebdc8`](#insn-004ebdc8)
- ブロック [`004ebdc8`](#insn-004ebdc8) 範囲 `[['004ebdc8', '004ebddb']]`
  - `CONDITIONAL_JUMP` [`004ebdd8`](#insn-004ebdd8) → [`004ebde4`](#insn-004ebde4)
  - `FALL_THROUGH` [`004ebdd8`](#insn-004ebdd8) → [`004ebddc`](#insn-004ebddc)
- ブロック [`004ebddc`](#insn-004ebddc) 範囲 `[['004ebddc', '004ebde3']]`
  - `FALL_THROUGH` [`004ebde0`](#insn-004ebde0) → [`004ebde4`](#insn-004ebde4)
- ブロック [`004ebde4`](#insn-004ebde4) 範囲 `[['004ebde4', '004ebdff']]`
  - `CONDITIONAL_JUMP` [`004ebdfc`](#insn-004ebdfc) → [`004ec158`](#insn-004ec158)
  - `FALL_THROUGH` [`004ebdfc`](#insn-004ebdfc) → [`004ebe00`](#insn-004ebe00)
- ブロック [`004ebe00`](#insn-004ebe00) 範囲 `[['004ebe00', '004ebe3f']]`
  - `CONDITIONAL_JUMP` [`004ebe3c`](#insn-004ebe3c) → [`004ec158`](#insn-004ec158)
  - `FALL_THROUGH` [`004ebe3c`](#insn-004ebe3c) → [`004ebe40`](#insn-004ebe40)
- ブロック [`004ebe40`](#insn-004ebe40) 範囲 `[['004ebe40', '004ebe4f']]`
  - `CONDITIONAL_JUMP` [`004ebe4c`](#insn-004ebe4c) → [`004ec158`](#insn-004ec158)
  - `FALL_THROUGH` [`004ebe4c`](#insn-004ebe4c) → [`004ebe50`](#insn-004ebe50)
- ブロック [`004ebe50`](#insn-004ebe50) 範囲 `[['004ebe50', '004ebe97']]`
  - `CONDITIONAL_JUMP` [`004ebe94`](#insn-004ebe94) → [`004ebedc`](#insn-004ebedc)
  - `FALL_THROUGH` [`004ebe94`](#insn-004ebe94) → [`004ebe98`](#insn-004ebe98)
- ブロック [`004ebe98`](#insn-004ebe98) 範囲 `[['004ebe98', '004ebea7']]`
  - `CONDITIONAL_JUMP` [`004ebea4`](#insn-004ebea4) → [`004ebed4`](#insn-004ebed4)
  - `FALL_THROUGH` [`004ebea4`](#insn-004ebea4) → [`004ebea8`](#insn-004ebea8)
- ブロック [`004ebea8`](#insn-004ebea8) 範囲 `[['004ebea8', '004ebeaf']]`
  - `UNCONDITIONAL_JUMP` [`004ebeac`](#insn-004ebeac) → [`004ebebc`](#insn-004ebebc)
- ブロック [`004ebeb0`](#insn-004ebeb0) 範囲 `[['004ebeb0', '004ebebb']]`
  - `CONDITIONAL_JUMP` [`004ebeb8`](#insn-004ebeb8) → [`004ebed0`](#insn-004ebed0)
  - `FALL_THROUGH` [`004ebeb8`](#insn-004ebeb8) → [`004ebebc`](#insn-004ebebc)
- ブロック [`004ebebc`](#insn-004ebebc) 範囲 `[['004ebebc', '004ebec3']]`
  - `CONDITIONAL_JUMP` [`004ebec0`](#insn-004ebec0) → [`004ebeb0`](#insn-004ebeb0)
  - `FALL_THROUGH` [`004ebec0`](#insn-004ebec0) → [`004ebec4`](#insn-004ebec4)
- ブロック [`004ebec4`](#insn-004ebec4) 範囲 `[['004ebec4', '004ebecf']]`
  - `UNCONDITIONAL_JUMP` [`004ebecc`](#insn-004ebecc) → [`004ebeb0`](#insn-004ebeb0)
- ブロック [`004ebed0`](#insn-004ebed0) 範囲 `[['004ebed0', '004ebed3']]`
  - `FALL_THROUGH` [`004ebed0`](#insn-004ebed0) → [`004ebed4`](#insn-004ebed4)
- ブロック [`004ebed4`](#insn-004ebed4) 範囲 `[['004ebed4', '004ebedb']]`
  - `FALL_THROUGH` [`004ebed8`](#insn-004ebed8) → [`004ebedc`](#insn-004ebedc)
- ブロック [`004ebedc`](#insn-004ebedc) 範囲 `[['004ebedc', '004ebee3']]`
  - `CONDITIONAL_JUMP` [`004ebee0`](#insn-004ebee0) → [`004ebf28`](#insn-004ebf28)
  - `FALL_THROUGH` [`004ebee0`](#insn-004ebee0) → [`004ebee4`](#insn-004ebee4)
- ブロック [`004ebee4`](#insn-004ebee4) 範囲 `[['004ebee4', '004ebef3']]`
  - `CONDITIONAL_JUMP` [`004ebef0`](#insn-004ebef0) → [`004ebf20`](#insn-004ebf20)
  - `FALL_THROUGH` [`004ebef0`](#insn-004ebef0) → [`004ebef4`](#insn-004ebef4)
- ブロック [`004ebef4`](#insn-004ebef4) 範囲 `[['004ebef4', '004ebefb']]`
  - `UNCONDITIONAL_JUMP` [`004ebef8`](#insn-004ebef8) → [`004ebf08`](#insn-004ebf08)
- ブロック [`004ebefc`](#insn-004ebefc) 範囲 `[['004ebefc', '004ebf07']]`
  - `CONDITIONAL_JUMP` [`004ebf04`](#insn-004ebf04) → [`004ebf1c`](#insn-004ebf1c)
  - `FALL_THROUGH` [`004ebf04`](#insn-004ebf04) → [`004ebf08`](#insn-004ebf08)
- ブロック [`004ebf08`](#insn-004ebf08) 範囲 `[['004ebf08', '004ebf0f']]`
  - `CONDITIONAL_JUMP` [`004ebf0c`](#insn-004ebf0c) → [`004ebefc`](#insn-004ebefc)
  - `FALL_THROUGH` [`004ebf0c`](#insn-004ebf0c) → [`004ebf10`](#insn-004ebf10)
- ブロック [`004ebf10`](#insn-004ebf10) 範囲 `[['004ebf10', '004ebf1b']]`
  - `UNCONDITIONAL_JUMP` [`004ebf18`](#insn-004ebf18) → [`004ebefc`](#insn-004ebefc)
- ブロック [`004ebf1c`](#insn-004ebf1c) 範囲 `[['004ebf1c', '004ebf1f']]`
  - `FALL_THROUGH` [`004ebf1c`](#insn-004ebf1c) → [`004ebf20`](#insn-004ebf20)
- ブロック [`004ebf20`](#insn-004ebf20) 範囲 `[['004ebf20', '004ebf27']]`
  - `FALL_THROUGH` [`004ebf24`](#insn-004ebf24) → [`004ebf28`](#insn-004ebf28)
- ブロック [`004ebf28`](#insn-004ebf28) 範囲 `[['004ebf28', '004ebf2f']]`
  - `CONDITIONAL_JUMP` [`004ebf2c`](#insn-004ebf2c) → [`004ebf38`](#insn-004ebf38)
  - `FALL_THROUGH` [`004ebf2c`](#insn-004ebf2c) → [`004ebf30`](#insn-004ebf30)
- ブロック [`004ebf30`](#insn-004ebf30) 範囲 `[['004ebf30', '004ebf37']]`
  - `FALL_THROUGH` [`004ebf34`](#insn-004ebf34) → [`004ebf38`](#insn-004ebf38)
- ブロック [`004ebf38`](#insn-004ebf38) 範囲 `[['004ebf38', '004ebf3f']]`
  - `CONDITIONAL_JUMP` [`004ebf3c`](#insn-004ebf3c) → [`004ebf98`](#insn-004ebf98)
  - `FALL_THROUGH` [`004ebf3c`](#insn-004ebf3c) → [`004ebf40`](#insn-004ebf40)
- ブロック [`004ebf40`](#insn-004ebf40) 範囲 `[['004ebf40', '004ebf4b']]`
  - `UNCONDITIONAL_JUMP` [`004ebf48`](#insn-004ebf48) → [`004ebf98`](#insn-004ebf98)
- ブロック [`004ebf4c`](#insn-004ebf4c) 範囲 `[['004ebf4c', '004ebf77']]`
  - `CONDITIONAL_JUMP` [`004ebf74`](#insn-004ebf74) → [`004ebd98`](#insn-004ebd98)
  - `FALL_THROUGH` [`004ebf74`](#insn-004ebf74) → [`004ebf78`](#insn-004ebf78)
- ブロック [`004ebf78`](#insn-004ebf78) 範囲 `[['004ebf78', '004ebf97']]`
  - `FALL_THROUGH` [`004ebf94`](#insn-004ebf94) → [`004ebf98`](#insn-004ebf98)
- ブロック [`004ebf98`](#insn-004ebf98) 範囲 `[['004ebf98', '004ebf9f']]`
  - `CONDITIONAL_JUMP` [`004ebf9c`](#insn-004ebf9c) → [`004ebfa8`](#insn-004ebfa8)
  - `FALL_THROUGH` [`004ebf9c`](#insn-004ebf9c) → [`004ebfa0`](#insn-004ebfa0)
- ブロック [`004ebfa0`](#insn-004ebfa0) 範囲 `[['004ebfa0', '004ebfa7']]`
  - `FALL_THROUGH` [`004ebfa4`](#insn-004ebfa4) → [`004ebfa8`](#insn-004ebfa8)
- ブロック [`004ebfa8`](#insn-004ebfa8) 範囲 `[['004ebfa8', '004ebfeb']]`
  - `CONDITIONAL_JUMP` [`004ebfe8`](#insn-004ebfe8) → [`004ec010`](#insn-004ec010)
  - `FALL_THROUGH` [`004ebfe8`](#insn-004ebfe8) → [`004ebfec`](#insn-004ebfec)
- ブロック [`004ebfec`](#insn-004ebfec) 範囲 `[['004ebfec', '004ec00f']]`
  - `FALL_THROUGH` [`004ec00c`](#insn-004ec00c) → [`004ec010`](#insn-004ec010)
- ブロック [`004ec010`](#insn-004ec010) 範囲 `[['004ec010', '004ec073']]`
  - `CONDITIONAL_JUMP` [`004ec070`](#insn-004ec070) → [`004ec0ac`](#insn-004ec0ac)
  - `FALL_THROUGH` [`004ec070`](#insn-004ec070) → [`004ec074`](#insn-004ec074)
- ブロック [`004ec074`](#insn-004ec074) 範囲 `[['004ec074', '004ec083']]`
  - `CONDITIONAL_JUMP` [`004ec080`](#insn-004ec080) → [`004ec0a4`](#insn-004ec0a4)
  - `FALL_THROUGH` [`004ec080`](#insn-004ec080) → [`004ec084`](#insn-004ec084)
- ブロック [`004ec084`](#insn-004ec084) 範囲 `[['004ec084', '004ec087']]`
  - `FALL_THROUGH` [`004ec084`](#insn-004ec084) → [`004ec088`](#insn-004ec088)
- ブロック [`004ec088`](#insn-004ec088) 範囲 `[['004ec088', '004ec09f']]`
  - `CONDITIONAL_JUMP` [`004ec09c`](#insn-004ec09c) → [`004ec088`](#insn-004ec088)
  - `FALL_THROUGH` [`004ec09c`](#insn-004ec09c) → [`004ec0a0`](#insn-004ec0a0)
- ブロック [`004ec0a0`](#insn-004ec0a0) 範囲 `[['004ec0a0', '004ec0a3']]`
  - `FALL_THROUGH` [`004ec0a0`](#insn-004ec0a0) → [`004ec0a4`](#insn-004ec0a4)
- ブロック [`004ec0a4`](#insn-004ec0a4) 範囲 `[['004ec0a4', '004ec0ab']]`
  - `FALL_THROUGH` [`004ec0a8`](#insn-004ec0a8) → [`004ec0ac`](#insn-004ec0ac)
- ブロック [`004ec0ac`](#insn-004ec0ac) 範囲 `[['004ec0ac', '004ec0b3']]`
  - `CONDITIONAL_JUMP` [`004ec0b0`](#insn-004ec0b0) → [`004ec0d8`](#insn-004ec0d8)
  - `FALL_THROUGH` [`004ec0b0`](#insn-004ec0b0) → [`004ec0b4`](#insn-004ec0b4)
- ブロック [`004ec0b4`](#insn-004ec0b4) 範囲 `[['004ec0b4', '004ec0d7']]`
  - `FALL_THROUGH` [`004ec0d4`](#insn-004ec0d4) → [`004ec0d8`](#insn-004ec0d8)
- ブロック [`004ec0d8`](#insn-004ec0d8) 範囲 `[['004ec0d8', '004ec0df']]`
  - `CONDITIONAL_JUMP` [`004ec0dc`](#insn-004ec0dc) → [`004ec0e8`](#insn-004ec0e8)
  - `FALL_THROUGH` [`004ec0dc`](#insn-004ec0dc) → [`004ec0e0`](#insn-004ec0e0)
- ブロック [`004ec0e0`](#insn-004ec0e0) 範囲 `[['004ec0e0', '004ec0e7']]`
  - `FALL_THROUGH` [`004ec0e4`](#insn-004ec0e4) → [`004ec0e8`](#insn-004ec0e8)
- ブロック [`004ec0e8`](#insn-004ec0e8) 範囲 `[['004ec0e8', '004ec0ef']]`
  - `CONDITIONAL_JUMP` [`004ec0ec`](#insn-004ec0ec) → [`004ec0f8`](#insn-004ec0f8)
  - `FALL_THROUGH` [`004ec0ec`](#insn-004ec0ec) → [`004ec0f0`](#insn-004ec0f0)
- ブロック [`004ec0f0`](#insn-004ec0f0) 範囲 `[['004ec0f0', '004ec0f7']]`
  - `FALL_THROUGH` [`004ec0f4`](#insn-004ec0f4) → [`004ec0f8`](#insn-004ec0f8)
- ブロック [`004ec0f8`](#insn-004ec0f8) 範囲 `[['004ec0f8', '004ec0ff']]`
  - `CONDITIONAL_JUMP` [`004ec0fc`](#insn-004ec0fc) → [`004ec108`](#insn-004ec108)
  - `FALL_THROUGH` [`004ec0fc`](#insn-004ec0fc) → [`004ec100`](#insn-004ec100)
- ブロック [`004ec100`](#insn-004ec100) 範囲 `[['004ec100', '004ec107']]`
  - `FALL_THROUGH` [`004ec104`](#insn-004ec104) → [`004ec108`](#insn-004ec108)
- ブロック [`004ec108`](#insn-004ec108) 範囲 `[['004ec108', '004ec10f']]`
  - `CONDITIONAL_JUMP` [`004ec10c`](#insn-004ec10c) → [`004ec118`](#insn-004ec118)
  - `FALL_THROUGH` [`004ec10c`](#insn-004ec10c) → [`004ec110`](#insn-004ec110)
- ブロック [`004ec110`](#insn-004ec110) 範囲 `[['004ec110', '004ec117']]`
  - `FALL_THROUGH` [`004ec114`](#insn-004ec114) → [`004ec118`](#insn-004ec118)
- ブロック [`004ec118`](#insn-004ec118) 範囲 `[['004ec118', '004ec11f']]`
  - `CONDITIONAL_JUMP` [`004ec11c`](#insn-004ec11c) → [`004ec128`](#insn-004ec128)
  - `FALL_THROUGH` [`004ec11c`](#insn-004ec11c) → [`004ec120`](#insn-004ec120)
- ブロック [`004ec120`](#insn-004ec120) 範囲 `[['004ec120', '004ec127']]`
  - `FALL_THROUGH` [`004ec124`](#insn-004ec124) → [`004ec128`](#insn-004ec128)
- ブロック [`004ec128`](#insn-004ec128) 範囲 `[['004ec128', '004ec137']]`
  - `CONDITIONAL_JUMP` [`004ec134`](#insn-004ec134) → [`004ec294`](#insn-004ec294)
  - `FALL_THROUGH` [`004ec134`](#insn-004ec134) → [`004ec138`](#insn-004ec138)
- ブロック [`004ec138`](#insn-004ec138) 範囲 `[['004ec138', '004ec157']]`
- ブロック [`004ec158`](#insn-004ec158) 範囲 `[['004ec158', '004ec197']]`
  - `CONDITIONAL_JUMP` [`004ec194`](#insn-004ec194) → [`004ec294`](#insn-004ec294)
  - `FALL_THROUGH` [`004ec194`](#insn-004ec194) → [`004ec198`](#insn-004ec198)
- ブロック [`004ec198`](#insn-004ec198) 範囲 `[['004ec198', '004ec1b3']]`
- ブロック [`004ec294`](#insn-004ec294) 範囲 `[['004ec294', '004ec297']]`

## 命令位置別の参照

- [`004ebcb0`](#insn-004ebcb0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ebcb4`](#insn-004ebcb4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ebcb8`](#insn-004ebcb8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ebcbc`](#insn-004ebcbc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ebcc0`](#insn-004ebcc0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ebcc4`](#insn-004ebcc4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ebcf0`](#insn-004ebcf0) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ebd20`](#insn-004ebd20) → [`004ebd3c`](#insn-004ebd3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ebd24`](#insn-004ebd24) → [`004ebdbc`](#insn-004ebdbc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ebd30`](#insn-004ebd30) → `Stack[-0x180]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ebd34`](#insn-004ebd34) → `Stack[-0x170]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ebd38`](#insn-004ebd38) → [`004ebdc8`](#insn-004ebdc8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ebd3c`](#insn-004ebd3c) → `Stack[-0x148]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ebd40`](#insn-004ebd40) → `Stack[-0x140]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ebd54`](#insn-004ebd54) → [`004ebf4c`](#insn-004ebf4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ebd5c`](#insn-004ebd5c) → [`004ebd98`](#insn-004ebd98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ebd60`](#insn-004ebd60) → `Stack[-0x138]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ebd78`](#insn-004ebd78) → `Stack[-0x147]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ebd80`](#insn-004ebd80) → `Stack[-0x13f]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ebd94`](#insn-004ebd94) → [`004ebf78`](#insn-004ebf78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ebda8`](#insn-004ebda8) → `002bec26`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`004ebda8`](#insn-004ebda8) → `002a9b52`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`004ebda8`](#insn-004ebda8) → `Stack[-0xc8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ebdb4`](#insn-004ebdb4) → [`0053691c`](../00536/0053691c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0053691c` · 推定シンボル `None` · 推定型 `None`
- [`004ebdb8`](#insn-004ebdb8) → [`004ebf98`](#insn-004ebf98) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ebdc4`](#insn-004ebdc4) → [`0043bb60`](../0043b/0043bb60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bb60` · 推定シンボル `None` · 推定型 `None`
- [`004ebdd0`](#insn-004ebdd0) → [`00c58e10`](../00c58/00c58e10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58e10` · 推定シンボル `None` · 推定型 `None`
- [`004ebdd4`](#insn-004ebdd4) → `Stack[-0x180]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ebdd8`](#insn-004ebdd8) → [`004ebde4`](#insn-004ebde4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ebddc`](#insn-004ebddc) → `Stack[-0x170]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ebde0`](#insn-004ebde0) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`004ebde4`](#insn-004ebde4) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ebde8`](#insn-004ebde8) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ebdfc`](#insn-004ebdfc) → [`004ec158`](#insn-004ec158) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ebe00`](#insn-004ebe00) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ebe1c`](#insn-004ebe1c) → `Stack[-0xaf]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ebe20`](#insn-004ebe20) → `Stack[-0xa7]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ebe3c`](#insn-004ebe3c) → [`004ec158`](#insn-004ec158) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ebe40`](#insn-004ebe40) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ebe4c`](#insn-004ebe4c) → [`004ec158`](#insn-004ec158) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ebe5c`](#insn-004ebe5c) → [`00c58c60`](../00c58/00c58c60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58c60` · 推定シンボル `None` · 推定型 `None`
- [`004ebe6c`](#insn-004ebe6c) → [`00c58c60`](../00c58/00c58c60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58c60` · 推定シンボル `None` · 推定型 `None`
- [`004ebe70`](#insn-004ebe70) → `Stack[-0xe0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ebe74`](#insn-004ebe74) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ebe78`](#insn-004ebe78) → `Stack[-0xf8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ebe7c`](#insn-004ebe7c) → `Stack[-0xe8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ebe80`](#insn-004ebe80) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ebe84`](#insn-004ebe84) → `Stack[-0x130]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ebe88`](#insn-004ebe88) → `Stack[-0x120]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ebe8c`](#insn-004ebe8c) → `Stack[-0x118]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ebe90`](#insn-004ebe90) → `Stack[-0x108]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ebe94`](#insn-004ebe94) → [`004ebedc`](#insn-004ebedc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ebe98`](#insn-004ebe98) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ebea4`](#insn-004ebea4) → [`004ebed4`](#insn-004ebed4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ebeac`](#insn-004ebeac) → [`004ebebc`](#insn-004ebebc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ebeb8`](#insn-004ebeb8) → [`004ebed0`](#insn-004ebed0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ebec0`](#insn-004ebec0) → [`004ebeb0`](#insn-004ebeb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ebec8`](#insn-004ebec8) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`004ebecc`](#insn-004ebecc) → [`004ebeb0`](#insn-004ebeb0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ebed0`](#insn-004ebed0) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ebed4`](#insn-004ebed4) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ebed8`](#insn-004ebed8) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`004ebedc`](#insn-004ebedc) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ebee0`](#insn-004ebee0) → [`004ebf28`](#insn-004ebf28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ebee4`](#insn-004ebee4) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ebef0`](#insn-004ebef0) → [`004ebf20`](#insn-004ebf20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ebef8`](#insn-004ebef8) → [`004ebf08`](#insn-004ebf08) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ebf04`](#insn-004ebf04) → [`004ebf1c`](#insn-004ebf1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ebf0c`](#insn-004ebf0c) → [`004ebefc`](#insn-004ebefc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ebf14`](#insn-004ebf14) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`004ebf18`](#insn-004ebf18) → [`004ebefc`](#insn-004ebefc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ebf1c`](#insn-004ebf1c) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ebf20`](#insn-004ebf20) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ebf24`](#insn-004ebf24) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`004ebf28`](#insn-004ebf28) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ebf2c`](#insn-004ebf2c) → [`004ebf38`](#insn-004ebf38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ebf30`](#insn-004ebf30) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ebf34`](#insn-004ebf34) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`004ebf38`](#insn-004ebf38) → `Stack[-0xc8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ebf3c`](#insn-004ebf3c) → [`004ebf98`](#insn-004ebf98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ebf40`](#insn-004ebf40) → `Stack[-0xb8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ebf44`](#insn-004ebf44) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`004ebf48`](#insn-004ebf48) → [`004ebf98`](#insn-004ebf98) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ebf4c`](#insn-004ebf4c) → `Stack[-0x138]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ebf64`](#insn-004ebf64) → `Stack[-0x147]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ebf74`](#insn-004ebf74) → [`004ebd98`](#insn-004ebd98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ebf88`](#insn-004ebf88) → `002ab371`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`004ebf88`](#insn-004ebf88) → `002bb295`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`004ebf88`](#insn-004ebf88) → `Stack[-0xc8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ebf94`](#insn-004ebf94) → [`0053691c`](../00536/0053691c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0053691c` · 推定シンボル `None` · 推定型 `None`
- [`004ebf98`](#insn-004ebf98) → `Stack[-0x148]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ebf9c`](#insn-004ebf9c) → [`004ebfa8`](#insn-004ebfa8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ebfa0`](#insn-004ebfa0) → `Stack[-0x138]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ebfa4`](#insn-004ebfa4) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`004ebfb0`](#insn-004ebfb0) → [`00c596b0`](../00c59/00c596b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c596b0` · 推定シンボル `None` · 推定型 `None`
- [`004ebfb8`](#insn-004ebfb8) → `Stack[-0xe0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ebfdc`](#insn-004ebfdc) → [`004e2494`](../004e2/004e2494.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004e2494` · 推定シンボル `None` · 推定型 `None`
- [`004ebfe0`](#insn-004ebfe0) → `Stack[-0x180]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ebfe8`](#insn-004ebfe8) → [`004ec010`](#insn-004ec010) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ebfec`](#insn-004ebfec) → `Stack[-0x178]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ebff0`](#insn-004ebff0) → `Stack[-0x170]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ebff4`](#insn-004ebff4) → `00c67808`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004ec004`](#insn-004ec004) → [`0112a058`](../0112a/0112a058.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `0112a058` · 推定シンボル `None` · 推定型 `None`
- [`004ec00c`](#insn-004ec00c) → [`00c58730`](../00c58/00c58730.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58730` · 推定シンボル `None` · 推定型 `None`
- [`004ec014`](#insn-004ec014) → `Stack[-0x170]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec018`](#insn-004ec018) → `Stack[-0x180]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec028`](#insn-004ec028) → [`00c58780`](../00c58/00c58780.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58780` · 推定シンボル `None` · 推定型 `None`
- [`004ec02c`](#insn-004ec02c) → `Stack[-0xc8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec040`](#insn-004ec040) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec054`](#insn-004ec054) → [`00c588f0`](../00c58/00c588f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c588f0` · 推定シンボル `None` · 推定型 `None`
- [`004ec05c`](#insn-004ec05c) → [`00c587a0`](../00c58/00c587a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c587a0` · 推定シンボル `None` · 推定型 `None`
- [`004ec068`](#insn-004ec068) → [`004a6df0`](../004a6/004a6df0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004a6df0` · 推定シンボル `None` · 推定型 `None`
- [`004ec06c`](#insn-004ec06c) → `Stack[-0x168]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec070`](#insn-004ec070) → [`004ec0ac`](#insn-004ec0ac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec074`](#insn-004ec074) → `Stack[-0x160]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec080`](#insn-004ec080) → [`004ec0a4`](#insn-004ec0a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec094`](#insn-004ec094) → [`00535bc0`](../00535/00535bc0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00535bc0` · 推定シンボル `None` · 推定型 `None`
- [`004ec09c`](#insn-004ec09c) → [`004ec088`](#insn-004ec088) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec0a0`](#insn-004ec0a0) → `Stack[-0x168]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec0a4`](#insn-004ec0a4) → `Stack[-0x160]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec0a8`](#insn-004ec0a8) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`004ec0ac`](#insn-004ec0ac) → `Stack[-0x180]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec0b0`](#insn-004ec0b0) → [`004ec0d8`](#insn-004ec0d8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec0b4`](#insn-004ec0b4) → `Stack[-0x178]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec0b8`](#insn-004ec0b8) → `Stack[-0x170]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec0bc`](#insn-004ec0bc) → `00c67808`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004ec0cc`](#insn-004ec0cc) → [`0112a058`](../0112a/0112a058.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `0112a058` · 推定シンボル `None` · 推定型 `None`
- [`004ec0d4`](#insn-004ec0d4) → [`00c58730`](../00c58/00c58730.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58730` · 推定シンボル `None` · 推定型 `None`
- [`004ec0d8`](#insn-004ec0d8) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec0dc`](#insn-004ec0dc) → [`004ec0e8`](#insn-004ec0e8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec0e0`](#insn-004ec0e0) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec0e4`](#insn-004ec0e4) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`004ec0e8`](#insn-004ec0e8) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec0ec`](#insn-004ec0ec) → [`004ec0f8`](#insn-004ec0f8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec0f0`](#insn-004ec0f0) → `Stack[-0x98]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec0f4`](#insn-004ec0f4) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`004ec0f8`](#insn-004ec0f8) → `Stack[-0xb8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec0fc`](#insn-004ec0fc) → [`004ec108`](#insn-004ec108) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec100`](#insn-004ec100) → `Stack[-0xb0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec104`](#insn-004ec104) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`004ec108`](#insn-004ec108) → `Stack[-0x118]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec10c`](#insn-004ec10c) → [`004ec118`](#insn-004ec118) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec110`](#insn-004ec110) → `Stack[-0x108]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec114`](#insn-004ec114) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`004ec118`](#insn-004ec118) → `Stack[-0x130]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec11c`](#insn-004ec11c) → [`004ec128`](#insn-004ec128) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec120`](#insn-004ec120) → `Stack[-0x120]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec124`](#insn-004ec124) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`004ec12c`](#insn-004ec12c) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec134`](#insn-004ec134) → [`004ec294`](#insn-004ec294) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec138`](#insn-004ec138) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec13c`](#insn-004ec13c) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec140`](#insn-004ec140) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec144`](#insn-004ec144) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec148`](#insn-004ec148) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec14c`](#insn-004ec14c) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec15c`](#insn-004ec15c) → [`00c57fc0`](../00c57/00c57fc0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fc0` · 推定シンボル `None` · 推定型 `None`
- [`004ec168`](#insn-004ec168) → `002bc686`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`004ec174`](#insn-004ec174) → [`00c58180`](../00c58/00c58180.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58180` · 推定シンボル `None` · 推定型 `None`
- [`004ec184`](#insn-004ec184) → [`00c58890`](../00c58/00c58890.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58890` · 推定シンボル `None` · 推定型 `None`
- [`004ec18c`](#insn-004ec18c) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec194`](#insn-004ec194) → [`004ec294`](#insn-004ec294) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ec1a0`](#insn-004ec1a0) → [`005358a8`](../00535/005358a8.md) · `PARAM` · `ANALYSIS` · 関数 `005358a8` · 推定シンボル `None` · 推定型 `None`
- [`004ec1a4`](#insn-004ec1a4) → `00c9ae58`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004ec1a4`](#insn-004ec1a4) → `00c66318`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTIN5Botan9ExceptionE` · 推定型 `pointer __((offset(0x10)))`
- [`004ec1b0`](#insn-004ec1b0) → [`00c57fe0`](../00c57/00c57fe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fe0` · 推定シンボル `None` · 推定型 `None`
- [`004ec294`](#insn-004ec294) → [`00c57fb0`](../00c57/00c57fb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fb0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`004ebcb0`](#insn-004ebcb0)

~~~json
{
  "source": "004ebcb0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ebcb4`](#insn-004ebcb4)

~~~json
{
  "source": "004ebcb4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ebcb8`](#insn-004ebcb8)

~~~json
{
  "source": "004ebcb8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ebcbc`](#insn-004ebcbc)

~~~json
{
  "source": "004ebcbc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ebcc0`](#insn-004ebcc0)

~~~json
{
  "source": "004ebcc0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ebcc4`](#insn-004ebcc4)

~~~json
{
  "source": "004ebcc4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ebcf0`](#insn-004ebcf0)

~~~json
{
  "source": "004ebcf0",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ebd20`](#insn-004ebd20)

~~~json
{
  "source": "004ebd20",
  "target": "004ebd3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ebd24`](#insn-004ebd24)

~~~json
{
  "source": "004ebd24",
  "target": "004ebdbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ebd30`](#insn-004ebd30)

~~~json
{
  "source": "004ebd30",
  "target": "Stack[-0x180]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ebd34`](#insn-004ebd34)

~~~json
{
  "source": "004ebd34",
  "target": "Stack[-0x170]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ebd38`](#insn-004ebd38)

~~~json
{
  "source": "004ebd38",
  "target": "004ebdc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ebd3c`](#insn-004ebd3c)

~~~json
{
  "source": "004ebd3c",
  "target": "Stack[-0x148]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ebd40`](#insn-004ebd40)

~~~json
{
  "source": "004ebd40",
  "target": "Stack[-0x140]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ebd54`](#insn-004ebd54)

~~~json
{
  "source": "004ebd54",
  "target": "004ebf4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ebd5c`](#insn-004ebd5c)

~~~json
{
  "source": "004ebd5c",
  "target": "004ebd98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ebd60`](#insn-004ebd60)

~~~json
{
  "source": "004ebd60",
  "target": "Stack[-0x138]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ebd78`](#insn-004ebd78)

~~~json
{
  "source": "004ebd78",
  "target": "Stack[-0x147]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ebd80`](#insn-004ebd80)

~~~json
{
  "source": "004ebd80",
  "target": "Stack[-0x13f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ebd94`](#insn-004ebd94)

~~~json
{
  "source": "004ebd94",
  "target": "004ebf78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ebda8`](#insn-004ebda8)

~~~json
{
  "source": "004ebda8",
  "target": "002bec26",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002bec26",
  "offset": 0,
  "size": 12,
  "datatype": "string",
  "bytes": "4145532d3235362f43424300",
  "capture_start": "002bec26",
  "capture_bytes": 12,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`004ebda8`](#insn-004ebda8)

~~~json
{
  "source": "004ebda8",
  "target": "002a9b52",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a9b52",
  "offset": 0,
  "size": 8,
  "datatype": "string",
  "bytes": "5348412d32353600",
  "capture_start": "002a9b52",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`004ebda8`](#insn-004ebda8)

~~~json
{
  "source": "004ebda8",
  "target": "Stack[-0xc8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ebdb4`](#insn-004ebdb4)

~~~json
{
  "source": "004ebdb4",
  "target": "0053691c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ebdb8`](#insn-004ebdb8)

~~~json
{
  "source": "004ebdb8",
  "target": "004ebf98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ebdc4`](#insn-004ebdc4)

~~~json
{
  "source": "004ebdc4",
  "target": "0043bb60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ebdd0`](#insn-004ebdd0)

~~~json
{
  "source": "004ebdd0",
  "target": "00c58e10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ebdd4`](#insn-004ebdd4)

~~~json
{
  "source": "004ebdd4",
  "target": "Stack[-0x180]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ebdd8`](#insn-004ebdd8)

~~~json
{
  "source": "004ebdd8",
  "target": "004ebde4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ebddc`](#insn-004ebddc)

~~~json
{
  "source": "004ebddc",
  "target": "Stack[-0x170]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ebde0`](#insn-004ebde0)

~~~json
{
  "source": "004ebde0",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ebde4`](#insn-004ebde4)

~~~json
{
  "source": "004ebde4",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ebde8`](#insn-004ebde8)

~~~json
{
  "source": "004ebde8",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ebdfc`](#insn-004ebdfc)

~~~json
{
  "source": "004ebdfc",
  "target": "004ec158",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ebe00`](#insn-004ebe00)

~~~json
{
  "source": "004ebe00",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ebe1c`](#insn-004ebe1c)

~~~json
{
  "source": "004ebe1c",
  "target": "Stack[-0xaf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ebe20`](#insn-004ebe20)

~~~json
{
  "source": "004ebe20",
  "target": "Stack[-0xa7]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ebe3c`](#insn-004ebe3c)

~~~json
{
  "source": "004ebe3c",
  "target": "004ec158",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ebe40`](#insn-004ebe40)

~~~json
{
  "source": "004ebe40",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ebe4c`](#insn-004ebe4c)

~~~json
{
  "source": "004ebe4c",
  "target": "004ec158",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ebe5c`](#insn-004ebe5c)

~~~json
{
  "source": "004ebe5c",
  "target": "00c58c60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ebe6c`](#insn-004ebe6c)

~~~json
{
  "source": "004ebe6c",
  "target": "00c58c60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ebe70`](#insn-004ebe70)

~~~json
{
  "source": "004ebe70",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ebe74`](#insn-004ebe74)

~~~json
{
  "source": "004ebe74",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ebe78`](#insn-004ebe78)

~~~json
{
  "source": "004ebe78",
  "target": "Stack[-0xf8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ebe7c`](#insn-004ebe7c)

~~~json
{
  "source": "004ebe7c",
  "target": "Stack[-0xe8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ebe80`](#insn-004ebe80)

~~~json
{
  "source": "004ebe80",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ebe84`](#insn-004ebe84)

~~~json
{
  "source": "004ebe84",
  "target": "Stack[-0x130]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ebe88`](#insn-004ebe88)

~~~json
{
  "source": "004ebe88",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ebe8c`](#insn-004ebe8c)

~~~json
{
  "source": "004ebe8c",
  "target": "Stack[-0x118]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ebe90`](#insn-004ebe90)

~~~json
{
  "source": "004ebe90",
  "target": "Stack[-0x108]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ebe94`](#insn-004ebe94)

~~~json
{
  "source": "004ebe94",
  "target": "004ebedc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ebe98`](#insn-004ebe98)

~~~json
{
  "source": "004ebe98",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ebea4`](#insn-004ebea4)

~~~json
{
  "source": "004ebea4",
  "target": "004ebed4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ebeac`](#insn-004ebeac)

~~~json
{
  "source": "004ebeac",
  "target": "004ebebc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ebeb8`](#insn-004ebeb8)

~~~json
{
  "source": "004ebeb8",
  "target": "004ebed0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ebec0`](#insn-004ebec0)

~~~json
{
  "source": "004ebec0",
  "target": "004ebeb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ebec8`](#insn-004ebec8)

~~~json
{
  "source": "004ebec8",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ebecc`](#insn-004ebecc)

~~~json
{
  "source": "004ebecc",
  "target": "004ebeb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ebed0`](#insn-004ebed0)

~~~json
{
  "source": "004ebed0",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ebed4`](#insn-004ebed4)

~~~json
{
  "source": "004ebed4",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ebed8`](#insn-004ebed8)

~~~json
{
  "source": "004ebed8",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ebedc`](#insn-004ebedc)

~~~json
{
  "source": "004ebedc",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ebee0`](#insn-004ebee0)

~~~json
{
  "source": "004ebee0",
  "target": "004ebf28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ebee4`](#insn-004ebee4)

~~~json
{
  "source": "004ebee4",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ebef0`](#insn-004ebef0)

~~~json
{
  "source": "004ebef0",
  "target": "004ebf20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ebef8`](#insn-004ebef8)

~~~json
{
  "source": "004ebef8",
  "target": "004ebf08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ebf04`](#insn-004ebf04)

~~~json
{
  "source": "004ebf04",
  "target": "004ebf1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ebf0c`](#insn-004ebf0c)

~~~json
{
  "source": "004ebf0c",
  "target": "004ebefc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ebf14`](#insn-004ebf14)

~~~json
{
  "source": "004ebf14",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ebf18`](#insn-004ebf18)

~~~json
{
  "source": "004ebf18",
  "target": "004ebefc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ebf1c`](#insn-004ebf1c)

~~~json
{
  "source": "004ebf1c",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ebf20`](#insn-004ebf20)

~~~json
{
  "source": "004ebf20",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ebf24`](#insn-004ebf24)

~~~json
{
  "source": "004ebf24",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ebf28`](#insn-004ebf28)

~~~json
{
  "source": "004ebf28",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ebf2c`](#insn-004ebf2c)

~~~json
{
  "source": "004ebf2c",
  "target": "004ebf38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ebf30`](#insn-004ebf30)

~~~json
{
  "source": "004ebf30",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ebf34`](#insn-004ebf34)

~~~json
{
  "source": "004ebf34",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ebf38`](#insn-004ebf38)

~~~json
{
  "source": "004ebf38",
  "target": "Stack[-0xc8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ebf3c`](#insn-004ebf3c)

~~~json
{
  "source": "004ebf3c",
  "target": "004ebf98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ebf40`](#insn-004ebf40)

~~~json
{
  "source": "004ebf40",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ebf44`](#insn-004ebf44)

~~~json
{
  "source": "004ebf44",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ebf48`](#insn-004ebf48)

~~~json
{
  "source": "004ebf48",
  "target": "004ebf98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ebf4c`](#insn-004ebf4c)

~~~json
{
  "source": "004ebf4c",
  "target": "Stack[-0x138]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ebf64`](#insn-004ebf64)

~~~json
{
  "source": "004ebf64",
  "target": "Stack[-0x147]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ebf74`](#insn-004ebf74)

~~~json
{
  "source": "004ebf74",
  "target": "004ebd98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ebf88`](#insn-004ebf88)

~~~json
{
  "source": "004ebf88",
  "target": "002ab371",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002ab371",
  "offset": 0,
  "size": 12,
  "datatype": "string",
  "bytes": "4145532d3235362f47434d00",
  "capture_start": "002ab371",
  "capture_bytes": 12,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`004ebf88`](#insn-004ebf88)

~~~json
{
  "source": "004ebf88",
  "target": "002bb295",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002bb295",
  "offset": 0,
  "size": 8,
  "datatype": "string",
  "bytes": "5348412d35313200",
  "capture_start": "002bb295",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`004ebf88`](#insn-004ebf88)

~~~json
{
  "source": "004ebf88",
  "target": "Stack[-0xc8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ebf94`](#insn-004ebf94)

~~~json
{
  "source": "004ebf94",
  "target": "0053691c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ebf98`](#insn-004ebf98)

~~~json
{
  "source": "004ebf98",
  "target": "Stack[-0x148]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ebf9c`](#insn-004ebf9c)

~~~json
{
  "source": "004ebf9c",
  "target": "004ebfa8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ebfa0`](#insn-004ebfa0)

~~~json
{
  "source": "004ebfa0",
  "target": "Stack[-0x138]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ebfa4`](#insn-004ebfa4)

~~~json
{
  "source": "004ebfa4",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ebfb0`](#insn-004ebfb0)

~~~json
{
  "source": "004ebfb0",
  "target": "00c596b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ebfb8`](#insn-004ebfb8)

~~~json
{
  "source": "004ebfb8",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ebfdc`](#insn-004ebfdc)

~~~json
{
  "source": "004ebfdc",
  "target": "004e2494",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ebfe0`](#insn-004ebfe0)

~~~json
{
  "source": "004ebfe0",
  "target": "Stack[-0x180]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ebfe8`](#insn-004ebfe8)

~~~json
{
  "source": "004ebfe8",
  "target": "004ec010",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ebfec`](#insn-004ebfec)

~~~json
{
  "source": "004ebfec",
  "target": "Stack[-0x178]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ebff0`](#insn-004ebff0)

~~~json
{
  "source": "004ebff0",
  "target": "Stack[-0x170]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ebff4`](#insn-004ebff4)

~~~json
{
  "source": "004ebff4",
  "target": "00c67808",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c67808",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004ec004`](#insn-004ec004)

~~~json
{
  "source": "004ec004",
  "target": "0112a058",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ec00c`](#insn-004ec00c)

~~~json
{
  "source": "004ec00c",
  "target": "00c58730",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ec014`](#insn-004ec014)

~~~json
{
  "source": "004ec014",
  "target": "Stack[-0x170]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec018`](#insn-004ec018)

~~~json
{
  "source": "004ec018",
  "target": "Stack[-0x180]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec028`](#insn-004ec028)

~~~json
{
  "source": "004ec028",
  "target": "00c58780",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ec02c`](#insn-004ec02c)

~~~json
{
  "source": "004ec02c",
  "target": "Stack[-0xc8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec040`](#insn-004ec040)

~~~json
{
  "source": "004ec040",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec054`](#insn-004ec054)

~~~json
{
  "source": "004ec054",
  "target": "00c588f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ec05c`](#insn-004ec05c)

~~~json
{
  "source": "004ec05c",
  "target": "00c587a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ec068`](#insn-004ec068)

~~~json
{
  "source": "004ec068",
  "target": "004a6df0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ec06c`](#insn-004ec06c)

~~~json
{
  "source": "004ec06c",
  "target": "Stack[-0x168]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec070`](#insn-004ec070)

~~~json
{
  "source": "004ec070",
  "target": "004ec0ac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec074`](#insn-004ec074)

~~~json
{
  "source": "004ec074",
  "target": "Stack[-0x160]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec080`](#insn-004ec080)

~~~json
{
  "source": "004ec080",
  "target": "004ec0a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec094`](#insn-004ec094)

~~~json
{
  "source": "004ec094",
  "target": "00535bc0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ec09c`](#insn-004ec09c)

~~~json
{
  "source": "004ec09c",
  "target": "004ec088",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec0a0`](#insn-004ec0a0)

~~~json
{
  "source": "004ec0a0",
  "target": "Stack[-0x168]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec0a4`](#insn-004ec0a4)

~~~json
{
  "source": "004ec0a4",
  "target": "Stack[-0x160]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec0a8`](#insn-004ec0a8)

~~~json
{
  "source": "004ec0a8",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ec0ac`](#insn-004ec0ac)

~~~json
{
  "source": "004ec0ac",
  "target": "Stack[-0x180]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec0b0`](#insn-004ec0b0)

~~~json
{
  "source": "004ec0b0",
  "target": "004ec0d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec0b4`](#insn-004ec0b4)

~~~json
{
  "source": "004ec0b4",
  "target": "Stack[-0x178]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec0b8`](#insn-004ec0b8)

~~~json
{
  "source": "004ec0b8",
  "target": "Stack[-0x170]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec0bc`](#insn-004ec0bc)

~~~json
{
  "source": "004ec0bc",
  "target": "00c67808",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c67808",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004ec0cc`](#insn-004ec0cc)

~~~json
{
  "source": "004ec0cc",
  "target": "0112a058",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ec0d4`](#insn-004ec0d4)

~~~json
{
  "source": "004ec0d4",
  "target": "00c58730",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ec0d8`](#insn-004ec0d8)

~~~json
{
  "source": "004ec0d8",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec0dc`](#insn-004ec0dc)

~~~json
{
  "source": "004ec0dc",
  "target": "004ec0e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec0e0`](#insn-004ec0e0)

~~~json
{
  "source": "004ec0e0",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec0e4`](#insn-004ec0e4)

~~~json
{
  "source": "004ec0e4",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ec0e8`](#insn-004ec0e8)

~~~json
{
  "source": "004ec0e8",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec0ec`](#insn-004ec0ec)

~~~json
{
  "source": "004ec0ec",
  "target": "004ec0f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec0f0`](#insn-004ec0f0)

~~~json
{
  "source": "004ec0f0",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec0f4`](#insn-004ec0f4)

~~~json
{
  "source": "004ec0f4",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ec0f8`](#insn-004ec0f8)

~~~json
{
  "source": "004ec0f8",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec0fc`](#insn-004ec0fc)

~~~json
{
  "source": "004ec0fc",
  "target": "004ec108",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec100`](#insn-004ec100)

~~~json
{
  "source": "004ec100",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec104`](#insn-004ec104)

~~~json
{
  "source": "004ec104",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ec108`](#insn-004ec108)

~~~json
{
  "source": "004ec108",
  "target": "Stack[-0x118]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec10c`](#insn-004ec10c)

~~~json
{
  "source": "004ec10c",
  "target": "004ec118",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec110`](#insn-004ec110)

~~~json
{
  "source": "004ec110",
  "target": "Stack[-0x108]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec114`](#insn-004ec114)

~~~json
{
  "source": "004ec114",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ec118`](#insn-004ec118)

~~~json
{
  "source": "004ec118",
  "target": "Stack[-0x130]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec11c`](#insn-004ec11c)

~~~json
{
  "source": "004ec11c",
  "target": "004ec128",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec120`](#insn-004ec120)

~~~json
{
  "source": "004ec120",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec124`](#insn-004ec124)

~~~json
{
  "source": "004ec124",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ec12c`](#insn-004ec12c)

~~~json
{
  "source": "004ec12c",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec134`](#insn-004ec134)

~~~json
{
  "source": "004ec134",
  "target": "004ec294",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec138`](#insn-004ec138)

~~~json
{
  "source": "004ec138",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec13c`](#insn-004ec13c)

~~~json
{
  "source": "004ec13c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec140`](#insn-004ec140)

~~~json
{
  "source": "004ec140",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec144`](#insn-004ec144)

~~~json
{
  "source": "004ec144",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec148`](#insn-004ec148)

~~~json
{
  "source": "004ec148",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec14c`](#insn-004ec14c)

~~~json
{
  "source": "004ec14c",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec15c`](#insn-004ec15c)

~~~json
{
  "source": "004ec15c",
  "target": "00c57fc0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ec168`](#insn-004ec168)

~~~json
{
  "source": "004ec168",
  "target": "002bc686",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002bc686",
  "offset": 0,
  "size": 17,
  "datatype": "string",
  "bytes": "556e737570706f72746564205042452000",
  "capture_start": "002bc686",
  "capture_bytes": 17,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`004ec174`](#insn-004ec174)

~~~json
{
  "source": "004ec174",
  "target": "00c58180",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ec184`](#insn-004ec184)

~~~json
{
  "source": "004ec184",
  "target": "00c58890",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ec18c`](#insn-004ec18c)

~~~json
{
  "source": "004ec18c",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec194`](#insn-004ec194)

~~~json
{
  "source": "004ec194",
  "target": "004ec294",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ec1a0`](#insn-004ec1a0)

~~~json
{
  "source": "004ec1a0",
  "target": "005358a8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ec1a4`](#insn-004ec1a4)

~~~json
{
  "source": "004ec1a4",
  "target": "00c9ae58",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9ae58",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004ec1a4`](#insn-004ec1a4)

~~~json
{
  "source": "004ec1a4",
  "target": "00c66318",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c66318",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004ec1b0`](#insn-004ec1b0)

~~~json
{
  "source": "004ec1b0",
  "target": "00c57fe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ec294`](#insn-004ec294)

~~~json
{
  "source": "004ec294",
  "target": "00c57fb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
