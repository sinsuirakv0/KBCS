# 00bb2bac

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00bb2bac",
  "name": "_ZN11flatbuffers21SetFileExistsFunctionEPFbPKcE",
  "size": 36,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e69b3f3ae5656ee822b49a48234c2efa13be03e785e304766e36a4bd976ca8a4",
  "source_text_sha256": "e69b3f3ae5656ee822b49a48234c2efa13be03e785e304766e36a4bd976ca8a4"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 377 bytes

~~~c

undefined * _ZN11flatbuffers21SetFileExistsFunctionEPFbPKcE(code *param_1)

{
  code *pcVar1;
  undefined *puVar2;
  
                    /* try { // try from 00bb2bac to 00cb2ea7 has its CatchHandler @ 00bb2b48 */
  pcVar1 = FUN_00bb2bd0;
  if (param_1 != (code *)0x0) {
    pcVar1 = param_1;
  }
  puVar2 = PTR_FUN_00ca4780;
  PTR_FUN_00ca4780 = pcVar1;
  return puVar2;
}

~~~
