# 004cadbc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-previous -->
**別版の対応** [v15.7.2 `004cadbc`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ca/004cadbc.md)
<!-- /kbcs-version-previous -->

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
