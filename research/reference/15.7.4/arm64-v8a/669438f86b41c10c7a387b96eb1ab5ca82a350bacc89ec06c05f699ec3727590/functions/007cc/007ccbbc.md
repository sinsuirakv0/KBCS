# 007ccbbc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

## 関数情報

~~~json
{
  "address": "007ccbbc",
  "name": "FUN_007ccbbc",
  "size": 24,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "799e737b3821d954548e2d836c8df8d7401bd0c2384f7b5575ebc4633fbdfe74",
  "source_text_sha256": "799e737b3821d954548e2d836c8df8d7401bd0c2384f7b5575ebc4633fbdfe74"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00885f80](../00885/00885f80.md)

## 疑似コード / UTF-8 252 bytes

~~~c

void FUN_007ccbbc(undefined8 param_1,undefined8 *param_2,int *param_3)

{
  if (*param_3 == 2) {
    FUN_00885f80(*param_2);
    return;
  }
                    /* try { // try from 007ccbd0 to 008ccc0b has its CatchHandler @ 007c86d0 */
  return;
}

~~~
