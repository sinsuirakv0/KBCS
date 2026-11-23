# 00bcb1dc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bcadb4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bcadb4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/alignment_unresolved-0010.md#compare-ef2551f47c204698318a9892909c5340)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/priority-0090.md#compare-f0b86d1c9cdd5d02efe43db52fb5a1e9)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcb1dc",
  "name": "_ZN8firebase4auth4Auth23RemoveAuthStateListenerEPNS0_17AuthStateListenerE",
  "size": 272,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "dfa9ec5a83ba8d411efb1aec999dec819d3ef069244fbcf1e1894d15bff76130",
  "source_text_sha256": "dfa9ec5a83ba8d411efb1aec999dec819d3ef069244fbcf1e1894d15bff76130"
}
~~~

## 呼び出し元

- [00c5da70](../00c5d/00c5da70.md)

## 呼び出し先

- [00c5aa00](../00c5a/00c5aa00.md)
- [00c5aa10](../00c5a/00c5aa10.md)

## 疑似コード / UTF-8 2382 bytes

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
          if (plVar2 + -1 == plVar3) goto LAB_00bcb270;
          plVar1 = plVar3 + 1;
          plVar3 = plVar3 + 1;
                    /* catch(type#1 @ 00000000) { ... } // from try @ 00bcb2b0 with catch @ 00bcb240
                       catch(type#1 @ 00000000) { ... } // from try @ 00bcb2e0 with catch @ 00bcb240
                       catch(type#1 @ 00000000) { ... } // from try @ 00bcb314 with catch @ 00bcb240
                       catch(type#1 @ 00000000) { ... } // from try @ 00bcb33c with catch @ 00bcb240
                       catch(type#1 @ 00000000) { ... } // from try @ 00bcb368 with catch @ 00bcb240
                        */
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
LAB_00bcb270:
    plVar3 = *(long **)(param_2 + 8);
    plVar2 = *(long **)(param_2 + 0x10);
    if (plVar2 != plVar3) {
      if ((long *)*plVar3 != param_1) {
        do {
          if (plVar2 + -1 == plVar3) goto LAB_00bcb2d4;
          plVar1 = plVar3 + 1;
          plVar3 = plVar3 + 1;
                    /* try { // try from 00bcb2a4 to 00ccb2af has its CatchHandler @ 00bcb3a4 */
        } while ((long *)*plVar1 != param_1);
      }
                    /* try { // try from 00bcb2b0 to 00ccb2d3 has its CatchHandler @ 00bcb240 */
      if (plVar3 != plVar2) {
        if (plVar2 + -1 != plVar3) {
          *plVar3 = plVar2[-1];
          plVar2 = *(long **)(param_2 + 0x10);
        }
        *(long **)(param_2 + 0x10) = plVar2 + -1;
      }
    }
LAB_00bcb2d4:
                    /* try { // try from 00bcb2d4 to 00ccb2df has its CatchHandler @ 00bcb3a4 */
    _ZN8firebase5Mutex7ReleaseEv(lVar4 + 0x268);
  }
                    /* try { // try from 00bcb2e0 to 00ccb307 has its CatchHandler @ 00bcb240 */
  return;
}

~~~
