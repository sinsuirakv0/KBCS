# 00afccb0

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00afccb0",
  "name": "FUN_00afccb0",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "846d46f2ab4594e647ae3f4a244cdbead4d62f941db83ae00ba09e4650d6dfc4",
  "source_text_sha256": "846d46f2ab4594e647ae3f4a244cdbead4d62f941db83ae00ba09e4650d6dfc4"
}
~~~

## 呼び出し元

- [005f2da8](../005f2/005f2da8.md)
- [00707f38](../00707/00707f38.md)
- [00711a48](../00711/00711a48.md)

## 呼び出し先

- [00851550](../00851/00851550.md)

## 疑似コード / UTF-8 452 bytes

~~~c

undefined4 FUN_00afccb0(int param_1,int param_2)

{
  long lVar1;
  
                    /* catch() { ... } // from try @ 00afc99c with catch @ 00afccb4 */
  lVar1 = FUN_00851550();
                    /* catch() { ... } // from try @ 00afbec8 with catch @ 00afcccc */
                    /* catch() { ... } // from try @ 00afc968 with catch @ 00afccec */
  return *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84c10);
}

~~~
