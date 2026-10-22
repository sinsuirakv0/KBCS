# 00adfbac

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00adfbac.md)

## 関数情報

~~~json
{
  "address": "00adfbac",
  "name": "FUN_00adfbac",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e7b6da05fe4726d3ee7a554627287ad49c3853801c29112257f2b178d44a0888",
  "source_text_sha256": "e7b6da05fe4726d3ee7a554627287ad49c3853801c29112257f2b178d44a0888"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード 1/1 / UTF-8 306 bytes

~~~c

long FUN_00adfbac(long param_1,long param_2)

{
  param_1 = param_1 + 8;
                    /* try { // try from 00adfbc0 to 00bdfbdf has its CatchHandler @ 00adfbfc */
  if (*(char **)(param_2 + 8) != "ZN18unlockPopupManager11createPopupEvE3$_1") {
    param_1 = 0;
  }
  return param_1;
}

~~~
