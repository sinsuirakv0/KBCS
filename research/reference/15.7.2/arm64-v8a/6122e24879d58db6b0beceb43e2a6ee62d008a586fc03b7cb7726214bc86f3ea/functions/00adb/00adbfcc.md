# 00adbfcc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

<!-- kbcs-version-next -->
**別版の対応** [v15.7.4 `00adc0d8`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adc/00adc0d8.md)
<!-- /kbcs-version-next -->

## 関数情報

~~~json
{
  "address": "00adbfcc",
  "name": "FUN_00adbfcc",
  "size": 72,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "fcab2c2bd2fb3508186b472a804cc0c3a17e575f2d604f020fb94d8f87df6a9d",
  "source_text_sha256": "fcab2c2bd2fb3508186b472a804cc0c3a17e575f2d604f020fb94d8f87df6a9d"
}
~~~

## 呼び出し元

- [005d996c](../005d9/005d996c.md)
- [006f424c](../006f4/006f424c.md)
- [006f42ec](../006f4/006f42ec.md)
- [006f4724](../006f4/006f4724.md)
- [006f478c](../006f4/006f478c.md)
- [009121c4](../00912/009121c4.md)
- [00957f9c](../00957/00957f9c.md)

## 呼び出し先

- [005c3468](../005c3/005c3468.md)

## 疑似コード / UTF-8 288 bytes

~~~c

void FUN_00adbfcc(byte *param_1,int param_2)

{
  *(uint *)param_1 =
       (uint)(param_1[7] ^ *param_1) + param_2 + (uint)(param_1[6] ^ param_1[1]) * 0x100 +
       (uint)(param_1[5] ^ param_1[2]) * 0x10000 + (uint)(param_1[4] ^ param_1[3]) * 0x1000000;
  FUN_005c3468();
  return;
}

~~~
