# 00bcb3cc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bcb304`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcb/00bcb304.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/af8e2f5c5fc38f06774ff85c/0-1/priority-0079.md#compare-9ff9a4ada5d036486218962e08dfbe60)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 構造資料不足
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcb3cc",
  "name": "FUN_00bcb3cc",
  "size": 120,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "750c5d00bc3b008376f5ddbf8e8ca8ec7c78f4db047f6c910629352cb98fdfcb",
  "source_text_sha256": "750c5d00bc3b008376f5ddbf8e8ca8ec7c78f4db047f6c910629352cb98fdfcb"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bbb158](../00bbb/00bbb158.md)
- [00bdb7c0](../00bdb/00bdb7c0.md)

## 関連文字列（未確認候補）

~~~text
"%s:%d: %s"
"out/llvm-project/libcxxabi/src/demangle/ItaniumDemangle.h"
~~~

## 疑似コード / UTF-8 557 bytes

~~~c

void FUN_00bcb3cc(long *param_1)

{
  long lVar1;
  long *__ptr;
  
  lVar1 = *param_1;
  if ((ulong)(*(long *)(lVar1 + 0x2a0) - *(long *)(lVar1 + 0x298) >> 3) < (ulong)param_1[1]) {
                    /* WARNING: Subroutine does not return */
    FUN_00bbb158("%s:%d: %s","out/llvm-project/libcxxabi/src/demangle/ItaniumDemangle.h",0xa4f,
                 &DAT_00296866);
  }
  __ptr = (long *)param_1[2];
  *(long *)(lVar1 + 0x2a0) = *(long *)(lVar1 + 0x298) + param_1[1] * 8;
  if (__ptr != param_1 + 5) {
    free(__ptr);
    return;
  }
  return;
}

~~~
