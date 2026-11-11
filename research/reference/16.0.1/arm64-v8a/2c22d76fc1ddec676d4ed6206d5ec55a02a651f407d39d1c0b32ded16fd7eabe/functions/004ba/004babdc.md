# 004babdc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "004babdc",
  "name": "_ZN5Botan6BigIntC1Em",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4a3843c37d2054e7e4b5a5594349ca285909d1c3c07092c844ab9e9eedf49b7c",
  "source_text_sha256": "4a3843c37d2054e7e4b5a5594349ca285909d1c3c07092c844ab9e9eedf49b7c"
}
~~~

## 呼び出し元

- [00c58920](../00c58/00c58920.md)

## 呼び出し先

- [00540920](../00540/00540920.md)

## 疑似コード / UTF-8 253 bytes

~~~c

void _ZN5Botan6BigIntC1Em(undefined8 *param_1,long param_2)

{
  *param_1 = 0;
  param_1[1] = 0;
  param_1[2] = 0;
  *(undefined4 *)(param_1 + 3) = 1;
  if (param_2 != 0) {
    FUN_00540920(param_1,8);
    *(long *)*param_1 = param_2;
  }
  return;
}

~~~
