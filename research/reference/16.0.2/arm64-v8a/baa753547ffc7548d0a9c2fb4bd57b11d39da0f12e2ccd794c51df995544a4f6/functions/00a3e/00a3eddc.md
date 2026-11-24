# 00a3eddc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00a3ed88`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3e/00a3ed88.md) · 移動量 `+0x54`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/priority-0061.md#compare-100f728ce77fd40c2b303539e53d7dcd)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/priority-0072.md#compare-8d4233a5561a872d78c6ca006dd49afd)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00a3eddc",
  "name": "FUN_00a3eddc",
  "size": 56,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "177b9095678c4e1f1d887c33d46ad3bc013c7c2bff626579125703f5614ec235",
  "source_text_sha256": "177b9095678c4e1f1d887c33d46ad3bc013c7c2bff626579125703f5614ec235"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [005c17dc](../005c1/005c17dc.md)

## 疑似コード / UTF-8 168 bytes

~~~c

void FUN_00a3eddc(undefined8 *param_1)

{
  *param_1 = &PTR_FUN_00c8b578;
  FUN_005c17dc(param_1 + 5,param_1[6]);
  FUN_005c17dc(param_1 + 2,param_1[3]);
  return;
}

~~~
