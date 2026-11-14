# 00aa3aac

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00aa3aac",
  "name": "FUN_00aa3aac",
  "size": 180,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "db867518f3ae7ef51d647a048bccefb0f593acb2590ad5284e61256279c6c820",
  "source_text_sha256": "db867518f3ae7ef51d647a048bccefb0f593acb2590ad5284e61256279c6c820"
}
~~~

## 呼び出し元

- [00a2c310](../00a2c/00a2c310.md)

## 呼び出し先

- [00480e98](../00480/00480e98.md)
- [00480ef0](../00480/00480ef0.md)
- [00480f48](../00480/00480f48.md)

## 疑似コード / UTF-8 2605 bytes

~~~c

void FUN_00aa3aac(long param_1,undefined8 param_2)

{
  undefined4 uVar1;
  long lVar2;
  long *plVar3;
  bool bVar4;
  long *plVar5;
  long *plVar6;
  
                    /* catch() { ... } // from try @ 00aa2674 with catch @ 00aa3ab0 */
                    /* catch() { ... } // from try @ 00aa3614 with catch @ 00aa3ab8
                       catch() { ... } // from try @ 00aa37d0 with catch @ 00aa3ab8
                       catch() { ... } // from try @ 00aa384c with catch @ 00aa3ab8 */
                    /* catch() { ... } // from try @ 00aa350c with catch @ 00aa3ac0
                       catch() { ... } // from try @ 00aa37b4 with catch @ 00aa3ac0
                       catch() { ... } // from try @ 00aa3834 with catch @ 00aa3ac0 */
                    /* catch() { ... } // from try @ 00aa29ec with catch @ 00aa3ac8
                       catch() { ... } // from try @ 00aa3798 with catch @ 00aa3ac8
                       catch() { ... } // from try @ 00aa381c with catch @ 00aa3ac8 */
                    /* catch() { ... } // from try @ 00aa28e4 with catch @ 00aa3ad0
                       catch() { ... } // from try @ 00aa377c with catch @ 00aa3ad0
                       catch() { ... } // from try @ 00aa3804 with catch @ 00aa3ad0 */
  FUN_00480ef0(param_2,*(undefined2 *)(param_1 + 0x28));
                    /* catch() { ... } // from try @ 00aa2774 with catch @ 00aa3ad8
                       catch() { ... } // from try @ 00aa3760 with catch @ 00aa3ad8
                       catch() { ... } // from try @ 00aa37ec with catch @ 00aa3ad8 */
  plVar5 = *(long **)(param_1 + 0x18);
                    /* catch() { ... } // from try @ 00aa36d4 with catch @ 00aa3ae0 */
                    /* catch() { ... } // from try @ 00aa2650 with catch @ 00aa3ae4 */
  while (plVar5 != (long *)(param_1 + 0x20)) {
    lVar2 = plVar5[4];
    uVar1 = *(undefined4 *)((long)plVar5 + 0x24);
    FUN_00480f48(param_2,*(undefined4 *)((long)plVar5 + 0x1c));
    FUN_00480e98(param_2,(int)lVar2);
    FUN_00480e98(param_2,uVar1);
    plVar3 = (long *)plVar5[1];
    plVar6 = plVar5;
    if ((long *)plVar5[1] == (long *)0x0) {
      do {
        plVar5 = (long *)plVar6[2];
        bVar4 = (long *)*plVar5 != plVar6;
        plVar6 = plVar5;
      } while (bVar4);
    }
    else {
      do {
        plVar5 = plVar3;
        plVar3 = (long *)*plVar5;
      } while ((long *)*plVar5 != (long *)0x0);
    }
  }
                    /* catch() { ... } // from try @ 00aa36b0 with catch @ 00aa3aec
                       catch() { ... } // from try @ 00aa3744 with catch @ 00aa3aec */
  return;
}

~~~
