# 009dcecc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `009dcd30`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009dc/009dcd30.md) · 移動量 `+0x19c`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/inspection-0032.md#compare-8d9ca67eb77bfb4bea519b5f8dddb798)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/inspection-0032.md#compare-0e8954012f98d89a1c965178564d1ebe)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "009dcecc",
  "name": "FUN_009dcecc",
  "size": 204,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0d40b5c960214e56f1437329f7ec3c72cdcdad0ccca6ee6a9dbff59013f99e70",
  "source_text_sha256": "0d40b5c960214e56f1437329f7ec3c72cdcdad0ccca6ee6a9dbff59013f99e70"
}
~~~

## 呼び出し元

- [0063acb4](../0063a/0063acb4.md)
- [0063b54c](../0063b/0063b54c.md)
- [0063bc98](../0063b/0063bc98.md)
- [0064ecb8](../0064e/0064ecb8.md)
- [006c0f38](../006c0/006c0f38.md)
- [006c119c](../006c1/006c119c.md)
- [006c2018](../006c2/006c2018.md)
- [006d3e3c](../006d3/006d3e3c.md)
- [006dd264](../006dd/006dd264.md)
- [006de788](../006de/006de788.md)
- [006dea94](../006de/006dea94.md)
- [006e1ea8](../006e1/006e1ea8.md)
- [006e3320](../006e3/006e3320.md)
- [006f24d4](../006f2/006f24d4.md)
- [00769d84](../00769/00769d84.md)
- [008dc120](../008dc/008dc120.md)
- [008e66ac](../008e6/008e66ac.md)
- [008ef9f4](../008ef/008ef9f4.md)
- [008f3044](../008f3/008f3044.md)
- [0098dc08](../0098d/0098dc08.md)
- [00a75dac](../00a75/00a75dac.md)

## 呼び出し先

- [0085b2a4](../0085b/0085b2a4.md)
- [0085b2ac](../0085b/0085b2ac.md)
- [0085b2b4](../0085b/0085b2b4.md)
- [0085b2bc](../0085b/0085b2bc.md)

## 疑似コード / UTF-8 1529 bytes

~~~c

undefined8 FUN_009dcecc(undefined8 param_1,int param_2,int param_3,int param_4,int param_5)

{
  int iVar1;
  
                    /* try { // try from 009dcee8 to 00adceef has its CatchHandler @ 009dcfd4 */
  iVar1 = FUN_0085b2a4();
  if (param_2 <= iVar1) {
                    /* try { // try from 009dcf04 to 00adcf23 has its CatchHandler @ 009dcfec */
    iVar1 = FUN_0085b2a4(param_1);
    if ((iVar1 <= param_4 + param_2) && (iVar1 = FUN_0085b2ac(param_1), param_3 <= iVar1)) {
      iVar1 = FUN_0085b2ac(param_1);
                    /* try { // try from 009dcf38 to 00adcf3f has its CatchHandler @ 009dcfb0 */
                    /* try { // try from 009dcf54 to 00adcf5b has its CatchHandler @ 009dcf60 */
                    /* catch() { ... } // from try @ 009dcc3c with catch @ 009dcf5c
                       try { // try from 009dcf5c to 00add02f has its CatchHandler @ 009dc934 */
                    /* catch() { ... } // from try @ 009dcc08 with catch @ 009dcf60
                       catch() { ... } // from try @ 009dcf54 with catch @ 009dcf60 */
      if (((iVar1 <= param_5 + param_3) &&
          (((iVar1 = FUN_0085b2b4(param_1), param_2 <= iVar1 &&
            (iVar1 = FUN_0085b2b4(param_1), iVar1 <= param_4 + param_2)) &&
           (iVar1 = FUN_0085b2bc(param_1), param_3 <= iVar1)))) &&
         (iVar1 = FUN_0085b2bc(param_1), iVar1 <= param_5 + param_3)) {
        return 1;
      }
    }
  }
                    /* catch() { ... } // from try @ 009dce44 with catch @ 009dcf78 */
  return 0;
}

~~~
