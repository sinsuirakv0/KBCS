# 00beaedc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00beae40`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bea/00beae40.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/no_difference_in_scope-0014.md#compare-84c73ebbb4fccad8332d4ffa060fb1a6)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/no_difference_in_scope-0014.md#compare-c87963a3e21e631496440d91576976e2)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00beaedc",
  "name": "FUN_00beaedc",
  "size": 296,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c45a72cf2ffda3dadceac383fe92453732998a122c9f231fa1e67a16bf9d6912",
  "source_text_sha256": "c45a72cf2ffda3dadceac383fe92453732998a122c9f231fa1e67a16bf9d6912"
}
~~~

## 呼び出し元

- [00be3fbc](../00be3/00be3fbc.md)
- [00beac1c](../00bea/00beac1c.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 1767 bytes

~~~c

void FUN_00beaedc(short *param_1,short *param_2,short *param_3,short *param_4,short *param_5)

{
  short sVar1;
  short sVar2;
  short sVar3;
  
  sVar1 = *param_2;
  sVar2 = *param_1;
  sVar3 = *param_3;
  if (sVar1 < sVar2) {
    if (sVar3 < sVar1) {
      *param_1 = sVar3;
    }
    else {
      *param_1 = sVar1;
      *param_2 = sVar2;
      sVar3 = *param_3;
      if (sVar2 <= sVar3) goto LAB_00beaf5c;
      *param_2 = sVar3;
    }
    *param_3 = sVar2;
    sVar3 = sVar2;
  }
  else if (sVar3 < sVar1) {
    *param_2 = sVar3;
    *param_3 = sVar1;
    sVar2 = *param_1;
    sVar3 = sVar1;
    if (*param_2 < sVar2) {
      *param_1 = *param_2;
      *param_2 = sVar2;
      sVar3 = *param_3;
    }
  }
LAB_00beaf5c:
  if (*param_4 < sVar3) {
    *param_3 = *param_4;
    *param_4 = sVar3;
    sVar3 = *param_2;
    if (*param_3 < sVar3) {
      *param_2 = *param_3;
      *param_3 = sVar3;
      sVar3 = *param_1;
      if (*param_2 < sVar3) {
        *param_1 = *param_2;
        *param_2 = sVar3;
      }
    }
  }
  sVar3 = *param_4;
  if (*param_5 < sVar3) {
    *param_4 = *param_5;
    *param_5 = sVar3;
    sVar3 = *param_3;
    if (*param_4 < sVar3) {
      *param_3 = *param_4;
      *param_4 = sVar3;
      sVar3 = *param_2;
      if (*param_3 < sVar3) {
        *param_2 = *param_3;
        *param_3 = sVar3;
        sVar3 = *param_1;
                    /* try { // try from 00beaff0 to 00ceaff7 has its CatchHandler @ 00beaff8 */
        if (*param_2 < sVar3) {
                    /* catch() { ... } // from try @ 00beaff0 with catch @ 00beaff8
                       try { // try from 00beaff8 to 00ceb02f has its CatchHandler @ 00beae8c */
          *param_1 = *param_2;
          *param_2 = sVar3;
        }
      }
    }
  }
  return;
}

~~~
