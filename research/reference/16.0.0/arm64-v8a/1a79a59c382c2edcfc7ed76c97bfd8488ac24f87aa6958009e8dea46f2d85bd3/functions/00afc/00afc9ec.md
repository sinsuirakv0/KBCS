# 00afc9ec

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00afc9ec",
  "name": "FUN_00afc9ec",
  "size": 84,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "26e1a7652d72235f75318227b7fd661a4596155383bcb5580f50e530cd8ef7de",
  "source_text_sha256": "26e1a7652d72235f75318227b7fd661a4596155383bcb5580f50e530cd8ef7de"
}
~~~

## 呼び出し元

- [005f2d28](../005f2/005f2d28.md)

## 呼び出し先

- [008514b8](../00851/008514b8.md)

## 疑似コード / UTF-8 1109 bytes

~~~c

void FUN_00afc9ec(int param_1,int param_2,int param_3)

{
  long lVar1;
  
  lVar1 = FUN_008514b8();
                    /* catch() { ... } // from try @ 00afbec8 with catch @ 00afca0c */
                    /* catch() { ... } // from try @ 00afbe98 with catch @ 00afca10
                       catch() { ... } // from try @ 00afbf74 with catch @ 00afca10 */
                    /* catch() { ... } // from try @ 00afbd54 with catch @ 00afca14 */
                    /* catch() { ... } // from try @ 00afc580 with catch @ 00afca18 */
  lVar1 = lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec;
                    /* catch() { ... } // from try @ 00afc544 with catch @ 00afca1c
                       catch() { ... } // from try @ 00afc628 with catch @ 00afca1c */
                    /* catch() { ... } // from try @ 00afc300 with catch @ 00afca20 */
  *(int *)(lVar1 + 0x84c70) = *(int *)(lVar1 + 0x84c70) + param_3;
                    /* catch() { ... } // from try @ 00afc2c4 with catch @ 00afca38
                       catch() { ... } // from try @ 00afc3a8 with catch @ 00afca38 */
  return;
}

~~~
