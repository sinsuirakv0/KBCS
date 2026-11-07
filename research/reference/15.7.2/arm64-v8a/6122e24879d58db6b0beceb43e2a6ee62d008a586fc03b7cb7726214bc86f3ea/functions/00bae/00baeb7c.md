# 00baeb7c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

<!-- kbcs-version-next -->
**別版の対応** [v15.7.4 `00baec88`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bae/00baec88.md)
<!-- /kbcs-version-next -->

## 関数情報

~~~json
{
  "address": "00baeb7c",
  "name": "_ZNKSt6__ndk120__codecvt_utf8_utf16IwE9do_lengthER9mbstate_tPKcS5_m",
  "size": 32,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4c77b4f5e7bd6dda52e6a7b90ea0da765997d64c607ecb2a866c5e579adbbde2",
  "source_text_sha256": "4c77b4f5e7bd6dda52e6a7b90ea0da765997d64c607ecb2a866c5e579adbbde2"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bac2fc](../00bac/00bac2fc.md)

## 疑似コード / UTF-8 430 bytes

~~~c

void _ZNKSt6__ndk120__codecvt_utf8_utf16IwE9do_lengthER9mbstate_tPKcS5_m
               (long param_1,undefined8 param_2,undefined8 param_3,undefined8 param_4,
               undefined8 param_5)

{
                    /* try { // try from 00baeb80 to 00caebd7 has its CatchHandler @ 00baeab8 */
  FUN_00bac2fc(param_3,param_4,param_5,*(undefined8 *)(param_1 + 0x18),
               *(undefined4 *)(param_1 + 0x20));
  return;
}

~~~
