# 00b7baac

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-previous -->
**別版の対応** [v15.7.2 `00b7b9a0`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7b/00b7b9a0.md)
<!-- /kbcs-version-previous -->

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
