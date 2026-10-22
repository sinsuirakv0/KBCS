# 00bdfae0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bdfae0.md)

## 関数情報

~~~json
{
  "address": "00bdfae0",
  "name": "reflection::Service::Verify",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3e6ce314003036de9f6b82b538b4267c2e5df7a2c9bb75d0cf05699f6a8bd35f",
  "source_text_sha256": "3e6ce314003036de9f6b82b538b4267c2e5df7a2c9bb75d0cf05699f6a8bd35f"
}
~~~
## 呼び出し元

- [00b352f8](../00b35/00b352f8.md)

## 呼び出し先

- [00b37648](../00b37/00b37648.md)

## 疑似コード 1/1 / UTF-8 138 bytes

~~~c

void __thiscall reflection::Service::Verify(Service *this,Verifier *param_1)

{
  (*(code *)PTR_Verify_00c1e5a8)();
  return;
}

~~~
