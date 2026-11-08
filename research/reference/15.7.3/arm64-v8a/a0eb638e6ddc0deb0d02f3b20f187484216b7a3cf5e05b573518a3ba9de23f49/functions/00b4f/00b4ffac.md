# 00b4ffac

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00b4ffac",
  "name": "_ZNSt6__ndk16vectorIhNS_9allocatorIhEEE6assignIN11flatbuffers14VectorIteratorIhhEEEENS_9enable_ifIXaasr21__is_forward_iteratorIT_EE5valuesr16is_constructibleIhNS_15iterator_traitsIS9_E9referenceEEE5valueEvE4typeES9_S9_",
  "size": 608,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7e2242dfa2ee451206b1ac9383e664e2df418387d071223adb288888e7ec90c2",
  "source_text_sha256": "7e2242dfa2ee451206b1ac9383e664e2df418387d071223adb288888e7ec90c2"
}
~~~

## 呼び出し元

- [00be0530](../00be0/00be0530.md)

## 呼び出し先

- [00bdaff0](../00bda/00bdaff0.md)
- [00bdb010](../00bdb/00bdb010.md)
- [00bdde60](../00bdd/00bdde60.md)

## 疑似コード / UTF-8 5257 bytes

~~~c

void _ZNSt6__ndk16vectorIhNS_9allocatorIhEEE6assignIN11flatbuffers14VectorIteratorIhhEEEENS_9enable_ifIXaasr21__is_forward_iteratorIT_EE5valuesr16is_constructibleIhNS_15iterator_traitsIS9_E9referenceEEE5valueEvE4typeES9_S9_
               (undefined8 *param_1,undefined8 *param_2,ulong *param_3)

{
  undefined8 *puVar1;
  undefined1 *puVar2;
  ulong uVar3;
  undefined1 *puVar4;
  undefined1 *puVar5;
  undefined1 *puVar6;
  undefined1 *puVar7;
  ulong uVar8;
  undefined8 *puVar9;
  undefined8 *puVar10;
  ulong uVar11;
  ulong uVar12;
  ulong uVar13;
  undefined8 uVar14;
  undefined8 uVar15;
  undefined8 uVar16;
  
  puVar7 = (undefined1 *)*param_2;
  uVar3 = param_1[2];
  puVar2 = (undefined1 *)*param_1;
  uVar13 = (long)*param_3 - (long)puVar7;
  if (uVar3 - (long)puVar2 < uVar13) {
    if (puVar2 != (undefined1 *)0x0) {
      param_1[1] = puVar2;
      _ZdlPv(puVar2);
      uVar3 = 0;
      *param_1 = 0;
      param_1[1] = 0;
                    /* try { // try from 00b4fffc to 00c50003 has its CatchHandler @ 00b50070 */
      param_1[2] = 0;
    }
    if ((long)uVar13 < 0) {
                    /* WARNING: Subroutine does not return */
      _ZNKSt6__ndk120__vector_base_commonILb1EE20__throw_length_errorEv(param_1);
    }
                    /* try { // try from 00b50004 to 00c50097 has its CatchHandler @ 00b4ff68 */
    if (uVar3 < 0x3fffffffffffffff) {
      if (uVar13 <= uVar3 << 1) {
        uVar13 = uVar3 << 1;
      }
    }
    else {
      uVar13 = 0x7fffffffffffffff;
    }
    puVar7 = (undefined1 *)_Znwm(uVar13);
    *param_1 = puVar7;
    param_1[1] = puVar7;
    param_1[2] = puVar7 + uVar13;
    puVar2 = (undefined1 *)*param_2;
    puVar4 = (undefined1 *)*param_3;
    uVar13 = (long)puVar4 - (long)puVar2;
                    /* catch() { ... } // from try @ 00b4fffc with catch @ 00b50070 */
    if (uVar13 != 0) {
      puVar6 = puVar7;
      if ((0x1f < uVar13) && ((puVar4 <= puVar7 || (puVar7 + uVar13 <= puVar2)))) {
        uVar8 = uVar13 & 0xffffffffffffffe0;
        puVar10 = (undefined8 *)(puVar2 + 0x10);
        puVar6 = puVar7 + uVar8;
        puVar2 = puVar2 + uVar8;
        puVar9 = (undefined8 *)(puVar7 + 0x10);
        uVar3 = uVar8;
        do {
          puVar1 = puVar10 + -1;
          uVar14 = puVar10[-2];
          uVar16 = puVar10[1];
          uVar15 = *puVar10;
          puVar10 = puVar10 + 4;
          uVar3 = uVar3 - 0x20;
          puVar9[-1] = *puVar1;
          puVar9[-2] = uVar14;
          puVar9[1] = uVar16;
          *puVar9 = uVar15;
          puVar9 = puVar9 + 4;
        } while (uVar3 != 0);
        puVar7 = puVar6;
        if (uVar13 == uVar8) goto LAB_00b500e8;
      }
      do {
        puVar5 = puVar2 + 1;
        puVar7 = puVar6 + 1;
        *puVar6 = *puVar2;
        puVar2 = puVar5;
        puVar6 = puVar7;
      } while (puVar4 != puVar5);
    }
LAB_00b500e8:
    param_1[1] = puVar7;
    return;
  }
  uVar3 = param_1[1] - (long)puVar2;
  puVar4 = puVar7 + (uVar3 & 0xffffffff);
  if (uVar13 <= uVar3) {
    puVar4 = (undefined1 *)*param_3;
  }
  uVar8 = (long)puVar4 - (long)puVar7;
  if (uVar8 != 0) {
    puVar6 = puVar2;
    if ((0x1f < uVar8) && ((puVar4 <= puVar2 || (puVar4 + ((long)puVar2 - (long)puVar7) <= puVar7)))
       ) {
      uVar11 = uVar8 & 0xffffffffffffffe0;
      puVar10 = (undefined8 *)(puVar2 + 0x10);
      puVar2 = puVar2 + uVar11;
      puVar9 = (undefined8 *)(puVar7 + 0x10);
      uVar12 = uVar11;
      do {
        puVar1 = puVar9 + -1;
        uVar14 = puVar9[-2];
        uVar16 = puVar9[1];
        uVar15 = *puVar9;
        uVar12 = uVar12 - 0x20;
        puVar9 = puVar9 + 4;
        puVar10[-1] = *puVar1;
        puVar10[-2] = uVar14;
        puVar10[1] = uVar16;
        *puVar10 = uVar15;
        puVar10 = puVar10 + 4;
      } while (uVar12 != 0);
      puVar6 = puVar2;
      puVar7 = puVar7 + uVar11;
      if (uVar11 == uVar8) goto LAB_00b50158;
    }
    do {
      puVar5 = puVar7 + 1;
      puVar2 = puVar6 + 1;
      *puVar6 = *puVar7;
      puVar6 = puVar2;
      puVar7 = puVar5;
    } while (puVar4 != puVar5);
  }
LAB_00b50158:
  if (uVar13 <= uVar3) {
    param_1[1] = puVar2;
    return;
  }
  puVar6 = (undefined1 *)*param_3;
  puVar7 = (undefined1 *)param_1[1];
  uVar13 = (long)puVar6 - (long)puVar4;
  puVar2 = puVar7;
  if (uVar13 != 0) {
    if ((0x1f < uVar13) && ((puVar6 <= puVar7 || (puVar7 + uVar13 <= puVar4)))) {
      uVar8 = uVar13 & 0xffffffffffffffe0;
      puVar10 = (undefined8 *)(puVar4 + 0x10);
      puVar2 = puVar7 + uVar8;
      puVar4 = puVar4 + uVar8;
      puVar9 = (undefined8 *)(puVar7 + 0x10);
      uVar3 = uVar8;
      do {
        puVar1 = puVar10 + -1;
        uVar14 = puVar10[-2];
        uVar16 = puVar10[1];
        uVar15 = *puVar10;
        puVar10 = puVar10 + 4;
        uVar3 = uVar3 - 0x20;
        puVar9[-1] = *puVar1;
        puVar9[-2] = uVar14;
        puVar9[1] = uVar16;
        *puVar9 = uVar15;
        puVar9 = puVar9 + 4;
      } while (uVar3 != 0);
      puVar7 = puVar2;
      if (uVar8 == uVar13) goto LAB_00b501f0;
    }
    do {
      puVar5 = puVar4 + 1;
      puVar2 = puVar7 + 1;
      *puVar7 = *puVar4;
      puVar4 = puVar5;
      puVar7 = puVar2;
    } while (puVar6 != puVar5);
  }
LAB_00b501f0:
  param_1[1] = puVar2;
  return;
}

~~~
