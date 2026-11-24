# 008ddcac

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `008ddc58`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008dd/008ddc58.md) · 移動量 `+0x54`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/alignment_unresolved-0003.md#compare-f90e0498e996fd8fc5dad56508e3e37b)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/priority-0062.md#compare-552cdd07da8b5b5942cca338f664481e)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "008ddcac",
  "name": "FUN_008ddcac",
  "size": 92,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "bb80e9339875cc955f5c3349ee642e34b5b55734f7d47ea33dfd6f5fb9785598",
  "source_text_sha256": "bb80e9339875cc955f5c3349ee642e34b5b55734f7d47ea33dfd6f5fb9785598"
}
~~~

## 呼び出し元

- [008ddff4](../008dd/008ddff4.md)

## 呼び出し先

- [008dc174](../008dc/008dc174.md)

## 疑似コード / UTF-8 464 bytes

~~~c

void FUN_008ddcac(long param_1)

{
  int *piVar1;
  undefined8 *puVar2;
  int *piVar3;
  
  puVar2 = (undefined8 *)(*(long *)(param_1 + 0x38) + (long)*(int *)(param_1 + 4) * 0x18);
  piVar1 = (int *)puVar2[1];
                    /* try { // try from 008ddcd8 to 009ddcdf has its CatchHandler @ 008de4a4 */
  for (piVar3 = (int *)*puVar2; piVar3 != piVar1; piVar3 = piVar3 + 1) {
    FUN_008dc174(*(long *)(param_1 + 8) + (long)*piVar3 * 0x100);
  }
  return;
}

~~~
