# 00b3cdac

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00b3cce4`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3c/00b3cce4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/af8e2f5c5fc38f06774ff85c/0-1/alignment_unresolved-0003.md#compare-9a30079725902720f056c55fee7e2470)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 構造資料不足
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b3cdac",
  "name": "_ZNSt6__ndk17__sort4IRN11flatbuffers17FlatBufferBuilder18TableKeyComparatorIN10reflection4EnumEEEPNS1_6OffsetIS5_EEEEjT0_SB_SB_SB_T_",
  "size": 484,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3a2beb84d94d929175f65f0ee717b31f55eef006080c2ac50ceaa7f2e2c21cd2",
  "source_text_sha256": "3a2beb84d94d929175f65f0ee717b31f55eef006080c2ac50ceaa7f2e2c21cd2"
}
~~~

## 呼び出し元

- [00be0100](../00be0/00be0100.md)

## 呼び出し先

- [00bdb1b0](../00bdb/00bdb1b0.md)
- [00be00a0](../00be0/00be00a0.md)

## 疑似コード / UTF-8 3250 bytes

~~~c

int _ZNSt6__ndk17__sort4IRN11flatbuffers17FlatBufferBuilder18TableKeyComparatorIN10reflection4EnumEEEPNS1_6OffsetIS5_EEEEjT0_SB_SB_SB_T_
              (uint *param_1,uint *param_2,uint *param_3,uint *param_4,long *param_5)

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
  
                    /* catch() { ... } // from try @ 00b3cd14 with catch @ 00b3cdd8 */
                    /* catch() { ... } // from try @ 00b3cd9c with catch @ 00b3cddc */
  iVar10 = _ZNSt6__ndk17__sort3IRN11flatbuffers17FlatBufferBuilder18TableKeyComparatorIN10reflection4EnumEEEPNS1_6OffsetIS5_EEEEjT0_SB_SB_T_
                     ();
  uVar5 = *param_4;
  uVar6 = *param_3;
  lVar1 = *(long *)(*param_5 + 0x28) + *(long *)(*param_5 + 0x20);
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
        iVar10 = iVar10 + 3;
        *param_1 = uVar5;
        *param_2 = uVar6;
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
