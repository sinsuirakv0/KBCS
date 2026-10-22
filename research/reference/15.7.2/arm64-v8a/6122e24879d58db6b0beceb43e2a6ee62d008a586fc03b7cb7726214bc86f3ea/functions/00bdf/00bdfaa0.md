# 00bdfaa0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bdfaa0.md)

## 関数情報

~~~json
{
  "address": "00bdfaa0",
  "name": "reflection::Object::Verify",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a5e4ff05aad33fe7bd8fbdf42e4c315aac5f513adbe7d7f35b75d2dd9ccecf0c",
  "source_text_sha256": "a5e4ff05aad33fe7bd8fbdf42e4c315aac5f513adbe7d7f35b75d2dd9ccecf0c"
}
~~~
## 呼び出し元

- [00b352f8](../00b35/00b352f8.md)
- [00b371b4](../00b37/00b371b4.md)
- [00b37c10](../00b37/00b37c10.md)

## 呼び出し先

- [00b359f8](../00b35/00b359f8.md)

## 疑似コード 1/1 / UTF-8 136 bytes

~~~c

void __thiscall reflection::Object::Verify(Object *this,Verifier *param_1)

{
  (*(code *)PTR_Verify_00c1e588)();
  return;
}

~~~
