# 004eebcc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](004eebcc.md)

## 関数情報

~~~json
{
  "address": "004eebcc",
  "name": "Botan::X509_Object::make_signed",
  "size": 488,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "445505ce0063a900c17bc1139841f0251c8c74c7f8f4c5d1ae44b5babf4e27f3",
  "source_text_sha256": "445505ce0063a900c17bc1139841f0251c8c74c7f8f4c5d1ae44b5babf4e27f3"
}
~~~
## 呼び出し元

- [00bdce10](../00bdc/00bdce10.md)

## 呼び出し先

- [00483ed8](../00483/00483ed8.md)
- [00512ca8](../00512/00512ca8.md)
- [0051d614](../0051d/0051d614.md)
- [00bdaf60](../00bda/00bdaf60.md)
- [00bdaf90](../00bda/00bdaf90.md)
- [00bdaff0](../00bda/00bdaff0.md)
- [00bdb710](../00bdb/00bdb710.md)
- [00bdb760](../00bdb/00bdb760.md)
- [00bdb770](../00bdb/00bdb770.md)
- [00bdb780](../00bdb/00bdb780.md)
- [00bdbbe0](../00bdb/00bdbbe0.md)
- [00bdc300](../00bdc/00bdc300.md)
- [010a5058](../010a5/010a5058.md)

## 疑似コード 1/1 / UTF-8 2743 bytes

~~~c

/* Botan::X509_Object::make_signed(Botan::PK_Signer*, Botan::RandomNumberGenerator&,
   Botan::AlgorithmIdentifier const&, std::__ndk1::vector<unsigned char,
   Botan::secure_allocator<unsigned char> > const&) */

void __thiscall
Botan::X509_Object::make_signed
          (X509_Object *this,PK_Signer *param_1,RandomNumberGenerator *param_2,
          AlgorithmIdentifier *param_3,vector *param_4)

{
  ulong uVar1;
  uchar *__src;
  uchar *puVar2;
  long lVar3;
  void *pvVar4;
  void *pvVar5;
  ulong __n;
  ulong uVar6;
  void *local_a0;
  void *pvStack_98;
  long local_90;
  void *pvStack_88;
  void *local_80;
  undefined8 uStack_78;
  void *local_70;
  void *local_68;
  long local_58;
  
  lVar3 = tpidr_el0;
  local_58 = *(long *)(lVar3 + 0x28);
  (**(code **)**(undefined8 **)this)
            (*(undefined8 **)this,*(long *)param_3,*(long *)(param_3 + 8) - *(long *)param_3);
  PK_Signer::signature((PK_Signer *)this,(RandomNumberGenerator *)param_1);
  pvStack_88 = (void *)0x0;
  local_90 = 0;
  uStack_78 = 0;
  local_80 = (void *)0x0;
  pvStack_98 = (void *)0x0;
  local_a0 = (void *)0x0;
  DER_Encoder::start_cons(&local_a0,0x10,0);
  __src = *(uchar **)param_3;
  puVar2 = *(uchar **)(param_3 + 8);
  __n = (long)puVar2 - (long)__src;
  if (local_80 == pvStack_88) {
    uVar6 = (long)pvStack_98 - (long)local_a0;
    uVar1 = uVar6 + __n;
    if (uVar6 < uVar1) {
      FUN_0051d614(&local_a0,__n);
    }
    else if (uVar6 != uVar1) {
      pvStack_98 = (void *)((long)local_a0 + uVar1);
    }
    if (puVar2 != __src) {
      memmove((void *)((long)local_a0 + uVar6),__src,__n);
    }
  }
  else {
    DER_Encoder::DER_Sequence::add_bytes((DER_Sequence *)((long)local_80 + -0x38),__src,__n);
  }
  (*(code *)**(undefined8 **)param_2)(param_2,&local_a0);
  DER_Encoder::encode((DER_Encoder *)&local_a0,local_70,(long)local_68 - (long)local_70,3,3,0);
  DER_Encoder::end_cons((DER_Encoder *)&local_a0);
  FUN_00483ed8(&local_a0);
  pvVar5 = pvStack_88;
  pvVar4 = local_80;
  if (pvStack_88 != (void *)0x0) {
    while (pvVar4 != pvVar5) {
      FUN_00512ca8(&uStack_78,(void *)((long)pvVar4 + -0x38));
      pvVar4 = (void *)((long)pvVar4 + -0x38);
    }
    local_80 = pvVar5;
    operator_delete(pvStack_88);
  }
  pvVar4 = local_a0;
  if (local_a0 != (void *)0x0) {
    pvStack_98 = local_a0;
    (*(code *)PTR_memset_00bea678)(local_a0,0,local_90 - (long)local_a0);
    free(pvVar4);
  }
  if (local_70 != (void *)0x0) {
    local_68 = local_70;
    operator_delete(local_70);
  }
  if (*(long *)(lVar3 + 0x28) != local_58) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return;
}

~~~
