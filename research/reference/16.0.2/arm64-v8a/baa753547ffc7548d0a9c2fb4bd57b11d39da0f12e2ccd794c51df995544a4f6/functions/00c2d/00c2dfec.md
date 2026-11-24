# 00c2dfec

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00c2df50`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2d/00c2df50.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/priority-0089.md#compare-ef438733699d93787ca472b1cc735008)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/priority-0101.md#compare-82c94ee279635166865e27d93e0d4377)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00c2dfec",
  "name": "_ZNKSt6__ndk120__time_get_c_storageIcE7__am_pmEv",
  "size": 108,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c21a09d4858c0cbd292899d7f55464b62b4b8a94f4835e269996166a18c646f3",
  "source_text_sha256": "c21a09d4858c0cbd292899d7f55464b62b4b8a94f4835e269996166a18c646f3"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c2e058](../00c2e/00c2e058.md)
- [00c57f20](../00c57/00c57f20.md)
- [00c57f40](../00c57/00c57f40.md)

## 疑似コード / UTF-8 404 bytes

~~~c

undefined1 * _ZNKSt6__ndk120__time_get_c_storageIcE7__am_pmEv(void)

{
  int iVar1;
  
  if (((DAT_01127ff0 & 1) == 0) && (iVar1 = __cxa_guard_acquire(&DAT_01127ff0), iVar1 != 0)) {
    FUN_00c2e058();
                    /* try { // try from 00c2e044 to 00d2e05f has its CatchHandler @ 00c2e514 */
    DAT_01127fe8 = &DAT_011287e8;
    __cxa_guard_release(&DAT_01127ff0);
  }
  return DAT_01127fe8;
}

~~~
