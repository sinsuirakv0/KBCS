# 004dbbdc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "004dbbdc",
  "name": "_ZN5Botan3lcmERKNS_6BigIntES2_",
  "size": 216,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "72dd29224750ccfbc8b32a005b1c9dc4d36b8f4857cea4a56f97d2a5e5c150e0",
  "source_text_sha256": "72dd29224750ccfbc8b32a005b1c9dc4d36b8f4857cea4a56f97d2a5e5c150e0"
}
~~~

## 呼び出し元

- [00c58f90](../00c58/00c58f90.md)

## 呼び出し先

- [00c57ae0](../00c57/00c57ae0.md)
- [00c58260](../00c58/00c58260.md)
- [00c58850](../00c58/00c58850.md)
- [00c58890](../00c58/00c58890.md)
- [00c58f60](../00c58/00c58f60.md)
- [0112a058](../0112a/0112a058.md)

## 疑似コード / UTF-8 922 bytes

~~~c

void _ZN5Botan3lcmERKNS_6BigIntES2_(undefined8 param_1,undefined8 param_2,undefined8 param_3)

{
  long lVar1;
  void *local_78;
  void *local_70;
  long local_68;
  void *local_58;
  void *local_50;
  long local_48;
  long local_38;
  
  lVar1 = tpidr_el0;
  local_38 = *(long *)(lVar1 + 0x28);
  _ZN5BotanmlERKNS_6BigIntES2_(&local_58);
  _ZN5Botan3gcdERKNS_6BigIntES2_(&local_78,param_2,param_3);
  _ZN5BotandvERKNS_6BigIntES2_(param_1,&local_58,&local_78);
  if (local_78 != (void *)0x0) {
    local_70 = local_78;
    (*(code *)PTR_memset_00c67338)(local_78,0,local_68 - (long)local_78);
    free(local_78);
  }
  if (local_58 != (void *)0x0) {
    local_50 = local_58;
    (*(code *)PTR_memset_00c67338)(local_58,0,local_48 - (long)local_58);
    free(local_58);
  }
  if (*(long *)(lVar1 + 0x28) == local_38) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
