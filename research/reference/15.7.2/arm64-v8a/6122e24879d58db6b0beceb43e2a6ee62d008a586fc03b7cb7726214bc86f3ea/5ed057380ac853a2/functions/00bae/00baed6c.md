# 00baed6c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00baed6c.md)

## 関数情報

~~~json
{
  "address": "00baed6c",
  "name": "_ZNKSt6__ndk120__codecvt_utf8_utf16IDiE5do_inER9mbstate_tPKcS5_RS5_PDiS7_RS7_",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "aa022cd3e817c298bfd85da7a64aeafe8dca7f13f9e426555061545f1e90e56e",
  "source_text_sha256": "aa022cd3e817c298bfd85da7a64aeafe8dca7f13f9e426555061545f1e90e56e"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bae8c8](../00bae/00bae8c8.md)

## 疑似コード 1/1 / UTF-8 834 bytes

~~~c

void _ZNKSt6__ndk120__codecvt_utf8_utf16IDiE5do_inER9mbstate_tPKcS5_RS5_PDiS7_RS7_
               (long param_1,undefined8 param_2,undefined8 param_3,undefined8 param_4,
               undefined8 *param_5,undefined8 param_6,undefined8 param_7,undefined8 *param_8)

{
  undefined8 local_30;
  undefined8 uStack_28;
  
                    /* catch() { ... } // from try @ 00baeb68 with catch @ 00baed7c */
                    /* catch() { ... } // from try @ 00baeb34 with catch @ 00baed90 */
                    /* catch() { ... } // from try @ 00baeb74 with catch @ 00baed98 */
  local_30 = param_6;
  uStack_28 = param_3;
  FUN_00bae8c8(param_3,param_4,&uStack_28,param_6,param_7,&local_30,*(undefined8 *)(param_1 + 0x10),
               *(undefined4 *)(param_1 + 0x18));
  *param_5 = uStack_28;
  *param_8 = local_30;
  return;
}

~~~
