# 00bfbcdc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bfbcdc",
  "name": "FUN_00bfbcdc",
  "size": 24,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "cac778f7bf7fa3005b4d3d16fd22d4e86fcb8d4aae853baead6eaaccbefc10f3",
  "source_text_sha256": "cac778f7bf7fa3005b4d3d16fd22d4e86fcb8d4aae853baead6eaaccbefc10f3"
}
~~~

## 呼び出し元

- [00bfba58](../00bfb/00bfba58.md)

## 呼び出し先

- [0043bad8](../0043b/0043bad8.md)

## 関連文字列（未確認候補）

~~~text
"vector"
~~~

## 疑似コード / UTF-8 119 bytes

~~~c

void FUN_00bfbcdc(void)

{
                    /* WARNING: Subroutine does not return */
  FUN_0043bad8("vector");
}

~~~
