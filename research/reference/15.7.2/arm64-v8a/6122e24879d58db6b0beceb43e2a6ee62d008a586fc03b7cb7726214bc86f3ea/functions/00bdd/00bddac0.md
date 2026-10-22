# 00bddac0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bddac0.md)

## 関数情報

~~~json
{
  "address": "00bddac0",
  "name": "firebase::auth::Auth::current_user",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "eb13a700b7d55423495cf9c668dee462c2dbb7eedd0613e63925b0de3bbd08ab",
  "source_text_sha256": "eb13a700b7d55423495cf9c668dee462c2dbb7eedd0613e63925b0de3bbd08ab"
}
~~~
## 呼び出し元

- [008480ec](../00848/008480ec.md)
- [0084859c](../00848/0084859c.md)
- [00b64df8](../00b64/00b64df8.md)
- [00b65208](../00b65/00b65208.md)

## 呼び出し先

- [00b5f770](../00b5f/00b5f770.md)

## 疑似コード 1/1 / UTF-8 113 bytes

~~~c

void firebase::auth::Auth::current_user(void)

{
  (*(code *)PTR_current_user_00c1d598)();
  return;
}

~~~
