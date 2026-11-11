# 00bda8fc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00bda8fc",
  "name": "_ZN8firebase4auth17PhoneAuthProviderD1Ev",
  "size": 108,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a16ac5707c15159dea4669b75def13b653c6450e518ac3f22aba750f0d9772f3",
  "source_text_sha256": "a16ac5707c15159dea4669b75def13b653c6450e518ac3f22aba750f0d9772f3"
}
~~~

## 呼び出し元

- [00c5d9c0](../00c5d/00c5d9c0.md)

## 呼び出し先

- [00c57eb0](../00c57/00c57eb0.md)
- [00c5b000](../00c5b/00c5b000.md)
- [00c5b080](../00c5b/00c5b080.md)
- [00c5b260](../00c5b/00c5b260.md)

## 関連文字列（未確認候補）

~~~text
"app != nullptr"
~~~

## 疑似コード / UTF-8 498 bytes

~~~c

void _ZN8firebase4auth17PhoneAuthProviderD1Ev(long *param_1)

{
  long lVar1;
  long *plVar2;
  
  if (*param_1 != 0) {
    lVar1 = _ZN8firebase10app_common9GetAnyAppEv();
    if (lVar1 == 0) {
      _ZN8firebase9LogAssertEPKcz("app != nullptr");
    }
    plVar2 = (long *)_ZNK8firebase3App9GetJNIEnvEv(lVar1);
    (**(code **)(*plVar2 + 0xb0))(plVar2,*(undefined8 *)(*param_1 + 8));
    if ((void *)*param_1 != (void *)0x0) {
      _ZdlPv((void *)*param_1);
      return;
    }
  }
  return;
}

~~~
