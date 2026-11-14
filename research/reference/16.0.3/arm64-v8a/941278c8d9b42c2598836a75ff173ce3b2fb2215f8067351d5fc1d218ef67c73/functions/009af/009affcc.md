# 009affcc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "009affcc",
  "name": "FUN_009affcc",
  "size": 308,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "868aad525f352bf1349955cd8a519282f42c4a47ca1046fd14b57b0abeefb72b",
  "source_text_sha256": "868aad525f352bf1349955cd8a519282f42c4a47ca1046fd14b57b0abeefb72b"
}
~~~

## 呼び出し元

- [0076a1b8](../0076a/0076a1b8.md)

## 呼び出し先

- [009b6ca4](../009b6/009b6ca4.md)
- [009b6ce8](../009b6/009b6ce8.md)
- [00c54d60](../00c54/00c54d60.md)
- [00c54d90](../00c54/00c54d90.md)
- [00c58f20](../00c58/00c58f20.md)
- [00c58f80](../00c58/00c58f80.md)

## 疑似コード / UTF-8 4419 bytes

~~~c

void FUN_009affcc(long *param_1)

{
  undefined8 *puVar1;
  long lVar2;
  int iVar3;
  ulong uVar4;
  long lVar5;
  undefined8 uVar6;
  long lVar7;
  ulong uVar8;
  long *plVar9;
  
                    /* try { // try from 009affe0 to 00aaffe7 has its CatchHandler @ 009b0048 */
  lVar2 = tpidr_el0;
                    /* catch() { ... } // from try @ 009afba0 with catch @ 009affe8
                       try { // try from 009affe8 to 00ab00b7 has its CatchHandler @ 009af808 */
  lVar7 = *(long *)(lVar2 + 0x28);
                    /* catch() { ... } // from try @ 009afb64 with catch @ 009afff0 */
                    /* catch() { ... } // from try @ 009afb54 with catch @ 009afff4 */
  lVar5 = *param_1;
                    /* catch() { ... } // from try @ 009afeac with catch @ 009afffc */
  if (param_1[1] != lVar5) {
                    /* catch() { ... } // from try @ 009afa50 with catch @ 009b0000
                       catch() { ... } // from try @ 009afe9c with catch @ 009b0000 */
    uVar8 = 0;
    do {
                    /* catch() { ... } // from try @ 009afb38 with catch @ 009b001c */
      puVar1 = (undefined8 *)(lVar5 + uVar8 * 0x10);
      plVar9 = (long *)puVar1[1];
      uVar6 = *puVar1;
                    /* catch() { ... } // from try @ 009afe90 with catch @ 009b0020 */
                    /* catch() { ... } // from try @ 009afccc with catch @ 009b0024 */
                    /* catch() { ... } // from try @ 009afbec with catch @ 009b0028 */
      if (plVar9 != (long *)0x0) {
                    /* catch() { ... } // from try @ 009afeec with catch @ 009b002c */
                    /* catch() { ... } // from try @ 009afe54 with catch @ 009b0034 */
        FUN_00c54d60(1,plVar9 + 1);
                    /* catch() { ... } // from try @ 009aff04 with catch @ 009b003c */
      }
                    /* catch() { ... } // from try @ 009afc48 with catch @ 009b0040 */
                    /* catch() { ... } // from try @ 009af99c with catch @ 009b0044 */
                    /* catch() { ... } // from try @ 009afdb8 with catch @ 009b0048
                       catch() { ... } // from try @ 009affe0 with catch @ 009b0048 */
      iVar3 = FUN_009b6ca4(uVar6);
                    /* catch() { ... } // from try @ 009afde4 with catch @ 009b0050 */
      if ((iVar3 == 4) && (uVar4 = FUN_009b6ce8(uVar6), (uVar4 & 1) != 0)) {
        *(int *)((long)param_1 + 0x1c) = (int)uVar8;
        if ((plVar9 != (long *)0x0) &&
           (lVar5 = FUN_00c54d90(0xffffffffffffffff,plVar9 + 1), lVar5 == 0)) {
                    /* try { // try from 009b00b8 to 00ab023f has its CatchHandler @ 009b00b8
                       catch() { ... } // from try @ 009b00b8 with catch @ 009b00b8
                       catch() { ... } // from try @ 009b0300 with catch @ 009b00b8
                       catch() { ... } // from try @ 009b0594 with catch @ 009b00b8
                       catch() { ... } // from try @ 009b0654 with catch @ 009b00b8
                       catch() { ... } // from try @ 009b07e4 with catch @ 009b00b8
                       catch() { ... } // from try @ 009b0870 with catch @ 009b00b8 */
          (**(code **)(*plVar9 + 0x10))(plVar9);
          _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar9);
        }
        uVar6 = 1;
        goto LAB_009b00d4;
      }
                    /* catch() { ... } // from try @ 009afcf0 with catch @ 009b0060
                       catch() { ... } // from try @ 009affc8 with catch @ 009b0060 */
                    /* catch() { ... } // from try @ 009afd38 with catch @ 009b0068 */
      if ((plVar9 != (long *)0x0) &&
         (lVar5 = FUN_00c54d90(0xffffffffffffffff,plVar9 + 1), lVar5 == 0)) {
        (**(code **)(*plVar9 + 0x10))(plVar9);
        _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar9);
      }
                    /* catch() { ... } // from try @ 009afbd4 with catch @ 009b0008 */
      lVar5 = *param_1;
      uVar8 = uVar8 + 1;
                    /* catch() { ... } // from try @ 009afa0c with catch @ 009b0010 */
                    /* catch() { ... } // from try @ 009af9fc with catch @ 009b0014 */
    } while (uVar8 < (ulong)(param_1[1] - lVar5 >> 4));
  }
  uVar6 = 0;
  *(undefined4 *)((long)param_1 + 0x1c) = 0xffffffff;
LAB_009b00d4:
  if (*(long *)(lVar2 + 0x28) == lVar7) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail(uVar6);
}

~~~
