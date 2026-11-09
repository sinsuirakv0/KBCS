# 00afb7ac

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00afb7ac",
  "name": "FUN_00afb7ac",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "18b38f7d67c3902b6e3225a013132a567e5c3df87fde79ae7aa1393b672b6c89",
  "source_text_sha256": "18b38f7d67c3902b6e3225a013132a567e5c3df87fde79ae7aa1393b672b6c89"
}
~~~

## 呼び出し元

- [005f2d28](../005f2/005f2d28.md)
- [00707ea0](../00707/00707ea0.md)
- [007154c0](../00715/007154c0.md)
- [00716d50](../00716/00716d50.md)

## 呼び出し先

- [008514b8](../00851/008514b8.md)

## 疑似コード / UTF-8 191 bytes

~~~c

undefined4 FUN_00afb7ac(int param_1,int param_2)

{
  long lVar1;
  
  lVar1 = FUN_008514b8();
  return *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x849c0);
}

~~~
