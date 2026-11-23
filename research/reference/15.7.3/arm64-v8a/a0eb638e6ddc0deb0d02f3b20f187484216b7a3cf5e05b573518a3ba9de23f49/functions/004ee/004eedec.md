# 004eedec

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `004eedec`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ee/004eedec.md) · 移動量 `+0x0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/af8e2f5c5fc38f06774ff85c/0-1/machine_only_observed-0006.md#compare-f1ad1854647f0e72cd9afd6d8ebf7e09)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 構造資料不足
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "004eedec",
  "name": "_ZNK5Botan7X509_CA7new_crlERNS_21RandomNumberGeneratorEj",
  "size": 140,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "cbc4a4365a9bde7dda2d1faec967f76dd65484b8010c1d47b7df8dca4152c3a1",
  "source_text_sha256": "cbc4a4365a9bde7dda2d1faec967f76dd65484b8010c1d47b7df8dca4152c3a1"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb040](../00bdb/00bdb040.md)
- [00bdb6e0](../00bdb/00bdb6e0.md)
- [00bdced0](../00bdc/00bdced0.md)

## 疑似コード / UTF-8 885 bytes

~~~c

void _ZNK5Botan7X509_CA7new_crlERNS_21RandomNumberGeneratorEj
               (undefined8 param_1,undefined8 param_2,undefined8 param_3,undefined4 param_4)

{
  long lVar1;
  undefined8 uVar2;
  undefined8 local_60;
  undefined8 uStack_58;
  undefined8 local_50;
  long local_48;
  
  lVar1 = tpidr_el0;
  local_48 = *(long *)(lVar1 + 0x28);
  uVar2 = _ZNSt6__ndk16chrono12system_clock3nowEv();
  local_60 = 0;
  uStack_58 = 0;
  local_50 = 0;
  _ZNK5Botan7X509_CA8make_crlERKNSt6__ndk16vectorINS_9CRL_EntryENS1_9allocatorIS3_EEEEjRNS_21RandomNumberGeneratorENS1_6chrono10time_pointINSB_12system_clockENSB_8durationIxNS1_5ratioILl1ELl1000000EEEEEEENSE_IxNSF_ILl1ELl1EEEEE
            (param_1,param_2,&local_60,1,param_3,uVar2,param_4);
  if (*(long *)(lVar1 + 0x28) == local_48) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
