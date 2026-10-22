# 007ccbbc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](007ccbbc.md)

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
  "source_sha256": "9ffa795bf9483038476f2270bfd1e0816232314b7c4b96054918304a6ed2f047",
  "source_text_sha256": "9ffa795bf9483038476f2270bfd1e0816232314b7c4b96054918304a6ed2f047"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00885f80](../00885/00885f80.md)

## 疑似コード 1/1 / UTF-8 264 bytes

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
