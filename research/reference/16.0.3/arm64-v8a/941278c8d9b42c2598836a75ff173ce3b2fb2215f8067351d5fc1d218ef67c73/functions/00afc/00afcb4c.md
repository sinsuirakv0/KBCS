# 00afcb4c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00afcb4c",
  "name": "FUN_00afcb4c",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8e6e6588674b5bed52c990808a6f3c3030ed3e8bc9294b8b123b56958d92eb52",
  "source_text_sha256": "8e6e6588674b5bed52c990808a6f3c3030ed3e8bc9294b8b123b56958d92eb52"
}
~~~

## 呼び出し元

- [007082e8](../00708/007082e8.md)

## 呼び出し先

- [008524fc](../00852/008524fc.md)

## 疑似コード / UTF-8 191 bytes

~~~c

undefined4 FUN_00afcb4c(int param_1,int param_2)

{
  long lVar1;
  
  lVar1 = FUN_008524fc();
  return *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x849d0);
}

~~~
