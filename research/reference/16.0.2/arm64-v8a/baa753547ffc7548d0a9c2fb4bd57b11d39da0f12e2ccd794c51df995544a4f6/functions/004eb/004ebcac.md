# 004ebcac

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

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
  "source_text_sha256": "d81e8010e1dc46bc9c213e1a3cabbfe8aa4fa5bf88495ea791d245eaf4bdccdc"
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
