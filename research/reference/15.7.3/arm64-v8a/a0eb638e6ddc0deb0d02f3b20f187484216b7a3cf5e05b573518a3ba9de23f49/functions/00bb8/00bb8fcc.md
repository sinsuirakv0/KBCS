# 00bb8fcc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00bb8fcc",
  "name": "FUN_00bb8fcc",
  "size": 80,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2d8ef82eb0ff2e8d131bc534fc37630aaf7c5c0dc3a1c4e1ad3c1ec9844505d4",
  "source_text_sha256": "2d8ef82eb0ff2e8d131bc534fc37630aaf7c5c0dc3a1c4e1ad3c1ec9844505d4"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb010](../00bdb/00bdb010.md)

## 疑似コード / UTF-8 253 bytes

~~~c

void FUN_00bb8fcc(void)

{
  long lVar1;
  
  lVar1 = 0x240;
  do {
    if ((*(byte *)((long)&DAT_010a2ef4 + lVar1 + 4) & 1) != 0) {
      _ZdlPv(*(void **)(&DAT_010a2f08 + lVar1));
    }
    lVar1 = lVar1 + -0x18;
  } while (lVar1 != 0);
  return;
}

~~~
