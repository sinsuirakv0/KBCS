# 00bfabb4

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00bfabb4",
  "name": "_ZNSt6__ndk115__thread_structC1Ev",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f61aa855640c1f0ce494933542efe4238457915152f0ef5ee4edceb53acc669b",
  "source_text_sha256": "f61aa855640c1f0ce494933542efe4238457915152f0ef5ee4edceb53acc669b"
}
~~~

## 呼び出し元

- [00c58100](../00c58/00c58100.md)

## 呼び出し先

- [00c57e90](../00c57/00c57e90.md)

## 疑似コード / UTF-8 261 bytes

~~~c

void _ZNSt6__ndk115__thread_structC1Ev(undefined8 *param_1)

{
  undefined8 *puVar1;
  
  puVar1 = (undefined8 *)_Znwm(0x30);
  *param_1 = puVar1;
  puVar1[1] = 0;
  *puVar1 = 0;
  puVar1[3] = 0;
  puVar1[2] = 0;
  puVar1[5] = 0;
  puVar1[4] = 0;
  return;
}

~~~
