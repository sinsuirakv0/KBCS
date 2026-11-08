# 00baeb9c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

## 関数情報

~~~json
{
  "address": "00baeb9c",
  "name": "_ZNKSt6__ndk120__codecvt_utf8_utf16IwE13do_max_lengthEv",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "dbabf756cd286ecc6a778e32eef7ac78ea865a800df328f6a2de0a7d91e92f81",
  "source_text_sha256": "dbabf756cd286ecc6a778e32eef7ac78ea865a800df328f6a2de0a7d91e92f81"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 205 bytes

~~~c

undefined4 _ZNKSt6__ndk120__codecvt_utf8_utf16IwE13do_max_lengthEv(long param_1)

{
  undefined4 uVar1;
  
  uVar1 = 4;
  if ((*(byte *)(param_1 + 0x20) & 4) != 0) {
    uVar1 = 7;
  }
  return uVar1;
}

~~~
