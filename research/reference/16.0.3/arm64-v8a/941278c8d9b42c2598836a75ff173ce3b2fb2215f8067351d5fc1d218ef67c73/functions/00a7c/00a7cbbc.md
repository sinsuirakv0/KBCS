# 00a7cbbc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00a7cbbc",
  "name": "FUN_00a7cbbc",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b26ff3cc98588af2890555e44b76b6bb81f06734b55719712999ba08db148be5",
  "source_text_sha256": "b26ff3cc98588af2890555e44b76b6bb81f06734b55719712999ba08db148be5"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 380 bytes

~~~c

void FUN_00a7cbbc(long param_1,undefined8 *param_2)

{
  undefined8 uVar1;
  
  uVar1 = *(undefined8 *)(param_1 + 8);
                    /* try { // try from 00a7cbc0 to 00b7cbc7 has its CatchHandler @ 00a7d390 */
                    /* try { // try from 00a7cbc8 to 00b7cbe7 has its CatchHandler @ 00a7d408 */
  *param_2 = &PTR_FUN_00c8caa0;
  param_2[1] = uVar1;
  return;
}

~~~
