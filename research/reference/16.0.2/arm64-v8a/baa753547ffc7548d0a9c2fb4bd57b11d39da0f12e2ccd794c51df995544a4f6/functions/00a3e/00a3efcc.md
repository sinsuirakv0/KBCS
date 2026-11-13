# 00a3efcc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00a3efcc",
  "name": "FUN_00a3efcc",
  "size": 48,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c9d77ba0f99f80804e90d1d88865340cc2e85c68cc8e02c4b383142dbd568e7b",
  "source_text_sha256": "c9d77ba0f99f80804e90d1d88865340cc2e85c68cc8e02c4b383142dbd568e7b"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [005c17dc](../005c1/005c17dc.md)

## 疑似コード / UTF-8 177 bytes

~~~c

void FUN_00a3efcc(long param_1)

{
  FUN_005c17dc(param_1 + 0x28,*(undefined8 *)(param_1 + 0x30));
  FUN_005c17dc(param_1 + 0x10,*(undefined8 *)(param_1 + 0x18));
  return;
}

~~~
