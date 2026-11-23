# 00afbbe8

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00afbba4`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afbba4.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/97ee0756e9de6c746e3ce399/1-2/high-0008.md#compare-be19faf2c45f0efaa56d5d84959d4da0)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 構造資料不足
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afbbe8",
  "name": "_ZN8firebase8callback26AddCallbackWithThreadCheckEPNS0_8CallbackE",
  "size": 136,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d5d1048d31b0a3b121267079c9a70ce196d8b98637eb32659875934cfb998bb6",
  "source_text_sha256": "d5d1048d31b0a3b121267079c9a70ce196d8b98637eb32659875934cfb998bb6"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb7d0](../00bdb/00bdb7d0.md)
- [00bdec30](../00bde/00bdec30.md)
- [00bdec90](../00bde/00bdec90.md)

## 疑似コード / UTF-8 995 bytes

~~~c

undefined8 _ZN8firebase8callback26AddCallbackWithThreadCheckEPNS0_8CallbackE(long *param_1)

{
  int iVar1;
  pthread_t __thread1;
  undefined8 uVar2;
  
  if (DAT_010a0d38 == '\x01') {
    __thread1 = pthread_self();
                    /* try { // try from 00afbc10 to 00bfbc17 has its CatchHandler @ 00aff45c */
    if ((__thread1 == 0) || (DAT_010a0d40 == 0)) {
      if (DAT_010a0d40 != 0 || __thread1 != 0) goto LAB_00afbc60;
    }
    else {
      iVar1 = pthread_equal(__thread1,DAT_010a0d40);
      if (iVar1 == 0) goto LAB_00afbc60;
    }
    (**(code **)(*param_1 + 0x10))(param_1);
    if (param_1 != (long *)0x0) {
                    /* try { // try from 00afbc40 to 00bfbc57 has its CatchHandler @ 00aff458 */
      (**(code **)(*param_1 + 8))(param_1);
    }
    return 0;
  }
LAB_00afbc60:
                    /* try { // try from 00afbc68 to 00bfbc7f has its CatchHandler @ 00b003c0 */
  uVar2 = _ZN8firebase8callback11AddCallbackEPNS0_8CallbackE(param_1);
  return uVar2;
}

~~~
