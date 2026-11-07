# 007caebc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

<!-- kbcs-version-next -->
**別版の対応** [v15.7.4 `007caebc`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ca/007caebc.md)
<!-- /kbcs-version-next -->

## 関数情報

~~~json
{
  "address": "007caebc",
  "name": "_ZdlPv",
  "size": 4,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2cf035e6feb95c70c1e1c797f93a935f9b2bdbb362d9ea51580474e7aba94ec1",
  "source_text_sha256": "2cf035e6feb95c70c1e1c797f93a935f9b2bdbb362d9ea51580474e7aba94ec1"
}
~~~

## 呼び出し元

- [0079bdf0](../0079b/0079bdf0.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 253 bytes

~~~c

/* WARNING: Unknown calling convention -- yet parameter storage is locked */

void _ZdlPv(void *__ptr)

{
                    /* try { // try from 007caebc to 008caec7 has its CatchHandler @ 007ce094 */
  (*(code *)PTR__ZdlPv_00c1bfe8)();
  return;
}

~~~
