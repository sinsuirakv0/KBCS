# 00ae1ddc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00ae1ddc",
  "name": "_ZN8firebase9analytics18AddVariantToBundleEP7_JNIEnvP8_jobjectPKcRKNS_7VariantE",
  "size": 816,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "17c19a4016e8347a57fb9e67f5b38d8190f6ce74958efefe13c2716967dedda9",
  "source_text_sha256": "17c19a4016e8347a57fb9e67f5b38d8190f6ce74958efefe13c2716967dedda9"
}
~~~

## 呼び出し元

- [00bde150](../00bde/00bde150.md)

## 呼び出し先

- [00551e14](../00551/00551e14.md)
- [00bddc60](../00bdd/00bddc60.md)
- [00bddc80](../00bdd/00bddc80.md)
- [00bde090](../00bde/00bde090.md)
- [00bde0c0](../00bde/00bde0c0.md)
- [00bde140](../00bde/00bde140.md)
- [00bde160](../00bde/00bde160.md)

## 疑似コード / UTF-8 4040 bytes

~~~c

undefined4
_ZN8firebase9analytics18AddVariantToBundleEP7_JNIEnvP8_jobjectPKcRKNS_7VariantE
          (long *param_1,undefined8 param_2,undefined8 param_3,int *param_4)

{
  undefined8 uVar1;
  undefined8 uVar2;
  undefined8 uVar3;
  undefined1 uVar4;
  byte *pbVar5;
  long lVar6;
  undefined4 uVar7;
  
                    /* try { // try from 00ae1df4 to 00be1dff has its CatchHandler @ 00ae1e14 */
  uVar7 = 0;
                    /* try { // try from 00ae1e00 to 00be1e3f has its CatchHandler @ 00ae1d8c */
                    /* catch() { ... } // from try @ 00ae1df4 with catch @ 00ae1e14 */
                    /* catch() { ... } // from try @ 00ae1dd4 with catch @ 00ae1e28 */
  switch(*param_4) {
  case 0:
    uVar1 = (**(code **)(*param_1 + 0x538))(param_1,param_3);
    uVar2 = _ZN8firebase4util6bundle11GetMethodIdENS1_6MethodE(5);
    uVar4 = 0;
    break;
  case 1:
    _ZNK8firebase7Variant14assert_is_typeENS0_4TypeE(param_4,1);
    uVar1 = *(undefined8 *)(param_4 + 2);
    uVar2 = (**(code **)(*param_1 + 0x538))(param_1,param_3);
    uVar3 = _ZN8firebase4util6bundle11GetMethodIdENS1_6MethodE(5);
    FUN_00551e14(param_1,param_2,uVar3,uVar2,uVar1);
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    (**(code **)(*param_1 + 0xb8))(param_1,uVar2);
    return 1;
  case 2:
    _ZNK8firebase7Variant14assert_is_typeENS0_4TypeE(param_4,2);
    uVar3 = *(undefined8 *)(param_4 + 2);
    uVar1 = (**(code **)(*param_1 + 0x538))(param_1,param_3);
    uVar2 = _ZN8firebase4util6bundle11GetMethodIdENS1_6MethodE(4);
    FUN_00551e14(uVar3,param_1,param_2,uVar2,uVar1);
    goto LAB_00ae1fa0;
  case 3:
    _ZNK8firebase7Variant14assert_is_typeENS0_4TypeE(param_4,3);
    uVar4 = (undefined1)param_4[2];
    uVar1 = (**(code **)(*param_1 + 0x538))(param_1,param_3);
    uVar2 = _ZN8firebase4util6bundle11GetMethodIdENS1_6MethodE(5);
    break;
  case 4:
  case 5:
  case 10:
    _ZNK8firebase7Variant16assert_is_stringEv(param_4);
    if (*param_4 == 5) {
      pbVar5 = *(byte **)(param_4 + 2);
      if ((*pbVar5 & 1) == 0) {
        pbVar5 = pbVar5 + 1;
      }
      else {
        pbVar5 = *(byte **)(pbVar5 + 0x10);
      }
    }
    else {
      pbVar5 = (byte *)(param_4 + 2);
      if (*param_4 == 4) {
        pbVar5 = *(byte **)pbVar5;
      }
    }
    uVar1 = (**(code **)(*param_1 + 0x538))(param_1,param_3);
    uVar2 = (**(code **)(*param_1 + 0x538))(param_1,pbVar5);
    uVar3 = _ZN8firebase4util6bundle11GetMethodIdENS1_6MethodE(6);
    FUN_00551e14(param_1,param_2,uVar3,uVar1,uVar2);
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    (**(code **)(*param_1 + 0xb8))(param_1,uVar2);
    goto LAB_00ae20d8;
  case 6:
    _ZNK8firebase7Variant14assert_is_typeENS0_4TypeE(param_4,6);
    uVar1 = _ZN8firebase9analytics23VectorOfMapsToArrayListEP7_JNIEnvRKNSt6__ndk16vectorINS_7VariantENS3_9allocatorIS5_EEEE
                      (param_1,*(undefined8 *)(param_4 + 2));
    uVar2 = (**(code **)(*param_1 + 0x538))(param_1,param_3);
    uVar3 = 8;
    goto LAB_00ae2020;
  case 7:
    _ZNK8firebase7Variant14assert_is_typeENS0_4TypeE(param_4,7);
    uVar1 = _ZN8firebase9analytics11MapToBundleEP7_JNIEnvRKNSt6__ndk13mapINS_7VariantES5_NS3_4lessIS5_EENS3_9allocatorINS3_4pairIKS5_S5_EEEEEE
                      (param_1,*(undefined8 *)(param_4 + 2));
    uVar2 = (**(code **)(*param_1 + 0x538))(param_1,param_3);
    uVar3 = 7;
LAB_00ae2020:
    uVar3 = _ZN8firebase4util6bundle11GetMethodIdENS1_6MethodE(uVar3);
    FUN_00551e14(param_1,param_2,uVar3,uVar2,uVar1);
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    (**(code **)(*param_1 + 0xb8))(param_1,uVar2);
    lVar6 = *param_1;
    goto LAB_00ae20e4;
  default:
    goto switchD_00ae1e28_caseD_8;
  }
  FUN_00551e14(param_1,param_2,uVar2,uVar1,uVar4);
LAB_00ae1fa0:
  _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
LAB_00ae20d8:
  lVar6 = *param_1;
LAB_00ae20e4:
  (**(code **)(lVar6 + 0xb8))(param_1,uVar1);
  uVar7 = 1;
switchD_00ae1e28_caseD_8:
  return uVar7;
}

~~~
