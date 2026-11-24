# 00baadf8

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00baad5c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00baa/00baad5c.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/alignment_unresolved-0010.md#compare-8f72f8107d8e4974cdc153759dc03c94)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/inspection-0035.md#compare-582a8694debe8fdc6812fe4404489e8e)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00baadf8",
  "name": "_ZNSt6__ndk16vectorINS_4pairIN11flatbuffers5ValueEPNS2_8FieldDefEEENS_9allocatorIS6_EEE21__push_back_slow_pathIS6_EEvOT_",
  "size": 432,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "10431d987574dde46092a933516d6754526d9b30b45170d1e1cbc3ccab55bbd2",
  "source_text_sha256": "10431d987574dde46092a933516d6754526d9b30b45170d1e1cbc3ccab55bbd2"
}
~~~

## 呼び出し元

- [00c5d110](../00c5d/00c5d110.md)

## 呼び出し先

- [00c57f60](../00c57/00c57f60.md)
- [00c57f80](../00c57/00c57f80.md)
- [00c5b210](../00c5b/00c5b210.md)

## 疑似コード / UTF-8 4355 bytes

~~~c

void _ZNSt6__ndk16vectorINS_4pairIN11flatbuffers5ValueEPNS2_8FieldDefEEENS_9allocatorIS6_EEE21__push_back_slow_pathIS6_EEvOT_
               (long *param_1,undefined8 *param_2)

{
  ulong uVar1;
  undefined8 *puVar2;
  void *pvVar3;
  long lVar4;
  undefined8 *puVar5;
  long lVar6;
  ulong uVar7;
  void *pvVar8;
  long lVar9;
  void *__ptr;
  ulong uVar10;
  undefined8 uVar11;
  undefined8 uVar12;
  undefined8 uVar13;
  
                    /* try { // try from 00baae10 to 00caae1b has its CatchHandler @ 00babc20 */
  lVar4 = param_1[1] - *param_1 >> 3;
  uVar10 = 0x38e38e38e38e38e;
  uVar1 = lVar4 * -0x71c71c71c71c71c7 + 1;
                    /* try { // try from 00baae3c to 00caae47 has its CatchHandler @ 00babbd4 */
  if (0x38e38e38e38e38e < uVar1) {
                    /* WARNING: Subroutine does not return */
    abort();
  }
  lVar6 = param_1[2] - *param_1 >> 3;
                    /* try { // try from 00baae60 to 00caae6b has its CatchHandler @ 00babbd0 */
  if ((ulong)(lVar6 * -0x71c71c71c71c71c7) < 0x1c71c71c71c71c7) {
    uVar7 = lVar6 * 0x1c71c71c71c71c72;
    uVar10 = uVar1;
    if (uVar1 <= uVar7) {
      uVar10 = uVar7;
    }
    if (uVar10 == 0) {
                    /* try { // try from 00baaf9c to 00caaf9f has its CatchHandler @ 00babd9c */
      lVar6 = 0;
      goto LAB_00baae90;
    }
  }
                    /* try { // try from 00baae8c to 00caae97 has its CatchHandler @ 00babb84 */
  lVar6 = _Znwm(uVar10 * 0x48);
LAB_00baae90:
  uVar11 = *param_2;
  uVar13 = param_2[3];
  uVar12 = param_2[2];
  puVar5 = (undefined8 *)(lVar6 + lVar4 * 8);
  puVar5[1] = param_2[1];
  *puVar5 = uVar11;
  puVar5[3] = uVar13;
  puVar5[2] = uVar12;
                    /* try { // try from 00baaea8 to 00caaeb3 has its CatchHandler @ 00babb80 */
  uVar12 = param_2[5];
  uVar11 = param_2[4];
  puVar5[6] = param_2[6];
  puVar5[5] = uVar12;
  puVar5[4] = uVar11;
                    /* try { // try from 00baaeb4 to 00caaed3 has its CatchHandler @ 00babed0 */
  param_2[5] = 0;
  param_2[6] = 0;
  param_2[4] = 0;
  *(undefined2 *)(puVar5 + 7) = *(undefined2 *)(param_2 + 7);
  puVar5[8] = param_2[8];
  pvVar8 = (void *)*param_1;
  pvVar3 = (void *)param_1[1];
  puVar2 = puVar5 + 9;
                    /* try { // try from 00baaed4 to 00caaf43 has its CatchHandler @ 00bac0a4 */
  __ptr = pvVar8;
  if (pvVar3 != pvVar8) {
    lVar4 = 0;
    do {
      uVar11 = *(undefined8 *)((long)pvVar3 + lVar4 + -0x38);
      uVar13 = *(undefined8 *)((long)pvVar3 + lVar4 + -0x40);
      uVar12 = *(undefined8 *)((long)pvVar3 + lVar4 + -0x48);
      lVar9 = lVar4 + -0x48;
      *(undefined8 *)((long)puVar5 + lVar4 + -0x30) = *(undefined8 *)((long)pvVar3 + lVar4 + -0x30);
      *(undefined8 *)((long)puVar5 + lVar4 + -0x38) = uVar11;
      *(undefined8 *)((long)puVar5 + lVar4 + -0x40) = uVar13;
      *(undefined8 *)((long)puVar5 + lVar4 + -0x48) = uVar12;
      uVar12 = *(undefined8 *)((long)pvVar3 + lVar4 + -0x20);
      uVar11 = *(undefined8 *)((long)pvVar3 + lVar4 + -0x28);
      *(undefined8 *)((long)puVar5 + lVar4 + -0x18) = *(undefined8 *)((long)pvVar3 + lVar4 + -0x18);
      *(undefined8 *)((long)puVar5 + lVar4 + -0x20) = uVar12;
      *(undefined8 *)((long)puVar5 + lVar4 + -0x28) = uVar11;
      *(undefined8 *)((long)pvVar3 + lVar4 + -0x20) = 0;
      *(undefined8 *)((long)pvVar3 + lVar4 + -0x18) = 0;
      *(undefined8 *)((long)pvVar3 + lVar4 + -0x28) = 0;
      *(undefined2 *)((long)puVar5 + lVar4 + -0x10) = *(undefined2 *)((long)pvVar3 + lVar4 + -0x10);
      *(undefined8 *)((long)puVar5 + lVar4 + -8) = *(undefined8 *)((long)pvVar3 + lVar4 + -8);
      lVar4 = lVar9;
    } while ((long)pvVar8 - (long)pvVar3 != lVar9);
    pvVar8 = (void *)param_1[1];
    puVar5 = (undefined8 *)((long)puVar5 + lVar9);
    __ptr = (void *)*param_1;
  }
  *param_1 = (long)puVar5;
  param_1[1] = (long)puVar2;
  param_1[2] = lVar6 + uVar10 * 0x48;
  while (pvVar3 = pvVar8, pvVar3 != __ptr) {
    pvVar8 = (void *)((long)pvVar3 + -0x48);
    if ((*(byte *)((long)pvVar3 + -0x28) & 1) != 0) {
      _ZdlPv(*(void **)((long)pvVar3 + -0x18));
                    /* try { // try from 00baaf88 to 00caaf93 has its CatchHandler @ 00babdbc */
    }
  }
  if (__ptr != (void *)0x0) {
                    /* try { // try from 00baaf64 to 00caaf6f has its CatchHandler @ 00babe2c */
    _ZdlPv(__ptr);
    return;
  }
  return;
}

~~~
