# 00adbf5c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00adbf5c.md)

## 関数情報

~~~json
{
  "address": "00adbf5c",
  "name": "FUN_00adbf5c",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5ea683ccbc5fac2ea1b3f5118801d065db4222eea07e1974e6451cd7d30460e2",
  "source_text_sha256": "5ea683ccbc5fac2ea1b3f5118801d065db4222eea07e1974e6451cd7d30460e2"
}
~~~
## 呼び出し元

- [0080dd1c](../0080d/0080dd1c.md)
- [00814828](../00814/00814828.md)

## 呼び出し先

- [005c3468](../005c3/005c3468.md)

## 疑似コード 1/1 / UTF-8 142 bytes

~~~c

void FUN_00adbf5c(undefined4 *param_1)

{
  *param_1 = 0;
  FUN_005c3468();
  *param_1 = 0;
  FUN_005c3468(param_1);
  return;
}

~~~
