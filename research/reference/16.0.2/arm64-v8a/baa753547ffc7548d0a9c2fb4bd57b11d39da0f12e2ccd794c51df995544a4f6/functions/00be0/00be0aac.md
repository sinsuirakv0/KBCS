# 00be0aac

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00be0aac",
  "name": "_ZNK8firebase4auth4User26ReauthenticateWithProviderEPNS0_21FederatedAuthProviderE",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b78a632a502f68706b4b60ef2300297a6d5b34765e83c4e40e34b0fe16b70dc1",
  "source_text_sha256": "b78a632a502f68706b4b60ef2300297a6d5b34765e83c4e40e34b0fe16b70dc1"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5acb0](../00c5a/00c5acb0.md)
- [00c5ad40](../00c5a/00c5ad40.md)
- [00c5b0d0](../00c5b/00c5b0d0.md)

## 関連文字列（未確認候補）

~~~text
"provider"
~~~

## 疑似コード / UTF-8 670 bytes

~~~c

void _ZNK8firebase4auth4User26ReauthenticateWithProviderEPNS0_21FederatedAuthProviderE
               (long param_1,long param_2,long *param_3)

{
  if (param_3 != (long *)0x0) {
                    /* WARNING: Could not recover jumptable at 0x00be0ae0. Too many branches */
                    /* WARNING: Treating indirect jump as call */
    (**(code **)(*param_3 + 0x20))(param_1,param_3,*(undefined8 *)(param_2 + 0x98));
    return;
  }
  _ZN8firebase9LogAssertEPKcz("provider");
  _ZN8firebase5MutexC1ENS0_4ModeE(param_1,0);
  *(undefined8 *)(param_1 + 0x28) = 0;
  _ZN8firebase12FutureHandleC1EmPNS_6detail18FutureApiInterfaceE(param_1 + 0x30,0,0);
  return;
}

~~~
