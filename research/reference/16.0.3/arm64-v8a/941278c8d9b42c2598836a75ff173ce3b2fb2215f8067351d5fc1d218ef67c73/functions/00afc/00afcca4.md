# 00afcca4

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00afcca4",
  "name": "FUN_00afcca4",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "216e9266c51c3f35409a53509723da6db47ac9e656d8d2da56fbf8b27d0e6d5d",
  "source_text_sha256": "216e9266c51c3f35409a53509723da6db47ac9e656d8d2da56fbf8b27d0e6d5d"
}
~~~

## 呼び出し元

- [00700f00](../00700/00700f00.md)
- [007106e0](../00710/007106e0.md)
- [00a50418](../00a50/00a50418.md)

## 呼び出し先

- [008524fc](../00852/008524fc.md)

## 疑似コード / UTF-8 217 bytes

~~~c

void FUN_00afcca4(int param_1,int param_2,undefined4 param_3)

{
  long lVar1;
  
  lVar1 = FUN_008524fc();
  *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x849c0) = param_3;
  return;
}

~~~
