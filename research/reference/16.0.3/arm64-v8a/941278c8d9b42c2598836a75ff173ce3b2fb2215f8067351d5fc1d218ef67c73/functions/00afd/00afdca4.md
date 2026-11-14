# 00afdca4

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00afdca4",
  "name": "FUN_00afdca4",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "390434cacd891e1fe780321d22ca7a48d3efb97316efad2607b4b27e38a44dc1",
  "source_text_sha256": "390434cacd891e1fe780321d22ca7a48d3efb97316efad2607b4b27e38a44dc1"
}
~~~

## 呼び出し元

- [005f3158](../005f3/005f3158.md)
- [007082e8](../00708/007082e8.md)
- [00711df8](../00711/00711df8.md)

## 呼び出し先

- [008524fc](../00852/008524fc.md)

## 疑似コード / UTF-8 278 bytes

~~~c

undefined4 FUN_00afdca4(int param_1,int param_2)

{
  long lVar1;
  
                    /* catch() { ... } // from try @ 00afcbac with catch @ 00afdcb0 */
  lVar1 = FUN_008524fc();
  return *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84c10);
}

~~~
