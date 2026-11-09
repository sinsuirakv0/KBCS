# 009abeac

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "009abeac",
  "name": "FUN_009abeac",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1102df87fce6b4c4c1f787cae99f84d9ac237d6646562d9fd3d136775c3131a8",
  "source_text_sha256": "1102df87fce6b4c4c1f787cae99f84d9ac237d6646562d9fd3d136775c3131a8"
}
~~~

## 呼び出し元

- [009abb24](../009ab/009abb24.md)
- [009ac11c](../009ac/009ac11c.md)

## 呼び出し先

- [0043b738](../0043b/0043b738.md)

## 関連文字列（未確認候補）

~~~text
"vector"
~~~

## 疑似コード / UTF-8 216 bytes

~~~c

void FUN_009abeac(void)

{
                    /* try { // try from 009abeb0 to 00aabecb has its CatchHandler @ 009abcb4 */
                    /* WARNING: Subroutine does not return */
  FUN_0043b738("vector");
}

~~~
