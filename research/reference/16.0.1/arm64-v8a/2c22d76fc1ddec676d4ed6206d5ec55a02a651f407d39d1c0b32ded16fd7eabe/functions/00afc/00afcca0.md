# 00afcca0

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00afcca0",
  "name": "FUN_00afcca0",
  "size": 84,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7404130cd79ee8132bec8e8ac4dcfeb2f046c49a1cf8b2a0d42f9f7be8526717",
  "source_text_sha256": "7404130cd79ee8132bec8e8ac4dcfeb2f046c49a1cf8b2a0d42f9f7be8526717"
}
~~~

## 呼び出し元

- [005f2d68](../005f2/005f2d68.md)

## 呼び出し先

- [008514f8](../00851/008514f8.md)

## 疑似コード / UTF-8 335 bytes

~~~c

void FUN_00afcca0(int param_1,int param_2,int param_3)

{
  long lVar1;
  
                    /* catch() { ... } // from try @ 00afbbac with catch @ 00afccb0 */
  lVar1 = FUN_008514f8();
  lVar1 = lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec;
  *(int *)(lVar1 + 0x84c10) = *(int *)(lVar1 + 0x84c10) + param_3;
  return;
}

~~~
