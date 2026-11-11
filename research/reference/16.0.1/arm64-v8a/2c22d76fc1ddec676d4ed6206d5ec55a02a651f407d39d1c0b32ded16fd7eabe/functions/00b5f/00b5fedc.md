# 00b5fedc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00b5fedc",
  "name": "_ZN8firebase26ReferenceCountedFutureImpl21AddCompletionCallbackERKNS_12FutureHandleEPFvRKNS_10FutureBaseEPvES7_PFvS7_Eb",
  "size": 436,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c78b314bbcd0279648d1c5a596262bedf428edaca61eb090ec4d2d1283c45766",
  "source_text_sha256": "c78b314bbcd0279648d1c5a596262bedf428edaca61eb090ec4d2d1283c45766"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57e90](../00c57/00c57e90.md)
- [00c57eb0](../00c57/00c57eb0.md)
- [00c5aa00](../00c5a/00c5aa00.md)
- [00c5aa10](../00c5a/00c5aa10.md)
- [00c5ae90](../00c5a/00c5ae90.md)

## 疑似コード / UTF-8 4122 bytes

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
  
                    /* try { // try from 00b5fef0 to 00c5feff has its CatchHandler @ 00b60068 */
  plVar4 = (long *)_Znwm(0x28);
  lVar1 = param_2 + 8;
                    /* try { // try from 00b5ff24 to 00c5ff3f has its CatchHandler @ 00b60070 */
  *plVar4 = (long)plVar4;
  plVar4[1] = (long)plVar4;
  plVar4[2] = param_4;
  plVar4[3] = param_5;
  plVar4[4] = param_6;
  _ZN8firebase5Mutex7AcquireEv(lVar1);
  uVar9 = *param_3;
                    /* try { // try from 00b5ff40 to 00c60097 has its CatchHandler @ 00b5fce8 */
  _ZN8firebase5Mutex7AcquireEv(lVar1);
  plVar7 = (long *)(param_2 + 0x38);
  plVar8 = (long *)*plVar7;
  plVar5 = plVar7;
  if (plVar8 == (long *)0x0) {
LAB_00b5ff80:
    _ZN8firebase5Mutex7ReleaseEv(lVar1);
  }
  else {
    do {
      if ((ulong)plVar8[4] >= uVar9) {
        plVar5 = plVar8;
      }
      plVar8 = (long *)plVar8[(ulong)plVar8[4] < uVar9];
    } while (plVar8 != (long *)0x0);
    if ((plVar5 == plVar7) || (uVar9 < (ulong)plVar5[4])) goto LAB_00b5ff80;
    piVar10 = (int *)plVar5[5];
    _ZN8firebase5Mutex7ReleaseEv(lVar1);
    if (piVar10 != (int *)0x0) {
      if ((param_7 & 1) == 0) {
        puVar3 = *(undefined8 **)(piVar10 + 0x16);
                    /* catch() { ... } // from try @ 00b5fd9c with catch @ 00b60034 */
                    /* catch() { ... } // from try @ 00b5fd70 with catch @ 00b60038 */
        plVar4 = (long *)((long)plVar4 + *(long *)(piVar10 + 0x18));
        piVar10[8] = piVar10[8] + 1;
        *puVar3 = plVar4;
        *plVar4 = (long)(piVar10 + 0x14);
        plVar4[1] = (long)puVar3;
        *(long **)(piVar10 + 0x16) = plVar4;
        iVar6 = *piVar10;
      }
      else {
        plVar5 = *(long **)(piVar10 + 0x12);
        if (plVar5 == (long *)0x0) {
                    /* catch() { ... } // from try @ 00b5fef0 with catch @ 00b60068 */
          iVar6 = piVar10[8];
        }
        else {
          if ((code *)plVar5[4] == (code *)0x0) {
LAB_00b60000:
            lVar2 = *plVar5;
            *(long *)(lVar2 + 8) = plVar5[1];
            *(long *)plVar5[1] = lVar2;
            _ZdlPv(plVar5);
          }
          else {
            (*(code *)plVar5[4])(plVar5[3]);
            plVar5 = *(long **)(piVar10 + 0x12);
            if (plVar5 != (long *)0x0) goto LAB_00b60000;
          }
          piVar10[0x12] = 0;
          piVar10[0x13] = 0;
          iVar6 = piVar10[8] + -1;
          piVar10[8] = iVar6;
        }
                    /* catch() { ... } // from try @ 00b5fda8 with catch @ 00b6006c */
                    /* catch() { ... } // from try @ 00b5fe4c with catch @ 00b60070
                       catch() { ... } // from try @ 00b5fed0 with catch @ 00b60070
                       catch() { ... } // from try @ 00b5ff24 with catch @ 00b60070 */
        piVar10[8] = iVar6 + 1;
        *(long **)(piVar10 + 0x12) = plVar4;
        iVar6 = *piVar10;
      }
                    /* catch() { ... } // from try @ 00b5fd3c with catch @ 00b60050 */
      if (iVar6 != 0) {
                    /* catch() { ... } // from try @ 00b5fe18 with catch @ 00b60054 */
        _ZN8firebase5Mutex7ReleaseEv(lVar1);
        *param_1 = param_4;
        param_1[1] = param_5;
        param_1[2] = param_6;
        return;
                    /* catch() { ... } // from try @ 00b5fe9c with catch @ 00b60064 */
      }
      _ZN8firebase26ReferenceCountedFutureImpl27ReleaseMutexAndRunCallbacksERKNS_12FutureHandleE
                (param_2,param_3);
      goto LAB_00b5ffa8;
    }
  }
  _ZN8firebase5Mutex7ReleaseEv(lVar1);
  lVar1 = *plVar4;
  *(long *)(lVar1 + 8) = plVar4[1];
  *(long *)plVar4[1] = lVar1;
  _ZdlPv(plVar4);
LAB_00b5ffa8:
  *param_1 = 0;
  param_1[1] = 0;
  param_1[2] = 0;
  return;
}

~~~
