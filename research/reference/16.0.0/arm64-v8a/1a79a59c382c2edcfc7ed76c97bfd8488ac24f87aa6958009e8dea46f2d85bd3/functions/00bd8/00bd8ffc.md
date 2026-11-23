# 00bd8ffc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b69afc`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b69/00b69afc.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/2-3/priority-0070.md#compare-842ffb01ddd84d61c42376e41a896cc6)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 構造資料不足
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bd8ffc",
  "name": "_ZN8firebase4auth17EmailAuthProvider13GetCredentialEPKcS3_",
  "size": 672,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0ab5fc1decb8a368de0f9771e0c562a4486f08a6970384014008d95e8a856b06",
  "source_text_sha256": "0ab5fc1decb8a368de0f9771e0c562a4486f08a6970384014008d95e8a856b06"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57ab0](../00c57/00c57ab0.md)
- [00c57ae0](../00c57/00c57ae0.md)
- [00c57be0](../00c57/00c57be0.md)
- [00c5a7a0](../00c5a/00c5a7a0.md)
- [00c5a8a0](../00c5a/00c5a8a0.md)
- [00c5ab60](../00c5a/00c5ab60.md)
- [00c5ac00](../00c5a/00c5ac00.md)
- [00c5ac80](../00c5a/00c5ac80.md)
- [00c5acb0](../00c5a/00c5acb0.md)
- [00c5ae60](../00c5a/00c5ae60.md)
- [00c5d910](../00c5d/00c5d910.md)
- [00c5d960](../00c5d/00c5d960.md)
- [00c5da00](../00c5d/00c5da00.md)

## 関連文字列（未確認候補）

~~~text
"A password must be provided."
"An email address must be provided."
"Firebase Auth was not initialized, unable to create a Credential. Create an Auth instance first."
"app != nullptr"
"email && password"
"g_methods_cached"
~~~

## 疑似コード / UTF-8 4249 bytes

~~~c

void _ZN8firebase4auth17EmailAuthProvider13GetCredentialEPKcS3_
               (undefined8 *param_1,char *param_2,char *param_3)

{
  ulong uVar1;
  long lVar2;
  void *pvVar3;
  undefined4 uVar4;
  long lVar5;
  long *plVar6;
  undefined8 uVar7;
  undefined8 uVar8;
  long lVar9;
  char *pcVar10;
  size_t sVar11;
  undefined8 local_98;
  undefined4 local_90;
  undefined8 local_88;
  undefined8 uStack_80;
  undefined8 local_78;
  ulong local_70;
  ulong local_68;
  void *local_60;
  long local_58;
  
  lVar2 = tpidr_el0;
  local_58 = *(long *)(lVar2 + 0x28);
                    /* try { // try from 00bd9028 to 00cd9037 has its CatchHandler @ 00bdeb0c */
  if ((param_2 == (char *)0x0) || (param_3 == (char *)0x0)) {
    pcVar10 = "email && password";
  }
  else {
                    /* try { // try from 00bd9038 to 00cd9997 has its CatchHandler @ 00bd6d50 */
    if (DAT_011268f8 != '\0') {
      lVar5 = _ZN8firebase10app_common9GetAnyAppEv();
      if (lVar5 == 0) {
        _ZN8firebase9LogAssertEPKcz("app != nullptr");
      }
      plVar6 = (long *)_ZNK8firebase3App9GetJNIEnvEv(lVar5);
      uVar7 = (**(code **)(*plVar6 + 0x538))(plVar6,param_2);
      uVar8 = (**(code **)(*plVar6 + 0x538))(plVar6,param_3);
      lVar5 = _ZN7_JNIEnv22CallStaticObjectMethodEP7_jclassP10_jmethodIDz
                        (plVar6,DAT_01126668,DAT_01126678,uVar7,uVar8);
      (**(code **)(*plVar6 + 0xb8))(plVar6,uVar7);
      (**(code **)(*plVar6 + 0xb8))(plVar6,uVar8);
      local_68 = 0;
      local_60 = (void *)0x0;
      local_70 = 0;
      if (lVar5 == 0) {
        sVar11 = strlen(param_2);
        if (sVar11 == 0) {
          _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar6);
          _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
                    (&local_70,"An email address must be provided.",0x22);
          uVar4 = 0x25;
          uVar7 = 0;
        }
        else {
          sVar11 = strlen(param_3);
          if (sVar11 == 0) {
            _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar6);
            _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
                      (&local_70,"A password must be provided.",0x1c);
            uVar4 = 0x26;
            uVar7 = 0;
          }
          else {
            uVar4 = _ZN8firebase4auth30CheckAndClearJniAuthExceptionsEP7_JNIEnvPNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEE
                              (plVar6,&local_70);
            uVar7 = 0;
          }
        }
      }
      else {
        lVar9 = _ZN8firebase10app_common9GetAnyAppEv();
        if (lVar9 == 0) {
          _ZN8firebase9LogAssertEPKcz("app != nullptr");
        }
        plVar6 = (long *)_ZNK8firebase3App9GetJNIEnvEv(lVar9);
        uVar7 = (**(code **)(*plVar6 + 0xa8))(plVar6,lVar5);
        (**(code **)(*plVar6 + 0xb8))(plVar6,lVar5);
        uVar4 = 0;
      }
      local_90 = 0;
      local_88 = 0;
      uStack_80 = 0;
      local_78 = 0;
      local_98 = uVar7;
      if (lVar5 == 0) {
        uVar1 = local_70 >> 1 & 0x7f;
        pvVar3 = (void *)((ulong)&local_70 | 1);
        if ((local_70 & 1) != 0) {
          uVar1 = local_68;
          pvVar3 = local_60;
        }
        local_90 = uVar4;
        _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
                  (&local_88,pvVar3,uVar1);
      }
      *param_1 = 0;
      *(undefined4 *)(param_1 + 1) = 0;
      param_1[2] = 0;
      param_1[3] = 0;
      param_1[4] = 0;
      _ZN8firebase4auth10CredentialaSERKS1_(param_1,&local_98);
      _ZN8firebase4auth10CredentialD2Ev(&local_98);
      if ((local_70 & 1) != 0) {
        _ZdlPv(local_60);
      }
      goto LAB_00bd91f0;
    }
    _ZN8firebase8LogErrorEPKcz("g_methods_cached");
    pcVar10 = 
    "Firebase Auth was not initialized, unable to create a Credential. Create an Auth instance first."
    ;
  }
  _ZN8firebase9LogAssertEPKcz(pcVar10);
  *param_1 = 0;
  *(undefined4 *)(param_1 + 1) = 0;
  param_1[3] = 0;
  param_1[4] = 0;
  param_1[2] = 0;
LAB_00bd91f0:
  if (*(long *)(lVar2 + 0x28) != local_58) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return;
}

~~~
