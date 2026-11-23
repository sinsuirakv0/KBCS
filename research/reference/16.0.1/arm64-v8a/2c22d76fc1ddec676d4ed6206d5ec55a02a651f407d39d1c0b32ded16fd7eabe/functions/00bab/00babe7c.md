# 00babe7c

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00baba54`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bab/00baba54.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/priority-0078.md#compare-a7937db785484c6f53db0f1987149039)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/priority-0087.md#compare-0f03fbca9717c2c20ca42c6ffc00095d)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00babe7c",
  "name": "_ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers9StructDefEEENS_19__map_value_compareIS7_SB_NS_4lessIS7_EELb1EEENS5_ISB_EEE12__find_equalIS7_EERPNS_16__tree_node_baseIPvEERPNS_15__tree_end_nodeISM_EERKT_",
  "size": 288,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b8649d53eace244423d68236fd3a8285bddc68a18fad11d9acd56f0cdaf472d9",
  "source_text_sha256": "b8649d53eace244423d68236fd3a8285bddc68a18fad11d9acd56f0cdaf472d9"
}
~~~

## 呼び出し元

- [00c5cf80](../00c5c/00c5cf80.md)

## 呼び出し先

- [00c58050](../00c58/00c58050.md)

## 疑似コード / UTF-8 4457 bytes

~~~c

long * _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers9StructDefEEENS_19__map_value_compareIS7_SB_NS_4lessIS7_EELb1EEENS5_ISB_EEE12__find_equalIS7_EERPNS_16__tree_node_baseIPvEERPNS_15__tree_end_nodeISM_EERKT_
                 (long param_1,undefined8 *param_2,byte *param_3)

{
  ulong uVar1;
  size_t __n;
  void *__s2;
  ulong uVar2;
  byte *__s1;
  byte bVar3;
  int iVar4;
  long *plVar5;
  long *plVar6;
  long *plVar7;
  void *__s1_00;
  
                    /* catch() { ... } // from try @ 00baa6d0 with catch @ 00babe84 */
                    /* catch() { ... } // from try @ 00baa6b0 with catch @ 00babe88 */
                    /* catch() { ... } // from try @ 00baa67c with catch @ 00babe98 */
                    /* catch() { ... } // from try @ 00baa658 with catch @ 00babe9c */
  plVar5 = (long *)(param_1 + 8);
  plVar6 = (long *)*plVar5;
  if (plVar6 == (long *)0x0) {
                    /* catch() { ... } // from try @ 00baa7c8 with catch @ 00babf6c */
    *param_2 = plVar5;
                    /* catch() { ... } // from try @ 00baa56c with catch @ 00babf7c */
                    /* catch() { ... } // from try @ 00ba9d88 with catch @ 00babf8c */
    return plVar5;
  }
                    /* catch() { ... } // from try @ 00baaa24 with catch @ 00babeac */
  uVar2 = *(ulong *)(param_3 + 8);
  __s1 = *(byte **)(param_3 + 0x10);
                    /* catch() { ... } // from try @ 00baa888 with catch @ 00babeb0 */
                    /* catch() { ... } // from try @ 00baa62c with catch @ 00babeb4 */
                    /* catch() { ... } // from try @ 00ba9e44 with catch @ 00babeb8 */
  plVar5 = (long *)(param_1 + 8);
                    /* catch() { ... } // from try @ 00baaa00 with catch @ 00babebc */
  if ((*param_3 & 1) == 0) {
    __s1 = param_3 + 1;
    uVar2 = (ulong)(*param_3 >> 1);
  }
  do {
    while( true ) {
      plVar7 = plVar6;
      bVar3 = *(byte *)(plVar7 + 4);
                    /* catch() { ... } // from try @ 00ba9e24 with catch @ 00babeec */
      uVar1 = (ulong)(bVar3 >> 1);
      if ((bVar3 & 1) != 0) {
        uVar1 = plVar7[5];
      }
      __n = uVar1;
                    /* catch() { ... } // from try @ 00baa9d4 with catch @ 00babefc */
      if (uVar2 <= uVar1) {
        __n = uVar2;
      }
                    /* catch() { ... } // from try @ 00baa838 with catch @ 00babf00 */
      if (__n == 0) break;
                    /* catch() { ... } // from try @ 00baa5dc with catch @ 00babf04 */
      __s1_00 = (void *)plVar7[6];
                    /* catch() { ... } // from try @ 00ba9df8 with catch @ 00babf08 */
      __s2 = __s1_00;
                    /* catch() { ... } // from try @ 00baa9b0 with catch @ 00babf0c */
      if ((bVar3 & 1) == 0) {
        __s2 = (void *)((long)plVar7 + 0x21);
      }
      iVar4 = memcmp(__s1,__s2,__n);
                    /* catch() { ... } // from try @ 00baa814 with catch @ 00babf1c */
      if (iVar4 == 0) break;
      if (iVar4 < 0) goto LAB_00babf30;
LAB_00babf48:
                    /* catch() { ... } // from try @ 00baa984 with catch @ 00babf4c */
      if ((bVar3 & 1) == 0) {
        __s1_00 = (void *)((long)plVar7 + 0x21);
      }
                    /* catch() { ... } // from try @ 00baa7e8 with catch @ 00babf50 */
                    /* catch() { ... } // from try @ 00baa58c with catch @ 00babf54 */
                    /* catch() { ... } // from try @ 00ba9da8 with catch @ 00babf58 */
      iVar4 = memcmp(__s1_00,__s1,__n);
                    /* catch() { ... } // from try @ 00baa964 with catch @ 00babf5c */
      if (iVar4 == 0) goto LAB_00babec8;
      if (-1 < iVar4) goto LAB_00babf64;
LAB_00babed0:
      plVar5 = plVar7 + 1;
      plVar6 = (long *)*plVar5;
      if ((long *)*plVar5 == (long *)0x0) {
LAB_00babf64:
        *param_2 = plVar7;
        return plVar5;
      }
    }
                    /* catch() { ... } // from try @ 00baa5b8 with catch @ 00babf2c */
    if (uVar1 <= uVar2) {
      if (__n != 0) {
        __s1_00 = (void *)plVar7[6];
        goto LAB_00babf48;
      }
LAB_00babec8:
                    /* catch() { ... } // from try @ 00baa864 with catch @ 00babecc */
      if (uVar2 <= uVar1) goto LAB_00babf64;
      goto LAB_00babed0;
    }
LAB_00babf30:
    plVar5 = plVar7;
    plVar6 = (long *)*plVar7;
    if ((long *)*plVar7 == (long *)0x0) {
      *param_2 = plVar7;
      return plVar7;
    }
  } while( true );
}

~~~
