# 00abeec0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

<!-- kbcs-version-next -->
**別版の対応** [v15.7.4 `00abefcc`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00abe/00abefcc.md)
<!-- /kbcs-version-next -->

## 関数情報

~~~json
{
  "address": "00abeec0",
  "name": "FUN_00abeec0",
  "size": 264,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f770cb9c150ae929fc5920e6762607badb297d82bd592dcc4f2fa37947e80669",
  "source_text_sha256": "f770cb9c150ae929fc5920e6762607badb297d82bd592dcc4f2fa37947e80669"
}
~~~

## 呼び出し元

- [00abe0c4](../00abe/00abe0c4.md)

## 呼び出し先

- [0041e380](../0041e/0041e380.md)
- [00bdaf40](../00bda/00bdaf40.md)
- [00bdaf60](../00bda/00bdaf60.md)

## 疑似コード / UTF-8 1675 bytes

~~~c

void FUN_00abeec0(long *param_1)

{
  undefined8 *puVar1;
  undefined8 *puVar2;
  void *__ptr;
  undefined8 *puVar3;
  undefined8 *puVar4;
  undefined8 *__ptr_00;
  ulong uVar5;
  undefined8 uVar6;
  
  puVar1 = (undefined8 *)param_1[1];
                    /* try { // try from 00abeed8 to 00bbefaf has its CatchHandler @ 00ac52f0 */
  __ptr_00 = (undefined8 *)*param_1;
  uVar5 = (long)puVar1 - (long)__ptr_00;
  if (uVar5 < (ulong)(param_1[2] - (long)__ptr_00)) {
    if (puVar1 == __ptr_00) {
      puVar2 = (undefined8 *)0x0;
    }
    else {
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
      } while (__ptr_00 != puVar1);
      __ptr_00 = (undefined8 *)*param_1;
    }
    *param_1 = (long)puVar2;
    param_1[1] = uVar5;
    param_1[2] = uVar5;
    if (__ptr_00 != (undefined8 *)0x0) {
      _ZdlPv(__ptr_00);
      return;
    }
  }
                    /* try { // try from 00abefcc to 00bbeff7 has its CatchHandler @ 00ac5290 */
  return;
}

~~~
