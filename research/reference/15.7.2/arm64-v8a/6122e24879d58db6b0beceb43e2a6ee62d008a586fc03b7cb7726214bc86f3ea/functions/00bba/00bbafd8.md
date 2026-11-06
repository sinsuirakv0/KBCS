# 00bbafd8

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

## 関数情報

~~~json
{
  "address": "00bbafd8",
  "name": "_ZNSt8bad_castC1Ev",
  "size": 24,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a924d8fa41a617d23a3f4988c13f148765c8f20710ee742d597a07231c8eaf45",
  "source_text_sha256": "a924d8fa41a617d23a3f4988c13f148765c8f20710ee742d597a07231c8eaf45"
}
~~~

## 呼び出し元

- [00be1380](../00be1/00be1380.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 114 bytes

~~~c

void _ZNSt8bad_castC1Ev(long *param_1)

{
  *param_1 = (long)(PTR__ZTVSt8bad_cast_00c1bf38 + 0x10);
  return;
}

~~~
