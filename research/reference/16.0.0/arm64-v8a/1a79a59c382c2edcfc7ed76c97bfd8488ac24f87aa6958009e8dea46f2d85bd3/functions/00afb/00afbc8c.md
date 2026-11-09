# 00afbc8c

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00afbc8c",
  "name": "FUN_00afbc8c",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0822bb1338d6e3fbe506c20996e92079bcb5c8b424dda3b048a857fbb3eebce6",
  "source_text_sha256": "0822bb1338d6e3fbe506c20996e92079bcb5c8b424dda3b048a857fbb3eebce6"
}
~~~

## 呼び出し元

- [00700ab8](../00700/00700ab8.md)
- [00710298](../00710/00710298.md)
- [00a4f1bc](../00a4f/00a4f1bc.md)

## 呼び出し先

- [008514b8](../00851/008514b8.md)

## 疑似コード / UTF-8 217 bytes

~~~c

void FUN_00afbc8c(int param_1,int param_2,undefined4 param_3)

{
  long lVar1;
  
  lVar1 = FUN_008514b8();
  *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84b20) = param_3;
  return;
}

~~~
