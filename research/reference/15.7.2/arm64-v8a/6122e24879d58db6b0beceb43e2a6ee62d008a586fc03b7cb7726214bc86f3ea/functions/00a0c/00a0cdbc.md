# 00a0cdbc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

<!-- kbcs-version-next -->
**別版の対応** [v15.7.4 `00a0ce00`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0c/00a0ce00.md)
<!-- /kbcs-version-next -->

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
