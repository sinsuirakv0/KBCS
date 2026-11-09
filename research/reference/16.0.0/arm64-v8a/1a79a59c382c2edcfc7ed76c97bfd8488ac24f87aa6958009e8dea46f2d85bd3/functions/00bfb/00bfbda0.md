# 00bfbda0

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bfbda0",
  "name": "_ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE6sentryC1ERS3_b",
  "size": 452,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c28bee5ac4eab5e3005744132dccc7e909fe01ec43366ffaa5a27c1b495db617",
  "source_text_sha256": "c28bee5ac4eab5e3005744132dccc7e909fe01ec43366ffaa5a27c1b495db617"
}
~~~

## 呼び出し元

- [00c599d0](../00c59/00c599d0.md)

## 呼び出し先

- [00c57e70](../00c57/00c57e70.md)
- [00c57e80](../00c57/00c57e80.md)
- [00c57e90](../00c57/00c57e90.md)
- [00c57ea0](../00c57/00c57ea0.md)
- [00c58af0](../00c58/00c58af0.md)

## 疑似コード / UTF-8 2402 bytes

~~~c

void _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE6sentryC1ERS3_b
               (undefined1 *param_1,long *param_2,ulong param_3)

{
  byte bVar1;
  int iVar2;
  long lVar3;
  long lVar4;
  ulong uVar5;
  long *plVar6;
  undefined1 auStack_38 [8];
  
  lVar4 = *param_2;
  *param_1 = 0;
  lVar3 = (long)param_2 + *(long *)(lVar4 + -0x18);
  if (*(uint *)(lVar3 + 0x20) != 0) {
    _ZNSt6__ndk18ios_base5clearEj(lVar3,*(uint *)(lVar3 + 0x20) | 4);
    return;
  }
  if (*(long *)(lVar3 + 0x88) != 0) {
    param_3 = param_3 & 0xffffffff;
    _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEE5flushEv();
    lVar4 = *param_2;
  }
  if (((param_3 & 1) != 0) ||
     ((*(byte *)((long)param_2 + *(long *)(lVar4 + -0x18) + 9) >> 4 & 1) == 0)) {
LAB_00bfbf14:
    *param_1 = *(int *)((long)param_2 + *(long *)(lVar4 + -0x18) + 0x20) == 0;
    return;
  }
  _ZNKSt6__ndk18ios_base6getlocEv(auStack_38);
  lVar3 = _ZNKSt6__ndk16locale9use_facetERNS0_2idE
                    (auStack_38,PTR__ZNSt6__ndk15ctypeIcE2idE_00c9a830);
  _ZNSt6__ndk16localeD1Ev(auStack_38);
  plVar6 = *(long **)((long)param_2 + *(long *)(*param_2 + -0x18) + 0x28);
joined_r0x00bfbe54:
  if (plVar6 != (long *)0x0) {
    do {
      if ((plVar6[3] == plVar6[4]) && (iVar2 = (**(code **)(*plVar6 + 0x48))(plVar6), iVar2 == -1))
      break;
      if ((byte *)plVar6[3] == (byte *)plVar6[4]) {
        uVar5 = (**(code **)(*plVar6 + 0x48))(plVar6);
        uVar5 = uVar5 & 0xff;
        if ((uint)uVar5 >> 7 == 0) goto LAB_00bfbec4;
LAB_00bfbf04:
        if (plVar6[3] != plVar6[4]) goto LAB_00bfbf10;
        iVar2 = (**(code **)(*plVar6 + 0x48))(plVar6);
        lVar4 = *param_2;
        if (iVar2 != -1) goto LAB_00bfbf14;
        goto LAB_00bfbeec;
      }
      bVar1 = *(byte *)plVar6[3];
      uVar5 = (ulong)bVar1;
      if ((char)bVar1 < '\0') goto LAB_00bfbf04;
LAB_00bfbec4:
      if ((*(ulong *)(*(long *)(lVar3 + 0x10) + uVar5 * 8) & 1) == 0) goto LAB_00bfbf04;
      if (plVar6[3] != plVar6[4]) goto code_r0x00bfbedc;
      (**(code **)(*plVar6 + 0x50))(plVar6);
      if (plVar6 == (long *)0x0) break;
    } while( true );
  }
  lVar4 = *param_2;
LAB_00bfbeec:
  lVar3 = (long)param_2 + *(long *)(lVar4 + -0x18);
  _ZNSt6__ndk18ios_base5clearEj(lVar3,*(uint *)(lVar3 + 0x20) | 6);
LAB_00bfbf10:
  lVar4 = *param_2;
  goto LAB_00bfbf14;
code_r0x00bfbedc:
  plVar6[3] = plVar6[3] + 1;
  goto joined_r0x00bfbe54;
}

~~~
