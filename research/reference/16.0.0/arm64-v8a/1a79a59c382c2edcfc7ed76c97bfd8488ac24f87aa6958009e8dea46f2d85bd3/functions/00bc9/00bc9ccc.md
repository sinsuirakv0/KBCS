# 00bc9ccc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bc9ccc",
  "name": "_ZN8firebase13remote_config32ConfigUpdateListenerRegistrationC1EOS1_",
  "size": 128,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6b7f65ea0aa637fe5243d5351675bad18f4715e6d16267c7e22c7dcef10a41ae",
  "source_text_sha256": "6b7f65ea0aa637fe5243d5351675bad18f4715e6d16267c7e22c7dcef10a41ae"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5a800](../00c5a/00c5a800.md)
- [00c5a810](../00c5a/00c5a810.md)

## 疑似コード / UTF-8 1509 bytes

~~~c

void _ZN8firebase13remote_config32ConfigUpdateListenerRegistrationC1EOS1_
               (long *param_1,long param_2)

{
  long lVar1;
  
                    /* catch() { ... } // from try @ 00bc9acc with catch @ 00bc9cd0 */
                    /* catch() { ... } // from try @ 00bc99fc with catch @ 00bc9cd8 */
                    /* catch() { ... } // from try @ 00bc9a1c with catch @ 00bc9ce0 */
                    /* catch() { ... } // from try @ 00bc9bc4 with catch @ 00bc9ce4 */
  *param_1 = (long)(PTR__ZTVN8firebase13remote_config32ConfigUpdateListenerRegistrationE_00c9b528 +
                   0x10);
  param_1[1] = *(long *)(param_2 + 8);
  param_1[2] = 0;
  lVar1 = 0;
  if (*(long *)(param_2 + 8) != 0) {
    _ZN8firebase15CleanupNotifier16UnregisterObjectEPv(*(long *)(param_2 + 8) + 0x138,param_2);
    lVar1 = param_1[2];
  }
  param_1[2] = *(long *)(param_2 + 0x10);
  *(long *)(param_2 + 0x10) = lVar1;
  if (param_1[1] != 0) {
                    /* catch() { ... } // from try @ 00bc99e4 with catch @ 00bc9d24
                       catch() { ... } // from try @ 00bc9b9c with catch @ 00bc9d24 */
                    /* catch() { ... } // from try @ 00bc9aec with catch @ 00bc9d2c */
    _ZN8firebase15CleanupNotifier14RegisterObjectEPvPFvS1_E
              (param_1[1] + 0x138,param_1,
               PTR__ZN8firebase13remote_config9CleanupFnINS0_32ConfigUpdateListenerRegistrationENS0_8internal20RemoteConfigInternalEE7CleanupEPv_00c9b520
              );
    return;
  }
  return;
}

~~~
