# 00bda7ec

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bda3c4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bda/00bda3c4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/inspection-0039.md#compare-7dee335f5822380e6d75e40b53a27043)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/inspection-0040.md#compare-9e028feb0cef754c24a90c050df454a8)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bda7ec",
  "name": "_ZN8firebase4auth17PhoneAuthProvider19ForceResendingTokenaSERKS2_",
  "size": 48,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a81525bcda9f99b25970576ecd2010e663e7053e802d3d68d6b82fbd325b3096",
  "source_text_sha256": "a81525bcda9f99b25970576ecd2010e663e7053e802d3d68d6b82fbd325b3096"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5de40](../00c5d/00c5de40.md)

## 疑似コード / UTF-8 254 bytes

~~~c

undefined8 *
_ZN8firebase4auth17PhoneAuthProvider19ForceResendingTokenaSERKS2_
          (undefined8 *param_1,undefined8 *param_2)

{
  _ZN8firebase4auth23ForceResendingTokenData6SetRefEP8_jobject(*param_1,*(undefined8 *)*param_2);
  return param_1;
}

~~~
