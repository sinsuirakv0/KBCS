# 00acd3dc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00acd3dc",
  "name": "FUN_00acd3dc",
  "size": 72,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b9f8b9ea995bc9c53dc5b3864cf5aee81e5ba363cd2c0f88d20a13386fe7ddc4",
  "source_text_sha256": "b9f8b9ea995bc9c53dc5b3864cf5aee81e5ba363cd2c0f88d20a13386fe7ddc4"
}
~~~

## 呼び出し元

- [00418828](../00418/00418828.md)

## 呼び出し先

- [0081f580](../0081f/0081f580.md)

## 疑似コード / UTF-8 395 bytes

~~~c

void FUN_00acd3dc(float param_1,float param_2,undefined8 param_3,undefined4 param_4)

{
  long *plVar1;
  
  plVar1 = (long *)FUN_0081f580();
                    /* WARNING: Could not recover jumptable at 0x00acd420. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  (**(code **)(*plVar1 + 0x40))(plVar1,2,(int)param_1,(int)param_2,param_4);
  return;
}

~~~
