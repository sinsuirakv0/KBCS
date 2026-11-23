# 009abeac

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `009763c8`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00976/009763c8.md) · 移動量 `+0x35ae4`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/2-3/alignment_unresolved-0011.md#compare-714894f29ea4034721e6e2f43158aa13)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 構造資料不足
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "009abeac",
  "name": "FUN_009abeac",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1102df87fce6b4c4c1f787cae99f84d9ac237d6646562d9fd3d136775c3131a8",
  "source_text_sha256": "1102df87fce6b4c4c1f787cae99f84d9ac237d6646562d9fd3d136775c3131a8"
}
~~~

## 呼び出し元

- [009abb24](../009ab/009abb24.md)
- [009ac11c](../009ac/009ac11c.md)

## 呼び出し先

- [0043b738](../0043b/0043b738.md)

## 関連文字列（未確認候補）

~~~text
"vector"
~~~

## 疑似コード / UTF-8 216 bytes

~~~c

void FUN_009abeac(void)

{
                    /* try { // try from 009abeb0 to 00aabecb has its CatchHandler @ 009abcb4 */
                    /* WARNING: Subroutine does not return */
  FUN_0043b738("vector");
}

~~~
