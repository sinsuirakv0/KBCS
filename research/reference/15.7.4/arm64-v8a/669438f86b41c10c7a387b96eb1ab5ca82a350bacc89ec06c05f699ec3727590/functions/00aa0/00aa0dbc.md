# 00aa0dbc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aa0d78`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0d78.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/97ee0756e9de6c746e3ce399/1-2/priority-0058.md#compare-a69133dfccc56eb73a027cafc9b7fd91)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 構造資料不足
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aa0dbc",
  "name": "FUN_00aa0dbc",
  "size": 136,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d0f872eb637ea0d2b9630c24aefe505fccdd20e1ca11f889d762f6e72d7159ad",
  "source_text_sha256": "d0f872eb637ea0d2b9630c24aefe505fccdd20e1ca11f889d762f6e72d7159ad"
}
~~~

## 呼び出し元

- [009f1ea8](../009f1/009f1ea8.md)
- [009f5650](../009f5/009f5650.md)

## 呼び出し先

- [005c2710](../005c2/005c2710.md)
- [0081f580](../0081f/0081f580.md)

## 疑似コード / UTF-8 1158 bytes

~~~c

undefined4 FUN_00aa0dbc(int param_1,int param_2,int param_3)

{
  undefined4 *puVar1;
  long lVar2;
  ulong uVar3;
  
                    /* try { // try from 00aa0dbc to 00ba0dcb has its CatchHandler @ 00aa1a40 */
                    /* try { // try from 00aa0dd4 to 00ba0de7 has its CatchHandler @ 00aa1a2c */
  lVar2 = FUN_0081f580();
                    /* try { // try from 00aa0de8 to 00ba0dfb has its CatchHandler @ 00aa1a18 */
  uVar3 = FUN_005c2710(lVar2 + (long)param_1 * 0x1f0 + 0x2678);
  lVar2 = FUN_0081f580();
                    /* try { // try from 00aa0e00 to 00ba0e07 has its CatchHandler @ 00aa1b48 */
                    /* try { // try from 00aa0e10 to 00ba0e1f has its CatchHandler @ 00aa19fc */
                    /* try { // try from 00aa0e28 to 00ba0e3b has its CatchHandler @ 00aa19f8 */
  puVar1 = (undefined4 *)((long)__DT_JMPREL + lVar2 + ((long)param_2 + 2) * 0x1c4 + 0xa448);
  if ((uVar3 & 1) != 0) {
    puVar1 = (undefined4 *)(lVar2 + ((long)param_2 + 2) * 0x770 + (long)param_3 * 0x1dc + 0x9ef94);
  }
                    /* try { // try from 00aa0e3c to 00ba0e4f has its CatchHandler @ 00aa19f4 */
  return *puVar1;
}

~~~
