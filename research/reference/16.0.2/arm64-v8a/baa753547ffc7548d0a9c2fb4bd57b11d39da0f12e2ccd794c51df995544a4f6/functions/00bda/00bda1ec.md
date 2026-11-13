# 00bda1ec

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00bda1ec",
  "name": "_ZN8firebase4auth13OAuthProvider13GetCredentialEPKcS3_S3_S3_",
  "size": 704,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "740792cfe53ff55b5c0ce96ecc2696358b579d5d4eec68cf418854cc1f642394",
  "source_text_sha256": "740792cfe53ff55b5c0ce96ecc2696358b579d5d4eec68cf418854cc1f642394"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00497874](../00497/00497874.md)
- [00c5ac70](../00c5a/00c5ac70.md)
- [00c5ad70](../00c5a/00c5ad70.md)
- [00c5b030](../00c5b/00c5b030.md)
- [00c5b0d0](../00c5b/00c5b0d0.md)
- [00c5b150](../00c5b/00c5b150.md)
- [00c5b330](../00c5b/00c5b330.md)

## 関連文字列（未確認候補）

~~~text
"Firebase Auth was not initialized, unable to create a Credential. Create an Auth instance first."
"app != nullptr"
"g_methods_cached"
"provider_id && id_token && raw_nonce"
~~~

## 疑似コード / UTF-8 3098 bytes

~~~c

void _ZN8firebase4auth13OAuthProvider13GetCredentialEPKcS3_S3_S3_
               (undefined8 *param_1,long param_2,long param_3,long param_4,long param_5)

{
  long lVar1;
  long *plVar2;
  undefined8 uVar3;
  undefined8 uVar4;
  undefined8 uVar5;
  ulong uVar6;
  undefined8 uVar7;
  undefined8 uVar8;
  char *pcVar9;
  long lVar10;
  
  if (((param_2 == 0) || (param_3 == 0)) || (param_4 == 0)) {
    pcVar9 = "provider_id && id_token && raw_nonce";
LAB_00bda394:
    _ZN8firebase9LogAssertEPKcz(pcVar9);
  }
  else {
    if (DAT_01126df8 == '\0') {
      _ZN8firebase8LogErrorEPKcz("g_methods_cached");
      pcVar9 = 
      "Firebase Auth was not initialized, unable to create a Credential. Create an Auth instance first."
      ;
      goto LAB_00bda394;
    }
    lVar1 = _ZN8firebase10app_common9GetAnyAppEv();
    if (lVar1 == 0) {
      _ZN8firebase9LogAssertEPKcz("app != nullptr");
    }
    plVar2 = (long *)_ZNK8firebase3App9GetJNIEnvEv(lVar1);
    uVar3 = (**(code **)(*plVar2 + 0x538))(plVar2,param_2);
    uVar4 = (**(code **)(*plVar2 + 0x538))(plVar2,param_3);
    uVar5 = (**(code **)(*plVar2 + 0x538))(plVar2,param_4);
    lVar1 = _ZN7_JNIEnv22CallStaticObjectMethodEP7_jclassP10_jmethodIDz
                      (plVar2,DAT_01126c28,DAT_01126c48,uVar3);
    uVar6 = _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar2);
    if ((uVar6 & 1) == 0) {
      uVar7 = FUN_00497874(plVar2,lVar1,DAT_01126d50,uVar4,uVar5);
      uVar6 = _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar2);
      if (((uVar6 & 1) == 0) && ((**(code **)(*plVar2 + 0xb8))(plVar2,uVar7), param_5 != 0)) {
        uVar7 = (**(code **)(*plVar2 + 0x538))(plVar2,param_5);
        uVar8 = FUN_00497874(plVar2,lVar1,DAT_01126d40,uVar7);
        (**(code **)(*plVar2 + 0xb8))(plVar2,uVar7);
        uVar6 = _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar2);
        if ((uVar6 & 1) != 0) {
          (**(code **)(*plVar2 + 0xb8))(plVar2,lVar1);
          goto LAB_00bda418;
        }
        (**(code **)(*plVar2 + 0xb8))(plVar2,uVar8);
      }
      if (lVar1 == 0) goto LAB_00bda418;
      lVar10 = FUN_00497874(plVar2,lVar1,DAT_01126d58);
      uVar6 = _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar2);
      (**(code **)(*plVar2 + 0xb8))(plVar2,lVar1);
      lVar1 = 0;
      if ((uVar6 & 1) == 0) {
        lVar1 = lVar10;
      }
    }
    else {
LAB_00bda418:
      lVar1 = 0;
    }
    (**(code **)(*plVar2 + 0xb8))(plVar2,uVar3);
    (**(code **)(*plVar2 + 0xb8))(plVar2,uVar5);
    (**(code **)(*plVar2 + 0xb8))(plVar2,uVar4);
    if (lVar1 != 0) {
      lVar10 = _ZN8firebase10app_common9GetAnyAppEv();
      if (lVar10 == 0) {
        _ZN8firebase9LogAssertEPKcz("app != nullptr");
      }
      plVar2 = (long *)_ZNK8firebase3App9GetJNIEnvEv(lVar10);
      uVar3 = (**(code **)(*plVar2 + 0xa8))(plVar2,lVar1);
      (**(code **)(*plVar2 + 0xb8))(plVar2,lVar1);
      goto LAB_00bda39c;
    }
  }
  uVar3 = 0;
LAB_00bda39c:
  *param_1 = uVar3;
  *(undefined4 *)(param_1 + 1) = 0;
  param_1[3] = 0;
  param_1[4] = 0;
  param_1[2] = 0;
  return;
}

~~~
