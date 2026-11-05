# 00babfbc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00babfbc.md)

## 関数情報

~~~json
{
  "address": "00babfbc",
  "name": "_ZNKSt6__ndk17codecvtIDsc9mbstate_tE5do_inERS1_PKcS5_RS5_PDsS7_RS7_",
  "size": 104,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8064a162dc1de59a03c611856d45e0153637913ec3249c8f0a0798841b782226",
  "source_text_sha256": "8064a162dc1de59a03c611856d45e0153637913ec3249c8f0a0798841b782226"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bac024](../00bac/00bac024.md)

## 疑似コード 1/1 / UTF-8 500 bytes

~~~c

void _ZNKSt6__ndk17codecvtIDsc9mbstate_tE5do_inERS1_PKcS5_RS5_PDsS7_RS7_
               (undefined8 param_1,undefined8 param_2,undefined8 param_3,undefined8 param_4,
               undefined8 *param_5,undefined8 param_6,undefined8 param_7,undefined8 *param_8)

{
  undefined8 local_30;
  undefined8 uStack_28;
  
  local_30 = param_6;
  uStack_28 = param_3;
  FUN_00bac024(param_3,param_4,&uStack_28,param_6,param_7,&local_30,0x10ffff,0);
  *param_5 = uStack_28;
  *param_8 = local_30;
  return;
}

~~~
