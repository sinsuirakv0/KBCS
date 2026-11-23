# 009dbcac

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `009a5f4c`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a5/009a5f4c.md) · 移動量 `+0x35d60`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/2-3/priority-0048.md#compare-38c08d41cd27acd1708c6646d3af4744)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 構造資料不足
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "009dbcac",
  "name": "FUN_009dbcac",
  "size": 120,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b8214ba32b92d57f6de53f8502d5ed4e079ede746ac6efcce2c2dde80b085a88",
  "source_text_sha256": "b8214ba32b92d57f6de53f8502d5ed4e079ede746ac6efcce2c2dde80b085a88"
}
~~~

## 呼び出し元

- [00707ea0](../00707/00707ea0.md)

## 呼び出し先

- [0046bd14](../0046b/0046bd14.md)
- [00470074](../00470/00470074.md)

## 疑似コード / UTF-8 546 bytes

~~~c

void FUN_009dbcac(undefined8 param_1,long param_2,undefined8 param_3,undefined4 param_4,
                 undefined4 param_5,undefined4 param_6,int param_7)

{
  long lVar1;
  long lVar2;
  
                    /* try { // try from 009dbcb0 to 00adbd83 has its CatchHandler @ 009db558 */
  lVar1 = 0x1560;
  if (param_7 != 0) {
    lVar1 = 0x1b80;
  }
  lVar2 = 0x1608;
  if (param_7 != 0) {
    lVar2 = 0x1c28;
  }
  FUN_00470074(param_2 + lVar1,param_2 + lVar2,param_6,0);
  FUN_0046bd14(param_3,param_2 + lVar1,param_4,param_5);
  return;
}

~~~
