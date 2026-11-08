# 00a1fddc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00a1fddc",
  "name": "FUN_00a1fddc",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "72f248b8dd45707db42fb63189c598c6215ced1ea0d7ee82f95eef053ee69f03",
  "source_text_sha256": "72f248b8dd45707db42fb63189c598c6215ced1ea0d7ee82f95eef053ee69f03"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 186 bytes

~~~c

void FUN_00a1fddc(long param_1,undefined8 *param_2)

{
  undefined8 uVar1;
  
  uVar1 = *(undefined8 *)(param_1 + 8);
  *param_2 = &PTR_FUN_00c0c3b0;
  param_2[1] = uVar1;
  return;
}

~~~
