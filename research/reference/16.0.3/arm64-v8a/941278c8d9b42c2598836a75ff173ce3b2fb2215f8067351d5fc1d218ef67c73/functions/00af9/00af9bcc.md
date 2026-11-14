# 00af9bcc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00af9bcc",
  "name": "FUN_00af9bcc",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d3c2bec73b8a74b421edc088ae6c667b32c3ca0b1adbfff207c5d4c2a981abfe",
  "source_text_sha256": "d3c2bec73b8a74b421edc088ae6c667b32c3ca0b1adbfff207c5d4c2a981abfe"
}
~~~

## 呼び出し元

- [00a50418](../00a50/00a50418.md)

## 呼び出し先

- [008524fc](../00852/008524fc.md)

## 疑似コード / UTF-8 907 bytes

~~~c

void FUN_00af9bcc(int param_1,int param_2,undefined4 param_3)

{
  long lVar1;
  
                    /* catch() { ... } // from try @ 00af98c4 with catch @ 00af9bcc
                       catch() { ... } // from try @ 00af9b9c with catch @ 00af9bcc */
                    /* catch() { ... } // from try @ 00af9888 with catch @ 00af9be4
                       catch() { ... } // from try @ 00af9b80 with catch @ 00af9be4 */
  lVar1 = FUN_008524fc();
                    /* catch() { ... } // from try @ 00af9764 with catch @ 00af9c00 */
  *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84c1c) = param_3;
                    /* catch() { ... } // from try @ 00af975c with catch @ 00af9c08 */
                    /* catch() { ... } // from try @ 00af96f0 with catch @ 00af9c10 */
                    /* catch() { ... } // from try @ 00af9680 with catch @ 00af9c14 */
  return;
}

~~~
