# 00bfa2dc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00bfa2dc",
  "name": "_ZNSt6__ndk111timed_mutexC1Ev",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "445bd422b4b830d75de7004f9557d56d098627bdc0d0d3719e9790047ef8ecc1",
  "source_text_sha256": "445bd422b4b830d75de7004f9557d56d098627bdc0d0d3719e9790047ef8ecc1"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 341 bytes

~~~c

void _ZNSt6__ndk111timed_mutexC1Ev(undefined8 *param_1)

{
  *(undefined8 *)((long)param_1 + 0x51) = 0;
  *(undefined8 *)((long)param_1 + 0x49) = 0;
  param_1[3] = 0;
  param_1[2] = 0;
  param_1[5] = 0;
  param_1[4] = 0;
  param_1[7] = 0;
  param_1[6] = 0;
  param_1[9] = 0;
  param_1[8] = 0;
  param_1[1] = 0;
  *param_1 = 0;
  return;
}

~~~
