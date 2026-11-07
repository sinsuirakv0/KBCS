# 00b7efbc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

<!-- kbcs-version-next -->
**別版の対応** [v15.7.4 `00b7f0c8`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f0c8.md)
<!-- /kbcs-version-next -->

## 関数情報

~~~json
{
  "address": "00b7efbc",
  "name": "_ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEEaSERKS3_",
  "size": 80,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "87721279f401cc3a527012c9eef0116bd99202df3f17decd80635b1e801ceeb9",
  "source_text_sha256": "87721279f401cc3a527012c9eef0116bd99202df3f17decd80635b1e801ceeb9"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00be11e0](../00be1/00be11e0.md)

## 疑似コード / UTF-8 662 bytes

~~~c

long _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEEaSERKS3_(long param_1,long param_2)

{
  undefined8 uVar1;
  
  _ZNSt6__ndk16localeaSERKS0_(param_1 + 8,param_2 + 8);
  uVar1 = *(undefined8 *)(param_2 + 0x10);
  *(undefined8 *)(param_1 + 0x18) = *(undefined8 *)(param_2 + 0x18);
  *(undefined8 *)(param_1 + 0x10) = uVar1;
  uVar1 = *(undefined8 *)(param_2 + 0x20);
  *(undefined8 *)(param_1 + 0x28) = *(undefined8 *)(param_2 + 0x28);
  *(undefined8 *)(param_1 + 0x20) = uVar1;
  uVar1 = *(undefined8 *)(param_2 + 0x30);
  *(undefined8 *)(param_1 + 0x38) = *(undefined8 *)(param_2 + 0x38);
  *(undefined8 *)(param_1 + 0x30) = uVar1;
  return param_1;
}

~~~
