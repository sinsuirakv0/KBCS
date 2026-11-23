# 00b6bebc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00b6bdf4`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6b/00b6bdf4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/af8e2f5c5fc38f06774ff85c/0-1/alignment_unresolved-0004.md#compare-6bc3b12a0327b294d09be5b285790fab)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 構造資料不足
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b6bebc",
  "name": "_ZN8firebase4auth22FederatedOAuthProvider15SetProviderDataERKNS0_26FederatedOAuthProviderDataE",
  "size": 108,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d9fdde45e04b4bf48cf951156c2f3cdd1d440252067e6358602b5ac538a9cb8a",
  "source_text_sha256": "d9fdde45e04b4bf48cf951156c2f3cdd1d440252067e6358602b5ac538a9cb8a"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [005188a4](../00518/005188a4.md)
- [00bde1e0](../00bde/00bde1e0.md)
- [00be0040](../00be0/00be0040.md)

## 疑似コード / UTF-8 1184 bytes

~~~c

void _ZN8firebase4auth22FederatedOAuthProvider15SetProviderDataERKNS0_26FederatedOAuthProviderDataE
               (long param_1,byte *param_2)

{
  ulong uVar1;
  byte *pbVar2;
  
  if ((byte *)(param_1 + 8) != param_2) {
    uVar1 = *(ulong *)(param_2 + 8);
    pbVar2 = *(byte **)(param_2 + 0x10);
                    /* try { // try from 00b6beec to 00c6beef has its CatchHandler @ 00b6c074 */
    if ((*param_2 & 1) == 0) {
      pbVar2 = param_2 + 1;
      uVar1 = (ulong)(*param_2 >> 1);
    }
    _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
              ((byte *)(param_1 + 8),pbVar2,uVar1);
    _ZNSt6__ndk16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE6assignIPS6_EENS_9enable_ifIXaasr21__is_forward_iteratorIT_EE5valuesr16is_constructibleIS6_NS_15iterator_traitsISC_E9referenceEEE5valueEvE4typeESC_SC_
              (param_1 + 0x20,*(undefined8 *)(param_2 + 0x18),*(undefined8 *)(param_2 + 0x20));
                    /* try { // try from 00b6bf18 to 00c6bf3b has its CatchHandler @ 00b6c01c */
    FUN_005188a4(param_1 + 0x38,*(undefined8 *)(param_2 + 0x30),param_2 + 0x38);
    return;
  }
  return;
}

~~~
