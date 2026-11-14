# 00afcdd0

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00afcdd0",
  "name": "FUN_00afcdd0",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f734448c81657e26fd555bde7bfd45ee647d601d28c76d7cb8dcd9de8c939758",
  "source_text_sha256": "f734448c81657e26fd555bde7bfd45ee647d601d28c76d7cb8dcd9de8c939758"
}
~~~

## 呼び出し元

- [00700f00](../00700/00700f00.md)

## 呼び出し先

- [008524fc](../00852/008524fc.md)

## 疑似コード / UTF-8 191 bytes

~~~c

undefined4 FUN_00afcdd0(int param_1,int param_2)

{
  long lVar1;
  
  lVar1 = FUN_008524fc();
  return *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84c3c);
}

~~~
