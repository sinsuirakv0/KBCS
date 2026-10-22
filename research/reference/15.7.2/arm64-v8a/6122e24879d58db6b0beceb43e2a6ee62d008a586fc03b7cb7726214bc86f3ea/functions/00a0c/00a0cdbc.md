# 00a0cdbc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00a0cdbc.md)

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
  "source_sha256": "a95917a63f1773308e91e67f36a6c1b93e648df555bed393f3cf9cedfa587542",
  "source_text_sha256": "a95917a63f1773308e91e67f36a6c1b93e648df555bed393f3cf9cedfa587542"
}
~~~
## 呼び出し元

- [006d6d04](../006d6/006d6d04.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード 1/1 / UTF-8 235 bytes

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
