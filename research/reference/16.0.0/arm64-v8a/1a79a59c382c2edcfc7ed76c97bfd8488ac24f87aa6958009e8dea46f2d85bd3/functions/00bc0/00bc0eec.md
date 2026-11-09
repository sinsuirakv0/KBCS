# 00bc0eec

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bc0eec",
  "name": "_INIT_287",
  "size": 48,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "aaa99cbe98d3db842b74fee27c340d156e2491a7111eab2812850f24732a6350",
  "source_text_sha256": "aaa99cbe98d3db842b74fee27c340d156e2491a7111eab2812850f24732a6350"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5a7c0](../00c5a/00c5a7c0.md)

## 関連文字列（未確認候補）

~~~text
"remote_config"
~~~

## 疑似コード / UTF-8 203 bytes

~~~c

void _INIT_287(void)

{
  DAT_01126010 = "remote_config";
  DAT_01126018 = FUN_00bc0e44;
  DAT_01126020 = FUN_00bc0e4c;
  DAT_01126028 = 0;
  _ZN8firebase11AppCallback11AddCallbackEPS0_();
  return;
}

~~~
