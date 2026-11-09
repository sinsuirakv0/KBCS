# 00aefbac

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00aefbac",
  "name": "_ZdlPv",
  "size": 4,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b60df0e95a43003ef4aafa80a5b038a13ec43078cfefc2ffb11476109da5983b",
  "source_text_sha256": "b60df0e95a43003ef4aafa80a5b038a13ec43078cfefc2ffb11476109da5983b"
}
~~~

## 呼び出し元

- [00ad075c](../00ad0/00ad075c.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 253 bytes

~~~c

/* WARNING: Unknown calling convention -- yet parameter storage is locked */

void _ZdlPv(void *__ptr)

{
                    /* try { // try from 00aefbac to 00befbaf has its CatchHandler @ 00aefc10 */
  (*(code *)PTR__ZdlPv_00c9bb18)();
  return;
}

~~~
