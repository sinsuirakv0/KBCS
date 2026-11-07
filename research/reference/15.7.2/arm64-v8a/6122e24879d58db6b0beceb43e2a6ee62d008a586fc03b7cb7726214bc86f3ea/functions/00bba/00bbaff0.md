# 00bbaff0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

<!-- kbcs-version-next -->
**別版の対応** [v15.7.4 `00bbb0fc`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb0fc.md)
<!-- /kbcs-version-next -->

## 関数情報

~~~json
{
  "address": "00bbaff0",
  "name": "_ZNSt8bad_castD1Ev",
  "size": 8,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "90aefd0e796e8803278559c7823991a0e3f222bd5807330272b7699e80813997",
  "source_text_sha256": "90aefd0e796e8803278559c7823991a0e3f222bd5807330272b7699e80813997"
}
~~~

## 呼び出し元

- [00be1390](../00be1/00be1390.md)

## 呼び出し先

- [00bdb390](../00bdb/00bdb390.md)

## 疑似コード / UTF-8 84 bytes

~~~c

void _ZNSt8bad_castD1Ev(void)

{
  _ZNSt20bad_array_new_lengthD1Ev();
  return;
}

~~~
