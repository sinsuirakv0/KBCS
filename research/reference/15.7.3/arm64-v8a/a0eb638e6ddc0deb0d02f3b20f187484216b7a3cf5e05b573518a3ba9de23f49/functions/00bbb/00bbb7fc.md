# 00bbb7fc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00bbb7fc",
  "name": "FUN_00bbb7fc",
  "size": 148,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "fc14a8f2f55abc751ddd38887e6bb3886273cd3a3da6723d5a9eea4686342132",
  "source_text_sha256": "fc14a8f2f55abc751ddd38887e6bb3886273cd3a3da6723d5a9eea4686342132"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 1752 bytes

~~~c

void FUN_00bbb7fc(long param_1,long param_2,long param_3,undefined4 param_4)

{
                    /* catch() { ... } // from try @ 00bbb334 with catch @ 00bbb808 */
                    /* catch() { ... } // from try @ 00bbb254 with catch @ 00bbb80c */
  if (*(long *)(param_1 + 8) != *(long *)(*(long *)(param_2 + 0x10) + 8)) {
                    /* WARNING: Could not recover jumptable at 0x00bbb820. Too many branches */
                    /* WARNING: Treating indirect jump as call */
    (**(code **)(**(long **)(param_1 + 0x10) + 0x38))();
    return;
  }
                    /* catch() { ... } // from try @ 00bbb244 with catch @ 00bbb824 */
  if (*(int *)(param_2 + 0x3c) != 0) {
                    /* catch() { ... } // from try @ 00bbb238 with catch @ 00bbb838 */
                    /* catch() { ... } // from try @ 00bbb044 with catch @ 00bbb83c
                       catch() { ... } // from try @ 00bbb124 with catch @ 00bbb83c */
                    /* catch() { ... } // from try @ 00bbafc8 with catch @ 00bbb840 */
    if ((*(long *)(param_2 + 0x28) == *(long *)(param_2 + 0x50)) &&
       (*(long *)(param_2 + 0x20) == param_3)) {
      if (*(int *)(param_2 + 0x30) == 2) {
        *(undefined4 *)(param_2 + 0x30) = param_4;
        return;
      }
    }
    else {
      *(int *)(param_2 + 0x3c) = *(int *)(param_2 + 0x3c) + 1;
                    /* catch() { ... } // from try @ 00bbafb8 with catch @ 00bbb858 */
      *(undefined4 *)(param_2 + 0x30) = 2;
      *(undefined1 *)(param_2 + 0x4e) = 1;
    }
    return;
  }
  *(undefined4 *)(param_2 + 0x30) = param_4;
  *(undefined4 *)(param_2 + 0x3c) = 1;
  *(long *)(param_2 + 0x20) = param_3;
  *(undefined8 *)(param_2 + 0x28) = *(undefined8 *)(param_2 + 0x50);
  return;
}

~~~
