# 00af3cbc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00af3cbc.md)

## 関数情報

~~~json
{
  "address": "00af3cbc",
  "name": "_ZN8firebase4util12JByteToUInt8EP7_JNIEnvP8_jobject",
  "size": 104,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a9927474e8d60337509c161737ac5edaf0a8ec9547d83a7e37988976a0012860",
  "source_text_sha256": "a9927474e8d60337509c161737ac5edaf0a8ec9547d83a7e37988976a0012860"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bde280](../00bde/00bde280.md)

## 疑似コード 1/1 / UTF-8 420 bytes

~~~c

undefined4 _ZN8firebase4util12JByteToUInt8EP7_JNIEnvP8_jobject(long *param_1,undefined8 param_2)

{
  char cVar1;
  undefined4 uVar2;
  
  uVar2 = _ZN7_JNIEnv14CallByteMethodEP8_jobjectP10_jmethodIDz(param_1,param_2,DAT_010a0560);
  cVar1 = (**(code **)(*param_1 + 0x720))(param_1);
  if (cVar1 != '\0') {
    (**(code **)(*param_1 + 0x80))(param_1);
    (**(code **)(*param_1 + 0x88))(param_1);
  }
  return uVar2;
}

~~~
