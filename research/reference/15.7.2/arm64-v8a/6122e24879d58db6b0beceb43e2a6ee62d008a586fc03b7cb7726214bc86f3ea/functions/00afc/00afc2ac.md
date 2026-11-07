# 00afc2ac

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

<!-- kbcs-version-next -->
**別版の対応** [v15.7.4 `00afc3b8`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afc3b8.md)
<!-- /kbcs-version-next -->

## 関数情報

~~~json
{
  "address": "00afc2ac",
  "name": "_ZN8firebase8callback16BlockingCallbackD2Ev",
  "size": 84,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "be97926dc2869e5c23a11911486bd001b3866818b23978a2b7561dbe6125a4ee",
  "source_text_sha256": "be97926dc2869e5c23a11911486bd001b3866818b23978a2b7561dbe6125a4ee"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdebc0](../00bde/00bdebc0.md)

## 疑似コード / UTF-8 468 bytes

~~~c

void _ZN8firebase8callback16BlockingCallbackD2Ev(long *param_1)

{
  *param_1 = (long)(PTR__ZTVN8firebase8callback16BlockingCallbackE_00c1b880 + 0x10);
  sem_post(*(sem_t **)param_1[2]);
  if ((long *)param_1[1] != (long *)0x0) {
                    /* WARNING: Could not recover jumptable at 0x00afc2f0. Too many branches */
                    /* WARNING: Treating indirect jump as call */
    (**(code **)(*(long *)param_1[1] + 8))();
    return;
  }
  return;
}

~~~
