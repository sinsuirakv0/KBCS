# 00bcaa0c

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b5b50c`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5b/00b5b50c.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/2-3/priority-0066.md#compare-fea2bfaa0b4950a158f97bc0db699d51)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 構造資料不足
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcaa0c",
  "name": "_ZN8firebase4auth4Auth20AddAuthStateListenerEPNS0_17AuthStateListenerE",
  "size": 436,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7001db8ca6205a502177ed7d5103b82795e7db2305a8d6f73ef57f98fd5e54b7",
  "source_text_sha256": "7001db8ca6205a502177ed7d5103b82795e7db2305a8d6f73ef57f98fd5e54b7"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57ae0](../00c57/00c57ae0.md)
- [00c5a600](../00c5a/00c5a600.md)
- [00c5a610](../00c5a/00c5a610.md)
- [00c5ac00](../00c5a/00c5ac00.md)
- [00c5d6f0](../00c5d/00c5d6f0.md)
- [00c5d710](../00c5d/00c5d710.md)

## 関連文字列（未確認候補）

~~~text
"listener_added == auth_added"
~~~

## 疑似コード / UTF-8 2525 bytes

~~~c

void _ZN8firebase4auth4Auth20AddAuthStateListenerEPNS0_17AuthStateListenerE
               (long *param_1,long *param_2)

{
  long *plVar1;
  undefined8 *puVar2;
  long lVar3;
  undefined8 *puVar4;
  long lVar5;
  bool bVar6;
  long lVar7;
  long *plVar8;
  undefined8 *puVar9;
  long *plVar10;
  long *local_58;
  long *plStack_50;
  long local_48;
  
  lVar5 = tpidr_el0;
  local_48 = *(long *)(lVar5 + 0x28);
  if (*param_1 == 0) goto LAB_00bcab94;
  lVar3 = *param_1 + 0x268;
  _ZN8firebase5Mutex7AcquireEv(lVar3);
  lVar7 = *param_1;
  plVar10 = *(long **)(lVar7 + 0x230);
  plVar8 = *(long **)(lVar7 + 0x238);
  local_58 = param_1;
  plStack_50 = param_2;
  if ((plVar10 == plVar8) || ((long *)*plVar10 == param_2)) {
    if (plVar10 == plVar8) goto LAB_00bcaaac;
LAB_00bcaa98:
    bVar6 = false;
  }
  else {
    do {
      if (plVar8 + -1 == plVar10) goto LAB_00bcaaac;
      plVar1 = plVar10 + 1;
      plVar10 = plVar10 + 1;
    } while ((long *)*plVar1 != param_2);
    if (plVar10 != plVar8) goto LAB_00bcaa98;
LAB_00bcaaac:
    if (plVar8 == *(long **)(lVar7 + 0x240)) {
      _ZNSt6__ndk16vectorIPN8firebase4auth17AuthStateListenerENS_9allocatorIS4_EEE21__push_back_slow_pathIRKS4_EEvOT_
                (lVar7 + 0x230,&plStack_50);
    }
    else {
      *plVar8 = (long)param_2;
      *(long **)(lVar7 + 0x238) = plVar8 + 1;
    }
    bVar6 = true;
  }
  puVar9 = (undefined8 *)param_2[1];
  puVar4 = (undefined8 *)param_2[2];
  if ((puVar9 == puVar4) || ((long *)*puVar9 == local_58)) {
    if (puVar9 == puVar4) goto LAB_00bcab2c;
LAB_00bcab18:
    if (bVar6) {
LAB_00bcab80:
      _ZN8firebase9LogAssertEPKcz("listener_added == auth_added");
    }
  }
  else {
    do {
      if (puVar4 + -1 == puVar9) goto LAB_00bcab2c;
      puVar2 = puVar9 + 1;
      puVar9 = puVar9 + 1;
    } while ((long *)*puVar2 != local_58);
    if (puVar9 != puVar4) goto LAB_00bcab18;
LAB_00bcab2c:
    if (puVar4 == (undefined8 *)param_2[3]) {
      _ZNSt6__ndk16vectorIPN8firebase4auth4AuthENS_9allocatorIS4_EEE21__push_back_slow_pathIRKS4_EEvOT_
                (param_2 + 1,&local_58);
    }
    else {
      *puVar4 = local_58;
      param_2[2] = (long)(puVar4 + 1);
    }
    if (!bVar6) goto LAB_00bcab80;
    if (*(char *)(*param_1 + 0x2b9) == '\0') {
      (**(code **)(*param_2 + 0x10))(param_2,param_1);
    }
  }
  _ZN8firebase5Mutex7ReleaseEv(lVar3);
LAB_00bcab94:
  if (*(long *)(lVar5 + 0x28) == local_48) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
