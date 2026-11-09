# 00bafc4c

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bafc4c",
  "name": "_ZN11flexbuffers7Builder3KeyEPKcm",
  "size": 336,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "856686002a95dcad79afd5d7bebac587d267c1a4b13760f4de3ee22584931245",
  "source_text_sha256": "856686002a95dcad79afd5d7bebac587d267c1a4b13760f4de3ee22584931245"
}
~~~

## 呼び出し元

- [00c5c4c0](../00c5c/00c5c4c0.md)

## 呼び出し先

- [00b994c4](../00b99/00b994c4.md)
- [00c57ae0](../00c57/00c57ae0.md)
- [00c5b260](../00c5b/00c5b260.md)
- [00c5b450](../00c5b/00c5b450.md)
- [00c5cbe0](../00c5c/00c5cbe0.md)
- [00c5cc80](../00c5c/00c5cc80.md)

## 疑似コード / UTF-8 2474 bytes

~~~c

void _ZN11flexbuffers7Builder3KeyEPKcm(long *param_1,long param_2,long param_3)

{
  long lVar1;
  int iVar2;
  ulong uVar3;
  ulong uVar4;
  long *plVar5;
  long *plVar6;
  ulong uVar7;
  long *plVar8;
  long lVar9;
  ulong local_70;
  undefined8 local_68;
  ulong local_60;
  long local_58;
  
                    /* try { // try from 00bafc5c to 00cafd13 has its CatchHandler @ 00baf838 */
  lVar1 = tpidr_el0;
  local_58 = *(long *)(lVar1 + 0x28);
  uVar4 = param_1[1] - *param_1;
  local_60 = uVar4;
  _ZNSt6__ndk16vectorIhNS_9allocatorIhEEE6insertIPKhEENS_9enable_ifIXaasr21__is_forward_iteratorIT_EE5valuesr16is_constructibleIhNS_15iterator_traitsIS8_E9referenceEEE5valueENS_11__wrap_iterIPhEEE4typeENSC_IS6_EES8_S8_
            (param_1,param_1[1],param_2,param_3 + param_2 + 1);
  uVar7 = uVar4;
  if ((*(byte *)((long)param_1 + 0x34) & 1) != 0) {
    plVar6 = param_1 + 9;
    plVar8 = (long *)*plVar6;
    if (plVar8 != (long *)0x0) {
      lVar9 = *(long *)param_1[0xb];
      plVar5 = plVar6;
      do {
        iVar2 = strcmp((char *)(lVar9 + plVar8[4]),(char *)(lVar9 + uVar4));
        if (iVar2 >= 0) {
          plVar5 = plVar8;
        }
        plVar8 = (long *)plVar8[iVar2 < 0];
      } while (plVar8 != (long *)0x0);
      if (plVar5 != plVar6) {
        uVar7 = plVar5[4];
        iVar2 = strcmp((char *)(lVar9 + uVar4),(char *)(lVar9 + uVar7));
        if (-1 < iVar2) {
          uVar3 = param_1[1] - *param_1;
          if (uVar4 < uVar3 || uVar4 - uVar3 == 0) {
            local_60 = uVar7;
            if (uVar4 < uVar3) {
              param_1[1] = *param_1 + uVar4;
            }
          }
          else {
            _ZNSt6__ndk16vectorIhNS_9allocatorIhEEE8__appendEm(param_1,uVar4 - uVar3);
            uVar7 = plVar5[4];
            local_60 = uVar7;
          }
          goto LAB_00bafd14;
        }
      }
    }
    _ZNSt6__ndk16__treeImN11flexbuffers7Builder16KeyOffsetCompareENS_9allocatorImEEE25__emplace_unique_key_argsImJRKmEEENS_4pairINS_15__tree_iteratorImPNS_11__tree_nodeImPvEElEEbEERKT_DpOT0_
              (param_1 + 8,&local_60,&local_60);
    uVar7 = local_60;
  }
LAB_00bafd14:
                    /* try { // try from 00bafd14 to 00cafd1b has its CatchHandler @ 00bafe10 */
  local_68 = DAT_002c42c0;
  local_70 = uVar7;
  FUN_00b994c4(param_1 + 3,&local_70);
  if (*(long *)(lVar1 + 0x28) != local_58) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail(local_60);
  }
  return;
}

~~~
