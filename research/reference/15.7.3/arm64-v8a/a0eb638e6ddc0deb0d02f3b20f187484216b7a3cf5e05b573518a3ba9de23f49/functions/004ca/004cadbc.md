# 004cadbc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

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
  "source_sha256": "1d4ef3cbf5e614f2e7bd29f630ac1cbb2cbb1a48f90f210232ee5434bb9d30b2",
  "source_text_sha256": "1d4ef3cbf5e614f2e7bd29f630ac1cbb2cbb1a48f90f210232ee5434bb9d30b2"
}
~~~

## 呼び出し元

- [00bdc790](../00bdc/00bdc790.md)

## 呼び出し先

- [00418fe0](../00418/00418fe0.md)
- [004c9e38](../004c9/004c9e38.md)
- [005229d4](../00522/005229d4.md)
- [00bdaff0](../00bda/00bdaff0.md)
- [00bdb010](../00bdb/00bdb010.md)
- [00bdb040](../00bdb/00bdb040.md)

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
  *plVar2 = (long)&PTR_FUN_00bed510;
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
