# 00afcaa4

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00afcaa4",
  "name": "FUN_00afcaa4",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d2ef84b7ce28af67bcd09b99049ad8adac451d66b7ddd8384bd95cad42ec5374",
  "source_text_sha256": "d2ef84b7ce28af67bcd09b99049ad8adac451d66b7ddd8384bd95cad42ec5374"
}
~~~

## 呼び出し元

- [00700b50](../00700/00700b50.md)
- [00716de8](../00716/00716de8.md)
- [00a4f424](../00a4f/00a4f424.md)

## 呼び出し先

- [00851550](../00851/00851550.md)

## 疑似コード / UTF-8 478 bytes

~~~c

void FUN_00afcaa4(int param_1,int param_2,undefined4 param_3)

{
  long lVar1;
  
  lVar1 = FUN_00851550();
                    /* catch() { ... } // from try @ 00afc094 with catch @ 00afcac8 */
                    /* catch() { ... } // from try @ 00afba7c with catch @ 00afcacc */
  *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84bc8) = param_3;
                    /* catch() { ... } // from try @ 00afba30 with catch @ 00afcae8 */
  return;
}

~~~
