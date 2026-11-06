# 00a3afac

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

ページ 1/1。[入口](00a3afac.md)

## 関数情報

~~~json
{
  "address": "00a3afac",
  "name": "FUN_00a3afac",
  "size": 24,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7603b020697afff2ec93f5de94be1e329340fab32a058501fb3b6429af46474e",
  "source_text_sha256": "7603b020697afff2ec93f5de94be1e329340fab32a058501fb3b6429af46474e"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード 1/1 / UTF-8 234 bytes

~~~c

void FUN_00a3afac(long param_1,undefined8 *param_2)

{
  undefined8 uVar1;
  
  *param_2 = &PTR_FUN_00c0ccb8;
  uVar1 = *(undefined8 *)(param_1 + 8);
  param_2[2] = *(undefined8 *)(param_1 + 0x10);
  param_2[1] = uVar1;
  return;
}

~~~
