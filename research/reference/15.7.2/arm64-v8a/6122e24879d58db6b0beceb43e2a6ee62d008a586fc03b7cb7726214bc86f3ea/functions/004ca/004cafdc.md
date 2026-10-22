# 004cafdc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](004cafdc.md)

## 関数情報

~~~json
{
  "address": "004cafdc",
  "name": "Botan::PKCS8::copy_key",
  "size": 244,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c7b28c38fa7f05eed04bacaf27eda858b0bc4f7bf234eb4e6772b283a9201bf4",
  "source_text_sha256": "c7b28c38fa7f05eed04bacaf27eda858b0bc4f7bf234eb4e6772b283a9201bf4"
}
~~~
## 呼び出し元

- [00bdc700](../00bdc/00bdc700.md)

## 呼び出し先

- [004c9e38](../004c9/004c9e38.md)
- [00522a98](../00522/00522a98.md)
- [00522a9c](../00522/00522a9c.md)
- [00bdaf60](../00bda/00bdaf60.md)
- [00bdaf90](../00bda/00bdaf90.md)
- [00bdb710](../00bdb/00bdb710.md)
- [00bdc570](../00bdc/00bdc570.md)
- [00bdc6a0](../00bdc/00bdc6a0.md)
- [010a5058](../010a5/010a5058.md)

## 疑似コード 1/1 / UTF-8 1319 bytes

~~~c

/* Botan::PKCS8::copy_key(Botan::Private_Key const&) */

void __thiscall Botan::PKCS8::copy_key(PKCS8 *this,Private_Key *param_1)

{
  long lVar1;
  undefined ***pppuVar2;
  long lVar3;
  DataSource_Memory aDStack_98 [8];
  void *local_90;
  void *local_88;
  long local_80;
  undefined **local_70 [2];
  void *local_60;
  undefined ***local_50;
  long local_38;
  
  lVar1 = tpidr_el0;
  local_38 = *(long *)(lVar1 + 0x28);
  PEM_encode((Private_Key *)this);
  DataSource_Memory::DataSource_Memory(aDStack_98,(basic_string *)local_70);
  if (((byte)local_70[0]._0_1_ & 1) != 0) {
    operator_delete(local_60);
  }
  local_70[0] = &PTR_FUN_00bed4f0;
  local_50 = local_70;
  FUN_004c9e38(aDStack_98,local_70,0);
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
    (*(code *)PTR_memset_00bea678)(local_90,0,local_80 - (long)local_90);
    free(local_90);
  }
  if (*(long *)(lVar1 + 0x28) == local_38) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
