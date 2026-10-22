# 00adfab0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00adfab0.md)

## 関数情報

~~~json
{
  "address": "00adfab0",
  "name": "FUN_00adfab0",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c6bd2e89913bbdeba170302224ee4e4ceb0497b5fbcc980d63006631c2b77731",
  "source_text_sha256": "c6bd2e89913bbdeba170302224ee4e4ceb0497b5fbcc980d63006631c2b77731"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード 1/1 / UTF-8 296 bytes

~~~c

void FUN_00adfab0(long param_1,undefined8 *param_2)

{
  undefined8 uVar1;
  
  uVar1 = *(undefined8 *)(param_1 + 8);
                    /* try { // try from 00adfab4 to 00bdfabb has its CatchHandler @ 00adfc0c */
  *param_2 = &PTR_FUN_00c0f948;
  param_2[1] = uVar1;
  return;
}

~~~
