# 008ebecc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "008ebecc",
  "name": "FUN_008ebecc",
  "size": 52,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "10dc578637a4f9751957f875a4faa70f70301ff036aa1c87d9ce0d3b6b284765",
  "source_text_sha256": "10dc578637a4f9751957f875a4faa70f70301ff036aa1c87d9ce0d3b6b284765"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c58f30](../00c58/00c58f30.md)

## 疑似コード / UTF-8 224 bytes

~~~c

void FUN_008ebecc(long param_1)

{
  undefined8 *puVar1;
  undefined8 uVar2;
  
  puVar1 = (undefined8 *)_Znwm(0x10);
  uVar2 = *(undefined8 *)(param_1 + 8);
  *puVar1 = &PTR_FUN_00c86870;
  puVar1[1] = uVar2;
  return;
}

~~~
