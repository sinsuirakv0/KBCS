# 00bdaec8

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bdae10`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdae10.md) · 移動量 `+0xb8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/af8e2f5c5fc38f06774ff85c/0-1/priority-0080.md#compare-2effd8f32a4890254855832e6ece5383)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 構造資料不足
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdaec8",
  "name": "_ZnwmSt11align_val_t",
  "size": 144,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f264c902acdd2565ceb5fc7994a0782381d572ab27fdf26feeb62121fb13c26f",
  "source_text_sha256": "f264c902acdd2565ceb5fc7994a0782381d572ab27fdf26feeb62121fb13c26f"
}
~~~

## 呼び出し元

- [00be1eb0](../00be1/00be1eb0.md)

## 呼び出し先

- [00bdb050](../00bdb/00bdb050.md)
- [00bdb070](../00bdb/00bdb070.md)
- [00bdbba0](../00bdb/00bdbba0.md)
- [00be1dd0](../00be1/00be1dd0.md)
- [00be1ec0](../00be1/00be1ec0.md)

## 疑似コード / UTF-8 1131 bytes

~~~c

void _ZnwmSt11align_val_t(size_t param_1,size_t param_2)

{
  code *pcVar1;
  undefined8 uVar2;
  void *local_28;
  
  if (param_1 < 2) {
    param_1 = 1;
  }
  if (param_2 < 9) {
    param_2 = 8;
  }
  while( true ) {
                    /* try { // try from 00bdaef4 to 00cdaf53 has its CatchHandler @ 00bdae94 */
    local_28 = (void *)0x0;
    posix_memalign(&local_28,param_2,param_1);
    if (local_28 != (void *)0x0) {
                    /* catch() { ... } // from try @ 00bdaebc with catch @ 00bdaf24 */
      return;
    }
    pcVar1 = (code *)_ZSt15get_new_handlerv();
    if (pcVar1 == (code *)0x0) break;
    (*pcVar1)();
  }
  uVar2 = __cxa_allocate_exception(8);
  _ZNSt9bad_allocC2Ev();
                    /* WARNING: Subroutine does not return */
                    /* try { // try from 00bdaf54 to 00cdaf7b has its CatchHandler @ 00bdaf54
                       catch() { ... } // from try @ 00bdaf54 with catch @ 00bdaf54
                       catch() { ... } // from try @ 00bdafb4 with catch @ 00bdaf54 */
  __cxa_throw(uVar2,PTR__ZTISt9bad_alloc_00c1afa8,PTR__ZNSt20bad_array_new_lengthD1Ev_00c1afb0);
}

~~~
