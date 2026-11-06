# 00abefcc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

ページ 1/1。[入口](00abefcc.md)

## 関数情報

~~~json
{
  "address": "00abefcc",
  "name": "FUN_00abefcc",
  "size": 264,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "eed80c529ded132fc061ad5c3047d0b8fca4416a91d897be52bf61de01d359e6",
  "source_text_sha256": "eed80c529ded132fc061ad5c3047d0b8fca4416a91d897be52bf61de01d359e6"
}
~~~
## 呼び出し元

- [00abe1d0](../00abe/00abe1d0.md)

## 呼び出し先

- [0041e380](../0041e/0041e380.md)
- [00bdb040](../00bdb/00bdb040.md)
- [00bdb060](../00bdb/00bdb060.md)

## 疑似コード 1/1 / UTF-8 2063 bytes

~~~c

void FUN_00abefcc(long *param_1)

{
  undefined8 *puVar1;
  undefined8 *puVar2;
  void *__ptr;
  undefined8 *puVar3;
  undefined8 *puVar4;
  undefined8 *__ptr_00;
  ulong uVar5;
  undefined8 uVar6;
  
                    /* try { // try from 00abefd8 to 00bbf003 has its CatchHandler @ 00ac529c */
  puVar1 = (undefined8 *)param_1[1];
  __ptr_00 = (undefined8 *)*param_1;
  uVar5 = (long)puVar1 - (long)__ptr_00;
  if (uVar5 < (ulong)(param_1[2] - (long)__ptr_00)) {
    if (puVar1 == __ptr_00) {
      puVar2 = (undefined8 *)0x0;
    }
    else {
                    /* try { // try from 00abf010 to 00bbf04b has its CatchHandler @ 00ac4f6c */
      if (0xaaaaaaaaaaaaaaa < (ulong)(((long)uVar5 >> 3) * -0x5555555555555555)) {
                    /* WARNING: Subroutine does not return */
        FUN_0041e380();
      }
      puVar2 = (undefined8 *)_Znwm(uVar5);
      uVar5 = (long)puVar2 + uVar5;
      puVar3 = puVar2;
      puVar4 = __ptr_00;
      do {
        uVar6 = *puVar4;
        puVar3[1] = puVar4[1];
        *puVar3 = uVar6;
        puVar3[2] = puVar4[2];
                    /* try { // try from 00abf050 to 00bbf067 has its CatchHandler @ 00ac5268 */
        puVar3 = puVar3 + 3;
        *puVar4 = 0;
        puVar4[1] = 0;
        puVar4[2] = 0;
        puVar4 = puVar4 + 3;
      } while (puVar4 != puVar1);
      do {
        __ptr = (void *)*__ptr_00;
        if (__ptr != (void *)0x0) {
          __ptr_00[1] = __ptr;
          _ZdlPv(__ptr);
        }
        __ptr_00 = __ptr_00 + 3;
                    /* try { // try from 00abf070 to 00bbf09b has its CatchHandler @ 00ac4f58 */
      } while (__ptr_00 != puVar1);
      __ptr_00 = (undefined8 *)*param_1;
    }
    *param_1 = (long)puVar2;
    param_1[1] = uVar5;
    param_1[2] = uVar5;
                    /* try { // try from 00abf0a0 to 00bbf0bb has its CatchHandler @ 00ac5268 */
    if (__ptr_00 != (undefined8 *)0x0) {
      _ZdlPv(__ptr_00);
      return;
    }
  }
                    /* try { // try from 00abf0c8 to 00bbf0ff has its CatchHandler @ 00ac4f64 */
  return;
}

~~~
