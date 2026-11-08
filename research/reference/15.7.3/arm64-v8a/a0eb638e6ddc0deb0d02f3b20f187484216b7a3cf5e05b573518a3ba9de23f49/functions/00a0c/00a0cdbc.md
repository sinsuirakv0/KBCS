# 00a0cdbc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00a0cdbc",
  "name": "FUN_00a0cdbc",
  "size": 36,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "97c3bedd2ceb5fd60cd3c0667f584bd026556dd77f01fc045ba48b6591157948",
  "source_text_sha256": "97c3bedd2ceb5fd60cd3c0667f584bd026556dd77f01fc045ba48b6591157948"
}
~~~

## 呼び出し元

- [006d6d04](../006d6/006d6d04.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 224 bytes

~~~c

void FUN_00a0cdbc(long param_1)

{
  if ((*(int *)(param_1 + 0x84) != -1) && (*(int *)(param_1 + 0x84) <= *(int *)(param_1 + 0x80))) {
    return;
  }
  *(int *)(param_1 + 0x80) = *(int *)(param_1 + 0x80) + 1;
  return;
}

~~~
