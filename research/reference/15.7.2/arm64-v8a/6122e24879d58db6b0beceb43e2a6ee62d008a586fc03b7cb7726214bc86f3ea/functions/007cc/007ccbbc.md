# 007ccbbc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

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
