# 00bffef4

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bffef4",
  "name": "_ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE6sentryC1ERS3_b",
  "size": 476,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "97fc733b2d7801eb2c1893d1a192f4a003aba6a01ea5d4bb6364dd9aec12926b",
  "source_text_sha256": "97fc733b2d7801eb2c1893d1a192f4a003aba6a01ea5d4bb6364dd9aec12926b"
}
~~~

## 呼び出し元

- [00c5e020](../00c5e/00c5e020.md)

## 呼び出し先

- [00c57e70](../00c57/00c57e70.md)
- [00c57e80](../00c57/00c57e80.md)
- [00c57e90](../00c57/00c57e90.md)
- [00c57ea0](../00c57/00c57ea0.md)
- [00c5dff0](../00c5d/00c5dff0.md)

## 疑似コード / UTF-8 2464 bytes

~~~c

void _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE6sentryC1ERS3_b
               (undefined1 *param_1,long *param_2,ulong param_3)

{
  long lVar1;
  undefined4 uVar2;
  int iVar3;
  long *plVar4;
  ulong uVar5;
  long lVar6;
  long *plVar7;
  undefined1 auStack_38 [8];
  
  lVar6 = *param_2;
  *param_1 = 0;
  lVar1 = (long)param_2 + *(long *)(lVar6 + -0x18);
  if (*(uint *)(lVar1 + 0x20) != 0) {
    _ZNSt6__ndk18ios_base5clearEj(lVar1,*(uint *)(lVar1 + 0x20) | 4);
    return;
  }
  if (*(long *)(lVar1 + 0x88) != 0) {
    param_3 = param_3 & 0xffffffff;
    _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEE5flushEv();
    lVar6 = *param_2;
  }
  if (((param_3 & 1) == 0) &&
     ((*(byte *)((long)param_2 + *(long *)(lVar6 + -0x18) + 9) >> 4 & 1) != 0)) {
    _ZNKSt6__ndk18ios_base6getlocEv(auStack_38);
    plVar4 = (long *)_ZNKSt6__ndk16locale9use_facetERNS0_2idE
                               (auStack_38,PTR__ZNSt6__ndk15ctypeIwE2idE_00c9b740);
    _ZNSt6__ndk16localeD1Ev(auStack_38);
    plVar7 = *(long **)((long)param_2 + *(long *)(*param_2 + -0x18) + 0x28);
    while (plVar7 != (long *)0x0) {
      while( true ) {
        if ((int *)plVar7[3] == (int *)plVar7[4]) {
          iVar3 = (**(code **)(*plVar7 + 0x48))(plVar7);
        }
        else {
          iVar3 = *(int *)plVar7[3];
        }
        if (iVar3 == -1) goto LAB_00c00050;
        if ((undefined4 *)plVar7[3] == (undefined4 *)plVar7[4]) {
          uVar2 = (**(code **)(*plVar7 + 0x48))(plVar7);
        }
        else {
          uVar2 = *(undefined4 *)plVar7[3];
        }
        uVar5 = (**(code **)(*plVar4 + 0x18))(plVar4,1,uVar2);
        if ((uVar5 & 1) == 0) {
          if ((int *)plVar7[3] == (int *)plVar7[4]) {
            iVar3 = (**(code **)(*plVar7 + 0x48))(plVar7);
          }
          else {
            iVar3 = *(int *)plVar7[3];
          }
          lVar6 = *param_2;
          if (iVar3 != -1) goto LAB_00c0006c;
          goto LAB_00c00054;
        }
        if (plVar7[3] == plVar7[4]) break;
        plVar7[3] = plVar7[3] + 4;
        if (plVar7 == (long *)0x0) goto LAB_00c00050;
      }
      (**(code **)(*plVar7 + 0x50))(plVar7);
    }
LAB_00c00050:
    lVar6 = *param_2;
LAB_00c00054:
    lVar1 = (long)param_2 + *(long *)(lVar6 + -0x18);
    _ZNSt6__ndk18ios_base5clearEj(lVar1,*(uint *)(lVar1 + 0x20) | 6);
    lVar6 = *param_2;
  }
LAB_00c0006c:
  *param_1 = *(int *)((long)param_2 + *(long *)(lVar6 + -0x18) + 0x20) == 0;
  return;
}

~~~
