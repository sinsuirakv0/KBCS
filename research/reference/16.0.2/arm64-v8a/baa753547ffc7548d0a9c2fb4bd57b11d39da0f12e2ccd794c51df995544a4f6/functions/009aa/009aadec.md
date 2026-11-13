# 009aadec

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "009aadec",
  "name": "FUN_009aadec",
  "size": 8,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5d3be1689cb7692e97e54ce3529037af092f9ceac913006a10f51d442902f0e8",
  "source_text_sha256": "5d3be1689cb7692e97e54ce3529037af092f9ceac913006a10f51d442902f0e8"
}
~~~

## 呼び出し元

- [009b5d94](../009b5/009b5d94.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 113 bytes

~~~c

void FUN_009aadec(long param_1,undefined1 param_2)

{
  *(undefined1 *)(param_1 + 0x35) = param_2;
  return;
}

~~~
