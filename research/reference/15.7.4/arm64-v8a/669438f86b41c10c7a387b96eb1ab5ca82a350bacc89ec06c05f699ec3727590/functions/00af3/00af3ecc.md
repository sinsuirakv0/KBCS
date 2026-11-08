# 00af3ecc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

## 関数情報

~~~json
{
  "address": "00af3ecc",
  "name": "_ZN8firebase4util11JCharToCharEP7_JNIEnvP8_jobject",
  "size": 104,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b215485ae769385424ccccbc15c4071daefc7e644b691d091b6852d239e6f92a",
  "source_text_sha256": "b215485ae769385424ccccbc15c4071daefc7e644b691d091b6852d239e6f92a"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bde390](../00bde/00bde390.md)

## 疑似コード / UTF-8 419 bytes

~~~c

undefined4 _ZN8firebase4util11JCharToCharEP7_JNIEnvP8_jobject(long *param_1,undefined8 param_2)

{
  char cVar1;
  undefined4 uVar2;
  
  uVar2 = _ZN7_JNIEnv14CallCharMethodEP8_jobjectP10_jmethodIDz(param_1,param_2,DAT_010a0688);
  cVar1 = (**(code **)(*param_1 + 0x720))(param_1);
  if (cVar1 != '\0') {
    (**(code **)(*param_1 + 0x80))(param_1);
    (**(code **)(*param_1 + 0x88))(param_1);
  }
  return uVar2;
}

~~~
