# 00b3befc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00b3be60`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3b/00b3be60.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/priority-0069.md#compare-601cbaf26d504ee152c52220c8ec32f7)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/machine_only_observed-0021.md#compare-00e8dec7207723919b84023f2a6467e6)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b3befc",
  "name": "FUN_00b3befc",
  "size": 8,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b48759e7ab334f5d65c3d01e383718a940f116af83912a528ce8175b5b24f852",
  "source_text_sha256": "b48759e7ab334f5d65c3d01e383718a940f116af83912a528ce8175b5b24f852"
}
~~~

## 呼び出し元

- [005fe6ac](../005fe/005fe6ac.md)
- [0071d254](../0071d/0071d254.md)
- [0071e34c](../0071e/0071e34c.md)
- [0071e3ec](../0071e/0071e3ec.md)
- [0071e824](../0071e/0071e824.md)
- [0071e88c](../0071e/0071e88c.md)
- [0075ebd8](../0075e/0075ebd8.md)
- [0084e5f4](../0084e/0084e5f4.md)
- [009472c0](../00947/009472c0.md)
- [0098dc5c](../0098d/0098dc5c.md)
- [00a06df0](../00a06/00a06df0.md)
- [00a26210](../00a26/00a26210.md)
- [00b2f7e4](../00b2f/00b2f7e4.md)
- [00b2f82c](../00b2f/00b2f82c.md)
- [00b2f8b0](../00b2f/00b2f8b0.md)
- [00b2f944](../00b2f/00b2f944.md)
- [00b2f9c8](../00b2f/00b2f9c8.md)

## 呼び出し先

- [005e81d8](../005e8/005e81d8.md)

## 疑似コード / UTF-8 212 bytes

~~~c

void FUN_00b3befc(undefined4 *param_1,undefined4 param_2)

{
  *param_1 = param_2;
                    /* try { // try from 00b3bf00 to 00c3bf03 has its CatchHandler @ 00b3cdc0 */
  FUN_005e81d8();
  return;
}

~~~
