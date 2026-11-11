# 00bde2ac

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00bde2ac",
  "name": "_ZNK8firebase4auth4User8is_validEv",
  "size": 32,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6fd6b615520bf22e6337b7f1c1f35d308921f20a39fcc03aeabadc0b2a6b79f0",
  "source_text_sha256": "6fd6b615520bf22e6337b7f1c1f35d308921f20a39fcc03aeabadc0b2a6b79f0"
}
~~~

## 呼び出し元

- [00c5aa60](../00c5a/00c5aa60.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 183 bytes

~~~c

bool _ZNK8firebase4auth4User8is_validEv(long param_1)

{
  if (*(long *)(param_1 + 0x98) != 0) {
    return *(long *)(*(long *)(param_1 + 0x98) + 0x200) != 0;
  }
  return false;
}

~~~
