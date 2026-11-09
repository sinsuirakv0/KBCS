# 00ac0dfc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00ac0dfc",
  "name": "FUN_00ac0dfc",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f5d2cc26617392e7281645c8455987402a3b300ad4bd7aaaf38be97358b6a82c",
  "source_text_sha256": "f5d2cc26617392e7281645c8455987402a3b300ad4bd7aaaf38be97358b6a82c"
}
~~~

## 呼び出し元

- [00abd6f0](../00abd/00abd6f0.md)

## 呼び出し先

- [0043b738](../0043b/0043b738.md)

## 関連文字列（未確認候補）

~~~text
"vector"
~~~

## 疑似コード / UTF-8 216 bytes

~~~c

void FUN_00ac0dfc(void)

{
                    /* try { // try from 00ac0dfc to 00bc0e47 has its CatchHandler @ 00ac0d64 */
                    /* WARNING: Subroutine does not return */
  FUN_0043b738("vector");
}

~~~
