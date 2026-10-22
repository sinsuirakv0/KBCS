# 00baa5cc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00baa5cc.md)

## 関数情報

~~~json
{
  "address": "00baa5cc",
  "name": "std::__ndk1::ctype_byname<char>::do_tolower",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3366b9d78a84ebea99af5f9f7809ce165e061a9b2f6e599fc9b6433206669b24",
  "source_text_sha256": "3366b9d78a84ebea99af5f9f7809ce165e061a9b2f6e599fc9b6433206669b24"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード 1/1 / UTF-8 305 bytes

~~~c

/* std::__ndk1::ctype_byname<char>::do_tolower(char) const */

byte __thiscall std::__ndk1::ctype_byname<char>::do_tolower(ctype_byname<char> *this,char param_1)

{
  byte bVar1;
  
  bVar1 = param_1 | 0x20;
  if (0x19 < (byte)param_1 - 0x41) {
    bVar1 = param_1;
  }
  return bVar1;
}

~~~
