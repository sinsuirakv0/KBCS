# 00af7ddc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00af7ddc",
  "name": "_ZNSt6__ndk16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE21__push_back_slow_pathIS6_EEvOT_",
  "size": 352,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5d2be82af3f607f9c527e591875f8cfbc4ec055e7dcc8313dc7c7eca030bd1b1",
  "source_text_sha256": "5d2be82af3f607f9c527e591875f8cfbc4ec055e7dcc8313dc7c7eca030bd1b1"
}
~~~

## 呼び出し元

- [00bde780](../00bde/00bde780.md)

## 呼び出し先

- [00bdaff0](../00bda/00bdaff0.md)
- [00bdb010](../00bdb/00bdb010.md)
- [00bde270](../00bde/00bde270.md)

## 疑似コード / UTF-8 3473 bytes

~~~c

void _ZNSt6__ndk16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE21__push_back_slow_pathIS6_EEvOT_
               (long *param_1,undefined8 *param_2)

{
  ulong uVar1;
  undefined8 *puVar2;
  byte bVar3;
  byte *pbVar4;
  long lVar5;
  byte *pbVar6;
  long lVar7;
  ulong uVar8;
  undefined8 *puVar9;
  byte *pbVar10;
  byte *__ptr;
  ulong uVar11;
  undefined8 uVar12;
  undefined8 uVar13;
  
                    /* try { // try from 00af7df8 to 00bf7e5b has its CatchHandler @ 00af560c */
  lVar5 = param_1[1] - *param_1 >> 3;
  uVar11 = 0xaaaaaaaaaaaaaaa;
  uVar1 = lVar5 * -0x5555555555555555 + 1;
  if (0xaaaaaaaaaaaaaaa < uVar1) {
                    /* WARNING: Subroutine does not return */
    abort();
  }
  lVar7 = param_1[2] - *param_1 >> 3;
  if ((ulong)(lVar7 * -0x5555555555555555) < 0x555555555555555) {
    uVar8 = lVar7 * 0x5555555555555556;
    uVar11 = uVar1;
    if (uVar1 <= uVar8) {
      uVar11 = uVar8;
    }
    if (uVar11 == 0) {
      lVar7 = 0;
                    /* try { // try from 00af7f34 to 00bf7f4f has its CatchHandler @ 00aff1e4 */
      goto LAB_00af7e60;
    }
  }
                    /* try { // try from 00af7e5c to 00bf7e5f has its CatchHandler @ 00b0037c */
  lVar7 = _Znwm(uVar11 * 0x18);
LAB_00af7e60:
  uVar13 = param_2[1];
  uVar12 = *param_2;
  puVar9 = (undefined8 *)(lVar7 + lVar5 * 8);
  puVar9[2] = param_2[2];
  puVar9[1] = uVar13;
  *puVar9 = uVar12;
  param_2[1] = 0;
  param_2[2] = 0;
  *param_2 = 0;
  pbVar6 = (byte *)*param_1;
  pbVar10 = (byte *)param_1[1];
  puVar2 = puVar9 + 3;
  __ptr = pbVar6;
  if (pbVar10 != pbVar6) {
    do {
      uVar13 = *(undefined8 *)(pbVar10 + -0x10);
      uVar12 = *(undefined8 *)(pbVar10 + -0x18);
                    /* try { // try from 00af7ea0 to 00bf7eab has its CatchHandler @ 00aff238 */
      puVar9[-1] = *(undefined8 *)(pbVar10 + -8);
      puVar9[-2] = uVar13;
      puVar9[-3] = uVar12;
      pbVar10[-0x10] = 0;
      pbVar10[-0xf] = 0;
      pbVar10[-0xe] = 0;
      pbVar10[-0xd] = 0;
      pbVar10[-0xc] = 0;
      pbVar10[-0xb] = 0;
      pbVar10[-10] = 0;
      pbVar10[-9] = 0;
      pbVar10[-8] = 0;
      pbVar10[-7] = 0;
      pbVar10[-6] = 0;
      pbVar10[-5] = 0;
      pbVar10[-4] = 0;
      pbVar10[-3] = 0;
      pbVar10[-2] = 0;
      pbVar10[-1] = 0;
      pbVar10[-0x18] = 0;
      pbVar10[-0x17] = 0;
      pbVar10[-0x16] = 0;
      pbVar10[-0x15] = 0;
      pbVar10[-0x14] = 0;
      pbVar10[-0x13] = 0;
      pbVar10[-0x12] = 0;
      pbVar10[-0x11] = 0;
                    /* try { // try from 00af7eb0 to 00bf7ecb has its CatchHandler @ 00aff1fc */
      pbVar10 = pbVar10 + -0x18;
      puVar9 = puVar9 + -3;
    } while (pbVar6 != pbVar10);
    pbVar6 = (byte *)param_1[1];
    __ptr = (byte *)*param_1;
  }
                    /* try { // try from 00af7ed0 to 00bf7edf has its CatchHandler @ 00b0037c */
  *param_1 = (long)puVar9;
  param_1[1] = (long)puVar2;
  param_1[2] = lVar7 + uVar11 * 0x18;
  if (pbVar6 != __ptr) {
    bVar3 = pbVar6[-0x18];
    pbVar10 = pbVar6 + -0x18;
    while( true ) {
      pbVar4 = pbVar10;
      if ((bVar3 & 1) != 0) {
        _ZdlPv(*(void **)(pbVar6 + -8));
      }
      if (__ptr == pbVar4) break;
      bVar3 = pbVar4[-0x18];
      pbVar10 = pbVar4 + -0x18;
      pbVar6 = pbVar4;
    }
  }
  if (__ptr != (byte *)0x0) {
    _ZdlPv(__ptr);
    return;
  }
                    /* try { // try from 00af7f24 to 00bf7f2f has its CatchHandler @ 00aff1f8 */
  return;
}

~~~
