# 00accf7c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00accf7c",
  "name": "FUN_00accf7c",
  "size": 8,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "196a267353192bdd1fd3bab06aff2148f4a1f494041be0254017af5930e4db38",
  "source_text_sha256": "196a267353192bdd1fd3bab06aff2148f4a1f494041be0254017af5930e4db38"
}
~~~

## 呼び出し元

- [007322cc](../00732/007322cc.md)
- [009366b0](../00936/009366b0.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 177 bytes

~~~c

void FUN_00accf7c(long param_1,undefined4 param_2,undefined4 param_3)

{
  *(undefined4 *)(param_1 + 0x10) = param_2;
  *(undefined4 *)(param_1 + 0x14) = param_3;
  return;
}

~~~
