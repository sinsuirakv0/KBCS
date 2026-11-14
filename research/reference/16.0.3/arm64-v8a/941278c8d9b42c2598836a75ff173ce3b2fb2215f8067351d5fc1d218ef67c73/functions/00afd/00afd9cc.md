# 00afd9cc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00afd9cc",
  "name": "FUN_00afd9cc",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "35fce9dec7b087bd76aa69d27127f53acd5763f854ac64e7b46576510d59aaf4",
  "source_text_sha256": "35fce9dec7b087bd76aa69d27127f53acd5763f854ac64e7b46576510d59aaf4"
}
~~~

## 呼び出し元

- [00700f00](../00700/00700f00.md)

## 呼び出し先

- [008524fc](../00852/008524fc.md)

## 疑似コード / UTF-8 452 bytes

~~~c

undefined4 FUN_00afd9cc(int param_1,int param_2)

{
  long lVar1;
  
                    /* catch() { ... } // from try @ 00afc528 with catch @ 00afd9d8 */
  lVar1 = FUN_008524fc();
                    /* catch() { ... } // from try @ 00afd6f8 with catch @ 00afd9f0 */
                    /* catch() { ... } // from try @ 00afd56c with catch @ 00afd9f4 */
  return *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84bc4);
}

~~~
