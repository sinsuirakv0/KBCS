# 004eebcc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "004eebcc",
  "name": "_ZN5Botan11X509_Object11make_signedEPNS_9PK_SignerERNS_21RandomNumberGeneratorERKNS_19AlgorithmIdentifierERKNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEE",
  "size": 488,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "292c4f57b5dc4a7d3e55a66373ef9f8f6335d003f3c5bea451e9413f4fa76b8a",
  "source_text_sha256": "292c4f57b5dc4a7d3e55a66373ef9f8f6335d003f3c5bea451e9413f4fa76b8a"
}
~~~

## 呼び出し元

- [00bdcec0](../00bdc/00bdcec0.md)

## 呼び出し先

- [00483ed8](../00483/00483ed8.md)
- [00512ca8](../00512/00512ca8.md)
- [0051d614](../0051d/0051d614.md)
- [00bdb010](../00bdb/00bdb010.md)
- [00bdb040](../00bdb/00bdb040.md)
- [00bdb0a0](../00bdb/00bdb0a0.md)
- [00bdb7c0](../00bdb/00bdb7c0.md)
- [00bdb810](../00bdb/00bdb810.md)
- [00bdb820](../00bdb/00bdb820.md)
- [00bdb830](../00bdb/00bdb830.md)
- [00bdbc90](../00bdb/00bdbc90.md)
- [00bdc3b0](../00bdc/00bdc3b0.md)
- [010a5058](../010a5/010a5058.md)

## 疑似コード / UTF-8 2506 bytes

~~~c

void _ZN5Botan11X509_Object11make_signedEPNS_9PK_SignerERNS_21RandomNumberGeneratorERKNS_19AlgorithmIdentifierERKNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEE
               (undefined8 param_1,undefined8 *param_2,undefined8 param_3,undefined8 *param_4,
               long *param_5)

{
  ulong uVar1;
  void *pvVar2;
  void *pvVar3;
  long lVar4;
  size_t __n;
  ulong uVar5;
  void *local_a0;
  void *pvStack_98;
  long local_90;
  void *pvStack_88;
  void *local_80;
  undefined8 uStack_78;
  void *local_70;
  void *local_68;
  long local_58;
  
  lVar4 = tpidr_el0;
  local_58 = *(long *)(lVar4 + 0x28);
  (*(code *)**(undefined8 **)*param_2)((undefined8 *)*param_2,*param_5,param_5[1] - *param_5);
  _ZN5Botan9PK_Signer9signatureERNS_21RandomNumberGeneratorE(&local_70,param_2,param_3);
  pvStack_88 = (void *)0x0;
  local_90 = 0;
  uStack_78 = 0;
  local_80 = (void *)0x0;
  pvStack_98 = (void *)0x0;
  local_a0 = (void *)0x0;
  _ZN5Botan11DER_Encoder10start_consENS_8ASN1_TagES1_(&local_a0,0x10,0);
  pvVar2 = (void *)*param_5;
  pvVar3 = (void *)param_5[1];
  __n = (long)pvVar3 - (long)pvVar2;
  if (local_80 == pvStack_88) {
    uVar5 = (long)pvStack_98 - (long)local_a0;
    uVar1 = uVar5 + __n;
    if (uVar5 < uVar1) {
      FUN_0051d614(&local_a0,__n);
    }
    else if (uVar5 != uVar1) {
      pvStack_98 = (void *)((long)local_a0 + uVar1);
    }
    if (pvVar3 != pvVar2) {
      memmove((void *)((long)local_a0 + uVar5),pvVar2,__n);
    }
  }
  else {
    _ZN5Botan11DER_Encoder12DER_Sequence9add_bytesEPKhm((long)local_80 + -0x38,pvVar2);
  }
  (**(code **)*param_4)(param_4,&local_a0);
  _ZN5Botan11DER_Encoder6encodeEPKhmNS_8ASN1_TagES3_S3_
            (&local_a0,local_70,(long)local_68 - (long)local_70,3,3,0);
  _ZN5Botan11DER_Encoder8end_consEv(&local_a0);
  FUN_00483ed8(param_1,&local_a0);
  pvVar3 = pvStack_88;
  pvVar2 = local_80;
  if (pvStack_88 != (void *)0x0) {
    while (pvVar2 != pvVar3) {
      FUN_00512ca8(&uStack_78,(void *)((long)pvVar2 + -0x38));
      pvVar2 = (void *)((long)pvVar2 + -0x38);
    }
    local_80 = pvVar3;
    _ZdlPv(pvStack_88);
  }
  pvVar2 = local_a0;
  if (local_a0 != (void *)0x0) {
    pvStack_98 = local_a0;
    (*(code *)PTR_memset_00bea728)(local_a0,0,local_90 - (long)local_a0);
    free(pvVar2);
  }
  if (local_70 != (void *)0x0) {
    local_68 = local_70;
    _ZdlPv(local_70);
  }
  if (*(long *)(lVar4 + 0x28) != local_58) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return;
}

~~~
