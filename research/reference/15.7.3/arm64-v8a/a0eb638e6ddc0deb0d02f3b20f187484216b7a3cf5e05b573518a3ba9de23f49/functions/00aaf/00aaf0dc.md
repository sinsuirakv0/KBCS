# 00aaf0dc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00aaf0dc",
  "name": "FUN_00aaf0dc",
  "size": 56,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9836494056f4f4bf9f4c8e86d73b2e95f9e5b73eb0b3c2837d7191f4cbd5a509",
  "source_text_sha256": "9836494056f4f4bf9f4c8e86d73b2e95f9e5b73eb0b3c2837d7191f4cbd5a509"
}
~~~

## 呼び出し元

- [009c5338](../009c5/009c5338.md)

## 呼び出し先

- [0045df50](../0045d/0045df50.md)

## 疑似コード / UTF-8 145 bytes

~~~c

void FUN_00aaf0dc(undefined4 *param_1,undefined8 param_2)

{
  FUN_0045df50(param_2,*param_1);
  FUN_0045df50(param_2,param_1[1]);
  return;
}

~~~
