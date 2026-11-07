# 004cadbc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

<!-- kbcs-version-next -->
**別版の対応** [v15.7.4 `004cadbc`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ca/004cadbc.md)
<!-- /kbcs-version-next -->

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
  "source_sha256": "4da76fe3b6b2dcff45d6e36a43354398ecfcee31520a98cb1e3b272276c899a7",
  "source_text_sha256": "4da76fe3b6b2dcff45d6e36a43354398ecfcee31520a98cb1e3b272276c899a7"
}
~~~

## 呼び出し元

- [00bdc6e0](../00bdc/00bdc6e0.md)

## 呼び出し先

- [00418fe0](../00418/00418fe0.md)
- [004c9e38](../004c9/004c9e38.md)
- [005229d4](../00522/005229d4.md)
- [00bdaf40](../00bda/00bdaf40.md)
- [00bdaf60](../00bda/00bdaf60.md)
- [00bdaf90](../00bda/00bdaf90.md)

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
  *plVar2 = (long)&PTR_FUN_00bed460;
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
