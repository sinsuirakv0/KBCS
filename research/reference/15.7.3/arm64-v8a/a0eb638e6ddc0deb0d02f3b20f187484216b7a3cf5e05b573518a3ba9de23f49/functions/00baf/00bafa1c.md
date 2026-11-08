# 00bafa1c

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00bafa1c",
  "name": "_ZNSt6__ndk114__num_get_base10__get_baseERNS_8ios_baseE",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c0d4b8c48462c2023c559e49b874327904d4646fc23798d600e2d25ca9b3cf01",
  "source_text_sha256": "c0d4b8c48462c2023c559e49b874327904d4646fc23798d600e2d25ca9b3cf01"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 285 bytes

~~~c

undefined8 _ZNSt6__ndk114__num_get_base10__get_baseERNS_8ios_baseE(long param_1)

{
  uint uVar1;
  
  uVar1 = *(uint *)(param_1 + 8) & 0x4a;
  if (uVar1 == 0) {
    return 0;
  }
  if (uVar1 != 0x40) {
    if (uVar1 == 8) {
      return 0x10;
    }
    return 10;
  }
  return 8;
}

~~~
