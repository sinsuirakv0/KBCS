# 004fdeac

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-previous -->
**別版の対応** [v15.7.2 `004fdeac`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fd/004fdeac.md)
<!-- /kbcs-version-previous -->

## 関数情報

~~~json
{
  "address": "004fdeac",
  "name": "_ZN5Botan16X509_CertificateC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE",
  "size": 216,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "12e2d34c012b6ffb41483921799c5af841de1088364247db925fdade64cc408c",
  "source_text_sha256": "12e2d34c012b6ffb41483921799c5af841de1088364247db925fdade64cc408c"
}
~~~

## 呼び出し元

- [00bdcc10](../00bdc/00bdcc10.md)

## 呼び出し先

- [00bdb060](../00bdb/00bdb060.md)
- [00bdb090](../00bdb/00bdb090.md)
- [00bdb840](../00bdb/00bdb840.md)
- [00bdc810](../00bdc/00bdc810.md)
- [00bdc820](../00bdc/00bdc820.md)
- [00bdce30](../00bdc/00bdce30.md)

## 疑似コード / UTF-8 1386 bytes

~~~c

void _ZN5Botan16X509_CertificateC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
               (long *param_1,undefined8 param_2)

{
  undefined *puVar1;
  long lVar2;
  ushort local_70 [8];
  void *local_60;
  long local_38;
  
  lVar2 = tpidr_el0;
  local_38 = *(long *)(lVar2 + 0x28);
  puVar1 = PTR__ZTVN5Botan19AlgorithmIdentifierE_00c1af48 + 0x10;
  *param_1 = (long)(PTR__ZTVN5Botan11X509_ObjectE_00c1b368 + 0x10);
  param_1[1] = (long)puVar1;
  local_70[0] = 0;
  _ZN5Botan3OIDC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
            (param_1 + 2,local_70);
  if ((local_70[0] & 1) != 0) {
    _ZdlPv(local_60);
  }
  param_1[0xe] = 0;
  param_1[0xb] = 0;
  param_1[10] = 0;
  param_1[0xd] = 0;
  param_1[0xc] = 0;
  puVar1 = PTR__ZTVN5Botan16X509_CertificateE_00c1b2f0;
  param_1[7] = 0;
  param_1[6] = 0;
  param_1[9] = 0;
  param_1[8] = 0;
  param_1[0xf] = 0;
  param_1[0x10] = 0;
  *param_1 = (long)(puVar1 + 0x10);
  _ZN5Botan17DataSource_StreamC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEb
            (local_70,param_2,1);
  _ZN5Botan11X509_Object9load_dataERNS_10DataSourceE(param_1,local_70);
  _ZN5Botan17DataSource_StreamD2Ev(local_70);
  if (*(long *)(lVar2 + 0x28) == local_38) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
