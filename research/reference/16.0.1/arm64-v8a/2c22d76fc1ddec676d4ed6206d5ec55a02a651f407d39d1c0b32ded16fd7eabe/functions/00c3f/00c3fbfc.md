# 00c3fbfc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c3f7d4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f7d4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/inspection-0044.md#compare-8d3ff68ca0fb55842c9a86ff27067f1f)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/inspection-0045.md#compare-243da58965fd549b4e31bb6895d81758)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00c3fbfc",
  "name": "FUN_00c3fbfc",
  "size": 124,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "53332f93d95124f80dfa4284d962799d75d0f5cd932936d34dcac8591946d1dc",
  "source_text_sha256": "53332f93d95124f80dfa4284d962799d75d0f5cd932936d34dcac8591946d1dc"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 583 bytes

~~~c

byte FUN_00c3fbfc(long param_1)

{
  ushort uVar1;
  byte bVar2;
  long *plVar3;
  
  if ((*(byte *)(param_1 + 0x20) & 1) == 0) {
    plVar3 = *(long **)(param_1 + 0x18);
    *(undefined1 *)(param_1 + 0x20) = 1;
    uVar1 = *(ushort *)((long)plVar3 + 9) >> 10 & 3;
                    /* try { // try from 00c3fc34 to 00d3fcbb has its CatchHandler @ 00c3fda0 */
    if (uVar1 == 2) {
      bVar2 = (**(code **)(*plVar3 + 0x10))(plVar3);
    }
    else {
      bVar2 = uVar1 == 0;
    }
    *(undefined1 *)(param_1 + 0x20) = 0;
  }
  else {
    bVar2 = 0;
  }
  return bVar2 & 1;
}

~~~
