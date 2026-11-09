# 00bfdfc0

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bfdfc0",
  "name": "_ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE7putbackEc",
  "size": 228,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b4f646a7221fc9a64369924e393fc876dc06b1d0f11148d250f65262b370dedb",
  "source_text_sha256": "b4f646a7221fc9a64369924e393fc876dc06b1d0f11148d250f65262b370dedb"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57ea0](../00c57/00c57ea0.md)
- [00c599d0](../00c59/00c599d0.md)

## 疑似コード / UTF-8 1120 bytes

~~~c

long * _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE7putbackEc(long *param_1,char param_2)

{
  int iVar1;
  long *plVar2;
  char *pcVar3;
  long lVar4;
  uint uVar5;
  char local_14 [4];
  
  lVar4 = *(long *)(*param_1 + -0x18);
  param_1[1] = 0;
  uVar5 = *(uint *)((long)param_1 + lVar4 + 0x20) & 0xfffffffd;
  _ZNSt6__ndk18ios_base5clearEj((long)param_1 + *(long *)(*param_1 + -0x18),uVar5);
  _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE6sentryC1ERS3_b(local_14,param_1,1);
  if (local_14[0] == '\0') {
    uVar5 = uVar5 | 4;
    goto LAB_00bfe074;
  }
  plVar2 = *(long **)((long)param_1 + *(long *)(*param_1 + -0x18) + 0x28);
  if (plVar2 != (long *)0x0) {
    if ((plVar2[2] != plVar2[3]) && (pcVar3 = (char *)(plVar2[3] + -1), *pcVar3 == param_2)) {
      plVar2[3] = (long)pcVar3;
      goto LAB_00bfe074;
    }
    iVar1 = (**(code **)(*plVar2 + 0x58))(plVar2,param_2);
    if (iVar1 != -1) goto LAB_00bfe074;
  }
  uVar5 = uVar5 | 1;
LAB_00bfe074:
  lVar4 = (long)param_1 + *(long *)(*param_1 + -0x18);
  _ZNSt6__ndk18ios_base5clearEj(lVar4,*(uint *)(lVar4 + 0x20) | uVar5);
  return param_1;
}

~~~
