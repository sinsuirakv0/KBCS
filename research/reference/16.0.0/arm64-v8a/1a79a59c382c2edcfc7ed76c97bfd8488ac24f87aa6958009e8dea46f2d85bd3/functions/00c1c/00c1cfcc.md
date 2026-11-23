# 00c1cfcc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00ba0584`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba0/00ba0584.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/2-3/alignment_unresolved-0019.md#compare-3f580f89e167ad899de117dc44bf50d2)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 構造資料不足
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00c1cfcc",
  "name": "_ZNKSt6__ndk18messagesIwE6do_getEliiRKNS_12basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEEE",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0243bb9b82b2378afc8cb768053bbcc768d509aacbac7ed9358ae0a7660a3849",
  "source_text_sha256": "0243bb9b82b2378afc8cb768053bbcc768d509aacbac7ed9358ae0a7660a3849"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [006d76a4](../006d7/006d76a4.md)

## 疑似コード / UTF-8 701 bytes

~~~c

void _ZNKSt6__ndk18messagesIwE6do_getEliiRKNS_12basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEEE
               (undefined8 *param_1)

{
  byte *in_x4;
  undefined8 uVar1;
  undefined8 uVar2;
  
  if ((*in_x4 & 1) == 0) {
    uVar2 = *(undefined8 *)in_x4;
    uVar1 = *(undefined8 *)(in_x4 + 0x10);
    param_1[1] = *(undefined8 *)(in_x4 + 8);
    *param_1 = uVar2;
                    /* try { // try from 00c1cfe4 to 00d1cfef has its CatchHandler @ 00c1dc18 */
    param_1[2] = uVar1;
    return;
  }
                    /* try { // try from 00c1cff0 to 00d1d033 has its CatchHandler @ 00c1dc24 */
  FUN_006d76a4(param_1,*(undefined8 *)(in_x4 + 0x10),*(undefined8 *)(in_x4 + 8));
  return;
}

~~~
