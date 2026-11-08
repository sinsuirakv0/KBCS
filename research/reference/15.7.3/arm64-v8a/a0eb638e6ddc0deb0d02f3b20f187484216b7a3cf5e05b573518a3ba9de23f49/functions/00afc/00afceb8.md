# 00afceb8

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00afceb8",
  "name": "_ZN8firebase4PathC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "bb9fa6c2ee70d20b99ce38081f484f75b92fcfb8ad669e609e4eaf8815671de5",
  "source_text_sha256": "bb9fa6c2ee70d20b99ce38081f484f75b92fcfb8ad669e609e4eaf8815671de5"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdece0](../00bde/00bdece0.md)

## 疑似コード / UTF-8 403 bytes

~~~c

void _ZN8firebase4PathC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
               (undefined8 param_1,undefined8 param_2)

{
                    /* try { // try from 00afcec4 to 00bfcf27 has its CatchHandler @ 00af560c */
  _ZN8firebase4Path16NormalizeSlashesERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
            (param_1,param_2);
  return;
}

~~~
