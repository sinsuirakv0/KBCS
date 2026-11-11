# 00baad5c

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00baad5c",
  "name": "_ZNSt6__ndk16vectorINS_4pairIN11flatbuffers5ValueEPNS2_8FieldDefEEENS_9allocatorIS6_EEE21__push_back_slow_pathIS6_EEvOT_",
  "size": 432,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ce418a59954d3681a686bdbec2d14d668232bb1afe8e114a60c105c889e0992c",
  "source_text_sha256": "ce418a59954d3681a686bdbec2d14d668232bb1afe8e114a60c105c889e0992c"
}
~~~

## 呼び出し元

- [00c5d040](../00c5d/00c5d040.md)

## 呼び出し先

- [00c57e90](../00c57/00c57e90.md)
- [00c57eb0](../00c57/00c57eb0.md)
- [00c5b140](../00c5b/00c5b140.md)

## 疑似コード / UTF-8 4258 bytes

~~~c

void _ZNSt6__ndk16vectorINS_4pairIN11flatbuffers5ValueEPNS2_8FieldDefEEENS_9allocatorIS6_EEE21__push_back_slow_pathIS6_EEvOT_
               (long *param_1,undefined8 *param_2)

{
  ulong uVar1;
  undefined8 *puVar2;
  void *pvVar3;
  long lVar4;
  undefined8 *puVar5;
  long lVar6;
  ulong uVar7;
  void *pvVar8;
  long lVar9;
  void *__ptr;
  ulong uVar10;
  undefined8 uVar11;
  undefined8 uVar12;
  undefined8 uVar13;
  
                    /* try { // try from 00baad7c to 00caad87 has its CatchHandler @ 00babbb4 */
  lVar4 = param_1[1] - *param_1 >> 3;
  uVar10 = 0x38e38e38e38e38e;
  uVar1 = lVar4 * -0x71c71c71c71c71c7 + 1;
                    /* try { // try from 00baada0 to 00caadab has its CatchHandler @ 00babbb0 */
  if (0x38e38e38e38e38e < uVar1) {
                    /* WARNING: Subroutine does not return */
    abort();
  }
  lVar6 = param_1[2] - *param_1 >> 3;
                    /* try { // try from 00baadcc to 00caadd7 has its CatchHandler @ 00babb64 */
  if ((ulong)(lVar6 * -0x71c71c71c71c71c7) < 0x1c71c71c71c71c7) {
    uVar7 = lVar6 * 0x1c71c71c71c71c72;
    uVar10 = uVar1;
    if (uVar1 <= uVar7) {
      uVar10 = uVar7;
    }
    if (uVar10 == 0) {
      lVar6 = 0;
      goto LAB_00baadf4;
    }
  }
                    /* try { // try from 00baadf0 to 00caadfb has its CatchHandler @ 00babb60 */
  lVar6 = _Znwm(uVar10 * 0x48);
LAB_00baadf4:
  uVar11 = *param_2;
  uVar13 = param_2[3];
  uVar12 = param_2[2];
  puVar5 = (undefined8 *)(lVar6 + lVar4 * 8);
  puVar5[1] = param_2[1];
  *puVar5 = uVar11;
  puVar5[3] = uVar13;
  puVar5[2] = uVar12;
  uVar12 = param_2[5];
  uVar11 = param_2[4];
  puVar5[6] = param_2[6];
  puVar5[5] = uVar12;
  puVar5[4] = uVar11;
                    /* try { // try from 00baae1c to 00caae27 has its CatchHandler @ 00babb14 */
  param_2[5] = 0;
  param_2[6] = 0;
  param_2[4] = 0;
  *(undefined2 *)(puVar5 + 7) = *(undefined2 *)(param_2 + 7);
  puVar5[8] = param_2[8];
  pvVar8 = (void *)*param_1;
  pvVar3 = (void *)param_1[1];
  puVar2 = puVar5 + 9;
                    /* try { // try from 00baae38 to 00caae43 has its CatchHandler @ 00babb10 */
  __ptr = pvVar8;
  if (pvVar3 != pvVar8) {
                    /* try { // try from 00baae44 to 00caae63 has its CatchHandler @ 00babe60 */
    lVar4 = 0;
    do {
      uVar11 = *(undefined8 *)((long)pvVar3 + lVar4 + -0x38);
      uVar13 = *(undefined8 *)((long)pvVar3 + lVar4 + -0x40);
      uVar12 = *(undefined8 *)((long)pvVar3 + lVar4 + -0x48);
      lVar9 = lVar4 + -0x48;
      *(undefined8 *)((long)puVar5 + lVar4 + -0x30) = *(undefined8 *)((long)pvVar3 + lVar4 + -0x30);
      *(undefined8 *)((long)puVar5 + lVar4 + -0x38) = uVar11;
      *(undefined8 *)((long)puVar5 + lVar4 + -0x40) = uVar13;
      *(undefined8 *)((long)puVar5 + lVar4 + -0x48) = uVar12;
                    /* try { // try from 00baae64 to 00caaed3 has its CatchHandler @ 00bac034 */
      uVar12 = *(undefined8 *)((long)pvVar3 + lVar4 + -0x20);
      uVar11 = *(undefined8 *)((long)pvVar3 + lVar4 + -0x28);
      *(undefined8 *)((long)puVar5 + lVar4 + -0x18) = *(undefined8 *)((long)pvVar3 + lVar4 + -0x18);
      *(undefined8 *)((long)puVar5 + lVar4 + -0x20) = uVar12;
      *(undefined8 *)((long)puVar5 + lVar4 + -0x28) = uVar11;
      *(undefined8 *)((long)pvVar3 + lVar4 + -0x20) = 0;
      *(undefined8 *)((long)pvVar3 + lVar4 + -0x18) = 0;
      *(undefined8 *)((long)pvVar3 + lVar4 + -0x28) = 0;
      *(undefined2 *)((long)puVar5 + lVar4 + -0x10) = *(undefined2 *)((long)pvVar3 + lVar4 + -0x10);
      *(undefined8 *)((long)puVar5 + lVar4 + -8) = *(undefined8 *)((long)pvVar3 + lVar4 + -8);
      lVar4 = lVar9;
    } while ((long)pvVar8 - (long)pvVar3 != lVar9);
    pvVar8 = (void *)param_1[1];
    puVar5 = (undefined8 *)((long)puVar5 + lVar9);
    __ptr = (void *)*param_1;
  }
  *param_1 = (long)puVar5;
  param_1[1] = (long)puVar2;
  param_1[2] = lVar6 + uVar10 * 0x48;
  while (pvVar3 = pvVar8, pvVar3 != __ptr) {
    pvVar8 = (void *)((long)pvVar3 + -0x48);
    if ((*(byte *)((long)pvVar3 + -0x28) & 1) != 0) {
      _ZdlPv(*(void **)((long)pvVar3 + -0x18));
    }
  }
  if (__ptr != (void *)0x0) {
    _ZdlPv(__ptr);
    return;
  }
                    /* try { // try from 00baaef4 to 00caaeff has its CatchHandler @ 00babdbc */
  return;
}

~~~
