# 00bcadb4

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

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
