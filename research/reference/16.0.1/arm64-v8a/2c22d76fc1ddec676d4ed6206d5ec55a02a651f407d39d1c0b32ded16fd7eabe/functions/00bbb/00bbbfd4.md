# 00bbbfd4

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00bbbfd4",
  "name": "_ZN8firebase9messaging27IsRegistrationOnInitEnabledEv",
  "size": 108,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9901f2158a0858d99b22820e4bee67bcdfcb9593c2c205c8a1fd40aa35baef45",
  "source_text_sha256": "9901f2158a0858d99b22820e4bee67bcdfcb9593c2c205c8a1fd40aa35baef45"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00497a48](../00497/00497a48.md)
- [00c5aca0](../00c5a/00c5aca0.md)
- [00c5b000](../00c5b/00c5b000.md)
- [00c5b080](../00c5b/00c5b080.md)

## 関連文字列（未確認候補）

~~~text
"Messaging not initialized."
"internal::IsInitialized()"
~~~

## 疑似コード / UTF-8 539 bytes

~~~c

bool _ZN8firebase9messaging27IsRegistrationOnInitEnabledEv(void)

{
  char cVar1;
  undefined8 uVar2;
  
  if (DAT_01126360 == 0) {
    _ZN8firebase8LogErrorEPKcz("internal::IsInitialized()");
    _ZN8firebase9LogAssertEPKcz("Messaging not initialized.");
    if (DAT_01126360 == 0) {
      return true;
    }
  }
  uVar2 = _ZNK8firebase3App9GetJNIEnvEv();
                    /* try { // try from 00bbc020 to 00cbc02b has its CatchHandler @ 00bbc7b8 */
  cVar1 = FUN_00497a48(uVar2,DAT_01126398,DAT_011262b8);
  return cVar1 != '\0';
}

~~~
