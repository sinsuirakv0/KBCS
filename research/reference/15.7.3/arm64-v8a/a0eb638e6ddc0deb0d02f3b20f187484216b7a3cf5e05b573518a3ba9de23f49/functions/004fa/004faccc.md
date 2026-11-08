# 004faccc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "004faccc",
  "name": "_ZNK5Botan14Cert_Extension14CRL_ReasonCode12encode_innerEv",
  "size": 296,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2cf21eb8f6237f0bc15ee46ce0a1493ca64c3bd2174da08ac03141e26788fe74",
  "source_text_sha256": "2cf21eb8f6237f0bc15ee46ce0a1493ca64c3bd2174da08ac03141e26788fe74"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00483ed8](../00483/00483ed8.md)
- [00512ca8](../00512/00512ca8.md)
- [00bdb010](../00bdb/00bdb010.md)
- [00bdb040](../00bdb/00bdb040.md)
- [00bdb7c0](../00bdb/00bdb7c0.md)
- [00bdba80](../00bdb/00bdba80.md)
- [00bdbc70](../00bdb/00bdbc70.md)
- [010a5058](../010a5/010a5058.md)

## 疑似コード / UTF-8 1492 bytes

~~~c

void _ZNK5Botan14Cert_Extension14CRL_ReasonCode12encode_innerEv(undefined8 param_1,long param_2)

{
  long lVar1;
  void *pvVar2;
  void *pvVar3;
  void *local_a0;
  void *pvStack_98;
  long local_90;
  void *pvStack_88;
  void *local_80;
  undefined8 auStack_78 [2];
  void *local_68;
  void *local_60;
  long local_58;
  long local_48;
  
  lVar1 = tpidr_el0;
  local_48 = *(long *)(lVar1 + 0x28);
  pvStack_88 = (void *)0x0;
  local_90 = 0;
  auStack_78[0] = 0;
  local_80 = (void *)0x0;
  pvStack_98 = (void *)0x0;
  local_a0 = (void *)0x0;
  _ZN5Botan6BigIntC1Em(&local_68,*(undefined4 *)(param_2 + 8));
  _ZN5Botan11DER_Encoder6encodeERKNS_6BigIntENS_8ASN1_TagES4_(&local_a0,&local_68,10,0);
  if (local_68 != (void *)0x0) {
    local_60 = local_68;
    (*(code *)PTR_memset_00bea728)(local_68,0,local_58 - (long)local_68);
    free(local_68);
  }
  FUN_00483ed8(param_1,&local_a0);
  pvVar3 = pvStack_88;
  pvVar2 = local_80;
  if (pvStack_88 != (void *)0x0) {
    while (pvVar2 != pvVar3) {
      FUN_00512ca8(auStack_78,(void *)((long)pvVar2 + -0x38));
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
  if (*(long *)(lVar1 + 0x28) != local_48) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return;
}

~~~
