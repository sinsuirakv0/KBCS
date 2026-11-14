# 007fdbbc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "007fdbbc",
  "name": "FUN_007fdbbc",
  "size": 24,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "17a9d6f4ea74845a63ea734f45131e6c60515f1828255a4c71dadb460659f759",
  "source_text_sha256": "17a9d6f4ea74845a63ea734f45131e6c60515f1828255a4c71dadb460659f759"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 204 bytes

~~~c

void FUN_007fdbbc(long param_1,undefined8 *param_2)

{
  undefined4 uVar1;
  
  uVar1 = *(undefined4 *)(param_1 + 8);
  *param_2 = &PTR_FUN_00c7e750;
  *(undefined4 *)(param_2 + 1) = uVar1;
  return;
}

~~~
