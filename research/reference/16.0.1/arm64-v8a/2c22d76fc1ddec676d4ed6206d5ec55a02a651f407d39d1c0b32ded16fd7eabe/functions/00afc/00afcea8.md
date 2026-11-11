# 00afcea8

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00afcea8",
  "name": "FUN_00afcea8",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "86451fa9b93333cb08e67915d42ceb7cb2ed3b26e45790133a09826465a742cb",
  "source_text_sha256": "86451fa9b93333cb08e67915d42ceb7cb2ed3b26e45790133a09826465a742cb"
}
~~~

## 呼び出し元

- [00700af8](../00700/00700af8.md)
- [00715500](../00715/00715500.md)
- [00716d90](../00716/00716d90.md)
- [00a4f3b4](../00a4f/00a4f3b4.md)

## 呼び出し先

- [008514f8](../00851/008514f8.md)

## 疑似コード / UTF-8 217 bytes

~~~c

void FUN_00afcea8(int param_1,int param_2,undefined4 param_3)

{
  long lVar1;
  
  lVar1 = FUN_008514f8();
  *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84ca8) = param_3;
  return;
}

~~~
