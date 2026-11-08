# 00bdacd8

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00bdacd8",
  "name": "FUN_00bdacd8",
  "size": 48,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c895b00262d6911d0d5a31a0ec7a2a7d69af6efb6c92338267a1c278f7db5e8b",
  "source_text_sha256": "c895b00262d6911d0d5a31a0ec7a2a7d69af6efb6c92338267a1c278f7db5e8b"
}
~~~

## 呼び出し元

- [00bd7ff4](../00bd7/00bd7ff4.md)

## 呼び出し先

解決済みの記録なし。

## 関連文字列（未確認候補）

~~~text
"unknown register"
~~~

## 疑似コード / UTF-8 279 bytes

~~~c

char * FUN_00bdacd8(int param_1)

{
  if (param_1 + 2U < 0x62) {
                    /* try { // try from 00bdacf0 to 00cdad27 has its CatchHandler @ 00bdad58 */
    return &DAT_002fe11c + *(int *)(&DAT_002fe11c + (ulong)(param_1 + 2U) * 4);
  }
  return "unknown register";
}

~~~
