# 00bddab0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bddab0.md)

## 関数情報

~~~json
{
  "address": "00bddab0",
  "name": "firebase::auth::Auth::SignOut",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5e487618010e6e0d3ca48707deb4be55d96094669b62459687e06eecfdfaeae4",
  "source_text_sha256": "5e487618010e6e0d3ca48707deb4be55d96094669b62459687e06eecfdfaeae4"
}
~~~
## 呼び出し元

- [008480dc](../00848/008480dc.md)

## 呼び出し先

- [00b5f9e4](../00b5f/00b5f9e4.md)

## 疑似コード 1/1 / UTF-8 120 bytes

~~~c

void __thiscall firebase::auth::Auth::SignOut(Auth *this)

{
  (*(code *)PTR_SignOut_00c1d590)();
  return;
}

~~~
