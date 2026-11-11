# 00af8edc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00af8edc",
  "name": "FUN_00af8edc",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "093fc55f9e6d291bd3c8388619ccaa4e856a4b40df4937f0e3f969363af7719c",
  "source_text_sha256": "093fc55f9e6d291bd3c8388619ccaa4e856a4b40df4937f0e3f969363af7719c"
}
~~~

## 呼び出し元

- [007102d8](../00710/007102d8.md)

## 呼び出し先

- [008514f8](../00851/008514f8.md)

## 疑似コード / UTF-8 385 bytes

~~~c

undefined4 FUN_00af8edc(int param_1,int param_2)

{
  long lVar1;
  
  lVar1 = FUN_008514f8();
                    /* try { // try from 00af8f08 to 00bf8f0f has its CatchHandler @ 00af9200 */
                    /* try { // try from 00af8f10 to 00bf8f43 has its CatchHandler @ 00af8cac */
  return *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x8499c);
}

~~~
