# 00b3bfbc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00b3bf20`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3b/00b3bf20.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/priority-0069.md#compare-588d953a29088c0c98e2449a9fe3960a)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/machine_only_observed-0021.md#compare-da907d6875993cd9c8da02e1426f5512)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b3bfbc",
  "name": "FUN_00b3bfbc",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "cf81e6170c340491d223c1b0774faca564fa7c34f01db0b4601f01472fbcbb6b",
  "source_text_sha256": "cf81e6170c340491d223c1b0774faca564fa7c34f01db0b4601f01472fbcbb6b"
}
~~~

## 呼び出し元

- [005dbfbc](../005db/005dbfbc.md)
- [006971c0](../00697/006971c0.md)
- [0071e618](../0071e/0071e618.md)
- [008e49f4](../008e4/008e49f4.md)
- [008e5238](../008e5/008e5238.md)

## 呼び出し先

- [005e81d8](../005e8/005e81d8.md)

## 疑似コード / UTF-8 284 bytes

~~~c

void FUN_00b3bfbc(byte *param_1,int param_2)

{
  *(uint *)param_1 =
       (((uint)(param_1[5] ^ param_1[2]) << 0x10 | (uint)(param_1[4] ^ param_1[3]) << 0x18 |
        (uint)(param_1[6] ^ param_1[1]) << 8) - param_2) + (uint)(param_1[7] ^ *param_1);
  FUN_005e81d8();
  return;
}

~~~
