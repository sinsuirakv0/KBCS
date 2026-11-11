# 00b6adbc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00b6adbc",
  "name": "_ZN8firebase10AppOptions28PopulateRequiredWithDefaultsEP7_JNIEnvP8_jobject",
  "size": 572,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "64c8523f169b6ea991e31901ef4e9cce3c2d5766440658720d5a2353ee9d7640",
  "source_text_sha256": "64c8523f169b6ea991e31901ef4e9cce3c2d5766440658720d5a2353ee9d7640"
}
~~~

## 呼び出し元

- [00c5b930](../00c5b/00c5b930.md)

## 呼び出し先

- [00879c88](../00879/00879c88.md)
- [00c57ee0](../00c57/00c57ee0.md)
- [00c5aca0](../00c5a/00c5aca0.md)
- [00c5b0b0](../00c5b/00c5b0b0.md)
- [00c5bec0](../00c5b/00c5bec0.md)

## 関連文字列（未確認候補）

~~~text
"App ID, API key, and Project ID must be specified in App options."
"Failed to load default options when attempting to populate missing fields"
~~~

## 疑似コード / UTF-8 5541 bytes

~~~c

void _ZN8firebase10AppOptions28PopulateRequiredWithDefaultsEP7_JNIEnvP8_jobject(undefined1 *param_1)

{
  ulong uVar1;
  byte bVar2;
  long lVar3;
  long lVar4;
  undefined8 uVar5;
  byte *pbVar6;
  undefined8 local_110;
  undefined8 uStack_108;
  undefined8 local_100;
  undefined8 uStack_f8;
  ulong local_f0;
  long lStack_e8;
  undefined8 local_e0;
  ulong uStack_d8;
  long lStack_d0;
  undefined8 uStack_c8;
  undefined8 local_c0;
  undefined8 uStack_b8;
  undefined8 uStack_b0;
  undefined8 uStack_a8;
  undefined8 local_a0;
  undefined8 uStack_98;
  undefined8 uStack_90;
  undefined8 uStack_88;
  undefined8 local_80;
  undefined8 uStack_78;
  undefined8 uStack_70;
  undefined8 uStack_68;
  undefined8 local_60;
  undefined8 uStack_58;
  undefined8 local_50;
  ulong local_48;
  long local_40;
  long local_38;
  
                    /* try { // try from 00b6add0 to 00c6add7 has its CatchHandler @ 00b6ae48 */
  lVar3 = tpidr_el0;
  local_38 = *(long *)(lVar3 + 0x28);
  pbVar6 = param_1 + 0x30;
  bVar2 = *pbVar6;
  if ((bVar2 & 1) == 0) {
    if (bVar2 >> 1 == 0) goto LAB_00b6ae70;
LAB_00b6adf4:
    if ((param_1[0x18] & 1) != 0) {
                    /* catch() { ... } // from try @ 00b6ad40 with catch @ 00b6ae50 */
      if (*(long *)(param_1 + 0x20) != 0) goto LAB_00b6ae04;
      goto LAB_00b6ae70;
    }
    if ((byte)param_1[0x18] >> 1 == 0) goto LAB_00b6ae70;
LAB_00b6ae04:
    if ((param_1[0xc0] & 1) == 0) {
      if ((byte)param_1[0xc0] >> 1 == 0) goto LAB_00b6ae70;
    }
    else if (*(long *)(param_1 + 200) == 0) goto LAB_00b6ae70;
    if ((bVar2 & 1) != 0) goto LAB_00b6afa4;
LAB_00b6ae18:
    if (bVar2 >> 1 != 0) {
LAB_00b6ae20:
      if ((param_1[0x18] & 1) == 0) {
        if ((byte)param_1[0x18] >> 1 != 0) {
LAB_00b6ae30:
          if ((param_1[0xc0] & 1) == 0) {
            if ((byte)param_1[0xc0] >> 1 != 0) {
LAB_00b6afb8:
              uVar5 = 1;
              goto LAB_00b6afd0;
            }
          }
          else if (*(long *)(param_1 + 200) != 0) goto LAB_00b6afb8;
        }
      }
      else {
                    /* catch() { ... } // from try @ 00b6ad08 with catch @ 00b6ae5c
                       catch() { ... } // from try @ 00b6ae40 with catch @ 00b6ae5c */
        if (*(long *)(param_1 + 0x20) != 0) goto LAB_00b6ae30;
      }
    }
  }
  else {
                    /* catch() { ... } // from try @ 00b6add0 with catch @ 00b6ae48
                       try { // try from 00b6ae48 to 00c6ae8f has its CatchHandler @ 00b6ac9c */
    if (*(long *)(param_1 + 0x38) != 0) goto LAB_00b6adf4;
LAB_00b6ae70:
    local_40 = 0;
    uStack_58 = 0;
    local_60 = 0;
    local_48 = 0;
    local_50 = 0;
    uStack_78 = 0;
    local_80 = 0;
    uStack_68 = 0;
    uStack_70 = 0;
    uStack_98 = 0;
    local_a0 = 0;
    uStack_88 = 0;
    uStack_90 = 0;
    uStack_b8 = 0;
    local_c0 = 0;
    uStack_a8 = 0;
    uStack_b0 = 0;
    uStack_d8 = 0;
    local_e0 = 0;
    uStack_c8 = 0;
    lStack_d0 = 0;
    uStack_f8 = 0;
    local_100 = 0;
    lStack_e8 = 0;
    local_f0 = 0;
    uStack_108 = 0;
    local_110 = 0;
    lVar4 = _ZN8firebase10AppOptions11LoadDefaultEPS0_P7_JNIEnvP8_jobject(&local_110);
    if (lVar4 == 0) {
      _ZN8firebase8LogErrorEPKcz
                ("Failed to load default options when attempting to populate missing fields");
    }
    else {
      if ((*pbVar6 & 1) == 0) {
        if (*pbVar6 >> 1 == 0) {
LAB_00b6aecc:
          if (&local_110 != (undefined8 *)param_1) {
            uVar1 = uStack_d8;
            lVar4 = lStack_d0;
            if ((local_e0 & 1) == 0) {
              uVar1 = local_e0 >> 1 & 0x7f;
              lVar4 = (long)&local_e0 + 1;
            }
            _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
                      (pbVar6,lVar4,uVar1);
          }
        }
      }
      else if (*(long *)(param_1 + 0x38) == 0) goto LAB_00b6aecc;
      bVar2 = param_1[0x18];
      if ((bVar2 & 1) == 0) {
        if (bVar2 >> 1 == 0) {
LAB_00b6af1c:
          if (&local_110 != (undefined8 *)param_1) {
            uVar1 = local_f0;
            lVar4 = lStack_e8;
            if ((uStack_f8 & 1) == 0) {
              uVar1 = uStack_f8 >> 1 & 0x7f;
              lVar4 = (long)&uStack_f8 + 1;
            }
            _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
                      (param_1 + 0x18,lVar4,uVar1);
          }
        }
      }
      else if (*(long *)(param_1 + 0x20) == 0) goto LAB_00b6af1c;
      bVar2 = param_1[0xc0];
      if ((bVar2 & 1) == 0) {
        if (bVar2 >> 1 == 0) {
LAB_00b6af68:
          if (&local_110 != (undefined8 *)param_1) {
            uVar1 = local_48;
            lVar4 = local_40;
            if ((local_50 & 1) == 0) {
              uVar1 = local_50 >> 1 & 0x7f;
              lVar4 = (long)&local_50 + 1;
            }
            _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
                      (param_1 + 0xc0,lVar4,uVar1);
          }
        }
      }
      else if (*(long *)(param_1 + 200) == 0) goto LAB_00b6af68;
    }
    FUN_00879c88(&local_110);
    bVar2 = *pbVar6;
    if ((bVar2 & 1) == 0) goto LAB_00b6ae18;
LAB_00b6afa4:
    if (*(long *)(param_1 + 0x38) != 0) goto LAB_00b6ae20;
  }
  _ZN8firebase8LogErrorEPKcz("App ID, API key, and Project ID must be specified in App options.");
  uVar5 = 0;
LAB_00b6afd0:
  if (*(long *)(lVar3 + 0x28) == local_38) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail(uVar5);
}

~~~
