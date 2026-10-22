# 00af3cbc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00af3cbc.md)

## 関数情報

~~~json
{
  "address": "00af3cbc",
  "name": "firebase::util::JByteToUInt8",
  "size": 104,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "edd8a17365de0c466a86085dbf09fa0e9b54abd86df143d4be1ef191325bec67",
  "source_text_sha256": "edd8a17365de0c466a86085dbf09fa0e9b54abd86df143d4be1ef191325bec67"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bde280](../00bde/00bde280.md)

## 疑似コード 1/1 / UTF-8 495 bytes

~~~c

/* firebase::util::JByteToUInt8(_JNIEnv*, _jobject*) */

undefined4 firebase::util::JByteToUInt8(_JNIEnv *param_1,_jobject *param_2)

{
  char cVar1;
  undefined4 uVar2;
  
  uVar2 = _JNIEnv::CallByteMethod((_jobject *)param_1,(_jmethodID *)param_2,DAT_010a0560);
  cVar1 = (**(code **)(*(long *)param_1 + 0x720))(param_1);
  if (cVar1 != '\0') {
    (**(code **)(*(long *)param_1 + 0x80))(param_1);
    (**(code **)(*(long *)param_1 + 0x88))(param_1);
  }
  return uVar2;
}

~~~
