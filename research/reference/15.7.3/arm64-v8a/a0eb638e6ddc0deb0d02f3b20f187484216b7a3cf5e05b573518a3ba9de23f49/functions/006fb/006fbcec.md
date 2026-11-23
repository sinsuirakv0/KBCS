# 006fbcec

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `006fbcec`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006fb/006fbcec.md) · 移動量 `+0x0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/af8e2f5c5fc38f06774ff85c/0-1/machine_only_observed-0021.md#compare-3287fa68649c4bddc8e1844b4d1a4e42)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 構造資料不足
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "006fbcec",
  "name": "FUN_006fbcec",
  "size": 136,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4cb8cf68fd69e8b34eff77943f0633469018559ed8ad1dc122543b6d9bc92dce",
  "source_text_sha256": "4cb8cf68fd69e8b34eff77943f0633469018559ed8ad1dc122543b6d9bc92dce"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb010](../00bdb/00bdb010.md)

## 疑似コード / UTF-8 1182 bytes

~~~c

void FUN_006fbcec(long param_1)

{
  void *pvVar1;
  void *pvVar2;
  void *pvVar3;
  
                    /* try { // try from 006fbcf4 to 007fbd03 has its CatchHandler @ 006fbf70 */
  pvVar2 = *(void **)(param_1 + 0x38);
  if (pvVar2 == (void *)0x0) {
    return;
  }
                    /* try { // try from 006fbd04 to 007fbd13 has its CatchHandler @ 006fbf6c */
  pvVar3 = *(void **)(param_1 + 0x40);
  pvVar1 = pvVar2;
  if (pvVar3 != pvVar2) {
    do {
      pvVar1 = *(void **)((long)pvVar3 + -0x18);
      if (pvVar1 != (void *)0x0) {
        *(void **)((long)pvVar3 + -0x10) = pvVar1;
        _ZdlPv(pvVar1);
      }
      pvVar1 = *(void **)((long)pvVar3 + -0x30);
      if (pvVar1 != (void *)0x0) {
        *(void **)((long)pvVar3 + -0x28) = pvVar1;
                    /* try { // try from 006fbd44 to 007fbd57 has its CatchHandler @ 006fbfbc */
        _ZdlPv(pvVar1);
      }
      pvVar3 = (void *)((long)pvVar3 + -0x88);
    } while (pvVar3 != pvVar2);
    pvVar1 = *(void **)(param_1 + 0x38);
  }
  *(void **)(param_1 + 0x40) = pvVar2;
                    /* try { // try from 006fbd5c to 007fbdb3 has its CatchHandler @ 006fbff4 */
  _ZdlPv(pvVar1);
  return;
}

~~~
