# 008acfdc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `008acf98`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ac/008acf98.md) · 移動量 `+0x44`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/priority-0048.md#compare-1fb064650b5a753232396695ff06a3d4)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/priority-0052.md#compare-d6ee3712bfd82f760e15eebf5ed54d34)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "008acfdc",
  "name": "FUN_008acfdc",
  "size": 72,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "633fbb7c19a3cdee9af151a82bfa9d5b3b15d24994ef657ec322e07e0f748516",
  "source_text_sha256": "633fbb7c19a3cdee9af151a82bfa9d5b3b15d24994ef657ec322e07e0f748516"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0047acf4](../0047a/0047acf4.md)
- [0047cdd4](../0047c/0047cdd4.md)
- [008b9178](../008b9/008b9178.md)

## 疑似コード / UTF-8 745 bytes

~~~c

void FUN_008acfdc(undefined8 param_1,undefined8 *param_2,int *param_3,int *param_4)

{
  undefined8 uVar1;
  undefined8 uVar2;
  
                    /* catch() { ... } // from try @ 008ace20 with catch @ 008acfe8 */
  if ((*param_3 == 2) && (*param_4 == 0)) {
                    /* catch() { ... } // from try @ 008acdf0 with catch @ 008acff8 */
    uVar2 = *param_2;
    uVar1 = FUN_0047acf4();
                    /* catch() { ... } // from try @ 008acdcc with catch @ 008ad00c */
    FUN_0047cdd4(uVar1,0xb,0);
                    /* catch() { ... } // from try @ 008acd60 with catch @ 008ad01c */
    FUN_008b9178(uVar2);
    return;
  }
                    /* catch() { ... } // from try @ 008acd50 with catch @ 008ad020 */
  return;
}

~~~
