# 00afdab0

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00afdab0",
  "name": "FUN_00afdab0",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "935eb19f48c32a6e4fd0c1dc50dd5b3bb55f800e28048fc39d27bd75d7e61948",
  "source_text_sha256": "935eb19f48c32a6e4fd0c1dc50dd5b3bb55f800e28048fc39d27bd75d7e61948"
}
~~~

## 呼び出し元

- [007154c0](../00715/007154c0.md)

## 呼び出し先

- [008514b8](../00851/008514b8.md)

## 疑似コード / UTF-8 191 bytes

~~~c

undefined4 FUN_00afdab0(int param_1,int param_2)

{
  long lVar1;
  
  lVar1 = FUN_008514b8();
  return *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84c7c);
}

~~~
