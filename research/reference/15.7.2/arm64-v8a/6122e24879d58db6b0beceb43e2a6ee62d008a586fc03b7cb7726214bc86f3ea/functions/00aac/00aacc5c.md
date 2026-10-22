# 00aacc5c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00aacc5c.md)

## 関数情報

~~~json
{
  "address": "00aacc5c",
  "name": "FUN_00aacc5c",
  "size": 32,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ac7deb9e8bc90bb516192547aacef90e7790e94ba85c0858d820addf2537ecf9",
  "source_text_sha256": "ac7deb9e8bc90bb516192547aacef90e7790e94ba85c0858d820addf2537ecf9"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード 1/1 / UTF-8 335 bytes

~~~c

void FUN_00aacc5c(long param_1,undefined8 *param_2)

{
  undefined8 uVar1;
  undefined8 uVar2;
  
  *param_2 = &PTR_FUN_00c0f1d8;
  uVar2 = *(undefined8 *)(param_1 + 0x10);
  uVar1 = *(undefined8 *)(param_1 + 8);
  param_2[3] = *(undefined8 *)(param_1 + 0x18);
  param_2[2] = uVar2;
  param_2[1] = uVar1;
  return;
}

~~~
