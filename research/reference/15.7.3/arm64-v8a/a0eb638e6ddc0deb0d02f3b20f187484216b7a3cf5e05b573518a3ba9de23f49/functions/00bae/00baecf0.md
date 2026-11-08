# 00baecf0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00baecf0",
  "name": "_ZNKSt6__ndk120__codecvt_utf8_utf16IDsE5do_inER9mbstate_tPKcS5_RS5_PDsS7_RS7_",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9e77444ccc37635cd39e097a7b1122ca0f6aa9007c8f8a2bc60459c14bb46b02",
  "source_text_sha256": "9e77444ccc37635cd39e097a7b1122ca0f6aa9007c8f8a2bc60459c14bb46b02"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bac0ec](../00bac/00bac0ec.md)

## 疑似コード / UTF-8 864 bytes

~~~c

void _ZNKSt6__ndk120__codecvt_utf8_utf16IDsE5do_inER9mbstate_tPKcS5_RS5_PDsS7_RS7_
               (long param_1,undefined8 param_2,undefined8 param_3,undefined8 param_4,
               undefined8 *param_5,undefined8 param_6,undefined8 param_7,undefined8 *param_8)

{
  undefined8 local_30;
  undefined8 uStack_28;
  
                    /* try { // try from 00baed1c to 00caed27 has its CatchHandler @ 00baedf8 */
                    /* try { // try from 00baed28 to 00caed37 has its CatchHandler @ 00baede0 */
  local_30 = param_6;
  uStack_28 = param_3;
                    /* try { // try from 00baed38 to 00caeea7 has its CatchHandler @ 00baeb80 */
  FUN_00bac0ec(param_3,param_4,&uStack_28,param_6,param_7,&local_30,*(undefined8 *)(param_1 + 0x10),
               *(undefined4 *)(param_1 + 0x18));
  *param_5 = uStack_28;
  *param_8 = local_30;
  return;
}

~~~
