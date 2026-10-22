# 00aaefdc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00aaefdc.md)

## 関数情報

~~~json
{
  "address": "00aaefdc",
  "name": "FUN_00aaefdc",
  "size": 56,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4254057d6f735e525f14e19099837506b6e47e4cba7f087a10e4e99cdfbb34ee",
  "source_text_sha256": "4254057d6f735e525f14e19099837506b6e47e4cba7f087a10e4e99cdfbb34ee"
}
~~~
## 呼び出し元

- [009bd6b8](../009bd/009bd6b8.md)

## 呼び出し先

- [0045d518](../0045d/0045d518.md)

## 疑似コード 1/1 / UTF-8 219 bytes

~~~c

void FUN_00aaefdc(undefined4 *param_1,undefined8 param_2)

{
  undefined4 uVar1;
  
  uVar1 = FUN_0045d518(param_2);
  *param_1 = uVar1;
  uVar1 = FUN_0045d518(param_2);
  param_1[1] = uVar1;
  return;
}

~~~
