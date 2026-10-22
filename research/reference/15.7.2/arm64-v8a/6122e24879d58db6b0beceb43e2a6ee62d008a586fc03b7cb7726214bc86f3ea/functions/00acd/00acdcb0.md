# 00acdcb0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00acdcb0.md)

## 関数情報

~~~json
{
  "address": "00acdcb0",
  "name": "FUN_00acdcb0",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0ab3b1b73b932a58c3976512bc9a7affd39f939d21a4f647452381abca00e210",
  "source_text_sha256": "0ab3b1b73b932a58c3976512bc9a7affd39f939d21a4f647452381abca00e210"
}
~~~
## 呼び出し元

- [00657e7c](../00657/00657e7c.md)

## 呼び出し先

- [00adcbcc](../00adc/00adcbcc.md)
- [00bdb140](../00bdb/00bdb140.md)

## 疑似コード 1/1 / UTF-8 199 bytes

~~~c

void FUN_00acdcb0(undefined8 *param_1)

{
  FUN_00adcbcc();
  *param_1 = &PTR_FUN_00bf7208;
  memset(param_1 + 0x15,0,0x220);
  *(undefined4 *)(param_1 + 0x59) = 0x3f800000;
  return;
}

~~~
