# 005cfcbc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "005cfcbc",
  "name": "FUN_005cfcbc",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "aa079ad4230c72a53c8731464e5d1774b78447b212e75e792e716dd69314442d",
  "source_text_sha256": "aa079ad4230c72a53c8731464e5d1774b78447b212e75e792e716dd69314442d"
}
~~~

## 呼び出し元

- [005cfaf4](../005cf/005cfaf4.md)
- [005cfd60](../005cf/005cfd60.md)
- [005d0344](../005d0/005d0344.md)
- [005d804c](../005d8/005d804c.md)

## 呼び出し先

- [0043b738](../0043b/0043b738.md)

## 関連文字列（未確認候補）

~~~text
"vector"
~~~

## 疑似コード / UTF-8 119 bytes

~~~c

void FUN_005cfcbc(void)

{
                    /* WARNING: Subroutine does not return */
  FUN_0043b738("vector");
}

~~~
