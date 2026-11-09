# 00bb1efc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bb1efc",
  "name": "_ZN11flatbuffers21FlatBufferBuilderImplILb0EE21CreateVectorOfStringsINSt6__ndk111__wrap_iterIPKNS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEEEEENS_6OffsetINS_6VectorINSE_INS_6StringEEEjEEEET_SK_",
  "size": 464,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d62923abd10461c91bee61e5c9948c96f4992533dd6ad03c79a84f82cea54267",
  "source_text_sha256": "d62923abd10461c91bee61e5c9948c96f4992533dd6ad03c79a84f82cea54267"
}
~~~

## 呼び出し元

- [00c5bec0](../00c5b/00c5bec0.md)

## 呼び出し先

- [00c5bda0](../00c5b/00c5bda0.md)
- [00c5be50](../00c5b/00c5be50.md)
- [00c5be80](../00c5b/00c5be80.md)
- [00c5bea0](../00c5b/00c5bea0.md)

## 疑似コード / UTF-8 3893 bytes

~~~c

undefined4
_ZN11flatbuffers21FlatBufferBuilderImplILb0EE21CreateVectorOfStringsINSt6__ndk111__wrap_iterIPKNS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEEEEENS_6OffsetINS_6VectorINSE_INS_6StringEEEjEEEET_SK_
          (long param_1,byte *param_2,byte *param_3)

{
  uint uVar1;
  byte *pbVar2;
  int iVar3;
  undefined4 uVar4;
  undefined4 *puVar5;
  long lVar6;
  ulong uVar7;
  int iVar8;
  long lVar9;
  ulong uVar10;
  ulong uVar11;
  ulong uVar12;
  long lVar13;
  
  lVar13 = (long)param_3 - (long)param_2;
  lVar9 = lVar13 >> 3;
  uVar10 = lVar9 * -0x5555555555555555;
  if ((ulong)(uint)(*(int *)(param_1 + 0x40) - *(int *)(param_1 + 0x48)) <
      (ulong)(lVar9 * -0x5555555555555554)) {
    _ZN11flatbuffers15vector_downwardIjE10reallocateEm(param_1,lVar9 * -0x5555555555555554);
  }
  for (; param_2 != param_3; param_2 = param_2 + 0x18) {
                    /* catch() { ... } // from try @ 00bb1e0c with catch @ 00bb1f78 */
    uVar12 = *(ulong *)(param_2 + 8);
    pbVar2 = *(byte **)(param_2 + 0x10);
    if ((*param_2 & 1) == 0) {
      pbVar2 = param_2 + 1;
      uVar12 = (ulong)(*param_2 >> 1);
    }
    _ZN11flatbuffers21FlatBufferBuilderImplILb0EE16CreateStringImplEPKcm(param_1,pbVar2,uVar12);
    puVar5 = *(undefined4 **)(param_1 + 0x48);
    uVar4 = *(undefined4 *)(param_1 + 0x30);
    if ((*(int *)(param_1 + 0x40) - (int)puVar5 & 0xfffffffcU) == 0) {
      _ZN11flatbuffers15vector_downwardIjE10reallocateEm(param_1,4);
      puVar5 = *(undefined4 **)(param_1 + 0x48);
    }
    *puVar5 = uVar4;
    *(undefined4 **)(param_1 + 0x48) = puVar5 + 1;
  }
  _ZN11flatbuffers21FlatBufferBuilderImplILb0EE11StartVectorINS_6OffsetEjEEvmmm(param_1,uVar10,4,4);
  lVar6 = *(long *)(param_1 + 0x48);
  if (lVar13 != 0) {
    uVar12 = 1;
    do {
      iVar3 = *(int *)(lVar6 + uVar12 * -4);
      if (*(ulong *)(param_1 + 0x68) < 4) {
        *(undefined8 *)(param_1 + 0x68) = 4;
      }
      iVar8 = *(int *)(param_1 + 0x30);
      uVar1 = -iVar8 & 3;
      uVar11 = (ulong)uVar1;
      if (uVar1 != 0) {
        lVar13 = *(long *)(param_1 + 0x40);
                    /* try { // try from 00bb2048 to 00cb2123 has its CatchHandler @ 00bb2048
                       catch() { ... } // from try @ 00bb2048 with catch @ 00bb2048
                       catch() { ... } // from try @ 00bb2144 with catch @ 00bb2048
                       catch() { ... } // from try @ 00bb21c4 with catch @ 00bb2048
                       catch() { ... } // from try @ 00bb2298 with catch @ 00bb2048
                       catch() { ... } // from try @ 00bb23cc with catch @ 00bb2048
                       catch() { ... } // from try @ 00bb24e4 with catch @ 00bb2048
                       catch() { ... } // from try @ 00bb2564 with catch @ 00bb2048 */
        if ((uint)((int)lVar13 - (int)lVar6) < uVar11) {
          _ZN11flatbuffers15vector_downwardIjE10reallocateEm(param_1,uVar11);
          lVar13 = *(long *)(param_1 + 0x40);
          iVar8 = *(int *)(param_1 + 0x30);
        }
        *(undefined1 **)(param_1 + 0x40) = (undefined1 *)(lVar13 - uVar11);
        *(uint *)(param_1 + 0x30) = iVar8 + uVar1;
        *(undefined1 *)(lVar13 - uVar11) = 0;
        if (uVar1 != 1) {
          uVar7 = 1;
          do {
            *(undefined1 *)(*(long *)(param_1 + 0x40) + uVar7) = 0;
            uVar7 = uVar7 + 1;
          } while (uVar11 != uVar7);
        }
      }
      _ZN11flatbuffers21FlatBufferBuilderImplILb0EE11PushElementIjjEET0_T_
                (param_1,(*(int *)(param_1 + 0x30) - iVar3) + 4);
      lVar6 = *(long *)(param_1 + 0x48);
      uVar12 = uVar12 + 1;
    } while (uVar12 <= uVar10);
  }
  *(long *)(param_1 + 0x48) = lVar6 + lVar9 * 0x5555555555555554;
  *(undefined1 *)(param_1 + 0x60) = 0;
  uVar4 = _ZN11flatbuffers21FlatBufferBuilderImplILb0EE11PushElementIjjEET0_T_
                    (param_1,uVar10 & 0xffffffff);
  return uVar4;
}

~~~
