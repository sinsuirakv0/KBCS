# 00afcb7c

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00afcb7c",
  "name": "FUN_00afcb7c",
  "size": 84,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1d7bd2d697ddc1ead15244967db44c98d986d5bf3d39f7fcb9c0b4d0fc6997a0",
  "source_text_sha256": "1d7bd2d697ddc1ead15244967db44c98d986d5bf3d39f7fcb9c0b4d0fc6997a0"
}
~~~

## 呼び出し元

- [00700b50](../00700/00700b50.md)

## 呼び出し先

- [00851550](../00851/00851550.md)

## 疑似コード / UTF-8 509 bytes

~~~c

void FUN_00afcb7c(int param_1,int param_2,int param_3)

{
  long lVar1;
  
                    /* catch() { ... } // from try @ 00afb6f0 with catch @ 00afcb84 */
  lVar1 = FUN_00851550();
                    /* catch() { ... } // from try @ 00afb6e4 with catch @ 00afcba4 */
  lVar1 = lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec;
                    /* catch() { ... } // from try @ 00afc848 with catch @ 00afcbbc */
  *(int *)(lVar1 + 0x84bcc) = *(int *)(lVar1 + 0x84bcc) + param_3;
  return;
}

~~~
