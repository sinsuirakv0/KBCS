# 00af5adc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00af5adc",
  "name": "FUN_00af5adc",
  "size": 84,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "bf5c6f45d3f23b425cd13b0dff714383757b85c01177c35587f4fc9f9f95288b",
  "source_text_sha256": "bf5c6f45d3f23b425cd13b0dff714383757b85c01177c35587f4fc9f9f95288b"
}
~~~

## 呼び出し元

- [0070eab4](../0070e/0070eab4.md)
- [00710330](../00710/00710330.md)
- [00711a48](../00711/00711a48.md)

## 呼び出し先

- [00851550](../00851/00851550.md)

## 疑似コード / UTF-8 1020 bytes

~~~c

void FUN_00af5adc(int param_1,int param_2,int param_3)

{
  long lVar1;
  
                    /* catch() { ... } // from try @ 00af596c with catch @ 00af5adc */
  lVar1 = FUN_00851550();
                    /* try { // try from 00af5b08 to 00bf5bc7 has its CatchHandler @ 00af5b08
                       catch() { ... } // from try @ 00af5b08 with catch @ 00af5b08
                       catch() { ... } // from try @ 00af5c28 with catch @ 00af5b08
                       catch() { ... } // from try @ 00af5cd8 with catch @ 00af5b08
                       catch() { ... } // from try @ 00af5d7c with catch @ 00af5b08
                       catch() { ... } // from try @ 00af5f18 with catch @ 00af5b08
                       catch() { ... } // from try @ 00af6048 with catch @ 00af5b08
                       catch() { ... } // from try @ 00af6124 with catch @ 00af5b08 */
  lVar1 = lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec;
  *(int *)(lVar1 + 0x84c68) = *(int *)(lVar1 + 0x84c68) + param_3;
  return;
}

~~~
