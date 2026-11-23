# 00b7baac

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00b7ba68`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7ba68.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/97ee0756e9de6c746e3ce399/1-2/high-0011.md#compare-dc5e308aedea4a3b4dddec8f1e83bf58)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 構造資料不足
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b7baac",
  "name": "_ZNSt6__ndk112system_errorC1ENS_10error_codeERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
  "size": 172,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e04ad5a3849f2b2f3f91288d2371f49edc295f716c9b1f615ba1041fc53cac81",
  "source_text_sha256": "e04ad5a3849f2b2f3f91288d2371f49edc295f716c9b1f615ba1041fc53cac81"
}
~~~

## 呼び出し元

- [00be1150](../00be1/00be1150.md)

## 呼び出し先

- [00418fe0](../00418/00418fe0.md)
- [00b7bba4](../00b7b/00b7bba4.md)
- [00bdb060](../00bdb/00bdb060.md)
- [00be0fa0](../00be0/00be0fa0.md)

## 疑似コード / UTF-8 972 bytes

~~~c

void _ZNSt6__ndk112system_errorC1ENS_10error_codeERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE
               (long *param_1,long param_2,long param_3,ulong *param_4)

{
  ulong local_60;
  ulong uStack_58;
  void *local_50;
  byte local_48 [16];
  void *local_38;
  long local_30;
  long lStack_28;
  
  local_30 = param_2;
  lStack_28 = param_3;
  if ((*param_4 & 1) == 0) {
    uStack_58 = param_4[1];
    local_60 = *param_4;
    local_50 = (void *)param_4[2];
  }
  else {
    FUN_00418fe0(&local_60,param_4[2],param_4[1]);
  }
  FUN_00b7bba4(local_48,&local_30,&local_60);
  _ZNSt13runtime_errorC2ERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE
            (param_1,local_48);
  if ((local_48[0] & 1) != 0) {
    _ZdlPv(local_38);
  }
  if ((local_60 & 1) != 0) {
    _ZdlPv(local_50);
  }
  *param_1 = (long)(PTR__ZTVNSt6__ndk112system_errorE_00c1bca0 + 0x10);
  param_1[3] = lStack_28;
  param_1[2] = local_30;
  return;
}

~~~
