# 00afcbd0

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00afcbd0",
  "name": "FUN_00afcbd0",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d61106c17658076a3c8011997a5fc222274b3e324a214d5af3a94e29186e966c",
  "source_text_sha256": "d61106c17658076a3c8011997a5fc222274b3e324a214d5af3a94e29186e966c"
}
~~~

## 呼び出し元

- [00707f38](../00707/00707f38.md)
- [00716de8](../00716/00716de8.md)

## 呼び出し先

- [00851550](../00851/00851550.md)

## 疑似コード / UTF-8 794 bytes

~~~c

undefined4 FUN_00afcbd0(int param_1,int param_2)

{
  long lVar1;
  
  lVar1 = FUN_00851550();
                    /* catch() { ... } // from try @ 00afc0b8 with catch @ 00afcbfc */
                    /* catch() { ... } // from try @ 00afc088 with catch @ 00afcc00
                       catch() { ... } // from try @ 00afc164 with catch @ 00afcc00 */
                    /* catch() { ... } // from try @ 00afbf44 with catch @ 00afcc04 */
                    /* catch() { ... } // from try @ 00afc770 with catch @ 00afcc08 */
                    /* catch() { ... } // from try @ 00afc734 with catch @ 00afcc0c
                       catch() { ... } // from try @ 00afc818 with catch @ 00afcc0c */
  return *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84bd4);
}

~~~
