# 00b6acdc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00b6acdc.md)

## 関数情報

~~~json
{
  "address": "00b6acdc",
  "name": "firebase::auth::PhoneAuthProvider::ForceResendingToken::ForceResendingToken",
  "size": 56,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "682fd9990e5b7db166d1eea48010f64add09288d54ad68b45eb5bd0b226a1c3f",
  "source_text_sha256": "682fd9990e5b7db166d1eea48010f64add09288d54ad68b45eb5bd0b226a1c3f"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdaf40](../00bda/00bdaf40.md)
- [00be0d40](../00be0/00be0d40.md)

## 疑似コード 1/1 / UTF-8 569 bytes

~~~c

/* firebase::auth::PhoneAuthProvider::ForceResendingToken::ForceResendingToken(firebase::auth::PhoneAuthProvider::ForceResendingToken
   const&) */

void __thiscall
firebase::auth::PhoneAuthProvider::ForceResendingToken::ForceResendingToken
          (ForceResendingToken *this,ForceResendingToken *param_1)

{
  ForceResendingTokenData *this_00;
  
  this_00 = operator_new(8);
  *(undefined8 *)this_00 = 0;
  *(ForceResendingTokenData **)this = this_00;
  ForceResendingTokenData::SetRef(this_00,(_jobject *)**(undefined8 **)param_1);
  return;
}

~~~
