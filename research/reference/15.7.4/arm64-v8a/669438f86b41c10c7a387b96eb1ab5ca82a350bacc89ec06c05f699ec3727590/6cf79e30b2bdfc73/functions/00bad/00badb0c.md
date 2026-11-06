# 00badb0c

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

ページ 1/1。[入口](00badb0c.md)

## 関数情報

~~~json
{
  "address": "00badb0c",
  "name": "_ZNKSt6__ndk115__codecvt_utf16IwLb0EE13do_max_lengthEv",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "870058c90c9c53b29a581d0313ca0ee210f190045fbb441eacc10848f0624f7a",
  "source_text_sha256": "870058c90c9c53b29a581d0313ca0ee210f190045fbb441eacc10848f0624f7a"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード 1/1 / UTF-8 204 bytes

~~~c

undefined4 _ZNKSt6__ndk115__codecvt_utf16IwLb0EE13do_max_lengthEv(long param_1)

{
  undefined4 uVar1;
  
  uVar1 = 4;
  if ((*(byte *)(param_1 + 0x20) & 4) != 0) {
    uVar1 = 6;
  }
  return uVar1;
}

~~~
