# 00af6eac

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00af6eac",
  "name": "FUN_00af6eac",
  "size": 72,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "bbe168a32f99fa8d4cf3caea128ac93f7e9871227b125a970da60f5e386bb30e",
  "source_text_sha256": "bbe168a32f99fa8d4cf3caea128ac93f7e9871227b125a970da60f5e386bb30e"
}
~~~

## 呼び出し元

- [0070ea1c](../0070e/0070ea1c.md)
- [007119b0](../00711/007119b0.md)

## 呼び出し先

- [008514b8](../00851/008514b8.md)

## 疑似コード / UTF-8 280 bytes

~~~c

bool FUN_00af6eac(int param_1,int param_2)

{
  long lVar1;
  
                    /* try { // try from 00af6ebc to 00bf6f07 has its CatchHandler @ 00af728c */
  lVar1 = FUN_008514b8();
  return *(int *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84c98) != 0;
}

~~~
