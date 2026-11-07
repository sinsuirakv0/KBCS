# 00acd4ac

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

<!-- kbcs-version-next -->
**別版の対応** [v15.7.4 `00acd5b8`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acd/00acd5b8.md)
<!-- /kbcs-version-next -->

## 関数情報

~~~json
{
  "address": "00acd4ac",
  "name": "FUN_00acd4ac",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0e12ae4655f84a5f60fc8b856c37b5e6dfc35995a1b8cb23efc47bc5bd2b471d",
  "source_text_sha256": "0e12ae4655f84a5f60fc8b856c37b5e6dfc35995a1b8cb23efc47bc5bd2b471d"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0081f580](../0081f/0081f580.md)

## 疑似コード / UTF-8 292 bytes

~~~c

void FUN_00acd4ac(void)

{
  long *plVar1;
  
  plVar1 = (long *)FUN_0081f580();
                    /* WARNING: Could not recover jumptable at 0x00acd4c4. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  (**(code **)(*plVar1 + 0x30))();
  return;
}

~~~
