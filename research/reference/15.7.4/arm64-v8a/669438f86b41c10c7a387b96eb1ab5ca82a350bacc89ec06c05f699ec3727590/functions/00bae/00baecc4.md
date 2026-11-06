# 00baecc4

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

## 関数情報

~~~json
{
  "address": "00baecc4",
  "name": "_ZNKSt6__ndk120__codecvt_utf8_utf16IDsE6do_outER9mbstate_tPKDsS5_RS5_PcS7_RS7_",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0467b6cbcc7e0681d091abd551204a84a34ff82efc05dd54a2d4171d773baaaf",
  "source_text_sha256": "0467b6cbcc7e0681d091abd551204a84a34ff82efc05dd54a2d4171d773baaaf"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00babe6c](../00bab/00babe6c.md)

## 疑似コード / UTF-8 768 bytes

~~~c

void _ZNKSt6__ndk120__codecvt_utf8_utf16IDsE6do_outER9mbstate_tPKDsS5_RS5_PcS7_RS7_
               (long param_1,undefined8 param_2,undefined8 param_3,undefined8 param_4,
               undefined8 *param_5,undefined8 param_6,undefined8 param_7,undefined8 *param_8)

{
  undefined8 local_30;
  undefined8 uStack_28;
  
                    /* try { // try from 00baece4 to 00caecef has its CatchHandler @ 00baee78 */
  local_30 = param_6;
  uStack_28 = param_3;
                    /* try { // try from 00baed08 to 00caed0f has its CatchHandler @ 00baee64 */
  FUN_00babe6c(param_3,param_4,&uStack_28,param_6,param_7,&local_30,*(undefined8 *)(param_1 + 0x10),
               *(undefined4 *)(param_1 + 0x18));
  *param_5 = uStack_28;
  *param_8 = local_30;
  return;
}

~~~
