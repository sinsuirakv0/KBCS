# 00aaebc4

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

## 関数情報

~~~json
{
  "address": "00aaebc4",
  "name": "FUN_00aaebc4",
  "size": 612,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d06a282ec5f6dff23c900debd4dc0c121265550fc7a65db6e22a224b617bd9bf",
  "source_text_sha256": "d06a282ec5f6dff23c900debd4dc0c121265550fc7a65db6e22a224b617bd9bf"
}
~~~

## 呼び出し元

- [0076dd00](../0076d/0076dd00.md)

## 呼び出し先

- [00418fe0](../00418/00418fe0.md)
- [0042eb00](../0042e/0042eb00.md)
- [00436518](../00436/00436518.md)
- [005742c4](../00574/005742c4.md)
- [0057462c](../00574/0057462c.md)
- [00aaea7c](../00aae/00aaea7c.md)
- [00bdb040](../00bdb/00bdb040.md)
- [00bdb060](../00bdb/00bdb060.md)
- [00bdb090](../00bdb/00bdb090.md)
- [00bdb150](../00bdb/00bdb150.md)
- [00bdb160](../00bdb/00bdb160.md)
- [00bdb170](../00bdb/00bdb170.md)
- [00bdb360](../00bdb/00bdb360.md)
- [00bdb390](../00bdb/00bdb390.md)
- [00bdb3a0](../00bdb/00bdb3a0.md)

## 関連文字列（未確認候補）

~~~text
"showPopup"
~~~

## 疑似コード / UTF-8 4417 bytes

~~~c

/* WARNING: Type propagation algorithm not settling */

void FUN_00aaebc4(undefined8 *param_1)

{
  byte *pbVar1;
  byte *pbVar2;
  long lVar3;
  undefined *puVar4;
  long *plVar5;
  long *plVar6;
  long lVar7;
  long lVar8;
  byte local_190 [16];
  void *local_180;
  byte local_178;
  char local_177 [8];
  undefined2 local_16f;
  void *local_168;
  long *local_160 [9];
  ulong local_118;
  undefined8 uStack_110;
  void *local_108;
  undefined8 uStack_100;
  undefined4 local_f8;
  undefined *local_f0 [3];
  undefined8 uStack_d8;
  undefined4 auStack_d0 [4];
  undefined8 local_c0;
  long local_58;
  
  lVar3 = tpidr_el0;
  local_58 = *(long *)(lVar3 + 0x28);
  plVar5 = (long *)_Znwm(0x28);
  pbVar1 = (byte *)*param_1;
  pbVar2 = (byte *)param_1[1];
  *(undefined4 *)(plVar5 + 1) = 6;
  *plVar5 = (long)&PTR_FUN_00bf06b8;
  plVar5[3] = 0;
  plVar5[4] = 0;
  plVar5[2] = 0;
  plVar6 = (long *)
           PTR__ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c1adc8
  ;
  puVar4 = PTR__ZTVNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c1ae98
  ;
  for (; PTR__ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c1adc8 =
              (undefined *)plVar6,
      PTR__ZTVNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c1ae98 =
           puVar4, pbVar1 != pbVar2; pbVar1 = pbVar1 + 0x18) {
    plVar6 = (long *)_Znwm(0x28);
    *(undefined4 *)(plVar6 + 1) = 5;
    *plVar6 = (long)&PTR_FUN_00be67a0;
    if ((*pbVar1 & 1) == 0) {
      lVar8 = *(long *)(pbVar1 + 8);
      lVar7 = *(long *)pbVar1;
      plVar6[4] = *(long *)(pbVar1 + 0x10);
      plVar6[3] = lVar8;
      plVar6[2] = lVar7;
    }
    else {
      FUN_00418fe0(plVar6 + 2,*(undefined8 *)(pbVar1 + 0x10),*(undefined8 *)(pbVar1 + 8));
    }
    local_160[0] = plVar6;
    FUN_0057462c(plVar5,local_160);
    plVar6 = local_160[0];
    local_160[0] = (long *)0x0;
    if (plVar6 != (long *)0x0) {
      (**(code **)(*plVar6 + 8))();
    }
    plVar6 = (long *)
             PTR__ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c1adc8
    ;
    puVar4 = 
    PTR__ZTVNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c1ae98;
  }
  local_c0 = 0;
  local_160[0] = (long *)plVar6[1];
  local_f0[0] = puVar4 + 0x40;
  *(long *)((long)local_160 + local_160[0][-3]) = plVar6[2];
  lVar7 = local_160[0][-3];
  _ZNSt6__ndk18ios_base4initEPv((long)local_160 + lVar7,local_160 + 1);
  local_160[0] = (long *)(puVar4 + 0x18);
  *(undefined8 *)((long)&uStack_d8 + lVar7) = 0;
  *(undefined4 *)((long)auStack_d0 + lVar7) = 0xffffffff;
  local_f0[0] = puVar4 + 0x40;
  _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEEC1Ev(local_160 + 1);
  puVar4 = PTR__ZTVNSt6__ndk115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c1add0;
  local_160[1] = (long *)(
                         PTR__ZTVNSt6__ndk115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c1add0
                         + 0x10);
  uStack_110 = 0;
  local_118 = 0;
  uStack_100 = 0;
  local_108 = (void *)0x0;
  local_f8 = 0x10;
  FUN_0042eb00(local_160,plVar5);
  local_178 = 0x12;
  local_16f = 0x70;
  local_177[0] = s_showPopup_00297307[0];
  local_177[1] = s_showPopup_00297307[1];
  local_177[2] = s_showPopup_00297307[2];
  local_177[3] = s_showPopup_00297307[3];
  local_177[4] = s_showPopup_00297307[4];
  local_177[5] = s_showPopup_00297307[5];
  local_177[6] = s_showPopup_00297307[6];
  local_177[7] = s_showPopup_00297307[7];
  _ZNKSt6__ndk115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE3strEv
            (local_190,local_160 + 1);
  FUN_00aaea7c(&local_178,local_190,1);
  if ((local_190[0] & 1) != 0) {
    _ZdlPv(local_180);
  }
  if ((local_178 & 1) != 0) {
    _ZdlPv(local_168);
  }
  local_160[0] = (long *)*plVar6;
  *(long *)((long)local_160 + local_160[0][-3]) = plVar6[3];
  local_160[1] = (long *)(puVar4 + 0x10);
  if ((local_118 & 1) != 0) {
    _ZdlPv(local_108);
  }
  _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEED2Ev(local_160 + 1);
  _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEED2Ev(local_160,plVar6 + 1);
  _ZNSt6__ndk19basic_iosIcNS_11char_traitsIcEEED1Ev(local_f0);
  (**(code **)(*plVar5 + 8))(plVar5);
  if (*(long *)(lVar3 + 0x28) == local_58) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
