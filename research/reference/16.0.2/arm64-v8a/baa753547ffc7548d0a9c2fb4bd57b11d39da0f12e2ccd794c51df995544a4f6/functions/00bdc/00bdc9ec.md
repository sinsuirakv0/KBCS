# 00bdc9ec

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00bdc9ec",
  "name": "_ZNSt6__ndk16__treeINS_12__value_typeIN8firebase7VariantES3_EENS_19__map_value_compareIS3_S4_NS_4lessIS3_EELb1EEENS_9allocatorIS4_EEE12__find_equalIS3_EERPNS_16__tree_node_baseIPvEENS_21__tree_const_iteratorIS4_PNS_11__tree_nodeIS4_SE_EElEERPNS_15__tree_end_nodeISG_EESH_RKT_",
  "size": 556,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c75be2148c87863479f9b71a9730792395a7e4bac8c409eccf6536b9c9a7b4fb",
  "source_text_sha256": "c75be2148c87863479f9b71a9730792395a7e4bac8c409eccf6536b9c9a7b4fb"
}
~~~

## 呼び出し元

- [00c5df30](../00c5d/00c5df30.md)

## 呼び出し先

- [00c5b670](../00c5b/00c5b670.md)

## 疑似コード / UTF-8 4277 bytes

~~~c

long * _ZNSt6__ndk16__treeINS_12__value_typeIN8firebase7VariantES3_EENS_19__map_value_compareIS3_S4_NS_4lessIS3_EELb1EEENS_9allocatorIS4_EEE12__find_equalIS3_EERPNS_16__tree_node_baseIPvEENS_21__tree_const_iteratorIS4_PNS_11__tree_nodeIS4_SE_EElEERPNS_15__tree_end_nodeISG_EESH_RKT_
                 (long *param_1,long *param_2,long *param_3,long *param_4,undefined8 param_5)

{
  bool bVar1;
  ulong uVar2;
  long lVar3;
  long *plVar4;
  long *plVar5;
  long *plVar6;
  long *plVar7;
  
  plVar6 = param_1 + 1;
  if (plVar6 == param_2) {
LAB_00bdca38:
    plVar5 = param_2;
    if ((long *)*param_1 != param_2) {
      plVar7 = (long *)*param_2;
      plVar4 = param_2;
      if ((long *)*param_2 == (long *)0x0) {
        do {
          plVar5 = (long *)plVar4[2];
          bVar1 = (long *)*plVar5 == plVar4;
          plVar4 = plVar5;
        } while (bVar1);
      }
      else {
        do {
          plVar5 = plVar7;
          plVar7 = (long *)plVar5[1];
        } while ((long *)plVar5[1] != (long *)0x0);
      }
      uVar2 = _ZNK8firebase7VariantltERKS0_(plVar5 + 4,param_5);
      if ((uVar2 & 1) == 0) {
        if ((long *)*plVar6 != (long *)0x0) {
          plVar5 = param_1 + 1;
          plVar6 = (long *)*plVar6;
          do {
            while( true ) {
              plVar7 = plVar6;
              uVar2 = _ZNK8firebase7VariantltERKS0_(param_5,plVar7 + 4);
              if ((uVar2 & 1) == 0) break;
              plVar5 = plVar7;
              plVar6 = (long *)*plVar7;
              if ((long *)*plVar7 == (long *)0x0) goto LAB_00bdcb84;
            }
            uVar2 = _ZNK8firebase7VariantltERKS0_(plVar7 + 4,param_5);
            if ((uVar2 & 1) == 0) break;
            plVar5 = plVar7 + 1;
            plVar6 = (long *)*plVar5;
          } while ((long *)*plVar5 != (long *)0x0);
LAB_00bdcbe4:
          *param_3 = (long)plVar7;
          return plVar5;
        }
        goto LAB_00bdcbec;
      }
    }
    if (*param_2 == 0) {
      *param_3 = (long)param_2;
      plVar6 = param_2;
    }
    else {
      *param_3 = (long)plVar5;
      plVar6 = plVar5 + 1;
    }
  }
  else {
                    /* try { // try from 00bdca20 to 00cdca6f has its CatchHandler @ 00bdee44 */
    uVar2 = _ZNK8firebase7VariantltERKS0_(param_5,param_2 + 4);
    if ((uVar2 & 1) != 0) goto LAB_00bdca38;
    uVar2 = _ZNK8firebase7VariantltERKS0_(param_2 + 4,param_5);
    if ((uVar2 & 1) == 0) {
      *param_3 = (long)param_2;
      *param_4 = (long)param_2;
      return param_4;
    }
                    /* try { // try from 00bdca70 to 00cdcb47 has its CatchHandler @ 00bd6fbc */
    plVar5 = (long *)param_2[1];
    if (plVar5 == (long *)0x0) {
      plVar5 = param_2 + 2;
      plVar7 = (long *)*plVar5;
                    /* try { // try from 00bdcb48 to 00cdcb4f has its CatchHandler @ 00bdecfc */
      if ((long *)*plVar7 != param_2) {
        do {
          lVar3 = *plVar5;
                    /* try { // try from 00bdcb50 to 00cdcd03 has its CatchHandler @ 00bd6fbc */
          plVar5 = (long *)(lVar3 + 0x10);
          plVar7 = (long *)*plVar5;
        } while (*plVar7 != lVar3);
      }
    }
    else {
      do {
        plVar7 = plVar5;
        plVar5 = (long *)*plVar7;
      } while ((long *)*plVar7 != (long *)0x0);
    }
    if ((plVar7 == plVar6) ||
       (uVar2 = _ZNK8firebase7VariantltERKS0_(param_5,plVar7 + 4), (uVar2 & 1) != 0)) {
      if (param_2[1] == 0) {
        *param_3 = (long)param_2;
        return param_2 + 1;
      }
LAB_00bdcb84:
      *param_3 = (long)plVar7;
      return plVar7;
    }
    if ((long *)*plVar6 != (long *)0x0) {
      plVar5 = param_1 + 1;
      plVar6 = (long *)*plVar6;
      do {
        while( true ) {
          plVar7 = plVar6;
          uVar2 = _ZNK8firebase7VariantltERKS0_(param_5,plVar7 + 4);
          if ((uVar2 & 1) == 0) break;
          plVar5 = plVar7;
          plVar6 = (long *)*plVar7;
          if ((long *)*plVar7 == (long *)0x0) goto LAB_00bdcb84;
        }
        uVar2 = _ZNK8firebase7VariantltERKS0_(plVar7 + 4,param_5);
        if ((uVar2 & 1) == 0) break;
        plVar5 = plVar7 + 1;
        plVar6 = (long *)*plVar5;
      } while ((long *)*plVar5 != (long *)0x0);
      goto LAB_00bdcbe4;
    }
LAB_00bdcbec:
    *param_3 = (long)plVar6;
  }
  return plVar6;
}

~~~
