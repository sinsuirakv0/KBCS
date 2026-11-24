# 00af7dbc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00af7d20`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af7d20.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/priority-0066.md#compare-ddbedaef24d9c5c335944b08efd9a82c)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/priority-0079.md#compare-a9f68434ade9d17ea418988cc35b94b3)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00af7dbc",
  "name": "FUN_00af7dbc",
  "size": 96,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "31571def2ecc362beedbf796c7cea50489db9c560fad7041b5f134bf7d51ff89",
  "source_text_sha256": "31571def2ecc362beedbf796c7cea50489db9c560fad7041b5f134bf7d51ff89"
}
~~~

## 呼び出し元

- [00a4f424](../00a4f/00a4f424.md)

## 呼び出し先

- [00851550](../00851/00851550.md)

## 疑似コード / UTF-8 278 bytes

~~~c

void FUN_00af7dbc(int param_1,int param_2,int param_3,undefined4 param_4)

{
  long lVar1;
  
  lVar1 = FUN_00851550();
  *(undefined4 *)
   (lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + (long)(int)(&DAT_0030a3e4)[param_3] * 4
   + 0x848c8) = param_4;
  return;
}

~~~
