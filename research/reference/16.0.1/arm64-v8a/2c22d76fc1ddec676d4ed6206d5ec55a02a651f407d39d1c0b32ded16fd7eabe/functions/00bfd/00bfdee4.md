# 00bfdee4

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bfdabc`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfdabc.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/inspection-0041.md#compare-55f6fe04cd72333891f7f148aec12d98)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/inspection-0042.md#compare-8cdebc5a98e4816ee9be1490adc2238d)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfdee4",
  "name": "_ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE6ignoreEli",
  "size": 360,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7dfa5252499c1a3dbe60a27c1e381642438f41986725c598e63fe52262f04e7a",
  "source_text_sha256": "7dfa5252499c1a3dbe60a27c1e381642438f41986725c598e63fe52262f04e7a"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c582a0](../00c58/00c582a0.md)
- [00c59dd0](../00c59/00c59dd0.md)

## 疑似コード / UTF-8 1832 bytes

~~~c

long * _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE6ignoreEli
                 (long *param_1,long param_2,uint param_3)

{
  byte *pbVar1;
  uint uVar2;
  long *plVar3;
  long lVar4;
  char local_24 [4];
  
  param_1[1] = 0;
  _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE6sentryC1ERS3_b(local_24,param_1,1);
  if (local_24[0] == '\0') {
    return param_1;
  }
  if (param_2 == 0x7fffffffffffffff) {
    do {
      plVar3 = *(long **)((long)param_1 + *(long *)(*param_1 + -0x18) + 0x28);
      pbVar1 = (byte *)plVar3[3];
      if (pbVar1 == (byte *)plVar3[4]) {
        uVar2 = (**(code **)(*plVar3 + 0x50))();
        if (uVar2 == 0xffffffff) goto LAB_00bfe014;
      }
      else {
        plVar3[3] = (long)(pbVar1 + 1);
        uVar2 = (uint)*pbVar1;
      }
      if (param_1[1] != 0x7fffffffffffffff) {
        param_1[1] = param_1[1] + 1;
      }
    } while (uVar2 != param_3);
  }
  else {
    lVar4 = param_1[1];
    if (lVar4 < param_2) {
      do {
        plVar3 = *(long **)((long)param_1 + *(long *)(*param_1 + -0x18) + 0x28);
        pbVar1 = (byte *)plVar3[3];
        if (pbVar1 == (byte *)plVar3[4]) {
          uVar2 = (**(code **)(*plVar3 + 0x50))();
          if (uVar2 == 0xffffffff) goto LAB_00bfe014;
          lVar4 = param_1[1];
          if (lVar4 != 0x7fffffffffffffff) goto LAB_00bfdfb8;
          lVar4 = param_1[1];
        }
        else {
          plVar3[3] = (long)(pbVar1 + 1);
          uVar2 = (uint)*pbVar1;
LAB_00bfdfb8:
          lVar4 = lVar4 + 1;
          param_1[1] = lVar4;
        }
      } while (uVar2 != param_3 && lVar4 < param_2);
    }
  }
  uVar2 = 0;
LAB_00bfe018:
  lVar4 = (long)param_1 + *(long *)(*param_1 + -0x18);
  _ZNSt6__ndk18ios_base5clearEj(lVar4,*(uint *)(lVar4 + 0x20) | uVar2);
  return param_1;
LAB_00bfe014:
  uVar2 = 2;
  goto LAB_00bfe018;
}

~~~
