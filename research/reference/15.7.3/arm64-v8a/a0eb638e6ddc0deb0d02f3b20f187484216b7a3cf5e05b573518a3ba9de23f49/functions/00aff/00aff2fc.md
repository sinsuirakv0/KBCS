# 00aff2fc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00aff2fc",
  "name": "_ZN8firebase26ReferenceCountedFutureImpl14CompleteHandleERKNS_12FutureHandleE",
  "size": 176,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "acd864e0b7bbe72d954f88f327a88735d6575adda60d107883cd8922a434bcb3",
  "source_text_sha256": "acd864e0b7bbe72d954f88f327a88735d6575adda60d107883cd8922a434bcb3"
}
~~~

## 呼び出し元

- [00bddf90](../00bdd/00bddf90.md)

## 呼び出し先

- [00bddbd0](../00bdd/00bddbd0.md)
- [00bddbe0](../00bdd/00bddbe0.md)
- [00bde130](../00bde/00bde130.md)

## 関連文字列（未確認候補）

~~~text
"backing != nullptr"
"backing->status != kFutureStatusComplete"
~~~

## 疑似コード / UTF-8 2308 bytes

~~~c

void _ZN8firebase26ReferenceCountedFutureImpl14CompleteHandleERKNS_12FutureHandleE
               (long param_1,ulong *param_2)

{
  long lVar1;
  long *plVar2;
  long *plVar3;
  long *plVar4;
  int *piVar5;
  ulong uVar6;
  
                    /* catch() { ... } // from try @ 00af73fc with catch @ 00aff30c */
  uVar6 = *param_2;
  lVar1 = param_1 + 8;
                    /* catch() { ... } // from try @ 00af74d0 with catch @ 00aff31c */
  _ZN8firebase5Mutex7AcquireEv(lVar1);
  plVar4 = (long *)(param_1 + 0x38);
  plVar3 = (long *)*plVar4;
  plVar2 = plVar4;
  if (plVar3 == (long *)0x0) {
LAB_00aff358:
    _ZN8firebase5Mutex7ReleaseEv(lVar1);
  }
  else {
    do {
                    /* catch() { ... } // from try @ 00af73f0 with catch @ 00aff334 */
      if ((ulong)plVar3[4] >= uVar6) {
        plVar2 = plVar3;
      }
      plVar3 = (long *)plVar3[(ulong)plVar3[4] < uVar6];
    } while (plVar3 != (long *)0x0);
                    /* catch() { ... } // from try @ 00afd258 with catch @ 00aff34c */
    if ((plVar2 == plVar4) || (uVar6 < (ulong)plVar2[4])) goto LAB_00aff358;
    piVar5 = (int *)plVar2[5];
                    /* catch() { ... } // from try @ 00afcfb0 with catch @ 00aff39c */
                    /* catch() { ... } // from try @ 00afcf80 with catch @ 00aff3a0 */
    _ZN8firebase5Mutex7ReleaseEv(lVar1);
                    /* catch() { ... } // from try @ 00afcf58 with catch @ 00aff3a4 */
    if (piVar5 != (int *)0x0) goto LAB_00aff370;
  }
                    /* catch() { ... } // from try @ 00afd178 with catch @ 00aff364 */
                    /* catch() { ... } // from try @ 00afd134 with catch @ 00aff368 */
  _ZN8firebase9LogAssertEPKcz("backing != nullptr");
  piVar5 = (int *)0x0;
LAB_00aff370:
  if (*piVar5 == 0) {
                    /* catch() { ... } // from try @ 00afd110 with catch @ 00aff37c */
                    /* catch() { ... } // from try @ 00afd0c0 with catch @ 00aff380 */
    _ZN8firebase9LogAssertEPKcz("backing->status != kFutureStatusComplete");
  }
                    /* catch() { ... } // from try @ 00afd070 with catch @ 00aff384 */
  *piVar5 = 0;
                    /* catch() { ... } // from try @ 00afd040 with catch @ 00aff388 */
                    /* catch() { ... } // from try @ 00afcff8 with catch @ 00aff38c */
  return;
}

~~~
