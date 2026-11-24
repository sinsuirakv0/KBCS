# 00befb9c

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00befb00`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bef/00befb00.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/machine_only_observed-0022.md#compare-5171a360f7c214ddd0e15aa4b1b6f32a)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/machine_only_observed-0022.md#compare-02015b505945b3155ee6f1275ea7d33c)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00befb9c",
  "name": "_ZNSt13exception_ptr31__from_native_exception_pointerEPv",
  "size": 12,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ab94efff6e48e1cc8254530256a475c6b1ab93394096bc081b569cafc16596a6",
  "source_text_sha256": "ab94efff6e48e1cc8254530256a475c6b1ab93394096bc081b569cafc16596a6"
}
~~~

## 呼び出し元

- [00c58420](../00c58/00c58420.md)

## 呼び出し先

- [00c5dff0](../00c5d/00c5dff0.md)

## 疑似コード / UTF-8 197 bytes

~~~c

void _ZNSt13exception_ptr31__from_native_exception_pointerEPv
               (undefined8 *param_1,undefined8 param_2)

{
  *param_1 = param_2;
  __cxa_increment_exception_refcount();
  return;
}

~~~
