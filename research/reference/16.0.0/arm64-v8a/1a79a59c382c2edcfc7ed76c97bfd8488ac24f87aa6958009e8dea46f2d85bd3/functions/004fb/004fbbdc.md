# 004fbbdc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "004fbbdc",
  "name": "_ZN5Botan11Invalid_OIDC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE",
  "size": 204,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ff739d39043a65ba153c11ecbd22286d7aca63f9bc64670138fe923671df9c3d",
  "source_text_sha256": "ff739d39043a65ba153c11ecbd22286d7aca63f9bc64670138fe923671df9c3d"
}
~~~

## 呼び出し元

- [00c583e0](../00c58/00c583e0.md)

## 呼び出し先

- [00c57ab0](../00c57/00c57ab0.md)
- [00c57ae0](../00c57/00c57ae0.md)
- [00c57cb0](../00c57/00c57cb0.md)
- [00c58380](../00c58/00c58380.md)

## 関連文字列（未確認候補）

~~~text
"Decoding error: "
"Invalid ASN.1 OID: "
"Invalid argument"
~~~

## 疑似コード / UTF-8 1222 bytes

~~~c

void _ZN5Botan11Invalid_OIDC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
               (long *param_1)

{
  long lVar1;
  byte local_58 [16];
  void *local_48;
  byte local_40 [16];
  void *local_30;
  long local_28;
  
  lVar1 = tpidr_el0;
  local_28 = *(long *)(lVar1 + 0x28);
  _ZNSt6__ndk1plIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EEPKS6_RKS9_
            (local_58,"Invalid ASN.1 OID: ");
  _ZNSt6__ndk1plIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EEPKS6_RKS9_
            (local_40,"Decoding error: ",local_58);
  _ZN5Botan9ExceptionC1EPKcRKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEE
            (param_1,"Invalid argument",local_40);
  *param_1 = (long)(PTR__ZTVN5Botan16Invalid_ArgumentE_00c9a960 + 0x10);
  if ((local_40[0] & 1) != 0) {
    _ZdlPv(local_30);
  }
  *param_1 = (long)(PTR__ZTVN5Botan14Decoding_ErrorE_00c9a968 + 0x10);
  if ((local_58[0] & 1) != 0) {
    _ZdlPv(local_48);
  }
  *param_1 = (long)(PTR__ZTVN5Botan11Invalid_OIDE_00c9aca0 + 0x10);
  if (*(long *)(lVar1 + 0x28) == local_28) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
