# 007febdc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "007febdc",
  "name": "FUN_007febdc",
  "size": 36,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "38b8b7e0c0c87f220b263642c0945b5514ab3a8c17a92e2a287b8cf26a1e980d",
  "source_text_sha256": "38b8b7e0c0c87f220b263642c0945b5514ab3a8c17a92e2a287b8cf26a1e980d"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c58f30](../00c58/00c58f30.md)

## 疑似コード / UTF-8 222 bytes

~~~c

void FUN_007febdc(void)

{
  undefined8 *puVar1;
  
                    /* catch() { ... } // from try @ 007feb50 with catch @ 007febdc */
  puVar1 = (undefined8 *)_Znwm(0x10);
  *puVar1 = &PTR_FUN_00c7ebb0;
  return;
}

~~~
