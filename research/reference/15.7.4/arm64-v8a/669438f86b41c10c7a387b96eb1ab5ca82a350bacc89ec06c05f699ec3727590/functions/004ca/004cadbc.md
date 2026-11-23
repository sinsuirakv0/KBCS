# 004cadbc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `004cadbc`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ca/004cadbc.md) · 移動量 `+0x0`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/97ee0756e9de6c746e3ce399/1-2/priority-0009.md#compare-90b7aedafbd67d1210397a1b67a583cd)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 構造資料不足
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "004cadbc",
  "name": "_ZN5Botan5PKCS88load_keyERNS_10DataSourceERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEE",
  "size": 244,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7f03daa5e3070a4ee5206e74777bde065328da6c7e488b1c394f7ee5cf3cbeef",
  "source_text_sha256": "7f03daa5e3070a4ee5206e74777bde065328da6c7e488b1c394f7ee5cf3cbeef"
}
~~~

## 呼び出し元

- [00bdc7e0](../00bdc/00bdc7e0.md)

## 呼び出し先

- [00418fe0](../00418/00418fe0.md)
- [004c9e38](../004c9/004c9e38.md)
- [005229d4](../00522/005229d4.md)
- [00bdb040](../00bdb/00bdb040.md)
- [00bdb060](../00bdb/00bdb060.md)
- [00bdb090](../00bdb/00bdb090.md)

## 疑似コード / UTF-8 1174 bytes

~~~c

void _ZN5Botan5PKCS88load_keyERNS_10DataSourceERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEE
               (undefined8 param_1,undefined8 param_2,ulong *param_3)

{
  long lVar1;
  long *plVar2;
  ulong local_90;
  ulong uStack_88;
  void *local_80;
  undefined1 auStack_70 [32];
  long *local_50;
  long local_38;
  
  lVar1 = tpidr_el0;
  local_38 = *(long *)(lVar1 + 0x28);
  if ((*param_3 & 1) == 0) {
    uStack_88 = param_3[1];
    local_90 = *param_3;
    local_80 = (void *)param_3[2];
  }
  else {
    FUN_00418fe0(&local_90,param_3[2],param_3[1]);
  }
  local_50 = (long *)0x0;
  plVar2 = (long *)_Znwm(0x20);
  *plVar2 = (long)&PTR_FUN_00bed560;
  if ((local_90 & 1) == 0) {
    plVar2[2] = uStack_88;
    plVar2[1] = local_90;
    plVar2[3] = (long)local_80;
  }
  else {
    FUN_00418fe0(plVar2 + 1,local_80,uStack_88);
  }
  local_50 = plVar2;
  FUN_004c9e38(param_1,param_2,auStack_70,1);
  (**(code **)(*plVar2 + 0x28))(plVar2);
  if ((local_90 & 1) != 0) {
    _ZdlPv(local_80);
  }
  if (*(long *)(lVar1 + 0x28) == local_38) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
