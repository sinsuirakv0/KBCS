# 00baecc0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

<!-- kbcs-version-next -->
**別版の対応** [v15.7.4 `00baedcc`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bae/00baedcc.md)
<!-- /kbcs-version-next -->

## 関数情報

~~~json
{
  "address": "00baecc0",
  "name": "_ZNKSt6__ndk120__codecvt_utf8_utf16IDsE9do_lengthER9mbstate_tPKcS5_m",
  "size": 32,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e71cec43b4c98418dca17f779d27456bcc63b404470abf7805b4da7dc0fe878e",
  "source_text_sha256": "e71cec43b4c98418dca17f779d27456bcc63b404470abf7805b4da7dc0fe878e"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bac2fc](../00bac/00bac2fc.md)

## 疑似コード / UTF-8 334 bytes

~~~c

void _ZNKSt6__ndk120__codecvt_utf8_utf16IDsE9do_lengthER9mbstate_tPKcS5_m
               (long param_1,undefined8 param_2,undefined8 param_3,undefined8 param_4,
               undefined8 param_5)

{
  FUN_00bac2fc(param_3,param_4,param_5,*(undefined8 *)(param_1 + 0x10),
               *(undefined4 *)(param_1 + 0x18));
  return;
}

~~~
