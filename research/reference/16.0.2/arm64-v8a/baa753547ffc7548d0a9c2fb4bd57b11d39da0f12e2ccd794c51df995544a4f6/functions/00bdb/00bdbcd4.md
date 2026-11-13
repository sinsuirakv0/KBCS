# 00bdbcd4

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00bdbcd4",
  "name": "FUN_00bdbcd4",
  "size": 576,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b0775e9671eb2853bfc7280ab4737b8d731194bdf216bbfc3b8a66d034bd32ae",
  "source_text_sha256": "b0775e9671eb2853bfc7280ab4737b8d731194bdf216bbfc3b8a66d034bd32ae"
}
~~~

## 呼び出し元

- [00bdb930](../00bdb/00bdb930.md)
- [00bdbf14](../00bdb/00bdbf14.md)
- [00bdc1ec](../00bdc/00bdc1ec.md)

## 呼び出し先

- [00497874](../00497/00497874.md)
- [00589734](../00589/00589734.md)
- [00c57fb0](../00c57/00c57fb0.md)
- [00c5ac70](../00c5a/00c5ac70.md)
- [00c5b080](../00c5b/00c5b080.md)
- [00c5b090](../00c5b/00c5b090.md)
- [00c5b150](../00c5b/00c5b150.md)
- [00c5b3f0](../00c5b/00c5b3f0.md)
- [00c5b4f0](../00c5b/00c5b4f0.md)

## 疑似コード / UTF-8 2540 bytes

~~~c

void FUN_00bdbcd4(undefined8 *param_1,byte *param_2)

{
  long lVar1;
  char cVar2;
  long *plVar3;
  undefined8 uVar4;
  undefined8 uVar5;
  undefined8 uVar6;
  code *pcVar7;
  byte *pbVar8;
  undefined8 local_50;
  long local_48;
  
  lVar1 = tpidr_el0;
  local_48 = *(long *)(lVar1 + 0x28);
  plVar3 = (long *)_ZNK8firebase3App9GetJNIEnvEv(*param_1);
  pbVar8 = *(byte **)(param_2 + 0x10);
  if ((*param_2 & 1) == 0) {
    pbVar8 = param_2 + 1;
  }
  uVar4 = (**(code **)(*plVar3 + 0x538))(plVar3,pbVar8);
  uVar5 = _ZN7_JNIEnv22CallStaticObjectMethodEP7_jclassP10_jmethodIDz
                    (plVar3,DAT_01126c28,DAT_01126c40,uVar4,param_1[0x3f]);
  (**(code **)(*plVar3 + 0xb8))(plVar3,uVar4);
  cVar2 = (**(code **)(*plVar3 + 0x720))(plVar3);
  if (cVar2 == '\0') {
    uVar4 = _ZN8firebase4util19StdVectorToJavaListEP7_JNIEnvRKNSt6__ndk16vectorINS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEENS8_ISA_EEEE
                      (plVar3,param_2 + 0x18);
    cVar2 = (**(code **)(*plVar3 + 0x720))(plVar3);
    if (cVar2 == '\0') {
      uVar6 = FUN_00497874(plVar3,uVar5,DAT_01126d18,uVar4);
      (**(code **)(*plVar3 + 0xb8))(plVar3,uVar4);
      cVar2 = (**(code **)(*plVar3 + 0x720))(plVar3);
      pcVar7 = *(code **)(*plVar3 + 0xb8);
      if (cVar2 == '\0') {
        (*pcVar7)(plVar3,uVar6);
        uVar4 = _ZN8firebase4util8hash_map8GetClassEv();
        uVar6 = _ZN8firebase4util8hash_map11GetMethodIdENS1_6MethodE(0);
        local_50 = FUN_00589734(plVar3,uVar4,uVar6);
        _ZN8firebase4util15StdMapToJavaMapEP7_JNIEnvPP8_jobjectRKNSt6__ndk13mapINS6_12basic_stringIcNS6_11char_traitsIcEENS6_9allocatorIcEEEESD_NS6_4lessISD_EENSB_INS6_4pairIKSD_SD_EEEEEE
                  (plVar3,&local_50,param_2 + 0x30);
        uVar4 = FUN_00497874(plVar3,uVar5,DAT_01126d10,local_50);
        (**(code **)(*plVar3 + 0xb8))(plVar3,local_50);
        cVar2 = (**(code **)(*plVar3 + 0x720))(plVar3);
        pcVar7 = *(code **)(*plVar3 + 0xb8);
        if (cVar2 == '\0') {
          (*pcVar7)(plVar3,uVar4);
          uVar4 = FUN_00497874(plVar3,uVar5,DAT_01126d20);
          (**(code **)(*plVar3 + 0xb8))(plVar3,uVar5);
          cVar2 = (**(code **)(*plVar3 + 0x720))(plVar3);
          if (cVar2 != '\0') {
            uVar4 = 0;
          }
          goto LAB_00bdbe94;
        }
      }
      (*pcVar7)(plVar3,uVar5);
    }
  }
  uVar4 = 0;
LAB_00bdbe94:
  if (*(long *)(lVar1 + 0x28) != local_48) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail(uVar4);
  }
  return;
}

~~~
