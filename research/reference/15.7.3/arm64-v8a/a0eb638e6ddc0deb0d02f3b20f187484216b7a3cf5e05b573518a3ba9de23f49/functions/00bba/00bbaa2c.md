# 00bbaa2c

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00bbaa2c",
  "name": "FUN_00bbaa2c",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3c4a59b84a0dec90c688fdb2338a13d3aed80cdc07faf334dbb6d99edda8781b",
  "source_text_sha256": "3c4a59b84a0dec90c688fdb2338a13d3aed80cdc07faf334dbb6d99edda8781b"
}
~~~

## 呼び出し元

- [00bba9a0](../00bba/00bba9a0.md)
- [00bd5144](../00bd5/00bd5144.md)
- [00bd524c](../00bd5/00bd524c.md)
- [00bd5414](../00bd5/00bd5414.md)
- [00bd56c4](../00bd5/00bd56c4.md)
- [00bd5a94](../00bd5/00bd5a94.md)
- [00bd6030](../00bd6/00bd6030.md)
- [00bd63f4](../00bd6/00bd63f4.md)

## 呼び出し先

- [00bbb158](../00bbb/00bbb158.md)

## 関連文字列（未確認候補）

~~~text
"terminate_handler unexpectedly returned"
~~~

## 疑似コード / UTF-8 264 bytes

~~~c

void FUN_00bbaa2c(code *param_1)

{
                    /* catch() { ... } // from try @ 00bb3920 with catch @ 00bbaa30 */
  (*param_1)();
                    /* WARNING: Subroutine does not return */
  FUN_00bbb158("terminate_handler unexpectedly returned");
}

~~~
