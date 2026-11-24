# 00ac8ccc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00ac8c5c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac8/00ac8c5c.md) · 移動量 `+0x70`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/no_difference_in_scope-0013.md#compare-16be5726888ae52ae2a662ff9f94fb39)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/no_difference_in_scope-0013.md#compare-c921aa6c2949bca578fabaadf4201ce1)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ac8ccc",
  "name": "FUN_00ac8ccc",
  "size": 12,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0eab0b9a3063f2a4333711102b05b03e8686ef02444deefdcafd5f793ff41839",
  "source_text_sha256": "0eab0b9a3063f2a4333711102b05b03e8686ef02444deefdcafd5f793ff41839"
}
~~~

## 呼び出し元

- [00789ca8](../00789/00789ca8.md)
- [008c5df8](../008c5/008c5df8.md)
- [00a72604](../00a72/00a72604.md)
- [00a7c3dc](../00a7c/00a7c3dc.md)
- [00a7e71c](../00a7e/00a7e71c.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 88 bytes

~~~c

void FUN_00ac8ccc(long param_1)

{
  *(undefined1 *)(param_1 + 0x3f) = 1;
  return;
}

~~~
