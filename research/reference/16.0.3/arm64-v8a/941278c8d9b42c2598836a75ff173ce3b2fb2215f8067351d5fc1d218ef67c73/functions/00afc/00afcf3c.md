# 00afcf3c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00afcf3c",
  "name": "FUN_00afcf3c",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ced6632025f7feca9ebd56d71350f2c778ab19b475a2fa6e153450fa2638f1c4",
  "source_text_sha256": "ced6632025f7feca9ebd56d71350f2c778ab19b475a2fa6e153450fa2638f1c4"
}
~~~

## 呼び出し元

- [007082e8](../00708/007082e8.md)
- [0070ee64](../0070e/0070ee64.md)
- [00711df8](../00711/00711df8.md)

## 呼び出し先

- [008524fc](../00852/008524fc.md)

## 疑似コード / UTF-8 191 bytes

~~~c

undefined4 FUN_00afcf3c(int param_1,int param_2)

{
  long lVar1;
  
  lVar1 = FUN_008524fc();
  return *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x849f8);
}

~~~
