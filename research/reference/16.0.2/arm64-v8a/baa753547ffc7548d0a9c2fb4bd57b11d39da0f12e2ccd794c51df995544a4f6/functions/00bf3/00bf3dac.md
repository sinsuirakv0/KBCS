# 00bf3dac

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bf3d10`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3d10.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/inspection-0040.md#compare-2b677be4b990d765d7980068f5cbe919)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/inspection-0038.md#compare-0eb224c774bbc9175ab57c7c06355e18)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bf3dac",
  "name": "_ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6appendEmw",
  "size": 296,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "11730acc14636afabbcf386d14aa0081dad217902ba7a7c660816b7c85cfd5e6",
  "source_text_sha256": "11730acc14636afabbcf386d14aa0081dad217902ba7a7c660816b7c85cfd5e6"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5a970](../00c5a/00c5a970.md)

## 疑似コード / UTF-8 1770 bytes

~~~c

void _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6appendEmw
               (ulong *param_1,ulong param_2,undefined4 param_3)

{
  ulong uVar1;
  long lVar2;
  ulong uVar3;
  uint uVar4;
  undefined4 *puVar5;
  ulong uVar6;
  ulong uVar7;
  undefined8 *puVar8;
  ulong uVar9;
  
  if (param_2 == 0) {
    return;
  }
  uVar3 = *param_1;
  lVar2 = 4;
  if ((*param_1 & 1) != 0) {
    lVar2 = (uVar3 & 0xfffffffffffffffe) - 1;
  }
  uVar4 = (uint)uVar3;
  uVar1 = uVar3 >> 1 & 0x7f;
  if ((uVar3 & 1) != 0) {
    uVar1 = param_1[1];
  }
  if (lVar2 - uVar1 < param_2) {
    _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE9__grow_byEmmmmmm
              (param_1,lVar2,(param_2 - lVar2) + uVar1,uVar1,uVar1,0,0);
    param_1[1] = uVar1;
    uVar4 = (uint)(byte)*param_1;
  }
  uVar3 = (long)param_1 + 4;
  if ((uVar4 & 1) != 0) {
    uVar3 = param_1[2];
  }
  puVar5 = (undefined4 *)(uVar3 + uVar1 * 4);
  uVar6 = param_2;
  if (7 < param_2) {
    uVar7 = param_2 & 0xfffffffffffffff8;
    uVar6 = param_2 & 7;
    puVar8 = (undefined8 *)(puVar5 + 4);
    uVar9 = uVar7;
    do {
      uVar9 = uVar9 - 8;
      puVar8[-1] = CONCAT44(param_3,param_3);
      puVar8[-2] = CONCAT44(param_3,param_3);
      puVar8[1] = CONCAT44(param_3,param_3);
      *puVar8 = CONCAT44(param_3,param_3);
      puVar8 = puVar8 + 4;
    } while (uVar9 != 0);
    puVar5 = puVar5 + uVar7;
    if (uVar7 == param_2) goto LAB_00bf3ea0;
  }
  do {
    uVar6 = uVar6 - 1;
    *puVar5 = param_3;
    puVar5 = puVar5 + 1;
  } while (uVar6 != 0);
LAB_00bf3ea0:
  uVar1 = uVar1 + param_2;
  if ((*param_1 & 1) == 0) {
    *(char *)param_1 = (char)((int)uVar1 << 1);
  }
  else {
    param_1[1] = uVar1;
  }
  *(undefined4 *)(uVar3 + uVar1 * 4) = 0;
  return;
}

~~~
