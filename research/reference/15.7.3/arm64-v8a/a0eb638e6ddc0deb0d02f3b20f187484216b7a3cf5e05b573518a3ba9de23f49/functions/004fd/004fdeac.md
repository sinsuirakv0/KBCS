# 004fdeac

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `004fdeac`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fd/004fdeac.md) · 移動量 `+0x0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/af8e2f5c5fc38f06774ff85c/0-1/priority-0012.md#compare-dc4c16c3b385f6ae7cc9894b73866fc7)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 構造資料不足
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

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
  "source_sha256": "bcb0fdd8e3a84af1ccfd56030dd8b3e3f71965ca55df3eb59045d8b13ceac510",
  "source_text_sha256": "bcb0fdd8e3a84af1ccfd56030dd8b3e3f71965ca55df3eb59045d8b13ceac510"
}
~~~

## 呼び出し元

- [00bdcbc0](../00bdc/00bdcbc0.md)

## 呼び出し先

- [00bdb010](../00bdb/00bdb010.md)
- [00bdb040](../00bdb/00bdb040.md)
- [00bdb7f0](../00bdb/00bdb7f0.md)
- [00bdc7c0](../00bdc/00bdc7c0.md)
- [00bdc7d0](../00bdc/00bdc7d0.md)
- [00bdcde0](../00bdc/00bdcde0.md)

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
  puVar1 = PTR__ZTVN5Botan19AlgorithmIdentifierE_00c1aef8 + 0x10;
  *param_1 = (long)(PTR__ZTVN5Botan11X509_ObjectE_00c1b318 + 0x10);
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
  puVar1 = PTR__ZTVN5Botan16X509_CertificateE_00c1b2a0;
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
