# 00bd2aac

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bd2a68`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd2/00bd2a68.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/97ee0756e9de6c746e3ce399/1-2/inspection-0019.md#compare-80adf62eb0225b1504e4150839c982b0)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 構造資料不足
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bd2aac",
  "name": "FUN_00bd2aac",
  "size": 132,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "705bb0285fc4a5f3b8edddbef23a514b224b604afb59771c6b4c8c9d189609cb",
  "source_text_sha256": "705bb0285fc4a5f3b8edddbef23a514b224b604afb59771c6b4c8c9d189609cb"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdd250](../00bdd/00bdd250.md)
- [00bde2c0](../00bde/00bde2c0.md)

## 疑似コード / UTF-8 1404 bytes

~~~c

void FUN_00bd2aac(long param_1,undefined8 *param_2)

{
  ulong uVar1;
  void *__ptr;
  long lVar2;
  size_t __size;
  
  (**(code **)(**(long **)(param_1 + 0x10) + 0x20))();
  lVar2 = param_2[1];
  __ptr = (void *)*param_2;
  if ((ulong)param_2[2] < lVar2 + 1U) {
                    /* catch() { ... } // from try @ 00bd2090 with catch @ 00bd2ae4 */
    __size = param_2[2] * 2;
                    /* catch() { ... } // from try @ 00bd1de8 with catch @ 00bd2ae8 */
    uVar1 = lVar2 + 0x3e1;
                    /* catch() { ... } // from try @ 00bd232c with catch @ 00bd2aec */
                    /* catch() { ... } // from try @ 00bd2300 with catch @ 00bd2af0
                       catch() { ... } // from try @ 00bd2850 with catch @ 00bd2af0 */
    if (__size < uVar1 || __size - uVar1 == 0) {
      __size = uVar1;
    }
    param_2[2] = __size;
                    /* catch() { ... } // from try @ 00bd2180 with catch @ 00bd2af8 */
    __ptr = realloc(__ptr,__size);
    *param_2 = __ptr;
    if (__ptr == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
      abort();
    }
    lVar2 = param_2[1];
  }
  *(undefined1 *)((long)__ptr + lVar2) = 0x20;
                    /* catch() { ... } // from try @ 00bd2138 with catch @ 00bd2b10
                       catch() { ... } // from try @ 00bd2834 with catch @ 00bd2b10 */
  param_2[1] = param_2[1] + 1;
  return;
}

~~~
