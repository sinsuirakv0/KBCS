# 00afdae4

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00afdae4",
  "name": "FUN_00afdae4",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "99e42a9d8fdc3e21c809454f09646d059b0b86d8fbd8c7ee484d58b163901f29",
  "source_text_sha256": "99e42a9d8fdc3e21c809454f09646d059b0b86d8fbd8c7ee484d58b163901f29"
}
~~~

## 呼び出し元

- [00700f00](../00700/00700f00.md)
- [007082e8](../00708/007082e8.md)

## 呼び出し先

- [008524fc](../00852/008524fc.md)

## 疑似コード / UTF-8 278 bytes

~~~c

undefined4 FUN_00afdae4(int param_1,int param_2)

{
  long lVar1;
  
  lVar1 = FUN_008524fc();
                    /* catch() { ... } // from try @ 00afc6c8 with catch @ 00afdb10 */
  return *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84bcc);
}

~~~
