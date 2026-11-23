# 00bfac2c

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b7e1e4`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e1e4.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/2-3/alignment_unresolved-0018.md#compare-b4fd68a7208fb2fe034f47c2d06bc0c1)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 構造資料不足
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfac2c",
  "name": "_ZNSt6__ndk18ios_base5imbueERKNS_6localeE",
  "size": 124,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d9e5bb60ea2e2c4bc05be3b4c65291d3c76f4ff04febc80bad695972007c688c",
  "source_text_sha256": "d9e5bb60ea2e2c4bc05be3b4c65291d3c76f4ff04febc80bad695972007c688c"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5a3d0](../00c5a/00c5a3d0.md)
- [00c5dee0](../00c5d/00c5dee0.md)

## 疑似コード / UTF-8 536 bytes

~~~c

void _ZNSt6__ndk18ios_base5imbueERKNS_6localeE(undefined8 param_1,long param_2,undefined8 param_3)

{
  long lVar1;
  
  _ZNSt6__ndk16localeC1ERKS0_(param_1,param_2 + 0x30);
  _ZNSt6__ndk16localeaSERKS0_(param_2 + 0x30,param_3);
  if (*(long *)(param_2 + 0x48) != 0) {
    lVar1 = *(long *)(param_2 + 0x48) + -1;
    do {
      (**(code **)(*(long *)(param_2 + 0x38) + lVar1 * 8))
                (1,param_2,*(undefined4 *)(*(long *)(param_2 + 0x40) + lVar1 * 4));
      lVar1 = lVar1 + -1;
    } while (lVar1 != -1);
  }
  return;
}

~~~
