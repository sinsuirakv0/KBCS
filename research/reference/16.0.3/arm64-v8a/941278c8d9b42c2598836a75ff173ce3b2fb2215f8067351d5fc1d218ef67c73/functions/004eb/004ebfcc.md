# 004ebfcc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

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
  "source_text_sha256": "77a32efd759780517b428b693bd3a5860d049219a74a859557dbca67ae5c9eb6"
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
