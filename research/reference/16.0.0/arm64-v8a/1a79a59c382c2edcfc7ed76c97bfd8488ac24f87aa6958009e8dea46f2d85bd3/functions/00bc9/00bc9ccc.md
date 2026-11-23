# 00bc9ccc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b5a7cc`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5a7cc.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/2-3/alignment_unresolved-0017.md#compare-5c1e47a59dd0e98c3aac396722ae0f6e)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 構造資料不足
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

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
