# 00afc7ec

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00afc7ec",
  "name": "FUN_00afc7ec",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0810037677beb4a322731ed2b71cc63818d02a7fd16ed37f412249780867df83",
  "source_text_sha256": "0810037677beb4a322731ed2b71cc63818d02a7fd16ed37f412249780867df83"
}
~~~

## 呼び出し元

- [005f2d28](../005f2/005f2d28.md)
- [00707ea0](../00707/00707ea0.md)
- [007119b0](../00711/007119b0.md)

## 呼び出し先

- [008514b8](../00851/008514b8.md)

## 疑似コード / UTF-8 365 bytes

~~~c

undefined4 FUN_00afc7ec(int param_1,int param_2)

{
  long lVar1;
  
  lVar1 = FUN_008514b8();
                    /* catch() { ... } // from try @ 00afb5c4 with catch @ 00afc81c */
                    /* catch() { ... } // from try @ 00afb39c with catch @ 00afc824 */
  return *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84c10);
}

~~~
