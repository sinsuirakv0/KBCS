# 004eedec

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-previous -->
**別版の対応** [v15.7.2 `004eedec`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ee/004eedec.md)
<!-- /kbcs-version-previous -->

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

- [00bdb090](../00bdb/00bdb090.md)
- [00bdb730](../00bdb/00bdb730.md)
- [00bdcf20](../00bdc/00bdcf20.md)

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
