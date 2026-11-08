# 00affcec

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00affcec",
  "name": "_ZN8firebase26ReferenceCountedFutureImpl21AddCompletionCallbackERKNS_12FutureHandleEPFvRKNS_10FutureBaseEPvES7_PFvS7_Eb",
  "size": 436,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c5cd43394f437014435c5adaab58c15818b0f8cb6b242b328b6cb4ab763c78eb",
  "source_text_sha256": "c5cd43394f437014435c5adaab58c15818b0f8cb6b242b328b6cb4ab763c78eb"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdaff0](../00bda/00bdaff0.md)
- [00bdb010](../00bdb/00bdb010.md)
- [00bddbd0](../00bdd/00bddbd0.md)
- [00bddbe0](../00bdd/00bddbe0.md)
- [00bddfc0](../00bdd/00bddfc0.md)

## 疑似コード / UTF-8 6273 bytes

~~~c

void _ZN8firebase26ReferenceCountedFutureImpl21AddCompletionCallbackERKNS_12FutureHandleEPFvRKNS_10FutureBaseEPvES7_PFvS7_Eb
               (long *param_1,long param_2,ulong *param_3,long param_4,long param_5,long param_6,
               uint param_7)

{
  long lVar1;
  long lVar2;
  undefined8 *puVar3;
  long *plVar4;
  long *plVar5;
  int iVar6;
  long *plVar7;
  long *plVar8;
  ulong uVar9;
  int *piVar10;
  
                    /* catch() { ... } // from try @ 00af5b40 with catch @ 00affcec */
                    /* catch() { ... } // from try @ 00af5b34 with catch @ 00affd04 */
                    /* catch() { ... } // from try @ 00af5b28 with catch @ 00affd10 */
                    /* catch() { ... } // from try @ 00af5b1c with catch @ 00affd28 */
  plVar4 = (long *)_Znwm(0x28);
  lVar1 = param_2 + 8;
                    /* catch() { ... } // from try @ 00af5b10 with catch @ 00affd34 */
  *plVar4 = (long)plVar4;
  plVar4[1] = (long)plVar4;
  plVar4[2] = param_4;
  plVar4[3] = param_5;
  plVar4[4] = param_6;
  _ZN8firebase5Mutex7AcquireEv(lVar1);
  uVar9 = *param_3;
                    /* catch() { ... } // from try @ 00af5b04 with catch @ 00affd4c */
  _ZN8firebase5Mutex7AcquireEv(lVar1);
                    /* catch() { ... } // from try @ 00af5ae4 with catch @ 00affd58 */
  plVar7 = (long *)(param_2 + 0x38);
  plVar8 = (long *)*plVar7;
  plVar5 = plVar7;
  if (plVar8 == (long *)0x0) {
LAB_00affd90:
                    /* catch() { ... } // from try @ 00af5ac0 with catch @ 00affd94 */
    _ZN8firebase5Mutex7ReleaseEv(lVar1);
  }
  else {
    do {
                    /* catch() { ... } // from try @ 00af5ad8 with catch @ 00affd70 */
      if ((ulong)plVar8[4] >= uVar9) {
        plVar5 = plVar8;
      }
      plVar8 = (long *)plVar8[(ulong)plVar8[4] < uVar9];
    } while (plVar8 != (long *)0x0);
                    /* catch() { ... } // from try @ 00af5acc with catch @ 00affd7c */
    if ((plVar5 == plVar7) || (uVar9 < (ulong)plVar5[4])) goto LAB_00affd90;
                    /* catch() { ... } // from try @ 00af5a50 with catch @ 00affddc */
    piVar10 = (int *)plVar5[5];
    _ZN8firebase5Mutex7ReleaseEv(lVar1);
                    /* catch() { ... } // from try @ 00af5a2c with catch @ 00affde8 */
    if (piVar10 != (int *)0x0) {
      if ((param_7 & 1) == 0) {
                    /* catch() { ... } // from try @ 00af59b0 with catch @ 00affe3c */
        puVar3 = *(undefined8 **)(piVar10 + 0x16);
                    /* catch() { ... } // from try @ 00af59a4 with catch @ 00affe44 */
        plVar4 = (long *)((long)plVar4 + *(long *)(piVar10 + 0x18));
                    /* catch() { ... } // from try @ 00af5998 with catch @ 00affe4c */
        piVar10[8] = piVar10[8] + 1;
        *puVar3 = plVar4;
                    /* catch() { ... } // from try @ 00af598c with catch @ 00affe54 */
        *plVar4 = (long)(piVar10 + 0x14);
        plVar4[1] = (long)puVar3;
        *(long **)(piVar10 + 0x16) = plVar4;
                    /* catch() { ... } // from try @ 00af5980 with catch @ 00affe5c */
        iVar6 = *piVar10;
      }
      else {
        plVar5 = *(long **)(piVar10 + 0x12);
                    /* catch() { ... } // from try @ 00af5a1c with catch @ 00affdf4 */
        if (plVar5 == (long *)0x0) {
          iVar6 = piVar10[8];
        }
        else {
                    /* catch() { ... } // from try @ 00af5a10 with catch @ 00affdfc */
          if ((code *)plVar5[4] == (code *)0x0) {
LAB_00affe10:
            lVar2 = *plVar5;
                    /* catch() { ... } // from try @ 00af59ec with catch @ 00affe14 */
            *(long *)(lVar2 + 8) = plVar5[1];
                    /* catch() { ... } // from try @ 00af59e0 with catch @ 00affe1c */
            *(long *)plVar5[1] = lVar2;
            _ZdlPv(plVar5);
          }
          else {
                    /* catch() { ... } // from try @ 00af5a04 with catch @ 00affe04 */
            (*(code *)plVar5[4])(plVar5[3]);
            plVar5 = *(long **)(piVar10 + 0x12);
                    /* catch() { ... } // from try @ 00af59f8 with catch @ 00affe0c */
            if (plVar5 != (long *)0x0) goto LAB_00affe10;
          }
                    /* catch() { ... } // from try @ 00af59d4 with catch @ 00affe24 */
          piVar10[0x12] = 0;
          piVar10[0x13] = 0;
                    /* catch() { ... } // from try @ 00af59c8 with catch @ 00affe2c */
          iVar6 = piVar10[8] + -1;
          piVar10[8] = iVar6;
                    /* catch() { ... } // from try @ 00af59bc with catch @ 00affe34 */
        }
                    /* catch() { ... } // from try @ 00af5950 with catch @ 00affe7c */
        piVar10[8] = iVar6 + 1;
                    /* catch() { ... } // from try @ 00af5944 with catch @ 00affe84 */
        *(long **)(piVar10 + 0x12) = plVar4;
        iVar6 = *piVar10;
                    /* catch() { ... } // from try @ 00af5938 with catch @ 00affe8c */
      }
      if (iVar6 != 0) {
                    /* catch() { ... } // from try @ 00af5974 with catch @ 00affe64 */
        _ZN8firebase5Mutex7ReleaseEv(lVar1);
                    /* catch() { ... } // from try @ 00af5968 with catch @ 00affe6c */
        *param_1 = param_4;
        param_1[1] = param_5;
        param_1[2] = param_6;
        return;
                    /* catch() { ... } // from try @ 00af595c with catch @ 00affe74 */
      }
                    /* catch() { ... } // from try @ 00af592c with catch @ 00affe94 */
      _ZN8firebase26ReferenceCountedFutureImpl27ReleaseMutexAndRunCallbacksERKNS_12FutureHandleE
                (param_2,param_3);
                    /* catch() { ... } // from try @ 00af5920 with catch @ 00affe9c */
      goto LAB_00affdb8;
    }
  }
  _ZN8firebase5Mutex7ReleaseEv(lVar1);
                    /* catch() { ... } // from try @ 00af5ab4 with catch @ 00affda0 */
  lVar1 = *plVar4;
  *(long *)(lVar1 + 8) = plVar4[1];
  *(long *)plVar4[1] = lVar1;
  _ZdlPv(plVar4);
LAB_00affdb8:
                    /* catch() { ... } // from try @ 00af5aa8 with catch @ 00affdb8 */
  *param_1 = 0;
  param_1[1] = 0;
  param_1[2] = 0;
                    /* catch() { ... } // from try @ 00af5a9c with catch @ 00affdc4 */
                    /* catch() { ... } // from try @ 00af5a60 with catch @ 00affdd0 */
  return;
}

~~~
