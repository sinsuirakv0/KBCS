# 009dbcac

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "009dbcac",
  "name": "FUN_009dbcac",
  "size": 120,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b8214ba32b92d57f6de53f8502d5ed4e079ede746ac6efcce2c2dde80b085a88",
  "source_text_sha256": "b8214ba32b92d57f6de53f8502d5ed4e079ede746ac6efcce2c2dde80b085a88"
}
~~~

## 呼び出し元

- [00707ea0](../00707/00707ea0.md)

## 呼び出し先

- [0046bd14](../0046b/0046bd14.md)
- [00470074](../00470/00470074.md)

## 疑似コード / UTF-8 546 bytes

~~~c

void FUN_009dbcac(undefined8 param_1,long param_2,undefined8 param_3,undefined4 param_4,
                 undefined4 param_5,undefined4 param_6,int param_7)

{
  long lVar1;
  long lVar2;
  
                    /* try { // try from 009dbcb0 to 00adbd83 has its CatchHandler @ 009db558 */
  lVar1 = 0x1560;
  if (param_7 != 0) {
    lVar1 = 0x1b80;
  }
  lVar2 = 0x1608;
  if (param_7 != 0) {
    lVar2 = 0x1c28;
  }
  FUN_00470074(param_2 + lVar1,param_2 + lVar2,param_6,0);
  FUN_0046bd14(param_3,param_2 + lVar1,param_4,param_5);
  return;
}

~~~
