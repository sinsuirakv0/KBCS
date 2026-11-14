# 00bacf0c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bacf0c",
  "name": "_ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers9StructDefEEENS_19__map_value_compareIS7_SB_NS_4lessIS7_EELb1EEENS5_ISB_EEE12__find_equalIS7_EERPNS_16__tree_node_baseIPvEERPNS_15__tree_end_nodeISM_EERKT_",
  "size": 288,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0cba7ac6ae23aeee96b33b6a5c331da7312a356356d67126b50ef94f6cbd4525",
  "source_text_sha256": "0cba7ac6ae23aeee96b33b6a5c331da7312a356356d67126b50ef94f6cbd4525"
}
~~~

## 呼び出し元

- [00c5e020](../00c5e/00c5e020.md)

## 呼び出し先

- [00c590f0](../00c59/00c590f0.md)

## 疑似コード / UTF-8 4283 bytes

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
  
                    /* catch() { ... } // from try @ 00baba88 with catch @ 00bacf10 */
                    /* catch() { ... } // from try @ 00bab8ec with catch @ 00bacf14 */
                    /* catch() { ... } // from try @ 00bab690 with catch @ 00bacf18 */
                    /* catch() { ... } // from try @ 00baaea8 with catch @ 00bacf1c */
                    /* catch() { ... } // from try @ 00baba64 with catch @ 00bacf20 */
  plVar5 = (long *)(param_1 + 8);
  plVar6 = (long *)*plVar5;
                    /* catch() { ... } // from try @ 00bab8c8 with catch @ 00bacf30 */
  if (plVar6 == (long *)0x0) {
    *param_2 = plVar5;
                    /* catch() { ... } // from try @ 00bab80c with catch @ 00bad020 */
    return plVar5;
                    /* catch() { ... } // from try @ 00bab9a8 with catch @ 00bad000 */
  }
  uVar2 = *(ulong *)(param_3 + 8);
  __s1 = *(byte **)(param_3 + 0x10);
                    /* catch() { ... } // from try @ 00bab66c with catch @ 00bacf40 */
  plVar5 = (long *)(param_1 + 8);
  if ((*param_3 & 1) == 0) {
                    /* catch() { ... } // from try @ 00baae88 with catch @ 00bacf50 */
    __s1 = param_3 + 1;
    uVar2 = (ulong)(*param_3 >> 1);
  }
  do {
    while( true ) {
                    /* catch() { ... } // from try @ 00baba14 with catch @ 00bacf70 */
      plVar7 = plVar6;
      bVar3 = *(byte *)(plVar7 + 4);
                    /* catch() { ... } // from try @ 00bab878 with catch @ 00bacf80 */
      uVar1 = (ulong)(bVar3 >> 1);
      if ((bVar3 & 1) != 0) {
        uVar1 = plVar7[5];
      }
      __n = uVar1;
      if (uVar2 <= uVar1) {
        __n = uVar2;
      }
                    /* catch() { ... } // from try @ 00bab61c with catch @ 00bacf90 */
      if (__n == 0) break;
      __s1_00 = (void *)plVar7[6];
      __s2 = __s1_00;
                    /* catch() { ... } // from try @ 00baae38 with catch @ 00bacfa0 */
      if ((bVar3 & 1) == 0) {
        __s2 = (void *)((long)plVar7 + 0x21);
      }
      iVar4 = memcmp(__s1,__s2,__n);
      if (iVar4 == 0) break;
                    /* catch() { ... } // from try @ 00bab9e8 with catch @ 00bacfb0 */
      if (iVar4 < 0) goto LAB_00bacfc0;
LAB_00bacfd8:
      if ((bVar3 & 1) == 0) {
        __s1_00 = (void *)((long)plVar7 + 0x21);
      }
                    /* catch() { ... } // from try @ 00bab5d0 with catch @ 00bacfe0 */
      iVar4 = memcmp(__s1_00,__s1,__n);
      if (iVar4 == 0) goto LAB_00bacf58;
                    /* catch() { ... } // from try @ 00baadec with catch @ 00bacff0 */
      if (-1 < iVar4) goto LAB_00bacff4;
LAB_00bacf60:
      plVar5 = plVar7 + 1;
                    /* catch() { ... } // from try @ 00baba38 with catch @ 00bacf60 */
                    /* catch() { ... } // from try @ 00bab89c with catch @ 00bacf64 */
                    /* catch() { ... } // from try @ 00bab640 with catch @ 00bacf68 */
      plVar6 = (long *)*plVar5;
      if ((long *)*plVar5 == (long *)0x0) {
LAB_00bacff4:
        *param_2 = plVar7;
        return plVar5;
      }
    }
                    /* catch() { ... } // from try @ 00bab5f0 with catch @ 00bacfb8 */
                    /* catch() { ... } // from try @ 00baae0c with catch @ 00bacfbc */
    if (uVar1 <= uVar2) {
                    /* catch() { ... } // from try @ 00bab82c with catch @ 00bacfd0 */
      if (__n != 0) {
        __s1_00 = (void *)plVar7[6];
        goto LAB_00bacfd8;
      }
LAB_00bacf58:
      if (uVar2 <= uVar1) goto LAB_00bacff4;
      goto LAB_00bacf60;
    }
LAB_00bacfc0:
                    /* catch() { ... } // from try @ 00bab9c8 with catch @ 00bacfc0 */
    plVar5 = plVar7;
    plVar6 = (long *)*plVar7;
    if ((long *)*plVar7 == (long *)0x0) {
      *param_2 = plVar7;
      return plVar7;
    }
  } while( true );
}

~~~
