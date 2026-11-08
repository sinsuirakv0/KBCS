# 00baedc4

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00baedc4",
  "name": "_ZNKSt6__ndk120__codecvt_utf8_utf16IDiE6do_outER9mbstate_tPKDiS5_RS5_PcS7_RS7_",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c40a8757b5ea11543cf697482040ab344830964da19c77c63874c961f33ce110",
  "source_text_sha256": "c40a8757b5ea11543cf697482040ab344830964da19c77c63874c961f33ce110"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bae6f8](../00bae/00bae6f8.md)

## 疑似コード / UTF-8 922 bytes

~~~c

void _ZNKSt6__ndk120__codecvt_utf8_utf16IDiE6do_outER9mbstate_tPKDiS5_RS5_PcS7_RS7_
               (long param_1,undefined8 param_2,undefined8 param_3,undefined8 param_4,
               undefined8 *param_5,undefined8 param_6,undefined8 param_7,undefined8 *param_8)

{
  undefined8 local_30;
  undefined8 uStack_28;
  
                    /* catch() { ... } // from try @ 00baed28 with catch @ 00baede0 */
                    /* catch() { ... } // from try @ 00baed1c with catch @ 00baedf8 */
  local_30 = param_6;
  uStack_28 = param_3;
                    /* catch() { ... } // from try @ 00baecf0 with catch @ 00baee10 */
  FUN_00bae6f8(param_3,param_4,&uStack_28,param_6,param_7,&local_30,*(undefined8 *)(param_1 + 0x10),
               *(undefined4 *)(param_1 + 0x18));
  *param_5 = uStack_28;
  *param_8 = local_30;
                    /* catch() { ... } // from try @ 00baecc4 with catch @ 00baee20 */
  return;
}

~~~
