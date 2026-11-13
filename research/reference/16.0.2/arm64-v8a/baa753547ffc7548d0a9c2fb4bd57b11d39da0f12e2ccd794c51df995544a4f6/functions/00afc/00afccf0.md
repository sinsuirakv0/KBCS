# 00afccf0

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00afccf0",
  "name": "FUN_00afccf0",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "dfc2f0c53ac448dd398c0ab8d94a4e0b5ec0e557a788ff04fef220ec67ea1803",
  "source_text_sha256": "dfc2f0c53ac448dd398c0ab8d94a4e0b5ec0e557a788ff04fef220ec67ea1803"
}
~~~

## 呼び出し元

- [00711a48](../00711/00711a48.md)
- [00a4f424](../00a4f/00a4f424.md)

## 呼び出し先

- [00851550](../00851/00851550.md)

## 疑似コード / UTF-8 304 bytes

~~~c

void FUN_00afccf0(int param_1,int param_2,undefined4 param_3)

{
  long lVar1;
  
                    /* catch() { ... } // from try @ 00afbc00 with catch @ 00afcd04 */
  lVar1 = FUN_00851550();
  *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84c10) = param_3;
  return;
}

~~~
