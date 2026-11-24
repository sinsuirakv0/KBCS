# 00befcac

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00befc10`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bef/00befc10.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/inspection-0040.md#compare-3320b15c656edb1728bb7306dab10a74)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/inspection-0037.md#compare-a7e2e334ef28575430a17719dd92a284)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00befcac",
  "name": "_ZSt17rethrow_exceptionSt13exception_ptr",
  "size": 24,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d153d160b8592e84431cf7fcd932e340fb1c58be0e2bca67c165e5d3c4cbc5fd",
  "source_text_sha256": "d153d160b8592e84431cf7fcd932e340fb1c58be0e2bca67c165e5d3c4cbc5fd"
}
~~~

## 呼び出し元

- [00c58590](../00c58/00c58590.md)

## 呼び出し先

- [00c580f0](../00c58/00c580f0.md)
- [00c5e030](../00c5e/00c5e030.md)

## 疑似コード / UTF-8 202 bytes

~~~c

void _ZSt17rethrow_exceptionSt13exception_ptr(undefined8 *param_1)

{
  __cxa_rethrow_primary_exception(*param_1);
                    /* WARNING: Subroutine does not return */
  _ZSt9terminatev();
}

~~~
