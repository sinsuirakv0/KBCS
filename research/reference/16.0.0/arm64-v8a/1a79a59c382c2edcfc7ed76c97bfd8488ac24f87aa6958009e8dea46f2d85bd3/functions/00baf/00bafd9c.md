# 00bafd9c

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bafd9c",
  "name": "_ZNSt6__ndk16__treeImN11flexbuffers7Builder16KeyOffsetCompareENS_9allocatorImEEE25__emplace_unique_key_argsImJRKmEEENS_4pairINS_15__tree_iteratorImPNS_11__tree_nodeImPvEElEEbEERKT_DpOT0_",
  "size": 288,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b2066b8c6d49944fe838a7ca06d54e4ba743aedb37aaa4d55496c3bc81bbbbaf",
  "source_text_sha256": "b2066b8c6d49944fe838a7ca06d54e4ba743aedb37aaa4d55496c3bc81bbbbaf"
}
~~~

## 呼び出し元

- [00c5cbe0](../00c5c/00c5cbe0.md)

## 呼び出し先

- [00c57a90](../00c57/00c57a90.md)
- [00c5b1e0](../00c5b/00c5b1e0.md)
- [00c5b450](../00c5b/00c5b450.md)

## 疑似コード / UTF-8 2633 bytes

~~~c

undefined1  [16]
_ZNSt6__ndk16__treeImN11flexbuffers7Builder16KeyOffsetCompareENS_9allocatorImEEE25__emplace_unique_key_argsImJRKmEEENS_4pairINS_15__tree_iteratorImPNS_11__tree_nodeImPvEElEEbEERKT_DpOT0_
          (long *param_1,long *param_2,undefined8 *param_3)

{
  char *__s1;
  char *__s2;
  int iVar1;
  undefined8 *puVar2;
  undefined8 uVar3;
  undefined8 *puVar4;
  long *plVar5;
  long *plVar6;
  long *plVar7;
  long *plVar8;
  long lVar9;
  undefined1 auVar10 [16];
  
  plVar5 = param_1 + 1;
  plVar6 = (long *)*plVar5;
  plVar8 = plVar5;
  if (plVar6 != (long *)0x0) {
    lVar9 = *(long *)param_1[3];
    __s1 = (char *)(lVar9 + *param_2);
    plVar5 = param_1 + 1;
    do {
      while( true ) {
        plVar7 = plVar6;
        __s2 = (char *)(lVar9 + plVar7[4]);
        iVar1 = strcmp(__s1,__s2);
        plVar8 = plVar7;
        if (-1 < iVar1) break;
                    /* try { // try from 00bafdf4 to 00cafe0f has its CatchHandler @ 00bafe2c */
        plVar5 = plVar7;
        plVar6 = (long *)*plVar7;
        if ((long *)*plVar7 == (long *)0x0) {
          puVar4 = (undefined8 *)*plVar7;
          goto joined_r0x00bafe34;
        }
      }
                    /* catch() { ... } // from try @ 00bafd14 with catch @ 00bafe10
                       try { // try from 00bafe10 to 00cafe67 has its CatchHandler @ 00baf838 */
      iVar1 = strcmp(__s2,__s1);
                    /* catch() { ... } // from try @ 00baf8e4 with catch @ 00bafe14 */
      if (-1 < iVar1) break;
      plVar5 = plVar7 + 1;
      plVar6 = (long *)*plVar5;
    } while ((long *)*plVar5 != (long *)0x0);
  }
                    /* catch() { ... } // from try @ 00baf954 with catch @ 00bafe30 */
  puVar4 = (undefined8 *)*plVar5;
  plVar7 = plVar5;
joined_r0x00bafe34:
                    /* catch() { ... } // from try @ 00baf948 with catch @ 00bafe34 */
  if (puVar4 == (undefined8 *)0x0) {
    puVar4 = (undefined8 *)_Znwm(0x28);
    uVar3 = *param_3;
    *puVar4 = 0;
    puVar4[1] = 0;
    puVar4[2] = plVar8;
    puVar4[4] = uVar3;
    *plVar7 = (long)puVar4;
    puVar2 = puVar4;
    if (*(long *)*param_1 != 0) {
      *param_1 = *(long *)*param_1;
      puVar2 = (undefined8 *)*plVar7;
    }
    _ZNSt6__ndk127__tree_balance_after_insertIPNS_16__tree_node_baseIPvEEEEvT_S5_(param_1[1],puVar2)
    ;
    uVar3 = 1;
    param_1[2] = param_1[2] + 1;
  }
  else {
                    /* catch() { ... } // from try @ 00baf93c with catch @ 00bafe38 */
    uVar3 = 0;
                    /* catch() { ... } // from try @ 00baf964 with catch @ 00bafe3c */
  }
  auVar10._8_8_ = uVar3;
  auVar10._0_8_ = puVar4;
  return auVar10;
}

~~~
