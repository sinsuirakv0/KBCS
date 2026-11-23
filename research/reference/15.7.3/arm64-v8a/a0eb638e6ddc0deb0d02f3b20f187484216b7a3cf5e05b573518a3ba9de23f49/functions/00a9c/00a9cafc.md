# 00a9cafc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00a9cafc`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a9c/00a9cafc.md) · 移動量 `+0x0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/af8e2f5c5fc38f06774ff85c/0-1/no_difference_in_scope-0024.md#compare-c2d0ca9b4401cfb9f13b2b7da36cfc14)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 構造資料不足
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00a9cafc",
  "name": "FUN_00a9cafc",
  "size": 92,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "24bcbf503c3e49725a49590c826b5fdd234f6947904c443a72f451529c136da9",
  "source_text_sha256": "24bcbf503c3e49725a49590c826b5fdd234f6947904c443a72f451529c136da9"
}
~~~

## 呼び出し元

- [006dde48](../006dd/006dde48.md)
- [006ddfb8](../006dd/006ddfb8.md)
- [006e3f80](../006e3/006e3f80.md)

## 呼び出し先

- [0081f580](../0081f/0081f580.md)

## 疑似コード / UTF-8 475 bytes

~~~c

undefined4 FUN_00a9cafc(int param_1,int param_2,int param_3)

{
  long lVar1;
  
                    /* try { // try from 00a9cb0c to 00b9cb0f has its CatchHandler @ 00a9d544 */
                    /* try { // try from 00a9cb10 to 00b9cb5b has its CatchHandler @ 00a9a654 */
  lVar1 = FUN_0081f580();
  return *(undefined4 *)
          (lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec +
           (long)*(int *)(&DAT_002f4804 + (long)param_3 * 4) * 4 + 0x84080);
}

~~~
