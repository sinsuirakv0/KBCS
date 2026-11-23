# 00bcadb4

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b5b8b4`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5b/00b5b8b4.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/2-3/alignment_unresolved-0017.md#compare-f022c8bc5ee2d8e9b979d86eec48c71c)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 構造資料不足
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcadb4",
  "name": "_ZN8firebase4auth4Auth23RemoveAuthStateListenerEPNS0_17AuthStateListenerE",
  "size": 272,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "76e004d4d0c8f41b0f194e0e9d8a3dcfdd2c98a18eb07c26d7758ae77c8b88c6",
  "source_text_sha256": "76e004d4d0c8f41b0f194e0e9d8a3dcfdd2c98a18eb07c26d7758ae77c8b88c6"
}
~~~

## 呼び出し元

- [00c5d670](../00c5d/00c5d670.md)

## 呼び出し先

- [00c5a600](../00c5a/00c5a600.md)
- [00c5a610](../00c5a/00c5a610.md)

## 疑似コード / UTF-8 1994 bytes

~~~c

void _ZN8firebase4auth4Auth23RemoveAuthStateListenerEPNS0_17AuthStateListenerE
               (long *param_1,long param_2)

{
  long *plVar1;
  long *plVar2;
  long *plVar3;
  long lVar4;
  
  lVar4 = *param_1;
  if (lVar4 != 0) {
    _ZN8firebase5Mutex7AcquireEv(lVar4 + 0x268);
    plVar3 = *(long **)(lVar4 + 0x230);
    plVar2 = *(long **)(lVar4 + 0x238);
    if (plVar2 != plVar3) {
      if (*plVar3 != param_2) {
        do {
          if (plVar2 + -1 == plVar3) goto LAB_00bcae48;
          plVar1 = plVar3 + 1;
          plVar3 = plVar3 + 1;
        } while (*plVar1 != param_2);
      }
      if (plVar3 != plVar2) {
        if (plVar2 + -1 != plVar3) {
          *plVar3 = plVar2[-1];
          plVar2 = *(long **)(lVar4 + 0x238);
        }
        *(long **)(lVar4 + 0x238) = plVar2 + -1;
      }
    }
LAB_00bcae48:
    plVar3 = *(long **)(param_2 + 8);
    plVar2 = *(long **)(param_2 + 0x10);
    if (plVar2 != plVar3) {
      if ((long *)*plVar3 != param_1) {
        do {
                    /* catch(type#1 @ 00000000) { ... } // from try @ 00bcaedc with catch @ 00bcae6c
                       catch(type#1 @ 00000000) { ... } // from try @ 00bcaf0c with catch @ 00bcae6c
                       catch(type#1 @ 00000000) { ... } // from try @ 00bcaf40 with catch @ 00bcae6c
                       catch(type#1 @ 00000000) { ... } // from try @ 00bcaf68 with catch @ 00bcae6c
                       catch(type#1 @ 00000000) { ... } // from try @ 00bcaf94 with catch @ 00bcae6c
                        */
          if (plVar2 + -1 == plVar3) goto LAB_00bcaeac;
          plVar1 = plVar3 + 1;
          plVar3 = plVar3 + 1;
        } while ((long *)*plVar1 != param_1);
      }
      if (plVar3 != plVar2) {
        if (plVar2 + -1 != plVar3) {
          *plVar3 = plVar2[-1];
          plVar2 = *(long **)(param_2 + 0x10);
        }
        *(long **)(param_2 + 0x10) = plVar2 + -1;
      }
    }
LAB_00bcaeac:
    _ZN8firebase5Mutex7ReleaseEv(lVar4 + 0x268);
  }
  return;
}

~~~
