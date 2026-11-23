# 00bdaea4

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdae54`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdae54.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/97ee0756e9de6c746e3ce399/1-2/alignment_unresolved-0004.md#compare-62385817288227516366d687b46ba813)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 構造資料不足
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdaea4",
  "name": "_Znwm",
  "size": 108,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8df75496413a9d600368ca2ba604d3d5a8ab7c3a8f627e5764d7dbc1c74c3e7c",
  "source_text_sha256": "8df75496413a9d600368ca2ba604d3d5a8ab7c3a8f627e5764d7dbc1c74c3e7c"
}
~~~

## 呼び出し元

- [00bdb040](../00bdb/00bdb040.md)

## 呼び出し先

- [00bdb0a0](../00bdb/00bdb0a0.md)
- [00bdb0c0](../00bdb/00bdb0c0.md)
- [00bdbbf0](../00bdb/00bdbbf0.md)
- [00bdd1d0](../00bdd/00bdd1d0.md)
- [00be1e20](../00be1/00be1e20.md)

## 疑似コード / UTF-8 923 bytes

~~~c

void _Znwm(size_t param_1)

{
  void *pvVar1;
  code *pcVar2;
  undefined8 uVar3;
  
  if (param_1 < 2) {
    param_1 = 1;
  }
  while( true ) {
    pvVar1 = malloc(param_1);
    if (pvVar1 != (void *)0x0) {
                    /* try { // try from 00bdaed8 to 00cdaeff has its CatchHandler @ 00bdaed8
                       catch() { ... } // from try @ 00bdaed8 with catch @ 00bdaed8
                       catch() { ... } // from try @ 00bdaf38 with catch @ 00bdaed8 */
      return;
    }
    pcVar2 = (code *)_ZSt15get_new_handlerv();
    if (pcVar2 == (code *)0x0) break;
    (*pcVar2)();
  }
  uVar3 = __cxa_allocate_exception(8);
  _ZNSt9bad_allocC2Ev();
                    /* try { // try from 00bdaf00 to 00cdaf37 has its CatchHandler @ 00bdaf68 */
                    /* WARNING: Subroutine does not return */
  __cxa_throw(uVar3,PTR__ZTISt9bad_alloc_00c1aff8,PTR__ZNSt20bad_array_new_lengthD1Ev_00c1b000);
}

~~~
