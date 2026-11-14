# 00abb7fc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00abb7fc",
  "name": "FUN_00abb7fc",
  "size": 56,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8ea8e871dc3e5831ac335b6601ee2c3449122d98b40c5a9c17a1a87dfbbee140",
  "source_text_sha256": "8ea8e871dc3e5831ac335b6601ee2c3449122d98b40c5a9c17a1a87dfbbee140"
}
~~~

## 呼び出し元

- [00a2c310](../00a2c/00a2c310.md)

## 呼び出し先

- [00481188](../00481/00481188.md)

## 疑似コード / UTF-8 145 bytes

~~~c

void FUN_00abb7fc(undefined4 *param_1,undefined8 param_2)

{
  FUN_00481188(param_2,*param_1);
  FUN_00481188(param_2,param_1[8]);
  return;
}

~~~
