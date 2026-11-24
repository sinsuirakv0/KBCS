# 00aa1dcc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00aa1d5c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aa1/00aa1d5c.md) · 移動量 `+0x70`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/inspection-0034.md#compare-080ff49f1dcfdc17bb87f876cc0b8410)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/inspection-0028.md#compare-96e974d5a82e56288a85147b0bdbce5b)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aa1dcc",
  "name": "FUN_00aa1dcc",
  "size": 80,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "681c19c16fce87a04e503be4ca3f3f4198600a21a4ddd489867afde8698f812f",
  "source_text_sha256": "681c19c16fce87a04e503be4ca3f3f4198600a21a4ddd489867afde8698f812f"
}
~~~

## 呼び出し元

- [00aa02d8](../00aa0/00aa02d8.md)
- [00aa1dcc](../00aa1/00aa1dcc.md)

## 呼び出し先

- [00aa1dcc](../00aa1/00aa1dcc.md)
- [00c57f80](../00c57/00c57f80.md)

## 疑似コード / UTF-8 359 bytes

~~~c

void FUN_00aa1dcc(undefined8 param_1,undefined8 *param_2)

{
  void *__ptr;
  
  if (param_2 != (undefined8 *)0x0) {
    FUN_00aa1dcc(param_1,*param_2);
    FUN_00aa1dcc(param_1,param_2[1]);
    __ptr = (void *)param_2[5];
    if (__ptr != (void *)0x0) {
      param_2[6] = __ptr;
      _ZdlPv(__ptr);
    }
    _ZdlPv(param_2);
    return;
  }
  return;
}

~~~
