# 00badd1c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00badd1c.md)

## 関数情報

~~~json
{
  "address": "00badd1c",
  "name": "_ZNKSt6__ndk115__codecvt_utf16IwLb1EE13do_max_lengthEv",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c576fe512f5773049e5eb747299a130e78932f72f5526c854a9257f40724ba7c",
  "source_text_sha256": "c576fe512f5773049e5eb747299a130e78932f72f5526c854a9257f40724ba7c"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード 1/1 / UTF-8 204 bytes

~~~c

undefined4 _ZNKSt6__ndk115__codecvt_utf16IwLb1EE13do_max_lengthEv(long param_1)

{
  undefined4 uVar1;
  
  uVar1 = 4;
  if ((*(byte *)(param_1 + 0x20) & 4) != 0) {
    uVar1 = 6;
  }
  return uVar1;
}

~~~
