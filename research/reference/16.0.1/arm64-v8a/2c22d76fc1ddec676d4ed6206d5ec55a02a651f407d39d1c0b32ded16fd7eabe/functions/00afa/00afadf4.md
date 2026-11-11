# 00afadf4

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00afadf4",
  "name": "FUN_00afadf4",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d3222c9007a1c96ed8840a29ef2c170b4fe49360fd15c686384dd3483da32246",
  "source_text_sha256": "d3222c9007a1c96ed8840a29ef2c170b4fe49360fd15c686384dd3483da32246"
}
~~~

## 呼び出し元

- [00a4f3b4](../00a4f/00a4f3b4.md)

## 呼び出し先

- [008514f8](../00851/008514f8.md)

## 疑似コード / UTF-8 306 bytes

~~~c

void FUN_00afadf4(int param_1,int param_2,uint param_3)

{
  long lVar1;
  
                    /* try { // try from 00afae0c to 00bfaf97 has its CatchHandler @ 00afabcc */
  lVar1 = FUN_008514f8();
  *(uint *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84a84) = param_3 & 1;
  return;
}

~~~
