# 00bdde4c

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bdde4c",
  "name": "_ZN8firebase4auth4UserD0Ev",
  "size": 56,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "96c5c421be0f76db1429b3273e76fd68a077e6612abd0bc7d18688552c741244",
  "source_text_sha256": "96c5c421be0f76db1429b3273e76fd68a077e6612abd0bc7d18688552c741244"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57ab0](../00c57/00c57ab0.md)
- [00c5d780](../00c5d/00c5d780.md)

## 疑似コード / UTF-8 261 bytes

~~~c

void _ZN8firebase4auth4UserD0Ev(long *param_1)

{
  undefined *puVar1;
  
  puVar1 = PTR__ZTVN8firebase4auth4UserE_00c9b5c0;
  param_1[0x13] = 0;
  *param_1 = (long)(puVar1 + 0x10);
  _ZN8firebase4auth17UserInfoInterfaceD2Ev();
  _ZdlPv(param_1);
  return;
}

~~~
