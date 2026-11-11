# 00bcea7c

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

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
