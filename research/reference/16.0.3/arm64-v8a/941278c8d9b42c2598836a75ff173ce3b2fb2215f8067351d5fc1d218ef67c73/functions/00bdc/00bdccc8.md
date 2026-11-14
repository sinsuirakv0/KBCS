# 00bdccc8

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bdccc8",
  "name": "FUN_00bdccc8",
  "size": 576,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "78bc1b1e3420acd0f447d442f445b485132a6e830b5f4e511758792cf74e095d",
  "source_text_sha256": "78bc1b1e3420acd0f447d442f445b485132a6e830b5f4e511758792cf74e095d"
}
~~~

## 呼び出し元

- [00bdc924](../00bdc/00bdc924.md)
- [00bdcf08](../00bdc/00bdcf08.md)
- [00bdd1e0](../00bdd/00bdd1e0.md)

## 呼び出し先

- [00497b94](../00497/00497b94.md)
- [00589a54](../00589/00589a54.md)
- [00c58f80](../00c58/00c58f80.md)
- [00c5bc40](../00c5b/00c5bc40.md)
- [00c5c050](../00c5c/00c5c050.md)
- [00c5c060](../00c5c/00c5c060.md)
- [00c5c120](../00c5c/00c5c120.md)
- [00c5c3c0](../00c5c/00c5c3c0.md)
- [00c5c4c0](../00c5c/00c5c4c0.md)

## 疑似コード / UTF-8 2540 bytes

~~~c

void FUN_00bdccc8(undefined8 *param_1,byte *param_2)

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
                    (plVar3,DAT_01127be8,DAT_01127c00,uVar4,param_1[0x3f]);
  (**(code **)(*plVar3 + 0xb8))(plVar3,uVar4);
  cVar2 = (**(code **)(*plVar3 + 0x720))(plVar3);
  if (cVar2 == '\0') {
    uVar4 = _ZN8firebase4util19StdVectorToJavaListEP7_JNIEnvRKNSt6__ndk16vectorINS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEENS8_ISA_EEEE
                      (plVar3,param_2 + 0x18);
    cVar2 = (**(code **)(*plVar3 + 0x720))(plVar3);
    if (cVar2 == '\0') {
      uVar6 = FUN_00497b94(plVar3,uVar5,DAT_01127cd8,uVar4);
      (**(code **)(*plVar3 + 0xb8))(plVar3,uVar4);
      cVar2 = (**(code **)(*plVar3 + 0x720))(plVar3);
      pcVar7 = *(code **)(*plVar3 + 0xb8);
      if (cVar2 == '\0') {
        (*pcVar7)(plVar3,uVar6);
        uVar4 = _ZN8firebase4util8hash_map8GetClassEv();
        uVar6 = _ZN8firebase4util8hash_map11GetMethodIdENS1_6MethodE(0);
        local_50 = FUN_00589a54(plVar3,uVar4,uVar6);
        _ZN8firebase4util15StdMapToJavaMapEP7_JNIEnvPP8_jobjectRKNSt6__ndk13mapINS6_12basic_stringIcNS6_11char_traitsIcEENS6_9allocatorIcEEEESD_NS6_4lessISD_EENSB_INS6_4pairIKSD_SD_EEEEEE
                  (plVar3,&local_50,param_2 + 0x30);
        uVar4 = FUN_00497b94(plVar3,uVar5,DAT_01127cd0,local_50);
        (**(code **)(*plVar3 + 0xb8))(plVar3,local_50);
        cVar2 = (**(code **)(*plVar3 + 0x720))(plVar3);
        pcVar7 = *(code **)(*plVar3 + 0xb8);
        if (cVar2 == '\0') {
          (*pcVar7)(plVar3,uVar4);
          uVar4 = FUN_00497b94(plVar3,uVar5,DAT_01127ce0);
          (**(code **)(*plVar3 + 0xb8))(plVar3,uVar5);
          cVar2 = (**(code **)(*plVar3 + 0x720))(plVar3);
          if (cVar2 != '\0') {
            uVar4 = 0;
          }
          goto LAB_00bdce88;
        }
      }
      (*pcVar7)(plVar3,uVar5);
    }
  }
  uVar4 = 0;
LAB_00bdce88:
  if (*(long *)(lVar1 + 0x28) != local_48) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail(uVar4);
  }
  return;
}

~~~
