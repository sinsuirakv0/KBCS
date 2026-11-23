# 00bafaec

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00baf6c4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00baf/00baf6c4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/alignment_unresolved-0009.md#compare-5805639db4419c957fef1e962bd51c4b)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/priority-0087.md#compare-e29e7383f86f994d31cb44160797d6e7)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bafaec",
  "name": "_ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers10ServiceDefEEENS_19__map_value_compareIS7_SB_NS_4lessIS7_EELb1EEENS5_ISB_EEE12__find_equalIS7_EERPNS_16__tree_node_baseIPvEERPNS_15__tree_end_nodeISM_EERKT_",
  "size": 288,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0b1cc717fd7456270472834adbab8244f39879a13fa7825d08faec7f92f89581",
  "source_text_sha256": "0b1cc717fd7456270472834adbab8244f39879a13fa7825d08faec7f92f89581"
}
~~~

## 呼び出し元

- [00c5ce60](../00c5c/00c5ce60.md)

## 呼び出し先

- [00c58050](../00c58/00c58050.md)

## 疑似コード / UTF-8 2585 bytes

~~~c

long * _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers10ServiceDefEEENS_19__map_value_compareIS7_SB_NS_4lessIS7_EELb1EEENS5_ISB_EEE12__find_equalIS7_EERPNS_16__tree_node_baseIPvEERPNS_15__tree_end_nodeISM_EERKT_
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
  
  plVar5 = (long *)(param_1 + 8);
  plVar6 = (long *)*plVar5;
  if (plVar6 == (long *)0x0) {
    *param_2 = plVar5;
    return plVar5;
  }
  uVar2 = *(ulong *)(param_3 + 8);
  __s1 = *(byte **)(param_3 + 0x10);
  plVar5 = (long *)(param_1 + 8);
  if ((*param_3 & 1) == 0) {
    __s1 = param_3 + 1;
    uVar2 = (ulong)(*param_3 >> 1);
  }
  do {
    while( true ) {
                    /* try { // try from 00bafb50 to 00cafb5f has its CatchHandler @ 00bb002c */
      plVar7 = plVar6;
      bVar3 = *(byte *)(plVar7 + 4);
                    /* try { // try from 00bafb60 to 00cafe57 has its CatchHandler @ 00bb0038 */
      uVar1 = (ulong)(bVar3 >> 1);
      if ((bVar3 & 1) != 0) {
        uVar1 = plVar7[5];
      }
      __n = uVar1;
      if (uVar2 <= uVar1) {
        __n = uVar2;
      }
      if (__n == 0) break;
      __s1_00 = (void *)plVar7[6];
      __s2 = __s1_00;
      if ((bVar3 & 1) == 0) {
        __s2 = (void *)((long)plVar7 + 0x21);
      }
      iVar4 = memcmp(__s1,__s2,__n);
      if (iVar4 == 0) break;
      if (iVar4 < 0) goto LAB_00bafba0;
LAB_00bafbb8:
      if ((bVar3 & 1) == 0) {
        __s1_00 = (void *)((long)plVar7 + 0x21);
      }
      iVar4 = memcmp(__s1_00,__s1,__n);
      if (iVar4 == 0) goto LAB_00bafb38;
      if (-1 < iVar4) goto LAB_00bafbd4;
LAB_00bafb40:
      plVar5 = plVar7 + 1;
                    /* try { // try from 00bafb44 to 00cafb4f has its CatchHandler @ 00bb0030 */
      plVar6 = (long *)*plVar5;
      if ((long *)*plVar5 == (long *)0x0) {
LAB_00bafbd4:
        *param_2 = plVar7;
        return plVar5;
      }
    }
    if (uVar1 <= uVar2) {
      if (__n != 0) {
        __s1_00 = (void *)plVar7[6];
        goto LAB_00bafbb8;
      }
LAB_00bafb38:
                    /* try { // try from 00bafb38 to 00cafb3f has its CatchHandler @ 00bb0034 */
      if (uVar2 <= uVar1) goto LAB_00bafbd4;
      goto LAB_00bafb40;
    }
LAB_00bafba0:
    plVar5 = plVar7;
    plVar6 = (long *)*plVar7;
    if ((long *)*plVar7 == (long *)0x0) {
      *param_2 = plVar7;
      return plVar7;
    }
  } while( true );
}

~~~
