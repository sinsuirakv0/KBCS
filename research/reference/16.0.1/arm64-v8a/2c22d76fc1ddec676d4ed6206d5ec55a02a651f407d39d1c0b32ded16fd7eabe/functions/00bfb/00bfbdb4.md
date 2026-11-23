# 00bfbdb4

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bfb98c`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb98c.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/reference_unresolved-0001.md#compare-074299586fc913bf4f5689e27439931f)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/reference_unresolved-0001.md#compare-ddb9e62889cce56ffdd231a60e5d85e3)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfbdb4",
  "name": "_ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE5sgetcEv",
  "size": 36,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0f95e795623d246432c6d584f81ecd706d7f9da055d4bfe8d453e1b2e6a0806e",
  "source_text_sha256": "0f95e795623d246432c6d584f81ecd706d7f9da055d4bfe8d453e1b2e6a0806e"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 422 bytes

~~~c

ulong _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE5sgetcEv(long *param_1)

{
  ulong uVar1;
  
  if ((byte *)param_1[3] != (byte *)param_1[4]) {
    return (ulong)*(byte *)param_1[3];
  }
                    /* WARNING: Could not recover jumptable at 0x00bfbdd4. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  uVar1 = (**(code **)(*param_1 + 0x48))();
  return uVar1;
}

~~~
