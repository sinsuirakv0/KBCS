# 00a9baac

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

<!-- kbcs-version-next -->
**別版の対応** [v15.7.4 `00a9baf0`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9b/00a9baf0.md)
<!-- /kbcs-version-next -->

## 関数情報

~~~json
{
  "address": "00a9baac",
  "name": "FUN_00a9baac",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e226690d0ef4f7fa3deb051f491fbb6573349657e753e8924cb44eb117a0a245",
  "source_text_sha256": "e226690d0ef4f7fa3deb051f491fbb6573349657e753e8924cb44eb117a0a245"
}
~~~

## 呼び出し元

- [009f1e64](../009f1/009f1e64.md)

## 呼び出し先

- [0081f580](../0081f/0081f580.md)

## 疑似コード / UTF-8 209 bytes

~~~c

void FUN_00a9baac(int param_1,int param_2,uint param_3)

{
  long lVar1;
  
  lVar1 = FUN_0081f580();
  *(uint *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84464) = param_3 & 1;
  return;
}

~~~
