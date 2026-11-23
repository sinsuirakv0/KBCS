# 00bfb6ac

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b7ec64`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7ec64.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/2-3/inspection-0020.md#compare-696f31e15d0853d335de88ec087b3f45)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 構造資料不足
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfb6ac",
  "name": "_ZNSt6__ndk18ios_base34__set_failbit_and_consider_rethrowEv",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ccb94dbdabd3f2a88123c9c9a5c0d6240a09456125c6af1715840440cd1bc37f",
  "source_text_sha256": "ccb94dbdabd3f2a88123c9c9a5c0d6240a09456125c6af1715840440cd1bc37f"
}
~~~

## 呼び出し元

- [00c5df30](../00c5d/00c5df30.md)

## 呼び出し先

- [00c58100](../00c58/00c58100.md)

## 疑似コード / UTF-8 360 bytes

~~~c

ulong _ZNSt6__ndk18ios_base34__set_failbit_and_consider_rethrowEv(ulong param_1)

{
  undefined1 uVar1;
  ulong uVar2;
  
  *(uint *)(param_1 + 0x20) = *(uint *)(param_1 + 0x20) | 4;
  if ((*(byte *)(param_1 + 0x24) >> 2 & 1) == 0) {
    return param_1;
  }
  uVar1 = __cxa_rethrow();
  uVar2 = (ulong)DAT_00ca4408;
  DAT_00ca4408 = uVar1;
  return uVar2;
}

~~~
