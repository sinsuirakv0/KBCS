# 00afcbc0

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00afcbc0",
  "name": "FUN_00afcbc0",
  "size": 84,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2e312347ecf49bceaa1f9774d8efd58d882304c8f789bfa4fef6ed6124b72c81",
  "source_text_sha256": "2e312347ecf49bceaa1f9774d8efd58d882304c8f789bfa4fef6ed6124b72c81"
}
~~~

## 呼び出し元

- [00716d90](../00716/00716d90.md)

## 呼び出し先

- [008514f8](../00851/008514f8.md)

## 疑似コード / UTF-8 851 bytes

~~~c

void FUN_00afcbc0(int param_1,int param_2,int param_3)

{
  long lVar1;
  
                    /* catch() { ... } // from try @ 00afc460 with catch @ 00afcbd4
                       catch() { ... } // from try @ 00afc544 with catch @ 00afcbd4 */
  lVar1 = FUN_008514f8();
                    /* catch() { ... } // from try @ 00afc278 with catch @ 00afcbe4 */
  lVar1 = lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec;
                    /* catch() { ... } // from try @ 00afc234 with catch @ 00afcbfc
                       catch() { ... } // from try @ 00afc328 with catch @ 00afcbfc */
  *(int *)(lVar1 + 0x84bd4) = *(int *)(lVar1 + 0x84bd4) + param_3;
                    /* catch() { ... } // from try @ 00afbc28 with catch @ 00afcc0c */
                    /* catch() { ... } // from try @ 00afb8b0 with catch @ 00afcc10 */
  return;
}

~~~
