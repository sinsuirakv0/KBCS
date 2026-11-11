# 00bcadfc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00bcadfc",
  "name": "_ZN8firebase4auth4Auth3appEv",
  "size": 56,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5d091b0ac1e4e2de17e851ba733b61c7dae759f81724e54341b7d3ae1144371b",
  "source_text_sha256": "5d091b0ac1e4e2de17e851ba733b61c7dae759f81724e54341b7d3ae1144371b"
}
~~~

## 呼び出し元

- [00c5da80](../00c5d/00c5da80.md)

## 呼び出し先

- [00c5b000](../00c5b/00c5b000.md)

## 関連文字列（未確認候補）

~~~text
"auth_data_ != nullptr"
~~~

## 疑似コード / UTF-8 282 bytes

~~~c

undefined8 _ZN8firebase4auth4Auth3appEv(undefined8 *param_1)

{
  undefined8 *puVar1;
  
  puVar1 = (undefined8 *)*param_1;
  if (puVar1 == (undefined8 *)0x0) {
    _ZN8firebase9LogAssertEPKcz("auth_data_ != nullptr");
    puVar1 = (undefined8 *)*param_1;
  }
  return *puVar1;
}

~~~
