# 00bdad8c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bdad8c.md)

## 関数情報

~~~json
{
  "address": "00bdad8c",
  "name": "FUN_00bdad8c",
  "size": 8,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "03d5afbc8ef8668b4f9951d43b2c7fe3982a3248419a987a9efd0ecb0899ea74",
  "source_text_sha256": "03d5afbc8ef8668b4f9951d43b2c7fe3982a3248419a987a9efd0ecb0899ea74"
}
~~~
## 呼び出し元

- [009613bc](../00961/009613bc.md)

## 呼び出し先

- [00963004](../00963/00963004.md)

## 疑似コード 1/1 / UTF-8 155 bytes

~~~c

void FUN_00bdad8c(void)

{
                    /* catch() { ... } // from try @ 00bdad04 with catch @ 00bdad8c */
  FUN_00963004();
  return;
}

~~~
