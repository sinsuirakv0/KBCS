# 004faccc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](004faccc.md)

## 関数情報

~~~json
{
  "address": "004faccc",
  "name": "Botan::Cert_Extension::CRL_ReasonCode::encode_inner",
  "size": 296,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6cb14e10cf6485babf3b79b793462c9f2d4265de8b38ac7000c167f335a63ec5",
  "source_text_sha256": "6cb14e10cf6485babf3b79b793462c9f2d4265de8b38ac7000c167f335a63ec5"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00483ed8](../00483/00483ed8.md)
- [00512ca8](../00512/00512ca8.md)
- [00bdaf60](../00bda/00bdaf60.md)
- [00bdaf90](../00bda/00bdaf90.md)
- [00bdb710](../00bdb/00bdb710.md)
- [00bdb9d0](../00bdb/00bdb9d0.md)
- [00bdbbc0](../00bdb/00bdbbc0.md)
- [010a5058](../010a5/010a5058.md)

## 疑似コード 1/1 / UTF-8 1578 bytes

~~~c

/* Botan::Cert_Extension::CRL_ReasonCode::encode_inner() const */

void Botan::Cert_Extension::CRL_ReasonCode::encode_inner(void)

{
  long lVar1;
  void *pvVar2;
  void *pvVar3;
  long in_x0;
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
  BigInt::BigInt((BigInt *)&local_68,(ulong)*(uint *)(in_x0 + 8));
  DER_Encoder::encode((DER_Encoder *)&local_a0,&local_68,10,0);
  if (local_68 != (void *)0x0) {
    local_60 = local_68;
    (*(code *)PTR_memset_00bea678)(local_68,0,local_58 - (long)local_68);
    free(local_68);
  }
  FUN_00483ed8(&local_a0);
  pvVar3 = pvStack_88;
  pvVar2 = local_80;
  if (pvStack_88 != (void *)0x0) {
    while (pvVar2 != pvVar3) {
      FUN_00512ca8(auStack_78,(void *)((long)pvVar2 + -0x38));
      pvVar2 = (void *)((long)pvVar2 + -0x38);
    }
    local_80 = pvVar3;
    operator_delete(pvStack_88);
  }
  pvVar2 = local_a0;
  if (local_a0 != (void *)0x0) {
    pvStack_98 = local_a0;
    (*(code *)PTR_memset_00bea678)(local_a0,0,local_90 - (long)local_a0);
    free(pvVar2);
  }
  if (*(long *)(lVar1 + 0x28) != local_48) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return;
}

~~~
