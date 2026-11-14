# 00bcfb0c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bcfb0c",
  "name": "_ZN8firebase4auth4Auth18SignInWithProviderEPNS0_21FederatedAuthProviderE",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ed2efcc22eaa55b65068fa05d6f49da405266be4e6646afc5dcb4b8653b2f631",
  "source_text_sha256": "ed2efcc22eaa55b65068fa05d6f49da405266be4e6646afc5dcb4b8653b2f631"
}
~~~

## 呼び出し元

- [00c5bc30](../00c5b/00c5bc30.md)

## 呼び出し先

- [00c5bc80](../00c5b/00c5bc80.md)
- [00c5bd10](../00c5b/00c5bd10.md)
- [00c5c0a0](../00c5c/00c5c0a0.md)

## 関連文字列（未確認候補）

~~~text
"provider"
~~~

## 疑似コード / UTF-8 645 bytes

~~~c

void _ZN8firebase4auth4Auth18SignInWithProviderEPNS0_21FederatedAuthProviderE
               (long param_1,undefined8 *param_2,long *param_3)

{
  if (param_3 != (long *)0x0) {
                    /* WARNING: Could not recover jumptable at 0x00bcfb40. Too many branches */
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
