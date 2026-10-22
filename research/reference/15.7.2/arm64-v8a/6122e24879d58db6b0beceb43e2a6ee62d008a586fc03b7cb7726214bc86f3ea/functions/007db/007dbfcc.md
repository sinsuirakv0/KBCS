# 007dbfcc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](007dbfcc.md)

## 関数情報

~~~json
{
  "address": "007dbfcc",
  "name": "FUN_007dbfcc",
  "size": 304,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "597a20429972686c66e91c6bc4c9cbae438b101ad5d7b1a3588dd09a090cc377",
  "source_text_sha256": "597a20429972686c66e91c6bc4c9cbae438b101ad5d7b1a3588dd09a090cc377"
}
~~~
## 呼び出し元

- [007db2f0](../007db/007db2f0.md)

## 呼び出し先

- [007bfcc8](../007bf/007bfcc8.md)
- [00bdaf40](../00bda/00bdaf40.md)
- [00bdaf60](../00bda/00bdaf60.md)
- [00bdaff0](../00bda/00bdaff0.md)
- [00bdb0b0](../00bdb/00bdb0b0.md)

## 疑似コード 1/1 / UTF-8 2063 bytes

~~~c

void FUN_007dbfcc(undefined8 *param_1,void *param_2,long param_3,ulong param_4)

{
  void *__src;
  ulong uVar1;
  size_t sVar2;
  ulong uVar3;
  void *__dest;
  
  uVar3 = param_1[2];
  __dest = (void *)*param_1;
  if (param_4 <= (ulong)((long)(uVar3 - (long)__dest) >> 4)) {
    sVar2 = (long)param_1[1] - (long)__dest;
    __src = param_2;
    if (((ulong)((long)sVar2 >> 4) < param_4) &&
       (__src = (void *)((long)param_2 + sVar2), (void *)param_1[1] != __dest)) {
                    /* try { // try from 007dc0a8 to 008dc0af has its CatchHandler @ 007dd318 */
      memmove(__dest,param_2,sVar2);
      __dest = (void *)param_1[1];
    }
    sVar2 = param_3 - (long)__src;
    if (sVar2 != 0) {
      memmove(__dest,__src,sVar2);
    }
LAB_007dc0d8:
                    /* try { // try from 007dc0dc to 008dc0e3 has its CatchHandler @ 007dd5a0 */
    param_1[1] = (long)__dest + sVar2;
    return;
  }
  if (__dest != (void *)0x0) {
    param_1[1] = __dest;
    operator_delete(__dest);
    uVar3 = 0;
    *param_1 = 0;
    param_1[1] = 0;
    param_1[2] = 0;
  }
  if (param_4 >> 0x3c == 0) {
    uVar1 = (long)uVar3 >> 3;
    if ((ulong)((long)uVar3 >> 3) <= param_4) {
      uVar1 = param_4;
    }
                    /* try { // try from 007dc03c to 008dc047 has its CatchHandler @ 007dd388 */
    if (0x7fffffffffffffef < uVar3) {
      uVar1 = 0xfffffffffffffff;
    }
    if (uVar1 >> 0x3c == 0) {
      __dest = operator_new(uVar1 * 0x10);
      sVar2 = param_3 - (long)param_2;
                    /* try { // try from 007dc068 to 008dc083 has its CatchHandler @ 007dd350 */
      *param_1 = __dest;
      param_1[1] = __dest;
      param_1[2] = (void *)((long)__dest + uVar1 * 0x10);
      if (sVar2 != 0) {
        memcpy(__dest,param_2,sVar2);
      }
      goto LAB_007dc0d8;
    }
  }
                    /* WARNING: Subroutine does not return */
                    /* try { // try from 007dc0f8 to 008dc0ff has its CatchHandler @ 007dd59c */
  FUN_007bfcc8(param_1);
}

~~~
