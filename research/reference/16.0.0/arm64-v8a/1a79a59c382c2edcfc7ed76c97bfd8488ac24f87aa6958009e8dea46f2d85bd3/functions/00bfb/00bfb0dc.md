# 00bfb0dc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bfb0dc",
  "name": "_ZNSt6__ndk18ios_base5clearEj",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c561438effb3311149076e5bd3001bf8bf467dd2d836129baa92bfb3d1f620fb",
  "source_text_sha256": "c561438effb3311149076e5bd3001bf8bf467dd2d836129baa92bfb3d1f620fb"
}
~~~

## 呼び出し元

- [00c57ea0](../00c57/00c57ea0.md)

## 呼び出し先

- [00bfb11c](../00bfb/00bfb11c.md)

## 関連文字列（未確認候補）

~~~text
"ios_base::clear"
~~~

## 疑似コード / UTF-8 327 bytes

~~~c

void _ZNSt6__ndk18ios_base5clearEj(long param_1,uint param_2)

{
  param_2 = *(long *)(param_1 + 0x28) == 0 | param_2;
  *(uint *)(param_1 + 0x20) = param_2;
  if ((*(uint *)(param_1 + 0x24) & param_2) == 0) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  FUN_00bfb11c("ios_base::clear");
}

~~~
