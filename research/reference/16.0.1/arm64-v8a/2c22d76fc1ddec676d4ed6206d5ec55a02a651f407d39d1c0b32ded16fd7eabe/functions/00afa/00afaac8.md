# 00afaac8

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00afaac8",
  "name": "FUN_00afaac8",
  "size": 72,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a6c21cb668c2a71ffc69098409a9a955156d34c9c33575451003af9c5bb8ea3c",
  "source_text_sha256": "a6c21cb668c2a71ffc69098409a9a955156d34c9c33575451003af9c5bb8ea3c"
}
~~~

## 呼び出し元

- [005f7940](../005f7/005f7940.md)
- [005fb93c](../005fb/005fb93c.md)
- [00714be8](../00714/00714be8.md)
- [00714db8](../00714/00714db8.md)

## 呼び出し先

- [008514f8](../00851/008514f8.md)

## 疑似コード / UTF-8 1047 bytes

~~~c

bool FUN_00afaac8(int param_1,int param_2)

{
  long lVar1;
  
                    /* catch() { ... } // from try @ 00afa068 with catch @ 00afaac8 */
                    /* catch() { ... } // from try @ 00afa058 with catch @ 00afaacc */
                    /* catch() { ... } // from try @ 00af9fe4 with catch @ 00afaad0 */
  lVar1 = FUN_008514f8();
                    /* catch() { ... } // from try @ 00af9fd4 with catch @ 00afaae8 */
                    /* catch() { ... } // from try @ 00afa5f4 with catch @ 00afab00 */
                    /* catch() { ... } // from try @ 00afa5c4 with catch @ 00afab04
                       catch() { ... } // from try @ 00afa690 with catch @ 00afab04 */
                    /* catch() { ... } // from try @ 00afa3e8 with catch @ 00afab08 */
                    /* catch() { ... } // from try @ 00afa3b8 with catch @ 00afab0c
                       catch() { ... } // from try @ 00afa494 with catch @ 00afab0c */
  return *(int *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84a24) != 0;
}

~~~
