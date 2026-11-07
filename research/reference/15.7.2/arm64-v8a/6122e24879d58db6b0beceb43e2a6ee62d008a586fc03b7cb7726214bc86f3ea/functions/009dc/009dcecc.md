# 009dcecc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

<!-- kbcs-version-next -->
**別版の対応** [v15.7.4 `009dcf10`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009dc/009dcf10.md)
<!-- /kbcs-version-next -->

## 関数情報

~~~json
{
  "address": "009dcecc",
  "name": "FUN_009dcecc",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "aecd03fc9fc09a1bbfd1d7270baee75e9de85b1c79f3e5cf02c9b89f59167f3d",
  "source_text_sha256": "aecd03fc9fc09a1bbfd1d7270baee75e9de85b1c79f3e5cf02c9b89f59167f3d"
}
~~~

## 呼び出し元

- [009dcca0](../009dc/009dcca0.md)

## 呼び出し先

- [00418c38](../00418/00418c38.md)

## 関連文字列（未確認候補）

~~~text
"vector"
~~~

## 疑似コード / UTF-8 206 bytes

~~~c

void FUN_009dcecc(void)

{
                    /* WARNING: Subroutine does not return */
                    /* catch() { ... } // from try @ 009d9d58 with catch @ 009dcedc */
  FUN_00418c38("vector");
}

~~~
