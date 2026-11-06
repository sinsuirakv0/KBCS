# 004cafdc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

ページ 1/1。[入口](004cafdc.md)

## 関数情報

~~~json
{
  "address": "004cafdc",
  "name": "_ZN5Botan5PKCS88copy_keyERKNS_11Private_KeyE",
  "size": 244,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b274a087e562cf1407ee6c39d16acb249a3225661e046a6657275fe880809188",
  "source_text_sha256": "b274a087e562cf1407ee6c39d16acb249a3225661e046a6657275fe880809188"
}
~~~
## 呼び出し元

- [00bdc800](../00bdc/00bdc800.md)

## 呼び出し先

- [004c9e38](../004c9/004c9e38.md)
- [00522a98](../00522/00522a98.md)
- [00522a9c](../00522/00522a9c.md)
- [00bdb060](../00bdb/00bdb060.md)
- [00bdb090](../00bdb/00bdb090.md)
- [00bdb810](../00bdb/00bdb810.md)
- [00bdc670](../00bdc/00bdc670.md)
- [00bdc7a0](../00bdc/00bdc7a0.md)
- [010a5058](../010a5/010a5058.md)

## 疑似コード 1/1 / UTF-8 1281 bytes

~~~c

void _ZN5Botan5PKCS88copy_keyERKNS_11Private_KeyE(undefined8 param_1)

{
  long lVar1;
  undefined ***pppuVar2;
  long lVar3;
  undefined1 auStack_98 [8];
  void *local_90;
  void *local_88;
  long local_80;
  undefined **local_70 [2];
  void *local_60;
  undefined ***local_50;
  long local_38;
  
  lVar1 = tpidr_el0;
  local_38 = *(long *)(lVar1 + 0x28);
  _ZN5Botan5PKCS810PEM_encodeERKNS_11Private_KeyE(local_70);
  _ZN5Botan17DataSource_MemoryC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
            (auStack_98,local_70);
  if (((byte)local_70[0] & 1) != 0) {
    _ZdlPv(local_60);
  }
  local_70[0] = &PTR_FUN_00bed5f0;
  local_50 = local_70;
  FUN_004c9e38(param_1,auStack_98,local_70,0);
  if (local_50 == local_70) {
    lVar3 = 0x20;
    pppuVar2 = local_70;
  }
  else {
    if (local_50 == (undefined ***)0x0) goto LAB_004cb078;
    lVar3 = 0x28;
    pppuVar2 = local_50;
  }
  (**(code **)((long)*pppuVar2 + lVar3))();
LAB_004cb078:
  if (local_90 != (void *)0x0) {
    local_88 = local_90;
    (*(code *)PTR_memset_00bea778)(local_90,0,local_80 - (long)local_90);
    free(local_90);
  }
  if (*(long *)(lVar1 + 0x28) == local_38) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
