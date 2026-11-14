# 00aef8dc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00aef8dc",
  "name": "FUN_00aef8dc",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "78c7ef7fd52813f1234cad0f3e5b2f4d123936a47d924643e457632b4636a745",
  "source_text_sha256": "78c7ef7fd52813f1234cad0f3e5b2f4d123936a47d924643e457632b4636a745"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 273 bytes

~~~c

void FUN_00aef8dc(long param_1,undefined8 *param_2)

{
  undefined8 uVar1;
  
  uVar1 = *(undefined8 *)(param_1 + 8);
                    /* catch() { ... } // from try @ 00aef3ec with catch @ 00aef8e0 */
  *param_2 = &PTR_FUN_00c8ed78;
  param_2[1] = uVar1;
  return;
}

~~~
