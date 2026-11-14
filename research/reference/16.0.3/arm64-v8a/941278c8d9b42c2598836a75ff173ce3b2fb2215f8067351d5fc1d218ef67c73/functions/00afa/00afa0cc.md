# 00afa0cc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00afa0cc",
  "name": "FUN_00afa0cc",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9d5f79d5dfe2217f42e36c06b5cef4592809e79ca5bd1430c0f6064f4e744a0b",
  "source_text_sha256": "9d5f79d5dfe2217f42e36c06b5cef4592809e79ca5bd1430c0f6064f4e744a0b"
}
~~~

## 呼び出し元

- [007106e0](../00710/007106e0.md)

## 呼び出し先

- [008524fc](../00852/008524fc.md)

## 疑似コード / UTF-8 191 bytes

~~~c

undefined4 FUN_00afa0cc(int param_1,int param_2)

{
  long lVar1;
  
  lVar1 = FUN_008524fc();
  return *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x849dc);
}

~~~
