# 00bae6cc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-previous -->
**別版の対応** [v15.7.2 `00bae5c0`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bae/00bae5c0.md)
<!-- /kbcs-version-previous -->

## 関数情報

~~~json
{
  "address": "00bae6cc",
  "name": "_ZNKSt6__ndk120__codecvt_utf8_utf16IwE6do_outER9mbstate_tPKwS5_RS5_PcS7_RS7_",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "26b4bf1e3e92f277b43a34aac4ab2869f8de2fe60311d0e8b75d2d5a115bc0c2",
  "source_text_sha256": "26b4bf1e3e92f277b43a34aac4ab2869f8de2fe60311d0e8b75d2d5a115bc0c2"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bae73c](../00bae/00bae73c.md)

## 疑似コード / UTF-8 659 bytes

~~~c

void _ZNKSt6__ndk120__codecvt_utf8_utf16IwE6do_outER9mbstate_tPKwS5_RS5_PcS7_RS7_
               (long param_1,undefined8 param_2,undefined8 param_3,undefined8 param_4,
               undefined8 *param_5,undefined8 param_6,undefined8 param_7,undefined8 *param_8)

{
  undefined8 local_30;
  undefined8 uStack_28;
  
                    /* catch() { ... } // from try @ 00bae8c8 with catch @ 00bae6ec */
  local_30 = param_6;
  uStack_28 = param_3;
  FUN_00bae73c(param_3,param_4,&uStack_28,param_6,param_7,&local_30,*(undefined8 *)(param_1 + 0x18),
               *(undefined4 *)(param_1 + 0x20));
  *param_5 = uStack_28;
  *param_8 = local_30;
  return;
}

~~~
