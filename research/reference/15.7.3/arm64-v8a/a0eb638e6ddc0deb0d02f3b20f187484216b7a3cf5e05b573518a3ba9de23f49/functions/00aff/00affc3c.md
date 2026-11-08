# 00affc3c

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00affc3c",
  "name": "_ZNK8firebase26ReferenceCountedFutureImpl15GetFutureResultERKNS_12FutureHandleE",
  "size": 176,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5cf7e34a2b03af1619d882079982a7671ab4f0d5d42ecf57adaa854b5fce0ba3",
  "source_text_sha256": "5cf7e34a2b03af1619d882079982a7671ab4f0d5d42ecf57adaa854b5fce0ba3"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bddbd0](../00bdd/00bddbd0.md)
- [00bddbe0](../00bdd/00bddbe0.md)

## 疑似コード / UTF-8 1913 bytes

~~~c

undefined8
_ZNK8firebase26ReferenceCountedFutureImpl15GetFutureResultERKNS_12FutureHandleE
          (long param_1,ulong *param_2)

{
  long lVar1;
  long *plVar2;
  long *plVar3;
  long *plVar4;
  undefined8 uVar5;
  int *piVar6;
  ulong uVar7;
  
                    /* catch() { ... } // from try @ 00af5be0 with catch @ 00affc44 */
  lVar1 = param_1 + 8;
                    /* catch() { ... } // from try @ 00af5bd4 with catch @ 00affc50 */
  _ZN8firebase5Mutex7AcquireEv(lVar1);
  uVar7 = *param_2;
                    /* catch() { ... } // from try @ 00af5bc8 with catch @ 00affc68 */
  _ZN8firebase5Mutex7AcquireEv(lVar1);
  plVar4 = (long *)(param_1 + 0x38);
  plVar3 = (long *)*plVar4;
  plVar2 = plVar4;
  if (plVar3 == (long *)0x0) {
LAB_00affca4:
    _ZN8firebase5Mutex7ReleaseEv(lVar1);
  }
  else {
    do {
      if ((ulong)plVar3[4] >= uVar7) {
        plVar2 = plVar3;
      }
      plVar3 = (long *)plVar3[(ulong)plVar3[4] < uVar7];
                    /* catch() { ... } // from try @ 00af5bb0 with catch @ 00affc8c */
    } while (plVar3 != (long *)0x0);
                    /* catch() { ... } // from try @ 00af5ba4 with catch @ 00affc98 */
    if ((plVar2 == plVar4) || (uVar7 < (ulong)plVar2[4])) goto LAB_00affca4;
    piVar6 = (int *)plVar2[5];
                    /* catch() { ... } // from try @ 00af5b80 with catch @ 00affcd4 */
    _ZN8firebase5Mutex7ReleaseEv(lVar1);
    uVar5 = 0;
    if (piVar6 == (int *)0x0) goto LAB_00affcb0;
                    /* catch() { ... } // from try @ 00af5b50 with catch @ 00affce0 */
    if (*piVar6 == 0) {
      uVar5 = *(undefined8 *)(piVar6 + 10);
      goto LAB_00affcb0;
    }
  }
  uVar5 = 0;
LAB_00affcb0:
                    /* catch() { ... } // from try @ 00af5b98 with catch @ 00affcb0 */
  _ZN8firebase5Mutex7ReleaseEv(lVar1);
                    /* catch() { ... } // from try @ 00af5b8c with catch @ 00affcbc */
  return uVar5;
}

~~~
