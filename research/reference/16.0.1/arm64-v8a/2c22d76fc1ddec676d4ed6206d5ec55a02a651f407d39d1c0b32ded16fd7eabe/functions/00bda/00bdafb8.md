# 00bdafb8

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00bdafb8",
  "name": "_ZN8firebase4auth17PhoneAuthProvider13GetCredentialEPKcS3_",
  "size": 380,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ff09e9dc10e55673ab4e84ab23ad0be64e7804f82d52baf166339cad6aafe459",
  "source_text_sha256": "ff09e9dc10e55673ab4e84ab23ad0be64e7804f82d52baf166339cad6aafe459"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5aba0](../00c5a/00c5aba0.md)
- [00c5aca0](../00c5a/00c5aca0.md)
- [00c5af60](../00c5a/00c5af60.md)
- [00c5b000](../00c5b/00c5b000.md)
- [00c5b080](../00c5b/00c5b080.md)
- [00c5b260](../00c5b/00c5b260.md)
- [00c5db30](../00c5d/00c5db30.md)
- [00c5db40](../00c5d/00c5db40.md)

## 関連文字列（未確認候補）

~~~text
"Firebase Auth was not initialized, unable to create a Credential. Create an Auth instance first."
"app != nullptr"
"g_methods_cached"
"verification_id && verification_code"
~~~

## 疑似コード / UTF-8 1711 bytes

~~~c

void _ZN8firebase4auth17PhoneAuthProvider13GetCredentialEPKcS3_
               (undefined8 param_1,undefined8 *param_2,long param_3,long param_4)

{
  long *plVar1;
  undefined8 uVar2;
  undefined8 uVar3;
  long lVar4;
  ulong uVar5;
  long lVar6;
  char *pcVar7;
  
  if ((param_3 == 0) || (param_4 == 0)) {
    pcVar7 = "verification_id && verification_code";
  }
  else {
    if (DAT_01126cf8 != '\0') {
      plVar1 = (long *)_ZNK8firebase3App9GetJNIEnvEv(**(undefined8 **)*param_2);
      uVar2 = (**(code **)(*plVar1 + 0x538))(plVar1,param_3);
      uVar3 = (**(code **)(*plVar1 + 0x538))(plVar1,param_4);
      lVar4 = _ZN7_JNIEnv22CallStaticObjectMethodEP7_jclassP10_jmethodIDz
                        (plVar1,DAT_01126bd0,DAT_01126be8,uVar2,uVar3);
      uVar5 = _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar1);
      (**(code **)(*plVar1 + 0xb8))(plVar1,uVar2);
      (**(code **)(*plVar1 + 0xb8))(plVar1,uVar3);
      uVar2 = 0;
      if (((uVar5 & 1) == 0) && (lVar4 != 0)) {
        lVar6 = _ZN8firebase10app_common9GetAnyAppEv();
        if (lVar6 == 0) {
          _ZN8firebase9LogAssertEPKcz("app != nullptr");
        }
        plVar1 = (long *)_ZNK8firebase3App9GetJNIEnvEv(lVar6);
        uVar2 = (**(code **)(*plVar1 + 0xa8))(plVar1,lVar4);
        (**(code **)(*plVar1 + 0xb8))(plVar1,lVar4);
      }
      _ZN8firebase4auth19PhoneAuthCredentialC2EPv(param_1,uVar2);
      return;
    }
    _ZN8firebase8LogErrorEPKcz("g_methods_cached");
    pcVar7 = 
    "Firebase Auth was not initialized, unable to create a Credential. Create an Auth instance first."
    ;
  }
  _ZN8firebase9LogAssertEPKcz(pcVar7);
  _ZN8firebase4auth19PhoneAuthCredentialC1Ev(param_1);
  return;
}

~~~
