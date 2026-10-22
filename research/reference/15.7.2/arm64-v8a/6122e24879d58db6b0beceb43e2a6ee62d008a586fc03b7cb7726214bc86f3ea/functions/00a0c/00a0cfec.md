# 00a0cfec

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00a0cfec.md)

## 関数情報

~~~json
{
  "address": "00a0cfec",
  "name": "FUN_00a0cfec",
  "size": 128,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8f1b2bd28a0f2c264cdd58a5b4f99f2191ec43399b0e6397ea4453500b478bec",
  "source_text_sha256": "8f1b2bd28a0f2c264cdd58a5b4f99f2191ec43399b0e6397ea4453500b478bec"
}
~~~
## 呼び出し元

- [006eccf4](../006ec/006eccf4.md)
- [009f4a74](../009f4/009f4a74.md)

## 呼び出し先

- [00a0cdf4](../00a0c/00a0cdf4.md)
- [00a0e088](../00a0e/00a0e088.md)
- [00a0e40c](../00a0e/00a0e40c.md)

## 疑似コード 1/1 / UTF-8 739 bytes

~~~c

void FUN_00a0cfec(long param_1,undefined4 param_2,undefined8 param_3,undefined8 param_4,
                 undefined8 param_5)

{
  int iVar1;
  
                    /* try { // try from 00a0d008 to 00b0d00f has its CatchHandler @ 00a0d41c */
                    /* try { // try from 00a0d010 to 00b0d663 has its CatchHandler @ 00a0a31c */
  FUN_00a0e40c(*(undefined8 *)(param_1 + 0x70),*(undefined4 *)(param_1 + 0x7c));
  iVar1 = FUN_00a0e088();
  if (iVar1 == 0) {
    iVar1 = FUN_00a0cdf4(param_1,param_2,param_3,param_4,param_5);
  }
  else {
    iVar1 = 0;
  }
  iVar1 = *(int *)(param_1 + 0x88) + iVar1;
  if (0x3b9ac9fe < iVar1) {
    iVar1 = 999999999;
  }
  *(int *)(param_1 + 0x88) = iVar1;
  return;
}

~~~
