# 00bba5bc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bba4f4`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba4f4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/af8e2f5c5fc38f06774ff85c/0-1/detail_skipped-0024.md#compare-4c93806776bd17a7212ca8178e7f85b3)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 構造資料不足
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bba5bc",
  "name": "_ZNKSt6__ndk123__match_any_but_newlineIwE6__execERNS_7__stateIwEE",
  "size": 88,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ab81cbe61f80fb3a41288b0678162b3f7737237f3273286d7d8fe08bb76a2f6d",
  "source_text_sha256": "ab81cbe61f80fb3a41288b0678162b3f7737237f3273286d7d8fe08bb76a2f6d"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 1018 bytes

~~~c

void _ZNKSt6__ndk123__match_any_but_newlineIwE6__execERNS_7__stateIwEE
               (long param_1,undefined4 *param_2)

{
  int *piVar1;
  int iVar2;
  undefined8 uVar3;
  
  piVar1 = *(int **)(param_2 + 4);
                    /* catch() { ... } // from try @ 00bb7988 with catch @ 00bba5c4 */
                    /* catch() { ... } // from try @ 00bb797c with catch @ 00bba5d8 */
                    /* catch() { ... } // from try @ 00bb78e8 with catch @ 00bba5dc */
  if ((piVar1 != *(int **)(param_2 + 6)) &&
     (iVar2 = *piVar1, (1 < iVar2 - 0x2028U && iVar2 != 0xd) && iVar2 != 10)) {
    uVar3 = *(undefined8 *)(param_1 + 8);
    *param_2 = 0xfffffc1d;
    *(int **)(param_2 + 4) = piVar1 + 1;
                    /* catch() { ... } // from try @ 00bb78cc with catch @ 00bba60c */
    *(undefined8 *)(param_2 + 0x14) = uVar3;
    return;
  }
  *(undefined8 *)(param_2 + 0x14) = 0;
  *param_2 = 0xfffffc1f;
                    /* catch() { ... } // from try @ 00bb78d8 with catch @ 00bba5f4 */
  return;
}

~~~
