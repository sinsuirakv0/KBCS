# 00bdc6cc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bdc2a4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdc2a4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/priority-0085.md#compare-dcd6de7be73f87f66e25f908b7c3a8c5)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/priority-0095.md#compare-3dc4920c0df47b5f83891f1e3f46ef7f)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdc6cc",
  "name": "_ZN8firebase4auth18AdditionalUserInfoC2ERKS1_",
  "size": 252,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "56b0cde10a21b4873f79356a852a6b9f6ebe10262ee18051a5b75331e8d628e8",
  "source_text_sha256": "56b0cde10a21b4873f79356a852a6b9f6ebe10262ee18051a5b75331e8d628e8"
}
~~~

## 呼び出し元

- [00c5de20](../00c5d/00c5de20.md)

## 呼び出し先

- [00c5b5b0](../00c5b/00c5b5b0.md)
- [00c5dd60](../00c5d/00c5dd60.md)
- [00c5de70](../00c5d/00c5de70.md)

## 疑似コード / UTF-8 1964 bytes

~~~c

void _ZN8firebase4auth18AdditionalUserInfoC2ERKS1_(long param_1,long param_2)

{
  bool bVar1;
  long *plVar2;
  long lVar3;
  undefined8 *puVar4;
  long *plVar5;
  
  _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2ERKS5_();
  _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2ERKS5_
            (param_1 + 0x18,param_2 + 0x18);
  puVar4 = (undefined8 *)(param_1 + 0x38);
  *puVar4 = 0;
  *(undefined8 *)(param_1 + 0x30) = puVar4;
  *(undefined8 *)(param_1 + 0x40) = 0;
  plVar5 = *(long **)(param_2 + 0x30);
  while (plVar5 != (long *)(param_2 + 0x38)) {
    _ZNSt6__ndk16__treeINS_12__value_typeIN8firebase7VariantES3_EENS_19__map_value_compareIS3_S4_NS_4lessIS3_EELb1EEENS_9allocatorIS4_EEE30__emplace_hint_unique_key_argsIS3_JRKNS_4pairIKS3_S3_EEEEENS_15__tree_iteratorIS4_PNS_11__tree_nodeIS4_PvEElEENS_21__tree_const_iteratorIS4_SM_lEERKT_DpOT0_
              ((undefined8 *)(param_1 + 0x30),puVar4,plVar5 + 4,plVar5 + 4);
    plVar2 = (long *)plVar5[1];
    if ((long *)plVar5[1] == (long *)0x0) {
      plVar2 = plVar5 + 2;
      bVar1 = *(long **)*plVar2 != plVar5;
      plVar5 = (long *)*plVar2;
      if (bVar1) {
        do {
          lVar3 = *plVar2;
                    /* try { // try from 00bdc77c to 00cdc79b has its CatchHandler @ 00bdebdc */
          plVar2 = (long *)(lVar3 + 0x10);
          plVar5 = (long *)*plVar2;
        } while (*plVar5 != lVar3);
      }
    }
    else {
      do {
        plVar5 = plVar2;
        plVar2 = (long *)*plVar5;
      } while ((long *)*plVar5 != (long *)0x0);
    }
  }
  *(undefined8 *)(param_1 + 0x48) = 0;
                    /* try { // try from 00bdc79c to 00cdc89f has its CatchHandler @ 00bd6f4c */
  *(undefined4 *)(param_1 + 0x50) = 0;
  *(undefined8 *)(param_1 + 0x58) = 0;
  *(undefined8 *)(param_1 + 0x60) = 0;
  *(undefined8 *)(param_1 + 0x68) = 0;
  _ZN8firebase4auth10CredentialaSERKS1_((undefined8 *)(param_1 + 0x48),param_2 + 0x48);
  return;
}

~~~
