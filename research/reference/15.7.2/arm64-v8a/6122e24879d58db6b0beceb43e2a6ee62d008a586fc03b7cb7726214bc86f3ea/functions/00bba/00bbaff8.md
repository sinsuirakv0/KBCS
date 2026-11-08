# 00bbaff8

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

## 関数情報

~~~json
{
  "address": "00bbaff8",
  "name": "_ZNSt8bad_castD0Ev",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b4bbe4d918b565e77cb003df5f54a414349b271dade725a75222b6de84767d6f",
  "source_text_sha256": "b4bbe4d918b565e77cb003df5f54a414349b271dade725a75222b6de84767d6f"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdaf60](../00bda/00bdaf60.md)
- [00be1390](../00be1/00be1390.md)

## 疑似コード / UTF-8 99 bytes

~~~c

void _ZNSt8bad_castD0Ev(void *param_1)

{
  _ZNSt8bad_castD1Ev();
  _ZdlPv(param_1);
  return;
}

~~~
