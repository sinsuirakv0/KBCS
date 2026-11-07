# 00baecfc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

<!-- kbcs-version-next -->
**別版の対応** [v15.7.4 `00baee08`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bae/00baee08.md)
<!-- /kbcs-version-next -->

## 関数情報

~~~json
{
  "address": "00baecfc",
  "name": "_ZNKSt6__ndk120__codecvt_utf8_utf16IDiE6do_outER9mbstate_tPKDiS5_RS5_PcS7_RS7_",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d102170e09986169a85fffc09b45abbee3a6b1a447f29e8017a0ccc921777949",
  "source_text_sha256": "d102170e09986169a85fffc09b45abbee3a6b1a447f29e8017a0ccc921777949"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bae630](../00bae/00bae630.md)

## 疑似コード / UTF-8 922 bytes

~~~c

void _ZNKSt6__ndk120__codecvt_utf8_utf16IDiE6do_outER9mbstate_tPKDiS5_RS5_PcS7_RS7_
               (long param_1,undefined8 param_2,undefined8 param_3,undefined8 param_4,
               undefined8 *param_5,undefined8 param_6,undefined8 param_7,undefined8 *param_8)

{
  undefined8 local_30;
  undefined8 uStack_28;
  
                    /* catch() { ... } // from try @ 00baec60 with catch @ 00baed18 */
                    /* catch() { ... } // from try @ 00baec54 with catch @ 00baed30 */
  local_30 = param_6;
  uStack_28 = param_3;
                    /* catch() { ... } // from try @ 00baec28 with catch @ 00baed48 */
  FUN_00bae630(param_3,param_4,&uStack_28,param_6,param_7,&local_30,*(undefined8 *)(param_1 + 0x10),
               *(undefined4 *)(param_1 + 0x18));
  *param_5 = uStack_28;
  *param_8 = local_30;
                    /* catch() { ... } // from try @ 00baebfc with catch @ 00baed58 */
  return;
}

~~~
