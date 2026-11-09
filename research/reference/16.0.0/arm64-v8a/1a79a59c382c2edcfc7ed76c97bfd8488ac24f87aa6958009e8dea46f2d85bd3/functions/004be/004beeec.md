# 004beeec

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "004beeec",
  "name": "_ZN5Botan8ECB_ModeC2EPNS_11BlockCipherEPNS_28BlockCipherModePaddingMethodE",
  "size": 408,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "594f6c5a40df9992454b58790f4593541135b2f15fe94fd13dc428da841f1d52",
  "source_text_sha256": "594f6c5a40df9992454b58790f4593541135b2f15fe94fd13dc428da841f1d52"
}
~~~

## 呼び出し元

- [00c589b0](../00c58/00c589b0.md)

## 呼び出し先

- [004a680c](../004a6/004a680c.md)
- [00c57ae0](../00c57/00c57ae0.md)
- [00c57af0](../00c57/00c57af0.md)
- [00c57b10](../00c57/00c57b10.md)
- [00c57b60](../00c57/00c57b60.md)
- [00c57b70](../00c57/00c57b70.md)
- [00c58270](../00c58/00c58270.md)

## 関連文字列（未確認候補）

~~~text
" cannot be used with "
"/ECB"
"Padding "
~~~

## 疑似コード / UTF-8 2518 bytes

~~~c

void _ZN5Botan8ECB_ModeC2EPNS_11BlockCipherEPNS_28BlockCipherModePaddingMethodE
               (long *param_1,long *param_2,long *param_3)

{
  long lVar1;
  undefined8 uVar2;
  ulong uVar3;
  undefined8 *puVar4;
  long lVar5;
  undefined1 auStack_e0 [24];
  undefined1 auStack_c8 [24];
  undefined8 local_b0;
  undefined8 uStack_a8;
  undefined8 local_a0;
  undefined8 local_90;
  undefined8 uStack_88;
  undefined8 local_80;
  undefined1 auStack_78 [24];
  undefined8 local_60;
  undefined8 uStack_58;
  undefined8 local_50;
  long local_48;
  
  lVar1 = tpidr_el0;
  local_48 = *(long *)(lVar1 + 0x28);
  *param_1 = (long)(PTR__ZTVN5Botan8ECB_ModeE_00c9aa48 + 0x10);
  param_1[1] = (long)param_2;
  lVar5 = *param_2;
  param_1[2] = (long)param_3;
  uVar2 = (**(code **)(lVar5 + 0x30))(param_2);
  uVar3 = (**(code **)(*param_3 + 0x10))(param_3,uVar2);
  if ((uVar3 & 1) == 0) {
    uVar2 = __cxa_allocate_exception(0x20);
    (**(code **)(*(long *)param_1[2] + 0x18))(auStack_c8,(long *)param_1[2]);
    puVar4 = (undefined8 *)
             _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6insertEmPKc
                       (auStack_c8,0,"Padding ");
    local_a0 = puVar4[2];
    uStack_a8 = puVar4[1];
    local_b0 = *puVar4;
    puVar4[1] = 0;
    puVar4[2] = 0;
    *puVar4 = 0;
    puVar4 = (undefined8 *)
             _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKc
                       (&local_b0," cannot be used with ");
    local_80 = puVar4[2];
    uStack_88 = puVar4[1];
    local_90 = *puVar4;
    puVar4[1] = 0;
    puVar4[2] = 0;
    *puVar4 = 0;
    (**(code **)(*param_2 + 0x20))(auStack_e0,param_2);
    FUN_004a680c(auStack_78,&local_90,auStack_e0);
    puVar4 = (undefined8 *)
             _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKc
                       (auStack_78,&DAT_002bb350);
    local_50 = puVar4[2];
    uStack_58 = puVar4[1];
    local_60 = *puVar4;
    puVar4[1] = 0;
    puVar4[2] = 0;
    *puVar4 = 0;
    _ZN5Botan16Invalid_ArgumentC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
              (uVar2,&local_60);
    if (*(long *)(lVar1 + 0x28) == local_48) {
                    /* WARNING: Subroutine does not return */
      __cxa_throw(uVar2,PTR__ZTIN5Botan16Invalid_ArgumentE_00c9a930,FUN_00535828);
    }
  }
  else if (*(long *)(lVar1 + 0x28) == local_48) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
