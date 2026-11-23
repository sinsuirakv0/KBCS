# 009aefcc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `009aee30`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ae/009aee30.md) · 移動量 `+0x19c`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/priority-0055.md#compare-fb84174c5a6560453dd77c5cb67f3884)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/priority-0060.md#compare-577c34165eacfd548fe23fa460d2262d)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "009aefcc",
  "name": "FUN_009aefcc",
  "size": 308,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "04dac6a96c52ad60926373969ead29410a3a9e512e0b99d27b199715a432ed33",
  "source_text_sha256": "04dac6a96c52ad60926373969ead29410a3a9e512e0b99d27b199715a432ed33"
}
~~~

## 呼び出し元

- [00769d84](../00769/00769d84.md)

## 呼び出し先

- [009b5ca4](../009b5/009b5ca4.md)
- [009b5ce8](../009b5/009b5ce8.md)
- [00c53cd0](../00c53/00c53cd0.md)
- [00c53d00](../00c53/00c53d00.md)
- [00c57e80](../00c57/00c57e80.md)
- [00c57ee0](../00c57/00c57ee0.md)

## 疑似コード / UTF-8 4419 bytes

~~~c

void FUN_009aefcc(long *param_1)

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
  
                    /* try { // try from 009aefdc to 00aaefe3 has its CatchHandler @ 009af044 */
                    /* catch() { ... } // from try @ 009aeb9c with catch @ 009aefe4
                       try { // try from 009aefe4 to 00aaf0b3 has its CatchHandler @ 009ae804 */
  lVar2 = tpidr_el0;
                    /* catch() { ... } // from try @ 009aeb60 with catch @ 009aefec */
  lVar7 = *(long *)(lVar2 + 0x28);
                    /* catch() { ... } // from try @ 009aeb50 with catch @ 009aeff0 */
  lVar5 = *param_1;
                    /* catch() { ... } // from try @ 009aeea8 with catch @ 009aeff8 */
                    /* catch() { ... } // from try @ 009aea4c with catch @ 009aeffc
                       catch() { ... } // from try @ 009aee98 with catch @ 009aeffc */
  if (param_1[1] != lVar5) {
    uVar8 = 0;
                    /* catch() { ... } // from try @ 009aebd0 with catch @ 009af004 */
    do {
                    /* catch() { ... } // from try @ 009aee8c with catch @ 009af01c */
      puVar1 = (undefined8 *)(lVar5 + uVar8 * 0x10);
      plVar9 = (long *)puVar1[1];
      uVar6 = *puVar1;
                    /* catch() { ... } // from try @ 009aecc8 with catch @ 009af020 */
                    /* catch() { ... } // from try @ 009aebe8 with catch @ 009af024 */
                    /* catch() { ... } // from try @ 009aeee8 with catch @ 009af028 */
      if (plVar9 != (long *)0x0) {
                    /* catch() { ... } // from try @ 009aee50 with catch @ 009af030 */
                    /* catch() { ... } // from try @ 009aef00 with catch @ 009af038 */
        FUN_00c53cd0(1,plVar9 + 1);
                    /* catch() { ... } // from try @ 009aec44 with catch @ 009af03c */
      }
                    /* catch() { ... } // from try @ 009ae998 with catch @ 009af040 */
                    /* catch() { ... } // from try @ 009aedb4 with catch @ 009af044
                       catch() { ... } // from try @ 009aefdc with catch @ 009af044 */
      iVar3 = FUN_009b5ca4(uVar6);
                    /* catch() { ... } // from try @ 009aede0 with catch @ 009af04c */
                    /* catch() { ... } // from try @ 009aecec with catch @ 009af05c
                       catch() { ... } // from try @ 009aefc4 with catch @ 009af05c */
      if ((iVar3 == 4) && (uVar4 = FUN_009b5ce8(uVar6), (uVar4 & 1) != 0)) {
        *(int *)((long)param_1 + 0x1c) = (int)uVar8;
                    /* try { // try from 009af0b4 to 00aaf23b has its CatchHandler @ 009af0b4
                       catch() { ... } // from try @ 009af0b4 with catch @ 009af0b4
                       catch() { ... } // from try @ 009af2fc with catch @ 009af0b4
                       catch() { ... } // from try @ 009af590 with catch @ 009af0b4
                       catch() { ... } // from try @ 009af650 with catch @ 009af0b4
                       catch() { ... } // from try @ 009af7e0 with catch @ 009af0b4
                       catch() { ... } // from try @ 009af86c with catch @ 009af0b4 */
        if ((plVar9 != (long *)0x0) &&
           (lVar5 = FUN_00c53d00(0xffffffffffffffff,plVar9 + 1), lVar5 == 0)) {
          (**(code **)(*plVar9 + 0x10))(plVar9);
          _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar9);
        }
        uVar6 = 1;
        goto LAB_009af0d4;
      }
                    /* catch() { ... } // from try @ 009aed34 with catch @ 009af064 */
      if ((plVar9 != (long *)0x0) &&
         (lVar5 = FUN_00c53d00(0xffffffffffffffff,plVar9 + 1), lVar5 == 0)) {
        (**(code **)(*plVar9 + 0x10))(plVar9);
        _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar9);
      }
      lVar5 = *param_1;
                    /* catch() { ... } // from try @ 009aea08 with catch @ 009af00c */
      uVar8 = uVar8 + 1;
                    /* catch() { ... } // from try @ 009ae9f8 with catch @ 009af010 */
                    /* catch() { ... } // from try @ 009aeb34 with catch @ 009af018 */
    } while (uVar8 < (ulong)(param_1[1] - lVar5 >> 4));
  }
  uVar6 = 0;
  *(undefined4 *)((long)param_1 + 0x1c) = 0xffffffff;
LAB_009af0d4:
  if (*(long *)(lVar2 + 0x28) == lVar7) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail(uVar6);
}

~~~
