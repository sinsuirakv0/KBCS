# 00afcaf0

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00afcaf0",
  "name": "FUN_00afcaf0",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "eb425c186296bba233bb1033e2f5ade9d8cc12c0b398a4660c2182dc759d2a59",
  "source_text_sha256": "eb425c186296bba233bb1033e2f5ade9d8cc12c0b398a4660c2182dc759d2a59"
}
~~~

## 呼び出し元

- [00700b50](../00700/00700b50.md)
- [00707f38](../00707/00707f38.md)

## 呼び出し先

- [00851550](../00851/00851550.md)

## 疑似コード / UTF-8 365 bytes

~~~c

undefined4 FUN_00afcaf0(int param_1,int param_2)

{
  long lVar1;
  
  lVar1 = FUN_00851550();
                    /* catch() { ... } // from try @ 00afb854 with catch @ 00afcb20 */
                    /* catch() { ... } // from try @ 00afb744 with catch @ 00afcb28 */
  return *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84bcc);
}

~~~
