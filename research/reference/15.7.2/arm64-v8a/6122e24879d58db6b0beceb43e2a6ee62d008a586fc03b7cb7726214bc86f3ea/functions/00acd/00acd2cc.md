# 00acd2cc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00acd2cc.md)

## 関数情報

~~~json
{
  "address": "00acd2cc",
  "name": "FUN_00acd2cc",
  "size": 72,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "89c069c5c8d3e98d61b0c35afd5218b0a419732fa416b936f5ca2e783b3a86dd",
  "source_text_sha256": "89c069c5c8d3e98d61b0c35afd5218b0a419732fa416b936f5ca2e783b3a86dd"
}
~~~
## 呼び出し元

- [00418828](../00418/00418828.md)

## 呼び出し先

- [0081f580](../0081f/0081f580.md)

## 疑似コード 1/1 / UTF-8 408 bytes

~~~c

void FUN_00acd2cc(float param_1,float param_2,undefined8 param_3,undefined4 param_4)

{
  long *plVar1;
  
  plVar1 = (long *)FUN_0081f580();
                    /* WARNING: Could not recover jumptable at 0x00acd310. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  (**(code **)(*plVar1 + 0x40))(plVar1,0,(int)param_1,(int)param_2,param_4);
  return;
}

~~~
