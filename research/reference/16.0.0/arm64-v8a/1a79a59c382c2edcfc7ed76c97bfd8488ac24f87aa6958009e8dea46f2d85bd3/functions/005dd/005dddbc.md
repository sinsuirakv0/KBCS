# 005dddbc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "005dddbc",
  "name": "FUN_005dddbc",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "368c67aa82ce90cd98969b6676ce19a0c9310110da88783d51b7eb54e87ea278",
  "source_text_sha256": "368c67aa82ce90cd98969b6676ce19a0c9310110da88783d51b7eb54e87ea278"
}
~~~

## 呼び出し元

- [005eba30](../005eb/005eba30.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 392 bytes

~~~c

void FUN_005dddbc(undefined1 *param_1)

{
  *param_1 = 0;
  param_1[0x24] = 0;
  *(undefined8 *)(param_1 + 0x28) = 0;
  param_1[0x30] = 0;
  *(undefined8 *)(param_1 + 0xc) = 0;
  *(undefined8 *)(param_1 + 4) = 0;
  *(undefined8 *)(param_1 + 0x1c) = 0;
  *(undefined8 *)(param_1 + 0x14) = 0;
  *(undefined8 *)(param_1 + 0x34) = 0;
  *(undefined4 *)(param_1 + 0x3c) = 0xffffffff;
  return;
}

~~~
