# 00babcf8

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

<!-- kbcs-version-next -->
**別版の対応** [v15.7.4 `00babe04`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bab/00babe04.md)
<!-- /kbcs-version-next -->

## 関数情報

~~~json
{
  "address": "00babcf8",
  "name": "_ZNKSt6__ndk17codecvtIDsc9mbstate_tE6do_outERS1_PKDsS5_RS5_PcS7_RS7_",
  "size": 104,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "725ad31e2d52185309b09f9fdcdc5dfbcd9c3aa1b7bcf8050614642a8e25b519",
  "source_text_sha256": "725ad31e2d52185309b09f9fdcdc5dfbcd9c3aa1b7bcf8050614642a8e25b519"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00babd60](../00bab/00babd60.md)

## 疑似コード / UTF-8 850 bytes

~~~c

void _ZNKSt6__ndk17codecvtIDsc9mbstate_tE6do_outERS1_PKDsS5_RS5_PcS7_RS7_
               (undefined8 param_1,undefined8 param_2,undefined8 param_3,undefined8 param_4,
               undefined8 *param_5,undefined8 param_6,undefined8 param_7,undefined8 *param_8)

{
  undefined8 local_30;
  undefined8 uStack_28;
  
  local_30 = param_6;
  uStack_28 = param_3;
                    /* try { // try from 00babd3c to 00cabf0b has its CatchHandler @ 00babd3c
                       catch() { ... } // from try @ 00babd3c with catch @ 00babd3c
                       catch() { ... } // from try @ 00babf28 with catch @ 00babd3c
                       catch() { ... } // from try @ 00bac1c4 with catch @ 00babd3c */
  FUN_00babd60(param_3,param_4,&uStack_28,param_6,param_7,&local_30,0x10ffff,0);
  *param_5 = uStack_28;
  *param_8 = local_30;
  return;
}

~~~
