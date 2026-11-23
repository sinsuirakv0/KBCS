# 00bfaf3c

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bfab14`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfab14.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/high-0010.md#compare-ca6c78eba0500e624be36afede0bd23a)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/high-0012.md#compare-dc391372d390537c1ceb297eb0003719)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfaf3c",
  "name": "_ZNSt6__ndk18ios_base7failureC1ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEERKNS_10error_codeE",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2cdb0063d584407980d4ba2f0c75c677f0cd7ed0a068256f21f7143d4c0712ad",
  "source_text_sha256": "2cdb0063d584407980d4ba2f0c75c677f0cd7ed0a068256f21f7143d4c0712ad"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5e150](../00c5e/00c5e150.md)

## 疑似コード / UTF-8 437 bytes

~~~c

void _ZNSt6__ndk18ios_base7failureC1ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEERKNS_10error_codeE
               (long *param_1,undefined8 param_2,undefined8 *param_3)

{
  _ZNSt6__ndk112system_errorC2ENS_10error_codeERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE
            (param_1,*param_3,param_3[1],param_2);
  *param_1 = (long)(PTR__ZTVNSt6__ndk18ios_base7failureE_00c9bae8 + 0x10);
  return;
}

~~~
