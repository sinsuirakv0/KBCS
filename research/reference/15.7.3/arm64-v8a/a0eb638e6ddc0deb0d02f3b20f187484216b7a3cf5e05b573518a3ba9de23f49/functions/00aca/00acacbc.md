# 00acacbc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00acacbc",
  "name": "FUN_00acacbc",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7df875ac0c017c2eac0f257838918237f1cb04afba71e5c707c02f93b6a1d1bd",
  "source_text_sha256": "7df875ac0c017c2eac0f257838918237f1cb04afba71e5c707c02f93b6a1d1bd"
}
~~~

## 呼び出し元

- [00abf52c](../00abf/00abf52c.md)

## 呼び出し先

- [00418c38](../00418/00418c38.md)

## 関連文字列（未確認候補）

~~~text
"vector"
~~~

## 疑似コード / UTF-8 119 bytes

~~~c

void FUN_00acacbc(void)

{
                    /* WARNING: Subroutine does not return */
  FUN_00418c38("vector");
}

~~~
