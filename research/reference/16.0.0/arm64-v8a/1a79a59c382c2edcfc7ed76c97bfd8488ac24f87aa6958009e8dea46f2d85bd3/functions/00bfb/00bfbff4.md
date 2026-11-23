# 00bfbff4

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b7f5ac`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f5ac.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/2-3/priority-0072.md#compare-c2150d99161d3f6c9ce0503236ee3675)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 構造資料不足
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfbff4",
  "name": "_ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEErsEPNS_15basic_streambufIcS2_EE",
  "size": 344,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "12e9ee9e58086e4d6c02119e934d964aa1db42503e5e86bcbd17af440971ffdd",
  "source_text_sha256": "12e9ee9e58086e4d6c02119e934d964aa1db42503e5e86bcbd17af440971ffdd"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57ea0](../00c57/00c57ea0.md)
- [00c599d0](../00c59/00c599d0.md)

## 疑似コード / UTF-8 1697 bytes

~~~c

long * _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEErsEPNS_15basic_streambufIcS2_EE
                 (long *param_1,long *param_2)

{
  long lVar1;
  undefined1 *puVar2;
  uint uVar3;
  int iVar4;
  long *plVar5;
  uint uVar6;
  char local_34 [4];
  
  param_1[1] = 0;
  _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE6sentryC1ERS3_b(local_34,param_1,1);
  if (local_34[0] == '\0') {
    return param_1;
  }
  if (param_2 != (long *)0x0) {
LAB_00bfc060:
    plVar5 = *(long **)((long)param_1 + *(long *)(*param_1 + -0x18) + 0x28);
    if ((byte *)plVar5[3] == (byte *)plVar5[4]) {
      uVar3 = (**(code **)(*plVar5 + 0x48))();
      if (uVar3 == 0xffffffff) {
        uVar3 = 2;
        goto LAB_00bfc108;
      }
    }
    else {
      uVar3 = (uint)*(byte *)plVar5[3];
    }
    puVar2 = (undefined1 *)param_2[6];
    if (puVar2 == (undefined1 *)param_2[7]) {
      iVar4 = (**(code **)(*param_2 + 0x68))(param_2,uVar3 & 0xff);
      if (iVar4 == -1) goto LAB_00bfc104;
    }
    else {
      param_2[6] = (long)(puVar2 + 1);
      *puVar2 = (char)uVar3;
    }
    if (param_1[1] != 0x7fffffffffffffff) {
      param_1[1] = param_1[1] + 1;
    }
    plVar5 = *(long **)((long)param_1 + *(long *)(*param_1 + -0x18) + 0x28);
    if (plVar5[3] == plVar5[4]) {
      (**(code **)(*plVar5 + 0x50))();
    }
    else {
      plVar5[3] = plVar5[3] + 1;
    }
    goto LAB_00bfc060;
  }
  uVar6 = 4;
LAB_00bfc118:
  lVar1 = (long)param_1 + *(long *)(*param_1 + -0x18);
  _ZNSt6__ndk18ios_base5clearEj(lVar1,*(uint *)(lVar1 + 0x20) | uVar6);
  return param_1;
LAB_00bfc104:
  uVar3 = 0;
LAB_00bfc108:
  uVar6 = uVar3 | 4;
  if (param_1[1] != 0) {
    uVar6 = uVar3;
  }
  goto LAB_00bfc118;
}

~~~
