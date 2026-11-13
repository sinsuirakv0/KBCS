# 00bafff0

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00bafff0",
  "name": "_ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers7EnumDefEEENS_19__map_value_compareIS7_SB_NS_4lessIS7_EELb1EEENS5_ISB_EEE12__find_equalIS7_EERPNS_16__tree_node_baseIPvEERPNS_15__tree_end_nodeISM_EERKT_",
  "size": 288,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "fad5501724178bc0c309a5f5f4e65268501d570ff1d1aea09b2377ff1c246b74",
  "source_text_sha256": "fad5501724178bc0c309a5f5f4e65268501d570ff1d1aea09b2377ff1c246b74"
}
~~~

## 呼び出し元

- [00c5cf90](../00c5c/00c5cf90.md)

## 呼び出し先

- [00c58120](../00c58/00c58120.md)

## 疑似コード / UTF-8 2906 bytes

~~~c

long * _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers7EnumDefEEENS_19__map_value_compareIS7_SB_NS_4lessIS7_EELb1EEENS5_ISB_EEE12__find_equalIS7_EERPNS_16__tree_node_baseIPvEERPNS_15__tree_end_nodeISM_EERKT_
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
      plVar7 = plVar6;
      bVar3 = *(byte *)(plVar7 + 4);
                    /* try { // try from 00bb0060 to 00cb007b has its CatchHandler @ 00bb0098 */
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
                    /* catch() { ... } // from try @ 00baff80 with catch @ 00bb007c
                       try { // try from 00bb007c to 00cb00d3 has its CatchHandler @ 00bafaa4 */
      __s2 = __s1_00;
                    /* catch() { ... } // from try @ 00bafb50 with catch @ 00bb0080 */
      if ((bVar3 & 1) == 0) {
        __s2 = (void *)((long)plVar7 + 0x21);
      }
      iVar4 = memcmp(__s1,__s2,__n);
      if (iVar4 == 0) break;
      if (iVar4 < 0) goto LAB_00bb00a4;
LAB_00bb00bc:
      if ((bVar3 & 1) == 0) {
        __s1_00 = (void *)((long)plVar7 + 0x21);
      }
      iVar4 = memcmp(__s1_00,__s1,__n);
      if (iVar4 == 0) goto LAB_00bb003c;
      if (-1 < iVar4) goto LAB_00bb00d8;
LAB_00bb0044:
      plVar5 = plVar7 + 1;
      plVar6 = (long *)*plVar5;
      if ((long *)*plVar5 == (long *)0x0) {
LAB_00bb00d8:
        *param_2 = plVar7;
        return plVar5;
      }
    }
                    /* catch() { ... } // from try @ 00bafbc0 with catch @ 00bb009c */
                    /* catch() { ... } // from try @ 00bafbb4 with catch @ 00bb00a0 */
    if (uVar1 <= uVar2) {
      if (__n != 0) {
        __s1_00 = (void *)plVar7[6];
        goto LAB_00bb00bc;
      }
LAB_00bb003c:
      if (uVar2 <= uVar1) goto LAB_00bb00d8;
      goto LAB_00bb0044;
    }
LAB_00bb00a4:
                    /* catch() { ... } // from try @ 00bafba8 with catch @ 00bb00a4 */
                    /* catch() { ... } // from try @ 00bafbd0 with catch @ 00bb00a8 */
    plVar5 = plVar7;
    plVar6 = (long *)*plVar7;
    if ((long *)*plVar7 == (long *)0x0) {
      *param_2 = plVar7;
      return plVar7;
    }
  } while( true );
}

~~~
