# 00bd4fcc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-previous -->
**別版の対応** [v15.7.2 `00bd4ec0`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd4/00bd4ec0.md)
<!-- /kbcs-version-previous -->

## 関数情報

~~~json
{
  "address": "00bd4fcc",
  "name": "_ZdaPvmSt11align_val_t",
  "size": 12,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "223824c7e299f2f9ee425f6c228d17159ef2bae892ebd2ccd1a88475b138d5ce",
  "source_text_sha256": "223824c7e299f2f9ee425f6c228d17159ef2bae892ebd2ccd1a88475b138d5ce"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00be1f40](../00be1/00be1f40.md)

## 疑似コード / UTF-8 94 bytes

~~~c

void _ZdaPvmSt11align_val_t(void *param_1)

{
  _ZdaPvSt11align_val_t(param_1);
  return;
}

~~~
