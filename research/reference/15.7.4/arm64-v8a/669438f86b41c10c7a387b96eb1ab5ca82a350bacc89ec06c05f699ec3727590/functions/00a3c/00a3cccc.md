# 00a3cccc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

## 関数情報

~~~json
{
  "address": "00a3cccc",
  "name": "FUN_00a3cccc",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7ec631f00c94df7c8dfba57aa6f2258bce6a550f57eff1a288e0d61eb96d76a3",
  "source_text_sha256": "7ec631f00c94df7c8dfba57aa6f2258bce6a550f57eff1a288e0d61eb96d76a3"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 186 bytes

~~~c

void FUN_00a3cccc(long param_1,undefined8 *param_2)

{
  undefined8 uVar1;
  
  uVar1 = *(undefined8 *)(param_1 + 8);
  *param_2 = &PTR_FUN_00c0d4c8;
  param_2[1] = uVar1;
  return;
}

~~~
