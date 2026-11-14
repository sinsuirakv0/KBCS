# 00bce4fc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bce4fc",
  "name": "_ZN8firebase4auth14SetEmulatorJniEPNS0_8AuthDataEPKcj",
  "size": 128,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "69521913cded4f61ea8f83b9047d34fe060c354701a9b3085c7a54517a18a5a7",
  "source_text_sha256": "69521913cded4f61ea8f83b9047d34fe060c354701a9b3085c7a54517a18a5a7"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0057504c](../00575/0057504c.md)
- [00c5c000](../00c5c/00c5c000.md)
- [00c5c120](../00c5c/00c5c120.md)

## 疑似コード / UTF-8 487 bytes

~~~c

void _ZN8firebase4auth14SetEmulatorJniEPNS0_8AuthDataEPKcj
               (undefined8 *param_1,undefined8 param_2,undefined4 param_3)

{
  long *plVar1;
  undefined8 uVar2;
  
  plVar1 = (long *)_ZNK8firebase3App9GetJNIEnvEv(*param_1);
  uVar2 = (**(code **)(*plVar1 + 0x538))(plVar1,param_2);
  FUN_0057504c(plVar1,param_1[0x3f],DAT_01127848,uVar2,param_3);
  (**(code **)(*plVar1 + 0xb8))(plVar1,uVar2);
  _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar1);
  return;
}

~~~
