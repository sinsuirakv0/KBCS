# 00bbabdc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00bbabdc",
  "name": "_ZSt14set_unexpectedPFvvE",
  "size": 52,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2528d91edbbb2871e2d91662c615e20378ae582b14e3fa1dc9fc7031f3acc696",
  "source_text_sha256": "2528d91edbbb2871e2d91662c615e20378ae582b14e3fa1dc9fc7031f3acc696"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bd6d90](../00bd6/00bd6d90.md)

## 疑似コード / UTF-8 314 bytes

~~~c

void _ZSt14set_unexpectedPFvvE(code *param_1)

{
  code *pcVar1;
  
  pcVar1 = FUN_00bbabbc;
  if (param_1 != (code *)0x0) {
    pcVar1 = param_1;
  }
  FUN_00bd6d90(pcVar1,PTR___cxa_unexpected_handler_00c1bfa8);
                    /* catch() { ... } // from try @ 00bb3784 with catch @ 00bbac04 */
  return;
}

~~~
