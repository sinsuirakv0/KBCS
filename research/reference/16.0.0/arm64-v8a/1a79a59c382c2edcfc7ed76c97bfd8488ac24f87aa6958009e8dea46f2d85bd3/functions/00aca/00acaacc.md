# 00acaacc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00a6cb38`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6c/00a6cb38.md) · 移動量 `+0x5df94`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/2-3/priority-0053.md#compare-c66c3596a503d389a26b91b025c04580)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 構造資料不足
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acaacc",
  "name": "FUN_00acaacc",
  "size": 228,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "655180e014d62fa3e0b6c30072214e8e53ae679e8ffc7c7d376b480c98455051",
  "source_text_sha256": "655180e014d62fa3e0b6c30072214e8e53ae679e8ffc7c7d376b480c98455051"
}
~~~

## 呼び出し元

- [006af35c](../006af/006af35c.md)
- [00830e5c](../00830/00830e5c.md)

## 呼び出し先

- [0057be68](../0057b/0057be68.md)
- [00ac9398](../00ac9/00ac9398.md)
- [00c57ae0](../00c57/00c57ae0.md)

## 疑似コード / UTF-8 1026 bytes

~~~c

void FUN_00acaacc(long param_1,long *param_2)

{
  long lVar1;
  long *plVar2;
  long *plVar3;
  long lVar4;
  long local_70 [4];
  long *local_50;
  long local_38;
  
  local_50 = local_70;
  plVar3 = local_70;
  lVar1 = tpidr_el0;
  local_38 = *(long *)(lVar1 + 0x28);
  plVar2 = (long *)param_2[4];
  *(undefined1 *)(param_1 + 0xa0) = 1;
  *(undefined4 *)(param_1 + 0xa4) = 0;
  if (plVar2 == (long *)0x0) {
    local_50 = (long *)0x0;
  }
  else if (plVar2 == param_2) {
    (**(code **)(*param_2 + 0x18))(param_2,local_70);
  }
  else {
    local_50 = (long *)(**(code **)(*plVar2 + 0x10))();
  }
  FUN_0057be68(local_70,param_1 + 0x140);
  if (local_50 == local_70) {
    lVar4 = 0x20;
  }
  else {
    if (local_50 == (long *)0x0) goto LAB_00acab80;
    lVar4 = 0x28;
    plVar3 = local_50;
  }
  (**(code **)(*plVar3 + lVar4))();
LAB_00acab80:
  FUN_00ac9398(param_1);
  if (*(long *)(lVar1 + 0x28) == local_38) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
