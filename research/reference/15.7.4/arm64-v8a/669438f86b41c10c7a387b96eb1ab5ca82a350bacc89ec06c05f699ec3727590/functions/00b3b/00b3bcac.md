# 00b3bcac

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

## 関数情報

~~~json
{
  "address": "00b3bcac",
  "name": "FUN_00b3bcac",
  "size": 632,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8696cfd4ce21430cc6e9e03b466b5bf67d775c89e09895b89ae4bc9a0f3cbeb7",
  "source_text_sha256": "8696cfd4ce21430cc6e9e03b466b5bf67d775c89e09895b89ae4bc9a0f3cbeb7"
}
~~~

## 呼び出し元

- [00b3b138](../00b3b/00b3b138.md)
- [00b3c0c0](../00b3c/00b3c0c0.md)

## 呼び出し先

- [00bdb200](../00bdb/00bdb200.md)
- [00be0170](../00be0/00be0170.md)

## 疑似コード / UTF-8 5453 bytes

~~~c

int FUN_00b3bcac(uint *param_1,uint *param_2,uint *param_3,uint *param_4,uint *param_5,long *param_6
                )

{
  long lVar1;
  uint *puVar2;
  uint *puVar3;
  uint uVar4;
  uint uVar5;
  uint uVar6;
  uint uVar7;
  uint uVar8;
  bool bVar9;
  int iVar10;
  int iVar11;
  int *piVar12;
  int *piVar13;
  
  iVar10 = _ZNSt6__ndk17__sort4IRN11flatbuffers17FlatBufferBuilder18TableKeyComparatorIN10reflection6ObjectEEEPNS1_6OffsetIS5_EEEEjT0_SB_SB_SB_T_
                     ();
  uVar5 = *param_5;
  uVar6 = *param_4;
  lVar1 = *(long *)(*param_6 + 0x28) + *(long *)(*param_6 + 0x20);
  piVar12 = (int *)(lVar1 - (ulong)uVar5);
  piVar13 = (int *)(lVar1 - (ulong)uVar6);
                    /* catch() { ... } // from try @ 00b3b988 with catch @ 00b3bd18 */
                    /* catch() { ... } // from try @ 00b3b97c with catch @ 00b3bd1c */
                    /* catch() { ... } // from try @ 00b3b878 with catch @ 00b3bd20 */
                    /* catch() { ... } // from try @ 00b3b86c with catch @ 00b3bd24 */
  puVar2 = (uint *)((long)piVar12 + (ulong)*(ushort *)((long)piVar12 + (4 - (long)*piVar12)));
                    /* catch() { ... } // from try @ 00b3b768 with catch @ 00b3bd28 */
  puVar3 = (uint *)((long)piVar13 + (ulong)*(ushort *)((long)piVar13 + (4 - (long)*piVar13)));
                    /* catch() { ... } // from try @ 00b3b75c with catch @ 00b3bd2c */
                    /* catch() { ... } // from try @ 00b3b650 with catch @ 00b3bd30 */
  puVar2 = (uint *)((long)puVar2 + (ulong)*puVar2);
  puVar3 = (uint *)((long)puVar3 + (ulong)*puVar3);
  uVar7 = *puVar2;
  uVar8 = *puVar3;
  uVar4 = uVar8;
                    /* catch() { ... } // from try @ 00b3b644 with catch @ 00b3bd48 */
  if (uVar7 <= uVar8) {
    uVar4 = uVar7;
  }
  iVar11 = memcmp(puVar2 + 1,puVar3 + 1,(ulong)uVar4);
  bVar9 = uVar7 < uVar8;
                    /* catch() { ... } // from try @ 00b3b598 with catch @ 00b3bd5c */
  if (iVar11 != 0) {
    bVar9 = iVar11 < 0;
  }
                    /* catch() { ... } // from try @ 00b3b58c with catch @ 00b3bd6c */
  if (bVar9) {
    *param_4 = uVar5;
    *param_5 = uVar6;
    uVar5 = *param_4;
    uVar6 = *param_3;
    piVar12 = (int *)(lVar1 - (ulong)uVar5);
    piVar13 = (int *)(lVar1 - (ulong)uVar6);
                    /* catch() { ... } // from try @ 00b3b56c with catch @ 00b3bd8c */
                    /* catch() { ... } // from try @ 00b3b550 with catch @ 00b3bd94 */
                    /* catch() { ... } // from try @ 00b3b538 with catch @ 00b3bd9c */
                    /* catch() { ... } // from try @ 00b3b488 with catch @ 00b3bda0 */
    puVar2 = (uint *)((long)piVar12 + (ulong)*(ushort *)((long)piVar12 + (4 - (long)*piVar12)));
    puVar3 = (uint *)((long)piVar13 + (ulong)*(ushort *)((long)piVar13 + (4 - (long)*piVar13)));
    puVar2 = (uint *)((long)puVar2 + (ulong)*puVar2);
                    /* catch() { ... } // from try @ 00b3b4a4 with catch @ 00b3bdb8 */
    puVar3 = (uint *)((long)puVar3 + (ulong)*puVar3);
    uVar7 = *puVar2;
                    /* catch() { ... } // from try @ 00b3b4d4 with catch @ 00b3bdc0 */
    uVar8 = *puVar3;
                    /* catch() { ... } // from try @ 00b3b4e8 with catch @ 00b3bdc4 */
    uVar4 = uVar8;
                    /* catch() { ... } // from try @ 00b3b4f8 with catch @ 00b3bdc8 */
    if (uVar7 <= uVar8) {
      uVar4 = uVar7;
    }
    iVar11 = memcmp(puVar2 + 1,puVar3 + 1,(ulong)uVar4);
    bVar9 = uVar7 < uVar8;
    if (iVar11 != 0) {
      bVar9 = iVar11 < 0;
    }
    if (bVar9) {
      *param_3 = uVar5;
      *param_4 = uVar6;
      uVar5 = *param_3;
      uVar6 = *param_2;
      piVar12 = (int *)(lVar1 - (ulong)uVar5);
      piVar13 = (int *)(lVar1 - (ulong)uVar6);
      puVar2 = (uint *)((long)piVar12 + (ulong)*(ushort *)((long)piVar12 + (4 - (long)*piVar12)));
      puVar3 = (uint *)((long)piVar13 + (ulong)*(ushort *)((long)piVar13 + (4 - (long)*piVar13)));
      puVar2 = (uint *)((long)puVar2 + (ulong)*puVar2);
      puVar3 = (uint *)((long)puVar3 + (ulong)*puVar3);
      uVar7 = *puVar2;
      uVar8 = *puVar3;
      uVar4 = uVar8;
      if (uVar7 <= uVar8) {
        uVar4 = uVar7;
      }
      iVar11 = memcmp(puVar2 + 1,puVar3 + 1,(ulong)uVar4);
      bVar9 = uVar7 < uVar8;
      if (iVar11 != 0) {
        bVar9 = iVar11 < 0;
      }
      if (bVar9) {
        *param_2 = uVar5;
        *param_3 = uVar6;
        uVar5 = *param_2;
        uVar6 = *param_1;
        piVar12 = (int *)(lVar1 - (ulong)uVar5);
        piVar13 = (int *)(lVar1 - (ulong)uVar6);
        puVar2 = (uint *)((long)piVar12 + (ulong)*(ushort *)((long)piVar12 + (4 - (long)*piVar12)));
        puVar3 = (uint *)((long)piVar13 + (ulong)*(ushort *)((long)piVar13 + (4 - (long)*piVar13)));
        puVar2 = (uint *)((long)puVar2 + (ulong)*puVar2);
        puVar3 = (uint *)((long)puVar3 + (ulong)*puVar3);
        uVar7 = *puVar2;
        uVar8 = *puVar3;
        uVar4 = uVar8;
        if (uVar7 <= uVar8) {
          uVar4 = uVar7;
        }
        iVar11 = memcmp(puVar2 + 1,puVar3 + 1,(ulong)uVar4);
        bVar9 = uVar7 < uVar8;
        if (iVar11 != 0) {
          bVar9 = iVar11 < 0;
        }
        if (bVar9) {
          iVar10 = iVar10 + 4;
          *param_1 = uVar5;
          *param_2 = uVar6;
        }
        else {
          iVar10 = iVar10 + 3;
        }
      }
      else {
        iVar10 = iVar10 + 2;
      }
    }
    else {
      iVar10 = iVar10 + 1;
    }
  }
  return iVar10;
}

~~~
