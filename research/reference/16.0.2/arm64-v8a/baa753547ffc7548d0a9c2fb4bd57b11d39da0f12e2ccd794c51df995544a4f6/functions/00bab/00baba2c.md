# 00baba2c

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00baba2c",
  "name": "_ZNSt6__ndk16vectorIN11flatbuffers5ValueENS_9allocatorIS2_EEE24__emplace_back_slow_pathIJS2_EEEvDpOT_",
  "size": 356,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "74c3d64390d5455b679c0584ebf86e8f588ca4a27e41da279ddff858aba98401",
  "source_text_sha256": "74c3d64390d5455b679c0584ebf86e8f588ca4a27e41da279ddff858aba98401"
}
~~~

## 呼び出し元

- [00c5d0d0](../00c5d/00c5d0d0.md)

## 呼び出し先

- [00c57f60](../00c57/00c57f60.md)
- [00c57f80](../00c57/00c57f80.md)
- [00c5b210](../00c5b/00c5b210.md)

## 疑似コード / UTF-8 5818 bytes

~~~c

void _ZNSt6__ndk16vectorIN11flatbuffers5ValueENS_9allocatorIS2_EEE24__emplace_back_slow_pathIJS2_EEEvDpOT_
               (long *param_1,undefined8 *param_2)

{
  undefined8 *puVar1;
  void *pvVar2;
  undefined8 *puVar3;
  long lVar4;
  ulong uVar5;
  void *pvVar6;
  long lVar7;
  void *__ptr;
  long lVar8;
  ulong uVar9;
  undefined8 uVar10;
  undefined8 uVar11;
  undefined8 uVar12;
  
                    /* catch() { ... } // from try @ 00bab4e0 with catch @ 00baba30 */
                    /* catch() { ... } // from try @ 00bab4b4 with catch @ 00baba40 */
                    /* catch() { ... } // from try @ 00bab490 with catch @ 00baba44 */
  lVar8 = param_1[1] - *param_1 >> 6;
  uVar9 = lVar8 + 1;
  if (uVar9 >> 0x3a != 0) {
LAB_00baba88:
                    /* WARNING: Subroutine does not return */
    abort();
  }
                    /* catch() { ... } // from try @ 00bab7fc with catch @ 00baba54 */
                    /* catch() { ... } // from try @ 00bab7d8 with catch @ 00baba58 */
  lVar4 = param_1[2] - *param_1;
                    /* catch() { ... } // from try @ 00bab7ac with catch @ 00baba68 */
                    /* catch() { ... } // from try @ 00bab464 with catch @ 00baba6c */
  if ((ulong)(lVar4 >> 6) < 0x1ffffffffffffff) {
                    /* catch() { ... } // from try @ 00bab440 with catch @ 00baba70 */
    uVar5 = lVar4 >> 5;
    if (uVar9 <= uVar5) {
      uVar9 = uVar5;
    }
    if (uVar9 == 0) {
      lVar4 = 0;
      goto LAB_00baba98;
    }
                    /* catch() { ... } // from try @ 00bab414 with catch @ 00baba80 */
                    /* catch() { ... } // from try @ 00bab78c with catch @ 00baba84 */
    if (uVar9 >> 0x3a != 0) goto LAB_00baba88;
  }
  else {
    uVar9 = 0x3ffffffffffffff;
  }
                    /* catch() { ... } // from try @ 00bab760 with catch @ 00baba94 */
  lVar4 = _Znwm(uVar9 << 6);
LAB_00baba98:
                    /* catch() { ... } // from try @ 00bab73c with catch @ 00baba98 */
  uVar10 = *param_2;
  uVar12 = param_2[3];
  uVar11 = param_2[2];
  puVar3 = (undefined8 *)(lVar4 + lVar8 * 0x40);
  puVar1 = puVar3 + 8;
  puVar3[1] = param_2[1];
  *puVar3 = uVar10;
  puVar3[3] = uVar12;
  puVar3[2] = uVar11;
                    /* catch() { ... } // from try @ 00bab3f4 with catch @ 00babaa8 */
  uVar11 = param_2[5];
  uVar10 = param_2[4];
  puVar3[6] = param_2[6];
  puVar3[5] = uVar11;
  puVar3[4] = uVar10;
                    /* catch() { ... } // from try @ 00bab3c8 with catch @ 00babab8 */
                    /* catch() { ... } // from try @ 00bab3a4 with catch @ 00bababc */
  param_2[5] = 0;
  param_2[6] = 0;
  param_2[4] = 0;
  *(undefined2 *)(puVar3 + 7) = *(undefined2 *)(param_2 + 7);
  pvVar6 = (void *)*param_1;
  pvVar2 = (void *)param_1[1];
                    /* catch() { ... } // from try @ 00bab710 with catch @ 00babacc */
                    /* catch() { ... } // from try @ 00bab6f0 with catch @ 00babad0 */
  __ptr = pvVar6;
  if (pvVar2 != pvVar6) {
    lVar8 = 0;
    do {
                    /* catch() { ... } // from try @ 00bab378 with catch @ 00babae0 */
                    /* catch() { ... } // from try @ 00bab358 with catch @ 00babae4 */
      uVar10 = *(undefined8 *)((long)pvVar2 + lVar8 + -0x40);
      uVar12 = *(undefined8 *)((long)pvVar2 + lVar8 + -0x28);
      uVar11 = *(undefined8 *)((long)pvVar2 + lVar8 + -0x30);
      lVar7 = lVar8 + -0x40;
                    /* catch() { ... } // from try @ 00bab6d0 with catch @ 00babaf4 */
      *(undefined8 *)((long)puVar3 + lVar8 + -0x38) = *(undefined8 *)((long)pvVar2 + lVar8 + -0x38);
      *(undefined8 *)((long)puVar3 + lVar8 + -0x40) = uVar10;
      *(undefined8 *)((long)puVar3 + lVar8 + -0x28) = uVar12;
      *(undefined8 *)((long)puVar3 + lVar8 + -0x30) = uVar11;
      uVar11 = *(undefined8 *)((long)pvVar2 + lVar8 + -0x18);
      uVar10 = *(undefined8 *)((long)pvVar2 + lVar8 + -0x20);
      *(undefined8 *)((long)puVar3 + lVar8 + -0x10) = *(undefined8 *)((long)pvVar2 + lVar8 + -0x10);
      *(undefined8 *)((long)puVar3 + lVar8 + -0x18) = uVar11;
      *(undefined8 *)((long)puVar3 + lVar8 + -0x20) = uVar10;
      *(undefined8 *)((long)pvVar2 + lVar8 + -0x18) = 0;
      *(undefined8 *)((long)pvVar2 + lVar8 + -0x10) = 0;
      *(undefined8 *)((long)pvVar2 + lVar8 + -0x20) = 0;
                    /* catch() { ... } // from try @ 00bab6bc with catch @ 00babb14 */
      *(undefined2 *)((long)puVar3 + lVar8 + -8) = *(undefined2 *)((long)pvVar2 + lVar8 + -8);
      lVar8 = lVar7;
                    /* catch() { ... } // from try @ 00bab698 with catch @ 00babb18 */
    } while ((long)pvVar6 - (long)pvVar2 != lVar7);
                    /* catch() { ... } // from try @ 00bab338 with catch @ 00babb1c */
    pvVar6 = (void *)param_1[1];
    puVar3 = (undefined8 *)((long)puVar3 + lVar7);
    __ptr = (void *)*param_1;
  }
  *param_1 = (long)puVar3;
  param_1[1] = (long)puVar1;
  param_1[2] = lVar4 + uVar9 * 0x40;
  while (pvVar2 = pvVar6, pvVar2 != __ptr) {
    pvVar6 = (void *)((long)pvVar2 + -0x40);
    if ((*(byte *)((long)pvVar2 + -0x20) & 1) != 0) {
                    /* catch() { ... } // from try @ 00bab1b4 with catch @ 00babb6c */
                    /* catch() { ... } // from try @ 00bab194 with catch @ 00babb70 */
      _ZdlPv(*(void **)((long)pvVar2 + -0x10));
    }
  }
                    /* catch() { ... } // from try @ 00bab324 with catch @ 00babb3c */
  if (__ptr != (void *)0x0) {
                    /* catch() { ... } // from try @ 00bab300 with catch @ 00babb40 */
                    /* catch() { ... } // from try @ 00baabf8 with catch @ 00babb50 */
    _ZdlPv(__ptr);
    return;
  }
                    /* catch() { ... } // from try @ 00baaea8 with catch @ 00babb80 */
                    /* catch() { ... } // from try @ 00baae8c with catch @ 00babb84 */
  return;
}

~~~
