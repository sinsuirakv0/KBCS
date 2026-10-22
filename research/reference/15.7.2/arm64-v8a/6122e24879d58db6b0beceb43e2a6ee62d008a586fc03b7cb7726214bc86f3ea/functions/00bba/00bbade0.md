# 00bbade0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bbade0.md)

## 関数情報

~~~json
{
  "address": "00bbade0",
  "name": "std::overflow_error::~overflow_error",
  "size": 88,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c347c2f2935a0106ec959730e3a5865b085c9b679f086ebff74a6fefb97f7e6d",
  "source_text_sha256": "c347c2f2935a0106ec959730e3a5865b085c9b679f086ebff74a6fefb97f7e6d"
}
~~~
## 呼び出し元

- [00bdd970](../00bdd/00bdd970.md)
- [00be0e70](../00be0/00be0e70.md)
- [00be0ed0](../00be0/00be0ed0.md)
- [00be10a0](../00be1/00be10a0.md)
- [00be1d80](../00be1/00be1d80.md)

## 呼び出し先

- [00bd6d30](../00bd6/00bd6d30.md)
- [00bdaf60](../00bda/00bdaf60.md)
- [00bdb390](../00bdb/00bdb390.md)

## 疑似コード 1/1 / UTF-8 468 bytes

~~~c

/* std::overflow_error::~overflow_error() */

void __thiscall std::overflow_error::~overflow_error(overflow_error *this)

{
  int iVar1;
  long lVar2;
  
  lVar2 = *(long *)(this + 8);
  *(undefined **)this = PTR_vtable_00c1bb68 + 0x10;
  iVar1 = FUN_00bd6d30(0xffffffff,lVar2 + -8);
  if (iVar1 + -1 < 0) {
    operator_delete((void *)(lVar2 + -0x18));
  }
  bad_array_new_length::~bad_array_new_length((bad_array_new_length *)this);
  return;
}

~~~
