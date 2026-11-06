# 00adfbbc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

ページ 1/1。[入口](00adfbbc.md)

## 関数情報

~~~json
{
  "address": "00adfbbc",
  "name": "FUN_00adfbbc",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f0e5a0470284ed5277015568a811d3ed865598f1ea12777a1581d1549a6e8e5b",
  "source_text_sha256": "f0e5a0470284ed5277015568a811d3ed865598f1ea12777a1581d1549a6e8e5b"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード 1/1 / UTF-8 186 bytes

~~~c

void FUN_00adfbbc(long param_1,undefined8 *param_2)

{
  undefined8 uVar1;
  
  uVar1 = *(undefined8 *)(param_1 + 8);
  *param_2 = &PTR_FUN_00c0fa48;
  param_2[1] = uVar1;
  return;
}

~~~
