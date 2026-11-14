# 00aaefdc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00aaefdc",
  "name": "FUN_00aaefdc",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "eda7ed1bf5acf89ebd162eb84be0b04df805e1e6b83b4cc8513ed303bc7bee42",
  "source_text_sha256": "eda7ed1bf5acf89ebd162eb84be0b04df805e1e6b83b4cc8513ed303bc7bee42"
}
~~~

## 呼び出し元

- [00796a68](../00796/00796a68.md)

## 呼び出し先

- [00b343b0](../00b34/00b343b0.md)

## 疑似コード / UTF-8 285 bytes

~~~c

void FUN_00aaefdc(undefined8 param_1,undefined8 param_2,undefined8 param_3,undefined8 param_4,
                 undefined8 param_5)

{
                    /* catch() { ... } // from try @ 00aaef38 with catch @ 00aaefe4 */
  FUN_00b343b0(param_2,param_3,param_4,param_5);
  return;
}

~~~
