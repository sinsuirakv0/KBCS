# 008cabac

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "008cabac",
  "name": "FUN_008cabac",
  "size": 8,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0d26265f795efabc50941ce4e297af72b560cd4bf1f29b963031f9e49b38af9f",
  "source_text_sha256": "0d26265f795efabc50941ce4e297af72b560cd4bf1f29b963031f9e49b38af9f"
}
~~~

## 呼び出し元

- [005fa824](../005fa/005fa824.md)
- [005fafd4](../005fa/005fafd4.md)
- [00a47f00](../00a47/00a47f00.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 87 bytes

~~~c

undefined1 FUN_008cabac(long param_1)

{
  return *(undefined1 *)(param_1 + 0x34);
}

~~~
