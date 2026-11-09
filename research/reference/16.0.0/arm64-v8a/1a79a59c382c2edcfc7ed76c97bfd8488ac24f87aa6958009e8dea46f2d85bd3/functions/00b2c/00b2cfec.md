# 00b2cfec

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00b2cfec",
  "name": "FUN_00b2cfec",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c8aa327de5cee3db40fd2650442c5986724d249ed07c3f4123e317def98d446a",
  "source_text_sha256": "c8aa327de5cee3db40fd2650442c5986724d249ed07c3f4123e317def98d446a"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [008514b8](../00851/008514b8.md)

## 疑似コード / UTF-8 292 bytes

~~~c

void FUN_00b2cfec(void)

{
  long *plVar1;
  
  plVar1 = (long *)FUN_008514b8();
                    /* WARNING: Could not recover jumptable at 0x00b2d004. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  (**(code **)(*plVar1 + 0x38))();
  return;
}

~~~
