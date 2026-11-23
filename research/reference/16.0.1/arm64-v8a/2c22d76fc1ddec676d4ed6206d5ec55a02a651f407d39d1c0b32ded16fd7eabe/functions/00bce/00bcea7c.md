# 00bcea7c

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bce654`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bce/00bce654.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/priority-0081.md#compare-f9f940aca01c9481fe6c1535ce994521)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/priority-0091.md#compare-a50187fd24ed6ce83e55c78ccd5ec271)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcea7c",
  "name": "_ZN8firebase4auth4Auth18SignInWithProviderEPNS0_21FederatedAuthProviderE",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2a959116734c5c8062ac470d0a15a4d27ef1397816705e8e27fc624e46093947",
  "source_text_sha256": "2a959116734c5c8062ac470d0a15a4d27ef1397816705e8e27fc624e46093947"
}
~~~

## 呼び出し元

- [00c5ab90](../00c5a/00c5ab90.md)

## 呼び出し先

- [00c5abe0](../00c5a/00c5abe0.md)
- [00c5ac70](../00c5a/00c5ac70.md)
- [00c5b000](../00c5b/00c5b000.md)

## 関連文字列（未確認候補）

~~~text
"provider"
~~~

## 疑似コード / UTF-8 732 bytes

~~~c

void _ZN8firebase4auth4Auth18SignInWithProviderEPNS0_21FederatedAuthProviderE
               (long param_1,undefined8 *param_2,long *param_3)

{
                    /* catch() { ... } // from try @ 00bcdb58 with catch @ 00bcea88 */
  if (param_3 != (long *)0x0) {
                    /* WARNING: Could not recover jumptable at 0x00bceab0. Too many branches */
                    /* WARNING: Treating indirect jump as call */
    (**(code **)(*param_3 + 0x10))(param_1,param_3,*param_2);
    return;
  }
  _ZN8firebase9LogAssertEPKcz("provider");
  _ZN8firebase5MutexC1ENS0_4ModeE(param_1,0);
  *(undefined8 *)(param_1 + 0x28) = 0;
  _ZN8firebase12FutureHandleC1EmPNS_6detail18FutureApiInterfaceE(param_1 + 0x30,0,0);
  return;
}

~~~
