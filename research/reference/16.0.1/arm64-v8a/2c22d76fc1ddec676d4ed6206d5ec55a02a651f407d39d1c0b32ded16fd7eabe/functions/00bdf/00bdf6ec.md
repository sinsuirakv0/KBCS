# 00bdf6ec

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00bdf6ec",
  "name": "_ZN8firebase4auth22AndroidWrappedUserInfoD2Ev",
  "size": 80,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3a798447537e403e0f3331058f17a37c65f7d3420924ea3aae838f6ef1829a0d",
  "source_text_sha256": "3a798447537e403e0f3331058f17a37c65f7d3420924ea3aae838f6ef1829a0d"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5b080](../00c5b/00c5b080.md)
- [00c5db80](../00c5d/00c5db80.md)

## 疑似コード / UTF-8 398 bytes

~~~c

void _ZN8firebase4auth22AndroidWrappedUserInfoD2Ev(long *param_1)

{
  long *plVar1;
  
  *param_1 = (long)(PTR__ZTVN8firebase4auth22AndroidWrappedUserInfoE_00c9ba60 + 0x10);
  plVar1 = (long *)_ZNK8firebase3App9GetJNIEnvEv(*(undefined8 *)param_1[0x13]);
  (**(code **)(*plVar1 + 0xb0))(plVar1,param_1[0x14]);
  param_1[0x14] = 0;
  _ZN8firebase4auth17UserInfoInterfaceD2Ev(param_1);
  return;
}

~~~
