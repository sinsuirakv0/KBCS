# 00ad6cbc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00ad6c78`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad6/00ad6c78.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/97ee0756e9de6c746e3ce399/1-2/priority-0060.md#compare-3e466af34811ab1f44532edee0fec0a5)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 構造資料不足
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ad6cbc",
  "name": "FUN_00ad6cbc",
  "size": 200,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "77d516ce3fa9a5f3bb0b7e53db8c3df7136093a5fb7d2df579acd6cfc776d686",
  "source_text_sha256": "77d516ce3fa9a5f3bb0b7e53db8c3df7136093a5fb7d2df579acd6cfc776d686"
}
~~~

## 呼び出し元

- [0058cea4](../0058c/0058cea4.md)

## 呼び出し先

- [00ad4a94](../00ad4/00ad4a94.md)
- [00bdb090](../00bdb/00bdb090.md)

## 疑似コード / UTF-8 914 bytes

~~~c

void FUN_00ad6cbc(long *param_1)

{
  long lVar1;
  long *plVar2;
  long *plVar3;
  long lVar4;
  long local_60 [4];
  long *local_40;
  long local_28;
  
  local_40 = local_60;
  plVar2 = local_60;
  lVar1 = tpidr_el0;
  local_28 = *(long *)(lVar1 + 0x28);
  plVar3 = (long *)param_1[4];
  if (plVar3 == (long *)0x0) {
    local_40 = (long *)0x0;
  }
  else if (plVar3 == param_1) {
    (**(code **)(*param_1 + 0x18))(param_1,local_60);
  }
  else {
    local_40 = (long *)(**(code **)(*plVar3 + 0x10))(plVar3);
  }
  FUN_00ad4a94(local_60,&DAT_0109fda0);
  if (local_40 == local_60) {
    lVar4 = 0x20;
  }
  else {
    if (local_40 == (long *)0x0) goto LAB_00ad6d60;
    lVar4 = 0x28;
    plVar2 = local_40;
  }
  (**(code **)(*plVar2 + lVar4))();
LAB_00ad6d60:
  if (*(long *)(lVar1 + 0x28) == local_28) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
