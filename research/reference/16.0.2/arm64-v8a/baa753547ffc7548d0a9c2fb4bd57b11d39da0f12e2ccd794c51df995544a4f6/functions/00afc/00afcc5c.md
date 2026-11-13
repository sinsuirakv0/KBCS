# 00afcc5c

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00afcc5c",
  "name": "FUN_00afcc5c",
  "size": 84,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "79b4f88ca520d9ad3c6438831947288f3dd3cf7493751a0c3cf8ed396860dc2d",
  "source_text_sha256": "79b4f88ca520d9ad3c6438831947288f3dd3cf7493751a0c3cf8ed396860dc2d"
}
~~~

## 呼び出し元

- [00716de8](../00716/00716de8.md)

## 呼び出し先

- [00851550](../00851/00851550.md)

## 疑似コード / UTF-8 422 bytes

~~~c

void FUN_00afcc5c(int param_1,int param_2,int param_3)

{
  long lVar1;
  
                    /* catch() { ... } // from try @ 00afbc7c with catch @ 00afcc60 */
                    /* catch() { ... } // from try @ 00afb904 with catch @ 00afcc64 */
  lVar1 = FUN_00851550();
  lVar1 = lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec;
  *(int *)(lVar1 + 0x84bd4) = *(int *)(lVar1 + 0x84bd4) + param_3;
  return;
}

~~~
