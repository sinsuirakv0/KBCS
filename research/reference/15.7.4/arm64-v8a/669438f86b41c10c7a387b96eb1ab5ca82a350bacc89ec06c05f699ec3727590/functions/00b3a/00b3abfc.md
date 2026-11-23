# 00b3abfc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00b3abb8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3a/00b3abb8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/97ee0756e9de6c746e3ce399/1-2/inspection-0010.md#compare-071dc8853389ceddc262c7ade37b6d52)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 構造資料不足
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b3abfc",
  "name": "_ZNSt6__ndk118__insertion_sort_3IRN11flatbuffers17FlatBufferBuilder18TableKeyComparatorIN10reflection5FieldEEEPNS1_6OffsetIS5_EEEEvT0_SB_T_",
  "size": 412,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8d0b5ba62b02d7258667cfd3b10f9570bd677861b13b3977169277ef915730ce",
  "source_text_sha256": "8d0b5ba62b02d7258667cfd3b10f9570bd677861b13b3977169277ef915730ce"
}
~~~

## 呼び出し元

- [00bdfd40](../00bdf/00bdfd40.md)

## 呼び出し先

- [00bdb200](../00bdb/00bdb200.md)
- [00be0100](../00be0/00be0100.md)

## 疑似コード / UTF-8 2890 bytes

~~~c

void _ZNSt6__ndk118__insertion_sort_3IRN11flatbuffers17FlatBufferBuilder18TableKeyComparatorIN10reflection5FieldEEEPNS1_6OffsetIS5_EEEEvT0_SB_T_
               (uint *param_1,uint *param_2,long *param_3)

{
  long lVar1;
  uint uVar2;
  uint uVar3;
  uint uVar4;
  uint uVar5;
  long lVar6;
  bool bVar7;
  int iVar8;
  uint *puVar9;
  uint *puVar10;
  int *piVar11;
  long lVar12;
  uint *puVar13;
  long lVar14;
  int *piVar15;
  ulong uVar16;
  
  _ZNSt6__ndk17__sort3IRN11flatbuffers17FlatBufferBuilder18TableKeyComparatorIN10reflection5FieldEEEPNS1_6OffsetIS5_EEEEjT0_SB_SB_T_
            (param_1,param_1 + 1,param_1 + 2,param_3);
  if (param_1 + 3 != param_2) {
    lVar14 = 0xc;
    lVar1 = *(long *)(*param_3 + 0x28) + *(long *)(*param_3 + 0x20);
    puVar9 = param_1 + 3;
    puVar13 = param_1 + 2;
    do {
      puVar10 = puVar9;
      uVar3 = *puVar10;
      uVar16 = (ulong)*puVar13;
      piVar15 = (int *)(lVar1 - (ulong)uVar3);
      piVar11 = (int *)(lVar1 - uVar16);
      puVar9 = (uint *)((long)piVar15 + (ulong)*(ushort *)((long)piVar15 + (4 - (long)*piVar15)));
      puVar13 = (uint *)((long)piVar11 + (ulong)*(ushort *)((long)piVar11 + (4 - (long)*piVar11)));
      puVar9 = (uint *)((long)puVar9 + (ulong)*puVar9);
      puVar13 = (uint *)((long)puVar13 + (ulong)*puVar13);
      uVar4 = *puVar9;
      uVar5 = *puVar13;
      uVar2 = uVar5;
      if (uVar4 <= uVar5) {
        uVar2 = uVar4;
      }
      iVar8 = memcmp(puVar9 + 1,puVar13 + 1,(ulong)uVar2);
      bVar7 = uVar4 < uVar5;
      if (iVar8 != 0) {
        bVar7 = iVar8 < 0;
      }
      lVar12 = lVar14;
      if (bVar7) {
        do {
          lVar6 = lVar12 + -4;
          *(int *)((long)param_1 + lVar12) = (int)uVar16;
          puVar9 = param_1;
          if (lVar6 == 0) goto LAB_00b3ac64;
          uVar16 = (ulong)*(uint *)((long)param_1 + lVar12 + -8);
          piVar11 = (int *)(lVar1 - uVar16);
          puVar9 = (uint *)((long)piVar15 + (ulong)*(ushort *)((long)piVar15 + (4 - (long)*piVar15))
                           );
          puVar13 = (uint *)((long)piVar11 +
                            (ulong)*(ushort *)((long)piVar11 + (4 - (long)*piVar11)));
          puVar9 = (uint *)((long)puVar9 + (ulong)*puVar9);
          uVar4 = *puVar9;
          puVar13 = (uint *)((long)puVar13 + (ulong)*puVar13);
          uVar5 = *puVar13;
          uVar2 = uVar5;
          if (uVar4 <= uVar5) {
            uVar2 = uVar4;
          }
          iVar8 = memcmp(puVar9 + 1,puVar13 + 1,(ulong)uVar2);
          bVar7 = uVar4 < uVar5;
          if (iVar8 != 0) {
            bVar7 = iVar8 < 0;
          }
          lVar12 = lVar6;
        } while (bVar7);
        puVar9 = (uint *)((long)param_1 + lVar6);
LAB_00b3ac64:
        *puVar9 = uVar3;
      }
      lVar14 = lVar14 + 4;
      puVar9 = puVar10 + 1;
      puVar13 = puVar10;
    } while (puVar10 + 1 != param_2);
  }
  return;
}

~~~
