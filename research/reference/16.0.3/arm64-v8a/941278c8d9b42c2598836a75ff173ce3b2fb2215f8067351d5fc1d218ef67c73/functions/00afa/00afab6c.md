# 00afab6c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00afab6c",
  "name": "FUN_00afab6c",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b8fe535bf9e1cd37ebed89dbd3c40fe1c8a192a55937da8d7e0f609ebe1c6de7",
  "source_text_sha256": "b8fe535bf9e1cd37ebed89dbd3c40fe1c8a192a55937da8d7e0f609ebe1c6de7"
}
~~~

## 呼び出し元

- [0071412c](../00714/0071412c.md)

## 呼び出し先

- [008524fc](../00852/008524fc.md)

## 疑似コード / UTF-8 191 bytes

~~~c

undefined4 FUN_00afab6c(int param_1,int param_2)

{
  long lVar1;
  
  lVar1 = FUN_008524fc();
  return *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x849a8);
}

~~~
