# 00b6acdc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

## 関数情報

~~~json
{
  "address": "00b6acdc",
  "name": "_ZN8firebase4auth17PhoneAuthProvider19ForceResendingTokenC2ERKS2_",
  "size": 56,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "478ecede73e1fded0dd956649e2e26fd274f9ffc82d663439e798c898e99cfb1",
  "source_text_sha256": "478ecede73e1fded0dd956649e2e26fd274f9ffc82d663439e798c898e99cfb1"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdaf40](../00bda/00bdaf40.md)
- [00be0d40](../00be0/00be0d40.md)

## 疑似コード / UTF-8 337 bytes

~~~c

void _ZN8firebase4auth17PhoneAuthProvider19ForceResendingTokenC2ERKS2_
               (undefined8 *param_1,undefined8 *param_2)

{
  undefined8 *puVar1;
  
  puVar1 = (undefined8 *)_Znwm(8);
  *puVar1 = 0;
  *param_1 = puVar1;
  _ZN8firebase4auth23ForceResendingTokenData6SetRefEP8_jobject(puVar1,*(undefined8 *)*param_2);
  return;
}

~~~
