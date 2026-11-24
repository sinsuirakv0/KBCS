# 00befbe4

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00befb48`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bef/00befb48.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/inspection-0040.md#compare-fc5f5b7da94b026f94334df4c324ffc8)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/inspection-0037.md#compare-2e8e47427953bcdcc9daa19b90610ad5)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00befbe4",
  "name": "_ZSt17current_exceptionv",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f8728db7cc57237c9b622542ef4abd517fbc75dabce2a85fce939f597b014453",
  "source_text_sha256": "f8728db7cc57237c9b622542ef4abd517fbc75dabce2a85fce939f597b014453"
}
~~~

## 呼び出し元

- [00c58630](../00c58/00c58630.md)

## 呼び出し先

- [00c5e010](../00c5e/00c5e010.md)

## 疑似コード / UTF-8 156 bytes

~~~c

void _ZSt17current_exceptionv(undefined8 *param_1)

{
  undefined8 uVar1;
  
  uVar1 = __cxa_current_primary_exception();
  *param_1 = uVar1;
  return;
}

~~~
