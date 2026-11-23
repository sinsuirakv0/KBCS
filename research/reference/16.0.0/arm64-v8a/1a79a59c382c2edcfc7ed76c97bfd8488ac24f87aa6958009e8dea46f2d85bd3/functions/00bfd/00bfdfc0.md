# 00bfdfc0

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b81578`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81578.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/2-3/priority-0072.md#compare-7dcb2d71e0cb5b5272999435266360c9)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 構造資料不足
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

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
