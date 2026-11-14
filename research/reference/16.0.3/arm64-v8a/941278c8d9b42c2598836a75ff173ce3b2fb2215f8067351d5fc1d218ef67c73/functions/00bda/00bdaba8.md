# 00bdaba8

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bdaba8",
  "name": "_ZN8firebase4auth18GoogleAuthProvider13GetCredentialEPKcS3_",
  "size": 420,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ab677bfb8fd4c021a9a31464a6a6c42b0da3d31d147c982974860801ded85dd9",
  "source_text_sha256": "ab677bfb8fd4c021a9a31464a6a6c42b0da3d31d147c982974860801ded85dd9"
}
~~~

## 呼び出し元

- [00c5ba70](../00c5b/00c5ba70.md)

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
~~~

## 疑似コード / UTF-8 2555 bytes

~~~c

void _ZN8firebase4auth18GoogleAuthProvider13GetCredentialEPKcS3_
               (undefined8 *param_1,char *param_2,char *param_3)

{
  long lVar1;
  long lVar2;
  long *plVar3;
  long lVar4;
  long lVar5;
  ulong uVar6;
  undefined8 uVar7;
  
  if (DAT_01127db8 == '\0') {
    _ZN8firebase8LogErrorEPKcz("g_methods_cached");
                    /* try { // try from 00bdac54 to 00cdb4e3 has its CatchHandler @ 00bd7fb0 */
    _ZN8firebase9LogAssertEPKcz
              (
              "Firebase Auth was not initialized, unable to create a Credential. Create an Auth instance first."
              );
  }
  else {
    lVar2 = _ZN8firebase10app_common9GetAnyAppEv();
    if (lVar2 == 0) {
      _ZN8firebase9LogAssertEPKcz("app != nullptr");
    }
    plVar3 = (long *)_ZNK8firebase3App9GetJNIEnvEv(lVar2);
                    /* try { // try from 00bdabf8 to 00cdac03 has its CatchHandler @ 00be0074 */
    lVar2 = 0;
    if (param_2 == (char *)0x0) {
LAB_00bdac1c:
      if (param_3 == (char *)0x0) goto LAB_00bdac68;
LAB_00bdac20:
      if (*param_3 == '\0') goto LAB_00bdac68;
                    /* try { // try from 00bdac2c to 00cdac37 has its CatchHandler @ 00be004c */
                    /* try { // try from 00bdac38 to 00cdac53 has its CatchHandler @ 00be0034 */
      lVar4 = (**(code **)(*plVar3 + 0x538))(plVar3,param_3);
    }
    else {
      if (*param_2 != '\0') {
        lVar2 = (**(code **)(*plVar3 + 0x538))(plVar3,param_2);
        goto LAB_00bdac1c;
      }
      lVar2 = 0;
      if (param_3 != (char *)0x0) goto LAB_00bdac20;
LAB_00bdac68:
      lVar4 = 0;
    }
    lVar5 = _ZN7_JNIEnv22CallStaticObjectMethodEP7_jclassP10_jmethodIDz
                      (plVar3,DAT_01127b88,DAT_01127b98,lVar2,lVar4);
    uVar6 = _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar3);
    lVar1 = 0;
    if ((uVar6 & 1) == 0) {
      lVar1 = lVar5;
    }
    if (lVar2 != 0) {
      (**(code **)(*plVar3 + 0xb8))(plVar3,lVar2);
    }
    if (lVar4 != 0) {
      (**(code **)(*plVar3 + 0xb8))(plVar3,lVar4);
    }
    if (lVar1 != 0) {
      lVar2 = _ZN8firebase10app_common9GetAnyAppEv();
      if (lVar2 == 0) {
        _ZN8firebase9LogAssertEPKcz("app != nullptr");
      }
      plVar3 = (long *)_ZNK8firebase3App9GetJNIEnvEv(lVar2);
      uVar7 = (**(code **)(*plVar3 + 0xa8))(plVar3,lVar1);
      (**(code **)(*plVar3 + 0xb8))(plVar3,lVar1);
      goto LAB_00bdad28;
    }
  }
  uVar7 = 0;
LAB_00bdad28:
  *param_1 = uVar7;
  *(undefined4 *)(param_1 + 1) = 0;
  param_1[3] = 0;
  param_1[4] = 0;
  param_1[2] = 0;
  return;
}

~~~
