# 00bbada4

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-previous -->
**別版の対応** [v15.7.2 `00bbac98`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bbac98.md)
<!-- /kbcs-version-previous -->

## 関数情報

~~~json
{
  "address": "00bbada4",
  "name": "_ZNKSt13bad_exception4whatEv",
  "size": 16,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8dd61e146edab738f57ac0bf3b288b75ad6c371a37c804dd9012da334d12e066",
  "source_text_sha256": "8dd61e146edab738f57ac0bf3b288b75ad6c371a37c804dd9012da334d12e066"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 関連文字列（未確認候補）

~~~text
"std::bad_exception"
~~~

## 疑似コード / UTF-8 341 bytes

~~~c

char * _ZNKSt13bad_exception4whatEv(void)

{
                    /* catch() { ... } // from try @ 00bb59f0 with catch @ 00bbada8 */
                    /* catch() { ... } // from try @ 00bb5278 with catch @ 00bbadac */
                    /* catch() { ... } // from try @ 00bb4e98 with catch @ 00bbadb0 */
  return "std::bad_exception";
}

~~~
