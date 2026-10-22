# 009dcecc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](009dcecc.md)

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
  "source_sha256": "c6ed3cb1627a37726b316df6c594569cf5f5aaf785ba59e0bfea834b919dedee",
  "source_text_sha256": "c6ed3cb1627a37726b316df6c594569cf5f5aaf785ba59e0bfea834b919dedee"
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
## 疑似コード 1/1 / UTF-8 215 bytes

~~~c

void FUN_009dcecc(void)

{
                    /* WARNING: Subroutine does not return */
                    /* catch() { ... } // from try @ 009d9d58 with catch @ 009dcedc */
  FUN_00418c38("vector");
}

~~~
