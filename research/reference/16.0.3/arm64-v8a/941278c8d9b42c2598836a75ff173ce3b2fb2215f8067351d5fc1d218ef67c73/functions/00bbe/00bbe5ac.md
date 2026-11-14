# 00bbe5ac

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bbe5ac",
  "name": "_ZNSt6__ndk16vectorINS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN8firebase16SafeFutureHandleIvEEEENS5_ISB_EEE21__push_back_slow_pathISB_EEvOT_",
  "size": 420,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "631b46ec5b8ac9767b84ac6aba33b1f78ae0399f9f53c49801f463f3cf8fd0b6",
  "source_text_sha256": "631b46ec5b8ac9767b84ac6aba33b1f78ae0399f9f53c49801f463f3cf8fd0b6"
}
~~~

## 呼び出し元

- [00c5e670](../00c5e/00c5e670.md)

## 呼び出し先

- [00c58f30](../00c58/00c58f30.md)
- [00c58f50](../00c58/00c58f50.md)
- [00c5bb30](../00c5b/00c5bb30.md)
- [00c5bdb0](../00c5b/00c5bdb0.md)
- [00c5cd00](../00c5c/00c5cd00.md)

## 疑似コード / UTF-8 4094 bytes

~~~c

void _ZNSt6__ndk16vectorINS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN8firebase16SafeFutureHandleIvEEEENS5_ISB_EEE21__push_back_slow_pathISB_EEvOT_
               (long *param_1,undefined8 *param_2)

{
  ulong uVar1;
  undefined8 *puVar2;
  byte *pbVar3;
  long lVar4;
  long lVar5;
  ulong uVar6;
  byte *pbVar7;
  byte *__ptr;
  undefined8 *puVar8;
  ulong uVar9;
  undefined8 uVar10;
  undefined8 uVar11;
  
  lVar4 = param_1[1] - *param_1 >> 3;
  uVar9 = 0x666666666666666;
  uVar1 = lVar4 * -0x3333333333333333 + 1;
  if (0x666666666666666 < uVar1) {
                    /* WARNING: Subroutine does not return */
    _ZNKSt6__ndk120__vector_base_commonILb1EE20__throw_length_errorEv(param_1);
  }
  lVar5 = param_1[2] - *param_1 >> 3;
  if ((ulong)(lVar5 * -0x3333333333333333) < 0x333333333333333) {
    uVar6 = lVar5 * -0x6666666666666666;
    uVar9 = uVar1;
    if (uVar1 <= uVar6) {
      uVar9 = uVar6;
    }
    if (uVar9 == 0) {
      lVar5 = 0;
      goto LAB_00bbe638;
    }
  }
  lVar5 = _Znwm(uVar9 * 0x28);
LAB_00bbe638:
  uVar11 = param_2[1];
  uVar10 = *param_2;
  puVar8 = (undefined8 *)(lVar5 + lVar4 * 8);
  puVar8[2] = param_2[2];
  puVar8[1] = uVar11;
  *puVar8 = uVar10;
  param_2[1] = 0;
  param_2[2] = 0;
  *param_2 = 0;
  _ZN8firebase12FutureHandleC1EOS0_(puVar8 + 3,param_2 + 3);
  __ptr = (byte *)*param_1;
  pbVar3 = (byte *)param_1[1];
  puVar2 = puVar8 + 5;
  pbVar7 = __ptr;
  if (pbVar3 != __ptr) {
    lVar4 = 0;
    do {
      uVar11 = *(undefined8 *)(pbVar3 + lVar4 + -0x20);
      uVar10 = *(undefined8 *)(pbVar3 + lVar4 + -0x28);
                    /* try { // try from 00bbe690 to 00cbe697 has its CatchHandler @ 00bbe72c */
      *(undefined8 *)((long)puVar8 + lVar4 + -0x18) = *(undefined8 *)(pbVar3 + lVar4 + -0x18);
      *(undefined8 *)((long)puVar8 + lVar4 + -0x20) = uVar11;
      *(undefined8 *)((long)puVar8 + lVar4 + -0x28) = uVar10;
      pbVar7 = pbVar3 + lVar4 + -0x20;
      pbVar7[0] = 0;
      pbVar7[1] = 0;
      pbVar7[2] = 0;
      pbVar7[3] = 0;
      pbVar7[4] = 0;
      pbVar7[5] = 0;
      pbVar7[6] = 0;
      pbVar7[7] = 0;
      pbVar7 = pbVar3 + lVar4 + -0x18;
      pbVar7[0] = 0;
      pbVar7[1] = 0;
      pbVar7[2] = 0;
      pbVar7[3] = 0;
      pbVar7[4] = 0;
      pbVar7[5] = 0;
      pbVar7[6] = 0;
      pbVar7[7] = 0;
      pbVar7 = pbVar3 + lVar4 + -0x28;
      pbVar7[0] = 0;
      pbVar7[1] = 0;
      pbVar7[2] = 0;
      pbVar7[3] = 0;
      pbVar7[4] = 0;
      pbVar7[5] = 0;
      pbVar7[6] = 0;
      pbVar7[7] = 0;
      _ZN8firebase12FutureHandleC1EOS0_((long)puVar8 + lVar4 + -0x10,pbVar3 + lVar4 + -0x10);
                    /* try { // try from 00bbe6ac to 00cbe6b3 has its CatchHandler @ 00bbe724 */
      lVar4 = lVar4 + -0x28;
    } while ((long)__ptr - (long)pbVar3 != lVar4);
    __ptr = (byte *)*param_1;
    puVar8 = (undefined8 *)((long)puVar8 + lVar4);
    pbVar7 = (byte *)param_1[1];
  }
  *param_1 = (long)puVar8;
  param_1[1] = (long)puVar2;
  param_1[2] = lVar5 + uVar9 * 0x28;
                    /* try { // try from 00bbe6c8 to 00cbe6cf has its CatchHandler @ 00bbe720 */
  while (pbVar3 = pbVar7, pbVar3 != __ptr) {
    _ZN8firebase12FutureHandleD2Ev(pbVar3 + -0x10);
    pbVar7 = pbVar3 + -0x28;
    if ((*pbVar7 & 1) != 0) {
      _ZdlPv(*(void **)(pbVar3 + -0x18));
                    /* catch() { ... } // from try @ 00bbe414 with catch @ 00bbe704
                       try { // try from 00bbe704 to 00cbe75b has its CatchHandler @ 00bbe340 */
    }
  }
  if (__ptr == (byte *)0x0) {
                    /* catch() { ... } // from try @ 00bbe45c with catch @ 00bbe728 */
                    /* catch() { ... } // from try @ 00bbe690 with catch @ 00bbe72c
                       catch() { ... } // from try @ 00bbe6e4 with catch @ 00bbe72c */
                    /* catch() { ... } // from try @ 00bbe548 with catch @ 00bbe730 */
    return;
  }
                    /* catch() { ... } // from try @ 00bbe6c8 with catch @ 00bbe720 */
                    /* catch() { ... } // from try @ 00bbe6ac with catch @ 00bbe724 */
  _ZdlPv(__ptr);
  return;
}

~~~
