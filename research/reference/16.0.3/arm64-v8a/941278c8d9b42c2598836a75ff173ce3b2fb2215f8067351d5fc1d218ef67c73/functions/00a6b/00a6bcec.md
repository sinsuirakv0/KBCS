# 00a6bcec

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00a6bcec",
  "name": "FUN_00a6bcec",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4bc46716577d193d5063bd91db9e8c48501836817532556a5727b260ea017c35",
  "source_text_sha256": "4bc46716577d193d5063bd91db9e8c48501836817532556a5727b260ea017c35"
}
~~~

## 呼び出し元

- [00700f00](../00700/00700f00.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 232 bytes

~~~c

bool FUN_00a6bcec(long param_1)

{
                    /* try { // try from 00a6bcec to 00b6bd2f has its CatchHandler @ 00a64fd8 */
  return *(int *)(param_1 + 0x84) != 0 && *(int *)(param_1 + 0x84) <= *(int *)(param_1 + 0x80);
}

~~~
