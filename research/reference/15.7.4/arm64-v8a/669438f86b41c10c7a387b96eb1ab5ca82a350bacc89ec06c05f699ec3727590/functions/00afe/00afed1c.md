# 00afed1c

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-previous -->
**別版の対応** [v15.7.2 `00afec10`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afe/00afec10.md)
<!-- /kbcs-version-previous -->

## 関数情報

~~~json
{
  "address": "00afed1c",
  "name": "_ZN8firebase26ReferenceCountedFutureImplD0Ev",
  "size": 36,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a9ad010502a1a246bb61a9dca977afaf76f1e1f31c463b98debf1a03cd224ada",
  "source_text_sha256": "a9ad010502a1a246bb61a9dca977afaf76f1e1f31c463b98debf1a03cd224ada"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb060](../00bdb/00bdb060.md)
- [00bdee20](../00bde/00bdee20.md)

## 疑似コード / UTF-8 325 bytes

~~~c

void _ZN8firebase26ReferenceCountedFutureImplD0Ev(void *param_1)

{
                    /* catch() { ... } // from try @ 00afdb74 with catch @ 00afed1c */
                    /* catch() { ... } // from try @ 00af6ff4 with catch @ 00afed20 */
  _ZN8firebase26ReferenceCountedFutureImplD1Ev();
  _ZdlPv(param_1);
  return;
}

~~~
