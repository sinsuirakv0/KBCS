# 00b7eedc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00b7eedc",
  "name": "FUN_00b7eedc",
  "size": 1140,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "636e944a18f25919806d1c68c60201da43a1c5aa6411b169b5b7777c8a3c664c",
  "source_text_sha256": "636e944a18f25919806d1c68c60201da43a1c5aa6411b169b5b7777c8a3c664c"
}
~~~

## 呼び出し元

- [00b764d0](../00b76/00b764d0.md)
- [00b79e94](../00b79/00b79e94.md)
- [00b7c308](../00b7c/00b7c308.md)
- [00b7d08c](../00b7d/00b7d08c.md)

## 呼び出し先

- [00b99610](../00b99/00b99610.md)
- [00c58f30](../00c58/00c58f30.md)
- [00c58f50](../00c58/00c58f50.md)
- [00c58f80](../00c58/00c58f80.md)
- [00c59020](../00c59/00c59020.md)
- [00c59080](../00c59/00c59080.md)
- [00c590a0](../00c59/00c590a0.md)
- [00c59150](../00c59/00c59150.md)
- [00c5a070](../00c5a/00c5a070.md)
- [00c5c1e0](../00c5c/00c5c1e0.md)
- [00c5d810](../00c5d/00c5d810.md)
- [00c5e1f0](../00c5e/00c5e1f0.md)

## 関連文字列（未確認候補）

~~~text
", constant does not fit "
"error: "
"invalid number: \""
~~~

## 疑似コード / UTF-8 7614 bytes

~~~c

/* WARNING: Type propagation algorithm not settling */

void FUN_00b7eedc(undefined2 *param_1,byte *param_2,undefined8 param_3,undefined4 *param_4)

{
  long lVar1;
  longlong lVar2;
  size_t sVar3;
  ulong *puVar4;
  int __base;
  __locale_t __loc;
  undefined4 uVar5;
  long lVar6;
  uint uVar7;
  void *pvVar8;
  ulong uVar9;
  byte local_120 [8];
  ulong local_118;
  void *local_110;
  ulong local_108;
  size_t local_100;
  void *local_f8;
  ulong local_f0;
  ulong uStack_e8;
  void *local_e0;
  ulong local_d0;
  size_t sStack_c8;
  void *local_c0;
  ulong local_b0;
  ulong uStack_a8;
  void *local_a0;
  ulong local_90;
  ulong uStack_88;
  void *local_80;
  byte *local_70 [2];
  void *local_60;
  long local_58;
  
  lVar1 = tpidr_el0;
  local_58 = *(long *)(lVar1 + 0x28);
  uVar7 = (uint)*param_2;
  if (*param_2 != 0) {
    lVar6 = 1;
    do {
                    /* try { // try from 00b7ef28 to 00c7f037 has its CatchHandler @ 00b7ef28
                       catch() { ... } // from try @ 00b7ef28 with catch @ 00b7ef28
                       catch() { ... } // from try @ 00b7f078 with catch @ 00b7ef28 */
      if (uVar7 - 0x30 < 10) {
        if ((uVar7 == 0x30) && ((param_2[lVar6] & 0xdf) == 0x58)) {
          __loc = *(__locale_t *)PTR__ZN11flatbuffers13ClassicLocale9instance_E_00c9c8d0;
          __base = 0x10;
          goto LAB_00b7ef84;
        }
        break;
      }
      uVar7 = (uint)param_2[lVar6];
      lVar6 = lVar6 + 1;
    } while (uVar7 != 0);
  }
  __loc = *(__locale_t *)PTR__ZN11flatbuffers13ClassicLocale9instance_E_00c9c8d0;
  __base = 10;
LAB_00b7ef84:
  local_70[0] = param_2;
  lVar2 = strtoll_l((char *)param_2,(char **)local_70,__base,__loc);
  if ((local_70[0] == param_2) || (*local_70[0] != 0)) {
    *param_4 = 0;
    sStack_c8 = 0;
    local_c0 = (void *)0x0;
    local_d0 = 0;
    sVar3 = strlen((char *)param_2);
    if (0xffffffffffffffef < sVar3) goto LAB_00b7f34c;
    if (sVar3 < 0x17) {
      pvVar8 = (void *)((ulong)&local_d0 | 1);
      local_d0 = CONCAT71(local_d0._1_7_,(char)((int)sVar3 << 1));
      if (sVar3 != 0) goto LAB_00b7f05c;
    }
    else {
      uVar9 = sVar3 + 0x10 & 0xfffffffffffffff0;
      pvVar8 = (void *)_Znwm(uVar9);
      local_d0 = uVar9 | 1;
      sStack_c8 = sVar3;
      local_c0 = pvVar8;
LAB_00b7f05c:
                    /* try { // try from 00b7f05c to 00c7f077 has its CatchHandler @ 00b7f0e8 */
      memcpy(pvVar8,param_2,sVar3);
    }
                    /* try { // try from 00b7f078 to 00c7f17b has its CatchHandler @ 00b7ef28 */
    *(undefined1 *)((long)pvVar8 + sVar3) = 0;
    puVar4 = (ulong *)_ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6insertEmPKcm
                                (&local_d0,0,"invalid number: \"",0x11);
    uStack_a8 = puVar4[1];
    local_b0 = *puVar4;
    local_a0 = (void *)puVar4[2];
    *puVar4 = 0;
    puVar4[1] = 0;
    puVar4[2] = 0;
    puVar4 = (ulong *)_ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKcm
                                (&local_b0,&DAT_002b5f9c,1);
    uStack_88 = puVar4[1];
    local_90 = *puVar4;
    local_80 = (void *)puVar4[2];
    *puVar4 = 0;
    puVar4[1] = 0;
    puVar4[2] = 0;
    _ZNSt6__ndk1plIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EEPKS6_RKS9_
              (local_70,"error: ",&local_90);
                    /* catch() { ... } // from try @ 00b7f05c with catch @ 00b7f0e8 */
    _ZN11flatbuffers6Parser7MessageERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
              (param_3,local_70);
    if (((ulong)local_70[0] & 1) != 0) {
      _ZdlPv(local_60);
    }
    *param_1 = 1;
    if ((local_90 & 1) != 0) {
      _ZdlPv(local_80);
    }
    pvVar8 = local_c0;
    uVar9 = local_d0;
    if ((local_b0 & 1) != 0) {
      _ZdlPv(local_a0);
      pvVar8 = local_c0;
      uVar9 = local_d0;
    }
  }
  else {
    uVar5 = 0x7fffffff;
    if (lVar2 < 0x80000000) {
      if (-0x80000001 < lVar2) {
        *param_4 = (int)lVar2;
        *param_1 = 0;
        goto LAB_00b7f31c;
      }
      uVar5 = 0x80000000;
    }
    *param_4 = uVar5;
    local_100 = 0;
    local_f8 = (void *)0x0;
    local_108 = 0;
    sVar3 = strlen((char *)param_2);
    if (0xffffffffffffffef < sVar3) {
LAB_00b7f34c:
                    /* WARNING: Subroutine does not return */
      abort();
    }
    if (sVar3 < 0x17) {
      pvVar8 = (void *)((ulong)&local_108 | 1);
      local_108 = CONCAT71(local_108._1_7_,(char)((int)sVar3 << 1));
      if (sVar3 != 0) goto LAB_00b7f168;
    }
    else {
      uVar9 = sVar3 + 0x10 & 0xfffffffffffffff0;
      pvVar8 = (void *)_Znwm(uVar9);
      local_108 = uVar9 | 1;
      local_100 = sVar3;
      local_f8 = pvVar8;
LAB_00b7f168:
                    /* catch() { ... } // from try @ 00b7f038 with catch @ 00b7f16c */
      memcpy(pvVar8,param_2,sVar3);
    }
    *(undefined1 *)((long)pvVar8 + sVar3) = 0;
    puVar4 = (ulong *)_ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6insertEmPKcm
                                (&local_108,0,"invalid number: \"",0x11);
    uStack_e8 = puVar4[1];
    local_f0 = *puVar4;
    local_e0 = (void *)puVar4[2];
    *puVar4 = 0;
    puVar4[1] = 0;
    puVar4[2] = 0;
    puVar4 = (ulong *)_ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKcm
                                (&local_f0,&DAT_002b5f9c,1);
    sStack_c8 = puVar4[1];
    local_d0 = *puVar4;
    local_c0 = (void *)puVar4[2];
    *puVar4 = 0;
    puVar4[1] = 0;
    puVar4[2] = 0;
    puVar4 = (ulong *)_ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKcm
                                (&local_d0,", constant does not fit ",0x18);
    local_a0 = (void *)puVar4[2];
    uStack_a8 = puVar4[1];
    local_b0 = *puVar4;
    *puVar4 = 0;
    puVar4[1] = 0;
    puVar4[2] = 0;
    FUN_00b99610(local_120);
    uVar9 = (ulong)(local_120[0] >> 1);
    pvVar8 = (void *)((ulong)local_120 | 1);
    if ((local_120[0] & 1) != 0) {
      uVar9 = local_118;
      pvVar8 = local_110;
    }
    puVar4 = (ulong *)_ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKcm
                                (&local_b0,pvVar8,uVar9);
    uStack_88 = puVar4[1];
    local_90 = *puVar4;
    local_80 = (void *)puVar4[2];
    *puVar4 = 0;
    puVar4[1] = 0;
    puVar4[2] = 0;
    _ZNSt6__ndk1plIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EEPKS6_RKS9_
              (local_70,"error: ",&local_90);
    _ZN11flatbuffers6Parser7MessageERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
              (param_3,local_70);
    if (((ulong)local_70[0] & 1) != 0) {
                    /* try { // try from 00b7f278 to 00c7f387 has its CatchHandler @ 00b7f278
                       catch() { ... } // from try @ 00b7f278 with catch @ 00b7f278
                       catch() { ... } // from try @ 00b7f3c8 with catch @ 00b7f278 */
      _ZdlPv(local_60);
    }
    *param_1 = 1;
    if ((local_90 & 1) != 0) {
      _ZdlPv(local_80);
    }
    if ((local_120[0] & 1) != 0) {
      _ZdlPv(local_110);
    }
    if ((local_b0 & 1) != 0) {
      _ZdlPv(local_a0);
    }
    if ((local_d0 & 1) != 0) {
      _ZdlPv(local_c0);
    }
    pvVar8 = local_f8;
    uVar9 = local_108;
    if ((local_f0 & 1) != 0) {
      _ZdlPv(local_e0);
      pvVar8 = local_f8;
      uVar9 = local_108;
    }
  }
  if ((uVar9 & 1) != 0) {
    _ZdlPv(pvVar8);
  }
LAB_00b7f31c:
  if (*(long *)(lVar1 + 0x28) != local_58) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return;
}

~~~
