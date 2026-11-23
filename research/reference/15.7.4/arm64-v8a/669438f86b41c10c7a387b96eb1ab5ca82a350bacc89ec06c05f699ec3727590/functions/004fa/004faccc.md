# 004faccc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `004faccc`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fa/004faccc.md) · 移動量 `+0x0`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/97ee0756e9de6c746e3ce399/1-2/priority-0012.md#compare-653e73168383d26fb2afc0798ff7e956)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 構造資料不足
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

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
  "source_sha256": "487445174efcd949d817489a5313a7e55c4141164220791518c63c7eb1e5bd23",
  "source_text_sha256": "487445174efcd949d817489a5313a7e55c4141164220791518c63c7eb1e5bd23"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00483ed8](../00483/00483ed8.md)
- [00512ca8](../00512/00512ca8.md)
- [00bdb060](../00bdb/00bdb060.md)
- [00bdb090](../00bdb/00bdb090.md)
- [00bdb810](../00bdb/00bdb810.md)
- [00bdbad0](../00bdb/00bdbad0.md)
- [00bdbcc0](../00bdb/00bdbcc0.md)
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
    (*(code *)PTR_memset_00bea778)(local_68,0,local_58 - (long)local_68);
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
    (*(code *)PTR_memset_00bea778)(local_a0,0,local_90 - (long)local_a0);
    free(pvVar2);
  }
  if (*(long *)(lVar1 + 0x28) != local_48) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return;
}

~~~
