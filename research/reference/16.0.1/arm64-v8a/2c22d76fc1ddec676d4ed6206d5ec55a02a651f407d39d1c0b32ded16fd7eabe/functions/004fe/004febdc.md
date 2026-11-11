# 004febdc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "004febdc",
  "name": "_ZN5Botan21runtime_version_checkEjjj",
  "size": 564,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5b127da73f123dea8c83e3a2f683b7cbe612ff50005180f7971bd59441fcf514",
  "source_text_sha256": "5b127da73f123dea8c83e3a2f683b7cbe612ff50005180f7971bd59441fcf514"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [004594d0](../00459/004594d0.md)
- [00c57eb0](../00c57/00c57eb0.md)
- [00c57ee0](../00c57/00c57ee0.md)
- [00c57fa0](../00c57/00c57fa0.md)
- [00c57fb0](../00c57/00c57fb0.md)
- [00c57fc0](../00c57/00c57fc0.md)
- [00c581b0](../00c58/00c581b0.md)
- [00c581e0](../00c58/00c581e0.md)
- [00c581f0](../00c58/00c581f0.md)
- [00c58960](../00c58/00c58960.md)

## 関連文字列（未確認候補）

~~~text
" does not match version built against "
"Warning: linked version ("
~~~

## 疑似コード / UTF-8 3865 bytes

~~~c

/* WARNING: Type propagation algorithm not settling */

void _ZN5Botan21runtime_version_checkEjjj(undefined8 param_1,int param_2,int param_3,int param_4)

{
  undefined *puVar1;
  long lVar2;
  undefined *puVar3;
  undefined *puVar4;
  undefined8 uVar5;
  long lVar6;
  byte local_198 [16];
  void *local_188;
  undefined1 local_17c [4];
  undefined *local_178 [9];
  ulong local_130;
  undefined8 uStack_128;
  void *local_120;
  undefined8 uStack_118;
  undefined4 local_110;
  undefined *local_108 [3];
  undefined8 uStack_f0;
  undefined4 auStack_e8 [4];
  undefined8 local_d8;
  long local_70;
  
  puVar4 = PTR__ZTVNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c9ac88
  ;
  puVar3 = PTR__ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c9abb8
  ;
  lVar2 = tpidr_el0;
  local_70 = *(long *)(lVar2 + 0x28);
  puVar1 = PTR__ZTVNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c9ac88
           + 0x40;
  local_178[0] = *(undefined **)
                  (
                  PTR__ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c9abb8
                  + 8);
  local_d8 = 0;
  local_108[0] = puVar1;
  *(undefined8 *)((long)local_178 + *(long *)(local_178[0] + -0x18)) =
       *(undefined8 *)
        (PTR__ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c9abb8 +
        0x10);
  lVar6 = *(long *)(local_178[0] + -0x18);
  _ZNSt6__ndk18ios_base4initEPv((long)local_178 + lVar6,local_178 + 1);
  local_178[0] = puVar4 + 0x18;
  *(undefined8 *)((long)&uStack_f0 + lVar6) = 0;
  *(undefined4 *)((long)auStack_e8 + lVar6) = 0xffffffff;
  local_108[0] = puVar1;
  _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEEC1Ev(local_178 + 1);
  puVar1 = PTR__ZTVNSt6__ndk115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c9abc0;
  local_178[1] = PTR__ZTVNSt6__ndk115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c9abc0
                 + 0x10;
  uStack_128 = 0;
  local_130 = 0;
  uStack_118 = 0;
  local_120 = (void *)0x0;
  local_110 = 0x10;
  if (((param_2 != 2) || (param_3 != 4)) || (param_4 != 0)) {
    uVar5 = FUN_004594d0(local_178,"Warning: linked version (",0x19);
    local_198[0] = 10;
    local_198[1] = 0x32;
    local_198[2] = 0x2e;
    local_198[3] = 0x34;
    local_198[4] = 0x2e;
    local_198[5] = 0x30;
    local_198[6] = 0;
    uVar5 = FUN_004594d0(uVar5,(ulong)local_198 | 1,5);
    uVar5 = FUN_004594d0(uVar5,&DAT_002ab332,1);
    uVar5 = FUN_004594d0(uVar5," does not match version built against ",0x26);
    uVar5 = FUN_004594d0(uVar5,&DAT_002afa22,1);
    uVar5 = _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEj(uVar5,param_2);
    local_17c[0] = 0x2e;
    uVar5 = FUN_004594d0(uVar5,local_17c,1);
    uVar5 = _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEj(uVar5,param_3);
    local_17c[0] = 0x2e;
    uVar5 = FUN_004594d0(uVar5,local_17c,1);
    uVar5 = _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEj(uVar5,param_4);
    FUN_004594d0(uVar5,&DAT_002a3205,2);
    if ((local_198[0] & 1) != 0) {
      _ZdlPv(local_188);
    }
  }
  _ZNKSt6__ndk115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE3strEv
            (param_1,local_178 + 1);
  local_178[0] = *(undefined **)puVar3;
  *(undefined8 *)((long)local_178 + *(long *)(local_178[0] + -0x18)) =
       *(undefined8 *)(puVar3 + 0x18);
  local_178[1] = puVar1 + 0x10;
  if ((local_130 & 1) != 0) {
    _ZdlPv(local_120);
  }
  _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEED2Ev(local_178 + 1);
  _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEED2Ev(local_178,puVar3 + 8);
  _ZNSt6__ndk19basic_iosIcNS_11char_traitsIcEEED1Ev(local_108);
  if (*(long *)(lVar2 + 0x28) == local_70) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
