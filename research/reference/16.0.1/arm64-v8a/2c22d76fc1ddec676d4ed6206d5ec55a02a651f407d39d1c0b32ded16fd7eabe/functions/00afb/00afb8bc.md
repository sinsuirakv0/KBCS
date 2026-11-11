# 00afb8bc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00afb8bc",
  "name": "FUN_00afb8bc",
  "size": 72,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "71397090cad051e4d0f58bdd6b3c9002b1113c308832cce5edb5eadc01a6ff5e",
  "source_text_sha256": "71397090cad051e4d0f58bdd6b3c9002b1113c308832cce5edb5eadc01a6ff5e"
}
~~~

## 呼び出し元

- [00700af8](../00700/00700af8.md)

## 呼び出し先

- [008514f8](../00851/008514f8.md)

## 疑似コード / UTF-8 183 bytes

~~~c

bool FUN_00afb8bc(int param_1,int param_2)

{
  long lVar1;
  
  lVar1 = FUN_008514f8();
  return *(int *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x849b8) != 0;
}

~~~
