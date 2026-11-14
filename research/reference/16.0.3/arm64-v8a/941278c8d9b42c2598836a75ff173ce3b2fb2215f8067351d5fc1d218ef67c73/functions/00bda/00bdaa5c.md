# 00bdaa5c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bdaa5c",
  "name": "_ZN8firebase4auth18GitHubAuthProvider13GetCredentialEPKc",
  "size": 332,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ce07d2f71c4bdeeb67d039230842751e709e8f1af69a5a7485b7b28292099e16",
  "source_text_sha256": "ce07d2f71c4bdeeb67d039230842751e709e8f1af69a5a7485b7b28292099e16"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5bc40](../00c5b/00c5bc40.md)
- [00c5bd40](../00c5b/00c5bd40.md)
- [00c5c000](../00c5c/00c5c000.md)
- [00c5c0a0](../00c5c/00c5c0a0.md)
- [00c5c120](../00c5c/00c5c120.md)
- [00c5c300](../00c5c/00c5c300.md)

## 関連文字列（未確認候補）

~~~text
"Firebase Auth was not initialized, unable to create a Credential. Create an Auth instance first."
"app != nullptr"
"g_methods_cached"
"token"
~~~

## 疑似コード / UTF-8 1619 bytes

~~~c

void _ZN8firebase4auth18GitHubAuthProvider13GetCredentialEPKc(undefined8 *param_1,long param_2)

{
  long lVar1;
  long *plVar2;
  undefined8 uVar3;
  ulong uVar4;
  long lVar5;
  char *pcVar6;
  
  if (param_2 == 0) {
    pcVar6 = "token";
  }
  else {
    if (DAT_01127db8 != '\0') {
      lVar1 = _ZN8firebase10app_common9GetAnyAppEv();
      if (lVar1 == 0) {
        _ZN8firebase9LogAssertEPKcz("app != nullptr");
      }
      plVar2 = (long *)_ZNK8firebase3App9GetJNIEnvEv(lVar1);
      uVar3 = (**(code **)(*plVar2 + 0x538))(plVar2,param_2);
      lVar1 = _ZN7_JNIEnv22CallStaticObjectMethodEP7_jclassP10_jmethodIDz
                        (plVar2,DAT_01127b68,DAT_01127b78,uVar3);
      uVar4 = _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar2);
      (**(code **)(*plVar2 + 0xb8))(plVar2,uVar3);
      uVar3 = 0;
      if (((uVar4 & 1) == 0) && (lVar1 != 0)) {
        lVar5 = _ZN8firebase10app_common9GetAnyAppEv();
        if (lVar5 == 0) {
          _ZN8firebase9LogAssertEPKcz("app != nullptr");
        }
        plVar2 = (long *)_ZNK8firebase3App9GetJNIEnvEv(lVar5);
        uVar3 = (**(code **)(*plVar2 + 0xa8))(plVar2,lVar1);
        (**(code **)(*plVar2 + 0xb8))(plVar2,lVar1);
      }
      goto LAB_00bdab84;
    }
    _ZN8firebase8LogErrorEPKcz("g_methods_cached");
    pcVar6 = 
    "Firebase Auth was not initialized, unable to create a Credential. Create an Auth instance first."
    ;
  }
  _ZN8firebase9LogAssertEPKcz(pcVar6);
  uVar3 = 0;
LAB_00bdab84:
  *param_1 = uVar3;
  *(undefined4 *)(param_1 + 1) = 0;
  param_1[3] = 0;
  param_1[4] = 0;
  param_1[2] = 0;
  return;
}

~~~
