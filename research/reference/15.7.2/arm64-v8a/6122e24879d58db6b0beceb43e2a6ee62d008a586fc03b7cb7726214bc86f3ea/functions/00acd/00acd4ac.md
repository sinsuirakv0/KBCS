# 00acd4ac

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00acd4ac.md)

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
  "source_sha256": "0cc7e3543cf3749f45005e283680adada6788d68ad3a5d799cd235cb6a8c9550",
  "source_text_sha256": "0cc7e3543cf3749f45005e283680adada6788d68ad3a5d799cd235cb6a8c9550"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0081f580](../0081f/0081f580.md)

## 疑似コード 1/1 / UTF-8 305 bytes

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
