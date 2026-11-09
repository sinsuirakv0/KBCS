# 00bdadac

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bdadac",
  "name": "_ZN8firebase4auth20JniAuthPhoneListener29nativeOnVerificationCompletedEP7_JNIEnvP8_jobjectlS5_",
  "size": 232,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5fbbdfca050cb9da1b4c93d144e5db05abcb2fefb35f1d9793fd4e1613913cfd",
  "source_text_sha256": "5fbbdfca050cb9da1b4c93d144e5db05abcb2fefb35f1d9793fd4e1613913cfd"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57ab0](../00c57/00c57ab0.md)
- [00c57ae0](../00c57/00c57ae0.md)
- [00c5ac00](../00c5a/00c5ac00.md)
- [00c5ac80](../00c5a/00c5ac80.md)
- [00c5ae60](../00c5a/00c5ae60.md)
- [00c5d730](../00c5d/00c5d730.md)
- [00c5da00](../00c5d/00c5da00.md)

## 関連文字列（未確認候補）

~~~text
"app != nullptr"
~~~

## 疑似コード / UTF-8 1121 bytes

~~~c

void _ZN8firebase4auth20JniAuthPhoneListener29nativeOnVerificationCompletedEP7_JNIEnvP8_jobjectlS5_
               (undefined8 param_1,undefined8 param_2,long *param_3,long param_4)

{
  long lVar1;
  long lVar2;
  long *plVar3;
  undefined8 uVar4;
  undefined1 auStack_88 [40];
  byte local_60;
  void *local_50;
  long local_48;
  
  lVar1 = tpidr_el0;
  local_48 = *(long *)(lVar1 + 0x28);
  if (param_4 == 0) {
    uVar4 = 0;
  }
  else {
    lVar2 = _ZN8firebase10app_common9GetAnyAppEv();
    if (lVar2 == 0) {
      _ZN8firebase9LogAssertEPKcz("app != nullptr");
    }
    plVar3 = (long *)_ZNK8firebase3App9GetJNIEnvEv(lVar2);
    uVar4 = (**(code **)(*plVar3 + 0xa8))(plVar3,param_4);
    (**(code **)(*plVar3 + 0xb8))(plVar3,param_4);
  }
  _ZN8firebase4auth19PhoneAuthCredentialC2EPv(auStack_88,uVar4);
  (**(code **)(*param_3 + 0x10))(param_3,auStack_88);
  if ((local_60 & 1) != 0) {
    _ZdlPv(local_50);
  }
  _ZN8firebase4auth10CredentialD2Ev(auStack_88);
  if (*(long *)(lVar1 + 0x28) == local_48) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
