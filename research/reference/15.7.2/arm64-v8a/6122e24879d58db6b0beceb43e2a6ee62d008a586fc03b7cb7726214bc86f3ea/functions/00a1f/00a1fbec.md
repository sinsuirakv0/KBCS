# 00a1fbec

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00a1fbec.md)

## 関数情報

~~~json
{
  "address": "00a1fbec",
  "name": "FUN_00a1fbec",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c0ab4f4ccbaeac4674030ac6e0e35ec2fca1dc45164898b208223f384523db14",
  "source_text_sha256": "c0ab4f4ccbaeac4674030ac6e0e35ec2fca1dc45164898b208223f384523db14"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード 1/1 / UTF-8 198 bytes

~~~c

void FUN_00a1fbec(long param_1,undefined8 *param_2)

{
  undefined8 uVar1;
  
  uVar1 = *(undefined8 *)(param_1 + 8);
  *param_2 = &PTR_FUN_00c0c200;
  param_2[1] = uVar1;
  return;
}

~~~
