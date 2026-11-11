# 00afaf1c

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00afaf1c",
  "name": "FUN_00afaf1c",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e0cf2e86e9ec0896181c2ff26cfe211846c9b94ac05135f0377c9cc5d5a4a878",
  "source_text_sha256": "e0cf2e86e9ec0896181c2ff26cfe211846c9b94ac05135f0377c9cc5d5a4a878"
}
~~~

## 呼び出し元

- [00a4f3b4](../00a4f/00a4f3b4.md)
- [00a51fc4](../00a51/00a51fc4.md)

## 呼び出し先

- [008514f8](../00851/008514f8.md)

## 疑似コード / UTF-8 209 bytes

~~~c

void FUN_00afaf1c(int param_1,int param_2,uint param_3)

{
  long lVar1;
  
  lVar1 = FUN_008514f8();
  *(uint *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84a98) = param_3 & 1;
  return;
}

~~~
