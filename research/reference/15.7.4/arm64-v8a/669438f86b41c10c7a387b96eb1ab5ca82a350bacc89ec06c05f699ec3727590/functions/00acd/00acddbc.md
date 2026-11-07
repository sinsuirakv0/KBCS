# 00acddbc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-previous -->
**別版の対応** [v15.7.2 `00acdcb0`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acd/00acdcb0.md)
<!-- /kbcs-version-previous -->

## 関数情報

~~~json
{
  "address": "00acddbc",
  "name": "FUN_00acddbc",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "140bcdbb7aa2293e32c2413214e4851318ac3d5917545375975af957326ff683",
  "source_text_sha256": "140bcdbb7aa2293e32c2413214e4851318ac3d5917545375975af957326ff683"
}
~~~

## 呼び出し元

- [00657e7c](../00657/00657e7c.md)

## 呼び出し先

- [00adccd8](../00adc/00adccd8.md)
- [00bdb240](../00bdb/00bdb240.md)

## 疑似コード / UTF-8 188 bytes

~~~c

void FUN_00acddbc(undefined8 *param_1)

{
  FUN_00adccd8();
  *param_1 = &PTR_FUN_00bf7308;
  memset(param_1 + 0x15,0,0x220);
  *(undefined4 *)(param_1 + 0x59) = 0x3f800000;
  return;
}

~~~
